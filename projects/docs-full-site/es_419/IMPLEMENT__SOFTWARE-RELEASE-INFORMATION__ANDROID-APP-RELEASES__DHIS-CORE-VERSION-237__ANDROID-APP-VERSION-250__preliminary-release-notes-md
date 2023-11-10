---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/2.5/android-releases/2.5/ReleaseNote-2.5.0.md"
revision_date: "2021-11-23"
---

# Notas de lanzamiento de la aplicación Android DHIS2 versión 2.5 { #dhis2-android-app-version-25-release-notes }

<!-- BEGIN-WEBSITE-SYNC-ID:android -->

<!-- Analíticas -->

## ANALÍTICAS LOCALES { #local-analytics }

**Analíticas de programas/set de datos sin conexión:** La aplicación de Android ahora puede representar análisis que se han creado en la aplicación Visualización de Datos en DHIS2. Las analíticas que se mostrarán requieren configuración mediante la aplicación web de configuración de Android (Android Settings Web App), donde los administradores podrán seleccionar los gráficos y tablas que se mostrarán a los usuarios finales. Estas visualizaciones se pueden presentar en la pantalla de inicio de la aplicación, en la pantalla del set de datos y a nivel de programas. Todos los análisis se agregan en el dispositivo utilizando datos locales. La función Analíticas es 100% funcional sin conexión.

Las analíticas soportadas en la aplicación Android son:

-   Tablas dinamicas
-   Gráfica de columna
-   Gráfica de línea
-   Gráfica de pastel
-   Gráfica radar
-   Valor único

Todas estas visualizaciones se pueden organizar y mostrar en grupos. Los grupos también se configuran utilizando la aplicación de Configuración de Android (Android Settings Web App). Para cada objeto de visualización, el usuario podrá filtrar en la aplicación por:

-   Período: diario, semanal, mensual, anual, este trimestre, último trimestre, últimos 4 trimestres y trimestre de este año.
-   Unidad organizativa: seleccione "Todas" para mostrar todas las unidades organizativas disponibles para el usuario o "Selección" para especificar una o varias unidades organizativas.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2557) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Home.png) | [Captura de pantalla 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Filtering.png) | [Captura de pantalla 3](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Groups.png) | [Captura de pantalla 4](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Android+Settings+Webapp.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#local-analytics-new-25)

## EXPERIENCIA DE USUARIO EN ENTRADA DE DATOS { #data-entry-user-experience }

**Rediseño del set de datos** El diseño para la entrada de datos del set de datos se ha rediseñado para ofrecer una experiencia de usuario más integrada y una interfaz de usuario más limpia. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4382) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Data+Sets+New+style.png)

**Exportar/compartir códigos de barras y QR:** Elementos de datos o atributos tipo texto pueden configurarse como códigos de barras o QR. Con la nueva opción de exportar/compartir, los usuarios podrán mostrar un código de barra o QR en una imagen para compartirlo e imprimirlo, tomar una captura de pantalla o mostrarlo en la pantalla para escanear. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3891) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Export+Share+QR+Code.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render_qr)

**Mejora de la representación de la entrada de datos basada en iconos:** Cuando el tipo de representación de las secciones del programa es usado en combinación con los iconos, una sección con un solo elemento de datos y un conjunto de opciones asociado muestra los iconos asignados junto a las opciones para simplificar la entrada de datos. La distribución y diseño de esta pantalla se han rediseñado y mejorado para ofrecer una mejor experiencia de usuario. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4027) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Visual+Data+Entry.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_rendering_type)

**Vista de calendario personalizada:** En la aplicación Capture para Android de DHIS2, los usuarios pueden cambiar la selección de la fecha desde la vista del spinner del calendario.  En esta versión, la aplicación recordará la última visualización seleccionada por el usuario y la usará la próxima vez que el usuario necesite seleccionar una fecha. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2402) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Calendar.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#personalized-calendar-view-new-25)

**Mostrar el motivo de los datos no editables:** Los datos se pueden bloquear por muchas razones en DHIS2, debido a restricciones de acceso o vencimiento, entre otras. Cuando un evento, TEI o conjunto de datos no se pueden editar, el usuario podrá encontrar el motivo en la sección "Detalles". Las posibles razones son:

