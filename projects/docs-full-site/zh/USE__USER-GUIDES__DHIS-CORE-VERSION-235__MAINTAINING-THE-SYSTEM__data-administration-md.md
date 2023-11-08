---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/data-administration.md"
revision_date: "2021-06-14"
---

# 资料管理 { #data_admin }

数据管理模块提供了一系列功能来确保
DHIS2数据库中存储的数据是完整的，并且
数据库性能得到优化。这些功能应在
由数据管理员定期检查以确保
存储的数据是最佳的。

## 数据的完整性 { #dataAdmin_dataIntegrity }

DHIS2可以对数据执行各种数据完整性检查
包含在数据库中。识别和纠正数据完整性
问题对于确保用于
分析目的是否有效。每个数据完整性检查
将描述系统执行的操作以及一般步骤
可以解决这些问题。

### 没有数据集的数据元素 { #data-elements-without-data-set }

每个数据元素必须分配给一个数据集。数据值
如果有数据，将无法将元素输入系统
元素未分配给数据集。选择
在主菜单中选择维护->数据库集->编辑，然后添加
将“孤立的”数据元素添加到适当的数据集。

### 没有组的数据元素 { #data-elements-without-groups }

一些数据元素已经分配给几个数据元素组。
目前不允许这样做，因为这会导致重复
分析记录集中的链接数据记录提供了汇总
数据。转到维护->数据元素组以查看每个数据
确定元素并删除不正确的组分配。

### 违反排他组的数据元素 { #data-elements-violating-exclusive-group-sets }

Some data elements have been allocated to several data element groups that are members of the same data element group set. All group sets in DHIS2 are defined as exclusive, which means that a data element can _only_ be allocated to _one_ data element group within that group set. Go to Maintenance -\> Data elements and indicators -\>Data element groups to review each data element identified in the integrity check. Either remove the data element from all groups except the one that it should be allocated to, or see if one of the groups should be placed in a different group set.

### 数据集中的数据元素，但不在表单或节中 { #data-elements-in-data-set-but-not-in-form-or-sections }

数据元素已分配给数据集，但尚未分配
分配给数据集表格的任何部分。使用的所有数据集
部分表格，通常应在数据集中包含所有数据元素
恰好分配给数据集的一部分。

### 分配给具有不同期间类型的数据集的数据元素 { #data-elements-assigned-to-data-sets-with-different-period-types }

数据元素不应分配给两个单独的数据集
期间类型不同。建议的方法是创建两个
单独的数据元素（例如，每月和每年的数据元素）
并将它们分配给各自的数据集。

### 数据集未分配给组织单位 { #data-sets-not-assigned-to-organisation-units }

所有数据集应分配给至少一个组织单位。

### 类别组合无效的部分 { #sections-with-invalid-category-combinations }

使用节表的数据集应仅具有一个类别
每个部分中的组合。违反可能是由于
将数据元素分配给节，然后更改类别
此数据元素在以后的某个时间点的组合。

### 具有相同公式的指标 { #indicators-with-identical-formulas }

尽管此规则不会影响数据质量，但通常不会
具有两个定义完全相同的指标是有意义的。评论
确定的指标及其公式，并删除或修改任何
指示器似乎是重复的。

### 没有分组的指标 { #indicators-without-groups }

