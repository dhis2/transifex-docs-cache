---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/features-supported.md"
revision_date: "2021-11-23"
---

# Programy { #capture_app_programs }

## Programy v Androidu { #capture_app_programs_android }

### Local Analytics (NOVINKA 2.5) { #local-analytics-new-25 }

Aplikace pro Android nyní může vykreslovat analýzy, které byly vytvořeny v aplikaci Data Visualizer v DHIS2. Analýzy, které mají být zobrazeny, musí být nakonfigurovány pomocí webové aplikace Android Settings, kde administrátoři budou moci rozhodnout, jaké grafy a tabulky se zobrazí koncovým uživatelům.

Chcete-li nakonfigurovat analýzu, otevřete webovou aplikaci Nastavení Android na svém serveru DHIS2 a postupujte podle následujících kroků:

1. V nabídce Analytika vyberte možnost Domovská strana, Program nebo Datová sada.
2. Klikněte na tlačítko "Přidat vizualizaci".
3. Vyhledejte zadáním názvu vizualizace a vyberte ji kliknutím
4. Přidejte alternativní název, jinak aplikace zobrazí název vizualizace

![](resources/images/capture-app-image162.png){ width=25%} ![](resources/images/capture-app-image164.png){ width=25%}

Analýzy se vytvářejí a konfigurují pomocí webových nástrojů, ale agregace dat probíhá offline pouze pomocí dat uložených v zařízení.

![](resources/images/capture-app-image165.png){ width=25%} ![](resources/images/capture-app-image166.png){ width=25%} ![](resources/images/capture-app-image167.png){ width=25%}

#### Typy a filtry analýzy { #analytics-types-and-filters }

Analýzy podporované v aplikaci pro Android jsou:

-   Kontingenční tabulky
-   Sloupcový graf
-   Spojnicový graf
-   Výsečový graf
-   Radarová mapa
-   Jedna hodnota

Pro každý objekt vizualizace bude uživatel moci v aplikaci filtrovat podle:

-   Období: Denně, Týdně, Měsíčně, Ročně, Toto čtvrtletí, Poslední čtvrtletí, Poslední 4 čtvrtletí a čtvrtletí tohoto roku.
-   Organizační jednotka: Vyberte „Vše“ pro zobrazení všech organizačních jednotek dostupných uživateli nebo „Výběr“ pro určení jedné nebo více organizačních jednotek. ![](resources/images/capture-app-image180.png){ width=25%} ![](resources/images/capture-app-image168.png){ width=25%} ![](resources/images/capture-app-image169.png){ width=25%}

Pokud je použit filtr, zobrazí se tlačítko reset. Vyberte Reset pro zobrazení výchozí vizualizace.

![](resources/images/capture-app-image170.png){ width=25%}

Uživatelé mohou také změnit typ analýzy mezi grafem, tabulkou nebo jednou hodnotou.

![](resources/images/capture-app-image166.png){ width=25%} ![](resources/images/capture-app-image171.png){ width=25%}

#### Skupiny { #groups }

Všechny tyto vizualizace lze organizovat a zobrazovat ve skupinách. Skupiny se také konfigurují pomocí webové aplikace Nastavení Android podle následujících kroků:

1. Otevřete aplikaci Nastavení Android
2. Kliknutím přidáte novou vizualizaci v nabídce Analytics (domovská stránka, program nebo soubor dat)
3. Vyberte vizualizaci
4. Zaškrtněte políčko „Použít skupinovou vizualizaci“.
5. Vytvořte nebo vyberte vytvořenou skupinu
6. Uložte vizualizaci

Své různé skupiny můžete pojmenovat, zobrazí se jako tlačítko v horní liště obrazovky analýzy.

![](resources/images/capture-app-image173.png){ width=25%}

#### Omezení { #limitations }

Android používá tabulky a grafy vytvořené pomocí webové aplikace Visualizer, nicméně aplikace Android používá pouze konfigurační parametry objektu: datové prvky, indikátory, typ grafu, nadpis, období...; všechny agregace jsou počítány offline aplikací pro Android. Výsledky budou založeny na datech uložených v zařízení přesně v daný okamžik.

Vzhledem k tomu, že zobrazené agregace a výpočty jsou počítány v zařízení, je implementace analytiky ve srovnání s webem omezená. V souhrnu jsou kompatibilní a podporované objekty a funkce:

-   Dobře tvarované analytické objekty (řady, kategorie, filtry)
-   Uživatel má přístup k prohlížení
-   Omezení pro kontingenční tabulky
    -   Počet řádků záhlaví: 1
    -   Počet sloupců záhlaví: 1
-   Omezení pro grafy
    -   Počet sérií: Bez omezení (ale nezapomeňte, že vykreslujete na malé obrazovce)
    -   Počet kategorií (neplatí pro koláčový graf): Bez omezení

