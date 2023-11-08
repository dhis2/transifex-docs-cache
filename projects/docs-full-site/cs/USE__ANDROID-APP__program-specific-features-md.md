---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/programs-specific-features.md"
revision_date: "2021-11-08"
---

# Datové sady { #capture_app_datsets }

## Datové sady v Androidu { #capture_app_datsets_android }

## Local Analytics (NOVINKA 2.5) { #local-analytics-new-25 }

Aplikace pro Android nyní může vykreslovat analýzy, které byly vytvořeny v aplikaci Data Visualizer v DHIS2. Analýzy, které mají být zobrazeny, musí být nakonfigurovány pomocí webové aplikace Android Settings, kde administrátoři budou moci rozhodnout, jaké grafy a tabulky se zobrazí koncovým uživatelům.

Chcete-li nakonfigurovat analýzu, otevřete webovou aplikaci Android Settings na svém serveru DHIS2 a postupujte podle následujících kroků:

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
-   Organizační jednotka: Vyberte „Vše“ pro zobrazení všech organizačních jednotek dostupných uživateli nebo „Výběr“ pro určení jedné nebo více organizačních jednotek.

![](resources/images/capture-app-image180.png){ width=25%} ![](resources/images/capture-app-image168.png){ width=25%} ![](resources/images/capture-app-image169.png){ width=25%}

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

### Omezení { #limitations }

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

### Navigační lišta { #navigation-bar }

Pomocí nového navigačního panelu můžete přepínat mezi formulářem pro zadávání údajů a obrazovkou s přehledem.

![](resources/images/capture-app-image139.png){ width=25%}

### Přehledová obrazovka { #overview-screen }

Nová karta Přehled obsahuje následující podrobnosti:

-   Název datové sady
-   Poslední aktualizace
-   Stav otevření / zavření
-   Období
-   Organizační jednotka
-   Kombinace možnosti kategorie

![](resources/images/capture-app-image122.png){ width=25%}

#### Ukládání datové sady { #saving-a-data-set }

Pravidla ověřování a dokončení datových sad jsou integrovány do akcí tlačítka Uložit:

-   Když je datová sada nakonfigurována tak, aby se dokončila pouze v případě, že ověření platnosti projde. Pokud je ověření úspěšné, zobrazí se dialogové okno s požadavkem na označení jako dokončené. Aplikace umožní dokončení pouze v případě, že mají všechna povinná pole hodnotu.

![](resources/images/capture-app-image131.png){ width=25%}

-   pokud není úspěšný, měl by se zobrazit chybový dialog a datová sada nebude označena jako úplná. Zobrazí se popis a pokyny ověřovacího pravidla, které uživateli pomohou identifikovat chybu.

![](resources/images/capture-app-image128.png){ width=25%}

-   Na datové sadě, která nemá nastavení „Dokončení povoleno, pouze pokud proběhne ověření“. Při kliknutí na tlačítko uložit; pokud má datová sada přidružená ověřovací pravidla, aplikace požádá uživatele o spuštění ověřovacích pravidel.

![](resources/images/capture-app-image130.png){ width=25%}

-   Pokud ověření není úspěšné, měl by se zobrazit chybový dialog, ale s možností datový soubor přesto dokončit. Zobrazí se popis a pokyny ověřovacího pravidla, které uživateli pomohou identifikovat chybu.

![](resources/images/capture-app-image129.png){ width=25%}

-   Pokud datová sada nemá ověřovací pravidla, bude datová sada označena jako úplná, pokud mají všechna povinná pole hodnotu.

### Zvětšit záhlaví řádků { #increase-row-headers }

Délka prvního sloupce v datových sadách se nyní vypočítá tak, aby zobrazoval celý text pro názvy datových prvků. Uživatelé mohou také upravit šířku, aby ji lépe přizpůsobili své velikosti obrazovky.

![](resources/images/capture-app-image113.png){ width=25%}

### Indikátory { #indicators }

Indikátory jsou nyní k dispozici ve výchozích a sekčních formulářích a jsou zobrazeny ve spodní části formuláře pro zadávání dat.

![](resources/images/capture-app-image140.png){ width=25%}

## Přehled podporovaných funkcí { #capture_app_datsets_supported_features }

Následuje úplný seznam všech funkcí dostupných pro datové sady v DHIS2 a poznámky o tom, zda byly, nebo nebyly implementovány v aplikaci Android Capture.

V poznámkách výraz „admin“ označuje někoho, kdo vyvíjí a konfiguruje systém DHIS2, a „user“ označuje někoho, kdo používá aplikace k pořizování dat, jejich aktualizaci a kontrole zpráv.

| Legenda | Popis |
| :-: | :-- |
| ![](resources/images/../../admin/icon-complete.png) | Funkce implementována |
| ![](resources/images/../../admin/icon-incomplete.png) | Funkce není implementována&nbsp; (bude ignorována) |
| ![](resources/images/../../admin/icon-na.png) | Nelze použít |
| ![](resources/images/../../admin/icon-wip.png) | Ve vývoji. Funkce ještě není zcela implementována nebo již bylo hlášeno neočekávané chování. |

