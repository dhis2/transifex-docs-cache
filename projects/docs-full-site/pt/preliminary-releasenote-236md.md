# DHIS versão 2.36 Nota de Lançamento

Este documento destaca os principais recursos do lançamento inicial do DHIS2 versão 2.36. Esta versão é totalmente compatível com o DHIS2 [Android Capture App] (https://www.dhis2.org/android-2-4) versão 2.4.


## RECURSOS DE ANÁLISE

**Gráficos de dispersão:** O aplicativo visualizador de dados agora apresenta gráficos de dispersão. Isso permite que os utilizadores façam um gráfico das unidades organizacionais como pontos em relação a duas variáveis para um único período com gráficos de dispersão.

  - *Amplie* clicando e arrastando o cursor sobre uma área que deseja ampliar. Isso geralmente é necessário para ver mais detalhes em áreas onde muitas unidades organizacionais estão agrupadas.
  - *A detecção de outlier* pode ser feita usando um escore z padrão, escore z modificado ou um intervalo interquartil por meio do menu de opções. Uma linha limite extrema vertical (eixo y) e horizontal (eixo x) também pode ser aplicada. Endossado pela OMS, esta é uma maneira muito clara e poderosa de identificar valores discrepantes que geralmente representam problemas de qualidade de dados. Pode identificar os valores discrepantes com maior probabilidade de prejudicar as estatísticas nacionais usando a detecção de valores discrepantes em combinação com as linhas de limite X e Y extremas.

[Captura de tela 1] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_plot.png) | [Captura de tela 2] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_outlier_options.png) | [Captura de tela 3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_scatter_outlier_analysis.png) | [Docs]()

**Modo de apresentação do item do painel em tela inteira:** Expanda qualquer item do painel (gráfico, mapa ou tabela dinâmica) para o tamanho da tela inteira. Isso é ótimo para apresentar dados em reuniões virtuais ou presenciais diretamente do painel.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_fullscreen.png) | [Docs]()

**Legendas do gráfico de barras e colunas:** Altere a cor de uma barra ou coluna com base em uma legenda predefinida. Isso torna mais fácil destacar o desempenho inferior e superior com gráficos de barras e colunas.

[Captura de tela 1] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_legend_chart.png) | [Captura de tela 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_legend_options.png) | [Docs]()

**Aplicativo de painel otimizado para celular:** O aplicativo de painel da web DHIS 2 agora é mais otimizado para celular e pode ser usado em dispositivos móveis. Isso permite que use o poder dos painéis de seu dispositivo móvel. Agora pode levar seus painéis, verificá-los a qualquer momento e partilhar dados com quem precisar com a conveniência de seu telefone. O aplicativo adotou vários dos princípios de _Progressive Web Apps_ (PWA). O suporte offline para painéis virá em uma versão futura.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_mobile.png) | [Docs]()

**Mapas populacionais do Google Earth Engine:** Muitas instâncias DHIS2 sofrem por não ter dados populacionais precisos. Este recurso permite que crie mapas com dados do Google Earth Engine, incluindo as últimas estimativas de população _World Pop_. Pode aplicar uma camada limite para visualizar os valores populacionais, densidade por hectare e média por hectare para unidades organizacionais. Pode aplicar um buffer ao redor de uma instalação para ver a população que cai dentro do buffer. O conjunto de dados populacionais está disponível para desagregação por idade e sexo. Isso é útil em áreas onde os dados do censo são incompletos ou não confiáveis, por exemplo, para planejar campanhas de extensão e estimar o risco de transmissão de doenças.

[Captura de tela 1] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_1.png) | [Captura de tela 2] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_2.png) | [Captura de tela 3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/maps_population_3.png) | [Docs]()

**Pesquisa universal de itens de dados:** O aplicativo visualizador de dados agora oferece suporte à pesquisa de itens de dados em todos os tipos, tornando muito mais fácil encontrar os itens de dados que deseja em indicadores, elementos de dados, conjuntos de dados, elementos de dados de programas e indicadores de programas. Tudo o que precisa fazer é pesquisar o item de dados e todas as correspondências serão exibidas, independentemente do tipo de item de dados. Ainda pode restringir sua pesquisa a partir da seleção de tipo.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/visualizer_universal_search.png) | [Docs]()

**Configurações de filtro do painel:** Os proprietários do painel agora podem definir quais filtros disponibilizar para cada painel. Freqüentemente, existe um grande número de dimensões de dados e nem todas se aplicam aos dados em um painel específico. Isso torna difícil encontrar e selecionar dimensões de dados relevantes. Ao definir exatamente quais dimensões de dados ficam disponíveis para um painel, a experiência do utilizador é simplificada e tornada mais envolvente. Vá para _Editar_> _Configurações de filtro_ para selecionar os filtros.

[Captura de tela] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_filter_settings.png) | [Captura de tela 2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_filter_list.png) | [Docs]()

