---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/2.5/android-releases/2.5/ReleaseNote-2.5.0.md"
revision_date: "2021-11-23"
---

# Notas de Lançamento do Aplicativo Android DHIS2 versão 2.5 { #dhis2-android-app-version-25-release-notes }

<!-- BEGIN-WEBSITE-SYNC-ID:android -->

<!-- Analytics -->

## ANÁLISES LOCAIS { #local-analytics }

**Programa offline no aplicativo/análise de conjunto de dados:** O aplicativo Android agora pode renderizar análises que foram criadas no aplicativo Data Visualizer no DHIS2. A análise a ser exibida requer configuração usando o Android Settings Web App, onde os administradores poderão selecionar os gráficos e tabelas a serem exibidos para os utilizadores finais. Essas visualizações podem ser renderizadas na tela inicial do aplicativo, na tela do conjunto de dados e no nível dos programas. Todas as análises são agregadas no dispositivo usando dados locais. O recurso Analyticis é 100% funcional offline.

As análises com suporte no aplicativo Android são:

-   Tabelas Dinâmicas
-   Gráfico de colunas
-   Gráfico de linha
-   Gráfico de pizza
-   Gráfico de radar
-   Valor unico

Todas essas visualizações podem ser organizadas e exibidas em grupos. Os grupos também são configurados usando o Android Settings Web App. Para cada objeto de visualização, o utilizador poderá filtrar no aplicativo por:

-   Período: Diário, Semanal, Mensal, Anual, Este Trimestre, Último Trimestre, Últimos 4 Trimestres e Trimestre deste ano.
-   OrgUnit: selecione "Todos" para exibir todas as unidades organizacionais disponíveis para o utilizador ou "Seleção" para especificar uma ou várias unidades organizacionais.

