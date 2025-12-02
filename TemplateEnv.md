### Exemplo _.env_

```sh
# Inserir como está salvo no banco de dados
# Formato correto para CPF
CPF="000.000.000-00"  # ou CPF="00.000.000/0000-00"

# Certificado A1
CERTIFICADO="/caminho/para/certificado"
SENHA_CERTIFICADO="senha_certificado"

# Configurações KeePass (Obrigatório)
KBDX_PATH="/caminho/para/database.kbdx"
KBDX_PASSWORD="senha_database"
```

**Disclaimer**

- As **váriáveis de ambiente** podem ser configuradas da seguinte forma:

  > - Diretamente no [**Sistema;**](https://www.alura.com.br/artigos/configurar-variaveis-ambiente-windows-linux-macos)
  > - Em um arquivo **`.env`**, desde de que o arquivo esteja salvo na mesma pasta de chamada do comando **`autenticapje`**
