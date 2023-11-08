---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/ReleaseNote-2.38.md"
revision_date: "2022-05-05"
---

# Poznámka k vydání DHIS verze 2.38 { #dhis-version-238-release-note }

## ANALYTICKÉ VLASTNOSTI { #analytics-features }

**Nová aplikace Line Listing:** Tato nová aplikace je masivním vylepšením pro vytváření seznamů řádek trasovaných entit v DHIS2 oproti aplikaci pro hlášení událostí. Nová aplikace pro vytváření řádků replikovala všechny funkce řádkového výpisu aplikace pro hlášení událostí a má zcela nové, mnohem vylepšené uživatelské prostředí, které uživatelům výrazně usnadňuje vytváření řádkového seznamu trasovaných entit. Obsahuje také mnoho nových funkcí. Níže je uveden seznam některých klíčových nových funkcí:

-   Vizualizace více opakujících se událostí: Nyní jste schopni vytvořit seznam řádků, který může zobrazovat data z více opakujících se fází pro jednu trasovanou entitu. Můžete určit, z kolika opakovaných fází chcete data zobrazit. To je užitečné pro mnoho zdravotnických a vzdělávacích programů, protože umožňuje vizualizaci dat zachycených opakovaně v průběhu času pro jednoho pacienta nebo studenta. [Snímek obrazovky 1](images/2.38repeatingevent.png) | [Snímek obrazovky 2](images/2.38repeatingevent2.png)
-   Nové dimenze období specifického pro sledování: V nové aplikaci Line Listing můžete vytvořit seznam řádků zobrazující datum registrace, datum události a/nebo datum incidentu. Každý z nich může být definován, tříděn a zobrazen společně v jednom řádku seznamu. [Snímek obrazovky](2.38linelisttimedemensions.png)
-   Vytvořil a Poslední aktualizace: Umožňuje zobrazit uživatelské jméno uživatele, který buď vytvořil registraci, nebo uživatele, který naposledy aktualizoval data trasované entity.

[Snímek obrazovky](images/2.38_linelist_2.png)

**Spádové oblasti pro organizační jednotky (zařízení, školy, zdravotní stanice atd.):** DHIS2.38 podporuje více geometrií (bodů a tvarů) pro všechny organizační jednotky. Ty lze zobrazit v aplikaci mapy pro jakoukoli standardní vrstvu prostřednictvím možnosti ve výběru organizačních jednotek. Prakticky to znamená, že správci systému mohou nahrávat spádové oblasti pro svá zařízení, zdravotnická zařízení, školy, nemocnice atd. a vizualizovat jakákoli data podle spádové oblasti.

[Snímek obrazovky](images/2.38_catchment_area.png) | [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-235/analysing-data/maps.html) |

**Podpora pro vrstvu Google Earth Building/Structures Layer:** Uživatelé nyní mohou v mapové aplikaci vidět obrysy struktury, jak je identifikuje datový soubor Open Building společnosti Google. Tento soubor dat zahrnuje 516 milionů budov (64 % afrického kontinentu). Je užitečná například pro odhad populace, městské plánování, informační a zdravotní programy a humanitární reakci. Počet budov lze zobrazit podle hranic povodí nebo organizační jednotky.

[Snímek obrazovky 1](images/2.38_structures_1.png) | [Snímek obrazovky 2](images/2.38_structures_2.png) | [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-235/analysing-data/maps.html) |

**Podpora vektorových dlaždic v Mapách:** Aplikace Mapy nyní používá a podporuje vektorové dlaždice. Výsledkem by měla být určitá vylepšení výkonu a aktualizované základní technologie.

**Indicator aggregationType override:** Indikátor může specifikovat typ agregace, který přepíše výchozí typ přiřazený datovému prvku. Pokud má například datový prvek typ agregace SUM, může indikátor také vykazovat hodnotu podle AVERAGE, COUNT, FIRST, LAST, MIN, MAX atd.