-   Finalización del evento
-   Finalización de la inscripción
-   Evento expirado
-   Unidad organizativa cerrada
-   Unidad organizativa fuera de alcance de captura
-   Sin acceso para capturar datos en el programa o set de datos
-   Sin acceso a una opción de categoría en el programa o set de datos [Jira](https://jira.dhis2.org/browse/ANDROAPP-3565) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Non+Editable+Data.png) | [Documentación ](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#reason-for-non-editable-data-new-25)

**Ajuste de las opciones del tablero TEI a la configuración del programa:** Las opciones que se ofrecen en el tablero TEI se adaptarán a la configuración específica del programa.

-   La pestaña Relaciones no estará visible si las relaciones del programa no están configuradas.
-   El botón de creación de eventos se ocultará cuando el usuario no pueda crear más eventos según la configuración del tracker.
-   La pestaña de indicadores no estará visible si el programa no tiene indicadores de programa configurados.
-   El filtro de unidad organizativa no estará visible si el usuario solo tiene una unidad organizativa configurada. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4097) | [Jira 2](https://jira.dhis2.org/browse/ANDROAPP-3129) | [Jira 3](https://jira.dhis2.org/browse/ANDROAPP-4099) | [Documentación](https://docs.dhis2.org/en/use/android-app/features-supported.html#tei-dashboard-navigation-panel-new-25)

## MAPAS { #maps }

**Experiencia general del usuario con mapas:** Después de tres versiones desde que se incluyeron los mapas en la aplicación DHIS2 para Android, hemos revisado y mejorado la experiencia del usuario basándonos en los comentarios de la comunidad.  
[Jira](https://jira.dhis2.org/browse/ANDROAPP-4024) | [Documentación]()

**Centrar a la posición del usuario:** Si el usuario otorga permisos de ubicación a la aplicación, el mapa mostrará la ubicación actual representada como un punto de color azul. Los mapas de la aplicación Capture para Android de DHIS2 ahora incluyen la posibilidad de centrar el mapa en la ubicación del usuario. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3583) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-User+position.png)

## FUNCIONALIDADES DE TRACKER { #tracker-features }

**Agregar soporte para relaciones Eventos - TEI:** La aplicación ahora permite a los usuarios agregar relaciones de eventos únicos(Event programs) to TEIs. There is a new tab in the event dashboard, named relationships, that is active when it is configured in the server. This version does not allow relationships from TEIs to events or using events that belong to an enrollment. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2275) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Event+TEI+Relationships.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/features-supported.html#event-tei-relationships-new-25)

**NUEVO filtro para TEIs marcadas como seguimiento:** En los programas de Tracker, el filtro 'Follow Up' permite al usuario filtrar los TEI que se han marcado como 'Follow Up'. Los TEI se pueden marcar para realizar un seguimiento en el tablero TEI.  [Jira](https://jira.dhis2.org/browse/ANDROAPP-3304) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Follow+Up+Filter.png) | [Documentación](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#follow-up-new-25)

## OTRAS FUNCIONALIDADES { #other-features }

**Idioma de la interfaz basado en el idioma de usuario de DHIS2:** El idioma de la interfaz corresponderá al idioma establecido en la configuración de usuario de DHIS2. Si el idioma no está disponible en la aplicación, seleccionará el idioma del dispositivo. Si ninguna de las configuraciones de idioma está disponible, la aplicación estará predeterminada en inglés. Las traducciones establecidas en DHIS2 para los metadatos también se mostrarán según el idioma en la configuración del usuario. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2925) | [Documentación](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#interface-language-new-25)

## MANTENIMIENTO { #maintenance }

**Calidad / Seguridad / Rendimiento:** Puede encontrar una lista de cuestiones relacionadas con la calidad, la seguridad y el rendimiento al abrir este [filtro jira](https://jira.dhis2.org/issues/?filter=12204).

**Corrección de errores:** Puede encontrar una lista de los errores corregidos en esta versión abriendo este [filtro jira](https://jira.dhis2.org/issues/?filter=12203).

## INFORMACIÓN DE LANZAMIENTO { #release-info }

| Información del Lanzamiento | Enlace |
| --- | --- |
| Descargar la aplicación desde Google Play o Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Documentación | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Detalles en JIRA de cada característica (requiere inicio de sesión) | [2.5 Features ](https://jira.dhis2.org/issues/?filter=12300) |
| Vista general en JIRA de errores corregidos (requiere inicio de sesión) | [2.5 Bugs](https://jira.dhis2.org/issues/?filter=12203) |
| Instancia demo (usuario/contraseña) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Credentials: android / Android123 |
| Comunidad DHIS 2 | [https://community.dhis2.org Mobile Community ](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Código fuente en Github | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Código fuente de SDK en Github | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |

<!-- END-WEBSITE-SYNC-ID:android -->
