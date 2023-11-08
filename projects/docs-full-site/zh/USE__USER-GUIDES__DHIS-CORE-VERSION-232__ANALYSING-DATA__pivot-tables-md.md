---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.32/src/commonmark/en/content/user/analyze-data-in-pivot-tables.md"
revision_date: '2019-02-21'
---

# 分析数据透视表中的数据 { #pivot } 

 <!--DHIS2-SECTION-ID:pivot-->

## 关于数据透视表应用 { #pivot_about } 

 <!--DHIS2-SECTION-ID:pivot_about-->

借助**数据透视表**应用，您可以基于所有内容创建数据透视表
DHIS2中的可用数据维度。数据透视表是用于
数据分析，可让您根据数据汇总和排列数据
方面。 DHIS2中的数据维度示例如下：

  - 数据维度本身（例如，数据元素，指标和
    事件）

  - 时间段（代表数据的时间段）

  - 组织层次结构（代表
    数据）

从这些尺寸中，您可以自由选择*尺寸项*以包括
在数据透视表中。您可以使用以下方法在DHIS2中创建其他尺寸
组设置功能。这允许不同的聚合
途径，例如按“合作伙伴”或机构类型进行汇总。

数据透视表可以在*列*，*行*和
*过滤器*。在列上放置数据维度时，数据透视表
将在每个维度项目中显示一列。如果放置多个数据
列上的尺寸，数据透视表将为所有列显示一列
所选维度中项目的组合。当您放置一个
数据维度在行上，数据透视表每维度显示一行
项目以类似的方式。您选择作为过滤器的尺寸不会
包含在数据透视表中，但会汇总并过滤该表
基于所选过滤器项的数据。

> **提示**
>
>-您必须在列或行上至少选择一个维度。
>
>-您必须至少包含一个期间。
>
>-数据元素组集和报告率无法显示在
>相同的数据透视表。
>
>-数据透视表不能包含超过最大数量的
>在系统设置中指定的分析记录。
>最大记录数也可能受限制
>您的浏览器可用的最大RAM。你将会
>提示警告，如果您请求的表超过
>特定尺寸。在此提示下，您可以取消
>请求或继续构建表。考虑缩小尺寸
>表格，而不是一个显示所有数据的表格
>元素和指标结合在一起。
>
>-**数据透视表**应用程序支持向下钻取和向上钻取一段时间，以及
>组织单位。这意味着您可以例如向下钻取
>从年度周期到季度，季度，几个月和几周
>表格。您还可以从全球组织单位下钻
>前往国家，省和设施。

## 创建数据透视表 { #pivot_create } 

 <!--DHIS2-SECTION-ID:pivot_create-->

1.  打开**数据透视表**应用。

2.  在左侧菜单中，选择要选择的尺寸项目
    分析，例如数据元素或指标。

3.  单击**布局**，然后将数据维排列为列，行
    和过滤器。

    您可以根据需要保留默认选择。

4.  点击**更新**。

在此示例中，指标被列为列，周期被列为行。

![](resources/images/pivot_table/basic_pivot.png)

### 选择尺寸项目 { #select-dimension-items } 

左侧菜单列出了所有可用数据维度的部分。从
每个部分都可以选择任意数量的维项目。作为一个
例如，您可以打开数据元素部分并选择
可用列表中的数据元素数量。您可以选择一个项目
通过标记并单击部分标题中的箭头或简单地
双击该项目。在您使用数据维度之前
数据透视表，您必须至少选择一个维度项目。如果你安排
维度为列或行，但不选择任何维度项，
尺寸被忽略。

您必须至少选择一种数据维度类型才能创建数据透视表
表。下表描述了可用的类型：

 <table>
 <caption>数据维度类型</caption>
 <colgroup>
 <col style="width: 33%" />
 <col style="width: 33%" />
 <col style="width: 33%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th>数据维度类型</th>
 <th>定义</th>
 <th>示例</th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td>指示灯</td>
 <td>指标是基于数据元素的计算公式。 </td>
 <td>特定地区的免疫覆盖率。 </td>
 </tr>
 <tr class="even">
 <td>数据元素</td>
 <td>代表已捕获数据的现象。 </td>
 <td>疟疾病例数；给予的卡介苗剂量。 </td>
 </tr>
 <tr class="odd">
 <td>数据集</td>
 <td>为数据收集分组的数据元素的集合。您可以选择：
 <ul>
 <li> <p> <strong>报告率</strong>：实际报告数与预期报告数的百分比</p> </li>
 <li> <p> <strong>时间报告率</strong>：基于及时提交表单的报告率。在报告期后的几天内必须及时提交。 </p> </li>
 <li> <p> <strong>实际报告</strong>：实际报告数量</p> </li>
 <li> <p> <strong>时间上的实际报告</strong>：基于及时提交表单的实际报告数。在报告期后的几天内必须及时提交。 </p> </li>
 <li> <p> <strong>预期报告</strong>：基于已分配数据集和报告频率的组织单位的预期报告数。 </p> </li>
 </ul> </td>
 <td>免疫和发病率报告率。 </td>
 </tr>
 <tr class="even">
 事件数据项<td> </td>
 <td>一个数据元素，它是表示已捕获事件的程序的一部分。 </td>
 <td>营养计划中儿童的平均体重和身高。 </td>
 </tr>
 <tr class="odd">
