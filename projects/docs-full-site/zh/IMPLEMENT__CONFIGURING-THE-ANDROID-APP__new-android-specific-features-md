---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/new-android-specific-features.md"
revision_date: "2021-07-29"
---

# 通用功能 { #capture_app_generic }

## 登录 { #capture_app_generic_login }

有两种访问应用程序的方法：

1. 手动：用户必须输入要使用的服务器的相应URL，然后输入用户名和密码。

   > **Note**
   >
   > Take note that login is only possible with servers from version 2.29.

2. QR：用户可以使用QR码代替输入URL。用户名和密码必须手动输入。

   > **Note**
   >
   > After the first login, the app will suggest URL and username of all successful connections.
   >
   > You are able to make an _offline_ login only if using the same user as the last online session.

![](resources/images/capture-app-image62.PNG){ width=25%} ![](resources/images/capture-app-image63.jpg){ width=25%}

> **警告**
>
> 在 DHIS2 2.30 以下版本中，如果用户尝试在线登录，并且其帐户已被禁用，如 [DHIS 2 手册 - 禁用用户](https://docs.dhis2.org/master/en/user 中所述/html/dhis2_user_manual_en_full.html#disable_user）所有数据都将从手机中擦除。确保在禁用用户之前所有数据已同步，或者您正在使用此功能远程擦除敏感数据，以防设备丢失。
>
> 由于登录 API 的更改，此功能在 2.31 及更高版本中不可用。

## 帐户恢复 { #capture_app_generic_recovery }

如果用户启用了以下设置，则他们将能够恢复自己的密码：已启用用户帐户恢复。

![](resources/images/capture-app-image64.PNG){ width=25%}

## 阻止会话（PIN） { #capture_app_generic_PIN }

用户可以使用4位PIN锁定会话。这样一来，您便可以移至手机中的其他应用，而无需删除本地数据。
如果用户忘记了PIN码，也可以通过输入凭据登录。

![](resources/images/capture-app-image65.PNG){width=25%} ![](resources/images/capture-app-image63.jpg){width=25%}

## 指纹 { #capture_app_generic_fingerprint }

如果设备中的功能被激活，则用户可以使用指纹扫描仪。

- 启用指纹扫描器而不启用PIN时，每次应用关闭，进入后台或设备被阻止时，会话将被锁定。一旦再次打开该应用程序，用户需要点击指纹图标以激活扫描仪。
- 如果设置了PIN和指纹，则在会话被锁定并且用户再次打开应用程序时，将询问PIN。

![](resources/images/capture-app-image104.jpg){width=25%} ![](resources/images/capture-app-image105.jpg){width=25%}

## 说明/信息按钮 { #capture_app_generic_instructions }

事件详细信息和 TEI 仪表板屏幕中提供了上下文指南。

![](resources/images/capture-app-image42.jpg){width=25%} ![](resources/images/capture-app-image66.png){width=25%}

> **提示**
>
>用户可以通过单击屏幕右上角的三个点来重新打开说明<!-- PALD: unnecessary: (trigger)-->。

## 过滤 { #capture_app_generic_filter }

<!-- PALD alternative: "The Filter allows you to narrow down the data available from the ..." -->

该应用程序为所有列表屏幕（主页、事件列表、tei 搜索和数据集）提供了新的和改进的过滤器。

按时期、组织过滤。单位、同步状态、事件状态、类别选项组合和“分配给我”。

![](resources/images/capture-app-image19.png){ width=25%} ![](resources/images/capture-app-image97.png){ width=25%} ![](resources/images/capture-app-image123.png){ width=25%} ![](resources/images/capture-app-image134.png){ width=25%}

过滤器将适应不同的程序和数据集。

1. 无需注册的计划：日期、组织。单位、同步状态、事件状态和类别组合。
2. 注册计划：活动日期、注册日期、组织。单位、同步、注册状态、事件状态和分配给我。仅当事件列表可用时才会显示过滤器图标（显示首页列表功能或搜索）
3. 数据集：期间、组织。单位和同步状态。

### 分配给我{ #capture_app_generic_filter_assigned }

可以根据事件分配给当前用户来过滤事件。 “分配给我”过滤器已添加到单个事件程序列表、TEI 列表以及 TEI 仪表板和地图视图中。仅当活动程序配置为将事件分配给用户时才会显示。

### 事件日期/日期/期间 { #capture_app_generic_filter_date }

过滤事件、TEI（基于其事件）和数据集，以下时间段可用：

- 今天
- 本星期
- 这个月
- 昨天
- 上星期
- 上个月
- 明天
- 下周
- 下个月
- 从到
- 其他（打开日期选择器）
- 任何时候

### 组织。单位{ #capture_app_generic_filter_orgunit }

允许用户键入搜索或从树中选择组织单位。

### 同步{ #capture_app_generic_filter_sync }

归档者：

- 同步（事件、TEI、数据集）
- 未同步
- 同步错误
- 短信同步

### 事件状态 { #capture_app_generic_filter_event }

按以下方式过滤事件：

- 打开
- 日程
- 逾期
- 已完成
- 跳过

允许多种状态选择。打开 TEI 后，过滤器将保留在仪表板中，并仅显示具有所选状态的事件。

显示的事件长达 5 年。

### 注册日期{ #capture_app_generic_filter_date_enroll }

“注册日期”将适用于 TEI 在计划中的注册日期。如果有多个注册日期，则应按最近的日期对结果进行排序。该过滤器的标签将在可用时显示。

### 注册状态 { #capture_app_generic_filter_enroll_status }

筛选器“注册状态”提供三个选项：活动、已完成、已取消。一次只能选择一个选项。如果您按“已完成”进行筛选并且 TEI 具有多个注册，则应用程序将打开“活动”注册。要查看已完成的项目，请选择仪表板右上角的三点菜单，然后选择“计划注册”。

### TEI 仪表板中添加了过滤：{ #capture_app_generic_filter_tei }

过滤器已添加到 TEI 仪表板。可以按时间段、组织单位、同步状态、事件状态和用户分配过滤跟踪实体实例注册的事件。

![](resources/images/capture-app-image114.png){ width=25%}

## 排序 { #capture_app_generic_sorting }

排序已集成在过滤器菜单中。

排序按钮将位于过滤栏上，具有以下行为：

- 一次仅适用一种排序。如果用户单击其他一项，则前一项将被禁用。
- 应用排序的图标显示它处于活动状态，其他则处于非活动状态。
- 重复点击会不断改变顺序。

![](resources/images/capture-app-image135.png){ width=25%}

### 日期（期间、日期、活动日期或注册日期）{ #capture_app_generic_sorting_dates }

- 事件日期先于截止日期，仅当没有事件日期时才使用截止日期。
- 从最近到不太最近的顺序排列。未来事件（截止日期）优先。

### 组织单位 { #capture_app_generic_sorting_orgunits }

- 列表将按组织单位名称的字母顺序排序。

### 注册状态 { #capture_app_generic_sorting_enrollment }

- 列表将按状态名称的字母顺序排序。

![](resources/images/capture-app-image123.png){ width=25%}

## 同步信息{ #capture_app_generic_sync_info }

允许用户检查特定程序的同步信息。现在，已同步的记录将不会显示任何图标。仅显示未同步，错误或SMS图标。

![](resources/images/capture-app-image67.png){ width=20%} ![](resources/images/capture-app-image69.png){ width=20%}

### 细粒度同步 { #capture_app_generic_sync_granular }

允许与服务器同步单个记录（程序，事件，TEI，数据集，数据值）。

![](resources/images/capture-app-image89.png){ width=25%} ![](resources/images/capture-app-image161.png){ width=25%}

### 短信同步 { #capture_app_generic_sync_sms }

没有互联网交流时，它允许通过几条SMS消息发送记录。
该记录被标记为“ SMS已同步”。

![](resources/images/capture-app-image91.png){ width=25%}

> **提示**
>
>在SMS设置（设置菜单）中编辑与SMS网关相关的参数

![](resources/images/capture-app-image90.png){ width=25%}

> **注意**
>
>请注意，为了使用SMS同步功能，需要按照（官方文档）[https://docs.dhis2.org/master/zh/dhis2_user_manual_en/mobile.html中的描述）在服务器端启用SMS服务。 ＃sms-service]。您还可以在（Android实施准则）[https://docs.dhis2.org/master/zh/dhis2_android_implementation_guideline/about-this-guide.html]中找到有关如何使用不同网关的更多信息。

## 组织单位 { #capture_app_generic_orgunit }

![](resources/images/capture-app-image30.png){ width=25%}

显示整个组织单位树。无法用于输入数据的组织单位将显示为灰色。
用户必须选中此框以选择所需的组织单位。

> **注意**
>
>不希望移动用户访问组织。整个国家的单位层次结构。组织单位的最大数量很难设置，因为应用程序没有设置限制，而是设备（内存，处理器）上的资源。我们可以说低于250个单位部门应该是安全的，但仍然认为对于移动用例来说这是一个很大的数字。

## 数据集 { #capture_app_generic_datasets }

用户现在可以输入组织单位，期间和一组数据元素的汇总数据，并将其发送到服务器。

![](resources/images/capture-app-image87.png){ width=25%} ![](resources/images/capture-app-image93.png){ width=25%} ![](resources/images/capture-app-image92.png){宽度=25%}

## 区分数据集，跟踪程序和事件程序 { #capture_app_generic_differentiating }

![](resources/images/capture-app-image87.png){ width=25%}

> **提示**
>
>区分它们的一种简单方法是查看左下角的单词。 “事件”一词将始终存在于事件程序中。在跟踪器中将出现被跟踪实体类型的名称（人，患者，建筑物等）。对于数据集，单词“ DataSets”将显示在记录数旁边。

## 共享资料 { #capture_app_generic_shargin }

![](resources/images/capture-app-image72.png){ width=25%} ![](resources/images/capture-app-image73.png){ width=25%}

## 捕捉坐标 { #capture_app_generic_capture_coord }

### TEI坐标 { #capture_app_generic_capture_coord_tei }

在注册表中获取TEI坐标。在TET功能类型中启用此功能。

![](resources/images/capture-app-image94.png){ width=25%}

### 多边形 { #capture_app_generic_capture_coord_polygons }

该应用程序现在支持geoJSON格式，并且用户能够捕获多边形。

![](resources/images/capture-app-image95.png){ width=25%}

## 图片 { #capture_app_generic_images }

ValueType图片已在应用端实现。
这允许为数据元素或属性选择图像并将其发送到服务器。
对于TEI，具有此值类型并标记为显示在列表中的第一个数据元素/属性将用作TEI配置文件映像。

![](resources/images/capture-app-image99.png){ width=25%} ![](resources/images/capture-app-image98.png){ width=25%} ![](resources/images/capture-app-image100.png){宽度=25%}

单击打开 TEI 个人资料图像。

![](resources/images/capture-app-image138.png){ width=25%}

## 在地图中显示事件和TEI { #capture_app_generic_display_events }

当节目阶段或跟踪的实体类型具有要素类型（并且对于注册的节目，启用了 displayFrontPageList 选项）时，可以切换列表以在地图中显示信息。通过单击导航面板中的地图图标进行切换。

![](resources/images/capture-app-image101.png){ width=25%} ![](resources/images/capture-app-image102.png){ width=25%}

如果 TEI 有个人资料图像，地图将显示它。 ![](resources/images/capture-app-image103.png){ width=25%}
