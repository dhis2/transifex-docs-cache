---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/stories/tanzania-integrated-health-information-architecture_B.md"
revision_date: '2021-06-14'
tags:
- 用户故事
---

# 坦桑尼亚：综合健康信息架构 { #user_story_udsm } 

## 关于此用例 { #about-this-use-case } 

**在此用例中，我们将研究如何实现的不同阶段
多个团队与达累斯萨拉姆大学（UDSM）合作，
卫生和社会福利部 (MoHSW) 以及新加坡大学
奥斯陆 (UiO) 将在以下地区实施综合卫生信息系统 (HIS)
坦桑尼亚大陆。吸取的主要经验教训是
逐步实施 HIS 以提供可持续的框架；
精简资源并促进合作；确保系统
灵活；促进数据所有权和数据共享；建筑
各级能力；尽早参与重大项目；和
投入时间和资源建立利益相关者社区。**

## 坦桑尼亚国家概况 { #tanzania-country-profile } 

坦桑尼亚联合共和国是东方最大的国家
非洲地区，人口4500万。它的组成是
两个国家：半自治岛屿桑给巴尔岛和坦噶尼喀岛，或
坦桑尼亚大陆。坦桑尼亚大陆分为25个行政区
地区分为 167 个区议会。各区
议会分为部门、区、村庄/街道。有
根据 SARA 的数据，大约每 8000 人就有 1 个医疗机构
（2012）。


![来源：BBC 非洲新闻 ©
2016](resources/images/use_cases/new_map_tanzania.png)

由于地区和地区之间存在巨大差异
地理、历史、人口和基础设施，某些领域
坦桑尼亚没有可靠的道路、电力或互联网。

## 从多种工具转移到统一系统 { #moving-from-multiple-tools-to-a-unified-system } 

### 在DHIS2之前 { #before-dhis2 } 

坦桑尼亚大陆的第一个 HIS 始于 90 年代，当时是纸质系统
在卫生机构和地区办事处使用。信息是
使用 Microsoft Access 数据库收集和处理。如果没有
资助机构聘请的外部顾问的干预，
没有任何策略通过升级或更新来维持系统
训练。

随着 HIS 需求的激增，MoHSW 面临着压力。
缺乏协调导致垂直项目各自为政
边。这造成了一种不可持续的局面，在这种情况下，我们的努力正在被
由于结果未收敛而重复。

2007年左右，一项名为“加强监测评估”的计划
该倡议由 MoSWH、UDSM、UiO 和其他合作伙伴发起。它的目标
是建立一个新的、集成的HIS，为客户提供可靠的数据
部委和其他利益相关者。一种新的纸质系统结合
DHIS2 推出。 <http://www.dhis2.org>

### 在坦桑尼亚引入综合性HIS { #introducing-an-integrated-his-in-tanzania } 

2010年，全面修订的HIS的适应和实施
开始了。这一过程是通过灵活的标准解决方案实现的
参与性方法在国家各级运作
健康系统。找到一个能够满足需求的解决方案非常重要
健康管理者、实施者、设计者和决策者的需求。

### 逐步的全国性HIS推广 { #a-gradual-national-his-rollout } 

2011年，普瓦尼沿海地区被用作试验场
基于纸质的数据收集工具和 DHIS2。在接下来的两年里，
修订后的系统已推广到其余 24 个区域
坦桑尼亚大陆的相关地区和卫生设施。在
完成本次推出后，我们的努力方向是
整合所有主要垂直项目，如疟疾、结核病/麻风病、
RCH、艾滋病毒/艾滋病纳入 DHIS2。随着实施过程的推进，
为执行伙伴、地区和
地区医院工作人员和 MoHSW 工作人员。

![](resources/images/use_cases/tanzania_rollout_phases_2014.png)

坦桑尼亚大陆 DHIS2 2014 年推出阶段

### 构建强大的HIS { #building-a-robust-his } 

以下是我们投入时间和资源的一些关键领域：

#### 开源哲学 { #open-source-philosophy } 

选择应用开源工具而不是通过
封闭的商业产品确保软件仍然存在
与更加多样化和灵活的设计范围进行协作。
此外，许多卫生部门利益攸关方的参与和
一个开源开发者社区暗示该系统将是
着眼于长期可持续发展而非短期
生命周期，取决于公司的付费维护服务。

