# 仪表盘和演示服务器 { #dashboard-and-demo-server } 

## 链接的Action Tracker仪表板和演示服务器

### 动作跟踪器应用简介 { #introduction-to-the-action-tracker-app } 

Action Tracker是利用瓶颈和计分卡的一部分
DHIS2分析功能可评估国家和国家以下各级的绩效
旨在改善卫生服务提供情况的关键优先干预措施
健康状况。这是一个有助于提高有效覆盖优先级的工具
通过跟踪为解决以下问题而采取的行动，在国家以下一级进行干预：
健康干预中关键瓶颈的根本原因。

Action Tracker App由HISP社区开发和维护
（奥斯陆大学（UiO），HISP坦桑尼亚和HISP乌干达）与
联合国儿童基金会。可从以下网址下载Action Tracker v1.0.0.rc.0。
[Dhis应用商店。]（https://play.dhis2.org/appstore/）当前兼容
DHIS2 2.28及更高版本。

![图 1.1-A：操作跟踪器仪表板的标准布局](../content/action_tracker/resources/images/image01.png){width=80%}

### 动作追踪器应用程序的优点 { #advantages-of-the-action-tracker-app } 

Action Tracker App可帮助跟踪为解决以下问题而采取的关键步骤的状态
 优先干预措施中关键瓶颈的根本原因。它内置于
 DHIS2与BNA，记分卡和根本原因分析应用程序一起使用
 系统分析，状态更新和后续行动以解决
 卫生服务交付中关键瓶颈的可能解决方案。

### 链接动作跟踪器应用的基本原理 { #rationale-for-the-linked-action-tracker-app } 

链接操作跟踪程序使卫生经理可以跟踪实施进度
建议解决方案的行动，并允许对这些行动进行审查和跟进
动作。遵循BNA，记分卡和根本原因分析应用程序的设计
DHIS2，最重要的是在DHIS2中设计动作跟踪器以完成
瓶颈分析的级联。

> __注意__
>链接的动作跟踪器应用程序依赖于BNA应用程序的实现。必须在Action Tracker应用程序上列出的所有操作都引用使用BNA应用程序识别的瓶颈。没有BNA应用程序，您将无法实施Action Tracker应用程序。

### 1.4访问链接的动作跟踪器 { #14-accessing-the-linked-action-tracker } 

本用户指南是使用链接的动作跟踪器应用记录的，
可在[DHIS2演示服务器]（https://scorecard-dev.dhis2.org/demo/）上找到。
在DHIS2演示服务器中设置了Action Tracker，并链接到
BNA，记分卡和根本原因分析应用程序。当前的演示服务器可以是
访问：<https://scorecard-dev.dhis2.org/demo/>
以及登录页面上提供的用户名和密码。

![图 1.4-A：记录和访问 Action Tracker 演示服务器](../content/action_tracker/resources/images/image02.png){width=50%}

该服务器托管在云中，可以通过以下方式在Internet上进行访问：
只要有互联网就可以从任何地方访问浏览器。


### 浏览动作跟踪器{＃browsing-action-tracker} <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/action_tracker/at-app-browsing.md -->

要浏览动作跟踪器应用，请使用登录名访问DHIS2演示服务器
页面上提供的凭据。登录后，在以下位置搜索Action Tracker
搜索栏。

![图 1.5.-A：单击“搜索应用”或“应用”图标以访问应用搜索选项](../content/action_tracker/resources/images/image03.png){width=60%}

![图 1.5.-B：在应用列表中搜索 Action Tracker 应用，或输入完整或部分应用名称“Action Tracker”](../content/action_tracker/resources/images/image04.png){width=60%}

点击动作跟踪器以加载动作跟踪器应用，加载后，
用户可以选择干预，期间，组织单位或修改图例
相应地

![图 1.5.-B：已加载的动作跟踪器应用](../content/action_tracker/resources/images/image05.png){width=70%}

#### 选择干预 { #selection-of-an-intervention } 

用户需要选择对其执行了瓶颈分析和根本原因分析的干预措施，并且现在希望跟踪改善该特定干预措施的措施。

1. 单击干预选项卡以显示所有可用干预的列表。
   ![图 1.5.1-A：提供干预选择访问的干预选项卡](../content/action_tracker/resources/images/image06.png){width=50%}

