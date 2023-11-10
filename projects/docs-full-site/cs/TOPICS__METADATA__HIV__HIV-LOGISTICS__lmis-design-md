---
edit_url: "https://github.com/dhis2-metadata/GEN_DOCS/blob/master/docs/lmis_general_aggregate_design.md"
revision_date: "2021-06-22"
---

# Logistika { #logistics }

## Úvod do logistických metadat { #introduction-to-logistics-metadata }

Mnoho zemí má zavedené systémy pro správu elektronických logistických informací (eLMIS), zatímco jiné se při správě logistických dat spoléhají na papírové metody a excelové listy. Tam, kde jsou eLMIS již implementovány, jsou často optimalizovány pro správu dat ve skladech a nerozšiřují se na úroveň zařízení pro rutinní reporting. V důsledku toho logistická data na úrovni poskytování zdravotních služeb často nejsou k dispozici pro triangulovanou analýzu se zdravotními službami a dalšími programovými daty. Mnoho zemí používá DHIS2 pro logistické hlášení na úrovni zařízení ke zvýšení viditelnosti údajů o zásobách a zdravotnických službách pro programové manažery, okresní zdravotnický personál a další klíčové uživatele dat. Vzhledem k tomu, že DHIS2 je široce používaným národním měřítkem pro podávání zpráv na úrovni zařízení a subnárodní analýzu, existuje příležitost posílit interoperabilitu s upstream logistickými datovými systémy a zlepšit sběr a využívání logistických dat poslední míle. Typické využití DHIS2 pro logistická data zahrnuje hlášení zásob zařízení (datové vstupy: měsíční nebo denní zprávy o zásobách) a výstupy (indikátory, grafy a řídicí panely k vizualizaci dostupnosti, distribuce a používání zásob).

DHIS2 nemá v úmyslu nahradit vhodné informační systémy pro správu logistiky pro daný účel. Zde zdokumentované balíčky metadat a principy návrhu jsou určeny k šíření terénních postupů a společných standardů metadat pro sběr logistických dat ve zdravotnických zařízeních a dalších místech poskytování služeb, na které se eLMIS nemusí vztahovat. Toto úsilí má za cíl:

1. Usnadnit analýzu zdravotnických služeb a skladových dat na řídicích panelech HMIS za účelem zlepšení programového rozhodování; a,
2. Vylepšit interoperabilitu mezi DHIS2 jako řešením pro sběr logistických dat koncových uživatelů a předřazeným LMIS.

## WHO Integrovaná analýza HMIS-LMIS { #who-hmis-lmis-integrated-analysis }

Aby se zlepšila analýza údajů o zdravotních službách společně s údaji o zásobách, byl v roce 2020 svolán Globální program WHO pro boj proti tuberkulóze, Globální program pro malárii a Globální program pro HIV, aby poskytl pokyny pro integrovanou analýzu klíčových údajů o zdravotních a zdravotních službách pro řídicí panely HMIS. Tato spolupráce vyústila ve vývoj společného logistického datového rámce aplikovaného napříč zdravotními programy pro agregované hlášení zařízení v DHIS2. K informování o návrhu společného rámce pro souhrnné vykazování všech položek zdravotních zásob byly použity koncepty z hlášení souhrnných údajů o zásobách zařízení v rámci balíčku WHO EPI, který je v zemích implementován od roku 2017.

Agregované balíčky metadat DHIS2 pro programy HIV, TBC, Malárie a EPI obsahují soubory dat pro rutinní vykazování zásob zařízení a řídicí panely, které umožňují triangulaci údajů o zásobách a zdravotnických službách. Tyto balíčky metadat poskytují referenční konfiguraci v DHIS2 na podporu přijetí logistických indikátorů doporučených WHO a jejich triangulace s HMIS pro analytické účely.

Klíčovými cíli WHO doporučených integrovaných balíků HMIS-LMIS pro agregované HMIS jsou:

1. Podporovat osvědčené postupy pro integrovanou analýzu a triangulaci mezi údaji o poskytování služeb a klíčovými logistickými údaji pro daný zdravotní program;
2. Stanovit pokyny/standardy pro klíčová skladová / logistická data, která mohou a) být hlášena ze zdravotnických zařízení do DHIS2 v nepřítomnosti alternativního LMIS, který dosáhne úrovně zařízení NEBO b) importovat / přijímat z funkčního elektronického logistického informačního systému.

K podpoře integrované analýzy v národních HMIS založených na DHIS2 zahrnují agregované balíčky metadat pro programy vertikálního zdraví:

1. Ovládací panely s vizualizacemi a grafy kombinujícími indikátory zdravotnických služeb (HMIS) a klíčové indikátory výkonnosti logistiky (LMIS)

