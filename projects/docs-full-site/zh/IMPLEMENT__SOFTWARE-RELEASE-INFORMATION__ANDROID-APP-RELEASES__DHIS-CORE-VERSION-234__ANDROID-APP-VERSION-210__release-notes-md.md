---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/android-releases/2.1/ReleaseNote-2.1.0.md"
revision_date: "2020-11-10"
---

# DHIS2 Android App版本2.1发行说明 { #dhis2-android-app-version-21-release-note }

DHIS2 [Android Capture App 2.1]（https://www.dhis2.org/android-2-1）具有许多新功能，改进和错误修复！此版本与[DHIS2版本2.34]（https://community.dhis2.org/t/dhis-version-2-34-is-released/39064）完全兼容。

## 数据集 { #data-sets }

---

**增加行标题：**现在计算出数据集中第一列的长度，以显示数据元素名称的全文。用户还可以调整宽度，使其更好地适应屏幕尺寸。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2716) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Data+Sets.png)

## 事件的列表，过滤和排序 { #listing-filtering-sorting-of-events }

---

** TEI仪表板中程序阶段的分组视图：** TEI仪表板现在提供了将事件列表从时间顺序视图更改为阶段分组视图的可能性。阶段分组视图将对每个程序阶段的事件进行分组和折叠。用户可以扩展每个程序阶段组，并且事件将按时间顺序显示。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2641) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-1654) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Groupin+1.png) | [屏幕截图2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Grouping+2.png) | [文档](https://docs.dhis2.org/2.33/en/dhis2_android_capture_app/programs.html#group-view-of-program-stages-in-tei-dashboard)

**在TEI仪表板中添加了过滤器：**过滤器已添加到TEI仪表板中。可以按时间段，组织单位，同步状态，事件状态和用户分配过滤跟踪实体实例注册的事件。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2760) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/TEI+Dashboard+filters.png)

## 数据输入格式（事件和跟踪程序） { #data-entry-forms-event-and-tracker-programs }

---

**保存事件或注册时改进的错误消息对话框：**应用程序现在将列出用户尝试完成事件或注册时缺少的必填字段的名称。包含缺失字段的部分将突出显示，以帮助用户找到缺失字段。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2733) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Error+message.png)

**支持QR和条形码：**数据元素或属性或类型文本可以配置为QR或条形码。当数据元素或属性呈现为QR /条形码时，应用程序将打开设备摄像头以读取代码图像。当QR /条形码是配置为可搜索的TEI属性时，将允许用户扫描代码以搜索和标识被跟踪实体实例。这也适用于选项集。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-1670) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/QR1.png) | [屏幕截图2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/QR2.png) | [屏幕截图3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Barcode1.png) | [屏幕截图4](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Barcode2.png) | [文档](https://docs.dhis2.org/2.33/en/dhis2_android_capture_app/visual-configurations.html#qr-and-barcodes)

**扩展的渲染选项：**可用的渲染选项已扩展为包括水平和垂直单选按钮，复选框和切换开关。允许的选项取决于值类型。

-   仅是：可以呈现为单选按钮或复选框。
-   是/否：可以呈现为水平/垂直单选按钮或水平/垂直复选框或切换。
-   文字：可以呈现为QR或条形码。当链接到选项集时，可以将其呈现为水平/垂直单选按钮或水平/垂直复选框。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-741) | [屏幕截图](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Rendering+types+1.jpg) | [屏幕截图2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Rendering+Types+2.jpg) |[屏幕截图3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Rendering+Types+3.jpg) |[文档](https://docs.dhis2.org/2.33/ zhs2_android_capture_app/visual-configurations.html#render-types)

**将对话框和按钮保存在与事件对齐的注册中：**已修改注册表单中“保存”按钮和相关对话框的设计，以与事件表单的用户体验保持一致。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2731) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Save+button+enrollment.png)

**各节中的改进：**各个节的显示已经过重新设计，以提供更简单的用户体验。此外，现在支持注册表格中的部分，并与事件部分的设计保持一致。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2732) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-656) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Sections+1.png) | [屏幕截图2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Sections+2.png)

**事件中的注释：**可以在单个事件程序和程序阶段事件中为事件添加注释。在数据输入表单的新选项卡中提供了注释。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-817) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-2671) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Notes+in+Events.png)

## 用户分配 { #user-assignment }

---

**根据用户分配过滤事件：**可以根据对当前用户的分配过滤事件。 “分配给我”过滤器已添加到单个事件程序列表，TEI列表以及TEI仪表板和地图视图中。仅当活动程序配置为向用户分配事件时，才会显示该消息。

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2586) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-1290) | [Jira3](https://jira.dhis2.org/browse/ANDROAPP-1292) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Assigned+to+me+1.png) | [屏幕截图2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.1/Assigned+to+me+2.png)

## 质量/安全性/性能 { #quality-security-performance }

---

修复了与应用程序PIN访问控制相关的漏洞

在表格[Jira]（https://jira.dhis2.org/browse/ANDROAPP-1998）的末尾创建并保留了事件。

SqlBrite查询已迁移到SDK [Jira]（https://jira.dhis2.org/browse/ANDROAPP-2662）

发布信息

---

| 发布信息 | 链接 |
| --- | --- |
| 从Google Play或Github下载应用 | https://www.dhis2.org/app-store |
| 文档和Javadocs | https://www.dhis2.org/android-documentation |
| 有关JIRA上每个功能的详细信息（需要登录） | [2.1 功能特点](https://jira.dhis2.org/issues/?filter=11837) |
| JIRA修复的错误概述（需要登录） | [2.1 错误](https://jira.dhis2.org/issues/?filter=11838) |
| Github上的源代码 | https://github.com/dhis2/dhis2-android-capture-app |
| 演示实例（用户/密码） | https://play.dhis2.org/2.34/ android / Android123 |
| DHIS 2社区 | [https://community.dhis2.org 移动社区](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Github上SDK的源代码 | [SDK 1.0.3](https://github.com/dhis2/dhis2-android-sdk/releases/tag/1.0.3) |
