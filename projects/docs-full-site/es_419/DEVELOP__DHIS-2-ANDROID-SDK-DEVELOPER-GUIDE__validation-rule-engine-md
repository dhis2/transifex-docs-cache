---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/validation-rule-engine.md" 
---
# Motor de reglas de validación

<!--DHIS2-SECTION-ID:validation_rule_engine-->

Las reglas de validación asociadas a un set de datos en particular se pueden evaluar utilizando el módulo de reglas de validación. Solo admite la evaluación de reglas de validación en el contexto de un formulario de entrada de datos, es decir, reglas de validación que utilizan valores de datos contenidos en una combinación particular de set de datos, periodo, unidad organizativa y combinación de opciones de atributos (dataSet, period, organisationUnit, attributeOptionCombo).

> ** Importante **
>
> Actualmente no es posible evaluar las reglas de validación en diferentes set de datos, periodos, unidades organizativas y combinación de opciones de atributos.

```java
d2.validationModule()
    .validationEngine()
    .validate(<dataSet-uid>, <period-id>, <organisation-unit-uid>, <attribute-option-combo-uid>);
```

Devuelve un resultado de validación que contiene la lista de infracciones. Cada violación incluye métodos útiles para obtener una representación legible del conflicto.


