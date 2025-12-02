from typer import Option, Typer
from typing_extensions import Annotated

from autenticapje import AutenticadorPJe

app = Typer()


@app.command()
def autenticar(regiao: Annotated["str", Option("1")] = "1") -> None:
    autenticador = AutenticadorPJe(regiao)
    autenticador.autenticar()
