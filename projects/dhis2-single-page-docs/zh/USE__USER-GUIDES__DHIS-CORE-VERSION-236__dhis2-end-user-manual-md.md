---
revision_date: "2022-02-08"
template: single.html
---

# 什么是DHIS2？ { #what_is_dhis2 }

阅读本章后，您将能够理解：

-   DHIS2 是什么以及它在卫生信息系统 (HIS) 方面的用途是什么？

-   部署 DHIS2 时主要的技术考虑是什么，以及使用新模块扩展 DHIS2 的选项有哪些？

-   基于患者的数据和汇总数据有什么区别？

-   将免费和开源软件 (FOSS) 用于 HIS 有哪些好处和挑战？

## DHIS2背景 { #mod1_1 }

DHIS2 是一个用于收集、验证、分析和展示的工具
汇总和基于患者的统计数据，量身定制（但不是
限于）综合健康信息管理活动。它是一个
通用工具而不是预配置的数据库应用程序，具有
开放的元数据模型和灵活的用户界面，允许用户
无需设计特定信息系统的内容
用于编程。 DHIS2 是一个模块化的基于 Web 的软件包
使用免费和开源的 Java 框架。

DHIS2 是在 BSD 许可下发布的开源软件，可以
免费获得。它可以在任何带有 Java 运行时的平台上运行
已安装环境（JRE 7 或更高版本）。

DHIS2 由健康信息系统计划 (HISP) 开发为
一个开放的全球分布式流程，开发人员目前
印度、越南、坦桑尼亚、爱尔兰和挪威。发展是
由奥斯陆大学协调，并得到 NORAD 和其他机构的支持
捐助者。

DHIS2 软件在非洲、亚洲、
和拉丁美洲，以及采用 DHIS2 作为其
全国范围的 HIS 软件包括肯尼亚、坦桑尼亚、乌干达、卢旺达、加纳、
利比里亚和孟加拉国。越来越多的国家和地区
组织正在开始新的部署。

随附的文档将尝试提供
应用程序的全面概述。鉴于抽象的性质
应用程序，本手册不会作为一个完整的逐步
在每种情况下如何使用应用程序的指南，但是
相反，将寻求提供 DHIS2 如何可以的插图和示例
通过通用示例在各种情况下实现。

在新环境中实施 DHIS2 之前，我们强烈建议阅读
DHIS2 实施指南（与本手册分开的手册），也
可在主 DHIS2 [网站](http://dhis2.org/documentation/) 获得。

## DHIS2的主要功能和目的 { #key-features-and-purpose-of-dhis2 }

DHIS2的主要功能和目的可归纳如下：

-   提供基于数据仓库原理和模块化结构的综合数据管理解决方案，可轻松针对管理信息系统的不同需求进行定制，支持组织层级不同层次的分析。

-   通过用户界面进行定制和本地适配。在新环境（国家、地区、地区等）中开始使用 DHIS2 无需编程。

-   提供数据输入工具，可以是标准列表或表格的形式，也可以定制为复制纸质表格。

-   为数据验证和提高数据质量提供不同类型的工具。

-   使用数据收集工具的设计，为选定的指标或摘要报告提供易于使用的一键式报告和图表。允许与流行的外部报告设计工具（例如 JasperReports）集成以添加更多自定义或高级报告。

-   分析模块（即 GIS、数据透视表、数据可视化器、事件报告等）中的灵活和动态（即时）数据分析。

-   一个用户特定的仪表板，用于快速访问相关的监控和评估工具，包括指标图表和指向最喜欢的报告、地图和系统中其他关键资源的链接。

-   易于使用的元数据管理用户界面，例如用于添加/编辑数据集或卫生设施。无需编程即可在新环境中设置系统。

-   设计和修改计算指标公式的功能。

-   用于密码、安全性和细粒度访问控制（用户角色）的用户管理模块。

-   可以向系统用户发送消息以获取反馈和通知。消息也可以发送到电子邮件和 SMS。

-   用户可以使用 Interpretations 在图表和报告中共享和讨论他们的数据，从而建立一个活跃的信息驱动的用户社区。

-   数据和元数据的导出导入功能，支持离线安装的同步以及与其他应用程序的互操作性。

-   使用 DHIS2 Web-API，允许与外部软件集成并通过使用自定义应用程序扩展核心平台。

-   可以根据用户需要开发和集成更多模块，或者作为 DHIS2 门户用户界面的一部分，或者作为通过 DHIS2 Web-API 交互的更松散耦合的外部应用程序。

综上所述，DHIS2 为
任何健康信息用户的报告和分析需求
等级。

## DHIS2在HIS中的使用：数据收集，处理，解释和分析。 { #use-of-dhis2-in-his-data-collection-processing-interpretation-and-analysis }

HIS 的更广泛背景可以通过
信息循环如下图 1.1 所示。信息循环
以图形方式描绘了不同的组件、阶段和过程
通过它收集数据、检查质量、处理、
分析和使用。

![The health information
cycle](resources/images/dhis2UserManual/dhis2_information_cycle.png)

DHIS2支持信息周期的不同方面，包括：

-   收集数据。

-   运行质量检查。

-   多个级别的数据访问。

-   正在报告。

-   制作图形和地图以及其他形式的分析。

-   实现跨时间（例如，前几个月）和空间（例如，跨设施和区域）的比较。

-   查看趋势（以时间序列显示数据以查看其最低和最高水平）。

作为第一步，DHIS2 用作数据收集、记录和
编译工具，所有数据（无论是数字还是文本形式）都可以
进入了它。数据输入可以在数据元素列表中完成，也可以在
定制的用户定义表格，可以开发成模仿纸张
以简化数据输入过程。

下一步，DHIS2 可用于提高数据质量。首先，在
数据输入点，可以检查数据是否在
任何特定的最小值和最大值的可接受范围水平
数据元素。例如，这种检查可以帮助识别打字
数据输入时的错误。此外，用户可以定义各种
验证规则，DHIS2可以通过验证运行数据
识别违规行为的规则。这些类型的检查有助于确保
输入系统的数据从一开始就是高质量的，并且可以
由最熟悉它的人改进。

输入并验证数据后，DHIS2 可以帮助
不同类型的报告。第一种是例行报告，
可以预定义，以便所有需要例行的报告
单击按钮即可生成。此外，DHIS2 可以帮助
通过比较例如生成分析报告
跨设施或随时间变化的指标。图表、地图、报告和
健康档案是 DHIS2 可以产生的输出之一，这些
应由卫生部门定期生成、分析和处理
经理。

## 技术背景 { #technical-background }

### DHIS2作为平台 { #dhis2-as-a-platform }

可以将 DHIS2 视为多个级别的平台。首先，
应用程序数据库的设计充分考虑了灵活性。
数据结构，例如数据元素、组织单元、表单和
用户角色可以通过应用程序用户完全自由定义
界面。这使得系统可以适应
大量的语言环境和用例。我们已经看到 DHIS2
支持常规数据捕获和分析的大多数主要要求
在国家实施中出现。它还使 DHIS2 成为可能
作为物流、实验室等领域的管理系统
金融。

其次，由于DHIS2的模块化设计，它可以扩展
附加软件模块或通过自定义应用程序。这些软件
模块/应用程序可以与 DHIS2 的核心模块并存
可以集成到 DHIS2 门户和菜单系统中。这是一个
强大的功能，因为它可以通过额外的方式扩展系统
需要时的功能，通常用于特定国家/地区的要求
如前所述。

软件模块可扩展性的缺点是它把
开发过程中的几个限制。开发人员创造
额外的功能仅限于 DHIS2 技术
编程语言和软件框架，除了
DHIS2 门户解决方案对模块设计的限制。
此外，这些模块必须包含在 DHIS2 软件中，当
软件是在网络服务器上构建和部署的，而不是动态的
运行。

为了克服这些限制并实现更松散的耦合
在 DHIS2 服务层和附加软件制品之间，一个
基于 REST 的 API 已作为 DHIS2 的一部分开发。这个 Web API
符合REST架构风格的规则。这意味着
那：

-   Web API 为完整的 DHIS2 数据模型提供了一个可导航和机器可读的接口。例如，可以访问数据元素的完整列表，然后使用提供的 URL 导航到感兴趣的特定数据元素，然后使用提供的 URL 导航到数据元素所属的数据集列表。

-   （元）数据通过使用普通 HTTP 请求的统一接口 (URL) 访问。没有花哨的传输格式或协议——只有经过充分测试、易于理解的 HTTP 协议，它是当今 Web 的主要构建块。这意味着第三方开发人员可以使用 DHIS2 数据模型和数据开发软件，而无需了解 DHIS2 2 特定技术或遵守 DHIS2 设计约束。

-   所有数据，包括元数据、报告、地图和图表，在 REST 术语中称为资源，都可以以当今 Web 的大多数流行表示格式进行检索，例如 XML、JSON、PDF 和 PNG。这些格式在应用程序和编程语言中得到广泛支持，并为第三方开发人员提供了广泛的实施选项。

### 了解平台独立性 { #understanding-platform-independence }

所有计算机都有一个操作系统 (OS) 来管理它和
运行它的程序。操作系统作为中间层
软件应用程序（如 DHIS2）和硬件（如
作为 CPU 和 RAM。 DHIS2 运行在 Java 虚拟机上，并且可以
因此可以在任何支持 Java 的操作系统上运行。平台
独立性意味着软件应用程序可以在任何操作系统上运行 -
Windows、Linux、Macintosh 等。 DHIS2 是独立于平台的，因此
可以在许多不同的上下文中使用，具体取决于确切的
要使用的操作系统的要求。

此外，DHIS2 支持三大数据库管理系统
系统 (DBMS)。 DHIS2 使用 Hibernate 数据库抽象框架
并与以下数据库系统兼容：PostgreSQL、MySQL
和 H2。 PostgreSQL 和 MySQL 是高质量的生产就绪
数据库，而 H2 是用于小规模的有用的内存数据库
应用程序或开发活动。

最后，也许是最重要的，因为 DHIS2 是一个基于浏览器的
应用程序，与系统交互的唯一真正要求是
使用网络浏览器。 DHIS2 支持大多数网络浏览器，尽管目前
推荐使用 Google Chrome、Mozilla Firefox 或 Opera。

### 部署策略-在线与离线 { #deployment-strategies-online-vs-offline }

DHIS2 是一个支持网络的应用程序，可以通过
Internet、本地 Intranet 以及本地安装的系统。这
DHIS2 的部署替代方案在本章中定义为 i)
离线部署 ii) 在线部署和 iii) 混合部署。这
以下部分将讨论含义和差异。

#### 离线部署 { #offline-deployment }

离线部署意味着多个独立的离线
实例是为最终用户安装的，通常是在地区级别。
该系统主要由最终用户/地区卫生部门维护
输入数据并从运行的系统生成报告的官员
他们的本地服务器。该系统通常也将由一个
国家超级用户团队定期访问该地区
部署。数据由最终用户在层次结构中向上移动
生成通过电子邮件或电子方式发送的数据交换文件
身体上通过邮件或个人旅行。 （注意简短的 Internet
发送电子邮件所需的连接不符合被
定义为在线）。这种部署方式有明显的好处
当适当的 Internet 连接不可用时，它可以工作。
另一方面，这种风格存在重大挑战，
将在下一节中描述。

-   **硬件：**运行独立系统需要在服务器和可靠电源方面安装先进的硬件，通常在全国各地的地区级别。这需要适当的采购资金和长期维护计划。

-   **软件平台：** 本地安装意味着需要大量维护。根据经验，最大的挑战是病毒和其他恶意软件，从长远来看，它们往往会感染本地安装。主要原因是最终用户使用记忆棒在私人计算机、其他工作站和运行应用程序的系统之间传输数据交换文件和文档。在离线环境中使防病毒软件和操作系统补丁保持最新是具有挑战性的，并且最终用户经常采用安全方面的不良做法。解决此问题的首选方法是为不允许使用记忆棒的应用程序运行专用服务器，并使用基于 Linux 的操作系统，该操作系统不像 MS Windows 那样容易感染病毒。

-   **软件应用程序：** 能够向用户分发健康信息软件的新功能和错误修复对于系统的维护和改进至关重要。依靠最终用户执行软件升级需要广泛的培训和高水平的能力，因为升级软件应用程序可能是一项技术上具有挑战性的任务。依靠国家级的超级用户团队来维护软件意味着很多旅行。

-   **数据库维护：**高效系统的先决条件是所有用户都使用标准化的元数据集（数据元素、表单等）输入数据。与前面关于软件升级的观点一样，如果以电子方式发送更新或组织良好的超级用户团队，则将元数据集的更改分发到大量离线安装需要最终用户的能力。未能保持元数据集同步将导致失去从地区移动数据的能力和/或不一致的国家数据库，因为例如在地区级别输入的数据将与国家级别的数据不兼容。

#### 在线部署 { #online-deployment }

在线部署意味着应用程序的单个实例设置在连接到 Internet 的服务器上。所有用户（客户）使用网络浏览器通过互联网连接到在线中央服务器。由于全球（移动）互联网覆盖范围的增加，以及随时可用且廉价的云计算资源，这种部署方式越来越可能。这些发展使得使用移动互联网调制解调器（也称为_dongles_）甚至可以在最偏远的农村地区访问在线服务器成为可能。

这种在线部署方式对
实施过程和应用程序维护相比
传统的离线独立风格：

-   **硬件：** 最终用户方面的硬件要求仅限于相当现代的计算机/笔记本电脑和通过固定线路或移动调制解调器的 Internet 连接。无需为每个用户配备专门的服务器，任何支持 Internet 的计算机就足够了。在线部署需要一台服务器，但由于只有一台（或多台）服务器需要采购和维护，这比在不同位置维护许多单独的服务器要简单得多（也更便宜）。鉴于云计算资源的价格持续稳步下降，同时计算能力不断提高，在云中建立强大的服务器比采购硬件便宜得多。

-   **软件平台：**最终用户只需要一个网络浏览器即可连接到在线服务器。当今所有流行的操作系统都附带 Web 浏览器，并且对什么类型或版本没有特殊要求。这意味着，如果发生病毒感染或软件损坏等严重问题，您可以随时重新格式化和安装计算机操作系统或获取新的计算机/笔记本电脑。用户可以继续输入数据，不会丢失任何数据。

-   **软件应用程序：**中央服务器部署方式意味着应用程序可以以集中的方式升级和维护。当发布具有新功能和错误修复的应用程序的新版本时，可以将其部署到单个在线服务器。下次最终用户通过 Internet 连接时，所有更改都将反映在客户端。这显然对改进系统的过程产生了巨大的积极影响，因为新功能可以立即分发给用户，所有用户将访问相同的应用程序版本，并且可以即时整理和部署错误和问题。

-   **数据库维护：**与上一点类似，元数据的更改可以集中在在线服务器上进行，并在下次连接到服务器时自动传播到所有客户端。这有效地消除了与维护与传统离线部署方式相关的升级和标准化元数据集相关的大量问题。例如，在初始数据库开发阶段和年度数据库修订过程中非常方便，因为即使经常发生更改，最终用户也将访问一致且标准化的数据库。

在 Internet 连接的情况下，此方法可能会出现问题
在很长一段时间内不稳定或丢失。然而 DHIS2 有
某些需要 Internet 连接才能使用的功能
只有系统正常工作的一部分时间，例如离线
数据输入。然而，一般来说，DHIS2 确实需要互联网连接
某种意义上，但这也越来越容易解决，即使在
偏远地区。

#### 混合部署 { #hybrid-deployment }

从到目前为止的讨论中，人们意识到在线部署
风格优于离线风格，但需要体面的互联网
将使用的连接。重要的是要注意，
提到的样式可以在共同部署中共存。它是完美的
可以在一个单一的范围内进行在线和离线部署
国家。一般规则是地区和设施应
在互联网足够的情况下通过互联网访问系统
存在连通性，离线系统应部署到地区
情况并非如此。

准确定义合适的互联网连接很难，但作为一个规则
拇指下载速度应至少为 10 KB/秒
客户端和至少 1 Mbit/sec（专用）带宽用于服务器。

在这方面，可以连接到移动互联网调制解调器
电脑或笔记本电脑和访问移动网络是一个非常有能力的
和可行的解决方案。移动互联网覆盖快速增长
在世界各地，通常以低廉的价格提供出色的连接
并且是本地网络和维护不善的固定网络的绝佳替代品
互联网线路。与全国移动网络取得联系
关于后付费订阅和潜在大订单的公司
好处是值得的。每个网络覆盖
应调查相关国家的网络运营商
决定选择哪种部署方法，因为它可能不同，并且
覆盖全国不同地区。

#### 服务器托管 { #server-hosting }

在线部署方法提出了在何处以及如何部署的问题
托管将运行 DHIS2 应用程序的服务器。通常有
有几个选项：

1.  卫生部内部托管

2.  在政府数据中心内托管

3.  通过外部托管公司托管

选择第一个选项的主要原因往往是政治性的
拥有数据库“物理所有权”的动机。这是
为了“拥有”和控制数据，许多人认为这很重要。
还希望为服务器管理建立本地能力
与项目的可持续性有关。这通常是捐助者驱动的
倡议，因为它被视为一项具体而有益的使命。

关于第二种方案，有些地方是政府数据中心
旨在促进和改善使用和
公共数据的可访问性。另一个原因是扩散
内部服务器环境对资源的要求很高，而且更多
有效地建立集中的基础设施和能力。

关于外部托管，最近有一种转向外包的趋势
对外部计算机资源的操作和管理
提供者，这些资源通常通过网络访问
称为“云计算”或“软件即服务”。那些
通常使用 Web 浏览器通过 Internet 访问资源。

在线服务器部署的主要目标是提供长期的
对预期服务的稳定和高性能可访问性。什么时候
决定为服务器环境选择哪个选项有很多
需要考虑的方面：

1.  服务器管理和操作的人力。必须有具备服务器管理一般技能的人力资源以及用于提供服务的应用程序的特定技术。此类技术的示例是 Web 服务器和数据库管理平台。

2.  可靠的自动化备份解决方案，包括本地服务器外备份和远程备份。

3.  稳定的连接性和高网络带宽用于进出服务器的流量。

4.  稳定的电源，包括备用解决方案。

5.  物理服务器的安全环境，涉及访问、盗窃和火灾等问题。

6.  存在灾难恢复计划。该计划必须包含一个切合实际的策略，以确保在发生硬件故障、网络停机等事件时，服务只会遭受短暂的停机时间。

7.  可行，强大而强大的硬件。

必须涵盖所有这些方面才能创建适当的
托管环境。硬件要求特意放在最后
因为有一个明显的趋势是给予它太多的关注。

回顾三个主要的托管选项，经验来自
发展中国家的执行任务表明，所有
在可行的情况下，选项一和选项二中很少出现托管方面
等级。在所有这些方面都达到可接受的水平具有挑战性
在人力资源和金钱方面，尤其是与
选项三的成本。它的好处是可以容纳
提到政治方面和建立服务器的本地能力
管理，另一方面，这可以在
替代方式。

