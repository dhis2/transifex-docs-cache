---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/android-releases/2.6/ReleaseNote-2.6.0.md"
revision_date: "2022-04-18"
---

# Notas de lançamento do aplicativo DHIS2 Android versão 2.6{ #dhis2-android-app-version-26-release-notes }

## RECURSOS DE SUPORTE À IMPLEMENTAÇÃO{ #implementation-support-features }

**Suporte a vários utilizadores off-line:** o aplicativo Android agora pode funcionar com até 3 utilizadores diferentes enquanto estiver off-line. Os utilizadores precisarão ter acesso à internet para o primeiro login de cada conta e poderão trocar de conta depois sem precisar acessar a Internet. Os utilizadores poderão gerenciar as contas de utilizadores e excluir contas, se necessário. Quando o número máximo de contas for atingido, será necessário excluir uma das contas existentes para fazer login em uma nova.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-653) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users.png)
 | [Captura de tela 2] (https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users-2.png)
| [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_multiuser)

**Solução de problemas de configuração:** este recurso é para administradores. O Android App incorpora uma opção na tela de configurações para verificar alguns aspectos da configuração do DHIS2.

-   Idioma: o utilizadores poderá alterar o idioma da interface de utilizador do aplicativo para identificar etiquetas, botões ou prompts com erros ou sem tradução.
-   Validação de regras do programa: este validador verificará as regras do programa no dispositivo e exibirá inconsistências de configuração.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-1655) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting.png)| [Captura de tela 2] (https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting-2.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_configuration_troubleshooting)

## ANÁLISE OFFLINE{ #offline-analytics }

**Suporte a legendas para tabelas no Analytics:** as legendas são exibidas em tabelas dinâmicas ativando o recurso "Usar legendas para cor do gráfico" no aplicativo Data Visualizer. O aplicativo Android irá colorir as células usando a legenda predefinida por item de dados ou uma única legenda para toda a tabela dinâmica, dependendo das configurações em Web.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4500) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Legend-Sets.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_pivot_legends)

## RECURSOS DO TRACKER { #tracker-features }

**Quebre o vidro:** se o programa estiver configurado com nível de acesso "Protegido" e uma pesquisa for feita fora do escopo do utilizador, uma caixa de diálogo solicitando um motivo de acesso será exibida para que o utilizador substitua temporariamente o privilégio de propriedade do programa. Isso significa que o utilizador terá acesso aos dados relacionados ao programa.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-657) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Break-the-glass.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_breaking_the_glass)

**Torne a pesquisa TEI obrigatória configurável:** Pesquisar TEIs antes de criar não é obrigatório agora. Usando o Android Settings App (v2.2.0) é possível configurar o fluxo de usuários para criação de TEIs. Se o recurso estiver ativado, o Android App exibirá um botão "criar novo" após abrir um programa e uma pesquisa será opcional.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4545) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Mandatory-TEI-Search-Config.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_configurable_search)

**Fluxos de pesquisa off-line/on-line separados:** para melhorar o tempo de resposta nos resultados da pesquisa, o aplicativo Android agora pesquisa off-line primeiro e exibe os resultados enquanto faz uma pesquisa on-line como uma segunda etapa, transparente para o utilizador. A pesquisa fora do programa é oferecida como uma segunda etapa quando os atributos usados na pesquisa contêm pelo menos um atributo Tracked Entity Type (TET)

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4023) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Search-flow.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_offline_online_search)

## RECURSOS DE ENTRADA DE DADOS E SINCRONIZAÇÃO{ #data-entry-and-sync-features }

**Digitalizar e exibir códigos QR de matriz de dados GS1:** Se um atributo ou tipo de renderização de elemento de dados estiver configurado como código QR, o aplicativo Android poderá ler e processar a string como códigos de matriz de dados GS1. Combinado com o uso de funções d2 nas regras do programa, os diferentes campos de um código GS1 podem ser gravados em diferentes elementos de dados ou atributos (d2:extractDataMatrixValue(key, dataMatrixText)).

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4329) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-GS1-Data-matrix.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_gs1)

**Permitir que o utilizador "atualize os dados" para obter os últimos dados atualizados do servidor:** os utilizadores agora podem recuperar os dados mais recentes do servidor antes de inserir novos dados. Um botão de atualização agora está localizado para acionar uma sincronização granular nas seguintes telas:

