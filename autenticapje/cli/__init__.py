import json
from os import environ as env
from pathlib import Path

from dotenv import load_dotenv
from tqdm import tqdm
from typer import Option, Typer
from typing_extensions import Annotated

from autenticapje import AutenticadorPJe

app = Typer()

load_dotenv()


class EnvKeys:
    CPF: str = None
    CERTIFICADO: str = None
    SENHA_CERTIFICADO: str = None
    KBDX_PATH: str = None
    KBDX_PASSWORD: str = None


@app.command()
def autenticar(regiao: Annotated[str, Option()] = "1") -> None:
    for item in dir(EnvKeys):
        if item.startswith("_"):
            continue

        if item not in env:
            raise KeyError(f'Chave "{item}" não está nas variáveis de ambiente!')

    autenticador = AutenticadorPJe(regiao)
    if autenticador.autenticar():
        tqdm.write("Autenticado com sucesso!")

        cookie_requestslib = autenticador.get_cookies_for_requests()
        arquivo1 = Path.home().joinpath("cookies_requests.json")
        arquivo1.write_text(json.dumps(cookie_requestslib))

        cookie_navegador = autenticador.get_cookies_browser()
        arquivo2 = Path.home().joinpath("cookies_navegador.json")
        arquivo2.write_text(json.dumps(cookie_navegador))

        tqdm.write(f"""

======================================
Cookies "Py" (Requests, Httpx, etc): {arquivo1.as_uri()}


Cookies Navegador: {arquivo2.as_uri()}
======================================
                   """)
