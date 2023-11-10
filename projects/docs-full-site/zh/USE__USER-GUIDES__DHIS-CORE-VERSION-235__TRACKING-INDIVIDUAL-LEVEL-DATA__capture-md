---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-the-capture-app.md"
revision_date: "2021-06-14"
---

# 使用捕获应用 { #capture_app }

## 关于Capture应用 { #about_capture_app }

Capture应用程序可替代Event Capture应用程序。将来，我们打算将Tracker Capture应用程序和Data Entry应用程序合并到Capture应用程序中。

在Capture应用程序中，您可以注册在特定时间和地点发生的事件。事件可以在任何给定的时间点发生。这与常规数据相反，常规数据可以按预定义的定期间隔进行捕获。事件有时称为案例或记录。在DHIS2中，事件链接到程序。通过捕获应用程序，您可以在输入事件信息之前选择组织单位和程序，并指定事件发生的日期。

## 实施者/管理员信息 { #implementer_info }

### 元数据缓存 { #metadata_caching }

出于性能原因，Capture应用程序在客户端浏览器中缓存元数据。在服务器上更新元数据时，需要将更改传播到已经缓存了元数据的客户端。根据更改，可以通过以下三种方式之一完成此操作：

1. 如果更改绑定到某个程序，则需要为该特定程序增加程序版本。例如，如果您更改程序或程序规则中的数据元素，则需要增加绑定程序的版本。

2. 如果更改未绑定到程序，则需要增加任何程序版本，以将更改传播到客户端。这里的示例是对常量，组织单位级别或组织单位组的更改。

3. 上面两个规则的例外是选项集。选项集具有自己的版本属性，即，增加选项集版本应确保将选项集元数据传播到客户端。

## 注册活动 { #capture_register_event }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

    您只能看到与所选组织部门关联的程序以及您有权访问的程序，并且这些程序通过数据级别共享与您的用户组共享。

4. 如果程序具有类别组合设置，则必须选择类别选项。

5. 点击**新建**。

    ![创建新事件](resources/images/capture_app/create_new_event.png)

6. 填写必填信息。如果将程序程序阶段配置为捕获位置：

    - 如果该字段是坐标字段，您可以直接输入坐标，也可以单击坐标字段左侧的 **地图** 图标。后者将打开一个地图，您可以在其中搜索位置或直接通过单击地图进行设置。

    - 如果该字段是多边形字段，您可以单击该字段左侧的 **地图** 图标。这将打开一个地图，您可以在其中搜索位置并捕获多边形（地图右上角的按钮）。

7. 如果需要，您可以通过单击表单底部的**写评论**按钮来添加评论。

8. 如果需要，您可以通过点击底部的**添加**按钮来添加关系形式。有关更多信息，请参见相关**添加关系**的部分。

9. 单击**保存并退出**或单击按钮旁边的箭头以选择**保存并添加另一个**。
    - **保存并添加另一个**将保存当前事件并清除表单。您捕获的所有事件将显示在页面底部的列表中。当您想要完成捕获事件时，如果表单为空，请单击“完成”按钮，或者如果您的表单包含数据，请单击“**保存并添加另一个**”旁边的箭头，然后选择“**保存并退出**”。

> 注 1：事件中的某些数据元素可能是强制性的（在数据元素标签旁边用红星标记）。这意味着在允许用户完成事件之前必须填写所有强制数据元素。例外情况是，如果用户具有名为 **“忽略跟踪器和事件捕获中必填字段的验证”的权限。** 如果用户具有此权限，则在保存之前将不需要填写必填数据元素并且数据元素标签旁边不会显示红色星号。请注意，拥有**“ALL”**权限的超级用户自动拥有此权限。

> 注2：数据输入表单也可以在**行视图**中显示。在此模式下，数据元素水平排列。这可以通过单击数据输入表单右上角的**切换到行视图**按钮来实现。如果您当前处于**行视图**，您可以通过单击数据输入表单右上角的**切换到表单视图**按钮切换到默认表单视图。

## 添加关系 { #capture_add_relationship }

Relationships can be added either during registration, editing or viewing of an event. Currently the **Capture App** only supports _Event to Tracked Entity Instance_ relationships.

1. 如果发生事件，请单击**添加关系**。

2. 选择您要创建的关系类型。

-   现在，您有两个选择：**链接到现有的跟踪实体实例**或**创建新的跟踪实体实例**。

![关系选项](resources/images/capture_app/relationship_options.png)

### 链接到现有的跟踪实体实例 { #link-to-an-existing-tracked-entity-instance }

3. Click **Link to an existing Tracked Entity Instance**.

