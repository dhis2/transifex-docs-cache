---
applicable_txt: 适用于2.5.0版本
author: 记分卡应用团队
commit: null
date: null
edit_url: "https://github.com/hisptz/unicef-apps-docs/blob/master/src/commonmark/en/dhis2_scorecard_manual_INDEX.md"
keywords:
    - DHIS2
    - HISP
logo: 资源/图像/image120.png
month: 十月
revision_date: "2021-10-04"
subauthor: 与 HISP UiO、HISP 坦桑尼亚和 HISP 乌干达合作
template: single.html
title: 交互式记分卡应用程序的 DHIS 2 手册
version: 2.5.0
year: 2021
---

<!--DHIS2-SECTION-ID:index-->

## 记分卡应用介绍 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/introduction-to-scorecard.md --> { #introduction-to-the-scorecard-app }

### 目标受众 { #intended-audience }

本指南适用于计划实施者，他们旨在在国家或组织级别配置计划（例如 RMNCH）记分卡，以供其他用户用来衡量其级别上商定指标的绩效。在大多数实施中，一个程序曾经有一个国家记分卡，其中包含一系列商定的指标，并在国家层面进行配置，而国家和地方层面的其他用户共享只读访问权限，以限制他们进行任何更改。

在本指南中，我们将在国家/地区提及实施者和普通用户。除了设置记分卡外，具有管理权限的用户应与用户或用户组共享记分卡。具有权限访问的用户可以像普通用户一样使用记分卡，具有访问配置的记分卡、访问和下载输出以及与他人共享的权限。要以普通用户身份访问，请访问 https://docs.google.com/document/d/1CI4A6MPr9Gr-KyuEnOFosfrdAG8Qdm1B/edit。最终用户手册。

### 记分卡App { #background-of-scorecard-app }的背景

在卫生部等公共卫生机构中，记分卡提供了一种有用且标准化的方法，用于使用交通信号灯颜色代码进行分析，将相关指标组合到一个表格中。记分卡可以提供健康计划（例如疫苗接种计划）绩效的整体视图，突出成功、弱点和需要改进的领域。

在 DHIS2 系统中，记分卡可以通过两种不同的方式创建，如 dhis 2 网站 http://www.dhis2.org 中所述

-   数据透视表
-   记分卡应用

本指南主要关注记分卡应用。记分卡应用程序的优势在于它针对高级记分卡分析进行了调整，由 HISP 社区开发和维护，与使用的数据透视表应用程序相比，它使用来自不同实现的大量不同用例来提出解决方案用于基本记分卡分析，由 Dhis2 核心团队开发和维护。虽然记分卡应用程序和数据透视表应用程序都为用户提供了下载和离线使用记分卡并在 DHIS2 仪表板上共享的选项，但记分卡应用程序提供了更高级的控制和功能，可以轻松创建和分析数据的多个元素和维度。

此外，记分卡应用程序通过在记分卡仪表板中包含瓶颈指标以及使用数据透视表、图表和地图等广泛的可视化工具分析数据，提供了级联分析的机会。此版本的记分卡旨在解决记分卡版本 2.4.1 中遇到的限制，包括适应同一指标的国家和地区目标的能力、在保持上级组织单位的同时对指标进行排序的能力、改变的能力等功能记分卡列表的布局，按特定设施类型、所有权和期间过滤记分卡的能力，对表现好或差的人进行排名等。修订后的记分卡应用程序考虑了用户的反馈和记分卡实施五年内的新用例。

### 记分卡 { #users-of-the-scorecard } 的用户

任何有权访问 DHIS2 系统的人都可以使用记分卡应用程序。任何有权访问 DHIS2 的人都可以创建记分卡。如果有人创建了记分卡，则只有创建者/所有者才能访问它，除非与 DHIS2 系统内的其他用户共享访问权限。大多数组织和国家更愿意为每个特定项目设置一个记分卡，其中选择并批准特定项目记分卡（如 RMNCH）的指标列表及其分界点。然后，来自组织或国家级别的程序的用户的任务是创建记分卡，并将其访问权限限制为只读给其他用户，以便他们只能可视化以评估程序性能。

