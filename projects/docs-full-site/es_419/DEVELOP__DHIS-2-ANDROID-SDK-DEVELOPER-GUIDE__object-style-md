---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/object-style.md" 
---
# Estilo de objeto

<!--DHIS2-SECTION-ID:object-style-->

Algunos elementos incluyen una propiedad llamada "estilo" que define un icono y un color. Esta información visual es muy útil para navegar rápidamente por la aplicación. Algunos casos de uso típicos:

- Distinga diferentes programas y trackedEntityTypes en una lista de programas.
- En formularios de entrada de datos con un Set de opciones, muestra las opciones con iconos y colores en lugar de nombres.
- Diferentes etapas de programa dentro de un programa.

Esta propiedad es opcional y no está definida en la mayoría de los casos. Un estilo de objeto puede tener un icono, un color o ambos.

## Icono

El conjunto de iconos utilizados en DHIS2 están incluidos en el SDK. Se encuentran dentro de los recursos, en la carpeta "drawable". Actualmente están predefinidos y no se pueden personalizar.

```java

// Illustrative code to get the resource id
if (program.style().icon() != null) {
    String iconName = program.style().icon();
    int resourceId = getResources().getIdentifier(iconName, "drawable", getPackageName());
}
```

## Color

Contiene el valor hexadecimal del color. Se puede utilizar para personalizar el fondo, el color del texto, los encabezados de línea, etc.

```java
program.style().color();    // For example #9C33FF

```