选项三 - 外部托管 - 的好处是它支持所有
以非常实惠的价格提供上述托管方面的服务。一些
托管提供商 - 虚拟服务器或软件即服务 - 提供
运行大多数类型的应用程序的可靠服务。示例
此类提供商是 [Linode](http://www.linode.com) 和 [Amazon Web
服务](http://aws.amazon.com)。此类服务器的管理发生
通过网络连接，最常见的情况是
本地服务器管理。服务器在此的物理位置
案例变得无关紧要，因为此类提供商在大多数情况下提供服务
世界的一部分。该解决方案正日益成为标准
托管应用程序服务的解决方案。建筑方面
服务器管理的本地容量与此选项兼容
因为本地 ICT 团队可以负责维护外部
托管服务器，但不必担心电源
通常存在于主要之外的供应和带宽限制
数据中心。

一种将外部托管的好处与需求相结合的方法
对于本地托管和物理所有权是使用外部托管
主要事务系统的提供者，同时反映这一点
服务器到本地托管的非关键服务器，用于
只读目的，例如数据分析和通过内联网访问。

## HIS中汇总数据和患者数据之间的差异 { #difference-between-aggregated-and-patient-data-in-a-his }

_患者数据_是与单个患者相关的数据，例如他/她的诊断、姓名、年龄、早期病史等。此数据通常基于单个患者与医护人员的交互。例如，当患者访问医疗保健诊所时，可能会记录各种详细信息，例如患者的体温、体重和各种血液检查。如果该患者被诊断为与 ICD-10 代码 D51.9 相对应的“维生素 B 12 缺乏性贫血，未指定”，这种特定的相互作用最终可能会在基于聚合的系统中被记录为“贫血”的实例。当您想要纵向跟踪患者随时间的进展时，基于患者的数据非常重要。例如，如果我们想跟踪患者对结核病治疗过程的坚持和反应（通常需要 6-9 个月），我们将需要基于患者的数据。

_汇总数据_是与多个患者相关的数据的合并，因此无法追溯到特定患者。它们只是计数，例如疟疾、结核病或其他疾病的发病率。通常，卫生机构处理的常规数据是这种汇总统计数据，用于生成常规报告和指标，最重要的是，用于卫生系统内的战略规划。汇总数据无法提供患者级别数据可以提供的详细信息类型，但对于卫生系统绩效的规划和指导至关重要。

在两者之间，您有基于案例的数据，或匿名的“患者”
数据。可以收集有关特定健康事件的大量详细信息
不必确定所涉及的患者。
住院或门诊就诊、霍乱新病例、孕产妇死亡
等是人们想要收集更多的常见用例
只是添加到案例或访问总数中的详细信息。这
数据通常以行列表类型的形式收集，或者更多
详细的审计表格。它不同于某种意义上的汇总数据
它包含有关特定事件的许多详细信息，而
汇总数据将计算某种类型的事件数量，例如如何
主要诊断为“疟疾”的门诊就诊次数，或有多少
死者没有参加 ANC 的孕产妇死亡人数，或有多少
5 岁以下儿童的霍乱爆发。在 DHIS2 中，这个数据是
通过单一事件类型的程序收集，没有
登记。

患者数据是高度机密的，因此必须加以保护
除了医生，没有人能得到它。在纸上时，它必须是
妥善存放在安全的地方。对于计算机，患者数据需求
使用密码、限制访问和审计日志来保护系统。

聚合数据的安全问题不像对患者那么重要
数据，因为通常不可能识别特定的人
汇总统计。然而，数据仍然可能被滥用和
被他人误解，不应在没有足够的情况下分发
数据发布政策到位。

## 自由和开源软件（FOSS）：好处和挑战 { #free-and-open-source-software-foss-benefits-and-challenges }

软件是带有指示计算机如何操作的指令。这些指令的人工创作结果和人类的可读形式被称为源代码。在计算机实际执行指令之前，必须将源代码编译为机器可读（二进制）格式，称为目标代码。所有发布的软件都包含目标代码，但是FOSS软件也包括可获得的源代码。

专有软件所有者将其受版权保护的对象代码授权给用户，从而允许用户运行该程序。另一方面，FOSS程序同时许可目标代码和源代码，从而允许用户运行，修改并可能重新分发程序。通过访问源代码，用户可以自由地出于任何目的运行程序，重新分发，探查，改编，学习，自定义软件以适应他们的需求，并为社区的利益向公众发布改进内容。因此，某些FOSS也被称为自由软件，其中“自由”首先是指上述自由，而不是用金钱这个词来形容。

在公共卫生部门内，FOSS 可能具有一系列
好处，包括：

-   降低成本，因为它不涉及支付高昂的许可费用。

-   鉴于卫生部门的信息需求不断变化和发展，用户需要有根据用户要求进行更改的自由。这通常在专有系统中受到限制。

-   访问源代码以实现集成和互操作性。在卫生部门，不同软件应用程序之间的互操作性变得越来越重要，这意味着使两个或多个系统能够通信元数据和数据。这项工作要容易得多，有时还依赖于创建集成的开发人员可用的源代码。在专有软件的情况下，这种可用性通常是不可能的。如果是这样，它会带来高昂的成本和合同义务。

-   像 DHIS2 这样的 FOSS 应用程序通常由全球开发人员网络支持，因此可以获得尖端的研发知识。

# 使用数据输入应用 { #data_entry_app }

## 关于数据输入应用 { #about_data_entry_app }

在**数据输入**应用程序中，您可以在DHIS2中手动输入汇总数据。您一次注册一个组织单位，一个期间和一组数据元素（数据集）的数据。数据集通常对应于基于纸张的数据收集工具。您可以在**维护**应用程序中配置数据集。

> **注意**
>
> 如果一个数据集同时有一个部分表格和一个自定义表格，系统在数据输入过程中显示自定义表格。输入数据的用户无法选择他们想要使用的表单。在基于 Web 的数据输入中，显示偏好的顺序是：
>
> 1. 自定义表单（如果存在）
>
> 2. 截面形式（如果存在）
>
> 3. 默认形式
>
> 移动设备不支持自定义表单。在基于移动的数据输入中，显示偏好的顺序是：
>
> 1. 截面形式（如果存在）
>
> 2. 默认形式

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

    -   若要移动到下一个字段，请按 Tab 键或向下箭头键。

    -   要返回上一个字段，请按 Shift+Tab 或向上箭头键。

    -   如果您输入了无效值，例如字段中只接受数值的字符，您将看到一个解释问题的弹出窗口，并且该字段将显示为黄色（未保存），直到您更正该值.

    -   如果您为该字段定义了一个最小最大值范围并且您输入了一个超出此范围的值，您将收到一条弹出消息，指出该值超出范围。在您更改值或更新值范围并重新输入值之前，该值将保持未保存状态。

6.  填写表单后，点击数据输入表单右上角或下方的**运行验证**。

    然后针对新数据运行涉及当前数据输入表单（数据集）中的数据元素的所有验证规则。如果没有违反验证规则，您将看到一条消息：_数据输入屏幕已成功通过验证_。如果存在验证违规，它们将显示在列表中。

    ![](resources/images/dhis2UserManual/Validation_Rule_Result.png)

7.  （可选）更正验证冲突。

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros.

8.  改正错误并完成数据输入后，请点击**完成**。

    系统在为区、县、省或国家级生成完整性报告时使用此信息。

## 将数据值标记为后续 { #mark_data_for_followup_in_data_entry_form }

![](resources/images/data_entry/data_entry_section_history.png)

例如，如果您有需要进一步调查的可疑值，则可以将其保留为系统，但将其标记为后续。然后，在 **数据质量** 应用中，您可以运行后续分析以查看和更正所有标记的值。

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  双击您要标记为后续的值的字段。

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

3.  双击具有要查看其历史记录的值的字段。

4.  点击**数据元素历史记录**。

## 显示数据值的审核记录 { #display_data_value_audit_trail }

![](resources/images/data_entry/data_entry_audit_trail.png)

审计跟踪允许您查看其他数据值
在当前值之前输入。审计跟踪还显示何时
数据值已更改以及进行更改的用户。

1.  打开**数据输入**应用。

2.  打开一个现有的数据输入表单。

3.  双击您要查看其审计跟踪值的字段。

4.  点击**审核记录**。

## 手动创建最小值最大值范围 { #change_min_max_range_manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  在**数据输入**应用中，打开一个数据输入表单。

2.  双击要设置最小最大值范围的字段。

3.  输入**最小限制**和**最大限制**。

4.  点击**保存**。 

    如果下次输入数据时值不在新值范围内，则数据输入单元格将以橙色背景显示。

5.  （可选）键入注释以解释差异的原因，例如可能产生大量客户的设施中的事件。

6.  （可选）点击**保存评论**。

> **提示**
>
>单击星号图标以标记该值以进行进一步跟踪。

## 离线输入数据 { #enter_data_offline }

即使您在数据输入过程中没有稳定的Internet连接，**数据输入**应用程序仍能正常工作。没有互联网连接时，输入的数据将保存到本地计算机。当Internet连接恢复时，该应用程序会将数据推送到服务器。由于不再从服务器为每个渲染检索数据输入表单，因此减少了总带宽使用量。

> **注意**
>
> 要使用此功能，您必须在有 Internet 连接时登录服务器。

-   当您连接到 Internet 时，该应用程序会在数据输入表单的顶部显示以下消息：

    ![](resources/images/data_entry/data_entry_online1.png)

-   如果您的 Internet 连接在数据输入期间中断，应用程序会检测到它并显示以下消息：

    ![](resources/images/data_entry/data_entry_offline1.png)

    现在您的数据将存储在本地。您可以继续正常输入数据。

-   一旦您输入了所有必要的数据并且应用程序检测到 Internet 连接已恢复，您将看到以下消息：

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

    数据元素将在表单中显示为列，组织单元显示为行。

    > **Note**
    >
    > The data entry forms should still be assigned to the facilities that you actually enter data for, that is the organisation units now appearing in the form.

## 也可以看看 { #data_entry_app_see_also }

-   [控制数据质量](https://docs.dhis2.org/master/en/user/html/control_data_quality.html)

-   [管理数据集和数据输入表格](https://docs.dhis2.org/master/en/user/html/manage_data_set.html)

-   [使用维护应用程序](https://docs.dhis2.org/master/en/user/html/maintenance_app.html)

# 使用捕获应用 { #capture_app }

## 关于Capture应用 { #about_capture_app }

> **注意**
>
>“捕获”应用程序可以代替“事件捕获”应用程序。将来，Tracker Capture应用程序和Data Entry应用程序也将合并到Capture应用程序中。

在Capture应用程序中，您可以注册在特定时间和地点发生的事件。事件可以在任何给定的时间点发生。这与常规数据形成对比，常规数据是按预定义的定期间隔捕获的。事件有时称为案例或记录。在DHIS2中，事件链接到程序。使用Capture应用程序，您可以在输入事件信息之前选择组织单位和程序，并指定事件发生的日期。

## 注册活动 { #capture_register_event }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   您将仅看到与所选组织单位相关联的程序以及您有权访问的程序，并且这些程序通过数据级别共享与用户组共享。

4. 如果程序具有类别组合设置，则必须选择类别选项。

5. 点击**新建**。

    ![创建新事件](resources/images/capture_app/create_new_event.png)

6. 填写必填信息。如果将程序程序阶段配置为捕获位置：

    - 如果该字段是坐标字段，您可以直接输入坐标，也可以单击坐标字段左侧的**地图**图标。后者将打开一张地图，您可以在其中搜索位置或通过单击地图直接进行设置。

    - 如果该字段是一个多边形字段，您可以单击该字段左侧的 **map** 图标。这将打开一个地图，您可以在其中搜索位置并捕获多边形（地图右上角的按钮）。

7. 如果需要，您可以通过单击表单底部的**写评论**按钮来添加评论。

8. 如果需要，您可以通过点击底部的**添加**按钮来添加关系形式。有关更多信息，请参见相关**添加关系**的部分。

9. 单击**保存并退出**或单击按钮旁边的箭头以选择**保存并添加另一个**。

    - **保存并添加另一个**将保存当前 事件 并清除 形式. 您捕获的所有事件将显示在页面底部的列表中。当您想完成捕获事件时，您可以，如果形式 为空白，单击完成按钮，或者如果您 形式 包含数据单击**保存并添加另一个**旁边的箭头，然后选择**保存并退出**。

> **注意** 
> 
> 一些数据元素事件可能是先在数据元素触发的（在数据元素中）。在允许用户，必须完成所有必填数据元素事件。例外是，情况用户如果知道**“不会漏查器中必填字段的验证和事件事件”。**用户有此权限，则无需填写数据元素，并且如果在查看红星数据元素标签。请注意，拥有**“ALL”**权限的超级用户自动拥有此权限。

> **提示** 
> 
> 数据录入形式也可以在**行视图**中显示。在这种模式下元素是水平排列的，这可以通过鼠标的数据行视图**切换到**按钮来实现形式。如果您当前处于**行视图**，则可以切换到默认形式，通过**切换到查看形式数据输入的查看**按钮形式。

## 注册跟踪的实体实例 { #register-a-tracked-entity-instance }

有两种不同的方式可以在组织单位下注册被跟踪的实体实例。
第一种方法是注册一个被跟踪实体实例而不将其注册到跟踪器程序。
第二个选项是向程序注册一个被跟踪的实体实例并注册它。

### 没有程序注册 { #without-a-program-enrollment }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 点击“新建”按钮。

    ![image](resources/images/capture_app/register-without-enrollment-new-button.png)

    您现在将被导航到注册页面。在该页面中，您将看到一个类似于下图中的下拉菜单。从下拉菜单中，您可以选择跟踪的实体类型，例如。建筑、人物等

    ![image](resources/images/capture_app/register-without-enrollment-dropdown-menu.png)

4. 选择要为其创建新实例的跟踪实体类型。

    ![image](resources/images/capture_app/register-without-enrollment-dropdown-menu-with-arrow.png)

5. 选择跟踪实体类型后，屏幕上将显示一个表单。

    将显示“个人资料”部分。在本节中，您可以添加与被跟踪实体实例相关的数据。 profile 部分主要包含链接到被跟踪实体类型的所有被跟踪实体属性。

    ![image](resources/images/capture_app/register-without-enrollment-form.png)

6. 填写必填信息。

   如果将跟踪的实体类型配置为捕获位置：

    - 如果该字段是坐标字段，您可以直接输入坐标，也可以单击坐标字段左侧的**地图**图标。后者将打开一张地图，您可以在其中搜索位置或通过单击地图直接进行设置。

    - 如果该字段是一个多边形字段，您可以单击该字段左侧的 **map** 图标。这将打开一个地图，您可以在其中搜索位置并捕获多边形（地图右上角的按钮）。

7. 单击**保存新的**按钮以注册跟踪的实体实例。
8. 现在将提示您进入跟踪的实体实例仪表板。

   仪表板将显示有关新创建的跟踪实体实例的相关信息。

### 报名参加 { #with-a-program-enrollment }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择您选择的跟踪器程序，类似于下图。

    ![创建新事件](resources/images/capture_app/register-and-enroll-program-selection.png)

4. 单击“新建”下拉按钮，然后单击第一个选项。

    第一个选项看起来类似于下图。我们示例中的文本是“儿童计划中的新人”。单击此选项将提示您进入所选程序的注册和注册页面。 ![创建新活动](resources/images/capture_app/register-and-enroll-dropdown-button-new-person-in-program.png)

5. 现在，您将能够看到类似于下图的表单。

    该表格将有两个部分。第一部分的标题是“注册”。在那里，您将添加与该计划注册相关的所有信息。第二部分的标题为“配置文件”，您将在其中添加与被跟踪实体实例相关的数据。 profile 部分主要包含链接到程序或被跟踪实体类型的所有被跟踪实体属性。

    ![创建新活动](resources/images/capture_app/register-and-enroll-form.png)

6. 填写两个部分的必填信息。如果被跟踪实体类型配置为捕获位置：

    - 如果该字段是坐标字段，您可以直接输入坐标，也可以单击坐标字段左侧的**地图**图标。后者将打开一张地图，您可以在其中搜索位置或通过单击地图直接进行设置。

    - 如果该字段是一个多边形字段，您可以单击该字段左侧的 **map** 图标。这将打开一个地图，您可以在其中搜索位置并捕获多边形（地图右上角的按钮）。

7. 单击**保存新**以注册跟踪的实体实例。
8. 现在将提示您进入跟踪的实体实例仪表板。

   仪表板将显示有关新创建的跟踪实体实例的相关信息。

> **注意** 
> 
> 一些数据元素事件可能是先在数据元素触发的（在数据元素中）。在允许用户，必须完成所有必填数据元素事件。例外是，情况用户如果知道**“不会漏查器中必填字段的验证和事件事件”。**用户有此权限，则无需填写数据元素，并且如果在查看红星数据元素标签。请注意，拥有**“ALL”**权限的超级用户自动拥有此权限。

> **提示** 
> 
> 数据录入形式也可以在**行视图**中显示。在这种模式下元素是水平排列的，这可以通过鼠标的数据行视图**切换到**按钮来实现形式。如果您当前处于**行视图**，则可以切换到默认形式，通过**切换到查看形式数据输入的查看**按钮形式。

### 使用自动生成的事件注册 { #enrollment-with-auto-generated-events }

程序可以配置为具有零个或多个程序阶段，这些阶段在新注册时自动生成。
这些阶段将根据元数据配置自动生成，如下所述。

要配置事件的自动生成，您需要执行以下步骤。

1. 打开维护应用程序

2. 选择程序选项卡 ![](resources/images/capture_app/auto-generated-01.png)

3. 选择一个跟踪程序 ![](resources/images/capture_app/auto-generated-02.png)

4. 选择程序阶段选项卡 ![](resources/images/capture_app/auto-generated-03.png)

5. 点击您要配置的阶段 ![](resources/images/capture_app/auto-generated-04.png)

6. 将舞台标记为自动生成的 ![](resources/images/capture_app/auto-generated-05.png)

现在，对于该计划中的每一个新注册，都会自动生成一个事件。一个程序也可以有多个标记为自动生成的阶段。
对于所有自动生成的事件

 a) 在注册期间，组织单位将与用户报告的组织单位相同，并且

 b) 所有事件都将成为当前注册的一部分。

根据配置，自动生成事件的状态可以是 ACTIVE 或 SCHEDULE。

#### 活动类型 { #active-type-of-event }

如果阶段选择了“注册后打开数据输入表”，则该事件将生成为 ACTIVE 状态。除了截止日期外，还将为事件计算其执行日期。
生成基于注册日期或事件日期。您可以从“报告使用日期”下拉菜单中选择报告日期。
![](resources/images/capture_app/auto-generated-06.png)

如图所示，您有三个选项，a) 事件日期 b) 注册日期或 c) 无值。
选择报告日期为“事件日期”表示事件执行日期和截止日期都将与事件日期相同。
选择报告日期为“注册日期”或“无值”表示事件执行日期和截止日期都将与注册日期相同。

#### 日程安排类型 { #schedule-type-of-event }

如果未勾选“注册后打开数据输入”，则表示生成的事件将是 SCHEDULE 事件。
预定事件没有执行日期，只有截止日期。这些未来事件的截止日期是根据注册日期或事件日期计算的。如果选中下面的标志，则参考日期是注册日期，如果未选中该标志，则使用事件日期。
![](resources/images/capture_app/auto-generated-07.png)

如果没有事件日期，则无论是否选中上述标志，参考日期都将退回到注册日期。

对于 SCHEDULE 类型的事件，用户还可以配置“从开始算起的预定天数”。这意味着如果一个阶段在“从开始算起的预定天数”中有一个数字，则参考日期将增加该数字。
在下面的示例中，我们将截止日期增加了 30 天。
![](resources/images/capture_app/auto-generated-08.png)

当“从开始的预定天数”不包含数字或包含 0 时，使用参考日期而不添加任何天数。

### 可能的重复检测 { #possible-duplicates-detection }

在注册被跟踪实体实例的两种情况下（有注册或没有注册），系统都会警告您可能的重复。
请注意，需要通过维护应用程序正确配置程序才能出现重复警告。

要通过维护应用程序配置程序，您必须：

1. 打开维护应用程序。 ![](resources/images/capture_app/duplicates-maintenance-config-00.png)

2. 在程序部分选择您的程序。我们为此示例选择子程序。 ![](resources/images/capture_app/duplicates-maintenance-config-01.png)

3. 选择属性选项卡。 ![](resources/images/capture_app/duplicates-maintenance-config-02.png)

4. 通过将程序属性检查为可搜索 ![](resources/images/capture_app/duplicates-maintenance-config-03.png) 来启用重复搜索

您选择为“可搜索”的属性将是系统用来检测可能的重复项的属性。
让我们通过一个示例来解释这一点，该示例演示在为儿童计划注册儿童时检测可能的重复项。

1. 打开 **Capture** 应用程序。 ![](resources/images/capture_app/duplicates-on-creation-00.png)

2. 从顶部的菜单中选择您的组织单位和计划。 ![](resources/images/capture_app/duplicates-on-creation-01.png)

3. 单击“新建”->“子程序中的新人”![](resources/images/capture_app/duplicates-on-creation-02.png)

4. 在表格中填写名字。 **请记住，我们在维护应用程序中已将名字检查为“可搜索”。** 因为我们已将名字检查为“可搜索”，系统才会开始寻找与您的名字 Sarah 匹配的可能重复项见下图。 ![](resources/images/capture_app/duplicates-on-creation-03.png)

5. 单击带有文本“可能重复”![](resources/images/capture_app/duplicates-on-creation-04.png) 的链接

6. 查看可能的重复项 ![](resources/images/capture_app/duplicates-on-creation-05.png)

> **提示**
>
> 您可以像我们为程序所做的那样，为跟踪的实体类型配置重复检测。

### 程序规则执行 { #program-rules-execution }

在注册跟踪实体实例的两种情况下（有注册或没有注册），系统将运行您配置的程序规则。
请注意，可以在维护应用程序中配置规则。

要在注册跟踪实体实例时查看正在执行的规则，您必须执行以下步骤。

1. 在维护应用程序中配置规则。对于下面的示例，我们配置了一个规则，当出生日期小于一年时会发出警告。

2. 打开 **Capture** 应用程序。 ![](resources/images/capture_app/duplicates-on-creation-00.png)

3. 从顶部的菜单中选择您的组织单位和计划。 ![](resources/images/capture_app/program-rules-on-creation-00.png)

4. 用小于一年的值填写出生日期。在我们的例子中，这是 2021 年 1 月 27 日。![](resources/images/capture_app/program-rules-on-creation-01.png)

5. 您现在可以在出生日期字段下方看到程序规则产生的警告。 ![](resources/images/capture_app/program-rules-on-creation-02.png)

## 添加关系 { #capture_add_relationship }

Relationships can be added either during registration, editing or viewing of an event. Currently the **Capture App** only supports _Event to Tracked Entity Instance_ relationships.

1. 如果发生事件，请单击**添加关系**。

2. 选择您要创建的关系类型。

您现在有两个选择：

-   **链接到现有的跟踪实体实例**或

-   **创建新的跟踪实体实例**。

![关系选项](resources/images/capture_app/relationship_options.png)

### 链接到现有的跟踪实体实例 { #link-to-an-existing-tracked-entity-instance }

1. Click **Link to an existing Tracked Entity Instance**.

-   您将看到一些用于搜索 **跟踪实体实例** 的选项。您可以选择**项目**。如果选择了**项目**，则属性源自所选的**项目**。如果未选择 **项目**，则只有属于 **跟踪实体实例** 的属性可见。

      ![搜索跟踪实体实例](resources/images/capture_app/search_tei.png)

    -   If the **Tracked Entity Instance** or **program** is configured with a unique attribute, this attribute can be used for finding a specific **Tracked Entity Instance** or **program**. This attribute should be presented alone. When the unique attribute field has been filled out, click the **Search** button located right below the unique attribute field.

    -   如果**跟踪实体Instance** 或 **program** 具有属性，这些属性可通过展开 **Search by attributes** 框用于搜索。填写完所有所需的属性字段后，单击位于底部的**按属性搜索** 按钮。您还可以通过设置**组织单位范围**来限制搜索。如果设置为 _All 可访问_，您将搜索 **跟踪实体您有权访问的所有组织单位中的实例**。如果您选择 _Selected_，系统会要求您选择要在哪些组织单位内进行搜索。

2. 成功搜索后，您将看到 ** 列表跟踪实体符合搜索条件的实例**。要创建关系，请单击 ** 上的 **Link** 按钮跟踪实体 您想与之建立关系的实例**。

-   如果你没有找到**追查实体您正在寻找的实例**，您可以点击**新搜索**或**编辑搜索**按钮。**新搜索**将带您进入新的空白搜索，而**编辑搜索**将带您返回到您只需执行的搜索，并保留搜索条件。

### 创建新的跟踪实体实例 { #create-new-tracked-entity-instance }

1. 点击**新建 追查实体 实例**。

-   您现在会看到一个 形式 用于注册新的**跟踪实体实例**。您可以选择注册或不注册程序。如果选择了一个程序，新的**跟踪实体实例**将被注册到所述程序中。您还可以通过删除自动设置的组织单位并选择新的组织单位来更改 **组织单位**。

    ![注册新的跟踪实体实例](resources/images/capture_app/register_tei.png)

2. 填写所需的（可能是必填的）属性和注册详细信息。

3. Click **Create Tracked Entity Instance and Link**.

> **注意**
>
> 填写数据时，您可能会遇到警告，告诉您已发现可能的重复项。您可以单击警告以查看这些重复项，如果重复项匹配，您可以选择链接该 **跟踪实体单击 **Link** 按钮实例**。如果完成数据填写后警告仍然存在，您将不会看到 **Create跟踪实体实例和链接**按钮。相反，您将看到一个名为 **Review duplicates** 的按钮。单击此按钮时，将显示可能重复的列表。如果这些重复项中的任何一个与 ** 匹配跟踪实体 您正在尝试创建的实例**您可以点击**链接**按钮，如果没有，您可以点击**另存为新人**按钮注册一个新的**跟踪实体 实例**。

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

> **提示**
>
> 您可以通过将数据元素拖放到列表中来重新组织数据元素的顺序。

## 过滤事件列表 { #capture_filter_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。

   注册到所选程序的所有事件均显示在列表中。

   事件列表顶部是按钮，其名称与列表中的列标题相同。

4. 使用列表顶部的按钮可根据报告日期或特定数据元素进行过滤。

    ![过滤事件](resources/images/capture_app/filter_event.png)

> **注意**
>
> 不同的数据元素类型以不同的方式进行拟合。例如，**Number** 数据元素将显示要筛选的范围，而 **Text** 数据元素将要求您输入要筛选的搜索查询。

## 排序活动清单 { #capture_sort_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。注册到所选程序的所有事件都显示在列表中。

4. 单击列标题之一，以按升序对该数据元素上的列表进行排序。

   列旁边会显示一个向上的小箭头，以表明列表是按升序排序的。

5. 再次单击列标题，以降序对该数据元素上的列表进行排序。

   该列旁边会显示一个小的向下箭头，以显示该列表以降序排列。

    ![排序事件](resources/images/capture_app/sort_event.png)

## 下载活动清单 { #capture_download_event_list }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个程序。注册到所选程序的所有事件都显示在列表中。

4. Click the **downward arrow** icon on the top right of the event list.

5. 选择您要下载的格式。

    ![下载活动列表](resources/images/capture_app/download_event_list.png)

> **注意**
>
> 您可以下载 JSON、XML 或 CSV 格式的事件列表。

## 预定义列表视图 { #capture_views }

您可以设置自己的视图并保存以供以后使用。这些视图也可以与其他人共享。视图由过滤器，列顺序和事件排序顺序组成。

### 保存新视图 { #capture_view_save }

1. 选择一个组织单位和一个程序。

2. 使用事件列表上方的过滤器按钮设置过滤器（在此处详细说明（#capture_filter_event_list））。

    ![](resources/images/capture_app/view_save_filters.png)

3. 通过单击齿轮图标设置列顺序，然后在弹出窗口中根据您的偏好指定布局（如何修改布局在[此处]（＃capture_modify_event_list_layout）详细说明）。

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

    > **Note**
    >
    > An asterisk(\*) is appended to the view name when the view has unsaved changes.

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

Capture应用程序尚不支持跟踪程序，但是仍列出了跟踪程序。如果您选择一个跟踪器程序，该应用程序将带您进入“跟踪器捕获”应用程序，如下所示。

![](resources/images/capture_app/tracker_program.png)

## 搜索跟踪的实体实例 { #search-for-tracked-entity-instances }

### 在计划范围内 { #in-program-scope }

1. 打开**捕获**应用。

2. 选择一个程序。

   您将仅看到与所选组织单位相关联的程序以及您有权访问的程序，并且这些程序通过数据级别共享与用户组共享。

3. 如果程序具有类别组合设置，则必须选择类别选项。

4. 单击查找按钮。

5. 从下拉菜单中单击第一个选项。

    ![](resources/images/capture_app/search-by-attributes-find-button.png)

   这些步骤将带您进入搜索页面。在这里，根据组织的配置，您将看到可以搜索的不同属性。下面是一个如何看起来的示例。

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-0.png)

   要立即执行搜索：

6. 填写要搜索的属性。

7. 单击**按属性搜索**按钮。 

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-1.png)

8. 搜索结果将显示如下。

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-2.png)

   在此列表中，您可以看到与搜索匹配的条目。对于每个条目，您总共可以有三个选项。

    一种。您可以通过单击“查看仪表板”按钮来选择查看 **Tracked Entity Instance** 的仪表板

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-5.png)

    湾您可以通过单击“查看活动注册”按钮查看 **跟踪实体实例** 的活动注册

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-3.png)

    C。您可以将 **Tracked Entity Instance** 重新注册到您正在搜索的当前程序中。

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-4.png)

#### 后备搜索 { #fallback-search }

您进行了完整的搜索结果，则您明确显示了这些结果。但是，正在搜索的具体**T 跟踪真实实例** 可能不同的中。如果在这种情况下，您可能希望将搜索扩展到其他项目。

要执行后备搜索，只需按下底部的“搜索所有程序”按钮。

> **注意**
>
> 只有在程序内搜索时才可以进行后备搜索。

![](resources/images/capture_app/search-by-attributes-fallback-overview-0.png)

### 在“跟踪的实体类型”范围中 { #in-tracked-entity-type-scope }

1. 打开**捕获**应用。

2. 点击**查找**按钮打开搜索页面。

3. 单击下拉菜单，然后选择要搜索的实体类型。

    ![](resources/images/capture_app/search-by-attributes-domain-selector-overview-0.png)

4. 从列表中进行选择。

    ![](resources/images/capture_app/search-by-attributes-domain-selector-overview-1.png)

   根据组织的配置，您将看到可以搜索的不同属性。下面是一个如何看起来的示例。

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-0.png)

   要立即执行搜索：

5. 填写要搜索的属性。

6. 单击按属性搜索按钮。

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-1.png)

7. 搜索结果将显示如下。

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-2.png)

    在此列表中，您可以看到与您的搜索匹配的条目。对于每个条目，您都可以选择单击“查看仪表板”按钮以查看 **Tracked Entity Instance** 的仪表板。

### 结果功能过多 { #too-many-results-functionality }

您正在其中搜索的程序或跟踪的实体类型可能配置有对从搜索中检索到的结果数的限制。如果您的搜索结果超过了此限制，则会显示一条警告消息，如下所示。

![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-too-many-results-message.png)

### 分页 { #pagination }

结果页面一次最多显示五个结果。您应该尝试使用特定的搜索条件，以便没有太多的匹配项。但是，如果有五个以上的结果，则可以使用页面末尾的**> **按钮查看下一个结果。

![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-pagination.png)

## 列出在程序 { #list-tracked-entity-instances-enrolled-in-program } 中注册的跟踪实体实例 { #list-tracked-entity-instances-enrolled-in-program }

1. 打开**捕获**应用。

2. 选择一个组织单位。

3. 选择一个跟踪程序。

4. 该程序可以具有与其关联的类别（实施合作伙伴将是此类类别的一个示例）。如果是这种情况，请填写它们。

### 过滤列表 { #filter-the-list }

使用列表本身上方的按钮对其进行过滤。

![](resources/images/capture_app/tei_list_filters.png)

