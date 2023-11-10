---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-the-data-entry-app.md"
revision_date: "2021-06-14"
---

# Usando la aplicación de entrada de datos { #data_entry_app }

## Acerca de la aplicación de entrada de datos { #about_data_entry_app }

La aplicación **Entrada de datos** es donde ingresa manualmente datos agregados en DHIS2. Registra datos para una unidad organizativa, un período y un conjunto de elementos de datos (set de datos) a la vez. Un set de datos generalmente corresponde a una herramienta de recopilación de datos en papel. Los set de datos se configuran en la aplicación **Mantenimiento**.

> **Nota**
>
> Si un set de datos tiene un formulario de sección y un formulario personalizado, el sistema muestra el formulario personalizado durante la entrada de datos. Los usuarios que introducen datos no pueden seleccionar qué formulario quieren usar. En la entrada de datos basada en web, el orden de preferencia de visualización es:
>
> 1. Formulario personalizado (si existe)
>
> 2. Formulario de sección (si existe)
>
> 3. Formulario predeterminado
>
> Los dispositivos móviles no admiten formularios personalizados. La entrada de datos basada en dispositivos móviles, el orden de preferencia de visualización es:
>
> 1. Formulario de sección (si existe)
>
> 2.  Formulario predeterminado

Cuando cierra una unidad organizativa, no puede registrar ni editar datos en esta unidad organizativa en la aplicación **Entrada de datos**.

## Introducir datos en un formulario de entrada de datos { #enter_data_in_data_entry_form }

![](resources/images/data_entry/data_entry_overview.png)

1.  Abra la aplicación **Entrada de datos**.

2.  En el árbol de unidades organizativas de la izquierda, seleccione una unidad organizativa.

3.  Seleccione un **Set de Datos**.

4.  Seleccione un **Periodo**.

    Los periodos disponibles están controlados por el tipo de período del set de datos (frecuencia de informes). Puede retroceder o avanzar un año haciendo click en **Año anterior** o **Año siguiente**.

    > **Note**
    >
    > Depending on how you've configured the data entry form, you might have to enter additional information before you can open the date entry form. This can for example be a project derived from a category combination.

5.  Introducir datos en un formulario de entrada de datos.

    -   Un campo verde significa que el sistema ha guardado el valor.

    -   Un campo gris significa que el campo está deshabilitado y no puede ingresar un valor. El cursor saltará automáticamente al siguiente campo abierto.

    -   Para pasar al siguiente campo, presione la tecla Tab o la tecla de flecha hacia abajo.

    -   Para volver al campo anterior, presione Shift+Tab o la tecla de flecha hacia arriba.

    -   Si escribe un valor invalido, por ejemplo, un carácter en un campo que solo acepta valores numéricos, aparecerá un pop-up que explica el problema y el campo se coloreará de amarillo (no guardado) hasta que haya corregido el valor. .

    -   Si ha definido un rango de valor máximo mínimo para el campo e ingresa un valor que está fuera de este rango, obtendrá un mensaje pop-up informando que el valor está fuera de rango. El valor permanece sin guardar hasta que cambie el valor o actualice el rango de valores y se vuelva a introducir el valor.

6.  Cuando haya completado el formulario, haga click en **Ejecutar validación** en la esquina superior derecha o debajo del formulario de entrada de datos.

    Todas las reglas de validación que involucran elementos de datos en el formulario de entrada de datos actual (set de datos) se ejecutan luego contra los nuevos datos. Si no hay violaciones de las reglas de validación, verá un mensaje que dice _La pantalla de entrada de datos pasó la validación con éxito_. Si hay violaciones de validación, se mostrarán en una lista.

    ![](resources/images/dhis2UserManual/Validation_Rule_Result.png)

7.  (Opcional) Corregir las violaciones de validación.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros.

8.  Cuando haya corregido los errores y completado la entrada de datos, haga clic en **Completar**.

    El sistema utiliza esta información al generar informes completos para el nivel de distrito, condado, provincia o nacional.

## Marcar un valor de datos para seguimiento { #mark_data_for_followup_in_data_entry_form }

![](resources/images/data_entry/data_entry_section_history.png)

Si, por ejemplo, tiene un valor sospechoso que necesita investigar más a fondo, puede mantenerlo en el sistema, pero marcarlo para seguimiento. En la aplicación **Calidad de Datos**, puede ejecutar un análisis por seguimiento para ver y corregir todos los valores marcados.

1.  Abra la aplicación **Entrada de datos**.

2.  Abra un formulario de entrada de datos existente.

3.  Haga doble clic en el campo con el valor que desea marcar para el seguimiento.

4.  Click en icono de estrella.

## Edite los valores de los datos en un formulario de entrada de datos completo { #edit_data_value_in_completed_form }

1.  Abra la aplicación **Entrada de datos**.

2.  Abra un formulario de entrada de datos existente.

3.  Click en **Incompleto**.

4.  Cambie los valores de datos relevantes.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros,

