---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/scheduling.md"
revision_date: "2021-06-14"
---

# 排程 { #scheduling }

计划程序是用于管理DHIS2中的后台作业的应用程序。
后台作业可以执行许多任务，例如运行分析，
同步数据和元数据，或发送推送分析报告。的
应用程序提供了创建，修改和删除此类作业的功能。

调度程序与DHIS2捆绑在一起，可以通过应用程序进行访问
菜单。

![](resources/images/scheduler/overview.png)

Scheduler 应用程序的起始页显示现有作业的概述。默认情况下，预定义的系统作业是隐藏的。要查看这些，请切换右上角的_显示系统作业_。

创建或修改作业时，将根据以下日期重新安排作业
选择的首选项。要按需运行作业，请按绿色三角形
标记为“立即运行”。此操作仅适用于已启用的作业。

## 创造工作 { #scheduling_create_job }

1.  打开** Scheduler **应用程序，然后单击右下角的添加按钮。

2.  Choose a suitable **Name** for the new job.

3.  选择作业的运行频率，即作业应在何时以及多久运行一次。

    1.  您可以从下拉菜单中选择预定义的频率，或者

    2.  如果您想要特定的计划，您可以使用 [Spring 计划](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/scheduling/support/CronSequenceGenerator.html) 语法为作业指定一个自定义 **Cron 表达式**。
    3.  Enabling the **Continuous execution** option will make the job run constantly. In other words, as soon as the job finishes, it will be scheduled to run again right away. Selecting this option will disable the other fields.

4.  Select the **Job type** you want to schedule using the drop-down menu.

5.  If the job type is customizable, a **Parameters** section will appear below. These additional options specify the details of the scheduled job, and will vary greatly depending on the job type.

6.  Press the **Add job** button to confirm the job creation. The newly created job should now be listed in the job overview, given that the **Show system jobs** setting is not enabled.

![](resources/images/scheduler/add_new_job.png)

默认情况下启用作业。

## 配置工作 { #scheduling_configure_job }

拥有适当的权限，您可以修改用户创建的详细信息
职位。请注意，对于系统作业，只有计划（cron表达式）可以
被改变。

To quickly enable or disable a user created job from running, use the **Enabled** column on the landing page of the Scheduler app. System jobs are always enabled.

进一步配置作业：

1.  Select a job from the landing page to unveil the **Attributes** and change them to accordingly. See the previous section for scheduling details.

2.  If the job type supports extra options, the **Parameters** section will also be available.

3.  When done, press the **Save changes** button to persist the changes.

## 删除工作 { #dataAdmin_scheduler_delete }

1.  选择要删除的作业。

2.  Press the **Delete** button in the bottom right corner.

3.  在弹出窗口中再次按** Delete **进行确认。

![](resources/images/scheduler/delete_job.png)

## 工作类型 { #job-types }

以下部分描述了各种作业类型。

### 资源表 { #scheduling_resource_table }

资源表作业负责生成和更新资源数据库表。这些表由DHIS 2中的各个组件使用，旨在简化针对数据库的查询。

请注意，当指定任何分析表作业时，资源表可以是该过程的一部分，并且也不必指定资源表作业。

### 分析表 { #scheduling_analytics_table }

分析表作业负责生成和更新分析表。分析表用作DHIS2中数据分析查询的基础。仪表板，可视化工具和地图等应用程序通过DHIS2分析API从这些表中检索数据，并且必须对其进行更新才能使分析数据可用。您可以安排此过程通过分析表作业类型定期运行。

默认情况下，分析表作业将填充所有年份和数据元素的数据。可以使用以下参数：

-   **过去几年：**为其填充分析表的最后几年的数量。例如，如果您指定2年，则该过程将更新最近两年的数据，而不更新较旧的数据。此参数对减少过程完成所需的时间很有用，并且如果旧数据没有更改，并且需要更新最新数据，则该参数非常适用。
-   **跳过资源表：**在分析表更新过程中跳过资源表。这减少了过程完成所需的时间，但导致元数据的更改未反映在分析数据中。
-   **跳过表类型：**跳过一种或多种分析表类型。这减少了过程完成所需的时间，但导致这些数据类型未在分析数据中更新。

