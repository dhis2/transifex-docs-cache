---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/modules-and-repositories.md" 
---
# Módulos e repositórios  { #modules_and_repositories } 

<!--DHIS2-SECTION-ID:modules_and_repositories-->

O objecto `D2` é o ponto de entrada para interagir com o SDK. O SDK força o objecto `D2` a ser um singleton em todo o aplicativo.

Os módulos estão na camada abaixo de `D2`. Eles atuam como um invólucro para funcionalidades relacionadas. Um módulo inclui alguns repositórios relacionados e pode expor alguns serviços e auxiliares.

Os repositórios atuam como uma fachada para o banco de dados (ou API da web em alguns casos). Eles oferecem recursos de leitura de metadados e leitura/gravação de dados.

## Lidando com tipos de retorno: RxJava { #dealing_with_rxjava } 

<!--DHIS2-SECTION-ID:dealing_with_rxjava-->

O SDK usa classes RxJava (Observable, Single, Completable, Flowable) como o tipo de retorno preferido para todos os métodos. As razões para escolher as classes RxJava são principalmente duas:

- **Para facilitar o tratamento assíncrono dos objetos retornados.** A maioria das acções no SDK são demoradas e devem ser executadas em um thread secundário. Esses tipos de retorno forçam o aplicativo a lidar com esse comportamento assíncrono.
- **Para notificar sobre o progresso.** Métodos como metadados ou sincronização de dados podem levar vários minutos para terminar. Da perspectiva do usuário, é muito útil ter uma noção do progresso.

Isso não significa que os aplicativos sejam forçados a usar RxJava em seu código: eles são forçados apenas a lidar com o comportamento assíncrono de alguns métodos. O SDK geralmente expõe a versão *de bloqueio* de cada método.

Por exemplo, a mesma consulta usando RxJava e AsyncTask:

*Using RxJava*

```java
d2.programModule().programs()
    .subscribeOn(Schedulers.io())
    .observeOn(AndroidSchedulers.mainThread())
    .get()
    .subscribe(programs -> {}); //List<Program>
```

*Using AsyncTask*

```java
new AsyncTask<Void, Void, List<Program>>() {
    protected List<Program> doInBackground() {
        return d2.programModule().programs().blockingGet();
    }

    protected void onPostExecute(List<Program> programs) {

    }
}.execute();
```

Acessar o banco de dados é demorado e é recomendado fazê-lo em um thread separado usando qualquer um dos
métodos. No entanto, os procedimentos que envolvem o acesso à API da web, como login, metadados ou download ou upload de dados **devem**
executado em um thread separado, caso contrário, o Android gerará um erro.

## Construção de consulta { #query_building } 

<!--DHIS2-SECTION-ID:query_building-->

Repositórios oferecem uma sintaxe de construtor com validação em tempo de compilação para acessar os recursos. Uma consulta típica é composta de alguns modificadores (filtro, pedido, campos aninhados) e termina com uma acção (get, count, getPaged,...).

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

Repositórios expõem a lista de filtros disponíveis prefixados pela palavra-chave "por". A lista de operadores de filtro disponíveis para cada filtro depende do tipo de valor do filtro: por exemplo, um tipo de valor `Data` oferecerá operadores como` depois`, `antes`,` inPeriods`, enquanto um tipo de valor `Booleano` oferecer `isFalse` ou` isTrue`.

Vários filtros podem ser anexados à mesma consulta em qualquer ordem. Os filtros são unidos globalmente usando o operador "AND". Isso significa que uma consulta como

```java
d2.eventModule().events()
    .byOrganisationUnitUid().eq("DiszpKrYNg8")
    .byEventDate().after(Date("2019-05-05"))
    ...
```

retornará os eventos atribuídos ao orgunit "DiszpKrYNg8" ** AND ** cujo eventDate é posterior a "2019-05-05".

### Ordenar por { #order_by } 

<!--DHIS2-SECTION-ID:order_by-->

Os modificadores de pedido são prefixados pela palavra-chave "orderBy".

Vários modificadores "orderBy" podem ser anexados à mesma consulta. A ordem dos modificadores "orderBy" na consulta determina a prioridade do pedido. Isso significa que uma consulta como

```java
d2.eventModule().events()
    .orderByEventDate(DESC)
    .orderByLastUpdated(DESC)
    ...
```

ordenará pelo descendente EventDate em primeiro lugar e, em seguida, pelo descendente LastUpdated.

### Incluir campos aninhados { #nested_fields } 

<!--DHIS2-SECTION-ID:nested_fields-->

Os repositórios retornam classes que não são uma correspondência exata das tabelas do banco de dados: eles são objetos mais complexos que podem incluir algumas propriedades obtidas de outras tabelas. Por exemplo, a classe `Event` tem uma propriedade chamada` trackedEntityDataValues` que inclui uma lista de TrackedEntityDataValues. O principal motivo para escolher esse tipo de objeto é absorver a complexidade de lidar com tabelas de links para que o aplicativo não precise se preocupar com a construção de links entre objetos.

Devido a problemas de desempenho, esse tipo de propriedade não é incluído por padrão: elas devem ser consultadas explicitamente. Nos repositórios, as propriedades que não são incluídas por padrão e precisam ser consultadas são prefixadas pela palavra-chave "com".

Várias propriedades podem ser anexadas à mesma consulta em qualquer ordem. Por exemplo, uma consulta como

```java
d2.programModule().programs()
    .withTrackedEntityType()
    ...
```

retornará um objecto aninhado `TrackedEntityType`.

## Ajudantes { #helpers } 

<!--DHIS2-SECTION-ID:helpers-->

O SDK inclui alguns auxiliares no pacote `org.hisp.dhis.android.core.arch.helpers`. Eles podem ser facilmente encontrados no Android Studio pesquisando `Helper` nos nomes das classes. Eles incluem alguns métodos úteis para realizar operações comuns:

- `AccessHelper`: relacionado ao objeto de acesso (configurações de compartilhamento).
- `CollectionsHelper`: operações comuns para coleções.
- `CoordinateHelper`,` GeometryHelper`: manipulação de dados geoespaciais.
- `FileResizeHelper`,` FileResourceDirectoryHelper`: manipulação de recursos de arquivo.
- `UidsHelper`: operações comuns para coleções de objetos com uid.
- `UserHelper`: operações relacionadas à autenticação do usuário.

## Lista de Módulos { #module_list } 

<!--DHIS2-SECTION-ID:module_list-->

Módulos do sistema:

- importModule
- módulo de manutenção
- systemInfoModule
- settingModule
- wipeModule

Módulos de bloco grande:

- metadataModule
- aggregatedDataModule

Módulos de concreto:

- categoryModule
- constantModule
- dataElementModule
- dataSetModule
- dataValueModule
- módulo de inscrição
- eventModule
- fileResourceModule
- indicadorModule
- legendSetModule
- noteModule
- organisationUnitModule
- optionModule
- periodModule
- programModule
- relacionamentoModule
- smsModule
- trackedEntityModule
- userModule
- validationModule