[Jira] (https://jira.dhis2.org/browse/ANDROAPP-2557) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Home.png) | [Captura de tela 2] (https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Filtering.png) | [Captura de tela 3] (https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Groups.png) | [Captura de tela 4] (https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Android+Settings+Webapp.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#local-analytics-new-25)

## EXPERIÊNCIA DO UTILIZADOR DE ENTRADA DE DADOS { #data-entry-user-experience }

**Redesenho do conjunto de dados** O layout para a entrada de dados dos conjuntos de dados foi redesenhado para uma experiência de utilizador mais integrada e interface de utilizador limpa. [Jira] (https://jira.dhis2.org/browse/ANDROAPP-4382) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Data+Sets+New+style.png)

**Exportar/partilhar códigos de barras e QR:** Elementos de dados ou atributos do tipo texto podem ser configurados como códigos de barras ou QR. Com a nova opção exportar/partilhar, os utilizadores poderão exibir uma barra ou código QR em uma imagem para que possa ser partilhada para impressão, fazer uma captura de tela ou mostrá-la na tela para digitalização. [Jira] (https://jira.dhis2.org/browse/ANDROAPP-3891) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Export+Share+QR+Code.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render_qr)

**Renderização aprimorada para entrada de dados baseada em ícones:** Quando o tipo de renderização das seções do programa é usado em combinação com ícones, uma seção com um único elemento de dados e Conjunto de Opções associado renderiza os ícones atribuídos ao lado das opções para simplificar a entrada de dados. O layout e o design dessa tela foram reprojetados e aprimorados para uma melhor experiência do utilizador. [Jira] (https://jira.dhis2.org/browse/ANDROAPP-4027) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Visual+Data+Entry.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_rendering_type)

**Visualização de calendário personalizado:** No aplicativo DHIS2 Android Capture, os utilizadores podem alternar a seleção de data de spinner para visualização de calendário. Nesta versão, o aplicativo se lembrará da última visualização selecionada pelo utilizador e a utilizará na próxima vez que o utilizador precisar selecionar uma data. [Jira] (https://jira.dhis2.org/browse/ANDROAPP-2402) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Calendar.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#personalized-calendar-view-new-25)

**Exibição de motivo para dados não editáveis:** Os dados podem ser bloqueados por vários motivos no DHIS2, devido a restrições de acesso ou expiração, entre outros. Quando um evento, TEI ou conjunto de dados não são editáveis, o utilizador poderá encontrar o motivo na seção "Detalhes". Os possíveis motivos são:

-   Conclusão do evento
-   Conclusão da inscrição
-   Evento expirado
-   Unidade de organização fechada
-   Unidade organizacional fora do escopo de captura
-   Sem acesso para capturar dados no programa ou conjunto de dados
-   Sem acesso a uma opção de categoria no programa ou conjunto de dados [Jira] (https://jira.dhis2.org/browse/ANDROAPP-3565) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Non+Editable+Data.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#reason-for-non-editable-data-new-25)

**Ajuste as opções do painel TEI para a configuração do programa:** As opções oferecidas no painel TEI serão adaptadas à configuração específica do programa.

-   A guia Relacionamentos não estará visível se os relacionamentos do programa não estiverem configurados.
-   O botão Criar evento ficará oculto quando o utilizador não puder criar mais eventos com base na configuração do rastreador.
-   A guia Indicadores não estará visível se o programa não tiver indicadores de programa configurados.
-   O filtro de Unidade de Organização não ficará visível se o utilizador tiver apenas uma Unidade de Organização configurada. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4097) | [Jira 2](https://jira.dhis2.org/browse/ANDROAPP-3129) | [Jira 3](https://jira.dhis2.org/browse/ANDROAPP-4099) | [Documentação](https://docs.dhis2.org/en/use/android-app/features-supported.html#tei-dashboard-navigation-panel-new-25)

## MAPAS { #maps }

**Experiência do utilizador de mapas gerais:** Após três versões desde que os mapas foram incluídos no aplicativo DHIS2 para Android, revisamos e melhoramos a experiência do utilizador com base nos comentários da comunidade.
[Jira](https://jira.dhis2.org/browse/ANDROAPP-4024) | [Documentação]()

**Centro para a posição do utilizador:** Se o utilizador conceder permissões de localização ao aplicativo, o mapa mostrará a localização atual representada como um ponto de cor azul. Os mapas no DHIS2 Android Capture App agora incluem a possibilidade de centralizar o mapa na localização do utilizador. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3583) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-User+position.png)

## RECURSOS DO TRACKER { #tracker-features }

**Adicionar suporte para eventos - relacionamentos TEI:** O aplicativo agora permite aos utilizadores adicionar relacionamentos de eventos únicos (Event programs) to TEIs. There is a new tab in the event dashboard, named relationships, that is active when it is configured in the server. This version does not allow relationships from TEIs to events or using events that belong to an enrollment. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2275) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Event+TEI+Relationships.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/features-supported.html#event-tei-relationships-new-25)

**NOVO filtro para TEIs marcados como follow-up:** Nos programas Tracker, o filtro 'Follow Up' permite ao utilizador filtrar os TEIs que foram marcados como 'Follow-up'. Os TEIs podem ser marcados para acompanhamento no TEI Dashbaord. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3304) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Follow+Up+Filter.png) | [Documentação](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#follow-up-new-25)

## OUTROS RECURSOS { #other-features }

**Idioma da interface com base no idioma do utilizador DHIS2:** O idioma da interface corresponderá ao idioma definido na configuração do utilizador DHIS2. Se o idioma não estiver disponível no aplicativo, ele escolherá o idioma do dispositivo. Se nenhuma das configurações de idioma estiver disponível, o aplicativo usará o inglês como padrão. As traduções configuradas no DHIS2 para metadados também serão mostradas de acordo com o idioma na configuração do utilizador. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2925) | [Documentação](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#interface-language-new-25)

## MANUTENÇÃO { #maintenance }

**Qualidade / Segurança / Desempenho:** Pode encontrar uma lista de questões relacionadas à qualidade, segurança e desempenho abrindo este [filtro jira](https://jira.dhis2.org/issues/?filter=12204).

**Correção de bugs:** Pode encontrar uma lista dos bugs corrigidos nesta versão abrindo este [filtro jira] (https://jira.dhis2.org/issues/?filter=12203).

## INFORMAÇÃO DE LANÇAMENTO { #release-info }

| Informação de Lançamento | Link |
| --- | --- |
| Baixe o aplicativo do Google Play ou Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Documentação | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Detalhes sobre cada recurso no JIRA (requer login) | [2.5 Recursos](https://jira.dhis2.org/issues/?filter=12300) |
| Visão geral dos bugs corrigidos no JIRA (requer login) | [2.5 Bugs] (https://jira.dhis2.org/issues/?filter=12203) |
| Instância de demonstração (utilizador / senha) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Credenciais: android / Android123 |
| Comunidade DHIS 2 | [https://community.dhis2.org Mobile Community] (https://community.dhis2.org/c/subcommunities/mobile/16) |
| Código fonte no Github | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Código fonte do SDK no Github | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |

<!-- END-WEBSITE-SYNC-ID:android -->
