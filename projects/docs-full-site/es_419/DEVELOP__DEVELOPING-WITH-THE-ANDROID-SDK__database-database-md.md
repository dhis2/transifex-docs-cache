---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/database.md" 
---
# Base de datos  { #database } 

<!--DHIS2-SECTION-ID:database-->

## Alcance de la base de datos { #database-scope } 
El SDK guarda los datos de un par [servidor, usuario] en una base de datos aislada.

Por el momento, solo un [servidor, usuario] es soportado, por lo que cerrar sesión y entrar con otro  [servidor, usuario]
eliminará la base de datos actual y creará una nueva.

## Cifrado { #encryption } 
A partir de la versión 1.1.0 del SDK, es posible almacenar los datos en una base de datos cifrada. La clave de cifrado se genera de forma aleatoria
por el SDK y se mantiene seguro.

El estado de cifrado (si la base de datos está cifrada o no) se puede configurar a nivel de servidor en la aplicación de configuración de Android.
El estado predeterminado es falso: si la aplicación no está instalada, la base de datos no estará cifrada.

Durante el primer inicio de sesión para un servidor y usuario determinados, el estado de cifrado se  descargará desde la API y
se creará una base de datos del tipo dado.

En inicios de sesión posteriores o sincronizaciones de metadatos, el SDK volverá a descargar el estado de cifrado desde el servidor y,
si se cambia, cifrará o descifrará la base de datos actual sin pérdida de datos.

### Rendimiento de cifrado { #encryption-performance } 
- Tamaño de la base de datos: el tamaño de la base de datos es aproximadamente el mismo, independientemente de que esté cifrada o no.
- Velocidad: las lecturas y escrituras son en promedio de un 5 a un 10% más lentas si se usa una base de datos cifrada.

