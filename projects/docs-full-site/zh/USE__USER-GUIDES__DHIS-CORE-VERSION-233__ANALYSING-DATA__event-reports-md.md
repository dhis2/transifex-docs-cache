---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.33/src/commonmark/en/content/user/using-the-event-reports-app.md"
revision_date: '2019-02-21'
---

# 使用事件报告应用 { #event_reports_app } 

 <!--DHIS2-SECTION-ID:event_reports_app-->

## 关于事件报告应用 { #event_reports_about } 

 <!--DHIS2-SECTION-ID:event_reports_about-->


![](resources/images/event_report/event_report.png)

使用 **Event Report**s 应用程序，您可以分析两种类型的事件
报告：

  - 汇总的事件报告：汇总的数据透视表样式分析
    事件数

    通过从左上角的菜单中选择 **Aggregated values**，您可以
    使用 **Event Reports** 应用程序创建聚合数据透视表
    事件数。事件报告始终基于程序。您
    可以基于一定范围的维度进行分析。每个维度都可以
    有一个相应的过滤器。尺寸可以从
    左侧菜单。与数据透视表应用类似，聚合事件
    报告可能会受到可访问的RAM数量的限制
    浏览器。如果您要求的表格超过设定的大小，您将
    收到警告提示，询问您是否要继续。

  - 个别事件报告：事件列表

    通过从左上角菜单中选择 **Events**，您可以使用
    **事件报告**应用程序，用于基于事件进行搜索或查询
    根据一组灵活的标准。该报告将显示为
    表，每个事件一行。每个维度都可以用作一列
    在表格中或作为过滤器。每个维度可以有一个条件
    （过滤）。类型选项集的数据元素允许“输入”条件，
    在这里可以选择多个选项。数值可以是
    与使用大于，等于或小于
    操作员。

## 创建事件报告 { #event_reports_create } 

 <!--DHIS2-SECTION-ID:event_reports_create-->

1.  Open the **Event Reports** app.

2.  Select **Aggregated values** or **Events**.

3.  在左侧菜单中，选择要分析的元数据。

4.  Click **Layout** and arrange the dimensions.

    您可以根据需要保留默认选择。

5.  点击**更新**。

## 选择尺寸项目 { #event_reports_select_dimensions } 

 <!--DHIS2-SECTION-ID:event_reports_select_dimensions-->

事件报告始终基于程序，您可以进行分析
基于一系列尺寸。对于具有类别组合的程序，
您可以将程序类别和类别选项组集用作
表格和图表的尺寸。每个维度项目可以有一个
相应的过滤器。

1.  选择数据元素：

    1.  点击**数据**。

    2.  选择一个程序和一个程序阶段。

        与所选程序关联的数据元素是
        列在**可用**下。每个数据元素都充当一个
        尺寸。

    3.  双击所需的数据元素
        名称。

        数据元素可以按类型进行过滤（数据元素，程序
        属性，程序指示器）并加上前缀
        容易识别。

        选择数据元素后，它在 **Selected 下可见
        数据项**。

    4.  （可选）为每个数据元素指定一个过滤器
        运算符，例如“大于”，“中”或“等于”，以及
        过滤值。

2.  选择期间。

    1.  点击**期间**。

    2.  选择一个或多个期间。

        您有三个期间选项：相对期间，固定期间
        和开始/结束日期。您可以结合固定期间和相对期间
        同一图表中的句点。您不能将固定期限和
        同一图表中具有开始/结束日期的相对期间。
        重叠周期被过滤，因此它们仅出现一次。

          - 固定期间：在**选择期间类型**框中，选择一个
            期间类型。您可以从以下任意数量的固定期间中选择
            任何期间类型。固定时间可以例如是“一月
            2014”。

          - 相对时期：在**期间的下部**
            部分中，选择任意多个相对时间段。的
            名称是相对于当前日期的。这意味着
            当前月份是三月，您选择**上个月**，
            图表中包含2月。相对的
            期间的优点是将数据保留在
            及时报告最新情况。

          - 开始/结束日期：在 **Periods** 选项卡下的列表中，
            选择**开始/结束日期**。此期间类型可让您
            在报告中指定时间跨度的灵活日期。

