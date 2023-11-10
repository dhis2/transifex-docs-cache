---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/android-releases/2.2/ReleaseNote-2.2.0.md"
revision_date: "2020-11-03"
---

# DHIS2 Android App版本2.2发行说明 { #dhis2-android-app-version-22-release-note }

[** DHIS2 Android Capture App版本2.2 **]（https://www.dhis2.org/android-2-2）提供了许多新功能，应用程序，改进和错误修复。此版本的主要新功能包括对数据集的验证规则，事件和TEI列表的新过滤器和排序，地图中的许多新可视化效果以及对设备数据库进行加密的可能性以及许多小的界面更改的支持从而带来更好的用户体验。

|重要更新信息| --- | |DHIS2 规则引擎使用的评估解析器已更新，您的某些程序规则可能会在 Android 应用程序中停止工作。 Web 界面可能会以不同的速度合并此更改，因此 Web 和 Android 中的行为可能会有所不同。请仔细阅读文档和有关 [**THIS**](https://community.dhis2.org/t/important-review-your-program-rules-before-updating-to-android-2-2 -in-product/39970?u=marta) 在生产环境中将您的应用程序更新到新版本之前发布。

该版本与[DHIS2版本2.34]（https://community.dhis2.org/t/dhis-version-2-34-is-released/39064）完全兼容。
您可以在下面找到详细的新功能和修复。

## 数据集 { #data-sets }

**验证规则：**该应用程序支持验证规则。验证步骤已集成到保存和完整流程中，并且当验证规则配置为强制性规则和可选规则时，应用程序均支持。该应用将显示带有错误的新卡，以帮助用户识别哪些值不正确。

[吉拉](https://jira.dhis2.org/browse/ANDROAPP-1174) | [Jira 2 ](https://jira.dhis2.org/browse/ANDROAPP-2999) | [Jira 3 ](https://jira.dhis2.org/browse/ANDROAPP-3000) | [Jira 4](https://jira.dhis2.org/browse/ANDROAPP-1157) | [Screenshots](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Validation+Rules.png)

## 事件的列表，过滤和排序 { #listing-filtering-sorting-of-events }

**事件和TEI列表的排序：**该应用程序现在支持事件和TEI列表的排序。排序与过滤器菜单集成在一起，并且允许用户按一个选定的参数以升序或降序对列表进行排序。排序适用于日期和组织单位，适用时适用于注册日期和状态。允许排序的屏幕是：

-   单项活动列表
-   TEI搜索屏幕列表（当TEI包含多个事件时，应用程序将根据最近的事件进行排序）
-   TEI仪表板事件列表

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2354) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Sorting.png)

**新过滤器-注册状态：**在“程序搜索”屏幕中，用户可以按注册状态过滤TEI列表。此过滤器不允许多选。用户一次不能过滤一个以上的注册状态。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3111) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Filter+Enrollment+Status.png)

**新过滤器-注册日期：**在“程序搜索”屏幕中，用户可以按注册日期（除了事件日期（已可用））过滤TEI列表。过滤器将使用注册日期的标签（如果有）。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3112) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Filter+Enrollment+Date.png)

**过滤器名称的更改：**先前的“ Period”过滤器已重命名，如下所示：

-   主屏幕和事件程序屏幕中的_日期_。
-   Tracker 程序屏幕中的_事件日期_。
-   保留为数据集的_Period_。

## 地图 { #maps }

**地图图层中的卫星视图：**用户将能够将地图背景更改为卫星视图。卫星视图是地图图层对话框中的一个选项。选中后，它将替换默认的背景图像。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2891) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Maps+-+Satellite+View.png)

** TEI程序地图中的事件层：**在跟踪程序中打开地图视图时，带有坐标的程序阶段将作为图层使用。选择程序阶段图层后，该阶段带有坐标的事件将与所选的其他图层一起显示在地图中。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-2979）| [屏幕快照]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Map+-+Event+layer+in+Tracker.png）

**在地图视图中显示TEI关系：**在跟踪器程序中打开地图视图时，带有坐标的TEI之间的关系将作为图层提供。当选择关系层，用坐标它们是关系的一部分将TEI将与选择的其它层被显示在地图上组合使用。关系的方向将被指向相应方向的箭头所代表。双向关联关系的两端都将带有箭头。