### 连续分析表 { #scheduling_continuous_analytics_table }

分析表作业负责生成和更新分析表。分析表用作DHIS2中数据分析查询的基础。仪表板，可视化工具和地图等应用程序通过DHIS2分析API从这些表中检索数据，并且必须对其进行更新才能使分析数据可用。您可以安排此过程通过分析表作业类型定期运行。

连续分析表作业基于两个阶段：

-   _最新更新：_最新数据的更新，其中最新是指自上次更新最新数据或完整数据以来已添加，更新或删除的数据。此过程将经常发生。
-   _完整更新：_多年来所有数据的更新。此过程每天进行一次。

连续分析表作业将经常更新最新数据。最新数据处理使用特殊的数据库分区，该分区仅用于保存最新数据。由于数据量相对较少，因此可以快速刷新此分区。分区的大小将增加，直到执行完全更新。每天一次，将更新所有年份的所有数据。这将清除最新的分区。

默认情况下，分析表作业将填充所有年份和数据元素的数据。可以使用以下参数：

-   **一天中的完整更新时间：**一天中的完整更新将在这一小时完成。例如，如果您指定1，则将在凌晨1点执行完整更新。
-   **过去几年：**为其填充分析表的最后几年的数量。例如，如果您指定2年，则该过程将更新最近两年的数据，而不更新较旧的数据。此参数对减少过程完成所需的时间很有用，并且如果旧数据没有更改，并且需要更新最新数据，则该参数非常适用。
-   **跳过资源表：**在分析表更新过程中跳过资源表。这减少了过程完成所需的时间，但导致元数据的更改未反映在分析数据中。

### 数据同步 { #scheduling_data_sync }

DHIS2 提供远程分布式实例与 DHIS2 中央实例之间的数据同步。这可能很有用，例如当您部署了多个独立的 DHIS2 实例时，需要将数据值提交到中央 DHIS2 实例。支持跟踪器数据和聚合数据同步。

这些是启用数据同步的步骤：

-   进入同步设置，输入远程服务器 URL、用户名和密码。按TAB键自动保存新密码。刷新页面并检查填充的值是否仍然存在。请注意，刷新后密码字段将为空，因为该值已加密，因此您可以认为它已保存。

-   使用调度程序应用程序，使用“事件程序数据同步”和/或“跟踪程序数据同步”作业类型创建新作业。完成后请确保它已启用。 （注：如果以前版本中可用的“程序数据同步”作业之前在 Scheduler 应用程序中设置过，则它会自动被两个新作业“Event Programs Data Sync”和“Tracker Programs Data Sync”替换，具有相同的功能）设置。 ）

数据同步功能的某些方面需要注意：

-   本地 DHIS2 实例会将远程实例上的用户帐户密码加密存储在本地数据库中。远程帐户用于传输数据时进行身份验证。出于安全目的，请确保将 _hibernate.properties_ 中的 _encryption.password_ 配置参数设置为强密码。

-   强烈建议在 SSL/HTTPS 上部署远程服务器，因为用户名和密码是使用基本身份验证以明文形式发送的，可能会被攻击者拦截。

-   数据同步使用数据元素、类别选项组合和组织单元的UID属性来匹配元数据。因此，同步取决于这三个元数据对象在本地和远程实例上的协调，以便正常工作。

-   DHIS2 第一次运行同步作业时，它将包含所有可用数据。后续同步作业将仅包含自上次成功作业以来添加和更改的数据。仅当所有数据成功保存在远程服务器上时，同步作业才被视为成功（任何成功同步的数据都将保留在接收实例上，无论作业最终是否失败）。作业是否成功可以根据中央服务器返回的导入摘要来判断。

-   初始同步作业可能需要大量时间，可能会减慢实例速度，具体取决于同步的数据量。将作业配置为在在线用户较少时运行可能是一个好主意，然后将其更改为您自己的偏好。如果您不想或不需要同步所有数据，可以<a href="#skip_changed_before">跳过部分正在同步的数据</a>。

    当DHIS2同步跟踪器数据时，它根据上次同步的时间确定要同步的数据集。每个跟踪的实体实例和事件都有自己的上次成功同步时间的记录。

