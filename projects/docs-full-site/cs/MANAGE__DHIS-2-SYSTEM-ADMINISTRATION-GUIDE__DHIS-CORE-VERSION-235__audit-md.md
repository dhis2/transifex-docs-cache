---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/commonmark/en/content/sysadmin/audit.md"
---

# Audit

## Úvod

DHIS2 podporuje novou auditorskou službu založenou na Apache ActiveMQ Artemis. Artemis je používán jako asynchronní systém zasílání zpráv DHIS2.

Poté, co je entita uložena do databáze, bude auditní zpráva odeslána spotřebitelské službě zpráv Artemis. Zpráva bude poté zpracována v jiném vlákně.

Protokoly auditu lze načíst z databáze DHIS2. V současné době není k dispozici žádné uživatelské rozhraní ani koncový bod API pro načítání záznamů auditu.


## Jedna tabulka auditu

<!--DHIS2-SECTION-ID:audit_table-->

Všechny položky auditu budou uloženy do jedné tabulky s názvem `audit`

| Sloupec     | Typ                        |                                                                                                                                                   |   |
|------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---|
| auditid    | celé číslo                     |                                                                                                                                                   |   |
| audittype  | text                        | READ, CREATE, UPDATE, DELETE, SEARCH                                                                                                                  |   |
| auditscope | text                        | METADATA, AGGREGATE, TRACKER                                                                                                                        |   |
| klass      | text                        | Název Java třídy auditu entity                                                                                                                       |   |
| atributy | jsonb                       | Řetězec Json ukládá atributy entity auditu používané pro vyhledávání. Příklad: {"valueType":"TEXT", "categoryCombo":"SWQW313FQY", "domainType":"TRACKER"} |   |
| data       | bytea                       | Komprimovaný řetězec Json entity auditu. Aktuálně je ve formátu bajtového pole a není čitelný člověkem.              |   |
| createdat  | časové razítko bez časového pásma |                                                                                                                                                   |   |
| createdby  | text                        |                                                                                                                                                   |   |
| uid        | text                        |                                                                                                                                                   |   |
| code       | text                        |                                                                                                                                                   |   |
|            |                             |   



Nová služba Audit využívá dva nové koncepty: Rozsahy auditu a Typ auditu.

## Rozsah auditu

<!--DHIS2-SECTION-ID:audit_scope-->

Rozsah auditu je logická oblast aplikace, kterou lze auditovat. V současné době existují tři rozsahy auditu:

```
Tracker

Metadata

Aggregate
```

- Pro rozsah auditu trasovače jsou auditované objekty:
Instance trasované entity, Hodnota atributu trasované entity, Zápis, událost

- Pro oblast metadat jsou auditovány všechny objekty „metadat“.

- U agregovaného rozsahu se auditují objekty agregované datové hodnoty.


## Typ auditu

<!--DHIS2-SECTION-ID:audit_type-->

Typ auditu je akce, která spouští operaci auditu. V současné době podporujeme následující typy:

```
READ

CREATE

UPDATE

DELETE
```

Jako příklad lze uvést, že když se vytvoří nová instance trasované entity, a pokud je takto nakonfigurována, použije se akce CREATE k vložení nové položky auditu do tabulky auditu db.

> **Pozor**
>
> Typ auditu READ vygeneruje v databázi spoustu dat a může mít dopad na výkon.

## Nastavení

<!--DHIS2-SECTION-ID:audit_configuration-->

Systém auditu je automaticky nakonfigurován tak, aby auditoval následující rozsahy a typy:

- CREATE, UPDATE, DELETE

- METADATA, TRACKER, AGGREGATE

**K aktivaci auditu není nutná žádná akce.**
Audit lze stále konfigurovat pomocí „matice auditu“. Matice auditu je řízena 3 vlastnostmi v dhis.conf:

```
audit.metadata

audit.tracker

audit.aggregate
```

Každá vlastnost přijímá seznam platných typů auditu oddělených středníkem:

```
CREATE

UPDATE

DELETE

READ
```

Například, aby bylo možné auditovat pouze vytváření a mazání objektů souvisejících s Trasovačem, měla by být do `dhis.conf` přidána následující vlastnost:

```
audit.tracker = CREATE;DELETE
```

Chcete-li zcela zakázat auditování, je to konfigurace, která se má použít:
```
audit.metadata = DISABLED 

audit.tracker = DISABLED 

audit.aggregate = DISABLED
```
