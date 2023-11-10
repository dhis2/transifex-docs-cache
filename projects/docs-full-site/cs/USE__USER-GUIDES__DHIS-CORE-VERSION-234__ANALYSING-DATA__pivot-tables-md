---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/analyze-data-in-pivot-tables.md"
revision_date: "2021-06-14"
---

# Analyzujte data v kontingenčních tabulkách { #pivot }

## O aplikaci Kontingenční tabulka { #pivot_about }

S aplikací **Kontingenční tabulka** můžete vytvářet kontingenční tabulky na základě všech dostupných datových dimenzí v DHIS2. Kontingenční tabulka je dynamický nástroj pro analýzu dat, který umožňuje sumarizovat a uspořádat data podle jejich dimenzí. Příklady datových dimenzí v DHIS2 jsou:

-   samotná datová dimenze (například datové prvky, indikátory a události)

-   období (představující časové období pro data)

-   hierarchie organizace (představující geografické umístění dat)

Z těchto dimenzí můžete libovolně vybrat _dimenzionální položky_, které chcete zahrnout do kontingenční tabulky. V DHIS2 můžete vytvořit další dimenze pomocí funkce skupiny. To umožňuje různé cesty agregace, například agregaci podle „partnera“ nebo typu zařízení.

Kontingenční tabulka může uspořádat datové dimenze na _sloupce_, _řádky_ a jako _filtry_. Když umístíte datovou dimenzi na sloupce, v kontingenční tabulce se zobrazí jeden sloupec na položku dimenze. Pokud na sloupce umístíte více datových dimenzí, kontingenční tabulka zobrazí jeden sloupec pro všechny kombinace položek ve vybraných dimenzích. Když umístíte datovou dimenzi na řádky, kontingenční tabulka zobrazí jeden řádek na položku dimenze podobným způsobem. Dimenze, které vyberete jako filtry, nebudou zahrnuty v kontingenční tabulce, ale agregují a filtrují data tabulky na základě vybraných položek filtru.

> **Tip**
>
> - Musíte vybrat alespoň jednu dimenzi na sloupcích nebo řádcích.
>
> - Musíte zahrnout alespoň jednu tečku.
>
> - Sady skupin datových prvků a četnosti přehledů se nemohou objevit ve stejné kontingenční tabulce.
>
> - Kontingenční tabulka nemůže obsahovat více než maximální počet analytických záznamů, který byl zadán v nastavení systému. Maximální počet záznamů může být také omezen maximální RAM, kterou má váš prohlížeč k dispozici. Pokud požadovaný stůl překročí určitou velikost, zobrazí se upozornění. Z této výzvy můžete buď zrušit požadavek, nebo pokračovat ve vytváření tabulky. Zvažte vytvoření menších tabulek namísto jedné tabulky, která zobrazuje všechny vaše datové prvky a indikátory společně.
>
> - Aplikace **Kontingenční tabulka** podporuje rozbalování a zvyšování pro období a organizační jednotku. To znamená, že v kontingenční tabulce můžete například procházet z ročních období na čtvrtletí, měsíce a týdny. Můžete také přejít z globální organizační jednotky do zemí, provincií a zařízení.

## Vytvořte kontingenční tabulku { #pivot_create }

1.  Otevřete aplikaci **Kontingenční tabulka**.

2.  V nabídce vlevo vyberte položky dimenze, které chcete analyzovat, například datové prvky nebo indikátory.

3.  Klikněte na **Rozložení** a uspořádejte datové dimenze jako sloupce, řádky a filtry.

    Pokud chcete, můžete ponechat výchozí výběr.

4.  Klikněte na **Aktualizovat**.

V tomto příkladu jsou indikátory uvedeny jako sloupce a období jako řádky.

![](resources/images/pivot_table/basic_pivot.png)

### Vyberte položky dimenze { #select-dimension-items }

V levé nabídce jsou uvedeny sekce všech dostupných dimenzí dat. V každé sekci můžete vybrat libovolný počet položek dimenze. Jako příklad můžete otevřít sekci pro datové prvky a vybrat libovolný počet datových prvků z dostupného seznamu. Položku můžete vybrat označením a kliknutím na šipku v záhlaví sekce nebo jednoduše poklepáním na položku. Než budete moci v kontingenční tabulce použít datovou dimenzi, musíte vybrat alespoň jednu položku dimenze. Pokud dimenzi uspořádáte jako sloupce nebo řádky, ale nevyberete žádné položky dimenze, bude dimenze ignorována.

