---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/importexport-app.md"
revision_date: "2021-06-14"
---

# 导入/导出应用 { #import_export }

在初级卫生系统中，HMIS通常涉及分布式
应用程序，同一应用程序在不同的位置运行
地理位置（PHC，CHC，医院，地区和州）。
这些物理位置中许多都没有Internet连接，并且
因此他们离线工作。在某个时候（通常在该地区
级别），则数据需要同步才能具有
特定地理区域的统一数据库。对于
因此，重要的是能够从一个位置导出数据（
正在离线工作（例如在医疗机构级别），然后导入
另一个（例如在地区级别）。
因此，导出和导入的此功能是HMIS的关键功能。
此功能还可以帮助我们克服某些方面对Internet的依赖
度，因为数据更新可以通过没有密钥的USB密钥进行传输
连接性，或者在互联网有限的情况下通过电子邮件
连接性。 DHIS2提供了强大的导出-导入功能来
满足这些需求。

要访问导入/导出应用，请在顶部标题栏中搜索
进出口。导入/导出应用程序提供了许多服务详细信息
可以在下面找到。

![](resources/images/import_export/overview.png)

## 汇入资料 { #importing_data }

### 导入进度记录器 { #import_progress_logger }

无论您导入什么（“数据”、“事件”、“GML”、“元数据”或“跟踪的实体实例”数据），您始终可以通过查看顶部的“作业摘要”来查看导入进度页面的。

### 导入摘要 { #metadata_import_summaries }

导入请求完成后，我们会在导入表单上方显示导入摘要。任何冲突或错误都会显示在导入主要摘要下方的表中。

![](resources/images/import_export/import_summary.png)

### 元数据导入 { #metadata_import }

可以从侧边栏单击来访问元数据导入
元数据导入。

![](resources/images/import_export/metadata_import.png)

1.  选择要上传的文件

2.  从可用格式中进行选择，例如_JSON_、_XML_ 或 _CSV_

3.  选择以下适当的设置：

    -   识别码
    -   导入报告模式
    -   预热模式
    -   导入策略
    -   原子模式
    -   合并模式

4.  Click **Advanced options** if you want to adjust one or more of the following settings before importing:

    -   冲洗模式
    -   跳过分享
    -   跳过验证
    -   异步
    -   包容性策略

5.  Click on the **Import** button which will upload the file and start the importing process.

> **Tip**
>
> **It is highly recommend to use the Dry run option** to test before importing data; to make sure you keep control over any changes to your Metadata, and to check for problems with out-of-sync data elements or organisation unit names

> **Note**
>
> If an organisation unit e.g. `Nduvuibu MCHP` had a unknown reference to an object with ID `aaaU6Kr7Gtpidn`, it means that the object with ID `aaaU6Kr7Gtpidn` was not present in your imported file, and it was not found in the existing database.
>
> You can control this using **Identifier** option, to indicate if you want to allow objects with such invalid references to be imported or not. If you choose to import invalid references you will have to correct the reference manually in DHIS2 later.

#### DXF2中的匹配标识符 { #matching_identifiers_in_dxf2 }

DXF2格式目前支持匹配两个标识符，即
内部DHIS2标识符（称为UID），也使用外部
标识符称为“代码”。进口商尝试搜索时
对于引用（例如上面的引用），它将首先转到UID字段，
然后转到代码字段。这使您可以从旧版导入
系统中没有每个元数据对象的UID。即如果你是
从旧版系统导入设施数据，您可以省略ID
完整字段（DHIS2将为您填写），然后将
代码字段中的旧系统自己的标识符，此标识符为
必须是唯一的。这不仅适用于组织单位，而且
用于各种元数据，从而可以轻松地从其他系统导入。

### 资料汇入 { #import }

可以通过单击侧边栏上的数据来访问数据导入
进口。

![](resources/images/import_export/data_import.png)

1.  选择要上传的文件

2.  从可用格式中选择：_JSON_、_XML_、_PDF_、_ADX_ 或 _CSV_

3.  选择以下适当的设置：

    -   战略
    -   预热缓存

4.  Click **Advanced options** if you want to adjust one or more of the following settings before importing:

    -   数据元素ID方案
    -   组织单位ID方案
    -   ID方案
    -   跳过现有支票

5.  Click on the **Import** button which will upload the file and start the importing process.

> **提示**
>
> **强烈建议在导入数据之前使用试运行选项**进行测试；确保您控制对元数据的任何更改，并检查数据元素或组织单位名称不同步的问题

#### PDF资料 { #importPDFdata }

DHIS2 supports import of data in the PDF format. This can be used to import data produced by off-line PDF data entry forms. Please refer to the section **Data set management** for details on how to produce a PDF form which can be used for off-line data entry.

To import a PDF data file, navigate to the _PDF Data Import_ item in the side menu. Upload the completed PDF file and click _Import_.

### 事件汇入 { #event_import }

通过单击事件可以从边栏中访问事件
进口。

![](resources/images/import_export/event_import.png)