All data elements and indicators must be assigned to at least one group, so these Indicators need to be allocated to their correct Data Element and Indicator Group. From the main menu, go to Data elements/Indicators -\> Indicator Groups, and allocate each of the \`Orphaned\` indicators to its correct group.

### 无效的指标分子 { #invalid-indicator-numerators }

违反此规则的原因可能是错误地引用了
删除或修改的数据元素。查看指标并进行
分子定义的更正。

### 无效的指标分母 { #invalid-indicator-denominators }

违反此规则的原因可能是错误地引用了
删除或修改的数据元素。查看指标并进行
分母定义的更正。

### 违反排他性组的指标 { #indicators-violating-exclusive-group-sets }

Some indicators have been allocated to several indicator groups that are members of the same indicator group set. All group sets in DHIS2 are defined as exclusive, which means that an indicator can _only_ be allocated to _one_ indicator group within that group set. Go to Maintenance -\> Data elements and indicators -\>Indicator groups to review each indicator identified in the integrity check. Either remove the indicator from all groups except the one that it should be allocated to, or see if one of the groups should be placed in a different group set.

### 重复期间 { #duplicate-periods }

如果已从外部应用程序导入了期间，则可能是
某些时期可能会重复。如果您有任何时期
在这里似乎重复的，您将需要解决这些问题
直接在DHIS2数据库中。所有已分配给
重复的期间，应移至正确的期间，并且
重复期间应删除。

### 具有循环引用的组织单位 { #organisation-units-with-cyclic-references }

组织单位不能同时是父级和子级，
直接或间接。如果发生这种情况，您将需要
直接在DHIS2数据库中解析循环引用
通过重新分配“组织单位”表中的“上级”字段
组织单位。

### 孤立的组织单位 { #orphaned-organisation-units }

所有组织单位必须存在于组织单位内
层次结构。转到“组织单位”>“层次结构操作”，然后将
将组织单位冒犯到层次结构中的适当位置。

### 没有团体的组织单位 { #organisation-units-without-groups }

All organisation units _must_ be allocated to at least _one_ group. The problem might either be that you have not defined any compulsory OrgUnit Group Set at all, or that there are violations of the compulsory rule for some OrgUnits . NOTE: If you have defined no compulsory OrgUnit Group Sets, then you must first define them by going to Organisation units-\>Organisation unit group sets and define at least one compulsory Group Set (the group set 'Type' are nearly universally relevant). If you have the relevant group sets, go to Maintenance -\> OrgUnit Groups to review each OrgUnit identified and add the relevant Group allocation.

### 组织单位违反必修课 { #organisation-units-violating-compulsory-group-sets }

These organisation units have not been assigned to the any organisation unit group within one of the _compulsory_ organisation unit group sets. When a group set is defined as compulsory, it means that an organisation unit must be allocated to at least one organisation unit group within that group set. For instance, all organisation units must belong to one of the groups in the 'Type' group set. It might belong to the \`Hospital\` or the \`Clinic\` or any other 'type' group - but it must belong to exactly one of them. Go to Organisation units-\>Organisation unit groups to review each organisation unit identified in the integrity check. Allocate all organisation units to exactly one compulsory group.

### 违反专属组的组织单位 { #organisation-units-violating-exclusive-group-sets }

Some organisation units have been allocated to several organisation unit groups that are members of the same organisation unit group set. All group sets in DHIS2 are defined as exclusive, which means that an organisation unit can _only_ be allocated to _one_ organisation unit group within that Group Set. For instance, one organisation unit cannot normally belong to the both the 'Hospital' and 'Clinic' groups , but rather to only to one of them. Go to Organisation unit-\>Organisation unit groups to review each organisation unit identified in the integrity check. Remove the organisation units from all groups except the one that it should be allocated to.

### 没有组集的组织单位组 { #organisation-unit-groups-without-group-sets }

此处列出的组织单位组尚未分配给
组集。转到维护->组织单位->组织单位
组设置并将组织单位组分配给适当的
组集。

### 无组验证规则 { #validation-rules-without-groups }

All validation rules must be assigned to a group. Go to **Maintenance** app \> **Validation rule group** and assign the offending validation rule to a group.

### 无效的验证规则左侧表达式 { #invalid-validation-rule-left-side-expressions }

An error exists in the left-side validation rule definition. Go to **Maintenance** app \> **Validation rule** and click **Edit** on the offending rule. Click **Left side** and make the required corrections.

### 无效的验证规则右侧表达式 { #invalid-validation-rule-right-side-expressions }

An error exists in the right-side validation rule definition. Go to **Maintenance** app \> **Validation rule** and click **Edit** on the offending rule. Click **Right side** and make the required corrections.

### 无条件的程序规则 { #programrules-with-no-condition }

Report will highlight all the **Program rules** not configured with **Condition**. Evaluation for rules not having condition are always evaluated as false.

### 没有优先权的ProgramRules { #programrules-with-no-priority }

Report will highlight all the **Program rules** not configured with **Priority**. This is optional but its existence is very important when **ProgramRuleActionType** is **ASSIGN**. Rules with ASSIGN action type should have higher priority then the rest of the action types.

### 不采取行动的ProgramRules { #programrules-with-no-action }

Report will highlight all the **Program rules** not configured with any **ProgramRuleAction**.

### 没有dataElements的ProgramRuleVariables { #programrulevariables-without-dataelements }

Report will highlight all the **Program rule variables** not configured with **DataElement**. Report will be based on source type configuration. DataElement should be provided when the source type of ProgramRuleVariable is **DataElement**.

### 没有属性的ProgramRuleVariables { #programrulevariables-without-attributes }

Report will highlight all the **Program rule variables** not configured with **TrackedEntityAttribute**. Report will be based on source type configuration. TrackedEntityAttribute should be provided when the source type of ProgramRuleVariable is **Attribute**.

### 没有数据对象的ProgramRuleActions。 { #programruleactions-with-no-data-objects }

Report will highlight all the **Program rule actions** not configured with any Data object. Data object can be either **DataElement** of **TrackedEntityAttribute**. There are certain ProgramRuleActions which are responsible for assinging values to either dataElement or trackedEntityAttribute.

### 没有通知的ProgramRuleActions { #programruleactions-with-no-notification }

Report will highlight all the **Program rule actions** which have ProgramRuleActionType set to SENDMESSAGE/SCHEDULEMESSAGE where the configuration does not provide any link to notification.

### 没有部分ID的ProgramRuleActions { #programruleactions-with-no-section-id }

Report will highlight all the **Program rule actions** which have ProgramRuleActionType set to **HIDESECTION** but configuration does not provide any section id.

### 没有程序阶段ID的ProgramRuleActions { #programruleactions-with-no-program-stage-id }

Report will highlight all the **Program rule actions** which have ProgramRuleActionType set to **HIDEPROGRAMSTAGE** but configuration does not provide any program stage id.

### 无效的程序指示符表达式 { #invalid-program-indicator-expression }

报告由无效** DataElement **或无效** TrackedEntityAttribute **引起的程序指示器表达式中的所有冲突。

### 无效的程序指示器过滤器表达式 { #invalid-program-indicator-filter-expression }

报告由无效** DataElement **或无效** TrackedEntityAttribute **引起的程序指示器过滤器表达式中的所有冲突。

## 保养 { #data_admin_maintenance }

<table>
<caption>Data maintenance functions in the Data Administration app</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Function</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Clear analytics tables</p></td>
<td><p>Completely empties the analytics tables. These tables are used to generate aggregate data for the pivot tables, GIS and reports.</p></td>
</tr>
<tr class="even">
<td><p>Remove zero data values</p></td>
<td><p>Removes zero data values from the database. Values registered for data elements with aggregation operator average is not removed, as such values will be significant when aggregating the data, contrary to values registered for data elements with aggregation operator sum.</p>
<p>Reducing the number of data values will improve system performance.</p></td>
</tr>
<tr class="odd">
<td><p>Permanently remove soft deleted data values</p></td>
<td><p>When a data value is deleted in DHIS2, the system will mark the corresponding database row as deleted, and not actually delete the row.</p>
<p>Running this maintenance function will physically remove these data value rows from the database.</p></td>
</tr>
<tr class="even">
<td><p>Prune periods</p></td>
<td><p>Removes all periods which have no registered data values. Reducing the number of periods will improve system performance.</p></td>
</tr>
<tr class="odd">
<td><p>Remove expired invitations</p></td>
<td><p>Will delete users which represent user account invitations that now have gone past their expiry date.</p></td>
</tr>
<tr class="even">
<td><p>Drop SQL views</p></td>
<td><p>DHIS2 lets you set up and manage SQL views as system objects with corresponding database SQL views.</p>
<p>Running this maintenance function will drop underlying SQL views for all system views. Use the <strong>Create SQL views</strong> function to recreate these SQL views.</p></td>
</tr>
<tr class="odd">
<td><p>Create SQL views</p></td>
<td><p>Recreates all SQL views in the database.</p></td>
</tr>
<tr class="even">
<td><p>Update category option combinations</p></td>
<td><p>Rebuilds the category option combinations. This may be required after altering the category options which belong to a given category.</p></td>
</tr>
<tr class="odd">
<td><p>Update organisation unit paths</p></td>
<td><p>The organisation unit table in the DHIS2 database has a column &quot;path&quot; which contains a concatenated string of all ancestors in the hierarchy for each organisation unit.</p>
<p>Running this maintenance function will update and ensure that these values are in sync with the current organisation unit hierarchy. This column is managed by DHIS2, but a manual update might be useful when doing data loading directly in the database.</p></td>
</tr>
<tr class="even">
<td><p>Clear application cache</p></td>
<td><p>Clears the system cache.</p></td>
</tr>
<tr class="odd">
<td><p>Reload apps</p></td>
<td><p>Manually reloads and detects installed DHIS2 apps.</p>
<p>The installed apps are also detected when the system starts and when installing or uninstall apps.</p></td>
</tr>
</tbody>
</table>

## 资源表 { #dataAdmin_resourceTables }

资源表是在分析过程中使用的支持表
数据。通常，将这些表的内容与
从第三方应用程序（例如，
Microsoft Excel。分析模块也广泛使用它们
DHIS2。资源表的重新生成只能执行一次
解决了所有数据完整性问题。资源表也
每次运行分析过程时，
系统。

-   组织单位结构（\ _orgunitstructure）

    每当组织单位层次结构发生任何更改时，都应重新生成此表。此表提供有关组织单位层次结构的信息。它为每个组织单位占一行，为每个组织单位级别占一列，并将谱系中所有父代的组织单位标识符作为值。

-   数据元素组集结构（\ _dataelementgroupsetstructure）

    此表提供有关哪些数据元素是哪些数据元素组集的成员的信息。该表对于每个数据元素具有一行，对于每个数据元素组集合具有一列以及作为值的数据元素组的名称。

-   指标组集结构（\ _indicatorgroupsetstructure）

    此表提供有关哪些指标属于哪个指标组集的成员的信息。该表中每个指标占一行，每个指标组集占一列，并且指标组的名称作为值。

-   组织单位组集结构 (\_organizationunitgroupsetstructural)

    此表提供有关哪些组织单位是哪些组织单位组集的成员的信息。该表中每个组织单位占一行，每个组织单位组集占一列，并以组织单位组的名称作为值。

-   类别结构（\ _categorystructure）

    此表提供有关哪些数据元素属于哪些类别的成员的信息。该表中每个数据元素占一行，每个类别占一列，并且类别选项的名称作为值。

-   数据元素类别选项组合名称（\ _categoryoptioncomboname）

    每当类别组合名称发生更改时，都应重新生成此表。它包含各种类别组合的可读名称。

-   数据元素结构（\ _dataelementstructure）

    此表提供有关所有数据元素以及它们捕获数据的周期类型（频率）的信息。周期类型是通过数据集成员资格确定的，因此依赖于数据元素是具有相似周期类型的数据集的成员以具有定义的行为。

-   期间结构（\ _dataperiodstructure）

    此表提供有关所有期间以及与其关联的期间类型的信息。对于每个频率低于其自身的周期类型，它包含有关其属于哪个周期的信息。

-   数据元素类别选项组合 (\_dataelementcategoryoptioncombo)

    该表提供了数据元素和所有可能的类别选项组合之间的映射。

## 分析表管理 { #analytics_tables_management }

DHIS2 generates database tables which the system then uses as basis for various analytics functions. These tables are also valuable if you write advanced SQL reports. In the **Data Administration** app, you can execute the tables generation immediately. If you want to schedule them to be executed at regular intervals, this can be done in the **Scheduler** app. This means that you can refresh recent analytics on demand and see updated pivot tables without waiting for all of the past years data to re-process.

> **注意**
>
> 您还可以通过 Web API 生成表格。此任务通常由系统管理员执行。

1.  Open the **Data Administration** app and click **Analytics Tables**.

2.  选择要跳过的分析过程部分：

    -   **跳过资源表的生成**

    -   **跳过汇总数据和完整性数据的生成**

    -   **跳过事件数据的生成**

    -   **跳过注册数据的生成**

3.  Select **Number of last years of data to include**.

4.  点击**开始导出**。

## 数据统计 { #dataAdmin_dataStatistics }

数据统计模块提供了对象数量的概述
存储在DHIS2数据库中。

![](resources/images/maintainence/data_stats.png)

每种类型的对象的总数以一系列
表，其中包含每个对象的摘要统计信息。

## 锁定异常 { #dataAdmin_lockException }

锁定异常可提供对豁免的细粒度控制
锁定的数据集。数据集到期后，数据输入将为
默认情况下被拒绝，除非已通过锁定授予了例外
异常接口。要启用锁定异常，请选择所需的
组织单位，数据集和时间段，然后按“添加”。通过
授予锁定例外，即使在
数据集的有效期限已过。

![](resources/images/maintainence/create_lock_exception.png)

在上面的示例中，将为“ ab
“丰富的生命组织”和“ ab第七日医院”的“护理”
和支持”数据集（“ 2012年2月”）。

## 最小-最大值生成 { #dataAdmin_minMaxValueGeneration }

此管理功能可用于生成最小值-最大值，
作为数据质量和验证过程的一部分，
特定的组织单位和数据集。只需选择数据集
从左手框架，然后选择所需的组织
单位以从组织单位生成最小-最大值
右侧的选择器。按“生成”按钮生成或
重新生成所有最小-最大值。按“删除”删除所有最小-最大
当前存储在数据库中的值。

![](resources/images/maintainence/min_max_value_generation.PNG)

## 缓存统计 { #dataAdmin_cacheStatistics }

此选项仅供系统管理员使用。缓存
统计信息显示应用程序级别缓存的状态。的
应用程序级缓存是指对象和查询结果
应用程序正在缓存以提高性能。如果数据库
已直接修改，需要清除应用程序缓存
它才能生效。
