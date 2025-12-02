"""Forneça funções utilitárias para formatar strings.

Este módulo contém funções para remover acentos e caracteres
especiais, tornando textos seguros para nomes de arquivos.
"""

from __future__ import annotations

import secrets
from traceback import format_exception_only

type AnyType = any


def random_base36() -> str:
    """Gere string aleatória em base 36 para identificadores.

    Returns:
        str: Valor aleatório em base 36 como string.

    """
    # Gera um número aleatório de 52 bits (mesma entropia de Math.random)
    random_number = secrets.randbits(52)
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ""
    while random_number:
        random_number, remainder = divmod(random_number, 36)
        result = chars[remainder] + result
    return "0." + result or "0.0"


def formata_msg(exc: Exception | None = None) -> str:
    """Formata mensagem de erro detalhada a partir de uma exceção fornecida ao bot.

    Args:
        exc (Exception | None): Exceção a ser formatada, se fornecida.

    Returns:
        str: Mensagem formatada contendo detalhes da exceção, se houver.

    """
    if exc:
        return "\n Exception: " + "\n".join(
            format_exception_only(exc),
        )

    return ""
