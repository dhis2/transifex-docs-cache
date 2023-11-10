---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/program-indicators.md"
revision_date: "2021-09-16"
---

# Programové Indikátory { #capture_app_program_ind }

Následuje úplný seznam všech proměnných indikátorů programu, které jsou k dispozici v DHIS2, a poznámky o tom, zda byly nebo nebyly implementovány v aplikaci Android Capture.

Jakékoli problémy spojené s používáním konkrétní funkce v systému Android jsou zvýrazněny vykřičníkem.

| legenda | popis |
| :-: | :-- |
| ![](resources/icons/icon-complete.png) | Komponenta implementována |
| ![](resources/icons/icon-incomplete.png) | Komponenta není implementována (pravidlo selže) |
| ![](resources/icons/icon-na.png) | Nelze použít |
| ![](resources/icons/icon-wip.png) | Ve vývoji. Funkce ještě není zcela implementována nebo již bylo hlášeno neočekávané chování. |

## Běžné funkce pro použití ve výrazu indikátoru programu nebo filtru { #capture_app_program_ind_common_functions }

| Funkce | Popis | Status | Poznámky k provádění |
| --- | --- | :-: | --- |
| if | Vyhodnotí logický výraz a pokud true vrátí hodnotu true výrazu, pokud false vrátí hodnotu falešného výrazu. Argumenty musí dodržovat pravidla pro jakýkoli výraz indikátoru. | ![](resources/icons/icon-complete.png) |  |
| isNull | Vrátí true, pokud chybí hodnota prvku (null), jinak false. | ![](resources/icons/icon-complete.png) |  |
| isNotNull | Vrátí true, pokud hodnota prvku nechybí (není null), jinak false. | ![](resources/icons/icon-complete.png) |  |
| firstNonNull | Vrátí hodnotu prvního prvku, který nechybí (není null). Lze zadat libovolný počet argumentů. Jakýkoli argument může být také číselný nebo řetězcový literál, který bude vrácen, pokud všechny předchozí objekty mají chybějící hodnoty. | ![](resources/icons/icon-complete.png) |  |
| největší | Vrátí největší (nejvyšší) hodnotu zadaných výrazů. Lze uvést libovolný počet argumentů. | ![](resources/icons/icon-complete.png) |  |
| nejméně | Vrátí nejnižší (nejnižší) hodnotu zadaných výrazů. Lze uvést libovolný počet argumentů. | ![](resources/icons/icon-complete.png) |  |

## (d2) Funkce pro použití ve výrazu indikátoru programu nebo filtru { #capture_app_program_ind_d2_functions }