-   现在应该会向您显示一些用于搜索 **跟踪实体实例** 的选项。您可以选择一个**程序**。如果选择了**程序**，则属性将从所选**程序**中派生。如果未选择**程序**，则只有属于**跟踪实体实例**的属性才会可见。

      ![搜索跟踪实体实例](resources/images/capture_app/search_tei.png)

    -   If the **Tracked Entity Instance** or **program** is configured with a unique attribute, this attribute can be used for finding a specific **Tracked Entity Instance** or **program**. This attribute should be presented alone. When the unique attribute field has been filled out, click the **Search** button located right below the unique attribute field.

    -   如果**跟踪实体Instance** 或 **program** 具有属性，这些属性可通过展开 **Search by attributes** 框用于搜索。填写完所有所需的属性字段后，单击位于底部的**按属性搜索** 按钮。您还可以通过设置**组织单位范围**来限制搜索。如果设置为 _All 可访问_，您将搜索 **跟踪实体您有权访问的所有组织单位中的实例**。如果您选择 _Selected_，系统会要求您选择要在哪些组织单位内进行搜索。

4. 成功搜索后，您将看到 ** 列表跟踪实体符合搜索条件的实例**。要创建关系，请单击 ** 上的 **Link** 按钮跟踪实体 您想与之建立关系的实例**。

-   如果你没有找到**追查实体您正在寻找的实例**，您可以点击**新搜索**或**编辑搜索**按钮。**新搜索**将带您进入新的空白搜索，而**编辑搜索**将带您返回到您只需执行的搜索，并保留搜索条件。

### 创建新的跟踪实体实例 { #create-new-tracked-entity-instance }

3. 点击**新建 追查实体 实例**。

-   您现在会看到一个 形式 用于注册新的**跟踪实体实例**。您可以选择注册或不注册程序。如果选择了一个程序，新的**跟踪实体实例**将被注册到所述程序中。您还可以通过删除自动设置的组织单位并选择新的组织单位来更改 **组织单位**。

    ![注册新的跟踪实体实例](resources/images/capture_app/register_tei.png)

4. 填写所需的（可能是必填的）属性和注册详细信息。

5. Click **Create Tracked Entity Instance and Link**.

> 注意：填写数据时，您可能会收到一条警告，告诉您已发现可能的重复项。您可以单击警告来查看这些重复项，如果重复项匹配，您可以选择通过单击 **链接** 按钮来链接该 **跟踪的实体实例**。如果填充数据后警告仍然存在，您将看不到 **创建跟踪实体实例和链接** 按钮。相反，您将看到一个名为**查看重复项**的按钮。当您单击此按钮时，将显示可能重复的列表。如果这些重复项中的任何一个与您尝试创建的 **跟踪实体实例** 匹配，您可以单击 **链接** 按钮，如果没有，您可以单击 **另存为新人** 按钮来注册新的 **跟踪的实体实例**。

## 编辑活动 { #capture_edit_event }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   注册到所选程序的所有事件均显示在列表中。

4. 单击您要修改的事件。

5. 点击**编辑事件**按钮。

6. 修改 事件 详细信息，然后单击**保存**。

## 删除活动 { #capture_delete_event }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   注册到所选程序的所有事件均显示在列表中。

4. 单击 **三点** 图标 事件 你想删除。

5. 在显示的菜单中点击**删除事件**。

    ![删除事件](resources/images/capture_app/delete_event.png)

## 修改事件列表布局 { #capture_modify_event_list_layout }

您可以选择在事件列表中显示或隐藏哪些列。这个可以
例如当您有很长的数据元素列表时很有用
分配到程序阶段。

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   注册到所选程序的所有事件均显示在列表中。

4. Click the **gear** icon on the top right of the event list.

5. Select the columns you want to display and click **Save**.

    ![修改事件列表](resources/images/capture_app/modify_event_list.png)

>注意：您可以通过将数据元素拖放到列表中来重新组织它们的顺序。

## 过滤事件列表 { #capture_filter_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   注册到所选程序的所有事件均显示在列表中。

    事件列表顶部是按钮，其名称与列表中的列标题相同。

4. 使用列表顶部的按钮可根据报告日期或特定数据元素进行过滤。

    ![过滤事件](resources/images/capture_app/filter_event.png)

>注意：数据元素的过滤方式略有不同。例如，** Number **数据元素将显示要过滤的范围，而** Text **数据元素将要求您输入搜索查询以进行过滤。

## 排序活动清单 { #capture_sort_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。注册到所选程序的所有事件都会显示在列表中。

4. 单击列标题之一，以按升序对该数据元素上的列表进行排序。

   列旁边会显示一个向上的小箭头，以表明列表是按升序排序的。

5. 再次单击列标题，以降序对该数据元素上的列表进行排序。

   该列旁边会显示一个小的向下箭头，以显示该列表以降序排列。

    ![排序事件](resources/images/capture_app/sort_event.png)

