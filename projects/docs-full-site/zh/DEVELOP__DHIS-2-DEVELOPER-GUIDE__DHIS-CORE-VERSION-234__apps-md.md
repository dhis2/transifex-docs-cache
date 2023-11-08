---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/commonmark/en/content/developer/apps.md"
---

# 应用

 <!--DHIS2-SECTION-ID:apps-->

打包的应用程序是 [Open Web
应用](https://developer.mozilla.org/en-US/docs/Open_Web_apps_and_Web_standards)
拥有所有资源（HTML、CSS、JavaScript、应用程序清单和
等等）包含在一个 zip 文件中。它可以上传到 DHIS2
在运行时直接通过用户界面安装。一个打包好的
app 是一个 ZIP 文件，带有 [app
清单](http://www.w3.org/2008/webapps/manifest/) 在它的根
目录。清单必须命名为`manifest.webapp`。彻底
可以获得应用程序的描述
[此处](https://developer.mozilla.org/en-US/Apps/Quickstart)。

## 打包应用程序的目的

 <!--DHIS2-SECTION-ID:apps_purpose_packaged_apps-->

打包应用的目的是扩展DHIS2的网络界面，
无需修改DHIS2本身的源代码。一个系统
部署通常会有自定义和独特的要求。应用程式
提供方便的用户界面扩展点。通过
应用程序，您可以通过以下方式补充和自定义DHIS2核心功能
以松散耦合和干净的方式定制解决方案。

应用没有权限直接与DHIS2 Java API进行交互。
相反，应用程序应使用功能并与
DHIS2 Web API通过使用DHIS2服务和数据。

## 创建应用

 <!--DHIS2-SECTION-ID:apps_creating_apps-->

DHIS2应用程序由HTML，JavaScript和CSS文件构成，类似
到任何其他Web应用程序。应用还需要一个名为
* manifest.webapp *，它描述了应用程序的内容。基本的
* manifest.webapp *的示例如下所示：

    {
        “ version”：“ 0.1”，
        “ name”：“我的应用”，
        “ description”：“我的应用程序是打包的应用程序”，
        “ launch_path”：“ /index.html”，
        “ appType”：“ APP”，
        “图标”：{
            “ 16”：“ /img/icons/mortar-16.png”，
            “ 48”：“ /img/icons/mortar-48.png”，
            “ 128”：“ /img/icons/mortar-128.png”
        }，
        “开发人员”：{
            “ name”：“ Me”，
            “ url”：“ http://me.com”
        }，
        “ default_locale”：“ en”，
        “活动”：{
            “ dhis”：{
                “ href”：“ *”，
                “ namespace”：“ my-namespace”
            }
        }，
        “当局”：[
             “ MY_APP_ADD_NEW”，
             “ MY_APP_UPDATE”，
             “ MY_APP_DELETE”
        }
    }

* manifest.webapp *文件必须位于项目的根目录。
这些属性包括：

  - * icons→48 *属性用于显示在
    DHIS2实例上安装的应用程序列表。

  - * activities *属性是dhis专有的扩展，旨在
    区分标准的Open Web App和可以
    安装在DHIS2中。

  - * authorities *属性包含DHIS2授权的列表
    可以用来限制用户对
    当前应用。该列表将在应用程序期间加载到DHIS2中
    安装过程，可以在“用户角色”中选择
    管理表格。

  - * href *的* \ **值将在以下情况下转换为适当的URL
    该应用已上传并安装在DHIS2中。这个值可以是
    应用程序的JavaScript和HTML文件使用它来调用
    DHIS2 Web API并标识DHIS2服务器的正确位置
    已安装该应用程序的位置。为了澄清，*活动*
    安装应用程序后，该部分的外观与此类似：

<!-- end list -->

    “活动”：{
        “ dhis”：{
            “ href”：“ http://apps.dhis2.org/demo”，
            “ namespace”：“ my-namespace”
        }
     }

如果您的应用程序利用了
dataStore或userDataStore api。添加命名空间属性时，仅
有权访问您应用的用户可以对
命名空间。命名空间只能以这种方式保留一次。如果另一个
应用尝试保留已使用的名称空间，
其他应用程序将失败。

如果您有一组想要共享相同名称空间的应用，
但也希望保留它，应用程序的用户需要具有
使用最初保留名称空间的应用程序的权限。

> **注意**
>
>只有至少一对键值对被创建时，才会创建命名空间
>存在于名称空间中。仅在清单中指定名称空间
>限制访问，并且不会在名称空间中创建任何数据。

* appType *属性指定应用将如何显示
DHIS2实例。 appType及其效果的可能值为
下表中有解释。

 <table>
 <caption> 应用程序类型 </caption>
 <colgroup>
 <col style="width: 27%" />
 <col style="width: 72%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> 应用程序类型 </th>
 <th> 说明 </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> APP </td>
 <td> 将列在 &quot;apps&quot; 菜单 </td>
 </tr>
 <tr class="even">
 <td> DASHBOARD_WIDGET </td>
 <td> 可从仪表板上的搜索框中获得，可以添加为任何仪表板上的项目 </td>
 </tr>
 <tr class="odd">
 <td> TRACKER_DASHBOARD_WIDGET </td>
 <td> 可以嵌入到追踪器仪表盘中 <em>（暂不支持此类型）</em></td>
 </tr>
 <tr class="even">
 <td> 资源 </td>
 <td> 资源应用程序是可以由多个其他应用程序共享的包。这些应用程序不会显示在 UI 中的任何位置，除了在应用程序管理应用程序中。 </td>
 </tr>
 </tbody>
 </table>

如果清单中未指定* appType *，则系统将使用“ APP”
默认。

要将JSON结构读入JavaScript，可以使用常规AJAX
请求并将JSON解析为一个对象。大多数Javascript库
提供一些支持，例如使用jQuery，可以这样完成：

    $ .getJSON（“ manifest.webapp”，function（json）{
        var apiBaseUrl = json.activities.dhis.href +“ / api”;
    }）；

该应用可以包含HTML，JavaScript，CSS，图像和其他文件
可能需要支持它。文件结构可能看起来有些像
像这样：

    /
    /manifest.webapp＃清单文件（必填）
    / css / #css样式表（可选）
    / img / #images（可选）
    / js / #javascripts（可选）

> **注意**
>
>只有`manifest.webapp`文件必须放置在
>根。由开发人员来组织CSS，图像和JavaScript
>根据需要在应用程序内添加文件。

项目中的所有文件应压缩为标准zip
存档。请注意manifest.webapp文件必须位于根目录下
zip归档文件（在归档文件中不包含父目录）。
然后可以将zip归档文件安装到DHIS2中，如您在
下一节。

## 将应用程序安装到DHIS2中

 <!--DHIS2-SECTION-ID:apps_installing_apps-->

可以通过将zip文件上传到应用管理器中来安装应用。在，
服务→应用程序，单击* App Store *菜单项。
！[]（resources / images / apps / app-management.png）该应用可以通过以下方式上传：
按“浏览”按钮，然后选择zip包后，文件
自动上载并安装在DHIS2中。您也可以浏览
通过DHIS2 [应用程序商店]中的应用程序（https://www.dhis2.org/appstore）
并从那里下载应用。 DHIS2应用商店允许应用
搜索，查看，评论，请求功能，对
社区的应用程序。

## 启动应用程序

 <!--DHIS2-SECTION-ID:apps_launching_apps-->

安装后，您的应用程序将与菜单系统集成
可以在“服务”下和“模块概述”页面中进行访问。它
也可以从apps模块的主页访问。点击一个
列表中的应用程序以启动它。