| Funkce | Popis | Status | Poznámky k provádění |
| --- | --- | :-: | --- |
| addDays | Vytvoří datum na základě data prvního argumentu a přidá počet dní druhého argumentu. | ![](resources/icons/icon-complete.png) |  |
| ceil | Zaokrouhlí vstupní argument na nejbližší celé číslo. | ![](resources/icons/icon-complete.png) |  |
| condition | Vyhodnotí logický výraz a pokud true vrátí hodnotu true výrazu, pokud false vrátí hodnotu výrazu false. Podmíněný výraz musí být označen uvozovkami. Argumenty true-expr a false-expr musí dodržovat pravidla libovolného výrazu indikátoru programu (včetně funkcí). | ![](resources/icons/icon-complete.png) |  |
| počet | Spočítá počet datových hodnot, které byly shromážděny pro danou fázi programu a datový prvek v průběhu registrace. Datový prvek argumentu je dodáván se syntaxí #{programStage.dataElement}. | ![](resources/icons/icon-complete.png) |  |
| countIfCondition | Spočítá počet datových hodnot, které odpovídají zadaným kritériím podmínek pro danou fázi programu a datový prvek v průběhu registrace. Datový prvek argumentu je dodáván se syntaxí #{programStage.dataElement}. Podmínka se dodává jako výraz v jednoduchých uvozovkách. | ![](resources/icons/icon-complete.png) |  |
| countIfValue | Spočítá počet datových hodnot, které odpovídají zadané přesné hodnotě pro danou fázi programu a datový prvek v průběhu registrace. Datový prvek argumentu je dodáván se syntaxí #{programStage.dataElement}. Hodnota může být pevně zapsaný text nebo číslo. | ![](resources/icons/icon-complete.png) |  |
| countIfZeroPos | Spočítá počet hodnot, které jsou nulové nebo kladné zadané pro zdrojové pole v argumentu. | ![](resources/icons/icon-complete.png) |  |
| daysBetween | Produkuje počet dní mezi dvěma datovými prvky / atributy typu datum. | ![](resources/icons/icon-complete.png) |  |
| floor | Zaokrouhlí vstupní argument na nejbližší celé číslo. | ![](resources/icons/icon-complete.png) |  |
| hasUserRole | Vrátí true, pokud má aktuální uživatel tuto roli, jinak false. | ![](resources/icons/icon-complete.png) |  |
| hasValue | Vrátí true, pokud má datový prvek / atribut hodnotu. | ![](resources/icons/icon-complete.png) |  |
| inOrgUnitGroup | Vyhodnocuje, zda je aktuální organizační jednotka ve skupině argumentů. Argument lze definovat buď ID, nebo kódem skupiny organizační jednotky. | ![](resources/icons/icon-complete.png) |  |
| left | Vyhodnocuje k levé části textu počet znaků od prvního znaku. | ![](resources/icons/icon-complete.png) |  |
| délka | Najděte délku řetězce. | ![](resources/icons/icon-complete.png) |  |
| minut mezi | Produkuje počet minut mezi dvěma datovými prvky / atributy typu „datum a čas“. | ![](resources/icons/icon-complete.png) |  |
| modulus | Produkuje absolutní hodnotu při dělení prvního a druhého argumentu. | ![](resources/icons/icon-complete.png) |  |
| monthsBetween | Produkuje počet celých měsíců mezi prvním a druhým argumentem. | ![](resources/icons/icon-complete.png) |  |
| oizp | Vrátí jeden, pokud je výraz nula nebo kladný, jinak vrátí nulu. | ![](resources/icons/icon-complete.png) |  |
| relationshipCount | Produkuje počet vztahů daného typu, který je připojen k zápisu nebo události. Pokud není uveden žádný typ, započítají se všechny typy. | ![](resources/icons/icon-incomplete.png) |  |
| vpravo | Vyhodnocuje na pravou část textu počet znaků od posledního znaku. | ![](resources/icons/icon-complete.png) |  |
| round | Zaokrouhlí vstupní argument na nejbližší celé číslo. | ![](resources/icons/icon-complete.png) |  |
| rozdělit | RSplit text oddělovačem a ponechat n-tý prvek (0 je první). | ![](resources/icons/icon-complete.png) |  |
| podřetězec | Vyhodnocuje se na část řetězce určenou počátečním a koncovým číslem znaku. | ![](resources/icons/icon-complete.png) |  |
| validatePatten | Vyhodnotí se jako true, pokud je vstupní text přesnou shodou s dodaným vzorem regulárního výrazu. | ![](resources/icons/icon-complete.png) |  |
| týdnů mezi | Produkuje počet celých týdnů mezi dvěma datovými prvky / atributy typu datum. | ![](resources/icons/icon-complete.png) |  |
| yearsBetween | Produkuje počet let mezi prvním a druhým argumentem. | ![](resources/icons/icon-complete.png) |  |
| zing | Vrátí nulu, pokud je výraz záporný, jinak vrátí hodnotu výrazu. | ![](resources/icons/icon-complete.png) |  |
| zpvc | Vrátí počet číselných nul a kladných hodnot mezi danými argumenty objektu. | ![](resources/icons/icon-complete.png) |  |

## Proměnné, které se mají použít ve výrazu nebo filtru indikátoru programu { #capture_app_program_ind_variables }

