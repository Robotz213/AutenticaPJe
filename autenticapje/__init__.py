"""Autenticador PJe."""

from __future__ import annotations

import traceback
from contextlib import suppress
from os import environ
from typing import NoReturn
from uuid import uuid4

import jpype
import pyotp
import requests
from dotenv import load_dotenv
from jpype import JClass
from selenium.common import TimeoutException
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from tqdm import tqdm

from autenticapje.driver import BotDriver

from .assinador import Assinador
from .elements import pje as el
from .formatadores import formata_msg, random_base36
from .keystore import KeyStore

if not jpype.isJVMStarted():
    jpype.startJVM()

load_dotenv()

NO_CONTENT_STATUS = 204
ENDPOINT_DESAFIO = "https://sso.cloud.pje.jus.br/auth/realms/pje/pjeoffice-rest"

MessageError = "Erro ao executar operaçao: "
ByteArrayInputStream = JClass("java.io.ByteArrayInputStream")
CertificateFactory = JClass("java.security.cert.CertificateFactory")
ArrayList = JClass("java.util.ArrayList")


class AutenticadorPJe:
    """Implemente autenticação no PJe usando certificado.

    A classe gerencia o fluxo de login com certificado
    digital e fator duplo de autenticação.
    """

    def __init__(self, regiao: str = "1") -> None:
        """Inicialize o autenticador com o driver e região.

        Args:
            regiao (str): Identificador da região do PJe.

        """
        bot_driver = BotDriver()

        self.driver = bot_driver.driver
        self.regiao = regiao
        self.wait = bot_driver.wait

    def print_message(self, message: str, message_type: str) -> None:
        """Escreva a mensagem formatada no progresso.

        Args:
            message (str): Texto a ser exibido.
            message_type (str): Tipo: info / error / warn.

        """
        # Prefixo baseado no tipo para melhor leitura
        prefixes = {
            "error": "[ERRO]",
            "erro": "[ERRO]",
            "info": "[INFO]",
            "warning": "[AVISO]",
            "warn": "[AVISO]",
            "aviso": "[AVISO]",
        }
        prefix = prefixes.get(message_type.lower(), "[MSG]")
        tqdm.write(f"{prefix} {message}")

    def autenticar(self) -> bool:
        """Realize o login no PJe e retorne True se bem-sucedido.

        Returns:
            bool: Indica se o login foi realizado com sucesso.

        """
        sucesso_login = False
        try:
            url = el.LINK_AUTENTICACAO_SSO.format(regiao=self.regiao)
            self.driver.get(url)

            if "https://sso.cloud.pje.jus.br/" not in self.driver.current_url:
                return True

            self.wait.until(
                ec.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        el.CSS_FORM_LOGIN,
                    )
                ),
            )

            self._login_certificado()
            self._desafio_duplo_fator()
            sucesso_login = WebDriverWait(
                driver=self.driver,
                timeout=10,
                poll_frequency=0.3,
                ignored_exceptions=(UnexpectedAlertPresentException),
            ).until(ec.url_contains("pjekz"))

        except (
            TimeoutException,
            UnexpectedAlertPresentException,
            requests.RequestException,
            Exception,
        ) as e:
            exc = "\n".join(traceback.format_exception(e))
            self.print_message(
                message=f"Erro ao realizar autenticação: {exc}",
                message_type="error",
            )

        return sucesso_login

    def _login_certificado(self) -> None:
        """Envie o desafio assinado ao endpoint do PJe.

        Gera UUID e desafio, assina, e submete o formulário.
        """
        # enviar diretamente ao endpoint PJe (exemplo)
        uuid_tarefa = str(uuid4())
        desafio = random_base36()
        assinador = Assinador()
        conteudo_assinado = assinador.assinar_conteudo(desafio)

        base64_conteudo = conteudo_assinado.conteudo_assinado_base64
        cadeia_base64 = conteudo_assinado.cadeia_base64

        ssopayload = {
            "uuid": uuid_tarefa,
            "mensagem": desafio,
            "assinatura": base64_conteudo,
            "certChain": cadeia_base64,
        }

        resp = requests.post(ENDPOINT_DESAFIO, json=ssopayload, timeout=30)

        if resp.status_code != NO_CONTENT_STATUS:
            _auth_error()

        self.driver.execute_script(el.COMMAND, el.ID_INPUT_DESAFIO, desafio)
        self.driver.execute_script(el.COMMAND, el.ID_CODIGO_PJE, uuid_tarefa)
        self.driver.execute_script("document.forms[0].submit()")

    def _desafio_duplo_fator(self) -> None:
        """Preencha e envie o token OTP para confirmar login.

        Obtém a URI OTP e envia o código ao formulário.
        """
        otp_uri = self._get_otp_uri()
        otp = str(pyotp.parse_uri(uri=otp_uri).now())

        input_otp = WebDriverWait(self.driver, 60).until(
            ec.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'input[id="otp"]',
                )
            ),
        )

        input_otp.send_keys(otp)
        input_otp.send_keys(Keys.ENTER)

    def _confirmar_login(self) -> bool:
        """Aguarde confirmação final do redirecionamento.

        Returns:
            bool: True se a URL indicar sessão autenticada.

        """
        with suppress(TimeoutException):
            return WebDriverWait(
                driver=self.driver,
                timeout=10,
                poll_frequency=0.3,
                ignored_exceptions=(UnexpectedAlertPresentException),
            ).until(ec.url_contains("pjekz"))

        return False

    def get_cookies_for_requests(self) -> dict[str, str]:
        """Retorne os headers e cookies atuais do navegador."""
        return self._cookie_to_dict()

    def get_cookies_browser(self) -> list[dict]:
        return list(self.driver.get_cookies())

    def _cookie_to_dict(self) -> dict[str, str]:
        """Converta cookies do driver em dicionário.

        Returns:
            dict[str, str]: Mapa nome -> valor dos cookies.

        """
        cookies_driver = self.driver.get_cookies()
        return {str(cookie["name"]): str(cookie["value"]) for cookie in cookies_driver}

    def _get_otp_uri(self) -> str:
        """Obtenha a URI OTP armazenada no keystore.

        Procura a entrada pelo CPF do ambiente.
        """
        kp = KeyStore()
        username = environ.get("CPF")
        entries = kp.find_entries({"username": username})

        if isinstance(entries, list):
            return list(filter(lambda x: x.otp, entries))[-1].otp

        return entries.otp


def _auth_error() -> NoReturn:
    """Levante erro de autenticação terminando a execução.

    Lança ExecutionError com mensagem formatada.
    """

    class ExecutionError(Exception):
        """Exceção para erros de execução do robô."""

        def __init__(
            self,
            message: str = MessageError,
            exc: Exception | None = None,
        ) -> None:
            """Inicialize exceção de execução com formatação.

            Args:
                message (str): Mensagem de erro principal.
                exc (Exception | None): Exceção original.

            """
            # Formatação especial para mensagem padrão com exceção completa
            if message == MessageError and exc:
                self.message = message + "\n".join(
                    traceback.format_exception(exc),
                )
            else:
                self.message = message + formata_msg(exc)

            # Chama Exception.__init__ diretamente para evitar reformatação
            Exception.__init__(self, self.message)

    raise ExecutionError(message="Erro de autenticacao")
