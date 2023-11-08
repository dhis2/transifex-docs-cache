---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/commonmark/en/content/user/using-the-tracker-capture-app.md"
---

# 使用Tracker Capture应用

 <!--DHIS2-SECTION-ID:tracker_capture_app-->

## 关于Tracker Capture应用

 <!--DHIS2-SECTION-ID:about_tracker_capture_app-->

![](resources/images/tracker_capture/tracker-capture-tei-list.png)

** Tracker Capture **应用程序是** Event的高级版本
捕获**应用。

  - **事件捕获**：处理单个事件 *无需*注册

  - **跟踪器捕获**：处理多个事件（包括单个事件）
    活动）*注册*。

  - 您捕获注册的跟踪实体实例的事件数据
    （TEI）。

  - 您只会看到与您拥有的组织单位相关的程序
    您可以选择并通过您的用户角色查看的程序。

  - 您在搜索和注册功能中看到的选项取决于
    您选择的程序。程序属性控制这些
    选项。该属性还决定TEI中的列名称
    清单。

    如果未选择程序，则系统将选择默认属性。

  - 跳过逻辑和验证错误/警告消息均受支持
    在注册期间。

  - 关闭单位部门后，您将无法注册或修改
    在 **Tracker Capture** 应用程序中将事件发送到此组织单位。你
    仍然可以搜索TEI并过滤搜索结果。您可以
    还可以查看特定TEI的仪表板。

## 关于跟踪的实体实例（TEI）仪表板

 <!--DHIS2-SECTION-ID:about_tracked_entity_instance_dashboard-->

![](resources/images/tracker_capture/tei_dashboard.png)

您可以通过 **Tracker Capture** 应用程序中的 TEI 仪表板管理 TEI。

  - 仪表板由小部件组成。拖放小部件以放置
    按照您想要的顺序和位置。

  - 单击图钉图标以将小部件的右列粘贴到修复
    位置。这在数据输入期间尤其有用。

    如果您需要填写许多数据元素或大表格，请粘贴
    右小部件列。然后，所有放置在右侧的小部件
    在数据输入部分中滚动时，该列保持可见。

  - 为您选择的程序定义的任何指标都将具有
    计算并显示在 **指标** 小部件中的值。

  - 导航：

      - **返回**：带您返回搜索和注册页面

      - 上一个和下一个按钮：带您进入上一个或下一个TEI
        TEI搜索结果列表中的仪表板

    <!-- end list -->

      - **其他程序**字段：如果TEI已注册其他
        程序，它们在这里列出。单击一个程序以更改
        您要为其输入所选TEI数据的程序。当你
        更改程序，小部件中的内容也会更改。

## 工作流程

 <!--DHIS2-SECTION-ID:workflow_tracker_capture-->

母子健康的工作过程
程序

![](resources/images/patients_programs/name_based_information_tracking_process.png)

1.  创建新的或找到现有的TEI。

    您可以搜索已定义的属性，例如名称或地址。

2.  将TEI注册到程序中。

3.  根据当时的计划服务，该应用会创建一个
    TEI的活动计划。

4.  根据程序，TEI将提供各种服务。
    记录所有服务。

5.  使用有关个别案例的信息来创建报告。

## 链接到Tracker Capture应用

 <!--DHIS2-SECTION-ID:linking_to_the_tracker_capture_app-->

### 链接到“主屏幕”上的特定程序
您可以在“主屏幕上共享程序选择。

1. 打开 **Tracker Capture** （随访采集）应用程序。

2. 选择要链接的程序。

3. 复制URL。

    * 确保URL包含“ program”参数。

4. 将网址粘贴到您选择的共享方法中，例如
  电子邮件或DHIS2中的消息。

  > Note: If the program does not exist in the selected organisation unit (that is stored in the local cache) the system will instead
  > select the first available program for that organisation unit. If the local cache is empty/clean and the root organisation unit
  > of the current user does not have the specified program, the system will also here select the first available program for the root
  > organisation unit.