3.  选择组织单位。

    1.  Click **Organisation units**.

    2.  点击齿轮箱图标。

    3.  Select a **Selection mode** and an organisation unit.

        共有三种不同的选择模式：

        <table>
        <caption>Selection modes</caption>
        <colgroup>
        <col style="width: 38%" />
        <col style="width: 61%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Selection mode</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><strong>Select organisation units</strong></p></td>
        <td><p>Lets you select the organisation units you want to appear in the chart from the organization tree.</p>
        <p>Select <strong>User org unit</strong> to disable the organisation unit tree and only select the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-units</strong> to disable the organisation unit tree and only select the sub-units of the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-x2-units</strong> to disable the organisation unit tree and only select organisation units two levels down from the organisation unit that is related to your profile.</p>
        <p>This functionality is useful for administrators to create a meaningful &quot;system&quot; favorite. With this option checked all users find their respective organisation unit when they open the favorite.</p></td>
        </tr>
        <tr class="even">
        <td><p><strong>Select levels</strong></p></td>
        <td><p>Lets you select all organisation units at one or more levels, for example national or district level.</p>
        <p>You can also select the parent organisation unit in the tree, which makes it easy to select for example, all facilities inside one or more districts.</p></td>
        </tr>
        <tr class="odd">
        <td><p><strong>Select groups</strong></p></td>
        <td><p>Lets you select all organisation units inside one or several groups and parent organisation units at the same time, for example hospitals or chiefdoms.</p></td>
        </tr>
        </tbody>
        </table>

4.  点击**更新**。

## 选择系列，类别和过滤器 { #event_reports_select_series_category_filter } 

 <!--DHIS2-SECTION-ID:event_reports_select_series_category_filter-->

您可以定义要显示为列，行的数据维度
并在数据透视表中进行过滤。每个数据元素都显示为单个
尺寸，可以放置在任何轴上。

> **注意**
>
>连续值类型（实数/十进制数）的数据元素
>只能用作过滤器，并会自动定位为
>布局对话框中的过滤器。原因是连续的
>数字不能分组为合理范围，不能用于列和
>行。

1.  Click **Layout**.

2.  将尺寸拖放到适当的空间。

3.  点击**更新**。

## 更改表格的显示 { #event_reports_change_display } 

 <!--DHIS2-SECTION-ID:event_reports_change_display-->

您可以自定义事件报告的显示。

1.  点击**选项**。

2.  根据需要设置选项。可用选项之间有所不同
    汇总的事件报告和单个事件报告。

    <table style="width:100%;">
    <caption>Event reports options</caption>
    <colgroup>
    <col style="width: 22%" />
    <col style="width: 22%" />
    <col style="width: 33%" />
    <col style="width: 22%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    <th><p>Available for report type</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p></td>
    <td><p>Displays totals at the end of each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show row totals</strong></p></td>
    <td><p>Displays totals at the end of each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td>Displays labels for dimensions.</td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide n/a data</strong></p></td>
    <td><p>Hides data tagged as N/A from the chart.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful when you want for example to exclude partial events in indicator calculations.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Limit</strong></p></td>
    <td><p>Sets a limit of the maximum number of rows that you can display in the table, combined with a setting for showing top or bottom values.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Output type</strong></p></td>
    <td><p>Defines the output type. The output types are <strong>Event</strong>, <strong>Enrollment</strong> and<strong>Tracked entity instance</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Program status</strong></p></td>
    <td><p>Filters data based on the program status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong> or <strong>Cancelled</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Event status</strong></p></td>
    <td><p>Filters data based on the event status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong>, <strong>Scheduled</strong>, <strong>Overdue</strong> or <strong>Skipped</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td><strong>Organisation units</strong></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Includes the names of all parents of each organisation unit in labels.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    </tbody>
    </table>

3.  点击**更新**。

## 下载图表数据源 { #event_reports_download_report } 

 <!--DHIS2-SECTION-ID:event_reports_download_report-->

您可以将事件报告背后的数据源下载为HTML，JSON，
XML，Microsoft Excel或CSV格式。

1.  点击**下载**。

2.  在**普通数据源**下，单击要下载的格式。

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 27%" />
    <col style="width: 72%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>HTML</p></td>
    <td><p>Creates HTML table based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>JSON</p></td>
    <td><p>Downloads data values in JSON format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>XML</p></td>
    <td><p>Downloads data values in XML format based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>Microsoft Excel</p></td>
    <td><p>Downloads data values in Microsoft Excel format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>CSV</p></td>
    <td><p>Downloads data values in CSV format based on selected meta data</p></td>
    </tr>
    </tbody>
    </table>

