---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/settings.md" 
---
# Definições

<!--DHIS2-SECTION-ID:settings-->

As configurações são baixadas em cada sincronização de metadados. Existem diferentes tipos de configurações:

`` `java
d2.settingModule ()
`` `

- ** Configurações do sistema **: propriedades de todo o sistema, como `flag` ou` style`.
- ** Configurações do usuário **: configurações específicas do usuário, como `keyDbLocale` ou` keyUiLocale`.
- ** Aplicativo de configurações **: essas configurações oferecem controle adicional sobre o comportamento do aplicativo. Mais sobre isso na próxima seção.



## App de configurações

<!--DHIS2-SECTION-ID:settings_app-->

A instância DHIS2 pode incluir um aplicativo da web chamado "Configurações do Android" que permite ter controle remoto sobre certos parâmetros do aplicativo. A instalação e configuração deste aplicativo é opcional.

Este SDK baixa essa configuração em cada sincronização de metadados e a mantém no banco de dados. Alguns desses parâmetros são consumidos automaticamente pelo SDK (em negrito).

Geral:

- Frequência de sincronização de metadados / dados: este valor deve ser consumido pelo aplicativo e usado para acionar a sincronização no SDK.
- Configuração do celular: número do gateway, número do remetente. Eles devem ser consumidos pelo aplicativo e usados para configurar o módulo SMS no SDK.
- ** Valores reservados **: número de valores de atributos a serem reservados.
- ** Criptografar banco de dados **: criptografar ou não o banco de dados local.

** Programas: ** esta seção controla os parâmetros de sincronização de dados do programa. Possui uma seção para definir os parâmetros globais ou padrão a serem usados na sincronização de todos os programas. Além disso, permite definir configurações específicas para programas específicos. Todos esses parâmetros são consumidos pelo SDK e usados no processo de sincronização.

** DataSets: ** esta seção controla os parâmetros de sincronização de dados agregados. Possui uma seção para definir os parâmetros globais ou padrão a serem usados na sincronização de todos os dataSets. Além disso, permite definir configurações específicas para conjuntos de dados particulares. Todos esses parâmetros são consumidos pelo SDK e usados no processo de sincronização.

`` `java
// Configurações Gerais
d2.settingModule (). generalSetting (). get ();

// Configurações do programa
d2.settingModule (). programSetting (). get ();

// Configurações do DataSet
d2.settingModule (). dataSetSetting (). get ();
`` `

Embora esses parâmetros sejam consumidos automaticamente pelo SDK, o aplicativo pode substituir alguns desses valores no processo de sincronização. Por exemplo, pode definir um TEI ou limite de evento diferente ou uma estratégia de download diferente (limitByOrgUnit, limitByProgram).