### 链接到TEI仪表板
您可以通过其网址共享TEI仪表板。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开您要共享的仪表板。

3.  复制URL。

    确保URL包含“ tei”，“ program”和“ ou”
    （组织单位）参数。

4.  将网址粘贴到您选择的共享方法中，例如
    电子邮件或DHIS2中的消息。

    如果您在单击链接时未登录DHIS2，则将
    要求这样做，然后带到仪表板。

## 创建TEI并将其注册到程序中

 <!--DHIS2-SECTION-ID:create_and_enroll_tracked_entity_instance-->

您可以创建TEI并通过一次操作将该TEI注册到程序中：

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  在左侧窗格的组织单位树中，选择一个
    组织单位。

3.  选择一个程序。

4.  点击**注册**。

5.  填写必填信息。

    跟踪的实体类型和程序都可以配置为使用要素类型。
    这样就可以捕获TEI或注册的几何图形。
    支持的要素类型为“点”和“多边形”。请参阅**如何使用几何**。

6. 如果所选程序配置为在注册期间显示第一阶段，
   该阶段中的所有必填字段都必须填写。在该阶段结束时
   还会询问您是否要完成输入数据的阶段。
   如果您选择**是**，则该阶段将在保存后处于完成状态。如果您选择**否**，
   舞台将活跃状态。

7.  如果配置了搜索程序，则将进行后台搜索
    在可搜索字段上执行以帮助您防止注册
    重复。如果有匹配的TEI，则将出现一个蓝色框
    显示在表格的右侧，可以查看
    这些匹配
TEI。

![](resources/images/tracker_capture/tracker_capture_register_integrated_search.png)

如果有任何匹配的 TEI，请单击 **Continue** 以查看可能的
在注册新的之前重复。

如果没有匹配的 TEI，请单击 **Save and continue** 或 **Save and
添新**

  - **保存并继续**：完成注册并打开
    注册的TEI仪表板

  - **保存并添加新**：完成注册但保留在
    同一页。要注册并注册一个时使用此选项
    TEI陆续没有输入数据。

>注意：必须填写所有必填属性才能保存。
>强制性属性在属性标签旁边标记有红色星号。
>如果用户具有__“忽略跟踪器和事件捕获中必填字段的验证”权限__
>您将不需要填写必填属性，并且将
>在属性标签旁边看不到红星。注意超级用户
具有__“ ALL” __权限的>将自动具有此权限。

## 打开现有的TEI仪表板

<!--DHIS2-SECTION-ID:open_existing_tracked_entity_instance_dashboard-->

查找TEI的方法有多种：使用“列表”
当前选择中的预定义列表，或“搜索”全局
抬头。

### 清单

<!--DHIS2-SECTION-ID:simple_tracked_entity_instance_search-->

列表用于查找和显示所选组织单位中的TEI
和程序。

1.  打开跟踪的捕获应用程序

2.  在左侧窗格的组织单位树中，选择一个
    组织单位

3.  选择一个程序

4.  如果尚未选择，请单击“列表”按钮

如果未配置，则一组预定义列表将可用：

1.  具有任何注册状态的任何TEI

2.  积极注册当前计划的TEI

3.  已完成当前课程注册的TEI

4.  已取消当前课程注册的TEI

![](resources/images/tracker_capture/tracker_capture_lists.png)

您可以选择要显示或隐藏在每个列表中的列
程序。这将保存在您的用户设置中。

1.  单击**网格**图标按钮

2.  检查您要包括的列

3.  点击**保存**

还有一个选项可以创建具有自己的自定义工作清单
过滤器。这可用于动态创建自定义列表。

![](resources/images/tracker_capture/tracker_capture_lists_custom.png)

列表也可以下载或打印。

![](resources/images/tracker_capture/tracker_capture_lists_download.png)

#### 自定义预定义列表

如果程序有任何与之关联的自定义跟踪实体过滤器，
这些将取代上面提到的四个预定义列表。
预定义的列表在配置好后将是查找的有效方法
或使用该程序中与用户相关的数据。

