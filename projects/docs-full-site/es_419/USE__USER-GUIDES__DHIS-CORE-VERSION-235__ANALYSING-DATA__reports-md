---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-reporting-functionality.md"
revision_date: "2022-02-08"
---

# Funcionalidad de informes en la aplicación informes { #using_the_reports_app }

La aplicación de informes permite informes listos para usar, informes estándar, informes a partir de set de datos, recursos e informes de distribución de unidades organizativas.

## Usar informes estándar { #standard_reports_in_the_beta_reports_app }

Puede acceder a los informes disponibles navegando a través de Aplicaciones - \> Informes. En el menú de informes de la barra izquierda, haga clic en Informe estándar. Aparecerá una lista de todos los informes predefinidos en la ventana principal.

![](resources/images/dhis2UserManual/react_reports_app_standard_reports.png)

Puede ejecutar/ver un informe haciendo click en el icono de tres puntos del informe y luego seleccionando "Crear" en el menú contextual. Si hay parámetros predefinidos, verá una ventana de parámetros  en la que deberá llenar los valores necesarios para la unidad organizativa y/o mes de informe, según lo que se haya definido en la(s) tabla(s) del informe subyacente. Haga click en "Generar informe" cuando esté listo. El informe aparecerá directamente en su navegador o estará disponible como un archivo PDF para descargar, dependiendo de la configuración de su navegador para manejar archivos PDF. Puede guardar el archivo y conservarlo localmente en su computadora para su uso posterior.

## Usar informes de set de datos { #dataset_reports_in_the_beta_reports_app }

Los informes de set de datos son vistas fáciles de imprimir de la pantalla de entrada de datos con datos sin procesar o agregados. 

Puede acceder a los informes de set de datos desde Aplicaciones-\>Informes.

Aparecerá una ventana de Criterios donde completará los detalles de su informe:

**Set de datos:** El set de datos que desea mostrar.

**Periodo del informe:** El periodo real para el que desea obtener datos. Esto puede ser agregado así como periodos sin procesar. Esto significa que puede solicitar un informe trimestral o anual aunque el set de datos se recopile mensualmente. El tipo de periodo de un set de datos (frecuencia de recopilación) se define en el mantenimiento del set de datos. Primero seleccione el tipo de periodo (mensual, trimestral, anual, etc.) en el menú desplegable junto a los botones Anterior y Siguiente, y luego seleccione uno de los periodos disponibles de la lista desplegable a continuación. Utilice Anterior y Siguiente para retroceder o avanzar un año.

**Usar datos solo para la unidad seleccionada:** Use esta opción si desea un informe para una unidad organizativa que tiene hijos, pero solo desea los datos recopilados directamente por esta unidad y no los datos recopilados por sus hijos. Si desea un informe agregado típico para una unidad organizativa, no debe marcar esta opción.

**Informe de la unidad organizativa:** Aquí selecciona la unidad organizativa para la que desea el informe. Esto puede ser en cualquier nivel de la jerarquía, ya que los datos se agregarán hasta este nivel automáticamente (si no marca la opción anterior).

Cuando haya terminado de completar los criterios del informe, haga clic en "Generar". El informe aparecerá como HTML en un formato para imprimir. Utilice las funciones de imprimir y guardar del navegador para imprimir o guardar el informe (como archivo HTML). También puede exportar el informe del set de datos en formatos Excel y PDF.

## Usar el resumen de la tasa de informes { #reporting_rate_summary_in_the_beta_reports_app }

Acceda al resumen de la tasa de informes desde el menú Aplicaciones-\>Informes. Los resúmenes de tasas de informes mostrarán cuántos set de datos (formularios) se han enviado por unidad organizativa y periodo.

El cálculo de la tasa de notificación se basa en registros de set de datos completos. Un registro de set de datos completo significa que el usuario marca el formulario de entrada de datos como completo, normalmente haciendo click en el botón completo en la pantalla de entrada de datos, indicando al sistema que considera que el formulario está completo. Esto es, por decir, un enfoque subjetivo para calcular la completitud.

El resumen de la tasa de informes mostrará para cada fila un rango de medida:

-   Informes reales: Indica el número de registros completos de entrada de datos para el set de datos correspondiente.

-   Informes esperados: indica cuántos registros completos de entrada de datos se esperan. Este número se basa en el número de unidades organizativas a las que se ha asignado el set de datos relevante (habilitado para la entrada de datos).

-   Tasa de informes: El porcentaje de informes registrados como completos en base al número esperado.

-   Informes a tiempo: Igual que los informes reales, solo los informes registrados como completos dentro del número máximo de días después del final del periodo de informe. Este número de días después del periodo de informe puede ser definido por set de datos en la administración de set de datos.

-   Tasa de informes a tiempo: igual que el porcentaje, solo los informes registrados como completos a tiempo se utilizan como numerador.

Para ejecutar el informe, puede seguir estos pasos:

-   Seleccionar una unidad organizativa del árbol.
-   Seleccionar un set de datos.

-   Seleccionar un tipo de periodo y un periodo de la lista de periodos disponibles para ese tipo de periodo.

-   A continuación, se generará el informe. Cambie cualquiera de los parámetros anteriores y haga click en "Obtener informe" nuevamente para ver los resultados correspondientes.

![](resources/images/dhis2UserManual/react_reports_app_reporting_rate_summary.png)

## Usar recursos { #resources_in_the_beta_reports_app }

La herramienta de recursos le permite subir ambos archivos desde su computadora local al servidor DHIS y agregar enlaces a otros recursos en Internet a través de URL. Si el almacenamiento en la nube está configurado para su sistema, los recursos se guardarán allí.

Para crear un nuevo recurso:

1.  Abrir la aplicación **Informes** y click en **Recursos**.

2.  Click en **Agregar nuevo**.

3.  Introducir un **Nombre**.

4.  Seleccionar un **Tipo**: **Cargar archivo** o **URL externa**.

5.  Click en **Guardar**.

## Usar informes de distribución de unidades organizativas { #orgunit_distribution_reports_in_the_beta_reports_app }

Puede acceder a los informes de distribución de unidades organizativas (Orgunit Distribution reports) desde el menú de la izquierda en Aplicaciones-\>Informes.

Los informes de distribución de unidades organizativas son informes que muestran cómo se distribuyen las unidades organizativas en varias propiedades como el tipo y la propiedad, y por zonas geográficas.

El resultado se puede presentar en un informe basado en tablas o en un gráfico.

**Ejecutar un informe:**

Para ejecutar un informe, primero seleccione la unidad organizativa en el árbol de unidad organizativa en la parte superior izquierda. El informe se basará en las unidades organizativas situadas debajo de la unidad organizativa seleccionada. Seleccione el set de grupos de unidad organizativa que desea utilizar, normalmente son Tipo, Propiedad, Rural/Urbano, pero puede ser cualquier set de grupos de unidad organizativa definido por el usuario.  A continuación, puede hacer click en Obtener informe para obtener la presentación basada en una tabla o en Obtener gráfico para obtener el mismo resultado en un gráfico. También puede descargar el informe basado en la tabla como Excel o CSV.

![](resources/images/dhis2UserManual/react_reports_app_org_unit_dist.png)
