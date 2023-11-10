---
edit_url: "https://github.com/dhis2-metadata/RMS0-Rapid_Mortality_Surveillance/blob/master/docs/rms_event_design.md"
revision_date: "2021-12-03"
---

# RMS – Návrh systému rychlého sledování úmrtnosti { #rms-event-design }

## Úvod { #introduction }

Zatímco počet úmrtí na COVID-19 je klíčovým ukazatelem pro měření dopadu pandemie na celém světě, není snadné tuto metriku shromáždit ve všech kontextech. Rychlé sledování úmrtnosti (RMS) je systém pro generování denních nebo týdenních počtů úmrtí podle věku, pohlaví, data úmrtí, místa úmrtí a místa obvyklého bydliště (WHO, 2020). V kombinaci s předpandemickými údaji o úmrtnosti umožňuje RMS zemím vypočítat nadměrnou úmrtnost během epidemie, definovanou jako stupeň, ve kterém aktuálně naměřená úmrtnost překračuje historicky stanovené úrovně.

Účelem tohoto balíčku je poskytnout praktické pokyny a základní sadu metadat pro implementaci rychlého sledování úmrtnosti v národních zdravotnických informačních systémech založených na DHIS2. Tento balíček je v souladu s [technickým balíčkem WHO pro rychlý dohled nad úmrtností a reakci na epidemie](https://www.who.int/publications/i/item/revealing-the-toll-of-covid-19) (2020) pro vyhodnocení mýta COVID-19 v zemích. Je navržen tak, aby byl flexibilní a proveditelný pro použití v prostředí s nízkými zdroji, včetně kontextů, kde sběr dat z velké části zůstává papírový.

Hlášení celkové úmrtnosti ze zařízení, komunit a midlegalského personálu (podle kontextu země) se základními údaji, jako je věk, pohlaví, datum úmrtí, místo úmrtí a bydliště, umožňuje úplnější obrázek o dopadu, zejména u úmrtí, která se mohou vyskytovat v domácnosti/komunitě nebo mohou být nepřímo spojeny s COVID-19. Navíc analýzy meziročních trendů před a po epidemii mohou odhalit nepřímý dopad související s narušením přístupu ke zdravotnickým službám a produktům.

## Přehled návrhu systému { #system-design-overview }

### Shrnutí případu použití { #use-case-summary }

Podle technického balíčku WHO RMS vyžaduje 1) zdroj rychle a běžně hlášených úmrtí podle věku, pohlaví a místa; a 2) některé prostředky pro stanovení základní úrovně předepidemické úmrtnosti podle věku a pohlaví, se kterou lze porovnat aktuální zprávy. Balíček metadat odpovídá těmto komponentám s programem událostí pro řádkový sběr dat o úmrtích optimalizovaných pro hlášení zařízení a komunity; a referenční panel, který umožňuje meziroční analýzu trendů prozkoumat nadměrnou úmrtnost ve srovnání s úrovněmi před pandemií.

Na rozdíl od systémů sledování úmrtnosti na základě příčin a systémů certifikace úmrtí je záměrem RMS zachytit _celkovou_ úmrtnost pro účely monitorování dopadu epidemie. Data jsou určena ke sběru jak v zařízení, tak v komunitě, aby byla zachycena všechna úmrtí. Tento přístup může překonat známé nedostatky při dosahování úplnosti a pokrytí systémů úmrtnosti na základě příčiny v mnoha zemích, jako je slabé propojení mezi hlášením úmrtí zdravotnických zařízení a národními systémy CRVS a také vysoký podíl úmrtí, ke kterým dochází v komunitě a které mohou zůstat nehlášené. .

