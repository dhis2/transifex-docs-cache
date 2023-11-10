---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/workflow.md" 
---
# Fluxo de trabalho { #workflow }

<!--DHIS2-SECTION-ID:workflow-->

ACtualmente, o SDK é principalmente orientado para construir aplicativos que funcionam em modo offline. Resumindo, o SDK mantém uma instância de banco de dados local que é usada para fazer o trabalho localmente (criar formulários, gerenciar dados, ...). Quando solicitado pelo cliente, este banco de dados local é sincronizado com o servidor.

Um fluxo de trabalho típico seria assim:

1. **Conecte-se**
2. **Metadados de sincronização:** o SDK baixa um subconjunto dos metadados do servidor para que esteja disponível para uso a qualquer momento. A sincronização de metadados é totalmente dependente do usuário (consulte [Sincronização] (#sincronização de metadados) para obter mais detalhes)
3. **Baixar dados:** se deseja ter os dados existentes disponíveis no dispositivo, mesmo quando offline, pode baixar e salvar o rastreador existente e dados agregados no dispositivo.
4. **Faça o trabalho:** neste ponto, o aplicativo é capaz de criar os formulários de entrada de dados e mostrar alguns dados existentes. Em seguida, o usuário pode editar/excluir/actualizar os dados.
5. **Carregar dados:** de vez em quando, o trabalho realizado na instância do banco de dados local é enviado ao servidor.
6. **Sincronizar metadados:** é recomendado sincronizar metadados com bastante frequência para detectar mudanças na configuração de metadados.

## Login/Logout { #login_logout }

<!--DHIS2-SECTION-ID:login_logout-->

Antes de interagir com o servidor, é necessário fazer o login na instância DHIS 2. Actualmente, o SDK suporta apenas um par "usuário - servidor" simultaneamente. Isso significa que apenas um usuário pode ser autenticado em apenas um servidor ao mesmo tempo.

```java
d2.userModule (). logIn (nome de usuário, senha, serverUrl)

d2.userModule (). logOut ()
```

Após um logout, o SDK rastreia o último usuário conectado para poder diferenciar os usuários recorrentes dos novos. Ele também mantém um hash das credenciais do usuário para autenticar o usuário, mesmo quando não há conectividade. Dito isso, o método de login irá:

- Se já existir um usuário autenticado: lance um erro.
- Caso contrário, se *Online*:
  - Tente **login online**: o SDK enviará o nome de usuário e a senha para a API, que determinará se estão corretos. Se bem-sucedido:
        - Se nenhum banco de dados existir: crie um novo banco de dados com valor de criptografia do servidor.
        - Se o banco de dados para outro [serverUrl, usuário] existir, exclua-o e crie um novo banco de dados com valor de criptografia do servidor. Os dados não sincronizados do usuário conectado anteriormente serão perdidos permanentemente.
        - Se o banco de dados para o par [serverUrl, usuário] atual existir, abra o banco de dados e criptografe ou descriptografe o banco de dados se o status da criptografia tiver mudado no servidor.
  - Se a conta do usuário foi desabilitada no servidor: exclua o banco de dados e acione um erro.
- Caso contrário, se *Off-lin *:
  - Se o par [serverUrl, usuário] foi o último autenticado:
    - Tente **login offline**: o SDK verificará se as credenciais são as mesmas fornecidas por último, que foram validadas anteriormente pela API.
  - Se o par [serverUrl, usuário] não foi o último autenticado: lance um erro

Chamar métodos de módulo ou repositório antes de um login bem-sucedido ou após um logout resultará em erros de "Banco de dados não criado".

O método de logout remove as credenciais do usuário, portanto, um novo login é necessário antes de qualquer interação com o servidor. Metadados e dados são preservados para que o usuário possa fazer logout / login sem perder nenhuma informação.

## Sincronização de metadados { #metadata_synchronization }

<!--DHIS2-SECTION-ID:metadata_synchronization-->

A sincronização de metadados geralmente é a primeira etapa após o login. Ele busca e persiste os metadados necessários para o usuário actual. Para iniciar a sincronização de metadados, devemos executar:

```java
d2.metadataModule (). download ();
```

Para economizar uso de largura de banda e espaço de armazenamento, o SDK não sincroniza todos os metadados no servidor, mas um subconjunto. Este subconjunto é definido como os metadados exigidos pelo usuário para realizar tarefas de entrada de dados: renderizar programas e conjuntos de dados, executar regras de programa, avaliar indicadores de programa em linha, etc.

Com base nisso, a sincronização de metadados inclui os seguintes elementos:

|   Elemento             |   Condição ou escopo |
|-----------------------|-------------|
| Informação do sistema           | Tudo |
| Configurações de sistema       | KeyFlag, KeyStyle |
| Configurações do Usuário         | KeyDbLocale, KeyUiLocale |
| Do utilizador                  | Apenas usuário autenticado |
| Papel do usuário              | Funções atribuídas ao usuário autenticado |
| Autoridade             | Autoridades atribuídas ao usuário autenticado |
| Programa               | Programas aos quais o usuário tem (pelo menos) acesso de leitura aos dados e que são atribuídos a qualquer orgunit visível pelo usuário |
| RelationshipTypes     | Tudo |
| OptionGroups          | Somente se o servidor for maior que 2.29 |
| DataSet               | DataSets aos quais o usuário tem (pelo menos) acesso de leitura de dados e que são atribuídos a qualquer orgunit visível pelo usuário |
| Regras de validação      | Regras de validação associadas aos dataSets |
| Indicadores            | Indicadores atribuídos a conjuntos de dados baixados |
| OrganisationUnit      | OrganisationUnits no escopo CAPTURE ou SEARCH (descendentes incluídos) |
| OrganisationUnitGroup | Grupos atribuídos a unidades organizacionais baixadas |
| OrganisationUnitLevel | Tudo |
| Constante              | Tudo |
| Metadados do módulo SMS   | Somente se o módulo SMS estiver habilitado |

No caso de Programas e DataSets, a sincronização de metadados inclui todos os metadados relacionados a eles: estágios, seções, dataElements, opções, categorias, etc. Aqueles elementos que não estão relacionados a nenhum Programa ou DataSet não estão incluídos.

### Configurações corrompidas { #corrupted-configurations }

Essa sincronização parcial de metadados pode expor problemas de configuração incorreta do lado do servidor. Por exemplo, um ProgramRuleVariable apontando para um DataElement que não pertence mais ao programa. Devido ao uso de restrições no nível do banco de dados, essa configuração incorreta aparecerá como um erro de chave estrangeira.

O SDK não falha na sincronização, mas armazena os erros em uma tabela para inspeção. Esses erros podem ser acessados por:

```java
d2.maintenanceModule (). ForeignKeyViolations ()
```

## Estados de dados { #data_states }

<!--DHIS2-SECTION-ID:data_states-->

Objectos de dados têm uma propriedade `state` somente leitura que indica o estado actual do objecto em termos de sincronização com o servidor. Este estado é mantido pelo SDK.

Os estados possíveis são:

- **SINCRONIZADO**. O elemento é sincronizado com o servidor. Não há mudanças locais para este valor.
- **TO_POST**. Dados criados localmente que ainda não existem no servidor.
- **TO_UPDATE**. Dados modificados localmente que existem no servidor.
- **ENVIANDO**. Os dados estão sendo carregados. Se for modificado antes de receber qualquer resposta do servidor, seu estado volta para `TO_UPDATE`. Quando chega a resposta do servidor, seu estado não muda para `SYNCED`, mas permanece em` TO_UPDATE` para indicar que há mudanças locais.
- **SENT_BY_SMS**. Os dados são enviados por sms e não há resposta do servidor ainda. Alguns servidores não têm a capacidade de enviar uma resposta, então este estado significa que os dados foram enviados, mas não sabemos se foram importados corretamente no servidor ou não.
- **SYNCED_BY_SMS**. Os dados são enviados por sms e há uma resposta bem-sucedida do servidor.
- **ERRO**. Dados que receberam um erro do servidor após o último upload.
- **AVISO**. Dados que receberam um aviso do servidor após o último upload.

Além disso, em `TrackedEntityInstance` podemos ter:

- **RELAÇÃO**. Este TrackedEntityInstance foi baixado com o único propósito de cumprir um relacionamento com outro TEI. Este TEI `RELATIONSHIP` contém apenas informações básicas (uid, tipo, etc) e a lista de TrackedEntityAttributes para poder imprimir informações significativas sobre o relacionamento. Outros dados, como inscrições, eventos ou relacionamentos não são baixados para este TEI. Além disso, este TEI não pode ser modificado ou carregado no servidor.

## Dados do rastreador { #tracker_data }

<!--DHIS2-SECTION-ID:tracker_data-->

### Download de dados do rastreador { #tracker-data-download }

> **Importante**
>
> Consulte a seção [Settings App] (#settings_app) para saber como esse aplicativo pode ser usado para controlar os parâmetros de sincronização.

Por padrão, o SDK baixa apenas TrackedEntityInstances and Events
que estão localizados no escopo de captura do usuário, mas também é possível
baixe TrackedEntityInstances no escopo de pesquisa.

O módulo de entidade rastreada contém o
`TrackedEntityInstanceDownloader`. O downloader segue um construtor
padrão que permite o download de instâncias de entidades rastreadas, filtrando por
**parâmetros diferentes**, bem como definir alguns **limites**. O mesmo
o comportamento pode ser encontrado no módulo de eventos para eventos.

O downloader rastreia o último download bem-sucedido para evitar
baixando dados não modificados. Ele faz uso de paginação com o melhor esforço
estratégia: no caso de uma página falhar ao ser baixada ou persistida, ela é
pulado e continuará com as próximas páginas.

Este é um exemplo de como pode ser usado.

```java
d2.trackedEntityModule (). trackedEntityInstanceDownloader ()
    . [filtros]
    . [limites]
    .download()
```

```java
d2.eventModule (). eventDownloader ()
    . [filtros]
    . [limites]
    .download()
```

Actualmente, é possível especificar os próximos filtros:

- `byProgramUid ()`. Filtra por uid de programa e baixa o não sincronizado
  objectos dentro do programa.
- `byUid ()`. Filtra pelo uid da instância da entidade rastreada e baixa um
  objecto único. Este filtro pode ser usado para baixar a entidade rastreada
  instâncias encontradas dentro do escopo da pesquisa. (Apenas para entidade rastreada
  instâncias).

O downloader também permite limitar o número de objectos baixados.
Esses limites também podem ser combinados entre si.

- `limit ()`. Limite o número máximo de objetos para download.
- `limitByProgram ()`. Pegue o limite estabelecido e aplique-o a cada
  programa. O número de objectos que serão baixados será o único
  obtido multiplicando o limite definido pelo número de programas do usuário.
- `limitByOrgunit ()`. Pegue o limite estabelecido e aplique-o para cada
  unidade organizacional. O número de objetos que serão baixados
  ser aquele obtido pela multiplicação do limite definido pelo número de usuários
  unidades organizacionais.

O próximo trecho de código mostra um exemplo do
Uso de TrackedEntityInstanceDownloader.

```java
d2.trackedEntityModule (). trackedEntityInstanceDownloader ()
    .byProgramUid ("program-uid")
    .limitByOrgunit (true)
    .limitByProgram (true)
    .limit (50)
    .download()
```

Além disso, se quiser que as imagens associadas aos valores dos dados `Image` estejam disponíveis para download no dispositivo, deve fazer o download. Veja a secção [*Lidando com FileResources*] (#transactions-with-fileresources) para mais detalhes.

### Pesquisa de dados do rastreador { #tracker-data-search }

DHIS2 tem uma funcionalidade para filtrar TrackedEntityInstances por relacionados
propriedades, como atributos, unidades de organização, programas ou inscrição
datas. O Sdk fornece o `TrackedEntityInstanceQueryCollectionRepository`
com métodos que permitem o download de entidade rastreada
instâncias dentro do escopo da pesquisa. Ele pode ser encontrado dentro do módulo de instância de entidade rastreada.

A consulta de instância de entidade rastreada é uma ferramenta poderosa que segue um
padrão de construtor e permite o download de instâncias de entidade rastreadas
filtrando por **parâmetros diferentes**.

```java
d2.trackedEntityModule (). trackedEntityInstanceQuery ()
    . [modo de repositório]
    . [filtros]
    .pegue()
```

A fonte de onde os TEIs são recuperados é definida pelo **modo de repositório**.
Estes são os diferentes modos de repositório disponíveis:

- `onlineOnly ()`. Apenas TrackedEntityInstances provenientes do servidor são
  retornado na lista. É necessária uma conexão com a Internet para usar este modo.
- `offlineOnly ()`. Apenas TrackedEntityInstances vindo do local
  banco de dados são retornados na lista.
- `onlineFirst ()`. TrackedEntityInstances provenientes do servidor são
  voltou em primeiro lugar. Assim que não houver mais resultados online,
  continua com TrackedEntityInstances no banco de dados local. Internet
  é necessária uma conexão para usar este modo.
- `offlineFirst ()`. TrackedEntityInstances provenientes do banco de dados local
  são devolvidos em primeiro lugar. Assim que não houver mais resultados, ele continua
  com TrackedEntityInstances vindo do servidor. Este método pode
  acelerar o carregamento inicial. É necessária conexão com a Internet para usar este
  modo.

Este repositório segue a mesma sintaxe de outros repositórios.
Além disso, o repositório oferece diferentes estratégias para buscar dados:

- `byAttribute ()`. Este método adiciona um filtro de * atributo * à consulta.
  Se este método for chamado várias vezes, as condições serão anexadas com um AND
  conector. Por exemplo:

  ```java
  d2.trackedEntityModule().trackedEntityInstanceQuery()
      .byAttribute("uid1").eq("value1")
      .byAttribute("uid2").eq("value2")
      .get()
  ```

  Isso significa que a instância deve ter o atributo `uid1` com valor
  Atributo `valor1` **AND**` uid2` com o valor `valor2`.

- `byFilter ()`. Este método adiciona um *filtro* à consulta. Se este
  método é chamado várias vezes, as condições são anexadas com um AND
  conector. Por exemplo:

  ```java
  d2.trackedEntityModule().trackedEntityInstanceQuery()
      .byFilter("uid1").eq("value1")
      .byFilter("uid2").eq("value2")
      .get()
  ```

  Isso significa que a instância deve ter o atributo `uid1` com valor
  Atributo `valor1` **AND**` uid2` com o valor `valor2`.

- `byQuery ()`. Pesquisar instâncias de entidades rastreadas com **qualquer** atributo
  correspondendo à consulta.
- `byProgram ()`. Filtrar por programa de inscrição. Apenas um programa pode ser
  Especificadas.
- `byOrgUnits ()`. Filtrar por unidades de organização de instância de entidade rastreada.
  Mais de uma unidade organizacional pode ser especificada.
- `byOrgUnitMode ()`. Defina o modo da unidade de organização. O possível
  os modos são os próximos:
  - **SELECIONADO**. Apenas unidades especificadas.
  - **CRIANÇAS**. Filhos imediatos de unidades especificadas, incluindo
    unidades especificadas.
  - ** DESCENDENTES **. Todas as unidades na sub-hierarquia de unidades especificadas,
    incluindo unidades especificadas.
  - **ACESSÍVEL**. Todas as unidades organizacionais acessíveis ao usuário
    (escopo de pesquisa).
  - **ALL**. Todas as unidades do sistema. Requer autoridade.
- `byProgramStartDate ()`. Defina uma data de início da inscrição. É só
  aplica-se se um programa tiver sido especificado.
- `byProgramEndDate ()`. Defina uma data de término da inscrição. Só se aplica
  se um programa foi especificado.
- `byTrackedEntityType ()`. Filtrar por TrackedEntityType. Apenas um tipo
  pode ser especificado.
- `byIncludeDeleted ()`. Incluir ou não excluir entidade rastreada
  instâncias. Actualmente, este filtro se aplica apenas a **offline**
  instâncias.
- `byStates ()`. Filtrar por status de sincronização. Usar este filtro força
  Modo **offline apenas**.

Exemplo:

```java
d2.trackedEntityModule().trackedEntityInstanceQuery()
                .byOrgUnits().eq("orgunitUid")
                .byOrgUnitMode().eq(OrganisationUnitMode.DESCENDANTS)
                .byProgram().eq("programUid")
                .byAttribute("attributeUid").like("value")
                .offlineFirst()
```

> **Importante**
>
> TrackedEntityInstances recuperados usando este repositório não são persistentes no banco de dados. É possível
para baixá-los totalmente usando o filtro `byUid ()` do `TrackedEntityInstanceDownloader` dentro do módulo de instância de entidade rastreada.

[//]: # (Include glass protected download)

### Gravação de dados do rastreador { #tracker-data-write } 

Em geral, existem dois casos diferentes para gerenciar a criação/edição/exclusão de dados: o caso em que o objeto é identificável (ou seja, possui uma propriedade `uid`) e o caso em que o objecto não é identificável.

**Objectos identificáveis** (TrackedEntityInstance, Enrollment, Event). Esses repositórios têm um método `uid ()` que dá acesso a métodos de edição para um único objeto. Caso o objecto ainda não exista, é necessário criá-lo primeiro. Um fluxo de trabalho típico para criar/editar um objecto seria:

- Use a classe `CreateProjection` para adicionar uma nova instância no repositório.
- Salve o uid retornado por este método.
- Use o método `uid ()` com o uid anterior para obter acesso aos métodos de edição.

E no código isso se pareceria com:

```java
String eventUid = d2.eventModule().events().add(
    EventCreateProjection.create("enrollment", "program", "programStage", "orgUnit", "attCombo"));

d2.eventModule().events().uid(eventUid).setStatus(COMPLETED);
```

**Objectos não identificáveis** (TrackedEntityAttributeValue, TrackedEntityDataValue). Esses repositórios têm um método `value ()` que dá acesso a métodos de edição para um único objeto. Os parâmetros aceitos por esse método são os parâmetros que identificam um valor de forma inequívoca.

Por exemplo, escrever um TrackedEntityDataValue seria assim:

```java
d2.trackedEntityModule().trackedEntityDataValues().value(eventUid, dataElementid).set(“5”);
```

Os valores de dados do tipo `Image` envolvem uma etapa adicional para criar/actualizar/ler o recurso de arquivo associado. Mais detalhes na seção [*Lidando com Recursos de Arquivos*] (#lidar com fontes de arquivos) abaixo.

### Upload de dados do rastreador { #tracker-data-upload } 

Os repositórios TrackedEntityInstance e Event têm um método `upload ()` para enviar dados do Tracker e dados do evento (sem registro), respectivamente. Se o escopo do repositório foi reduzido por métodos de filtro, apenas os objectos filtrados serão carregados.

```java
d2.( trackedEntityModule() | eventModule() )
    .[ filters ]
    .upload();
```

Dados cujo estado é `ERROR` ou` WARNING` não podem ser carregados. É necessário resolver os conflitos antes de tentar um novo upload: isso significa fazer uma modificação nos dados problemáticos, o que força seu estado de volta para `TO_UPDATE`.

#### Conflitos de rastreador { #tracker-conflicts } 

A resposta do servidor é analisada para garantir que os dados foram carregados corretamente para o servidor. Caso a resposta do servidor inclua conflitos de importação, esses conflitos são armazenados no banco de dados, para que o aplicativo possa verificá-los e tomar uma ação para resolvê-los.

```java
d2.importModule().trackerImportConflicts()
```

Os conflitos vinculados a TrackedEntityInstance, Enrollment ou Evento são removidos automaticamente após um upload bem-sucedido do objeto.

O SDK tenta identificar o conflito dataElement ou atributo analisando a resposta do servidor. Nesse caso, ele também armazena o valor do elemento quando o conflito ocorreu para que o aplicativo possa destacar o elemento no formulário quando o valor ainda não foi fixado.

### Dados do rastreador: valores reservados { #tracker-data-reserved-values } 

Atributos de entidade rastreados configurados como **únicos** e **gerados automaticamente** são gerados pelo servidor seguindo um padrão definido pelo usuário. Esses valores só podem ser gerados pelo servidor, o que significa que precisamos reservá-los com antecedência para que possamos utilizá-los ao operar offline.

O aplicativo é responsável por reservar os valores gerados antes de ficar offline. Isso pode ser acionado por:

```java
// Reserve values for all the unique and automatically generated trackedEntityAttributes.
d2.trackedEntityModule().reservedValueManager().downloadAllReservedValues(numValuesToFillUp)

// Reserve values for a particular trackedEntityAttribute.
d2.trackedEntityModule().reservedValueManager().downloadReservedValues("attributeUid", numValuesToFillUp)
```

Dependendo de quanto tempo o aplicativo espera ficar offline, ele pode decidir a quantidade de valores a reservar. Caso o padrão de atributo dependa do código orgunit, o SDK reservará valores para todos os orgunits relevantes. Mais detalhes sobre a lógica em Javadoc.

Os valores reservados podem ser obtidos por:

```java
d2.trackedEntityModule().reservedValueManager().getValue("attributeUid", "orgunitUid")
```

### Dados do rastreador: relacionamentos { #tracker-data-relationships } 

Actualmente, o SDK oferece suporte apenas a relacionamentos de TEI para TEI. Eles são acessados usando o módulo de relacionamentos.

Relacionamentos de consulta associados a um TEI.

```java
d2.relationshipModule().relationships().getByItem(
    RelationshipHelper.teiItem("trackedEntityInstanceUid")
)
```

No mesmo módulo, pode criar novos relacionamentos usando este método:

```java
Relationship relationship = RelationshipHelper.teiToTeiRelationship("fromTEIUid", "toTEIUid", "relationshipTypeUid");

d2.relationshipModule().relationships().add(relationship);
```

Se o trackedEntityInstance relacionado ainda não existir e houver valores de atributos que devem ser herdados, pode usar o método a seguir para herdar valores de atributos de um TEI para outro no contexto de um determinado programa. Apenas os atributos marcados como `herdar` serão herdados.

```java
d2.trackedEntityModule().trackedEntityInstanceService()
    .inheritAttributes("fromTeiUid", "toTeiUid", "programUid");
```

## Dados agregados { #aggregated_data } 

<!--DHIS2-SECTION-ID:aggregated_data-->

### Download de dados agregados { #aggregated-data-download } 

> **Important**
>
> Consulte a seção [Settings App] (# settings_app) para saber como esse aplicativo pode ser usado para controlar os parâmetros de sincronização.

```java
d2.aggregatedModule().data().download()
```

Por padrão, o SDK baixa **valores de dados agregados**, **conjunto de dados
valores completos de registro** e **aprovações** correspondentes a:

- **DataSets**: todos os dataSets disponíveis (aqueles que o usuário leu pelo menos
  acesso de dados para).
- **Unidades Organizacionais**: escopo de captura.
- **Períodos**: todos os períodos disponíveis, o que significa pelo menos:
  - Dias: últimos 60 dias.
  - Semanas: últimas 13 semanas (incluindo variantes do dia inicial).
  - Quinzenal: últimas 13 semanas.
  - Mensal: últimos 12 meses.
  - Bimestral: últimos 6 bi-meses.
  - Trimestres: últimos 5 trimestres.
  - Semestral: últimos 5 semestrais (começando em janeiro e abril).
  - Anual: últimos 5 anos (incluindo variantes do exercício).

  Além disso, se algum conjunto de dados permitir a entrada de dados para **períodos futuros**,
  o SDK fará o download dos dados para esses períodos abertos e os armazenará.

O SDK também mantém registro do último download bem-sucedido para
evite baixar dados não modificados do servidor.

No download de **aprovações de dados**, fluxo de trabalho e opção de atributo
identificadores de combinação serão considerados além do
unidades organizacionais e períodos. Os diferentes estados possíveis para os dados
aprovação são:

- `NÃO APROVÁVEL`. A aprovação de dados não se aplica a esta seleção. (Dados
  não é *aprovado* nem *não aprovado*).
- `UNAPPROVED_WAITING`. Os dados poderiam ser aprovados para esta seleção, mas
  está esperando por alguma aprovação de nível inferior antes de estar pronto para ser
  aprovado.
- `UNAPPROVED_ELSEWHERE`. Os dados não foram aprovados e estão esperando por
  aprovação em outro lugar (não pode ser aprovado aqui).
- `UNAPPROVED_READY`. Os dados não foram aprovados e estão prontos para serem aprovados
  para esta seleção.
- `UNAPPROVED_ABOVE`. Os dados não foram aprovados acima.
- `APPROVED_HERE`. Os dados foram aprovados e foram aprovados aqui (e podem ser
  não aprovado aqui).
- `APPROVED_ELSEWHERE`. Os dados foram aprovados, mas não foram aprovados aqui (então
  não pode ser reprovado aqui).
- `APPROVED_ABOVE`. Os dados são aprovados acima.
- `ACCEPTED_HERE`. Os dados são aprovados e aceitos aqui (e poderiam ser
  não aprovado aqui).
- `ACCEPTED_ELSEWHERE`. Os dados são aprovados e aceitos, mas em outro lugar.

As aprovações de dados são baixadas apenas para versões superiores a 2.29.

### Gravação de dados agregados { #aggregated-data-write } 

#### Períodos { #periods } 

Para gravar valores de dados ou registros completos de conjuntos de dados, é obrigatório fornecer um id de período. Os períodos são armazenados em uma tabela no banco de dados e
os ids de período fornecidos já devem estar presentes nessa tabela, caso contrário, um erro de chave estrangeira será gerado. Para evitar essa situação, o `PeriodHelper` é
exposto dentro do `PeriodModule`. Antes de adicionar dados agregados relacionados a um dataSet, o seguinte método deve ser chamado:

```java
Single<List<Period>> periods = d2.periodModule().periodHelper().getPeriodsForDataSet("dataSetUid");
```

Isso irá garantir que:
1. O aplicativo escolherá um dos períodos fornecidos, evitando períodos malformados ou incorretos.
2. O aplicativo só poderá escolher os períodos futuros definidos pelo campo `DataSet.openFuturePeriods`.
3. O aplicativo só poderá escolher os períodos passados definidos com base nos limites declarados na seção Download de Dados Agregados.

#### Valor de dados { #data-value } 

DataValueCollectionRepository tem um método `value ()` que dá acesso aos métodos de edição. Os parâmetros aceitos por esse método são os parâmetros que identificam um valor de forma inequívoca.

```java
DataValueObjectRepository valueRepository = d2.dataValueModule().dataValues()
    .value("periodId", "orgunitId", "dataElementId", "categoryOptionComboId", "attributeOptionComboId");

valueRepository.set("value")
```

#### Registro completo do conjunto de dados { #data-set-complete-registration } 

O Sdk fornece dentro do módulo de conjunto de dados um repositório de coleta para
registros completos do conjunto de dados. Este repositório contém métodos para adicionar
novas conclusões e excluí-las.

Para adicionar um novo registro completo do conjunto de dados está disponível um `add ()`
método:

```java
d2.dataSetModule().dataSetCompleteRegistrations()
    .add(dataSetCompleteRegistration);
```

Para removê-los do banco de dados, o repositório tem um `valor ()`
método que dá acesso aos métodos de exclusão (`delete ()` e
`deleteIfExist ()`). Os parâmetros aceitos por este método são os
parâmetros que identificam inequivocamente o conjunto de dados completo
cadastro.

```java
d2.dataSetModule().dataSetCompleteRegistrations()
    .value("periodId", "orgunitId", "dataSetUid","attributeOptionCombo")
    .delete()
```

### Upload de dados agregados { #aggregated-data-upload } 

DataValueCollectionRepository tem um método `upload ()` para fazer upload de valores de dados agregados.

```java
d2.dataValueModule().dataValues().upload();
```

### Instâncias de DataSet { #dataset-instances } 

Um DataSetInstance no SDK é uma representação útil dos dados agregados existentes. Um DataSetInstance representa uma combinação única de DataSet - Period - Orgunit - AttributeOptionCombo e inclui informações extras como estado de sincronização, contagem de valor ou displayName para algumas propriedades.

```java
d2.dataSetModule().dataSetInstances()
    .[ filters ]
    .get()

// For example
d2.dataSetModule().dataSetInstances()
    .byDataSetUid().eq("datasetUid")
    .byOrganisationUnitUid().eq("orgunitUid")
    .byPeriod().in("201901", "201902")
    .get();
```

Se só precisa de uma visão geral de alto nível do status dos dados agregados, pode usar o repositório `DataSetInstanceSummary`. Ele aceita os mesmos filtros e retorna uma contagem de `DataSetInstance` para cada combinação.

## Lidando com FileResources { #file_resources } 

<!--DHIS2-SECTION-ID:file_resources-->

O SDK oferece um módulo (o `FileResourceModule`) e dois auxiliares (o` FileResourceDirectoryHelper` e `FileResizerHelper`) que permitem trabalhar com arquivos.

### Módulo de recursos de arquivo { #file-resources-module } 

Este módulo contém métodos para baixar os recursos de arquivo associados aos dados baixados e o repositório de coleta de recursos de arquivo do banco de dados.

- **Download de recursos de arquivo**.
O método `download ()` pesquisará os valores de atributo de entidade rastreados e valores de dados de entidade rastreados cujo tipo de atributo de entidade rastreado e tipo de elemento de dados são do tipo imagem e cujo recurso de arquivo não foi baixado anteriormente e o método irá baixar os recursos de arquivo associados.

  ```java
  d2.fileResourceModule().download();
  ```

  Depois de baixar os arquivos, pode obter os diferentes recursos de arquivo baixados por meio do repositório.

- **Repositório de coleta de recursos de arquivo**.
Através deste repositório é possível solicitar arquivos, salvar novos e enviá-los ao servidor.

  - **Obter**. Ele se comporta de maneira semelhante a qualquer outro repositório Sdk. Ele permite obter coleções aplicando diferentes filtros, se desejado.

    ```java
    d2.fileResourceModule().fileResources()
        .[ filters ]
        .get()
    ```

  - **Adicionar**. Para salvar um arquivo, deve adicioná-lo usando o método `add ()` do repositório, fornecendo um objecto do tipo `Arquivo`. O método `add ()` retornará o uid que foi gerado ao adicionar o arquivo. Este uid deve ser usado para actualizar o valor do atributo da entidade rastreada ou o valor dos dados da entidade rastreada associado ao recurso de arquivo.

    ```java
    d2.fileResourceModule().fileResources()
        .add(file); // Single<String> The fileResource uid
    ```

  - **Envio**. Chamar o método `upload ()` irá disparar uma série de chamadas sucessivas nas quais todos os arquivos não sincronizados serão enviados ao servidor. Após cada upload, a resposta do servidor será processada. O servidor fornecerá um novo uid para o recurso de arquivo e o Sdk renomeará automaticamente o arquivo e actualizará o objecto `FileResource` e os valores de atributo de entidade rastreados ou valores de dados de entidade rastreados associados a ele.

    ```java
    d2.fileResourceModule().fileResources()
        .upload()
    ```

### Ajudante de redimensionamento de arquivo { #file-resizer-helper } 

O Sdk fornece um auxiliar para redimensionar arquivos de imagem (`FileResizerHelper`). Este auxiliar contém um método `resizeFile ()` que aceita o arquivo que deseja reduzir e a dimensão para a qual deseja reduzi-lo.

As dimensões possíveis estão na tabela a seguir.

| Pequeno | Médio | ampla  |
|-------|--------|--------|
| 256px | 512px  | 1024px |

O ajudante pega o arquivo, mede a altura e largura da imagem, determina qual dos dois lados é maior e reduz o maior dos lados para a dimensão dada e o outro lado é dimensionado para seu tamanho proporcional. **O dimensionamento da imagem sempre manterá as proporções**.

Caso a última imagem seja menor que a dimensão para a qual deseja redimensioná-la, o mesmo arquivo será devolvido sem ser modificado.

O método `resizeFile ()` retornará um novo arquivo localizado no mesmo diretório pai do arquivo a ser redimensionado com o nome `resized-DIMENSION-` + o nome do arquivo sem redimensionar.

### Auxiliar de diretório de recursos de arquivo { #file-resource-directory-helper } 

A classe auxiliar `FileResourceDirectoryHelper` fornece dois métodos.

- `getFileResourceDirectory ()`. Este método retorna um objecto `File` cujo caminho aponta para o diretório` sdk_resources` onde o Sdk salvará os arquivos associados aos recursos do arquivo.

- `getFileCacheResourceDirectory ()`. Este método retorna um objecto `File` cujo caminho aponta para o diretório` sdk_cache_resources`. Este deve ser o local onde os arquivos voláteis são armazenados, como fotos da câmera ou imagens a serem redimensionadas. Como o diretório está contido no diretório de cache, o Android pode excluir automaticamente os arquivos do diretório de cache quando o sistema está prestes a ficar sem memória. Os aplicativos de terceiros também podem excluir arquivos do diretório de cache. Até mesmo o usuário pode limpar manualmente o cache em Configurações. No entanto, o facto de o cache poder ser limpo nos métodos explicados acima não significa que o cache será limpo automaticamente; portanto, o cache precisará ser organizado de vez em quando de maneira proativa.


