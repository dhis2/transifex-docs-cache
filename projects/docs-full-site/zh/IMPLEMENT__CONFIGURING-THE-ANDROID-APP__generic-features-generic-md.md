---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/edit/master/docs/src/commonmark/en/content/capture-app/new-android-specific-features.md" 
---
# 通用功能  { #generic } 

 <!-- DHIS2-SECTION-ID:generic -->

## 登录 { #generic_login } 

  <!-- DHIS2-SECTION-ID:generic_login -->

有两种访问应用程序的方法：

1. 手动：用户必须输入要使用的服务器的相应URL，然后输入用户名和密码。

    > **Note**
    >
    > Take note that the login only possible with 2.29, 2.30, 2.31 and 2.32 servers.

2. QR：用户可以使用QR码代替输入URL。用户名和密码必须手动输入。

    > **Note**
    >
    > After the first login, the app will suggest URL and username of all successful connections.
    >
    > You are able to make an *offline* login only if using the same user as the last online session.

！[]（../ content / capture-app / resources / images / image62.PNG）{width = 25％}
！[]（../ content / capture-app / resources / images / image63.jpg）{width = 25％}

> **警告**
>
>在DHIS2版本（最高2.30）中，如果用户尝试进行在线登录并且其帐户已被禁用，请参见[DHIS 2手册-禁用用户]（https://docs.dhis2.org/master/zh/user /html/dhis2_user_manual_en_full.html#disable_user）所有数据都会从手机中删除。在禁用用户之前，请确保已同步所有数据，或者在设备丢失的情况下使用此功能远程擦除敏感数据。
>
>由于登录API的更改，此功能在2.31、2.32和2.33中不可用。


## 帐户恢复 { #generic_recovery } 

  <!-- DHIS2-SECTION-ID:generic_recovery -->

如果用户启用了以下设置，则他们将能够恢复自己的密码：已启用用户帐户恢复。

！[]（../ content / capture-app / resources / images / image64.PNG）{width = 25％}

## 阻止会话（PIN） { #generic_pin } 

  <!-- DHIS2-SECTION-ID:generic_pin -->

用户可以使用4位PIN锁定会话。这样一来，您便可以移至手机中的其他应用，而无需删除本地数据。
如果用户忘记了PIN码，也可以通过输入凭据登录。

！[]（../ content / capture-app / resources / images / image65.PNG）{width = 25％}
！[]（../ content / capture-app / resources / images / image63.jpg）{width = 25％}

## 指纹 { #generic_fingerprint } 

  <!-- DHIS2-SECTION-ID:generic_fingerprint -->

如果设备中的功能被激活，则用户可以使用指纹扫描仪。

* 启用指纹扫描器而不启用PIN时，每次应用关闭，进入后台或设备被阻止时，会话将被锁定。一旦再次打开该应用程序，用户需要点击指纹图标以激活扫描仪。
* 如果设置了PIN和指纹，则在会话被锁定并且用户再次打开应用程序时，将询问PIN。

！[]（../ content / capture-app / resources / images / image104.jpg）{width = 25％}
！[]（../ content / capture-app / resources / images / image105.jpg）{width = 25％}

## 说明/信息按钮 { #generic_instructions } 

  <!-- DHIS2-SECTION-ID:generic_instructions -->

用户首次打开应用程序时会打开上下文指南。

！[]（../ content / capture-app / resources / images / image42.jpg）{width = 25％}
！[]（../ content / capture-app / resources / images / image66.png）{width = 25％}

> **提示**
>
>用户可以通过单击屏幕右上角的三个点来重新打开说明<!-- PALD: unnecessary: (trigger)-->。

## 过滤 { #generic_filter } 

  <!-- DHIS2-SECTION-ID:generic_filter -->

 <!-- PALD alternative: "The Filter allows you to narrow down the data available from the ..." -->
该应用程序为所有列表屏幕（主页，事件列表，tei搜索和数据集）提供了经过改进的新过滤器。

按期间，组织过滤。单位，同步状态，事件状态，类别选项组合和“分配给我”。

