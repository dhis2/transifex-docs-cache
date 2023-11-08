---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/settings.md" 
---
# Configuración  { #settings } 

<!--DHIS2-SECTION-ID:settings-->

Las configuraciones se descargan en cada sincronización de metadatos. Hay diferentes tipos de configuraciones:

```java
d2.settingModule()
```

- **Configuración del Sistema**: propiedades de todo el sistema como `flag` o` style`.
- **Configuración de usuario**: configuración específica de usuario como `keyDbLocale` o` keyUiLocale`.
- **Aplicación Configuraciones**: estas configuraciones ofrecen un control adicional sobre el comportamiento de la aplicación. Más sobre esto en la siguiente sección.



## Aplicación Configuraciones { #settings_app } 

<!--DHIS2-SECTION-ID:settings_app-->

La instancia de DHIS2 podría incluir una aplicación web llamada "Configuración de Android" que permite tener control remoto sobre ciertos parámetros de la aplicación. La instalación y configuración de esta aplicación es opcional.

Este SDK descarga esta configuración en cada sincronización de metadatos y la mantiene en la base de datos. Algunos de estos parámetros son consumidos automáticamente por el SDK (en negrita).

General:

- Frecuencia de sincronización de metadatos/datos: este valor debe ser consumido por la aplicación y utilizarlo para activar la sincronización en el SDK.
- Configuración del móvil: número de gateway, número de remitente. Deben ser consumidos por la aplicación y utilizados para configurar el módulo SMS en el SDK.
- **Valores reservados**: número de valores de atributo a reservar.
- **Encriptar base de datos**: encriptar o no la base de datos local.

**Programas:** esta sección controla los parámetros de sincronización de datos del programa. Tiene una sección para definir los parámetros globales o predeterminados que se utilizarán en la sincronización de todos los programas. Además, permite establecer configuraciones específicas para programas particulares. Todos estos parámetros son consumidos por el SDK y utilizados en el proceso de sincronización.

**Set de Datos:** esta sección controla los parámetros de sincronización de datos agregados. Tiene una sección para definir los parámetros globales o predeterminados que se utilizarán en la sincronización de todos los Set de datos. Además, permite establecer configuraciones específicas para Set de datos particulares. Todos estos parámetros son consumidos por el SDK y utilizados en el proceso de sincronización.

```java
// General settings
d2.settingModule().generalSetting().get();

// Program settings
d2.settingModule().programSetting().get();

// DataSet settings
d2.settingModule().dataSetSetting().get();
```

Aunque estos parámetros son consumidos automáticamente por el SDK, la aplicación puede anular algunos de esos valores en el proceso de sincronización. Por ejemplo, puede definir un límite de TEI o de eventos diferente o una estrategia de descarga diferente (limitByOrgUnit, limitByProgram).