1.  从可用格式中进行选择，例如_JSON_、_XML_ 或 _CSV_

2.  Click **Advanced options** if you want to adjust one or more of the following settings before importing:

    -   事件ID方案
    -   数据元素ID方案
    -   组织单位ID方案
    -   ID方案

3.  Click on the **Import** button which will upload the file and start the importing process.

### GML导入 { #gml_import }

单击侧边栏上的GML可以访问GML导入
进口。

![](resources/images/import_export/gml_import.png)

1.  使用 _GML_（地理标记语言）格式上传文件。

2.  Click on the **Import** button which will upload the file and start the importing process.

### 跟踪实体实例导入 { #tei_import }

可以通过单击 TEI 导入从侧边栏访问跟踪实体实例导入。

![](resources/images/import_export/tei_import.png)

1.  选择要上传的文件

2.  从可用格式中进行选择，例如_JSON_ 或 _XML_

3.  选择以下适当的设置：

    -   识别码
    -   导入报告模式
    -   预热模式
    -   导入策略
    -   原子模式
    -   合并模式

4.  Click **Advanced options** if you want to adjust one or more of the following settings before importing:

    -   冲洗模式
    -   跳过分享
    -   跳过验证
    -   包容性策略

5.  Click on the **Import** button which will upload the file and start the importing process.

> **提示**
>
> **强烈建议在导入数据之前使用试运行选项**进行测试；以确保您可以控制对跟踪实体实例的任何更改。

## 汇出资料 { #exporting-data }

### 元数据导出 { #metadata_export }

单击侧边栏上的，可以访问元数据导出
元数据导出。

![](resources/images/import_export/metadata_export.png)

1.  选择您要导出的对象列表。

2.  选择导出_格式_ _JSON_、_CSV_ 或 _XML_

3.  选择_压缩_类型_zip_、_gzip_或_未压缩_

4.  Choose option _Sharing_ with or without sharing.

5.  Click **Export metadata** which will open a new web-browser window that will give you a file to download to your local computer.

### 具有依赖项的元数据导出 { #metadata_export_dependencies }

具有依赖项的元数据导出使您可以为以下内容创建罐头导出
元数据对象。这种类型的导出将包括元数据对象
和元数据对象的相关对象；即元数据
与主要对象一起属于

<table>
<caption>Object types and their dependencies</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Object type</p></th>
<th><p>Dependencies included in export</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Data sets</strong></p>
<!--DHIS2_SECTION_ID:docs-internal-guid-4a3662ce-63b9-1efd-e640-8ba874d1bcde--></td>
<td><p>Data elements</p>
<p>Sections</p>
<p>Indicators</p>
<p>Indicator types</p>
<p>Attributes</p>
<p>Data entry forms</p>
<p>Legend sets</p>
<p>Legends</p>
<p>Category combinations</p>
<p>Categories</p>
<p>Category options</p>
<p>Category option combinations</p>
<p>Option sets</p></td>
</tr>
<tr class="even">
<td><p>Programs</p></td>
<td><p>Data entry form</p>
<p>Tracked entity</p>
<p>Program stages</p>
<p>Program attributes</p>
<p>Program indicators</p>
<p>Program rules</p>
<p>Program rule actions</p>
<p>Program rule variables</p>
<p>Program attributes</p>
<p>Data elements</p>
<p>Category combinations</p>
<p>Categories</p>
<p>Category options</p>
<p>Category option combinations</p>
<p>Option sets</p></td>
</tr>
<tr class="odd">
<td><p>Category combination</p></td>
<td><p>Category combinations</p>
<p>Categories</p>
<p>Category options</p>
<p>Category option combinations</p>
<p>Attributes</p></td>
</tr>
<tr class="even">
<td><p>Dashboard</p></td>
<td><p>Dashboard items</p>
<p>Charts</p>
<p>Event charts</p>
<p>Pivot tables</p>
<p>Event reports</p>
<p>Maps</p>
<p>Reports</p>
<p>Resources</p></td>
</tr>
<tr class="odd">
<td><p>Data element groups</p></td>
<td><p>Data elements</p>
<p>Category combinations</p>
<p>Categories</p>
<p>Category options</p>
<p>Category option combinations</p>
<p>Option sets</p>
<p>Attributes</p>
<p>Legend sets</p>
<p>Legends</p></td>
</tr>
<tr class="even">
<td><p>OptionSets</p></td>
<td><p>Option</p></td>
</tr>
</tbody>
</table>

![](resources/images/import_export/metadata_dependency_export.png)

![](resources/images/import_export/metadata_dependency_export_object_types.png)

1.  选择 **对象类型**：**数据集**、**程序**、**类别组合**、**仪表板**、**数据元素组** 或 **选项集**。

2.  选择一个**对象**。

3.  选择一种格式：** JSON **或** XML **。

4.  选择** Compression **：** Zip **，** Gzip **或** Uncompressed **。

5.  Click **Export metadata dependencies** which will open a new web-browser window that will give you a file to download to your local computer.