K vytvoření kontingenční tabulky musíte vybrat alespoň jeden typ datové dimenze. Dostupné typy jsou popsány v této tabulce:

<table>
<caption> typy datových dimenzí </caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th> Typ datové dimenze </th>
<th> Definice </th>
<th> Příklady </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Indikátory </td>
<td> Indikátor je vypočítaný vzorec založený na datových prvcích. </td>
<td> Pokrytí imunizace v konkrétním okrese. </td>
</tr>
<tr class="even">
<td> Datové prvky </td>
<td> Představuje jev, pro který byla data zachycena. </td>
<td> Počet případů malárie; počet podaných dávek BCG. </td>
</tr>
<tr class="odd">
<td> Datové sady </td>
<td> Kolekce datových prvků seskupených pro sběr dat. Můžete vybrat:
<ul>
<li> <p> <strong> Míry hlášení </strong>: procento skutečných zpráv ve srovnání s očekávaným počtem zpráv </p> </li>
<li> <p> <strong> sazby hlášení včas </strong>: sazby hlášení založené na včasném odeslání formuláře. Včasné podání musí proběhnout do několika dnů po období, za které se podává zpráva. </p> </li>
<li> <p> <strong> skutečné zprávy </strong>: skutečný počet zpráv </p> </li>
<li> <p> <strong> aktuální zprávy včas </strong>: skutečný počet zpráv na základě včasného odeslání formuláře. Včasné podání musí proběhnout do několika dnů po období, za které se podává zpráva. </p> </li>
<li> <p> <strong> Očekávané zprávy </strong>: počet očekávaných zpráv na základě organizačních jednotek, kde byla přiřazena datová sada a četnost hlášení. </p> </li>
</ul> </td>
<td> Míry hlášení pro imunizaci a morbiditu. </td>
</tr>
<tr class="even">
<td> datové položky události </td>
<td> Datový prvek, který je součástí programu představujícího zachycené události. </td>
<td> Průměrná hmotnost a výška dětí ve výživovém programu. </td>
</tr>
<tr class="odd">
<td> Programové indikátory </td>
<td> Vypočítaný vzorec založený na datových prvcích v programu představujících události. </td>
<td> Průměrné skóre BMI u dětí ve výživovém programu. </td>
</tr>
</tbody>
</table>

Tyto dimenze můžete kombinovat a zobrazit například agregovaná data s rychlostí vykazování nebo datové položky událostí společně s indikátory programu, vše ve stejných kontingenčních tabulkách. U datové dimenze „datový prvek“ můžete také vybrat „Součty“ a „Podrobnosti“, což vám umožní zobrazit různé možnosti kombinace kategorií společně na stejné kontingenční tabulce.

U dimenze období si můžete vybrat mezi použitím pevných období nebo relativních období. Příkladem pevného období je „leden 2012“. Chcete-li vybrat pevná období, začněte výběrem typu období ze seznamu typů období. Potom můžete vybrat období ze seznamu dostupných období.

Relativní období jsou období vztahující se k aktuálnímu datu. Příklady relativních období jsou „Poslední měsíc“, „Posledních 12 měsíců“, „Posledních 5 let“. Relativní období lze vybrat zaškrtnutím políček vedle každého období. Hlavní výhodou použití relativních období je to, že když uložíte oblíbenou kontingenční tabulku, zůstane aktualizována nejnovějšími daty, jak plyne čas, aniž byste ji museli neustále aktualizovat.

Pro dimenzi organizační jednotky můžete z hierarchie vybrat libovolný počet organizačních jednotek. Chcete-li vybrat všechny organizační jednotky pod konkrétní nadřazenou organizační jednotkou, klikněte pravým tlačítkem a klikněte na „Vybrat všechny podřízené“. Chcete-li ručně vybrat více organizačních jednotek, klikněte a podržte klávesu **Ctrl** a klikněte na organizační jednotky. Chcete-li dynamicky vložit organizační jednotku nebo jednotky spojené s vaším uživatelským účtem, můžete zaškrtnout „Organizační jednotky uživatele“, „Podřízené org jednotky uživatele“ nebo „Uživatelské jednotky 2. podúrovně“. To je užitečné, když uložíte oblíbenou kontingenční tabulku a chcete ji sdílet s ostatními uživateli, protože při prohlížení oblíbené položky se použijí organizační jednotky propojené s účtem jiného uživatele.

