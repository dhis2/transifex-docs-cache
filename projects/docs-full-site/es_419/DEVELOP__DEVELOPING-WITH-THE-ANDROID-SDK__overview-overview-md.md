---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/overview.md" 
---
# Visión general  { #overview } 

<!--DHIS2-SECTION-ID:overview-->

DHIS2 Android SDK es una biblioteca que abstrae la complejidad de interactuar con la API web DHIS2. Su objetivo es ser un punto de partida para crear aplicaciones Android para DHIS2, cubriendo algunas tareas que cualquier aplicación de Android debería implementar, como metadatos y sincronización de datos.

Objetivos principales:

- **API web abstracta de DHIS2**. No es necesario realizar consultas de API en el servidor. El SDK incluye métodos para interactuar con la API web.
- **Trabajar sin conexión**. Implementa una versión simplificada del modelo DHIS2 que se conserva en una base de datos local (SQLite). Garantiza que todos los metadatos necesarios para realizar las tareas de entrada de datos estén disponibles en cualquier momento para crear los formularios de entrada de datos. Los datos se guardan localmente y se cargan en el servidor cuando la conexión está disponible.
- **Ensure DHIS2 compatibility**. Encapsula los cambios entre las versiones de DHIS2 para que la aplicación no tenga que preocuparse por ellos. En caso de que el SDK introduzca algunos cambios para adaptarse a una nueva versión de DHIS2, la aplicación puede detectar estos cambios de forma segura en tiempo de compilación.

## Visión general de la tecnología  { #technology_overview } 

<!--DHIS2-SECTION-ID:technology_overview-->

El SDK está escrito principalmente en Java 8 utilizando el subconjunto reducido de funciones permitidas en la versión mínima de la API de Android. El SDK utiliza algunos componentes específicos de Android, como bibliotecas para crear listas paginadas (LiveData, PagedList) o para acceder al sistema de archivos. Por esta razón, actualmente **el SDK solo se puede ejecutar en un entorno Android**.

Utilizar [RxJava] (https://github.com/ReactiveX/RxJava) para facilitar el tratamiento asincrónico de algunos métodos. Aunque es opcional, recomendamos este enfoque para garantizar que las llamadas no se bloqueen.

Otras bibliotecas utilizadas internamente por el SDK son: [Dagger] (https://github.com/google/dagger) para inyección de dependencia, [Jackson] (https://github.com/FasterXML/jackson) para análisis JSON, [ Retrofit] (https://square.github.io/retrofit/) y [OkHttpClient] (https://square.github.io/okhttp/) para comunicación API o [SQLBrite] (https://github.com/ square / sqlbrite) para migraciones de bases de datos.


