---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.33/ReleaseNote-2.33.0.md"
revision_date: '2020-10-22'
---

# DHIS版本2.33发行说明 { #dhis-version-233-release-note } 

本文档重点介绍了DHIS2 2.33版的初始版本的主要功能。

## 分析功能 { #analytics-features } 

**多个地图和时间线**：在地图应用程序中，您现在可以在同一屏幕上渲染多个地图，以显示数据随着时间的变化。您还可以具有一个地图，该地图可以“播放”时间线上的数据更改以显示随时间的更改。这很有用，例如以显示爆发是如何随着时间传播的，或者服务的覆盖范围如何随时间而变化。

[演示]（https://play.dhis2.org/2.33.0/dhis-web-dashboard/#/xP1jtPjus1c）| [截屏1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/multiple_maps1.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/multiple_maps2.png）| [3]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/timeline.png）| [吉拉](https://jira.dhis2.org/browse/DHIS2-2255)

**单个值图表和仪表板项目**：您现在可以在数据可视化器中呈现单个汇总值。这种简单的可视化显示单个值，可以将其保存并添加到仪表板。这允许仪表板项目一目了然地提供基本信息，例如疾病的新病例数或当前缺货的设施数。 |

[演示]（https://play.dhis2.org/2.33.0/dhis-web-dashboard/#/xP1jtPjus1c）| [截屏1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/single_value_charts.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/single_value_dashboard_items.png）| [吉拉](https://jira.dhis2.org/browse/DHIS2-3536)

**具有事件报告中多个阶段数据的患者行列表**：现在，您可以基于注册创建患者或被跟踪实体实例的列表，在单个表格中显示任意多个阶段的数据。如果是疾病监测患者，则通常是人口统计学数据（患者/ TEA），初始临床检查和诊断（阶段1），标本跟踪和实验室结果（阶段2x），病例调查（阶段3x）访视阶段和最终结果阶段，都在一个表中。

