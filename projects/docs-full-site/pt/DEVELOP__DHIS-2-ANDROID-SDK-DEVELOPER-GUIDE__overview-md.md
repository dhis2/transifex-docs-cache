---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/overview.md" 
---
# Visão Geral

<!--DHIS2-SECTION-ID:overview-->

DHIS2 Android SDK é uma biblioteca que abstrai a complexidade da interação com a API da web DHIS2. Pretende ser um ponto de partida para construir aplicativos Android para DHIS2, cobrindo algumas tarefas que qualquer aplicativo Android deve implementar, como metadados e sincronização de dados.

Objetivos principais:

- ** API da web DHIS2 abstrata **. Não há necessidade de realizar consultas de API no servidor. O SDK inclui métodos para interagir com a API da web.
- **Trabalho offline**. Ele implementa uma versão simplificada do modelo DHIS2 que é persistido em um banco de dados local (SQLite). Ele garante que todos os metadados necessários para realizar as tarefas de entrada de dados estejam disponíveis a qualquer momento para construir os formulários de entrada de dados. Os dados são salvos localmente e carregados no servidor quando a conexão está disponível.
- ** Garanta a compatibilidade DHIS2 **. Ele encapsula as alterações entre as versões DHIS2 para que o aplicativo não precise se preocupar com elas. Caso o SDK introduza algumas alterações para acomodar uma nova versão DHIS2, o aplicativo pode detectar com segurança essas alterações em tempo de compilação.

## Visão geral da tecnologia

<!--DHIS2-SECTION-ID:technology_overview-->

O SDK é escrito em Java 8 usando o subconjunto reduzido de recursos permitidos na versão mínima da API Android. O SDK usa alguns componentes específicos do Android, como bibliotecas para criar listas pagináveis (LiveData, PagedList) ou para acessar o sistema de arquivos. Por esse motivo, atualmente ** o SDK só pode ser executado em um ambiente Android **.

Ele usa [RxJava] (https://github.com/ReactiveX/RxJava) para facilitar o tratamento assíncrono de alguns métodos. Embora seja opcional, recomendamos essa abordagem para garantir chamadas sem bloqueio.

Outras bibliotecas usadas internamente pelo SDK são: [Dagger](https://github.com/google/dagger) para injeção de dependência, [Jackson] (https://github.com/FasterXML/jackson) para análise JSON, [ Retrofit] (https://square.github.io/retrofit/) e [OkHttpClient] (https://square.github.io/okhttp/) para comunicação de API ou [SQLBrite](https://github.com/square/sqlbrite) para migrações de banco de dados.