可以使用多种选项来定义工作列表，这里有一些
例子：

- 在给定的程序阶段显示至少一个事件的所有TEI
- 截止日期为当前日期。
- 显示至少具有一个分配给该事件的事件的所有TEI
- 登录用户。
- 显示所有活动的但未分配给任何用户的TEI。

![跟踪器捕获中的预定义工作列表](resources/images/tracker_capture/predefined_working_list_based_on_user_assignment.png)

有关支持的功能的完整列表，请参见API文档。
这些预定义的跟踪实体实例过滤器。

### 搜索

<!--DHIS2-SECTION-ID:advanced_tracked_entity_instance_search-->

搜索用于在用户拥有的组织单位中搜索TEI
搜索访问。如果您想查找TEI，则可以使用它，但是您可以
不知道TEI参加了哪个组织单位或程序。
有两种方法：有和没有程序上下文。
需要配置可搜索字段。用于配置搜索
程序上下文，这是针对
程序维护应用程序。用于不使用程序配置搜索
上下文中，这是针对
跟踪的实体类型维护应用。

**在没有程序上下文的情况下进行搜索：**

1.  打开 **Tracker Capture 应用程序**

2.  点击**搜索**按钮

3.  可搜索字段将成组显示。唯一属性是
    仅可单独搜索。可以组合非唯一属性。

4.  填写搜索条件并点击**搜索**图标按钮。

**在程序上下文中搜索：**

1.  打开 **Tracker Capture 应用程序**

2.  选择具有您要搜索的程序的组织单位
    在

3.  选择程序

4.  点击**搜索**按钮

5.  可搜索字段将成组显示。唯一属性是
    仅可单独搜索。可以组合非唯一属性。

6.  填写搜索条件并点击**搜索**图标按钮

![](resources/images/tracker_capture/tracker_capture_search_screen.png)

搜索完成后，将向您显示搜索
结果。显示的内容取决于搜索结果。

对于唯一属性搜索：

  - 如果找不到匹配的TEI，则可以打开
    报名表格。

  - 如果在选定的组织单位中找到TEI，则TEI
    仪表板将自动打开。

  - 如果在选定的组织单位外部找到TEI，则您
    将有可能开放TEI。

对于非唯一属性搜索：

  - 如果找不到匹配的TEI，则可以打开
    报名表格。

  - 如果找到匹配的TEI，则可以单击
    结果列表，或打开注册表。

  - 如果找到太多匹配项，系统将提示您
    优化搜索条件

![](resources/images/tracker_capture/tracker_capture_search_results.png)

搜索结果具有用于标记跟踪的实体实例的功能
尽可能的重复，请参见下一章。

选择打开注册表格时，搜索值将
自动填写注册表。

### 将跟踪的实体实例标记为潜在重复项

在跟踪器捕获应用程序中搜索被跟踪实体实例时，用户
有时会怀疑一个或多个搜索命中是重复的
其他跟踪的实体实例。用户可以选择点击
**在搜索结果网格的最右列中标记可能的重复**链接。

以这种方式标记的跟踪实体实例将被标记为“可能重复”
在DHIS2数据库中。该标志表示被跟踪的实体实例是/具有
重复。用户在两个地方都可以看到这样的标记。一个是
结果列表本身（在此示例中，Mark Robinson已被标记为潜在
重复）：

![Tracker 捕获搜索结果](resources/images/tracker_capture/tracker_capture_search_results.png)

另一个位置在跟踪的实体实例仪表板中：

![被跟踪的实体实例标记为重复](resources/images/tracker_capture/tracked_entity_instance_flagged_as_duplicate.png)

除了可能通知用户有关所跟踪实体实例的信息外
如果是重复项，该标志将被基础系统用于查找和
在以后的DHIS2版本中合并重复项。

### 打破玻璃

<!--DHIS2-SECTION-ID:break_glass-->