![](resources/images/pivot_table/period_dimension.png)

Dynamické dimenze mohou sestávat ze sad skupin organizačních jednotek, sad skupin datových prvků nebo skupin skupin voleb kategorií, které byly nakonfigurovány s typem „Rozčlenění“. Jakmile budou sady skupin nakonfigurovány, budou k dispozici v kontingenčních tabulkách a lze je použít jako další dimenze analýzy, například k analýze agregovaných dat podle typu organizační jednotky nebo implementujícího partnera. Dynamické dimenze fungují stejně jako pevné dimenze.

> **Tip**
>
> Některé dynamické dimenze mohou obsahovat mnoho položek. To může způsobit problémy s určitými prohlížeči kvůli délce adresy URL, když je vybráno mnoho členů dimenze. Pro dynamické dimenze je k dispozici speciální zaškrtávací políčko „Vše“, které umožňuje implicitně zahrnout všechny dostupné dimenze do kontingenční tabulky, aniž byste museli specifikovat každého člena dimenze.

### Upravit rozložení kontingenční tabulky { #modify-pivot-table-layout }

Po výběru datových dimenzí je čas uspořádat kontingenční tabulku. Kliknutím na „Rozvržení“ v horní nabídce otevřete obrazovku rozvržení. Na této obrazovce můžete umístit své datové dimenze jako sloupce tabulky, řádky nebo filtry kliknutím a přetažením dimenzí ze seznamu dimenzí do příslušného seznamu sloupců, řádků a filtrů. V libovolném ze seznamů můžete nastavit libovolný počet dimenzí. Například můžete kliknout na „Organizační jednotky“ a přetáhnout jej do seznamu řádků, abyste umístili dimenzi organizační jednotky jako řádky tabulky. Uvědomte si, že indikátory, datové prvky a rychlosti vykazování sady dat jsou součástí běžné dimenze „Data“ a budou zobrazeny společně v kontingenční tabulce. Například po výběru indikátorů a datových prvků v levé nabídce můžete přetáhnout „Organizační jednotku“ ze seznamu dostupných dimenzí do seznamu dimenzí řádků a uspořádat je jako řádky v kontingenční tabulce.

![](resources/images/pivot_table/table_layout.png)

Po nastavení kontingenční tabulky můžete její kontingenční tabulku vykreslit kliknutím na „Aktualizovat“ nebo kliknutím na „Skrýt“ skrýt obrazovku rozvržení, aniž by se změny projevily. Protože jsme v našem příkladu vybrali jako řádky dimenzi období i organizační jednotky, kontingenční tabulka vygeneruje všechny kombinace položek v těchto dimenzích a vytvoří takovou tabulku:

![](resources/images/pivot_table/pivot_rows.png)

## Změňte zobrazení kontingenční tabulky { #pivot_change_display }

1.  Otevřete aplikaci **Kontingenční tabulka**.

2.  Vytvořte novou kontingenční tabulku nebo otevřete oblíbenou položku.

3.  Klikněte na **Možnosti**.

