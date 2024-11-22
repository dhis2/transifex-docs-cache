# Información Lanzamiento de DHIS 2.36

Este documento destaca las características clave del lanzamiento inicial de DHIS2 versión 2.36. Esta versión es totalmente compatible con DHIS2 [Android Capture App](https://www.dhis2.org/android-2-4) versión 2.4.


## FUNCIONALIDADES DE ANÁLISIS

** Gráficos de dispersión: ** La aplicación para la visualización de datos ha incluido los gráficos de dispersión. Estos gráficos permiten a los usuarios representar unidades organizativas como puntos frente a dos variables para un período específico.

  - *Zoom in* haciendo clic y arrastrando el cursor sobre un área en la que le gustaría hacer zoom. Esto a menudo es necesario para ver más detalle en áreas donde hay muchas unidades organizativas agrupadas.
  - * La detección de valores atípicos * se puede realizar utilizando una puntuación z estándar, una puntuación z modificada o un rango intercuartílico a través del menú de opciones. También se puede aplicar una línea de umbral extrema vertical (eje y) y horizontal (eje x). Respaldada por la OMS, esta es una forma muy clara y poderosa de identificar valores atípicos que a menudo representan problemas de calidad de los datos. Puede identificar los valores atípicos que tienen más probabilidades de alterar las estadísticas nacionales utilizando la detección de valores atípicos en combinación con las líneas de umbral X e Y extremas.

[Captura de pantalla 1](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_plot.png) | [Captura de pantalla 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_outlier_options.png) | [Captura de pantalla 3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_outlier_analysis.png) | [Docs]()

** Pantalla completa para elementos del cuadro de mandos: ** Puede expandir cualquier elemento de cuadro de mandos (gráfico, mapa o tabla dinámica) a toda la pantalla. Esto es excelente para presentar datos en reuniones virtuales o en persona sin tener que salir del cuadro de mandos.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_fullscreen.png) | [Docs]()

** Leyendas para gráficos de barras y columnas: ** Cambie el color de las barras y columnas con leyendas predefinidas. Esto facilita resaltar valores acorde a sus necesidades con gráficos de barras y columnas.

[Captura de pantalla 1](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_legend_chart.png) | [Captura de pantalla 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_legend_options.png) | [Docs]()

** Cuadro de Mandos compatible con dispositivos móviles: ** La aplicación web de Cuadro de Mandos de DHIS 2 es ahora compatible con dispositivos móviles y está optimizada para pantallas pequeñas. Esto le permite utilizar el poder de los cuadros de mandos desde su dispositivo móvil. Ahora puede llevarse sus paneles de control, consultarlos en cualquier momento y compartir datos con quien necesite desde la comodidad de su teléfono. La aplicación ha adoptado varios de los principios de _Progressive Web Apps_ (PWA). El soporte de cuadros de mandos sin conexión será implementado en las próximas versiónes.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_mobile.png) | [Docs]()

** Mapas demográficos de Google Earth: ** Muchas instancias de DHIS2  no tienen datos de población precisos. Esta función le permite crear mapas con datos de Google Earth Engine, incluidas las últimas estimaciones de población de _World Pop_. Puede aplicar una capa de limites de área para visualizar los valores de población, la densidad por hectárea y el promedio por hectárea para las unidades organizativas. Puede aplicar un búfer alrededor de un establecimiento para ver la población que le corresponde. Hay disponibles datos de población desglosados por edad y sexo, de utilidad en áreas donde los datos del censo están incompletos o no son confiables, p. Ej. para planificar campañas en zonas remotas o estimar riesgos de transmisión de enfermedades.

[Captura de pantalla 1](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_1.png) | [Captura de pantalla 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_2.png) | [Captura de pantalla 3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_3.png) | [Docs]()

