---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/program-indicator-engine.md" 
---
# Mechanismus indikátoru programu  { #program_indicator_engine } 

<!--DHIS2-SECTION-ID:program_indicator_engine-->

Sada SDK obsahuje vlastní modul programových indikátorů pro hodnocení **in-line programových indikátorů**. Tyto druhy indikátorů se hodnotí v kontextu registrace nebo jediné události a obvykle se umisťují do formuláře pro zadávání dat, který nabízí další informace kodéru dat. To znamená, že i když jsou běžnými indikátory programu a lze je vypočítat napříč registracemi, poskytují užitečné informace v rámci jedné registrace.

Dobrým příkladem je „Průměrná doba mezi návštěvami“.

Špatný příklad: „Počet aktivních TEI“: vždy by to bylo 1.

Chcete-li spustit modul indikátoru programu, stačí provést:

```java
d2.programModule()
    .programIndicatorEngine()
    .getProgramIndicatorValue(<enrollment-uid>, <event-uid>, <program-indicator-uid>);
```

Buď uidment-uid nebo event-uid musí mít nenulovou hodnotu.

Tabulka kompatibility:

| Společné funkce  | Podporováno |
|-------------------|-----------|
| if                | Ano       |
| isNull            | Ano       |
| isNotNull         | Ano       |
| firstNonNull      | Ano       |
| největší          | Ano       |
| nejméně             | Ano       |

| Funkce (d2:)(doc)| Podporováno |
|--------------------|-----------|
| addDays           |   Ano     |
| ceil              |   Ano     |
| concatenate       |   Ano     |
| condition         |   Ano     |
| počet             |   Ano     |
| countIfCondition  |   Ano     |
| countIfValue      |   Ano     |
| countIfZeroPos    |   No doc  |
| daysBetween       |   Ano     |
| floor             |   Ano     |
| hasUserRole       |   No doc  |
| hasValue          |   Ano     |
| inOrgUnitGroup    |   No doc  |
| left              |   Ano     |
| délka            |   Ano     |
| minut mezi    |   Ano     |
| modulus           |   Ano     |
| monthsBetween     |   Ano     |
| oizp              |   Ano     |
| relationshipCount |   Ne      |
| vpravo             |   Ano     |
| round             |   Ano     |
| rozdělit             |   Ano     |
| podřetězec         |   Ano     |
| validatePatten    |   Ano     |
| týdnů mezi      |   Ano     |
| yearsBetween      |   Ano     |
| zing              |   Ano     |
| zpvc              |   Ano     |

| Proměnné (doc)       | Podporováno |
|-----------------------|-----------|
| completed_date        | Ano       |
| creation_date         | Ano       |
| current_date          | Ano       |
| due_date              | Ano       |
| enrollment_count      | Ano       |
| enrollment_date       | Ano       |
| enrollment_status     | Ano       |
| event_count           | Ano       |
| event_date            | Ano       |
| incident_date         | Ano       |
| organisationunit_count| Nedostupné       |
| program_stage_id      | Ne        |
| program_stage_name    | Ne        |
| reporting_period_end  | Nedostupné       |
| reporting_period_start| Nedostupné       |
| sync_date             | Ne        |
| tei_count             | Nedostupné       |
| value_count           | Ano       |
| zero_pos_value_count  | Ano       |

Další komponenty:

| Součást             | Podporováno |
|-----------------------|-----------|
| PS_EVENTDATE          | Ano       |


