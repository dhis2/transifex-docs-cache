---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-event-reports-app.md"
revision_date: "2021-06-14"
---

# 使用事件报告应用 { #event_reports_app }

## 关于事件报告应用 { #event_reports_about }

![](resources/images/event_report/event_report.png)

使用**事件报告**应用程序，您可以分析两种类型的报告中的事件：

-   聚合事件报告：具有聚合事件数的数据透视表式分析

    By selecting **Aggregated values** from the top-left menu you can use the **Event Reports** app to create pivot tables with aggregated numbers of events. An event report is always based on a program. You can do analysis based on a range of dimensions. Each dimension can have a corresponding filter. Dimensions can be selected from the left-side menu. Similar to the pivot tables app, aggregated event reports may be limited by the amount of RAM accessible by the browser. If your requested table exceeds a set size, you will recieve a warning prompt asking whether or not you want to continue.

-   个别事件报告：事件列表

    By selecting **Events** from the top-left menu you can use the **Event Reports** app to make searches or queries for events based on a flexible set of criteria. The report will be displayed as a table with one row per event. Each dimension can be used as a column in the table or as a filter. Each dimension can have a criteria (filter). Data elements of type option set allows for "in" criteria, where multiple options can be selected. Numeric values can be compared to filter values using greater than, equal or less than operators.

## 创建事件报告 { #event_reports_create }

1.  Open the **Event Reports** app.

2.  Select **Aggregated values** or **Events**.

3.  在左侧菜单中，选择要分析的元数据。

4.  Click **Layout** and arrange the dimensions.

    您可以根据需要保留默认选择。

5.  点击**更新**。

## 选择尺寸项目 { #event_reports_select_dimensions }

事件报告始终基于程序，您可以进行分析
基于一系列维度。对于具有类别组合的程序，
您可以使用程序类别和类别选项组集作为
表格和图表的维度。每个维度项可以有一个
相应的过滤器。

1.  选择数据元素：

    1.  点击**数据**。

    2.  选择一个程序和一个程序阶段。

        The data elements associated with the selected program are listed under **Available**. Each data element acts as a dimension.

    3.  通过双击名称来选择所需的数据元素。

        数据元素可以按类型（数据元素、程序属性、程序指示符）进行过滤，并添加前缀以使它们易于识别。

        After selecting a data element, it is visible under **Selected data items**.

    4.  （可选）对于每个数据元素，指定一个带有“大于”、“in”或“等于”等运算符的过滤器以及过滤器值。

2.  选择期间。

    1.  点击**期间**。

    2.  选择一个或多个期间。

        您有三个期间选项：相对期间、固定期间和开始/结束日期。您可以在同一图表中组合固定期间和相对期间。您不能将固定期间和相对期间与开始/结束日期合并在同一图表中。重叠的时间段将被过滤，以便它们仅出现一次。

        -   Fixed periods: In the **Select period type** box, select a period type. You can select any number of fixed periods from any period type. Fixed periods can for example be "January 2014".

        -   Relative periods: In the lower part of the **Periods** section, select as many relative periods as you like. The names are relative to the current date. This means that if the current month is March and you select **Last month**, the month of February is included in the chart. Relative periods has the advantage that it keeps the data in the report up to date as time goes.

        -   Start/end dates: In the list under the **Periods** tab, select **Start/end dates**. This period type lets you specify flexible dates for the time span in the report.

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

您可以定义要显示为列、行的数据维度
和数据透视表中的过滤器。每个数据元素都显示为单独的
尺寸，可以放置在任何轴上。

> **注意**
>
> 连续值类型（实数/小数）的数据元素只能用作过滤器，并且将自动在布局对话框中定位为过滤器。其原因是连续数字无法分组到合理的范围内并用于列和行。

1.  Click **Layout**.

2.  将尺寸拖放到适当的空间。

3.  点击**更新**。

## 更改表格的显示 { #event_reports_change_display }

您可以自定义事件报告的显示。

1.  点击**选项**。

2.  根据需要设置选项。聚合事件报告和单独事件报告之间的可用选项不同。

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

您可以下载 HTML、JSON、
XML、Microsoft Excel 或 CSV 格式。

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

将您的图表或数据透视表保存为收藏夹，便于查找
他们后来。您还可以选择与其他用户共享它们作为
解释或显示在仪表板上。

您可以在**数据透视表**，**数据可视化器**，**事件可视化器**，**事件报告**应用中查看收藏夹的详细信息和解释。使用**收藏夹**菜单来管理您的收藏夹。

### 打开收藏夹 { #open-a-favorite }

1.  点击**收藏夹** \> **打开**。

2.  在搜索字段中输入收藏夹的名称，或单击“**上一页**”和“**下一页**”以显示收藏夹。

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

解释是到资源的链接，该资源具有给定时间段的数据描述。该信息在**仪表板**应用中可见。要创建解释，您首先需要创建收藏夹。如果您已经与其他人分享了自己的最爱，那么这些人就可以看到您编写的解释。

1.  点击**收藏夹** \> **写入解释**。

2.  在文本字段中，输入评论，问题或解释。您也可以使用'@username'提及其他用户。首先输入' @'，再加上用户名或真实姓名的首字母，然后出现一个提述栏，以显示可用的用户。提及的用户将收到内部DHIS2消息以及解释或评论。您可以在**仪表板**应用中查看解释。

    通过使用 Markdown 样式标记 \* 和 \_ 分别表示 **粗体** 和 _斜体_，可以将文本格式化为 **粗体**、_斜体_。还可以使用键盘快捷键：Ctrl/Cmd + B 和 Ctrl/Cmd + I。支持一组有限的表情符号，可以通过键入以下字符组合之一来使用：:) :-) :( :-( :+ 1 :-1. URL 会被自动检测并转换为可点击的链接。

3.  搜索您想要与之分享收藏夹的用户组，然后单击 **+** 图标。

4.  更改要修改的用户组的共享设置。

    -   **可以编辑和查看**：每个人都可以查看和编辑对象。

    -   **只能查看**：每个人都可以查看对象。

    -   **无**：公众将无法访问该对象。此设置仅适用于**公共访问**。

5.  点击**共享**。

### 订阅收藏 { #subscribe-to-a-favorite }

当您订阅收藏时，您会收到内部消息
每当另一个用户喜欢/创建/更新解释或
创建/更新此收藏夹的解释注释。

1.  打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击右上角的响铃图标以订阅此收藏。

### 创建指向收藏夹的链接 { #create-a-link-to-a-favorite }

1.  点击**收藏夹** \> **获取链接**。

2.  选择以下之一：

    -   **在此应用程序中打开**：您将获得收藏夹的 URL，您可以通过电子邮件或聊天与其他用户共享该 URL。

    -   **在 Web api 中打开**：您将获得 API 资源的 URL。默认情况下，这是 HTML 资源，但您可以将文件扩展名更改为“.json”或“.csv”。

### 删除收藏夹 { #delete-a-favorite }

1.  点击**收藏** \> **删除**。

2.  点击**确定**。

### 查看基于相对期间的解释 { #view-interpretations-based-on-relative-periods }

要查看相对时期的解释，例如一年前：

1.  用解释打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击解释。您的图表根据创建解释的时间显示数据和日期。要查看其他解释，请单击它们。

## 将事件报告可视化为图表 { #event_reports_open_as_chart }

制作事件报告后，可以将其作为图表打开：

单击**图表** \> **以表形式打开此图表**。