-   Pagina Inicial
-   Procurar
-   Painel TEI
-   Listagem do programa de eventos
-   Detalhes do evento
-   Listagem do conjunto de dados
-   Detalhes do conjunto de dados

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4331) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Refresh-data.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_refresh_data)

**Renderizar ícones em formulários de inscrição:** A entrada de dados baseada em ícones agora pode ser usada em formulários de inscrição. Quando uma seção de inscrição contém um ou mais Atributos de Entidade Rastreada com conjuntos de opções e ícones atribuídos, o aplicativo pode exibi-los como uma matriz ou sequência com base no tipo de renderização da seção. Nas seções anteriores do aplicativo, esse recurso estava disponível apenas para elementos de dados.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4258) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Render-icons-in-enrollment-forms.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_icon_lib)

**Melhorar o fluxo de Gravar e Concluir em eventos:** Novas caixas de diálogo são exibidas ao gravar uma inscrição ou evento. O botão 'Reabrir' agora está localizado na tela de detalhes e estará disponível somente se o utilizador tiver a autoridade correta ('Eventos incompletos') para reabrir um evento concluído. O conceito e o diálogo de "conclusão" agora são mais intuitivos e fáceis de usar.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4610) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Save-and-complete-flow.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Novo design para avisos/erros e caixas de diálogo de conclusão:** As mensagens de erro e aviso foram aprimoradas para fornecer ao utilizador  mais e melhores informações. Os novos diálogos ao salvar, permitem que o usuário descarte as alterações, salve e corrija posteriormente ou continue editando o formulário para corrigir os valores dependendo da configuração.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-4591) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Warnings-errors-dialogs.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_common_features_errors)

**Melhorar o design das colunas dos conjuntos de dados:** as setas de redimensionamento agora estão fixas no canto superior esquerdo da tela .

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-3016) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Dataset-span.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/datasets-features.html#capture_app_data_sets_row)

**Mostrar dica da UO selecionada ao abrir a hierarquia da UO:** se uma unidade organizacional for selecionada, quando a hierarquia for exibida, todas as UOs ascendentes (pai) estarão em negrito para ajudar o utilizador a navegar na seleção anterior.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-2520) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Ou-hint.png)| [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_orgunit)

**Melhore a prevenção de duplicação de identificadores exclusivos:** ao pesquisar por atributos exclusivos e, em seguida, criar uma nova inscrição, se a pesquisa retornar um resultado, o aplicativo não persistirá os valores dos atributos exclusivos no formulário de inscrição.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4250) | [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_search)

**Ocultar botão gravar se o formulário não for editável:** se um evento tiver expirado ou tiver direitos somente de visualização, o botão "gravar" ficará oculto.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4613) | [Documentação](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Barra inferior de navegação de eventos de alinhamento:** a guia de detalhes na barra de navegação de eventos foi aprimorada para oferecer uma melhor experiência ao utilizador.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3651) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#navigation-bar)

**Melhorar o design do elemento de dados "Somente sim":** o rótulo "Sim" ao lado da caixa de seleção ou do botão de opção foi removido.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4493) | [Documentation](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render)

## MANUTENÇÃO { #maintenance }

**Qualidade / Segurança / Desempenho:**  pode encontrar uma lista de problemas relacionados à qualidade, segurança e desempenho abrindo este [filtro jira](https://jira.dhis2.org/issues/?filter=12363).

**Correção de bugs:** você pode encontrar uma lista dos bugs corrigidos nesta versão abrindo este [filtro jira](https://jira.dhis2.org/issues/?filter=12364).

## INFORMAÇÃO DE LANÇAMENTO { #release-info }

| Informação de Lançamento | Link |
| --- | --- |
| Baixe o aplicativo do Google Play ou Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Documentação | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Detalhes sobre cada recurso no JIRA (requer login) | [2.6 Features ](https://jira.dhis2.org/issues/?filter=12365) |
| Visão geral dos bugs corrigidos no JIRA (requer login) | [2.6 Bugs](https://jira.dhis2.org/issues/?filter=12364) |
| Instância de demonstração (utilizador / senha) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Credenciais: android / Android123 |
| Comunidade DHIS 2 | [https://community.dhis2.org Mobile Community] (https://community.dhis2.org/c/subcommunities/mobile/16) |
| Código fonte no Github | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Código fonte do SDK no Github | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |
