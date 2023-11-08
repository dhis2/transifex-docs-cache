---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/blob/master/docs/content/developer/database.md"
revision_date: '2022-08-31'
tags:
- Desenvolver
---

# Banco de Dados { #android_sdk_database }

## Escopo do banco de dados { #database-scope } 
O SDK mantém um par de [servidor, utilizador] numa base de dados isolada. Assim como na versão 1.6.0, o SDK suporta múltiplas contas(pares de [servidor, utilizador]) e  informação de cada conta é armazenada numa base de dados isolada. A base de dados apenas é eliminada quando elimina-se a conta.. As base de dados são criadas automaticamente quando um login é feito com sucesso.

## Encriptação { #encryption } 
A partir da versão 1.1.0, do SDK, é possível armazenar os dados em um banco de dados criptografado. A chave de criptografia é gerada aleatoriamente
pelo SDK e mantido em segurança.

O status de criptografia (se o banco de dados está criptografado ou não) pode ser configurado no nível do servidor no android-settings-app.
O status padrão é falso: se o aplicativo não estiver instalado, o banco de dados não será criptografado.

Durante o primeiro login para um determinado servidor e usuário, o status da criptografia será baixado da API e um
banco de dados do tipo fornecido será criado.

Em logins posteriores ou sincronizações de metadados, o SDK baixará novamente o status de criptografia do servidor e,
se alterado, criptografará ou descriptografará o banco de dados atual sem perda de dados.

### Desempenho de criptografia { #encryption-performance } 
- Tamanho do banco de dados: o tamanho do banco de dados é aproximadamente o mesmo, independentemente de ser criptografado ou não.
- Velocidade: leituras e gravações são em média 5 a 10% mais lentas usando um banco de dados criptografado.

