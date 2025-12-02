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

- Python 3.14+ obrigatório.
- Dependências listadas em `pyproject.toml`.

**Estrutura do código**

- `autenticapje/assinador.py` — lógica de assinatura e APIs públicas para assinar arquivos.
- `autenticapje/keystore.py` — carregamento e abstração de certificados (PKCS#12, etc.).
- `autenticapje/formatadores.py` — utilitários de formatação para dados do PJe.
- `autenticapje/driver/` — automação e integração com webdrivers.
- `autenticapje/elements/pje.py` — elementos/seletores específicos do PJe.

**Contatos / Suporte**

- Para dúvidas sobre o código, abra uma issue no repositório ou contate o [mantenedor](mailto:nicholas@robotz.dev) do projeto.
