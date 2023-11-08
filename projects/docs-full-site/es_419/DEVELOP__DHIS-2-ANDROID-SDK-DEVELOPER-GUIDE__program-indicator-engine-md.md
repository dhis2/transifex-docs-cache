---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/program-indicator-engine.md" 
---
# Motor indicador de programa

<!--DHIS2-SECTION-ID:program_indicator_engine-->

El SDK incluye su propio motor de indicadores de programa para la evaluación de **indicadores de programa en línea**. Este tipo de indicadores se evalúan dentro del contexto de una inscripción o un evento único y generalmente se colocan en el formulario de entrada de datos ofreciendo información adicional al codificador de datos. Esto significa que, aunque son indicadores de programa regulares y pueden calcularse a través de las inscripciones, proporcionan información útil dentro de una sola inscripción.

Un buen ejemplo, "Tiempo promedio entre visitas".

Un mal ejemplo, "Número de TEIs activos": siempre sería 1.

Para activar el motor de indicador de programa, simplemente ejecute:

```java
d2.programModule()
    .programIndicatorEngine()
    .getProgramIndicatorValue(<enrollment-uid>, <event-uid>, <program-indicator-uid>);
```

El uid de inscripción o el uid de evento no deben ser nulos.

Tabla de compatibilidad:

| Funciones comunes  | Soportado |
|-------------------|-----------|
| if                | Sí        |
| isNull            | Sí        |
| isNotNull         | Sí        |
| firstNonNull      | Sí        |
| greatest          | Sí        |
| least             | Sí        |

| Function (d2:)(doc)| Soportado |
|--------------------|-----------|
| addDays           |   Sí      |
| ceil              |   Sí      |
| concatenate       |   Sí      |
| condition         |   Sí      |
| Conteo             |   Sí      |
| countIfCondition  |   Sí      |
| countIfValue      |   Sí      |
| countIfZeroPos    |   No doc  |
| daysBetween       |   Sí      |
| floor             |   Sí      |
| hasUserRole       |   No doc  |
| hasValue          |   Sí      |
| inOrgUnitGroup    |   No doc  |
| left              |   Sí      |
| length            |   Sí      |
| minutesBetween    |   Sí      |
| modulus           |   Sí      |
| monthsBetween     |   Sí      |
| oizp              |   Sí      |
| relationshipCount |   No      |
| right             |   Sí      |
| round             |   Sí      |
| split             |   Sí      |
| substring         |   Sí      |
| validatePatten    |   Sí      |
| weeksBetween      |   Sí      |
| yearsBetween      |   Sí      |
| zing              |   Sí      |
| zpvc              |   Sí      |

| Variables (doc)       | Soportado |
|-----------------------|-----------|
| completed_date        | Sí        |
| creation_date         | Sí        |
| current_date          | Sí        |
| due_date              | Sí        |
| enrollment_count      | Sí        |
| enrollment_date       | Sí        |
| enrollment_status     | Sí        |
| event_count           | Sí        |
| event_date            | Sí        |
| incident_date         | Sí        |
| organisationunit_count| N/A       |
| program_stage_id      | No        |
| program_stage_name    | No        |
| reporting_period_end  | N/A       |
| reporting_period_start| N/A       |
| sync_date             | No        |
| tei_count             | N/A       |
| value_count           | Sí        |
| zero_pos_value_count  | Sí        |

Otros componentes:

| Component             | Soportado |
|-----------------------|-----------|
| PS_EVENTDATE          | Sí        |