5.  Click en **Completo**.

## Mostrar el historial de un valor de datos { #display_data_value_history }

![](resources/images/data_entry/data_entry_section_history.png)

Puede mostrar los últimos 12 valores registrados para un campo.

1.  Abra la aplicación **Entrada de datos**.

2.  Abra un formulario de entrada de datos existente.

3.  Haga doble clic en el campo con el valor para el que desea ver el historial.

4.  Haga clic en **Historial de elementos de datos**.

## Mostrar la pista de auditoría de un valor de datos { #display_data_value_audit_trail }

![](resources/images/data_entry/data_entry_audit_trail.png)

La pista de auditoría le permite ver otros valores de datos que se han ingresado antes del valor actual. La pista de auditoría también muestra cuándo el valor de los datos fue modificado y qué usuario realizó los cambios.

1.  Abra la aplicación **Entrada de datos**.

2.  Abra un formulario de entrada de datos existente.

3.  Haga doble click en el campo con el valor para el que desea ver la pista de auditoría.

4.  Haga clic en **Registro de auditoría**

## Crear rango de valor máximo mínimo manualmente { #change_min_max_range_manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  En la aplicación **Entrada de datos**, abra un formulario de entrada de datos.

2.  Haga doble click en el campo para el que desea establecer el rango de valor mínimo/máximo.

3.  Introduzca el **límite mínimo** y el **límite máximo**.

4.  Click en **Guardar**.

    Si los valores no están dentro del nuevo rango de valores la próxima vez que introduzca datos, la celda de entrada de datos aparecerá con un fondo naranja.

5.  (Opcional) Escriba un comentario para explicar el motivo de la discrepancia, por ejemplo, Por ejemplo, un evento que podría haber generado un gran número de clientes.

6.  (Opcional) Click en **Guardar comentario**.

> **Consejo**
>
> Click en el icono de estrella para marcar el valor para seguimientor posterior.

## Ingresar datos sin conexión { #enter_data_offline }

La aplicación **Entrada de datos** funciona incluso si no tiene una conexión a Internet estable durante la entrada de datos. Cuando no tiene una conexión a Internet, los datos que ingresa se guardan en su computadora local. Cuando se recupere la conexión a Internet, la aplicación enviará los datos al servidor. El uso total de ancho de banda se reduce ya que los formularios de entrada de datos ya no se recuperan del servidor para cada renderización

> **Nota**
>
> Para utilizar esta funcionalidad, debe iniciar sesión en el servidor mientras tenga una conexión a Internet.

-   Cuando está conectado a Internet, la aplicación muestra este mensaje en la parte superior del formulario de entrada de datos:

    ![](resources/images/data_entry/data_entry_online1.png)

-   Si su conexión a Internet se interrumpe durante la entrada de datos, la aplicación lo detecta y muestra este mensaje:

    ![](resources/images/data_entry/data_entry_offline1.png)

    Ahora sus datos se almacenarán localmente. Puede continuar ingresando datos con normalidad.

-   Una vez que hayas introducido todos los datos necesarios y la aplicación detecte que la conexión a Internet ha vuelto, verás este mensaje:

    ![](resources/images/data_entry/data_entry_offline_upload.png)

    Click en **Subir** para sincronizar los datos con el servidor

-   Cuando los datos se hayan sincronizado correctamente con el servidor, verá este mensaje de confirmación:

    ![](resources/images/data_entry/data_entry_offline_upload_success1.png)

## Habilitar la entrada de datos de unidades multiorganización { #data_entry_multiple_organisation_units }

![](resources/images/data_entry/data_entry_multiple_org_unit.png)

Puede resultar útil introducir datos para varias unidades organizativas en el mismo formulario de entrada de datos, por ejemplo, si hay pocos elementos de datos en el formulario y una gran cantidad de unidades organizativas en la jerarquía. En ese caso, puede habilitar la entrada de datos de unidades multiorganizativas.

> **Nota**
>
> La entrada de datos de unidades multiorganizativas solo funciona para formularios de sección.

1.  Abril la aplicación **Configuración del Sistema**

2.  Seleccione **Habilitar formularios de unidades multiorganizativas**.

3.  En la aplicación **Entrada de datos**, seleccione la unidad organizativa situada justo encima de la unidad organizativa para la que desea insertar datos en la jerarquía de la unidad organizativa.

    Los elementos de datos aparecerán como columnas y las Unidades organizativas como filas en el formulario.

    > **Note**
    >
    > The data entry forms should still be assigned to the facilities that you actually enter data for, that is the organisation units now appearing in the form.

## Ver también { #data_entry_app_see_also }

-   [Control de calidad de datos](https://docs.dhis2.org/master/en/user/html/control_data_quality.html)

-   [Gestionar set de datos y formularios de entrada de datos.](https://docs.dhis2.org/master/en/user/html/manage_data_set.html)

-   [Uso de la aplicación de mantenimiento](https://docs.dhis2.org/master/en/user/html/maintenance_app.html)