2. 单击已发现瓶颈的干预措施。该干预将被选择并显示在右侧。

![图 1.5.1-B：可供选择的可用干预措施列表](../content/action_tracker/resources/images/image07.png){width=50%}

3. 单击更新以保存干预

![图 1.5.1-A：干预措施的选择](../content/action_tracker/resources/images/image08.png){width=50%}

> __注意__
>选择错误的干预措施将不会在操作跟踪器上显示“根本原因分析”数据。

#### 期间选择 { #period-selection } 

“动作跟踪器”使您可以为固定时间段，相对时间段和扩展的相对时间段选择时间段。所有期间选择类型都从单击“期间”选项卡开始。

单击周期选项卡可显示选项
![图 1.5.3-A：点击期间可访问期间选择选项](../content/action_tracker/resources/images/image14.png){width=60%}

单击期间类型以选择所需的期间类型；固定期间或相对期间

![图1.5.3-B：点击选定的时间段(default monthly) to access period options](../content/action_tracker/resources/images/image15.png){width=60%}

选择所需的时间段。这将出现在右侧
![图 1.5.3-D：选择跟踪的首选时段](../content/action_tracker/resources/images/image16.png){width=60%}

#### 组织单位选择 { #organization-unit-selection } 

组织单位选择允许您选择要跟踪其动作的组织单位级别。这是进行根本原因分析的级别。

单击组织单位选项卡以访问组织单位选择选项

![图 1.5.4-A：访问组织单位选择选项](../content/action_tracker/resources/images/image19.png){width=60%}

选择所需的组织单位级别

![图1.5.4-B：组织单位的选择](../content/action_tracker/resources/images/image20.png){width=60%}

单击更新以保存所选的组织单位级别

![图 1.5.4-C：保存选择显示的组织单位](../content/action_tracker/resources/images/image21.png){width=60%}

> __注意__
>选择错误的组织单位级别将不会在操作跟踪器上显示根本原因分析数据

一旦选择并保存了组织单位，就可以从根本原因分析表中检索数据，并激活数据输入模块以允许输入和编辑动作跟踪器。

![图 1.5.4-D：在操作跟踪器中显示根本原因分析的信息](../content/action_tracker/resources/images/image22.png){width=60%}

#### 动作状态设置配置 { #action-status-settings-configurations } 

用户可以根据跟踪动作状态的阶段数来修改图例。当前，动作跟踪器有4种颜色代码，用于指示跟踪动作的级别。栗色表示“已取消”，黄色表示“进行中”，绿色表示“已完成”，红色表示操作“未完成”。

点击右上角的设置图标可以编辑动作状态设置
![图 1.5.2-A：访问图例配置选项卡](../content/action_tracker/resources/images/image10.png){width=40%}

![图 1.5.2-B：选择操作状态设置](../content/action_tracker/resources/images/image11.png){width=40%}

单击颜色选项卡以编辑颜色

![图1.5.2-C：编辑图例颜色](../content/action_tracker/resources/images/image12.png){width=40%}

将图例编辑为所需的图例名称。

![图1.5.2-D：编辑图例名称](../content/action_tracker/resources/images/image13.png){width=40%}

通过单击图钉设置默认图例。该引脚将变为绿色。这将是您开始动作跟踪后出现的图例

![图1.5.2-E：设置默认图例](../content/action_tracker/resources/images/image13a.png){width=40%}

单击更新以保存对图例所做的更改

![图 1.5.2-A：保存对图例配置的更改已完成](../content/action_tracker/resources/images/image13b.png){width=40%}

__注意：__

>对图例配置的访问取决于用户的访问角色

#### 1.5.3必填字段设置配置 { #153-mandatory-field-settings-configurations } 

单击右上角的设置图标以编辑“必填字段”设置

![图 1.5.3-A：访问必填字段设置](../content/action_tracker/resources/images/image13c.png){width=40%}

![图 1.5.3-B：选择必填字段设置](../content/action_tracker/resources/images/image13d.png){width=50%}

选择在操作跟踪期间应在列表上显示的必填字段。

![检查必填字段。](../content/action_tracker/resources/images/image13e.png){width=50%}

![点击“更新”保存对必填字段设置所做的更改。](../content/action_tracker/resources/images/image13f.png){width=50%}

__注意：__

>对“必填字段设置”配置的访问取决于用户的访问角色。