Pro sledování úmrtnosti na základě příčiny se prosím podívejte na [balíček metadat DHIS2 Cause of Death] (#cod-design) navržený tak, aby podporoval lékařské osvědčení o příčině smrti doporučené WHO a normy Mezinárodní klasifikace nemocí (ICD).

### Určení uživatelé { #intended-users }

Balíček je navržen s ohledem na následující koncové uživatele:

1. Zaměstnanci zdravotnického zařízení odpovědní za hlášení úmrtí
2. Komunitní zdravotní pracovníci, dobrovolníci, náboženští nebo komunitní vůdci, kteří slouží jako komunitní reportéři

3. Lékařský personál (tj. koroneři, soudní lékaři) v zemích, kde je vysoký podíl úmrtí zachycován těmito pracovníky
4. Týmy pro reakci na epidemii, národní pracovní skupiny COVID-19 a tvůrci politik odpovědní za analýzu dat a řízení opatření v reakci na epidemii

### Datový tok { #data-flow }

Rychlý dohled nad úmrtností se snaží získat data z více zdrojů hlášení, aby získal úplný obraz o celkové úmrtnosti.

![rms_system_graphic_who_2020](resources/images/rms_system_graphic.png)

V ideálním případě se identifikace a hlášení úmrtí v rámci RMS používá také jako oznámení pro systém evidence obyvatel, kde je to možné. Mělo by být zváženo pečlivé zvážení stávajících protokolů hlášení úmrtí v komunitách a zařízeních, úplnost a pokrytí hlášení životně důležitých událostí a rozsah, v jakém mohou být systémy úmrtnosti a úmrtí na základě příčiny udržovány v adekvátní úplnosti a tempu během epidemie. při navrhování národních RMS.

Typický obchodní proces pro reporting založený na zařízení je následující:

![rms-community-reporting-who-2020](resources/images/rms_community_reporting.png)

## Konfigurace programu { #program-configuration }

Tento balíček používá datový model události v DHIS2 k zaznamenávání úmrtí. Model události byl vybrán, protože:

1. Je dostatečně flexibilní, aby mohl hlásit a analyzovat klíčové proměnné RMS věk, pohlaví, datum úmrtí, místo úmrtí a místo obvyklého pobytu;
2. Údaje jsou hlášeny pro dané úmrtí v jediném časovém okamžiku a nevyžadují dlouhodobé trasování;
3. V tomto programu nejsou zachyceny žádné přímo osobně identifikovatelné údaje.

## Skupiny uživatelů { #user-groups }

Balíček obsahuje tři základní skupiny uživatelů.

-   RMS – přístup (zobrazit data / zobrazit metadata)
-   RMS – správce (žádný přístup k datům / úpravám metadat)
-   RMS - sběr dat (zachycení dat / zobrazení metadat

Ve výchozím nastavení jsou těmto skupinám uživatelů přiřazena následující oprávnění:

| Objekt | Uživatelská skupina |  |  |
| --- | --- | --- | --- |
|  | _RMS - access_ | _RMS - admin_ | _RMS - data capture_ |
| _*Program*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze upravovat a prohlížet <br> Data: bez přístupu | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit |
| _*Fáze programu*_ | Metadata : lze zobrazit <br> Data: lze zobrazit | Metadata: lze zobrazit <br> Data: bez přístupu | Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit |
| _*Ovládací panely*_ | Metadata : lze zobrazit | Metadata : lze zobrazit | Metadata : lze zobrazit |

Uživatelé jsou přiřazeni do příslušné skupiny uživatelů na základě jejich role v systému. Sdílení pro další objekty v balíčku může být upraveno v závislosti na nastavení. Další informace naleznete v [dokumentaci DHIS2 o sdílení](#sharing).

## Analytika { #analytics }

Balíček obsahuje čtyři základní programové indikátory používané ve vizualizacích, mapách a tabulkách sestav:

| UID | Název | Popis |
| --- | --- | --- |
| `UMX5BHF0tJL` | RMS – úmrtí (počet) | Celkový počet úmrtí ve vykazovaném období |
| `WqcliBMvwaf` | RMS – Úmrtí – kumulativní (počet) | Kumulativní počet úmrtí |
| `mNiLSRgYdAB` | RMS – Úmrtí – žena (počet) | Počet úmrtí mezi ženami |
| `CFaSySxD8TD` | RMS – Úmrtí – muži (počet) | Počet úmrtí mezi muži |

Administrativní oblast bydliště (organizační jednotka) a místo úmrtí (souřadnice) zachycené v registru slouží k vizualizaci údajů o úmrtnosti na mapách.

## Ovládací panel { #dashboard }

Balíčky Rapid Mortality Surveillance obsahují řídicí panel obsahující následující položky řídicího panelu:

| UID | Název | Typ | Popis |
| --- | --- | --- | --- |
| `GLVdm5xK6lH` | RMS - Úmrtí podle místa, posledních 52 týdnů | Mapa | Údaje o úmrtnosti podle místa úmrtí (souřadnic), posledních 52 týdnů |
| `mNiLSRgYdAB` | RMS – Úmrtí podle regionů podle měsíců v tomto roce | Mapa | Údaje o úmrtnosti, regionální, měsíce letošního roku, podle vykazující organizační jednotky |
| `CFaSySxD8TD` | RMS - Úmrtí podle pohlaví | Sloupec | Počet zemřelých podle pohlaví za posledních 52 týdnů, organizační jednotka uživatele |
| `yIB5hqPsjf6` | RMS - Úmrtí podle roku | Rok po roce (řádek) | Počet úmrtí podle týdnů za rok, letos a posledních 5 let |
| `UMX5BHF0tJL` | RMS - Úmrtí podle věku, pohlaví | Zpráva o události | Počet zemřelých podle věkových skupin (0-4,5-14,15-44,45+) a pohlaví (muži, ženy, neznámé) |

![Úmrtí podle místa, posledních 52 týdnů](resources/images/rms-dsh-deaths_by_place.png)

![Počet úmrtí na region, podle měsíců v tomto roce](resources/images/rms-dsh-deaths_per_region.png)

![Úmrtí podle pohlaví](resources/images/rms-dsh-deaths_by_sex.png)

![Úmrtí podle roku](resources/images/rms-dsh-deaths_by_year.png)

![Smrt podle věku, pohlaví](resources/images/rms-dsh-deaths_by_age_sex.png)

## Aspekty implementace { #implementation-considerations }

Je možné implementovat Rapid Mortality Surveillance souběžně s balíčkem WHO pro příčiny smrti. Některé generické datové prvky jsou mezi těmito balíčky sdíleny. V mnoha kontextech není lékařské potvrzení o příčině smrti (MCCOD) včas vyplněno u všech úmrtí, ke kterým dojde, zejména těch úmrtí, která mohou nastat v komunitě. Rapid Mortality Surveillance umožňuje uživatelům rychle hlásit fakt smrti pomocí datového modelu události v DHIS2. Analýzy jsou programově odděleny (COD vs RMS), takže tato data lze analyzovat bez rizika dvojího započítání. V závislosti na kontextu země, pracovních postupech a úplnosti sledování příčin smrti lze také zvážit integrovanou analýzu, která kombinuje úmrtí hlášená prostřednictvím RMS jako „skutečnost úmrtí“ vs. úmrtí hlášená ze zařízení, kterým byla přiřazena základní příčina.