Na Android Analytics se vztahuje mnohem více omezení týkajících se mnoha možností konfigurace dostupných ve Web Visualizer a také podporovaných funkcí a výpočtů souvisejících s indikátory a indikátory programu. [Tato tabulka](https://docs.google.com/spreadsheets/d/1127cz7M0K4fux5CU0V54V2Z77NZWCr0BTrZ6jcCec4Q) shrnuje všechny podporované funkce.

### Událost – vztahy TEI (NOVINKA 2.5) { #event-tei-relationships-new-25 }

Aplikace umožňuje přidávat vztahy z jednotlivých akcí (v programech akcí) do TEI. Na obrazovce události je nová karta s názvem vztahy, která se zobrazí pouze tehdy, když je tento typ vztahů na serveru nakonfigurován pro konkrétní program.

> > Tato verze neumožňuje TEI vztahovat se k událostem nebo používat události, které patří k zápisu.

![](resources/images/capture-app-image175.png){ width=25%}

### Nová navigační lišta { #new-navigation-bar }

Pomocí nové navigační lišty můžete přecházet z jedné obrazovky na druhou.

#### Události { #events }

1. Detaily
2. Vstup dat
3. Analytika
4. Poznámky

![](resources/images/capture-app-image141.jpg){ width=25%}

#### Ovládací panel TEI { #tei-dashboard }

1. Detaily
2. Analytika
3. Vztahy
4. Poznámky

![](resources/images/capture-app-image142.jpg){ width=25%}

#### Seznam událostí pro programy pro sledování událostí a tracker { #event-listing-for-event-and-tracker-programs }

1. Zobrazení Seznam
2. Zobrazení mapy

![](resources/images/capture-app-image143.jpg){ width=25%}
![](resources/images/capture-app-image144.jpg){ width=25%}

### Dokončit / Znovu otevřít událost { #capture_app_programs_complete_reopen }

Uživatel musí zadat událost a poté kliknout na ikonu dokončení v pravém dolním rohu.

![](resources/images/capture-app-image37.jpg){ width=25%}
![](resources/images/capture-app-image74.png){ width=25%}

Budou představeny dvě možnosti:

1. Ukončit a dokončit
2. Ukončit

![](resources/images/capture-app-image75.png){ width=25%}

> **Poznámka**
>
> Chcete-li ověřit, zda je událost dokončena, podívejte se na ikonu, musí to být zelené zaškrtávací políčko.

> **Poznámka**
>
> Aplikace musí vzít v úvahu, zda má uživatel správné oprávnění („Nedokončené události“) znovu otevřít dokončenou událost.

### Procento dokončení pole { #capture_app_programs_field_percentage }

Procento dat dokončených v každé události se zobrazuje v pravém horním rohu události, když je otevřena po první registraci.

![](resources/images/capture-app-image80.png){ width=25%}

> **Poznámka**

### Sekce Navigace { #capture_app_programs_sections_nav }

Vyobrazení pro sekce bylo přepracováno pro jednodušší uživatelský zážitek. Kromě toho jsou nyní sekce ve formuláři pro zápis podporovány a jsou zarovnány s designem sekcí událostí.

![](resources/images/capture-app-image115.png){ width=25%}
![](resources/images/capture-app-image116.png){ width=25%}

### Chybové zprávy { #capture_app_programs_errors }

Když se uživatel pokusí dokončit událost nebo registraci, aplikace nyní zobrazí seznam povinných polí, která chybí. Sekce obsahující chybějící pole budou zvýrazněna, aby pomohla uživateli najít chybějící pole.

![](resources/images/capture-app-image117.png){ width=25%}

Chyby a varování se také zobrazují jako indikátor vedle názvu sekce.

![](resources/images/capture-app-image145.png){ width=25%}

### Poznámky k Události { #capture_app_programs_event_notes }

K událostem je možné přidávat poznámky v programech jednotlivých událostí a událostech programových scén. Poznámky jsou k dispozici na nové kartě ve formuláři pro zadávání údajů.

![](resources/images/capture-app-image106.png){ width=25%}
![](resources/images/capture-app-image107.jpg){ width=25%}

### Mapy { #capture_app_programs_maps }

#### Vrstvy mapy { #capture_app_programs_map_layers }

Možné vrstvy, které se mají zobrazit na mapách, jsou:

-   Zobrazit události (pro programy bez registrace)
-   Satelitní pohled
-   Souřadnice TEI (standardně v programech s registrací)
-   Souřadnice zápisu (pouze pro programy s registrací)
-   Souřadnice fáze programu (pouze pro programy s registrací)
-   Vztahy (pouze pro programy s registrací)
-   Teplotní mapa (pouze pro programy s registrací)
-   Atributy trasované entity (typ hodnoty souřadnic – pouze pro programy s registrací)
-   Datové prvky (typ hodnoty souřadnic)

Uživatel může vybrat jednu nebo více vrstev, které se mají zobrazit.

Na mapách se zobrazí souřadnice a polygony.

![](resources/images/capture-app-image125.png){ width=25%} ![](resources/images/capture-app-image136.png){ width=25%}

#### Karusel map { #capture_app_programs_map_carousel }

V mapovém zobrazení programu se zobrazí karusel karet, jeden pro každý zaregistrovaný TEI (Programy trasovačů) nebo Událost (Programy událostí).

-   Karty TEI na karuselu mají stejný design jako zobrazení seznamu TEI.

-   Při vodorovném posouvání karuselu se mapa přiblíží na vybrané souřadnice. Pokud je pole souřadnic prázdné, místo toho se zobrazí zpráva.

![](resources/images/capture-app-image126.png){ width=25%} ![](resources/images/capture-app-image133.png){ width=25%}

Každá karta zobrazuje trasované atributy entit (pro programy Tracker) a datové prvky (pro programy událostí) nakonfigurované jako 'Zobrazit v seznamu'.

![](resources/images/capture-app-image147.png){ width=25%}

#### Vztahy { #capture_app_programs_map_relationships }

V trasovači může uživatel zobrazit vztahy na mapě klepnutím na ikonu mapy na kartě vztahy.

-   Ve směru vztahu je zobrazena šipka.
-   U obousměrných vztahů ukazuje šipka na obě strany.
-   Každý typ vztahu zobrazuje jinou barvu.
-   Pokud má jeden nebo oba TEI jako souřadnici polygony, čára jde od nejbližšího bodu jednoho (a k nejbližšímu druhého) polygonu obou TEI.

![](resources/images/capture-app-image132.png){ width=25%}

#### Aktuální umístění (vylepšeno 2.5) { #current-location-improved-25 }

Pokud uživatel udělí aplikaci oprávnění k poloze, mapa zobrazí aktuální polohu znázorněnou jako modrý barevný bod. Mapy v aplikaci DHIS2 Android Capture App nyní obsahují možnost vycentrovat mapu na místo uživatele.

![](resources/images/capture-app-image148.png){ width=25%}

#### Navigace na konkrétní místo { #navigation-to-specific-location }

Pokud má TEI nebo událost souřadnice, v pravém horním rohu karty se zobrazí navigační ikona. Kliknutím otevřete umístění v aplikaci Mapy.

![](resources/images/capture-app-image149.png){ width=25%} ![](resources/images/capture-app-image150.png){ width=25%} ![](resources/images/capture-app-image151.jpg){ width=25%}

### Pracovní seznamy { #working-lists }

Pracovní seznamy jsou nyní kompatibilní s aplikací pro Android. Jakmile je vybrán seznam, filtry budou blokovány a nebude jim dovoleno měnit, dokud uživatel neobnoví vyhledávání.

Pracovní seznamy jsou k dispozici v programech událostí a sledovačů.

![](resources/images/capture-app-image152.png){ width=25%} ![](resources/images/capture-app-image153.png){ width=25%}

### Programové Indikátory { #program-indicators }

Nová karta analytiky nyní podporuje zobrazení páru text a klíč / hodnota v sekci zpětné vazby nebo indikátoru.

![](resources/images/capture-app-image154.png){ width=25%}

### Legendy { #legends }

Legendy jsou nyní k dispozici v aplikaci pro Android. Zobrazí se vedle hodnoty s příslušnou barvou a štítkem.

![](resources/images/capture-app-image155.png){ width=25%}

## Program s registrací v systému Android { #capture_app_programs_with_reg }

### Navigační panel TEI Dashboard (nový 2.5) { #tei-dashboard-navigation-panel-new-25 }

Pro zjednodušení a přizpůsobení uživatelské zkušenosti budou akce uživatelského rozhraní nabízené uživateli na ovládacím panelu TEI přizpůsobeny konkrétní konfiguraci každého programu.

-   Karta Vztahy nebude viditelná, pokud nejsou nakonfigurovány vztahy programu
-   Tlačítko „Vytvořit událost“ bude skryto, když uživatel nemůže vytvořit další události na základě konfigurace měřiče.
-   Záložka Indikátor nebude viditelná, pokud program nemá nakonfigurovány žádné indikátory programu.
-   Filtr organizačních jednotek nebude viditelný, pokud má uživatel nakonfigurovanou pouze jednu organizační jednotku.

### TEI Card Design { #capture_app_programs_tei_design }

Nový design karty TEI zahrnuje:

-   Datum poslední aktualizace
-   První 2 atributy s možností displayInList
    -   Pokud je jich více, zobrazí se šipka pro zobrazení celého seznamu
-   Zápis organizační jednotky
-   Štítek stavu registrace, pokud je **dokončen** nebo **zrušen**
-   Ikona po termínu, pokud existuje událost po termínu s nejnovějším datem události po termínu 
-   Ikona sledování, pokud je označeno TEI
-   Karta Obrázku (jedna z následujících možností):
    -   Profilový obrázek, pokud je k dispozici, nebo
    -   První písmeno prvního atributu nebo
    -   Ikona typu trasované entity
    -   Pokud není k dispozici žádná z možností, zobrazí se pomlčka

![](resources/images/capture-app-image124.png){ width=25%}

### Dokončete / deaktivujte registraci { #capture_app_programs_complete_deactivate_enrollment }

Chcete-li registraci dokončit nebo deaktivovat, klikněte na nabídku se třemi tečkami v pravém horním rohu a vyberte možnost „Dokončit“ nebo „Deaktivovat“.

![](resources/images/capture-app-image76.jpg){ width=25%}

### Resetujte vyhledávací pole { #capture_app_programs_reset_search }

Všechny sledovací programy přenesou uživatele na obrazovku vyhledávání. Vyhledávací pole se používají k vyhledání konkrétní entity a šipkou v kroužku se vyhledávání resetuje. Všechna pole budou pro nového uživatele prázdná.

Zpočátku je uživatel povinen provést vyhledávání. Pokud neexistují žádné koincidence, tlačítko vyhledávání se změní na tlačítko „Přidat“, aby uživatel vytvořil novou registraci.

![](resources/images/capture-app-image79.png){ width=25%}

### Obrazovka vyhledávání všech typů sledovaných entit { #capture_app_programs_search_screen }

Uživatel je schopen vyhledávat ve všech programech jednoho typu trasované entity (TET). Na obrazovce Hledat je rozevírací seznam, který zobrazuje všechny programy dostupné pro aktivní TET (aktivní TET je definován výběrem programu na domovské obrazovce). Tato rozevírací nabídka by měla mít také možnost s názvem TET. (například: osoba)

Když uživatel vybere tuto možnost, budou vyhledávacími poli k dispozici pouze atributy TET (žádné atributy specifické pro program). Omezení vyhledávání neplatí, protože patří k programům.

![](resources/images/capture-app-image44.png){ width=25%}
![](resources/images/capture-app-image22.png){ width=25%}

Hledání vrátí nalezené TEI v místní databázi a také ty ve vyhledávací organizační jednotce uživatele (když je uživatel online). U uživatelů nalezených online je bude muset uživatel vybrat a stáhne se celý záznam.

> **Poznámka**
>
> Při konfiguraci vyhledávací organizační jednotky se ujistěte, že vaše zachycené org. jednotky jsou obsaženy ve vašem vyhledávání org. jednotek, aby to zachytilo org. jednotky které musí být vybrány, stejně jako vyhledávací org. jednotky.

### Ovládací panel TEI napříč programy { #capture_app_programs_tei_dashboard }

Uživatel může zobrazit panel TEI bez jakéhokoli programu výběrem TEI v seznamu, pokud bylo vyhledávání bez programu.

Na ovládacích panelech se zobrazí seznam aktivních registrací.

![](resources/images/capture-app-image22.png){ width=25%}
![](resources/images/capture-app-image38.png){ width=25%}

### Historie zápisu TEI a nový zápis { #capture_app_programs_tei_history }

Uživatel je schopen zobrazit kompletní historický záznam TEI. Kliknutím na nabídku v pravém horním rohu vyberte možnost „Programové zápisy“ a zobrazí se seznam aktivních zápisů následovaný seznamem minulých zápisů (dokončených nebo zrušených) a dále programy, do kterých lze TEI zaregistrovat. Uživatel se může také vrátit na 'TEI Ovládací panel bez jakéhokoli programu' výběrem 'Všechny registrace'.

Uživatelé by měli být schopni přejít na různé registrace ze seznamu.

![](resources/images/capture-app-image40.jpg){ width=25%}
![](resources/images/capture-app-image7.png){ width=25%}

### Smazat TEI a registrace { #capture_app_programs_delete_tei }

Chcete-li odstranit TEI nebo zápis, vyberte na ovládacím panelu TEI nabídku tří teček.

Místní TEI nebo zápis budou z databáze odstraněny. Záznamy, které byly dříve synchronizovány se serverem, budou označeny k odstranění, pokud má uživatel oprávnění:

F_ENROLLMENT_CASCADE_DELETE</br> F_TEI_CASCADE_DELETE

Zobrazí se v seznamu hledání TEI, ale nebudou přístupné.

![](resources/images/capture-app-image86.jpg){ width=25%}

### Skupinové zobrazení fází programu v TEI Dashboard { #capture_app_programs_group_view }

TEI ovládací panel nyní nabízí možnost změnit seznam událostí z chronologického zobrazení na zobrazení seskupení scén. Zobrazení seskupení fází seskupí a sbalí události podle jednotlivých fází programu. Každou skupinu programových fází může uživatel rozšířit a události se zobrazí chronologicky.

![](resources/images/capture-app-image108.png){ width=25%}
![](resources/images/capture-app-image109.jpg){ width=25%}

### Zdědit hodnoty { #capture_app_programs_inherit_values }

Při vytváření nového TEI pro vztah zdědíte jakýkoli atribut programu označený zaškrtnutím zdědění na webu.

To znamená, že všechny existující atributy v prvním TEI by měly projít novým TEI a být zobrazeny v registračním formuláři.

### Rozbití skla { #capture_app_programs_breaking_the_glass }

Funkce „rozbití skla“ zatím není v aplikaci DHIS2 Android Capture podporována. Pokud je program nakonfigurován jako „chráněný“, výchozí chování pro Android bude stejné, jako kdyby byl program nakonfigurován jako „uzavřený“. To znamená, že uživatel Androidu nebude moci číst ani upravovat registrace TEI mimo jejich zachycovací org. jednotky. TEI registrované ve vyhledávací organizační jednotce budou vráceny hledáním TE Type, ale pokud je program uzavřen nebo chráněn, uživateli nebude povoleno vidět nebo vytvořit nový zápis. Pokud uživatelé systému Android musí mít přístup k TEI mimo organizační jednotku pro sběr dat, měl by být program nakonfigurován na úrovni přístupu „Otevřít“.

![](resources/images/capture-app-image137.jpg){ width=25%}

### Analytické grafy { #analytic-charts }

Je možné zobrazit vývoj v datových prvcích jako grafy, hodnoty nebo tabulky. Tyto datové prvky musí být typu číselné hodnoty a musí být konfigurovány v opakovatelné fázi.

1. Jedna hodnota: Zobrazí nejnovější hodnotu v programu.

![](resources/images/capture-app-image156.png){ width=25%}

2. Grafy: Hodnoty je možné zobrazit jako spojnicový graf nebo jako sloupcový graf.

![](resources/images/capture-app-image157.png){ width=25%}

Grafy růstu výživy jsou zobrazeny podle standardů WHO. Tato možnost vykreslí obrázek na pozadí a použije osu (0 až 5 měsíčně) podle modelu WHO.

![](resources/images/capture-app-image159.png){ width=25%}

3. Tabulky: Zobrazí datové prvky nebo indikátory v řádcích a období ve sloupcích.

![](resources/images/capture-app-image160.png){ width=25%}

## Přehled podporovaných funkcí { #capture_app_programs_supported_features }

Následuje úplný seznam všech funkcí dostupných pro programy s registrací a bez registrace v DHIS2 a poznámky o tom, zda byly nebo nebyly implementovány v aplikaci Android Capture.

V poznámkách výraz „admin“ označuje někoho, kdo vyvíjí a konfiguruje systém DHIS2, a „user“ označuje někoho, kdo používá aplikace k pořizování dat, jejich aktualizaci a kontrole zpráv.

| Legenda | Popis |
| :-: | :-- |
| ![](resources/images/../../admin/icon-complete.png) | Funkce implementována |
| ![](resources/images/../../admin/icon-incomplete.png) | Funkce není implementována&nbsp; (bude ignorována) |
| ![](resources/images/../../admin/icon-na.png) | Nelze použít |
| ![](resources/images/../../admin/icon-wip.png) | Ve vývoji. Funkce ještě není zcela implementována nebo již bylo hlášeno neočekávané chování. |

### Program { #capture_app_programs_supported_features_program }

| Funkce | Popis funkce | Program s registrací | Program bez registrace | Poznámky k provádění |
| --- | --- | :-: | :-: | --- | --- |
| Metoda zadávání dat pro sady možností | Umožňuje správci zvolit, jak se budou možnosti zobrazovat na obrazovce v celém programu (tj. Jako rozevírací seznamy nebo jako přepínače) | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-incomplete.png) | To bude nahrazeno novými možnostmi vykreslení. |
| Kombinace kategorií <br /> (atribut CatCombo) | Umožňuje správci připojit kategorii (sadu voleb) k programu a vyžaduje, aby uživatelé kategorizovali každý zápis. (Tomu se v DHIS 2 říká kombinace kategorií atributů.) | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Pracovní postup schválení dat | Pokud správce vybere předkonfigurovaný pracovní postup schvalování dat, použije se k vynucení kaskády &lsquo;schválení&rsquo; nebo &lsquo; akceptace a schválení&rsquo;, což uživatelům umožní odhlásit se a uzamknout data. | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Zobrazit seznam titulních stránek | Pokud je tato možnost zaškrtnutá, zobrazí se na vstupní stránce seznam aktivních registrací, jakmile bude vybrána jednotka organizace a program. (Zobrazené atributy jsou ty, které jsou zaškrtnuty jako „zobrazit v seznamu“.) | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| První fáze se objeví na registrační stránce | Pokud je vybrána tato možnost, pak se během registrace programu zobrazí také obrazovka pro první fázi programu (registrace a první událost jsou zachyceny společně na jedné obrazovce). | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) | V Androidu se to implementuje otevřením události automaticky po dokončení registrace, místo přidání formuláře na stejnou obrazovku. |
| Dny vypršení platnosti dokončených událostí | Umožňuje správcům uzamknout zadávání dat určitý počet dní po dokončení události. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Typ doby platnosti + dny platnosti | Umožňuje správcům nastavit období (např. týdenní, měsíční) a zamknout zadávání dat určitý počet dní po skončení období. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Povolit budoucí data zápisu | Pokud je zaškrtnuto, umožňuje to uživateli zadat budoucí data registrace během registrace do programu; jinak jsou uživatelé omezeni na dnešní nebo minulá data. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Povolit budoucí data incidentu | Pokud je zaškrtnuto, umožňuje to uživateli zadat budoucí data incidentu během registrace do programu; jinak jsou uživatelé omezeni na dnešní nebo minulá data. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Zaregistrovat se pouze jednou (za dobu životnosti instance trasované entity) | Pokud je zaškrtnuto, brání tomu, aby TEI (např. osoba) byla zapsána do tohoto programu více než jednou. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Zobrazit datum incidentu | Pokud je zatrženo, zobrazí se uživateli data zápisu i incidentu pro sběr dat; jinak se zobrazí / zachytí pouze datum zápisu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Popis data incidentu | Umožňuje správci přizpůsobit štítek, který se používá pro datum incidentu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Popis data zápisu | Umožňuje správci přizpůsobit štítek, který se používá pro datum zápisu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Zachyťte souřadnice (zápis) | Umožňuje uživatelům zachytit zeměpisné souřadnice během zápisu do programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Zachycení polygonu (zápis) | Umožňuje uživatelům zaznamenávat umístění (uzavřené oblasti) během zápisu do programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Souřadnice TEI | Umožňuje uživatelům zaznamenávat zeměpisné souřadnice TEI během zápisu do programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Vztahy: vytváření a aktualizace | Umožňuje uživatelům vytvářet a aktualizovat vztahy. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Vztahy - odkaz na přidání příbuzného | To umožňuje správcům přidat odkaz na jeden konkrétní vztah na ovládací panel, což uživatelům umožňuje přímo vytvořit propojený TEI (např. „dětský“ pacient). | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Atributy: zobrazit v seznamu | Toto nastavení určuje, zda lze atribut zobrazit v seznamech, například ve výsledcích vyhledávání, a zda jej lze zobrazit v užším seznamu atributů zobrazeném v části „Profil“ na hlavním panelu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) | Zobrazí se první tři atributy |  |
| Atributy: povinné | To umožňuje správci označit atribut jako „povinný“; což znamená, že zápis nemůže být uložen, dokud nebude hodnota zachycena. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Atributy: datum v budoucnosti | U atributů data to umožňuje správci zabránit nebo povolit zachycení budoucích dat. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Registrační formulář - výchozí | Výchozí formulář pro zadávání dat jednoduše uvádí všechny atributy definované pro TEI. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Registrační formulář - vlastní | To umožňuje správci definovat vlastní rozložení (pomocí HTML) pro registrační formulář. | - | ![](resources/images/../../admin/icon-na.png) | V aplikaci pro Android nejsou vlastní rozvržení podporována |  |
| Oznámení o programu | Můžete nastavit automatická oznámení, kdy dojde k registraci nebo dokončení programu, nebo v nastaveném intervalu před / po incidentu nebo datu registrace. Ty lze odesílat jako interní zprávy DHIS 2, e-maily nebo SMS. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) | Tato funkce se provádí na straně serveru, jakmile jsou přijata data. Nefunguje, když aplikace pracuje offline. |  |
| Aktivovat / deaktivovat zápis | Deaktivace ovládacího panelu TEI způsobí, že se TEI stane jen ke čtení. To znamená, že nemůžete zadávat data, registrovat TEI nebo upravovat profil TEI. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Dokončení povoleno, pouze pokud ověření proběhne | Zaškrtnutím políčka vynutíte, aby událost vytvořená tímto programem byla dokončena, až když prošly všechna pravidla ověřování. | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Data otevření / zavření organizační jednotky | Umožňuje správci nastavit otevírací a uzavírací data pro organizační jednotku, která uživatelům blokuje přidávání nebo úpravy událostí mimo tato data. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Může zachytit data | Umožňuje uživateli přidávat nové události, upravovat data a mazat události v programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Může zobrazit data | Umožňuje uživateli zobrazit seznam událostí v rámci programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Žádný přístup | Uživatel nebude moci program vidět | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |

### Fáze programu { #capture_app_programs_supported_features_program_stage }

| Funkce | Popis funkce | Program s registrací | Program bez registrace | Poznámky k provádění |
| --- | --- | :-: | :-: | --- |
| Formulář události - výchozí | Výchozí formulář pro zadávání dat jednoduše uvádí všechny atributy patřící k registraci programu | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Formulář akce - formuláře sekcí | Formuláře oddílů umožňují rozdělit existující formuláře do segmentů | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Formulář události - vlastní | Definujte vlastní formulář události jako stránku HTML. | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-incomplete.png) | V aplikaci pro Android nejsou vlastní rozvržení podporována. |
| Oznámení fáze programu | Můžete nastavit automatická upozornění na dokončení fáze programu nebo v nastaveném intervalu před / po naplánovaných datech událostí. Ty lze odesílat jako interní zprávy DHIS 2, e-maily nebo SMS zprávy. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) | Tato funkce se provádí na straně serveru, jakmile jsou přijata data. Nefunguje, když aplikace pracuje offline. |
| Opakovatelný | Pokud je zaškrtnuto Opakovatelné, lze tuto fázi opakovat během jedné registrace programu. Pokud to není, pak se fáze může stát pouze jednou během registrace programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Opakovatelný | Pokud je zaškrtnuto Opakovatelné, lze tuto fázi opakovat během jedné registrace programu. Pokud to není, pak se fáze může stát pouze jednou během registrace programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Opakovatelné + standardní intervalové dny | Systém navrhne datum vypršení termínu jako výpočet poslední události + standardní data intervalu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Typ období | Umožňuje správci nakonfigurovat sadu období (např. týdnů nebo měsíců) pro každou událost ve fázi programu, nikoli pouze datum. Při vytváření událostí jsou uživatelé požádáni, aby si vybrali období (místo data) pro každou novou událost, kterou vytvoří v dané fázi programu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Automaticky generovat událost | Pokud je zatrženo, vygeneruje se při zápisu pro tuto programovou fázi „rezervace“ na základě „plánovaných dnů od začátku“. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Generovat události na základě data registrace (nikoli data incidentu) | Zkontrolujte na něm automatické generování termínů událostí z programových fází tohoto programu na základě data registrace. Pokud není zaškrtnuto, jsou termíny vygenerovány na základě data incidentu. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Otevřete formulář pro zadávání údajů po registraci + datum hlášení, které chcete použít | Pokud je tato možnost vybrána, měl by se ihned po dokončení zápisu otevřít formulář pro zadávání dat událostí.  | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Po dokončení fáze požádejte uživatele o dokončení programu | Pokud je tato možnost vybrána, po dokončení fáze programu by měl být uživatel vyzván k dokončení programu. (Toto nastavení je ignorováno, pokud je zaškrtnuto také „Požádat uživatele o vytvoření nové události“.) | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Až bude fáze dokončena, požádejte uživatele o vytvoření nové události | Pokud je tato možnost vybrána, po dokončení fáze programu je uživatel vyzván k rezervaci. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Skrýt termín | Zobrazuje pouze skutečné datum událostí, skrývá datum konce platnosti. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Zachycuje souřadnice (událost) / bod typu prvku | Umožňuje uživateli zachytit zeměpisné souřadnice při vytvoření každé události ![](resources/images/../../admin/icon-incomplete.png) zvláště užitečné v zařízeních s GPS (např. Android), protože místo toho, aby musel zadávat souřadnice, může je uživatel automaticky vyplnit stisknutím tlačítka. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Zachytit Polygon (událost) / Polygon typu objektu | Umožňuje uživatelům po vytvoření každé události zachytit umístění (uzavřené oblasti). Polygon musí obsahovat alespoň 4 body. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Popis data zprávy | Umožňuje správci přizpůsobit štítek, který se používá pro datum událostí. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Datové prvky - povinné | To umožňuje správci označit datový prvek jako „povinný“, což znamená, že událost nelze uložit, dokud není zachycena hodnota. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Datové prvky - povoleny poskytované jinde | Ve formuláři toto umístí zaškrtávací políčko vedle vybraného datového prvku a umožní načtení předchozích dat do datového prvku. | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-na.png) |  |
| Datové prvky - zobrazení v hlášeních zpráv | Zobrazí hodnotu tohoto datového prvku do jediné události bez funkce zadávání registračních dat. | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Datové prvky - datum v budoucnosti | U Datových prvků umožňuje datum správci buď zabránit, nebo povolit zachycení budoucích dat. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Možnosti vykreslení datových prvků jako rádio | Umožňuje správci zvolit, jak se budou možnosti zobrazovat na obrazovce pro každý datový prvek (tj. Buď jako rozevírací seznam nebo jako přepínací tlačítka). | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Po vyplnění zablokujte přihlašovací formulář | Zabrání všem úpravám událostí po jejich dokončení. | ![](resources/images/../../admin/icon-complete.png) | ![](resources/images/../../admin/icon-complete.png) |  |
| Komentáře k události | Umožňuje uživateli přidat k události celkové komentáře. Tyto komentáře jsou kumulativní (nové komentáře jsou přidány pod existující komentáře). | ![](resources/images/../../admin/icon-incomplete.png) | ![](resources/images/../../admin/icon-na.png) |  |