**Tipo de visualização para itens do painel:** Países e projetos trabalham duro para criar painéis que contam uma história específica, onde o tipo de visualização (mapas, gráficos ou tabelas) é cuidadosamente selecionado e otimizado. Nas versões anteriores, o utilizador pode alterar o tipo de visualização de cada item do painel para uma tabela, mapa ou gráfico. Em alguns casos, isso pode prejudicar a história cuidadosamente elaborada que o proprietário do painel está tentando comunicar. Novas configurações do sistema agora estão disponíveis na seção _Analytics_ do aplicativo de configurações para controlar se os utilizadores podem alternar o tipo de visualização, abrir itens no aplicativo visualizador, visualizar interpretações e visualizar em tela inteira.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/dashboard_system_settings.png) | [Docs]()


## RECURSOS DO TRACKER E DO EVENTO

**Melhorias de desempenho:** Um grande número de melhorias de desempenho foi incluído no 2.36 e há amplas melhorias no desempenho do rastreador, em particular em torno de otimizações de consulta de banco de dados. As melhorias estão levando a tempos de resposta mais baixos, consultas de banco de dados mais rápidas e menos consumo de memória. A maioria dessas atualizações foi aplicada às versões 2.34.4, 2.35.2 e 2.36.0. Implementações de DHIS2 em grande escala são aconselhadas a atualizar.

[Jira]()

**Funcionalidade do rastreador no aplicativo Capture:** O aplicativo de captura agora tem mais suporte para programas rastreadores do que antes. Os utilizadores agora serão capazes de listar e interagir com instâncias de entidades rastreadas da mesma forma que eventos, e terão acesso para pesquisar e registrar / inscrever instâncias de entidades rastreadas no próprio aplicativo Capture. Outras interações com inscrições e eventos em inscrições ainda ocorrerão em 2.36 no aplicativo Tracker Capture, mas a navegação entre os aplicativos acontecerá perfeitamente. Isso permitirá que o utilizador de entrada de dados acesse os dados do rastreador e do evento no mesmo lugar e tenha um fluxo de trabalho mais integrado.

[Captura de tela 1] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_list_tei.png) | [2] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_list_tei_filter.png) | [3] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_search_tei.png) | [4] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/capture_register_tei_and_enroll.png) | [Docs]() | [Jira]()

**Novo endpoint para importar dados do rastreador:** Uma nova API para dados do rastreador agora é lançada lado a lado com a API existente. A nova API foi reprojetada e reimplementada de baixo para cima com uma nova arquitetura. A nova implementação é mais sustentável e produz um potencial maior para aprimoramentos de desempenho do que era possível alcançar na base de código antiga. A nova API executará uma execução completa de regras de programa e permite a atribuição de campos do lado do servidor e validação de carga útil, além da funcionalidade existente para o envio de mensagens. A nova API vai substituir a existente nas versões posteriores do DHIS2, mas é lançada lado a lado neste momento para permitir que os desenvolvedores de aplicativos iniciem processos de integração.

[Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-5068)

**Novo endpoint para recuperar dados do tracker:** Uma nova API para recuperar dados do tracker foi lançada com o novo endpoint para importar dados do tracker. Esta nova API permite o download de dados do rastreador no mesmo formato do novo endpoint para importação de dados, tornando mais fácil a integração com este novo conjunto de serviços.

[Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-10093)

**Nova funcionalidade do indicador do programa:** Agora é possível construir expressões e filtros do indicador do programa com base no status do evento, usando a variável `V{event_status}`.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#program_indicator_functions_variables_operators) | [Jira](https://jira.dhis2.org/browse/DHIS2-10294)

**Nome completo mostrado nas notas** Na captura do rastreador, o nome completo agora é mostrado para o utilizador que inseriu uma nota / comentário. Anteriormente, apenas o nome de utilizador era mostrado. O nome completo é útil nos casos em que o nome de utilizador não é legível.

[Captura de tela]() | [Jira](https://jira.dhis2.org/browse/DHIS2-9574)

**Entrada de dados apenas pelo teclado:** Na captura do rastreador, os dados agora podem ser inseridos sem o uso de um mouse. Agora é possível pesquisar e selecionar opções em conjuntos de opções e campos booleanos usando o teclado.

[Jira](https://jira.dhis2.org/browse/DHIS2-5902)

## RECURSOS DA PLATAFORMA

**Detecção de valores discrepantes:** Uma detecção de valores discrepantes nova e aprimorada está disponível no aplicativo de qualidade de dados. Os valores atípicos agora são classificados e os valores atípicos mais significativos são retornados primeiro, tornando muito mais fácil encontrar e corrigir os valores atípicos que afetam muito a análise de dados. Anteriormente, os valores discrepantes eram retornados sem um pedido. Outliers são classificados por *distância absoluta da média*. O *escore z* do valor, bem como a média, desvio padrão, mínimo e máximo estão disponíveis na resposta.

[Captura de tela 1] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/outlier_selection.png) | [Captura de tela 2] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/outlier_detection.png) | [Documentos do utilizador]() |[API docs]()

