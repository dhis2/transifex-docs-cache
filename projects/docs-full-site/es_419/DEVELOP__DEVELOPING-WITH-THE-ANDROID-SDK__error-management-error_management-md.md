---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/error-management.md" 
---
# Gestión de errores  { #error_management } 

<!--DHIS2-SECTION-ID:error_management-->

Los errores que se producen en el contexto del SDK se envuelven en un tipo de excepción: `D2Error`, con los siguientes campos:

| Atributo         | Tipo              | Opcional   | Descripción |
|-------------------|-------------------|-----------|-------------| 
| errorComponent    | D2ErrorComponent  | verdadero      | Origen del error: base de datos, SDK o servidor.|
| errorCode         | D2ErrorCode       | verdadero      | Código de error único definido por el SDK |
| errorDescription  | Cadena            | verdadero      | Descripción del error en inglés (detalles técnicos, solo para registros y depuración). |
| httpErrorCode     | Entero           | falso     | Si es causado por una solicitud HTTP, código de error HTTP. |
| originalException | Excepción         | falso     | Excepción Java original que causa el error, si lo hubiera. |

Cualquier operación solicitada al SDK puede generar un error.

- Para las operaciones que devuelven objetos RxJava, los errores se pueden extraer
  de la siguiente manera:

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

- Para las operaciones de bloqueo, también es posible recuperar un `D2Error`.
  Los errores se pueden extraer almacenándolos en caché, como se muestra a continuación
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

`D2Errors` se conservan en la base de datos cuando ocurren, por lo que pueden ser
analizados posteriormente y diagnosticar posibles problemas. Se puede acceder a ellos
a través de su propio repositorio:

```java
d2.maintenanceModule().d2Errors()
    .byD2ErrorComponent().eq(D2ErrorComponent.Server)
    .get();
```

El equipo de SDK ahora está trabajando junto con el equipo principal para proporcionar una lista completa de códigos de error comunes, pero aún es un trabajo en progreso.


