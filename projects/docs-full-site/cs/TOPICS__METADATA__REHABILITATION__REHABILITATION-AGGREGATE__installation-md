---
edit_url: "https://github.com/dhis2-metadata/REHAB_AGG/blob/master/docs/rehab_agg-installation.md"
revision_date: "2022-05-25"
---

# Rehabilitace – Průvodce instalací agregátu { #rehab-installation }

Tento dokument obsahuje instalační příručku pro souhrnný balíček Rehabilitace.

Výchozí jazyk systému: angličtina

Dostupné překlady: francouzština, španělština, portugalština, arabština

## Přehled { #overview }

=== "DHIS2.35"

    ```json
    "package": {
        "DHIS2Build": "834b25f",
        "DHIS2Version": "2.35.8",
        "code": "RHAG00",
        "description": "",
        "lastUpdated": "20220221T181704",
        "locale": "en",
        "name": "RHAG00_DHIS2.35",
        "type": "AGG",
        "version": "1.0.0"
    }
    ```

=== "DHIS2.36"

    ```json
    "package": {
        "DHIS2Build": "aa38c7f",
        "DHIS2Version": "2.36.8",
        "code": "RHAG00",
        "description": "",
        "lastUpdated": "20220222T131957",
        "locale": "en",
        "name": "RHAG00_DHIS2.36",
        "type": "AGG",
        "version": "1.0.0"
    }
    ```

=== "DHIS2.37"

    ```json
    "package": {
        "DHIS2Build": "a7328e1",
        "DHIS2Version": "2.37.3",
        "code": "RHAG00",
        "description": "",
        "lastUpdated": "20220222T132004",
        "locale": "en",
        "name": "RHAG00_DHIS2.37",
        "type": "AGG",
        "version": "1.0.0"
    }
    ```

## Instalace { #installation }

Instalace modulu se skládá z několika kroků:

1. [Příprava souboru metadat s metadaty DHIS2](#preparing-the-metadata-file).
2. [Import souboru metadat do DHIS2](#importing-metadata).
3. [Konfigurace importovaných metadat](#configuration).
4. [Přizpůsobení programu po importu](#adapting-the-program)

Před zahájením procesu instalace a konfigurace v DHIS2 se doporučuje nejprve přečíst každou část instalační příručky. Identifikujte příslušné sekce v závislosti na typu vašeho importu:

1. importovat do prázdné instance DHIS2
2. importovat do instance DHIS2 s existujícími metadaty.

Kroky popsané v tomto dokumentu by měly být otestovány v testovací instanci DHIS2 a teprve poté aplikovány na produkční prostředí.

## Požadavky { #requirements }

Pro instalaci modulu je vyžadován uživatelský účet správce na DHIS2.

Velkou péči je třeba věnovat tomu, aby byl server samotný i aplikace DHIS2 dobře zabezpečeny, měla by být definována přístupová práva ke shromážděným datům. Podrobnosti o zabezpečení systému DHIS2 jsou mimo rozsah tohoto dokumentu a odkazujeme na [dokumentaci DHIS2](https://docs.dhis2.org/).

## Soubory metadat { #metadata-files }

I když to není vždy nutné, může být často výhodné provést určité úpravy souboru metadat před jeho importem do DHIS2.

## Příprava souboru metadat { #preparing-the-metadata-file }

### Výchozí dimenze dat { #default-data-dimension }

V dřívějších verzích DHIS2 byla UID výchozích datových dimenzí automaticky generována. I když tedy všechny instance DHIS2 mají výchozí volbu kategorie, kategorii datových prvků, kombinaci kategorií a kombinaci možností kategorie, UID těchto výchozích hodnot se mohou lišit. Novější verze DHIS2 mají pevně zakódovaná UID pro výchozí dimenzi a tato UID se používají v konfiguračních balíčcích.

Aby se předešlo konfliktům při importu metadat, je vhodné vyhledat a nahradit celý soubor .json pro všechny výskyty těchto výchozích objektů a nahradit UID souboru .json UID z instance, do které bude soubor importován. Tabulka 1 ukazuje UID, která by měla být nahrazena, a také koncové body API pro identifikaci stávajících UID

| Objekt | UID | Koncový bod API |
| --- | --- | --- |
| Kategorie | `GLevLNI9wkl` | `../api/categories.json?filter=name:eq:default` |
| Možnost kategorie | `xYerKDKCefk` | `../api/categoryOptions.json?filter=name:eq:default` |
| Kombinace kategorií | `bjDvmb4bfuf` | `../api/categoryCombos.json?filter=name:eq:default` |
| Kombinace možností kategorie | `HllvX50cXC0` | `../api/categoryOptionCombos.json?filter=name:eq:default` |

Identifikujte UID výchozích dimenzí ve vaší instanci pomocí uvedených požadavků API a nahraďte UID v souboru json UID z instance.

> **POZNÁMKA**
>
> Pamatujte, že tato operace hledání a nahrazování musí být provedena pomocí editoru prostého textu, nikoli textového procesoru, jako je Microsoft Word.

### Typy indikátorů { #indicator-types }

Typ indikátoru je dalším typem objektu, který může způsobit konflikt importu, protože určitá jména se používají v různých databázích DHIS2 (např. "Procento"). Vzhledem k tomu, že typy indikátorů jsou definovány svým faktorem (včetně 1 pro indikátory „pouze čitatel“), jsou jednoznačné a lze je nahradit vyhledáváním a nahrazováním UID. Tato metoda pomáhá vyhnout se potenciálním konfliktům při importu a zabraňuje implementátoru ve vytváření duplicitních typů indikátorů. Níže uvedená tabulka obsahuje UID, která lze nahradit, a také koncové body API pro identifikaci stávajících UID:

| Objekt | UID | Koncový bod API |
| --- | --- | --- |
| Pouze čitatel (číslo) | `kHy61PbChXr` | `../api/indicatorTypes.json?filter=number:eq:true&filter=factor:eq:1` |

### Vizualizace pomocí kořenové organizační jednotky UID { #visualizations-using-root-organisation-unit-uid }

Vizualizace, sestavy událostí, tabulky sestav a mapy, které jsou přiřazeny konkrétní úrovni organizační jednotky nebo skupině organizačních jednotek, mají odkaz na kořenovou organizační jednotku (úroveň 1). Takové objekty, pokud jsou v souboru metadat přítomny, obsahují zástupný symbol ` <OU_ROOT_UID> `. Použijte funkci vyhledávání v editoru souborů .json k případné identifikaci tohoto zástupného symbolu a jeho nahrazení UID organizační jednotky úrovně 1 v cílové instanci.

### Kódy možností { #option-codes }

Podle konvencí pojmenování DHIS2 používají kódy metadat velká písmena, podtržítka a žádné mezery. Některé výjimky, které se mohou vyskytnout, jsou uvedeny v dokumentaci příslušného balíčku. Všechny kódy obsažené v objektech metadat v aktuálním balíčku odpovídají konvencím pojmenování. Může se stát, že kódy existujících objektů metadat používaných v cílové databázi používají malá písmena. V tomto případě je důležité tyto hodnoty aktualizovat přímo v databázi.

> **Důležité**
>
> Během importu budou stávající kódy možností přepsány aktualizovanými kódy s velkými písmeny. Pro aktualizaci datových hodnot pro existující data v databázi je nutné aktualizovat hodnoty uložené v databázi pomocí databázových příkazů. Před výměnou hodnot se ujistěte, že jste namapovali stávající staré kódy možností a nové kódy možností. Před provedením úprav na produkčním serveru použijte nejprve pracovní instanci.

Pro hodnoty datových prvků použijte:

```SQL
UPDATE programstageinstance
SET eventdatavalues = jsonb_set(eventdatavalues, '{"<affected data element uid>","value"}', '"<new value>"')
WHERE eventdatavalues @> '{"<affected data element uid>":{"value": "<old value>"}}'::jsonb
AND programstageid=<database_programsatgeid>;
```

### Pořadí řazení pro možnosti { #sort-order-for-options }

Zkontrolujte, zda pořadí řazení `sortOrder` možností ve vašem systému odpovídá pořadí řazení možností obsažených v balíčku metadat. To platí pouze v případě, že soubor json a cílová instance obsahují volby a sady voleb se stejným UID.

Po importu se ujistěte, že pořadí řazení možností v sadě možností začíná na 1. V hodnotách pořadí řazení by neměly být žádné mezery (např. 1,2,3,5,6).

Pořadí řazení lze upravit v aplikaci Údržba.

1. Přejděte na příslušnou sadu možností
2. Otevřete sekci „Možnosti“.
3. Použijte alternativy "ŘADIT PODLE JMÉNA", "ŘADIT PODLE KÓDU/HODNOTY" nebo "ŘADIT RUČNĚ".

Balíček Rehabilitace obsahuje jednu sadu možností a dvě možnosti:

```json
{
    "optionSets": [
        {
            "name": "YES/NO (numeric)",
            "id": "TdDqpX1kdd2",
            "code": "YES_NO_NUM",
            "valueType": "INTEGER_ZERO_OR_POSITIVE",
            "options": [
                {
                    "id": "VavIEUmBv8j"
                },
                {
                    "id": "Xu8ieCbS7jH"
                }
            ]
        }
    ],
    "options": [
        {
            "name": "Yes",
            "id": "VavIEUmBv8j",
            "code": "1",
            "sortOrder": 1,
            "optionSet": {
                "id": "TdDqpX1kdd2"
            }
        },
        {
            "name": "No",
            "id": "Xu8ieCbS7jH",
            "code": "0",
            "sortOrder": 2,
            "optionSet": {
                "id": "TdDqpX1kdd2"
            }
        }
    ]
}
```

Tato sada možností Ano/Ne je založena na hodnotách možností „INTEGER_ZERO_OR_POSITIVE“, které jsou vyhodnoceny v prediktorech, aby se určila **Dostupnost nezbytných balíčků rehabilitace na úrovni primární péče** a počet zařízení nabízejících nezbytné balíčky.

### Skupiny organizačních jednotek a sady skupin { #rehab-orgunitgroups }

Balíček obsahuje následující skupiny organizačních jednotek:

| Název | UID | Popis | Účel |
| --- | --- | --- | --- |
| PHC | `aT5pkgRLbw5` | Primární zdravotnická zařízení | přiřazení datové sady, analytika |
| REHAB - Hlavní seznam zařízení | `Uvefj6bDfzo` | Zahrnuje všechna zařízení podávající zprávy o rehabilitaci | přiřazení datové sady, analytika |
| REHAB - PHC | `bbsxlCu3Vya` | Zahrnuje všechna primární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| REHAB - SHC | `wZJCB2cj9jg` | Zahrnuje všechna sekundární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| REHAB - THC | `Re0iJ3vtBzE` | Zahrnuje všechna terciární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| Rehabilitační lůžkové oddělení | `AGK6oOK4ncb` | Zahrnuje všechna zařízení s vyhrazeným rehabilitačním oddělením | Analytika |
| Nemocniční obvod | `Y9lBaYVm9j7` | Zahrnuje všechny okresní nemocnice | Analytika |

a následující sady skupin organizačních jednotek:

| Název | UID | Popis | Účel |
| --- | --- | --- | --- |
| Administrativní úrovně péče | `dSwpdHITQ85` | Administrativní úroveň péče např. PHC, SHC, THC | Analytika |
| REHAB - Administrativní úrovně | `wkjpdklqOIt` | Rehabilitační úroveň péče např. REHAB PHC, REHAB SHC, REHAB THC | Analytika |
| Typ | `VQT2m5uMawR` | Zahrnuje typy zařízení, např. Okresní nemocnice, zdravotní střediska atd. | Analytika |

Tyto objekty metadat je třeba nakonfigurovat.

1. Pokud cílová instance neobsahuje žádné skupiny organizačních jednotek, které odpovídají popisu skupin obsažených v balíčku, postupujte během konfigurace a importu podle následujících kroků:

    1. Importujte balíček spolu se zahrnutými skupinami organizačních jednotek.
    2. Přiřaďte příslušná zařízení novým skupinám organizačních jednotek v aplikaci Údržba.

2. Pokud cílová instance již obsahuje skupiny organizačních jednotek, které odpovídají popisu pro dané objekty metadat, postupujte při konfiguraci a importu podle následujících kroků:

    1. Poznamenejte si UID odpovídajících skupin organizačních jednotek v cílové instanci.
    2. Nahraďte všechny výskyty UID organizaceUnitGrop v souboru json metadat odpovídajícími UID uvedenými v kroku 1.
    3. Před importem odstraňte objekty metadat OrganizationUnitGroup ze souboru json metadat. Tento krok je velmi důležitý, jinak dojde k přepsání aktuálního přiřazení organizačních jednotek ke stávajícím skupinám v cílové instanci.
    4. Pokud není vyžadována žádná další předkonfigurace / úprava, pokračujte k importu balíčku.

3. Pokud cílová instance neobsahuje sady skupin organizačních jednotek, které odpovídají poskytnutému popisu, je třeba tyto skupiny organizačních jednotek importovat do cílové instance. Příslušné skupiny organizačních jednotek je třeba přidat do sad skupin organizačních jednotek v uživatelském rozhraní nebo pomocí rozhraní API.

4. Pokud cílová instance již obsahuje sady skupin organizačních jednotek, které odpovídají poskytnutému popisu, postupujte během konfigurace a importu podle následujících kroků:

    1. Nahraďte UID odpovídajících sad skupin organizačních jednotek v souboru metadat odpovídajícími UID sad skupin organizačních jednotek z cílové instance.
    2. Před importem odstraňte objekty sady skupin organizačních jednotek ze souboru metadat. Tento krok je velmi důležitý, jinak dojde k přepsání aktuálního přiřazení skupin organizačních jednotek k existujícím sadám skupin v cílové instanci.
    3. Přidejte nově importované skupiny organizačních jednotek do sad skupin organizačních jednotek. (Viz tabulky výše).

> **Příklad**
>
> Cílová instance již může obsahovat skupinu organizačních jednotek primární péče. V tomto případě před importem nahraďte UID `aT5pkgRLbw5` skupiny a všechny její výskyty v souboru json odpovídajícím UID z cílové instance. Poté ze souboru json odeberte objekt metadat orgUnitGroup „PHC“. Najdete jej pod `"organisationUnitGroups":`

### Údaje o počtu obyvatel, výskytu a hustotě personálu { #population-incidence-and-personnel-density-data }

Balíček Rehabilitace obsahuje datové prvky, indikátory a další metadatové objekty, které se používají na datech **populace**, **incidence** a **hustota personálu**.

Úrovně organizačních jednotek, na kterých se zadávají údaje o populaci v cílové instanci, se mohou lišit.

V generickém balíčku Rehabilitace jsou tato metadata přidána do datových sad na úrovni zařízení uvedených v tabulce níže.

| Datový prvek | UID | Název sady dat | UID sady dat | Typ období datové sady | Datová sada skupiny organizačních jednotek |
| --- | --- | --- | --- | --- | --- |
| GEN – Populace | `DkmMEcubiPv` | REHAB - hustota personálu | `Sm2fALTZROS` | Ročně | REHAB - Hlavní seznam zařízení |
| REHAB - výskyt amputací % | `jEc1P0VAPcs` | REHAB - údaje o hustotě lůžek a incidenci | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |
| REHAB - výskyt popálenin % | `rtYJONzb7OY` | REHAB - údaje o hustotě lůžek a incidenci | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |
| REHAB - výskyt MMT % | `jlS0RS2LplZ` | REHAB - údaje o hustotě a výskytu lůžek | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |
| REHAB - výskyt SCI % | `Iy6ylb65g4V` | REHAB - údaje o hustotě lůžek a incidenci | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |
| REHAB - výskyt mrtvice % | `OIADGq0kCHW` | REHAB - údaje o hustotě a výskytu lůžek  | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |
| REHAB - výskyt TBI % | `rzVRv6GpduW` | REHAB - údaje o hustotě a výskytu lůžek | `giKizLegiUW` | Ročně | Rehabilitační lůžkové oddělení |

Pokud cílová instance již má infrastrukturu metadat, která se používá pro shromažďování **údajů o populaci, personálu nebo incidenci**, postupujte podle kroků uvedených níže:

1. Zvolte strategii pro zarovnání metadat populace v cílové instanci a v souboru .json.

    - Alternativa 1: Nahraďte UID datových prvků a všechny jejich výskyty v souboru json UID z cílového systému
    - Alternativa 2: Zvažte nahrazení UID těchto datových prvků v cílovém systému UID ze souboru json. Datové prvky GEN jsou součástí základní knihovny metadat DHIS2 a používají se v jiných balíčcích metadat.

2. Ukazatele, které používají **data o populaci, zaměstnancích nebo incidenci**, budou agregovat data na úrovni/úrovních, kde jsou data zadána.

3. Po importu balíčku může být vyžadováno další mapování a konfigurace. Viz [sekce konfigurace datové sady](#rehab-dataset-config)

> **POZNÁMKA**
>
> Při aktualizaci UID prvku metadat ve stávající instamce DHIS2 budete muset spustit příkaz SQL v databázi a dodatečně nahradit všechny výskyty a odkazy jeho UID v jiných objektech metadat: prediktor, indikátor, výrazy ověřovacích pravidel atd. .

### Predikce { #rehab-predictors }

Balíček obsahuje následující prediktory:

| Název | UID | Typ období | Chybějící hodnotová strategie | Výstupní datový prvek - název | Výstupní datový prvek - UID | Úrovně organizačních jednotek |
| --- | --- | --- | --- | --- | --- | --- |
| REHAB - Dostupnost (základní balíček) | `zYbrCP7xGtk` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB – dostupnost balíčku (celkově) | `bUJKsy9u2xv` | Úroveň zařízení |
| REHAB - Dostupnost (ergoterapeuti) | `MaWSMzXDLkm` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (ergoterapeuti) | `RPKfAe7voO3` | Úroveň zařízení |
| REHAB - Dostupnost (jiný personál) | `aphqcwJiK5s` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (jiný personál) | `qVvudaOdniT` | Úroveň zařízení |
| REHAB - Dostupnost (fyzioterapeuti) | `ydlTJLDcFBj` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (fyzioterapeuti) | `N6ru55bPe1o` | Úroveň zařízení |
| REHAB - Dostupnost (protetik/ortotik) | `K3QZ2zs0opc` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (protetik/ortotik) | `klLHQzY0lw2` | Úroveň zařízení |
| REHAB - Dostupnost (psychologové) | `RpxclhlYJxw` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (psychologové) | `pNNIXV0kOus` | Úroveň zařízení |
| REHAB - Dostupnost (rehabilitační lékaři) | `CbnJeF5K1cM` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (rehabilitační lékaři) | `LQ10SQqGKyf` | Úroveň zařízení |
| REHAB - Dostupnost (logopedi) | `qHJTzQcMSd4` | roční | Přeskočte, pokud chybí všechny hodnoty | REHAB - Dostupnost (logopedi) | `SuZDPYOgFbN` | Úroveň zařízení |

Metadata prediktoru zahrnují úrovně organizačních jednotek používané pro agregaci hodnot dat. Soubor metadat balíčku obsahuje zástupné symboly, které je třeba nahradit UID odpovídajících úrovní organizačních jednotek v cílové databázi.

Kroky k přípravě prediktorů pro import jsou popsány níže:

1. Identifikujte UID organizaceUnitLevel úrovně zařízení, na které budou data pro prediktory agregována. K identifikaci požadovaného UID použijte následující koncový bod API: `../api/organisationUnitLevels.json?fields=id,name`
2. Najděte následující zástupné symboly OrganizationUnitLevel v souboru json: `<OU_LEVEL_FACILITY_UID>`
3. Nahraďte zástupné symboly UID identifikované úrovně zařízení v cílové instanci.
4. Identifikujte číslo úrovně zařízení v cílové instanci.
5. Najděte vlastnosti **prvků výstupních dat** v souboru json pomocí UID uvedených ve sloupci "Prvek výstupních dat - UID".
6. Hledejte vlastnost: `"aggregationLevels": [4]`
7. Pokud úroveň odpovídá úrovni v cílové instanci, ponechte číslo tak, jak je. Pokud se číslo úrovně zařízení v cílové nstanci liší, upravte číslo podle toho.

### Pravidla ověření { #rehab-validation-rules }

Ověřovací pravidla obsažená v balíčku jsou seskupena podle datových sad, pro které byla nakonfigurována.

Všechny skupiny ověřovacích pravidel a odpovídající ověřovací pravidla jsou uvedeny v dodatku k této instalační příručce:

[Rehabilitace – pravidla validace](resources/rehab_validation_rules.xlsx)

Skupiny organizačních jednotek pro všechna pravidla ověřování jsou nastaveny na úroveň zařízení. Hodnota úrovně zařízení se nachází ve vlastnosti `"organisationUnitLevels"` každého ověřovacího pravidla. Ve výchozím nastavení je nastavena na `4`. Upravte tyto úrovně v souboru metadat tak, aby odpovídaly úrovni zařízení v cílové instanci před importem balíčku.

## Import metadat { #importing-metadata }

K importu balíčků metadat použijte aplikaci [Import/Export](#import_export) DHIS2. Před pokusem o skutečný import metadat je vhodné použít funkci „suchého běhu“ k identifikaci problémů. Pokud "suchý běh" nahlásí nějaké problémy nebo konflikty, podívejte se do sekce [konflikty importu](#handling-import-conflicts) níže. Pokud import „suché spuštění“/„ověření“ funguje bez chyby, pokuste se importovat metadata. Pokud import proběhne bez chyb, můžete přistoupit ke [konfiguraci](#configuration) modulu. V některých případech se konflikty nebo problémy při importu nezobrazí během „suchého běhu“, ale objeví se při pokusu o vlastní import. V tomto případě budou v souhrnu importu uvedeny všechny chyby, které je třeba vyřešit.

### Řešení konfliktů importu { #handling-import-conflicts }

> **POZNÁMKA**
>
> Pokud importujete balíček do nové instance DHIS2, nezaznamenáte konflikty importu, protože v cílové databázi nejsou žádná metadata. Po importu metadat přejděte k části „[Konfigurace](#configuration)“.

Může dojít k řadě různých konfliktů, i když nejběžnějším je, že v konfiguračním balíčku jsou objekty metadat s názvem, zkratkou a/nebo kódem, které již v cílové databázi existují. Existuje několik alternativních řešení těchto problémů s různými výhodami a nevýhodami. Který z nich je vhodnější, bude záviset například na typu objektu, u kterého ke konfliktu dojde.

#### Alternativa 1 { #alternative-1 }

Přejmenujte existující objekt v databázi DHIS2, u kterého existuje konflikt. Výhodou tohoto přístupu je, že není potřeba upravovat soubor .json, protože změny se místo toho provádějí prostřednictvím uživatelského rozhraní DHIS2. To bude pravděpodobně méně náchylné k chybám. To také znamená, že konfigurační balíček zůstane tak, jak je, což může být výhodou například při vydání aktualizací balíčku. Na původní objekty balíčku se také často odkazuje ve školicích materiálech a dokumentaci.

#### Alternativa 2 { #alternative-2 }

Přejmenujte objekt, u kterého došlo ke konfliktu v souboru .json. Výhodou tohoto přístupu je, že stávající metadata DHIS2 jsou ponechána tak, jak jsou. To může být faktor, když existuje školicí materiál nebo dokumentace, jako jsou SOP datových slovníků propojených s daným objektem, a to nezahrnuje žádné riziko záměny uživatelů úpravou metadat, se kterými jsou obeznámeni.

Všimněte si, že pro alternativu 1 i 2 může být modifikace stejně jednoduchá jako přidání malého pre / post-fix k názvu, aby se minimalizovalo riziko záměny.

#### Alternativa 3 { #alternative-3 }

Třetím a komplikovanějším přístupem je úprava souboru .json pro opětovné použití existujících metadat. Například v případech, kdy pro určitý koncept již existuje sada možností (např. „Pohlaví“), by tato sada možností mohla být odstraněna ze souboru .json a všechny odkazy na jeho UID nahrazeny odpovídající sadou možností již v databázi. Velkou výhodou tohoto (která se neomezuje na případy přímého konfliktu importu) je vyhnout se vytváření duplicitních metadat v databázi. Při provádění tohoto typu modifikace je třeba provést několik klíčových úvah:

-   vyžaduje odborné znalosti podrobné struktury metadat DHIS2
-   přístup nefunguje u všech typů objektů. Zejména určité typy objektů mají závislosti, které se tímto způsobem komplikovaně řeší, například v souvislosti s rozčleněními.
-   budoucí aktualizace konfiguračního balíčku budou komplikované.

## Konfigurace { #configuration }

Po úspěšném importu všech metadat existuje několik kroků, které je třeba provést, než bude modul funkční.

### Sdílení { #sharing }

Nejprve budete muset pomocí funkce _Sdílení_ DHIS2 nakonfigurovat, kteří uživatelé (skupiny uživatelů) by měli vidět metadata a data spojená s programem a také kdo může registrovat / zadávat data do programu. Ve výchozím nastavení je sdílení nakonfigurováno pro následující:

-   Ovládací panely
-   Vizualizace, mapy, zprávy o událostech a tabulky zpráv
-   Datové sady
-   Možnosti kategorie

Další informace o sdílení naleznete v [dokumentaci DHIS2](#sharing).

Balíček obsahuje tři základní skupiny uživatelů:

-   Rehabilitační přístup (zobrazit metadata/zobrazit data)
-   Rehab admin (zobrazit a upravit metadata / žádný přístup k datům)
-   Rehabilitace – (zobrazení metadat/zachycení a zobrazení dat)

Uživatelé jsou přiřazeni do příslušné skupiny uživatelů na základě jejich role v systému. Sdílení pro další objekty v balíčku může být upraveno v závislosti na nastavení. Další informace naleznete v [dokumentaci DHIS2 o sdílení](#sharing).

### Uživatelské role { #user-roles }

Uživatelé budou potřebovat uživatelské role, aby mohli pracovat s různými aplikacemi v rámci DHIS2. Doporučují se následující minimální role:

1. Analýza dat trasovače: Může zobrazit analytiku událostí a přistupovat k ovládacím panelům, zprávám o událostech, vizualizátorům událostí, vizualizátorům dat, kontingenčním tabulkám, zprávám a mapám.
2. Zachycování dat Trasovače: Může přidávat datové hodnoty, aktualizovat trasované entity, prohledávat trasované entity napříč organizačními jednotkami a přistupovat k zachycení trasovačů

Další informace o konfiguraci rolí uživatelů najdete v [dokumentaci DHIS2](https://docs.dhis2.org/).

### Přiřazení organizační jednotky { #organisation-unit-assignment }

Sady dat musí být přiřazeny organizačním jednotkám v rámci existující hierarchie, aby byly přístupné prostřednictvím aplikace pro zachycení. Níže uvedená tabulka poskytuje informace o přiřazení organizační jednotky pro datové sady Rehabilitace:

| Datová sada | UID | Typ formuláře datové sady | Období sběru dat | Typy zařízení |
| --- | --- | --- | --- | --- |
| Údaje o hustotě a incidenci postele | `giKizLegiUW` | výchozí | roční | Rehabilitační zařízení s vyhrazeným rehabilitačním lůžkovým oddělením |
| Dostupnost základního balíčku na PHC | `MGzqZDWvPhL` | sekce | roční | Primární zdravotnická zařízení podávající zprávy o rehabilitaci (Rehab PHC) |
| Personální obsazenost | `Sm2fALTZROS` | sekce | roční | Všechna zařízení hlásí Rehab (hlavní seznam zařízení) |
| Zpráva o hospitalizaci | `WjN1YoDtlOd` | vlastní | měsíčně | Všechna zařízení s lůžkovým oddělením (ne vyhrazeným rehabilitačním oddělením), které podává rehabilitaci (seznam hlavních zařízení) |
| Zpráva o rehabilitačním oddělení | `tP8et8TNWgF` | vlastní | měsíčně | Všechna zařízení s vyhrazeným rehabilitačním lůžkovým oddělením vykazujícím rehabilitaci (seznam hlavních zařízení) |
| Ambulantní zpráva | `zInFVXb98JD` | vlastní | měsíčně | Všechna zařízení s ambulantním oddělením s hlášením o rehabilitaci (hlavní seznam zařízení) |

### Přiřazení skupiny organizačních jednotek { #organisation-unit-group-assignment }

Organizační jednotky v cílovém systému musí být přiřazeny skupinám organizačních jednotek Rehab na základě přehledu v sekci [Skupiny organizačních jednotek](#rehab-orgunitgroups).

### Soubory dat { #rehab-dataset-config }

Následující soubory dat vyžadují po importu další konfiguraci:

#### Hustota lůžek { #bed-density }

Pokud jsou roční údaje o celkovém počtu rehabilitačních lůžek již shromažďovány ve stávajícím HMIS, není soubor údajů o hustotě rehabilitačních lůžek potřeba. Ujistěte se, že jste nahradili všechny výskyty datového prvku **"Dostupná rehabilitační lůžka (celkem)"** `K0Y94lADtGw` existujícím datovým prvkem UID ve všech metadatových objektech, kde se na tento datový prvek odkazuje:

| UID objektu metadat | Typ objektu metadat | Detaily |
| --- | --- | --- |
| `VOdQ2YRmSzf` | Indikátor | Datový prvek je odkazován v čitateli |

#### Personální hustota { #personnel-density }

Pokud jsou roční údaje o populaci již shromažďovány ve stávajícím HMIS, lze datový prvek **"GEN - Population"** `DkmMEcubiPv` ze souboru dat `Sm2fALTZROS` odstranit. Ujistěte se, že jste nahradili všechny výskyty datového prvku \*"GEN - Populace"\*\* existujícím UID datového prvku ve všech metadatových objektech, kde se na tento datový prvek odkazuje:

| UID objektu metadat | Typ objektu metadat | Detaily |
| --- | --- | --- |
| `OnxT9nXB9yB` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `hLkZBsoxgwG` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `VOdQ2YRmSzf` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `n0cE7LiP4j8` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `peWxNUcIjZw` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `dXNfY2I7umm` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `hpP5GW43n1J` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `s9SRcnMtI0K` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `RRCtatVRlI0` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `PuSDjaFs2we` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `tsIeJwq6x8L` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `U5tL3Eqq3Vj` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `NcA1znaVgFH` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `M0UPequfEYf` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `U5WwSS3zxlX` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `fhZ9MI3qTaA` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `YEjkkya4JCJ` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `xW6TcvEMhwG` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `TNjjTJr7fLe` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `uKK11dDx8HH` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `qTq20E3B08y` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `ePjfu6Fr4Jq` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `zNzm3AUiQ3B` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `Vq98oh9BIB1` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `klNqjksyNAL` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `bW75ZyPq9aZ` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `ME2YCnift7x` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `HTZ7STQR648` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `Z2f5wDvVxUL` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `XlISfeHbzxc` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `NVbwb4XlTVo` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `t26ObhmhjOb` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `FjVJNnVOu6S` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `fDj7xDywd5C` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `BLUTcTXPhts` | Indikátor | Datový prvek je odkazován ve jmenovateli |
| `RFVOIDIULVO` | Indikátor | Datový prvek je odkazován ve jmenovateli |

Úroveň sběru údajů pro údaje o **incidenci** musí být stejná nebo nižší než úroveň shromažďování údajů pro údaje o **populaci**.

Přiřazení souboru dat organizační jednotky **Personální hustota** by mělo zůstat na úrovni zařízení pro účely analytických výstupů.

### Duplikovaná metadata { #duplicated-metadata }

> **POZNÁMKA**
>
> Tato část platí pouze v případě, že importujete do databáze DHIS2, ve které již jsou přítomna metadata. Pokud pracujete s novou instancí DHIS2, přeskočte prosím tuto část a přejděte na [Přizpůsobení programu trasování](#adapting-the-tracker-program). Pokud používáte aplikace třetích stran, které se spoléhají na aktuální metadata, vezměte prosím v úvahu, že tato aktualizace by je mohla narušit.“

I když byla metadata úspěšně importována bez jakýchkoli konfliktů při importu, v metadatech mohou existovat duplikáty - datové prvky, trasované atributy entit nebo sady voleb, které již existují. Jak bylo uvedeno v části výše o řešení konfliktů, je třeba mít na paměti důležitý problém, že rozhodnutí o provádění změn metadat v DHIS2 musí také zohledňovat další dokumenty a zdroje, které jsou různými způsoby spojeny s existujícími metadaty a metadata, která byla importována prostřednictvím konfiguračního balíčku. Vyřešení duplikátů tedy není jen otázkou „vyčištění databáze“, ale také zajištěním toho, aby se tak dělo například bez narušení potenciálu integrace s jinými systémy, možnosti použít školicí materiál, rozbití SOP atd. To bude velmi záviset na kontextu.

Jedna důležitá věc, kterou je třeba mít na paměti, je, že DHIS2 má nástroje, které mohou skrýt některé složitosti potenciálních duplikací v metadatech. Například tam, kde existují duplicitní sady možností, mohou být skryty pro skupiny uživatelů pomocí [sharing](#sharing).

## Přizpůsobení programu { #adapting-the-program }

Po importu programu možná budete chtít provést určité úpravy programu. Příklady místních úprav, které _by mohly_ být provedeny, zahrnují:

-   Přidání dalších proměnných do formuláře.
-   Přizpůsobení názvů datových prvků / možností podle národních konvencí.
-   Přidávání překladů do proměnných nebo do formuláře pro zadávání údajů.
-   Modifikace ukazatelů na základě definic místních případů

Důrazně se však doporučuje věnovat velkou pozornost, pokud se rozhodnete změnit nebo odebrat některý ze zahrnutých formulářů / metadat. Existuje nebezpečí, že by úpravy mohly narušit funkčnost, například pravidla programu a indikátory programu.

### Mapování indikátoru { #indicator-mapping }

Částečnou implementaci balíčku Rehabilitace, tj. implementaci přizpůsobené sady klíčových indikátorů WHO, naleznete v [tabulce mapování indikátorů WHO na DHIS2](resources/rehab_indicator_mapping.xlsx).

Při přizpůsobování metadat se ujistěte, že identifikujete vizualizace a ovládací panely, kde se používají příslušné indikátory, a také datové prvky a kombinace kategorií použité v odpovídajících souborech dat.

## Odebírání metadat { #removing-metadata }

Aby byla vaše instance čistá a předešlo se chybám, doporučuje se z instance odstranit nepotřebná metadata. Odstranění nepotřebných metadat vyžaduje pokročilé znalosti DHIS2 a různých závislostí.