<td> 程序指示器</td>
 <td>基于表示事件的程序中的数据元素计算得出的公式。</td> 
 <td>营养计划中儿童的BMI平均得分。 </td>
 </tr>
 </tbody>
 </table>

您可以组合这些维度以显示例如汇总数据
报告率或事件数据项以及程序
指标，都在同一数据透视表中。对于“数据元素”数据
维度，您还可以选择“总计”和“详细信息”，
将允许您一起查看不同的类别组合选项
在同一数据透视表上。

对于期间维度，您可以选择使用固定期间还是
相对时期。固定期限的一个示例是“ 2012年1月”。至
选择固定期间是从期间中选择期间类型开始
类型列表。然后，您可以从可用列表中选择时间段
期。

相对期间是相对于当前日期的期间。示例
相对期间为“过去一个月”，“过去12个月”，“过去5年”。
可以通过选中每个相对应的复选框来选择相对时间段
期。使用相对期间的主要优点是
保存数据透视表收藏夹，它将使用最新数据保持更新
随着时间的流逝，无需不断更新。

对于组织单位维度，您可以选择任意数量的
层次结构中的组织单位。选择所有组织单位
在特定上级组织单位下，右键单击并单击“选择
所有孩子”。要手动选择多个组织单位，请点击
在单击单位部门时，按住** Ctrl **键。你可以打勾
“用户组织单位”，“用户子单位”或“用户子x2单位”
动态插入与您的组织关联的一个或多个组织单位
用户帐号。当您保存数据透视表收藏夹和
想要与其他用户共享，因为与
查看收藏夹时将使用其他用户的帐户。


![](resources/images/pivot_table/period_dimension.png)

动态维度可以包含组织单位组集，数据
元素组集或类别选项组集
配置为“分类”类型。一旦组集
已配置，它们将在数据透视表中可用，并且
可以用作其他分析维度，例如进行分析
根据组织单位或实施伙伴的类型汇总数据。
动态尺寸与固定尺寸相同。

> **提示**
>
>一些动态尺寸可能包含许多项目。这可能会导致问题
>在某些浏览器中由于网址的长度而存在多个维度
>已选择成员。特殊的“全部”复选框可用于
>动态尺寸，可让您包含所有可用尺寸
>在数据透视表中隐式包含维度，而无需指定每个和
>每个维度成员。

### 修改数据透视表布局 { #modify-pivot-table-layout } 

选择数据维度之后，该安排数据透视表了。
单击顶部菜单中的“布局”以打开布局屏幕。在这个画面
您可以将数据维度定位为表格的列，行或过滤器
通过将尺寸从尺寸列表中拖放到
相应的列，行和过滤器列表。您可以设置任意数量的
任何列表中的尺寸。例如，您可以点击
将“单位部门”拖放到行列表中以进行定位
组织单位维度作为表格行。注意指标
数据元素和数据集报告率是常见“数据”的一部分
尺寸，并将一起显示在数据透视表中。对于
例如，在左侧菜单中选择指标和数据元素后，
您可以将“单位部门”从可用尺寸列表中拖到
行维度列表，以便将它们排列为枢轴中的行
表。


![](resources/images/pivot_table/table_layout.png)

设置数据透视表后，您可以点击“更新”以进行渲染
您的数据透视表，或单击“隐藏”以隐藏布局屏幕，而不显示任何内容
更改生效。由于我们在示例中选择了
周期和单位部门尺寸作为行，数据透视表将
生成这些维度中项目的所有组合，并生成
像这样的表：

![](resources/images/pivot_table/pivot_rows.png)

## 更改数据透视表的显示 { #pivot_change_display } 

 <!--DHIS2-SECTION-ID:pivot_change_display-->

1.  打开**数据透视表**应用。

2.  创建一个新的数据透视表或打开收藏夹。