例如，您可以过滤列表以仅显示已分配事件的跟踪实体实例：单击“分配给”过滤器 (1)，选择“我”(2)，然后“应用”更改 (3 ）。

![](resources/images/capture_app/tei_list_filter_example.png)

### 对列表进行排序 { #sort-the-list }

单击列标题之一以按该列对列表进行排序。列标题旁边会显示一个小箭头，以指示当前的排序顺序。再次单击可在升序和降序之间切换。

![](resources/images/capture_app/tei_list_sort_order.png)

### 修改列表布局 { #modify-the-list-layout }

您可以选择要在列表中显示的列，还可以重新组织列的顺序。

单击列表右上角的**齿轮** 图标。勾选要显示的列的复选框 (1) 并通过拖放 (2) 重新组织列。 

![](resources/images/capture_app/tei_list_column_layout.png)

### 加载预定义的列表视图 { #loading-a-predefined-list-view }

您将在列表过滤器上方找到预定义的列表视图。单击以加载视图。

![](resources/images/capture_app/tei_list_predefined_views.png)

## 实施者/管理员信息 { #implementer_info }

### 元数据缓存 { #metadata_caching }

出于性能原因，Capture应用程序在客户端浏览器中缓存元数据。在服务器上更新元数据时，需要将更改传播到已经缓存了元数据的客户端。根据更改，可以通过以下三种方式之一完成此操作：

1. 如果更改绑定到某个程序，则需要为该特定程序增加程序版本。例如，如果您更改程序或程序规则中的数据元素，则需要增加绑定程序的版本。

2. 如果更改未绑定到程序，则需要增加任何程序版本，以将更改传播到客户端。这里的示例是对常量，组织单位级别或组织单位组的更改。

3. 上面两个规则的例外是选项集。选项集具有自己的版本属性，即，增加选项集版本应确保将选项集元数据传播到客户端。

## 注册仪表板 { #enrollment-dashboard }

### 通过 url { #reaching-the-enrollment-dashboard-via-url } 到达注册仪表板 { #reaching-the-enrollment-dashboard-via-url }

您可以通过在浏览器的地址栏中键入或使用捕获应用程序的用户界面来访问注册仪表板。
在本节中，我们关注第一个用例，您可以在地址栏中键入或粘贴要访问的 url。

![](resources/images/capture_app/enrollment-dash-01.png)

访问注册仪表板并查看特定跟踪实体实例的注册的一种方法是使用 _only_ 注册 ID。例如链接 .../dhis-web-capture/#/?enrollmentId=wBU0RAsYjKE 将
为您提供 ID 为`wBU0RAsYjKE`的注册仪表板。

仪表板的顶部定义了您的上下文。例如下图中的上下文如下，选择的程序是“Child Programme”，组织单位是“Ngelehun CHC”，选择的人是“Anna Jones”，选择的招生是“2017-11-16 11 :38"。

![](resources/images/capture_app/enrollment-dash-02.png)

您可以通过单击“x”按钮来更改上下文。

![](resources/images/capture_app/enrollment-dash-03.png)

#### 取消选择程序 { #deselecting-the-program }

当您取消选择该程序时，您会看到以下内容

![](resources/images/capture_app/enrollment-dash-05.png)

##### 选择一个有注册的程序 { #selecting-a-program-with-enrollments }

当程序_和_注册选择为空时，您首先必须选择一个程序。
如果被跟踪实体实例（在本例中为“Anna Jones”）在您选择的程序下注册，您将看到以下消息。

![](resources/images/capture_app/enrollment-dash-09.png)

##### 选择零注册的程序 { #selecting-a-program-with-zero-enrollments }

如果被跟踪的实体实例（在本例中为“Anna Jenkins”）在您选择的计划下没有注册，您将看到一条消息，说明该计划没有注册。
您还可以选择在该计划中注册“安娜·詹金斯”。

![](resources/images/capture_app/enrollment-dash-10.png)

##### 选择活动程序 { #selecting-an-event-program }

当您选择一个事件程序时，您将看到以下内容。 （请记住，事件程序在系统中没有注册，只有跟踪程序有）。

![](resources/images/capture_app/enrollment-dash-11.png)

您还可以选择为所选节目创建新事件或查看所选节目的工作列表。

##### 选择具有不同跟踪实体类型的程序 { #selecting-a-program-with-a-different-tracked-entity-type }

当您选择的跟踪实体类型是人时，如我们的 Anna Jenkins 示例，并且您选择的程序不是人类型而是疟疾病例类型，您将看到以下内容。

![](resources/images/capture_app/enrollment-dash-12.png)

您还可以选择在您选择的程序中注册跟踪实体实例。

#### 取消选择组织单位 { #deselecting-the-organisation-unit }

当您取消选择组织单位时，您会看到以下内容

![](resources/images/capture_app/enrollment-dash-06.png)

#### 取消选择跟踪实体实例 { #deselecting-the-tracked-entity-instance }

当您取消选择被跟踪实体实例时，在本例中为“Anna Jones”，您将被带到该 Tracker 程序中的工作列表。

![](resources/images/capture_app/enrollment-dash-07.png)

#### 取消选择注册 { #deselecting-the-enrollment }

当您取消选择注册时，您会看到以下内容

![](resources/images/capture_app/enrollment-dash-08.png)

# 使用事件捕获应用 { #event_capture_app }

## 关于事件捕获应用 { #about_event_capture_app }

![](resources/images/event_capture/event_list.png)

在**事件捕获**应用中，您可以注册在特定时间和地点发生的事件。事件可以在任何给定的时间点发生。这与常规数据相反，常规数据可以按预定义的定期间隔进行捕获。事件有时称为案例或记录。在DHIS2中，事件链接到程序。通过**事件捕获**应用程序，您可以在输入事件信息之前选择组织单位和程序，并指定事件发生的日期。

**事件捕获**应用程序可在线和离线使用。如果互联网连接中断，您可以继续连接事件。事件将本地存储器客户端浏览。当恢复时，系统会要求您上传本地存储的数据。然后系统将数据发送到存储数据的服务器。

> **注意**
>
> 如果您在离线模式下关闭 Web 浏览器，则无法重新打开新的 Web 浏览器窗口并继续工作会话。但是数据仍然会保存在本地，下次机器在线并且您已登录服务器时，可以将数据上传到服务器。

-   您只能看到与您选择的组织单位相关联的计划，以及您有权通过您的用户角色查看的计划。

-   注册期间支持跳过逻辑和验证错误/警告消息。

-   当您关闭一个组织单位时，您将在**中向该组织单位注册或编辑活动事件捕捉**应用程序。您还可以查看和过滤事件并查看详细信息。

-   支持动态指标表达式评估。如果一个程序有为其定义的指标，并且与指标表达式相关的所有值都被填充，系统将计算指标并显示结果。

    ![](resources/images/event_capture/event_editing.png)

-   **排序：**这可以通过单击每个列标题的排序图标来完成。红色排序图标表示当前排序列。但是，排序功能仅在显示的页面内有效。目前，无法从服务器端进行排序。

-   **过滤：**这是通过单击每个列标题右侧显示的小搜索图标来完成的。单击它们会提供一个输入字段以键入过滤条件。系统在用户开始键入时开始应用过滤器。在过滤期间，可以定义日期类型数据元素的开始和结束日期以及数字类型的下限和上限。目前不支持服务器端过滤。

## 注册活动 { #event_capture_register_event }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    您只会看到与所选组织单位相关联的计划以及您可以通过您的用户角色访问的计划。

4.  点击**注册事件**。

5.  选择一个日期。

6.  填写必填信息。

    如果程序的程序阶段配置为捕获GPS坐标，则可以通过两种方式输入坐标：

    -   直接在相应字段中输入值。

    -   在地图中选择一个位置。地图选项还显示为组织单位定义的多边形和点。

7.  点击**保存并添加新**或**保存并返回**。

> 注意：事件中的某些数据元素可能是强制性的（在数据元素标签旁边标有红星）。这意味着在允许用户保存事件之前，必须填写所有必需的数据元素。例外情况是，如果用户拥有名为**“忽略跟踪器和事件捕获中的必填字段的验证”的权限。** 如果用户拥有此权限，则在保存之前不需要填写必填数据元素并且红色星号不会显示在数据元素标签旁边。请注意，拥有 **"ALL"** 权限的超级用户自动拥有此权限。

## 编辑活动 { #event_capture_edit_event }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  点击事件您要修改并选择**编辑**。

5.  修改事件详细信息并点击**更新**。

## 编辑网格中的事件 { #event_capture_edit_event_grid }

**在网格中编辑**功能允许您编辑选定的 事件在表格中，但只有那些列（数据元素）在网格中可见。如果您需要更多列，请使用**显示/隐藏列** 指定应在列表中显示哪些列。

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  点击 事件 您要修改并选择**在网格中编辑**。

5.  修改事件详细信息。

6.  单击另一个事件以关闭编辑模式。

## 在编辑模式下分享活动 { #event_capture_share_event_edit_mode }

您可以通过事件的网址以编辑模式共享事件。

1.  打开**事件采集**应用。

2.  在编辑模式下打开要共享的事件。

3.  复制URL。

    确保 URL 包含“event”和“ou”（组织单位）参数。

4.  将 URL 粘贴到您选择的共享方法中，例如 DHIS2 中的电子邮件或消息。

    如果您在单击链接时未登录 DHIS2，系统会要求您登录，然后转到仪表板。

## 查看事件审核历史记录 { #event_capture_view_event_audit_history }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  单击一个 事件 并选择**审计历史**。

## 删除活动 { #event_capture_delete_event }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  单击一个 事件 并选择**删除**。

5.  点击**删除**确认删除。

## 修改事件列表的布局 { #event_capture_modify_event_list_layout }

您可以选择在事件列表中显示或隐藏哪些列。这个可以
例如当您有很长的数据元素列表时很有用
分配到程序阶段。一旦你修改了布局，它就会被保存
在您的用户个人资料上。您可以针对不同的布局使用不同的布局
程式。

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  点击**显示/隐藏列**图标。

5.  选择要显示的列，然后单击**关闭**。

## 打印事件列表 { #event_capture_print_event_list }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  点击**打印列表**。

## 下载活动清单 { #event_capture_download_event_list }

1.  打开**事件采集**应用。

2.  选择一个组织单位。

3.  选择一个程序。

    注册到所选程序的所有事件均显示在列表中。

4.  点击** Downlad **图标，然后选择一种格式。

    您可以下载XML，JSON或CSV格式的事件列表。

# 使用Tracker Capture应用 { #tracker_capture_app }

## 关于Tracker Capture应用 { #about_tracker_capture_app }

![](resources/images/tracker_capture/tracker-capture-tei-list.png)

**Tracker Capture **应用程序是** Event Capture **”应用程序的高级版本。

-   **事件 捕获**：处理单个事件_无需_注册

-   **Tracker Capture**：处理多个事件（包括单个事件）_with_注册。

-   您为已注册的被跟踪实体实例 (TEI) 捕获事件数据。

-   您只能看到与您选择的组织单位相关联的计划，以及您有权通过您的用户角色查看的计划。

-   您在搜索和注册功能中看到的选项取决于您选择的程序。程序属性控制这些选项。这些属性还决定了 TEI 列表中的列名。

    如果未选择程序，则系统将选择默认属性。

-   注册期间支持跳过逻辑和验证错误/警告消息。

-   关闭单位部门后，您将无法在**跟踪随访**应用程序中注册或编辑事件到该单位部门。您仍然可以搜索TEI并过滤搜索结果。您还可以查看特定TEI的仪表板。

## 关于跟踪的实体实例（TEI）仪表板 { #about_tracked_entity_instance_dashboard }

![](resources/images/tracker_capture/tei_dashboard.png)

您可以通过 **Tracker Capture** 应用程序中的 TEI 仪表板管理 TEI。

-   仪表板由小部件组成。拖放小部件以将它们按顺序放置在您想要的位置。

-   单击图钉图标将小部件的右列固定到固定位置。这在数据输入期间尤其有用。

    如果您有许多数据元素或大表格要填写，请粘贴正确的小部件列。然后，当您在数据输入部分滚动时，您放置在右栏中的所有小部件仍然可见。

-   为您选择的程序定义的任何指标都将计算其值并显示在 **Indicators** 小部件中。

-   导航：

    -   **返回**：带您返回搜索和注册页面

    -   上一个和下一个按钮：将您带到 TEI 搜索结果列表中的上一个或下一个 TEI 仪表板

    <!-- end list -->

    -   **其他计划** 字段：如果 TEI 注册了其他计划，则会在此处列出。单击一个程序以更改您为所选 TEI 输入数据的程序。当您更改程序时，小部件中的内容也会发生变化。

## 工作流程 { #workflow_tracker_capture }

母婴健康工作流程
程序

![](resources/images/patients_programs/name_based_information_tracking_process.png)

1.  创建新的或找到现有的TEI。

    您可以搜索已定义的属性，例如名称或地址。

2.  将TEI注册到程序中。

3.  该应用程序根据该计划的服务时间，为 TEI 创建一个活动计划。

4.  TEI 根据项目提供各种服务。记录所有服务。

5.  使用有关个别案例的信息来创建报告。

## 链接到Tracker Capture应用 { #linking_to_the_tracker_capture_app }

### 链接到“主屏幕”上的特定程序 { #link-to-a-specific-program-on-the-home-screen }

您可以在“主屏幕上共享程序选择。

1. 打开 **随访采集** 应用程序。

2. 选择要链接的程序。

3. 复制URL。

    - 确保URL包含“ program”参数。

4. 将 URL 粘贴到您选择的共享方法中，例如 DHIS2 中的电子邮件或消息。

> 注意：如果所选组织单元中不存在程序（存储在本地缓存中），系统将改为选择该组织单元的第一个可用程序。如果本地缓存为空/干净且当前用户的根组织单元没有指定的程序，系统也会在此处为根组织单元选择第一个可用的程序。

### 链接到TEI仪表板 { #linking-to-tei-dashboard }

您可以通过其网址共享TEI仪表板。

1.  打开 **随访采集** 应用程序。

2.  打开您要共享的仪表板。

3.  复制URL。

    确保 URL 包含“tei”、“program”和“ou”（组织单位）参数。

4.  将 URL 粘贴到您选择的共享方法中，例如 DHIS2 中的电子邮件或消息。

    如果您在单击链接时未登录 DHIS2，系统会要求您登录，然后转到仪表板。

## 创建TEI并将其注册到程序中 { #create_and_enroll_tracked_entity_instance }

您可以创建TEI并通过一次操作将该TEI注册到程序中：

1.  打开 **随访采集** 应用程序。

2.  在左侧窗格的组织单位树中，选择一个组织单位。

3.  选择一个程序。

4.  点击**注册**。

5.  填写必填信息。

    被跟踪实体类型和程序都可以配置为使用特征类型。这使得捕获 TEI 或注册的几何图形成为可能。支持的要素类型是点和多边形。请参阅**如何使用几何图形**。

6.  如果所选程序配置为在注册期间显示第一阶段，则必须填写该阶段中的所有必填字段。在该阶段结束时，还会询问您是否要完成已为其输入数据的阶段. 如果您选择**是**，则该阶段将在保存后处于完成状态。如果您选择 **No**，舞台将处于活动状态。

7.  如果配置了搜索程序，将对可搜索字段执行后台搜索，以帮助您防止注册重复。如果有任何匹配的 TEI，表格右侧将显示一个蓝色框，可以查看这些匹配的 TEI。

![](resources/images/tracker_capture/tracker_capture_register_integrated_search.png)

If there is any matching TEIs, click **Continue** to review possible duplicates before registering a new one.

If there is no matching TEIs, click **Save and continue** or **Save and add new**

-   **保存并继续**：完成注册并打开注册的 TEI 的仪表板

-   **保存并添加新的**：完成注册但停留在同一页面上。如果您想在不输入数据的情况下一个接一个地注册和注册 TEI，请使用此选项。

> 注意：必须填写所有必填属性才能保存。强制属性在属性标签旁边用红星标记。如果用户拥有名为**“忽略跟踪器和事件捕获中必填字段的验证”**的权限，则不需要填写必填属性，也不会看到属性标签旁边的红星。请注意，拥有 **"ALL"** 权限的超级用户自动拥有此权限。

## 打开现有的TEI仪表板 { #open_existing_tracked_entity_instance_dashboard }

有多种方法可以找到 TEI：使用“列表”
当前选择中的预定义列表，或“搜索”全局
抬头。

### 清单 { #simple_tracked_entity_instance_search }

列表用于查找和显示所选组织单位中的 TEI
和程序。

1.  打开跟踪的捕获应用程序

2.  在左侧窗格的组织单位树中，选择一个组织单位

3.  选择一个程序

4.  如果尚未选择，请单击“列表”按钮

如果未配置，则一组预定义列表将可用：

1.  具有任何注册状态的任何TEI

2.  积极注册当前计划的TEI

3.  已完成当前课程注册的TEI

4.  已取消当前课程注册的TEI

![](resources/images/tracker_capture/tracker_capture_lists.png)

您可以选择在列表中为每个列显示或隐藏哪些列
程序。这将保存在您的用户设置中。

1.  单击**网格**图标按钮

2.  检查您要包括的列

3.  点击**保存**

还可以选择使用自己的方式创建自定义工作列表
过滤器。这可用于动态创建自定义列表。

![](resources/images/tracker_capture/tracker_capture_lists_custom.png)

列表也可以下载或打印。

![](resources/images/tracker_capture/tracker_capture_lists_download.png)

#### 自定义预定义列表 { #custom-predefined-lists }

如果程序有任何与之关联的自定义跟踪实体过滤器，
这些将取代上面提到的四个预定义列表。
预定义列表在配置良好时将成为查找的有效方法
或在该程序中使用与用户相关的数据。

可以使用多种选项定义工作列表，这里有一些
例子：

-   在给定的程序阶段显示至少一个事件的所有TEI
-   截止日期为当前日期。
-   显示至少具有一个分配给该事件的事件的所有TEI
-   登录用户。
-   显示所有活动的但未分配给任何用户的TEI。

![跟踪器捕获中的预定义工作列表](resources/images/tracker_capture/predefined_working_list_based_on_user_assignment.png)

有关支持的功能的完整列表，请参阅 API 文档
这些预定义的跟踪实体实例过滤器。

### 搜索 { #advanced_tracked_entity_instance_search }

搜索用于在用户拥有的组织单位中搜索 TEI
搜索访问。如果您想查找 TEI，这可以使用，但您
不知道 TEI 注册的是哪个组织单位或项目。
有两种方法可以做到这一点：有和没有程序上下文。
需要配置可搜索字段。用于配置搜索
程序上下文，这是针对程序中的每个程序单独完成的
程序维护应用程序。用于在没有程序的情况下配置搜索
上下文中，这是针对每个跟踪的实体类型单独完成的
跟踪实体类型维护应用程序。

**在没有程序上下文的情况下进行搜索：**

1.  打开 **Tracker Capture 应用程序**

2.  点击**搜索**按钮

3.  可搜索的字段将按组显示。唯一属性只能单独搜索。可以组合非唯一属性。

4.  填写搜索条件并点击**搜索**图标按钮。

**在程序上下文中搜索：**

1.  打开 **Tracker Capture 应用程序**

2.  选择具有您要搜索的程序的组织单位

3.  选择程序

4.  点击**搜索**按钮

5.  可搜索的字段将按组显示。唯一属性只能单独搜索。可以组合非唯一属性。

6.  填写搜索条件并点击**搜索**图标按钮

![](resources/images/tracker_capture/tracker_capture_search_screen.png)

搜索完成后，您将看到搜索
结果。显示的内容取决于搜索结果。

对于唯一属性搜索：

-   如果未找到匹配的 TEI，您将可以打开注册表。

-   如果在所选组织单位中找到 TEI，则 TEI 仪表板将自动打开。

-   如果在所选组织单位之外发现 TEI，您将有可能打开 TEI。

对于非唯一属性搜索：

-   如果没有找到匹配的 TEI，您将可以打开注册表。

-   如果找到匹配的 TEI，您可以单击结果列表中的任何 TEI，或打开注册表。

-   如果找到的匹配项过多，系统将提示您优化搜索条件

![](resources/images/tracker_capture/tracker_capture_search_results.png)

搜索结果具有标记跟踪实体实例的功能
尽可能重复，请参阅下一章。

选择打开注册表时，搜索值将
自动填写到注册表中。

### 将跟踪的实体实例标记为潜在重复项 { #flagging-tracked-entity-instance-as-potential-duplicate }

寻找时被追踪实体在追踪器应用程序的实例中，用户有时会选择怀疑一个或多个搜索匹配与其他搜索匹配被追踪的实体实例。用户点击搜索结果追踪中可以列的**标记可能重复**链接。

以这种方式标记的跟踪实体实例将被标记为“可能重复”
在 DHIS2 数据库中。该标志表示被跟踪的实体实例是/具有
复制。用户可以在两个位置看到此类标志的存在。一个是
结果列表本身（在这个例子中，Mark Robinson 已经被标记为潜在的
复制）：

![Tracker 捕获搜索结果](resources/images/tracker_capture/tracker_capture_search_results.png)

另一个位置在跟踪的实体实例仪表板中：

![被跟踪的实体实例标记为重复](resources/images/tracker_capture/tracked_entity_instance_flagged_as_duplicate.png)

除了潜在地通知用户被跟踪的实体实例
作为重复，该标志将被底层系统用于查找和
在即将发布的 DHIS2 版本中合并重复项。

### 打破玻璃 { #break_glass }

如果程序配置了访问级别**protected**，并且用户搜索并找到 被跟踪实体如果用户没有数据捕获权限的组织单位拥有的实例，则向用户提供打破玻璃的选项。用户将给出打破玻璃的原因，然后获得该玻璃的临时所有权被跟踪实体 实例。

## 在程序中注册现有的TEI { #enroll_existing_tracked_entity_instance_in_program }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  选择一个程序。

4.  在**注册**小元件中，点击**添加新**。

5.  填写需要信息，然后点击**注册**。

## 输入TEI的事件数据 { #enter_event_data_for_tracked_entity_instance }

### 数据输入小部件 { #widgets-for-data-entry }

####

在TEI仪表板中，您输入事件**时间线数据输入**或**表格数据输入**小元件中的数据。

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

### 建立活动 { #creating-an-event }

您可以通过以下方式为TEI创建事件：

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在 **时间线数据条目** 或 **表格数据条目** 小部件中，单击 **+** 按钮。

4.  选择 **Programstage** 并设置 **Report date**。

    程序阶段可以配置为使用功能类型。这使得捕获事件的几何图形成为可能。支持的要素类型是点和多边形。请参阅**如何使用几何图形**。

5.  点击**保存**。 

### 安排活动 { #schedule-an-event }

您可以通过以下方式取消事件的将来日期：

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在**时间线数据条目** 或**表格数据条目** 小部件中，单击**日历** 图标。

4.  选择 **Programstage** 并设置 **Schedule date**。

5.  点击**保存**。 

### 推荐活动 { #refer-an-event }

有时，将患者转诊至不同的**组织单位** 可能会令人感到害怕。要引用 TEI：

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在 **时间轴数据条目** 或 **表格数据条目** 小部件中，单击 **箭头** 图标。

4.  选择**节目阶段**、**组织单位**并设置\***\*报告日期\*\***。

5.  点击任一**一次性推荐**，这将只推荐一个单一的 TEI 事件或**永久移动**，这会将 TEI 所有权移至选定的**组织单位**。对 TEI 的进一步访问将基于所有权组织单位。

### 事件中的强制数据元素 { #mandatory-data-elements-in-events }

事件中的某些数据元素可能是强制性的（在数据元素标签旁边用红星标记）。这意味着在允许用户完成事件之前，必须填写所有必需的数据元素。例外情况是，如果用户拥有名为**“忽略跟踪器和事件捕获中的必填字段的验证”的权限。** 如果用户拥有此权限，则在保存之前不需要填写必填数据元素并且红色星号不会显示在数据元素标签旁边。请注意，拥有 **"ALL"** 权限的超级用户自动拥有此权限。

## 如何使用几何 { #how-to-use-geometry }

跟踪实体类型、程序和程序阶段可以配置为
使用特征类型。这使得捕获几何图形成为可能
TEI、计划或活动。支持的特征类型是点和多边形。

### 捕捉坐标 { #capture-coordinate }

**选项1：**在字段中填写纬度和经度。

**选项2：**

1.  点击**地图图标**
2.  通过搜索或在地图上找到您想要的位置
3.  详细您的目的的位置，然后选择**设置坐标**
4.  点击底部的**捕获**

### 捕捉多边形 { #capture-polygon }

1.  点击**地图图标**
2.  通过搜索或在地图上找到您想要的位置
3.  在地图左上角，点击**多边形图标**
4.  在地图上画一个多边形。最后，将最后一个点与第一个点连接起来
5.  点击底部的**捕获**

![](resources/images/tracker_capture/capture_geometry.png)

多边形也可以删除

1.  点击**地图图标**
2.  点击地图左侧的**垃圾桶图标**，然后选择**全部清除**

## 如何为事件分配用户 { #how-to-assign-a-user-to-an-event }

在维护应用程序中，可以配置程序阶段以允许用户分配。
如果启用了用户分配，您将能够为事件分配用户。

1. 单击**分配的用户** 字段。
2. 滚动或搜索用户。
3. 单击用户。

## 管理TEI的注册 { #manage_tracked_entity_instance_enrollment }

注册小部件提供对信息和功能的访问
用于注册所选课程。

![注册小部件](resources/images/tracker_capture/enrollment_widget.png)

### TEI 所有权 { #tei-ownership }

显示所选程序中所有注册的当前所有权
在注册小部件的“所有者”部分中。所有权将始终开始
作为首先将 TEI 注册到给定计划的组织单位。

TEIS 不同项目的所有权可能不同，例如一个诊所可以
对 HIV 患者进行随访，而另一家诊所则对 MCH 中的同一患者进行随访。

要更新 TEI/程序组合的所有权，用户必须使用
推荐功能并在推荐时选择“永久移动”选项。

对作为当前所有者的组织单位具有捕获访问权限的用户
TEI/计划将拥有对该 TEI/计划组合的所有注册的写访问权限。
对作为当前所有者的组织单位具有搜索权限的用户将拥有
访问搜索和查找 TEI/程序组合。

### 停用TEI的注册 { #deactivate_tracked_entity_instance_enrollment }

如果您停用 TEI 仪表板，TEI 将变为“只读”。你
无法输入数据、注册 TEI 或编辑 TEI 的配置文件。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在里面**注册**小点，点击**手指**。

4.  单击**是**进行确认。

### 激活TEI的注册 { #activate_tracked_entity_instance_enrollment }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **激活**。

4.  单击**是**进行确认。

### 将TEI的注册标记为已完成 { #mark_tracked_entity_instance_enrollment_complete }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **完成**。

4.  单击**是**进行确认。

### 重新打开已完成的注册 { #reopen_complete_tracked_entity_instance_enrollment }

如果注册已完成，则可以重新开放该计划的注册。但是，如果同一计划中正在进行另一个有效注册，则无法重新开放注册（因为如果该计划已存在另一个有效注册，则您无法注册该计划）。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在里面**注册**小点，点击**打开**。

4.  单击**是**进行确认。

### 显示TEI的注册历史 { #display_tracked_entity_instance_enrollment_history }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在**Profile**小元件中，点击**Audit history**图标。

### 创建TEI注册说明 { #create_tracked_entity_instance_enrollment_note }

注册说明可用于记录有关例如原因的信息
取消了注册。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在** Notes **小部件中，键入您的注释，然后单击** Add **。

## 发信息给TEI { #send_message_to_tracked_entity_instance }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在 **Messaging** 小部件中并选择 **SMS** 或 **E-mail**。

4.  输入所需的联系信息。

    如果 TEI 的个人资料包含电子邮件地址或电话号码，则会自动填写这些字段。

5.  键入一条消息。

6.  点击**发送**。

## 将TEI标记为后续 { #mark_tracked_entity_instance_for_follow_up }

您可以使用标记 TEI 注册用于跟进，然后在您创建 **即将发生的事件** 和 **过期事件** 报告时将此状态用作过滤器。例如，这对于在怀孕计划期间监测高风险病例非常有用。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在里面 **注册** 小部件，单击 **标记为跟进** 图标。

## 编辑TEI的个人资料 { #edit_tracked_entity_instance_profile }

您编辑 TEI 的个人资料或 被跟踪实体 **Profile** 小部件中的属性。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在 **Profile** 小部件中，单击 **Edit**。

4.  修改配置文件并单击**保存**。

## 将关系添加到TEI { #add_relationship_to_tracked_entity_instance }

例如，您可以创建从一个 TEI 到另一个 TEI 的关系
将母亲和孩子或丈夫和妻子联系在一起。依赖
关于如何配置关系类型，亲属可以继承
属性。

假设有两个项目：母亲的产前护理和
为孩子接种疫苗。如果名字、姓氏和地址
两个程序都需要属性，可以配置
姓氏和地址属性是可继承的。然后在孩子期间
注册，不需要输入这些可继承的属性。
您可以根据母亲的值自动添加它们。如果你想
要为孩子设置不同的值，您可以覆盖
自动生成的值。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在**关系** 小部件中，单击**添加**。

4.  选择一种关系类型。

5.  搜索亲戚并选择它。搜索遵循与从跟踪器首页搜索被跟踪实体实例时相同的模式。默认情况下，搜索覆盖用户的搜索范围。

6.  在弹出窗口中选择与搜索条件匹配的跟踪实体实例。

7.  点击**保存**。 

> 注意：如果关系是双向关系，则该关系将显示在创建该关系的 TEI 和该关系链接到的 TEI 中。此外，如果关系是双向的，则关系的每一端都有一个唯一的名称，该名称将显示在“关系”列下的关系小部件中。

## 共享TEI仪表板 { #share_tracked_entity_instance_dashboard }

您可以通过其网址共享TEI仪表板。

1.  打开 **随访采集** 应用程序。

2.  打开您要共享的仪表板。

3.  复制URL。

    确保 URL 包含“tei”、“program”和“ou”（组织单位）参数。

4.  将 URL 粘贴到您选择的共享方法中，例如 DHIS2 中的电子邮件或消息。

    如果您在单击链接时未登录 DHIS2，系统会要求您登录，然后转到仪表板。

## 停用TEI { #deactivate_tracked_entity_instance }

如果您停用某个 TEI，该 TEI 将变为“只读”。相关数据
与 TEI 不删除。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在右上角，单击 ![](resources/images/tracker_capture/tc_tei_red_icon.png) 按钮 \> **Deactivate**。

4.  单击**是**进行确认。

## 激活TEI { #activate_tracked_entity_instance }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在右上角，单击 ![](resources/images/tracker_capture/tc_tei_red_icon.png) 按钮 \> **Activate**。

4.  单击**是**进行确认。

## 删除TEI { #delete_tracked_entity_instance }

> **警告**
>
>删除TEI时，将删除与TEI相关的所有数据。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  在右上角，单击 ![](resources/images/tracker_capture/tc_tei_red_icon.png) 按钮 \> **Delete**。

4.  单击**是**进行确认。

## 配置TEI仪表板 { #configure_tracked_entity_instance_dashboard }

### 显示或隐藏小部件 { #tracked_entity_instance_dashboard_show_hide_widget }

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置** 图标，然后选择**显示/隐藏小部件**。

4.  选择要显示或隐藏的小部件。

5.  点击**关闭**。

### 将仪表板的布局保存为默认布局 { #tracked_entity_instance_dashboard_save_layout }

您可以将仪表板的布局保存为程序的默认设置。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置**图标，然后选择**保存仪表板 布局 默认**。

### 锁定仪表板的布局 { #lock-dashboards-layout }

如果您是**管理员**，您可以选择锁定 布局 所有用户的仪表板。

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  将小部件组织到所需的布局并将其保存为默认布局（请参阅上面的部分）。

4.  单击**设置**图标，然后选择**锁定 布局 对于所有用户**。

用户仍然可以暂时重新组织小部件，但
页面刷新后，布局将重置为管理员保存的布局。这
当仪表板布局为时，删除小部件按钮将被隐藏
锁定。

### 顶栏 { #top-bar }

顶部栏是一个有用的工具，可以快速查看重要数据。
简单的方法。要开始使用顶部栏：

1.  打开 **随访采集** 应用程序。

2.  打开现有的TEI仪表板。

3.  单击**设置**图标，然后选择**顶栏设置**。

4.  单击 **Activate top bar** 并单击要在顶部栏中显示的数据。

![](resources/images/tracker_capture/top_bar.png)

### 更改 **时间线数据输入** 小部件 { #change-table-display-mode-for-timeline-data-entry-widget } 的表格显示模式 { #change-table-display-mode-for-timeline-data-entry-widget }

**时间线数据输入**小控件有5种不同的表格模式选择。不同的选项是：

-   **默认格式**-垂直显示所有数据元素。

-   **比较之前的表格**-在当前选定的程序阶段旁边显示prevoius（可重复）程序阶段。

-   **全部比较表格**-在当前所选程序阶段旁边显示所有prevoius（可重复）程序阶段。

-   **网格形式**-水平显示数据元素。

-   ** POP表单**-与** Grid表单**相同，但是单击时，数据元素将显示在弹出窗口中。

要更改当前的显示模式，请单击小部件顶部栏中的第二个图标（请参见下图）：

![](resources/images/tracker_capture/compareForm.png)

一旦选择了一个选项，该选择将存储在该特殊程序阶段。这意味着您可以为程序中的不同程序阶段使用不同的表模式。

> **注意事项：**
>
> 1. _The **Compare 形式** 如果您有多个可重复事件（同一程序阶段），选项将发挥最佳作用。_
> 2. _The **Grid 形式** 和 **POP-over 形式** 如果程序阶段有超过 10 个数据元素，则选项不可选。_
> 3. _小部件栏中的图标将根据您选择的选项而变化。_

## 建立报告 { #create_report_tracker_capture }

1.  打开 **随访采集** 应用程序。

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

摘要报告显示 TEI 列表及其记录
“MNCH/PNC（成年女性）”计划。记录按以下形式组织
选项卡，其中每个选项卡是一个程序阶段。表中的列是
配置为显示在报告中的数据元素
程序阶段定义。

# 数据审批 { #data_approval }

DHIS2 有一个可选功能，允许授权用户批准
输入的数据。它允许审查和批准数据
在组织单位层次结构中的选定级别，因此批准
遵循从低到高的层次结构
水平。

数据被批准用于 (a) 期间、(b) 组织单位的组合
(c) 工作流程。可以为组织单位批准数据
它被输入，以及为更高级别的组织单位
数据是聚合的。作为系统设置的一部分，您可以选择
批准数据的组织单位级别。有可能
只有在所有这些都得到批准后才能在更高级别上批准
同一工作流的较低级别的组织单位的后代
和时期。当您批准工作流程时，它会批准任何数据的数据
已分配给该工作流的集合。

一段时间后，组织单元和工作流组合已经
批准后，与该工作流关联的数据集将被锁定
那个时期和组织单位，以及任何进一步的数据输入或
除非首先未经批准，否则将禁止修改。

例如，下图说明数据已经
已批准用于组织单位 C 和 D，在特定时期内，并且
工作流程。现在可以为组织单位 B 批准相同的
期间和工作流程。但它还没有准备好被组织批准
单元 A。在它被批准为组织单元 A 之前，它必须是
批准用于 B，以及组织单元 A 的任何其他子级，用于
那个时期和工作流程。

![组织批准
单位](resources/images/data_approval/approval_hierarchy.png){.center width=50% }

## 批准并接受 { #data_approvals_approving_accepting }

DHIS2 支持两种不同类型的审批流程：
在每个级别批准数据的一步过程，或两步
数据首先被批准然后在每个级别被接受的过程。
如下图所示：

![批准和
接受](resources/images/data_approval/approval_level_steps.png){.center width=69% }

在一步流程中，数据经过一级审批，然后
上一级批准。直到下次批准
更高级别，可能在第一级未获批准。 （例如，如果
数据被批准我的错误，这允许批准者撤消他们的
错误。）一旦数据被上一级批准，它可能不会
除非在下一级未经批准，否则不得在较低级别获得批准
更高层次。

In the two-step process, data is approved at one level, and then the approval is accepted at the same level. This acceptance is done by a user who is authorized to approve data at the next higher level. Once the data is accepted, it may not be changed or unapproved unless it is first _unaccepted_.

DHIS2 不需要两步过程。这是一个可选步骤
供用户查看下一个更高级别的数据。它有好处
从下面的级别锁定接受，因此审稿人不会
必须担心数据可能会从下面发生变化
正在审核中。它也可以被更高级别的用户用来保持
跟踪哪些较低级别的数据已被审查。

Two-step process can be activated by checking **Acceptance required before approval** in SystemSettings app under General section.

## 数据审批机关 { #data_approvals_authorities }

要批准数据，您必须被分配一个包含以下其中一项的角色
当局：

-   **批准数据** - 您可以批准分配给您的组织单位的数据。请注意，此权限不允许您批准您被分配到的组织单位以下较低级别的数据。这有助于将授权在一级批准的用户与授权在下一级批准的用户分开。

-   **批准较低级别的数据** - 允许您批准分配给您的组织单位以下所有较低级别的数据。例如，如果您是区级用户，其角色包括批准该区内所有设施的数据，但不批准该区本身的数据，这将非常有用。如果您被分配了此权限以及_批准数据_权限，您可以在您被分配到的组织单位级别以及以下任何级别批准数据。

-   **接受较低级别的数据** - 允许您接受仅低于分配给您的组织单位的级别的数据。此权限可以授予与批准数据相同的用户。或者，如果您希望有一些用户接受来自下一层的数据，以及批准数据进入上一层的不同用户集，则它可能会分配给不同的用户。

## 配置数据批准 { #data_approvals_configuration }

在_数据审批级别_下的_维护应用程序_部分中，您可以指定要在系统中审批数据的级别。单击此页面上的添加新按钮，然后选择您想要批准的组织单位级别。它将被添加到批准设置列表中。您可以将系统配置为在每个组织单位级别或仅在选定的组织单位级别批准数据。

请注意，当您添加新的批准级别时，您可以选择一个
类别选项组集。此功能将在本文后面讨论
章节。

Also in maintenance under _Data approval workflow_, you can define the workflows that will be used for approving data. Each workflow can be associated with one or more approval levels. Any two workflows may operate at all the same approval levels as each other, some of the same and some different levels, or completely different levels.

如果您希望根据工作流程批准数据集的数据，
然后在添加或编辑数据时将工作流分配给数据集
放。如果您不希望某个数据集的数据受到批准，
然后不要为该数据集分配任何工作流程。对于您的数据集
想同时审批，分配给同一个
工作流程。对于要独立审批的数据集，分配
每个数据集到自己的工作流程。

在_系统设置_ -> _分析_下，您可以控制哪些未经批准的数据（如果有）将出现在分析中。请参阅本用户指南的“分析设置”部分。请注意，分配到数据已准备好待批准的组织单位的用户始终可以在分析中查看此数据，如果分配到更高级别的组织单位的用户具有_批准较低级别的数据_权限或_查看未批准的数据_权限，他们也可以查看此数据。

## 数据可视性 { #data_approvals_data_visibility }

If the option _Hide unapproved data in analytics_ is enabled, data will be hidden from viewing by users associated with higher levels. When determining whether a data record should be hidden for a specific user, the system associates a user with a specific approval level and compares it to the level to which the data record has been approved up to. A user is associated with the approval level which matches the level of the organisation unit(s) she is linked to, or if no approvel level exists at that level, the next approval level linked to an organisation unit level below herself. A user will be allowed to see data which has been approved up to the level immediately below her associated approval level. The rationale behind this is that a user must be ablet to view the data that has been approved below so that she can eventually view and approve it herself.

请注意，如果用户被授予_查看未批准的数据_或_ALL_权限，她将能够查看数据而不管批准状态如何。

_让我们考虑以下示例：_ 有四个组织单位级别，审批级别与级别 2 和 4 相关联。国家级别 (1) 的_用户 A_ 与审批级别 1 相关联，因为审批级别与组织处于同一级别单位级别。 _用户 B_ 与批准级别 2 相关联，因为没有直接链接到她的组织单位级别的批准级别，而批准级别 2 是下面的直接级别。 _用户 C_ 与批准级别 2 相关联。_用户 D_ 低于所有批准级别，这意味着她可以看到在她的组织单位级别或低于她的组织单位级别输入的所有数据。

![隐藏未经批准的
数据](resources/images/data_approval/approval_data_hiding.png){.center}

使用此示例，让我们考虑一些方案：

-   在设施级别输入数据：只有_用户 D_ 可以看到数据，因为数据还没有被批准。

-   数据由_用户 D_ 在设施级别批准：数据对用户 C 和用户 B 可见，因为数据现在在他们的级别获得批准。

-   数据在地区级别由_用户 C_ 批准：数据对用户 A 可见，因为数据现在在她自己下面的级别获得批准。

## 批准数据 { #data_approvals_approving_data }

要批准数据，请转到 _Reports_ 并选择 _Data Approval_。当此报表显示配置为审批的数据时，它会显示报表中数据的审批状态。批准状态将是以下之一：

-   **等待较低级别的组织单位批准** - 此数据尚未准备好批准，因为它首先需要为该组织单位的所有子组织单位批准，用于相同的工作流和时间段。

-   **准备批准** - 此数据现在可以由授权用户批准。

-   **已批准**-此数据已被批准。

-   **已批准并接受** - 此数据已获得批准，也已接受。

如果您正在查看的数据处于可以采取行动的批准状态，并且如果您有足够的权限，您可以在_数据批准_表单上执行以下一项或多项操作：

-   **Approve** - 批准尚未批准的数据，或以前批准但未批准的数据。

-   **未批准** - 返回已批准或接受的未批准状态数据。

-   **接受**-接受已批准的数据。

-   **Unaccept** - 返回已接受的未接受（但仍批准）状态数据。

要取消批准给定单位部门的数据，您必须拥有
批准该组织单位的数据或批准
数据所属的更高级别组织单位的数据
汇总。其原因如下： 如果您正在查看数据
要获得更高组织单位级别的批准，您应该考虑
下级组织单位的数据是否合理。我摔倒
下级数据看起来不错，可以在上级批准数据
等级。如果某些较低级别的数据看起来可疑，您可以取消批准
较低级别的数据。这允许在以下位置再次查看数据
下级，必要时更正，并通过审核重新批准
根据层次结构划分的组织单位级别。

## 按类别选项组批准 { #data_approvals_approving_by_cogs }

定义审批级别时，指定组织单位级别
届时将批准数据。您还可以选择指定一个
类别选项组集。如果您使用类别，这很有用
选项组来定义数据的其他维度，并且您想要
批准基于这些尺寸。下面的例子
说明如何在单个类别选项组中完成此操作
集，并通过使用多个类别选项组集。

### 按一个类别选项组集批准 { #approving-by-one-category-option-group-set }

例如，假设您定义了一个类别选项组集来表示
在一个或多个组织单位担任医疗保健合作伙伴的非政府组织。
此集合中的每个类别选项组代表一个不同的
伙伴。合作伙伴 1 的类别选项组可以组合在一起
使用的类别选项（例如资金帐户代码）
合作伙伴作为数据的一个维度。所以合作伙伴 1 输入的数据是
归因于合作伙伴 1 的类别选项组中的类别选项。
而合作伙伴 2 输入的数据归因于
合作伙伴 2 的类别选项组：

<table align="center">
<caption>Example Category Option Groups</caption>
<thead>
<tr class="header">
<th>Category option group set</th>
<th>Category option group</th>
<th>Category options</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Partner</td>
<td>Partner 1</td>
<td>Account 1A, Account 1B</td>
</tr>
<tr class="even">
<td>Partner</td>
<td>Partner 2</td>
<td>Account 2A, Account 2B</td>
</tr>
</tbody>
</table>

每个合作伙伴都可以独立于他们的帐户输入数据
其他，对于相同或不同的工作流程，相同或不同
设施。例如，数据可以在
每个合作伙伴的以下级别，彼此独立：

![示例类别选项
组](resources/images/data_approval/approval_partner_example.png){.center}

> **提示**
>
> 您可以使用类别选项和类别选项组的共享功能，以确保用户只能为某些类别选项和组输入数据（和/或查看数据）。如果您不希望用户看到超出其分配的类别选项和/或类别选项组的数据，您可以在添加或更新用户时分配_用于数据分析的选定维度限制_。

您可以选择在任何或
所有这些组织单位级别。例如，您可以定义任何
或以下所有批准级别：

 <table align="center">
 <caption> 示例类别选项组 设置批准级别 </caption>
 <thead>
 <tr class="header">
 <th> 批准级别 </th>
 <th> 组织单位级别 </th>
 <th> 类别选项组设置 </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> 1 </td>
 <td> 国家 </td>
 <td> 合作伙伴 </td>
 </tr>
 <tr class="even">
 <td> 2 </td>
 <td> 区 </td>
 <td> 合作伙伴 </td>
 </tr>
 <tr class="odd">
 <td> 3 </td>
 <td> 设施 </td>
 <td> 合作伙伴 </td>
 </tr>
 </tbody>
 </table>

## 通过多个类别选项组集批准 { #approving_by_multiple_category_option_group_sets }

您还可以为不同的类别选项组定义批准级别
套。继续这个例子，假设你有不同的机构
管理向不同合作伙伴提供的资金。例如，机构 A
资金账户 1A 和 2A，而机构 B 资金账户 1B 和 2B。你
可以为机构 A 和机构 B 设置类别选项组，并使
它们都是名为 Agency 的类别选项组集的一部分。那么你
将有：

<table align="center">
<caption>Example Multiple Category Option Group Sets</caption>
<thead>
<tr class="header">
<th>Category option group set</th>
<th>Category option group</th>
<th>Category options</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Partner</td>
<td>Partner 1</td>
<td>Account 1A, Account 1B</td>
</tr>
<tr class="even">
<td>Partner</td>
<td>Partner 2</td>
<td>Account 2A, Account 2B</td>
</tr>
<tr class="odd">
<td>Agency</td>
<td>Agency A</td>
<td>Account 1A, Account 2A</td>
</tr>
<tr class="even">
<td>Agency</td>
<td>Agency B</td>
<td>Account 1B, Account 2B</td>
</tr>
</tbody>
</table>

现在假设在国家/地区级别，您希望每个合作伙伴批准
该合作伙伴输入的数据。完成此批准后，您需要
每个机构然后批准来自由管理的帐户的数据
那个机构。最后，您要批准国家/地区级别的数据
跨越所有机构。您可以通过定义以下内容来做到这一点
审批级别：

<table align="center">
<caption>Example Multiple Category Option Group Set approval levels</caption>
<thead>
<tr class="header">
<th>Approval level</th>
<th>Organisation unit level</th>
<th>Category option group set</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Country</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>Country</td>
<td>Agency</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Country</td>
<td>Partner</td>
</tr>
</tbody>
</table>

请注意，可以为相同的权限定义多个审批级别
组织单位层面。在我们的示例中，合作伙伴 1 将批准
来自类别选项账户 1A 的批准级别 3 的全国数据
和账户 1B。接下来，A 机构将批准全国范围的数据
类别选项帐户 1A 中的批准级别 2（经批准后
合作伙伴 1) 和账户 2A（经合作伙伴 2 批准后。）最后，在
获得所有机构的批准，全国范围的数据可以在
所有类别选项的批准级别为 1。请注意，批准级别 1
不指定类别选项组集，这意味着它用于
批准所有类别选项的数据。

