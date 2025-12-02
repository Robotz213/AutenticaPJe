# AutenticaPJe

Biblioteca Python para auxiliar tarefas de autenticação e assinatura no contexto do PJe (Processo Judicial Eletrônico).

**Visão geral**

- **AutenticaPJe**: utilitários para assinar digitalmente documentos, gerenciar keystores e fornecer ferramentas de integração/automação com componentes relacionados ao PJe.
- Organização do projeto:
  - `autenticapje/assinador.py` — funções para assinar documentos digitalmente.
  - `autenticapje/keystore.py` — helpers para carregar e usar certificados/keystores.
  - `autenticapje/formatadores.py` — formatações e utilitários auxiliares.
  - `autenticapje/cli/` — comandos de linha de comando (se presentes) para operações comuns.
  - `autenticapje/driver/` — drivers e helpers para automação (p.ex. interação com webdrivers).
  - `autenticapje/elements/pje.py` — componentes ou seletores específicos do PJe.

**Funcionalidades principais**

- Assinatura digital de arquivos/documentos.
- Gerenciamento e carregamento de certificados a partir de arquivos PKCS#12 / keystores.
- Utilitários de formatação para adequar dados ao PJe.
- Componentes e helpers para automação e integração via driver/elementos.

**Requisitos**

- Python 3.8+ recomendado.
- Dependências listadas em `pyproject.toml`.

**Instalação (modo desenvolvimento)**

1. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv;
.\.venv\Scripts\Activate.ps1
```

2. Instale em modo editable:

```powershell
pip install -e .
```

Ou instale dependências diretamente com:

```powershell
pip install -r requirements.txt
```

**Uso básico (exemplo)**

Exemplo mínimo de como usar a biblioteca para carregar um keystore e assinar um arquivo:

```python
from autenticapje.keystore import Keystore
from autenticapje.assinador import Assinador

# carregar certificado (exemplo)
ks = Keystore.from_p12('meu_certificado.p12', senha='senha')

# criar objeto assinador e assinar
assinador = Assinador(keystore=ks)
assinador.assinar_arquivo('documento.pdf', 'documento-assinado.pdf')
```

Substitua os nomes de classes/métodos conforme a API real presente nos módulos.

**Uso via CLI**

Se o pacote expõe comandos na pasta `autenticapje/cli`, você poderá executar algo como:

```powershell
python -m autenticapje.cli comando --opcao valor
```

Consulte os módulos em `autenticapje/cli` para ver as opções disponíveis.

**Estrutura do código**

- `autenticapje/assinador.py` — lógica de assinatura e APIs públicas para assinar arquivos.
- `autenticapje/keystore.py` — carregamento e abstração de certificados (PKCS#12, etc.).
- `autenticapje/formatadores.py` — utilitários de formatação para dados do PJe.
- `autenticapje/driver/` — automação e integração com webdrivers.
- `autenticapje/elements/pje.py` — elementos/seletores específicos do PJe.

**Desenvolvimento e testes**

- Para rodar testes (se houver), execute o runner de testes da sua escolha, p.ex.:

```powershell
pytest
```

- Recomenda-se adicionar um `requirements-dev.txt` com ferramentas de lint e testes.

**Contribuição**

- Abra issues para discutir bugs e features.
- Faça fork, crie branch com nome descritivo e envie pull requests com mudanças pequenas e bem documentadas.

**Licença**

Verifique a licença no `pyproject.toml` ou no arquivo `LICENSE` do repositório. Se não houver um arquivo de licença, considere adicionar uma antes de redistribuir.

**Contatos / Suporte**

- Para dúvidas sobre o código, abra uma issue no repositório ou contate o mantenedor do projeto.

---

Este README foi gerado automaticamente como ponto de partida. Posso ajustar exemplos, adicionar instruções específicas para as funções reais do código ou traduzir se preferir outro formato.