2. Indikátory a prediktory pro generování vypočítaných hodnot jako součást společného rámce metadat logistiky a klíčových indikátorů monitorování výkonu pro logistiku jako součást celkového řízení programu

3. Datové sady a datové prvky pro hlášení logistických dat zařízení pro programy vertikálního zdraví, předkonfigurované pro sadu typických skladových položek monitorovaných pro každý program zdraví

## Společný rámec metadat logistiky { #common-logistics-metadata-framework }

### Základní logistická metadata { #core-logistics-metadata }

Logistická metadata DHIS2 zahrnutá v balíčcích metadat WHO pro základní HMIS (agregát) jsou navržena tak, aby byla koncepčně harmonizována napříč různými zdravotními programy. Toho bylo dosaženo dodržováním společného rámce logistických dat založeného na konsensu mezi zdravotními programy WHO a odbornými vstupy odborníků na logistiku.

Společný rámec metadat logistiky byl aplikován následovně, přičemž koncepty metadat DHIS2 jsou uvedeny v pravém sloupci. Pro každou položku zdravotního skladu jsou konfigurována stejná logistická metadata, která jsou relevantní pro každý zdravotní program (např. Malárie RDT, testovací soupravy na HIV, kazety GenXpert atd.).

| Logistické datové koncepce | Definice | Koncept konfigurace DHIS2 |
| --- | --- | --- |
| Počáteční zůstatek (vypočteno) | Počáteční zůstatek odráží skutečný počet použitelných položek zásob na začátku vykazovaného období. Počáteční zůstatek aktuálního období se rovná fyzickému počtu zásob na poslední období. Pokud nedojde k nesrovnalostem v vykazování údajů nebo skladových položkách, počáteční zůstatek by se rovnal také „konečnému zůstatku (vypočtenému) z předchozího období. | Datový prvek je naplněn prediktorem. Protože toto pole je automaticky vypočítáváno pomocí DHIS2, není možné jej uživatelem zadávání dat upravit. |
| Přijaté zásoby (zaznamenané) | Celkové množství zásob přijatých během vykazovaného období. Mohou být také označovány jako „skladové příjmy“. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |
| Vydané (evidované) zásoby | Množství zásob fyzicky distribuovaných z lékárny, které jsou buď přímo vydávány pacientům, nebo vydávány na oddělení, ambulantní oddělení nebo jiné služby v rámci poskytování služeb pacientům. Vydané zásoby se někdy označují jako „spotřeba“ nebo „použité“. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |
| Zásoba vyřazena (zaznamenána) | Množství zásoby, které bylo z jakéhokoli důvodu (například vypršení platnosti nebo poškození) vyřazeno (vyřazeno ze skladu). Tyto ztráty zásob jsou známy a zaznamenávány; mohou být považovány za "zaúčtované ztráty". Tyto ztráty zásob jsou někdy označovány jako „plýtvání“. Vyřazené zásoby se liší od chybějících / ztracených zásob, protože jsou zaznamenány počty těchto vyřazených položek. Pojem „vyřazené zásoby“ lze dále rozčlenit podle potřeby pro analýzu specifickou pro program. Například v balíčku EPI mohou být zásoby vyřazené pro určité vakcíny rozčleněny z důvodů, jako jsou zmrazené nebo rozbité. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |
| Zásoby přerozděleny (zaznamenány) | Množství zásob přerozdělených zpět do dodavatelského řetězce (například vrácených do okresních obchodů nebo darovaných jiným zdravotnickým zařízením) a již není určeno k použití pacienty vykazujícího zdravotnického zařízení. To se týká zásob, které opouštějí zařízení, ale nebyly vydány pacientům nebo použity během poskytování služby. Zásoby „přerozděleny“ proti proudu, například na úroveň okresu, se také někdy označují jako „výnosy“. Zásoby přerozdělené do jiných zdravotnických zařízení jsou někdy považovány za darované. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |
| Skladové zásoby k dispozici (zaznamenané) | Množství zásob fyzicky dostupných a zaúčtovaných v lékárně / obchodě / zařízení na konci vykazovaného období. Pokud byly všechny položky skladu řádně zaúčtovány, zaznamenaný datový prvek „Zásoby na skladě“ by se měl rovnat vypočtenému „konečnému zůstatku“. Mohou však existovat chyby v kvalitě dat nebo nezaznamenané ztráty zásob, které mohou vést k nesrovnalosti mezi skladem k dispozici a konečným zůstatkem. Vzhledem k těmto úvahám je datový prvek „Zásoby na skladě“ považován za přesnější a spolehlivější než vypočtený konečný zůstatek. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |
| Konečný zůstatek (vypočteno) | Konečný zůstatek se vypočítá automaticky na základě výše uvedených logistických údajů vykázaných zdravotnickým zařízením. Vzorec pro tento indikátor je (Počáteční zůstatek + přijatá zásoba - vydaná zásoba - vyřazená zásoba - přerozdělena zásoba). Vypočtený konečný zůstatek nezohledňuje (a nemůže zohlednit) ztráty zásob, ale umožňuje jejich výpočet. | Indikátor; vypočítáno v DHIS2 za běhu |
| Dny bez zásob (zaznamenané) | Počítá počet dní během vykazovaného období, ve kterém byla příslušná skladová položka kdykoli nebo pro jakékoli denní období na skladě. Počet dní do vyprodání zásob je jedním z ukazatelů výkonu logistiky. | Datový prvek; ručně zadané uživatelem zadávání dat do skladového formuláře. |