！[]（../ content / capture-app / resources / images / image19.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image97.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image123.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image134.png）{width = 25％}

过滤器将适应不同的程序和数据集。

1.没有注册的程序：日期，组织。单位，同步状态，事件状态和类别组合。
2.注册程序：活动日期，注册日期，组织。单元，同步，注册状态，事件状态并已分配给我
3.数据集：期间，单位。单位和同步状态。

###分配给我{＃assigned-to-me}

可以根据事件对当前用户的分配来过滤事件。 “分配给我”过滤器已添加到单个事件程序列表，TEI列表以及TEI仪表板和地图视图中。仅当活动程序配置为向用户分配事件时，才会显示该消息。

###事件日期/日期/期间{＃event-datedateperiod}

过滤事件，TEI（基于事件）和数据集，以下时间段可用：
-今天
- 本星期
- 这个月
-昨天
- 上个星期
- 上个月
-明天
- 下周
- 下个月
- 从到
-其他（打开日期选择器）
- 任何时候

###组织单位{＃org-unit}

允许用户键入搜索或从树中选择组织单位。

###同步{#sync}

提交人：
-已同步（事件，TEI，数据集）
-未同步
-同步错误
-短信同步

###事件状态{＃event-status}

通过以下方式过滤事件：
-开放
-时间表
-逾期
-完成
-跳过

允许选择多个状态。打开TEI后，过滤器将保留在仪表板中，仅显示具有选定状态的事件。

显示的活动最多可追溯5年。

###注册日期{＃date-of-enrollment}

“入学日期”将适用于该计划中TEI的入学日期。如果注册日期不止一个，则应按最新日期对结果进行排序。可用时将显示此过滤器的标签。

###注册状态{＃enrollment-status}

过滤器“注册状态”提供三个选项：有效，已完成，已取消。一次只能选择一个选项。如果您按“已完成”过滤，并且TEI拥有多个注册，则该应用程序将打开“活动”注册。要查看完成的菜单，请选择仪表板右上角的三点菜单，然后选择“程序注册”。

###在TEI仪表板中添加了过滤：{＃filtering-added-in-tei-dashboard}

筛选器已添加到TEI仪表板。可以按时间段，组织单位，同步状态，事件状态和用户分配过滤跟踪实体实例注册的事件。

！[]（../ content / capture-app / resources / images / image114.png）{width = 25％}

##排序{#sorting}

排序已集成在过滤器菜单中。

排序按钮将在过滤器栏上具有以下行为：
-一次仅适用一种排序。如果用户单击其他按钮，则前一个按钮将被禁用。
-应用排序的图标显示该图标处于活动状态，其他图标则处于非活动状态。
-重复点击会不断改变顺序。

！[]（../ content / capture-app / resources / images / image135.png）{width = 25％}

###日期（期间，日期，事件日期或注册日期）{＃dates-period-date-event-date-or-enrollment-date}

-事件日期在截止日期之前，仅在没有事件日期时使用截止日期。
-从最新到最近的顺序。未来事件（到期日）优先。

###组织单位{＃org-units}

-列表将按组织单位名称的字母顺序排序。

###注册状态{＃enrollment-status}

-列表将按字母顺序按状态名称排序。

！[]（../ content / capture-app / resources / images / image123.png）{width = 25％}

##同步信息{#generic_sync}

 <!-- DHIS2-SECTION-ID:generic_sync -->

允许用户检查特定程序的同步信息。现在，已同步的记录将不会显示任何图标。仅显示未同步，错误或SMS图标。

！[]（../ content / capture-app / resources / images / image67.png）{width = 20％}
！[]（../ content / capture-app / resources / images / image69.png）{width = 20％}
！[]（../ content / capture-app / resources / images / image70.png）{width = 20％}

### 细粒度同步 { #generic_granular_sync } 

 <!-- DHIS2-SECTION-ID:generic_granular_sync -->

允许与服务器同步单个记录（程序，事件，TEI，数据集，数据值）。

！[]（../ content / capture-app / resources / images / image89.png）{width = 25％}


### 短信同步 { #generic_sms_sync } 

 <!-- DHIS2-SECTION-ID:generic_sms_sync -->