3.  点击**选项**。

4.  根据需要设置选项。

    <table>
    <caption>Pivot table options</caption>
    <colgroup>
    <col style="width: 21%" />
    <col style="width: 35%" />
    <col style="width: 42%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p>
    <p><strong>Show row totals</strong></p></td>
    <td><p>Displays total values in the table for each row and column, as well as a total for all values in the table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p>
    <p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays subtotals in the table for each dimension.</p>
    <p>If you only select one dimension, subtotals will be hidden for those columns or rows. This is because the values will be equal to the subtotals.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td><p>Shows the dimension names as part of the pivot tables.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide empty columns</strong></p></td>
    <td><p>Hides empty columns from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Skip rounding</strong></p></td>
    <td><p>Skips the rounding of data values, offering the full precision of data values. Can be useful for finance data where the full dollar amount is required.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Aggregation type</strong></p></td>
    <td><p>The default aggregation operator can be over-ridden here, by selecting a different aggregation operator. Some of the aggregation types are <strong>Count</strong>, <strong>Min</strong> and <strong>Max</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Number type</strong></p></td>
    <td><p>Sets the type of value you want to display in the pivot table: <strong>Value</strong>, <strong>Percentage of row</strong> or <strong>Percentage of column</strong>.</p>
    <p>The options <strong>Percentage of row</strong> and<strong>Percentage of column</strong> mean that you'll display values as percentages of row total or percentage of column total instead of the aggregated value. This is useful when you want to see the contribution of data elements, categories or organisation units to the total value.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Measure criteria</strong></p></td>
    <td><p>Allows for the data to be filtered on the server side.</p>
    <p>You can instruct the system to return only records where the aggregated data value is equal, greater than, greater or equal, less than or less or equal to certain values.</p>
    <p>If both parts of the filter are used, it's possible to filter out a range of data records.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Events</strong></p></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful for example to exclude partial events in indicator calculations.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Organisation units</strong></p></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Shows the name of all ancestors for organisation units, for example &quot;Sierra Leone / Bombali / Tamabaka / Sanya CHP&quot; for Sanya CHP.</p>
    <p>The organisation units are then sorted alphabetically which will order the organisation units according to the hierarchy.</p>
    <p>When you download a pivot table with organisation units as rows and you've selected <strong>Show hierarchy</strong>, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Legend</strong></p></td>
    <td><p><strong>Apply legend</strong></p></td>
    <td><p>Applies a legend to the values. This mean that you can apply a colour to the values.</p>
    <p>Select <strong>By data item</strong> to color the table cells individually according to each data element or indicator.</p>
    <p>You configure legends in the <strong>Maintenance</strong> app.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Style</strong></p></td>
    <td><p>Colors the text or background of cells in pivot tables based on the selected legend.</p>
    <p>You can use this option for scorecards to identify high and low values at a glance.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>General</strong></p></td>
    <td><p><strong>Table title</strong></p></td>
    <td><p>Type a title here to display it above the table.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Parameters (for standard reports only)</strong></p></td>
    <td><blockquote>
    <p><strong>Note</strong></p>
    <p>You create standard reports in the <strong>Reports</strong> app.</p>
    <p>In the <strong>Pivot Table</strong> app you set which parameters the system should prompt the user for.</p>
    </blockquote></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Reporting period</strong></p></td>
    <td><p>Controls whether to ask user to enter a report period.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter an organisation unit.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Parent organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter a parent organisation unit.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include regression</strong></p></td>
    <td><p>Includes a column with regression values to the pivot table.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Include cumulative</strong></p></td>
    <td><p>Includes a column with cumulative values to the pivot table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Sort order</strong></p></td>
    <td><p>Controls the sort order of the values.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Top limit</strong></p></td>
    <td><p>Controls the maximum number of rows to include in the pivot table.</p></td>
    </tr>
    </tbody>
    </table>

5.  点击**更新**。

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

## 从数据透视表下载数据 { #pivot_download_data } 

 <!--DHIS2-SECTION-ID:pivot_download_data-->

### 下载表格布局数据格式 { #download-table-layout-data-format } 

要下载当前数据透视表中的数据：

1.  点击**下载**。

2.  在**表格布局**下，单击要下载的格式：
    Microsoft Excel，CSV或HTML。

    数据表每个维度只有一列，并包含名称
    尺寸项。

    > **Tip**
    >
    > When you download a pivot table with organisation units as rows
    > and you've selected **Show hierarchy** in **Table options**, each
    > organisation unit level is rendered as a separate column. This is
    > useful for example when you create Excel pivot tables on a local
    > computer.