-   系统将根据作业配置中设置的规则启动同步作业。如果同步作业在没有连接到远程服务器的情况下启动，则在中止之前最多会重试 3 次。该作业将在预定时间再次运行。

-   服务器单独处理每组节目，即一组节目可以同步成功，而另一组则同步失败。其中一个的失败或成功不会影响另一个，因为如前所述，每个项目的上次成功同步时间都是单独跟踪的。

-   如果 TrackedEntityInstances (TrackedEntityAttribute) 的属性和 ProgramStages (ProgramStageDataElement) 的“跳过同步”选项打开，则不会同步。此功能允许您决定不同步某些敏感或不相关的数据，而仅将它们保留在本地。

-   The authority `Ignore validation of required fields in Tracker and Event Capture` (`F\_IGNORE\_TRACKER\_REQUIRED\_VALUE\_VALIDATION`) should be used when there is a requirement that some mandatory attribute / data element has at the same time a "Skip synchronization" property turned on. Such a setting will lead to validation failure on the central server as the given attribute / data element will not be present in the payload.

    对于具有此权限的用户，验证不会失败。应将权限分配给中央服务器上将用于同步作业的用户。

-   在特定情况下，**所有数据的初始同步可能是不可取的**；例如，当本地实例上的数据库是中央实例上存在的数据库的新副本时，或者当优选不同步旧数据以有利于花费更少时间的初始同步时。

    The _syncSkipSyncForDataChangedBefore_ SettingKey can be used to skip the synchronisation of all the data (data values, Event and Tracker program data, complete data set registrations) that were _last changed before the specified date_. The `SettingKey` is used in the synchronization job all the time. Therefore, if you need to synchronize the old data, you should change the `SettingKey`.

-   Tracker Programs 和 Event Programs 同步作业都支持分页，以避免超时并应对不稳定的网络。 “事件程序数据同步”作业的默认页面大小设置为 60。“跟踪程序数据同步”作业的默认页面大小设置为 20。

    如果默认值不符合您的目的，可以通过调度程序应用程序中特定同步作业的参数指定自己的页面大小。

### 元数据同步调度 { #scheduling_metadata_sync }

DHIS2提供了用于同步远程元数据的功能
实例到DHIS2的本地实例。当您有
部署了DHIS2的多个独立实例，您需要创建
所有本地实例中的元数据都类似于中央DHIS2
实例。

这些是启用元数据同步的步骤：

-   进入设置\>同步，输入远程服务器 URL、用户名和密码，然后单击保存。

-   转至元数据管理 \> 计划。在“元数据同步设置策略”为“已启用”下，选择时间段并单击“开始”。

元数据同步功能的某些方面需要注意：

-   本地 DHIS2 实例会将远程实例的用户帐户密码存储在其数据库中。远程用户帐户用于传输/下载数据时进行身份验证。出于安全目的，请确保将 _hibernate.properties_ 中的 _encryption.password_ 配置参数设置为强密码。

-   强烈建议在 SSL/HTTPS 上部署远程服务器，因为用户名和密码是使用基本身份验证以明文形式发送的，可能会被攻击者拦截。

-   还要确保远程用户没有 ALL 权限，而是简单地创建一个具有 F_METADATA_MANAGE 权限的用户，这样即使这些详细信息被黑客截获，也无法完全控制远程系统。

-   元数据同步依赖于底层导入层。每个元数据版本都是两个给定时间戳之间元数据的导出。每次同步元数据版本都是尝试将该元数据快照导入本地实例。版本的同步是增量的。本地实例将尝试逐个从中央实例下载元数据版本。未能同步特定元数据版本将不会让同步继续到其他版本。如果发生故障，必须对中央元数据进行适当的更改，以确保错误得到解决。元数据配置至关重要，用户在向生产环境推出更新时应小心。始终建议建立临时环境，以确保元数据版本的健全性及其之后的影响。本地实例将同步第一个版本的元数据，以便保持和谐并且本地和中央实例能够正常工作。

-   系统将在预定时间尝试同步。如果本地或远程服务器当时没有可用的 Internet 连接，则同步将中止并在按照 _dhis.conf_ 文件中提到的重试计数后重新尝试。

-   您可以在“上次成功”标签旁边的计划屏幕中看到上次与远程服务器成功同步的时间。