_Příklad výrazu v indikátorech: #{EX2jBdKe4Yq}.aggregationType(COUNT)_ Popis: ER Teachers Trained.aggregationType(COUNT)

[Dokumenty](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

**Ukazatel minDate a maxDate:** Pro načtení datového prvku pro ukazatel lze zadat minimální a/nebo maximální datum. To může být užitečné, když se sémantika dat čas od času mění a vyžaduje různé výpočty pro stejný výsledek. Umožňuje indikátoru konzistentně podávat zprávy o všech těchto změnách změnou způsobu výpočtu indikátoru v průběhu času. Nezapomeňte, že funkci periodOffset (od 2.36) lze také použít k zahrnutí dat z jiného období do výrazu indikátoru.

_Příklad výrazu minDate a maxDate v indikátorech: #{EX2jBdKe4Yq}.minDate(2021-1-1).maxDate(2021-6-30)_ Description: ER Teachers Trained.minDate(2021-1-1).maxDate(2021- 6-30) -> Při výpočtu indikátoru budou použity pouze hodnoty mezi 1. lednem 2021 a 30. červnem 2021 pro učitele ER vyškolené.

_Příklad výrazu periodOffset v indikátorech: #{EX2jBdKe4Yq} + #{EX2jBdKe4Yq}.periodOffset(-1) + #{EX2jBdKe4Yq}.periodOffset(-2)_ Description: ER Trained ER Teachers Trained + Teachers Trained + Description (-1) + ER Teachers Trained.periodOffset(-2) -> Součet ER učitelů vyškolených za poslední tři měsíce ve vztahu k výběru období v analytické aplikaci použité k vizualizaci této hodnoty.

[Dokumenty](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

**Podvýrazy indikátoru (pro 2.38.1):** Indikátory mohou počítat počet organizačních jednotek, kde se datový prvek porovnává specifickým způsobem s pevnou hodnotou.

_Ukázkový výraz podVýraz v indikátorech: subVýraz( if (#{vq2q03TrNi} > 100, 1, 0) )_ Popis: subExpression(if(IDSR Malárie>100,1,0)) -> Spočítá počet organizačních jednotek, kde je více než Bylo hlášeno 100 případů malárie během daného období definovaného v analytické aplikaci použité k vizualizaci této hodnoty.

[Dokumenty](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

## VLASTNOSTI TRASOVÁNÍ A UDÁLOSTÍ { #tracker-and-event-features }

**Vylepšení pracovních seznamů programu Tracker:** Funkčnost pracovních seznamů programů Tracker byla rozšířena tak, aby byla podobná funkcím pracovních seznamů událostí. Aplikace Capture nyní umožňuje konfigurovat, ukládat, sdílet, mazat a aktualizovat pracovní seznamy prostřednictvím uživatelského rozhraní.

[Snímek obrazovky 1](images/Working_list.png) | [Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#capture_views) | [Jira](https://jira.dhis2.org/browse/DHIS2-9275)

**Překlad akcí programových pravidel v aplikaci Tracker Capture and Capture:** Obsah akcí programových pravidel – „statický text“, který je vizualizován uživatelům, lze přeložit a zobrazit v programech Tracker. [Jira](https://jira.dhis2.org/browse/DHIS2-12137)

**Popis a adresy URL pro datové prvky a atributy trasovaných entit:** Popis a adresa URL nastavená pro tyto datové položky se zobrazí ve vyskakovacím okně. K tomuto vyskakovacímu okně lze přistupovat kliknutím na ikonu „i“, která se zobrazí za názvem datového prvku. Popis je nastaven v aplikaci Údržba a lze jej použít k poskytnutí dalších informací o tom, co se má pro datovou položku zachytit.

[Snímek obrazovky 1](images/Capture_DE_description.png) | [Jira](https://jira.dhis2.org/browse/DHIS2-5345)

**Nová komponenta organizační jednotky implementovaná v aplikaci Capture:** Komponenta organizační jednotky použitá v aplikaci Capture byla nahrazena přepracovanou organizační jednotkou z d2-ui.

[Jira](https://jira.dhis2.org/browse/DHIS2-11806)

**Podpora pro GS1 Data Matrix:** GS1 Data Matrix se používá pro čárové kódování farmaceutických a zdravotnických komodit a bude podporovat případy použití v dodavatelském řetězci. Vzhledem k hodnotě pole formátované podle standardu datové matice GS1 a řetězcovému klíči z identifikátorů aplikace GS1 nyní existuje podpora pro programová pravidla extrahující hodnoty z tohoto textu s oddělovači a přiřazující hodnoty k jejich určeným polím. To je implementováno v aplikaci Tracker Capture, Capture a Android Capture.

[Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#program_rules_operators_functions) | [Jira](https://jira.dhis2.org/browse/DHIS2-12353)

**Typ dat/hodnoty pro proměnnou programového pravidla:** U proměnných programových pravidel s typem zdroje „Vypočítaná hodnota“ nabídne aplikace Údržba uživateli přiřazení typu hodnoty. Výchozí typ hodnoty pro vypočítané hodnoty bude text. U všech ostatních typů zdroje proměnných programových pravidel by výběr typu hodnoty neměl být viditelný, protože proměnná zdědí typ ze základního datového prvku nebo atributu trasované entity.

[Jira](https://jira.dhis2.org/browse/DHIS2-12096)

**Programy mohou zůstat otevřené po koncovém datu možnosti atributu:** Určitý program může zůstat otevřený i po uzavření možnosti souvisejícího atributu.

[Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#tracker_enter_programs_details) | [Jira](https://jira.dhis2.org/browse/DHIS2-12118)

**Aplikace Capture vychází průběžně:** Aplikace Capture bude od verze 2.38 průběžně vydávána v centru aplikací. Opravy chyb a nové funkce proto budou k dispozici ke stažení a integraci v době, kdy jsou potřeba, bez upgradu zbytku aplikace. První aktualizovaná verze aplikace Capture bude k dispozici v centru aplikací krátce po vydání 2.38.0. Centrum aplikací je přístupné prostřednictvím aplikace pro správu aplikací.

**Funkce trasování v aplikaci Capture:** Kromě funkce trasování, která byla přidána ve verzi 2.37 pro uzavřené beta testování, byly přidány další funkce. Nové funkce lze otestovat instalací aktualizované aplikace Capture z centra aplikací a přihlášením k používání funkcí sledování v aplikaci Capture. Pouze superuživatelé nebo uživatelé s přístupem ke změně metadat programu budou mít k dispozici funkci opt-in. Zde jsou uvedeny nové funkce sledování, které lze otestovat přihlášením:

-   Widget profilu TEI: Na ovládacím panelu registrace můžete zobrazit widget profilu instance trasované entity. Uvnitř widgetu profilu můžete zobrazit hodnoty klíčových atributů. Klepnutím na tlačítko Upravit proveďte změny v profilu instance trasované entity. Úpravou profilu se otevře dialog, kde lze změnit atributy profilu.
    [Jira](https://jira.dhis2.org/browse/DHIS2-10946)
-   Formulář widgetu pro plánování události: Namísto hlášení události může uživatel zvolit naplánování události později. To se provádí s naplánovaným datem. Otevře se dialog s navrhovaným plánovaným datem a toto datum je určeno sadou pravidel z konfigurace fáze programu a konfigurace programu.
    [Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#schedule-event-widget-form) | [Jira](https://jira.dhis2.org/browse/DHIS2-11861)
-   Rychlé akce v ovládacím panelu zápisu: Widget rychlých akcí nabízí zkratky pro často používané akce pro aktuální registraci, včetně vytvoření události a naplánování události.
    [Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#quick-actions) | [Jira](https://jira.dhis2.org/browse/DHIS2-11953)
-   "Přidat nové" pro dokončené zápisy do widgetu pro zápis: V daném okamžiku může být aktivní pouze jeden zápis, ale pokud budou dokončeny všechny zápisy, bude možnost znovu zapsat TEI do programu ve widgetu pro zápis do programu umožňuje více než jeden zápis na TEI. Pokud program neumožňuje více než jednu registraci, tlačítko přidat nový bude deaktivováno. [Jira](https://jira.dhis2.org/browse/DHIS2-12141)
-   Znovu zapište existující instanci trasované entity: Tím, že v uzamčeném voliči vyberete instanci trasované entity a vyberete jiný program, můžete nyní znovu zaregistrovat existující TEI do jiných programů. Registrační stránka bude předem vyplněna všemi překrývajícími se hodnotami atributů trasované entity.
    [Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#re-enroll-an-existing-tracked-entity-instance) | [Jira](https://jira.dhis2.org/browse/DHIS2-12141)

## VLASTNOSTI PLATFORMY { #platform-features }

**Upozornění na kontrolu verze:** Zavádí se nová služba upozornění na kontrolu verze DHIS 2, která bude zasílat upozornění ve formě zpráv systémové schránky DHIS 2, když budou k dispozici novější verze DHIS 2. To zahrnuje hlavní a opravné verze. To je užitečné k povzbuzení systémových administrátorů k upgradu DHIS 2, aby byla jejich instance zabezpečená a aktuální.

Dokumenty | [Jira](https://jira.dhis2.org/browse/DHIS2-9897)

**Atributy metadat GeoJSON:** GeoJSON je nyní podporován jako typ hodnoty pro atributy metadat. To vám umožní uložit libovolný počet dokumentů GeoJSON, např. pro organizační jednotky.

[Dokumenty]() | [Jira](https://jira.dhis2.org/browse/DHIS2-12328)

**Export ADX:** Aplikace pro import/export nyní umožňuje import a export dat pomocí datového formátu ADX.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/maintaining-the-system/importexport-app.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-4978)

**Konfigurovatelná úroveň protokolu:** Úrovně protokolování lze nyní konfigurovat v konfiguračním souboru `dhis.conf` na úrovni balíčku. To znamená, že můžete zadat úroveň protokolu pro výstup pro konkrétní rámce a moduly v rámci DHIS 2 přímo v konfiguračním souboru DHIS 2.

[Dokumenty](https://docs.dhis2.org/en/manage/performing-system-administration/dhis-core-version-master/installation.html#log-level-configuration) | [Jira](https://jira.dhis2.org/browse/DHIS2-11898)

**Oznámení o deaktivaci účtu:** Při automatické deaktivaci uživatelů prostřednictvím naplánované úlohy deaktivace uživatelů může být příslušnému uživateli zasláno e-mailové upozornění. Počet dní před oznámením lze definovat v konfiguraci úlohy. To je užitečné, aby uživatelé měli možnost se přihlásit, než bude jejich účet deaktivován.

[Dokumenty](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-238/maintaining-the-system/scheduling.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-11589)

**Schéma vstupu sady datových hodnot:** Pro koncový bod rozhraní API sad datových hodnot jsou nyní podporována vstupní schémata, což vám umožňuje importovat data pomocí pole kódu k odkazování na metadata.

[Dokumenty](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-238/data.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-9822)

**Krátký název sady skupin:** Sada skupin indikátorů a sady skupin možností kategorií nyní mají vlastnosti krátkého názvu, což umožňuje přesné vykreslování vhodné pro uživatelské rozhraní. Krátké názvy se nyní používají jako názvy sloupců v tabulkách prostředků místo názvů.

[Jira](https://jira.dhis2.org/browse/DHIS2-7317)

**Zacházení s mezipamětí Analytiky:** Mezipaměť pro analytická data se nyní automaticky vyprázdní při aktualizaci tabulek analytické databáze. To zajišťuje, že analytické dotazy čtou nejnovější data z analytických dat a zkracují časovou prodlevu mezi aktualizací analytických tabulek a daty zobrazenými ve vizualizacích dat.

[Jira](https://jira.dhis2.org/browse/DHIS2-12072)

### PLATFORM API FEATURES { #platform-api-features }

**Vylepšení úložiště dat:** Rozhraní API úložiště dat doznalo řady vylepšení, aby se stalo plnohodnotným úložištěm dat a užitečnějším pro webové aplikace a další klienty.

-   **Filtrování polí:** Umožňuje vrátit pouze konkrétní klíče a hodnoty položek v úložišti dat pomocí parametru `fields`. Funguje podobně jako filtrování polí v rozhraní API metadat. Filtrování probíhá na úrovni jmenného prostoru a je užitečné, když klient potřebuje vypsat mnoho položek se specifickými klíči/hodnotami v jediném dotazu. [Dokumenty](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#datastore-query-api) | [Jira](https://jira.dhis2.org/browse/DHIS2-12154)
-   **Stránkování:** V odpovědích na dotazy je stránkování ve výchozím nastavení podporováno a povoleno. Stránkování můžete určit explicitně pomocí parametrů `page` a `pageSize`. Stránkování je užitečné pro práci s jmennými prostory s vysokým počtem záznamů. [Dokumenty](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#datastore-query-api) | [Jira](https://jira.dhis2.org/browse/DHIS2-12329)
-   **Filtrování záznamů:** Umožňuje porovnat a filtrovat záznamy v jmenném prostoru na základě různých operátorů, jako jsou `eq`, `lt`, `le`, `gt`, `ge`, `like`, `null` pomocí parametru `filter`. Funguje podobně jako filtrování objektů v rozhraní API metadat. Filtrování je užitečné, když chce klient vypsat mnoho záznamů, které odpovídají jednomu nebo více kritériím. [Dokumenty](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#filtering-entries) | [Jira](https://jira.dhis2.org/browse/DHIS2-12331)
-   **Řazení:** Umožňuje seřadit položky ve jmenném prostoru vzestupně nebo sestupně na základě konkrétního klíče/hodnoty pomocí parametru `order`. To je užitečné, když mají klienti specifické požadavky na řazení seznamu záznamů. Dokumenty | [Jira](https://jira.dhis2.org/browse/DHIS2-12330)

**Protokolování požadavků:** Klienti rozhraní API nyní mohou odesílat hodnotu s hlavičkou HTTP `X-Request-ID`, která je součástí všech výpisů protokolu. To je užitečné, když se díváte na protokoly DHIS 2 a snažíte se pochopit, který klient/aplikace zadal požadavek, například při ladění problému, který se týká konkrétní instalace aplikace pro Android do telefonu.

[Dokumenty](https://docs.dhis2.org/en/manage/performing-system-administration/dhis-core-version-238/installation.html#log-configuration) | [Jira](https://jira.dhis2.org/browse/DHIS2-6494)

**Zrušení úloh analytických tabulek:** Nyní můžete zrušit (zastavit) úlohy analytických tabulek, když jsou spuštěny. To je užitečné, chcete-li zastavit dlouho běžící úlohy, aniž byste museli čekat na jejich dokončení.

Dokumenty | [Jira](https://jira.dhis2.org/browse/DHIS2-6314)

### VLASTNOSTI VÝVOJÁŘE PLATFORMY { #platform-developer-features }

## INFORMACE O VYDÁNÍ { #release-info }

| Informace o vydání | Odkaz |
| --- | --- |
| Stáhněte si verzi a ukázkovou databázi | https://www.dhis2.org/downloads |
| Dokumentace | [https://docs.dhis2.org](https://docs.dhis2.org/) |
| Poznámky k upgradu | [Poznámky k upgradu na GitHubu](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/README.md) |
| Úplný seznam funkcí a chyb v této verzi | [Poznámka k vydání](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/ReleaseNote-2.38.md) |
| Zdrojový kód na Githubu | https://github.com/dhis2 |
| Ukázková instance | https://play.dhis2.org/2.38/ |
| Docker image | `docker pull dhis2/core:2.38.0` |
| Obrázky Docker Hub | https://hub.docker.com/repository/docker/dhis2/core |
| komunitní fórum | https://community.dhis2.org/ |