> **提示**
>
>您可以从下载的Microsoft Excel中创建数据透视表
> Excel文件。

### 下载纯数据源格式 { #download-plain-data-source-format } 

您可以使用JSON，XML，Excel，
和CSV作为具有不同标识方案（ID，
代码和名称）。数据文档使用维的标识符
项目并在新的浏览器窗口中打开以显示
请求到地址栏中的Web API。这对开发人员很有用
基于DHIS2 Web API的应用程序和其他客户端模块
谁需要计划数据源，例如导入统计数据
包。

要下载纯数据源格式：

1.  点击**下载**。

2.  在**普通数据源**下，单击要下载的格式。

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 18%" />
    <col style="width: 33%" />
    <col style="width: 47%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Action</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>JSON</p></td>
    <td><p>Click <strong>JSON</strong></p></td>
    <td><p>Downloads JSON format based on ID property.</p>
    <p>You can also download JSON format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>XML</p></td>
    <td><p>Click <strong>XML</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download XML format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Microsoft Excel</p></td>
    <td><p>Click <strong>Microsoft Excel</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download Microsoft Excel format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>CSV</p></td>
    <td>Click <strong>CSV</strong></td>
    <td><p>Downloads CSV format based on ID property.</p>
    <p>You can also download CSV format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>JRXML</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>JRXML</strong></p></td>
    <td><p>Produces a template of a Jasper Report which can be further customized based on your exact needs and used as the basis for a standard report in DHIS2.</p></td>
    </tr>
    <tr class="even">
    <td><p>Raw data SQL</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>Raw data SQL</strong></p></td>
    <td><p>Provides the actual SQL statement used to generate the pivot table. You can use it as a data source in a Jasper report, or as the basis for an SQL view.</p></td>
    </tr>
    </tbody>
    </table>

### 下载CSV格式，而不在网络浏览器中呈现数据 { #download-a-csv-format-without-rendering-data-in-the-web-browser } 

您可以直接下载CSV格式的数据，而无需呈现数据
在网络浏览器中。这有助于减少系统中的任何约束
关于最大数量设置的设置
分析记录。这使您可以下载大批数据
可用于以后的脱机分析。

以CSV格式下载数据而无需先在网络中呈现数据
浏览器：

1.  单击**更新**旁边的箭头。

    ![](resources/images/pivot_table/data_dump.png)

2.  单击** CSV **以根据ID属性下载格式。

    该文件下载到您的计算机。

    > **Tip**
    >
    > You can also download CSV format based on **Code** or **Name**
    > property.

## 在外部网页中嵌入数据透视表 { #pivot_embed } 

 <!--DHIS2-SECTION-ID:pivot_embed-->

DHIS2中与分析相关的某些资源，例如数据透视表，图表
和地图，可以使用插件嵌入任何网页中。你会
在的“ Web API”一章中找到有关插件的更多信息。
*《 DHIS2开发人员手册》 *。

生成可用于显示数据透视表的HTML片段
在外部网页中：

1.  点击**嵌入**。

2.  单击**选择**以突出显示HTML片段。

## 将数据透视表数据可视化为图表或地图 { #pivot_integration } 

 <!--DHIS2-SECTION-ID:pivot_integration-->

制作数据透视表后，您可以在数据透视表之间进行切换，
数据的图表和地图可视化。

### 打开数据透视表作为图表 { #open-a-pivot-table-as-a-chart } 

1.  单击**图表** \> **以图表形式打开此表**。

    当前的数据透视表将以图表的形式打开。


![](resources/images/pivot_table/pivot_integration.png)

### 打开数据透视表选择作为图表 { #open-a-pivot-table-selection-as-a-chart } 

如果您想将数据透视表的一小部分可视化为图表，则可以
可以直接单击表中的值，而不是打开整个
表。

1.  在数据透视表中，单击一个值。


    ![](resources/images/pivot_table/pivot_integration_table.png)

2.  要验证选择，请将光标悬停在**“打开选择为”
    图表**。表格中突出显示的尺寸标题指示
    哪些数据将显示为图表。

3.  点击**打开选择为图表**。

### 打开数据透视表作为地图 { #open-a-pivot-table-as-a-map } 

1.  点击**图表** \> **以地图形式打开该表格**

    当前的数据透视表将作为地图打开。

### 打开数据透视表选择作为地图 { #open-a-pivot-table-selection-as-a-map } 

1.  在数据透视表中，单击一个值。

    显示菜单。

2.  点击**将选择作为地图打开**。

    您的选择将作为地图打开。