#### 增量，灵活和可扩展的设计 { #incremental-flexible-and-scalable-design } 

DHIS2 是以渐进的方式实施的，而不是一次性实施。喜欢
问题可以在推出过程中直接解决，并且
直接响应用户反馈而实施。最明显的缺陷
因此很容易被发现，并且更加稳定和高效的系统
建造的。

#### 数据收集标准 { #standards-for-data-collection } 

我们使用了一套涵盖数据的通用数据收集标准
收集、报告、分析和质量程序和工具。全部
非正式工具被删除，重复条目的记录
数据下降。

#### 参与式设计 { #participatory-design } 

用户社区，例如 HIS 的经理、支持合作伙伴
和实施者交换电子邮件，在论坛和研讨会上发言
关于如何使软件更加用户友好。这有帮助
实施者微调他们的计划并确保 DHIS2 得到实施
最佳使用。

#### 行动主导型研究 { #action-led-research } 

在 UiO 和 UDSM 攻读博士和硕士学位课程的学生
进行了“以行动为主导的研究”，使他们能够参与
在进行研究的同时推出 DHIS2。通过这样做，他们学习并
记录了有关系统定制、用户支持的最佳实践，
培训和数据分析。

#### 地方能力建设 { #local-capacity-building } 

人们学会了对 DHIS2 软件进行故障排除，用户受到了鼓励
在许多不同的组织层面相互协助
角色。通过灌输主人翁意识和自给自足感，差距
因此减少了实施者和用户之间的关系。培训重点
DHIS2的软件使用、数据分析以及基本和高级功能
适用于健康和数据管理者。

#### 使用信息准则和标准 { #using-information-guidelines-and-standards } 

为了推动决策并实现国家健康目标，每年
计划目标和千年发展目标 (MDG)、创建的团队
有关如何有效生成和使用数据的流程。

#### DHIS2与其他系统的互操作性 { #interoperability-of-dhis2-with-other-systems } 

自2014年起，DHIS2已与其他软件系统集成，
使卫生工作者能够跨领域交叉、分析和共享数据
组织。以下是一些集成或制造的系统示例
可与 DHIS2 互操作：

##### eIDSR（电子综合疾病监控和响应） { #eidsr-electronic-integrated-disease-surveillance-and-response } 

eIDSR 是使用 USSD 技术从头开始开发的，并与
DHIS2 用于立即报告传染病数据。这
该工具旨在提高对疾病和疾病的检测和响应时间
在坦桑尼亚的所有医疗机构中使用。

##### HRHIS（健康信息系统人力资源） { #hrhis-human-resources-for-health-information-systems } 

HRHIS 的开发目的是报告所有内部的健康数据信息
坦桑尼亚的卫生设施。它有助于评估人力资源问题、管理
人力资源的分配，以及规划和评估人力资源干预措施。

##### MFL（主设备列表） { #mfl-master-facility-list } 

MFL 是一个医疗机构登记册，用于保存有关医疗机构的记录
配置文件。

##### eLMIS（物流管理信息系统） { #elmis-logistics-management-information-systems } 

eLMIS 是一个用于药品分销和库存的供应链系统
和其他商品。

#### 数据使用和意识解决方案 { #data-use-and-awareness-solutions } 

提高人们对数据使用、数据最佳实践的认识的解决方案
分析和数据传播已嵌入 DHIS2 中。这些
解决方案是：

##### 计分卡 { #scorecards } 

记分卡用于传达关键进展的状态
全球、区域和国家对具体指标的承诺。这
视觉指标的表现具有刺激行动者的作用
通过有效的政策和措施迅速应对形势
投资。


![](resources/images/use_cases/new_scorecards.png)

##### HMIS网站门户 { #hmis-web-portal } 

HMIS 门户网站由 MoHSW 托管并由卫生部门使用
利益相关者。公众也可以使用它。
<https://hmisportal.moh.go.tz/>


![](resources/images/use_cases/hmis_web_portal.png)

##### P4P（绩效工资）/ RBF（基于结果的财务） { #p4p-pay-for-performance-rbf-result-based-finance } 