从这个角度来看，创建和维护程序记分卡的人称为实施者，而对程序记分卡具有只读访问权限的任何其他用户称为普通用户。

![](content/scorecard/resources/images/important.png)**重要**：在本指南中，实施者是指创建和维护特定记分卡的用户，并且只向其余用户提供视图访问权限；而任何其他只能查看特定节目记分卡而没有编辑能力的用户被称为普通用户。

## 登录DHIS2系统<!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/accessing-scorecard-app.md --> { #login-dhis2-system }

要访问记分卡，用户必须使用登录凭据登录到 DHIS2 系统。当您有可用的互联网连接时，您可以使用互联网浏览器访问该应用程序。互联网浏览器； Google Chrome、Mozilla Firefox、Safari 可用于访问该应用程序。但是，推荐的网络浏览器是 Google Chrome。

![登录DHIS2系统](content/scorecard/resources/images/Figure1.png)

成功登录后，用户将登陆 DHIS2 仪表板或应用程序列表，具体取决于系统的设置。然后，用户将需要从 DHIS2 全局菜单访问记分卡菜单。

![在DHIS2系统中定位记分卡应用程序。](content/scorecard/resources/images/Figure2.png)

### 记分卡配置的元数据 { #metadata-for-scorecard-configuration }

记分卡应用程序从通用 DHIS2 数据源中借用其元数据，并使用它来创建数据存储，以便于分析和可视化。指标和指标组等记分卡应用元数据使用 DHIS2 指标维护应用程序进行管理。

### 创建记分卡 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/creating-scorecard.md --> { #creating-the-scorecard }

用户必须单击记分卡应用程序以获取已创建记分卡的列表，或者有权创建新记分卡。要创建新的记分卡，用户必须单击屏幕右上角的“添加新记分卡”按钮。

![在 DHIS2 系统中创建新记分卡。](content/scorecard/resources/images/Figure3.png)

#### 填写记分卡{ #filling-up-the-general-information-of-the-scorecard }的一般信息

用户应单击记分卡应用程序将其打开并有权进行配置。然后根据字段标签在“常规”选项卡下的每个字段中填写相应字段中的信息。

![在一般选项卡下填写基本信息。](content/scorecard/resources/images/Figure4.png)

#### 图例定义 { #legend-definition }

要设置图例定义，用户必须向上滚动页面并更改颜色代码并通过单击可用的颜色选择器关联图例定义。要添加更多图例定义，用户需要单击图例定义下方的“添加项目”按钮。要删除图例，用户需要使用每个图例旁边的删除按钮。

![在 DHIS2 记分卡创建中定义图例。](content/scorecard/resources/images/Figure5.png)

#### 在记分卡 { #creating-group-for-related-indicators-in-the-scorecard } 中为相关指标创建组

要选择指标组、指标和表现不佳、平均和良好的分界点，用户必须导航到“数据配置”选项卡。用户应该单击“添加”组才能添加用于记分卡配置的项目。在右侧，有指导生成记分卡所需完成的项目的信息。

![在记分卡生成中添加指标组。](content/scorecard/resources/images/Figure6.png)

要编辑单击“添加组”按钮后创建的默认组，用户必须单击默认组名称（组 1）的编辑图标，并写入适当的组名称并保存。

