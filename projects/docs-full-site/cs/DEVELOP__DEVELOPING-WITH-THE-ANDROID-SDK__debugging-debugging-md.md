---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/debugging.md" 
---
# Ladění  { #debugging } 

<!--DHIS2-SECTION-ID:debugging-->

Kromě běžných nástrojů pro ladění v AndroidStudiu umožňuje knihovna [Stetho](http://facebook.github.io/stetho/) použití nástrojů pro vývojáře Chrome k ladění síťového provozu a prozkoumání databáze.

Nastavit Stetho přidáním následujících závislostí do souboru gradle:

```gradle
dependencies {
    implementation 'com.facebook.stetho:stetho:1.5.0'
    implementation 'com.facebook.stetho:stetho-okhttp3:1.5.0'
}
```

Poté přidejte síťový interceptor do objektu `D2Configuration`:

```java
D2Configuration.builder()
    ...
    .networkInterceptors(Collections.singletonList(new StethoInterceptor()))
    ...
    .build();
```

Nakonec povolte inicializaci Stetho ve třídě `Application`:

```java
if (DEBUG) {
    Stetho.initializeWithDefaults(this);
}
```

V tomto okamžiku byste měli být schopni ladit aplikaci / sdk pomocí nástroje Chrome Inspector Tools:

- Spusťte test v režimu ladění a nastavte breakpoint.
- V prohlížeči Chrome otevřete [device inspector](chrome://inspect/devices#devices).
- Vyberte vzdálený cíl a klikněte na Zkontrolovat. Objeví se nová okna s nástroji pro vývojáře Chrome.
- Prozkoumejte databázi v části "Zdroje > Web SQL“.
- Prozkoumejte síťový provoz v části „Síť“.


