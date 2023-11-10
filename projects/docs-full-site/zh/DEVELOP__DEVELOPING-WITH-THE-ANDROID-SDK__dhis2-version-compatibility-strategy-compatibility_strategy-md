---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/compatibility-strategy.md" 
---
# DHIS2版本兼容性策略  { #compatibility_strategy } 

 <!--DHIS2-SECTION-ID:compatibility_strategy-->

该SDK确保与最新的三个DHIS 2版本兼容（请参阅[兼容性]（＃compatibility））。如果SDK仍与以前的DHIS2版本兼容，并且未检测到主要问题，则可以将兼容性扩展到以前的版本。

为了避免意外登录到不受支持的DHIS 2实例，SDK会阻止与尚不支持或已弃用的版本的连接。

关于数据模型和兼容性，主要方法是扩展数据模型以能够支持所有DHIS 2版本。通常，新的DHIS 2版本会引入额外的功能并且不会删除现有功能，因此支持新的DHIS 2版本通常意味着使用最新的数据模型。

作为一般规则，SDK 会尽量避免对其 API 进行重大更改，并且新功能对用户来说是可选的。尽可能遵循此规则，但在某些情况下，支持新旧 API 以避免破坏的成本非常高。在这种情况下，**SDK 可能会引入重大更改以与新的 DHIS 2 版本兼容**。

在这里，您可以找到一些SDK更改和应用程序效果的示例。

## 示例：次要更改 { #example-minor-change } 

在2.30版之前，程序模型具有一个称为“ captureCoordinates”的布尔属性。此属性指示是否必须在该程序中存储坐标（点）。从2.30版开始，此属性已由“ featureType”替换为四个可能的值：NONE，POINT，POLYGON，MULTI_POLYGON。

* SDK中的更改：*

从2.30开始，SDK使用属性“ featureType”。如果服务器版本低于2.30，则SDK会将“ captureCoordinates”值映射到：

- 假-无
- 正确-要点

*应用程序中的更改：*

现在，该应用被强制使用“ featureType”。代码中的修改非常简单。

## 示例：重大更改 { #example-major-change } 

从2.30版本开始，Relationship模型遭受了深度重构，以允许事件，注册和trackedEntityInstances之间建立关系。 SDK在2.30中采用了该模型，并将该模型公开给应用程序。与API交互时，SDK在内部在两个模型之间进行转换。

*应用程序中的更改：*

此更改意味着该应用程序必须采用其他模型，并且更改并非如此简单。


