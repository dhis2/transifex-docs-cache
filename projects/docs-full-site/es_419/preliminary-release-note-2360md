# Información Lanzamiento de DHIS 2.36

Este documento destaca las características clave del lanzamiento inicial de DHIS2 versión 2.36. Esta versión es totalmente compatible con DHIS2 [Android Capture App](https://www.dhis2.org/android-2-4) versión 2.4.


## FUNCIONALIDADES DE ANÁLISIS

** Gráficos de dispersión: ** Permite a los usuarios representar unidades organizativas como puntos frente a dos variables para un período con gráficos de dispersión.

  - *Zoom in* haciendo clic y arrastrando el cursor sobre un área en la que le gustaría hacer zoom. Esto a menudo es necesario para ver más detalle en áreas donde hay muchas unidades organizativas agrupadas.
  - * La detección de valores atípicos * se puede realizar utilizando una puntuación z estándar, una puntuación z modificada o un rango intercuartílico a través del menú de opciones. También se puede aplicar una línea de umbral extrema vertical (eje y) y horizontal (eje x). Respaldada por la OMS, esta es una forma muy clara y poderosa de identificar valores atípicos que a menudo representan problemas de calidad de los datos. Puede identificar los valores atípicos que tienen más probabilidades de alterar las estadísticas nacionales utilizando la detección de valores atípicos en combinación con las líneas de umbral X e Y extremas.

[Captura de Pantalla]() | [Docs]()

** Pantalla completa para elementos del cuadro de mandos: ** Puede expandir cualquier elemento de cuadro de mandos (gráfico, mapa o tabla dinámica) a toda la pantalla. Esto es excelente para presentar datos en reuniones virtuales o en persona sin tener que salir del cuadro de mandos.

[Captura de Pantalla]() | [Docs]()

** Leyendas para gráficos de barras y columnas: ** Cambie el color de las barras y columnas con leyendas predefinidas. Esto facilita resaltar valores acorde a sus necesidades con gráficos de barras y columnas.

[Captura de Pantalla]() | [Docs]()

** Cuadro de Mandos compatible con dispositivos móviles: ** La aplicación web de Cuadro de Mandos de DHIS 2 es ahora compatible con dispositivos móviles y está optimizada para pantallas pequeñas. Esto le permite utilizar el poder de los cuadros de mandos desde su dispositivo móvil. Ahora puede llevarse sus paneles de control, consultarlos en cualquier momento y compartir datos con quien necesite desde la comodidad de su teléfono. La aplicación ha adoptado varios de los principios de _Progressive Web Apps_ (PWA). El soporte de cuadros de mandos sin conexión será implementado en las próximas versiónes.

[Captura de Pantalla]() | [Docs]()



[Captura de Pantalla]() | [Docs]()



[Captura de Pantalla]() | [Docs]()



[Captura de Pantalla]() | [Docs]()



[Captura de Pantalla]() | [Docs]()


## FUNCIONALIDADES DE EVENTOS Y TRACKER



[Jira]()



[]() | [Jira]()



[Docs]() | [Jira]()

## FUNCIONALIDADES DE LA PLATAFORMA

** Detección de valores atípicos: ** Una nueva y mejorada detección de valores atípicos está disponible en la aplicación de calidad de datos. Los valores atípicos ahora se clasifican y los más significativos se devuelven primero, lo que hace que sea mucho más fácil encontrar y corregir valores atípicos, lo mejora sustancialmente su análisis de datos. Anteriormente, los valores atípicos se devolvían sin seguir ningún orden. Los valores atípicos se clasifican por * distancia absoluta de la media *. La * puntuación z * del valor, así como la media, el desviación estándar, el mínimo y el máximo se incluyen en la respuesta.



** OpenID Connect: ** La compatibilidad con OpenID Connect (OIDC) ha mejorado enormemente. Ahora se encuentra disponible una solución genérica que funciona con la mayoría de los proveedores de OIDC. También se han añadido proveedores específicos para Azure y WSO2. Los proveedores que han sido probados y verificados para funcionar son Google, Microsoft / Azure, Okta, Keykloak y WSO2. OIDC permite el inicio de sesión único en varios sistemas mientras administra las identidades en una instancia central.

[Docs]()



[Docs]() | [Jira 1](https://jira.dhis2.org/browse/DHIS2-10562) | [2](https://jira.dhis2.org/browse/DHIS2-10556) | [3](https://jira.dhis2.org/browse/DHIS2-10487) | [4](https://jira.dhis2.org/browse/DHIS2-8669) | [5](https://jira.dhis2.org/browse/DHIS2-8297) | [6](https://jira.dhis2.org/browse/DHIS2-5587)

** Caducidad de cuentas de usuario: ** Las cuentas de usuario ahora se pueden configurar para que caduquen en una fecha determinada. Esto es útil para crear cuentas temporales, p. Ej. al invitar a socios con cuentas de invitado.

[Jira](https://jira.dhis2.org/browse/DHIS2-8089)

** Deshabilitar usuarios inactivos: ** Hay disponible una nueva rutina del sistema para deshabilitar automáticamente a los usuarios que han estado inactivos (sin iniciar sesión) durante un número determinado de meses. Esto es útil desde una perspectiva de seguridad para evitar que las cuentas de usuarios inactivos se vean comprometidas.

[Docs]()

** Uso compartido de lectura de datos para vistas SQL: ** Ahora se requiere el uso compartido de lectura de datos para ver los datos que devuelve una vista SQL. Esto permite a los implementadores otorgar acceso a los usuarios para leer los datos de las vistas SQL sin dar acceso para creanr vistas nuevas o editar las existentes.

[Docs]()

** Rendimiento de las comprobaciones de integridad de datos: ** El rendimiento de las comprobaciones de integridad de los datos (en la aplicación de administración de datos) se ha mejorado y su ejecución termina mucho más rápido.

[Docs]()

** Deshabilitar la ejecución de reglas de programa: ** Una nueva propiedad de configuración está disponible en `dhis.conf` para habilitar / deshabilitar la ejecución de reglas de programa en el servidor.

[Docs]()

## FUNCIONALIDADES DE LA API

** Nodo líder de clúster: ** En una configuración de clúster, el ID del nodo líder está disponible en el nuevo endpoint `/ api / cluster / leader`. Esto es útil para que los administradores de sistemas sepan qué nodo del clúster actúa como líder y ejecuta los trabajos programados.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#cluster-info) | [Jira](https://jira.dhis2.org/browse/DHIS2-102579)

** Seguimiento de valore de datos: ** Un nuevo endpoint está disponible para marcar los valores de los datos para seguimiento.

[Docs](https://docs.dhis2.org/master/en/dhis2_developer_manual/web-api.html#follow-up)

** Zona horaria del servidor: ** La información de la zona horaria del servidor se ha agregado  al endpoint `/ api / system / info`.

[Docs]()

** Borrado de los resultados de la validación: ** Hay un nuevo endpoint disponible para borrar los resultados de la validación.



## INFORMACIÓN DE LANZAMIENTO


|Información del Lanzamiento|Enlace|
| --- | --- |
|Descarga de la nueva versión y base de datos de pruebas|https://www.dhis2.org/downloads|
|Documentación|[](https://docs.dhis2.org/)|
|Notas sobre la actualización|[Notas sobre la actualización en GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Detalles en JIRA de cada característica|https://jira.dhis2.org/issues/?filter=XXXXX|
|Vista general en JIRA de errores corregidos|https://jira.dhis2.org/issues/?filter=XXXXX|
|Código fuente en Github|https://github.com/dhis2|
|Instancia demo|https://play.dhis2.org/2.36/|
|Docker|`docker pull dhis2/core:2.36.0`<br>_for more docker image variants see [dockerhub](https://hub.docker.com/repository/docker/dhis2/core)_|
|Comunidad DHIS 2|https://community.dhis2.org/|
