---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/user/analyze-data-in-pivot-tables.md"
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

Tabulka: Typy datových dimenzí

| Typ datové dimenze | Definice | Příklady |
| --- | --- | --- |
| Indikátory | Indikátor je vypočítaný vzorec založený na datových prvcích. | Pokrytí očkování v konkrétním okrese. |
| Datové prvky | Představuje jev, pro který byla data zachycena. | Počet případů malárie; počet podaných dávek BCG. |
| Datové sady | Kolekce datových prvků seskupených pro sběr dat. Můžete si vybrat: <br> _ **Sazby hlášení**: procento skutečných hlášení ve srovnání s očekávaným počtem hlášení <br> _ **Poměry hlášení včas**: sazby hlášení založené na včasném odeslání formuláře. Včasné předložení musí proběhnout do několika dnů po období hlášení. <br> _ **Skutečné zprávy**: skutečný počet zpráv <br> _ **Skutečné zprávy včas**: skutečný počet zpráv na základě včasného odeslání formuláře. Včasné předložení musí proběhnout do několika dnů po období hlášení. <br> \* **Očekávané zprávy**: počet očekávaných zpráv na základě organizačních jednotek, kterým byla přiřazena datová sada a frekvence podávání zpráv. | Hlášení míry pro imunizaci a formy nemocnosti. |
| Datové položky událostí | Datový prvek, který je součástí programu představujícího události, které byly zachyceny. | Průměrná hmotnost a výška dětí ve výživovém programu. |
| Indikátory programu | Vypočítaný vzorec založený na datových prvcích v programu představujícím události. | Průměrné skóre BMI pro děti ve výživovém programu. |

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

    Tabulka: Možnosti kontingenční tabulky

    | | Možnost | Popis |
    | --- | --- | --- |
    | **Údaje** | **Zobrazit součty sloupců** <br> <br> **Zobrazit součty řádků** | Zobrazí celkové hodnoty v tabulce pro každý řádek a sloupec a také součet všech hodnot v tabulce. |
    | | **Zobrazit sloupcové mezisoučty** <br> <br> **Zobrazit řádkové mezisoučty** | Zobrazí mezisoučty v tabulce pro každou dimenzi. <br> <br> Pokud vyberete pouze jednu dimenzi, mezisoučty budou pro tyto sloupce nebo řádky skryté. Hodnoty se totiž budou rovnat mezisoučtům. |
    | | **Zobrazit štítky dimenzí** | Zobrazuje názvy dimenzí jako součást kontingenčních tabulek. |
    | | **Skrýt prázdné řádky** | Skryje prázdné řádky z tabulky. To je užitečné, když se díváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
    | | **Skrýt prázdné sloupce** | Skryje prázdné sloupce z tabulky. To je užitečné, když se díváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
    | | **Přeskočit zaokrouhlování** | Přeskočí zaokrouhlování datových hodnot a nabízí plnou přesnost datových hodnot. Může být užitečné pro finanční data, kde je vyžadována celá částka v dolarech. |
    | | **Typ agregace** | Výchozí operátor agregace zde lze přepsat výběrem jiného operátora agregace. Některé z typů agregace jsou **Počet**, **Min** a **Max**. |
    | | **Typ čísla** | Nastavuje typ hodnoty, kterou chcete zobrazit v kontingenční tabulce: **Hodnota**, **Procento řádku** nebo **Procento sloupce**. <br> <br> Možnosti **Procento řádku** a**Procento sloupce** znamenají, že zobrazíte hodnoty jako procenta z celkového počtu řádků nebo procenta z celkového počtu sloupců namísto agregované hodnoty. To je užitečné, když chcete vidět příspěvek datových prvků, kategorií nebo organizačních jednotek k celkové hodnotě. |
    | | **Kritéria měření** | Umožňuje filtrování dat na straně serveru. <br> <br> Systému můžete dát pokyn, aby vracel pouze záznamy, kde je agregovaná hodnota dat rovna, větší než, větší nebo rovna, menší nebo menší nebo rovna určitým hodnotám. <br> <br> Pokud jsou použity obě části filtru, je možné odfiltrovat řadu datových záznamů. |
    | **Události** | **Zahrnout pouze dokončené události** | Zahrnuje pouze dokončené události v procesu agregace. To je užitečné například pro vyloučení dílčích událostí ve výpočtech indikátorů. |
    | **Organizační jednotky** | **Zobrazit hierarchii** | Zobrazuje jména všech předků organizačních jednotek, například "Sierra Leone / Bombali / Tamabaka / Sanya CHP" pro Sanya CHP. <br> <br> Organizační jednotky jsou poté seřazeny abecedně, což seřadí organizační jednotky podle hierarchie. <br> <br> Když stáhnete kontingenční tabulku s organizačními jednotkami jako řádky a vyberete **Zobrazit hierarchii**, každá úroveň organizační jednotky se vykreslí jako samostatný sloupec. To je užitečné například při vytváření kontingenčních tabulek Excelu na místním počítači. |
    | **Legenda** | **Použít legendu** | Aplikuje na hodnoty legendu. To znamená, že na hodnoty můžete použít barvu. <br> <br> Chcete-li obarvit buňky tabulky jednotlivě podle každého datového prvku nebo indikátoru, vyberte **Podle datové položky**. <br> <br> Legendy konfigurujete v aplikaci **Údržba**. |
    | | **Styl** | Obarví text nebo pozadí buněk v kontingenčních tabulkách na základě vybrané legendy. <br> <br> Tuto volbu můžete použít pro skórkarty, abyste na první pohled identifikovali vysoké a nízké hodnoty. |
    | **Styl** | **Hustota zobrazení** | Řídí velikost buněk v tabulce. Můžete jej nastavit na **Pohodlné**, **Normální** nebo **Kompaktní**. <br> <br> **Kompaktní** je užitečné, když chcete na obrazovku prohlížeče umístit velké tabulky. |
    | | **Velikost písma** | Řídí velikost písma textu tabulky. Můžete jej nastavit na **Velký**, **Normální** nebo **Malý**. |
    | | **Oddělovač skupin číslic** | Určuje, který znak oddělit skupiny číslic nebo "tisíce". Můžete jej nastavit na **Čárka**, **Mezerník** nebo **Žádný**. |
    | **Obecné** | **Název tabulky** | Zadejte název, který se zobrazí nad tabulkou. |
    | **Parametry (pouze pro standardní přehledy)** | **Poznámka** <br> Standardní sestavy vytváříte v aplikaci **Přehledy**. <br> V aplikaci **Kontingenční tabulka** nastavujete, které parametry má systém uživatele vyzvat. | |
    | | **Období vykazování** | Určuje, zda požádat uživatele o zadání období sestavy. |
    | | **Organizační jednotka** | Řídí, zda požádat uživatele o zadání organizační jednotky. |
    | | **Mateřská organizační jednotka** | Řídí, zda požádat uživatele o zadání nadřazené organizační jednotky. |
    | | **Zahrnout regresi** | Zahrnuje sloupec s regresními hodnotami do kontingenční tabulky. |
    | | **Zahrnout kumulativní** | Zahrnuje sloupec s kumulativními hodnotami do kontingenční tabulky. |
    | | **Pořadí řazení** | Řídí pořadí řazení hodnot. |
    | | **Top limit** | Řídí maximální počet řádků, které mají být zahrnuty do kontingenční tabulky. |

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

    Tabulka: Dostupné formáty

    | Formát | Akce | Popis |
    | --- | --- | --- |
    | JSON | Klikněte na **JSON** | Stáhne formát JSON na základě vlastnosti ID. <br> <br> Můžete si také stáhnout formát JSON založený na vlastnosti **Code** nebo **Name**. |
    | XML | Klikněte na **XML** | Stáhne formát XML na základě vlastnosti ID. <br> <br> Můžete si také stáhnout formát XML založený na vlastnosti **Code** nebo **Name**. |
    | Microsoft Excel | Klikněte na **Microsoft Excel** | Stáhne formát XML na základě vlastnosti ID. <br> <br> Můžete si také stáhnout formát Microsoft Excel založený na vlastnosti **Code** nebo **Name**. |
    | CSV | Klikněte na **CSV** | Stáhne formát CSV na základě vlastnosti ID. <br> <br> Můžete si také stáhnout formát CSV založený na vlastnosti **Code** nebo **Name**. |
    | JRXML | Umístěte kurzor na **Advanced** a klikněte na **JRXML** | Vytváří šablonu zprávy Jasper, kterou lze dále upravit na základě vašich přesných potřeb a použít jako základ pro standardní zprávu v DHIS2. |
    | Nezpracovaná data SQL | Umístěte kurzor na **Advanced** a klikněte na **Raw data SQL** | Poskytuje skutečný příkaz SQL použitý ke generování kontingenční tabulky. Můžete jej použít jako zdroj dat v sestavě Jasper nebo jako základ pro zobrazení SQL. |

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
