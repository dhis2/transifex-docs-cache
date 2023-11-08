---
edit_url: "https://github.com/dhis2-metadata/REHAB_AGG/blob/master/docs/rehab_agg-design.md"
revision_date: "2022-05-25"
---

# Návrh rehabilitačního agregačního systému { #rehab-agg-design }

![](resources/images/rehab_logo-en.png){ .center }

## Úvod { #introduction }

Globální trendy v oblasti zdraví a stárnutí signalizují potřebu zásadního rozšíření rehabilitačních služeb v zemích po celém světě a zejména v zemích s nízkými a středními příjmy. Investice do rehabilitace umožňuje lidem se zdravotním stavem dosáhnout a udržet optimální fungování zlepšením jejich zdraví a zvýšením jejich účasti na životě. Posílení rehabilitace ve zdravotnických systémech je zásadní pro reakci na rostoucí poptávku a pro zajištění dostupnosti a dostupné rehabilitace pro ty, kteří ji potřebují. Jak doporučuje [iniciativa WHO Rehabilitation 2030, Výzva k akci](https://www.who.int/initiatives/rehabilitation-2030), klíčovou akcí k posílení rehabilitace je shromažďování údajů relevantních pro rehabilitaci za účelem zlepšení informací o zdraví systémy (HIS).

Data, která jsou shromažďována prostřednictvím rutinního hlášení rehabilitačního zdravotnického zařízení, jak z individuálních záznamů, tak ze záznamů o službách, se používají ke shromažďování informací pro definování cílů a výsledků rehabilitace, klinického rozhodování, odhadů využití služeb a řízení kvality. Pravidelné monitorování rehabilitačních služeb na národní a subnárodní úrovni poskytuje informace o jejich dostupnosti a distribuci, které mohou informovat o opatřeních, která jsou přijímána k dosažení všeobecné zdravotní péče (UHC). Data o rehabilitaci na systémové úrovni a informace o fungování podporují rozhodování o rehabilitaci ve zdravotní politice, managementu a klinické péči. Informace o fungování jsou zásadní pro rozhodování v rehabilitaci na všech úrovních zdravotního systému, protože cílem rehabilitace je optimalizovat fungování ve světle postižení, úrazů a akutních či chronických onemocnění.

## Účel { #purpose }

Dokument Návrh rehabilitačního agregačního systému poskytuje přehled konstrukčních principů a pokynů používaných k vývoji balíčku digitálních dat pro souhrnný rehabilitační dohled. Tento dokument je určen pro použití implementátory DHIS2 na národní a regionální úrovni, aby mohli podporovat implementaci a lokalizaci balíčku. Balíček metadat Rehabilitace lze přizpůsobit místním potřebám a národním směrnicím. Při lokalizaci a přijímání balíčku je třeba vzít v úvahu zejména místní pracovní toky a národní směrnice.

## Pozadí { #background }

Poskytování rehabilitačních služeb pokrývá široké spektrum činností pro různé zdravotní stavy a zajišťuje je multidisciplinární pracovní síla na všech administrativních úrovních zdravotnictví. Rehabilitační indikátory pro rutinní výkaznictví zdravotnických zařízení pokrývají běžné typy poskytované rehabilitace a jejich relevantní vlastnosti pro rozhodování jak na úrovni systému, tak na úrovni zdravotnického zařízení. Tento modul, který si je plně vědom potenciální zátěže sběru dat ve zdravotnických zařízeních, využívá obecný přístup z hlediska poskytování služeb a nezahrnuje monitorování konkrétních rehabilitačních intervencí ani funkce související s konkrétními typy intervencí.

**Jaké jsou očekávané výsledky?**

-   Indikátory řídí shromážděná data a podporují integraci rehabilitace do výkaznictví na úrovni zařízení.

-   Analytický rámec podporuje rozhodování ve zdravotnictví o rehabilitaci. Informuje analytické, monitorovací a hodnotící týmy a umožňuje manažerům podívat se na výkon rehabilitačního sektoru, včetně jeho integrace do zdravotnického systému, trendy zdravotního stavu a využití rehabilitačních služeb, vzorce vlastností a geografické rozdíly v pokrytí služeb. dodání v průběhu času. Rámec analýzy by měl pomoci programovým manažerům a zdravotním plánovačům odpovědět na otázky M&E rehabilitace, jako jsou: Jsou rehabilitační služby vybaveny adekvátními zdroji a kde jsou mezery? Do jaké míry jsou rehabilitační služby využívány a jaké jsou vlastnosti využití ve vztahu ke kapacitě služeb, profilu uživatele a platformě poskytování služeb? Jak rehabilitace přispívá k UHC? Jak se účinnost rehabilitace vyvíjí v čase? Jak dobře je rehabilitace integrována do zdravotního systému a do kontinua péče? Do jaké míry mají lidé, kteří potřebují delší pobyt, vysoce intenzivní, multidisciplinární rehabilitaci, přístup ke kvalitní péči?

-   Programoví manažeři a plánovači by mohli data využít k vytvoření a sledování měření v reálném čase týkajících se přístupnosti, dostupnosti, lidských zdrojů, kvality a výsledku služeb.

-   Navržené standardní indikátory mohou být použity pro účely monitorování operačního a strategického plánování obnovy. Údaje se poté shromažďují za účelem sledování pokroku směrem k cílům (národního) strategického plánu. Zatímco dokument „WHO Rehabilitation in Health System – Guide for Action“ poskytuje návod pro posílení zdravotnického systému, obsahuje část o monitorování strategického plánu rehabilitace nazvaného FRAME2. Pro tento záměr je zahrnuta nabídka indikátorů rehabilitace (RIM) se 40 indikátory. Ze 40 indikátorů RIM je 11 indikátorů shromažďováno s využitím dat primárně poskytovaných zdravotnickými zařízeními. Těchto 11 ukazatelů jako takových tvoří základ seznamu ukazatelů zařízení pro rehabilitaci, které jsou doporučovány k běžnému sběru zařízeními a shromažďovány prostřednictvím informačních systémů okresního zdravotnického managementu (DHMIS).

## Předpokládaní uživatelé { #intended-users }

Informace poskytované rutinním sběrem dat a hlášením z rehabilitačních zdravotnických zařízení je třeba analyzovat a využívat. To obvykle provádí následující cílové publikum:

-   Ministerstvo zdravotnictví s rozhodovací pravomocí, jako jsou manažeři rehabilitačních programů, manažeři dat a manažeři zdravotnických informačních systémů;
-   partneři rehabilitačního programu a plánovači programů;
-   Manažeři zdravotnických zařízení pro rehabilitaci;
-   Výzkumné ústavy zapojené do hodnocení a zlepšování rehabilitačních dat a informačních systémů.

## Přehled modulu { #module-overview }

Souhrnný balíček Rehabilitace obsahuje 6 navrhovaných datových sad pro sběr dat a 7 dashboardů.

### Datové sady { #data-sets }

Formuláře pro zadávání dat jsou logicky rozděleny podle období sběru dat a typů zdravotnických zařízení.

#### Údaje o hustotě a výskytu lůžek { #bed-density-and-incidence-data }

![Hustota lůžek](resources/images/rehab_bed_density_dataset-en.png){ width=50 % }

| Hustota lůžek | `giKizLegiUW` |
| --- | --- |
| Typ formuláře datové sady | **výchozí** |
| Období sběru dat | **roční** |
| Typy zařízení | **Rehabilitační zařízení s vyhrazeným rehabilitačním lůžkovým oddělením** |

Datový soubor hustoty lůžek je samostatný soubor dat, který obsahuje 2 části:

-   Hustota lůžek
    -   K dispozici rehabilitační lůžka (celkem)
-   Údaje o incidenci
    -   Amputace
    -   popáleniny
    -   MMT
    -   SCI
    -   Mrtvice
    -   TBI

> **Poznámka**
>
> 1. Pokud jsou data o hustotě rehabilitačního lůžka již sbírána ve stávajícím systému DHIS2 HMIS, je možné nahradit navrhovaný datový prvek a jeho reference stávajícím prvkem v systému. Informace o dodatečné konfiguraci indikátorů hustoty lůžka naleznete v [Průvodci instalací rehabilitačního balíčku](#rehab-installation).
> 2. Seznam zdravotních stavů lze upravit podle národních směrnic.

#### Dostupnost základního balíčku na PHC { #essential-package-availability-at-phc }

![Dostupnost základního balíčku](resources/images/rehab_pkg_availability_dataset-en.png){ width=30 % }

| Dostupnost základního balíčku | `MGzqZDWvPhL` |
| --- | --- |
| Typ formuláře datové sady | **sekce** |
| Období sběru dat | **roční** |
| Typy zařízení | **Primární zdravotnická zařízení podávající zprávy o rehabilitaci (Rehab PHC)** |

Datový soubor o dostupnosti základních balíčků shromažďuje údaje o dostupnosti základních rehabilitačních balíčků v primárních zdravotnických zařízeních:

-   Základní balíček WHO
-   Balíček vybraný z národních pokynů

#### Hustota personálu { #personnel-density }

![Rehabilitační skupiny povolání](resources/images/rehab_personnel_dataset-en.png)

| Personální obsazenost | `Sm2fALTZROS` |
| --- | --- |
| Typ formuláře datové sady | **sekce** |
| Období sběru dat | **roční** |
| Typy zařízení | **Všechna zařízení hlásí Rehab (hlavní seznam zařízení)** |

Rehabilitační pracovní skupiny obvykle zahrnují rehabilitační lékaře, rehabilitační sestry, fyzioterapeuty, ergoterapeuty, logopedy, protetiky a ortotiky a psychology. Mohou být zahrnuty i další rehabilitační profesní skupiny relevantní pro danou zemi, například audiologové, sociální pracovníci a střední rehabilitační profesní skupiny. Je také možné zahrnout nemocniční rehabilitační personál, který nepracuje na rehabilitačním oddělení. Národní plán pracovních sil ve zdravotnictví obvykle obsahuje seznam profesních skupin pro danou zemi a doporučuje se nahlédnout do tohoto seznamu při vytváření systému hlášení v zemi.

Tento soubor dat shromažďuje počty následujících rehabilitačních skupin v zařízeních:

1. Rehabilitační lékaři
2. Fyzioterapeuti
3. Ergoterapeuti
4. Logopedi
5. protetici / ortotici
6. psychologové
7. Ostatní personál

Pokud jsou tato čísla již shromážděna ve stávajícím systému DHIS2 HMIS, je možné nahradit navrhovaný datový prvek a všechny jeho výskyty stávajícím prvkem v systému. Informace o dodatečné konfiguraci datových prvků a indikátorů rehabilitačních skupin povolání naleznete v [instalační příručce](#rehab-installation).

![Populace](resources/images/rehab_population_est_dataset-en.png){ width=50% }

Úroveň organizační jednotky pro sběr populačních dat se může případ od případu použití lišit. Další informace o konfiguraci shromažďování údajů o obyvatelstvu a zaměstnancích naleznete v [instalační příručce](#rehab-installation).

#### Zpráva o hospitalizaci { #inpatient-report }

| Zpráva o hospitalizaci | `WjN1YoDtlOd` |
| --- | --- |
| Typ formuláře datové sady | **custom** |
| Období sběru dat | **monthly** |
| Typy zařízení | **Všechna zařízení s lůžkovým oddělením (ne vyhrazeným rehabilitačním oddělením), které podává rehabilitaci (seznam hlavních zařízení)** |

Tato datová sada používá vlastní html formulář pro zadávání dat, který obsahuje čtyři tabulky:

**Rehabilitační případy** – Celkový počet hospitalizovaných pacientů, kteří dostávají rehabilitační služby na lůžkových odděleních, která nejsou vyhrazenými rehabilitačními odděleními, a rozdělení těchto případů podle věku, pohlaví a skupin zdravotního stavu (HCG), které zahrnují muskuloskeletální, neurologické, mentální, senzorické, kardiovaskulární, rakovinové a respirační HCG.

![Rehabilitační případy](resources/images/rehab_cases_dataset-en.png){ width=70 % }

**Rehabilitační příjem** – Celkový počet sezení poskytnutých hospitalizovaným pacientům na nerehabilitačních odděleních a rozdělení podle HCG

![Rehabilitace](resources/images/rehab_uptake_dataset-en.png){ width=30 % }

**Využití v rehabilitačních zařízeních** – Počet sezení poskytovaných různými rehabilitačními profesními skupinami (rehabilitační lékaři, fyzioterapeuti, ergoterapeuti, logopedi, protetici/ortotici, psychologové, další pracovníci)

![Využití v rehabilitačním zařízení](resources/images/rehab_facility_uptake_dataset-en.png){ width=50 % }

**Asistenční produkty (AP)** – Počet asistenčních produktů poskytovaných pacientům rozdělených podle věku (0-4, 5-17, 18+) a skupin AP (mobilita, zrak, sluch, kognice, komunikace, sebepéče) a čekací dny na poskytnutí asistenčních produktů

![Asistenční produkty (AP)](resources/images/rehab_ap_dataset-en.png){ width=70% }

#### Zpráva  o rehabilitačním oddělení { #rehab-ward-report }

| Zpráva o rehabilitačním oddělení | `tP8et8TNWgF` |
| --- | --- |
| Typ formuláře datové sady | **custom** |
| Období sběru dat | **monthly** |
| Typy zařízení | **Všechna zařízení s vyhrazeným rehabilitačním lůžkovým oddělením vykazujícím rehabilitaci (seznam hlavních zařízení)** |

Tato datová sada používá vlastní html formulář pro zadávání dat, který obsahuje šest tabulek:

**Rehabilitační případy** – Celkový počet hospitalizovaných pacientů využívajících rehabilitační služby na rehabilitačním oddělení a rozdělení těchto případů podle věku, pohlaví a skupin zdravotního stavu (HCG), které zahrnují muskuloskeletální, neurologické, mentální, senzorické, kardiovaskulární, rakovinné a respirační HCG .

![Rehabilitační případy](resources/images/rehab_cases_dataset-en.png){ width=70 % }

**Rehabilitační využití** – Celkový počet sezení poskytnutých hospitalizovaným pacientům a rozdělení podle HCG

![Rehabilitace](resources/images/rehab_uptake_dataset-en.png){ width=30 % }

**Využití v rehabilitačních zařízeních** – Počet sezení poskytovaných různými rehabilitačními profesními skupinami (rehabilitační lékaři, fyzioterapeuti, ergoterapeuti, logopedi, protetici/ortotici, psychologové, další pracovníci)

![Využití v rehabilitačním zařízení](resources/images/rehab_facility_uptake_dataset-en.png){ width=50 % }

**Rehabilitační doporučení** – Celkový počet nových případů přistupujících do zařízení během vykazovaného měsíce a počet doporučení rozdělených podle poskytování asistenčních produktů a dalších rehabilitačních služeb.

![Rehabilitační doporučení](resources/images/rehab_referral_dataset-en.png){ width=30 % }

**Asistenční produkty (AP)** Počet poskytovaných asistenčních produktů rozdělených podle věku (0-4, 5-17, 18+) a skupin AP (mobilita, zrak, sluch, kognice, komunikace, samostatná péče) a čekacích dnů pro poskytování asistenčních produktů

![Asistenční produkty (AP)](resources/images/rehab_ap_dataset-en.png){ width=70% }

**Rehabilitační pobyt** Celkový počet nových případů během vykazovaného měsíce, rozdělený podle zdravotních stavů (HC), které zahrnují SCI, TBI, popáleniny, velká mnohočetná traumata, amputace a mrtvice; počet nových případů s komplexním plánem individualizované péče; délka pobytu u propuštěných případů, počet propuštěných případů, průměrné funkční skóre pro propuštěné případy při přijetí a propuštění v členění podle HC.

![Rehabilitační pobyt](resources/images/rehab_stay_dataset-en.png){ width=70% }

#### Ambulantní zpráva { #outpatient-report }

| Ambulantní zpráva | `zInFVXb98JD` |
| --- | --- |
| Typ formuláře datové sady | **custom** |
| Období sběru dat | **monthly** |
| Typy zařízení | **Všechna zařízení s ambulantním oddělením hlásícím se k Rehab (Seznam hlavních zařízení)** |

Tato datová sada používá vlastní html formulář pro zadávání dat, který obsahuje šest tabulek:

**Rehabilitační případy** – Celkový počet ambulantních pacientů využívajících rehabilitační služby v zařízení a rozdělení těchto případů podle věku, pohlaví a skupin zdravotního stavu (HCG), které zahrnují muskuloskeletální, neurologické, mentální, senzorické, kardiovaskulární, rakovinné a respirační HCG .

![Rehabilitační případy](resources/images/rehab_cases_dataset-en.png){ width=70 % }

**Rehabilitace** – Celkový počet sezení poskytnutých ambulantním pacientům a rozdělení podle HCG

![Rehabilitace](resources/images/rehab_uptake_dataset-en.png){ width=30 % }

**Rehabilitační doporučení** – Celkový počet nových případů přistupujících do zařízení během vykazovaného měsíce a počet doporučení rozdělených podle poskytování asistenčních produktů a dalších rehabilitačních služeb.

![Rehabilitační doporučení](resources/images/rehab_referral_otpt_dataset-en.png){ width=30 % }

**Využití v rehabilitačních zařízeních** - Počet sezení poskytovaných různými rehabilitačními profesními skupinami (rehabilitační lékaři, fyzioterapeuti, ergoterapeuti, logopedi, protetici/ortotici, psychologové, další personál), počet nových případů (první návštěvy) rozdělené podle rehabilitačních profesních skupin a celkový počet dnů čekání na první sezení

![Využití založené na rehabilitačním zařízení](resources/images/rehab_facility_uptake_otpt_dataset-en.png){ width=70 % }

**Asistenční produkty (AP)** – Počet asistenčních produktů poskytovaných pacientům rozdělených podle věku (0-4, 5-17, 18+) a skupin AP (mobilita, zrak, sluch, kognice, komunikace, sebepéče) a čekací dny na poskytnutí asistenčních produktů

![Asistenční produkty (AP)](resources/images/rehab_ap_dataset-en.png){ width=70% }

**Využití terénního programu** – Počet terénních sezení poskytovaných klientům rozděleným podle věku (0-4, 5-17, 18+) a pohlaví

![Využití terénního programu](resources/images/rehab_outreach_uptake_dataset-en.png){ width=50 % }

### Skupiny organizačních jednotek { #organisation-unit-groups }

Balíček Rehabilitace pracuje se sadou předdefinovaných skupin organizačních jednotek. Účelem těchto skupin je:

-   pomozte implementátorům nakonfigurovat balíček po jeho importu do nové nebo existující instance DHIS2
-   přiřaďte rehabilitační datové sady příslušným skupinám organizačních jednotek
-   využít předkonfigurované ovládací panely pro účely analýzy.

Předdefinované skupiny organizačních jednotek jsou uvedeny v tabulce níže:

| Název | UID | Popis | Účel |
| --- | --- | --- | --- |
| PHC | `aT5pkgRLbw5` | Primární zdravotnická zařízení | přiřazení datové sady, analytika |
| REHAB - Hlavní seznam zařízení | `Uvefj6bDfzo` | Zahrnuje všechna zařízení podávající zprávy o rehabilitaci | přiřazení datové sady, analytika |
| REHAB - PHC | `bbsxlCu3Vya` | Zahrnuje všechna primární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| REHAB - SHC | `wZJCB2cj9jg` | Zahrnuje všechna sekundární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| REHAB - THC | `Re0iJ3vtBzE` | Zahrnuje všechna terciární zdravotnická zařízení podávající zprávy o rehabilitaci | Analytika |
| Rehabilitační lůžkové oddělení | `AGK6oOK4ncb` | Zahrnuje všechna zařízení s vyhrazeným rehabilitačním oddělením | Analytika |

Další informace o konfiguraci skupin organizačních jednotek naleznete v [Průvodce instalací rehabilitačního balíčku](#rehab-orgunitgroups)

### Indikátory { #indicators }

Konfigurace indikátorů obsažených v balíčku Rehabilitation je podrobněji popsána v [Průvodce instalací balíčku Rehabilitation](#rehab-indicators)

### Pravidla ověřování { #validation-rules }

Aby byla zachována kvalita dat během sběru dat, balíček obsahuje sadu pravidel validace pro ambulantní, hospitalizované a rehabilitační oddělení.

Konfigurace těchto ověřovacích pravidel je podrobněji popsána v [průvodci instalací rehabilitačního balíčku](#rehab-validation-rules)

### Predikce { #predictors }

Rehabilitační balíček obsahuje sadu prediktorů, které se používají k vytváření datových hodnot pro rehabilitační pracovní skupiny a indikátory dostupnosti rehabilitačního balíčku:

| Název | UID | Typ období |
| --- | --- | --- |
| REHAB - Dostupnost (základní balíček) | `zYbrCP7xGtk` | roční |
| REHAB - Dostupnost (ergoterapeuti) | `MaWSMzXDLkm` | roční |
| REHAB - Dostupnost (jiný personál) | `aphqcwJiK5s` | roční |
| REHAB - Dostupnost (fyzioterapeuti) | `ydlTJLDcFBj` | roční |
| REHAB - Dostupnost (protetik/ortotik) | `K3QZ2zs0opc` | roční |
| REHAB - Dostupnost (psychologové) | `RpxclhlYJxw` | roční |
| REHAB - Dostupnost (rehabilitační lékaři) | `CbnJeF5K1cM` | roční |
| REHAB - Dostupnost (logopedi) | `qHJTzQcMSd4` | roční |

### Ovládací panely { #dashboards }

Modul Rehabilitace obsahuje 7 ovládacích panelů popsaných níže.

#### REHAB.01 - Vstupní / Rehabilitační vstupní data { #rehab01-input-rehabilitation-input-data }

Účel: Dva ukazatele hustota rehabilitačních lůžek a hustota personálu jsou vybrány tak, aby reprezentovaly tuto kategorii, protože poskytují základní informace o dostupnosti základních zdrojů potřebných pro poskytování základních rehabilitačních služeb. Nepřímo hodnotí kvalitu systému poskytování rehabilitačních služeb prostřednictvím souboru dovedností lidských zdrojů dostupných v zařízeních. Kromě programových manažerů zařízení jsou tyto informace součástí informací o zdravotnickém systému, které manažeři zdravotnického systému potřebují pro účely monitorování, plánování a koordinace: potřebují vědět, zda jsou rehabilitační lůžka a zdravotničtí pracovníci správně rozmístěni po zdravotnických zařízeních a napříč programy, aby byly splněny potřeby cílové populace.

01.01 - Lůžková a celková hustota personálu, (pod)národní, v loňském roce

![Lůžková a celková hustota personálu](resources/images/rehab-0101-en.png)

01.02 - Hustota zaměstnanců pro různé skupiny povolání (sub)národní, minulý rok

![Personální hustota pro různé rehabilitační profese](resources/images/rehab-0102-en.png)

01.03 - Časový trend hustoty lůžek, (sub)národní, posledních 5 let

![Časová osa hustoty lůžka](resources/images/rehab-0103-en.png)

01.04 - Časová osa hustoty personálu na skupinu povolání, (sub)národní, za posledních 5 let

![Časová osa hustoty personálu na skupinu povolání](resources/images/rehab-0104-en.png)

01.05 - Mapa zařízení a počtu rehabilitačních pracovníků, minulý rok

![Mapa zařízení a počet rehabilitačního personálu](resources/images/rehab-0105-en.png)

01.06 - Počet rehabilitačních pracovníků na skupinu povolání, podle správních úrovní, národní, v loňském roce

![Počet rehabilitačního personálu na skupinu povolání](resources/images/rehab-0106-en.png)

01.07.01 – Zařízení (%) vykazující rehabilitaci (MFL) podle profesní skupiny, úroveň primární péče, národní, posledních 5 let

![Zařízení PHC (%) reporting on rehab (MFL) per occupational group](resources/images/rehab-010701-en.png)

01.07.02 – Zařízení (%) vykazující rehabilitaci (MFL) podle profesní skupiny, úroveň SHC, národní, posledních 5 let

![Zařízení SHC (%) reporting on rehab (MFL) per occupational group](resources/images/rehab-010702-en.png)

01.07.03 – Zařízení (%) vykazující rehabilitaci (MFL) podle profesní skupiny, úroveň THC, národní, posledních 5 let

![Zařízení THC (%) reporting on rehab (MFL) per occupational group](resources/images/rehab-010703-en.png)

#### REHAB.02 - Dostupnost služby specifické pro výstup / rehabilitaci { #rehab02-output-rehabilitation-specific-service-availability }

Účel: WHO doporučuje dostupnost základního balíčku (EP) pro rehabilitaci na úrovni primární zdravotní péče (PHC) pro dosažení univerzálního zdravotního pokrytí (UHC). Tento ukazatel měří procento zařízení primární péče, která nabízí 1 nebo více základních doporučených balíčků (s jedním minimálním požadavkem) a poskytuje informace o stavu implementace tohoto doporučení v zemích. Ukazatel zobrazí seznam všech zařízení nabízejících alespoň 1 z vybraných balíčků, přičemž země mohou dále rozlišovat podle typů základních balíčků.

02.01 – Geografické rozložení zařízení primární péče (%) nabízejících EP, (sub)národní, minulý rok

![Geografické rozložení zařízení primární péče (%) offering an EP](resources/images/rehab-0201-en.png)

02.02 – Časová osa zařízení primární péče (%) nabízejících EP, (sub)národní, posledních 5 let

![Časová osa zařízení PHC (%) offering an EP](resources/images/rehab-0202-en.png)

02.03 - Mapa zařízení primární zdravotní péče nabízející údaje o využití EP a okresních ambulancí za loňský rok

![Zařízení PHC nabízející údaje o využití EP a okresních ambulantních pacientů, minulý rok](resources/images/rehab-0203-en.png)

02.04 - Počet nových ambulantních pacientů nastupujících do primární zdravotní péče a okresních nemocnic podle okresů za posledních 5 let

![Počet nových ambulantních pacientů přistupujících do primárních zdravotních a okresních nemocnic](resources/images/rehab-0204-en.png)

02.05 – Procento zařízení primární péče nabízející EP, podle typu EP, (sub)národní, v loňském roce

![% PHC zařízení nabízejících EP, podle typu EP](resources/images/rehab-0205-en.png)

#### REHAB.03 - Využití výstupu / rehabilitační služby { #rehab03-output-rehabilitation-service-utilization }

Účel: Využití rehabilitační služby je orientační pro dostupnost rehabilitace. Tato část sady indikátorů měří počet rehabilitačních sezení a nových klientů podle předem nastavené skupiny zdravotního stavu, počet vydaných asistenčních produktů a počet rehabilitačních sezení poskytnutých prostřednictvím terénních programů.

03.01 – Rehabilitace v zařízení: interní a ambulantní, (sub)národní, poslední čtvrtletí (uživatel orgsnizační jednotky)

![Rehabilitační sezení, interní a ambulantní pacienti](resources/images/rehab-0301-en.png)

03.01.01 - Mapa čerpání ústavní rehabilitace za loňský rok (organizační jednotka uživatele)

![Využívání ústavní rehabilitace](resources/images/rehab-030101-en.png)

03.01.02 - Mapa čerpání ambulantní rehabilitace v zařízení za loňský rok (organizační jednotka uživatele)

![Ambulantní rehabilitace v zařízení](resources/images/rehab-030102-en.png)

03.02 - Příjem rehabilitace a využití služeb, celkem, (sub)národní, poslední čtvrtletí (organizační jednotka uživatele)

![Rehabilitace a využití služeb, celkem](resources/images/rehab-0302-en.png)

03.03.01 - Příjem a využití rehabilitačních služeb pro vybranou skupinu zdravotních stavů, (sub)národní, poslední čtvrtletí

![Rehabilitace a využití služeb – muskuloskeletální HCG](resources/images/rehab-030301-en.png)

03.04 - Příjem a využití rehabilitačních služeb podle skupiny zdravotních stavů za poslední čtvrtletí (organizační jednotka uživatele)

![Rehabilitace a využití služeb, podle skupiny zdravotních stavů](resources/images/rehab-0304-en.png)

03.05.01 - Využití rehabilitace pro konkrétní skupinu zdravotního stavu podle geografického regionu, podle věkové skupiny, poslední čtvrtletí (organizační jednotka uživatele)

![Využití rehabilitace, muskuloskeletální HCG](resources/images/rehab-030501-en.png)

03.06 - Využití rehabilitace na skupinu zdravotních stavů, (sub)národní, poslední čtvrtletí (organizační jednotka uživatele)

![Využití rehabilitace na skupinu zdravotních stavů](resources/images/rehab-0306-en.png)

03.07 - Využití rehabilitace podle skupiny zdravotních stavů, celostátní, minulý rok (organizační jednotka uživatele)

![Využití rehabilitace na skupinu zdravotních stavů](resources/images/rehab-0307-en.png)

03.08 - Mapa využití služeb a hustoty personálu podle okresů, (pod)státní, v loňském roce

![Využití služeb a personální hustota](resources/images/rehab-0308-en.png)

03.09 - Příjem AP u hospitalizovaných a ambulantních pacientů podle kategorie APL, (sub)národní, poslední čtvrtletí (jednotka uživatelské organizace)

![Využití AP pro interní a ambulantní pacienty podle kategorie APL](resources/images/rehab-0309-en.png)

03.10 – Využívání terénních programů podle věkových skupin, (sub)národní, poslední čtvrtletí (organizační jednotka uživate)

![Využívání terénních programů v jednotlivých věkových skupinách](resources/images/rehab-0310-en.png)

03.11 – Časová osa čerpání v zařízeních podle skupin zdravotních stavů, vnitrostátní, posledních 5 let (Organizační jednotka uživatele)

![Časová osa čerpání v zařízeních podle skupin zdravotního stavu](resources/images/rehab-0311-en.png)

03.12 - Využití rehabilitace a dostupnost personálu v posledním roce (orgaizační jednotka uživatele)

![Využití rehabilitace a dostupnost personálu](resources/images/rehab-0312-en.png)

#### REHAB.04 - Výstup / Kvalita rehabilitačních služeb { #rehab04-output-rehabilitation-service-quality }

Účel: Měření kvality a výsledky služeb pro specializovanou lůžkové rehabilitaci jsou zvláště zajímavé pro manažery. Individuální plán péče přispívá k lepším výsledkům rehabilitace u klientů a délka rehabilitačního pobytu informuje o hodnocení účinnosti a efektivity. Hodnocení funkční změny během rehabilitační epizody poskytuje míru výsledku rehabilitační epizody. Zlepšení fungování odráží zvýšenou schopnost samostatného života a společenské participace, což je celkovým cílem rehabilitace.

04.01 - Časová osa pacientů (%) s individuálním plánem péče, podle nemocnice s vyhrazeným oddělením, posledních 6 měsíců (organizační jednotka uživatele)

![Časová osa pacientů (%) with individualised care plan](resources/images/rehab-0401-en.png)

04.02.01 - Časová osa LoS pro konkrétní zdravotní stav, podle nemocnice s vyhrazeným oddělením, posledních 5 let (organizační jednotka uživatele)

![Časová osa LoS pro SCI](resources/images/rehab-040201-en.png)

04.03 - Funkční změna a LoS podle zdravotního stavu, posledních 6 měsíců (organizační jednotka uživatele)

![Funkční změna a ztráta podle zdravotního stavu](resources/images/rehab-0403-en.png)

04.04.01 - Funkční změna a LoS pro konkrétní zdravotní stav, podle nemocnice s vyhrazeným oddělením, posledních 6 měsíců (organizační jednotka uživatele)

![Funkční změna a LoS pro SCI, v nemocnici s vyhrazeným oddělením](resources/images/rehab-040401-en.png)

04.05.01 - Časová osa funkční změny a LoS pro konkrétní zdravotní stav, posledních 5 let (organizační jednotka uživatele)

![Časová osa funkční změny a LoS pro SCI](resources/images/rehab-040501-en.png)

#### REHAB.05 – Výsledek / pokrytí služeb { #rehab05-outcome-service-coverage }

Účel: Pokrytí se měří prostřednictvím procenta lidí s akutními a komplexními potřebami rehabilitace, kteří mají přístup k adekvátně poskytovaným kvalitním rehabilitačním službám. Správná klinická praxe předepisuje lůžkovou multidisciplinární rehabilitaci na vyhrazeném rehabilitačním oddělení pro účinnou rehabilitaci skupiny zdravotních stavů s komplexními rehabilitačními potřebami. Výběr zdravotního stavu, který má být měřen, musí vycházet z národních priorit a dostupnosti jmenovatele. Ve většině zemí bude nutné určit zdroj dat pro jmenovatele (odhadovaný počet lidí v zemi s definovaným zdravotním stavem). Může to být národní odhad z průzkumu založeného na populaci nebo kódování ICD. Země mohou také využít spádovou populaci a použít odhady prevalence pro region pro výpočet jmenovatele. Z důvodu dostupnosti jmenovatele bude pokrytí zachyceno pouze na (sub)národní úrovni. V případě nedostupnosti jmenovatele může analytik ještě využít indikátoru „Využití lidí s akutními a komplexními potřebami“.

05.01 - Pokrytí, podle zdravotního stavu, národní, minulý rok

![Pokrytí, dle zdravotního stavu](resources/images/rehab-0501-en.png)

05.02.01 - Mapa specializovaných zařízení + dostupnost pro osoby s akutní a komplexní potřebou konkrétního zdravotního stavu + údaje o hustotě lůžek, loňský rok

![Specializované zařízení + využití (SCI) + bed density](resources/images/rehab-050201-en.png)

05.03 - Dostupnost pro osoby s akutními a komplexními potřebami, podle zdravotního stavu, (sub)národní, posledních 6 měsíců (organizační jednotka uživatele)

![Dostupnost pro osoby s akutními a komplexními potřebami, dle zdravotního stavu](resources/images/rehab-0503-en.png)

05.04 - Časová osa pokrytí, podle zdravotního stavu, (sub)národní, posledních 5 let

![Časová osa pokrytí, podle zdravotního stavu](resources/images/rehab-0504-en.png)

05.05 - Časová osa dostupnosti pro osoby s akutními a komplexními potřebami, podle zdravotního stavu, (sub)národní, posledních 5 let (organizační jednotka uživatele)

![Časová osa dostupnosti pro lidi s akutními a komplexními potřebami, podle zdravotního stavu](resources/images/rehab-0505-en.png)

#### REHAB.06 - Výsledek / změna fungování { #rehab06-outcome-functioning-change }

06.01 - Funkční změna podle zdravotního stavu, podle nemocnice s vyhrazeným oddělením, posledních 6 měsíců (organizační jednotka uživatele)

![Funkční změna podle zdravotního stavu, podle nemocnice s vyhrazeným oddělením](resources/images/rehab-0601-en.png)

06.02.01 - Časová osa funční změny pro konkrétní zdravotní stav, podle nemocnice s vyhrazeným oddělením, posledních 5 let (organizační jednotka uživatele)

![Funkční změna časové osy pro SCI, podle nemocnice s vyhrazeným oddělením](resources/images/rehab-060201-en.png)

06.03.01 - Časová osa funkční změny (včetně před a po skóre) pro konkrétní zdravotní stav ve vybrané nemocnici s vyhrazeným oddělením, posledních 5 let (organizační jednotka uživatele)

![Časová osa funkční změny (including pre and post scores) for SCI at selected hospital with dedicated ward](resources/images/rehab-060301-en.png)

#### REHAB.07 - Kontinuum péče { #rehab07-continuum-of-care }

Účel: Tato část poskytuje informace o výkonnosti sektoru rehabilitace. Rehabilitace je běžně součástí kontinua péče a silné kontinuum vede k lepším zdravotním výsledkům. Jak rehabilitační doporučení, tak čekací doba svědčí pro efektivní využití kontinua péče. Dobře fungující procesy doporučení probíhají v obou směrech napříč úrovněmi zdravotní péče a doporučení musí být dokumentována u každého případu, aby se prokázalo efektivní využití mechanismů procesu doporučení. Včasné poskytnutí rehabilitace přispívá k její účinnosti a celkové kvalitě péče.

07.01 - Časová osa čekací doby na poskytování AP (ambulantní pacienti) podle kategorie APL, pro vybraný subnárodní region, posledních 5 let (organizační jednotka uživatele)

![Časová osa čekací doby na poskytnutí AP (outpatients) per APL category, for selected subnational region](resources/images/rehab-0701-en.png)

07.02 - Časová osa doporučení na rehabilitaci a čekací doby na rehabilitaci podle typu profese, pro vybranou správní úroveň, (sub)národní, posledních 5 let (organizační jednotka uživatele)

![Časová osa doporučení na rehabilitaci a čekací doby na rehabilitaci podle typu povolání, pro THC](resources/images/rehab-0702-en.png)

07.03 - Čekací doba na rehabilitaci podle skupiny povolání, podle správní úrovně, pro vybraný krajský region, posledních 6 měsíců (organizační jednotka uživatele)

![Čekací doba na rehabilitaci na skupinu povolání, podle administrativní úrovně](resources/images/rehab-0703-en.png)

07.04 - Počet doporučení a ambulantních pacientů podle správní úrovně, podle geografického regionu, poslední čtvrtletí (organizační jednotka uživatele)

![Počet doporučení a ambulantních pacientů podle administrativní úrovně, podle geografického regionu](resources/images/rehab-0704-en.png)

07.05 – Součty a podíly doporučení na administrativní úroveň za posledních 6 měsíců (organizační jednotka uživatele)

![Součty a podíly doporučení na administrativní úroveň](resources/images/rehab-0705-en.png)

07.06 - Doporučení na rehabilitaci (%) pro administrativní úrovně, podle subnárodních regionů, za posledních 6 měsíců

![Rehab doporučení (%) for administrative levels, by subnational region](resources/images/rehab-0705-en.png)

> **Poznámka**
>
> 1. Všechny vizualizace, které jsou označeny (uživatelská organizační jednotka), mohou být zkompilovány do dalšího dashboardu pro analýzu na úrovni zařízení.
> 2. Vizualizace 03.03.01, 03.05.01, 04.02.01, 04.04.01, 04.05.01, 05.02.01, 06.02.01 a 06.03.01 jsou nakonfigurovány pro konkrétní skupinu zdravotních stavů / zdravotní stav Nakonfigurujte vizualizace pro další skupiny zdravotních stavů / pomocné stavy na základě poskytnutých příkladů.
