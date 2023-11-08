---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-the-maps-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Mapy { #using_maps }

## O aplikaci Mapy { #about_maps }

Aplikace Mapy je představena ve verzi 2.29 a slouží jako náhrada aplikace GIS. Nabízí intuitivnější a uživatelsky přívětivější rozhraní. Mapovací modul od verze 2.34 je založen na technologii WebGL, která dokáže zobrazit tisíce funkcí na mapě současně.

S aplikací Mapy můžete překrýt více vrstev a vybrat si mezi různými základními mapami. Můžete vytvářet tematické mapy oblastí a bodů, prohlížet zařízení na základě klasifikací a vizualizovat spádové oblasti pro každé zařízení. Můžete přidat štítky do oblastí a bodů a vyhledávat a filtrovat podle různých kritérií. Body můžete přesouvat a nastavovat polohy za chodu. Mapy lze uložit jako oblíbené a sdílet s ostatními uživateli a skupinami nebo stáhnout jako obrázek.

> **Poznámka**
>
> Chcete-li použít předdefinované legendy v aplikaci **Mapy**, musíte je nejprve vytvořit v aplikaci **Údržba**.

![](resources/images/maps/maps_main.png)

-   **Panel vrstev** na levé straně pracovního prostoru zobrazuje přehled vrstev pro aktuální mapu:

    -   V pořadí jak jsou vrstvy přidávány pomocí tlačítka **(+) Přidat vrstvu**, jsou uspořádány a spravovány na tomto panelu.

    -   Na panelu se vždy zobrazuje **základní mapa**. Výchozí základní mapa je OSM Light a je vybrána ve výchozím nastavení. OpenStreetMap Podrobně obsahuje další prvky mapy a názvy míst. K dispozici jsou 4 základní mapy z Bing Maps, které nahrazují Mapy Google poskytované v předchozích verzích. Bing Road a Bing Dark zobrazuje silnice, hranice a místa. Pokud jsou barvy na vrstvách mapy jasné, použijte tmavou verzi. Štítky Bing Aerial a Bing Aerial Labs jsou satelitní a podrobné letecké snímky. Přepínejte mezi nimi výběrem požadovaného obrázku.

    -   Malé tlačítko se šipkou vpravo od panelu vrstvy nahoře umožňuje panel skrýt nebo zobrazit.

<!-- konec seznamu -->

-   Tlačítko **Soubor** vlevo nahoře umožňuje otevírat a ukládat mapy:

    -   Nový

        vymaže všechny existující vrstvy mapy a vytvoří novou mapu.

    -   Otevřít

        zobrazí dialogové okno se seznamem existujících map, kde budou otevřeny, přejmenovány, sdíleny a odstraněny. _Název aktuální mapy je zobrazen v záhlaví nad tlačítkem Soubor_.

    -   Uložit

        uloží všechny změny na aktuální mapu.

    -   Uložit jako

        uloží aktuální mapu pod novým názvem.

    -   Přejmenovat

        umožňuje změnit název a / nebo popis aktuální mapy.

    -   Překládejte

        vám umožní přeložit název a / nebo popis aktuální mapy.

    -   Sdílet

        otevře dialog, kde lze aktuální mapu sdílet se všemi nebo se skupinou uživatelů.

    -   Získat odkaz

        poskytne přímý odkaz na aktuální mapu.

    -   Vymazat

        vymaže aktuální mapu.

<!-- konec seznamu -->

-   Tlačítko **Stáhnout** vedle tlačítka Soubor vám umožňuje stáhnout aktuální mapu jako obrázek PNG.

<!-- konec seznamu -->

-   Tlačítko **Interpretace** vpravo nahoře otevírá panel interpretací na pravé straně pracovního prostoru. Na tlačítko lze kliknout, pouze pokud je mapa uložena.

    -   **Podrobnosti mapy** zobrazuje informace o aktuální mapě.

    -   **Interpretace** vám umožňuje prohlížet, přidávat, upravovat a sdílet interpretace aktuální mapy.

<!-- konec seznamu -->

-   Tlačítka **+** a **-** na mapě umožňují přiblížit a oddálit mapu. Přiblížení kolečka myši je plynulé, což nám umožňuje dokonale přizpůsobit mapu vašemu obsahu.

-   Tlačítko **otočit mapu** (trojúhelníkové šipky) umožňuje otáčet a naklánět mapu a vylepšit tak zobrazení vašich dat. Stisknutím tlačítka (nebo ovládací klávesy na klávesnici) při pohybu myši změňte zobrazení mapy. Klepnutím na tlačítko znovu obnovíte zobrazení.

-   **Celá obrazovka** (čtyři šipky) umožňuje zobrazit mapu na celou obrazovku. Chcete-li ukončit celou obrazovku, klikněte znovu na tlačítko nebo na klávesu Escape na klávesnici.

*   **Přiblížit na obsah** (ohraničený symbol lupy) automaticky upraví úroveň přiblížení a polohu středu mapy tak, aby byla data na mapě zaostřena.

*   **Hledat** (symbol lupy) umožňuje vyhledávat a přeskakovat na místo na mapě.

*   Tlačítko **měřítko** umožňuje měřit vzdálenosti a oblasti na mapě.

*   Kliknutím pravým tlačítkem na mapu zobrazíte zeměpisnou délku a šířku daného místa.

**Základní mapy**

Vrstvy základní mapy jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

![](resources/images/maps/maps_basemap_card.png)

V horní části karty základní mapy zleva doprava jsou:

-   Název vybrané základní mapy

-   Symbol šipky pro sbalení a rozbalení karty základní mapy

Ve středu karty základní mapy je seznam dostupných základních map. Aktuální základní mapa je zvýrazněna.

Pod spodní částí karty základní mapy je:

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

## Vytvořte novou mapu { #using_maps_create_map }

1.  V nabídce **Aplikace** klikněte na **Mapy**. Otevře se okno **DHIS2 Mapy**.

2.  Klikněte na tlačítko (+) Přidat vrstvu vlevo nahoře. Zobrazí se dialogové okno pro výběr vrstvy:

    ![](resources/images/maps/maps_layer_selection.png)

3.  Vyberte vrstvu, kterou chcete přidat na aktuální mapu. Možnosti jsou:

    -   [Tematické](#using_maps_thematic_layer)

    -   [Události](#using_maps_event_layer)

    -   [Trasované entity](#using_maps_tracked_entity_layer)

    -   [Zařízení](#using_maps_facility_layer)

    -   [Hranice](#using_maps_boundary_layer)

    Kromě toho existuje několik vrstev poskytovaných aplikací Google Earth Engine a dalšími službami:

    -   Hustota obyvatel

    -   Nadmořská výška

    -   Teplota

    -   Srážky

    -   Zemský pokryv

    -   Noční světla

    _Překrytí štítky_ je [externí vrstva](#using_maps_external_map_layers) definovaná v aplikaci Údržba.

## Spravujte tematické vrstvy { #using_maps_thematic_layer }

_Tematické mapy_ představují prostorové variace geografických distribucí. Vyberte požadovanou kombinaci indikátoru / datového prvku, období a úrovně organizační jednotky. Pokud má vaše databáze souřadnice a agregované hodnoty dat pro tyto organizační jednotky, zobrazí se na mapě.

> **Poznámka**
>
> Musíte mít vygenerované analytické tabulky DHIS2, abyste měli k dispozici agregované hodnoty dat.

![](resources/images/maps/maps_thematic_mapping.png)

Tematické vrstvy jsou v panelu vrstev reprezentovány vrstvou _karty_, například:

V horní části tematické karty zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název a období spojené s vrstvou

-   Symbol šipky pro sbalení a rozbalení tematické karty

Uprostřed tematické karty je legenda označující rozsahy hodnot zobrazené na vrstvě.

Ve spodní části tematické karty zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte tematickou vrstvu { #create-a-thematic-layer }

Chcete-li vytvořit vrstvu události, vyberte **Thematic** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy Události.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_thematic_layer_dialog_DATA.png)

    -   Vyberte datový typ a poté vyberte skupinu a cílový prvek. Dostupná pole závisí na typu vybrané položky.

    -   Vyberte hodnotu z pole **Typ agregace**, aby se hodnoty dat zobrazily na mapě. Ve výchozím nastavení je vybrána možnost „Podle datového prvku“. Alternativní hodnoty jsou: Count; Průměrný; Součet; Standardní odchylka; Odchylka; Min; Max. Viz také [Agregační operátory](https://dhis2.github.io/dhis2-docs/master/en/user/html/ch10s05.html#d0e8082).

2.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_thematic_layer_dialog_PERIOD.png)

    -   vyberte časové období, během kterého jsou tematická data mapována. Můžete vybrat relativní nebo pevné období.

        -   Relativní období

            V poli **Typ období** vyberte **Relativní** a poté vyberte jedno z relativních období, například **Minulý rok** nebo **Posledních 12 měsíců**, v poli **Období**.

            **Výchozí relativní období pro analýzu** lze nastavit v aplikaci **Nastavení systému**.

            Pokud vyberete relativní období pokrývající více let / měsíců / týdnů / dnů, může být vrstva zobrazena jako

            -   Single (agregát)

                Zobrazit agregované hodnoty pro vybrané relativní období (výchozí).

            -   Časová osa

                Zahrnuje časovou osu, která vám umožní procházet obdobími. Na stejnou mapu lze přidat pouze jednu vrstvu časové osy.

            -   Rozdělit zobrazení mapy

                Zobrazit více map, které vám umožní porovnávat různá období vedle sebe. Podporováno pro relativní období s 12 nebo méně položkami. Nelze kombinovat s jinými typy vrstev.

        -   Pevné období

            V poli **Typ období** vyberte délku období a poté vyberte cíl v poli **Období**.

        -   Datum zahájení / ukončení

            V poli **Typ období** vyberte **Datum zahájení / ukončení** a vyplňte datum zahájení a datum ukončení.

3.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_thematic_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek, úrovně organizačních jednotek v hierarchii, skupiny organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

4.  Na kartě **FILTR**:

    ![](resources/images/maps/maps_thematic_layer_dialog_FILTER.png)

    -   Kliknutím na PŘIDAT FILTR a výběrem dostupné datové položky přidáte do sady dat nový filtr.

        -   V rozevíracím seznamu vyberte datovou dimenzi. Počet zobrazených kót můžete snížit pomocí vyhledávacího pole. Kliknutím na název vyberte dimenzi.

        -   Když je vybrána dimenze, dostanete druhou rozbalovací nabídku s položkami dimenze. Zaškrtněte položky, které chcete do filtru zahrnout.

        Lze přidat více filtrů. Filtr odstraníte kliknutím na tlačítko koše vpravo od filtru.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_thematic_layer_dialog_STYLE.png)

    -   Vyberte buď **Choropleth** nebo **Bublinové mapy**.

        -   Choropleth přiřadí barvu každému tvaru jednotky org podle hodnoty dat. Toto je doporučená technika, pokud jsou data normalizována (na obyvatele).

        -   Bublinová mapa zobrazí hodnoty dat jako proporcionální kruhy. Tuto techniku použijte, pokud data nejsou normalizována (absolutní čísla). Kruhy jsou umístěny ve středu každé organizační jednotky.

    -   Nastavte **Nízký poloměr** a **Vysoký poloměr** pro proporcionální kruhy nebo bodové vybavení. Kruhy budou škálovány mezi nízkým a vysokým poloměrem podle hodnoty dat. Poloměr musí být mezi 0 a 50 px.

    -   **Zobrazit štítky**: Umožňuje zobrazení názvů organizačních jednotek ve vrstvě. Zde lze upravit velikost, váhu, styl a barvu písma.

    -   **Zobrazit žádná data**: Ve výchozím nastavení se organizační jednotky s chybějícími datovými hodnotami na mapě nezobrazí. Toto políčko zaškrtněte, pokud je chcete ukázat s barvou. Kliknutím barvu změníte.

    -   Vyberte typ legendy:

        -   **Automatická barevná legenda**: aplikace pro vás vytvoří legendu podle toho, jakou metodu klasifikace, počet tříd a barevnou škálu vyberete. Nastavte **Klasifikace** buď:

            -   Stejné intervaly

                rozsah každého intervalu bude (nejvyšší hodnota dat - nejnižší hodnota dat / počet tříd)

            -   Stejné počty

                tvůrce legendy se pokusí rozdělit organizační jednotky rovnoměrně.

        -   **Předdefinovaná barevná legenda**: Vyberte mezi předdefinovanými legendami.

        -   **Jednobarevná legenda**: Vyberte barvu bublin nebo kruhů. K dispozici pouze pro bublinové mapy.

6.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte tematickou vrstvu { #modify-a-thematic-layer }

1.  Na panelu vrstev klikněte na ikonu úpravy (tužka) na kartě tematické vrstvy.

2.  Podle potřeby upravte nastavení na libovolné kartě.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty v tematické vrstvě { #filter-values-in-a-thematic-layer }

Tematické vrstvy mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě tematické vrstvy.

![](resources/images/maps/maps_thematic_layer_data_table.png)

Tabulka dat zobrazuje data tvořící tematickou vrstvu.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   HODNOTA

        filtruje hodnoty podle zadaných čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   LEGENDA

        filtrovat podle legendy obsahující daný text

    -   ROZSAH

        filtrovat podle rozsahů obsahujících daný text

    -   ÚROVEŇ

        úroveň filtru podle čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   NADŘAZENÉ

        filtrovat podle nadřazených názvů obsahujících daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

    -   BARVA

        filtruje podle barevných názvů obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte organizační jednotku { #search-for-an-organisation-unit }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých organizačních jednotek.

### Procházejte mezi hierarchiemi organizace { #navigate-between-organisation-hierarchies }

Pokud jsou na mapě viditelné organizační jednotky, můžete v hierarchii snadno procházet nahoru a dolů bez použití uživatelského rozhraní úrovně / nadřazené.

1.  Klepněte pravým tlačítkem na jednu z organizačních jednotek.

2.  Vyberte **Přejít výš o jednu úroveň** nebo **Přejít níž o jednu úroveň**.

    Možnost rozbalení je zakázána, pokud jste na nejnižší úrovni nebo pokud na níže uvedené úrovni nejsou k dispozici žádné souřadnice. Podobně je na nejvyšší úrovni zakázána možnost procházení.

### Odstraňte tematickou vrstvu { #remove-thematic-layer }

Chcete-li vymazat všechna data v tematické vrstvě:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy událostí { #using_maps_event_layer }

Vrstva událostí zobrazuje geografické umístění událostí registrovaných ve sledovači DHIS2. Za předpokladu, že události mají přidružené souřadnice bodu nebo mnohoúhelníku, můžete pomocí této vrstvy přejít z agregovaných dat zobrazených v tematických vrstvách na jednotlivé jednotlivé události nebo případy.

Můžete také zobrazit agregované události v objektu nebo na hranici. Děláte to prostřednictvím tematické vrstvy pomocí datových položek událostí. To je užitečné, pokud máte pouze souřadnice pro organizační jednotku, pod kterou jsou události zaznamenávány.

![](resources/images/maps/maps_event_layer.png)

Vrstvy událostí jsou reprezentovány vrstvou _cards_ v panelu vrstev, například:

V horní části karty události zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název a období spojené s vrstvou

-   Symbol šipky pro sbalení a rozbalení karty události

Uprostřed karty události je legenda označující styl vrstvy.

Ve spodní části karty události zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu události { #maps_create_event_layer }

Chcete-li vytvořit vrstvu událostí, vyberte **Události** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy Události.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_event_layer_dialog_DATA.png)

    -   Vyberte program a poté vyberte fázi programu. Pole **Fáze** se zobrazí pouze po výběru programu.

        Pokud je pro vybraný program k dispozici pouze jeden stupeň, stupeň se automaticky vybere.

    -   Vyberte hodnotu v **souřadnicovém poli** pro polohy zobrazené na mapě. Ve výchozím nastavení je vybrána možnost „Umístění události“. V závislosti na datových prvcích nebo atributech, které patří k programu, jsou k dispozici další souřadnice, například „Pozice domácnosti“.

    -   Ve výchozím nastavení jsou všechny události se souřadnicemi zobrazeny na mapě. Pomocí pole **Stav události** můžete zobrazit pouze události, které mají jeden stav: Aktivní, Dokončeno, Naplánováno, Zpožděno nebo Přeskočeno.

2.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_event_layer_dialog_PERIOD.png)

    -   vyberte časové rozpětí, kdy došlo k událostem. Můžete vybrat pevné období nebo relativní období.

        -   Relativní období

            V poli **Období** vyberte jedno z relativních období, například **Tento měsíc** nebo **Minulý rok**.

            **Výchozí relativní období pro analýzu** lze nastavit v aplikaci **Nastavení systému**.

        -   Pevné období

            V poli **Období** vyberte **Datum zahájení / ukončení** a vyplňte datum zahájení a datum ukončení.

3.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_event_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

4.  Na kartě **FILTR**:

    ![](resources/images/maps/maps_event_layer_dialog_FILTER.png)

    -   Kliknutím na PŘIDAT FILTR a výběrem dostupné datové položky přidáte do sady dat nový filtr.

        -   U datové položky typu _sada možností_ můžete vybrat libovolnou z možností z rozevíracího seznamu pomocí šipky dolů nebo začátkem psaní přímo do pole pro filtrování možností.

        -   U datové položky typu _číslo_ můžete vybrat operátory jako rovná se, nerovná se, větší nebo menší než.

        -   U datové položky typu _boolean_ (ano / ne) můžete zaškrtnout políčko, pokud má být podmínka platná nebo pravdivá.

        -   Pro datovou položku typu _text_ získáte dvě možnosti: **Obsahuje** znamená, že dotaz bude odpovídat všem hodnotám, které obsahují vaši vyhledávací hodnotu, a **Je přesný** znamená, že pouze hodnoty, které jsou zcela identické s vaším vyhledávacím dotazem bude vrácena.

        Lze přidat více filtrů. Filtr odstraníte kliknutím na tlačítko koše vpravo od filtru.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_event_layer_dialog_STYLE.png)

    -   Vyberte **Seskupit události** pro seskupení blízkých událostí (klastr) nebo **Zobrazit všechny události** pro samostatné zobrazení událostí.

    -   Vyberte **barvu** pro událost nebo body klastru.

    -   Vyberte **okruh** (mezi 1 a 20) pro události.

    -   Vyberte **Zobrazit vyrovnávací paměť**, chcete-li zobrazit vizuální vyrovnávací paměť kolem každé události. Zde lze upravit poloměr vyrovnávací paměti. Tato možnost je k dispozici, pouze pokud vyberete **Zobrazit všechny události** výše.

    -   Vyberte **Styl podle datového prvku**, aby se události vybarvily podle hodnoty dat. Pokud také zvolíte seskupení událostí, budou se příchutě zobrazovat jako malé koblihové grafy ukazující distribuci hodnot dat. Možnosti se u různých datových typů liší:

        -   **Sady možností**: Vyberte barvu pro každou možnost v sadě možností. V aplikaci Údržba můžete nastavit výchozí barvy možnosti.

        -   **Čísla**: Numerický datový prvek můžete stylovat [stejným způsobem jako tematické vrstvy](#using_maps_thematic_layer_style) pomocí automatických nebo předdefinovaných legend.

        -   **Booleans**: Vyberte barvu pro true / yes a jinou pro false / no.

6.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte vrstvu události { #modify-an-event-layer }

1.  V panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy událostí.

2.  Podle potřeby upravte nastavení na kartách DATA, OBDOBÍ, FILTR, ORG JEDNOTKA a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Výpis a filtrování událostí { #listing-and-filtering-events }

Vrstvy událostí mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy událostí.

![](resources/images/maps/maps_event_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu událostí.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   ID

        filtrovat podle ID událostí obsahujících daný text

    -   ORG JEDNOTKA

        filtrovat podle názvu organizační jednotky obsahující daný text

    -   UDÁLOST

        filtrovat podle času události obsahujícího daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

    -   **Styl podle datového prvku**: Pokud jsou události stylizovány datovým prvkem (např. Pohlaví), lze filtrovat jak datovou hodnotu, tak barvu.

    -   **Zobrazit ve zprávách**: Datové prvky, u kterých je zaškrtnuto zobrazení ve zprávách, se zobrazí v samostatných sloupcích (viz níže, jak se přidávají).

    -   Hodnoty číselných dat lze filtrovat podle daných čísel a / nebo rozsahů, například: 2,\>3&\<8

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Upravit informace v tabulce dat událostí a vyskakovacích oknech { #modify-information-in-event-data-table-and-popups }

Informace zobrazené ve vyskakovacím okně události můžete upravit.

![](resources/images/maps/maps_eventlayer_eventinfopopup.png)

1.  Otevřete aplikaci **Údržba**.

2.  Vyberte **Program**.

3.  Klikněte na program, který chcete upravit, a vyberte **2 Přiřadit datové prvky**.

4.  U každého datového prvku, který chcete zobrazit ve vyskakovacím okně, vyberte odpovídající **Zobrazit ve zprávách**.

5.  Klikněte **Uložit**.

### Stáhněte si nezpracovaná data vrstvy událostí { #download-raw-event-layer-data }

Nezpracovaná data pro vrstvy událostí lze stáhnout ve formátu GeoJSON pro pokročilejší geoanalýzu a zpracování v desktopovém GIS softwaru, jako je [QGIS](https://www.qgis.org/). Stažená data zahrnují všechny jednotlivé události jako funkce GeoJSON, včetně atributů pro každý datový prvek vybraný pro **Zobrazit v přehledech**.

![](resources/images/maps/maps_data_download_dialog.png)

-   Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Stáhnout data**

-   Vyberte **ID format**, který se má použít jako klíč pro hodnoty datových prvků ve staženém souboru GeoJSON. K dispozici jsou tři možnosti:

    -   **ID** - Použijte jedinečné ID datového prvku
    -   **Název** - Použijte lidsky čitelný Název datového prvku (přeložený)
    -   **Kód** - Použijte kód datového prvku

-   Vyberte, zda **Použít čitelné klíče** pro další atributy Události, jako je fáze programu, zeměpisná šířka, délka, data události a ID organizační jednotky, název a kód. Pokud tato možnost **není** vybrána, tyto hodnoty budou ID vhodné pro počítač namísto názvu čitelného (a přeloženého) pro člověka.

-   Kliknutím na tlačítko **STÁHNOUT** vygenerujte a stáhněte soubor GeoJSON. Data budou vyžádána ze serveru DHIS2 a zpracována mapovou aplikací. Dokončení této operace může trvat několik minut.

-   Po stažení souboru GeoJSON jej lze importovat do většiny standardních softwarových aplikací GIS.

> Uvědomte si, že stažená data neobsahují informace o stylu, protože nejsou nativně podporována formátem GeoJSON. Styly lze volitelně znovu vytvořit v externích aplikacích GIS pomocí atributů každé funkce.

### Vymazat vrstvu událostí { #clear-event-layer }

Postup vymazání všech dat vrstvy událostí na mapě:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy sledovaných entit { #using_maps_tracked_entity_layer }

Vrstva trasovaných entit zobrazuje geografické umístění trasovaných entit registrovaných v DHIS2. Pokud trasované entity mají přidružené souřadnice bodu nebo mnohoúhelníku, můžete je prozkoumat na mapě.

![](resources/images/maps/maps_tracked_entity_layer.png)

Sledované vrstvy entit jsou reprezentovány kartami vrstev v panelu vrstev, například:

V horní části karty trasované entity zleva doprava jsou:

-   Pole pro uchopení myší umožňující přetahování a nové pořadí vrstev.

-   Název a období spojené s vrstvou.

-   Symbol šipky pro sbalení a rozbalení karty trasované entity.

Ve středu karty trasované entity je legenda označující stylování vrstvy.

Ve spodní části karty trasované entity zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu trasované entity { #maps_create_tracked_enity_layer }

Chcete-li vytvořit vrstvu trasované entity, vyberte **Sledované entity** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy trasované entity.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_DATA.png)

    -   Vyberte **Typ trasované entity**, který chcete zobrazit na mapě.

    -   Vyberte **Program**, kam trasované entity patří.

    -   Pomocí pole **Stav programu** vyberte stav registrace sledovaných entit, které chcete zahrnout: Všechny, Aktivní, Dokončeno nebo Zrušeno.

    -   Nastavte stav **Sledování** trasované entity pro daný program.

2.  Na kartě **Vztahy**

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_RELATIONSHIPS.png)

    > **Caution**
    >
    > Displaying tracked entity relationships in Maps is an experimental feature

    -   Pokud byl zároveň vybrán typ trasované entity, můžete zaškrtnout políčko **Zobrazit vztahy trasované entity**

    -   Po zaškrtnutí můžete z rozevíracího seznamu vybrat typ vztahu, který se má zobrazit na mapě. K dispozici jsou pouze vztahy FROM vybraného typu trasované entity.

3.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_PERIOD.png)

    -   Pokud není vybrán žádný program, můžete nastavit počáteční a konečné datum, kdy byly trasované entity naposledy aktualizovány.

    -   Pokud je vybrán program, můžete nastavit období, kdy byly trasované entity naposledy aktualizovány nebo kdy byly zaregistrovány nebo zapsány do programu.

4.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Máte 3 režimy výběru:

        -   **Pouze vybrané**: Zahrnout pouze trasované entity patřící k vybraným organizačním jednotkám.

        -   **Vybrané a níže**: Zahrnuty trasované entity ve vybraných organizačních jednotkách a další přímo pod nimi.

        -   **Vybrané a všechny níže**: Zahrnuty trasované entity a všechny níže vybrané organizační jednotky.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_STYLE.png)

    -   Vyberte **barvu** pro body a polygony trasované entity.

    -   Vyberte **velikost bodu** (poloměr mezi 1 a 20) pro body.

    -   Vyberte **Zobrazit vyrovnávací paměť**, chcete-li zobrazit vizuální vyrovnávací paměť kolem každé trasované entity. Zde lze upravit vzdálenost vyrovnávací paměti v metrech.

    -   Pokud byl na kartě relací vybrán typ vztahu, můžete pro vztahy a související trasované entity vybrat **barvu**, **velikost bodu** a **barvu čáry**

6.  Klikněte na **PŘIDAT / AKTUALIZOVAT VRSTVU**.

### Upravte vrstvu trasované entity { #modify-a-tracked-entity-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy trasované entity.

2.  Podle potřeby upravte nastavení na kartách DATA, OBDOBÍ, ORGANIZAČNÍ JEDNOTKA a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Vymazat vrstvu trasované entity { #clear-a-tracked-entity-layer }

Postup vymazání vrstvy trasované entity z mapy:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy zařízení { #using_maps_facility_layer }

Vrstva zařízení zobrazuje ikony, které představují typy zařízení. Polygony se nezobrazují na mapě, takže se ujistěte, že jste vybrali úroveň organizační jednotky, která má zařízení.

_Polygon je uzavřená oblast na mapě představující zemi, okres nebo park._

![](resources/images/maps/maps_facility_layer.png)

Vrstvy zařízení jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

V horní části karty zařízení zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název **Zařízení**

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Symbol šipky pro sbalení a rozbalení karty zařízení

Uprostřed karty zařízení je legenda označující zastoupení skupiny.

Ve spodní části karty zařízení zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu zařízení { #create-a-facility-layer }

Chcete-li vytvořit vrstvu zařízení, vyberte **Zařízení** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy zařízení.

1.  Na kartě **NASTAVENÍ SKUPIN**:

    ![](resources/images/maps/maps_facility_layer_dialog_GROUPSET.png)

    -   Vyberte ** Skupinovou sadu ** ze seznamu sad skupin organizačních jednotek definovaných pro vaši instanci DHIS2.

2.  Na kartě **ORGANIZAČNÍ JEDNOTKY**

    ![](resources/images/maps/maps_facility_layer_dialog_ORG_UNITS.png)

    -   vyberte úroveň (úrovně) organizační jednotky nebo skupiny (skupin) z polí pro výběr na pravé straně.

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

3.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_facility_layer_dialog_STYLE.png)

    -   vyberte jakýkoli styl, který chcete použít na zařízení.

        -   Zobrazit štítky

            Umožňuje zobrazit štítky na vrstvě. Zde lze upravit velikost, řez a barvu písma.

        -   Zobrazit vyrovnávací paměť

            Umožňuje zobrazit vizuální vyrovnávací paměť na vrstvě kolem každého zařízení. Zde lze upravit poloměr vyrovnávací paměti.

4.  Klikněte na **PŘIDAT VRSTVU**.

### Vytvořte nebo upravte vrstvu zařízení { #create-or-modify-a-facility-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy zařízení.

2.  Podle potřeby upravte nastavení na kartách NASTAVENÍ SKUPIN, ORGANIZAČNÍ JEDNOTKY a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty ve vrstvě zařízení { #filter-values-in-a-facility-layer }

Vrstvy zařízení mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy zařízení.

![](resources/images/maps/maps_facility_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu zařízení.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte zařízení { #search-for-a-facility }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých zařízení.

### Odstraňte vrstvu zařízení { #remove-facility-layer }

Chcete-li vymazat všechna data ve vrstvě zařízení:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

### Spravujte zařízení ve vrstvě { #manage-facilities-in-a-layer }

Můžete mít zařízení ve vrstvách **Zařízení**, **Hranice** a **Tematické**.

#### Přemístěte zařízení { #relocate-a-facility }

1.  Klikněte pravým tlačítkem na zařízení a klikněte na **Přemístit**.

2.  Umístěte kurzor na nové místo.

    Nová souřadnice je uložena trvale. To nelze vrátit zpět.

#### Přehodit zeměpisnou délku a šířku zařízení { #swap-longitude-and-latitude-of-a-facility }

1.  Klikněte pravým tlačítkem na zařízení a klikněte na **Prohodit zeměpisnou délku / šířku**.

    To je užitečné, pokud uživatel při vytváření organizační jednotky převrátil souřadnice zeměpisné šířky a délky.

#### Zobrazit informace o zařízení { #display-facility-information }

Informace o organizační jednotce nastavené správcem můžete zobrazit takto:

<table>
<caption>Zobrazit informace o organizační jednotce</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>Funkce</th>
<th>Akce</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Zobrazit informace pro aktuální období</p></td>
<td><ol type="1">
<li><p>Klikněte na zařízení.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><p>Zobrazit informace za vybrané období</p></td>
<td><ol type="1">
<li><p>Klikněte pravým tlačítkem na zařízení a klikněte na <strong>Zobrazit informace</strong>.</p></li>
<li><p>V sekci <strong>Infrastrukturní data</strong>, vyberte období.</p></li>
</ol>
<blockquote>
<p><strong>Poznámka</strong></p>
<p>Nakonfigurujete zobrazená data infrastruktury v aplikaci <strong>Systémové Nastavení</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Spravujte vrstvy hranic { #using_maps_boundary_layer }

Vrstva hranic zobrazuje hranice a umístění vašich organizačních jednotek. Tato vrstva je zvláště užitečná, pokud jste offline a nemáte přístup k mapám na pozadí.

![](resources/images/maps/maps_bound_layers.png)

Vrstvy hranic jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

V horní části karty hranic zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název **Hranice**

-   Symbol šipky pro sbalení a rozšíření hraniční karty

Pod spodní hraniční kartou zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořit vrstvu hranic { #create-a-boundary-layer }

Chcete-li vytvořit vrstvu hranic, zvolte **Hranice** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy hranic.

1.  Na kartě **ORGANIZAČNÍ JEDNOTKY**

    ![](resources/images/maps/maps_boundary_layer_dialog_ORG_UNITS.png)

    -   vyberte úroveň (úrovně) organizační jednotky nebo skupiny (skupin) z polí pro výběr na pravé straně.

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

2.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_boundary_layer_dialog_STYLE.png)

    -   vyberte jakýkoli styl, který chcete použít na hranice.

        -   Zobrazit štítky

            Umožňuje zobrazit štítky na vrstvě. Zde lze upravit velikost a řez písma.

        -   Poloměr bodu

            Nastavte základní poloměr, když jsou na vrstvě hranic prezentovány prvky typu bodu, například zařízení.

3.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte vrstvu hranic { #modify-a-boundary-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy hranic.

2.  Podle potřeby upravte nastavení na kartách ORGANIZAČNÍ JEDNOTKY a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty ve vrstvě hranic { #filter-values-in-a-boundary-layer }

Vrstvy hranic mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy hranic.

![](resources/images/maps/maps_bound_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu hranic.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   ÚROVEŇ

        úroveň filtru podle čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   NADŘAZENÉ

        filtrovat podle nadřazených názvů obsahujících daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte organizační jednotku { #search-for-an-organisational-unit }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých organizačních jednotek zobrazených ve vrstvě hranic.

### Procházejte mezi hierarchiemi organizace { #navigate-between-organisation-hierarchies }

Můžete upravit cíl vrstvy hranic v hierarchii bez použití uživatelského rozhraní úrovně / nadřazené.

1.  Klepněte pravým tlačítkem na jednu z hranic.

2.  Vyberte **Přejít výš o jednu úroveň** nebo **Přejít níž o jednu úroveň**.

    Možnost procházení níže je vypnuta, pokud jste na nejnižší úrovni. Podobně je na nejvyšší úrovni vypnuta možnost procházení na vyšší úroveň.

### Odstranit vrstvu hranic { #remove-boundary-layer }

Chcete-li vymazat všechna data ve vrstvě hranic:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvu Earth Engine { #using_maps_gee }

![](resources/images/maps/maps_earth_eng_layer.png)

Vrstva Google Earth Engine vám umožňuje zobrazit satelitní snímky a geoprostorové datové sady z rozsáhlého katalogu Google. Tyto vrstvy jsou užitečné v kombinaci s tematickými vrstvami a vrstvami událostí pro vylepšení analýzy. Podporovány jsou následující vrstvy:

-   Odhady hustoty obyvatelstva s národními součty upravenými tak, aby odpovídaly odhadům populačního rozdělení OSN. Počet obyvatel v buňkách mřížky 100 x 100 m (od roku 2010).

-   Nadmořská výška. Můžete upravit minimální a maximální hodnoty tak, aby lépe reprezentovaly terén ve vašem regionu.

-   Teplota: Teploty povrchu země získané ze satelitu. V oblastech s přetrvávající oblačností se objeví prázdná místa.

-   Srážky shromážděné ze satelitů a meteorologických stanic na zemi. Hodnoty jsou v milimetrech během 5 dnů. Aktualizováno měsíčně, během 3. týdne následujícího měsíce.

-   Krajinná pokrývka: 17 odlišných typů krajinného pokryvu získaných ze satelitů.

-   Noční světla: Světla z měst, měst a dalších míst s trvalým osvětlením, včetně plynových světlic (od roku 2013).

### Vytvořte vrstvu Earth Engine { #create-an-earth-engine-layer }

Chcete-li vytvořit vrstvu Earth Engine, vyberte požadovanou vrstvu z výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy.

1.  Na kartě **STYL**

    ![](resources/images/maps/maps_ee_layer_dialog_POPULATION.png)

    -   Upravte parametry specifické pro typ vrstvy.

    -   Podle potřeby upravte rozsah legendy, kroky a barvy.

2.  Klikněte na **PŘIDAT VRSTVU**.

## Přidejte externí vrstvy mapy { #using_maps_external_map_layers }

Externí mapové vrstvy jsou reprezentovány buď:

-   Základní mapy

    Ty jsou k dispozici na kartě **základní mapy** v panelu vrstev a jsou vybrány jako všechny ostatní základní mapy.

-   Překryvné vrstvy

    Ty jsou k dispozici ve výběru **Přidat vrstvu**. Na rozdíl od základních map lze překryvy umístit nad nebo pod jakékoli jiné vrstvy překrytí.

Překryvné vrstvy jsou reprezentovány další vrstvou _karty_ v panelu vrstev, například:

V horní části karty překrytí zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název externí mapové vrstvy

-   Symbol šipky pro sbalení a rozbalení překryvné karty

Ve spodní části překryvné karty zleva doprava jsou:

-   Posuvník pro úpravu průhlednosti vrstvy

-   Ikona odstranění (koše) pro odstranění vrstvy z aktuální tematické mapy.

Zde je několik příkladů externích vrstev:

![](resources/images/maps/maps_black_basemap_and_nighttime_lights.png)

![](resources/images/maps/maps_terrain_imagery.png)

![](resources/images/maps/maps_aerial_imagery.png)

## Nabídka Soubor { #using_maps_file_menu }

Ke správě map použijte nabídku **Soubor**. Několik položek nabídky bude deaktivováno, dokud neotevřete nebo neuložíte mapu.

Uložení map usnadňuje jejich pozdější obnovení. Také vám dává příležitost sdílet je s ostatními uživateli jako výklad nebo je umístit na ovládací panel. Všechny typy konfigurací vrstev můžete uložit jako oblíbené.

### Vytvořte novou mapu { #create-a-new-map }

Klikněte na **Soubor** \> **Nový**.

NB\! Toto vymaže aktuální vrstvy mapy, které máte, bez uložení.

### Otevřete novou mapu { #open-a-new-map }

1.  Klikněte na **Soubor** \> **Otevřít**. Otevře se dialogové okno se seznamem map.

2.  Najděte oblíbenou položku, kterou chcete otevřít. Uloženou mapu můžete vyhledat pomocí \< a \> nebo vyhledávacího pole. Seznam je filtrován podle všech znaků, které zadáte. Seznam můžete filtrovat výběrem **Zobrazit vše**, **Vytvořeno mnou** nebo **Vytvořeno ostatními**.

3.  Klikněte na název mapy, kterou chcete otevřít.

### Uložte mapu { #save-a-map }

Když jste vytvořili mapu, je vhodné ji uložit pro pozdější použití:

1.  Klikněte na **Soubor** \> **Uložit**.

2.  Při prvním uložení mapy zadejte **název** (povinné) a **popis** (volitelné).

3.  Klikněte **ULOŽIT**.

### Uložení kopie mapy { #save-a-copy-of-a-map }

1.  Klikněte na **Soubor** \> **Uložit jako ...**

2.  Zadejte **Název** (povinné) a **Popis** (volitelné) pro mapu.

3.  Klikněte **ULOŽIT**.

### Přejmenujte mapu { #rename-a-map }

1.  Klikněte na **Soubor** \> **Přejmenovat**.

2.  Zadejte pro svou mapu nový **Název** nebo **Popis**.

3.  Klikněte na **PŘEJMENOVAT**. Mapa je aktualizována.

### Přeložit mapu { #translate-a-map }

1.  Klikněte na **Soubor** \> **Přeložit**.

2.  Vyberte **národní prostředí** (jazyk), který chcete přeložit.

3.  Zadejte přeložený **Název** a **Popis**. Původní text se zobrazí pod polem.

4.  Klikněte **ULOŽIT**.

### Upravte nastavení sdílení pro mapu { #modify-sharing-settings-for-a-map }

Jakmile mapu vytvoříte a uložíte, můžete mapu sdílet se všemi nebo se skupinou uživatelů. Úprava nastavení sdílení:

1.  Klikněte na **Soubor** \> **Sdílet**. Otevře se dialogové okno nastavení sdílení.

2.  V textovém poli vyhledejte jméno uživatele nebo skupiny, se kterou chcete sdílet své oblíbené, a vyberte jej.

    Vybraný uživatel nebo skupina se přidá do seznamu příjemců.

    Opakováním kroku přidejte další skupiny uživatelů.

3.  Chcete-li povolit externí přístup, zaškrtněte příslušné políčko.

4.  Pro každou skupinu uživatelů zvolte nastavení přístupu. Možnosti jsou:

    -   Žádné (pouze pro výchozí skupiny, protože je nelze odebrat)

    -   Může zobrazit

    -   Může upravovat a prohlížet

5.  Kliknutím na **ZAVŘÍT** dialog zavřete.

### Získejte odkaz na mapu { #get-the-link-to-a-map }

1.  Klikněte na **Soubor** \> **Získat odkaz**. Otevře se dialogové okno odkazu.

2.  Zkopírujte odkaz.

### Odstranění mapy { #delete-a-map }

1.  Klikněte na **Soubor** \> **Odstranit**. Zobrazí se potvrzovací dialog.

2.  Kliknutím na **ODSTRANIT** potvrďte, že chcete oblíbenou položku smazat. Vaše mapa je odstraněna a vrstvy jsou z pohledu vymazány.

## Interpretace map { #mapsInterpretation }

Interpretace je popis mapy v daném období. Tyto informace jsou viditelné v **aplikaci Ovládací panel**. Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací. Na tlačítko lze kliknout, pouze pokud je mapa uložena.

![](resources/images/maps/maps_interpretations_panel.png)

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací.

3.  Klikněte na interpretaci. Vaše mapa zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

### Napište interpretaci pro mapu { #write-interpretation-for-a-map }

Chcete-li vytvořit interpretaci, musíte nejprve vytvořit mapu a uložit ji. Pokud jste svou mapu sdíleli s jinými lidmi, interpretace, kterou napíšete, je viditelná pro tyto lidi.

1.  Otevřete oblíbené s interpretacemi.

2.  Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací.

3.  U uživatelů, kteří mají přístup k oblíbeným položkám se zobrazí textové pole se zástupným symbolem „Napsat interpretaci“.

4.  Do textového pole zadejte komentář, otázku nebo interpretaci. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s interpretací nebo komentářem. Interpretaci můžete vidět v **aplikaci Ovládací panel**.

5.  Pokud chcete, aby vaše interpretace měla stejné nastavení sdílení jako mapa, klikněte na **ULOŽIT**.

    Chcete-li pro svou interpretaci změnit nastavení sdílení (viz níže), klikněte na **ULOŽIT & SDÍLET**.

### Změňte nastavení sdílení pro interpretaci { #change-sharing-settings-for-an-interpretation }

1.  Klikněte na interpretaci (viz výše, jak zobrazit interpretaci).

2.  Klikněte na **Sdílet** pod interpretací. Otevře se dialogové okno nastavení sdílení.

3.  Vyhledejte a přidejte uživatele a skupiny uživatelů, se kterými chcete svou mapu sdílet.

4.  Změňte nastavení sdílení pro uživatele, které chcete upravit:

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádný přístup**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro veřejný přístup.

5.  Po aktualizaci nastavení sdílení klikněte na **ZAVŘÍT**.

## Uložte mapu jako obrázek { #using_maps_image_export }

Svou mapu si můžete stáhnout jako obrázek kliknutím na tlačítko Stáhnout v horní nabídce

![](resources/images/maps/maps_download.png)

Stahování map není podporováno v Internet Exploreru nebo Safari, doporučujeme použít Google Chrome nebo Firefox.

1.  Vyberte, zda chcete zahrnout název mapy nebo ne. Tato možnost je k dispozici, pouze pokud je mapa uložena.

2.  Vyberte, zda chcete zahrnout legendu mapy. Legendu můžete umístit do jednoho ze 4 rohů mapy.

3.  Kliknutím na **Stáhnout** si stáhnete mapu.

## Vyhledejte místo { #using_maps_search }

Funkce vyhledávání míst umožňuje vyhledávat téměř jakékoli místo nebo adresu. Tato funkce je užitečná k vyhledání například míst, zařízení, vesnic nebo měst na mapě.

![](resources/images/maps/maps_place_search.png)

1.  Na pravé straně okna Mapy klikněte na ikonu lupy.

2.  Zadejte hledané místo.

    Během psaní se zobrazí seznam shodných míst.

3.  Ze seznamu vyberte umístění. Špendlík označuje polohu na mapě.

## Změřte vzdálenosti a oblasti na mapě { #using_maps_measure_distance }

1.  V levé horní části mapy umístěte kurzor na ikonu **Měření vzdáleností a oblastí** (pravítko) a klikněte na **Vytvořit nové měření**.

2.  Přidejte na mapu body.

3.  Klikněte na **Dokončit měření**.

![](resources/images/maps/maps_measure_distance.png)

## Získejte zeměpisnou šířku a délku na jakémkoli místě { #using_maps_latitude_longitude }

Klikněte pravým tlačítkem na bod na mapě a vyberte **Zobrazit zeměpisnou délku / šířku**. Hodnoty se zobrazí ve vyskakovacím okně.

## Viz také { #see-also }

-   [Spravovat legendy](https://docs.dhis2.org/master/en/user/html/manage_legend.html)
