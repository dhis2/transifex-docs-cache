---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.34/ReleaseNote-2.34.0.md"
revision_date: '2020-10-22'
---

# DHIS版本2.34发行说明 { #dhis-version-234-release-note } 

本文档重点介绍了DHIS2版本2.34的初始版本的主要功能。该版本与DHIS2版本[2.1 Android Capture App]（https://community.dhis2.org/t/dhis2-android-capture-app-version-2-1-is-released/39065）完全兼容。

## 分析功能 { #analytics-features } 

**数据可视化器应用程序中的数据透视表：**数据可视化器应用程序现在支持数据透视表，这意味着数据透视表应用程序的功能已合并到数据可视化器应用程序中。数据透视表现在只是数据可视化器应用程序中的另一种可视化类型。这为用户提供了用于构建数据透视表的更直观的体验，并且更加无缝地允许在数据透视表和其他图表类型之间移动。数据透视表的性能也得到了显着提高，从而允许使用非常大的数据透视表，其数据量是传统数据透视表应用程序的至少三倍。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-7687）| [截屏1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/pivot_table_1.png）| [2]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/pivot_table_2.png）| [3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/pivot_table_3.png)

**维度建议：**在数据可视化器应用程序中，数据透视表现在支持“维度建议”，这意味着与所选数据元素相关的维度将在左侧面板中用绿点表示。

[屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/pivot_table_dimension_recommendation.png)

**持续分析表更新：** 分析表调度程序现在支持分析表的持续更新，提供“实时分析”体验。输入数据和数据在分析应用程序中可见之间的延迟现在只需几秒，而不是几小时或几天。引入了包含最新数据的新表分区，可以实现更快的更新。这可以通过选择_连续分析表_作业类型在_Scheduler_应用程序中进行配置。 _Delay in Seconds_ 字段指的是最新数据分区的每次更新之间的延迟（以秒为单位）。 _一天中的完整更新时间_字段是指一天中运行完整分析表更新的时间。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/continuous_analytics_table_job.png）| [文档](https://docs.dhis2.org/master/en/dhis2_user_manual_en/scheduling.html#continuous-analytics-table)

**渐进式缓存：**渐进式缓存通过创建新的缓存层来减少渲染仪表板和加速分析的时间。本质上，这使输入后无需运行分析表即可立即在分析中查看数据。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-8352）

**单一值的传说：**现在可以将图例添加到单一值图表类型。值的文本颜色由值所属的图例决定。这使用户可以更有效地传达价值观的相对绩效。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-8348）| [截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/single_value.png)

**改进的量规表：**量规表的实用性得到了极大的提高。现在，量规图表可以包括基线和目标线，将根据显示的值更改图表颜色的图例以及最小和最大数据范围。

[吉拉1]（https://jira.dhis2.org/browse/DHIS2-8330）| [2]（https://jira.dhis2.org/browse/DHIS2-7888）| [3]（https://jira.dhis2.org/browse/DHIS2-7887）| [截屏1]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/gauge_options.png）| [2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/gauge_chart.png)

**按数据透视表中的总计排序：**现在，您可以按数据透视表中的小计和总计列进行排序。

[屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/pivot_table_sort_by_totals.png)

**仪表板项目的视觉改进：**每个仪表板项目都有用于长名称的文字换行。现在，所有仪表板项目选项都可以通过菜单代替图标使用，从而为标题提供了更多空间，并使标题在仪表板中更加可见。

[屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/dashboard_item_title_menu.png)

**数据透视表和统计图类型可视化过滤器**：在可视化列表中，可视化_type_过滤器可用，可让您按数据透视表和统计图进行过滤。列表中的每一行都会显示一个代表可视化类型的图标，可以快速查看每种可视化的类型。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-8413）| [截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/visualization_type_selector.png)

**地图增强和WebGL **：2.34版中的映射引擎是全新的，并且基于[WebGL]（https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API）技术与以前的解决方案相比，性能更高。

[吉拉](https://jira.dhis2.org/browse/DHIS2-5846)

现在，“地图”中提供了以下主要功能：

*   **性能**：现在，我们能够在地图上同时显示数千个要素，并且地图的响应速度更快。

    [屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/map_performance_events.png)

*   **地图旋转和倾斜：**现在，您可以旋转和倾斜地图以增强数据视图。

    [屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/map_bing_maps_rotated.png)

*   **连续缩放**：缩放现在是连续的，使您可以将地图完美地适合您的内容，并避免了以前较大的缩放“步幅”。

*   **全屏视图：**现在可以在全屏模式下查看地图。这对于空间有限的仪表板地图特别有用。您可以单击地图右侧的全屏按钮以启用它。
*   ** Bing地图：**由于技术和法律问题，不再支持Google Maps，但我们提供了Bing的四张新基础地图，应该可以很好地替代。

    [屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/map_bing_basemap.png)
*   **甜甜圈群集**：我们增加了对“甜甜圈群集”的支持，如果您通过数据元素设置样式，它将显示事件群集的分布。


    [屏幕截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/map_donut_clusters.png）


## 跟踪器和事件功能 { #tracker-and-event-features } 

**性能和稳定性改进：**已进行了与性能和安全性有关的一系列改进：

*   跟踪器捕获性能：[Jira]（https://jira.dhis2.org/browse/DHIS2-8066）
*   监视基础结构：[Jira]（https://jira.dhis2.org/browse/DHIS2-6954）
*   改进的缓存：[Jira]（https://jira.dhis2.org/browse/DHIS2-7174）
*   各种错误修复：[吉拉]（https://jira.dhis2.org/issues/?jql=project%20%3D%20DHIS2%20AND%20issuetype%20in%20（错误％2C%20Epic％2C%20Feature％2C％20Test％2C％20Design）%20AND%20component%20in％20（%22%5BApp％5D ％20Tracker%20capture%22%2C%20%22％5BApp％5D%20Event%20capture%22%2C%20%22％5BApi％5D％20Tracker%22%2C%20%22％5BApi％5D%20Events%22%2C%20%22％5BApp％5D％20Capture％22）%20AND％20Sprint%20in％20（％22Tracker%202.34%20-％20MS1%22%2C%20%22Tracker%202.34%20MS2％22）%20AND%20status%20in％20（％22To％20Do%22%2C%20%22In％20Progress%22%2C％ 20Done％2C%20%22In％20Review％22）%20AND%20issuetypea0f08df6929 87fz03D％20Bug）
*   程序规则的Antlr解析：[Jira]（https://jira.dhis2.org/browse/DHIS2-7945）

**增强的审计服务：**现在为所有类型的元数据和数据存储了审计跟踪。审核跟踪默认情况下处于启用状态，并且可以在此_dhis.conf_配置文件中进行配置。该解决方案是集中式的，基于_Apache ActiveMQ [Artemis]（https://activemq.apache.org/components/artemis/）_异步消息代理。审核解决方案涵盖跨元数据，聚合数据和跟踪器数据的_create _，_ read _，_ update_和_delete_操作。当前可以从DHIS2数据库的_audit_表中检索审核日志。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-7837）| [文档](https://docs.dhis2.org/master/en/dhis2_system_administration_guide/audit.html)

** Capture应用程序中的预定义事件视图：**在Capture应用程序中，现在可以保存和共享自定义的预定义列表视图/事件过滤器。用户可以基于任何其他可过滤的属性（例如事件数据值，事件日期，受让人等）来保存命名过滤器。这可以是私有过滤器，也可以是共享的，以便其他用户可以查看和使用它。这种过滤器的一种用例是创建分配给已登录用户的事件的默认工作列表。

[吉拉]（https://jira.dhis2.org/browse/DHIS2-4440）| [截屏]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/dhis2_4440_working_list_assigned_to_me.png）| [文档](https://docs.dhis2.org/master/en/dhis2_user_manual_en/using-the-capture-app.html#predefined-list-views)

**跟踪器捕获亲戚：**现在，用户可以在其搜索范围内搜索关系并将其链接到任何跟踪的实体实例。以前，只能在用户报告组织单位内搜索和链接关系。在Covid-19联系人跟踪中，在不同组织中进行搜索非常有用，因为该联系人可能居住在该国的另一部分。


[吉拉]（https://jira.dhis2.org/browse/DHIS2-7226）| [截屏]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/dhis2_7226_search_tei_relationship_widget.png）| [文档](https://docs.dhis2.org/master/en/dhis2_user_manual_en/using-the-tracker-capture-app.html#add-a-relationship-to-a-tei)


## 应用程序功能 { #apps-features } 

**数据批准：**数据批准功能作为名为_Data批准_的单独应用重新引入。它提供的功能与以前可通过“报告”应用访问的功能相同。它允许按数据集和时间段批准数据。我们正在使用新技术栈开发一个新的批准应用程序，它将支持数据批准工作流模型。

[屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/data_approval_app.png)

** App Hub：** App Store已更名为App Hub。 App Hub已被重写，以支持改进的应用程序管理。 DHIS2 2.34默认使用新的应用程序中心（[https://apps.dhis2.org]（https://apps.dhis2.org））。旧版App Store中的应用程序已尽可能迁移到新的App Hub。 DHIS2的早期版本使用的旧App Store链接将继续起作用，但在不久的将来将无缝地重定向到新的App Hub。应用开发者现在应该使用新的应用中心来共享您的应用。

[https://apps.dhis2.org](https://apps.dhis2.org)

**数据导入导出中的属性ID方案：**导入导出应用程序现在允许选择用于数据导入和导出的基于属性的标识符方案。

[截图]（https://s3-eu-west-1.amazonaws.com/content.dhis2.org/releases/screenshots/34/data_import_export_attribute_id_schemes.png）| [吉拉](https://jira.dhis2.org/browse/DHIS2-7495)


## API功能 { #api-features } 

**用于分析可视化的新组合端点**：已弃用_reportsTables_和_charts_端点，而使用新的和合并的_visualizations_端点。

[文件](https://docs.dhis2.org/master/en/dhis2_developer_manual/web-api.html#visualization)



## 发行信息 { #release-info } 

|发布信息|链接|
|:---|:---|
|下载发行版和样本数据库|https://www.dhis2.org/downloads|
|文档和Javadocs|https://www.dhis2.org/documentation|
|升级说明|[GitHub上2.34的升级说明](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.34/README.md)|
|有关JIRA上每个功能的详细信息（需要登录）|[2.34功能](https://jira.dhis2.org/issues/?filter=11845)|
|JIRA修复的错误概述（需要登录）|[2.34错误](https://jira.dhis2.org/issues/?filter=11846)|
|Github上的源代码|https://github.com/dhis2|
|演示实例|https://play.dhis2.org/2.34.0/|
|码头工人|`docker pull dhis2 / core：2.34.0` <br> _有关更多docker映像变体的信息，请参见[dockerhub]（https://hub.docker.com/repository/docker/dhis2/core）_|
