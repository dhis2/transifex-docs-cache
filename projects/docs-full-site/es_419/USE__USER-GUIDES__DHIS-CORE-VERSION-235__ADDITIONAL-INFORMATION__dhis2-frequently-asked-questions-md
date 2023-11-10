---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/dhis2-frequently-asked-questions.md"
revision_date: "2021-06-14"
---

# DHIS2 Preguntas frecuentes { #dhis2-frequently-asked-questions }

**P:** He introducido datos en un formulario de entrada de datos, pero no puedo ver los datos en ningún informe (tablas dinámicas, gráficos, mapas). ¿Por qué los datos introducidos no aparecen inmediatamente en mis gráficos en DHIS2?

**R:** Los datos introducidos en DHIS2 primero deben procesarse con "Analíticas". Esto significa que los datos no están disponibles inmediatamente en los recursos de análisis (como informes, tablas dinámicas, visualizador de datos, SIG, etc.) después de que se hayan ingresado. Si la programación está activa, el proceso de analíticas se ejecutará automáticamente a la medianoche todos los días. Después de eso, se harán visibles los nuevos datos que se ingresaron desde la última vez que se ejecutó el proceso de analíticas.

Puede activar el proceso de analíticas manualmente seleccionando Informes-\>Analíticas en el menú principal y presionando el botón "Iniciar exportación". Tenga en cuenta que el proceso puede llevar una cantidad significativa de tiempo dependiendo de la cantidad de datos en su base de datos.

Otros factores que pueden afectar la visibilidad de los datos son:

-   Aprobación de datos: si los datos no han sido aprobados a un nivel que corresponde a su nivel de usuarios, es posible que no pueda verlos.

-   Compartir objetos de meta-datos: si ciertos objetos de meta-datos no han sido compartidos con un grupo de usuarios del que es miembro, los datos pueden no ser visibles para ti.

-   Almacenamiento en caché de analíticas: en muchos casos, los administradores del servidor almacenan en caché objetos analíticos (como tablas dinámicas, mapas, gráficos) en el servidor. Si ha introducido datos, ha vuelto a ejecutar analíticas y aún no ve ningún dato (actualizado), asegúrese de que el servidor no esté almacenando sus datos en caché.

**P:** Descargué DHIS2 de <https://www.dhis2.org/downloads> pero cuando intento ingresar al sistema, necesito un nombre de usuario y una contraseña. ¿Cuál debo usar?

**R:** Por defecto, el nombre de usuario será "admin" y la contraseña "distrito". Los nombres de usuario y las contraseñas distinguen entre mayúsculas y minúsculas.