如果程序配置了访问级别 **protected**，并且
用户搜索并查找由以下人员拥有的跟踪实体实例
用户没有数据采集权限的组织单位
因为，用户可以选择打破玻璃。这
用户会给出一个打破玻璃的原因，然后获得暂时的
被跟踪实体的所有权
实例。

## 在程序中注册现有的TEI

 <!--DHIS2-SECTION-ID:enroll_existing_tracked_entity_instance_in_program-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  选择一个程序。

4.  在**注册**小元件中，点击**添加新**。

5.  填写需要信息，然后点击**注册**。

## 输入TEI的事件数据

 <!--DHIS2-SECTION-ID:enter_event_data_for_tracked_entity_instance-->

### 数据输入小部件

#### 

在 TEI 仪表板中，您在 **时间线数据条目** 中输入事件数据
或**表格数据输入**小部件。

 <table>
 Tracker Capture应用程序中的<caption>数据输入小部件</caption>
 <colgroup>
 <col style="width: 31%" />
 <col style="width: 68%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p>小部件名称</p> </th>
 <th> <p>说明</p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>时间轴数据条目</strong> </p> </td>
 <td> <p>使用默认或自定义格式输入数据。 </p>
 <p>根据程序定义，特别是程序阶段，将及时显示事件。单击任何一个将显示相应的数据条目。如果某个阶段需要新事件，则会显示一个加号图标以创建新事件。要进行数据输入，必须具有事件日期。指定事件日期后，将无法更改到期日期。假设通过指定事件日期，事件已经发生。如果尚未发生该事件，则可以更改到期日-这实际上只是在重新安排时间。底部的按钮有助于更改所选事件的状态。 </p>
 <p>此小部件的另一个关键功能是为事件添加多个注释。通常，数据记录是通过数据元素进行的，但是在某些情况下，有必要记录其他信息或注释。这是笔记部分方便的地方。但是，无法删除便笺。这个想法是笔记更像是日志。数据输入期间同时支持跳过逻辑消息和验证错误/警告消息。 </p>
 <p>时间线数据条目中还包含用于将数据条目与以前的条目进行比较的选项。可以通过单击&quot;开关以比较“时间轴数据”输入小部件右上角的form&quot;按钮（两张纸）来启用此功能。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p> <strong>表格数据条目</strong> </p> </td>
 <td> <p>用于表格式数据输入。 </p>
 <p>该小部件将程序阶段列表显示为左侧标签。事件将在表中列出以供可重复的程序阶段使用，并允许对事件数据值进行在线编辑。 </p> </td>
 </tr>
 </tbody>
 </table>

### 建立活动

您可以通过以下方式为TEI创建事件：

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在 **时间线数据条目** 或 **表格数据条目** 小部件中，
    点击** + **按钮。

4.  选择 **Programstage** 并设置 **Report date**。

    程序阶段可以配置为使用功能部件类型。
    这样就可以捕获事件的几何形状。
    支持的要素类型为“点”和“多边形”。请参阅**如何使用几何**。

5.  点击**保存**。

### 安排活动

您可以通过以下方式取消事件的将来日期：

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在 **时间线数据条目** 或 **表格数据条目** 小部件中，
    单击**日历** 图标。

4.  选择 **Programstage** 并设置 **Schedule date**。

5.  点击**保存**。

### 推荐活动

有时将病人转介给其他人可能很必要
**组织单位**。引用TEI：

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在 **时间线数据条目** 或 **表格数据条目** 小部件中，
    单击**箭头**图标。

4.  选择 **Programstage**、**Organisation unit** 并设置一个
    ****报告日期****。

5.  单击 **一次性推荐**，这将只推荐一个 TEI
    单个事件或**永久移动**，这将移动 TEI 所有权
    到选定的**组织单位**。进一步访问 TEI
    将基于所有权组织单位。

