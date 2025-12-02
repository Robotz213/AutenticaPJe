# AutenticaPJe

Biblioteca Python para auxiliar tarefas de autenticação e assinatura no contexto do PJe (Processo Judicial Eletrônico).

**Configuração**

**Instalação**

> ```sh
> pip install "git+https://github.com/Robotz213/AutenticaPJe.git"
> ```

**Uso**

> ```sh
> autenticapje --regiao 1 # Região para autenticar (ex.: TRT1 = 1)
> ```

**Requisitos**

- [`Keepass`](https://keepassxc.org/) (Banco de dados configurado com OTP);
- [`Python 3.14`](https://www.python.org/ftp/python/3.14.1/python-3.14.1-amd64.exe) (**obrigatório**);
- [`Java 21+`](https://builds.openlogic.com/downloadJDK/openlogic-openjdk-jre/21.0.9+10/openlogic-openjdk-jre-21.0.9+10-windows-x64.msi) (Necessário para o [Jpype1](https://jpype.readthedocs.io/en/stable/));
- Configuração das [`variáveis de ambiente`](./TemplateEnv.md)

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

**Estrutura do código**

- `autenticapje/assinador.py` — lógica de assinatura e APIs públicas para assinar arquivos.
- `autenticapje/keystore.py` — carregamento e abstração de certificados (PKCS#12, etc.).
- `autenticapje/formatadores.py` — utilitários de formatação para dados do PJe.
- `autenticapje/driver/` — automação e integração com webdrivers.
- `autenticapje/elements/pje.py` — elementos/seletores específicos do PJe.

**Contatos / Suporte**

- Para dúvidas sobre o código, abra uma issue no repositório ou contate o [mantenedor](mailto:nicholas@robotz.dev) do projeto.
