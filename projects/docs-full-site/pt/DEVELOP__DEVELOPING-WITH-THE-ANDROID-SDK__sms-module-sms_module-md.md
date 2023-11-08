---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/sms.md" 
---
# Módulo SMS  { #sms_module } 

<!--DHIS2-SECTION-ID:sms_module-->

O Módulo SMS pode ser usado como um método alternativo para fazer upload de dados quando uma conexão com a Internet não estiver disponível. Requer uma configuração adicional no servidor: um gateway SMS deve ser configurado no servidor para poder receber SMS; opcionalmente, o servidor pode ter a capacidade de enviar SMS de volta aos clientes com a resposta.

Dependendo da operadora de celular, o envio de SMS pode implicar em um custo extra. Por esse motivo, o Módulo SMS se destina apenas ao **upload de dados granulares**. Não é usado para download de metadados ou download/upload de dados em massa. Além disso, os dados são compactados usando a [biblioteca de compactação de SMS] (https://github.com/dhis2/sms-compression) para que o conteúdo caiba em um número menor de mensagens. Esta biblioteca é compartilhada com o back-end.

Para fins de teste, pode usar o [DHIS2 Android SMS Gateway] (https://github.com/dhis2/dhis2-sms-android-gateway).

No SDK, o módulo SMS pode ser acessado em `D2`.

```java
d2.smsModule()
```

Este módulo está **desabilitado por padrão** e deve ser explicitamente habilitado e configurado. Inclui três componentes que dão acesso aos recursos do módulo.

- ConfigCase: é usado para definir os dados iniciais que são comuns para todas as tarefas de envio de sms como números de gateway, tempo limite, executar download
de objecto de ids de metadados.
- SmsSubmitCase. serve para converter os dados *DHIS2* que serão enviados pelo Sdk, para enviá-los por SMS e para verificar o andamento da submissão e seu resultado.
- QrCodeCase: é usado para converter dados *DHIS2* em String. Esta string é uma representação compactada dos dados *DHIS2*. Isso é útil para evitar o envio de grande conteúdo em SMS.

Um fluxo de trabalho típico para usar o Módulo SMS seria:

- Ative o módulo SMS.
- Sincronize os metadados. O Módulo SMS baixa metadados adicionais do servidor, portanto, esta etapa deve ser realizada enquanto a conexão com a Internet estiver disponível e **depois** do módulo ser habilitado.
- Envie dados usando o Módulo SMS.

Este é um exemplo de código de um fluxo de trabalho típico (ele usou métodos de bloqueio para simplificar o código):

```java
// Enable SMS Module
d2.smsModule().configCase().setModuleEnabled(true).blockingAwait();

// Sync SMS Module metadata using SMS Module
d2.smsModule().configCase().refreshMetadataIds().blockingAwait();
// or using metadata module
d2.metadataModule().blockingDownload();

// Configure, at least, the gateway number. See ConfigCase for more parameters
d2.smsModule().configCase().setGatewayNumber("gateway-number").blockingAwait();

// Send data. For example a tracker event:
SmsSubmitCase case = d2.smsModule().smsSubmitCase();
Integer numSMSs = case.convertTrackerEvent("event-uid").blockingGet();

case.send().blockingSubscribe();
```
> **Importante**
>
> O aplicativo é responsável por solicitar as permissões do usuário (READ_PHONE_STATE, SEND_SMS, READ_SMS, RECEIVE_SMS). Caso contrário, o módulo SMS falhará.

## Versão SMS { #sms_version } 

<!--DHIS2-SECTION-ID:sms_version-->

Os SMSs são enviados em formato compactado de/para o servidor. Esta tarefa é realizada pela [biblioteca de compressão de SMS] (https://github.com/dhis2/sms-compression), que é responsável por fazer a conversão entre o texto simples e o formato compactado.

O SDK inclui a versão mais recente disponível da biblioteca de compactação, mas não há garantia de que o servidor também a esteja usando. Por este motivo, é necessário verificar a versão do servidor para habilitar/desabilitar algumas funcionalidades. A versão do SMS no servidor pode ser verificada por:

```java
d2.systemInfoModule().versionManager().getSmsVersion()
```

Visão geral das versões - recursos:

Versão 1:

- Dados agregados.
- Dados do rastreador / evento, mas existem alguns bugs conhecidos. Recomendamos não habilitar a sincronização de SMS do rastreador na versão 1.

Versão 2:

- Adicione suporte para listas vazias.
- Adicione suporte para geometria em eventos (PONTO).
- Adicione propriedades ausentes em eventos (dados do evento, data de vencimento) e inscrições (data de execução, data de incidente).
- Adicione suporte para o envio de inscrição + eventos no mesmo caso de envio de SMS.

Para obter mais informações, consulte [repositório de compressão de SMS] (https://github.com/dhis2/sms-compression).

## ConfigCase { #sms_module_config_case } 

<!--DHIS2-SECTION-ID:sms_module_config_case-->

```java
d2.smsModule().configCase()
```

Use este caso para configurar o Módulo SMS antes de usá-lo. É necessário, pelo menos, para:

- Habilite o módulo.
- Defina um número de gateway.
- Baixe os IDs de metadados.

Existem outros parâmetros opcionais para controlar se o SDK deve esperar uma resposta do servidor ou não e o tempo limite de resposta. Além disso, é possível especificar o número do remetente para que as mensagens recebidas de outros remetentes sejam ignoradas.

## SmsSubmitCase { #sms_module_submit_case } 

<!--DHIS2-SECTION-ID:sms_module_submit_case-->

Use este caso para criar um novo envio e enviá-lo. Os casos de envio não são reutilizáveis e podem ser enviados apenas uma vez. Para criar um novo caso de envio, chame o método:

```java
SmsSubmitCase case = d2.smsModule().smsSubmitCase();
```

Um envio envolve as seguintes etapas:

- Especifique os dados a serem enviados. Isso significa chamar um método como `convert * ()`.
- Envie a mensagem.
- Opcionalmente, verifique o SMS de confirmação.

Por exemplo, o envio de um evento de rastreamento será como:

```java
SmsSubmitCase case = d2.smsModule().smsSubmitCase();
Integer numSMSs = case.convertTrackerEvent("event-uid").blockingGet();

case.send().blockingSubscribe();
```

Os próximos métodos podem ser usados para definir os dados *DHIS2* a serem enviados:

- `convertSimpleEvent ()`. Para definir um evento simples.
- `convertTrackerEvent ()`. Para definir um evento de rastreamento.
- `convertEnrollment ()`. Para definir uma inscrição.
- `convertDataSet ()`. Para definir um conjunto de dados.
- `convertRelationship ()`. Para estabelecer um relacionamento.
- `convertDeletion ()`. Para deletar um evento.

Os métodos acima retornam um único com o número de mensagens que o
itens ocupam. Um exemplo do uso desses métodos é mostrado no
próximo trecho.

```java
Single<Integer> convertTask = d2.smsModule().smsSubmitCase()
    .convertEnrollment("enrollment_uid")
```

Para enviar os dados convertidos anteriormente, o Sdk fornece um método `send ()`
que retorna um fluxo dos estados atuais. Também é possível obter
o id de envio chamando o método `getSubmissionId ()`.

```java
d2.smsModule().smsSubmitCase().send()
```

Também é possível aguardar o resultado do SMS ligando para o
método `checkConfirmationSms ()`. Ele retorna um objeto `Completable` onde
conclusão significa que o SMS foi recebido com sucesso. Em caso de
o resultado não pode ser encontrado, ele retorna um erro. A data aceita é
a data mínima para a qual a confirmação será verificada, esta é
usado para pular mensagens antigas que podem ter o mesmo id de envio.

```java
d2.smsModule().smsSubmitCase().checkConfirmationSms(new Date());
```

Esses métodos podem falhar e retornar um objeto `PreconditionFailed` se algum
as condições não são satisfeitas. Os erros de pré-condições são:

- `NO_NETWORK`.
- `NO_CHECK_NETWORK_PERMISSION`.
- `NO_RECEIVE_SMS_PERMISSION`.
- `NO_SEND_SMS_PERMISSION`.
- `NO_GATEWAY_NUMBER_SET`.
- `NO_USER_LOGGED_IN`.
- `NO_METADATA_DOWNLOADED`.
- `SMS_MODULE_DISABLED`.

## QrCodeCase { #sms_module_qr_code_case } 

<!--DHIS2-SECTION-ID:sms_module_qr_code_case-->

```java
d2.smsModule().qrCodeCase()
```

Use este método para obter uma representação compactada dos dados.

`QrCodeCase` pode converter o próximo tipo de objectos *DHIS2*:

- **Eventos simples**. Usando o método `generateSimpleEventCode ()` e passando um uid de evento.
- **Eventos do rastreador**. Usando o método `generateTrackerEventCode ()` e passando um uid de evento.
- **Inscrições**. Usando o método `generateEnrollmentCode ()` e passando um uid de inscrição.
- **Relacionamentos**. Usando o método `generateRelationshipCode ()` e passando um uid de relacionamento.
- **Conjuntos de dados**. Usando o método `generateDataSetCode ()` e passando um conjunto de dados uid, um uid de unidade de organização, um combo de opção de atributo e um id de período.

Também é possível obter strings compactadas que podem ser usadas para excluir eventos:

- **Exclusões**. Usando o método `generateDeletionCode ()` e passando o uid do evento.

Esses métodos retornam um `Single` com os dados compactados. O próximo trecho de código mostra um exemplo de como ele pode ser usado.

```java
Single<String> convertTask = d2.smsModule().qrCodeCase().generateEnrollmentCode(enrollmentUid);
```