此示例仅用于说明。你可以定义尽可能多的
您需要的类别选项组，以及尽可能多的审批级别
不同类别选项需要在同一组织单位级别
组套。

如果您对同一组织单位级别的不同类别选项组集有多个审批级别，您可以在_系统审批设置_下的_设置_部分更改审批顺序。只需单击您要移动的批准级别，然后选择_Move up_ 或_Move down_。如果您的审批级别未设置类别选项组，则它必须是该组织单位级别的最高审批级别。

# 管理仪表板 { #dashboard }

## 关于仪表盘 { #about-dashboards }

仪表板旨在提供对不同分析的快速访问
对象（地图、图表、报告、表格等）给单个用户。
仪表板可以与用户组共享。仪表板也可以打印。

用户或管理员可以创建一个名为“产前保健”的仪表板
其中可能包含有关产前保健的所有相关信息。这
然后可以与名为“ANC 控制”的用户组共享仪表板，
可能包括 ANC 控制程序的所有用户。所有用户
然后，该组内将能够查看相同的仪表板。

## 仪表板和控制栏 { #dashboards_setup }

仪表板具有标题、描述和任意数量的仪表板项目。
仪表板项目可以是许多不同的类型，包括图表、
地图、报告、表格、资源、消息和文本项目。以上
仪表板是控制栏，显示所有可用的仪表板，
包括一个仪表板搜索字段和一个 **+** 按钮，用于创建一个
新仪表板。

仪表板有两种模式：查看和编辑/创建。第一次登录时
到 DHIS2，您最近使用的仪表板将显示在视图中
模式，如果您与之前在同一台计算机上。如果你是
使用不同的计算机，那么第一个加星标的仪表板将是
显示。如果没有加星标的仪表板，则是第一个仪表板（按字母顺序）
将显示。已加星标的仪表板始终首先显示在仪表板中
列表。

下面的屏幕截图显示了一个名为“产前护理”的仪表板，其中
已经填充了图表和地图。

![](resources/images/dashboard/dashboard-view-mode.png)

### 小屏幕上的响应视图 { #responsive-view-on-small-screens }

在小屏幕（例如手机竖屏）上查看仪表盘时，仪表盘会适应屏幕并在单列中显示所有项目。某些选项（包括编辑、过滤和共享）将不可用。

![](resources/images/dashboard/dashboard-small-screen.png)

### 在仪表板列表中搜索 { #searching-in-the-list-of-dashboards }

您可以使用搜索栏中的搜索字段搜索特定仪表板
标题为“搜索仪表板”的控制栏左上角。这
搜索不区分大小写，当您键入时，仪表板列表将
过滤到与您的搜索文本匹配的那些。

### 自定义控制栏的高度 { #customizing-the-height-of-the-control-bar }

您可以通过右键单击并拖动控制栏的底部边缘来为仪表板控制栏设置特定的高度。完成拖动后，将设置新的高度。单击**显示更多**，将控制栏扩展到最大高度（10个“”行”）。单击**显示较少 **会将高度重置为您自定义的高度。

## 创建仪表板 { #creating-a-dashboard }

要创建新仪表板，请单击左侧的绿色 **+** 按钮
控制栏的一角进入创建模式。在标题中添加
标题字段，以及可选的描述字段中的描述。如果您不添加标题，仪表板将自动命名为“未命名仪表板”。

![](resources/images/dashboard/dashboard-add-new.png)

**创建模式：**

![](resources/images/dashboard/dashboard-create-mode.png)

### 将项目添加到仪表板 { #adding-items-to-the-dashboard }

通过从项目选择器中的搜索添加项目到仪表板
仪表板区域的右上角。可用项目包括：

-   可视化

-   地图

-   活动报告

-   活动图

-   报告

-   资源资源

-   应用

-   电子邮件

-   文字框

-   垫片

根据您输入的搜索文本，下拉列表中的项目列表最初显示10个可视化效果（图表和表格），以及其他每个类别中的5个。在下拉菜单中还可以找到电子邮件，文本框和分隔符项目。要查看更多项目，请单击**显示更多**，该类型的列表将扩展为25个项目。如果仍然找不到所需的项目，请尝试输入更具体的搜索文本。

![](resources/images/dashboard/dashboard-item-selector.png)

一旦您选择了一个项目，它将被添加到左上角的位置
仪表板。添加的项目可以使用鼠标移动
向下单击该项目并将其拖动到所需位置。它
也可以通过向下单击拖动手柄来使用鼠标调整大小
并拖动到所需大小。

#### 垫片项目 { #spacer-items }

仪表板配置了“反重力”设置
定位项。这意味着项目将“上升”直到它们
遇到另一个项目。为了强制空的垂直空间之间
项（如空行），您可以向仪表板添加间隔项。
它们仅在编辑/创建模式下可见。在查看模式下，它们不是
显示，但占用定义的空间。

**编辑/创建模式**中的空格：

![](resources/images/dashboard/dashboard-spacer-edit-mode.png)

**查看模式下的垫片**：

![](resources/images/dashboard/dashboard-spacer-view-mode.png)

### 移除物品 { #removing-items }

单击右上角的红色垃圾桶删除项目
物品。请注意，由于“反重力”设置
仪表板，当您删除一个项目时，位于下方的项目
被移除的物品将向上“升起”。

### 打印预览 { #print-preview }

单击**打印预览**按钮，以查看仪表板在仪表板布局打印中的外观。

![](resources/images/dashboard/dashboard-edit-print-preview.png)

单击**退出打印预览**以返回到编辑仪表板。

请注意，某些项目可能会向下移动以避免分页符。项目也可能会缩短以适合一页。缩短的项目在预览的右上角显示一个信息图标。该图标在实际打印中被删除。

### 限制仪表板过滤器 { #restricting-dashboard-filters }

默认情况下，用户将能够按系统中定义的任何维度过滤仪表板项目。通过单击**过滤器设置**，可以为给定的仪表板编辑仪表板过滤器设置。

![](resources/images/dashboard/dashboard-filter-settings-button.png)

要限制可用过滤器，您可以单击**仅允许按选定维度过滤**，然后在仪表板上选择您希望允许的过滤器。当仪表板处于查看模式时，用户将只能从选定的过滤器中进行选择。默认情况下将选择期间和组织单位，但可以根据需要删除。

![](resources/images/dashboard/dashboard-filter-settings.png)

为了保存对过滤器设置的更新，您需要先点击 **Confirm** 关闭过滤器设置，然后点击 **Save changes** 保存仪表板更改。

### 保存仪表板 { #saving-the-dashboard }

创建或编辑仪表板时，仅在单击页面顶部的仪表板编辑栏中的**保存更改**按钮时才保存更改。如果您不想保存所做的更改，请单击右上角的**不保存退出**按钮。然后，您将使用之前查看的仪表板返回查看模式。

## 编辑现有的仪表板 { #editing-an-existing-dashboard }

如果您有权编辑当前活动的仪表板，则在查看模式下，仪表板标题的右侧将有一个**编辑**按钮。单击此按钮进入编辑模式。

![](resources/images/dashboard/dashboard-title-bar.png)

有关创建仪表板的信息，请参阅上述部分
向仪表板添加和删除项目。

![](resources/images/dashboard/dashboard-edit-mode.png)

### 翻译仪表板标题和描述 { #translating-dashboard-title-and-description }

您可以在仪表板标题和描述中添加翻译
编辑模式。该对话框提供了要翻译成的语言列表，以及
在名称输入字段下方显示原始仪表板标题。

![](resources/images/dashboard/dashboard-translation-dialog.png)

1.  点击位于仪表盘上方的**翻译**按钮

2.  选择您要为其添加翻译的语言。

3.  添加标题和/或描述，然后单击**保存**

## 删除仪表板 { #deleting-a-dashboard }

如果您有权删除仪表板，则在编辑模式下，仪表板上方将有一个**删除**按钮。首先将显示一个确认对话框，以确认您要删除仪表板。

## 查看仪表板 { #viewing-a-dashboard }

在查看模式下，您可以切换显示说明，为仪表板加注星标，应用过滤器，打印仪表板以及与其他用户和组共享仪表板。

### 显示说明 { #show-description }

要切换说明，请点击** ...更多**按钮，然后选择**显示说明**（或**隐藏说明**）。您打开的所有仪表板都会记住该设置。此设置适用于您，不适用于其他用户。

![](resources/images/dashboard/dashboard-title-bar-show-description.png)

### 已加星标的仪表板 { #starred-dashboards }

已加星标的仪表板首先列在仪表板列表中。至
为仪表板加星标，单击标题右侧的星标按钮。您还可以从 **...更多** 菜单切换星号。
当星号为“填充”时，表示仪表板已加星标。主演
仪表板仅适用于您，不适用于其他用户。

### 筛选仪表板 { #filtering-a-dashboard }

可以将多个过滤器应用于仪表板以更改数据
显示在各种仪表板项目中。
过滤器以相同的方式应用于每个仪表板项目：
每个添加的过滤器都会覆盖该维度的原始值
原始图表、表格或地图（可视化）。
可以过滤组织单位、期间和其他
动态维度取决于 DHIS2 实例。

要添加过滤器，请点击**添加过滤器**按钮，然后选择尺寸：

![添加过滤器](resources/images/dashboard/dashboard-filters.png)

将打开一个对话框，您可以在其中选择过滤器。

![组织单位过滤器选择](resources/images/dashboard/dashboard-orgunit-filter-dialog.png)

在对话框中单击**确认**，以将过滤器应用于当前仪表板。

过滤器不会被存储，所以当切换到不同的仪表板时，它们
丢失了。
筛选器徽章显示在仪表板项目上方以
指示仪表板项目中显示的内容不是原始内容
可视化，但过滤器覆盖的操纵
存储维度的值。

![当前过滤器显示为仪表板上方的标志](resources/images/dashboard/dashboard-filter-badges.png)

可以单击过滤器标记以打开过滤器选择对话框，从而可以进行过滤器编辑。通过单击徽章中的**删除**按钮，可以删除过滤器。每当添加，编辑或删除过滤器时，仪表板项目都会重新加载以显示更新的数据。滚动仪表板内容时，过滤器徽标始终在页面顶部可见。

