---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/database.md" 
---
# Base de dados

<!--DHIS2-SECTION-ID:database-->

## Escopo do banco de dados
O SDK mantém os dados de um par [servidor, usuário] em um banco de dados isolado.

No momento, apenas um par de [servidor, usuário] é compatível, portanto, faça logout e login com outro [servidor, usuário]
O par excluirá o banco de dados atual e criará um novo.

## Encriptação
A partir da versão 1.1.0, do SDK, é possível armazenar os dados em um banco de dados criptografado. A chave de criptografia é gerada aleatoriamente
pelo SDK e mantido em segurança.

O status de criptografia (se o banco de dados está criptografado ou não) pode ser configurado no nível do servidor no android-settings-app.
O status padrão é falso: se o aplicativo não estiver instalado, o banco de dados não será criptografado.

Durante o primeiro login para um determinado servidor e usuário, o status da criptografia será baixado da API e um
banco de dados do tipo fornecido será criado.

Em logins posteriores ou sincronizações de metadados, o SDK baixará novamente o status de criptografia do servidor e,
se alterado, criptografará ou descriptografará o banco de dados atual sem perda de dados.

### Desempenho de criptografia
- Tamanho do banco de dados: o tamanho do banco de dados é aproximadamente o mesmo, independentemente de ser criptografado ou não.
- Velocidade: leituras e gravações são em média 5 a 10% mais lentas usando um banco de dados criptografado.