## 管理收藏夹 { #manage-favorites } 

将图表或数据透视表另存为收藏夹可轻松查找
他们以后。您还可以选择与其他用户共享
解释或将其显示在仪表板上。

您可以在“收藏夹”中查看收藏夹的详细信息和解释。
**数据透视表**，**数据可视化器**，**事件可视化器**，**事件
报告**应用程序。使用**收藏夹**菜单管理您的收藏夹。

### 打开收藏夹 { #open-a-favorite } 

1.  点击**收藏夹** \> **打开**。

2.  在搜索字段中输入收藏夹的名称，或单击**上一页**
    和**下一步**显示收藏夹。

3.  单击您要打开的收藏夹的名称。

### 保存收藏夹 { #save-a-favorite } 

1.  点击**收藏夹** \> **另存为**。

2.  输入您喜欢的**名称**和**描述**。 description字段支持RTF格式，有关更多详细信息，请参见解释部分。

3.  点击**保存**。

### 重命名收藏夹 { #rename-a-favorite } 

1.  点击**收藏** \> **重命名**。

2.  输入您喜欢的新名称。

3.  点击**更新**。

### 为最喜欢的人写一个诠释 { #write-an-interpretation-for-a-favorite } 

解释是指向具有数据描述的资源的链接
在给定的时期。该信息在**仪表板**应用中可见。
要创建解释，您首先需要创建收藏夹。如果
您已经与其他人分享了自己的最爱，
写给那些人看。

1.  点击**收藏夹** \> **写入解释**。

2.  在文本字段中，输入评论，问题或解释。您
    也可以使用“ @username”提及其他用户。首先输入“ @”
    加上用户名或真实姓名的首字母以及提及
    栏将显示可用的用户。提及的用户将收到
    内部DHIS2消息及其解释或注释。您
    可以在**仪表板**应用中查看解释。

    您可以使用**粗体**，*斜体*格式化文本
    Markdown样式标记\ *和\ _分别为**粗体**和*斜体*。
    键盘快捷键也可用：Ctrl / Cmd + B和Ctrl / Cmd +I。
    支持有限的表情符号集，可以通过键入以下其中一个来使用
    以下字符组合：:) :-) :( :-(：+1：-1。URL为
    自动检测并转换为可点击的链接。

3.  搜索您要与之共享收藏夹的用户组，
    然后点击** + **图标。

4.  更改要修改的用户组的共享设置。

      - **可以编辑和查看**：每个人都可以查看和编辑对象。

      - **只能查看**：每个人都可以查看对象。

      - **无**：公众将无法访问该对象。这个
        设置仅适用于**公共访问**。

5.  点击**共享**。

### 订阅收藏 { #subscribe-to-a-favorite } 

订阅收藏夹后，您会收到内部消息
每当其他用户喜欢/创建/更新解释时，或
创建/更新此收藏夹的解释注释。

1.  打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击右上角的响铃图标以订阅此收藏。

### 创建指向收藏夹的链接 { #create-a-link-to-a-favorite } 

1.  点击**收藏夹** \> **获取链接**。

2.  选择以下之一：

      - **在此应用程序中打开**：您会获得自己喜欢的收藏的URL
        可以通过电子邮件或聊天与其他用户共享。

      - **在网络api中打开**：您会获得API资源的网址。通过
        默认情况下，这是HTML资源，但是您可以更改文件
        “ .json”或“ .csv”的扩展名。

### 删除收藏夹 { #delete-a-favorite } 

1.  点击**收藏** \> **删除**。

2.  点击**确定**。

### 查看基于相对期间的解释 { #view-interpretations-based-on-relative-periods } 

要查看相对时期的解释，例如一年前：

1.  用解释打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击一个解释。您的图表显示数据和日期
    根据解释的创建时间。查看其他
    解释，请单击它们。

## 将事件报告可视化为图表 { #event_reports_open_as_chart } 

 <!--DHIS2-SECTION-ID:event_reports_open_as_chart-->

制作事件报告后，可以将其作为图表打开：

单击**图表** \> **以表形式打开此图表**。