| Typ proměnné | Popis typu proměnné | Status | Poznámky k provádění |
| --- | --- | :-: | --- | --- |
| Datum události<br/>event_date | Datum, kdy se událost konala. | ![](resources/icons/icon-complete.png) |  |
| Datum vytvoření\*<br/>creation_date | Datum, kdy byla v systému vytvořena událost nebo registrace. | ![](resources/icons/icon-complete.png) |  |
| Datum platnosti<br/>due_date | Datum ukončení platnosti události. | ![](resources/icons/icon-complete.png) |  |
| Datum synchronizace\*<br/>sync_date | Datum, kdy byla událost nebo zápis naposledy synchronizována s aplikací pro Android. | ![](resources/icons/icon-incomplete.png) |  |
| Datum incidentu<br/>incident_date | Datum výskytu události. | ![](resources/icons/icon-complete.png) |  |
| Datum zápisu (na uživatelském rozhraní není viditelné) <br/>enrollment_date | Datum, kdy byla trasovaná instance entity zapsána do programu. | ![](resources/icons/icon-complete.png) |  |
| Stav Zápisu<br/>enrollment_status | Lze použít k zahrnutí nebo vyloučení zápisů v určitých stavech. | ![](resources/icons/icon-complete.png) |  |
| Aktuální datum<br/>current_date | Aktuální datum. | ![](resources/icons/icon-complete.png) |  |
| Dokončené datum | Datum události je dokončeno. | ![](resources/icons/icon-complete.png) |  |
| Počet hodnot<br/>value_count | Počet nenulových hodnot ve výrazové části události. | ![](resources/icons/icon-complete.png) |  |
| Počet nulových nebo kladných hodnot<br/>zero_pos_value_count | Počet číselných kladných hodnot ve výrazové části události. | ![](resources/icons/icon-complete.png) |  |
| Počet událostí<br/>event_count | Počet událostí (užitečné v kombinaci s filtry). | ![](resources/icons/icon-complete.png) |  |
| Počet zápisů<br/>enrollment_count | Počet zápisů (užitečné v kombinaci s filtry). | ![](resources/icons/icon-complete.png) | Indikátory v aplikaci pro Android se počítají v doméně jednoho zápisu TEI. Hodnota vždy 1. |  |
| Počet TEI<br/>tei_count | Počet trasovaných instancí entit (užitečné v kombinaci s filtry). | ![](resources/icons/icon-na.png) | Indikátory v aplikaci pro Android se počítají v doméně jednoho zápisu TEI. Hodnota vždy 1. |  |
| Název fáze programu<br/>program_stage_name | Lze použít ve filtrech pro zahrnutí pouze určitých fází programu do filtru pro programy sledování. | ![](resources/icons/icon-incomplete.png) |  |
| ID fáze programu<br/>program_stage_id | Lze použít ve filtrech pro zahrnutí pouze určitých fází programu do filtru pro programy sledování. | ![](resources/icons/icon-incomplete.png) |  |
| Začátek období hlášení zpráv<br/>reporting_period_start | Lze použít ve filtrech nebo výrazech pro srovnání jakéhokoli data s prvním datem v každém vykazovaném období. | ![](resources/icons/icon-na.png) | Indikátory v aplikaci pro Android se počítají v doméně jedné registrace TEI. |  |
| Konec období hlášení zpráv<br/>reporting_period_end | Lze použít ve filtrech nebo výrazech pro porovnání libovolného data s posledním inkluzivním datem v každém vykazovaném období. | ![](resources/icons/icon-na.png) | Indikátory v aplikaci pro Android se počítají v doméně jedné registrace TEI. |  |
| Počet organizačních jednotek<br/>organisationunit_count | . | ![](resources/icons/icon-na.png) |  |  |

[Reference k dokumentaci](https://docs.dhis2.org/master/en/user/html/configure_program_indicator.html%23program_indicator_functions_variables_operators&sa=D&ust=1557433016643000)
