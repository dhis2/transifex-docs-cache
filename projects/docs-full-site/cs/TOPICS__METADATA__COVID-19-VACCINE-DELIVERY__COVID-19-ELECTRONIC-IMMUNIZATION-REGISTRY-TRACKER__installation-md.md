---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/docs/CVIR-installation.md"
revision_date: "2022-01-19"
---

# Elektronický registr imunizace Covid-19 – Průvodce instalací trasovače{ #cvc-eir-trk-installation }

Tento dokument obsahuje instalační příručku pro aktualizovaný balíček trasování elektronického imunizačního registru COVAC a doplňkový agregační modul pro denní hlášení na základě údajů z trasování.

Výchozí jazyk systému: angličtina

Dostupné překlady: francouzština, španělština, portugalština

## Přehled { #overview }

Soubory json metadat balíčku obsahují komponentu „balíček“, která poskytuje technické podrobnosti o verzi a obsahu balíčku. Níže jsou uvedeny soubory dostupné v aktuální verzi balíčku.

### DHIS2.35 { #dhis235 }

=== "Kompletní balíček"

    ```json
    "package": {
        "DHIS2Build": "35d663a",
        "DHIS2Version": "2.35.11",
        "code": "CVIR00",
        "description": "COVID19 Electronic Immunization Registry",
        "lastUpdated": "20220118T163027",
        "locale": "en",
        "name": "COVAC_EIR_TKR_1.2.0_DHIS2.35.11-en",
        "type": "TKR",
        "version": "1.2.0"
    }
    ```

=== "Souhrnný balíček"

    ```json
    "package": {
        "DHIS2Build": "35d663a",
        "DHIS2Version": "2.35.11",
        "code": "CVIRAG",
        "description": "",
        "lastUpdated": "20220119T094326",
        "locale": "en",
        "name": "CVIR_EIR_AGG_1.2.0_DHIS2.35.11-en",
        "type": "AGG",
        "version": "1.2.0"
    }
    ```

=== "Indikátory programu (přenos z trasování na agregát)"

    ```json
    "package": {
        "DHIS2Build": "35d663a",
        "DHIS2Version": "2.35.11",
        "code": "CVIRPI",
        "description": "COVID19 Electronic Immunization Registry",
        "lastUpdated": "20220118T163027",
        "locale": "en",
        "name": "COVAC_EIR_TKR_1.2.0_DHIS2.35.11-en",
        "type": "TKR",
        "version": "1.2.0"
    }
    ```

### DHIS2.36 { #dhis236 }

=== "Kompletní balíček"

    ```json
    "package": {
        "DHIS2Build": "5d136cb",
        "DHIS2Version": "2.36.6",
        "code": "CVIR00",
        "description": "COVID19 Electronic Immunization Registry",
        "lastUpdated": "20220119T084447",
        "locale": "en",
        "name": "COVAC_EIR_TKR_1.2.0_DHIS2.36.6-en",
        "type": "TKR",
        "version": "1.2.0"
    }
    ```

=== "Souhrnný balíček"

    ```json
    "package": {
        "DHIS2Build": "5d136cb",
        "DHIS2Version": "2.36.6",
        "code": "CVIRAG",
        "description": "",
        "lastUpdated": "20220119T084447",
        "locale": "en",
        "name": "CVIR_EIR_AGG_1.2.0_DHIS2.36.6-en",
        "type": "AGG",
        "version": "1.2.0"
    }
    ```

