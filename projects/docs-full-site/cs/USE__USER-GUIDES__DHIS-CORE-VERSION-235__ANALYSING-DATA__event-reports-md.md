---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-the-event-reports-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Hlášení o události { #event_reports_app }

## O aplikaci Hlášení o události { #event_reports_about }

![](resources/images/event_report/event_report.png)

S aplikací **Zpráva o události** můžete analyzovat události ve dvou typech přehledů:

-   Agregované zprávy o událostech: Analýza stylu kontingenční tabulky s agregovaným počtem událostí

    Výběrem **Agregované hodnoty** z nabídky vlevo nahoře můžete pomocí aplikace **Zprávy událostí** vytvořit kontingenční tabulky s agregovaným počtem událostí. Zpráva o události je vždy založena na programu. Můžete provést analýzu na základě řady dimenzí. Každá dimenze může mít odpovídající filtr. Rozměry lze vybrat z nabídky vlevo. Podobně jako v aplikaci kontingenčních tabulek mohou být agregované zprávy o událostech omezeny množstvím paměti RAM přístupné prohlížečem. Pokud vámi požadovaná tabulka přesahuje nastavenou velikost, obdržíte varovnou výzvu s dotazem, zda chcete pokračovat.

-   Jednotlivé zprávy o událostech: Seznamy událostí

    Výběrem **Události** z nabídky vlevo nahoře můžete pomocí aplikace **Zprávy o událostech** provádět vyhledávání nebo dotazy na události na základě flexibilní sady kritérií. Zpráva se zobrazí jako tabulka s jedním řádkem na událost. Každá dimenze může být použita jako sloupec v tabulce nebo jako filtr. Každá dimenze může mít kritéria (filtr). Datové prvky sady možností typu umožňují kritéria „in“, kde lze vybrat více možností. Číselné hodnoty lze porovnat s hodnotami filtru pomocí operátorů větší než, rovný nebo menší než.

## Vytvořte zprávu o události { #event_reports_create }

1.  Otevřete aplikaci **Hlášení událostí**.

2.  Vyberte **Agregované hodnoty** nebo **Události**.

3.  V nabídce vlevo vyberte metadata, která chcete analyzovat.

4.  Klikněte na **Rozložení** a uspořádejte dimenze.

    Pokud chcete, můžete ponechat výchozí výběr.

5.  Klikněte na **Aktualizovat**.

## Vyberte položky dimenze { #event_reports_select_dimensions }

Zpráva o události je vždy založena na programu a můžete provádět analýzu na základě řady dimenzí. U programů s kombinacemi kategorií můžete jako dimenze pro tabulky a grafy použít kategorie programů a skupiny skupin voleb možností. Každá položka dimenze může mít odpovídající filtr.

1.  Vyberte datové prvky:

    1.  Klikněte na **Data**.

    2.  Vyberte program a fázi programu.

        Datové prvky spojené s vybraným programem jsou uvedeny v části **Dostupné**. Každý datový prvek funguje jako dimenze.

    3.  Poklepáním na jejich názvy vyberte datové prvky, které potřebujete.

        Datové prvky lze filtrovat podle typu (datové prvky, atributy programu, indikátory programu) a mají předponu, aby byly snadno rozpoznatelné.

        Po výběru datového prvku je viditelný pod **Vybrané datové položky**.

    4.  (Volitelné) Pro každý datový prvek zadejte filtr s operátory, jako je „větší než“, „v“ nebo „rovno“, spolu s hodnotou filtru.

2.  Vyberte období

    1.  Klikněte na **Období**.

    2.  Vyberte jedno nebo několik období.

        Máte tři možnosti období: relativní období, pevná období a datum zahájení / ukončení. Ve stejném grafu můžete kombinovat pevná období a relativní období. Nemůžete kombinovat pevná období a relativní období s daty zahájení a ukončení ve stejném grafu. Překrývající se období jsou filtrována tak, aby se objevila pouze jednou.

        -   Pevná období: V poli **Vyberte typ období** vyberte typ období. Můžete vybrat libovolný počet pevných období z jakéhokoli typu období. Pevná období mohou být například „leden 2014“.

        -   Relativní období: Ve spodní části části **Období** vyberte tolik relativních období, kolik chcete. Názvy jsou relativní k aktuálnímu datu. To znamená, že pokud je aktuální měsíc březen a vyberete **minulý měsíc**, bude do grafu zahrnut i měsíc únor. Relativní období má tu výhodu, že udržuje data v přehledu aktuální podle času.

        -   Datum zahájení / ukončení: V seznamu na kartě **Období** vyberte **Datum zahájení / ukončení**. Tento typ období umožňuje určit flexibilní data pro časové rozpětí ve zprávě.

3.  Vyberte organizační jednotky.

    1.  Klikněte na **Organizační jednotky**

    2.  Klikněte na ikonu ozubeného kolečka.

    3.  Vyberte **režim výběru** a organizační jednotku.

        Existují tři různé režimy výběru:

        <table>
        <caption>Selection modes</caption>
        <colgroup>
        <col style="width: 38%" />
        <col style="width: 61%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Selection mode</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><strong>Select organisation units</strong></p></td>
        <td><p>Lets you select the organisation units you want to appear in the chart from the organization tree.</p>
        <p>Select <strong>User org unit</strong> to disable the organisation unit tree and only select the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-units</strong> to disable the organisation unit tree and only select the sub-units of the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-x2-units</strong> to disable the organisation unit tree and only select organisation units two levels down from the organisation unit that is related to your profile.</p>
        <p>This functionality is useful for administrators to create a meaningful &quot;system&quot; favorite. With this option checked all users find their respective organisation unit when they open the favorite.</p></td>
        </tr>
        <tr class="even">
        <td><p><strong>Select levels</strong></p></td>
        <td><p>Lets you select all organisation units at one or more levels, for example national or district level.</p>
        <p>You can also select the parent organisation unit in the tree, which makes it easy to select for example, all facilities inside one or more districts.</p></td>
        </tr>
        <tr class="odd">
        <td><p><strong>Select groups</strong></p></td>
        <td><p>Lets you select all organisation units inside one or several groups and parent organisation units at the same time, for example hospitals or chiefdoms.</p></td>
        </tr>
        </tbody>
        </table>

4.  Klikněte na **Aktualizovat**.

## Vyberte sérii, kategorii a filtr { #event_reports_select_series_category_filter }

Můžete určit, která datová dimenze se má v kontingenční tabulce zobrazit jako sloupce, řádky a filtry. Každý datový prvek se jeví jako jednotlivé dimenze a lze jej umístit na kteroukoli z os.

> **Poznámka**
>
> Datové prvky typů spojitých hodnot (reálná čísla / desetinná čísla) lze použít pouze jako filtry a budou automaticky umístěny jako filtry v dialogovém okně rozložení. Důvodem je to, že spojité číslo nelze seskupit do rozumných rozsahů a použít na sloupcích a řádcích.

1.  Klikněte na **Rozložení**.

2.  Přetáhněte dimenze do příslušného prostoru.

3.  Klikněte na **Aktualizovat**.

## Změňte zobrazení tabulky { #event_reports_change_display }

Můžete přizpůsobit zobrazení zprávy o události.

1.  Klikněte na **Možnosti**.

2.  Nastavte možnosti podle potřeby. Dostupné možnosti se mezi agregovanými přehledy událostí a jednotlivými přehledy událostí liší.

    <table style="width:100%;">
    <caption>Event reports options</caption>
    <colgroup>
    <col style="width: 22%" />
    <col style="width: 22%" />
    <col style="width: 33%" />
    <col style="width: 22%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    <th><p>Available for report type</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p></td>
    <td><p>Displays totals at the end of each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show row totals</strong></p></td>
    <td><p>Displays totals at the end of each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td>Displays labels for dimensions.</td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide n/a data</strong></p></td>
    <td><p>Hides data tagged as N/A from the chart.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful when you want for example to exclude partial events in indicator calculations.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Limit</strong></p></td>
    <td><p>Sets a limit of the maximum number of rows that you can display in the table, combined with a setting for showing top or bottom values.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Output type</strong></p></td>
    <td><p>Defines the output type. The output types are <strong>Event</strong>, <strong>Enrollment</strong> and<strong>Tracked entity instance</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Program status</strong></p></td>
    <td><p>Filters data based on the program status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong> or <strong>Cancelled</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Event status</strong></p></td>
    <td><p>Filters data based on the event status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong>, <strong>Scheduled</strong>, <strong>Overdue</strong> or <strong>Skipped</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td><strong>Organisation units</strong></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Includes the names of all parents of each organisation unit in labels.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    </tbody>
    </table>

3.  Klikněte na **Aktualizovat**.

## Stáhněte si zdroj dat grafu { #event_reports_download_report }

Zdroj dat za zprávou o události si můžete stáhnout ve formátech HTML, JSON, XML, Microsoft Excel nebo CSV.

1.  Klikněte na **Stáhnout**.

2.  V části **Zdroj prostých dat** klikněte na formát, který chcete stáhnout.

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 27%" />
    <col style="width: 72%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>HTML</p></td>
    <td><p>Creates HTML table based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>JSON</p></td>
    <td><p>Downloads data values in JSON format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>XML</p></td>
    <td><p>Downloads data values in XML format based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>Microsoft Excel</p></td>
    <td><p>Downloads data values in Microsoft Excel format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>CSV</p></td>
    <td><p>Downloads data values in CSV format based on selected meta data</p></td>
    </tr>
    </tbody>
    </table>

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

## Vizualizujte zprávu o události jako graf { #event_reports_open_as_chart }

Když jste vytvořili zprávu o události, můžete ji otevřít jako graf:

Klikněte na **Graf** \> **Otevřít tento graf jako tabulku**.
