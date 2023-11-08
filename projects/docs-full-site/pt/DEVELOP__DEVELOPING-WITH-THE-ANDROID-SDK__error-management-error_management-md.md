---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/error-management.md" 
---
# Gerenciamento de erros  { #error_management } 

<!--DHIS2-SECTION-ID:error_management-->

Os erros que acontecem no contexto do SDK estão envolvidos em um tipo de exceção: `D2Error`, com os seguintes campos:

| Atributo         | Modelo              | Opcional  | Descrição |
|-------------------|-------------------|-----------|-------------| 
| errorComponent    | D2ErrorComponent  | verdade      | Origem do erro: Banco de dados, SDK ou servidor.|
| Erro de código         | D2ErrorCode       | verdade      | Código de erro exclusivo definido pelo SDK. |
| descrição de erro  | Corda            | verdade      | Descrição do erro em inglês (detalhes técnicos, apenas para logs e depuração). |
| httpErrorCode     | Inteiro           | falso     | Se causado por solicitação HTTP, código de erro HTTP. |
| originalException | Exceção         | falso     | Exceção Java original que causa o erro, se houver. |

Qualquer operação solicitada ao SDK pode gerar um erro.

- Para operações que retornam objectos RxJava, os erros podem ser extraídos
  Da seguinte maneira:

    ```java
    d2.userModule().logIn(username, password, url)
        .subscribe(
            user -> { },
            error -> {
                if (error instanceof D2Error) {
                    D2Error d2Error = (D2Error) error;
                    Log.e("LOGIN", d2Error.errorComponent() + " " + d2Error.httpErrorCode() + " " + d2Error.errorCode());
                }
            }
        );
    ```

- Para operações de bloqueio, também é possível recuperar um `D2Error`.
  Os erros podem ser extraídos armazenando-os em cache, conforme mostrado a seguir
  fragmento de código:

    ```java
    try {
        d2.userModule().blockingLogIn(username, password, url);
    } catch (Exception e) {
        if (e.getCause() instanceof D2Error) {
            D2Error d2Error = (D2Error) e.getCause();
            Log.e("LOGIN", d2Error.errorComponent() + " " + d2Error.httpErrorCode() + " " + d2Error.errorCode());
        }
    }
    ```

`D2Errors` são persistidos no banco de dados quando ocorrem, então eles podem ser
analisado posteriormente e diagnosticar possíveis problemas. Eles podem ser acessados
através de seu próprio repositório:

```java
d2.maintenanceModule().d2Errors()
    .byD2ErrorComponent().eq(D2ErrorComponent.Server)
    .get();
```

A equipe do SDK agora está trabalhando junto com a equipe principal para fornecer uma lista completa de códigos de erro comuns, mas ainda é um trabalho em andamento.


