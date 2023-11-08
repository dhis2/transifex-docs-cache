# DHIS versão 2.36 Nota de Lançamento

Este documento destaca os principais recursos do lançamento inicial do DHIS2 versão 2.36. Esta versão é totalmente compatível com o DHIS2 [Android Capture App] (https://www.dhis2.org/android-2-4) versão 2.4.


## RECURSOS DE ANÁLISE



  - *Amplie* clicando e arrastando o cursor sobre uma área que deseja ampliar. Isso geralmente é necessário para ver mais detalhes em áreas onde muitas unidades organizacionais estão agrupadas.
  - *A detecção de outlier* pode ser feita usando um escore z padrão, escore z modificado ou um intervalo interquartil por meio do menu de opções. Uma linha limite extrema vertical (eixo y) e horizontal (eixo x) também pode ser aplicada. Endossado pela OMS, esta é uma maneira muito clara e poderosa de identificar valores discrepantes que geralmente representam problemas de qualidade de dados. Você pode identificar os valores discrepantes com maior probabilidade de prejudicar as estatísticas nacionais usando a detecção de valores discrepantes em combinação com as linhas de limite X e Y extremas.

[Captura de tela]() | [Docs]()

**Modo de apresentação do item do painel em tela inteira:** Expanda qualquer item do painel (gráfico, mapa ou tabela dinâmica) para o tamanho da tela inteira. Isso é ótimo para apresentar dados em reuniões virtuais ou presenciais diretamente do painel.

[Captura de tela]() | [Docs]()

**Legendas do gráfico de barras e colunas:** Altere a cor de uma barra ou coluna com base em uma legenda predefinida. Isso torna mais fácil destacar o desempenho inferior e superior com gráficos de barras e colunas.

[Captura de tela]() | [Docs]()

**Aplicativo de painel otimizado para celular:** O aplicativo de painel da web DHIS 2 agora é mais otimizado para celular e pode ser usado em dispositivos móveis. Isso permite que você use o poder dos painéis de seu dispositivo móvel. Agora você pode levar seus painéis com você, verificá-los a qualquer momento e compartilhar dados com quem você precisar com a conveniência de seu telefone. O aplicativo adotou vários dos princípios de _Progressive Web Apps_ (PWA). O suporte offline para painéis virá em uma versão futura.

[Captura de tela]() | [Docs]()



[Captura de tela]() | [Docs]()



[Captura de tela]() | [Docs]()



[Captura de tela]() | [Docs]()



[Captura de tela]() | [Docs]()


## RECURSOS DO TRACKER E DO EVENTO



[Jira]()



[]() | [Jira]()



[Documentos]() | [Jira]()

## RECURSOS DA PLATAFORMA

**Detecção de valores discrepantes:** Uma detecção de valores discrepantes nova e aprimorada está disponível no aplicativo de qualidade de dados. Os valores atípicos agora são classificados e os valores atípicos mais significativos são retornados primeiro, tornando muito mais fácil encontrar e corrigir os valores atípicos que afetam muito a análise de dados. Anteriormente, os valores discrepantes eram retornados sem um pedido. Outliers são classificados por * distância absoluta da média *. O * escore z * do valor, bem como a média, dev padrão, mínimo e máximo estão disponíveis na resposta.



**OpenID Connect:** O suporte ao OpenID Connect (OIDC) foi bastante aprimorado. Uma solução genérica agora está disponível, que funcionará com a maioria dos provedores OIDC. Provedores específicos para Azure e WSO2 também foram adicionados. Os provedores que foram testados e verificados para funcionar são Google, Microsoft / Azure, Okta, Keykloak e WSO2. O OIDC permite o Single Sign-On em vários sistemas enquanto gerencia identidades em um local central.

[Docs]()



[Docs]() | [Jira 1](https://jira.dhis2.org/browse/DHIS2-10562) | [2](https://jira.dhis2.org/browse/DHIS2-10556) | [3](https://jira.dhis2.org/browse/DHIS2-10487) | [4](https://jira.dhis2.org/browse/DHIS2-8669) | [5](https://jira.dhis2.org/browse/DHIS2-8297) | [6](https://jira.dhis2.org/browse/DHIS2-5587)

**Vencimento da conta do usuário:** As contas do usuário agora podem ser configuradas para expirar em uma data específica. Isso é útil para criar contas temporárias, por exemplo ao convidar parceiros por meio de contas de convidados.

[](https://jira.dhis2.org/browse/DHIS2-8089)

**Desabilitar usuários inativos:** Um novo trabalho do sistema está disponível para desabilitar automaticamente os usuários que estiveram inativos (não logados) por um determinado número de meses. Isso é útil do ponto de vista da segurança para evitar que contas de usuários inativos sejam comprometidas.

[Docs]()

**Compartilhamento de leitura de dados para visualizações SQL:** O compartilhamento de leitura de dados agora é necessário para ler a saída de uma visualização SQL. Isso permite que os implementadores concedam aos usuários acesso para ler a saída de visualizações SQL sem dar acesso para adicionar ou editar as visualizações.

[Docs]()

**Desempenho das verificações de integridade de dados:** O desempenho das verificações de integridade de dados (no aplicativo de administração de dados) foi melhorado e concluído muito mais rápido.

[Docs]()

**Desabilite a execução da regra do programa:** Uma nova propriedade de configuração está disponível em `dhis.conf` para desabilitar / habilitar a execução da regra do programa do lado do servidor.

[Docs]()

## RECURSOS DA API

**Nó líder do cluster:** Em uma configuração de cluster, o ID do nó líder está disponível no novo endpoint `/ api / cluster / leader`. Isso é útil para administradores de sistemas para entender qual nó do cluster está atuando como o líder e executando trabalhos agendados.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#cluster-info) | [Jira](https://jira.dhis2.org/browse/DHIS2-102579)

**Acompanhamento do valor dos dados:** Um novo ponto final está disponível para marcar os valores dos dados para acompanhamento.

[Documentos](https://docs.dhis2.org/master/en/dhis2_developer_manual/web-api.html#follow-up)

**Fuso horário do servidor:** As informações de fuso horário do servidor são adicionadas ao endpoint `/api/system/info`.

[Docs]()

**Excluir resultados de validação:** Um novo endpoint está disponível para excluir resultados de validação.



## DIVULGAR INFORMAÇÕES


|Informação de Lançamento|Ligação|
| --- | --- |
|Baixar versão e banco de dados de amostra||
|Documentação|[](https://docs.dhis2.org/)|
|Notas de atualização|[Notas de atualização no GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Detalhes sobre cada recurso no JIRA||
|Visão geral dos bugs corrigidos no JIRA||
|Código fonte no Github||
|Instância de demonstração||
||`docker pull dhis2 / core: 2.36.0` <br> _para mais variantes de imagem docker, consulte [dockerhub](https://hub.docker.com/repository/docker/dhis2/core)_|
|Comunidade DHIS 2||