### 事件中的强制数据元素
事件中的某些数据元素可能是必需的（在数据元素标签旁边标记有红色星号）。
这意味着必须在允许用户完成事件之前填写所有必需的数据元素。
例外情况是，如果用户具有被称为__“忽略跟踪器和事件捕获中必填字段的验证”的权限。__
如果用户拥有此权限，则在保存和删除之前不需要填写必需的数据元素。
红色星形将不会显示在数据元素标签旁边。请注意，具有__“ ALL” __权限的超级用户会自动
有这个权限。

## 如何使用几何

跟踪的实体类型，程序和程序阶段可以配置为
使用要素类型。这样就可以捕获用于
TEI，程序或事件。支持的要素类型为“点”和“多边形”。

### 捕捉坐标
**选项1：**在字段中填写纬度和经度。

**选项2：**
1.  点击**地图图标**
2.  通过在其上搜索或定位找到所需的位置
    地图
3.  详细您的目的的位置，然后选择**设置坐标**
4.  点击底部的**捕获**

### 捕捉多边形
1.  点击**地图图标**
2.  通过在其上搜索或定位找到所需的位置
    地图
3.  在地图左上角，点击**多边形图标**
4.  在地图上绘制一个多边形。最后，将最后一点与
    第一点
5.  点击底部的**捕获**

![](resources/images/tracker_capture/capture_geometry.png)

多边形也可以删除
1.  点击**地图图标**
2.  点击地图左侧的**垃圾箱图标**，然后选择
    **清除所有**

## 如何为事件分配用户

在维护应用程序中，可以将程序阶段配置为允许用户分配。
如果启用了用户分配，则可以为事件分配用户。

1. 单击**分配的用户** 字段。
2. 滚动或搜索用户。
3. 单击用户。

## 管理TEI的注册

<!--DHIS2-SECTION-ID:manage_tracked_entity_instance_enrollment-->
注册小部件可以访问信息和功能
用于注册所选课程。

![注册小部件](resources/images/tracker_capture/enrollment_widget.png)

### TEI 所有权

显示所选计划中所有注册的当前所有权
在注册小部件的“所有者”部分。所有权将永远开始
作为首先将 TEI 注册到给定计划的组织单位。

对于不同的 TEIS 计划，所有权可能不同，例如，一个诊所可以
另一家诊所对同一名妇幼保健院患者进行随访。

要更新 TEI/程序组合的所有权，用户必须利用
推荐功能并在推荐时选择“永久移动”选项。

具有对作为当前所有者的组织单位的捕获访问权限的用户
TEI/计划将对该 TEI/计划组合的所有注册拥有写入权限。
对作为当前所有者的组织部门具有搜索权限的用户将拥有
访问搜索和查找 TEI/程序组合。

### 停用 TEI 注册

<!--DHIS2-SECTION-ID:deactivate_tracked_entity_instance_enrollment-->

如果禁用TEI仪表板，则TEI变为“只读”。您
无法输入数据，注册TEI或编辑TEI的个人资料。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在里面**注册**小点，点击**手指**。

4.  单击**是**进行确认。

### 激活TEI的注册

 <!--DHIS2-SECTION-ID:activate_tracked_entity_instance_enrollment-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **激活**。

4.  点击**是**
确认。

### 将TEI的注册标记为已完成

 <!--DHIS2-SECTION-ID:mark_tracked_entity_instance_enrollment_complete-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **完成**。

4.  点击**是**
确认。

### 重新打开已完成的注册

 <!--DHIS2-SECTION-ID:reopen_complete_tracked_entity_instance_enrollment-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在里面**注册**小点，点击**打开**。

4.  点击**是**
确认。

### 显示TEI的注册历史

 <!--DHIS2-SECTION-ID:display_tracked_entity_instance_enrollment_history-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在**Profile**小元件中，点击**Audit history**图标。

### 创建TEI注册说明

 <!--DHIS2-SECTION-ID:create_tracked_entity_instance_enrollment_note-->

入学笔记对于记录有关原因的信息很有用
登记被取消。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在** Notes **小部件中，键入您的注释，然后单击** Add **。

## 发信息给TEI

 <!--DHIS2-SECTION-ID:send_message_to_tracked_entity_instance-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在 **Messaging** 小部件中并选择 **SMS** 或 **E-mail**。