### Program s registrací: Ovládací panel trasované entity { #capture_app_programs_supported_features_program_with_reg }

| Funkce | Popis funkce | Status | Poznámky k provádění |
| --- | --- | :-: | --- | --- |
| Zprávy | Umožňuje uživatelům odesílat ad hoc volné textové zprávy TEI (např. Pacientům) prostřednictvím SMS nebo e-mailu. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Značka pro sledování (tlačítko s vykřičníkem) | Umožňuje uživateli označit TEI (např. Pacienta) jako vyžadující sledování. | ![](resources/images/../../admin/icon-complete.png) |  |
| Zobrazí historii auditu TEI | Umožňuje uživateli zobrazit historii všech úprav atributů pro tuto TEI (např. Pacienta). | - |  |
| Indikátory vloženého programu | Pokud je zaškrtnuto políčko „zobrazit ve formuláři“ indikátoru programu, indikátor se zobrazí na ovládacím panelu Tracker Capture a je aktualizován živě, jakmile dojde k zachycení dat. | ![](resources/images/../../admin/icon-complete.png) |  |  |
| Smazat události | Umožňuje uživateli odstranit událost. | ![](resources/images/../../admin/icon-complete.png) |  |
| Naplánujte události | V dialogu pro generování události by se uživateli měla zobrazit také možnost naplánovat událost. Proces je jako vytvoření události, ale uživatel bude po naplánování události odeslán zpět na ovládací panel TEI. | ![](resources/images/../../admin/icon-complete.png) |  |
| Doporučení pacientů | V dialogu generování událostí by se uživateli měla zobrazit také možnost odkázat pacienta. Proces je jako vytváření / plánování události, ale uživatel může změnit organizační jednotku a musí určit, zda jde o jednorázové nebo trvalé doporučení. Jednou se událost vytvoří pouze v zadané organizační jednotce. | ![](resources/images/../../admin/icon-complete.png) |  |
| Resetujte vyhledávací pole | Uživatel je schopen vyčistit vyhledávací pole stisknutím ikony se zaoblenou šipkou v pravém horním rohu obrazovky vyhledávání. | ![](resources/images/../../admin/icon-complete.png) |  |
| Obrazovka vyhledávání všech typů TE | Uživatel je schopen vyhledávat ve všech programech jednoho typu trasované entity (TET). Na obrazovce Hledání je rozevírací seznam, který zobrazuje všechny programy dostupné pro aktivní TET (aktivní TET je definován výběrem programu na domovské obrazovce). Tato rozevírací nabídka by měla mít také možnost s názvem TET. (Osoba na našem serveru). Když uživatel vybere tuto možnost, vyhledávací pole, která jsou k dispozici, budou pouze atributy TET (žádné atributy specifické pro program). Všechna omezení vyhledávání neplatí, protože patří k programům. | ![](resources/images/../../admin/icon-complete.png) |  |
| Ovládací panel TEI bez programu | Uživatel může zobrazit ovládací panel TEI bez jakéhokoli programu výběrem TEI v seznamu, pokud bylo vyhledávání bez programu. Ovládací panely zobrazují atributy TET na kartě podrobností a seznam aktivních registrací. | ![](resources/images/../../admin/icon-complete.png) |  |
| Historie zápisu TEI a nový zápis | Uživatel je schopen zobrazit kompletní záznam historie TEI. Kliknutím na ikonu v pravém horním rohu se jim zobrazí seznam aktivních zápisů, následovaný seznamem minulých zápisů (dokončených nebo zrušených) a programy, do kterých lze TEI zapsat. Uživatelé by měli být schopni přejít na různé zápisy ze seznamu. | ![](resources/images/../../admin/icon-complete.png) |  |
| Přístupová úroveň - rozbití skla | Pokud je program nakonfigurován s chráněnou úrovní přístupu a uživatel prohledá a najde trasované instance entit, které jsou vlastněny organizační jednotkou, pro kterou uživatel nemá oprávnění pro sběr dat, je uživateli nabídnuta možnost porušení zabezpečení. Uživatel zjistí důvod porušení zabezpečení a poté získá dočasné vlastnictví trasované instance entity. | ![](resources/images/../../admin/icon-incomplete.png) |  |