### 资料汇出 { #data_export }

可以通过单击数据从侧边栏访问数据导出
出口。

![](resources/images/import_export/data_export.png)

1.  选择_组织单位_。

2.  选择是否要导出包含步骤 1 中选择的组织单位的后代或仅包含手动选择的组织单位。

3.  选择_数据集_。

4.  设置_开始_和_结束日期_。

5.  选择一种格式：** XML **，** CSV **或** JSON **。

6.  选择** Compression **：** Zip **，** Gzip **或** Uncompressed **。

7.  Click **Advanced options** if you want to adjust one or more of the following settings before exporting:

    -   包括已删除
    -   数据元素ID方案
    -   组织单位ID方案
    -   ID方案

8.  Click **Export data** which will open a new web-browser window that will give you a file to download to your local computer.

### 活动导出 { #event_export }

通过单击事件可以从边栏中访问事件导出
出口。

![](resources/images/import_export/event_export.png)

You can export event or tracker data in **XML** , **JSON** or **CSV** formats.

1.  选择一个组织单位。

2.  选择**包含**：

    -   **选定**：仅导出选定组织部门的事件数据

    -   **正下方**：导出事件数据，包括选择内的第一级组织单位以及所选组织单位本身。

    -   **以下全部**：导出所选内容内所有组织单位以及所选组织单位本身的事件数据。

3.  选择一个程序和一个程序阶段（如果适用）。

4.  选择**开始日期**和**结束日期**。

5.  选择一种格式：** XML **，** JSON **或** CSV **。

6.  选择** Compression **：** Zip **，** Gzip **或** Uncompressed **。

7.  Click **Advanced options** if you want to adjust one or more of the following settings before exporting:

    -   包括已删除
    -   数据元素ID方案
    -   组织单位ID方案
    -   ID方案

8.  Click **Export events** which will open a new web-browser window that will give you a file to download to your local computer.

### 跟踪实体实例导出 { #tei_export }

可以通过单击 TEI 导出从侧边栏访问跟踪的实体实例导出。

![](resources/images/import_export/tei_export.png)

You can export event or tracker data in **XML** , **JSON** or **CSV** formats.

1.  选择应包含的_组织单位_。

2.  选择是否要按_节目_或_跟踪实体类型_进行过滤。

3.  选择一种格式：** XML **，** JSON **或** CSV **。

4.  Click **Advanced options** if you want to adjust one or more of the following settings before exporting:

    -   按上次更新日期筛选
    -   分配的用户模式
    -   包括已删除
    -   包括所有属性
    -   数据元素ID方案
    -   事件ID方案
    -   组织单位ID方案
    -   ID方案

5.  Click **Export tracked entity instances** which will open a new web-browser window that will give you a file to download to your local computer.

## 工作概述 { #job_overview }

可以通过单击_作业概述_从侧边栏访问作业概述页面。

![](resources/images/import_export/job_overview.png)

通过此页面，您可以查看已启动此会话的所有导入的进度。您可以在左侧看到所有作业的列表，并在右侧看到有关特定选定作业的详细信息。

### 按导入作业类型过滤 { #filtering-by-import-job-type }

![](resources/images/import_export/job_overview_filter.png)

默认情况下，所有导入类型的作业都会显示在作业列表中，但您可以通过单击作业列表上方的作业类型过滤器来过滤您感兴趣的类别。

### 重新创建上一份工作 { #recreating-a-previous-job }

![](resources/images/import_export/job_overview_recreate.png)

假设您已从列表中选择了一个作业，您可以通过单击页面底部的_重新创建作业_按钮来重新创建以前运行的导入作业。这将带您进入正确的导入页面，并填写与您选择重新创建的作业完全相同的所有表单详细信息。

## 方案 { #schemes }

许多导入和导出页面中使用的各种方案也称为标识符方案，用于在导入期间将元数据对象映射到其他元数据，以及将元数据呈现为导出的一部分。

<table>
<caption>可用值</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>方案</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ID、UID</td>
<td>匹配 DHIS2 稳定标识符，这是默认 ID 方案。</td>
</tr>
<tr class="even">
<td>代码</td>
<td>匹配 DHIS2 代码，主要用于与外部系统交换数据。</td>
</tr>
<tr class="odd">
<td>姓名</td>
<td>匹配 DHIS2 名称，请注意，这使用可用的 <em>object.name</em>，而不是翻译名称。另请注意，名称并不总是唯一的，在这种情况下，无法使用它们。</td>
</tr>
<tr class="even">
<td>属性：ID</td>
<td>匹配元数据属性，该属性需要分配给您要匹配的类型，并且唯一属性设置为<em> true</em>。它的主要用途也是与外部系统交换数据，它比 <em>CODE</em> 有一些优势，因为多个属性可以添加，因此可用于与多个系统同步。</td>
</tr>
</tbody>
</table>

### ID方案 { #id-scheme }

ID 方案适用于所有类型的对象，但可以被更具体的对象类型覆盖。