![[在记分卡设置期间编辑组名。](content/scorecard/resources/images/Figure7.png)

#### 将指标添加到组 { #adding-indicators-to-the-group }

然后用户可以通过单击添加项目按钮并从列表中选择指标并移动到右侧，单击“添加按钮”将它们添加到记分卡中来添加指标。

![选择指标并添加到组。](content/scorecard/resources/images/Figure8.png)

注意：在一个组中添加指标组和指标的过程可以如图 8 所示重复，直到所有组及其指标都用完。

保存选定的指标后，每个选定指标的指标布局和截止点、有效差距的数量以及显示有效差距的箭头和显示颜色的选项都可供管理用户使用。

![在 DHIS2 记分卡设置中设置选定指标的截止点。](content/scorecard/resources/images/Figure9.png)

#### 通过减小值{ #configuration-of-indicators-whose-performance-is-good-by-decreasing-the-value }来配置性能良好的指标

对于在百分比数量减少时表现良好的指标，可以通过取消选中仅显示在顶部指标截止点上的“High is Good”选项来简单地配置指标。

![以递减数字衡量良好性能的指标配置。](content/scorecard/resources/images/Figure10.png)

#### 配对相关指标{ #paring-related-indicators }

对于相关指标的配对情况，点击指标右侧的超链接即可轻松完成。这有助于节省记分卡布局的水平空间并将相关指标放在一列中以进行比较。

![DHIS2系统记分卡配置中配对相关指标](content/scorecard/resources/images/Figure11.png)

#### 选择突出显示的指标 { #selecting-highlighted-indicators }

要在显示记分卡时为应突出显示的指标选择指标，用户必须导航到“突出显示的指标”按钮并添加。通过突出显示的指标，用户可以在生成的记分卡之上快速查看此类指标的表现。

![为记分卡设置突出显示的指标。](content/scorecard/resources/images/Figure12a.png)

![设置记分卡的共享设置。](content/scorecard/resources/images/Figure12b.png)

#### 共享访问 { #sharing-access }

记分卡应共享给个人用户或用户组，以供他们访问。这是 DHIS2 中的一个非常重要的概念，即除了创建的对象之外，任何对象都不能被任何人访问，除非它被授予公共访问共享，或者与用户或一组用户共享。记分卡共享可以扩展来决定共享到哪个级别的访问权限。例如，一个程序可以配置一个地区记分卡，并且只与地区级别以及用户组共享。对于正在配置的记分卡，已为测试用户分配了读取访问权限，以允许拥有测试帐户的用户仅浏览记分卡而不进行任何更改。

![设置记分卡的共享设置。](content/scorecard/resources/images/Figure13.png)

#### 设置选项 { #setting-the-options }

要在任何用户在自己选择选项之前加载记分卡时选择默认显示的选项列表，用户可以通过选择显示窗口右上角的选项按钮来配置记分卡。即使普通用户做出他/她自己的选择并随后决定重新加载记分卡，所选选项仍然存在。

![设置记分卡的默认选项。](content/scorecard/resources/images/Figure14.png)

### 保存配置并加载记分卡 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/saving-configurations.md --> { #saving-configuration-and-load-the-scorecard }

用户需要保存所做的配置并加载记分卡以将其可视化，就像其他普通用户一样（图 15）。这将最终确定记分卡配置并将其保存到系统中，以供具有共享访问权限的用户访问。

![保存更改并加载记分卡。](content/scorecard/resources/images/Figure15.png)

## 查看记分卡应用程序分析输出 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/viewing-scorecard.md --> { #viewing-the-scorecard-app-analysis-outputs }

### 目标受众 { #intended-audience }

第 3 章和之后的其他内容适用于没有访问权限的记分卡应用用户来编辑他们正在查看的特定仪表板。这些用户有权访问配置的记分卡、访问和下载输出以及与他人共享。要创建新的记分卡，请参阅第 1 章和第 2 章，重点介绍想要创建仪表板或有权编辑他们正在访问的仪表板的用户。

### 记分卡应用程序 { #rationale-for-the-scorecard-app } 的基本原理

DHIS2 等健康管理信息平台的使用帮助健康管理者收集、监控和使用数据进行规划和决策。并非所有健康管理人员都具备执行数据分析和随时间推移生成趋势的分析技能。使用记分卡之类的工具为这些管理人员提供了一种工具，该工具可以自动生成分析并以允许他们做出决策的方式显示它们。

与基于 DHIS2 的类似应用程序相关，例如瓶颈分析 (BNA) 和动作跟踪器应用程序；记分卡为健康管理人员提供了一种跟踪用户配置的无限数量指标绩效的方法。而BNA允许基于人力资源、商品、地域覆盖、初始利用、持续利用和有效利用的指标配置；记分卡应用程序使用户能够根据自己的喜好跟踪和分组指标。

### 记分卡应用程序 { #advantages-of-the-scorecard-app } 的优点

记分卡应用程序为您提供不同指标的快速可视化输出，从而轻松观察性能和趋势。使用默认的传统颜色代码红色（表示性能不佳）、黄色（表示正常）和绿色（表示良好），用户可以很容易地找到需要特别注意问题的指标和位置。

![](content/scorecard/resources/images/note.png)**注**：虽然红色、黄色和绿色被用作默认颜色，但用户可以为指示器输出使用不同的颜色代码。

### 记分卡应用元数据 { #scorecard-app-meta-data }

记分卡应用程序从通用 DHIS2 数据源中借用其元数据，并使用它来创建数据存储，以便于分析和可视化。指标和指标组等记分卡应用元数据使用 DHIS2 指标维护应用程序进行管理。

![指标维护应用](content/scorecard/resources/images/Figure16.png)

## 记分卡应用架构 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/scorecard-app-architecture.md --> { #scorecard-app-architecture }

记分卡应用程序建立在这样一种架构之上.

### 全局 DHIS2 菜单 { #global-dhis2-menu }

使用记分卡应用程序时，全局 DHIS2 菜单可在其通常位置访问。用户可以使用全局菜单访问其他应用程序并退出系统。大多数应用程序通知将弹出 DHIS2 全局菜单所在的顶部位置。

![通过 DHIS2 全局菜单访问记分卡应用程序。](content/scorecard/resources/images/Figure17.png)

### 选择记分卡以跟踪 { #selecting-scorecard-to-track }

从全局 DHIS2 菜单中选择记分卡应用程序后，您可以选择要跟踪和可视化的记分卡。

![供用户选择的记分卡列表。](content/scorecard/resources/images/Figure18.png)

#### 更改记分卡列表布局 { #changing-scorecards-listing-layout }

您单击用于管理显示布局的选项以将记分卡的显示从水平列表更改为垂直列表，反之亦然

![用于检查记分卡列表选项的菜单选项。](content/scorecard/resources/images/Figure19.png)

![计分卡列表的替代布局。](content/scorecard/resources/images/Figure20.png)

#### 搜索记分卡 { #searching-for-the-scorecard }

如果在搜索记分卡名称列表中看到它，您可以选择要访问的记分卡，方法是在搜索栏选项中键入名称。

![ 用于搜索记分卡的选项。](content/scorecard/resources/images/Figure21.png)

除了使用搜索选项，您还可以使用列表底部的导航栏从记分卡列表的一页移动到另一页。

## 访问和翻译记分卡 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/accessing-and-translating-scorecard.md --> { #accessing-and-translating-the-scorecard }

记分卡应用程序可以在应用程序菜单中找到。如果您的 DHIS2 实例中尚未安装应用程序或安装有问题，请参阅实施指南的安装说明以获得进一步指导，或联系 DHIS2 管理员寻求帮助。

![在 DHIS2 应用程序菜单上访问记分卡应用程序。](content/scorecard/resources/images/Figure22.png)

### 选择记分卡 { #selecting-the-scorecard }

要选择要可视化的记分卡，请单击 View 选项，如下面的图 10 所示。如果您没有看到想要可视化的记分卡，请参阅第 2.4.2 节了解如何搜索记分卡。

![用于选择要可视化的记分卡的菜单选项。](content/scorecard/resources/images/Figure23.png)

单击“查看”选项后，您将被带到您选择的记分卡的主页。记分卡的主页将包括以下选项：

**_组织单位的管理：_** 本部分将为您提供选择位置（组织单位）的选项，您要为其可视化记分卡

**_期间管理：_** 本部分将为您提供您希望为显示、导出和帮助选项完成记分卡分析的期间的选项：本部分将提供用于管理记分卡分析输出应如何显示为的选项以及用于导出和/或打印记分卡输出的选项。帮助选项提供了有关如何使用记分卡应用程序的不同菜单选项的内置导航指南。

**_记分卡分析输出8_**：此部分将输出记分卡的所有选定组织单元和指标或指标组的分析结果。输出部分前面是颜色编码的键，用于解释应如何解释每个记分卡。

![记分卡的主要部分，包括组织单位、期间、显示选项和分析输出的管理。](content/scorecard/resources/images/Figure24.png)

### 组织单位管理 { #organization-units-management }

此部分将允许您选择要在其上进行记分卡分析的组织单位。您将能够选择三个选项来选择显示记分卡的组织单位；按组织单位进行第一次选择（选择要查看记分卡的特定位置），按级别进行第二次选择（选择组织单位级别，例如要查看记分卡的地区或地区）和按组织单位组进行第三次选择（选择组织单位组，例如，医院查看记分卡）

![要查看的组织单位的选择选项。](content/scorecard/resources/images/Figure25.png)

选择要查看的组织单元的类别后，您将能够选择要选择的特定子选项。按组织单位选择的第一个选项，您将可以选择一个子单元查看，对于按级别选择的第二个选项，您将可以选择要查看的特定级别，对于选择的第三个选项组，您将能够选择特定的组织单位查看

![选择组织单位、级别或组后要查看的组织单位的选择选项。](content/scorecard/resources/images/Figure26.png)

要在上面的图 12 和 13 中列出的选择选项之后选择特定的组织单位，您可以单击特定组织单位的名称来选择组织单位以可视化其记分卡。

![选择特定的组织单元进行可视化。](content/scorecard/resources/images/Figure27.png)

选择要查看的组织单位选项后，单击更新以确认选择并更改记分卡显示以匹配您选择的选定组织单位。

### 经期管理 { #periods-management }

期间管理部分允许您选择要为其可视化仪表板的特定期间或期间。要获得选择周期的选项，请单击周期选择选项卡（图 15）

![为记分卡可视化选择首选时段的选项。](content/scorecard/resources/images/Figure28.png)

您可以使用相对期间或固定期间选项来选择期间。期间选项将列在左侧。要选择时间段，请双击时间段。一旦选择（双击），周期将移至右侧（下图）。要取消选择期间（从右侧），请双击它。

![为记分卡可视化选择相对时期的选项。](content/scorecard/resources/images/Figure29.png)

![为记分卡可视化选择固定期间的选项。](content/scorecard/resources/images/Figure30.png)

### 显示和导出选项 { #display-and-export-options }

此显示管理部分允许您选择显示选项以确定记分卡输出的显示方式。

![用于管理记分卡上应显示的内容以及内容应如何排序的选项。](content/scorecard/resources/images/Figure31.png)

记分卡显示选项允许您管理以下内容：

**_Legend:_**选择是否显示图例 **_Title:_** 选择是否显示记分卡标题 **_Item number:_**选择组织单位列表是否应包括项目编号**_空行：_**选择是否应显示具有零值的记分卡输出 **_显示层次结构：_**在显示记分卡输出时显示组织单位层次结构的选项 **_平均列：_**选择是否显示平均值列是否应显示 **_Average 行：_** 选择是否应显示平均行 **_Highlighted 指标：_** 用于显示作为感兴趣指标添加到跟踪的指标的选项。 **_平均：_**允许您选择显示所有组织单位或仅显示低于或高于平均水平的组织单位。 **_Options:_**选择是否要显示与要显示的指标的颜色编码输出相关的变化（性能增加或减少）和实际性能数据（数字）的箭头

显示和导出部分还包括下载记分卡的选项。单击“下载”图标以获取允许下载的文件格式选项。单击首选文件格式，然后将要下载的文件保存到您的首选位置（根据您的浏览器设置）。记分卡可以下载为 Excel、PDF、CSV 或 ALMA 选项（JSON 或 CSV 元数据）

![下载记分卡输出或元数据的选项。](content/scorecard/resources/images/Figure32.png)

对于每个显示，此部分还允许您刷新记分卡并获取最新的分析输出。如果您在查看记分卡时正在进行更改或需要清除缓存的显示，这可能是相关的。

![使用最新分析输出重新加载记分卡的选项。](content/scorecard/resources/images/Figure33.png)

### 记分卡分析输出 { #scorecard-analysis-outputs }

此部分用于根据第 3.1.1、3.1.2 和 3.1.3 节中选择的选项显示记分卡输出。

![记分卡分析输出部分。](content/scorecard/resources/images/Figure34.png)

记分卡分析输出部分有以下主要部分

*标题：*显示记分卡的标题 *图例描述：*描述使用的颜色代码和性能提高或降低的标记 *组织单位列表：*显示分析的组织单位列表，并可选择搜索特定组织单位以显示 *记分卡输出：*包含有关指标组（如果添加）、指标名称、分析周期和分析的颜色编码输出以及相应性能的信息。

## 记分卡应用程序内置支持和维护选项 <!-- DHIS2-EDIT:https://github.com/hisptz/unicef-apps-docs/edit/master/src/commonmark/en/content/scorecard/support-and-maintanace-options.md --> { #scorecard-app-built-in-support-and-maintenance-options }

### 帮助导航 { #help-navigation }

除了本用户指南之外，记分卡应用程序还有一个内置的帮助导航选项，可为您提供说明。要访问帮助指南，请单击帮助按钮，然后按照突出显示不同记分卡选项及其功能的步骤进行操作。

![访问帮助导航菜单。](content/scorecard/resources/images/Figure35.png)

![使用帮助菜单的导航指南示例。](content/scorecard/resources/images/Figure36.png)

使用上一个或下一个按钮从帮助导航的一个选项导航到另一个选项。要结束帮助导航，您可以单击跳过选项

### 清除应用程序缓存 { #clearing-application-cache }

如果记分卡操作跟踪器应用程序加载时间过长，并且您的网络不是很慢，请确保您已清除浏览器缓存。

记分卡应用充分利用缓存文件以获得更好的离线体验，因此，在安装更高版本时，记分卡应用可能会使用旧版本的缓存文件，从而在加载时崩溃。

清除应用程序缓存和浏览器界面的方法各不相同
浏览器到浏览器；例如Mozilla Firefox的键盘
快捷方式是“ CTRL + SHIFT + DELETE”，而对于谷歌浏览器，键盘
快捷方式是“ CTRL + SHIFT + J”。

访问清除浏览器缓存的界面可以通过以下方式进行：

• 谷歌浏览器​：进入右上角的菜单图标，点击打开，进入更多工具菜单，选择“清除浏览数据”。打开界面后，确保“清除以下项目”设置为“开始时间”。

• Mozilla Firefox​：进入右上角的菜单图标，点击打开，进入->图书馆，进入历史，选择“清除最近的历史”。打开界面后，确保“清除时间范围”设置为“全部”，并展开“详细信息”选项以显示所有详细信息选项。在清除浏览数据或最近历史记录后，勾选“缓存”、“Cookie”、“托管应用数据”或“离线网站数据”。清除所有缓存的文件、cookie 和本地存储的数据。

![Google chrome 和 firefox 中的菜单图标。](content/scorecard/resources/images/Figure37.png)

![](content/scorecard/resources/images/note.png)**_注意_**：_这些也会清除您在浏览器中访问的其他网站的所有缓存信息和 cookie。_

![用于清除浏览器缓存的谷歌浏览器界面。](content/scorecard/resources/images/Figure38.png)

![用于清除浏览器缓存的Mozilla firefox界面。](content/scorecard/resources/images/Figure39.png)

### 记分卡应用程序错误消息 { #scorecard-app-error-messages }

记分卡应用程序包含可能发生的预期错误的错误消息。

**未找到记分卡错误：** 当提供的记分卡 ID（在地址栏上）与系统中存在的任何记分卡配置不匹配时，会出现此错误（如下图所示）。当用户通过在地址栏上粘贴链接来访问记分卡时，很可能会发生此错误。要解决此错误，请确保提供的链接适用于有效的记分卡配置。

![未找到记分卡错误消息。](content/scorecard/resources/images/Figure40.png)

**访问被拒绝错误：** 当用户尝试访问他无权访问的记分卡时，会出现此错误（如下图所示）。当用户通过在地址栏上粘贴链接来访问记分卡时，很可能会发生这种情况。要解决此问题，请确保当前用户具有对记分卡的正确访问权限。

![拒绝访问错误消息。](content/scorecard/resources/images/Figure41.png)

**一般错误：**由于各种原因（例如网络问题），应用程序使用过程中可能会出现其他错误。错误将如下图所示。将显示一条简单的错误消息。如果错误是技术性的，当用户单击查看日志按钮时可以查看描述性消息。这些错误中的大多数可以通过刷新应用程序（通过刷新按钮或浏览器的刷新按钮或 CTRL + R）来解决

![一般错误页面。](content/scorecard/resources/images/Figure42.png)