没有互联网交流时，它允许通过几条SMS消息发送记录。
该记录被标记为“ SMS已同步”。

！[]（../ content / capture-app / resources / images / image91.png）{width = 25％}

> **提示**
>
>在SMS设置（设置菜单）中编辑与SMS网关相关的参数

！[]（../ content / capture-app / resources / images / image90.png）{width = 25％}

> **注意**
>
>请注意，为了使用SMS同步功能，需要按照（官方文档）[https://docs.dhis2.org/master/zh/dhis2_user_manual_en/mobile.html中的描述）在服务器端启用SMS服务。 ＃sms-service]。您还可以在（Android实施准则）[https://docs.dhis2.org/master/zh/dhis2_android_implementation_guideline/about-this-guide.html]中找到有关如何使用不同网关的更多信息。

## 组织单位 { #generic_ou } 

 <!-- DHIS2-SECTION-ID:generic_ou -->

！[]（../ content / capture-app / resources / images / image30.png）{宽度= 25％}

显示整个组织单位树。无法用于输入数据的组织单位将显示为灰色。
用户必须选中此框以选择所需的组织单位。


> **注意**
>
>不希望移动用户访问组织。整个国家的单位层次结构。组织单位的最大数量很难设置，因为应用程序没有设置限制，而是设备（内存，处理器）上的资源。我们可以说低于250个单位部门应该是安全的，但仍然认为对于移动用例来说这是一个很大的数字。

## 数据集 { #generic_datasets } 

 <!-- DHIS2-SECTION-ID:generic_datasets -->

用户现在可以输入组织单位，期间和一组数据元素的汇总数据，并将其发送到服务器。

！[]（../ content / capture-app / resources / images / image87.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image93.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image92.png）{width = 25％}

## 区分数据集，跟踪程序和事件程序 { #generic_differentiating } 

  <!-- DHIS2-SECTION-ID:generic_differentiating -->

！[]（../ content / capture-app / resources / images / image87.png）{width = 25％}

> **提示**
>
>区分它们的一种简单方法是查看左下角的单词。 “事件”一词将始终存在于事件程序中。在跟踪器中将出现被跟踪实体类型的名称（人，患者，建筑物等）。对于数据集，单词“ DataSets”将显示在记录数旁边。

## 共享资料 { #generic_sharing } 

 <!-- DHIS2-SECTION-ID:generic_sharing -->

！[]（../ content / capture-app / resources / images / image72.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image73.png）{width = 25％}

## 捕捉坐标 { #generic_coords } 

 <!-- DHIS2-SECTION-ID:generic_coords -->

### TEI坐标 { #generic_coords_tei } 

 <!-- DHIS2-SECTION-ID:generic_coords_tei -->

在注册表中获取TEI坐标。在TET功能类型中启用此功能。

！[]（../ content / capture-app / resources / images / image94.png）{width = 25％}

### 多边形 { #generic_coords_polygons } 

 <!-- DHIS2-SECTION-ID:generic_coords_polygons -->

该应用程序现在支持geoJSON格式，并且用户能够捕获多边形。

！[]（../ content / capture-app / resources / images / image95.png）{width = 25％}

## 图片 { #generic_images } 

 <!-- DHIS2-SECTION-ID:generic_images -->

ValueType图片已在应用端实现。
这允许为数据元素或属性选择图像并将其发送到服务器。
对于TEI，具有此值类型并标记为显示在列表中的第一个数据元素/属性将用作TEI配置文件映像。

！[]（../ content / capture-app / resources / images / image99.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image98.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image100.png）{width = 25％}

## 在地图中显示事件和TEI { #generic_events_tei_maps } 

 <!-- DHIS2-SECTION-ID:generic_events_tei_maps -->

当程序阶段或跟踪的实体类型具有要素类型时（对于已注册的程序，启用了displayFrontPageList选项），可以切换列表以在地图中显示信息。

！[]（../ content / capture-app / resources / images / image101.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image102.png）{width = 25％}
！[]（../ content / capture-app / resources / images / image103.png）{width = 25％}


