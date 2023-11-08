---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/commonmark/en/content/developer/apps.md"
---

# Apps

<!--DHIS2-SECTION-ID:apps-->

A packaged app is an [Open Web
App](https://developer.mozilla.org/en-US/docs/Open_Web_apps_and_Web_standards)
that has all of its resources (HTML, CSS, JavaScript, app manifest, and
so on) contained in a zip file. It can be uploaded to a DHIS2
installation directly through the user interface at runtime. A packaged
app is a ZIP file with an [app
manifest](http://www.w3.org/2008/webapps/manifest/) in its root
directory. The manifest must be named `manifest.webapp`. A throrough
description of apps can be obtained
[here](https://developer.mozilla.org/en-US/Apps/Quickstart).

## Objetivo dos aplicativos empacotados

<!--DHIS2-SECTION-ID:apps_purpose_packaged_apps-->

O objectivo dos aplicativos empacotados é estender a interface da web do DHIS2,
sem a necessidade de modificar o código-fonte do próprio DHIS2. Um sistema
a implantação geralmente terá requisitos personalizados e exclusivos. Os aplicativos
fornecer um ponto de extensão conveniente para a interface do usuário. Através
aplicativos, pode complementar e personalizar a funcionalidade principal do DHIS2 com
soluções personalizadas de maneira fracamente acoplada e limpa.

Os aplicativos não têm permissão para interagir diretamente com a API DHIS2 Java.
Em vez disso, espera-se que os aplicativos usem funcionalidades e interajam com o
Serviços e dados DHIS2 utilizando a API DHIS2 Web.

## Criação de aplicativos

<!--DHIS2-SECTION-ID:apps_creating_apps-->

Os aplicativos DHIS2 são construídos com arquivos HTML, JavaScript e CSS, semelhantes
para qualquer outro aplicativo da web. Os aplicativos também precisam de um arquivo especial chamado
*manifest.webapp* que descreve o conteúdo do aplicativo. Um basico
exemplo do *manifest.webapp* é mostrado abaixo:

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

O arquivo *manifest.webapp* deve estar localizado na raiz do projecto.
Entre as propriedades estão:

  - A propriedade *icons→48* é usada para o ícone que é exibido no
    a lista de aplicativos instalados em uma instância DHIS2.

  - A propriedade *actividades* é uma extensão específica do dhis destinada a
    diferencie entre um Open Web App padrão e um aplicativo que pode ser
    instalado no DHIS2.

  - A propriedade *autoridades* contém uma lista de autoridades DHIS2
    que pode ser usado para restringir usuários de certas ações no
    aplicativo atual. Esta lista será carregada no DHIS2 durante o aplicativo
    processo de instalação e disponível para seleção na função do usuário
    forma de gestão.

  - O valor *\** para *href* é convertido no URL apropriado quando
    o aplicativo é carregado e instalado no DHIS2. Este valor pode então ser
    usado pelos arquivos JavaScript e HTML do aplicativo para fazer chamadas para
    a API da Web DHIS2 e identificar a localização correta do servidor DHIS2
    no qual o aplicativo foi instalado. Para esclarecer, as *actividades*
    parte será semelhante a esta depois que o aplicativo for instalado:

<!-- end list -->

    "Actividades": {
        "dhis": {
            "href": "http://apps.dhis2.org/demo",
            "namespace": "my-namespace"
        }
     }

A propriedade do namespace pode ser adicionada se seu aplicativo estiver utilizando o
dataStore ou userDataStore api. Ao adicionar a propriedade do namespace, apenas
os usuários com acesso ao seu aplicativo têm permissão para fazer alterações no
namespace. Um namespace só pode ser reservado dessa maneira uma vez. Se outro
aplicativo tenta reservar um namespace já em uso, a instalação do
outro aplicativo irá falhar.

Se tiver uma coleção de aplicativos que deseja compartilhar o mesmo namespace,
mas também desejam reservá-lo, os usuários dos aplicativos precisam ter o
autoridade para usar o aplicativo que inicialmente reservou o namespace.

> **Nota**
>
> Os namespaces não serão criados até que pelo menos um par de valores-chave seja
> presente no namespace. Especificar um namespace apenas no manifesto
> restringe o acesso e não cria nenhum dado no namespace.

A propriedade *appType* especifica como o aplicativo será exibido pelo
Instância DHIS2. Os valores possíveis para appType e seus efeitos são
explicado na tabela a seguir.

<table>
<caption>App types</caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>App type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>APP</td>
<td>Will be listed in the &quot;apps&quot; menu</td>
</tr>
<tr class="even">
<td>DASHBOARD_WIDGET</td>
<td>Available from the search box on the dashboard, can be added as an item on any dashboard</td>
</tr>
<tr class="odd">
<td>TRACKER_DASHBOARD_WIDGET</td>
<td>Can be embedded in the tracker dashboard <em>(this type is not yet supported)</em></td>
</tr>
<tr class="even">
<td>RESOURCE</td>
<td>Resource apps are packages that can be shared by multiple other apps. These apps are not shown anywhere in the UI, except from in the app management app.</td>
</tr>
</tbody>
</table>

Se nenhum *appType* for especificado no manifesto, o sistema usará "APP"
por padrão.

Para ler a estrutura JSON em JavaScript, pode usar um AJAX regular
solicitar e analisar o JSON em um objeto. A maioria das bibliotecas Javascript
fornecer algum suporte, por exemplo, com jQuery pode ser feito assim:

    $.getJSON( "manifest.webapp", function( json ) {
        var apiBaseUrl = json.activities.dhis.href + "/api";
    } );

O aplicativo pode conter HTML, JavaScript, CSS, imagens e outros arquivos que
pode ser necessário para apoiá-lo. A estrutura do arquivo pode ser algo
como isso:

    /
    /manifest.webapp    #manifest file (mandatory)
    /css/               #css stylesheets (optional)
    /img/               #images (optional)
    /js/                #javascripts (optional)

> **Nota**
>
> É apenas o arquivo `manifest.webapp` que deve ser colocado no
> root. Cabe ao desenvolvedor organizar CSS, imagens e JavaScript
> arquivos dentro do aplicativo, conforme necessário.

Todos os arquivos do projeto devem ser compactados em um arquivo zip padrão
arquivo. Observe que o arquivo manifest.webapp deve estar localizado na raiz
do arquivo zip (não inclua um diretório pai no arquivo).
O arquivo zip pode então ser instalado no DHIS2 como você verá no
próxima seção.

## Instalando aplicativos no DHIS2

 <!--DHIS2-SECTION-ID:apps_installing_apps-->

Os aplicativos podem ser instalados carregando um arquivo zip no App Manager. Dentro,
Serviços → Aplicativos, clique no item de menu * App Store *.
![](resources/images/apps/app-management.png) O aplicativo pode ser carregado por
pressionando o botão Browse e depois de selecionar o pacote zip, o arquivo
é carregado automaticamente e instalado no DHIS2. Você também pode navegar
por meio de aplicativos na DHIS2 [app store] (https://www.dhis2.org/appstore)
e baixe aplicativos de lá. A loja de aplicativos DHIS2 permite aplicativos
pesquisando, revisando, comentando, solicitando recursos, classificando no
aplicativos da comunidade.

## Aplicativos de lançamento

 <!--DHIS2-SECTION-ID:apps_launching_apps-->

Após a instalação, seus aplicativos serão integrados ao sistema de menus
e pode ser acessado em serviços e na página de visão geral do módulo. Isto
também pode ser acessado na página inicial do módulo de aplicativos. Clique em um
aplicativo na lista para iniciá-lo.