**OpenID Connect:** O suporte ao OpenID Connect (OIDC) foi bastante aprimorado. Uma solução genérica agora está disponível, que funcionará com a maioria dos provedores OIDC. Provedores específicos para Azure e WSO2 também foram adicionados. Os provedores que foram testados e verificados para funcionar são Google, Microsoft / Azure, Okta, Keykloak e WSO2. O OIDC permite o Single Sign-On em vários sistemas enquanto gerencia identidades em um local central.

[Documentos](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-validation.html#outlier-detection)

**Traduções:** As traduções de metadados dinâmicos foram estendidas para cobrir muito mais entidades e propriedades e permitem que traduza a maior parte do aplicativo DHIS 2 em qualquer número de idiomas. Isso é útil para instâncias DHIS2 em vários idiomas.

[Docs]() | [Jira 1](https://jira.dhis2.org/browse/DHIS2-10562) | [2](https://jira.dhis2.org/browse/DHIS2-10556) | [3](https://jira.dhis2.org/browse/DHIS2-10487) | [4](https://jira.dhis2.org/browse/DHIS2-8669) | [5](https://jira.dhis2.org/browse/DHIS2-8297) | [6](https://jira.dhis2.org/browse/DHIS2-5587)

**Expiração da conta do utilizador:** As contas do utilizador agora podem ser configuradas para expirar em uma data específica. Isso é útil para criar contas temporárias, por exemplo ao convidar parceiros por meio de contas de convidados.

[Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/user_expiration.png) | [Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-8089)

**Desabilitar utilizadores inativos:** Um novo trabalho do sistema está disponível para desabilitar automaticamente os utilizadores que estiveram inativos (não logados) por um determinado número de meses. Isso é útil do ponto de vista da segurança para evitar que contas de utilizadores inativos sejam comprometidas.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/scheduler_disable_inactive_users.png) | [Docs]()

**Partilha de leitura de dados para visualizações SQL:** A partilha de leitura de dados agora é necessário para ler a saída de uma visualização SQL. Isso permite que os implementadores concedam aos utilizadores acesso para ler a saída de visualizações SQL sem dar acesso para adicionar ou editar as visualizações.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/sql_view_data_sharing.png) | [Docs]()

**Desempenho das verificações de integridade de dados:** O desempenho das verificações de integridade de dados (no aplicativo de administração de dados) foi melhorado e concluído muito mais rápido.

[Captura de tela](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/36/data_integrity_checks.png) | [Docs]()

**Desabilite a execução da regra do programa:** Uma nova propriedade de configuração está disponível em `dhis.conf` para desabilitar / habilitar a execução da regra do programa do lado do servidor.

[Docs]()

**Modernização de aplicativos principais:** A maioria dos aplicativos principais empacotados com a versão 2.36.0 DHIS2 foram atualizados para aproveitar o mais recente conjunto de ferramentas de aplicativos DHIS2. Isso garante que os aplicativos modernizados tenham uma barra de cabeçalho idêntica, cobertura de tradução aprimorada e elementos de interface de utilizador mais padronizados.

[Jira](https://jira.dhis2.org/browse/DHIS2-10026)

## RECURSOS DA API

**Nó líder do cluster:** Em uma configuração de cluster, o ID do nó líder está disponível no novo endpoint `/api/cluster/leader`. Isso é útil para administradores de sistemas para entender qual nó do cluster está atuando como o líder e executando trabalhos agendados.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#cluster-info) | [Jira](https://jira.dhis2.org/browse/DHIS2-102579)

**Acompanhamento do valor dos dados:** Um novo endpoint está disponível para marcar os valores dos dados para acompanhamento.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data.html#webapi_follow_up) | [Jira](https://jira.dhis2.org/browse/DHIS2-10344)

**Fuso horário do servidor:** As informações de fuso horário do servidor são adicionadas ao endpoint `/api/system/info`.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#webapi_system_resource_view_system_information) | [Jira](https://jira.dhis2.org/browse/DHIS2-9970)

**Excluir resultados de validação:** Um novo endpoint está disponível para excluir resultados de validação.

 [Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-validation.html#webapi_validation_results) | [Jira](https://jira.dhis2.org/browse/DHIS2-74399)

## DIVULGAR INFORMAÇÕES


|Informação de Lançamento|Ligação|
| --- | --- |
|Baixar versão e banco de dados de amostra|https://www.dhis2.org/downloads|
|Documentação|[https://docs.dhis2.org](https://docs.dhis2.org/)|
|Notas de atualização|[Notas de atualização no GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Detalhes sobre cada recurso no JIRA|https://jira.dhis2.org/issues/?filter=XXXXX|
|Visão geral dos bugs corrigidos no JIRA|https://jira.dhis2.org/issues/?filter=XXXXX|
|Código fonte no Github|https://github.com/dhis2|
|Instância de demonstração|https://play.dhis2.org/2.36/|
|Docker|`docker pull dhis2 / core: 2.36.0` <br> _para mais variantes de imagem docker, consulte [dockerhub](https://hub.docker.com/repository/docker/dhis2/core)_|
|Comunidade DHIS 2|https://community.dhis2.org/|