## 下载活动清单 { #capture_download_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。注册到所选程序的所有事件都会显示在列表中。

4. Click the **downward arrow** icon on the top right of the event list.

5. 选择您要下载的格式。

    ![下载活动列表](resources/images/capture_app/download_event_list.png)

>注意：您可以下载JSON，XML或CSV格式的事件列表。

## 预定义列表视图 { #capture_views }

您可以设置自己的视图并保存以供以后使用。这些视图也可以与其他人共享。视图由过滤器，列顺序和事件排序顺序组成。

### 保存新视图 { #capture_view_save }

1. 选择一个组织单位和一个程序。

2. 使用事件列表上方的过滤器按钮设置过滤器（在此处详细说明（#capture_filter_event_list））。

![](resources/images/capture_app/view_save_filters.png)

3. 通过单击齿轮图标来设置列顺序，然后在弹出窗口中根据您的偏好指定布局（如何修改布局在[此处]（＃capture_modify_event_list_layout）详细说明）。

![](resources/images/capture_app/view_save_column_order.png)

4. 通过单击列标题之一对事件进行排序（在[此处]（＃capture_sort_event_list）详细说明）。

![](resources/images/capture_app/view_save_sort_order.png)

5. 打开右侧的更多菜单（三个点图标），然后选择“保存当前视图...”

![](resources/images/capture_app/view_save_menu.png)

6. 填写视图的名称，然后单击“保存”。

![](resources/images/capture_app/view_save_name.png)

### 加载视图 { #capture_view_load }

1. 选择具有预定义视图的组织单位和程序。

2. 这些视图应在事件列表本身上方。单击一个视图以加载它。

![](resources/images/capture_app/view_load_unselected.png)

3. 加载视图的示例。

![](resources/images/capture_app/view_load_selected.png)

### 更新视图 { #capture_view_update }

1. 加载您要更新的视图（请参见[加载视图]（＃capture_view_load））。

2. 对过滤器，列顺序和/或事件排序顺序进行更改。

> **注意**
>
> 当视图有未保存的更改时，星号 (\*) 会附加到视图名称中。

3. 打开右侧的更多菜单（三个点图标），然后选择“更新视图”。

![](resources/images/capture_app/view_update.png)

### 分享观点 { #capture_view_share }

1. 加载您要共享的视图（请参见[加载视图]（＃capture_view_load））。

2. 打开右侧的更多菜单（三个点图标），然后选择“共享视图...”

![](resources/images/capture_app/view_share.png)

3. 进行更改。通常，您将添加用户/组（1）和/或更改先前添加的用户/组的访问权限（2）。

![](resources/images/capture_app/view_share_access.png)

### 删除视图 { #capture_view_delete }

1. 加载您要删除的视图（请参见[加载视图]（＃capture_view_load））。

2. 打开右侧的更多菜单（三个点图标），然后选择“删除视图”。

![](resources/images/capture_app/view_delete.png)

## 用户分配 { #capture_user_assignment }

可以将事件分配给用户。必须为每个程序启用此功能。

### 分配新事件 { #capture_user_assignment_new }

1. 选择启用了用户分配的组织单位和程序。

2. Click **New Event** in the upper right corner.

3. 您会在数据输入页面底部附近找到受让人部分。搜索并选择要将事件分配给的用户。保存事件时将保留受让人。

    ![](resources/images/capture_app/user_assignment_new.png)

    ![](resources/images/capture_app/user_assignment_new_filled.png)

### 变更受让人 { #capture_user_assignment_edit }

1. 选择启用了用户分配的组织单位和程序。

2. 单击列表中的事件

3. 在右列中，您将找到“受让人”部分。

    ![](resources/images/capture_app/user_assignment_edit.png)

4. Click the edit button, or the **Assign** button if the event is not currently assigned to anyone.

    ![](resources/images/capture_app/user_assignment_edit_button.png)

    ![](resources/images/capture_app/user_assignment_edit_add.png)

5. 搜索并选择要将事件重新分配给的用户。作业将立即保存。

### 事件列表中的受让人 { #capture_user_assignment_event_list }

在事件列表中，您将可以查看每个事件的受让人。此外，您可以由受让人对列表进行排序和过滤。

#### 按受让人过滤 { #filter-by-assignee }

1. 单击**分配给**过滤器。

    ![](resources/images/capture_app/user_assignment_event_list.png)

2. 选择您的首选受理人筛选器，然后单击“更新”。

    ![](resources/images/capture_app/user_assignment_event_list_options.png)

## 追踪程式 { #capture_tracker_programs }

Capture应用程序尚不支持跟踪程序，但是仍列出了跟踪程序。如果您选择一个跟踪程序，该应用程序将引导您进入“跟踪器捕获”应用程序，如下所示。

![](resources/images/capture_app/tracker_program.png)