** Búsqueda universal: ** La aplicación de visualización de datos ahora admite la búsqueda de datos de de cualquier tipo, lo que hace que sea mucho más fácil encontrar los elementos deseados en indicadores, elementos de datos, conjuntos de datos, elementos de datos de programas individuales e indicadores de programas. Todo lo que necesita hacer es buscar el elemento y todas las coincidencias se mostrarán independientemente de su tipo. Sigue siendo posible limitar la búsqueda utilizando el selector de tipo.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_universal_search.png) | [Docs]()

** Configuración de filtros del cuadro de mandos: ** Los propietarios del cuadro de mandos pueden definir qué filtros poner habilitar de cada cuadro de mandos. Hay una gran cantidad de dimensiones de datos y no siempre se aplican todas a los datos de un cuadro de mandos específico. Esto dificulta la búsqueda y selección de dimensiones de datos relevantes. Al definir exactamente qué dimensiones de datos estarán disponibles para un cuadro de mandos, la experiencia de usuario se simplifica y se hace más atractiva. Vaya a _Editar_> _Configuración de filtro_ para seleccionar los filtros a mostrar.

[Captura de pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_filter_settings.png) | [Captura de pantalla 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_filter_list.png) | [Docs]()

** Tipo de visualización para elementos del cuadro de mandos: ** Los países y proyectos trabajan arduamente para diseñar cuadros de mandos que representen una historia específica, donde el tipo de visualización (mapas, gráficos o tablas) se selecciona y optimiza cuidadosamente. En versiones anteriores, un usuario podía cambiar el tipo de visualización de cada elemento a una tabla, mapa o gráfico. En algunos casos, esto puede deformar el mensaje cuidadosamente elaborado que el creador del cuadro de mandos está tratando de comunicar. La nueva configuración del sistema está disponible en la sección _Analytics_ de la aplicación de configuración para controlar si los usuarios pueden cambiar el tipo de visualización, abrir elementos en la aplicación del visualizador de datos, ver interpretaciones y ver en pantalla completa.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_system_settings.png) | [Docs]()


## FUNCIONALIDADES DE EVENTOS Y TRACKER

** Mejoras de rendimiento: ** 2.36 incluye muchas mejoras de rendimiento, hay grandes mejoras en el rendimiento de tracker, en particular en cuanto a las consultas de la base de datos. Las mejoras dan lugar a menores tiempos de respuesta, consultas a la base de datos más rápidas y menos consumo de memoria. La mayoría de estas actualizaciones se han aplicado a las versiones 2.34.4, 2.35.2 y 2.36.0. Se recomienda actualizar las implementaciones de DHIS2 a gran escala.

[Jira]()

** Funcionalidad de Tracker en la aplicación Capture: ** La aplicación de captura soporta mas funcionalidades de programas de tracker. Los usuarios ahora pueden enumerar e interactuar con TEIs como lo hacían antes con eventos, y tienen acceso a buscar y registrar / inscribir TEIs en la propia aplicación Capture. La modificaciones en los atributos y eventos en 2.36 todavía se siguen haciendo desde Tracker Capture, pero la navegación entre ambas aplicaciones se puede hacer de manera intuitiva. Esto permite al usuario de captura de datos acceder al tracker y a los datos de eventos en el mismo lugar y tener un flujo de trabajo más integrado.

[Captura de pantalla 1](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_list_tei.png) | [2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_list_tei_filter.png) | [3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_search_tei.png) | [4](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_register_tei_and_enroll.png) | [Docs]() | [Jira]()

** Nuevo endpoint para importar datos de tracker: ** Esta version incluye una nueva API para datos de tracker que convive con la API anterior. La nueva API se ha rediseñado e implementado por completo con una nueva arquitectura. La nueva implementación es más fácil de mantener y tiene un mayor potencial de mejoras de rendimiento de lo que era posible lograr partiendo del código anterior. La nueva API realizará una ejecución completa de las reglas de programas y permitirá hacer asignaciones de valores en el servidor y la validación los payloads, además de incorporar la funcionalidad existente para envío de mensajes. La nueva API reemplazará a la existente en versiones posteriores de DHIS2, pero se lanza ahora en paralelo para permitir que los desarrolladores de aplicaciones comiencen los procesos de integración.

[Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-5068)

** Nuevo endpoint para extraer datos de tracker: ** Se incluye también en esta versión una nueva API para extraer datos de tracker con el nuevo endpoint para importar datos de tracker. Esta nueva API permite descargar datos de tracker en el mismo formato que el nuevo endpoint para importar, lo que facilita la integración con este nuevo conjunto de servicios.

[Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-10093)

** Nueva funcionalidad de indicadores de programa: ** Ahora es posible crear expresiones de indicadores de programa y filtros basados en el estado del evento, usando la variable `V {event_status}`.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#program_indicator_functions_variables_operators) | [Jira](https://jira.dhis2.org/browse/DHIS2-10294)

** El nombre completo se muestra en las notas ** En tracker capture, ahora se muestra el nombre completo del usuario que ingresó una nota / comentario. Anteriormente, solo se mostraba el nombre de usuario. El nombre completo es útil en los casos en que el nombre de usuario no es informativo.

[Captura de pantalla]() | [Jira](https://jira.dhis2.org/browse/DHIS2-9574)

** Entrada de datos solo con el teclado: ** En tracker capture, ahora se pueden introducir datos sin el uso de un ratón.Se puede buscar y seleccionar opciones en conjuntos de opciones y campos booleanos usando el teclado.

[Jira](https://jira.dhis2.org/browse/DHIS2-5902)

## FUNCIONALIDADES DE LA PLATAFORMA

** Detección de valores atípicos: ** Una nueva y mejorada detección de valores atípicos está disponible en la aplicación de calidad de datos. Los valores atípicos ahora se clasifican y los más significativos se devuelven primero, lo que hace que sea mucho más fácil encontrar y corregir valores atípicos, lo mejora sustancialmente su análisis de datos. Anteriormente, los valores atípicos se devolvían sin seguir ningún orden. Los valores atípicos se clasifican por * distancia absoluta de la media *. La * puntuación z * del valor, así como la media, el desviación estándar, el mínimo y el máximo se incluyen en la respuesta.

[Captura de pantalla 1](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/outlier_selection.png) | [Captura de pantalla 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/outlier_detection.png) | [Docs de usuario]() |[API docs]()

** OpenID Connect: ** La compatibilidad con OpenID Connect (OIDC) ha mejorado enormemente. Ahora se encuentra disponible una solución genérica que funciona con la mayoría de los proveedores de OIDC. También se han añadido proveedores específicos para Azure y WSO2. Los proveedores que han sido probados y verificados para funcionar son Google, Microsoft / Azure, Okta, Keykloak y WSO2. OIDC permite el inicio de sesión único en varios sistemas mientras administra las identidades en una instancia central.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-validation.html#outlier-detection)

** Traducciones: ** Las traducciones dinámicas de metadatos se han ampliado para cubrir muchas más entidades y propiedades y permiten traducir la mayor parte de la aplicación DHIS 2 en cualquier idioma. Esto es útil para instancias DHIS2 que tienen varios idiomas.

[Docs]() | [Jira 1](https://jira.dhis2.org/browse/DHIS2-10562) | [2](https://jira.dhis2.org/browse/DHIS2-10556) | [3](https://jira.dhis2.org/browse/DHIS2-10487) | [4](https://jira.dhis2.org/browse/DHIS2-8669) | [5](https://jira.dhis2.org/browse/DHIS2-8297) | [6](https://jira.dhis2.org/browse/DHIS2-5587)

** Caducidad de cuentas de usuario: ** Las cuentas de usuario ahora se pueden configurar para que caduquen en una fecha determinada. Esto es útil para crear cuentas temporales, p. Ej. al invitar a socios con cuentas de invitado.

[Captura de pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/user_expiration.png) | [Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-8089)

** Deshabilitar usuarios inactivos: ** Hay disponible una nueva rutina del sistema para deshabilitar automáticamente a los usuarios que han estado inactivos (sin iniciar sesión) durante un número determinado de meses. Esto es útil desde una perspectiva de seguridad para evitar que las cuentas de usuarios inactivos se vean comprometidas.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/scheduler_disable_inactive_users.png) | [Docs]()

** Uso compartido de lectura de datos para vistas SQL: ** Ahora se requiere el uso compartido de lectura de datos para ver los datos que devuelve una vista SQL. Esto permite a los implementadores otorgar acceso a los usuarios para leer los datos de las vistas SQL sin dar acceso para creanr vistas nuevas o editar las existentes.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/sql_view_data_sharing.png) | [Docs]()

** Rendimiento de las comprobaciones de integridad de datos: ** El rendimiento de las comprobaciones de integridad de los datos (en la aplicación de administración de datos) se ha mejorado y su ejecución termina mucho más rápido.

[Captura de Pantalla](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/data_integrity_checks.png) | [Docs]()

** Deshabilitar la ejecución de reglas de programa: ** Una nueva propiedad de configuración está disponible en `dhis.conf` para habilitar / deshabilitar la ejecución de reglas de programa en el servidor.

[Docs]()

** Modernización de las aplicaciones: ** La mayoría de las aplicaciones principales incluidas en la versión 2.36.0 DHIS2 se han actualizado para aprovechar el último conjunto de herramientas de aplicaciones DHIS2. Esto asegura que tengan una cabecera idéntica, una cobertura de traducción mejorada y elementos de interfaz de usuario más estandarizados.

[Jira](https://jira.dhis2.org/browse/DHIS2-10026)

## FUNCIONALIDADES DE LA API

** Nodo líder de clúster: ** En una configuración de clúster, el ID del nodo líder está disponible en el nuevo endpoint `/ api / cluster / leader`. Esto es útil para que los administradores de sistemas sepan qué nodo del clúster actúa como líder y ejecuta los trabajos programados.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#cluster-info) | [Jira](https://jira.dhis2.org/browse/DHIS2-102579)

** Seguimiento de valore de datos: ** Un nuevo endpoint está disponible para marcar los valores de los datos para seguimiento.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data.html#webapi_follow_up) | [Jira](https://jira.dhis2.org/browse/DHIS2-10344)

** Zona horaria del servidor: ** La información de la zona horaria del servidor se ha agregado  al endpoint `/ api / system / info`.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#webapi_system_resource_view_system_information) | [Jira](https://jira.dhis2.org/browse/DHIS2-9970)

** Borrado de los resultados de la validación: ** Hay un nuevo endpoint disponible para borrar los resultados de la validación.

 [Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-validation.html#webapi_validation_results) | [Jira](https://jira.dhis2.org/browse/DHIS2-74399)

## INFORMACIÓN DE LANZAMIENTO


|Información del Lanzamiento|Enlace|
| --- | --- |
|Descarga de la nueva versión y base de datos de pruebas|https://www.dhis2.org/downloads|
|Documentación|[https://docs.dhis2.org](https://docs.dhis2.org/)|
|Notas sobre la actualización|[Notas sobre la actualización en GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Detalles en JIRA de cada característica|https://jira.dhis2.org/issues/?filter=XXXXX|
|Vista general en JIRA de errores corregidos|https://jira.dhis2.org/issues/?filter=XXXXX|
|Código fuente en Github|https://github.com/dhis2|
|Instancia demo|https://play.dhis2.org/2.36/|
|Docker|`docker pull dhis2/core:2.36.0`<br>_para otras imágenes docker vea [dockerhub](https://hub.docker.com/repository/docker/dhis2/core)_|
|Comunidad DHIS 2|https://community.dhis2.org/|
