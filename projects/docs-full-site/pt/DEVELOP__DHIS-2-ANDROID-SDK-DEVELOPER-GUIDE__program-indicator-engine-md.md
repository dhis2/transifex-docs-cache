---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/program-indicator-engine.md" 
---
# Motor indicador de programa

<!--DHIS2-SECTION-ID:program_indicator_engine-->

O SDK inclui seu próprio mecanismo de Indicador de Programa para a avaliação de **Indicadores de Programa em linha**. Esses tipos de indicadores são avaliados no contexto de uma inscrição ou de um único evento e geralmente são colocados no formulário de entrada de dados, oferecendo informações adicionais ao codificador de dados. Isso significa que, embora sejam indicadores regulares do programa e possam ser calculados entre inscrições, eles fornecem informações úteis em uma única inscrição.

Um bom exemplo, "Tempo médio entre visitas".

Um mau exemplo, "Número de TEIs activos": seria sempre 1.

Para acionar o motor indicador do programa, basta executar:

```java
d2.programModule()
    .programIndicatorEngine()
    .getProgramIndicatorValue(<enrollment-uid>, <event-uid>, <program-indicator-uid>);
```

O uid de inscrição ou uid de evento deve ser não nulo.

Tabela de compatibilidade:

| Funções comuns  | Suportado |
|-------------------|-----------|
| E se                | sim       |
| é nulo            | sim       |
| não é nulo         | sim       |
| firstNonNull      | sim       |
| maior          | sim       |
| menos             | sim       |

| Função (d2:) (doc)| Suportado |
|--------------------|-----------|
| addDays           |   sim     |
| teto              |   sim     |
| concatenar       |   sim     |
| doença         |   sim     |
| contagem             |   sim     |
| countIfCondition  |   sim     |
| countIfValue      |   sim     |
| countIfZeroPos    |   Sem doc  |
| dias entre       |   sim     |
| chão             |   sim     |
| hasUserRole       |   Sem doc  |
| hasValue          |   sim     |
| inOrgUnitGroup    |   Sem doc  |
| esquerda              |   sim     |
| comprimento            |   sim     |
| minutos entre    |   sim     |
| módulo           |   sim     |
| meses entre     |   sim     |
| oizp              |   sim     |
| relacionamentoCount |   Não      |
| certo             |   sim     |
| volta             |   sim     |
| Dividido             |   sim     |
| substring         |   sim     |
| validatePatten    |   sim     |
| semanas entre      |   sim     |
| anos entre      |   sim     |
| zing              |   sim     |
| zpvc              |   sim     |

| Variáveis (doc)       | Suportado |
|-----------------------|-----------|
| concluída_data        | sim       |
| creation_date         | sim       |
| current_date          | sim       |
| due_date              | sim       |
| inscrição_conta      | sim       |
| enrollment_date       | sim       |
| enrollment_status     | sim       |
| event_count           | sim       |
| event_date            | sim       |
| incidente_data         | sim       |
| organisationunit_count| N/D       |
| program_stage_id      | Não        |
| program_stage_name    | Não        |
| reporting_period_end  | N/D       |
| reporting_period_start| N/D       |
| sync_date             | Não        |
| tei_count             | N/D       |
| valor_contagem           | sim       |
| zero_pos_value_count  | sim       |

Outros componentes:

| Componente             | Suportado |
|-----------------------|-----------|
| PS_EVENTDATE          | sim       |


