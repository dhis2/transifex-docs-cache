---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/debugging.md" 
---
# Depurando  { #debugging } 

<!--DHIS2-SECTION-ID:debugging-->

Além das ferramentas de depuração regulares no AndroidStudio, a biblioteca [Stetho] (http://facebook.github.io/stetho/) permite o uso das Ferramentas de desenvolvedor do Chrome para depurar o tráfego da rede e explorar o banco de dados.

Configure o Stetho adicionando as seguintes dependências em seu arquivo Gradle:

```gradle
dependencies {
    implementation 'com.facebook.stetho:stetho:1.5.0'
    implementation 'com.facebook.stetho:stetho-okhttp3:1.5.0'
}
```

Em seguida, adicione um interceptor de rede no objeto `D2Configuration`:

```java
D2Configuration.builder()
    ...
    .networkInterceptors(Collections.singletonList(new StethoInterceptor()))
    ...
    .build();
```

Por fim, habilite inicializar Stetho na classe `Application`:

```java
if (DEBUG) {
    Stetho.initializeWithDefaults(this);
}
```

Neste ponto, você deve ser capaz de depurar o app / sdk usando as ferramentas do Chrome Inspector:

- Execute um teste no modo de depuração e defina um ponto de interrupção.
- No navegador Chrome, abra o [inspetor de dispositivo](chrome://inspect/devices#devices).
- Selecione o alvo remoto e clique em Inspecionar. Uma nova janela aparecerá mostrando as ferramentas de desenvolvedor do Chrome.
- Explore o banco de dados em "Recursos> Web SQL".
- Explore o tráfego de rede em "Rede".