### Program bez registrace: Program jedné události { #capture_app_programs_supported_features_program_without_reg }

| Funkce | Popis funkce | Status | Poznámky k provádění |
| --- | --- | :-: | --- | --- |
| Výpis událostí (mřížka) | Seznam existujících událostí, který se zobrazí po výběru programu. | ![](resources/images/../../admin/icon-complete.png) |  |
| Třídit a filtrovat události v mřížce | Umožňuje uživateli třídit uvedené události nebo filtrovat události na základě klíčových slov nebo konkrétních rozsahů dat / čísel. | ![](resources/images/../../admin/icon-complete.png) | Události jsou řazeny chronologicky. Uživatel může filtrovat podle období a organizační jednotky. |  |
| Úpravy událostí v mřížce | Umožňuje uživateli přímo upravit datové prvky zobrazené v seznamu událostí / mřížce. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Zobrazit historii auditu událostí | Umožňuje uživateli zobrazit historii všech změn datových prvků event&rsquo;s. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Zobrazit / skrýt sloupce (v seznamu událostí / mřížce) | Umožňuje uživateli upravit datové prvky zobrazené v seznamu událostí / mřížce (platí pouze pro daného uživatele). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Procento dokončení pole | Procento dat dokončených v každé události se zobrazuje v pravém horním rohu události, když je otevřena po první registraci. Procenta by měla být přizpůsobena účinkům pravidel programu ve formulářích. | ![](resources/images/../../admin/icon-complete.png) | Procento dokončení nebere v úvahu nepodporované typy hodnot ve formulářích. |  |
| Smazat události | Umožňuje uživateli odstranit událost. | ![](resources/images/../../admin/icon-complete.png) |  |
