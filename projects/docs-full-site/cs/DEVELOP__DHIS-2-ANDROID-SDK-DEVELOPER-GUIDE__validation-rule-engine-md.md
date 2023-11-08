---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/validation-rule-engine.md" 
---
# Mechanismus ověřovacího pravidla

<!--DHIS2-SECTION-ID:validation_rule_engine-->

Ověřovací pravidla přidružená ke konkrétní datové sadě lze vyhodnotit pomocí modulu ověřovacích pravidel. Podporuje pouze vyhodnocení ověřovacích pravidel v kontextu formuláře pro zadávání dat, tj. Ověřovacích pravidel, která používají datové hodnoty obsažené v konkrétní kombinaci datové sady, období, organisationUnit a attributeOptionCombo.

> **Důležité**
>
> V současné době není možné vyhodnotit ověřovací pravidla pro různé datové sady, období, organisationUnits nebo atributOptionCombos.

```java
d2.validationModule()
    .validationEngine()
    .validate(<dataSet-uid>, <period-id>, <organisation-unit-uid>, <attribute-option-combo-uid>);
```

Vrátí výsledek ověření obsahující seznam porušení. Každé porušení zahrnuje užitečné metody k získání člověkem čitelné reprezentace konfliktu.


