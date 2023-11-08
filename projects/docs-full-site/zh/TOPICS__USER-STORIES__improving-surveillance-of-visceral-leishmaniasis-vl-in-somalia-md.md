---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/stories/dhis2-tracker-improving-surveillance-of-visceral-leishmaniasis-vl-in-somalia-draft.md"
revision_date: '2021-06-14'
tags:
- 用户故事
---

# DHIS2跟踪器可改善索马里内脏利什曼病（VL）的监视-草稿 { #user_story_vl_who } 

## 利什曼病-什么？ { #leishmaniasis-what-is-it } 

利什曼病是一种由“原生动物”引起的疾病
寄生虫”。 [原生动物](https://www.cdc.gov/parasites/about.html) 是
能够在人类体内繁殖的微观单细胞生物，
造成严重感染。利什曼病通过以下途径传播给人类
被感染的雌性白蛉叮咬。

![](resources/images/use_cases/vl_who_sandfly2.jpg)

这种疾病最严重的形式称为**内脏利什曼病（VL）**，
它在 80 多个国家流行。人们通常会遭受
不规则发热、体重减轻、脾脏肿大
肝病、贫血。

## 谁受内脏利什曼病（VL）影响？ { #who-is-affected-by-visceral-leishmaniasis-vl } 

这种疾病影响着地球上一些最贫穷的人。这是
与营养不良、人口流离失所、住房条件恶劣有关
免疫系统薄弱且缺乏财政资源。最多的情况是
发现于印度次大陆和东非，估计在那里
每年发生 200, 000 – 400, 000 个新病例。约占所有新病例的 90%
巴西、埃塞俄比亚、印度、索马里、南苏丹和
苏丹。如果不及时治疗，VL 将在两年内杀死一个人
95%以上的病例都会发病。 *来源：[被忽视
热带病](http://www.who.int/neglected_diseases/diseases/en/),
世界卫生组织，2017 ©*

## 在索马里处理VL { #tackling-vl-in-somalia } 

VL 的诊断和治疗并不容易。在流行国家，仅
很少有卫生机构拥有训练有素的卫生工作者和设备
进行正确的诊断和病例管理。有能力去
准确绘制 VL 病例的分布图并计算发病率和
处于危险中的人群，有几个因素发挥作用：

  - 确定资源的目标卫生设施
    （培训、设备、药物、诊断测试）、

  - 将病例分配到可能的感染地点（或至少
    居住地），而不是该人目前所在的地方
    治疗。

## 正在进行的由世卫组织支持的培训和监测计划{正在进行的由谁支持的培训和监测计划} { #ongoing-who-supported-training-and-surveillance-programs } 

鉴于该国困难的情况，索马里做得很好
在 VL 监测方面。 2013年以来，卫生部
在世界卫生组织和索马里SOS的支持下，培训了来自索马里的卫生工作者
三个卫生机构负责 VL 诊断、病例管理和数据
收藏。

在 Excel 电子表格中收集每个 VL 案例的单独数据
并与中央卫生部共享。基本的
对数据进行了描述性分析。然而，以下
限制影响了数据的质量：

  - 没有中央数据库来存储、清理和编译数据。

  - 发现病例的地点没有标准化。

  - 卫生部没有能力绘制村庄的病例图
    等级。

## 使用DHIS2跟踪器和事件捕获来改善VL监视 { #improving-vl-surveillance-with-dhis2-tracker-and-event-capture } 

2016 年，世界卫生组织全球利什曼病规划制定了通用的“VL
使用 DHIS2 Tracker 的“患者表格”和通用的“VL 患者登记册”
使用 DHIS2 事件捕获。目标是支持索马里卫生部
使用这些通用模块来加强 VL 监视和控制
在索马里。


![](resources/images/use_cases/vl_who_tracker_somalia.png)

## 将回顾性监视数据导入DHIS2事件捕获 { #importing-retrospective-surveillance-data-into-dhis2-event-capture } 

世卫组织团队在现有的基础上开发了一款“Excel 导入器”应用程序
来自 HISP 越南的 DHIS2 应用程序。 2013 年至 2015 年 VL 事件数据为
导入，然后可将数据用于分析被忽视的热带地区
疾病（NTD）监测和控制。

为索马里实施了 DHIS2 仪表板，其中包含主要指标，以及
代表居住村 VL 病例的地图，作为
感染村。


![](resources/images/use_cases/vl_who_dashboard_somalia.png)

## 使用DHIS2进行预期数据收集 { #using-dhis2-for-prospective-data-collection } 

2017 年 2 月，索马里恩德培的 24 名卫生工作者接受了
关于如何在 WHO-VL 模块中输入数据的培训。培训，
由世卫组织与乌干达 HISP 合作进行，持续了
5天。卫生工作者了解了诸如识别
为每位 VL 患者收集的最少数据； DHIS2 工具和
监视功能（个人和汇总数据输入、数据
验证、数据分析和使用仪表板）；且实用
Tracker Capture 中数据输入的会话。培训结束时，
参与者应该知道如何：

  - 连接平台，

  - 输入个人和汇总数据，

  - 使用数据验证工具验证他们的数据，

  - 通过解释仪表板显示来分析数据
    利什曼病计划要求的指标。

## 收集VL数据的几个计划阶段 { #several-planned-phases-for-gathering-vl-data } 

自本次培训以来，数据输入均在摩加迪沙集中收集。
这是第一阶段，旨在测试系统的可用性
追踪器“VL 患者表格”。第二阶段邀请周边
每月一次到摩加迪沙，在“VL 患者”中输入数据
形式”。第三阶段是测试输入数据的可能性
外围级别。


![](resources/images/use_cases/vl_who_event_somalia.png)

## 现在的中介解决方案 { #an-intermediary-solution-for-now } 

尽管 VL 控制计划最初计划分为三个阶段
在索马里，由于后勤限制，外围水平
继续使用 Excel 解决方案，中央级别的任务是
将数据上传至 DHIS2。部署“VL 患者表格”或
经过进一步分析，“VL 寄存器”计划在后期进行
外围层面的技术要求。

这个中间解决方案代表了对
索马里 VL 控制计划。事实上，它将实现更好的数据质量，
将所有数据集中在一个数据库中，保护数据安全
数据，轻松与主要合作伙伴共享，改进数据使用并改进
反馈到外围级别。