=== "Indikátory programu (přenos z trasování na agregát)"

    ```json
    "package": {
        "DHIS2Build": "5d136cb",
        "DHIS2Version": "2.36.6",
        "code": "CVIRPI",
        "description": "COVID19 Electronic Immunization Registry",
        "lastUpdated": "20220119T084447",
        "locale": "en",
        "name": "COVAC_EIR_TKR_1.2.0_DHIS2.36.6-en",
        "type": "TKR",
        "version": "1.2.0"
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

Balíček sledování elektronického registru imunizace Covid-19 obsahuje tři soubory metadat. Obsah a účel každého jednotlivého souboru jsou popsány níže:

| Identifikátor balíku | Obsah | Účel |
| --- | --- | --- |
| CVC_EIR-TRK-Electronic_Immunization_Registry_Covid19_Vaccines | Aktualizovaný balíček trasovače, <br> agregovaná datová sada pro automatizovaný tracker-to-aggregate-transfer, <br> ovládací panel založený na agregovaných hodnotách indikátorů | Nová implementace |
| CVC_EIR-AGG-Electronic_Immunization_Registry_Covid19_Vaccines | Souhrnná datová sada pro automatizovaný tracker-to-aggregate-transfer, <br> dashboard na základě agregovaných hodnot indikátorů | Aktualizace na existující implementaci sledovače, <br> Nastavení přenosu z trasovače na agregát, <br> Použití denního souhrnného ovládacího panelu |
| CVC_EIR-PI-Electronic_Immunization_Registry_Covid19_Vaccines | 13 aktualizovaných programových indikátorů z původního balíčku. <br> PI jsou mapovány na agregované datové prvky a kombinace možností kategorie v denní sadě souhrnných dat | Aktualizace na stávající implementaci |

> **Poznámka**
>
> Balíček není hotový nástroj pro přenos dat ze sledovače na souhrnný. Struktura balíčku metadat a navrhované mapování metadat umožňuje implementátorovi nastavit přenos dat na základě existujících nástrojů a pokynů. Další informace jsou k dispozici v [Dokumentu pro sledování agregovaného přenosu dat](https://docs.dhis2.org/en/implement/maintenance-and-use/tracker-and-aggregate-data-integration.html#how-to-saving-aggregated-tracker-data-as-aggregate-data-values).

## Příprava souboru metadat { #preparing-the-metadata-file }

### Průvodce mapováním pro přenos dat { #mapping-guide-for-data-transfer }

13 programových indikátorů, které lze použít pro přenos dat z trasovače do agregovaného, je mapováno na odpovídající datové prvky a kombinace možností kategorií souhrnné datové sady.

> **Příklad**
>
> Indikátor programu **Počet lidí, kteří dostanou první dávku (ženy 0-59)** `RJ6pdxga9Od`je mapován na kombinaci možností kategorie **Žena, 0-59 let** `FsZSFGKirY0` datového prvku **COVAC - Lidé s 1. dávkou** `RjT7dmzunF4`

Mapování je založeno na kódech objektů metadat.

Vlastní atribut **Datový prvek pro export souhrnných dat** `vudyDP7jUy5` obsahuje referenční kód prvků agregovaných dat, např. **CVC_EIR_AGG_PPL_1ST_DOSE**

Pole **Kombinace možností kategorie pro agregovaný export** obsahuje referenční kódy kombinací možností kategorií, např. **CVC_EIR_0059Y_F**

Navrhovaný přenos hodnot z trasovače na agregát je založen na následujících požadavcích GET a POST API:

1. Zdrojový požadavek:  `../api/analytics/dataValueSet.json?dimension=dx:` "{program indicator uid/s}" `&dimension=pe:` "{relative period/s}" `&dimension=ou:` {organisation unit level} `&outputIdScheme=ATTRIBUTE:` {"custom attribute:`vudyDP7jUy5`"}
2. Cílový požadavek: `..api/dataValueSets?dataElementIdScheme=CODE&categoryOptionComboIdScheme=CODE&importStrategy=CREATE_AND_UPDATE&mergeMode=REPLACE&dryRun=false`

### Indikátory programu { #program-indicators }

Programové indikátory potřebné pro agregaci hodnot dat jsou zahrnuty ve skupině programových indikátorů **COVAC - Trasovač na souhrn** `NXBR4r6MwAO`

| Indikátor programu | UID | Kód | DE pro agregovaný vývoz | CoC pro agregovaný export |
| --- | --- | --- | --- | --- |
| Počet lidí, kteří dostali první dávku (ženy 0-59) | `RJ6pdxga9Od` | CVC_EIR_PPL_1ST_DOSE_0059Y_F | CVC_EIR_AGG_PPL_1ST_DOSE | 0059Y_F |
| Počet lidí, kteří dostali první dávku (ženy 60+) | `x4L0LuEBHhW` | CVC_EIR_PPL_1ST_DOSE_60PLUSY_F | CVC_EIR_AGG_PPL_1ST_DOSE | 60PLUSY_F |
| Počet lidí, kteří dostali první dávku (muži 0-59) | `hqm8znlAzkT` | CVC_EIR_PPL_1ST_DOSE_0059Y_M | CVC_EIR_AGG_PPL_1ST_DOSE | 0059Y_M |
| Počet lidí, kteří dostali první dávku (muži 60+) | `aIIHyDy8AMW` | CVC_EIR_PPL_1ST_DOSE_60PLUSY_M | CVC_EIR_AGG_PPL_1ST_DOSE | 60PLUSY_M |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (ženy 0-59) | `xY4T9hHXNji` | CVC_EIR_PPL_2ND_DOSE_0059Y_F | CVC_EIR_AGG_PPL_2ND_DOSE | 0059Y_F |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (ženy 60+) | `h9G7i6mQKef` | CVC_EIR_PPL_2ND_DOSE_60PLUSY_F | CVC_EIR_AGG_PPL_2ND_DOSE | 60PLUSY_F |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (muži 0-59) | `MGjwUUNsE60` | CVC_EIR_PPL_2ND_DOSE_0059Y_M | CVC_EIR_AGG_PPL_2ND_DOSE | 0059Y_M |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (muži 60+) | `qh0kIjHZbP8` | CVC_EIR_PPL_2ND_DOSE_60PLUSY_M | CVC_EIR_AGG_PPL_2ND_DOSE | 60PLUSY_M |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového přípravku (ženy 0-59) | `Zp39TSOR8eW` | CVC_EIR_PPL_LAST_DOSE_0059Y_F | CVC_EIR_AGG_PPL_LAST_DOSE | 0059Y_F |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (ženy 60+) | `XFUvVgqPukT` | CVC_EIR_PPL_LAST_DOSE_60PLUSY_F | CVC_EIR_AGG_PPL_LAST_DOSE | 60PLUSY_F |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (muži 0-59) | `FZNIlzPRMmL` | CVC_EIR_PPL_LAST_DOSE_0059Y_M | CVC_EIR_AGG_PPL_LAST_DOSE | 0059Y_M |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (muži 60+) | `zovL7DKBRuK` | CVC_EIR_PPL_LAST_DOSE_60PLUSY_M | CVC_EIR_AGG_PPL_LAST_DOSE | 60PLUSY_M |
| Základní podmínky - Lidé s | `Zn0UuSRYyJw` | CVC_EIR_PPL_UNDER_CONDITIONS | CVC_EIR_AGG_PPL_UNDER_CONDITIONS | VÝCHOZÍ |

Tyto programové indikátory jsou součástí původního balíčku, ale musí být aktualizovány kvůli přidanému mapování.

> **Poznámka**
>
> Pokud byly původní programové indikátory ve vašem systému upraveny jako součást místního adaptačního procesu, mějte na paměti, že po importu aktualizované sady programových indikátorů budou všechny změny přepsány. Pokud některý z vašich upravených programových indikátorů má stejné UID jako programové indikátory uvedené v tabulce výše, ujistěte se, že jste před importem zkopírovali upravené programové indikátory.

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
| Pouze čitatel (číslo) | `CqNPn5KzksS` | `../api/indicatorTypes.json?filter=number:eq:true&filter=factor:eq:1` |

### TrackedEntityType { #tracked-entity-type }

Stejně jako typy indikátorů můžete mít ve své databázi DHIS2 již existující typy trasovaných entit. Odkazy na typ trasované entity by se měly změnit tak, aby odrážely to, co je ve vašem systému, abyste nevytvářeli duplikáty. Níže uvedená tabulka obsahuje UID, která lze nahradit, a také koncové body API pro identifikaci stávajících UID:

| Objekt | UID | Koncový bod API |
| --- | --- | --- |
| Osoba | `MCPQUTHX1Ze` | `../api/trackedEntityTypes.json?filter=name:eq:Person` |

### Vizualizace pomocí UID kořenové organizační jednotky { #visualizations-using-root-organisation-unit-uid }

Vizualizace, sestavy událostí, tabulky sestav a mapy, které jsou přiřazeny konkrétní úrovni organizační jednotky nebo skupině organizačních jednotek, mají odkaz na kořenovou organizační jednotku (úroveň 1). Takové objekty, pokud jsou v souboru metadat přítomny, obsahují zástupný symbol ` <OU_ROOT_UID> `. Použijte funkci vyhledávání v editoru souborů .json k případné identifikaci tohoto zástupného symbolu a jeho nahrazení UID organizační jednotky úrovně 1 v cílové instanci.

### Kódy možností { #option-codes }

Podle konvencí pojmenování DHIS2 používají kódy metadat velká písmena, podtržítka a žádné mezery. Některé výjimky, které se mohou vyskytnout, jsou uvedeny v dokumentaci příslušného balíčku. Všechny kódy zahrnuté v objektech metadat v aktuální verzi balíčku byly upraveny tak, aby odpovídaly konvencím pojmenování. Může se stát, že kódy používané v dřívějších verzích balíčku používaly malá písmena. Pokud hodnoty dat ve stávajících implementacích obsahují malá písmena, je důležité tyto hodnoty aktualizovat přímo v databázi.

Níže uvedená tabulka obsahuje všechny sady možností, kde byly kódy v balíčku metadat změněny na velká písmena. Před importem metadat do instance zkontrolujte, zda se sady možností ve stávajícím systému shodují se sadami v balíčku .json a použijte stejné kódy možností velkými písmeny.

| Název sady možností               | Možnost nastavit UID |
| ----------------------------- | -------------- |
| COVAC - AEFI Těhotenství        | `ilxtWultuYP`  |
| COVAC - Povolání            | `CNNH0YKxRh9`  |
| COVAC - Trimestr             | `kgDmgTYZICP`  |
| COVAC Značka vakcíny           | `UJTnyCB3cyk`  |
| COVAC - Výrobci vakcín | `DtOGtoLbaB5`  |
| COVAC - Názvy vakcín         | `VQo3HkUlMHc`  |
| Pohlaví                           | `WDUwjiW2rGH`  |
| Ano / Ne / Neznámý                | `L6eMZDJkCwX`  |

Níže uvedená tabulka obsahuje prvky metadat, které používají ovlivněnou sadu možností:

| Objekt metadat | Název | UID |
| --- | --- | --- |
| Datový prvek | COVAC - Těhotenství | `BfNZcj99yz4` |
| Datový prvek | COVAC - Průběh těhotenství | `CBAs12YL4g7` |
| Datový prvek | COVAC – Dříve nakažený COVID | `LOU9t0aR0z7` |
| Datový prvek | COVAC - Základní zdravotní stav | `bCtWZGjSWM8` |
| Datový prvek | COVAC - Značka vakcíny | `rWYryQb3ohn` |
| Datový prvek | COVAC - Výrobce vakcín | `rpkH9ZPGJcX` |
| Datový prvek | COVAC - Název vakcíny | `bbnyNYD1wgS` |
| Atribut trasované entity | COVID - Povolání | `LY2bDXpNvS7` |
| Atribut trasované entity | Pohlaví | `oindugucx72` |

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

Pro hodnoty atributu trasované entity použijte:

    ```SQL
    UPDATE trackedentityattributevalue
    SET value = <new value>
    WHERE trackedentityattributeid=<affected trackedentityattribute database_id> AND value=<old value>;
    ```

> **Příklad**
>
> Chcete-li nahradit kód možnosti 'yes' za 'YES' pro existující datové hodnoty (datový prvek COVAC - Dříve infikovaný COVID `LOU9t0aR0z7`) v programové fázi s id=1510410385 (příklad id), bude příkaz nakonfigurován následovně :
>
> ```SQL
> UPDATE programstageinstance
> SET eventdatavalues = jsonb_set(eventdatavalues, '{"LOU9t0aR0z7","value"}', '"YES"')
> WHERE eventdatavalues @> '{"LOU9t0aR0z7":{"value": "yes"}}'::jsonb
> AND programstageid=1510410385;
> ```

Kódy voleb se také používají ve výrazech programových pravidel, programových indikátorech atd. Pokud aktualizujete volby kódu ve vašem systému, ujistěte se, že aktualizujete kódy ve všech dotčených objektech metadat.

### Pořadí řazení pro možnosti { #sort-order-for-options }

Zkontrolujte, zda pořadí řazení `sortOrder` možností ve vašem systému odpovídá pořadí řazení možností obsažených v balíčku metadat. To platí pouze v případě, že soubor json a cílová instance obsahují volby a sady voleb se stejným UID.

Po importu se ujistěte, že pořadí řazení možností v sadě možností začíná na 1. V hodnotách pořadí řazení by neměly být žádné mezery (např. 1,2,3,5,6).

Pořadí řazení lze upravit v aplikaci Údržba.

1. Přejděte na příslušnou sadu možností
2. Otevřete sekci „Možnosti“.
3. Použijte alternativy "ŘADIT PODLE JMÉNA", "ŘADIT PODLE KÓDU/HODNOTY" nebo "ŘADIT RUČNĚ".

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

-   Typ trasované entity
-   Program
-   Fáze programu
-   Ovládací panely
-   Vizualizace, mapy, zprávy o událostech a tabulky zpráv
-   Datové sady
-   Možnosti kategorie

Další informace o sdílení naleznete v [dokumentaci DHIS2](#sharing).

Balíček obsahuje čtyři základní skupiny uživatelů:

-   COVAC - Analýza dat imunizace COVID-19
-   COVAC – Správa údajů o imunizaci COVID-19
-   COVAC – Zadání údajů o imunizaci COVID-19
-   COVAC – Správa metadat imunizace COVID-19

Ve výchozím nastavení jsou těmto skupinám uživatelů přiřazena následující oprávnění:

| Objekt | Uživatelská skupina |  |  |  |
| --- | --- | --- | --- | --- |
|  | _COVAC – Analýza dat o imunizaci COVID-19_ | _COVAC – Správce údajů o imunizaci COVID-19_ | _COVAC – Zadání údajů o imunizaci COVID-19_ | _COVAC – Správce metadat imunizace COVID-19_ |
| _*Typ trasované entity*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit | Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit |
| _*Program*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit | Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit |
| _*Fáze programu*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit | Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit |
| _*Ovládací panely*_ | Metadata : lze zobrazit | Metadata : lze zobrazit | Žádný přístup | Metadata : lze upravovat a prohlížet |
| _*Datové sady*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit | Žádný přístup | Metadata: lze upravovat a prohlížet <br> Data: Bez přístupu |

Uživatelé jsou přiřazeni do příslušné skupiny uživatelů na základě jejich role v systému. Sdílení pro další objekty v balíčku může být upraveno v závislosti na nastavení. Další informace naleznete v [dokumentaci DHIS2 o sdílení](#sharing).

### Uživatelské role { #user-roles }

Uživatelé budou potřebovat uživatelské role, aby mohli pracovat s různými aplikacemi v rámci DHIS2. Doporučují se následující minimální role:

1. Analýza dat trasovače: Může zobrazit analytiku událostí a přistupovat k ovládacím panelům, zprávám o událostech, vizualizátorům událostí, vizualizátorům dat, kontingenčním tabulkám, zprávám a mapám.
2. Zachycování dat Trasovače: Může přidávat datové hodnoty, aktualizovat trasované entity, prohledávat trasované entity napříč organizačními jednotkami a přistupovat k zachycení trasovačů

Další informace o konfiguraci rolí uživatelů najdete v [dokumentaci DHIS2](https://docs.dhis2.org/).

### Organizační jednotky { #organisation-units }

Program a datové sady musí být přiřazeny organizačním jednotkám v rámci stávající hierarchie, aby byly přístupné prostřednictvím aplikací pro sledování / zachycování.

### Duplikovaná metadata { #duplicated-metadata }

> **POZNÁMKA**
>
> Tato část platí pouze v případě, že importujete do databáze DHIS2, ve které již jsou přítomna metadata. Pokud pracujete s novou instancí DHIS2, přeskočte prosím tuto část a přejděte na [Přizpůsobení programu trasování](#adapting-the-program). Pokud používáte aplikace třetích stran, které se spoléhají na aktuální metadata, vezměte prosím v úvahu, že tato aktualizace by je mohla poškodit.

I když byla metadata úspěšně importována bez jakýchkoli konfliktů při importu, v metadatech mohou existovat duplikáty - datové prvky, trasované atributy entit nebo sady voleb, které již existují. Jak bylo uvedeno v části výše o řešení konfliktů, je třeba mít na paměti důležitý problém, že rozhodnutí o provádění změn metadat v DHIS2 musí také zohledňovat další dokumenty a zdroje, které jsou různými způsoby spojeny s existujícími metadaty a metadata, která byla importována prostřednictvím konfiguračního balíčku. Vyřešení duplikátů tedy není jen otázkou „vyčištění databáze“, ale také zajištěním toho, aby se tak dělo například bez narušení potenciálu integrace s jinými systémy, možnosti použít školicí materiál, rozbití SOP atd. To bude velmi záviset na kontextu.

Jedna důležitá věc, kterou je třeba mít na paměti, je, že DHIS2 má nástroje, které mohou skrýt některé složitosti potenciálních duplikací v metadatech. Například tam, kde existují duplicitní sady možností, mohou být skryty pro skupiny uživatelů pomocí [sharing](#sharing).

## Přizpůsobení programu { #adapting-the-program }

Po importu programu možná budete chtít provést určité úpravy programu. Příklady místních úprav, které _by mohly_ být provedeny, zahrnují:

-   Přidání dalších proměnných do formuláře.
-   Přizpůsobení názvů datových prvků / možností podle národních konvencí.
-   Přidávání překladů do proměnných nebo do formuláře pro zadávání údajů.
-   Úprava indikátorů programu na základě místních definic případů

Důrazně se však doporučuje věnovat velkou pozornost, pokud se rozhodnete změnit nebo odebrat některý ze zahrnutých formulářů / metadat. Existuje nebezpečí, že by úpravy mohly narušit funkčnost, například pravidla programu a indikátory programu.

## Odebírání metadat { #removing-metadata }

Aby byla vaše instance čistá a předešlo se chybám, doporučuje se z instance odstranit nepotřebná metadata.

Původní ovládací panel **COVAC - registr vakcín COVID-19** `YYtAbckt77l` byl z aktualizovaného balíčku odstraněn a nahrazen novým ovládacím panelem: **COVAC - Daily monitoring** `iBWlFCvvtkH`

Chcete-li odstranit starý ovládací panel ze systému, musíte:

1. Poznamenat si názvy / UID všech objektů obsažených na ovládacím panelu.
2. Odstranit všechny položky z ovládacího panelu a uložit to.
3. Smazat ovládací panel.
4. Odstranit všechny vizualizace, mapy, zprávy o událostech a tabulky zpráv obsažené v původním ovládacím panelu.

> **POZNÁMKA**
>
> Přímo z databáze pomocí SQL příkazů je možné smazat ovládací panel, jeho položky  a všechny relevantní vizualizace, mapy a sestavy.
