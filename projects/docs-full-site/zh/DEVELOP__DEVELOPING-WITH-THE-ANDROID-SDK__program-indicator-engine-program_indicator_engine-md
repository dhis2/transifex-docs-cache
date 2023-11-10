---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/program-indicator-engine.md" 
---
# 程序指示器引擎  { #program_indicator_engine } 

 <!--DHIS2-SECTION-ID:program_indicator_engine-->

SDK 包含自己的计划指标引擎，用于评估**内联计划指标**。此类指标在注册或单个事件的背景下进行评估，并且通常放置在数据输入表单中，为数据编码器提供附加信息。这意味着，尽管它们是常规计划指标并且可以跨注册进行计算，但它们在单个注册中提供了有用的信息。

一个很好的例子，“两次访问之间的平均时间”。

一个不好的例子，“活动TEI的数量”：始终为1。

为了触发程序指示器引擎，只需执行：

```java
d2.programModule()
    .programIndicatorEngine()
    .getProgramIndicatorValue(<enrollment-uid>, <event-uid>, <program-indicator-uid>);
```

注册uid或事件uid必须为非null。

兼容性表：

| 常用功能  | 支持的 |
|-------------------|-----------|
| 如果                | 是       |
| 一片空白            | 是       |
| isNotNull         | 是       |
| firstNonNull      | 是       |
| 最伟大的          | 是       |
| 最小             | 是       |

| 函数（d2：）（doc）| 支持的 |
|--------------------|-----------|
| addDays           |   是     |
| 细胞              |   是     |
| 级联       |   是     |
| 健康）状况         |   是     |
| 计数             |   是     |
| countIfCondition  |   是     |
| countIfValue      |   是     |
| countIfZeroPos    |   没有文件  |
| 天之间       |   是     |
| 地板             |   是     |
| hasUserRole       |   没有文件  |
| hasValue          |   是     |
| inOrgUnitGroup    |   没有文件  |
| 剩下              |   是     |
| 长度            |   是     |
| 分钟之间    |   是     |
| 模数           |   是     |
| 月份之间     |   是     |
| 奥兹普              |   是     |
| RelationshipCount |   没有      |
| 对             |   是     |
| 回合             |   是     |
| 分裂             |   是     |
| 子串         |   是     |
| validatePatten    |   是     |
| 周之间      |   是     |
| 年份之间      |   是     |
| zing              |   是     |
| 聚氯乙烯              |   是     |

| 变量（文档）       | 支持的 |
|-----------------------|-----------|
| completed_date        | 是       |
| creation_date         | 是       |
| current_date          | 是       |
| due_date              | 是       |
| enrollment_count      | 是       |
| enrollment_date       | 是       |
| enrollment_status     | 是       |
| event_count           | 是       |
| event_date            | 是       |
| incident_date         | 是       |
| Organisationunit_count| 不适用       |
| program_stage_id      | 没有        |
| program_stage_name    | 没有        |
| report_period_end  | 不适用       |
| report_period_start| 不适用       |
| sync_date             | 没有        |
| tei_count             | 不适用       |
| value_count           | 是       |
| zero_pos_value_count  | 是       |

其他组件：

| 零件             | 支持的 |
|-----------------------|-----------|
| PS_EVENTDATE          | 是       |


