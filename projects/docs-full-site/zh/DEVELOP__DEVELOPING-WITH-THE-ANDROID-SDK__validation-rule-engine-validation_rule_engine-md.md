---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/validation-rule-engine.md" 
---
# 验证规则引擎  { #validation_rule_engine } 

 <!--DHIS2-SECTION-ID:validation_rule_engine-->

可以使用验证规则模块来评估与特定数据集关联的验证规则。它仅支持在数据输入表单的上下文中对验证规则进行评估，即使用包含在dataSet，period，organisationUnit和attributeOptionCombo的特定组合中的数据值的验证规则。

> **重要**
>
>当前，无法评估包含不同数据集，期间，organizationalUnit或attributeOptionCombos的验证规则。

```java
d2.validationModule()
    .validationEngine()
    .validate(<dataSet-uid>, <period-id>, <organisation-unit-uid>, <attribute-option-combo-uid>);
```

它返回包含违规列表的验证结果。每种违规行为都包含有用的方法，以使人类可以理解该冲突。


