---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/commonmark/en/content/developer/apps.md"
---

# Apps

<!--DHIS2-SECTION-ID:apps-->

Um aplicativo empacotado é um [Open Web
App] (https://developer.mozilla.org/en-US/docs/Open_Web_apps_and_Web_standards)
que tem todos os seus recursos (HTML, CSS, JavaScript, manifesto do aplicativo e
assim por diante) contido em um arquivo zip. Ele pode ser carregado para um DHIS2
instalação diretamente por meio da interface do usuário em tempo de execução. Um embalado
app é um arquivo ZIP com um [app
manifesto] (http://www.w3.org/2008/webapps/manifest/) em sua raiz
diretório. O manifesto deve ser denominado `manifest.webapp`. Um throrough
a descrição dos aplicativos pode ser obtida
[aqui] (https://developer.mozilla.org/en-US/Apps/Quickstart).

## Objetivo dos aplicativos empacotados

 <!--DHIS2-SECTION-ID:apps_purpose_packaged_apps-->

O objetivo dos aplicativos empacotados é estender a interface da web do DHIS2,
sem a necessidade de modificar o código-fonte do próprio DHIS2. Um sistema
a implantação geralmente terá requisitos personalizados e exclusivos. Os aplicativos
fornecer um ponto de extensão conveniente para a interface do usuário. Através
aplicativos, você pode complementar e personalizar a funcionalidade principal do DHIS2 com
soluções personalizadas de maneira fracamente acoplada e limpa.

Os aplicativos não têm permissão para interagir diretamente com a API DHIS2 Java.
Em vez disso, espera-se que os aplicativos usem funcionalidades e interajam com o
Serviços e dados DHIS2 utilizando a API DHIS2 Web.

## Criação de aplicativos

 <!--DHIS2-SECTION-ID:apps_creating_apps-->

Os aplicativos DHIS2 são construídos com arquivos HTML, JavaScript e CSS, semelhantes
para qualquer outro aplicativo da web. Os aplicativos também precisam de um arquivo especial chamado
* manifest.webapp * que descreve o conteúdo do aplicativo. Um basico
exemplo do * manifest.webapp * é mostrado abaixo:

    {
        "versão": "0.1",
        "nome": "Meu aplicativo",
        "descrição": "Meu aplicativo é um aplicativo empacotado",
        "launch_path": "/index.html",
        "appType": "APP",
        "ícones": {
            "16": "/img/icons/mortar-16.png",
            "48": "/img/icons/mortar-48.png",
            "128": "/img/icons/mortar-128.png"
        },
        "desenvolvedor": {
            "nomeie-me",
            "url": "http://me.com"
        },
        "default_locale": "en",
        "Atividades": {
            "dhis": {
                "href": "*",
                "namespace": "my-namespace"
            }
        },
        "autoridades": [
             "MY_APP_ADD_NEW",
             "MY_APP_UPDATE",
             "MY_APP_DELETE"
        }
    }

O arquivo * manifest.webapp * deve estar localizado na raiz do projeto.
Entre as propriedades estão:

  - A propriedade * icons → 48 * é usada para o ícone que é exibido no
    a lista de aplicativos instalados em uma instância DHIS2.

  - A propriedade * atividades * é uma extensão específica do dhis destinada a
    diferencie entre um Open Web App padrão e um aplicativo que pode ser
    instalado no DHIS2.

  - A propriedade * autoridades * contém uma lista de autoridades DHIS2
    que pode ser usado para restringir usuários de certas ações no
    aplicativo atual. Esta lista será carregada no DHIS2 durante o aplicativo
    processo de instalação e disponível para seleção na função do usuário
    forma de gestão.

  - O valor * \ ** para * href * é convertido no URL apropriado quando
    o aplicativo é carregado e instalado no DHIS2. Este valor pode então ser
    usado pelos arquivos JavaScript e HTML do aplicativo para fazer chamadas para
    a API da Web DHIS2 e identificar a localização correta do servidor DHIS2
    no qual o aplicativo foi instalado. Para esclarecer, as * atividades *
    parte será semelhante a esta depois que o aplicativo for instalado:

 <!-- end list -->

    "Atividades": {
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

Se você tiver uma coleção de aplicativos que deseja compartilhar o mesmo namespace,
mas também desejam reservá-lo, os usuários dos aplicativos precisam ter o
autoridade para usar o aplicativo que inicialmente reservou o namespace.

> ** Nota **
>
> Os namespaces não serão criados até que pelo menos um par de valores-chave seja
> presente no namespace. Especificar um namespace apenas no manifesto
> restringe o acesso e não cria nenhum dado no namespace.

A propriedade * appType * especifica como o aplicativo será exibido pelo
Instância DHIS2. Os valores possíveis para appType e seus efeitos são
explicado na tabela a seguir.

 <table>
 <caption> Tipos de aplicativos </caption>
 <colgroup>
 <col style="width: 27%" />
 <col style="width: 72%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> Tipo de aplicativo </th>
 <th> Descrição </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> APP </td>
 <td> Será listado no menu &quot;apps&quot; </td>
 </tr>
 <tr class="even">
 <td> DASHBOARD_WIDGET </td>
 <td> Disponível na caixa de pesquisa no painel, pode ser adicionado como um item em qualquer painel </td>
 </tr>
 <tr class="odd">
 <td> TRACKER_DASHBOARD_WIDGET </td>
 <td> Pode ser incorporado no painel do rastreador <em> (este tipo ainda não é compatível) </em> </td>
 </tr>
 <tr class="even">
 <td> RECURSO </td>
 <td> Aplicativos de recursos são pacotes que podem ser compartilhados por vários outros aplicativos. Esses aplicativos não são mostrados em qualquer lugar na IU, exceto no aplicativo de gerenciamento de aplicativos. </td>
 </tr>
 </tbody>
 </table>

Se nenhum * appType * for especificado no manifesto, o sistema usará "APP"
por padrão.

Para ler a estrutura JSON em JavaScript, você pode usar um AJAX regular
solicitar e analisar o JSON em um objeto. A maioria das bibliotecas Javascript
fornecer algum suporte, por exemplo com jQuery pode ser feito assim:

    $ .getJSON ("manifest.webapp", function (json) {
        var apiBaseUrl = json.activities.dhis.href + "/ api";
    });

O aplicativo pode conter HTML, JavaScript, CSS, imagens e outros arquivos que
pode ser necessário para apoiá-lo. A estrutura do arquivo pode ser algo
como isso:

    /
    /manifest.webapp #manifest file (obrigatório)
    / css / #css stylesheets (opcional)
    / img / #images (opcional)
    / js / #javascripts (opcional)

> ** Nota **
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
