---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/edit/master/docs/src/commonmark/en/content/mdm/A-b-flyve.md" 
---
# 附件B-MDM PoC：Flyve MDM  { #annex-b-mdm-poc-flyve-mdm } 

本附件介绍了经过测试的MDM的结果：[https://www.flyve-mdm.com/](https://www.flyve-mdm.com/）

Flyve MDM 基于 [GLPI](https://glpi-project.org/)，因此需要 GLPI 作为子系统才能使用 Flyve MDM。 GLPI _是一个开源 IT 资产管理、问题跟踪系统和服务台系统。该软件是用 PHP 编写的，并根据 GNU 通用公共许可证分发。_


## 安装和使用 { #installation-usage } 

在本地进行测试很容易，因为它们提供了允许快速测试的docker容器。

也可以要求提供有关云版本的演示。

GLPI在一开始可能看起来有些不知所措，但是如果已经有这样的解决方案，那将是一个很大的优势。

F-Droid上提供了应用程序，因此可以简化安装或测试过程。

可在此处找到受支持功能的列表：[http://flyve.org/android-mdm-agent/howtos/policies](http://flyve.org/android-mdm-agent/howtos/policies）


## 问题 { #issues } 

不支援KIOSK模式

MDM仪表板是一个更好的控制台，但仍然依赖于下面的GLPI。


## 结论 { #conclusion } 

取决于设置，可能不值得，因为如果该软件没有以前的经验，则MDM管理控制台和GLPI可能会让人不知所措。同样，KIOSK模式不可用可能会破坏交易。

它是开源的，因此如果自托管，则可以大大降低成本；可能对于非常小的实施或在扩展之前测试MDM的功能来说是理想的选择。