用户将能够从TEI仪表板关系选项卡在列表视图和地图视图之间切换。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3004) | [Jira 2](https://jira.dhis2.org/browse/ANDROAPP-3005) | [Jira 3](https://jira.dhis2.org/browse/ANDROAPP-3118) | [Jira 4](https://jira.dhis2.org/browse/ANDROAPP-3090) | [Screenshots](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Maps+-+Relationships.png)

**用于在地图视图中导航事件，TEI和关系的轮播：**具有TEI，事件或关系卡的轮播已添加到地图视图。轮播和地图将在两个方向上响应用户选择。如果用户在地图上选择一个对象，则轮播会将相应的卡片定位在屏幕上。如果用户在轮播上选择了一张卡片，则地图将居中于地图中的相应对象，并且地图中任何选定对象的图标将以稍大的尺寸标记。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-3172）| [吉拉2]（https://jira.dhis2.org/browse/ANDROAPP-3121）| [截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Map+Event+Card.png）

## 一般功能 { #generic-features }

**在输入事件时预先选择上一个组织单位：**在跟踪程序或事件程序中创建新事件时，如果用户为数据捕获分配了多个组织单位，则应用将预先选择组织单位用户上次选择的内容。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2335)

**在预定义的选项字段中禁用语法拼写：**对于使用选项集或类别的字段，禁用语法拼写。即使选项有拼写错误，该应用程序也不会显示警告。删除此警告的原因是，对于预定义选项，即使应用程序指出了错误，用户也无法纠正错误。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-3094）