4.  输入所需的联系信息。

    如果TEI的个人资料包含电子邮件地址或电话号码，
    这些字段会自动填写。

5.  键入一条消息。

6.  点击**发送**。

## 将TEI标记为后续

 <!--DHIS2-SECTION-ID:mark_tracked_entity_instance_for_follow_up-->

您可以使用标记 TEI 的注册进行跟进，然后使用此
当您创建 **Upcoming events** 和 **Overdue 时作为过滤器的状态
事件**报道。例如，这可以用于监控高风险
怀孕计划期间的病例。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **标记为跟进** 图标。

## 编辑TEI的个人资料

 <!--DHIS2-SECTION-ID:edit_tracked_entity_instance_profile-->

您在 **Profile** 中编辑 TEI 的配置文件或跟踪的实体属性
小部件。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在 **Profile** 小部件中，单击 **Edit**。

4.  修改配置文件并单击**保存**。

## 将关系添加到TEI

 <!--DHIS2-SECTION-ID:add_relationship_to_tracked_entity_instance-->

例如，您可以创建一个TEI与另一个TEI的关系。
将母亲和孩子联系在一起，或者将丈夫和妻子联系在一起。取决于
关于如何配置关系类型，亲戚可以继承
属性。

假设有两个程序：母亲的产前保健和
为孩子接种疫苗。如果是名字，姓氏和地址
这两个程序都需要属性，可以配置
姓氏和地址属性为可继承。然后在孩子
注册时，无需输入这些可继承属性。
您可以根据母亲的价值自动添加它们。如果你想
要为孩子使用不同的值，您可以覆盖
自动生成的值。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  在**关系** 小部件中，单击**添加**。

4.  选择一种关系类型。

5.  搜索亲戚并选择它。搜索遵循与从跟踪器首页搜索被跟踪实体实例时相同的模式。默认情况下，搜索覆盖用户的搜索范围。

6.  在弹出窗口中选择与搜索条件匹配的跟踪实体实例。

7.  点击**保存**。

>注意：如果该关系是双向关系，则该关系将在TEI中显示为该关系
>是在与该关系链接的TEI中和内部创建的。另外，如果关系是双向的，则
>关系将具有唯一名称，该名称将显示在“关系”列下的关系窗口小部件中。

## 共享TEI仪表板

 <!--DHIS2-SECTION-ID:share_tracked_entity_instance_dashboard-->

您可以通过其网址共享TEI仪表板。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开您要共享的仪表板。

3.  复制URL。

    确保URL包含“ tei”，“ program”和“ ou”
    （组织单位）参数。

4.  将网址粘贴到您选择的共享方法中，例如
    电子邮件或DHIS2中的消息。

    如果您在单击链接时未登录DHIS2，则将
    要求这样做，然后带到仪表板。

## 停用TEI

 <!--DHIS2-SECTION-ID:deactivate_tracked_entity_instance-->

如果禁用TEI，则TEI变为“只读”。关联数据
与TEI一起删除。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  点击右上角的
    ![](resources/images/tracker_capture/tc_tei_red_icon.png) button \>
    **停用**。

4.  单击**是**进行确认。

## 激活TEI

 <!--DHIS2-SECTION-ID:activate_tracked_entity_instance-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  点击右上角的
    ![](resources/images/tracker_capture/tc_tei_red_icon.png) button \>
    **启用**。

4.  单击**是**进行确认。

## 删除TEI

 <!--DHIS2-SECTION-ID:delete_tracked_entity_instance-->

> **警告**
>
>删除TEI时，将删除与TEI相关的所有数据。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  点击右上角的
    ![](resources/images/tracker_capture/tc_tei_red_icon.png) button \>
    **删除**。

4.  点击**是**
确认。

## 配置TEI仪表板

 <!--DHIS2-SECTION-ID:configure_tracked_entity_instance_dashboard-->