4.  Nastavte možnosti podle potřeby.

    <table>
    <caption>Pivot table options</caption>
    <colgroup>
    <col style="width: 21%" />
    <col style="width: 35%" />
    <col style="width: 42%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p>
    <p><strong>Show row totals</strong></p></td>
    <td><p>Displays total values in the table for each row and column, as well as a total for all values in the table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p>
    <p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays subtotals in the table for each dimension.</p>
    <p>If you only select one dimension, subtotals will be hidden for those columns or rows. This is because the values will be equal to the subtotals.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td><p>Shows the dimension names as part of the pivot tables.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide empty columns</strong></p></td>
    <td><p>Hides empty columns from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Skip rounding</strong></p></td>
    <td><p>Skips the rounding of data values, offering the full precision of data values. Can be useful for finance data where the full dollar amount is required.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Aggregation type</strong></p></td>
    <td><p>The default aggregation operator can be over-ridden here, by selecting a different aggregation operator. Some of the aggregation types are <strong>Count</strong>, <strong>Min</strong> and <strong>Max</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Number type</strong></p></td>
    <td><p>Sets the type of value you want to display in the pivot table: <strong>Value</strong>, <strong>Percentage of row</strong> or <strong>Percentage of column</strong>.</p>
    <p>The options <strong>Percentage of row</strong> and<strong>Percentage of column</strong> mean that you'll display values as percentages of row total or percentage of column total instead of the aggregated value. This is useful when you want to see the contribution of data elements, categories or organisation units to the total value.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Measure criteria</strong></p></td>
    <td><p>Allows for the data to be filtered on the server side.</p>
    <p>You can instruct the system to return only records where the aggregated data value is equal, greater than, greater or equal, less than or less or equal to certain values.</p>
    <p>If both parts of the filter are used, it's possible to filter out a range of data records.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Events</strong></p></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful for example to exclude partial events in indicator calculations.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Organisation units</strong></p></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Shows the name of all ancestors for organisation units, for example &quot;Sierra Leone / Bombali / Tamabaka / Sanya CHP&quot; for Sanya CHP.</p>
    <p>The organisation units are then sorted alphabetically which will order the organisation units according to the hierarchy.</p>
    <p>When you download a pivot table with organisation units as rows and you've selected <strong>Show hierarchy</strong>, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Legend</strong></p></td>
    <td><p><strong>Apply legend</strong></p></td>
    <td><p>Applies a legend to the values. This mean that you can apply a colour to the values.</p>
    <p>Select <strong>By data item</strong> to color the table cells individually according to each data element or indicator.</p>
    <p>You configure legends in the <strong>Maintenance</strong> app.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Style</strong></p></td>
    <td><p>Colors the text or background of cells in pivot tables based on the selected legend.</p>
    <p>You can use this option for scorecards to identify high and low values at a glance.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>General</strong></p></td>
    <td><p><strong>Table title</strong></p></td>
    <td><p>Type a title here to display it above the table.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Parameters (for standard reports only)</strong></p></td>
    <td><blockquote>
    <p><strong>Note</strong></p>
    <p>You create standard reports in the <strong>Reports</strong> app.</p>
    <p>In the <strong>Pivot Table</strong> app you set which parameters the system should prompt the user for.</p>
    </blockquote></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Reporting period</strong></p></td>
    <td><p>Controls whether to ask user to enter a report period.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter an organisation unit.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Parent organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter a parent organisation unit.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include regression</strong></p></td>
    <td><p>Includes a column with regression values to the pivot table.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Include cumulative</strong></p></td>
    <td><p>Includes a column with cumulative values to the pivot table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Sort order</strong></p></td>
    <td><p>Controls the sort order of the values.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Top limit</strong></p></td>
    <td><p>Controls the maximum number of rows to include in the pivot table.</p></td>
    </tr>
    </tbody>
    </table>

5.  Klikněte na **Aktualizovat**.

## Spravujte oblíbené položky { #manage-favorites }

Uložení grafů nebo kontingenčních tabulek jako oblíbených usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli jako interpretaci nebo je zobrazit na ovládacím panelu.

Podrobnosti a interpretace vašich oblíbených položek zobrazíte v aplikacích **Kontingenční tabulka**, **Zobrazení dat**, **Zobrazení událostí**, **Zprávy o událostech**. Pomocí nabídky **Oblíbené** můžete spravovat své oblíbené položky.

### Otevřete oblíbenou položku { #open-a-favorite }

1.  Klikněte na **Oblíbené** \> **Otevřít**.

2.  Zadejte název oblíbené položky do vyhledávacího pole nebo kliknutím na **Předchozí** a **Další** zobrazte oblíbené položky.

3.  Klikněte na název oblíbené položky, kterou chcete otevřít.

### Uložit oblíbené { #save-a-favorite }

1.  Klikněte na **Oblíbené** \> **Uložit jako**.

2.  Zadejte **Název** a **Popis** pro vaši oblíbenou položku. Pole popisu podporuje formát RTF, další podrobnosti najdete v části interpretace.

3.  Klikněte **Uložit**.

### Přejmenujte oblíbenou položku { #rename-a-favorite }

1.  Klikněte na **Oblíbené** \> **Přejmenovat**.

2.  Zadejte nový název své oblíbené položky.

3.  Klikněte na **Aktualizovat**.

### Napište interpretaci pro oblíbené { #write-an-interpretation-for-a-favorite }

