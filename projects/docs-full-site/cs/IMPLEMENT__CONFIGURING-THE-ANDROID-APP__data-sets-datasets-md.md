---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/edit/master/docs/src/commonmark/en/content/capture-app/programs-specific-features.md" 
---
# Datové sady  { #datasets } 

<!-- DHIS2-SECTION-ID:datasets -->

## Datové sady v Androidu { #datasets_android } 

<!-- DHIS2-SECTION-ID:datasets_android -->

### Přehledová obrazovka { #overview-screen } 

Nová karta Přehled obsahuje následující podrobnosti:

- Název datové sady
- Poslední aktualizace
- Stav otevření / zavření
- Období
- Organizační jednotka
- Kombinace možnosti kategorie

![](../content/capture-app/resources/images/image122.png){ width=25%}

#### Ukládání datové sady { #saving-a-data-set } 

Pravidla ověřování a dokončení datových sad jsou integrovány do akcí tlačítka Uložit:

- Když je datová sada nakonfigurována tak, aby se dokončila pouze v případě, že ověření platnosti projde. Pokud je ověření úspěšné, zobrazí se dialogové okno s požadavkem na označení jako dokončené. Aplikace umožní dokončení pouze v případě, že mají všechna povinná pole hodnotu.

![](../content/capture-app/resources/images/image131.png){ width=25%}

- pokud není úspěšný, měl by se zobrazit chybový dialog a datová sada nebude označena jako úplná. Zobrazí se popis a pokyny ověřovacího pravidla, které uživateli pomohou identifikovat chybu.

![](../content/capture-app/resources/images/image128.png){ width=25%}

- Na datové sadě, která nemá nastavení „Dokončení povoleno, pouze pokud proběhne ověření“. Při kliknutí na tlačítko uložit; pokud má datová sada přidružená ověřovací pravidla, aplikace požádá uživatele o spuštění ověřovacích pravidel.

![](../content/capture-app/resources/images/image130.png){ width=25%}

- Pokud ověření není úspěšné, měl by se zobrazit chybový dialog, ale s možností datový soubor přesto dokončit. Zobrazí se popis a pokyny ověřovacího pravidla, které uživateli pomohou identifikovat chybu.

![](../content/capture-app/resources/images/image129.png){ width=25%}

- Pokud datová sada nemá ověřovací pravidla, bude datová sada označena jako úplná, pokud mají všechna povinná pole hodnotu.

### Zvětšit záhlaví řádků { #datasets_android_increase } 

<!-- DHIS2-SECTION-ID:datasets_android_increase -->

Délka prvního sloupce v datových sadách se nyní vypočítá tak, aby zobrazoval celý text pro názvy datových prvků. Uživatelé mohou také upravit šířku, aby ji lépe přizpůsobili své velikosti obrazovky.

![](../content/capture-app/resources/images/image113.png){ width=25%}

## Přehled podporovaných funkcí { #datasets_supported } 

<!-- DHIS2-SECTION-ID:datasets_supported -->

Následuje úplný seznam všech funkcí dostupných pro datové sady v DHIS2 a poznámky o tom, zda byly, nebo nebyly implementovány v aplikaci Android Capture.

V poznámkách výraz „admin“ označuje někoho, kdo vyvíjí a konfiguruje systém DHIS2, a „user“ označuje někoho, kdo používá aplikace k pořizování dat, jejich aktualizaci a kontrole zpráv.

|Legenda|Popis|
|:--:|:------|
|![](../../../resources/images/admin/icon-complete.png)|Funkce implementována|
|![](../../../resources/images/admin/icon-incomplete.png)|Funkce není implementována&nbsp; (bude ignorována)|
|![](../../../resources/images/admin/icon-na.png)|Nelze použít|
|![](../../../resources/images/admin/icon-wip.png)|Ve vývoji. Funkce ještě není zcela implementována nebo již bylo hlášeno neočekávané chování.|


