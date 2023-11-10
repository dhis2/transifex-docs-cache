---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/debugging.md" 
---
# Depuración

<!--DHIS2-SECTION-ID:debugging-->

Además de las herramientas de depuración habituales de AndroidStudio, la biblioteca [Stetho](http://facebook.github.io/stetho/) permite el uso de herramientas de desarrollo de Chrome para depurar el tráfico de red y explorar la base de datos.

Configure Stetho añadiendo las siguientes dependencias en su archivo gradle:

```gradle
dependencies {
    implementation 'com.facebook.stetho:stetho:1.5.0'
    implementation 'com.facebook.stetho:stetho-okhttp3:1.5.0'
}
```

A continuación, agregue un interceptor de red en `D2Configuration` objeto:

```java
D2Configuration.builder()
    ...
    .networkInterceptors(Collections.singletonList(new StethoInterceptor()))
    ...
    .build();
```

Por último, habilite la inicialización de Stetho en la clase `Application`:

```java
if (DEBUG) {
    Stetho.initializeWithDefaults(this);
}
```

En este punto, debería poder depurar la app / sdk utilizando Chrome Inspector Tools:

- Ejecute una prueba en modo de depuración y establezca un punto de interrupción.
- En el navegador Chrome, abra el [inspector de dispositivos] (chrome://inspect/devices#devices).
- Seleccione el objetivo remoto y haga clic en Inspeccionar. Aparecerá una nueva ventana que muestra las herramientas para desarrolladores de Chrome.
- Explore la base de datos en "Recursos> Web SQL".
- Explore el tráfico de la red en "Red".