默认情况下，用户可以按系统中定义的任何维度过滤仪表板项目。要限制可用的过滤器，请参阅[限制仪表板过滤器](#restricting-dashboard-filters)。

### 打印仪表板 { #printing-a-dashboard }

从** ...更多**菜单中，您可以打印活动的仪表板。仪表板打印有两种样式：仪表板布局和每页一项。对于这两种样式，将添加一个标题页，以显示仪表板标题，描述（如果启用了“显示描述”设置）以及所有应用的仪表板过滤器。

![](resources/images/dashboard/dashboard-print-menu.png)

为了获得最佳打印效果：

-   使用Chrome或Edge
-   等到所有仪表板项目都已加载后再打印
-   使用具有默认边距的A4横向设置

#### 打印仪表板布局 { #print-dashboard-layout }

仪表板布局打印将近似显示在浏览器中的仪表板布局。请注意，可能需要对布局进行一些调整以避免分页符：某些项目的位置可能会向下调整，而高于一页的项目则会缩短。

单击右上角的**打印**按钮以触发浏览器打印功能。

![](resources/images/dashboard/dashboard-print-layout.png)

#### 每页打印一项 { #print-one-item-per-page }

这种打印样式会将每个仪表板项目打印在单独的页面上，从而最大程度地利用纸张。

单击右上角的**打印**按钮以触发浏览器打印功能。

![](resources/images/dashboard/dashboard-print-oipp.png)

## 带有图表、数据透视表或地图的仪表板项目 { #dashboard-items-with-charts-pivot-tables-or-maps }

带有图表、数据透视表或地图的仪表板项目可能在项目的右上角有一个上下文菜单按钮，其中包含其他查看选项，具体取决于为实例配置的系统设置。如果所有相关系统设置都已禁用，则不会有上下文菜单按钮。以下是可能的菜单选项：

### 在可视化之间切换 { #switching-between-visualizations }

显示图表、数据透视表和地图的仪表板项目可以切换
在这些可视化之间。单击项目上下文菜单按钮并选择所需的视图（例如，**以表格方式查看**、**以地图方式查看**、**以图表方式查看**）：

![](resources/images/dashboard/dashboard-item-menu.png)

### 全屏查看项目 { #view-item-in-fullscreen }

要全屏查看图表、表格或地图，请单击**查看全屏**选项。要退出全屏，您可以按 **esc** 键或单击全屏视图右上角的退出按钮。

### 在应用程序中打开 { #open-in-app }

要在其相关应用程序（例如，数据可视化工具、地图）中打开可视化效果，请单击 **在 [应用程序名称] 应用程序中打开** 选项。

## 显示解释和细节 { #show-interpretations-and-details }

您可以为图表、数据透视表、地图、事件编写解释
单击**显示解释和详细信息**以查看报告和事件图表项目：

![](resources/images/dashboard/dashboard-item-menu-interpretations.png)

> **注意**
>
> 如果系统设置_允许用户显示仪表盘最喜欢的解释和详细信息_未选中，则此选项可能在您的系统上被禁用。）

该项目将在下方垂直展开以显示说明，
解释和答复。你可以喜欢一个解释，回复一个
解释，并添加您自己的解释。您可以编辑、分享或删除
您自己的解释和回复，如果您有版主访问权限，
你可以删除别人的解释。

可以格式化描述字段和解释
使用Markdown样式标记\*和\ _带有**粗体**，_italic_
分别代表**粗体**和_italic_。用于编写新文本的文本字段
解释具有用于添加富文本的工具栏。键盘快捷键
也可以使用：Ctrl / Cmd + B和Ctrl / Cmd +I。
smilies受支持，可以通过键入以下命令之一来使用
字符组合：:) :-) :( :-(：+1：-1。URL是自动的
检测并转换为可点击的链接。

解释按日期降序排列，最新的显示在顶部。
解释回复按日期升序排列，最早的显示在顶部。

![](resources/images/dashboard/dashboard-interpretations.png)

## 共享仪表板 { #dashboard_sharing }

为了与用户组共享仪表板，请单击**分享**
仪表板标题右侧的按钮以显示仪表板
共享设置选项。与特定用户共享仪表板或
用户组，在输入字段中输入名称以将其添加到
仪表板共享设置

![](resources/images/dashboard/dashboard-sharing-dialog.png)

默认情况下，所有仪表板都有两个共享组。

-   外部访问（无需登录）

    选中此选项后，可通过 API 作为外部资源访问仪表板。当您创建外部 Web 门户但希望从您在 DHIS2 内部创建的仪表板中调用信息时，这很有用。默认情况下，未选择此选项。有关详细信息，请参阅开发者指南中的[查看分析资源表示](https://docs.dhis2.org/master/en/developer/html/webapi_viewing_analytical_resource_representations.html#)。

-   公共访问（登录）

    此选项允许将选定的仪表板推送给您的 DHIS2 实例中的所有用户。这也可以通过选择“无”选项从公共视图中隐藏，这是新仪表板的默认选项。

手动添加的用户组可以分配两种类型
仪表板中的权限

-   可以查看

    为用户组提供对仪表板的仅查看权限。

-   可以编辑和查看

    除了查看仪表板外，还允许用户组编辑仪表板。编辑允许更改布局、调整大小和删除项目、重命名/删除仪表板等。

您可以向用户提供仪表板的 url，允许他们
直接导航到仪表板。要获取仪表板网址，只需
在查看模式下访问仪表板，并复制浏览器 url。为了
例如，play.dhis2.org/demo 中产前保健仪表板的网址
是：

https://play.dhis2.org/demo/dhis-web-dashboard/\#/nghVC4wtyzi

# 使用数据可视化器应用 { #data_visualizer }

![](resources/images/data-visualizer/data-visualizer-overview.png)

## 创建和编辑可视化 { #creating-and-editing-visualizations }

当从dhis2菜单打开data-visualizer应用程序时，将显示空白面板，您可以立即开始创建可视化。

![](resources/images/data-visualizer/data-visualizer-new.png)

### 选择可视化类型 { #select-visualization-type }

从左上角的选择器中选择所需的可视化类型。
对于每种可视化类型，都有一个简要说明，并提供有关在布局中的何处使用主要维度的建议。

![](resources/images/data-visualizer/data-visualizer-visualization-type.png)

| 可视化类型 | 描述 |
| --- | --- |
| 柱 | 将信息显示为垂直矩形列，其长度与它们代表的值成比例。<br><br>示例：比较不同地区的性能。<br><br>  布局限制：正好为1个尺寸系列，正好为1个尺寸类别。 |
| 堆积柱 | 将信息显示为垂直的矩形列，其中代表多个类别的条形图相互堆叠。<br><br>示例：显示趋势或相关数据元素的总和。 <br><br> 布局限制：与“列”相同。 |
| 酒吧 | 与Column相同，仅带有水平条。 |
| 叠杆 | 与堆积列相同，仅带有水平条。 |
| 线 | 将信息显示为由直线连接的一系列点。也称为时间序列。<br><br>示例：可视化指标数据在一定时间间隔内的趋势。 <br><br> 布局限制：与“列”相同。 |
| 区 | 基于一条线（上方），轴与线之间的空间充满了颜色，并且线彼此堆叠。 <br> <br>示例：比较相关指标的趋势。 <br> <br>布局限制：与“列”相同。 |
| 堆积面积 | 与“面积”相同，但是各个尺寸项目的面积彼此堆叠。 <br> <br>示例：比较相关指标的趋势。 <br> <br>布局限制：与区域相同。 |
| 馅饼 | 将圆圈划分为多个扇区（或多个切片）。<br><br>示例：可视化单个数据元素的数据比例与所有数据元素的总和之比较。 <br><br> 布局限制：正好是1个尺寸的系列，没有类别。 |
| 雷达 | 在从同一点开始的轴上显示数据。也称为蜘蛛图。 <br> <br>布局限制：与“列”相同。 |
| 测量 | 半圆形，显示单个值，通常不超过100％（可配置起始值和终止值）。 <br> <br>布局限制：正好1个维，正好有1个项目作为序列，数据维被锁定为序列。 |
| 逐年（行） | 当您想要将一年的数据与其他年份的数据进行比较时很有用。基于日历年。 <br> <br>布局限制：期间尺寸已禁用。 |
| 逐年（列） | 与逐年（行）相同，仅具有列。 |
| 单值 | 以仪表板友好的方式显示单个值。 <br> <br>布局限制：与仪表相同。 |
| 数据透视表 | 汇总更广泛的表的数据，并可能包括总和，平均值或其他统计数据，数据透视表以有意义的方式将它们分组在一起。 <br> <br>布局限制：无。 |
| 分散 | 散点图使用户能够将组织单位绘制为针对单个固定或相对时期的两个变量的点。 <br> <br> 布局限制：垂直和水平各1个项目，数据维度锁定为垂直和水平，组织单位锁定为点。 |

### 选择尺寸 { #select-dimensions }

从左侧的维度菜单中，您可以选择要在可视化中显示的维度，包括数据，期间，组织单位和动态维度。可以通过单击尺寸，将尺寸拖放到布局区域或将鼠标悬停在尺寸上并使用其上下文菜单（三个点）来添加这些尺寸。

![](resources/images/data-visualizer/data-visualizer-dimensions.png)

就像在尺寸菜单中一样，在布局区域中，您还可以通过单击尺寸，拖放尺寸或使用尺寸的上下文菜单（三个点）来更改选择。

![](resources/images/data-visualizer/data-visualizer-layout-area.png)

-   **系列**：系列是一组连续的相关元素（例如期间或数据元素），您希望将其可视化以强调其数据中的趋势或关系。也称为数据透视表可视化的列。

<!-- end list -->

-   **类别**：类别是您要比较其数据的一组元素（例如指标或组织单位）。也称为数据透视表可视化的行。

<!-- end list -->

-   **过滤器**：过滤器选择将过滤可视化中显示的数据。请注意，如果您使用数据维度作为过滤器，您只能将单个指标或数据集指定为过滤器项，而对于其他维度类型，您可以选择任意数量的项。

### 选择尺寸项目 { #data_vis_select_dim_items }

维度是指描述系统中数据值的元素。系统中有三个主要维度：

-   **数据**：包括数据元素、指标和数据集（报告率），描述数据的现象或事件。

<!-- end list -->

-   **时段**：描述事件发生的时间。

<!-- end list -->

-   **组织单位**：描述事件发生的地点。

Data Visualizer在允许您将这些维度用作系列，类别和过滤器方面具有高度的灵活性。

要选择尺寸项目，请通过单击尺寸打开尺寸模式窗口。在向布局中添加没有选定项目的尺寸时，该窗口也会自动打开。通过双击某个项目或单击一次并使用中间的箭头选择一个项目，选择要添加到可视化中的项目。出现的顺序将与它们的选择顺序相同。通过将所选项目拖放到“所选”部分中，可以对它们进行重新排序。

#### 选择数据项 { #select-data-items }

选择数据项时，有多种过滤显示项的方法。通过使用顶部的搜索字段，可以在当前选定的**数据类型** 中按项目名称执行全局搜索。通过从下拉列表中选择**数据类型**，可以按类型和子类型过滤项目，其中可用的子类型取决于所选数据类型。名称搜索和类型/子类型过滤也可以结合起来进行更详细的过滤。每个显示项目的类型由项目上的相应图标指示。通过将鼠标悬停在项目上，还可以查看类型的名称。

![](resources/images/data-visualizer/data-visualizer-dimension-modal.png)

#### 选择时期 { #select-periods }

选择期间时，您必须选择在固定期间和相对期间之间进行选择。这些也可以组合。重叠时间段被过滤，因此它们仅出现一次。对于相对期间，名称是相对于当前日期的，例如如果当前月份为3月，并且选择了**上个月**，则2月将显示在可视化文件中。

![](resources/images/data-visualizer/data-visualizer-period-dimension-modal.png)

#### 选择组织单位 { #select-organisation-units }

组织单位对话框非常灵活，提供了三种选择组织单位的方式：

-   显式选择：使用**树**显式选择要在可视化中显示的组织单位。如果您右键单击组织单位，则可以轻松选择以选择其下的所有组织单位。

-   级别和组：**级别**和**组**下拉菜单是一种方便的方法，可以选择一个或多个组织单位组或特定级别的所有单位。示例：选择_Chiefdom_（级别3）以获取该级别的所有单位部门。

    请注意，一旦至少选择了一个级别或组，组织单位树现在将作为级别/组的边界。例如：如果在树中选择_Chiefdom_（第3级）和_Kailahun_ org单位（第2级），则将获得Kailahun地区内的所有酋长单位。

-   用户的组织单位：

    -   用户组织单位：这是一种动态选择已登录用户所关联的组织单位的方法。

    -   用户子单位：选择用户组织单位的子单位。

    -   User sub-x2-units：选择用户组织单位下两级的单位。

![](resources/images/data-visualizer/data-visualizer-organisation-unit-dimension-modal.png)

### 两个类别图 { #two-category-charts }

大多数图表可视化类型可以显示两个类别。
从 Pivot Table 切换到 Column、Bar、Area（以及它们的堆叠版本）和 Line 将前两个维度保留在 Category 中，任何额外的维度都移动到 Filter。
类别中第一个维度的标签显示在图表顶部，第二个维度的标签显示在底部。
生成的可视化由单独的图表组成，第一维中的每个项目一个。

![](resources/images/data-visualizer/data-visualizer-two-category.png)

## 更改可视化的显示 { #change-the-display-of-your-visualization }

可视化的显示可以通过启用/禁用和配置多个选项来更改。每种可视化类型可以具有一组不同的可用选项。选项在**选项对话框**中的选项卡中以及每个选项卡内的部分中进行组织。

1.  单击**选项**以打开**选项 对话框**。

2.  浏览对话框中的选项卡以查看可用选项。

3.  根据需要配置所需的选项。

4.  单击**更新**以将更改应用于可视化。

### 可用选项列表 { #list-of-available-options }

| 选项 | 描述 |
| --- | --- |
|  | **数据标签** |
| 聚集类型 | 定义如何在可视化中汇总数据元素或指标。一些聚合类型为“按数据元素”，“计数”，“最小”和“最大”。 |
| 基准线 | 在给定的域值上显示一条水平线。例如，在您想要可视化自流程开始以来性能如何变化时很有用。 |
| 列小计 | 在数据透视表中显示每个维的小计。 <br>如果仅选择一个维度，则这些列的小计将被隐藏。这是因为值将等于小计。 |
| 列总计 | 在数据透视表中显示每一列的总计值，以及表中所有值的总计。 |
| 累计值 | 在列，堆积列，条形图，堆积条形图，线和面积可视化图中显示累积值 |
| 自定义排序顺序 | 控制值的排序顺序。 |
| 尺寸标签 | 将维度名称显示为数据透视表的一部分。 |
| 隐藏空类别 | 隐藏可视化中没有数据的类别项目。 <br> **在第一个**之前：仅在第一个值之前隐藏缺少的值<br> **在last **之后：仅在最后一个值之后隐藏缺少的值<br> **在第一个和最后一个之前**：仅在第一个之前值和最后一个值之后<br> **全部**：隐藏所有缺少的值<br>例如，当您创建列和条形图时，这很有用。 |
| 隐藏空列 | 隐藏数据透视表中的空列。当您查看大型表时，其中很大一部分的维项目没有数据以保持表的可读性，这很有用。 |
| 隐藏空行 | 隐藏数据透视表中的空行。当您查看大型表时，其中很大一部分的维项目没有数据以保持表的可读性，这很有用。 |
| 号码类型 | 设置要在数据透视表中显示的值的类型：“值”，“行百分比”或“列百分比”。 <br>选项行百分比和列百分比意味着您将以行总百分比或列总百分比显示值，而不是合计值。当您想查看数据元素，类别或组织单位对总价值的贡献时，此功能很有用。 |
| 仅包括已完成的事件 | 在聚合过程中仅包括已完成的事件。例如，这对于在指标计算中排除部分事件很有用。 |
| 行小计 | 在数据透视表中显示每个维的小计。 <br>如果仅选择一个维度，则这些行的小计将被隐藏。这是因为值将等于小计。 |
| 行总计 | 显示数据透视表中每一行的总计值以及表中所有值的总计。 |
| 跳过舍入 | 跳过数据值的舍入，提供数据值的全精度。对于需要全额美元金额的财务数据很有用。 |
| 堆叠的值总计为100％ | 在堆积列和堆积条形图中显示100％堆积值。 |
| 目标线 | 在给定的域值上显示一条水平线。例如，当您想将性能与当前目标进行比较时很有用。 |
| 趋势线 | 显示趋势线，以可视化方式显示数据随时间的变化。例如，如果性能正在改善或恶化。选择期间作为类别时很有用。 |
| 值标签 | 在可视化中显示序列上方的值。 |
|  | 轴标签 |
| 轴范围 | 定义在范围轴上可见的最大值和最小值。 |
| 轴标题 | 在此处输入标题以在x或y轴旁边显示标签。当您想为可视化提供上下文信息时，例如有关度量单位的信息时很有用。 |
| 小数点 | 定义将用于范围轴值的小数位数。 |
| 脚步 | 定义在范围轴上可见的刻度线数。 |
|  | **传奇标签** |
| 显示图例 | 对值应用图例，这意味着您可以对值应用颜色。您可以在`维护应用`中配置图例。 |
| 图例类型 | 控制应用哪个图例。 <br>`对每个数据项使用预定义的图例`根据在`维护应用`中分配给每个数据元素或指标的图例，分别将图例应用于每个数据元素或指标。 <br>`为整个可视化选择单个图例`将单个图例应用于所有数据项，在可用图例的下拉列表中选择。 |
| 图例风格 | 控制图例中的颜色应用于文本或背景的位置。您可以将此选项用于记分卡，以便一目了然地识别高值和低值。不适用于`单值`、`列`或`条`可视化。 |
|  | **系列标签** |
|  | 在此选项卡中设置了用于添加更多轴和更改不同系列显示方式的选项。请在下面的相应部分中查看有关其工作原理的详细说明。 |
|  | **样式标签** |
| 数字组分隔符 | 控制使用哪个字符来分隔数字或“千”组。您可以将其设置为逗号，空格或无。 |
| 显示密度 | 控制数据透视表中单元格的大小。您可以将其设置为“舒适”，“普通”或“紧凑”。当您要将大型表放入浏览器屏幕时，<br> Compact很有用。 |
| 显示组织单位层次结构 | 显示组织单位的所有祖先的名称，例如，“三亚CHP”的名称为"塞拉利昂/孟买/塔马巴卡/三亚CHP”。然后，<br>按字母顺序对组织单位进行排序，这将根据层次结构对组织单位进行排序。 <br>当您下载以单位部门为行的数据透视表并选择了显示单位部门层次结构时，每个单位部门级别均显示为单独的列。例如，当您在本地计算机上创建Excel数据透视表时，这很有用。 |
| 字体大小 | 控制数据透视表文本字体的大小。您可以将其设置为大，普通或小。 |
| 图表/表格标题 | 控制显示在可视化文件上方的标题。自动生成的<br>使用从可视化的尺寸/过滤器生成的默认标题。 <br>无将删除标题。 <br>“自定义”选项允许您键入自定义标题。 |
| 图表/表格字幕 | 控制显示在可视化效果上方的字幕。自动生成的<br>使用从可视化的尺寸/过滤器生成的默认字幕。 <br>无将删除字幕。 <br>“自定义”选项允许您键入自定义字幕。 |
| 显示图例键 | 打开和关闭图例，为可视化本身留出更多空间。 |
| 条/列之间没有空格 | 删除可视化中的列或条之间的空间。对于将可视化显示为EPI曲线很有用。 |
| 值标签 | 在可视化中显示序列上方的值。 |
| 图表/表格标题 | 控制显示在可视化文件上方的标题。自动生成的<br>使用从可视化的尺寸/过滤器生成的默认标题。 <br>无将删除标题。 <br>“自定义”选项允许您键入自定义标题。 |
| 颜色集 | 控制图表中使用的颜色。将显示可用颜色集的列表以及这些颜色的预览。还有一个“单声道图案”选项，该选项使用彩色图案而不是纯色。 |
|  | **限制值标签** |
| 限制最小值/最大值 | 允许在服务器端过滤数据。<br>您可以指示系统仅返回聚合数据值等于，大于，大于或等于，小于或小于或等于某些值的记录。<br> 如果同时使用了过滤器的两个部分，则可以过滤掉一系列数据记录。 |
|  | **参数标签** |
| 自定义排序顺序 | 控制值的排序顺序。 |
| 包括累积 | 包含具有数据透视表累积值的列。 |
| 包括回归 | 包括具有对数据透视表的回归值的列。 |
| 组织单位 | 控制在“报告”应用中创建标准报告时是否要求用户输入组织单位。 |
| 上级组织单位 | 控制在“报告”应用中创建标准报告时是否要求用户输入上级组织单位。 |
| 报告期 | 控制在“报告”应用中创建标准报告时是否要求用户输入报告期间。 |
| 最高限额 | 控制要包含在数据透视表中的最大行数。 |
|  | **异常值选项卡** |
| 异常值检测方法 | 异常值分析是一个涉及识别数据集中异常观察的过程。在 Data Visualizer 中，通过首先将数据标准化为线性回归线，然后分析每个点与回归线的距离来检测异常值。目前支持三种方法。 **四分位距 (IQR)** 基于将数据集划分为四分位数，而 **修正 z 分数** 基于中值绝对偏差 (MAD)。 IQR 和 MAD 被认为是两种最常见的稳健规模度量。 **标准 z 分数**基于标准偏差，因此被认为不太稳健，因为它受异常值的影响很大。 |
| 阈值系数 | 与异常值阈值相乘的数量。控制阈值范围的灵敏度。 IQR 的默认因子为 1.5，z 分数的默认因子为 3。 |

### 图表中文本和图例的自定义样式 { #custom-styling-for-text-and-legend-in-charts }

可以使用文本样式工具自定义以下选项：`图表标题`，`图表字幕`，`显示图例键`，`目标线`，`基准线`，`轴标题`和`标签`（水平和垂直）垂直轴。文本样式工具允许选择字体大小，颜色和斜体/粗体变体。也可以选择文本的位置。

![](resources/images/data-visualizer/data-visualizer-text-styling-tool.png)

## 添加分配的类别 { #adding-assigned-categories }

分配的类别是一个组合维，表示与所选数据元素的类别组合相关的类别选项组合。可以通过从左侧维度菜单中将**分配的类别**维度拖动到可视化布局中来添加此维度：

![](resources/images/data-visualizer/data-visualizer-assigned-categories.png)

添加分配的类别的另一种方法是访问`数据`维度的上下文菜单中的**添加分配的类别**选项（不适用于`计量`，`年度`或`单个值`）。

## 添加更多轴 { #adding-more-axes }

当将数据与不同的测量比例组合在一起时，通过拥有多个轴，您将获得更有意义的可视化效果。对于`栏`，`栏`，`区域`和`线`，您可以通过单击`选项`对话框中的**系列标签**来实现。如果禁用该选项，请确保`数据`维度位于`系列`轴上，并且至少添加了两个项目。

有四个轴可用，两个在图表的左侧（轴 1 和 3），两个在右侧（轴 2 和 4）。
每个轴都有不同的颜色，图表项目将相应地着色。

注意：当使用多个轴时，其他选项选项卡中的某些选项（如`线`，`垂直（y）轴`和`颜色设置`）将被禁用。

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis.png)

## 使用多种可视化类型 { #using-multiple-visualization-types }

可以将`柱形图`与`线形`项目组合在一起，反之亦然。这是通过单击`选项`对话框中的 **系列选项卡 **并更改 `可视化类型 `来完成的。也可以将其与使用多个轴组合（如上节所述）。

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis-multi-type.png)

这将产生一个结合了`列`和`线`类型的图表。

![](resources/images/data-visualizer/data-visualizer-multi-type-chart.png)

## 数据钻探 { #data-drilling }

`数据透视表`可视化类型启用了此功能，并允许通过单击表中的值单元格来钻取数据。将打开一个包含各种选项的上下文菜单。

您可以按组织单位钻取数据，这意味着在组织单位树中上下浏览。数据钻取会影响布局区域中的当前尺寸选择。

![](resources/images/data-visualizer/data-visualizer-pt-drill.png)

## 管理保存的可视化 { #manage-saved-visualizations }

保存可视化文件可以方便以后查找。您也可以选择与其他用户共享或在仪表板上显示它们。

### 打开可视化 { #open-a-visualization }

1.  点击**文件** \> **打开**。

2.  在搜索字段中输入可视化的名称，或单击** <** and **> **箭头在不同页面之间导航。还可以使用右上角的相应菜单按类型和所有者过滤结果。

3.  单击您要打开的名称。

![](resources/images/data-visualizer/data-visualizer-open-dialog.png)

### 保存可视化 { #save-a-visualization }

1. a）单击**文件** \> **保存**。

2. 为您的可视化输入 **名称 **和 **描述 **。

3. 点击**保存**。 

![](resources/images/data-visualizer/data-visualizer-save-dialog.png)

### 重命名可视化 { #rename-a-visualization }

1.  点击**文件** \> **重命名**。

2.  输入新名称和/或描述。

3.  点击 **重命名 **。

![](resources/images/data-visualizer/data-visualizer-rename-dialog.png)

### 删除可视化 { #delete-a-visualization }

1.  点击**文件** \>  **删除**。

2.  点击**删除**。

### 获取可视化链接 { #get-the-link-to-the-visualization }

1. 点击**文件** \> **获取链接**。

2. 可以通过右键单击链接时打开的浏览器上下文菜单复制URL。

![](resources/images/data-visualizer/data-visualizer-delete-dialog.png)

## 可视化解释 { #visualization-interpretations }

查看保存的可视化文件时，可以通过单击右上角的“解释”按钮来扩展右侧的解释。还将显示可视化说明。说明支持RTF格式。

可以通过在右下角的文本字段中键入来添加新的解释。其他用户可以用`@ username`提及。首先输入` @`，再加上用户名或真实姓名的首字母，然后将显示匹配的用户列表。提及的用户将收到内部DHIS2消息以及解释或评论。解释也可以在 **仪表板 **应用中看到。

可以通过分别使用Markdown样式标记`*`和`_`分别代表**bold**和_italic_来用 **粗体**，_italic_设置文本格式（也提供键盘快捷键：`Ctrl `/ `Cmd `+`B`和`Ctrl` /`Cmd` +`I`）。支持有限的表情符号集，可通过键入以下字符组合之一来使用： `:)` `:-)` `:(` `:-(` `:+1` `:-1`. 。URL被自动检测并转换为可点击的链接。

要根据特定解释的日期查看可视化效果，请单击解释或它的`查看`按钮。这将重新生成具有相关日期的可视化文件，该日期显示在可视化文件标题旁边。单击`返回所有解释`将重新生成具有当前日期的可视化文件。

要订阅已保存的可视化，请单击右上角的响铃图标。每当其他用户喜欢/创建/更新此已保存的可视化中的解释时，您将收到内部消息。

![](resources/images/data-visualizer/data-visualizer-view-interpretation.png)

## 共享可视化 { #share-a-visualization }

可以通过单击 **File** \> **Share** 访问共享设置。更改要修改的用户组的共享设置，可用设置有：

-   **可以编辑和查看**：可以查看和编辑可视化。

-   **只能查看**：仅可以查看可视化。

-   **无访问权限**：无权访问可视化。此设置仅适用于**公共访问**和**外部访问**。

可以通过在`添加用户和用户组`下按名称搜索新用户来添加新用户。

![](resources/images/data-visualizer/data-visualizer-share-dialog.png)

## 下载 { #download }

可视化可以使用 **下载 **菜单下载。除`数据透视表`类型外，所有可视化类型均支持`图形`和`纯数据源`下载，可将其下载为`表格布局`和`纯数据源`。

### `图形`下载 { #graphics-download }

将图像（.png）或PDF（.pdf）文件下载到您的计算机。

### `表格布局`下载 { #table-layout-download }

将Excel（.xls），CSV（.csv）或HTML（.html）文件下载到您的计算机。

### `普通数据源`下载 { #plain-data-source-download }

您可以下载 JSON、XML、Excel 格式的可视化数据源，
具有不同标识方案的 CSV、JXRML 或原始数据 SQL 格式
（ID、代码和名称）。数据文档使用以下标识符
维度项目并在新的浏览器窗口中打开以显示
地址栏中对 Web API 的请求。这对
基于 DHIS2 Web API 的应用程序和其他客户端模块的开发人员
或者对于那些需要计划数据源的人，例如用于导入
进入统计包。

**可用格式**

| 格式 | 行动 | 描述 |
| --- | --- | --- |
| JSON格式 | 点击JSON | 根据ID，Code或Name属性下载JSON格式。 |
| XML格式 | 单击XML | 根据ID，Code或Name属性下载XML格式。 |
| 微软Excel | 单击Microsoft Excel | 根据ID，Code或Name属性下载Microsoft Excel格式。 |
| CSV | 点击CSV | 根据ID，代码或名称属性下载CSV格式。 |
| XML数据值集 | 单击高级> XML。 | 将原始数据值下载为XML，而不是沿各个维度聚合的数据。 |
| JSON数据值集 | 单击高级> JSON | 将原始数据值下载为JSON，而不是沿各个维度聚合的数据。 |
| JRXML | 单击高级> JRXML | 生成Jasper报告的模板，该模板可根据您的确切需求进行进一步定制，并用作DHIS 2中标准报告的基础。 |
| 原始数据SQL | 单击高级>原始数据SQL | 提供用于生成数据可视化的实际SQL语句。您可以将其用作Jasper报表中的数据源，或用作SQL视图的基础。 |

## 以地图查看可视化 { #see-visualization-as-map }

要查看可视化效果在地图上的外观，请在完成可视化效果构建后选择`打开为地图`可视化效果类型。

![](resources/images/data-visualizer/data-visualizer-open-as-map.png)

# 使用地图应用 { #using_maps }

## 关于地图应用 { #about_maps }

地图应用程序在 2.29 版中引入并作为替代
GIS 应用程序提供更直观和用户友好的界面。
2.34 版本的映射引擎基于 WebGL 技术，
能够同时在地图上显示数千个特征。

使用地图应用程序，您可以覆盖多个图层并从中选择
不同的底图。您可以创建区域和点的专题地图，
根据分类查看设施，并可视化集水区
每个设施。您可以为区域和点添加标签，并搜索
并使用各种标准进行过滤。您可以移动点并设置位置
在飞行中。地图可以保存为收藏夹并与其他用户共享
和组，或作为图像下载。

> **注意**
>
> 要在 **Maps** 应用程序中使用预定义图例，您需要先在 **Maintenance** 应用程序中创建它们。

![](resources/images/maps/maps_main.png)

-   工作区左侧的 **图层面板 **显示了当前地图的图层概览：

    -   随着图层的添加，使用 **(+) 添加图层** 按钮，它们在此面板中进行排列和管理。

    -    **底图 **始终显示在面板中。默认底图是OSM Light，默认情况下处于选中状态。 OpenStreetMap Details包含更多地图特征和地名。 Bing Maps提供了4种底图，替代了先前版本中提供的Google Maps。必应之路和必应之暗显示了道路，边界和地方。如果地图图层上的颜色较亮，请使用深色版本。 Bing航空和Bing航空标签shos卫星和详细的航空影像。通过选择所需的图像在它们之间切换。

    -   顶部图层面板右侧的小箭头按钮允许隐藏或显示面板。

<!-- end list -->

-   左上角的 **文件**按钮可用于打开和保存地图：

    -   新

        将清除所有现有地图图层以创建新地图。

    -   打开

        将显示一个对话框，其中包含现有地图的列表，这些地图将在其中打开，重命名，共享和删除。 _当前地图的标题显示在文件按钮上方的标题栏中_。

    -   保存

        会将所有更改保存到当前地图。

    -   另存为

        将使用新名称保存当前地图。

    -   改名

        允许您更改当前地图的名称和/或描述。

    -   翻译

        允许您翻译当前地图的名称和/或描述。

    -   分享

        将打开一个对话框，可以在其中与所有人或一组用户共享当前地图。

    -   获取链接

        将提供直接链接到当前地图。

    -   删除

        删除当前地图。

<!-- end list -->

-   文件按钮旁边的 **下载**按钮可让您将当前地图下载为PNG图像。

<!-- end list -->

-   右上角的**解释**按钮将在工作区的右侧打开一个解释面板。仅在保存了地图的情况下该按钮才可单击。

    -   **地图详细信息**显示有关当前地图的信息。

    -   **解释**允许您查看、添加、编辑和分享有关当前地图的解释。

<!-- end list -->

-   地图上的 **+** 和 **-** 按钮允许您分别放大和缩小地图。鼠标滚轮缩放是连续的，使我们能够将地图完美地适应您的内容。

-   使用**旋转地图**按钮（三角形箭头）可以旋转和倾斜地图，以增强数据视图。在移动鼠标时按下按钮（或键盘上的Control键）以更改地图视图。再次单击以重置视图。

-   **全屏**（四个箭头）允许您全屏查看地图。要退出全屏，请再次单击该按钮或键盘上的退出键。

*   **缩放到内容**（有界放大镜符号）会自动调整缩放级别和地图中心位置，以使地图上的数据成为焦点。

*   **搜索**（放大镜符号）允许搜索并跳转到地图上的某个位置。

*   使用**直尺**按钮，您可以测量地图上的距离和面积。

*   右键单击地图以显示该位置的经度和纬度。

**底图**

底图图层由图层面板中的图层 _cards_ 表示，例如
作为：

![](resources/images/maps/maps_basemap_card.png)

在底图卡的顶部，从左到右分别是：

-   所选底图的标题

-   折叠和展开底图卡的箭头符号

底图卡片的中间是可用底图的列表。这
当前底图突出显示。

底图卡的底部是：

-   用于切换图层可见性的眼睛符号

-   用于修改图层透明度的滑块

## 建立新地图 { #using_maps_create_map }

1.  在**应用**菜单中，单击**地图**。随即打开**DHIS2 Maps**窗口。

2.  单击左上角的 (+) 添加图层按钮。您将看到图层选择对话框：

    ![](resources/images/maps/maps_layer_selection.png)

3.  选择要添加到当前地图的图层。可能的选项是：

    -   [专题](#using_maps_thematic_layer)

    -   [事件](#using_maps_event_layer)

    -   [跟踪实体](#using_maps_tracked_entity_layer)

    -   [设施](#using_maps_facility_layer)

    -   [边界](#using_maps_boundary_layer)

    此外，Google Earth Engine 和其他服务还提供了几层：

    -   人口

    -   人口年龄组

    -   海拔

    -   沉淀

    -   温度

    -   土地覆盖

    _Labels overlay_ 是在维护应用程序中定义的 [external layer](#using_maps_external_map_layers)。

## 管理主题层 { #using_maps_thematic_layer }

_专题图_代表地理分布的空间变化。
选择您想要的指标/数据元素、周期和
组织单位层面。如果您的数据库有坐标并聚合
这些组织单位的数据值，它们将出现在地图上。

> **注意**
>
> 您必须生成 DHIS2 分析表才能获得可用的聚合数据值。

![](resources/images/maps/maps_thematic_mapping.png)

专题图层由图层面板中的图层 _cards_ 表示，例如
作为：

主题卡的顶部从左到右分别是：

-   抓取字段，允许使用鼠标拖动和重新排序图层

-   与图层关联的标题和时期

-   折叠和展开主题卡片的箭头符号

主题卡的中间是一个图例，表示价值
显示在图层上的范围。

主题卡的底部从左到右分别是：

-   编辑（铅笔）按钮以打开图层配置对话框

-   用于切换图层可见性的眼睛符号

-   用于修改图层透明度的滑块

-   具有更多选项的更多操作（三个点）按钮：

    -   **数据表**切换按钮可显示或隐藏与图层关联的数据表

    -   **下载数据**允许您以GeoJSON格式下载此图层的数据，以供其他地图软件使用

    -   **编辑图层**与上方的编辑按钮相同

    -   **移除图层**将从当前地图中移除该图层。

### 创建一个主题层 { #create-a-thematic-layer }

要创建事件层，请在**添加层**选择上选择**主题**。这将打开“事件”层配置对话框。

1.  在**数据**标签中：

    ![](resources/images/maps/maps_thematic_layer_dialog_DATA.png)

    -   选择数据类型，然后分别选择组和目标元素。可用字段取决于所选项目的类型。

    -   从**汇总类型**字段中选择一个值，以将数据值显示在地图上。默认情况下，“按数据元素”处于选中状态。替代值是：计数；平均数;和;标准偏差方差;敏最大限度。另请参阅[聚合运算符] [Aggregation operators](https://dhis2.github.io/dhis2-docs/master/en/user/html/ch10s05.html#d0e8082)。

2.  在**期间**标签中

    ![](resources/images/maps/maps_thematic_layer_dialog_PERIOD.png)

    -   选择专题数据映射的时间跨度。您可以选择相对周期或固定周期。

        -   相对时期

            在**期间类型**字段中，选择**相对**，然后在**期间**字段中选择一个相对期间，例如**去年**或**过去12个月**。

            可以在**系统设置**应用中设置**分析的默认相对周期**。

            如果您选择涵盖多年/月/周/日的相对时期，则图层可以显示为

            -   单（合计）

                显示所选相对期间的汇总值（默认）。

            -   时间线

                包括一个时间线，让您可以逐步了解各个时期。同一地图只能添加一个时间线图层。

            -   拆分地图视图

                显示多张地图，让您并排比较不同时期。支持 12 项或以下的相对期间。不能与其他图层类型组合。

        -   固定期间

            在**期间类型**字段中，选择期间长度，然后在**期间**字段中选择目标。

        -   开始/结束日期

            在**期间类型**字段中，选择**开始/结束日期**，然后填写开始日期和结束日期。

3.  在**ORG UNITS**标签中：

    ![](resources/images/maps/maps_thematic_layer_dialog_ORG_UNITS.png)

    -   选择要包含在图层中的组织单位。可以选择

        -   一个或多个特定的组织单元、层次结构中的组织单元级别、组织单元组，或

        -   组织单位层次结构中相对于用户的相对级别。通过选择**用户组织单位**，对于组织单位层次结构中不同级别的用户，地图数据将以不同的方式显示。

4.  在**过滤器**标签中：

    ![](resources/images/maps/maps_thematic_layer_dialog_FILTER.png)

    -   单击添加过滤器并选择可用数据项以将新过滤器添加到数据集。

        -   从下拉框中选择数据维度。您可以使用搜索字段减少显示的维数。单击名称以选择维度。

        -   选择维度后，您将获得第二个包含维度项目的下拉菜单。检查要包含在过滤器中的项目。

        可以添加多个过滤器。单击过滤器右侧的垃圾桶按钮将其删除。

5.  在**样式**标签中：

    ![](resources/images/maps/maps_thematic_layer_dialog_STYLE.png)

    -   选择**钟形**或**气泡图**。

        -   Choropleth 将根据数据值为每个组织单位形状分配颜色。如果数据是标准化的（人均），这是推荐的技术。

        -   气泡图将数据值显示为比例圆圈。如果数据未标准化（绝对数字），请使用此技术。圆圈位于每个组织单位的中心。

    -   为比例圆或点设施设置**低半径**和**高半径**。圆将根据数据值在低半径和高半径之间缩放。半径必须在0到50像素之间。

    -   **显示标签**：允许在图层上显示组织单位名称。可以在此处修改字体大小、粗细、样式和颜色。

    -   **不显示数据**：默认情况下，缺少数据值的组织单位不会显示在地图上。如果您想用颜色显示它们，请选中此框。单击颜色进行更改。

    -   选择图例类型：

        -   **自动颜色图例**：应用程序将根据您选择的分类方法、类数和色标为您创建一个图例。将**分类**设置为：

            -   等间隔

                每个间隔的范围将是（最高数据值-最低数据值/类数）

            -   均数

                图例创建者将尝试平均分配组织单位。

        -   **预定义的颜色图例**：在预定义的图例之间进行选择。

        -   **单色图例**：选择气泡或圆圈的颜色。仅适用于气泡图。

6.  点击**添加图层**。

### 修改主题层 { #modify-a-thematic-layer }

1.  在图层面板中，单击专题图层卡片上的编辑（铅笔）图标。

2.  根据需要修改任何选项卡上的设置。

3.  点击**更新图层**。

### 筛选主题层中的值 { #filter-values-in-a-thematic-layer }

专题图层有一个 **data table** 选项，可以打开或
从专题图层卡上关闭。

![](resources/images/maps/maps_thematic_layer_data_table.png)

数据表显示构成主题层的数据。

-   单击标题将根据该列对表格进行排序；在上升和下降之间切换。

-   在标题下方的过滤器字段中输入文本或表达式会将这些过滤器应用于数据，并且显示将根据过滤器进行调整。过滤器应用如下：

    -   名称

        按包含给定文本的名称过滤

    -   值

        按给定的数字和/或范围过滤值，例如：2,\>3&\<8

    -   传说

        按图例过滤并包含给定的文本

    -   范围

        按包含给定文本的范围过滤

    -   水平

        按数字和/或范围过滤级别，例如：2，\> 3＆\ <8

    -   父母

        按包含给定文本的父项名称过滤

    -   ID

        按包含给定文本的ID进行过滤

    -   类型

        按包含给定文本的GIS显示类型过滤

    -   颜色

        按包含给定文本的颜色名称过滤

> **注意**
>
> 数据表过滤器是临时的，不会与地图图层一起保存为收藏夹的一部分。

### 搜索组织单位 { #search-for-an-organisation-unit }

数据表中的 NAME 过滤器字段提供了一种有效的方法
搜索单个组织单位。

### 在组织层次结构之间导航 { #navigate-between-organisation-hierarchies }

当地图上有可见的组织单位时，您可以轻松地
在不使用级别/父级的情况下在层次结构中上下导航
用户界面。

1.  右键单击组织单位之一。

2.  选择**向上钻取一级**或**向下钻取一级**。

    如果您在最低级别或如果在下面的级别上没有可用的坐标，则会禁用向下钻取选项。同样，从最高级别禁用向上钻取选项。

### 删除主题层 { #remove-thematic-layer }

要清除主题层中的所有数据：

1.  在左侧的图层卡中，单击_more actions_（三个点）图标，然后在**删除图层**上单击。

    该图层将从当前地图中删除。

## 管理事件层 { #using_maps_event_layer }

事件层显示注册事件的地理位置
在 DHIS2 跟踪器中。只要事件具有关联的点或多边形
坐标，您可以使用此图层从聚合的
显示在专题层中的数据给底层个人
事件或案例。

您还可以在设施或在
边界水平。您可以使用事件数据通过专题图层执行此操作
项目。当您只有 Org 的坐标时，这很有用
记录事件的单位。

![](resources/images/maps/maps_event_layer.png)

事件层由层面板中的层 _cards_ 表示，例如
作为：

在事件卡的顶部，从左到右分别是：

-   抓取字段，允许使用鼠标拖动和重新排序图层

-   与图层关联的标题和时期

-   折叠和扩展事件卡的箭头符号

在事件卡的中间是一个说明样式的图例
层。

在事件卡的底部，从左到右分别是：

-   编辑（铅笔）按钮以打开图层配置对话框

-   用于切换图层可见性的眼睛符号

-   用于修改图层透明度的滑块

-   具有更多选项的更多操作（三个点）按钮：

    -   **数据表**切换按钮可显示或隐藏与图层关联的数据表

    -   **下载数据**允许您以GeoJSON格式下载此图层的数据，以供其他地图软件使用

    -   **编辑图层**与上方的编辑按钮相同

    -   **移除图层**将从当前地图中移除该图层。

### 创建一个事件层 { #maps_create_event_layer }

要创建事件层，请在**添加层**选择上选择**事件**。这将打开事件层配置对话框。

1.  在**数据**标签中：

    ![](resources/images/maps/maps_event_layer_dialog_DATA.png)

    -   选择一个项目，然后选择一个项目阶段。仅在选择项目后才显示**阶段**字段。

        如果所选程序只有一个阶段可用，则自动选择阶段。

    -   从**坐标字段**中为地图上显示的位置选择一个值。默认情况下，选择“事件位置”。根据属于程序的数据元素或属性，还可以使用其他坐标，例如“住所位置”。

    -   默认情况下，所有带有坐标的事件都显示在地图上。使用**事件状态**字段仅显示具有以下一种状态的事件：有效，已完成，计划，过期或已跳过。

2.  在**期间**标签中

    ![](resources/images/maps/maps_event_layer_dialog_PERIOD.png)

    -   选择事件发生的时间跨度。您可以选择固定期间或相对期间。

        -   相对时期

            在 **Period** 字段中，选择一个相对时期，例如 **This month** 或 **Last year**。

            可以在**系统设置**应用中设置**分析的默认相对周期**。

        -   固定期间

            在**期间**字段中，选择**开始/结束日期**，然后填写开始日期和结束日期。

3.  在**ORG UNITS**标签中：

    ![](resources/images/maps/maps_event_layer_dialog_ORG_UNITS.png)

    -   选择要包含在图层中的组织单位。可以选择

        -   一个或多个特定的组织单位，或

        -   组织单位层次结构中相对于用户的相对级别。通过选择**用户组织单位**，对于组织单位层次结构中不同级别的用户，地图数据将以不同的方式显示。

4.  在**过滤器**标签中：

    ![](resources/images/maps/maps_event_layer_dialog_FILTER.png)

    -   单击添加过滤器并选择可用数据项以将新过滤器添加到数据集。

        -   对于 _option set_ 类型的数据项，您可以使用向下箭头从下拉框中选择任何选项，或者直接在框中开始输入以过滤选项。

        -   对于_number_类型的数据项，可以选择等于、不等于、大于或小于等运算符。

        -   对于 _boolean_ 类型的数据项（是/否），您可以选中该框是否条件应为有效或为真。

        -   对于_text_类型的数据项，您将有两种选择：**包含**表示查询将匹配包含您的搜索值的所有值，**是精确**表示仅与搜索查询完全相同的值将被退回。

        可以添加多个过滤器。单击过滤器右侧的垃圾桶按钮将其删除。

5.  在**样式**标签中：

    ![](resources/images/maps/maps_event_layer_dialog_STYLE.png)

    -   选择**分组事件**以将附近的事件（集群）分组，或选择**查看所有事件**以单独显示事件。

    -   为事件或聚类点选择一种**颜色**。

    -   为事件选择**半径**（1到20之间）。

    -   选择**显示缓冲区**以在每个事件周围显示可视缓冲区。缓冲区的半径可以在这里修改。仅当您选择上面的**查看所有事件**时，此选项才可用。

    -   选择**按数据元素样式 **以根据数据值为事件着色。如果您还选择对事件进行分组，则用户将显示为小的甜甜圈图，以显示数据值的分布。这些选项因不同的数据类型而异：

        -   **选项集**：为选项集中的每个选项选择一种颜色。您可以在维护应用程序中为选项设置默认颜色。

        -   **数字**：您可以使用自动或预定义的图例以 [与专题图层相同的方式](#using_maps_thematic_layer_style) 设置数字数据元素的样式。

        -   **布尔值**：为真/是选择一种颜色，为假/否选择另一种颜色。

6.  点击**添加图层**。

### 修改事件层 { #modify-an-event-layer }

1.  在图层面板中，单击事件图层卡片上的编辑（铅笔）图标。

2.  根据需要修改 DATA、PERIOD、FILTER、ORG UNIT 和 STYLE 选项卡上的设置。

3.  点击**更新图层**。

### 列出和过滤事件 { #listing-and-filtering-events }

事件层有一个 **data table** 选项，可以打开或
从事件层卡上关闭。

![](resources/images/maps/maps_event_layer_data_table.png)

数据表显示构成事件层的数据。

-   单击标题将根据该列对表格进行排序；在上升和下降之间切换。

-   在标题下方的过滤器字段中输入文本或表达式会将这些过滤器应用于数据，并且显示将根据过滤器进行调整。过滤器应用如下：

    -   ID

        按包含给定文本的事件ID进行过滤

    -   组织单位

        按包含给定文本的组织单位名称过滤

    -   活动时间

        按包含给定文本的事件时间过滤

    -   类型

        按包含给定文本的GIS显示类型过滤

    -   **按数据元素设置样式**：如果事件由数据元素（例如性别）设置样式，则可以过滤数据值和颜色。

    -   **在报告中显示**：选中以显示在报告中的数据元素将显示在单独的列中（请参阅下文如何添加它们）。

    -   数字数据值可以按给定的数字和/或范围过滤，例如：2,\>3&\<8

> **注意**
>
> 数据表过滤器是临时的，不会与地图图层一起保存为收藏夹的一部分。

### 修改事件数据表和弹出窗口中的信息 { #modify-information-in-event-data-table-and-popups }

您可以修改事件弹出窗口中显示的信息。

![](resources/images/maps/maps_eventlayer_eventinfopopup.png)

1.  打开**维护**应用程序。

2.  选择**程序**。

3.  单击要修改的程序，然后选择** 2分配数据元素**。

4.  对于要在弹出窗口中显示的每个数据元素，选择相应的**在报告中显示**。

5.  点击**保存**。 

### 下载原始事件层数据 { #download-raw-event-layer-data }

可以以GeoJSON格式下载事件层的原始数据，以便在桌面GIS软件（例如[QGIS]https://www.qgis.org/）中进行更高级的地理分析和处理。下载的数据包括所有单独的事件，作为GeoJSON功能，包括为**在报告中显示**选择的每个数据元素的属性。

![](resources/images/maps/maps_data_download_dialog.png)

-   在左侧的图层卡中，点击_more actions_（三个点）图标，然后点击**下载数据**

-   选择** ID格式**用作下载的GeoJSON文件中数据元素值的键。共有三个选项：

    -   ** ID **-使用数据元素的唯一ID
    -   **名称**-使用数据元素的人性化名称（翻译）
    -   **代码**-使用数据元素的代码

-   选择是否对其他事件属性（例如程序阶段，纬度，经度，事件数据以及组织单位ID，名称和代码）**使用人类可读的键**。如果**未**选中此选项，则这些值将是计算机友好的ID，而不是人类可读（和翻译）的名称。

-   单击**下载**按钮以生成和下载GeoJSON文件。数据将从DHIS2服务器请求并由地图应用程序处理。此操作可能需要几分钟才能完成。

-   一旦下载了GeoJSON文件，就可以将其导入大多数标准GIS软件应用程序中。

>请注意，下载的数据不包含样式信息，因为GeoJSON格式本身不支持它。可以选择使用每个要素的属性在外部GIS应用程序中重新创建样式。

### 清除事件层 { #clear-event-layer }

要清除地图中的所有事件层数据：

1.  在左侧的图层卡中，单击_more actions_（三个点）图标，然后在**删除图层**上单击。

    该图层将从当前地图中删除。

## 管理跟踪的实体层 { #using_maps_tracked_entity_layer }

被追踪实体图层显示被追踪的地理位置
在 DHIS2 中注册的实体。前提是被跟踪的实体有
关联的点或多边形坐标，您可以在地图上探索这些。

![](resources/images/maps/maps_tracked_entity_layer.png)

跟踪实体图层由图层面板中的图层卡片表示
如：

沿着跟踪实体卡的顶部，从左到右分别是：

-   允许使用鼠标拖动和重新排序图层的抓取字段。

-   与图层关联的标题和时期。

-   箭头符号，用于折叠和展开被跟踪的实体卡。

被追踪实体卡片的中间是一个图例，表明
图层样式。

跟踪实体卡的底部从左到右分别是：

-   编辑（铅笔）按钮以打开图层配置对话框

-   用于切换图层可见性的眼睛符号

-   用于修改图层透明度的滑块

-   具有更多选项的更多操作（三个点）按钮：

    -   **编辑图层**与上方的编辑按钮相同

    -   **移除图层**将从当前地图中移除该图层。

### 创建一个跟踪实体层 { #maps_create_tracked_enity_layer }

要创建跟踪实体层，请在**添加层**选择上选择**跟踪实体**。这将打开跟踪的实体层配置对话框。

1.  在**数据**标签中：

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_DATA.png)

    -   选择要在地图上显示的**跟踪实体类型**。

    -   选择被跟踪实体所属的**程序**。

    -   使用**计划状态**字段选择要跟踪的实体的注册状态，包括：全部，活动，已完成或已取消。

    -   设置给定程序的被跟踪实体的**跟踪**状态。

2.  在**关系**标签中

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_RELATIONSHIPS.png)

    > **Caution**
    >
    > Displaying tracked entity relationships in Maps is an experimental feature

    -   如果选择了跟踪的实体类型，则可以选中**显示跟踪的实体关系**复选框

    -   选中后，您可以从下拉列表中选择要显示在地图上的关系类型。仅来自所选“跟踪的实体”类型的关系可用。

3.  在**期间**标签中

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_PERIOD.png)

    -   如果未选择任何程序，您可以设置上次更新跟踪实体的开始和结束日期。

    -   如果选择了一个程序，您可以设置跟踪实体最后一次更新的时间段，或者它们在程序中注册或注册的时间。

4.  在**ORG UNITS**标签中：

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_ORG_UNITS.png)

    -   选择要包含在图层中的组织单位。您有 3 种选择模式：

        -   **仅选定**：仅包括属于选定组织单位的跟踪实体。

        -   **选定及以下**：包括在选定组织单位中和正下方的跟踪实体。

        -   **选定和以下所有**：包括在选定组织单位中和所有以下的跟踪实体。

5.  在**样式**标签中：

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_STYLE.png)

    -   为跟踪的实体点和多边形选择一种**颜色**。

    -   为点选择**点大小**（半径在 1 到 20 之间）。

    -   选择**显示缓冲区**以在每个被跟踪实体周围显示可视缓冲区。可以在此处修改以米为单位的缓冲距离。

    -   如果在关系选项卡上选择了关系类型，则可以为关系和相关的跟踪实体实例选择**颜色**，**点大小**和**线颜色**

6.  点击**添加/更新图层**。

### 修改跟踪的实体层 { #modify-a-tracked-entity-layer }

1.  在图层面板中，单击被跟踪实体图层卡上的编辑（铅笔）图标。

2.  根据需要修改 DATA、PERIOD、ORG UNIT 和 STYLE 选项卡上的设置。

3.  点击**更新图层**。

### 清除跟踪的实体层 { #clear-a-tracked-entity-layer }

要从地图上清除跟踪的实体层：

1.  在左侧的图层卡中，单击_more actions_（三个点）图标，然后在**删除图层**上单击。

    该图层将从当前地图中删除。

## 管理设施层 { #using_maps_facility_layer }

设施层显示代表设施类型的图标。
多边形不会显示在地图上，因此请确保选择一个
具有设施的组织单位级别。

_多边形是表示国家，地区或公园的地图上的封闭区域_。

![](resources/images/maps/maps_facility_layer.png)

设施层由层面板中的层 _cards_ 表示，例如
作为：

在设施卡的顶部，从左到右分别是：

-   抓取字段，允许使用鼠标拖动和重新排序图层

-   **设施**标题

-   用于切换图层可见性的眼睛符号

-   折叠和扩展设施卡的箭头符号

在设施卡的中间是一个指示组的图例
设置表示。

设施卡的底部从左到右分别是：

-   编辑（铅笔）按钮以打开图层配置对话框

-   用于修改图层透明度的滑块

-   具有更多选项的更多操作（三个点）按钮：

    -   **数据表**切换按钮可显示或隐藏与图层关联的数据表

    -   **下载数据**允许您以GeoJSON格式下载此图层的数据，以供其他地图软件使用

    -   **编辑图层**与上方的编辑按钮相同

    -   **移除图层**将从当前地图中移除该图层。

### 创建设施层 { #create-a-facility-layer }

要创建设施层，请在“添加层**选择上选择**设施**。这将打开“设施层**配置对话框。

1.  在**组集**标签中：

    ![](resources/images/maps/maps_facility_layer_dialog_GROUPSET.png)

    -   从为您的DHIS2实例定义的组织单位组集的列表中选择一个**组集**。

2.  在**组织单位**标签中

    ![](resources/images/maps/maps_facility_layer_dialog_ORG_UNITS.png)

    -   从右侧的选择字段中选择组织单位级别和/或组。

    -   选择要包含在图层中的组织单位。可以选择

        -   一个或多个特定的组织单位，或

        -   组织单位层次结构中相对于用户的相对级别。通过选择**用户组织单位**，对于组织单位层次结构中不同级别的用户，地图数据将以不同的方式显示。

3.  在**样式**标签中：

    ![](resources/images/maps/maps_facility_layer_dialog_STYLE.png)

    -   选择您想要应用于设施的任何样式。

        -   显示标签

            允许在图层上显示标签。字体大小、粗细和颜色可以在这里修改。

        -   显示缓冲区

            允许在每个设施周围的图层上显示视觉缓冲区。可以在此处修改缓冲区的半径。

4.  点击**添加图层**。

### 创建或修改设施层 { #create-or-modify-a-facility-layer }

1.  在图层面板中，单击设施图层卡上的编辑（铅笔）图标。

2.  根据需要修改 GROUP SET、ORGANIZATION UNITS 和 STYLE 选项卡上的设置。

3.  点击**更新图层**。

### 过滤设施层中的值 { #filter-values-in-a-facility-layer }

设施层有一个**数据表**选项，可以打开或
离设施层卡。

![](resources/images/maps/maps_facility_layer_data_table.png)

数据表显示构成设施层的数据。

-   单击标题将根据该列对表格进行排序；在上升和下降之间切换。

-   在标题下方的过滤器字段中输入文本或表达式会将这些过滤器应用于数据，并且显示将根据过滤器进行调整。过滤器应用如下：

    -   名称

        按包含给定文本的名称过滤

    -   ID

        按包含给定文本的ID进行过滤

    -   类型

        按包含给定文本的GIS显示类型过滤

> **注意**
>
> 数据表过滤器是临时的，不会与地图图层一起保存为收藏夹的一部分。

### 搜索设施 { #search-for-a-facility }

数据表中的 NAME 过滤器字段提供了一种有效的方法
寻找个人设施。

### 删除设施层 { #remove-facility-layer }

要清除设施层中的所有数据：

1.  在左侧的图层卡中，单击_more actions_（三个点）图标，然后在**删除图层**上单击。

    该图层将从当前地图中删除。

### 分层管理设施 { #manage-facilities-in-a-layer }

您可以在**设施**，**边界**和**主题**层中使用设施。

#### 搬迁设施 { #relocate-a-facility }

1.  右键单击设施，然后单击**重新定位**。

2.  将光标放在新位置。

    新坐标将永久存储。这不能被撤消。

#### 交换设施的经度和纬度 { #swap-longitude-and-latitude-of-a-facility }

1.  右键单击设施，然后单击**交换经度/纬度**。

    如果用户在创建组织单位时反转纬度和经度坐标，这很有用。

#### 显示设施信息 { #display-facility-information }

您可以查看管理员设置的组织单位信息为
如下：

 <table>
 <caption>查看组织单位信息</caption>
 <colgroup>
 <col style="width: 40%" />
 <col style="width: 59%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th>功能</th>
 <th>操作</th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p>查看当前期间的信息</p> </td>
  <ol type="1"><td>
 <li><p>单击设施。 </p></li>
 </ol> </td>
 </tr>
 <tr class="even">
 <td> <p>查看选定时间段的信息 </p></td>
 <td> <ol type="1">
  <li><p>右键单击设施，然后单击<strong>显示信息</strong></p>
</li>  
<li><p> 在<strong>基础数据</strong>部分中，选择一个周期。 </p></li>
 </ol>
 <blockquote>
 <p><strong>注意</strong></p>
 <p>您可以在<strong>系统设置</strong>应用中配置显示的基础数据。 </p>
 </blockquote> </td>
 </tr>
 </tbody>
 </table>

## 管理边界层 { #using_maps_boundary_layer }

边界层显示您的边界和位置
组织单位。如果您处于离线状态，此层特别有用
并且无法访问背景地图。

![](resources/images/maps/maps_bound_layers.png)

边界层由层面板中的层 _cards_ 表示，例如
作为：

边界卡的顶部从左到右分别是：

-   抓取字段，允许使用鼠标拖动和重新排序图层

-   **边界**标题

-   箭头符号，用于折叠和展开边界卡

边界卡的底部从左到右分别是：

-   编辑（铅笔）按钮以打开图层配置对话框

-   用于切换图层可见性的眼睛符号

-   用于修改图层透明度的滑块

-   具有更多选项的更多操作（三个点）按钮：

    -   **数据表**切换按钮可显示或隐藏与图层关联的数据表

    -   **下载数据**允许您以GeoJSON格式下载此图层的数据，以供其他地图软件使用

    -   **编辑图层**与上方的编辑按钮相同

    -   **移除图层**将从当前地图中移除该图层。

### 创建边界层 { #create-a-boundary-layer }

要创建边界层，请在**添加层**选择上选择**边界**。这将打开边界层配置对话框。

1.  在**组织单位**标签中

    ![](resources/images/maps/maps_boundary_layer_dialog_ORG_UNITS.png)

    -   从右侧的选择字段中选择组织单位级别和/或组。

    -   选择要包含在图层中的组织单位。可以选择

        -   一个或多个特定的组织单位，或

        -   组织单位层次结构中相对于用户的相对级别。通过选择**用户组织单位**，对于组织单位层次结构中不同级别的用户，地图数据将以不同的方式显示。

2.  在**样式**标签中：

    ![](resources/images/maps/maps_boundary_layer_dialog_STYLE.png)

    -   选择要应用于边界的任何样式。

        -   显示标签

            允许在图层上显示标签。字体大小和粗细可以在这里修改。

        -   点半径

            当点类型元素（例如设施）出现在边界层上时，设置基本半径。

3.  点击**添加图层**。

### 修改边界层 { #modify-a-boundary-layer }

1.  在图层面板中，单击边界图层卡上的编辑（铅笔）图标。

2.  根据需要修改 ORGANIZATION UNITS 和 STYLE 选项卡上的设置。

3.  点击**更新图层**。

### 过滤边界层中的值 { #filter-values-in-a-boundary-layer }

边界层有一个**数据表**选项，可以从边界层卡上打开或关闭。

![](resources/images/maps/maps_bound_layer_data_table.png)

数据表显示构成边界层的数据。

-   单击标题将根据该列对表格进行排序；在上升和下降之间切换。

-   在标题下方的过滤器字段中输入文本或表达式会将这些过滤器应用于数据，并且显示将根据过滤器进行调整。过滤器应用如下：

    -   名称

        按包含给定文本的名称过滤

    -   水平

        按数字和/或范围过滤级别，例如：2，\> 3＆\ <8

    -   父母

        按包含给定文本的父项名称过滤

    -   ID

        按包含给定文本的ID进行过滤

    -   类型

        按包含给定文本的GIS显示类型过滤

> **注意**
>
> 数据表过滤器是临时的，不会与地图图层一起保存为收藏夹的一部分。

### 搜索组织单位 { #search-for-an-organisational-unit }

数据表中的 NAME 过滤器字段提供了一种有效的方法
搜索边界中显示的单个组织单位
层。

### 在组织层次结构之间导航 { #navigate-between-organisation-hierarchies }

您可以在层次结构中修改边界层的目标，而无需
使用级别/父用户界面。

1.  用鼠标右键单击边界之一。

2.  选择**向上钻取一级**或**向下钻取一级**。

    如果您处于最低级别，则会禁用向下钻取选项。同样，从最高级别禁用向上钻取选项。

### 移除边界层 { #remove-boundary-layer }

要清除边界层中的所有数据：

1.  在左侧的图层卡中，单击_more actions_（三个点）图标，然后在**删除图层**上单击。

    该图层将从当前地图中删除。

## 管理地球引擎层 { #using_maps_gee }

![](resources/images/maps/maps_earth_eng_layer.png)

Google Earth Engine 中的图层可让您显示和聚合外部
数据到您的组织单位。使用人口图层来计算
居住在一个地区或距离卫生保健机构不远的人数
设施。高程图层允许您找到最低、最高和
平均海拔。使用土地覆盖层查看森林覆盖、农田
或城市地区，并计算每个组织单位的百分比。

支持以下层：

![](resources/images/maps/maps_earth_eng_layer_types.png)

-   **人口**：来自 WorldPop 的详细人口数据，显示居住在某个地区的估计人口数量。从 2000 年及以后的年度期间可用。

-   **人口年龄组**：居住在一个地区的估计人数，按年龄和性别分组。

-   **海拔**：海拔高度。

-   **降水量**：数值以毫米为单位，以 5 天为单位。每月更新一次，在下个月的第三周。从地面的卫星和气象站收集。

-   **温度**：从卫星收集的地表温度。空白点将出现在持续云层覆盖的区域。

-   **土地覆盖**：美国宇航局从卫星收集的 17 种不同的土地覆盖类型。

### 创建地球引擎图层 { #create-an-earth-engine-layer }

要创建 Earth Engine 图层，请从 **Add
层**选择。这将打开层配置对话框。

1.  在**数据**标签中：

    ![](resources/images/maps/maps_ee_layer_dialog_DATA.png)

    -   对于“人口年龄组”，您可以选择在汇总数据时要包含的年龄/性别**组**。

    -   选择在计算选定组织单位的值时要使用的**聚合方法**。

        -   **Sum**：计算每个组织单位内的总数。推荐用于人口层。

        -   **Min**：返回所选内容下方显示的图层单位中的最小值。对于人口层，它将是每公顷的最低_人数_。对于高程图层，它将返回最低海拔（海拔米）。

        -   **Max**：以层为单位返回最大值。对于人口层，它将是_每公顷的最低人数_。对于高程图层，它将返回每个组织单位的最高海拔。

        -   **Mean**：返回层单位的平均值。对于人口层，它将是平均_每公顷人数_。对于降水层，它将是整个组织单位的平均降雨量，以毫米为单位。

        -   **Median**：以层为单位返回平均值。对于人口层，它将是每公顷的中位数_人_。对于温度层，它将是组织单元白天的中值°C。

        -   **标准偏差**：以层为单位返回标准偏差值。

        -   **Variance**：以层为单位返回方差值。

2.  在**期间**标签中

    ![](resources/images/maps/maps_ee_layer_dialog_PERIOD.png)

    -   选择数据源的时间段。可用时间段由数据提供者设置。 “人口年龄组”图层只有一个时期，而“人口”图层具有 2000 年及以后的年度数据。降水数据以 5 天为周期提供，温度数据以 8 天为周期提供。

3.  在**ORG UNITS**标签中：

    ![](resources/images/maps/maps_ee_layer_dialog_ORG_UNITS.png)

    -   选择您希望在其中查看聚合数据值的组织单位。可以选择

        -   一个或多个特定的组织单元、层次结构中的组织单元级别、组织单元组，或

        -   组织单位层次结构中相对于用户的相对级别。通过选择**用户组织单位**，对于组织单位层次结构中不同级别的用户，地图数据将以不同的方式显示。

4.  在**样式**标签中

    ![](resources/images/maps/maps_ee_layer_dialog_STYLE.png)

    -   修改特定于图层类型的参数。

    -   根据需要调整图例范围，步长和颜色。

    -   如果您选择具有单点坐标（设施）的组织单位，您可以设置一个半径缓冲区来计算其中的数据值。 5000 米的半径将汇总距离设施 5 公里范围内的所有可用值。

5.  点击**添加图层**。

单击地图区域或设施以查看其聚合结果
组织单位。

### 数据值列表 { #listing-of-data-values }

地球引擎层有一个**数据表**选项，可以打开或
离层卡。

![](resources/images/maps/maps_ee_layer_data_table.png)

数据表显示所选组织单位的所有聚合值。

-   单击标题将根据该列对表格进行排序；在上升和下降之间切换。

-   在标题下方的过滤器字段中输入文本或表达式会将这些过滤器应用于数据，并且显示将根据过滤器进行调整。过滤器应用如下：

-   名称

    按包含给定文本的组织单位名称过滤

-   ID

    按包含给定文本的事件ID进行过滤

-   类型

    按包含给定文本的GIS显示类型过滤

-   聚合值

    每个选择的聚合类型都有一列

    数值数据值可以按给定的数字和/或范围过滤，例如：2,\>3&\<8

> **注意**
>
> 数据表过滤器是临时的，不会与地图图层一起保存。

## 添加外部地图图层 { #using_maps_external_map_layers }

![](resources/images/maps/maps_terrain_imagery.png)

外部地图图层表示为：

-   底图

    这些可在图层面板的**底图**卡中找到，并被选择为其他任何底图。

-   叠加层

    这些在**添加图层**选择中可用。与底图不同，可以将叠加层放置在任何其他叠加层的上方或下方。

叠加层由层中的附加层_cards_表示
面板如：

覆盖卡的顶部从左到右分别是：

-   抓取字段，允许使用鼠标拖动和重新排序图层

-   外部地图图层的标题

-   折叠和展开覆盖卡的箭头符号

如果图层有图例，则卡的中间是图例。

覆盖卡的底部从左到右分别是：

-   用于修改图层透明度的滑块

-   删除（垃圾桶）图标，用于从当前专题图中删除图层。

## 文件菜单 { #using_maps_file_menu }

![](resources/images/maps/maps_file_menu.png)

使用**文件”菜单**来管理您的地图。在打开或保存地图之前，将禁用几个菜单项。

保存您的地图可以轻松地在以后恢复它们。它还给你
有机会与其他用户分享它们作为解释或
把它放在仪表板上。您可以保存所有类型的图层配置
作为最爱。

### 建立新地图 { #create-a-new-map }

点击**文件** \> **新建**。

注意！这将清除您当前拥有的地图图层，而不进行保存。

### 开启新地图 { #open-a-new-map }

1.  点击**文件** \> **打开**。将打开一个对话框，其中包含地图列表。

2.  查找您要打开的收藏夹。您可以使用\ < and \>或搜索字段来查找已保存的地图。该列表将根据您输入的每个字符进行过滤。您可以通过选择**显示全部**，**由我创建**或**由其他人创建**来过滤列表。

3.  点击要打开的地图的名称。

### 保存地图 { #save-a-map }

创建地图后，可以方便地将其保存以备后用：

1.  单击**文件** \> **保存**。

2.  首次保存地图时输入**名称**（必填）和**描述**（可选）。

3.  点击**保存**。

### 保存地图副本 { #save-a-copy-of-a-map }

1.  单击**文件** \> **另存为... **

2.  输入地图的**名称**（必填）和**描述**（可选）。

3.  点击**保存**。

### 重命名地图 { #rename-a-map }

1.  点击**文件** \> **重命名**。

2.  为您的地图输入新的**名称**和/或**描述**。

3.  点击**重命名**。地图已更新。

### 翻译地图 { #translate-a-map }

1.  点击**文件** \>**翻译**。

2.  选择您的翻译的**地方语言**（语言）。

3.  输入翻译后的**名称**和**说明**。原始文本将显示在该字段下方。

4.  点击**保存**。

### 修改地图的共享设置 { #modify-sharing-settings-for-a-map }

创建并保存地图后，您可以与以下人员共享地图
每个人或一个用户组。要修改共享设置：

1.  点击**文件** \>**共享**。共享设置对话框打开。

2.  在文本框中，搜索您要与之共享最爱的用户或组的名称并选择它。

    所选的用户或组将添加到收件人列表中。

    重复该步骤以添加更多用户组。

3.  如果要允许外部访问，请选择相应的框。

4.  对于每个用户组，选择一个访问设置。选项包括：

    -   无（仅适用于默认组，因为它们无法删除）

    -   可以查看

    -   可以编辑和查看

5.  单击**关闭**以关闭对话框。

### 获取地图链接 { #get-the-link-to-a-map }

1.  点击**文件** \> **获取链接**。将打开一个链接对话框。

2.  复制链接。

### 删除地图 { #delete-a-map }

1.  点击**文件** \>**删除**。显示确认对话框。

2.  单击 **DELETE** 以确认您要删除收藏夹。您的地图将被删除，图层将从视图中清除。

## 地图解译 { #mapsInterpretation }

解释是对给定时间段内地图的描述。此信息在“仪表板应用程序”中可见。单击工作区右上方的**解释”**以打开**解释**面板。仅在保存了地图的情况下，该按钮才可单击。

![](resources/images/maps/maps_interpretations_panel.png)

### 查看基于相对期间的解释 { #view-interpretations-based-on-relative-periods }

要查看相对时期的解释，例如一年前：

1.  用解释打开收藏夹。

2.  单击工作区右上方的**解释**以打开解释面板。

3.  单击解释。您的地图会根据创建解释的时间显示数据和日期。要查看其他解释，请单击它们。

### 为地图写解释 { #write-interpretation-for-a-map }

要创建解释，您首先需要创建地图并保存。
如果您与其他人分享了您的地图，您的解释
write 对那些人是可见的。

1.  用解释打开收藏夹。

2.  单击工作区右上方的**解释**以打开解释面板。

3.  对于对收藏夹具有读取权限的用户，将出现一个带有占位符“写一个解释”的文本字段。

4.  在文本字段中，输入评论，问题或解释。您也可以使用' @username'提及其他用户。首先输入' @'，再加上用户名或真实姓名的首字母，然后出现一个提述栏，以显示可用的用户。提及的用户将收到内部DHIS2消息以及解释或评论。您可以在**仪表板应用程序**中查看解释。

5.  如果您希望您的解释与地图具有相同的共享设置，请单击**保存**。

    如果要更改共享设置（请参阅下文）以进行解释，请单击**保存并共享**。

### 更改解释的共享设置 { #change-sharing-settings-for-an-interpretation }

1.  单击一个解释（请参阅上面的查看解释）。

2.  单击解释下方的**共享**。共享设置对话框打开。

3.  搜索并添加要与之共享地图的用户和用户组。

4.  更改要修改的用户的共享设置：

    -   **可以编辑和查看**：每个人都可以查看和编辑对象。

    -   **只能查看**：每个人都可以查看对象。

    -   **无权访问**：公众无权访问该对象。此设置仅适用于公共访问。

5.  共享设置更新后，单击**关闭**。

## 将地图另存为图像 { #using_maps_image_export }

您可以通过单击顶部菜单中的“下载”按钮将地图下载为图像

![](resources/images/maps/maps_download.png)

Internet Explorer 或 Safari 不支持地图下载，我们建议您
使用谷歌浏览器或火狐浏览器。

1.  选择是否要包含地图名称。此选项仅在保存地图时可用。

2.  选择是否要包含地图图例。您可以将图例放置在地图的 4 个角之一。

3.  点击**下载**以下载地图。

## 搜索位置 { #using_maps_search }

地点搜索功能可让您搜索几乎任何位置
或地址。此功能可用于定位例如
地图上的地点、设施、村庄或城镇。

![](resources/images/maps/maps_place_search.png)

1.  在“地图”窗口的右侧，单击放大镜图标。

2.  输入您要查找的位置。

    键入时会显示匹配位置的列表。

3.  从列表中选择一个位置。大头针指示地图上的位置。

## 测量地图中的距离和面积 { #using_maps_measure_distance }

1.  在地图的左上角，将光标放在**测量距离和面积**（标尺）图标上，然后单击**创建新测量**。

2.  在地图上添加点。

3.  点击**完成测量**。

![](resources/images/maps/maps_measure_distance.png)

## 获取任意位置的纬度和经度 { #using_maps_latitude_longitude }

右键点击地图上的一个点，然后选择**显示经度/纬度**。值显示在弹出窗口中。

## 也可以看看 { #see-also }

-   [管理图例](https://docs.dhis2.org/master/en/user/html/manage_legend.html)

# 分析数据透视表中的数据 { #pivot }

## 关于数据透视表应用 { #pivot_about }

借助**数据透视表**应用，您可以基于DHIS2中的所有可用数据维度创建数据透视表。数据透视表是用于数据分析的动态工具，可让您根据数据的维度汇总和排列数据。 DHIS2中的数据维度示例如下：

-   数据维度本身（例如数据元素、指标和事件）

-   时间段（代表数据的时间段）

-   组织层次结构（表示数据的地理位置）

从这些维度中，您可以自由选择要包含在数据透视表中的_维度项目_。您可以使用组集功能在 DHIS2 中创建其他维度。这允许不同的聚合途径，例如按“合作伙伴”或设施类型的聚合。

数据透视表可以在 _columns_、_rows_ 和 _filters_ 上排列数据维度。当您在列上放置数据维度时，数据透视表将为每个维度项显示一列。如果您在列上放置多个数据维度，则数据透视表会为选定维度中项目的所有组合显示一列。当您将数据维度放在行上时，数据透视表会以类似的方式为每个维度项目显示一行。您选择作为过滤器的维度不会包含在数据透视表中，但会根据选定的过滤器项目聚合和过滤表数据。

> **提示**
>
> - 您必须在列或行上至少选择一个维度。
>
> - 您必须至少包含一个句点。
>
> - 数据元素组集和报告率不能出现在同一个数据透视表中。
>
> - 数据透视表不能包含超过系统设置中指定的最大分析记录数。最大记录数也可能受浏览器可用的最大 RAM 限制。如果您请求的表格超出特定大小，您将收到警告提示。在此提示中，您可以取消请求或继续构建表。考虑制作更小的表格，而不是一张将所有数据元素和指标一起显示的表格。
>
> - **数据透视表**应用程序支持期间和组织单位的向下和向上钻取。这意味着您可以在数据透视表中从年度期间向下钻取到季度、月和周。您还可以从全球组织单位向下钻取到国家、省和设施。

## 创建数据透视表 { #pivot_create }

1.  打开**数据透视表**应用。

2.  在左侧的菜单中，选择要分析的维度项，例如数据元素或指标。

3.  单击**布局**，然后将数据维排列为列，行和过滤器。

    您可以根据需要保留默认选择。

4.  点击**更新**。

在此示例中，指标被列为列，周期被列为行。

![](resources/images/pivot_table/basic_pivot.png)

### 选择尺寸项目 { #select-dimension-items }

左侧菜单列出了所有可用数据维度的部分。从
每个部分都可以选择任意数量的维度项。作为
例如，您可以打开数据元素部分并选择任何
可用列表中的数据元素数。您可以选择一个项目
通过标记它并单击部分标题中的箭头或简单地
双击该项目。在您可以使用数据维度之前
数据透视表您必须至少选择一个维度项目。如果你安排
一个维度作为列或行，但不选择任何维度项目，
维度被忽略。

您必须至少选择一种数据维度类型才能创建数据透视表
桌子。下表描述了可用的类型：

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
<td> 事件数据项 </td>
 <td>一个数据元素，它是表示已捕获事件的程序的一部分。 </td>
 <td>营养计划中儿童的平均体重和身高。 </td>
 </tr>
 <tr class="odd">
 <td>程序指示器</td>
 <td>基于表示事件的程序中的数据元素计算得出的公式。</td> 
 <td>营养计划中儿童的BMI平均得分。 </td>
 </tr>
 </tbody>
 </table>

您可以组合这些维度来显示例如聚合数据
与报告率，或事件数据项与程序
指标，都在同一个数据透视表中。对于“数据元素”数据
维度，您还可以选择“总计”和“详细信息”，
将允许您一起查看不同的类别组合选项
在同一个数据透视表上。

对于期间维度，您可以选择使用固定期间或
相对时期。固定时间段的一个示例是“2012 年 1 月”。至
选择固定期间首先从期间中选择期间类型
类型列表。然后，您可以从可用的列表中选择期间
期间。

相对期间是相对于当前日期的期间。示例
相对期间为“上个月”、“过去 12 个月”、“过去 5 年”。
可以通过勾选每个旁边的复选框来选择相对期间
时期。使用相对期间的主要优点是，当您
保存一个喜欢的数据透视表，它会保持最新数据的更新
随着时间的推移，无需不断更新它。

对于组织单位维度，您可以选择任意数量的
层次结构中的组织单位。选择所有组织单位
在特定上级组织单位下方，右键单击并单击“选择
所有子级”。要手动选择多个组织单位，请单击
单击组织单位时按住 **Ctrl** 键。你可以打勾
“用户组织单位”、“用户子单位”或“用户子 x2 单位”以便
动态插入一个或多个与您的组织单位相关的单位
用户帐号。这在您保存数据透视表收藏夹时很有用，并且
想与其他用户共享，因为组织单位与
查看收藏夹时将使用其他用户的帐户。

![](resources/images/pivot_table/period_dimension.png)

动态维度可以由组织单位组集、数据
元素组集或类别选项组集
配置为“分解”类型。一旦组集有
已配置，它们将在数据透视表中可用，并且
可以用作额外的分析维度，例如分析
按组织单位或实施伙伴的类型汇总数据。
动态尺寸与固定尺寸的工作方式相同。

> **提示**
>
> 一些动态维度可能包含许多项目。由于选择了许多维度成员时，由于URL的长度，这可能会导致某些浏览器的问题。一个特殊的“全部”复选框可用于动态维度，它允许您在数据透视表中隐式包含所有可用维度，而无需指定每个维度成员。

### 修改数据透视表布局 { #modify-pivot-table-layout }

选择数据维度后，是时候安排您的数据透视表了。
单击顶部菜单中的“布局”以打开布局屏幕。在这个画面
您可以将数据维度定位为表格列、行或过滤器
通过单击尺寸列表中的尺寸并将其拖到
相应的列、行和过滤器列表。您可以设置任意数量
任何列表中的维度。例如，您可以单击
“组织单位”并将其拖到行列表中以定位
组织单位维度作为表行。注意指标，
数据元素和数据集报告率是共同“数据”的一部分
维度并将一起显示在数据透视表中。为了
例如，在左侧菜单中选择指标和数据元素后，
您可以将“组织单位”从可用维度列表中拖到
行维度列表，以便将它们排列为枢轴中的行
桌子。

![](resources/images/pivot_table/table_layout.png)

设置数据透视表后，您可以单击“更新”进行渲染
您的数据透视表，或单击“隐藏”以隐藏布局屏幕而没有任何
更改生效。由于我们在我们的示例中同时选择了
期间和组织单位维度作为行，数据透视表将
生成这些维度中项目的所有组合并生成一个
像这样的表：

![](resources/images/pivot_table/pivot_rows.png)

## 更改数据透视表的显示 { #pivot_change_display }

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

将您的图表或数据透视表保存为收藏夹，便于查找
他们后来。您还可以选择与其他用户共享它们作为
解释或显示在仪表板上。

您可以在**数据透视表**，**数据可视化器**，**事件可视化器**，**事件报告**应用中查看收藏夹的详细信息和解释。使用**收藏夹**菜单来管理您的收藏夹。

### 打开收藏夹 { #open-a-favorite }

1.  点击**收藏夹** \> **打开**。

2.  在搜索字段中输入收藏夹的名称，或单击 **Prev** 和 **Next** 以显示收藏夹。

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

    可以通过使用 Markdown 样式标记 \* 和 \_ 分别为 **bold** 和 _italic_ 来格式化文本为 **bold** 和 _italic_。键盘快捷键也可用：Ctrl/Cmd + B 和 Ctrl/Cmd + I。支持一组有限的表情符号，可以通过键入以下字符组合之一来使用：:) :-) :( :-( :+ 1 :-1. URL 被自动检测并转换为可点击的链接。

3.  搜索您想与之分享您最爱的用户组，然后单击 **+** 图标。

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

    -   **在此应用中打开**：您将获得收藏夹的 URL，您可以通过电子邮件或聊天与其他用户分享。

    -   **在 web api 中打开**：您将获得 API 资源的 URL。默认情况下，这是一个 HTML 资源，但您可以将文件扩展名更改为“.json”或“.csv”。

### 删除收藏夹 { #delete-a-favorite }

1.  点击**收藏** \> **删除**。

2.  点击**确定**。

### 查看基于相对期间的解释 { #view-interpretations-based-on-relative-periods }

要查看相对时期的解释，例如一年前：

1.  用解释打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击解释。您的图表根据创建解释的时间显示数据和日期。要查看其他解释，请单击它们。

## 从数据透视表下载数据 { #pivot_download_data }

### 下载表格布局数据格式 { #download-table-layout-data-format }

要下载当前数据透视表中的数据：

1.  点击**下载**。

2.  在**表格布局**下，单击您要下载的格式：Microsoft Excel，CSV或HTML。

    数据表每个维度有一列，并包含维度项的名称。

    > **Tip**
    >
    > When you download a pivot table with organisation units as rows and you've selected **Show hierarchy** in **Table options**, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.

> **提示**
>
> 您可以从下载的 Excel 文件在 Microsoft Excel 中创建数据透视表。

### 下载纯数据源格式 { #download-plain-data-source-format }

您可以下载 JSON、XML、Excel 格式的当前数据透视表中的数据，
和 CSV 作为具有不同标识方案（ID、
代码和名称）。数据文档使用维度的标识符
项目并在新的浏览器窗口中打开以显示项目的 URL
地址栏中的 Web API 请求。这对开发人员很有用
基于 DHIS2 Web API 的应用程序和其他客户端模块
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

可以直接下载CSV格式的数据，无需渲染数据
在网络浏览器中。这有助于减少系统中的任何约束
已设置的关于最大数量的设置
分析记录。这使您可以下载更大批量的数据
可用于以后的离线分析。

以 CSV 格式下载数据，而无需先在 Web 中呈现数据
浏览器：

1.  单击**更新**旁边的箭头。

    ![](resources/images/pivot_table/data_dump.png)

2.  单击** CSV **以根据ID属性下载格式。

    该文件下载到您的计算机。

    > **Tip**
    >
    > You can also download CSV format based on **Code** or **Name** property.

## 在外部网页中嵌入数据透视表 { #pivot_embed }

DHIS2 中某些与分析相关的资源，如数据透视表、图表和地图，可以使用插件嵌入到任何网页中。您将在_DHIS2 开发人员手册_ 的 Web API 章节中找到有关插件的更多信息。

生成可用于显示数据透视表的 HTML 片段
在外部网页中：

1.  点击**嵌入**。

2.  单击**选择**以突出显示HTML片段。

## 将数据透视表数据可视化为图表或地图 { #pivot_integration }

制作数据透视表后，您可以在数据透视表之间切换，
数据的图表和地图可视化。

### 打开数据透视表作为图表 { #open-a-pivot-table-as-a-chart }

1.  单击**图表** \> **以图表形式打开此表**。

    当前的数据透视表将以图表的形式打开。

![](resources/images/pivot_table/pivot_integration.png)

### 打开数据透视表选择作为图表 { #open-a-pivot-table-selection-as-a-chart }

如果您想将数据透视表的一小部分可视化为图表，您可以
可以直接点击表格中的一个值而不是打开整个
桌子。

1.  在数据透视表中，单击一个值。

        ![](resources/images/pivot_table/pivot_integration_table.png)

2.  要验证选择，请将光标悬停在**按图表打开选择**上。表格中突出显示的维度标题指示将哪些数据可视化为图表。

3.  点击**打开选择为图表**。

### 打开数据透视表作为地图 { #open-a-pivot-table-as-a-map }

1.  点击**图表** \> **以地图形式打开该表格**

    当前的数据透视表将作为地图打开。

### 打开数据透视表选择作为地图 { #open-a-pivot-table-selection-as-a-map }

1.  在数据透视表中，单击一个值。

    显示菜单。

2.  点击**将选择作为地图打开**。

    您的选择将作为地图打开。

# 使用事件报告应用 { #event_reports_app }

## 关于事件报告应用 { #event_reports_about }

![](resources/images/event_report/event_report.png)

使用**事件报告**应用程序，您可以分析两种类型的报告中的事件：

-   聚合事件报告：具有聚合事件数量的数据透视表式分析

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

    3.  通过双击它们的名称来选择您需要的数据元素。

        数据元素可以按类型（数据元素、程序属性、程序指示符）进行过滤，并添加前缀以使其易于识别。

        After selecting a data element, it is visible under **Selected data items**.

    4.  （可选）对于每个数据元素，使用“大于”、“在”或“等于”等运算符以及过滤器值指定过滤器。

2.  选择期间。

    1.  点击**期间**。

    2.  选择一个或多个期间。

        您有三个期间选项：相对期间、固定期间和开始/结束日期。您可以在同一图表中组合固定期间和相对期间。您不能将固定期间和相对期间与同一图表中的开始/结束日期结合起来。重叠的时段被过滤，以便它们只出现一次。

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
> 连续值类型（实数/十进制数）的数据元素只能用作过滤器，并在布局对话框中自动定位为过滤器。这样做的原因是连续数字不能分组到合理的范围内并用于列和行。

1.  Click **Layout**.

2.  将尺寸拖放到适当的空间。

3.  点击**更新**。

## 更改表格的显示 { #event_reports_change_display }

您可以自定义事件报告的显示。

1.  点击**选项**。

2.  根据需要设置选项。聚合事件报告和单个事件报告之间的可用选项不同。

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

2.  在搜索字段中输入收藏夹的名称，或单击 **Prev** 和 **Next** 以显示收藏夹。

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

    可以通过使用 Markdown 样式标记 \* 和 \_ 分别为 **bold** 和 _italic_ 来格式化文本为 **bold** 和 _italic_。键盘快捷键也可用：Ctrl/Cmd + B 和 Ctrl/Cmd + I。支持一组有限的表情符号，可以通过键入以下字符组合之一来使用：:) :-) :( :-( :+ 1 :-1. URL 被自动检测并转换为可点击的链接。

3.  搜索您想与之分享您最爱的用户组，然后单击 **+** 图标。

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

    -   **在此应用中打开**：您将获得收藏夹的 URL，您可以通过电子邮件或聊天与其他用户分享。

    -   **在 web api 中打开**：您将获得 API 资源的 URL。默认情况下，这是一个 HTML 资源，但您可以将文件扩展名更改为“.json”或“.csv”。

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

# 使用事件可视化器应用 { #event_visualizer_app }

## 关于事件可视化器应用 { #about-the-event-visualizer-app }

![](resources/images/event_visualizer/event_visualizer.png)

With the **Event Visualizer** app, you can create charts based on event data.

## 创建图表 { #create-a-chart }

1.  \<Open the **Event Visualizer** app and select a chart type.

2.  在左侧菜单中，选择要分析的元数据。

3.  Click **Layout** and arrange the dimensions.

    您可以根据需要保留默认选择。

4.  点击**更新**。

## 选择图表类型 { #select-a-chart-type }

The **Event Visualizer** app has eight different chart types, each with different characteristics. To select a chart type:

1.  In **Chart type**, click the chart type you need.

    <table>
    <caption>Chart types</caption>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 66%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Chart type</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Column chart</p></td>
    <td><p>Displays information as vertical rectangular columns with lengths proportional to the values they represent.</p>
    <p>Useful when you want to, for example, compare performance of different districts.</p></td>
    </tr>
    <tr class="even">
    <td><p>Stacked column chart</p></td>
    <td><p>Displays information as vertical rectangular columns, where bars representing multiple categories are stacked on top of each other.</p>
    <p>Useful when you want to, for example, display trends or sums of related data elements.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Bar chart</p></td>
    <td><p>Same as column chart, only with horizontal bars.</p></td>
    </tr>
    <tr class="even">
    <td><p>Stacked bar chart</p></td>
    <td><p>Same as stacked column chart, only with horizontal bars.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Line chart</p></td>
    <td><p>Displays information as a series of points connected by straight lines. Also referred to as time series.</p>
    <p>Useful when you want to, for example, visualize trends in indicator data over multiple time periods.</p></td>
    </tr>
    <tr class="even">
    <td><p>Area chart</p></td>
    <td><p>Is based on line chart, with the space between the axis and the line filled with colors and the lines stacked on top of each other.</p>
    <p>Useful when you want to compare the trends of related indicators.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Pie chart</p></td>
    <td><p>Circular chart divided into sectors (or slices).</p>
    <p>Useful when you want to, for example, visualize the proportion of data for individual data elements compared to the total sum of all data elements in the chart.</p></td>
    </tr>
    <tr class="even">
    <td><p>Radar chart</p></td>
    <td><p>Displays data on axes starting from the same point. Also known as spider chart.</p></td>
    </tr>
    </tbody>
    </table>

2.  点击**更新**。

## 选择尺寸项目 { #event_visualizer_select_dimensions }

事件图表始终基于程序，您可以进行分析
基于一系列维度。对于具有类别组合的程序，
您可以使用程序类别和类别选项组集作为
表格和图表的维度。每个维度项可以有一个
相应的过滤器。您从左侧选择维度项目
菜单。

1.  选择数据元素：

    1.  点击**数据**。

    2.  选择一个程序和一个程序阶段。

        The data elements associated with the selected program are listed under **Available**. Each data element acts as a dimension.

    3.  通过双击它们的名称来选择您需要的数据元素。

        数据元素可以按类型（数据元素、程序属性、程序指示符）进行过滤，并添加前缀以使其易于识别。

        After selecting a data element, it is visible under **Selected data items**.

    4.  （可选）对于每个数据元素，使用“大于”、“在”或“等于”等运算符以及过滤器值指定过滤器。

2.  选择期间。

    1.  点击**期间**。

    2.  选择一个或多个期间。

        您有三个期间选项：相对期间、固定期间和开始/结束日期。您可以在同一图表中组合固定期间和相对期间。您不能将固定期间和相对期间与同一图表中的开始/结束日期结合起来。重叠的时段被过滤，以便它们只出现一次。

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

## 选择系列，类别和过滤器 { #select-series-category-and-filter }

您可以定义要显示为系列的数据维度，
类别和过滤器。每个数据元素都显示为单独的维度
并且可以放置在任何轴上。系列和类别面板可以
当时只有一维。

> **注意**
>
> 连续值类型（实数/十进制数）的数据元素只能用作过滤器，并在布局对话框中自动定位为过滤器。这样做的原因是连续数字不能分组到合理的范围内并用于列和行。

1.  Click **Layout**.

2.  将尺寸拖放到适当的空间。每个部分只能有一个维度。

3.  点击**更新**。

## 更改图表的显示 { #event_visualizer_change_display }

您可以自定义事件报告的显示。

1.  点击**选项**。

2.  根据需要设置选项。

    <table>
    <caption>Chart options</caption>
    <colgroup>
    <col style="width: 28%" />
    <col style="width: 28%" />
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
    <td><p><strong>Show values</strong></p></td>
    <td><p>Displays values as numbers on top of each series.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Use 100% stacked values</strong></p></td>
    <td><p>Displays 100 % stacked values in column charts.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Use cumulative values</strong></p></td>
    <td><p>Displays cumulative values in line charts.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide n/a data</strong></p></td>
    <td><p>Hides data tagged as N/A from the chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful when you want for example to exclude partial events in indicator calculations.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty categories</strong></p></td>
    <td><p>Hides the category items with no data from the chart.</p>
    <p><strong>None</strong>: doesn't hide any of the empty categories</p>
    <p><strong>Before first</strong>: hides missing values only before the first value</p>
    <p><strong>After last</strong>: hides missing values only after the last value</p>
    <p><strong>Before first and after last</strong>: hides missing values only before the first value and after the last value</p>
    <p><strong>All</strong>: hides all missing values</p>
    <p>This is useful for example when you create column and bar charts.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Trend line</strong></p></td>
    <td><p>Displays the trend line which visualizes how your data evolves over time. For example if performance is improving or deteriorating. Useful when periods are selected as category.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Target line value/title</strong></p></td>
    <td><p>Displays a horizontal line and title (optional) at the given domain value. Useful for example when you want to compare your performance to the current target.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Base line value/title</strong></p></td>
    <td><p>Displays a horizontal line and title (optional) at the given domain value. Useful for example when you want to visualize how your performance has evolved since the beginning of a process.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Sort order</strong></p></td>
    <td><p>Allows you to sort the values on your chart from either low to high or high to low.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Output type</strong></p></td>
    <td><p>Defines the output type. The output types are <strong>Event</strong>, <strong>Enrollment</strong> and<strong>Tracked entity instance</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Program status</strong></p></td>
    <td><p>Filters data based on the program status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong> or <strong>Cancelled</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Event status</strong></p></td>
    <td><p>Filters data based on the event status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong>, <strong>Scheduled</strong>, <strong>Overdue</strong> or <strong>Skipped</strong>.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Axes</strong></p></td>
    <td><p><strong>Range axis min/max</strong></p></td>
    <td><p>Defines the maximum and minimum value which will be visible on the range axis.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Range axis tick steps</strong></p></td>
    <td><p>Defines the number of ticks which will be visible on the range axis.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Range axis decimals</strong></p></td>
    <td><p>Defines the number of decimals which will be used for range axis values.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Range axis title</strong></p></td>
    <td><p>Type a title here to display a label next to the range axis (also referred to as the Y axis). Useful when you want to give context information to the chart, for example about the unit of measure.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Domain axis title</strong></p></td>
    <td><p>Type a title here to display a label below the domain axis (also referred to as the X axis). Useful when you want to give context information to the chart, for example about the period type.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>General</strong></p></td>
    <td><p><strong>Hide chart legend</strong></p></td>
    <td><p>Hides the legend and leaves more room for the chart itself.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide chart title</strong></p></td>
    <td><p>Hides the title (default or custom) of your chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Chart title</strong></p></td>
    <td><p>Type a title here to display a custom title above the chart. If you don't enter a title, the default title is displayed.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide chart subtitle</strong></p></td>
    <td><p>Hides the subtitle of your chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Chart subtitle</strong></p></td>
    <td><p>Type a subtitle here to display a custom subtitle above the chart but below the title. If you don't enter a subtitle, no subtitle is displayed in the chart.</p></td>
    </tr>
    </tbody>
    </table>

3.  点击**更新**。

## 将图表下载为图像或PDF { #download-a-chart-as-an-image-or-a-pdf }

创建图表后，您可以将其下载到本地
计算机作为图像或 PDF 文件。

1.  点击**下载**。

2.  在**图形**下，单击** PNG（.png）**或** PDF（.pdf）**。

    该文件会自动下载到您的计算机。例如，现在您可以将图像文件作为报告的一部分嵌入到文本文档中。

## 下载图表数据源 { #download-chart-data-source }

您可以下载 HTML、JSON、XML 格式的图表背后的数据源，
Microsoft Excel 或 CSV 格式。数据文档使用以下标识符
维度项并在新的浏览器窗口中打开以显示 URL
地址栏中对 Web API 的请求。这对
基于 DHIS2 Web API 的应用程序和其他客户端模块的开发人员
或者对于那些需要计划数据源的人，例如用于导入
进入统计包。

要下载纯数据源格式：

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

2.  在搜索字段中输入收藏夹的名称，或单击 **Prev** 和 **Next** 以显示收藏夹。

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

    可以通过使用 Markdown 样式标记 \* 和 \_ 分别为 **bold** 和 _italic_ 来格式化文本为 **bold** 和 _italic_。键盘快捷键也可用：Ctrl/Cmd + B 和 Ctrl/Cmd + I。支持一组有限的表情符号，可以通过键入以下字符组合之一来使用：:) :-) :( :-( :+ 1 :-1. URL 被自动检测并转换为可点击的链接。

3.  搜索您想与之分享您最爱的用户组，然后单击 **+** 图标。

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

    -   **在此应用中打开**：您将获得收藏夹的 URL，您可以通过电子邮件或聊天与其他用户分享。

    -   **在 web api 中打开**：您将获得 API 资源的 URL。默认情况下，这是一个 HTML 资源，但您可以将文件扩展名更改为“.json”或“.csv”。

### 删除收藏夹 { #delete-a-favorite }

1.  点击**收藏** \> **删除**。

2.  点击**确定**。

### 查看基于相对期间的解释 { #view-interpretations-based-on-relative-periods }

要查看相对时期的解释，例如一年前：

1.  用解释打开收藏夹。

2.  单击工作区右上方的** \> \> \> **。

3.  单击解释。您的图表根据创建解释的时间显示数据和日期。要查看其他解释，请单击它们。

## 将图表可视化为数据透视表 { #visualize-a-chart-as-a-pivot-table }

制作图表后，可以将其作为数据透视表打开：

单击**图表** \> **以表形式打开此图表**。

# 报告应用程序中的报告功能 { #using_the_reports_app }

该报告应用程序可用于罐装，标准报告，数据集报告，资源和组织单位分布报告。

## 使用标准报告 { #standard_reports_in_the_beta_reports_app }

您可以通过导航到 Apps-\>Reports 来访问可用的报告。在里面
在左侧栏中的报告菜单中，单击标准报告。所有的清单
预定义的报告将出现在主窗口中。

![](resources/images/dhis2UserManual/react_reports_app_standard_reports.png)

您可以通过单击报告的三点图标来运行/查看报告，然后
从上下文菜单中选择“创建”。如果有任何
预定义的参数，您将看到一个报告参数窗口，您可以在其中
必须填写组织单位和/或报告月份所需的值，
取决于在基础报告表中定义的内容。
准备好后，单击“生成报告”。报告要么出现
直接在您的浏览器中或作为 PDF 文件下载，
取决于您处理 PDF 文件的浏览器设置。你可以保存
文件并将其保存在本地计算机上以备后用。

## 使用数据集报告 { #dataset_reports_in_the_beta_reports_app }

数据集报告是数据输入屏幕的打印机友好视图，其中填充了原始数据或汇总数据。

您可以从Apps-> Reports访问数据集报告。

将出现一个标准窗口，您可以在其中填写您的详细信息
报告：

**数据集：**您要显示的数据集。

**报告期间：** 您想要数据的实际期间。这可以是
聚合期和原始期。这意味着您可以要求
季度或年度报告，即使收集了数据集
每月。数据集的周期类型（收集频率）定义在
数据集维护。首先选择期间类型（Monthly、Quarterly、
每年等）在 Prev 和 Next 按钮旁边的下拉菜单中，然后
从下面的下拉列表中选择一个可用的时间段。用
Prev 和 Next 可向后或向前跳跃一年。

**仅使用所选单位的数据：** 如果您想要一个
报告有孩子的组织单位，但只想要数据
直接为本单位收集的数据，而不是其收集的数据
孩子们。如果您想要一个组织单位的典型汇总报告，您可以
不想勾选这个选项。

**报告组织单位：** 在这里选择你想要的组织单位
的报告。这可以在层次结构中的任何级别作为数据
将自动聚合到此级别（如果您不勾选
上面的选项）。

填写完报告标准后，单击
“产生”。该报告将以 HTML 格式以打印机友好的格式显示。
使用浏览器中的打印和另存为功能进行打印或保存（如
HTML) 报告。您还可以在 Excel 中导出数据集报告和
PDF 格式。

## 使用报告率摘要 { #reporting_rate_summary_in_the_beta_reports_app }

从应用程序-\>报告菜单访问报告率摘要。
报告率摘要将显示有多少数据集（表格）
由组织单位和时间提交。

报告率是根据完整的数据集注册计算得出的。
完整的数据集注册是指用户将数据输入表单标记为
完成，通常通过单击数据输入屏幕中的完成按钮，
特此向系统表明她认为该表格是
完全的。这是一种主观的计算方法
完整性。

报告率摘要将为每一行显示一系列度量：

-   实际报告：表示相关数据集的数据输入完成注册数。

-   预期报告：指示预期有多少数据输入完成注册。此数字基于相关数据集已分配到的组织单位的数量（已启用数据输入）。

-   报告率：根据预期数量登记为完整的报告的百分比。

-   及时报告：与实际报告相同，仅在报告期结束后的最大天数内登记为完整的报告。可以在数据集管理中为每个数据集定义报告期之后的天数。

-   报告准时率：与百分比相同，仅作为分子记录为按时完成的报告。

要运行报告，您可以按照以下步骤操作：

-   从树中选择一个组织单位。

-   选择一个数据集。

-   从该期间类型的可用期间列表中选择期间类型和期间。

-   然后将呈现报告。更改上面的任何参数，然后再次单击“获取报告”查看相应的结果。

![](resources/images/dhis2UserManual/react_reports_app_reporting_rate_summary.png)

## 使用资源 { #resources_in_the_beta_reports_app }

资源工具允许您从本地上传这两个文件
计算机到 DHIS 服务器并添加到其他资源的链接
通过 URL 上网。如果您的系统配置了云存储，
资源将保存在那里。

要创建新资源：

1.  打开**报告**应用，然后单击**资源**。

2.  点击**添加新**。

3.  输入一个**名称**。

4.  选择**类型**：**上传文件**或**外部URL**。

5.  点击**保存**。 

## 使用组织单位分布报告 { #orgunit_distribution_reports_in_the_beta_reports_app }

您可以从左侧菜单访问 Orgunit Distribution 报告
在应用程序-\>报告中。

组织单位分布报告是显示组织单位如何
分布在各种属性上，如类型和所有权，以及
地理区域。

结果可以显示在基于表的报告或图表中。

**运行报告：**

要运行报告，首先在左上角的组织单位中选择一个组织单位
树。该报告将基于位于所选
单位。选择要使用的组织单位组集，
通常这些是类型、所有权、农村/城市，但可以是任何
用户定义的组织单位组集。您可以单击获取报告
获取基于表格的演示或获取图表以获得相同的结果
在图表中。您还可以将基于表格的报告下载为 Excel 或
CSV。

![](resources/images/dhis2UserManual/react_reports_app_org_unit_dist.png)

# 讯息传递 { #messages }

## 关于消息和反馈消息 { #about-messages-and-feedback-messages }

![](resources/images/messaging/view_inbox.png)

在 DHIS2 中，您可以向用户发送消息和反馈消息，用户
团体和组织单位。当您发送反馈消息时，它是
路由到称为反馈接收者组的特定用户组。
如果您是该用户组的成员，您可以访问反馈
处理工具。例如，您可以设置传入的状态
在您等待信息时向“待定”反馈。

除了用户对用户和反馈消息外，取决于您的
配置系统还会向您发送系统生成的消息。
这些消息可以由不同的事件触发，包括系统
或后台作业失败和验证分析结果。反馈
处理工具也可用于验证结果和
优先级将设置为违反验证规则的重要性。

要访问该应用程序，请点击标**题栏中的消息图标**或在应用程序搜索框中找到**消息传递**应用程序。

> **注意**
>
> 消息和反馈消息不会发送到用户的电子邮件地址，消息仅出现在 DHIS2 中。
>
> 在 2.30 中，我们引入了一个新的消息传递应用程序，它提供了更丰富的消息传递体验。具体来说：
>
> - 通过单击右上角的图标在列表视图和紧凑视图之间切换。
>
> - 列表视图非常简单，可以很好地概述所有消息，特别适合反馈和验证消息。
> - 紧凑视图是一种查看消息的现代方式，用户在一个视图中拥有更多信息，因此查看和回复多条消息更容易。
>
> 此部分的第一个屏幕截图显示列表视图，而**阅读消息**部分的屏幕截图显示紧凑视图。
>
> - 添加了一个新的搜索字段，使用户能够搜索消息。搜索过滤不同消息属性的消息；主题、文本和发件人。这意味着您可以通过输入搜索来缩小消息对话列表的范围。
>
> - 添加了自动刷新功能，以便应用以设定的时间间隔（每 5 分钟一次）获取新消息。默认情况下禁用此功能。
>
> - 对于每个消息对话，您都可以将参与者添加到对话中。如果您想对特定对话进行输入，或者如果有人也应该看到信息，这将非常有用。无法从对话中删除参与者。

## 建立讯息 { #create-a-message }

![](resources/images/messaging/create_private_message.png)

1.  点击**撰写**。

2.  定义您希望接收消息的人。您可以向组织单位、用户和用户组发送消息。

    -   在 **To** 字段中，您可以搜索组织单位、用户和用户组并选择所需的收件人。

3.  键入一个主题和一条消息。

4.  点击**发送**。

## 阅读讯息 { #read-a-message }

![](resources/images/messaging/read_message.png)

1.  在左侧选择适当的消息类型。

2.  单击一条消息。

    如果消息是对话的一部分，您将看到此对话中的所有消息。

## 创建反馈消息 { #create-a-feedback-message }

1.  按照创建消息的步骤进行操作，仅选择**反馈消息 **，而不输入收件人。

2.  该消息将被创建为反馈消息，并将出现在所有指定用户的 ** Ticket**文件夹中。

## 附件 { #attachments }

在 2.31 中，我们为消息引入了附件。创建时或
回复您可以添加的消息对话
附件。目前没有对类型或大小的限制
文件。

## 管理验证和反馈消息 { #manage-validation-and-feedback-messages }

> **注意**
>
> 如果您是设置为处理反馈消息的用户组的成员，您将只能看到反馈消息并可以访问扩展处理工具。
>
> 使用新应用程序，您可以通过查看消息或检查对话列表中的消息时出现的图标菜单来管理票证和验证消息的扩展工具。

### 选择所有消息 { #all-messages-selected }

![已选择所有消息](resources/images/messaging/view_validation_select_all.png)

### 选择所有邮件并选择扩展选择器 { #all-messages-selected-and-extended-choice-picker-selected }

![选择了所有消息并选择了扩展选择器](resources/images/messaging/view_validation_select_all_icon_menu.png)

您将收到反馈信息到**Ticket**文件夹，并收到确认消息到**Validation**文件夹。对于反馈和验证消息，除了消息选项外，还具有以下选项：

 <table style="width:100%;">
 <caption>反馈处理工具</caption>
 <colgroup>
 <col width="23%" />
 <col width="76%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th>功能</th>
 <th>说明</th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> <strong>优先级</strong> </p> </td>
 <td> <p>您可以标记具有不同优先级的反馈/验证消息：<strong>无</strong>，<strong>低</strong>，<strong>中</strong>或<strong>高</strong>， </p>
 <p>设置优先级可以更轻松地跟踪您首先需要解决的反馈消息以及可以等待的反馈消息。 </p> </td>
 </tr>
 <tr class="even">
 <td> <p><strong> 状态 </strong></p> </td>
 <td> <p>所有反馈/验证消息的状态均为创建后<strong>打开</strong>。 </p>
 <p>要跟踪现有的反馈消息，可以将状态更改为<strong>待处理</strong><strong>无效</strong>或<strong>已解决</strong>。</p>
 <p>您可以使用内部标题栏中的两个下拉菜单，根据反馈/验证消息的状态过滤反馈/验证消息。</p> </td>
 </tr>
 <tr class="odd">
 <td>  <p><strong>分配给</strong></p>  </td>
 <td><p>您可以将反馈消息分配给设置为处理反馈消息的用户组的任何成员。 </p>
 <p>您可以将验证消息分配给系统中的任何用户。 </p>
 <p><strong> -</strong>表示您尚未将用户分配给反馈消息。  </p></td>
 </tr>
 <tr class="even">
  <td><p><strong> 内部回复  </strong></p></td> 
<td><p>在反馈处理小组中工作时，您可能需要先讨论反馈，然后再将答案发送给发件人。您可以将此讨论与反馈本身保持在同一消息对话中。 </p>
 <p>要在反馈处理用户组中发送答复，请单击<strong>内部答复</strong>。 </p></td>
 </tr>
 </tbody>
 </table>

## 配置反馈信息功能 { #configure-feedback-message-function }

要配置反馈消息功能，您必须：

1.  创建包含应接收反馈消息的所有用户的用户组（例如“反馈消息收件人”）。

2.  打开**系统设置**应用程序，然后单击**常规**\>**反馈收件人**并选择您在上一步中创建的用户组。

# 设置用户帐户首选项 { #user_account_preferences }

在**用户设置**中，您可以更改DHIS2的显示语言和数据库的语言。数据库语言是元数据的翻译内容，例如数据元素和指示符。您还可以选择一种显示样式，并启用或禁用SMS和电子邮件通知。如果愿意，可以选择在分析模块中显示一个短名称，例如“ Joe”，而不是全名。

在**用户个人资料**中，您可以将个人信息添加到个人资料中，例如电子邮件地址，手机号码，出生日期，个人资料图片等。当您发送消息时，接收消息的人可以看到这些个人资料详细信息。您还可以提供系统将使用的各种直接消息传递服务的帐户名。

在**帐户设置**中，您可以重设密码并设置2-Factor身份验证。设置2-Factor身份验证将需要您在移动设备上下载Google Authenticator应用。

在**查看完整的个人资料**部分，您可以找到个人资料详细信息的摘要。本节包含一些您无法编辑的字段，例如用户角色和用户组织单位。

在**关于DHIS2**部分中，您找到有关DHIS2实例的详细信息列表。
