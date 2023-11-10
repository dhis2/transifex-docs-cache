---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/getting-started.md" 
---
# Začínáme  { #getting_started } 

<!--DHIS2-SECTION-ID:getting_started-->

## Instalace { #installation } 

<!--DHIS2-SECTION-ID:installation-->

Zahrnout závislost do build.gradle.

```gradle
dependencies {
    implementation "org.hisp.dhis:android-core:1.3.0"
    ...
}
```

Kromě toho musíte toto úložiště zahrnout do souboru root gradle, pokud tam ještě není:

```gradle
allprojects {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
}
```

## Inicializace D2 { #initialization } 

<!--TODO-->

<!--DHIS2-SECTION-ID:initialization-->

Aby bylo možné začít používat SDK, je prvním krokem inicializace objektu `D2`. Pomocná třída `D2Manager` nabízí statické metody pro nastavení a inicializaci instance` D2`. Rovněž zajišťuje, že `D2` je v aplikaci singleton.

Minimální konfigurace, která musí být předána do `D2Manager`, je následující:

```java
D2Configuration configuration = D2Configuration.builder()
    .context(context)
    .build();
```

Pomocí konfigurace můžete vytvořit instanci `D2`.

```java
Single<D2> d2Single = D2Manager.instantiateD2(configuration);
```

Po dokončení Single můžete přistupovat k D2 následující metodou:

```java
D2 d2 = D2Manager.getD2();
```

Pokud nepoužíváte RxJava, můžete instanci `D2` vytvořit blokujícím způsobem:

```java
D2 d2 = D2Manager.blockingInstantiateD2(configuration);
```

Objekt `D2Configuration` má mnoho polí pro konfiguraci chování SDK.

|  Atribut    |   Požadované    |   Popis | Výchozí
|-|-|-|-|
| kontext       | true          | Kontext aplikace | -
| appName       | false         | Slouží k vytvoření záhlaví „user-agent“ | Z manifestu pro Android
| appVersion    | false         | Slouží k vytvoření záhlaví „user-agent“ | Z manifestu pro Android
| readTimeoutInSeconds | false  | Časový limit čtení pro dotazy HTTP | 30 sekund
| connectTimeoutInSeconds | false | Časový limit připojení pro dotazy http | 30 sekund
| writeTimeoutInSeconds | false | Časový limit zápisu pro dotazy HTTP | 30 sekund
| interceptors  | false         | Interceptory pro OkHttpClient | Žádný
| networkInterceptors | false   | NetworkInterceptors pro OkHttpClient | Žádný