**更改表单中长文本字段的颜色：**长文本值类型字段的背景较暗。它已更改为白色以使其与其他值类型对齐。
[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-2849）| [截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Data+Entry+Long+Text.png）

**使类别选项可搜索：**在程序中创建事件或使用类别强制数据集时，必须滚动长列表而不选择搜索，这会使数据输入速度变慢。当类别中的选项超过15个时，该应用程序现在将带有一个搜索框。在以下屏幕中实现：

-   活动列表类别选项组合过滤器
-   事件初始类别选项选择器
-   数据集列表类别选项组合过滤器
-   数据集初始类别选项选择器
-   TEI仪表板用于自动生成事件

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-2295）| [截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/CatOptionSearchable.png）

## 跟踪器功能 { #tracker-features }

**为新关系创建 TEI 时继承值：** 创建新 TEI 作为关系的一部分时，TEI 将继承跟踪实体属性配置中标有 _Inherit_ 参数的任何程序属性。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-3144）

## 用户体验和用户界面 { #user-experience-and-user-interface }

**重新设计事件和TEI卡：**对事件和TEI卡进行了改进，使其更加直观和实用。现在，这些卡片在前三个要显示的标记的值旁边显示属性或数据元素的名称。也可以扩展卡以显示其余的属性或数据元素，这些属性或数据元素以相同的格式显示。在TEI列表，TEI仪表板事件和地图轮播中的卡中，可以在Tracker程序中使用这些新卡。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2655) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/TEI+Cards.png)

**改进数据集屏幕：** 数据集屏幕已重新设计，标题信息已简化，并且在数据输入中添加了包含数据集详细信息（状态、期间、组织单位）的选项卡部分。数据集将始终在_数据输入_选项卡中打开。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-2550）| [屏幕截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/DataSet+Screen.png）

**禁用数据集中选项卡的水平滑动：**水平滑动将在数据集表内导航用户，但不会导航不同的选项卡。用户体验有时会令人困惑，并导致该部分的非自愿更改。更改部分需要用户显式单击secion标题菜单中的特定选项卡。

[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-3158）

**将事件状态图标更新为新设计：**新设计简化了图标，并使外观与应用程序的用户界面保持一致。所有图标都可以通过其形状来识别。颜色区分不再用于添加信息。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3206) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Event+Status+Icons.png)

**将同步图标更新为新设计：**新设计将删除仅按颜色区分的图标。所有图标都可以通过其形状来识别。当对象已经同步时，不会显示同步图标。
[吉拉]（https://jira.dhis2.org/browse/ANDROAPP-3123）| [截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.2/Sync+Status+Icons.png）

**改进了Android设置DHIS2 Web应用程序中同步参数的设置部分：**同步设置部分已经过重新设计和扩展，以适应新的Android设置DHIS2 Web应用程序中的设置。新的Android设置网络应用允许您为实施中的所有设备配置同步设置。集中配置设置后，它们将覆盖设备级别的设置。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2675) | [Web App Announcement](https://community.dhis2.org/t/new-dhis2-android-settings-web-app-version-1-0-is-released/39926) | [Web App Documentation](https://docs.dhis2.org/master/en/dhis2_android_capture_app/android-settings-app.html)

## 质量/安全性/性能 { #quality-security-performance }

**加密数据库：**：现在可以对android设备中的数据库进行加密，以增强对敏感信息的保护。此操作将影响与您的服务器同步的所有android设备的本地数据库（它不会加密DHIS2服务器数据库）。

默认情况下，Android 应用程序数据库未加密，但管理员可以在新的 Android 设置 DHIS2 Web 应用程序中检查_加密设备数据库_，以加密每个设备中存储的数据和元数据。加密数据库会对数据库容量和Android应用程序的性能产生影响。选择或取消选择此选项不会导致数据丢失（即使之前尚未与服务器同步）。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-588) | [Jira SDK](https://jira.dhis2.org/browse/ANDROSDK-3)| [Web App Announcement](https://community.dhis2.org/t/new-dhis2-android-settings-web-app-version-1-0-is-released/39926) | [Web App Documentation](https://docs.dhis2.org/master/en/dhis2_android_capture_app/android-settings-app.html)

**扩展的错误日志：**应用程序中的错误日志已扩展为包括在使用应用程序期间捕获的所有错误。错误日志在“设置”屏幕中可用，并且可以通过任何Android智能手机的默认选项（电子邮件，即时消息应用程序，SMS，复制文本...）进行共享。

**其他质量和性能改进**

[地图] 统一地图数据管理器 [Jira](https://jira.dhis2.org/browse/ANDROAPP-2991)

[地图] 统一几何实用程序 [Jira](https://jira.dhis2.org/browse/ANDROAPP-2990)

[地图] 库和地图视图初始化（一）-库初始化和结构 [Jira](https://jira.dhis2.org/browse/ANDROAPP-3017)

[地图]图书馆和地图视图初始化（II）-地图视图初始化[Jira]（https://jira.dhis2.org/browse/ANDROAPP-3018）

[Bitrise][ci] 创建每天启动两次的 PR 提醒 [Jira](https://jira.dhis2.org/browse/ANDROAPP-2971)

[功能测试][同步]数据集[Jira](https://jira.dhis2.org/browse/ANDROAPP-2995)

[功能测试][同步]事件[Jira](https://jira.dhis2.org/browse/ANDROAPP-2997)

[功能测试][tei 仪表板]注册[Jira](https://jira.dhis2.org/browse/ANDROAPP-3199)

[功能测试][同步] Tei [Jira](https://jira.dhis2.org/browse/ANDROAPP-2996)

[性能] 提高家庭性能 [Jira](https://jira.dhis2.org/browse/ANDROAPP-3189)

发行信息

| 发布信息 | 链接 |
| --- | --- |
| 从Google Play或Github下载应用 | [https://www.dhis2.org/install ](https://www.dhis2.org/app-store) |
| 文档和Javadocs | [https://www.dhis2.org/android-documentation](https://www.dhis2.org/android-documentation) |
| 有关JIRA上每个功能的详细信息（需要登录） | [2.2 功能特点](https://jira.dhis2.org/issues/?filter=11877) |
| JIRA修复的错误概述（需要登录） | [2.2 错误修复](https://jira.dhis2.org/issues/?filter=11878) |
| Github上的源代码 | [https://github.com/dhis2/dhis2-android-capture-app](https://github.com/dhis2/dhis2-android-capture-app) |
| 演示实例（用户/密码） | [https://play.dhis2.org/2.34/]（https://play.dhis2.org/2.34/）android / Android123 |
| DHIS 2社区 | [https://community.dhis2.org 移动社区](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Github上SDK的源代码 | [SDK 1.2.0](https://github.com/dhis2/dhis2-android-sdk/releases/tag/1.2.0) |
| Github上RuleEngine的源代码 | [SDK 2.0.6](https://github.com/dhis2/dhis2-rule-engine/tree/f3aae2a5420b2c73e7c34a86bf6f221e11c98b0e) |
