---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-data-entry-app.md"
revision_date: "2021-06-14"
---

# 使用数据输入应用 { #data_entry_app }

## 关于数据输入应用 { #about_data_entry_app }

在**数据输入**应用程序中，您可以在DHIS2中手动输入汇总数据。您一次注册一个组织单位，一个期间和一组数据元素（数据集）的数据。数据集通常对应于基于纸张的数据收集工具。您可以在**维护**应用程序中配置数据集。

> **注意**
>
> 如果数据集同时具有分区表单和自定义表单，则系统在数据输入时显示自定义表单。输入数据的用户无法选择他们想要使用的表单。在基于 Web 的数据输入中，显示首选项的顺序为：
>
> 1. 自定义表单（如果存在）
>
> 2. 章节表格（如果有）
>
> 3.默认表单
>
> 移动设备不支持自定义表单。在基于移动设备的数据输入中，显示首选项的顺序是：
>
> 1. 章节表格（如果有）
>
> 2.默认表单

关闭组织机构时，您无法在**数据输入**应用程序中向该组织单位注册或编辑数据。

## 以数据输入形式输入数据 { #enter_data_in_data_entry_form }

![](resources/images/data_entry/data_entry_overview.png)

1.  打开**数据输入**应用。

2.  在左侧的组织单位树中，选择一个组织单位。

3.  选择一个**数据集**。

4.  选择一个**期间**。

    可用时段由数据集的时段类型（报告频率）控制。您可以单击**上一年**或**下一年**来后退一年。

    > **Note**
    >
    > Depending on how you've configured the data entry form, you might have to enter additional information before you can open the date entry form. This can for example be a project derived from a category combination.

5.  在数据输入表单中输入数据。

    -   绿色字段表示系统已保存该值。

    -   灰色字段表示该字段已禁用，您无法输入值。光标将自动跳转到下一个打开的字段。

    -   要移动到下一个字段，请按 Tab 键或向下箭头键。

    -   要返回到上一个字段，请按 Shift+Tab 或向上箭头键。

    -   如果您输入无效值，例如在仅接受数值的字段中输入字符，您将看到一个弹出窗口来解释问题，并且该字段将显示为黄色（未保存），直到您更正该值。

    -   如果您已为该字段定义了最小最大值范围，并且输入了超出此范围的值，您将收到一条弹出消息，指出该值超出范围。在您更改值或更新值范围然后重新输入值之前，该值将保持未保存状态。

6.  填写表单后，点击数据输入表单右上角或下方的**运行验证**。

    然后，针对新数据运行涉及当前数据输入表单（数据集）中的数据元素的所有验证规则。如果没有违反验证规则，您将看到一条消息：_数据输入屏幕已成功通过验证_。如果存在验证违规，它们将显示在列表中。

    ![](resources/images/dhis2UserManual/Validation_Rule_Result.png)

7.  （可选）更正验证冲突。

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros.

8.  改正错误并完成数据输入后，请点击**完成**。

    系统在生成区、县、省或国家级别的完整性报告时使用此信息。

## 将数据值标记为后续 { #mark_data_for_followup_in_data_entry_form }

![](resources/images/data_entry/data_entry_section_history.png)

例如，如果您有需要进一步调查的可疑值，则可以将其保留为系统，但将其标记为后续。然后，在 **数据质量** 应用中，您可以运行后续分析以查看和更正所有标记的值。

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  双击包含要标记为后续操作的值的字段。

4.  单击星号图标。

## 在完整的数据输入表单中编辑数据值 { #edit_data_value_in_completed_form }

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  点击**未完成**。

4.  更改相关数据值。

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros,

5.  点击**完成**。

## 显示数据值的历史记录 { #display_data_value_history }

![](resources/images/data_entry/data_entry_section_history.png)

您可以显示为一个字段注册的最后12个值。

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  双击包含要查看其历史记录的值的字段。

4.  点击**数据元素历史记录**。

## 显示数据值的审核记录 { #display_data_value_audit_trail }

![](resources/images/data_entry/data_entry_audit_trail.png)

审计跟踪允许您查看其他数据值
在当前值之前输入。审计跟踪还显示何时
数据值已更改以及进行更改的用户。

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  双击包含要查看其审核跟踪的值的字段。

4.  点击**审核记录**。

## 手动创建最小值最大值范围 { #change_min_max_range_manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  在**数据输入**应用中，打开一个数据输入表单。

2.  双击要设置最小最大值范围的字段。

3.  输入**最小限制**和**最大限制**。

4.  点击**保存**。 

    如果下次输入数据时值不在新值范围内，则数据输入单元格将以橙色背景显示。

5.  （可选）键入注释来解释差异的原因，例如可能产生大量客户的设施中的事件。

6.  （可选）点击**保存评论**。

> **提示**
>
>单击星号图标以标记该值以进行进一步跟踪。

## 离线输入数据 { #enter_data_offline }

即使您在数据输入过程中没有稳定的Internet连接，**数据输入**应用程序仍能正常工作。没有互联网连接时，输入的数据将保存到本地计算机。当Internet连接恢复时，该应用程序会将数据推送到服务器。由于不再从服务器为每个渲染检索数据输入表单，因此减少了总带宽使用量。

> **注意**
>
> 要使用此功能，您必须在有 Internet 连接时登录服务器。

-   当您连接到 Internet 时，应用程序会在数据输入表单的顶部显示以下消息：

    ![](resources/images/data_entry/data_entry_online1.png)

-   如果您的互联网连接在数据输入期间中断，应用程序会检测到并显示以下消息：

    ![](resources/images/data_entry/data_entry_offline1.png)

    现在您的数据将存储在本地。您可以继续照常输入数据。

-   输入所有必要的数据并且应用程序检测到互联网连接恢复后，您将看到以下消息：

    ![](resources/images/data_entry/data_entry_offline_upload.png)

    单击**上传**以与服务器同步数据。

-   当数据与服务器成功同步后，您将看到以下确认消息：

    ![](resources/images/data_entry/data_entry_offline_upload_success1.png)

## 启用多组织单位数据输入 { #data_entry_multiple_organisation_units }

![](resources/images/data_entry/data_entry_multiple_org_unit.png)

为多个组织单位输入数据可能很有用
相同的数据输入表单，例如，如果数据元素很少
形式和层次结构中的大量组织单位。在那里面
在这种情况下，您可以启用多组织单位数据输入。

> **注意**
>
>多组织单位数据输入仅适用于部分表格。

1.  打开**系统设置**应用。

2.  选择**启用多组织机构表格**。

3.  在**数据输入**应用中，选择要在组织单位层次结构中输入数据的组织单位正上方的组织单位。

    数据元素将在表单中显示为列，组织单元将显示为行。

    > **Note**
    >
    > The data entry forms should still be assigned to the facilities that you actually enter data for, that is the organisation units now appearing in the form.

## 也可以看看 { #data_entry_app_see_also }

-   [控制数据质量](https://docs.dhis2.org/master/en/user/html/control_data_quality.html)

-   [管理数据集和数据输入表单](https://docs.dhis2.org/master/en/user/html/manage_data_set.html)

-   [使用维护应用](https://docs.dhis2.org/master/en/user/html/maintenance_app.html)
