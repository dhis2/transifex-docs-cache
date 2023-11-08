---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/modules-and-repositories.md" 
---
# Módulos y repositorios  { #modules_and_repositories } 

<!--DHIS2-SECTION-ID:modules_and_repositories-->

El objeto `D2` es el punto de entrada para interactuar con el SDK. El SDK obliga al objeto `D2` a ser un singleton en toda la aplicación.

Los módulos son la capa debajo de `D2`. Actúan como un contenedor para la funcionalidad relacionada. Un módulo incluye algunos repositorios relacionados y puede exponer algunos servicios y helpers.

Los repositorios actúan como una fachada para la base de datos (o API web en algunos casos). Ofrecen capacidades de lectura de metadatos y lectura/escritura de datos.

## Tratar con tipos de retorno: RxJava { #dealing_with_rxjava } 

<!--DHIS2-SECTION-ID:dealing_with_rxjava-->

El SDK usa clases RxJava (Observable, Single, Completable, Flowable) como el tipo de retorno preferido para todos los métodos. Las razones para elegir las clases de RxJava son principalmente dos:

- **Para facilitar el tratamiento asincrónico de los objetos devueltos** La mayoría de las acciones en el SDK consumen mucho tiempo y deben ser ejecutadas en un subproceso secundario. Estos tipos de retorno obligan a la aplicación a lidiar con este comportamiento asincrónico.
- **Para notificar sobre el progreso.** Métodos como los metadatos o la sincronización de datos pueden tardar varios minutos en completarse. Desde la perspectiva del usuario, es muy útil tener una sensación de progreso.

Esto no significa que las aplicaciones estén obligadas a usar RxJava en su código: solo están obligadas a lidiar con el comportamiento asincrónico de algunos métodos. El SDK generalmente expone la versión *blocking* de cada método.

Por ejemplo, la misma consulta usando RxJava y AsyncTask:

*Usando RxJava*

```java
d2.programModule().programs()
    .subscribeOn(Schedulers.io())
    .observeOn(AndroidSchedulers.mainThread())
    .get()
    .subscribe(programs -> {}); //List<Program>
```

*Usando AsyncTask*

```java
new AsyncTask<Void, Void, List<Program>>() {
    protected List<Program> doInBackground() {
        return d2.programModule().programs().blockingGet();
    }

    protected void onPostExecute(List<Program> programs) {

    }
}.execute();
```

Acceder a la base de datos requiere mucho tiempo y se recomienda hacerlo en un subproceso separado usando cualquiera de los métodos
recomendados. Sin embargo, los procedimientos que implican el acceso a la API web, como el inicio de sesión, los metadatos o la descarga o carga de datos **deben**
ejecutarse en un subproceso separado, de lo contrario, Android arrojará un error.

## Construcción de consultas { #query_building } 

<!--DHIS2-SECTION-ID:query_building-->

Los repositorios ofrecen una sintaxis de constructor con validación en tiempo de compilación para acceder a los recursos. Una consulta típica se compone de algunos modificadores (filtro, orden, campos anidados) y termina con una acción (get, count, getPaged, ...).

```java
// Generic syntax
d2.<module>.<repository>
    .[ filter | orderBy | nested fields ]
    .<action>;

// An example for events
d2.eventModule().events()
    .byOrganisationUnitUid().eq("DiszpKrYNg8")
    .byEventDate().after(Date("2019-05-05"))
    .orderByEventDate(DESC)
    .withTrackedEntityDataValues()
    .get();
```

### Filtros { #filters } 

<!--DHIS2-SECTION-ID:filters-->

Los repositorios exponen la lista de filtros disponibles precedidos por la palabra clave "by". La lista de operadores de filtro disponibles para cada filtro depende del tipo de valor del filtro: por ejemplo, un tipo de valor `Fecha` ofrecerá operadores como `después`, `antes`, `en períodos`, mientras que un tipo de valor `Booleano` oferta `isFalse` o ` isTrue`.

Varios filtros pueden ser anexados a la misma consulta en cualquier orden. Los filtros se unen globalmente mediante el operador "AND". Esto significa que una consulta como

```java
d2.eventModule().events()
    .byOrganisationUnitUid().eq("DiszpKrYNg8")
    .byEventDate().after(Date("2019-05-05"))
    ...
```

retornará los eventos asignados a la unidad organizativa "DiszpKrYNg8" **AND** cuya fecha de evento sea posterior a "2019-05-05".

### Ordenar por { #order_by } 

<!--DHIS2-SECTION-ID:order_by-->

Los modificadores de orden tienen como prefijo la palabra clave "orderBy".

Varios modificadores "orderBy" pueden ser anexados a la misma consulta. El orden de los modificadores "orderBy" dentro de la consulta determina la prioridad del orden. Esto significa que una consulta como

```java
d2.eventModule().events()
    .orderByEventDate(DESC)
    .orderByLastUpdated(DESC)
    ...
```

ordenará por descendiente EventDate en primer lugar, y luego por descendiente LastUpdated

### Incluir campos anidados { #nested_fields } 

<!--DHIS2-SECTION-ID:nested_fields-->

Los repositorios retornan clases que no coinciden exactamente con las tablas de la base de datos: son objetos más complejos que pueden incluir algunas propiedades obtenidas de otras tablas. Por ejemplo, la clase `Event` tiene una propiedad llamada `trackedEntityDataValues` que incluye una lista de TrackedEntityDataValues. La razón principal para elegir este tipo de objetos es absorber la complejidad de tratar con tablas de enlaces para que la aplicación no tenga que preocuparse por construir enlaces entre objetos.

Por cuestiones de rendimiento, este tipo de propiedades no se incluyen por defecto: deben ser consultadas explícitamente. En los repositorios, las propiedades que no están incluidas por defecto y necesitan ser consultadas tienen como prefijo la palabra clave "with".

Varias propiedades pueden ser anexadas en la misma consulta en cualquier orden. Por ejemplo, una consulta como

```java
d2.programModule().programs()
    .withTrackedEntityType()
    ...
```

retornará un objeto anidado `TrackedEntityType`.

## Helpers { #helpers } 

<!--DHIS2-SECTION-ID:helpers-->

El SDK incluye algunos helpers en el paquete `org.hisp.dhis.android.core.arch.helpers`. Se pueden encontrar fácilmente en Android Studio buscando `Helper` en los nombres de las clases. Incluyen algunos métodos útiles para realizar operaciones comunes:

- `AccessHelper`: relacionado con el objeto de acceso (configuración de uso compartido).
- `CollectionsHelper`: operaciones comunes para colecciones.
- `CoordinateHelper`,` GeometryHelper`: manipulación de datos geoespaciales.
- `FileResizeHelper`, `FileResourceDirectoryHelper`: manipulación de recursos de archivos.
- `UidsHelper`: operaciones comunes  para colecciones de objetos con uid.
- `UserHelper`: operaciones relacionadas con la autenticación de usuarios.

## Lista de módulos { #module_list } 

<!--DHIS2-SECTION-ID:module_list-->

Módulos del sistema:

- importModule
- maintenanceModule
- systemInfoModule
- settingModule
- wipeModule

Módulos de bloque grande:

- metadataModule
- aggregatedDataModule

Módulos específicos:

- categoryModule
- constantModule
- dataElementModule
- dataSetModule
- dataValueModule
- enrollmentModule
- eventModule
- fileResourceModule
- indicatorModule
- legendSetModule
- noteModule
- organisationUnitModule
- optionModule
- periodModule
- programModule
- relationshipModule
- smsModule
- trackedEntityModule
- userModule
- validationModule


