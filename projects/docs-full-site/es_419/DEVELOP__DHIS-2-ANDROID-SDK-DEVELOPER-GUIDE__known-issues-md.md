---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/known-issues.md" 
---
# Problemas conocidos

<!--DHIS2-SECTION-ID:known_issues-->

## Completar set de datos

- En DHIS2 versión 2.33.0 y 2.33.1, si un set de datos se marca como incompleto en el servidor, este valor no se actualiza en el SDK. En esas versiones, la API no exponía suficiente información para saber si el estado era completo o incompleto.

