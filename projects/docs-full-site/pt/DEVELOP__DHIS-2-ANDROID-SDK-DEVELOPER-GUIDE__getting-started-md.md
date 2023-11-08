---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/getting-started.md" 
---
# Começando

<!--DHIS2-SECTION-ID:getting_started-->

## Instalação

<!--DHIS2-SECTION-ID:installation-->

Inclui dependência em build.gradle.

```gradle
dependencies {
    implementation "org.hisp.dhis:android-core:1.3.0"
    ...
}
```

Além disso, você precisa incluir este repositório em seu arquivo gradle raiz, se ainda não estiver lá:

`` `gradle
allprojects {
    repositórios {
        ...
        maven {url 'https://jitpack.io'}
    }
}
`` `

## Inicialização D2

<!--TODO-->

<!--DHIS2-SECTION-ID:initialization-->

Para começar a usar o SDK, a primeira etapa é inicializar um objeto `D2`. A classe auxiliar `D2Manager` oferece métodos estáticos para configurar e inicializar a instância` D2`. Além disso, garante que `D2` seja um singleton em todo o aplicativo.

A configuração mínima que deve ser passada ao `D2Manager` é a seguinte:

```java
D2Configuration configuration = D2Configuration.builder()
    .context(context)
    .build();
```

Usando a configuração, você pode instanciar `D2`.

```java
Single<D2> d2Single = D2Manager.instantiateD2(configuration);
```

Assim que o Single for concluído, você pode acessar D2 com o seguinte método:

```java
D2 d2 = D2Manager.getD2();
```

Se você não estiver usando RxJava, você pode instanciar `D2` de forma bloqueadora:

```java
D2 d2 = D2Manager.blockingInstantiateD2(configuration);
```

O objeto `D2Configuration` possui vários campos para configurar o comportamento do SDK.

|  Atributo    |   Requerido    |   Descrição | Padrão
|-|-|-|-|
| contexto       | verdade          | Contexto de aplicação | -
| nome do aplicativo       | falso         | Use para criar o cabeçalho "user-agent" | Do Android Manifest
| appVersion    | falso         | Use para criar o cabeçalho "user-agent" | Do Android Manifest
| readTimeoutInSeconds | falso  | Tempo limite de leitura para consultas http | 30 segundos
| connectTimeoutInSeconds | falso | Tempo limite de conexão para consultas http | 30 segundos
| writeTimeoutInSeconds | falso | Tempo limite de gravação para consultas http | 30 segundos
| interceptores  | falso         | Interceptadores para OkHttpClient | Nenhum
| networkInterceptors | falso   | NetworkInterceptors para OkHttpClient | Nenhum