Interpretace je odkaz na zdroj s popisem dat v daném období. Tyto informace jsou viditelné v aplikaci **Ovládací panel**. Chcete-li vytvořit interpretaci, musíte nejprve vytvořit oblíbenou položku. Pokud jste sdíleli své oblíbené položky s jinými lidmi, interpretace, kterou píšete, je viditelná pro tyto lidi.

1.  Klikněte na **Oblíbené** \> **Napsat výklad**.

2.  Do textového pole zadejte komentář, otázku nebo výklad. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s výkladem nebo komentářem. Výklad můžete vidět v aplikaci **Dashboard**.

    Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown \* a \_ pro **tučné** a _italic_. K dispozici jsou také klávesové zkratky: Ctrl / Cmd + B a Ctrl / Cmd + I. Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: :) :-) :( :-(: +1 :-1. URL jsou automaticky detekovány a převedeny na odkaz, na který lze kliknout.

3.  Vyhledejte skupinu uživatelů, se kterou chcete sdílet své oblíbené, a klikněte na znaménko **+**.

4.  Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit.

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádné**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro **Veřejný přístup**.

5.  Klikněte na **Sdílet**.

### Přihlaste se k odběru oblíbené položky { #subscribe-to-a-favorite }

Když jste přihlášeni k odběru oblíbené položky, dostáváte interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci nebo vytvoří / aktualizuje komentář k interpretaci této oblíbené položky.

1.  Otevřete oblíbenou položku.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Kliknutím na ikonu zvonku vpravo nahoře se přihlásíte k odběru této oblíbené položky.

### Vytvořte odkaz na oblíbenou položku { #create-a-link-to-a-favorite }

1.  Klikněte na **Oblíbené** \> **Získat odkaz**.

2.  Vyberte jednu z následujících možností:

    -   **Otevřít v této aplikaci**: Získáte URL oblíbené položky, kterou můžete sdílet s ostatními uživateli prostřednictvím e-mailu nebo chatu.

    -   **Otevřít ve webovém rozhraní API**: Získáte adresu URL prostředku API. Ve výchozím nastavení se jedná o zdroj HTML, ale můžete změnit příponu souboru na „.json“ nebo „.csv“.

### Odstranit oblíbenou položku { #delete-a-favorite }

1.  Klikněte na **Oblíbené** \> **Odstranit**.

2.  Klikněte **OK**.

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Klikněte na interpretaci. Váš graf zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

## Stáhněte si data z kontingenční tabulky { #pivot_download_data }

### Stáhněte si datový formát rozložení tabulky { #download-table-layout-data-format }

Postup stažení dat v aktuální kontingenční tabulce:

1.  Klikněte na **Stáhnout**.

2.  V části **Rozvržení tabulky** klikněte na formát, který chcete stáhnout: Microsoft Excel, CSV nebo HTML.

    Tabulka dat bude mít jeden sloupec na dimenzi a bude obsahovat názvy položek dimenze.

    > **Tip**
    >
    > When you download a pivot table with organisation units as rows and you've selected **Show hierarchy** in **Table options**, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.

> **Tip**
>
> Kontingenční tabulku můžete vytvořit v aplikaci Microsoft Excel ze staženého souboru aplikace Excel.

### Stáhněte si zdrojový formát  plain data { #download-plain-data-source-format }

Můžete si stáhnout data v aktuální kontingenční tabulce v JSON, XML, Excel a CSV jako prosté datové formáty s různými identifikačními schématy (ID, kód a název). Datový dokument používá identifikátory položek dimenze a otevře se v novém okně prohlížeče, aby se v adresním řádku zobrazila adresa URL požadavku na webové rozhraní API. To je užitečné pro vývojáře aplikací a dalších klientských modulů založených na webovém rozhraní DHIS2 nebo pro ty, kteří vyžadují zdroj dat plánu, například pro import do statistických balíčků.

Postup stažení formátů prostého zdroje dat:

1.  Klikněte na **Stáhnout**.

2.  V části **Zdroj prostých dat** klikněte na formát, který chcete stáhnout.

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 18%" />
    <col style="width: 33%" />
    <col style="width: 47%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Action</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>JSON</p></td>
    <td><p>Click <strong>JSON</strong></p></td>
    <td><p>Downloads JSON format based on ID property.</p>
    <p>You can also download JSON format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>XML</p></td>
    <td><p>Click <strong>XML</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download XML format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Microsoft Excel</p></td>
    <td><p>Click <strong>Microsoft Excel</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download Microsoft Excel format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>CSV</p></td>
    <td>Click <strong>CSV</strong></td>
    <td><p>Downloads CSV format based on ID property.</p>
    <p>You can also download CSV format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>JRXML</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>JRXML</strong></p></td>
    <td><p>Produces a template of a Jasper Report which can be further customized based on your exact needs and used as the basis for a standard report in DHIS2.</p></td>
    </tr>
    <tr class="even">
    <td><p>Raw data SQL</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>Raw data SQL</strong></p></td>
    <td><p>Provides the actual SQL statement used to generate the pivot table. You can use it as a data source in a Jasper report, or as the basis for an SQL view.</p></td>
    </tr>
    </tbody>
    </table>

### Stáhněte si formát CSV bez vykreslování dat ve webovém prohlížeči { #download-a-csv-format-without-rendering-data-in-the-web-browser }

Data si můžete stáhnout přímo ve formátu CSV, aniž byste je museli vykreslovat ve webovém prohlížeči. To pomáhá snížit veškerá omezení v nastavení systému, která byla nastavena s ohledem na maximální počet analytických záznamů. To vám umožní stáhnout mnohem větší dávky dat, které můžete použít pro pozdější offline analýzu.

Postup stažení dat ve formátu CSV bez předchozího vykreslení dat ve webovém prohlížeči:

1.  Klikněte na šipku vedle **Aktualizovat**.

    ![](resources/images/pivot_table/data_dump.png)

2.  Kliknutím na **CSV** stáhnete formát založený na ID property.

    Soubor se stáhne do vašeho počítače.

    > **Tip**
    >
    > You can also download CSV format based on **Code** or **Name** property.

## Vložit kontingenční tabulku na externí webovou stránku { #pivot_embed }

Některé zdroje související s analýzou v DHIS2, jako jsou kontingenční tabulky, grafy a mapy, lze vložit na libovolnou webovou stránku pomocí zásuvného modulu. Více informací o zásuvných modulech najdete v kapitole Web API v _DHIS2 Developer Manual_.

Chcete-li vygenerovat fragment HTML, který můžete použít k zobrazení kontingenční tabulky na externí webové stránce, postupujte takto:

1.  Klikněte na **Vložit**.

2.  Kliknutím na **Vybrat** zvýrazněte fragment HTML.

## Vizualizujte data kontingenční tabulky jako graf nebo mapu { #pivot_integration }

Když jste vytvořili kontingenční tabulku, můžete přepínat mezi vizualizací kontingenční tabulky, grafu a mapy vašich dat.

### Otevřít kontingenční tabulku jako graf { #open-a-pivot-table-as-a-chart }

1.  Klikněte na **Graf** \> **Otevřít tuto tabulku jako graf**.

    Vaše aktuální kontingenční tabulka se otevře jako graf.

![](resources/images/pivot_table/pivot_integration.png)

### Otevřete výběr kontingenční tabulky jako graf { #open-a-pivot-table-selection-as-a-chart }

Pokud chcete vizualizovat malou část své kontingenční tabulky jako graf, můžete místo otevření celé tabulky kliknout přímo na hodnotu v tabulce.

1.  V kontingenční tabulce klikněte na hodnotu.

        ![](resources/images/pivot_table/pivot_integration_table.png)

2.  Chcete-li ověřit výběr, podržte kurzor nad **Otevřít výběr jako graf**. Zvýrazněná záhlaví dimenzí v tabulce označují, jaká data budou zobrazena jako graf.

3.  Klikněte na **Otevřít výběr jako graf**.

### Otevřete kontingenční tabulku jako mapu { #open-a-pivot-table-as-a-map }

1.  Klikněte na **Graf** \> **Otevřít tuto tabulku jako mapu**

    Vaše aktuální kontingenční tabulka se otevře jako mapa.

### Otevřete výběr kontingenční tabulky jako mapu { #open-a-pivot-table-selection-as-a-map }

1.  V kontingenční tabulce klikněte na hodnotu.

    Zobrazí se nabídka.

2.  Klikněte na **Otevřít výběr jako mapu**.

    Váš výběr se otevře jako mapa.
