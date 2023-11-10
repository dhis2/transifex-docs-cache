---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/compatibility-strategy.md" 
---
# Estrategia de compatibilidad de la versión DHIS2{ #compatibility_strategy } 

<!--DHIS2-SECTION-ID:compatibility_strategy-->

El SDK garantiza la compatibilidad con las tres últimas versiones de DHIS 2 (véase [Compatibilidad] (#compatibility)). En caso de que el SDK siga siendo compatible con versiones anteriores de DHIS2 y no se hayan detectado problemas importantes, la compatibilidad podría extenderse a versiones anteriores.

Para evitar el inicio de sesión accidental en instancias de DHIS 2 no soportadas, el SDK bloquea las conexiones a versiones que aún no son compatibles o que han sido obsoletas.

En cuanto al modelo de datos y la compatibilidad, el enfoque principal es ampliar el modelo de datos para poder soportar todas las versiones de DHIS 2. Suele ocurrir que las nuevas versiones de DHIS 2 introducen funcionalidades adicionales y no eliminan las existentes, por lo que dar soporte a una nueva versión de DHIS 2 suele significar utilizar el último modelo de datos.

Como regla general, el SDK intenta evitar cambios significativos en su API y las nuevas funciones son opcionales para el usuario. Esta regla se sigue tanto como sea posible, pero hay casos en los que el soporte de API antiguas y nuevas para evitar que se rompan tiene un costo muy alto. En este escenario, el **SDK podría introducir cambios importantes para ser compatible con la nueva versión de DHIS 2**.

Aquí puede encontrar algunos ejemplos de cambios en el SDK y el efecto en la aplicación.

## Ejemplo: cambio menor { #example-minor-change } 

Hasta la versión 2.30, el modelo de programa tenía un atributo booleano llamado "captureCoordinates". Este atributo indica si las coordenadas (punto) deben almacenarse en ese programa. A partir de 2.30, este atributo fue reemplazado por "featureType" con 4 valores posibles: NONE, POINT, POLYGON, MULTI_POLYGON.

*Cambios en el SDK:*

A partir de las 2.30, el SDK utiliza el atributo "featureType". Si la versión del servidor es inferior a 2.30, el SDK asigna el valor de "captureCoordinates" a:

- false - NONE
- true - POINT

*Cambios en la aplicación:*

La aplicación ahora está obligada a utilizar "featureType". Los cambios en el código son bastante sencillos.

## Ejemplo: cambio mayor { #example-major-change } 

A partir de la versión 2.30, el modelo de relaciones ha sido objeto de una profunda refactorización para permitir las relaciones entre eventos, inscripciones y trackedEntityInstances. El SDK adoptó el modelo para 2.30 y expone este modelo a la aplicación. Al interactuar con la API, el SDK traduce internamente entre los dos modelos.

*Cambios en la aplicación:*

Este cambio implica que la aplicación debe adoptar un modelo diferente y los cambios no son tan sencillos.


