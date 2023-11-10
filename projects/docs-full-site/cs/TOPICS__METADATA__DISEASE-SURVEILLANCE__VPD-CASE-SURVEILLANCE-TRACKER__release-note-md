---
edit_url: "https://github.com/dhis2-metadata/VPD_CS/blob/master/docs/vpd_cs-release_note-1.1.0.md"
revision_date: "2022-09-19"
---

# Poznámka k vydání { #release-note }

Byla vydána nová verze (1.1.0) trasování případu VPD s novými indikátory, opravami konfigurace a vylepšeními. Ty jsou shrnuty níže.

## Nový obsah { #new-content }

-   Nové **indikátory programu** pro vizualizaci případů spalniček podle věkového pásma a stavu očkování. Tyto programové indikátory se používají v doplňkovém řídicím panelu Immunity Gaps (vydáno jako samostatný balíček), určeném k triangulaci údajů o imunizaci a sledování.
-   Nové **indikátory** pro indikátory přiměřenosti a citlivosti laboratorních vzorků spalniček/zarděnek
    -   CBS – míra vyřazení spalniček/zarděnek (/100000) `Neerc3YIske`
    -   CBS - Podíl adekvátnosti vzorku spalniček/zarděnek obdržený národní laboratoří (%) `MKzrxSTNUGe`
    -   CBS – Podíl přiměřenosti vzorku spalniček/zarděnek (%) `rg1o94xciwp`

## Opravy a vylepšení { #fixes-improvements }

-   Objektové **názvy** a **kódy** byly aktualizovány, aby opravily pravopisné chyby a byly v souladu s postupy kódování metadat doporučenými DHIS2.

-   Byly provedeny následující opravy výrazů **programový indikátor**:
    -   Aktualizované a pevné PI na základě věku pro přesný výpočet věkových PI, ať už bylo datum narození zadáno ručně nebo odhadnuté na základě věku daného během registrace případu. Přidaná podmínka ve výrazech PI kontroluje odhadovaný 'věk (měsíce)' nebo odhadovaný 'věk (roky)' nebo věk na základě hodnoty atributu 'datum narození'
    -   Opravené výrazy PI založené na registraci TEI, aby se počítal na základě _enrollment_ vs. _event_
    -   Opravené PI výrazy, kde bylo použito celé číslo 1 místo správného kódu 'YES' ze základní sady možností HIS Ano/Ne. Ovlivněné PI: `x0n3BxFa6SC`, `1X9hhSxGrU`, `fy6f9KZgAJV`.
-   Opraveno několik **vizualizací ovládacího panelu** (analytické objekty) pomocí „pevných“ období k exportu s „relativními“ obdobími
