---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/validation-rule-engine.md" 
---
# Motor de regras de validação  { #validation_rule_engine } 

 <!--DHIS2-SECTION-ID:validation_rule_engine-->

As regras de validação associadas a um determinado dataSet podem ser avaliadas usando o módulo de regra de validação. Ele suporta apenas a avaliação de regras de validação no contexto de um formulário de entrada de dados, ou seja, regras de validação que usam valores de dados contidos em uma combinação particular de dataSet, period, organisationUnit e attributeOptionCombo.

> ** Importante **
>
> Atualmente não é possível avaliar as regras de validação através de diferentes conjuntos de dados, períodos, unidades de organização ou atributosOpçãoCombos.

```java
d2.validationModule()
    .validationEngine()
    .validate(<dataSet-uid>, <period-id>, <organisation-unit-uid>, <attribute-option-combo-uid>);
```

Ele retorna um resultado de validação contendo a lista de violações. Cada violação inclui métodos úteis para obter uma representação legível do conflito.