### 显示或隐藏小部件

 <!--DHIS2-SECTION-ID:tracked_entity_instance_dashboard_show_hide_widget-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置** 图标，然后选择**显示/隐藏小部件**。

4.  选择要显示或隐藏的小部件。

5.  点击**关闭**。

### 将仪表板的布局保存为默认布局

 <!--DHIS2-SECTION-ID:tracked_entity_instance_dashboard_save_layout-->

您可以将仪表板的布局保存为程序的默认设置。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置**图标，然后选择**将仪表板布局另存为
    默认**。

### 锁定仪表板的布局

如果您是**管理员**，则可以选择锁定
所有用户的仪表板布局。

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  将小部件组织成所需的布局并将其保存为默认布局
    （请参见上文）。

4.  单击 **Settings** 图标，然后选择 **Lock layout for all
    用户**。

用户仍然可以暂时重新组织小部件，但是
页面刷新后，版式将重置为管理员保存的版式。的
当仪表板布局为
锁定。

### 顶栏

顶部栏可能是一个有用的工具，可以快速，快速地查看重要数据
简单的方法。要开始使用顶部栏：

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置**图标，然后选择**顶栏设置**。

4.  点击**激活顶部栏**，然后点击您想要的数据
    显示在顶部栏中。

![](resources/images/tracker_capture/top_bar.png)

### 更改 **Timeline Data Entry** 小部件的表格显示模式

**时间线数据输入**小控件有5种不同的表格显示模式选择。不同的选项是：
- **默认格式**-垂直显示所有数据元素。

- **比较之前的表格**-在当前选定的程序阶段旁边显示prevoius（可重复）程序阶段。

- **全部比较表格**-在当前所选程序阶段旁边显示所有prevoius（可重复）程序阶段。

- **网格形式**-水平显示数据元素。

- ** POP表单**-与** Grid表单**相同，但是单击时，数据元素将显示在弹出窗口中。

要更改当前的显示模式，请单击小部件顶部栏中的第二个图标（请参见下图）：

![](resources/images/tracker_capture/compareForm.png)

一旦选择了一个选项，该选择将存储在该特殊程序阶段。这意味着您可以为程序中的不同程序阶段使用不同的表模式。

> **注意事项：**
> 1. *如果存在多个可重复事件（同一程序阶段），**比较表单** 选项将发挥最佳作用。*
> 2. *如果程序阶段的数据元素超过 10 个，则**网格形式**和**弹出式形式**选项不可选。*
> 3. *小部件栏中的图标将根据您选择的选项而变化。*

## 建立报告

 <!--DHIS2-SECTION-ID:create_report_tracker_capture-->

1.  打开 **Tracker Capture** （随访采集）应用程序。

2.  点击**报告**。

3.  选择报告类型。

    <table>
    <caption>Report types in the Tracker Capture app</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Report type</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Program summary</p></td>
    <td><p>A summary report for a particular program, organisation unit and time frame. The report consist of a list of TEIs and their records organised based on program stages.</p></td>
    </tr>
    <tr class="even">
    <td><p>Program statistics</p></td>
    <td><p>A statistics report for a particular program. The report provides for example an overview of drop-outs or completion rates in a given time frame at a particular organisation unit.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Upcoming events</p></td>
    <td><p>A tabular report showing tracked entity instances and their upcoming events for a selected program and time. You can sort the columns and search the values. Show/hide operations are possible on the columns. You can also export the table to Microsoft Excel.</p></td>
    </tr>
    <tr class="even">
    <td><p>Overdue events</p></td>
    <td><p>A list of events for a selected program. The report displays a list of TEIs and their events that are not completed on time. You can sort the columns and search the values You can also export the table to Microsoft Excel.</p></td>
    </tr>
    </tbody>
    </table>

![](resources/images/tracker_capture/program_summary_report.png)

摘要报告显示TEI的列表及其记录
“ MNCH / PNC（成年女性）”程序。记录以以下形式组织
选项卡，其中每个选项卡都是程序阶段。表中的列是
数据元素，配置为在报表中显示
程序阶段定义。
