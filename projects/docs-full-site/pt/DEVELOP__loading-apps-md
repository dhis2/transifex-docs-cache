---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/developer/apps.md"
revision_date: "2021-06-14"
---

# Aplicativos { #apps }

Um aplicativo empacotado é um [Open Web App] (https://developer.mozilla.org/en-US/docs/Open_Web_apps_and_Web_standards) que contém todos os seus recursos (HTML, CSS, JavaScript, manifesto do aplicativo e assim por diante) em um arquivo zip. Ele pode ser carregado para uma instalação DHIS2 diretamente por meio da interface do usuário no tempo de execução. Um aplicativo empacotado é um arquivo ZIP com um [manifesto do aplicativo] (http://www.w3.org/2008/webapps/manifest/) em seu diretório raiz. O manifesto deve ser denominado `manifest.webapp`. Uma descrição completa dos aplicativos pode ser obtida [aqui] (https://developer.mozilla.org/en-US/Apps/Quickstart).

## Objetivo dos aplicativos empacotados { #apps_purpose_packaged_apps }

O objetivo dos aplicativos empacotados é estender a interface da web do DHIS2, sem a necessidade de modificar o código-fonte do próprio DHIS2. Uma implantação de sistema geralmente terá requisitos personalizados e exclusivos. Os aplicativos fornecem um ponto de extensão conveniente para a interface do usuário. Por meio de aplicativos, pode complementar e personalizar a funcionalidade principal do DHIS2 com soluções personalizadas de maneira fracamente acoplada e limpa.

Os aplicativos não têm permissão para interagir diretamente com a API DHIS2 Java. Em vez disso, espera-se que os aplicativos usem funcionalidades e interajam com os serviços e dados DHIS2, utilizando a API DHIS2 Web.

## Criação de aplicativos { #apps_creating_apps }

Os aplicativos DHIS2 são construídos com arquivos HTML, JavaScript e CSS, semelhantes a qualquer outro aplicativo da web. Os aplicativos também precisam de um arquivo especial chamado _manifest.webapp_ que descreve o conteúdo do aplicativo. Um exemplo básico do _manifest.webapp_ é mostrado abaixo:

    {
        "version": "0.1",
        "name": "My App",
        "description": "My App is a Packaged App",
        "launch_path": "/index.html",
        "appType": "APP",
        "icons": {
            "16": "/img/icons/mortar-16.png",
            "48": "/img/icons/mortar-48.png",
            "128": "/img/icons/mortar-128.png"
        },
        "developer": {
            "name": "Me",
            "url": "http://me.com"
        },
        "default_locale": "en",
        "activities": {
            "dhis": {
                "href": "*",
                "namespace": "my-namespace"
            }
        },
        "authorities": [
             "MY_APP_ADD_NEW",
             "MY_APP_UPDATE",
             "MY_APP_DELETE"
        }
    }

O arquivo _manifest.webapp_ deve estar localizado na raiz do projecto. Entre as propriedades estão:

- A propriedade _icons→48_é usada para o ícone que é exibido na lista de aplicativos que estão instalados em uma instância DHIS2.

- A propriedade _activities_ é uma extensão específica dhis destinada a diferenciar entre um Open Web App padrão e um aplicativo que pode ser instalado no DHIS2.

- A propriedade _authorities_ contém uma lista de autoridades DHIS2 que podem ser usadas para restringir os usuários de certas ações no aplicativo atual. Esta lista será carregada no DHIS2 durante o processo de instalação do aplicativo e disponível para seleção no formulário de gerenciamento de função do usuário.

- O valor \*\** para *href* é convertido no URL apropriado quando o aplicativo é carregado e instalado no DHIS2. Esse valor pode então ser usado pelos arquivos JavaScript e HTML do aplicativo para fazer chamadas para a API da Web DHIS2 e identificar o local correto do servidor DHIS2 no qual o aplicativo foi instalado. Para esclarecer, a parte *actividades\* será semelhante a esta depois que o aplicativo for instalado:

<!-- end list -->

    "actividades": {
        "dhis": {
            "href": "http://apps.dhis2.org/demo",
            "namespace": "my-namespace"
        }
     }

- Uma propriedade _settings_ é opcional e pode ser usada em um aplicativo de widget de painel para suprimir a exibição do título do widget quando o widget é exibido em um painel:

<!-- end list -->

    "definições": {
        "dashboardWidget": {
            "hideTitle": verdadeiro
        }
    }

A propriedade do namespace pode ser adicionada se seu aplicativo estiver utilizando a API dataStore ou userDataStore. Ao adicionar a propriedade do namespace, apenas os usuários com acesso ao seu aplicativo têm permissão para fazer alterações no namespace. Um namespace só pode ser reservado dessa maneira uma vez. Se outro aplicativo tentar reservar um namespace já em uso, a instalação do outro aplicativo falhará.

Se tiver uma coleção de aplicativos que deseja compartilhar o mesmo namespace, mas também deseja reservá-lo, os usuários dos aplicativos precisam ter autoridade para usar o aplicativo que inicialmente reservou o namespace.

> **Nota**
>
> Os namespaces não serão criados até que pelo menos um par de valores-chave esteja presente no namespace. Especificar um namespace no manifesto apenas restringe o acesso e não cria nenhum dado no namespace.

A propriedade _appType_ especifica como o aplicativo será exibido pela instância DHIS2. Os valores possíveis para appType e seus efeitos são explicados na tabela a seguir.

Tabela: tipos de aplicativos

| Tipo de aplicativo | Descrição |
| --- | --- |
| APLICATIVO | Será listado no menu "apps" |
| DASHBOARD_WIDGET | Disponível na caixa de pesquisa do painel, pode ser adicionado como um item em qualquer painel |
| TRACKER_DASHBOARD_WIDGET | Pode ser incorporado no painel do rastreador _ (este tipo ainda não é compatível) _ |
| RECURSO | Os aplicativos de recursos são pacotes que podem ser compartilhados por vários outros aplicativos. Esses aplicativos não são mostrados em qualquer lugar na IU, exceto no aplicativo de gerenciamento de aplicativos. |

Se nenhum _appType_ for especificado no manifesto, o sistema usará "APP" por padrão.

Para ler a estrutura JSON em JavaScript, pode usar uma solicitação AJAX regular e analisar o JSON em um objecto. A maioria das bibliotecas Javascript fornece algum suporte, por exemplo, com jQuery, pode ser feito assim:

    $.getJSON( "manifest.webapp", function( json ) {
        var apiBaseUrl = json.activities.dhis.href + "/api";
    } );

O aplicativo pode conter HTML, JavaScript, CSS, imagens e outros arquivos que podem ser necessários para suportá-lo. A estrutura do arquivo pode ser semelhante a esta:

    /
    /manifest.webapp    #manifest file (mandatory)
    /css/               #css stylesheets (optional)
    /img/               #images (optional)
    /js/                #javascripts (optional)

> **Nota**
>
> É apenas o arquivo `manifest.webapp` que deve ser colocado na raiz. Cabe ao desenvolvedor organizar arquivos CSS, imagens e JavaScript dentro do aplicativo conforme necessário.

Todos os arquivos do projecto devem ser compactados em um arquivo zip padrão. Observe que o arquivo manifest.webapp deve estar localizado na raiz do arquivo zip (não inclua um diretório pai no arquivo). O arquivo zip pode então ser instalado no DHIS2, como verá na próxima secção.

## Instalando aplicativos em DHIS2 { #apps_installing_apps }

Os aplicativos podem ser instalados carregando um arquivo zip no App Manager. Em Serviços → Aplicativos, clique no item de menu _App Store_. ![](resources/images/apps/app-management.png) O aplicativo pode ser carregado pressionando o botão Procurar e depois de selecionar o pacote zip, o arquivo é carregado automaticamente e instalado no DHIS2. Você também pode navegar por aplicativos na DHIS2 [app store] (https://www.dhis2.org/appstore) e baixar aplicativos de lá. A loja de aplicativos DHIS2 permite pesquisar, revisar, comentar, solicitar recursos e avaliar os aplicativos pela comunidade.

## Iniciando Apps { #apps_launching_apps }

Após a instalação, seus aplicativos serão integrados ao sistema de menu e podem ser acessados em serviços e na página de visão geral do módulo. Ele também pode ser acessado na página inicial do módulo de aplicativos. Clique em um aplicativo da lista para iniciá-lo.