### Základní logistické ukazatele { #core-logistics-indicators }

Programy WHO proti HIV, TBC a malárii dále doporučily zahrnout do balíčků řídicího panelu HMIS společné programové ukazatele pro monitorování programového výkonu. Následující ukazatele byly nakonfigurovány a zahrnuty do souhrnných balíčků pro každou skladovou položku zahrnutou v balíčku metadat podle pokynů WHO:

| Název indikátoru | Popis indikátoru |
| :-: | :-: |
| Nesrovnalosti v zásobách (%) | Rozdíl mezi vypočítaným konečným zůstatkem a zaznamenanou zásobou. Nesrovnalosti v zásobách se automaticky vypočítají odečtením vypočítaného konečného zůstatku od zaznamenaných zásob na skladě. Nesrovnalosti mohou být způsobeny chybami při zadávání dat, chybným účtováním, krádeží nebo chybným zásobováním. Výsledná hodnota je většinou záporná (<0) → nesrovnalost v zásobách pak odpovídá ztrátám, které nejsou zaúčtovány a nelze je vysvětlit. Příležitostně může stavový nesoulad nabývat kladných hodnot ("nadměrné zásoby", >0). - např. pokud je zaznamenané množství vydaných zásob větší než fyzicky vydané množství nebo pokud nebyly přijaté zásoby zaznamenány. |
| Zásoba vyřazena | Vyřazené zásoby (účtované plýtvání) lze použít ke sledování ztrát zásob. V návrhu metadat DHIS2 je indikátor „Vyřazeno z zásoby“ stejný jako datový prvek vyřazeného ze zásob vykázaný ve zprávě o stavu zásob zdravotnického zařízení. Lze jej agregovat směrem nahoru v hierarchii a určit celkový vyřazený stav za okres nebo na národní úrovni. |
| Zařízení s výpadkem zásob (%) | Podíl zařízení, která vykazují alespoň jeden skladový den, mezi všechna zařízení, která předložila zprávu o stavu zásob. Čitatel = počet organizačních jednotek, pro které jsou pro danou skladovou položku vykázány dny vyprodání zásob. Jmenovatel = počet zařízení, která byla hlášena během vykazovaného období. |
| Doba pokrytí podle zařízení (poměr) | Čitatel: Počáteční zůstatek + přijaté zásoby Použitelné zásoby / Vydané + Vyřazené + Přerozděleny = počet měsíců, kde použitelné zásoby = počáteční zůstatek + přijato |
| Dny bez zásob podle zařízení | Celkový počet dní do vyčerpání zásob vykázaných zařízením během období analýzy pro jakoukoli danou skladovou položku |

Všechny základní indikátory jsou konfigurovány **podle položek** v závislosti na zdravotním programu.

Balíček metadat umožňuje programům monitorovat kritické indikátory řízení výkonu logistiky v rámci HMIS. **Počet dní do vyčerpání zásob** je klíčovým výkonnostním indikátorem pro hodnocení kvality plánování poptávky, prognózování, výpočtů doplňování zásob, objednávání a také spolehlivosti a včasnosti logistických služeb pro dodávky zdravotnických produktů. Všechny zdravotnické produkty by měly být neustále na skladě a veškeré zásoby je třeba urychleně řešit.

**Ztráty zásob** (nebo „plýtvání“) je druhou kritickou součástí pro programatické sledování výkonnosti zásob. Ztráty akcií jsou buď „Vyřazené zásoby“, protože byly poškozeny, vypršela jejich platnost nebo se staly nepoužitelnými z jiných důvodů (ztráty, které lze zaúčtovat), nebo „Nesrovnalosti v zásobách“, které představují nevysvětlené nebo nezapočítané ztráty pro danou skladovou položku. Tyto dva typy ztrát (vyřazené a nesrovnalosti) jsou zahrnuty v klíčových logistických ukazatelích pro každou položku na skladě a lze je triangulovat, abychom porozuměli výkonnosti zásob.