奖励一个或多个人交付一项或多项产出或成果
激励措施可以是经济上的或其他方面的。 P4P/RBF 程序是
集成到 DHIS 2 中，使卫生服务提供商能够监控
他们的表现和报酬。

##### DHP / RHP（地区和区域健康状况） { #dhprhp-district-and-region-health-profile } 

为地区卫生提供规划和进度指导
管理团队。例如，它提供了地区健康状况的摘要
通过反映该地区优先健康指标的条件
人口健康状况、卫生系统状况和
卫生服务提供状况。

## 挑战 { #challenges } 

与任何大规模实施的大型项目一样，
由于医疗保健环境复杂，出现了许多挑战。

### 行政结构的意外变更 { #unforeseen-changes-to-the-administrative-structure } 

地区和区域行政边界经常更新。
新地区的建立产生了当地的新代表
人口数据。这种破坏对比较产生了影响
分析 HIS 数据，例如健康指标的表现。

### 减少独立程序 { #reducing-standalone-programs } 

减少现有独立程序的数量通常可以实现
通过展示单个程序的局限性，以及
强调 DHIS2 的潜力。但由于有些保留，
一些垂直项目仍然与 DHIS2 并行运行。

### 缺乏训练有素的人员和地域覆盖 { #lack-of-trained-personnel-and-geographical-coverage } 

缺乏具备足够 HIS 技能的人才有时会造成严重影响
关于实施和扩大 DHIS2 从试点地区到整个地区
国家。坦桑尼亚在 168 个地区拥有 7000 多个医疗机构
理事会。

## 结果 { #the-outcome } 

DHIS2 现已成为整个坦桑尼亚认可的标准系统
被认可如下：

  - 加强健康的综合电子医疗架构
    数据收集，改进分析、使用和协调
    数据和利益相关者。

  - 超过 150 万个数据条目正在被收集并添加到
    国家数据仓库每月一次，使用调制解调器、宽带
    局域网和 VSAT。

  - 多种可靠的集成工具可帮助改进
    基于证据的决策（例如记分卡、仪表板、
    P4P）。

  - 由社区发起的开放获取倡议（HMIS 门户网站）
    的利益相关者。

  - 改进数据验证和质量检查以实现更好的监控
    和健康计划评估。

## 学到了什么？ { #what-are-the-lessons-learned } 

以下是从滚动经验中学到的一些重要教训
以可持续的方式推出 DHIS2。

### 应用渐进式流程 { #apply-a-gradual-incremental-process } 

该系统必须灵活且适应性强，以满足新出现的需求。经过
从之前的迭代中学习，可以扩展
系统到其他地区。

### 制定并批准一项全面的国家计划 { #develop-and-endorse-a-comprehensive-national-plan } 

节省资源并防止重复的风险
在部署 DHIS2 之前，努力精简所有资源和 HIS
所有利益相关者的活动，并以 MoHSW 作为牵头组织。

### 建立可信赖的关系 { #establish-a-trustworthy-relationship } 

促进 MoHSW 内的系统和数据所有权。鼓励数据
在卫生计划和利益相关者之间共享，以帮助制定
对常规 HIS 以及其资源和能力的信任感
可以支持一下。

### 在国家，地区和地方各级进行能力建设 { #build-capacity-at-national-regional-and-local-levels } 

可靠的系统由训练有素且知识渊博的人员维护
人们。能力建设需要成为一项持续的战略。容量为
系统开发、维护和信息使用所需的
确保系统每天正常运行并生成信息
用于健康管理、规划和决策。

### 让其他健康计划参与 { #get-other-health-programs-involved } 

主要的卫生项目有艾滋病毒/艾滋病、妇幼保健（MCH）、
疟疾和结核病。在 HMIS 中获取此类大型程序
早期阶段是激发其他项目兴趣的一种手段，
相关利益相关者。

### 将适当的时间和资源分配给您的程序 { #dedicate-the-right-amount-of-time-and-resources-to-your-program } 

花费了大量的时间和精力将垂直项目整合到
HIS/DHIS2平台并逐步推出HIS。今天我们已经
建立了一个由拥有共同共同点的利益相关者组成的大型社区
有兴趣为未来构建可持续的 HIS/DHIS2 平台
几代人使用和发展。

