---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/getting-started.md" 
---
# Comenzar  { #getting_started } 

<!--DHIS2-SECTION-ID:getting_started-->

## Instalación { #installation } 

<!--DHIS2-SECTION-ID:installation-->

Incluir la dependencia en build.gradle.

```gradle
dependencies {
    implementation "org.hisp.dhis:android-core:1.3.0"
    ...
}
```

Adicionalmente, debe incluir este repositorio en su archivo root gradle si aún no está allí:

```gradle
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

## inicialización D2 { #initialization } 

<!--TODO-->

<!--DHIS2-SECTION-ID:initialization-->

Para comenzar a usar el SDK, el primer paso es inicializar un objeto `D2`. La clase auxiliar `D2Manager` ofrece métodos estáticos para configurar e inicializar la instancia` D2`. Además, asegura que  `D2`  sea un singleton en toda la aplicación.

La configuración mínima que debe pasarse al `D2Manager` es la siguiente:

```java
D2Configuration configuration = D2Configuration.builder()
    .context(context)
    .build();
```

Usando la configuración puede instanciar `D2`.

```java
Single<D2> d2Single = D2Manager.instantiateD2(configuration);
```

Una vez completado el Single, puede acceder a D2 con el siguiente método:

```java
D2 d2 = D2Manager.getD2();
```

Si no está utilizando RxJava, puede crear una instancia `D2` en forma de bloqueo:

```java
D2 d2 = D2Manager.blockingInstantiateD2(configuration);
```

El objeto `D2Configuration` tiene muchos campos para configurar el comportamiento del SDK.

|  Atributo    |   Requerido    |   Descripción | Predeterminado
|-|-|-|-|
| contexto       | verdadero          | Contexto de la aplicación | -
| appName       | falso         | Utilizar para crear la cabecera "user-agent" | Desde Android Manifest
| appVersion    | falso         | Utilizar para crear la cabecera "user-agent" | Desde Android Manifest
| readTimeoutInSeconds | falso  | Tiempo límite de lectura para consultas http | 30 segundos
| connectTimeoutInSeconds | falso | Tiempo límite de conexión para consultas http | 30 segundos
| writeTimeoutInSeconds | falso | Tiempo límite de escritura para consultas http | 30 segundos
| interceptores  | falso         | Interceptores para OkHttpClient | Ninguno
| networkInterceptors | falso   | NetworkInterceptors para OkHttpClient | Ninguno


