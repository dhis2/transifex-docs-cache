---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/sms.md" 
---
# Módulo SMS

<!--DHIS2-SECTION-ID:sms_module-->

El módulo SMS se puede utilizar como método alternativo para  subir datos cuando no hay una conexión a Internet disponible. Requiere una configuración adicional en el servidor: se debe configurar un gateway SMS en el servidor para poder recibir SMS; opcionalmente, el servidor podría tener la capacidad de enviar SMS de vuelta a los clientes con la respuesta.

Dependiendo del proveedor de telefonía móvil, el envío de SMS podría implicar un costo adicional. Por esta razón, el módulo SMS solo está diseñado para **carga de datos granulares**. No se utiliza para la descarga de metadatos ni para la descarga/carga masiva de datos. Además, los datos se comprimen utilizando la [biblioteca de compresión de SMS](https://github.com/dhis2/sms-compression) para que el contenido pueda caber en un menor número de mensajes. Esta biblioteca se comparte con el backend.

Para fines de prueba, puede utilizar el [DHIS2 Android SMS Gateway](https://github.com/dhis2/dhis2-sms-android-gateway).

En el SDK, se puede acceder al módulo SMS desde `D2`.

```java
d2.smsModule()
```

Este módulo está **deshabilitado por defecto** y debe habilitarse y configurarse explícitamente. Incluye tres componentes que dan acceso a las funciones del módulo.

- ConfigCase: se utiliza para establecer datos iniciales que son comunes para todas las tareas de envío de sms, como números de gateway , timeout (tiempo límite), ejecución de descarga
del objeto ids de metadatos.
- SmsSubmitCase:  se utiliza para convertir los datos *DHIS2* que serán enviados por el Sdk, enviarlos por SMS y verificar el progreso del envío y su resultado.
- QrCodeCase: se utiliza para convertir los datos *DHIS2* en una cadena. Esta cadena es una representación comprimida de los datos *DHIS2*. Esto es útil para evitar enviar contenido de gran tamaño en SMS.

Un flujo de trabajo típico para usar el módulo SMS sería como:

- Habilitar el módulo SMS.
- Sincronizar metadatos. El módulo SMS descarga metadatos adicionales desde el servidor, por lo que este paso debe realizarse mientras la conexión a Internet esté disponible y **después** de que el módulo esté habilitado.
- Envío de datos usando el módulo SMS.

Este es un ejemplo de código de un flujo de trabajo típico (usó métodos de bloqueo para simplificar el código):

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
> La aplicación es responsable de solicitar al usuario los permisos (READ_PHONE_STATE, SEND_SMS, READ_SMS, RECEIVE_SMS). De lo contrario, el módulo SMS fallará.

## Versión SMS

<!--DHIS2-SECTION-ID:sms_version-->

Los SMS se envían en formato comprimido desde/hacia el servidor. Esta tarea es realizada por la [biblioteca de compresión de SMS] (https://github.com/dhis2/sms-compression), que se encarga de hacer la conversión entre el texto plano y el formato comprimido.

El SDK incluye la última versión disponible de la biblioteca de compresión, pero no hay garantía de que el servidor también la esté utilizando. Por esta razón, es necesario verificar la versión del servidor para habilitar/deshabilitar algunas funcionalidades. La versión de SMS en el servidor se puede verificar mediante:

```java
d2.systemInfoModule().versionManager().getSmsVersion()
```

Resumen de versiones - características:

Versión 1:

- Datos agregados
- Datos tracker / evento, pero hay algunos errores conocidos. Recomendamos no habilitar la sincronización SMS del tracker en la versión 1.

Versión 2:

- Agregue soporte para listas vacías.
- Agregue soporte para geometría en eventos (POINT).
- Agregue propiedades faltantes en eventos (datos del evento, fecha de vencimiento) e inscripciones (fecha de ejecución, fecha del incidente).
- Agregue soporte para enviar inscripción + eventos en el mismo caso de envío de SMS.

Para más información, consulte el [repositorio de compresión de SMS] (https://github.com/dhis2/sms-compression).

## ConfigCase

<!--DHIS2-SECTION-ID:sms_module_config_case-->

```java
d2.smsModule().configCase()
```

Utilice este caso para configurar el módulo SMS antes de utilizarlo. Se requiere, al menos, para:

- Habilitar el módulo.
- Establecer un número de gateway
- Descargar los ids de metadatos.

Hay otros parámetros opcionales para controlar si el SDK debe esperar una respuesta del servidor o no y el tiempo límite de respuesta. Además, es posible especificar el número del remitente para que los mensajes recibidos de otros remitentes sean ignorados.

## SmsSubmitCase

<!--DHIS2-SECTION-ID:sms_module_submit_case-->

Utilizar este caso para crear un nuevo envío y enviarlo. Los casos de envío no son reutilizables y solo se pueden enviar una vez. Para crear un nuevo caso de envío, llame al método:

```java
SmsSubmitCase case = d2.smsModule().smsSubmitCase();
```

Un envío implica los siguientes pasos:

- Especificar los datos a enviar. Esto significa llamar a un método como `convert*()`.
- Enviar el mensaje.
- Opcionalmente, verifique el SMS de confirmación.

Por ejemplo, enviar un evento tracker será como:

```java
SmsSubmitCase case = d2.smsModule().smsSubmitCase();
Integer numSMSs = case.convertTrackerEvent("event-uid").blockingGet();

case.send().blockingSubscribe();
```

Los siguientes métodos se pueden utilizar para establecer los datos *DHIS2* a enviar:

- `convertSimpleEvent()`. Para establecer un evento simple.
- `convertTrackerEvent()`. Para establecer un evento tracker.
- `convertEnrollment()`. Para establecer una inscripción.
- `convertDataSet()`. Para definir un set de datos.
- `convertRelationship()`. Para establecer una relación.
- `convertDeletion()`.  Para eliminar un evento.

Los métodos anteriores devuelven uno solo con el número de mensajes que
ocupan los elementos. Un ejemplo del uso de estos métodos se muestra en el
siguiente fragmento.

```java
Single<Integer> convertTask = d2.smsModule().smsSubmitCase()
    .convertEnrollment("enrollment_uid")
```

Para enviar los datos convertidos anteriormente, el Sdk proporciona un método `send()`
que devuelve un flujo de los estados actuales. También es posible obtener
la id del envío llamando al método `getSubmissionId ()`.

```java
d2.smsModule().smsSubmitCase().send()
```

También es posible esperar el resultado del SMS llamando al método `checkConfirmationSms()`. Devuelve un objeto `Completable` donde
la finalización significa que el SMS se recibió con éxito. En caso de que
no se pueda encontrar el resultado, devuelve un error. La fecha aceptada es
la fecha mínima para la cual se va a verificar la confirmación, esto se
usa para omitir mensajes antiguos que pueden tener el mismo ID de envío.

```java
d2.smsModule().smsSubmitCase().checkConfirmationSms(new Date());
```

Estos métodos pueden fallar y devolver un objeto `PreconditionFailed` si no se cumplen algunas
condiciones. Los errores de precondiciones son:

- `NO_NETWORK`.
- `NO_CHECK_NETWORK_PERMISSION`.
- `NO_RECEIVE_SMS_PERMISSION`.
- `NO_SEND_SMS_PERMISSION`.
- `NO_GATEWAY_NUMBER_SET`.
- `NO_USER_LOGGED_IN`.
- `NO_METADATA_DOWNLOADED`.
- `SMS_MODULE_DISABLED`.

## QrCodeCase

<!--DHIS2-SECTION-ID:sms_module_qr_code_case-->

```java
d2.smsModule().qrCodeCase()
```

Utilizar este método para obtener una representación comprimida de los datos.

`QrCodeCase` puede convertir el siguiente tipo de objetos *DHIS2*:

- **Eventos simples**. Usando el método `generateSimpleEventCode ()` y pasando un uid de evento.
- **Eventos tracker**. Usando el método `generateTrackerEventCode()` y pasando un uid de evento.
- **Inscripciones**. Usando el método `generateEnrollmentCode()` y pasando un uid de inscripción.
- **Relaciones**. Usando el método `generateRelationshipCode()` y pasando un uid de relación.
- **Set de datos**. Usando el método `generateDataSetCode()` y pasando un uid de set de datos, un uid de unidad organizativa, una combinación de opciones de atributos y un id de período.

También es posible obtener cadenas comprimidas que se pueden usar para eliminar eventos:

- **Eliminaciones**. Usando el método `generateDeletionCode()` y pasando el uid del evento.

Estos métodos devuelven un `Single` con los datos comprimidos. El siguiente fragmento de código muestra un ejemplo de cómo se puede utilizar.

```java
Single<String> convertTask = d2.smsModule().qrCodeCase().generateEnrollmentCode(enrollmentUid);
```