| Funkce | Popis funkce | Status | Poznámky k provádění |
| --- | --- | :-: | --- |
| Typ období | Určuje období pokryté zadáváním údajů. | ![](resources/images/../../admin/icon-complete.png) |  |
| Konec platnosti | Nastavuje termín (dny po období), po kterém DHIS2 uzamkne veškeré zadávání dat pro období (0 znamená, že nebudou vůbec zamknuty). Období lze stále otevírat, ale buňky budou zašedlé. | ![](resources/images/../../admin/icon-complete.png) |  |
| Otevřete budoucí období pro zadávání údajů | Toto nastavení lze použít k odemčení aktuálního období nebo všech období do určitého bodu v budoucnosti. | ![](resources/images/../../admin/icon-complete.png) |  |
| Období zadávání dat | Umožňuje nastavit konkrétní rozsah dat pro zadávání dat období a zabrání shromažďování dat pro období mimo toto období. | ![](resources/images/../../admin/icon-complete.png) |  |
| Dny po období, aby bylo možné se včas přihlásit | Nastavuje termín (dny po období), po kterém DHIS2 považuje zadávání dat za „pozdě“. | ![](resources/images/../../admin/icon-complete.png) |  |
| Kombinace kategorie [Atribut] | Umožňuje správci připojit kategorii (sadu možností) k datové sadě a vygenerovat pro každou možnost samostatnou obrazovku pro zadávání dat (v DHIS2 se tomu říká kombinace kategorie atributů). | ![](resources/images/../../admin/icon-complete.png) |  |
| [Atribut] Omezení možností kombinace kategorií | Pokud se používají kombinace kategorií atributů (viz výše), pak tato funkce dává správcům možnost omezit, které konkrétní možnosti jsou k dispozici v rozevíracím seznamu. Každá možnost může být omezena na konkrétní rozsah dat a / nebo organizačních jednotek a tato možnost se nezobrazí, pokud jsou data pořizována mimo tyto data nebo organizační jednotky. | ![](resources/images/../../admin/icon-complete.png) |  |
| Vyplňte příjemce oznámení | Odešle zprávu DHIS2 vybrané skupině uživatelů, když je datový soubor označen jako „dokončen“. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Odeslat oznámení dokončujícímu uživateli | Odešle zprávu DHIS2 uživateli zadávajícímu data, když je soubor dat označen jako „dokončen“. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Všechna pole pro datové prvky jsou povinná | Pokud se k rozčlenění datového prvku používá jedna nebo více kategorií, toto nastavení donutí uživatele buď dokončit všechna členění, nebo je nechat všechny prázdné. | ![](resources/images/../../admin/icon-complete.png) |  |
| Vyplňte, pouze pokud ověření proběhne | Pouze umožňuje označit soubor dat jako úplný, pokud nejsou spuštěna žádná ověřovací pravidla. | ![](resources/images/../../admin/icon-complete.png) |  |
| Přeskočit offline | Vyžaduje, aby uživatel přidal „komentář“, pokud je hodnota ponechána prázdná (nebo nelze datovou sadu „dokončit“). Umožňuje pouze výběr datové sady pro zadávání dat při připojení k internetu (i když je tato položka jednou vybrána, může pokračovat offline). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Dekorace datových prvků | Zobrazuje popis datového prvku, když kurzor myši přejde přes název datového prvku. | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře sekcí - vykreslení sekcí jako záložek | Zobrazí každou část ve formuláři jako samostatnou kartu, místo všech společně na stejné stránce. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Sekce Formulářů - vykreslení nad sebou |  | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Datový prvek - CatCombos | Umožňuje automatické rozdělení jednotlivého datového prvku do jedné nebo více kategorií (např. Muž / žena i dítě / dospělý), přičemž pro každou z těchto členění jsou shromážděna samostatná pole / hodnoty. | ![](resources/images/../../admin/icon-complete.png) |  |
| Inline indikátory / součty sekcí formuláře | Umožňuje přepsat výchozí CatCombo pro každý datový prvek jiným CatCombo pouze pro tuto datovou sadu. | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře sekcí - vykreslení sekcí jako záložek | Přidání indikátorů do datových sad je zpřístupní pro použití ve formulářích oddílů a vlastních formulářích; do těchto formulářů lze také přidat součty řádků a / nebo sloupců. (Obě se zobrazují na obrazovce vedle buněk pro sběr dat a automaticky se aktualizují, když jsou zachyceny hodnoty.) | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Přiřazení organizační jednotky | Zajistí, aby byl datový soubor k dispozici pouze pro ty organizační jednotky, kterým byl přiřazen. | ![](resources/images/../../admin/icon-complete.png) |  |
| Povinné datové prvky | To umožňuje označení konkrétních datových prvků / CatCombos jako „povinných“, což znamená, že uživatelé musí zadat hodnotu (nesmí být ponechána prázdná). | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře - výchozí formuláře | DHIS2 automaticky vykreslí formulář jako tabulku (tabulky), s novou tabulkou spuštěnou pokaždé, když se změní kombinace kategorií (= různé záhlaví sloupců). | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře - formuláře sekce | Lze zadat části formuláře a názvy oddílů, což vám dává větší kontrolu nad seskupením a rozložením formuláře (ale stále se vykresluje automaticky). Tento formulář sekce automaticky přepíše výchozí formulář, pokud je implementován. | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře - vlastní formuláře | Lze navrhnout vlastní formulář HTML, který poskytuje úplnou kontrolu nad rozvržením a umožňuje zahrnutí kódu JavaScript do formuláře. Pokud je implementován, tento vlastní formulář automaticky přepíše výchozí a oddílové formuláře. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Formuláře sekce - deaktivace polí (šedá) | U formulářů oddílů to umožňuje jednotlivě 'vyšednout' pole (celý datový prvek nebo konkrétní možnosti CatCombo), aby do něj uživatelé nemohli zadávat data. | ![](resources/images/../../admin/icon-complete.png) |  |
| Formuláře jednotek pro více organizací | Když je toto nastavení serveru povoleno, rozvržení formulářů se změní tak, aby zobrazovaly více organizačních jednotek jako řádky a všechny datové prvky / CatCombos jako sloupce (tj. Velmi plochý a široký formulář na organizační jednotku). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Vyskakovací okno s datovou hodnotou: označte hodnotu pro následnou kontrolu | Umožňuje uživateli označit tuto konkrétní hodnotu dat pro následnou kontrolu (označené hodnoty lze zkontrolovat ve webové aplikaci Data Quality). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Vyskakovací okno s datovou hodnotou: přidat komentář k hodnotě | Umožňuje uživateli přidat komentář k této konkrétní datové hodnotě. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Vyskakovací okno s hodnotou dat: zobrazení historie datových prvků | Zobrazuje historii tohoto konkrétního datového prvku v čase (tj. hodnoty předchozích 12 měsíců). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Vyskakovací okno s hodnotami dat: zobrazení audit trail | Zobrazuje historii předchozích úprav této konkrétní hodnoty dat. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Vyskakovací okno s hodnotami dat: minimální / maximální rozsahy (dostupné také prostřednictvím aplikace Data Administration) | To umožňuje uživatelům nastavit minimální a maximální očekávané hodnoty pro datový prvek, což umožňuje DHIS2 zvýrazňovat hodnoty mimo tento rozsah během zadávání dat (ale nebrání to uložení nebo „dokončení“). Můžete nastavit minimální / maximální rozsahy automaticky / hromadně (prostřednictvím aplikace Data Administration) nebo ručně / jednotlivě (prostřednictvím aplikace Data Entry). | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Tisknout formulář / tisknout prázdný formulář | Umožňuje tisk formuláře pro zadávání dat, umožňující sběr dat na papír a zadávání dat později. | ![](resources/images/../../admin/icon-incomplete.png) |  |
| Uložit data | Data zadaná na obrazovku nebudou zachycena, dokud nebudou „uložena“ - do té doby jsou uchovávána pouze v paměti a jsou ztracena, pokud je vypnuto napájení atd. | ![](resources/images/../../admin/icon-complete.png) |  |
| Dokončená sada dat | To umožňuje uživateli označit vstup dat pro jednotku období / org / atd. Jako „kompletní“. Všimněte si, že to slouží pouze pro účely trasování a včasnosti zadávání dat a nezamkne sadu dat ani nezabrání dalším úpravám. | ![](resources/images/../../admin/icon-complete.png) |  |
| Datové prvky: pravidla ověřování | Umožňuje vytváření pravidel (na úrovni datových prvků) k vynucení kvality dat na základě porovnání různých hodnot / kolekcí hodnot. (Např. Počet pacientů viděných v měsíci musí být menší než počet návštěv za měsíc.) | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Může zachytit data | Umožňuje uživateli přidávat nové hodnoty, upravovat hodnoty a mazat hodnoty v datové sadě. | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Může zobrazit data | Umožňuje uživateli zobrazit hodnoty v datové sadě. | ![](resources/images/../../admin/icon-complete.png) |  |
| Úrovně sdílení dat / Žádný přístup | Uživatel nebude moci zobrazit datovou sadu. | ![](resources/images/../../admin/icon-complete.png) |  |
| Pracovní postup schválení dat | Pokud správce vybere předkonfigurovaný pracovní postup pro schvalování dat, použije se k vynucení kaskády „schválení“ nebo „přijetí a schválení“, která uživatelům umožní odhlásit se a uzamknout data. | ![](resources/images/../../admin/icon-complete.png) | Proces schvalování musí být proveden na webu. Po schválení sady dat již nebude možné data v aplikaci upravovat. |
| Chybějící hodnoty vyžadují komentář po dokončení | Chybějící hodnoty budou vyžadovat komentář, který odůvodní jejich nepřítomnost. | - |  |