[屏幕快照1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/ Patient_line_listing.png）| [吉拉](https://jira.dhis2.org/browse/DHIS2-7459)

**改进了事件报告中的日期报告**：现在，事件报告可以显示注册日期和事件日期以及事件程序阶段的日期。它还可以显示这些日期的描述，而不仅仅是“事件日期”。这可以在程序中配置，例如作为“出生日期”或“产后访问日期”。

[屏幕快照1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/improved_date_reporting.png）| [吉拉1]（https://jira.dhis2.org/browse/DHIS2-2480）| [2](https://jira.dhis2.org/browse/DHIS2-2757)

** Google Earth Engine层**：Google Earth Engine对温度和降水层进行了一些改进。以前，加载多年的每周时间花了很长时间。添加了两个下拉菜单，一个下拉菜单用于年份（默认为最新），另一个下拉菜单用于一周。对于温度层，数据集已更新为包括最近的时间段。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/earth_engine_layers.png）| [吉拉1]（https://jira.dhis2.org/browse/DHIS2-6321）| [2](https://jira.dhis2.org/browse/DHIS2-6993)

## 跟踪器和事件功能 { #tracker-and-event-features } 

**性能和稳定性改进**：此版本提供了显着的性能和稳定性改进，尤其是在事务处理和查询优化方面：

- 已对该系统进行了审查，以最大程度地减少昂贵的读写事务数量，这会影响整体性能并可能导致数据库死锁。

- 跟踪器属性唯一性检查性能已得到优化。

- 跟踪器通知是异步的，以避免阻塞。

- 跟踪实体实例审核是异步的，以避免阻塞。

- 删除了对跟踪的实体实例，注册和事件的昂贵的循环检查。

- 删除了在导入期间检查数据元素访问权限的昂贵循环。

- 检查数据库索引以确保相关索引用于数据密集型查询。

**基于跟踪器捕获中的用户分配的工作列表**：现在可以基于事件的用户分配来构建工作列表。此功能列出了跟踪的实体实例和过滤条件，并使其更易于查看和跟踪事件。工作清单可以合并到用户的正常工作流程中，从而可以进行计划，确定优先级，并专注于特定事件和特定TEI。

[屏幕快照1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/working_lists_user_assignment_tracker.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/predefined_working_list_user_assignment_tracker.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/open_existing_tracked_entity_instance_dashboard.html#simple_tracked_entity_instance_search）| [吉拉](https://jira.dhis2.org/browse/DHIS2-6053)

**捕获应用程序中的工作列表和用户分配**：类似于跟踪器捕获中的工作列表，现在可以将单个事件程序配置为允许事件的用户分配，并根据用户，日期，状态等过滤条件创建工作列表等

[演示]（https://play.dhis2.org/2.33.0/dhis-web-capture/index.html#/programId=VBqh0ynB2wv&orgUnitId=DiszpKrYNg8）| [截屏1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Capture_App_Working_Lists_2.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Capture_App_Working_Lists_1.png）| [文档1]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#capture_user_assignment）| [文档2]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#capture_working_lists）| [吉拉1]（https://jira.dhis2.org/browse/DHIS2-6048）| [吉拉2](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#capture_working_lists)

**捕获应用程序中的跟踪器程序列表**：捕获应用程序现在在程序选择器中列出了跟踪器程序以及单个事件程序。选择跟踪器程序会提供一个信息屏幕，说明该程序是在另一个应用程序中处理的，用户可以单击深层链接以在正确的组织单位和程序中打开跟踪器。此功能使用户可以在同一位置查看其所有程序，包括跟踪程序和事件程序。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Tracker_Programs_in_Capture_App.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#capture_tracker_programs）| [吉拉](https://jira.dhis2.org/browse/DHIS2-6018)

**程序所有权的显示**：所选程序中所有注册的当前所有权现在在注册小部件中显示为“拥有者”。所有权首先分配给将TEI注册到给定程序中的组织单位，然后通过使用“永久移动”选项引用TEI进行转让。单个TEI在不同程序中的所有权可能不同，例如，一个诊所可以跟进一名HIV感染者，而另一家诊所可以跟进同一名MCH患者。

拥有对TEI /程序的当前所有者的组织单位的访问权限的用户将对该TEI /程序组合的所有注册具有写权限。对当前拥有者的组织单位具有搜索访问权限的用户将有权搜索和找到TEI /程序组合。

[屏幕快照1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Ownership_1.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Ownership_2.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/manage_tracked_entity_instance_enrollment.html#）| [吉拉](https://jira.dhis2.org/browse/DHIS2-5968)

**跟踪器捕获中的重复数据删除标记**：现在，在跟踪器捕获中搜索被跟踪实体实例时，现在可以标记结果中可能存在重复项。标记重复项后，它会提醒您需要清除数据，并为在日常工作中使用数据的任何人提供信息。该数据还可用于将来的功能，以识别和合并重复项。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/duplicate_flagging_in_tracker_capture.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/open_existing_tracked_entity_instance_dashboard.html#flagging-tracked-entity-instance-as-potential-duplicate）| [吉拉](https://jira.dhis2.org/browse/DHIS2-6070)

**双向关系**：现在可以在跟踪器捕获中配置双向关系。关系表示跟踪器数据模型中两个实体之间的链接，并且在DHIS2中被视为基于关系类型的数据，类似于被跟踪实体实例基于被跟踪实体类型的方式。现在可以将关系定义为单向或双向，其中双向关系会在链接的实体（例如“母子”）的两侧创建自动关系。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Bidirectional_Relationships.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#relationship_model）| [吉拉](https://jira.dhis2.org/browse/DHIS2-5293)

**更新的图标库**：图标库已更新，包括534个可搜索图标，涵盖了与健康，农业，运输和教育相关的各种主题。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Icon_Library.png）| [吉拉](https://jira.dhis2.org/browse/DHIS2-5447?jql=text%20~%20icon%20ORDER%20BY%20updated%20DESC)

**图像调整大小**：现在可以通过API返回时调整在服务器中存储的图像的大小/降级，以减少将相关图像下载到DE，TE属性或选项时的带宽消耗，并最大程度地减少存储在Android数据库。当请求类型为image的数据值时，查询可以指定Small（256x256px）；中（512x512px）;大（1024x1024px）。

[文档]（https://docs.dhis2.org/master/zh/developer/html/webapi_tracker_api.html#webapi_events）| [吉拉](https://jira.dhis2.org/browse/DHIS2-4842)

**程序指示符和程序规则运行状况检查**：现在，在数据管理应用程序的完整性检查期间评估程序指示符和规则，以检查无效的表达式和过滤器；缺少动作或优先事项等等。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Program_Indicator_Health_Check.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/data_admin.html#dataAdmin_dataIntegrity）| [吉拉](https://jira.dhis2.org/browse/DHIS2-5750)

**程序规则中的Z分数计算**：现在，程序规则中提供了用于计算Z分数“身高体重”和“身高年龄”的标准功能。年龄权重的Z分数计算从2.32开始。这在某些情况下很有用，在这种情况下，临床医生会手工计算Z分数。 d2函数根据WHO身高体重指标提供的数据计算z得分。根据高度值，其值在-3.5至3.5之间变化。

[屏幕快照1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Z_Score_Weight_for_Height.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/Z_Score_Height_for_Age.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/configure_program_rule.html#program_rules_operators_functions）| [吉拉1]（https://jira.dhis2.org/browse/DHIS2-6579）| [2](https://jira.dhis2.org/browse/DHIS2-6578)

## 应用程序功能 { #apps-features } 

**“报告”应用**：新的报告应用已经过Beta测试，并进行了许多新改进。例如，标准报表现在可以链接，并且可以从URL打开。旧的报告模块已被删除。

[演示1]（https://play.dhis2.org/2.33.0/dhis-web-reports/#/）| [2]（https://play.dhis2.org/2.33.0/dhis-web-reports/index.html#/standard-report/view/fqERdm6UtkI?&ou=O6uvpzGd5pu）| [截屏]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/new-reports-app.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#using_reporting）| [吉拉](https://jira.dhis2.org/browse/DHIS2-7134)

**注册部分表格**：您现在可以在Tracker中为注册创建基于部分的表格。可以在维护应用程序中的跟踪器程序配置向导中“属性”部分>“创建注册表单”下完成配置。这样就可以创建基于节的跟踪器注册表单，而无需创建基于HTML的自定义表单。

[演示]（https://play.dhis2.org/2.33.0/dhis-web-maintenance/index.html#/edit/programSection/program/WSGAb5XwJ3Y）| [截屏]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/33/program-attribute-sections.png）| [文档]（https://docs.dhis2.org/master/zh/user/html/dhis2_user_manual_en_full.html#create-or-edit-a-tracker-program）| [吉拉](https://jira.dhis2.org/browse/DHIS2-4407)

## 发行信息 { #release-info } 

|发布信息|链接|
| --- | --- |
|下载发行版和样本数据库|https://www.dhis2.org/downloads|
|文档和Javadocs|https://www.dhis2.org/documentation|
|升级说明|[GitHub上2.33的升级说明](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.33/README.md)|
|有关JIRA上每个功能的详细信息（需要登录）|[https://jira.dhis2.org/issues/?filter=11153](https://jira.dhis2.org/issues/?filter=11421)|
|JIRA中已修复的错误概述（需要登录）|[https://jira.dhis2.org/issues/?filter=11159](https://jira.dhis2.org/issues/?filter=11422)|
|Github上的源代码|https://github.com/dhis2|
|演示实例|https://play.dhis2.org/2.33.0/|
|DHIS 2社区|https://community.dhis2.org/|