|Funkce|Popis funkce|Status|Poznámky k provádění|
|-|---|:-:|---|
|Typ období|Určuje období pokryté zadáváním údajů.|![](../../../resources/images/admin/icon-complete.png) | |
|Konec platnosti|Nastavuje termín (dny po období), po kterém DHIS2 uzamkne veškeré zadávání dat pro období (0 znamená, že nebudou vůbec zamknuty). Období lze stále otevírat, ale buňky budou zašedlé.| ![](../../../resources/images/admin/icon-complete.png) | |
|Otevřete budoucí období pro zadávání údajů|Toto nastavení lze použít k odemčení aktuálního období nebo všech období do určitého bodu v budoucnosti.|![](../../../resources/images/admin/icon-complete.png) | |
|Období zadávání dat|Umožňuje nastavit konkrétní rozsah dat pro zadávání dat období a zabrání shromažďování dat pro období mimo toto období.|![](../../../resources/images/admin/icon-complete.png) | |
|Dny po období, aby bylo možné se včas přihlásit|Nastavuje termín (dny po období), po kterém DHIS2 považuje zadávání dat za „pozdě“.| ![](../../../resources/images/admin/icon-complete.png)| |
|Kombinace kategorie [Atribut]|Umožňuje správci připojit kategorii (sadu možností) k datové sadě a vygenerovat pro každou možnost samostatnou obrazovku pro zadávání dat (v DHIS2 se tomu říká kombinace kategorie atributů).| ![](../../../resources/images/admin/icon-complete.png)| |
|[Atribut] Omezení možností kombinace kategorií|Pokud se používají kombinace kategorií atributů (viz výše), pak tato funkce dává správcům možnost omezit, které konkrétní možnosti jsou k dispozici v rozevíracím seznamu. Každá možnost může být omezena na konkrétní rozsah dat a / nebo organizačních jednotek a tato možnost se nezobrazí, pokud jsou data pořizována mimo tyto data nebo organizační jednotky.| ![](../../../resources/images/admin/icon-complete.png)| [ANDROAPP-1153](https:/jira.dhis2.org/browse/ANDROAPP-1153) Omezení je možné pouze pomocí datumu.|
|Vyplňte příjemce oznámení|Odešle zprávu DHIS2 vybrané skupině uživatelů, když je datový soubor označen jako „dokončen“.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Odeslat oznámení dokončujícímu uživateli|Odešle zprávu DHIS2 uživateli zadávajícímu data, když je soubor dat označen jako „dokončen“.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Všechna pole pro datové prvky jsou povinná|Pokud se k rozčlenění datového prvku používá jedna nebo více kategorií, toto nastavení donutí uživatele buď dokončit všechna členění, nebo je nechat všechny prázdné.|![](../../../resources/images/admin/icon-complete.png) | |
|Vyplňte, pouze pokud ověření proběhne|Pouze umožňuje označit soubor dat jako úplný, pokud nejsou spuštěna žádná ověřovací pravidla.|![](../../../resources/images/admin/icon-complete.png)| |
|Přeskočit offline|Vyžaduje, aby uživatel přidal „komentář“, pokud je hodnota ponechána prázdná (nebo nelze datovou sadu „dokončit“). Umožňuje pouze výběr datové sady pro zadávání dat při připojení k internetu (i když je tato položka jednou vybrána, může pokračovat offline).|![](../../../resources/images/admin/icon-incomplete.png)| |
|Dekorace datových prvků|Zobrazuje popis datového prvku, když kurzor myši přejde přes název datového prvku.|![](../../../resources/images/admin/icon-complete.png) | |
|Formuláře sekcí - vykreslení sekcí jako záložek|Zobrazí každou část ve formuláři jako samostatnou kartu, místo všech společně na stejné stránce.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Sekce Formulářů - vykreslení nad sebou||![](../../../resources/images/admin/icon-incomplete.png)| |
|Datový prvek - CatCombos|Umožňuje automatické rozdělení jednotlivého datového prvku do jedné nebo více kategorií (např. Muž / žena i dítě / dospělý), přičemž pro každou z těchto členění jsou shromážděna samostatná pole / hodnoty.|![](../../../resources/images/admin/icon-complete.png)| |
|Inline indikátory / součty sekcí formuláře|Umožňuje přepsat výchozí CatCombo pro každý datový prvek jiným CatCombo pouze pro tuto datovou sadu.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Formuláře sekcí - vykreslení sekcí jako záložek|Přidání indikátorů do datových sad je zpřístupní pro použití ve formulářích oddílů a vlastních formulářích; do těchto formulářů lze také přidat součty řádků a / nebo sloupců. (Obě se zobrazují na obrazovce vedle buněk pro sběr dat a automaticky se aktualizují, když jsou zachyceny hodnoty.)|![](../../../resources/images/admin/icon-incomplete.png)| |
|Přiřazení organizační jednotky|Zajistí, aby byl datový soubor k dispozici pouze pro ty organizační jednotky, kterým byl přiřazen.|![](../../../resources/images/admin/icon-complete.png) | |
|Povinné datové prvky|To umožňuje označení konkrétních datových prvků / CatCombos jako „povinných“, což znamená, že uživatelé musí zadat hodnotu (nesmí být ponechána prázdná).| ![](../../../resources/images/admin/icon-complete.png)| |
|Formuláře - výchozí formuláře|DHIS2 automaticky vykreslí formulář jako tabulku (tabulky), s novou tabulkou spuštěnou pokaždé, když se změní kombinace kategorií (= různé záhlaví sloupců).|![](../../../resources/images/admin/icon-complete.png) | |
|Formuláře - formuláře sekce|Lze zadat části formuláře a názvy oddílů, což vám dává větší kontrolu nad seskupením a rozložením formuláře (ale stále se vykresluje automaticky). Tento formulář sekce automaticky přepíše výchozí formulář, pokud je implementován.|![](../../../resources/images/admin/icon-complete.png) | |
|Formuláře - vlastní formuláře|Lze navrhnout vlastní formulář HTML, který poskytuje úplnou kontrolu nad rozvržením a umožňuje zahrnutí kódu JavaScript do formuláře. Pokud je implementován, tento vlastní formulář automaticky přepíše výchozí a oddílové formuláře.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Formuláře sekce - deaktivace polí (šedá)|U formulářů oddílů to umožňuje jednotlivě 'vyšednout' pole (celý datový prvek nebo konkrétní možnosti CatCombo), aby do něj uživatelé nemohli zadávat data.|![](../../../resources/images/admin/icon-complete.png) | |
|Formuláře jednotek pro více organizací|Když je toto nastavení serveru povoleno, rozvržení formulářů se změní tak, aby zobrazovaly více organizačních jednotek jako řádky a všechny datové prvky / CatCombos jako sloupce (tj. Velmi plochý a široký formulář na organizační jednotku).|![](../../../resources/images/admin/icon-incomplete.png)| |
|Vyskakovací okno s datovou hodnotou: označte hodnotu pro následnou kontrolu|Umožňuje uživateli označit tuto konkrétní hodnotu dat pro následnou kontrolu (označené hodnoty lze zkontrolovat ve webové aplikaci Data Quality).|![](../../../resources/images/admin/icon-incomplete.png)| |
|Vyskakovací okno s datovou hodnotou: přidat komentář k hodnotě|Umožňuje uživateli přidat komentář k této konkrétní datové hodnotě.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Vyskakovací okno s hodnotou dat: zobrazení historie datových prvků|Zobrazuje historii tohoto konkrétního datového prvku v čase (tj. hodnoty předchozích 12 měsíců).|![](../../../resources/images/admin/icon-incomplete.png)| |
|Vyskakovací okno s hodnotami dat: zobrazení audit trail|Zobrazuje historii předchozích úprav této konkrétní hodnoty dat.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Vyskakovací okno s hodnotami dat: minimální / maximální rozsahy (dostupné také prostřednictvím aplikace Data Administration)|To umožňuje uživatelům nastavit minimální a maximální očekávané hodnoty pro datový prvek, což umožňuje DHIS2 zvýrazňovat hodnoty mimo tento rozsah během zadávání dat (ale nebrání to uložení nebo „dokončení“). Můžete nastavit minimální / maximální rozsahy automaticky / hromadně (prostřednictvím aplikace Data Administration) nebo ručně / jednotlivě (prostřednictvím aplikace Data Entry).|![](../../../resources/images/admin/icon-incomplete.png)| |
|Tisknout formulář / tisknout prázdný formulář|Umožňuje tisk formuláře pro zadávání dat, umožňující sběr dat na papír a zadávání dat později.|![](../../../resources/images/admin/icon-incomplete.png)| |
|Uložit data|Data zadaná na obrazovku nebudou zachycena, dokud nebudou „uložena“ - do té doby jsou uchovávána pouze v paměti a jsou ztracena, pokud je vypnuto napájení atd.|![](../../../resources/images/admin/icon-complete.png)| |
|Dokončená sada dat|To umožňuje uživateli označit vstup dat pro jednotku období / org / atd. Jako „kompletní“. Všimněte si, že to slouží pouze pro účely trasování a včasnosti zadávání dat a nezamkne sadu dat ani nezabrání dalším úpravám.|![](../../../resources/images/admin/icon-complete.png)| |
|Datové prvky: pravidla ověřování|Umožňuje vytváření pravidel (na úrovni datových prvků) k vynucení kvality dat na základě porovnání různých hodnot / kolekcí hodnot. (Např. Počet pacientů viděných v měsíci musí být menší než počet návštěv za měsíc.)|![](../../../resources/images/admin/icon-complete.png)| |
|Úrovně sdílení dat / Může zachytit data|Umožňuje uživateli přidávat nové hodnoty, upravovat hodnoty a mazat hodnoty v datové sadě.|![](../../../resources/images/admin/icon-complete.png) | |
|Úrovně sdílení dat / Může zobrazit data|Umožňuje uživateli zobrazit hodnoty v datové sadě.|![](../../../resources/images/admin/icon-complete.png) | |
|Úrovně sdílení dat / Žádný přístup|Uživatel nebude moci zobrazit datovou sadu.|![](../../../resources/images/admin/icon-complete.png) | |
|Pracovní postup schválení dat|Pokud správce vybere předkonfigurovaný pracovní postup pro schvalování dat, použije se k vynucení kaskády „schválení“ nebo „přijetí a schválení“, která uživatelům umožní odhlásit se a uzamknout data.|![](../../../resources/images/admin/icon-complete.png) | Proces schvalování musí být proveden na webu. Po schválení sady dat již nebude možné data v aplikaci upravovat. |
|Chybějící hodnoty vyžadují komentář po dokončení|Chybějící hodnoty budou vyžadovat komentář, který odůvodní jejich nepřítomnost.|-||


