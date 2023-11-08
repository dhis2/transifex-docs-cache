---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/configure-metadata.md"
revision_date: "2021-06-14"
---

# Nakonfigurujte metadata { #maintenance_app }

## O aplikaci Údržba { #about_maintenance_app }

V aplikaci **Údržba** konfigurujete všechny objekty metadat, které potřebujete ke shromažďování a analýze dat:

-   Kategorie

-   Datové prvky

-   Datové sady a formuláře pro zadávání údajů

-   Indikátory

-   Organizační jednotky

-   Metadata programu: trasovaná entita, atribut trasované entity a typ vztahu

-   Pravidla ověřování

-   Atributy

-   Konstanty

-   Sady možností

-   Legendy

-   Prediktory

-   Nabízené zprávy

-   Externí mapové vrstvy

> **Poznámka**
>
> Funkce, ke kterým máte přístup, závisí na přístupových oprávněních vaší uživatelské role.

### Navigace v objektech metadat { #navigating_metadata }

Objekty metadat jsou uvedeny v seznamu s předdefinovanými sloupci, které jsou relevantní pro každý objekt. Můžete upravit, které sloupce se zobrazí v seznamu pro aktuální objekt. Tyto úpravy se vztahují na uživatele, a proto nebudou mít vliv na ostatní uživatele. Všimněte si, že tyto změny nezmění žádná metadata, pouze způsob prezentace seznamu.

#### Správa viditelných sloupců { #managing-visible-columns }

![](resources/images/maintainence/configurable_columns_dialog.png)

1. Klikněte na ikonu ![Ikona nastavení](resources/images/maintainence/icon_settings.png) v pravém horním rohu seznamu objektů, které chcete konfigurovat.
2. Zobrazí se rozbalovací nabídka a vyberte možnost **Spravovat sloupce**.
3. Zobrazí se dialogové okno s vybranými výchozími sloupci.
4. Kliknutím na název libovolného sloupce v seznamu **Dostupné sloupce** je přidáte do seznamu vybraných sloupců.
5. Uspořádání vybraných sloupců můžete provést přetažením ikony ![Uspořádání ikon](resources/images/maintainence/icon_reorder.png)
6. Libovolný sloupec můžete ze zobrazení také odebrat kliknutím na ikonu X vedle názvu.
7. Až budete se svými změnami spokojeni, klikněte na **Uložit**.

Výchozí hodnoty můžete snadno obnovit kliknutím na tlačítko **Obnovit výchozí**.

##### Stáhnout metadata { #download-metadata }

Můžete si stáhnout metadata pro objekt, který si právě prohlížíte. Stahování metadat bude respektovat všechny filtry, které máte pro seznam aktivní.

1. Klikněte na ikonu ![Ikona nastavení](resources/images/maintainence/icon_settings.png) v pravém horním rohu seznamu objektů, které chcete konfigurovat.
2. Zobrazí se rozbalovací nabídka a vyberte možnost **Stáhnout**.
3. Zobrazí se dialogové okno, kde můžete vybrat požadovaný formát a kompresi.
4. **Se sdílením** lze vybrat, aby zahrnovala data sdílení pro metadata.

## Spravujte kategorie { #manage_category }

### O kategoriích { #about_category }

Kategorie jsou obvykle pojem, například „Pohlaví“, „Věk“ nebo „Stav nemoci“. Datové prvky, jako je „Počet případů potvrzené malárie“, jsou často rozděleny na menší části, aby se určil například počet potvrzených případů malárie u konkrétních věkových skupin.

Pomocí kategorií rozdělíte datové prvky na jednotlivé komponenty. Můžete také použít kategorie k přiřazení atributů metadat ke všem údajům zaznamenaným v konkrétní datové sadě, například „Implementující partner“ nebo „Financující agentura“.

Vytvořte tři kategorie: „Pod 1“, „1-5“ a „Více než 5“. Přiřaďte je jako kategorie k datovému prvku. Tím se vytvoří tři samostatná pole pro tato data ve formulářích pro zadávání dat:

-   Počet potvrzených případů malárie (pod 1)

-   Počet potvrzených případů malárie (1-5)

-   Počet potvrzených případů malárie (více než 5)

Bez kategorií byste museli každý z výše uvedených datových prvků vytvořit samostatně.

V aplikaci **Údržba** spravujete následující a kategorie objektů:

<table>
<caption> Kategorie objektů v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Možnost kategorie </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> kategorie </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> kombinace kategorií </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> kombinace možností kategorie </p> </td>
<td> <p> Upravit a zobrazit podrobnosti </p> </td>
</tr>
<tr class="odd">
<td> <p> skupina možností kategorie </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> sada skupin možností možností </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Pracovní postup { #workflow_category }

1.  Vytvořte všechny možnosti kategorií.

2.  Vytvořte kategorie složené z několika možností kategorií, které jste vytvořili.

3.  Vytvářejte kombinace kategorií složené z jedné nebo více kategorií.

4.  Vytvořte datové prvky a přiřaďte je ke kombinaci kategorií.

### Vytvořte nebo upravte možnost kategorie { #create_category_option }

Pokud je to možné, recyklujte možnosti kategorií. Mohou například existovat dvě kategorie, které mohou sdílet možnost konkrétní kategorie (například \<1 rok věku). Při vytváření kategorií lze tuto možnost kategorie znovu použít. To je důležité, pokud je třeba analyzovat konkrétní možnosti kategorie (nebo kombinace možností kategorie), které je třeba analyzovat společně.

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Možnost Kategorie**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Datum začátku**

    3.  **Datum ukončení**

4.  Vyberte organizační jednotky a přiřaďte je.

    > **Tip**
    >
    > You can automatically select all organisation units that belong to an organisation unit level or organisation unit group, for example "Chiefdom" or "Urban. To do this:
    >
    > Select an **Organisation unit level** or **Organisation unit group** and click **Select**.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte kategorii { #create_category }

Když jste pro konkrétní kategorii vytvořili všechny možnosti kategorií, můžete tuto kategorii vytvořit.

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Kategorie**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Kód**

    3.  **Typ datové dimenze**

        Kategorie může být typu „Rozčlenění“ nebo „Atribut“. Pro rozčlenění datových prvků vyberete **Rozčlenění**. Typ datové dimenze „Atribut“ umožňuje kategorii použít k přiřazení kombinace kategorií k datům zaznamenaným prostřednictvím datové sady.

    4.  **Datová dimenze**

        Pokud vyberete **Datová dimenze**, bude kategorie k dispozici analytikům jako další dimenze kromě standardních dimenzí „Období“ a „Organizační jednotka“.

4.  Vyberte možnosti kategorií a přiřaďte je.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte kombinaci kategorií { #create_category_combination }

Kombinace kategorií vám umožní kombinovat více kategorií do související sady.

Datový prvek „Počet nových infekcí HIV“ můžete rozčlenit do následujících kategorií:

-   Služba HIV: „Jiné“, „PMTCT“, „TB“

-   Pohlaví "muž", "žena"

V tomto příkladu existují dvě úrovně členění, které se skládají ze dvou samostatných kategorií datových prvků. Každá kategorie datových prvků se skládá z několika možností kategorií datových prvků.

V DHIS2 jsou různé datové prvky rozděleny podle společné sady kategorií. Kombinací těchto různých kategorií do kombinace kategorií a přiřazením těchto kombinací datovým prvkům můžete rychle použít příslušné úrovně členění na velký počet datových prvků.

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Kombinace kategorií**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Kód**

    3.  **Typ datové dimenze**

    4.  **Přeskočit kategorie celkem v přehledech**

4.  Vyberte kategorie a přiřaďte je.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu možností kategorie { #create_category_option_group }

Možnosti kategorií můžete seskupit a klasifikovat pomocí skupin možností kategorií. Hlavním účelem skupiny skupin možností možností je přidat do vašich zachycených dat pro analýzu více dimenzí, například v aplikacích **Kontingenční tabulka** nebo **Datový Visualizer**.

Zvažte systém, kde jsou data shromažďována na „projekty“ a projekty jsou modelovány jako možnosti kategorií. Systém musí být schopen analyzovat data na základě toho, který dárce projekt podporuje. V takovém případě vytvořte skupinu možností skupiny s názvem „Dárce“. Každý dárce může být vytvořen jako skupina možností kategorie, kde je každá možnost kategorie / projekt zařazena do příslušné skupiny. V aplikacích pro analýzu dat se skupina skupin „Dárce“ zobrazí jako datová dimenze, zatímco každý dárce se zobrazí jako položky dimenze, které budou připraveny k zahrnutí do přehledů.

Vytvoření skupiny možností kategorie:

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Skupina možností kategorie**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Krátký název**: Definujte krátký název pro datový prvek.

    3.  **Kód**

    4.  **Typ datové dimenze**

4.  Vyberte **Možnosti kategorie** a přiřaďte je.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte sadu skupin možností kategorií { #create_category_option_group_set }

Skupiny voleb kategorií můžete seskupit do sad skupin možností skupin. Hlavním účelem sady skupin možností kategorií je přidat do vašich zachycených dat pro analýzu více dimenzí, například v aplikacích **Kontingenční tabulka** nebo **Data Visualizer**.

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Sada skupin možností kategorie**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Popis**

    3.  **Datová dimenze**

    4.  **Typ datové dimenze**

4.  Vyberte **Skupiny možností kategorie** a přiřaďte je.

5.  Klikněte **Uložit**.

### Pro datové sady použijte kombinace kategorií { #use_category_combo_for_data_set }

Pokud kategorie a kombinace kategorií mají typ datové dimenze "Atribut", mohou použít společnou sadu atributů na související sadu datových hodnot obsažených v datové sadě. Jsou-li jako atribut použity kombinace kategorií, slouží jako další dimenze (podobně jako „Období“ a „Organizační jednotka“), které můžete použít ve své analýze.

Předpokládejme, že nevládní organizace poskytuje služby ART v daném zařízení. Budou muset každý měsíc podávat zprávu o „měsíčním souhrnu ART“, který by obsahoval řadu datových prvků. Nevládní organizace a projekt by se mohly časem změnit. Chcete-li kdykoli přiřadit data dané nevládní organizaci a projektu, musíte tyto informace zaznamenat ke každé hodnotě dat v okamžiku zadání dat.

1.  Vytvořte dvě kategorie s typem datové dimenze „Atribut“: „Implementující partner“ a „Projekty“.

2.  Vytvořte kombinaci kategorií s typem datové dimenze "Atribut": "Implementace partnerů a projektů".

3.  Přiřaďte vytvořené kategorie ke kombinaci kategorií.

4.  Vytvořte datovou sadu nazvanou „ART měsíční souhrn“ a vyberte kombinaci kategorií „Implementace partnerů a projektů“.

Když zadáváte data v aplikaci **Zadávání dat**, můžete vybrat „Implementační partner“ a „Projekt“. Každé zaznamenané hodnotě dat je jako atribut přiřazena konkrétní kombinace těchto kategorií. Tyto atributy (pokud jsou zadány jako dimenze) lze použít v analytických aplikacích podobně jako v jiných dimenzích, například v období a organizační jednotce.

![](resources/images/maintainence/categories_dataset_attributes.png)

### Přiřaďte kód kombinaci možností kategorie { #assign_code_category_option_combo }

Kombinacím možností kategorií můžete přiřadit kód. To usnadňuje výměnu dat mezi DHIS2 a externími systémy. Systém vytváří kombinace možností kategorií automaticky.

1.  Otevřete aplikaci **Údržba** a klikněte na **Kategorie** \> **Kombinace možností kategorie**.

2.  V seznamu najděte objekt, který chcete upravit.

3.  Klikněte na nabídku možností a vyberte **Upravit**.

4.  Zadejte kód.

5.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Správa datových prvků { #manage_data_element }

### O datových prvcích { #about_data_element }

Datové prvky jsou základem DHIS2. Datové prvky definují, co se ve skutečnosti skutečně zaznamenává v systému, například počet imunizací nebo počet případů malárie.

Datové prvky, jako je „Počet případů potvrzené malárie“, jsou často rozděleny na menší části, aby se určil například počet potvrzených případů malárie u konkrétních věkových skupin.

V aplikaci **Údržba** spravujete následující objekty datových prvků:

<table>
<caption> Objekty datových prvků v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Datový prvek </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> skupina datových prvků </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> Sada skupiny datových prvků </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Pracovní postup { #workflow_data_element }

1.  Vytvořte všechny možnosti kategorií.

2.  Vytvořte kategorie složené z několika možností kategorií, které jste vytvořili.

3.  Vytvářejte kombinace kategorií složené z jedné nebo více kategorií.

4.  Vytvořte datové prvky a přiřaďte je ke kombinaci kategorií.

### Vytvořte nebo upravte datový prvek { #create_data_element }

![](resources/images/maintainence/create_data_element.png)

1.  Otevřete aplikaci **Údržba** a klikněte na **Datové prvky** \> **Datový prvek**.

2.  Klikněte na tlačítko Přidat.

3.  V poli **Název** definujte přesný název datového prvku.

    Každý datový prvek musí mít jedinečný název.

4.  V poli **Krátký název** definujte krátký název pro datový prvek.

    Krátký název je obvykle zkratkou celého názvu datového prvku. Tento atribut se často používá v sestavách k zobrazení názvu datového prvku, kde je omezený prostor.

5.  (Volitelné) V poli **Kód** přiřaďte kód.

    V mnoha zemích je datovým prvkům přiřazen kód.

6.  (Volitelné) V poli **Barva** přiřaďte barvu, která bude použita pro tento datový prvek v aplikacích pro sběr dat.

7.  (Volitelné) V poli **Ikona** přiřaďte ikonu, která bude použita pro tento datový prvek v aplikacích pro sběr dat.

8.  Do pole **Popis** zadejte popis datového prvku. Buďte co nejpřesnější a uveďte úplné informace o tom, jak se datový prvek měří a jaký je jeho účel.

9.  (Volitelné) V poli **Maska pole** můžete zadat šablonu, která slouží k poskytování rad pro správné formátování datového prvku.

    > **NOTE**
    >
    > So far this is only implemented in the DHIS2 Android Capture app; not in the Capture and Tracker Capture web apps.

    Následují speciální znaky, které lze v masce použít. Speciální znaky odpovídají přesně jednomu znaku daného typu.

    | Znak | Odpovídá                        |
    | --------- | -------------------------- |
    | \\d       | číslice                      |
    | \\x       | malé písmeno          |
    | \\X       | velké písmeno            |
    | \\ w        | jakýkoli alfanumerický znak |

    Vzor lze například použít k zobrazení pomlček podle potřeby ve vstupním poli datového prvku. Např. "\d\d\d-\d\d\d-\d\d\d, zobrazí spojovník pro každou třetí číslici.

10. Do pole **Název formuláře** zadejte alternativní název datového prvku. Tento název lze použít buď v sekci, nebo ve formulářích pro automatické zadávání dat. Název formuláře se použije automaticky.

11. V poli **Typ domény** vyberte, zda je datový prvek agregovaný nebo sledovací typ datového prvku.

12. V poli **Typ hodnoty** vyberte typ dat, který bude datový prvek zaznamenávat.

    <table>
    <caption>Value types</caption>
    <colgroup>
    <col style="width: 53%" />
    <col style="width: 46%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Value type</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Age</p></td>
    <td><p>-</p></td>
    </tr>
    <tr class="even">
    <td><p>Coordinate</p></td>
    <td><p>A point coordinate specified as longitude and latitude in decimal degrees. All coordinate should be specified in the format &quot;-19.23 , 56.42&quot; with a comma separating the longitude and latitude.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Date</p></td>
    <td><p>Dates rendered as calendar widget in data entry.</p></td>
    </tr>
    <tr class="even">
    <td><p>Date &amp; time</p></td>
    <td><p>Is a combination of the <strong>DATE</strong> and <strong>TIME</strong> data elements.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Email</p></td>
    <td><p>Email.</p></td>
    </tr>
    <tr class="even">
    <td><p>File</p></td>
    <td><p>A file resource where you can store external files, for example documents and photos.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Image</p></td>
    <td><p>A file resource where you can store photos.</p>
    <p>Unlike the <strong>FILE</strong> data element, the <strong>IMAGE</strong> data element can display the uploaded image directly in forms.</p></td>
    </tr>
    <tr class="even">
    <td><p>Integer</p></td>
    <td><p>Any whole number (positive and negative), including zero.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Letter</p></td>
    <td><p>A single letter.</p></td>
    </tr>
    <tr class="even">
    <td><p>Long text</p></td>
    <td><p>Textual value. Renders as text area with no length constraint in forms.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Negative integer</p></td>
    <td><p>Any whole number less than (but not including) zero.</p></td>
    </tr>
    <tr class="even">
    <td><p>Number</p></td>
    <td><p>Any real numeric value with a single decimal point. Thousands separators and scientific notation is not supported.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Percentage</p></td>
    <td><p>Whole numbers inclusive between 0 and 100.</p></td>
    </tr>
    <tr class="even">
    <td><p>Phone number</p></td>
    <td><p>Phone number.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Positive integer</p></td>
    <td><p>Any whole number greater than (but not including) zero.</p></td>
    </tr>
    <tr class="even">
    <td><p>Positive of zero integer</p></td>
    <td><p>Any positive whole number, including zero.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Organisation unit</p></td>
    <td><p>Organisation units rendered as a hierarchy tree widget.</p>
    <p>If the user has assigned &quot;search organisation units&quot;, these will be displayed instead of the assigned organisation units.</p></td>
    </tr>
    <tr class="even">
    <td><p>Unit interval</p></td>
    <td><p>Any real number greater than or equal to 0 and less than or equal to 1.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Text</p></td>
    <td><p>Textual value. The maximum number of allowed characters per value is 50,000.</p></td>
    </tr>
    <tr class="even">
    <td><p>Time</p></td>
    <td><p>Time is stored in HH:mm format.</p>
    <p>HH is a number between 0 and 23</p>
    <p>mm is a number between 00 and 59</p></td>
    </tr>
    <tr class="odd">
    <td><p>Tracker associate</p></td>
    <td><p>Tracked entity instance. Rendered as dialog with a list of tracked entity instances and a search field.</p></td>
    </tr>
    <tr class="even">
    <td><p>Username</p></td>
    <td><p>DHIS2 user. Rendered as a dialog with a list of users and a search field. The user will need the "View User" authority to be able to utilise this data type</p></td>
    </tr>
    <tr class="odd">
    <td><p>Yes/No</p></td>
    <td><p>Boolean values, renders as drop-down lists in data entry.</p></td>
    </tr>
    <tr class="even">
    <td><p>Yes only</p></td>
    <td><p>True values, renders as check-boxes in data entry.</p></td>
    </tr>
    </tbody>
    </table>

13. V poli **Typ agregace** vyberte výchozí agregační operaci, která se použije u datového prvku.

    Většina datových prvků by měla mít operátor **Sum**. To zahrnuje všechny datové prvky, které by se měly sečíst. Jiné datové prvky, například úrovně zaměstnanců, by měly být nastaveny tak, aby používaly operátor **Průměr**, kdy by hodnoty podél časové dimenze neměly být sčítány, ale spíše zprůměrovány.

    <table>
    <caption>Aggregation operators</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Aggregation operator</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Average</p></td>
    <td><p>Average the values in both the period as and the organisation unit dimensions.</p></td>
    </tr>
    <tr class="even">
    <td><p>Average (sum in organisation unit hierarchy)</p></td>
    <td><p>Average of data values in the period dimension, sum in the organisation unit dimensions.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Count</p></td>
    <td><p>Count of data values.</p></td>
    </tr>
    <tr class="even">
    <td><p>Min</p></td>
    <td><p>Minimum of data values.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Max</p></td>
    <td><p>Maximum of data values.</p></td>
    </tr>
    <tr class="even">
    <td><p>None</p></td>
    <td><p>No aggregation is performed in any dimension.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Sum</p></td>
    <td><p>Sum of data values in the period and organisation unit dimension.</p></td>
    </tr>
    <tr class="even">
    <td><p>Standard deviation</p></td>
    <td><p>Standard deviation (population-based) of data values.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Variance</p></td>
    <td><p>Variance (population-based) of data values.</p></td>
    </tr>
    </tbody>
    </table>

14. Chcete-li z určitého důvodu uložit nuly, vyberte možnost **Uložit nulové hodnoty dat**. Ve výchozím nastavení DHIS2 neukládá nuly zadané v modulu zadávání dat.

15. Do pole **URL** zadejte odkaz na podrobný popis datového prvku.

    Například odkaz na úložiště metadat nebo registr, který obsahuje podrobné technické informace o definici a měření datového prvku.

16. V poli **kombinace kategorií** definujte, jakou kombinaci kategorie má mít datový prvek. Toto se také nazývá „rozčlenění“.

17. Vyberte **sadu možností**.

    Sady možností jsou předdefinované seznamy možností, které lze použít při zadávání dat.

18. Vyberte **možnost nastavenou pro komentáře**.

    Sady možností pro komentáře jsou předdefinované seznamy možností, které lze použít k určení standardizovaných komentářů k datovým hodnotám při zadávání dat.

19. Přiřaďte jednu nebo více **legend**.

    Legendy se používají například v aplikaci **Mapy** k zobrazení určitých datových prvků s určitými ikonami.

20. Nastavením **úrovní agregace** umožníte agregaci datového prvku na jedné nebo více úrovních:

    1.  V levém podokně vyberte úrovně, které chcete přiřadit datovému prvku.

    2.  Kliknutím na šipku doprava přiřadíte úrovně agregace.

    Ve výchozím nastavení začne agregace od nejnižší přiřazené organizační jednotky. Pokud například vyberete „Obec“, znamená to, že agregáty „Obec“, „Okres“ a „Stát“ používají jako zdroj dat „Obec“ (nejvyšší dostupná úroveň agregace) a data PHU nebudou zahrnuta. Data PHU budou stále k dispozici pro úroveň PHU, ale nebudou zahrnuta v agregacích na výše uvedené úrovně.

    Pokud vyberete jak „Okres“, tak „Náčelník“, znamená to, že agregáty na úrovni „Okres“ a „Národní“ používají jako zdroj údaje okresu, „Náčelník“ použije náčelník a „PHU“ použije PHU.

21. Pokud je to možné, zadejte hodnoty vlastních atributů, například **Klasifikace** nebo **Metoda sběru**.

    > **Note**
    >
    > You create custom attributes in the **Maintenance** app: **Other** > \> **Attributes**.

22. Pokud je to možné, vyberte povinné skupiny datových prvků, například **Hlavní skupina datových prvků** nebo **Data založená na trasovači**.

    > **Note**
    >
    > You'll only see data element group sets in this form if you've created them and set them to **Compulsory**.
    >
    > You create data element group sets in the **Maintenance** app: **Data element** \> **Date element group set**.

23. Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu datových prvků { #create_data_element_group }

Skupiny datových prvků umožňují klasifikovat související datové prvky do společného tématu. Například dva datové prvky „Imunizace proti spalničkám“ a „BCG Imunizace“ lze seskupit do skupiny datových prvků „Dětská imunizace“.

Vytvoření skupiny datových prvků:

1.  Otevřete aplikaci **Údržba** a klikněte na **Datové prvky** \> **Skupina datových prvků**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Krátký název**

    3.  **Kód**

4.  Vyberte datové prvky a přiřaďte je.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte sadu skupin datových prvků { #create_data_element_group_set }

Sady skupin datových prvků umožňují kategorizovat více skupin datových prvků do sady. Systém používá skupiny skupin datových prvků během analýzy a vytváření sestav ke kombinování podobných skupin datových prvků do společného tématu. Skupina datových prvků může být součástí několika sad skupin datových prvků.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datové prvky** \> **Sada skupin datových prvků**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Kód**

    3.  **Popis**

    4.  **Povinný**

    5.  **Datová dimenze**

4.  Vyberte skupiny datových prvků a přiřaďte je.

    Dostupné skupiny datových prvků se zobrazují na levém panelu. Skupiny datových prvků, které jsou aktuálně členy skupiny datových prvků, se zobrazují na pravém panelu.

5.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte datové sady a formuláře pro zadávání dat { #manage_data_set }

### O datových sadách a formulářích pro zadávání dat { #about_dataset_dataform }

Veškeré zadávání dat v DHIS2 je uspořádáno do datových sad. Datová sada je kolekce datových prvků seskupených pro zadávání a export dat mezi instancemi DHIS2. Chcete-li použít datovou sadu ke shromažďování dat pro konkrétní organizační jednotku, musíte přiřadit organizační jednotku k datové sadě. Jakmile přiřadíte datovou sadu organizační jednotce, je tato datová sada k dispozici v aplikaci **Zadávání dat**. Datové sady mohou pro zadávání dat používat pouze organizační jednotky, kterým jste přiřadili datovou sadu.

Kombinace kategorií může odkazovat na datové prvky i datové sady. Pokud pro datovou sadu používáte kombinaci kategorií, lze kombinace kategorií použít pro celý formulář. To znamená, že můžete použít kategorie k zachycení informací, které jsou společné pro celý formulář, například název projektu nebo grantu. Když je datová sada propojena s kombinací kategorií, tyto kategorie se zobrazí jako rozevírací pole v aplikaci **Zadávání dat**. Data zachycená ve formuláři budou poté propojena s vybranými možnostmi kategorie z těchto rozevíracích polí. Informace o tom, jak vytvořit kategorie a kombinace kategorií, najdete v části „Správa datových prvků a kategorií“. Ujistěte se, že jste nastavili typ kategorií a kombinací kategorií na „Atribut“.

Scénář, kdy jsou kategorie užitečné, je, když potřebujete zachytit formulář pro zadávání dat pro implementující partnerskou organizaci a projekt. V tom případě:

1.  Vytvořte možnosti kategorií a kategorie pro všechny partnerské organizace a projekty a propojte je v nové kombinaci kategorií.

2.  Přiřaďte kombinaci kategorií k datové sadě (formuláři), pro kterou potřebujete tyto informace zachytit.

    Při otevírání této datové sady v modulu zadávání dat se kategorie partnerské organizace a projektu automaticky vykreslí jako rozevírací seznamy, což vám umožní vybrat konkrétní implementující partnerskou organizaci a projekt, než budete pokračovat v zadávání dat.

Sady dat můžete vytvářet a upravovat v aplikaci **Údržba**. Zde například definujete, které datové prvky chcete zahrnout do datové sady a frekvenci sběru dat.

Data zadáváte v aplikaci **Zadávání dat**. Aplikace **Zadávání dat** používá k zadávání datových formulářů formuláře pro zadávání dat. Existují tři typy formulářů pro zadávání údajů:

<table>
<caption> typy formulářů pro zadávání dat </caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th> typ formuláře pro zadávání dat </th>
<th> Popis </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Výchozí forma </p> </td>
<td> <p> Jakmile přiřadíte datovou sadu organizační jednotce, automaticky se vytvoří výchozí formulář. Výchozí formulář je poté k dispozici v aplikaci <strong> Zadávání dat </strong> pro organizační jednotky, kterým jste jej přiřadili. </p>
<p> Výchozí formulář se skládá ze seznamu datových prvků patřících k datové sadě a sloupce pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s jinou než výchozí kombinací kategorií, například věkové skupiny nebo pohlaví, vytvoří se automaticky další sloupce ve výchozím formuláři na základě různých kategorií. </p>
<p> Pokud používáte více než jednu kombinaci kategorií, získáte více sloupců ve výchozím formuláři s různými záhlavími sloupců pro možnosti. </p> </td>
</tr>
<tr class="even">
<td> <p> Formulář sekce </p> </td>
<td> <p> Pokud výchozí formulář nesplňuje vaše potřeby, můžete jej upravit a vytvořit formulář oddílu. Formuláře oddílů vám dávají větší flexibilitu, pokud jde o používání tabulkových formulářů. </p>
<p> Ve formuláři sekce můžete například vytvořit více tabulek s podnadpisy a deaktivovat (šedě) buňky v tabulce. </p>
<p> Když jste do sady dat přidali formulář oddílu, formulář oddílu je k dispozici v aplikaci <strong> Zadání dat </strong>. </p> </td>
</tr>
<tr class="odd">
<td> <p> Vlastní formulář </p> </td>
<td> <p> Pokud je formulář, který chcete navrhnout, příliš komplikovaný pro výchozí nebo oddílové formuláře, můžete vytvořit vlastní formulář. Vytvoření vlastního formuláře trvá déle než formuláře oddílu, ale nad návrhem máte plnou kontrolu. </p>
<p> Můžete například napodobit existující formulář agregace papíru pomocí vlastního formuláře. To usnadňuje zadávání dat a mělo by se snížit počet nesprávně zadaných datových prvků. </p>
<p> Když jste do sady dat přidali vlastní formulář, je vlastní formulář k dispozici v aplikaci Data <strong> Data </strong>. </p> </td>
</tr>
</tbody>
</table>

> **Poznámka**
>
> Pokud má datová sada formulář sekce i vlastní formulář, zobrazí systém během zadávání dat vlastní formulář. Uživatelé, kteří zadávají data, si nemohou vybrat, jaký formulář chtějí použít. Při zadávání dat z webu je pořadí preferencí zobrazení:
>
> 1. Vlastní formulář (pokud existuje)
>
> 2. Formulář sekce (pokud existuje)
>
> 3. Výchozí formulář
>
> Mobilní zařízení nepodporují vlastní formuláře. Při zadávání dat na mobilních zařízeních je pořadí preferencí zobrazení:
>
> 1. Formulář sekce (pokud existuje)
>
> 2. Výchozí formulář

V aplikaci **Údržba** spravujete následující objekty sady dat:

<table>
<caption> Objekty datové sady v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Datová sada </p> </td>
<td> <p> Vytvořit, přiřadit organizačním jednotkám, upravit, sdílet, mazat, zobrazit podrobnosti a přeložit </p>
<p> Úprava povinných datových prvků </p>
<p> Přidat a odebrat více datových sad do organizačních jednotek najednou </p> </td>
</tr>
<tr class="even">
<td> <p> Formulář sekce </p> </td>
<td> <p> Vytváření, úpravy a správa šedých polí </p> </td>
</tr>
<tr class="odd">
<td> <p> sekce </p> </td>
<td> <p> Změnit pořadí zobrazení, mazat a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> Vlastní formulář </p> </td>
<td> <p> Vytvořit, upravit a skriptovat </p> </td>
</tr>
</tbody>
</table>

### Pracovní postup { #workflow_data_set }

Abyste mohli vytvářet datové sady a formuláře pro zadávání dat, musíte mít datové prvky a kategorie.

1.  Vytvořte datovou sadu.

2.  Přiřaďte datovou sadu organizačním jednotkám.

    Výchozí formulář se vytvoří automaticky.

3.  Vytvořte formulář sekce nebo vlastní formulář.

    Nyní můžete data zaregistrovat v aplikaci **Zadávání dat**.

### Vytvořte nebo upravte datovou sadu { #create_data_set }

![](resources/images/datasets/data_set_create.png)

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte přesný název datové sady.

4.  V poli **Krátký název** definujte krátký název datové sady.

    Krátký název je obvykle zkratkou názvu celé sady dat. Tento atribut se často používá k zobrazení názvu datové sady, kde je omezený prostor.

5.  (Volitelné) V poli **Kód** přiřaďte kód.

6.  Do pole **Popis** zadejte popis datové sady.

7.  Zadejte číslo **Dnů platnosti**.

    Počet dnů vypršení termínu určuje, jak dlouho by mělo být možné pro tuto sadu dat zadávat data do aplikace **Zadávání dat**. Dny vypršení termínu se vztahují k počtu dní po datu ukončení vybraného období pro zadávání údajů, kdy by měl být formulář pro zadávání údajů otevřen pro vstup. Po uplynutí počtu dní bude soubor dat uzamčen pro další zadávání.

    K tomu můžete nastavit ruční výjimky pomocí funkce výjimky zámku v aplikaci **Správa Dat**.

    > **Note**
    >
    > To allow data entry into all possible historical time periods, set the number of expiry days to zero.

8.  Pokud chcete, aby bylo možné zadávat data pro budoucí období, zadejte počet období do pole **Otevřít budoucí období pro zadávání dat**.

    Hodnota je počet budoucích období, která jsou k dispozici pro zadávání údajů.

    U měsíčního datového souboru vám hodnota 2 umožňuje zadávat data na 2 měsíce předem. To je užitečné například pro údaje o populaci, cíli a plánování.

9.  Do pole **Dny po období, kdy se chcete kvalifikovat pro včasné odeslání**, zadejte počet dní, ve kterých lze zadat údaje, aby byly považovány za nahlášené včas.

    Chcete-li ověřit počet včasných odeslaných přehledů, přejděte do části **Přehledy** \> **Souhrn míry přehledů**.

10. Vyberte **Typ období**.

    Typ období definuje frekvenci hlášení pro konkrétní soubor dat. Četnost může být například denní, čtvrtletní nebo roční.

11. Vyberte **kombinaci kategorií** a přiřaďte ji k datové sadě.

    > **Tip**
    >
    > Click **Add new** to create category combinations that you're missing. In the form that opens, create the category combinations you need. When you're done, click **Refresh values**.

12. V seznamu **Oznámení příjemci o dokončení** vyberte skupinu uživatelů, která by měla obdržet zprávu, když je sada dat v aplikaci **Zadávání dat** označena jako úplná.

    Zpráva je doručena prostřednictvím systému doručování zpráv DHIS2.

13. Pokud chcete, aby uživatel, který zadal data, obdržel zprávu, když bude sada dat v aplikaci **Zadávání dat** označena jako úplná, vyberte **Odeslat oznámení dokončujícímu uživateli**.

    Zpráva je doručena prostřednictvím systému doručování zpráv DHIS2.

14. Je-li to možné, vyberte **pracovní postup schválení dat**.

15. Pokud chcete, aby bylo možné použít datovou sadu v aplikaci Java mobile DHIS2, vyberte **Povolit pro mobilního klienta Java**.

16. Pokud chcete, aby bylo vyplnění všech hodnot pro datový prvek v zadávání dat povinné, pokud byla vyplněna jedna nebo více hodnot, vyberte **Všechna pole pro datové prvky jsou povinné**.

    To znamená, že pokud zadáte jednu datovou hodnotu pro datový prvek do vstupního pole (tj. Pro kombinaci možnosti kategorie), musíte zadat data pro všechna pole patřící k danému datovému prvku (tj. Všechny kombinace možností kategorie).

17. Pokud chcete, aby bylo možné označit formulář pro zadávání dat jako úplný pouze v případě, že je ověření tohoto formuláře úspěšné, vyberte **Dokončení povoleno, pouze pokud ověření proběhne**.

    Pokud vyberete tuto možnost, nemůžete označit formulář jako úplný, pokud se ověření nezdaří.

18. Chcete-li, aby bylo povinné, aby všechny chybějící hodnoty vyžadovaly komentář, který by ospravedlnil jejich nepřítomnost, vyberte **Chybějící hodnoty vyžadují komentář po dokončení**.

19. (Volitelné) Přiřaďte jednu nebo více **legend**.

20. Pokud je to možné, vyberte **Přeskočit offline**.

    Tato možnost určuje, zda má být tento formulář pro zadávání údajů stažen a uložen ve webovém prohlížeči uživatele. Za normálních okolností byste neměli vybrat možnost **Přeskočit offline**. Toto je výchozí nastavení. Pokud máte velké formuláře, které se zřídka používají, můžete zvážit výběr této možnosti, abyste urychlili počáteční načítání v modulu zadávání dat.

21. Pokud je to možné, vyberte **Dekorace datového prvku**

    Pokud vyberete tuto možnost, budou se popisy datových prvků vykreslovat ve výzvách stažených datových sad v offline režimu v aplikaci **Zadávání dat**.

22. Pokud je to možné, vyberte **Vykreslit sekce jako karty**.

    Tato možnost je použitelná pouze pro formuláře oddílů. Tato možnost umožňuje vykreslit každou sekci jako záložku vodorovně nad datovou sadou. To je užitečné pro dlouhé datové sady, protože umožňuje rychlý výběr příslušných sekcí bez nutnosti procházet celým formulářem.

23. Pokud je to možné, vyberte **Vykreslit svisle**.

    Tato možnost je použitelná pouze pro formuláře oddílů.

24. Vyberte datové prvky a přiřaďte je.

    Kombinaci kategorií pro každou vybranou datovou sadu můžete přepsat kliknutím na ikonu ozubeného kola nad seznamem vybraných datových prvků. To vám umožní použít konkrétní kombinaci kategorií (rozčlenění) v aktuální datové sadě namísto kombinace kategorií přidružené přímo k samotnému datovému prvku.

25. Vyberte indikátory a přiřaďte je.

26. Ve stromu organizační jednotky vyberte organizační jednotky, kterým chcete přiřadit datovou sadu.

    > **Tip**
    >
    > -   Click **Organisation unit level** to select all organisation units that belong to a certain organisation level.
    >
    > -   Click **Organisation unit group** to select all organisation units that belong to a certain organisation unit group.

27. Klikněte **Uložit**.

Nyní můžete použít datovou sadu v aplikaci **Zadávání dat** pro organizační jednotky, které jste přiřadili, a pro období podle vybrané frekvence (typ období).

### Vytvořit nebo upravit oznámení sady dat { #create_data_set_notification }

1.  Otevřete aplikaci **Údržba** a klikněte na **Sada dat** \> **Oznámení sady dat**.

2.  Klikněte na tlačítko Přidat.

#### Co poslat? { #what-to-send }

![](resources/images/datasets/dataset_notification_create.png)

1.  Do pole **Název** zadejte přesný název oznámení sady dat.

2.  (Volitelné) V poli **Kód** přiřaďte kód.

3.  Zadejte **datové sady**.

    Tyto datové sady budou přidruženy k tomuto oznámení. V případě, že je některý z nich dokončen na určité období a organizační jednotku, systém vygeneruje oznámení.

    > **Note**
    >
    > Nothing will happen if no data set is selected

4.  V části **Šablona zprávy** jsou dva parametry.

    -   **Šablona předmětu** předmět oznámení zaslaného v oznámení. Může mít hodnoty ze seznamu proměnných, které jsou k dispozici na pravé straně.

    -   **Šablona zprávy** skutečné zprávy odeslána v oznámení. Může mít hodnoty ze seznamu proměnných, které jsou k dispozici na pravé straně.

    > **Note**
    >
    > Subject is only relevant in case of Email and internal DHIS2 messages. It is ignored in case of SMS.

#### Kdy poslat? { #when-to-send }

![](resources/images/datasets/when_to_send.png)

1.  **Spouštěč oznámení sady dat** pole určuje, kdy se má oznámení odeslat.

    -   **Dokončení datové sady** spustí upozornění, jakmile je datová sada dokončena.

    -   **Plánované Dny** naplánuje oznámení na základě počtu dní ve vztahu k naplánovanému datu. O datu harmonogramu rozhodne období spojené s datovou sadou.

        -   **Odeslat oznámení jako** poskytuje dva různé typy oznámení

            -   **Celkové shrnutí** Odeslat oznámení v celkové náladě

            -   **Jedno oznámení** odesílá oznámení v jedné náladě

    > **Note**
    >
    > **Send notification as** option is only available in case of scheduled notification. This option is set to default which is **Single notification** in case of completion notification

#### Komu poslat? { #who-to-send }

![](resources/images/datasets/who_to_send.png)

1.  **Příjemce oznámení** pole určuje příjemce oznámení.

    -   **Kontakt na organizační jednotku** odešle oznámení kontaktu přiřazenému organizační jednotce, ze kterého byla data shromážděna.

    -   **UserGroup** zašle oznámení všem členům vybrané Skupiny Uživatelů

    > **Note**
    >
    > An internal DHIS2 message will be sent in case if recipient is UserGroup. Moreover user will also receive SMS/EMAIL if phone number and email address exist for that user and SMS/EMAIL notifications are enabled in SystemSettings

### Přepsat kombinace kategorií datových prvků v datové sadě { #override_dataelement_catcombo_in_dataset }

Můžete přepsat kombinaci kategorií, která se má použít pro datový prvek v kontextu datové sady. To znamená, že datový prvek může používat různé kombinace kategorií v rámci různých datových sad. To je užitečné, pokud chcete znovu použít datový prvek, protože nemusíte replikovat datový prvek, abyste povolili více kombinací kategorií.

Pokud různé regiony v hierarchii organizační jednotky používají různé rozčlenění nebo se rozčlenění v průběhu času mění, můžete to vyjádřit vytvořením různých datových sad s příslušnými kombinacemi kategorií.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, kterou chcete upravit.

3.  Klikněte na nabídku možností a vyberte **Upravit**.

4.  Přejděte do části datové prvky a klikněte na ikonu klíče.

5.  Vyberte nové kombinace kategorií a klikněte na **Zavřít**.

6.  Klikněte **Uložit**.

### Upravte povinné datové prvky v datové sadě { #edit_compulsory_dataelement_in_dataset }

Můžete přidat nebo odebrat datové prvky, které budou během zadávání dat označeny jako povinné.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, kterou chcete upravit.

3.  Klikněte na nabídku možností a vyberte **Upravit povinné datové prvky**.

4.  Přiřaďte povinné datové prvky.

5.  Klikněte **Uložit**.

### Stáhněte si výchozí datové formuláře ve formátu PDF { #download_defaultform_pdf }

Můžete si stáhnout výchozí data z formátu PDF pro zadávání dat offline.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte objekt, který chcete stáhnout.

3.  Klikněte na nabídku možností a vyberte **Získat PDF pro zadávání dat**.

### Spravovat formuláře sekcí { #manage_section_form }

#### Vytvořte formulář sekce { #create-a-section-form }

Formuláře sekcí jsou automaticky odděleny kombinacemi kategorií datových prvků, které vytvářejí tabulkový procesor jako formulář pro zadávání dat pro každou sekci.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete vytvořit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Spravovat sekce**.

4.  Klikněte na tlačítko Přidat.

5.  (Volitelné) Do pole **Název** zadejte název sekce.

6.  (Volitelné) Do pole **Popis** zadejte popis sekce.

7.  (Volitelné) Chcete-li během zadávání dat zobrazit součty řádků ve formuláři sekce, vyberte **Zobrazit součty řádků**.

8.  (Volitelné) Chcete-li během zadávání dat zobrazit součty sloupců ve formuláři sekce, vyberte **Zobrazit součty sloupců**.

9.  Přiřaďte datové prvky do sekce:

    1.  (Volitelné) Vyberte **kombinovaný filtr kategorie**.

        > **Note**
        >
        > You can only use one category combination per section.

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Option</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><strong>None</strong></p></td>
        <td><p>Displays all data elements that don't have a category combination.</p></td>
        </tr>
        <tr class="even">
        <td><p><strong>&lt;No filter&gt;</strong></p></td>
        <td><p>Displays all data elements.</p></td>
        </tr>
        </tbody>
        </table>

    2.  Vyberte datové prvky a přiřaďte je.

10. (Volitelné) Seřadit datové prvky v sekci pomocí šipek nahoru a dolů nalevo od pole přiřazených datových prvků.

11. Klikněte **Uložit**.

12. Opakujte kroky přidání sekce pro každou sekci, kterou chcete mít ve formuláři sekce.

    V aplikaci **Zadávání dat** nyní můžete použít formulář sekce. Formulář sekce se zobrazí automaticky, když jsou k dispozici sekce pro vybranou sadu dat. Datové sady, které mají formuláře sekcí, automaticky zobrazí formulář sekce.

Všimněte si, jak byla každá kategorie datových prvků rozdělena do samostatné sekce a systém automaticky vygeneroval tabulku zadávání dat. Použití formulářů sekcí v kombinaci s kategoriemi datových prvků může drasticky zkrátit dobu potřebnou k vytvoření formulářů pro zadávání dat pro datové sady.

![](resources/images/dhis2UserManual/section_form.png)

#### Upravte formulář sekce { #edit-a-section-form }

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete upravit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Spravovat sekce**.

4.  V seznamu vyhledejte část, kterou chcete upravit.

5.  Klikněte na nabídku možností a vyberte **Upravit**.

6.  Upravte sekci a klikněte na **Uložit**.

7.  Opakujte kroky úprav sekce pro každou sekci, kterou chcete upravit.

#### Spravujte šedá pole ve formuláři sekce { #manage-grey-fields-in-a-section-form }

Můžete zakázat datové prvky a možnosti kategorií pro zadávání dat. To znamená, že během zadávání dat nebude možné do těchto polí zadávat data.

![](resources/images/datasets/section_form_grey_fields.png)

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete upravit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Spravovat sekce**.

4.  V seznamu vyhledejte část, kterou chcete upravit.

5.  Klikněte na nabídku možností a vyberte **Správa šedých polí**.

6.  Vyberte pole, která chcete deaktivovat.

    > **Note**
    >
    > If you've sections that contain data elements assigned to multiple category combinations, switch between the category combinations to view all fields.

7.  Klikněte **Uložit**.

#### Změňte pořadí zobrazení sekcí ve formuláři sekce { #change-section-display-order-in-a-section-form }

Můžete určit, ve kterém pořadí sekcí se zobrazí ve formuláři sekce.

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete upravit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Spravovat sekce**.

4.  V seznamu vyhledejte část, kterou chcete přesunout.

5.  Klikněte na nabídku možností a vyberte **Posunout nahoru** nebo **Posunout dolů**.

    Pokud je sekce, kterou chcete přesunout, první nebo poslední sekcí v seznamu, zobrazí se pouze jedna z možností přesunu.

#### Odstraňte sekci ve formuláři sekce { #delete-a-section-in-a-section-form }

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete upravit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Spravovat sekce**.

4.  V seznamu vyhledejte část, kterou chcete odstranit.

5.  Klikněte na nabídku možností a vyberte **Odstranit**.

#### Přeložit sekci ve formuláři sekce { #translate-a-section-in-a-section-form }

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada** \> **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, pro kterou chcete upravit formulář sekce.

3.  Klikněte na nabídku možností a vyberte **Přeložit**.

4.  Vyberte národní prostředí.

5.  Zadejte požadované informace.

6.  Klikněte na **Zavřít**.

### Spravujte vlastní formuláře { #manage_customform }

#### Vytvořte vlastní formulář { #create-a-custom-form }

Navrhujete vlastní formuláře ve vestavěném editoru HTML WYSIWYG. Pokud vyberete **Zdroj**, můžete vložit HTML kód přímo do editační oblasti. Úplný návod, jak editor používat, najdete v dokumentu <http://docs.ckeditor.com/>.

![](resources/images/datasets/data_set_custom_form_create.png)

Vytvoření vlastního formuláře:

1.  Otevřete aplikaci **Údržba** a klikněte na **Datová Sada**.

2.  V seznamu vyhledejte datovou sadu, do které chcete přidat vlastní formulář.

3.  Klikněte na nabídku možností a vyberte **Návrh formuláře pro zadání dat**.

4.  V editační oblasti vytvořte vlastní formulář.

    -   Poklepáním na objekt v levém seznamu jej vložíte do formuláře.

    -   Pokud již máte kód HTML pro svůj formulář, klikněte na **Zdroj** a vložte kód.

5.  Vyberte **styl zobrazení formuláře**.

6.  Klikněte **Uložit**.

#### Skriptování ve vlastních formulářích { #scripting-in-custom-forms }

Ve formuláři pro zadávání vlastních dat můžete použít JavaScript k vytvoření dynamického chování a přizpůsobení. Jako příklad můžete skrýt oddíly formuláře na základě konkrétního vstupu uživatele pro datové prvky nebo zobrazit konkrétní informace při načtení formuláře.

##### Události { #events }

Modul pro zadávání dat DHIS2 poskytuje řadu událostí, pro které se můžete zaregistrovat a použít k provedení akcí v určitých časech. Události jsou registrovány na prvku dokumentu. Objekt události jQuery a identifikátor datové sady jsou vždy první dva argumenty poskytované funkcím zpětného volání. Tabulka níže poskytuje přehled událostí a kdy jsou spuštěny.

<table>
<caption> zadávání dat Událostí </caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 39%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th> klíč </th>
<th> Popis </th>
<th> Argumenty </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> dhis2.de.event.formLoaded </p> </td>
<td> <p> Spustí se po vykreslení formuláře pro zadávání dat, ale před nastavením datových hodnot do vstupních polí. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="even">
<td> <p> dhis2.de.event.dataValuesLoaded </p> </td>
<td> <p> Spustí se po nastavení datových hodnot do vstupních polí. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="odd">
<td> <p> dhis2.de.event.formReady </p> </td>
<td> <p> Spustí se, když je formulář pro zadávání dat zcela vykreslen a načten se všemi prvky. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="even">
<td> <p> dhis2.de.event.dataValueSaved </p> </td>
<td> <p> Spustí se, když je datová hodnota úspěšně uložena. </p> </td>
<td> <p> Událost | ID souboru dat | Objekt datové hodnoty </p> </td>
</tr>
<tr class="odd">
<td> <p> dhis2.de.event.com dokončeno </p> </td>
<td> <p> Spustí se, když je datová sada úspěšně označena jako úplná. </p> </td>
<td> <p> Událost | ID souboru dat | Dokončete registrační objekt </p> </td>
</tr>
<tr class="even">
<td> <p> dhis2.de.event.uncompleted </p> </td>
<td> <p> Spustí se, když je datová sada úspěšně označena jako neúplná. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="odd">
<td> <p> dhis2.de.event.validationSuccess </p> </td>
<td> <p> Spustí se po provedení ověření a nedošlo k žádnému porušení. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="even">
<td> <p> dhis2.de.event.validationError </p> </td>
<td> <p> Spustí se po ověření a došlo k jednomu nebo více porušením. </p> </td>
<td> <p> Událost | ID datové sady </p> </td>
</tr>
<tr class="odd">
<td> <p> dhis2.ou.event.orgUnitSelected </p> </td>
<td> <p> Spustí se, když je ve webovém stromu jednotky org. vybrána jedna nebo více organizačních jednotek. </p> </td>
<td> <p> Událost | ID organizační jednotky | Názvy jednotek organizace | ID podřízené organizace </p> </td>
</tr>
</tbody>
</table>

Registrace na akci:

    <script type="text/javascript">

    dhis2.util.on( 'dhis2.de.event.formReady', function( event, ds ) {
      console.log( 'The form with id: ' + ds + ' is loaded!' );
    } );

    dhis2.util.on( 'dhis2.de.event.dataValueSaved', function( event, ds, dv ) {
      console.log( 'Data value: ' + dv.value + ' was saved with data element: ' + dv.de );
    } );

    dhis2.util.on( 'dhis2.de.event.completed', function( event, ds, cr ) {
      console.log( 'Form was completed for org unit: ' + cr.ou );
    } );

    </script>

> **Poznámka**
>
> Dávejte pozor, abyste používali pouze události se stejným názvem, jako jsou ty z výše uvedeného příkladu, a nikoli ty obecné, jako je „kliknutí“, protože metoda dhis2.util.on nejprve odhlásí událost.

Pokud vaše funkce platí pouze pro určité datové sady, můžete použít dodaný identifikátor datové sady a zkratku vaší funkce pro nechtěné datové sady, jako je tato:

    dhis2.de.on( 'dhis2.de.event.validationSuccess', function( event, ds ) {
      if ( $.inArray( ds, ['utXOiGbEj14', 'Re7qzHEThSC'] ) == -1 ) {
        return false;
      }
      console.log( 'Form with id: ' + ds + ' validated successfully!' );
    } );

Identifikátory vstupních polí ve formuláři pro zadávání údajů jsou ve formátu popsaném níže. Tento formát lze použít k výběru vstupních polí ve skriptu a provádění akcí s nimi:

    <dataelementid>-<optioncomboid>-val

Vzhledem k tomu, že pro všechny události je k dispozici identifikátor datové sady, je proveditelnou alternativou využití prostředku webového rozhraní API „soubory“ a uchování funkcí zpětného volání v jediném souboru, kde necháte kód JavaScript provést akci na základě aktuálně načtené datové sady.

##### Funkce { #functions }

Modul pro zadávání dat DHIS2 obsahuje funkce rozhraní API JavaScriptu, ke kterým lze přistupovat z vlastních formulářů pro zadávání dat.

**dhis2.de.api.getSelections**: Tato funkce vrací objekt JavaScriptu, který obsahuje vlastnosti pro všechny dimenze s odpovídajícími hodnotami pro identifikátory vybraných možností. Obsahuje vlastnosti pro „ds“ (datový soubor), „pe“ (období), „ou“ (organizační jednotka) a identifikátory pro všechny kategorie datových souborů.

Příklad odpovědi vypadá takto:

    {
     +  ds: "lyLU2wR22tC",
     +  pe: "201605",
     +  ou: "g8upMTyEZGZ",
     +  LFsZ8v5v7rq: "CW81uF03hvV",
     +  yY2bQYqNt0o: "yMj2MnmNI8L"
     +}

Příklad použití této funkce pomocí JavaScriptu:

    var sel = dhis2.de.api.getSelections();
     +var orgUnit = sel["ou"];
     +var partner = sel["LFsZ8v5v7rq"];

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Správa indikátorů { #manage_indicator }

### O indikátorech { #about_indicator }

Indikátor je vzorec, který se může skládat z více datových prvků, konstant, počtů skupin organizačních jednotek a matematických operátorů. Indikátor se obvykle skládá z čitatele a jmenovatele. Pomocí indikátorů vypočítáte míru pokrytí, incidenci a další hodnoty, které jsou výsledkem hodnot datových prvků, které byly zadány do systému. Vypočítané součty nemají jmenovatele.

> **Poznámka**
>
> Nikdy nezadáváte hodnoty indikátorů přímo v DHIS2, vypočítáváte je.

Vzorec indikátoru se může skládat z matematických operátorů, například plus a mínus; funkce (viz níže); a následujících prvků:

<table>
<caption> Prvky Indikátorů </caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th> Prvek Indikátoru </th>
<th> Typ </th>
<th> Popis </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> konstantní </p> </td>
<td> <p> komponenta </p> </td>
<td> <p> Konstanty jsou číselné hodnoty, které zůstávají stejné pro všechny výpočty indikátorů. To je užitečné, abyste měli jediné místo pro změnu hodnot, které se mohou časem změnit. </p>
<p> Konstanty se použijí PO agregování hodnot datových prvků. </p> </td>
</tr>
<tr class="even">
<td> <p> Datové prvky </p> </td>
<td> <p> komponenta </p> </td>
<td> <p> Datové prvky jsou nahrazeny datovou hodnotou zachycenou pro datový prvek. </p> </td>
</tr>
<tr class="odd">
<td> <p> dny </p> </td>
<td> <p> operátor </p> </td>
<td> <p> &quot;Days&quot; je speciální operátor, který vždy poskytuje počet dní pro daný výpočet indikátoru. </p>
<p> Například: chcete-li vypočítat &quot;Percentní podíl času, kdy byla vakcína nefunkčníal&quot;, můžete definovat čitatel jako: </p>
<p> (&quot;Days-&quot; Počet dní, kdy byla k dispozici chladnička vakcín) / &quot;Days&quot;</p>

<p> Pokud byla lednička k dispozici 25 dní v červnu, indikátor by se počítal jako: </p>
<p> (30-25 / 25) * 100 = 17% </p>
<p> Pokud chcete vypočítat součet za 1. čtvrtletí, bude počet dní (&quot;Days&quot;): </p>
<p> 31+28+31 = 90 </p>
<p> Parametr &quot;Days&quot; bude vždy počet dní v období zájmu. </p> </td>
</tr>
<tr class="even">
<td> <p> Počítá se organizační jednotka </p> </td>
<td> <p> komponenta </p> </td>
<td> <p> Skupiny organizačních jednotek můžete použít ve vzorcích. Budou nahrazeny počtem organizačních jednotek ve skupině. Během agregace budou organizační jednotky ve skupině protínány s požadovanou částí hierarchie organizačních jednotek. </p>
<p> To vám umožní použít počet veřejných zařízení v konkrétním okrese v indikátorech. To je užitečné například při vytváření průzkumů a sestav infrastruktury infrastruktury. </p> </td>
</tr>
<tr class="odd">
<td> <p> programy </p> </td>
<td> <p> komponenta </p> </td>
<td> <p> Klikněte na <strong> Programy </strong> a vyberte program pro zobrazení všech datových prvků, atributů a indikátorů souvisejících s konkrétním programem. </p>
<p> Součásti programu, které zahrnete do vzorce, budou mít přiřazenou značku programu. </p> </td>
</tr>
</tbody>
</table>

Ve vzorci indikátoru můžete použít následující funkce:

<table>
<caption> Funkce indikátoru </caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Funkce indikátoru </p> </th>
<th> <p> Argumenty </p> </th>
<th> <p> Popis </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> pokud </p> </td>
<td> <p> (boolean-expr, true-expr, false-expr) </p> </td>
<td> <p> Vyhodnotí booleovský výraz a pokud true vrátí hodnotu skutečného výrazu, pokud false vrátí hodnotu falešného výrazu. Argumenty musí dodržovat pravidla pro jakýkoli výraz indikátoru. </p> </td>
</tr>
<tr class="even">
<td> <p> isNull </p> </td>
<td> <p> (prvek) </p> </td>
<td> <p> Vrací hodnotu true, pokud chybí hodnota prvku (null), v opačném případě false. </p> </td>
</tr>
<tr class="odd">
<td> <p> isNotNull </p> </td>
<td> <p> (prvek) </p> </td>
<td> <p> Vrací hodnotu true, pokud hodnota prvku nechybí (není null), v opačném případě false. </p> </td>
</tr>
<tr class="even">
<td> <p> prvníNonNull </p> </td>
<td> <p> (prvek [, prvek ...]) </p> </td>
<td> <p> Vrátí hodnotu prvního prvku, který nechybí (není null). Lze zadat libovolný počet argumentů. Jakýkoli argument může být také číselný nebo řetězcový literál, který bude vrácen, pokud všechny předchozí objekty mají chybějící hodnoty. </p> </td>
</tr>
<tr class="odd">
<td> <p> největší </p> </td>
<td> <p> (výraz [, výraz ...]) </p> </td>
<td> <p> Vrátí největší (nejvyšší) hodnotu uvedených výrazů. Lze zadat libovolný počet argumentů. </p> </td>
</tr>
<tr class="even">
<td> <p> nejméně </p> </td>
<td> <p> (výraz [, výraz ...]) </p> </td>
<td> <p> Vrátí nejnižší (nejnižší) hodnotu z uvedených výrazů. Lze zadat libovolný počet argumentů. </p> </td>
</tr>
</tbody>
</table>

V aplikaci **Údržba** spravujete následující objekty indikátorů:

<table>
<caption> objekty indikátoru v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> indikátor </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> Typ indikátoru </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> skupina indikátorů </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> Sada skupiny indikátorů </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Pracovní postup { #workflow_indicator }

1.  Vytvořte typy indikátorů.

2.  Vytvořte indikátory.

3.  Vytvořte skupiny indikátorů.

4.  Vytvořte sady skupin indikátorů.

### Vytvořte nebo upravte typ indikátoru { #create_indicator_type }

![](resources/images/maintainence/indicator_type_create.png)

Typy indikátorů definují faktor, který se použije během agregace. Hodnoty indikátoru, které se počítají během exportu datového tržiště nebo procesu generování tabulky sestavy, se zobrazí správně naformátované, a proto nebudou vyžadovat další multiplikátor (například 100 v případě procent), aby se hodnoty zobrazily správně naformátované.

> **Poznámka**
>
> Od verze 2.4 DHIS2 byl objekt „Vypočítaný datový prvek“ zastaralý. Místo toho můžete vytvořit vypočítaný datový prvek vytvořením typu indikátoru s faktorem „1“ a nastavením možnosti „Počet“ na „Ano“. Efekt nastavení možnosti „Počet“ na „Ano“ bude takový, že indikátor ve skutečnosti nebude mít jmenovatele. Budete tedy moci definovat pouze čitatel, který bude sloužit jako vzorec vypočítaného datového prvku.

1.  Otevřete aplikaci **Údržba** a klikněte na **Indikátor** \> **Typ indikátoru**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název typu indikátoru, například „Na sto“, „Na tisíc“, „Na deset tisíc“.

4.  Zadejte **faktor**.

    Faktor je číselný faktor, který se během výpočtu indikátoru vynásobí vzorcem indikátoru.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte indikátor { #create_indicator }

![](resources/images/maintainence/indicator_create.png)

1.  Otevřete aplikaci **Údržba** a klikněte na **Indikátor** \> **Indikátor**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte celý název indikátoru, například „Výskyt potvrzených případů malárie na 1000 obyvatel“.

4.  Do pole **Krátký název** zadejte zkrácený název indikátoru, například „Výsk. Malárie na 1000 ob.“.

    Krátký název musí být menší nebo roven 25 znakům, včetně mezer.

5.  (Volitelné) V poli **Kód** přiřaďte kód.

    V mnoha zemích je indikátorům přiřazen kód.

6.  (Volitelné) V poli **Barva** přiřaďte barvu k opětovnému zadání indikátoru.

7.  (Volitelné) V poli **Ikona** přiřaďte ikonu, která ilustruje význam indikátoru.

8.  Do pole **Popis** zadejte krátký informativní popis indikátoru a způsobu jeho výpočtu.

9.  Pokud chcete během výpočtu indikátoru použít anualizační faktor, vyberte **Anualizováno**.

    Typicky je čitatel anualizovaného indikátoru vynásoben faktorem 12 a jmenovatelem je například roční počet obyvatel. To umožňuje vypočítat hodnoty měsíčního pokrytí s ročními údaji o počtu obyvatel.

10. Vyberte počet **desetinných míst ve výstupu dat**.

11. Vyberte **typ indikátoru**.

    Toto pole určuje faktor, který se automaticky použije při výpočtu indikátoru. Možné volby jsou určeny typy indikátorů. Například indikátor „Procenta“ se při exportu do datového trhu automaticky vynásobí faktorem 100, takže se bude zobrazovat v procentech.

12. (Volitelné) Přiřaďte jednu nebo více **legend**.

13. Do pole **URL** zadejte odkaz, například odkaz na registr indikátorů, kde lze zpřístupnit úplný popis metadat indikátoru.

14. (Volitelné) Zadejte **kombinaci možností kategorie pro export agregovaných dat.**.

    Toto nastavení slouží k mapování agregovaných dat exportovaných jako nezpracovaná data na jiný server. Tento typ mapování výměny dat obvykle provádíte, když chcete vytvořit anonymní agregovaná data z dat pacientů zaznamenaných v programech (data událostí).

15. (Volitelné) Zadejte **kombinaci možností atributů pro export agregovaných dat.**.

    Toto nastavení slouží k mapování agregovaných dat exportovaných jako nezpracovaná data na jiný server. Tento typ mapování výměny dat obvykle provádíte, když chcete vytvořit anonymní agregovaná data z dat pacientů zaznamenaných v programech (data událostí).

16. Pokud je to možné, zadejte hodnoty vlastních atributů, například **Klasifikace** nebo **Metoda sběru**.

    > **Note**
    >
    > You create custom attributes in the **Maintenance** app: **Other** > \> **Attributes**.

17. Klikněte na **Upravit čitatel**.

    1.  Zadejte jasný popis čitatele.

    2.  Definujte čitatel poklepáním na komponenty v pravém poli. Komponenty se poté zobrazí jako součást vzorce v levém poli. Matematické operátory přidáte poklepáním na ikony pod levým polem.

        Váš vzorec musí být matematicky platný. To zahrnuje správné použití závorek, pokud je to nutné.

    3.  Kliknutím na **Hotovo** uložíte všechny změny do čitatele.

18. Klikněte na **Upravit jmenovatele**.

    1.  Zadejte jasný popis jmenovatele.

    2.  Definujte jmenovatele poklepáním na komponenty v pravém poli. Komponenty se poté zobrazí jako součást vzorce v levém poli. Matematické operátory přidáte poklepáním na ikony pod levým polem.

        Váš vzorec musí být matematicky platný. To zahrnuje správné použití závorek, pokud je to nutné.

    3.  Kliknutím na **Hotovo** uložíte všechny změny jmenovatele.

19. Je-li to možné, vyberte povinné skupiny skupin indikátorů, například **Lidské zdroje**.

    > **Note**
    >
    > You'll only see indicator group sets in this form if you've created them and set them to **Compulsory**.
    >
    > You create indicator group sets in the **Maintenance** app: **Indicator** \> **Indicator group set**.

20. Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu indikátorů { #create_indicator_group }

![](resources/images/maintainence/indicator_group_create.png)

1.  Otevřete aplikaci **Údržba** a klikněte na **Indikátor** \> **Skupina indikátorů**.

2.  Klikněte na tlačítko Přidat.

3.  Zadejte název.

4.  Vyberte indikátory a přiřaďte je.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte sadu skupin indikátorů { #create_indicator_group_set }

![](resources/images/maintainence/indicator_group_set_create.png)

Sady skupin indikátorů vytvářejí kombinované skupiny podobných indikátorů. Můžete mít například skupinu indikátorů zvaných „malárie“ a „leishmanióza“. Obě tyto skupiny lze kombinovat do skupiny nazvané „Vektorem přenášené nemoci“. Skupiny skupin indikátorů se používají při analýze dat ke kombinování podobných témat indikátorů.

1.  Otevřete aplikaci **Údržba** a klikněte na **Indikátory** \> **Skupina indikátorů**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**

    2.  **Popis**

    3.  **Povinný**

4.  Vyberte skupiny indikátorů a přiřaďte je.

    Dostupné skupiny indikátorů se zobrazují na levém panelu. Skupiny indikátorů, které jsou aktuálně členy skupiny skupin indikátorů, se zobrazují na pravém panelu.

5.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravovat organizační jednotky { #manage_organisation_unit }

V této části se naučíte, jak:

-   Vytvořit novou organizační jednotku a vytvořit hierarchii organizační jednotky

-   Vytvořit skupiny organizačních jednotek, skupiny skupin a přiřadit jim organizační jednotky

-   Upravit hierarchii organizační jednotky

### O organizačních jednotkách { #about_organisation_unit }

Hierarchie organizačních jednotek definuje organizační strukturu DHIS2, například jak jsou navzájem uspořádána zdravotnická zařízení, správní oblasti a další geografické oblasti. Je to dimenze „kde“ DHIS2, podobná tomu, jak období představují dimenzi „kdy“.

Hierarchie organizační jednotky je vytvořena na základě vztahů nadřazený - podřazený. V DHIS2 je každý z těchto uzlů organizační jednotkou. Země může mít například osm krajů a každý kraj může mít jako podřazené řadu okresů. Nejnižší úrovně se obvykle skládají ze zařízení, kde se shromažďují údaje. Zařízení na sběr dat lze také umístit na vyšších úrovních, například krajská nebo okresní nemocnice. Proto můžete v DHIS2 vytvářet zkosené organizační stromy.

-   Můžete mít pouze jednu organizační hierarchii současně.

-   V hierarchii můžete mít libovolný počet úrovní.

    Hierarchie národních organizací v oblasti veřejného zdraví mají obvykle čtyři až šest úrovní.

-   Další klasifikace můžete vytvořit pomocí organizačních skupin a sad organizačních skupin.

    Například k vytvoření paralelních administrativních hranic do sektoru zdravotní péče.

-   K vytvoření negeografické hierarchie se doporučuje použít skupiny organizačních jednotek.

-   Organizační jednotka může být pouze členem jedné skupiny organizačních jednotek v sadě skupin organizačních jednotek.

-   Skupina organizační jednotky může být součástí několika sad skupin organizačních jednotek.

-   Hierarchie organizačních jednotek je hlavním prostředkem agregace dat v geografické dimenzi.

-   Když zavřete organizační jednotku, nemůžete registrovat ani upravovat události v této organizační jednotce v aplikacích **Zachycení Události** a **Tracker Capture**.

> **Důležité**
>
> Po vytvoření hierarchie organizační jednotky můžete změnit, a to i organizační jednotky, které shromažďují data. DHIS2 však pro agregaci dat vždy používá nejnovější hierarchii. Takže pokud změníte hierarchii, ztratíte časovou reprezentaci hierarchie v čase.
>
> Okres A je dále rozdělen na okres B a okres C. Zařízení, která patřila do okresu A, jsou přeřazena do okresu B a C. Jakákoli historická data, která jste zadali před rozdělením, jsou stále registrována jako patřící do okresu B a C , nikoli do zastaralého okresu A.

V aplikaci **Údržba** spravujete následující objekty organizační jednotky:

<table>
<caption> Objekty organizační jednotky v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> organizační jednotka </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> skupina organizačních jednotek </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> Sada skupiny organizačních jednotek </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> úroveň organizační jednotky </p> </td>
<td> <p> Upravit a přeložit </p> </td>
</tr>
<tr class="odd">
<td> <p> Hierarchické operace </p> </td>
<td> <p> Přesunout organizační jednotky </p> </td>
</tr>
</tbody>
</table>

### Pracovní postup { #workflow_organisation_unit }

Doporučený pracovní postup je:

1.  Vytvořte organizační jednotky.

2.  Vytvořte skupiny organizačních jednotek.

3.  Vytvořte sady skupin organizačních jednotek.

### Vytvořte nebo upravte organizační jednotku { #create_organisation_unit }

![](resources/images/orgunits/create_new_orgunit.png)

Organizační jednotky přidáváte do hierarchie jeden po druhém, buď jako kořenová jednotka, nebo jako podřízená jednotka vybrané organizační jednotky. Můžete mít pouze jednu kořenovou jednotku.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Organizační jednotka**.

2.  Klikněte na tlačítko Přidat.

3.  Vyberte, do které organizační jednotky bude vaše nová organizační jednotka patřit:

    1.  Klikněte na **Nadřazená organizační jednotka**.

    2.  Ve stromu organizační jednotky vyhledejte nadřazenou organizační jednotku a vyberte ji. Váš výběr je označen žlutě.

        > **Tip**
        >
        > Click the arrows to expand the organisation unit tree.

    3.  Klikněte na **Vybrat**.

4.  Zadejte **název** organizační jednotky.

    Každá organizační jednotka musí mít jedinečný název.

5.  Zadejte **zkrácený název** pro organizační jednotku.

    Krátký název je obvykle zkratkou celého názvu organizační jednotky. Tento atribut se často používá v sestavách k zobrazení názvu organizační jednotky, kde je omezený prostor.

6.  (Volitelné) Přiřaďte **kód**.

    V mnoha zemích je organizačním jednotkám přidělen kód.

7.  (Volitelné) Zadejte **popis** organizační jednotky.

8.  Vyberte **Datum zahájení**.

    Otevírací data řídí, které organizační jednotky, které existovaly v určitém okamžiku, například při analýze historických dat.

9.  Je-li to relevantní, vyberte **Datum ukončení**.

10. Do pole **Komentář** zadejte všechny další informace, které chcete přidat.

11. (Volitelné) Do pole **URL** zadejte odkaz na externí web, který obsahuje další informace o organizační jednotce.

12. Zadejte kontaktní údaje:

    -   Kontaktní osoba

    -   Adresa

    -   E-mail

    -   Telefonní číslo

13. (Volitelné) Zadejte **Zeměpisnou šířku** a **Zeměpisnou délku**.

    K vytváření map v aplikaci **Mapy** musíte mít hodnoty zeměpisné šířky a délky. Pak mohou být vaše organizační jednotky reprezentovány jako body na mapě, například zdravotnické zařízení. Bez těchto informací nebude aplikace **Mapy** fungovat.

    Může být efektivnější importovat souřadnice později jako dávková úloha pro všechny organizační jednotky pomocí aplikace **Import-Export**. Pomocí aplikace **Import-Export** také vytváříte polygony. Polygon je organizační jednotka, která představuje správní hranici.

14. Pokud je to možné, vyberte **Datové Sady** a přiřaďte je.

    > **Note**
    >
    > You control whether a user should be able to assign data sets to an organisation unit in the **System Settings** app:
    >
    > Open the **System Settings** app, click **Access** and select **Allow assigning object to related objects during add or update**.

15. Pokud je to možné, vyberte **Programy** a přiřaďte je.

    > **Note**
    >
    > You control whether a user should be able to assign programs to an organisation unit in the **System Settings** app:
    >
    > Open the **System Settings** app, click **Access** and select **Allow assigning object to related objects during add or update**.

16. Pokud je to možné, zadejte hodnoty vlastních atributů, například **identifikátor HR**.

    > **Note**
    >
    > You configure the custom attributes in the **Maintenance** app:
    >
    > Open the **Maintenance** app and click **Other** \> **Attribute**.

17. Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu organizační jednotky { #create_organisation_unit_group }

Skupiny organizačních jednotek umožňují klasifikovat související organizační jednotky do společného tématu. Můžete například seskupit všechny organizační jednotky, které jsou nemocnicemi, do skupiny **Nemocnice**.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Skupina organizační jednotky**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplňte formulář:

    1.  **Název**: Zadejte přesný, jedinečný a popisný název skupiny organizačních jednotek.

    2.  **Krátký název**: Krátký název by měl mít méně než 25 znaků. Krátký název je obvykle zkratkou celého názvu organizační jednotky. Tento atribut se používá na určitých místech v DHIS2, kde je omezený prostor.

    3.  **Kód**

    4.  **Symbol**: Vyberte symbol, který se použije k zobrazení organizační jednotky (pouze body), když se vrstva zobrazí v aplikaci **Mapy**.

4.  Ve stromu organizace klikněte na organizační jednotky, které chcete přidat do skupiny organizačních jednotek.

    Organizační jednotku ve stromu můžete vyhledat rozšířením větví (kliknutím na symbol šipky) nebo vyhledáním podle názvu.

    Vybrané organizační jednotky se zobrazí oranžově.

5.  Klikněte **Uložit**.

### Vytvořte nebo upravte sadu skupin organizačních jednotek { #create_organisation_unit_group_set }

Sady skupin organizačních jednotek vám umožňují vytvářet další klasifikace organizačních jednotek. Skupinové sady vytvářejí nové dimenze, takže můžete provádět podrobnější analýzu dat. Data můžete snadno filtrovat, organizovat nebo agregovat podle skupin v rámci skupiny.

-   Můžete mít libovolný počet sad skupin organizačních jednotek.

-   Výchozí sady skupin organizačních jednotek jsou **Typ** a **Vlastnictví**.

-   Organizační jednotka může být pouze členem jedné skupiny organizačních jednotek v sadě skupin organizačních jednotek.

-   Skupina organizační jednotky může být součástí několika sad skupin organizačních jednotek.

-   Můžete definovat, zda je sada skupin organizačních jednotek povinná, či nikoli, což ovlivní úplnost dat. Povinné znamená, že všechny organizační jednotky musí být členy skupiny v dané skupině.

> **Poznámka**
>
> V části **Integrita dat** aplikace **Správa dat** můžete ověřit, zda jste omylem přiřadili stejnou organizační jednotku více skupinám v rámci stejné skupiny. V této aplikaci najdete také informace o organizačních jednotkách, které nejsou členy povinné skupiny skupin organizačních jednotek.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Sada skupin organizačních jednotek**.

2.  Klikněte na tlačítko Přidat.

3.  Vyplnit:

    1.  **Název**: Zadejte přesný název pro sadu skupin organizačních jednotek.

    2.  **Kód**

    3.  **Popis**: Popište, co měří nebo zachycuje skupina organizačních jednotek.

4.  Pokud chcete, aby všechny organizační jednotky byly členy skupiny v rámci skupiny, vyberte **Povinné**.

5.  (Volitelné) Vyberte **Datová dimenze**.

6.  (Volitelné) Vyberte **Zahrnout do analytiky subhierarchii**.

    Pokud toto vyberete, zdědí podřízená organizační jednotka vlastnost skupiny organizační jednotky od své nejbližší „nadřazené“ organizační jednotky. Jakákoli vlastnost v podřízené organizační jednotce přepíše dědičnou hodnotu.

    Pokud organizační jednotka nemá žádnou přidruženou skupinu organizačních jednotek, může organizační jednotka zdědit skupinu nejbližší nadřazené organizační jednotky. Pokud žádná ze skupin nadřazené organizační jednotky nemá skupinu organizačních jednotek pro danou sadu skupin organizačních jednotek, bude výsledek stále „prázdný“, ale pokud alespoň jeden z rodičů má skupinu organizační jednotky, zdědí ji podřízená organizační jednotka.

    zahrnout subhierarchii do analytiky "je povoleno, což znamená, že jednotky org zdědí své nejbližší rodiče skupinu jednotek org, pokud je jednotka org bílá (žádná skupina org jednotek s nimi spojená)."

7.  Vyberte skupiny organizačních jednotek a přiřaďte je.

    V levém seznamu najdete dostupné skupiny organizačních jednotek. Pomocí šipek můžete přesouvat vybrané skupiny mezi dvěma seznamy.

    Pokud v seznamu nalevo nejsou žádné skupiny organizačních jednotek, klikněte na **Přidat nové**. Ve formuláři, který se otevře, vytvořte skupinu organizačních jednotek, kterou potřebujete. Po dokončení klikněte na **Obnovit hodnoty**.

    > **Note**
    >
    > An organisation unit can only be a member of a single organisation unit group within an organisation unit group set.

8.  Klikněte **Uložit**.

![](resources/images/implementation_guide/organisation_unit_hiearchy.png)

Chcete analyzovat data na základě vlastnictví zařízení. Všechna zařízení mají vlastníka, takže musíte zajistit, aby všechny organizační jednotky získaly tuto klasifikaci. K tomu můžete použít možnost **Povinné**:

1.  Vytvořte skupinu pro každý typ vlastnictví, například „MZ“, „Soukromé“ a „Na základě víry“.

2.  Přiřaďte všechna zařízení v databázi jedné z těchto skupin.

3.  Vytvořte sadu skupin organizačních jednotek nazvanou „Vlastnictví“ a vyberte **Povinné**.

4.  Přiřaďte skupiny organizačních jednotek „MZ“, „Soukromé“ a „Na základě víry“ do skupiny organizačních skupin „Vlastnictví“.

![](resources/images/maintainence/analytics-include-org-unit-subhierarchy.png)

![](resources/images/maintainence/include-subhierarchy-analytics.png)

Seskupte organizační jednotku dvěma způsoby a agregujte data na těchto dvou paralelních hierarchiích

Slouží k agregaci dat (pouze v analytických aplikacích)

Další nastavení sady skupin organizačních jednotek vytváří dynamické „členství“ v sadě skupin organizačních jednotek.

Hierarchii organizačních jednotek nezměníte

Škálovatelné a dynamické

Dynamické zahrnutí hierarchie

Dynamická dodatečná klasifikace

### Přiřaďte názvy na úrovni organizačních jednotek { #name_organisation_unit_level }

Když přidáte podřazené do organizační jednotky, DHIS2 v případě potřeby automaticky vytvoří novou úroveň organizační jednotky. Systém také přiřadí této úrovni obecný název, například „Úroveň 5“. Obecný název můžete nahradit kontextovým názvem, například „Země“, „Kraj“, „Okres“ nebo „Zdravotnické zařízení“. DHIS2 používá kontextové názvy kdekoli, na které se odkazuje, například v aplikaci **Mapy**.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Úroveň organizační jednotky**.

    Doba načítání seznamu závisí na hloubce stromu hierarchie organizačních jednotek.

2.  Pro úrovně organizační jednotky, které chcete upravit, zadejte název.

3.  Vyberte počet úrovní offline.

    > **Note**
    >
    > You configure the default value in the **System Settings** app:
    >
    > Open the **System Settings** app, click **General** and select a level in the **Max offline organisation unit levels** list.

4.  Klikněte **Uložit**.

### Přesuňte organizační jednotky v rámci hierarchie { #move_organisation_unit }

Organizační jednotky můžete v rámci hierarchie přesunout změnou nadřazené položky vybrané organizační jednotky.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Hierarchické operace**.

2.  Ve stromu levé hierarchie vyberte organizační jednotky(ek), které chcete přesunout.

    > **Note**
    >
    > If the selected organisation unit is has sub-organisation units, all of them move to the new parent organisation unit.

3.  V pravém stromu hierarchie vyberte, do které organizační jednotky chcete vybrané organizační jednotku(y) přesunout.

4.  Klikněte na **Přesunout x organizační jednotky**, kde x znamená počet organizačních jednotek, které jste vybrali.

    Vaše změny se okamžitě projeví ve stromu hierarchie na levé straně.

### Zavřete organizační jednotku { #close_organisation_unit }

Když zavřete organizační jednotku, nemůžete registrovat ani upravovat události v této organizační jednotce v aplikacích **Zachycení Události** a **Tracker Capture**.

1.  Otevřete aplikaci **Údržba** a klikněte na **Organizační jednotka** \> **Organizační jednotka**.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Upravit**.

3.  Vyberte **Datum ukončení**.

4.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## \[Probíhá zpracovávání\] Spravujte pravidla pro ověřování { #manage_validation_rule }

### O pravidlech ověřování { #about_validation_rule }

Pravidlo ověření je založeno na výrazu. Výraz definuje vztah mezi hodnotami datových prvků. Výraz tvoří podmínku s určitými logickými kritérii.

Výraz se skládá z:

-   Levá strana

-   Pravé strany

-   Operátoru

Pravidlo validace, které tvrdí, že celkový počet vakcín podaných kojencům je menší nebo roven celkovému počtu kojenců.

V aplikaci **Údržba** spravujete následující objekty pravidel ověření:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Co můžete udělat </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> ověřovací pravidlo </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="even">
<td> <p> skupina ověřovacích pravidel </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, sdílet, zobrazit podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> Oznámení o ověření </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

#### O posuvných oknech { #sliding_windows }

Můžete použít posuvná okna ke seskupení dat _napříč více obdobími_, na rozdíl od výběru dat pro _jedno období_. Posuvná okna mají velikost, to znamená počet dní, které mají být pokryty, počáteční a koncový bod. Níže uvedený příklad ukazuje data sledování nemocí:.

-   Data v oranžové části vybírají data na základě aktuálního období. Existuje prahová hodnota, která se počítá jednou za každý týden nebo období, a je uvedena v části „Výsledek“.

-   Data v modré části jsou posuvné okno. Vybírá data za posledních 7 dní. „Výsledek“ zobrazuje celkový počet potvrzených případů onemocnění.

-   Pravidlo ověřování zajišťuje, že uživatelé budou upozorněni, když celkový počet případů překročí prahovou hodnotu pro dané období.

![](resources/images/maintainence/validation_rules_sliding_window.gif)

<table>
<caption> Různé chování ověřovacích pravidel </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> s posuvnými okny </p> </th>
<th> <p> bez posuvných oken </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Používá se pouze pro data událostí. </p> </td>
<td> <p> Používá se pro data událostí a agregovaná data. </p> </td>
</tr>
<tr class="even">
<td> <p> Výběr dat je založen na pevném počtu dní (periodType). </p> </td>
<td> <p> Výběr dat je vždy založen na období. </p> </td>
</tr>
<tr class="odd">
<td> <p> Poloha posuvného okna je vždy <em> vzhledem k </em> srovnávané období. </p> </td>
<td> <p> Data jsou vždy vybrána pro stejné období <em> </em> jako srovnávané období. </p> </td>
</tr>
</tbody>
</table>

Viz také: Jak používat posuvná okna, když [Vytváříte nebo upravujete ověřovací pravidlo](https://docs.dhis2.org/master/en/user/html/manage_validation_rule.html#create_validation_rule).

#### O skupinách pravidel ověření { #about-validation-rule-groups }

Skupina ověřovacích pravidel vám umožňuje seskupovat související ověřovací pravidla. Když spustíte _[analýza ověřovacích pravidel](https://docs.dhis2.org/master/en/user/html/validation_rule_analysis.html)_, můžete zvolit spuštění všech ověřovacích pravidel ve vašem systému, nebo jen ověřovací pravidla v jedné skupině.

#### O oznámeních o ověření { #validation_notifications }

Můžete nakonfigurovat analýzu ověřovacích pravidel tak, aby automaticky odesílala oznámení o chybách ověření vybraným skupinám uživatelů. Tyto zprávy se nazývají _ověřovací oznámení_. Jsou odesílány prostřednictvím interního systému zpráv DHIS2.

Oznámení o pravidlech ověření můžete odesílat jako jednotlivé zprávy nebo jako souhrny zpráv. To je užitečné například, pokud chcete odesílat jednotlivé zprávy o ohniscích nemocí s vysokou prioritou a souhrny chyb rutiny s nízkou prioritou při ověřování dat.

### Vytvořte nebo upravte ověřovací pravidlo { #create_validation_rule }

1.  Otevřete aplikaci **Údržba** a klikněte na **Ověření** \> **Pravidlo ověření**.

2.  Klikněte na tlačítko Přidat.

3.  Zadejte **Název**.

    Název musí být mezi pravidly ověření jedinečný.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  (Volitelné) Zadejte **Popis**.

6.  Vyberte **Důležitost**: **Vysoká**, **Střední** nebo **Nízká**.

7.  Vyberte **Typ období**.

8.  Vyberte **Provozovatele**: **Povinná dvojice**, **Rovná se**, **Exkluzivní dvojice**, **Větší než**, **Větší než nebo rovno** nebo **Nerovná se s**.

    Operátor **Povinné dvojice** umožňuje požadovat, aby hodnoty dat musely být zadány pro formulář pro levou i pravou stranu výrazu nebo pro žádnou stranu. To znamená, že můžete požadovat, že pokud je vyplněno jedno pole ve formuláři, musí být vyplněno také jedno nebo více dalších polí.

    **Exkluzivní pár** umožňuje tvrdit, že pokud existuje nějaká hodnota na levé straně, pak by neměly být žádné hodnoty na pravé straně (nebo naopak). To znamená, že datové prvky, které tvoří pravidlo na obou stranách, by se měly vzájemně vylučovat, a to pro dané časové období / kombinace organizační jednotky / atributu.

9.  Vytvořte levou stranu výrazu:

    1.  Klikněte na **Levá strana**.

    2.  Vyberte **Posuvné okno**, pokud chcete zobrazit data ve vztahu k srovnávanému období. Viz také [O pravidlech ověřování](https://docs.dhis2.org/master/en/user/html/manage_validation_rule.html#about_validation_rule).

    3.  Vyberte strategii **Chybějící hodnota**. Tento výběr nastavuje, jak systém vyhodnotí ověřovací pravidlo, pokud chybí data.

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Option</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>Skip if any value is missing</p></td>
        <td><p>The validation rule will be skipped if any of the values which compose the expression are missing. This is the default option.</p>
        <p>Always select this option you use the <strong>Exclusive pair</strong> or <strong>Compulsory pair</strong> operator.</p></td>
        </tr>
        <tr class="even">
        <td><p>Skip if all values are missing</p></td>
        <td><p>The validation rule will be skipped only if all of the operands which compose it are missing.</p></td>
        </tr>
        <tr class="odd">
        <td><p>Never skip</p></td>
        <td><p>The validation rule will never be skipped in case of missing data, and all missing operands will be treated effectively as a zero.</p></td>
        </tr>
        </tbody>
        </table>

    4.  Zadejte **Popis**.

    5.  Vytvořte výraz založený na dostupných datových prvcích, programových objektech, organizačních jednotkách, počtech a konstantách.

        V pravém podokně poklepejte na datové objekty, které chcete zahrnout do výrazu. Kombinujte s matematickými operátory umístěnými pod levým podoknem.

    6.  Klikněte **Uložit**.

10. Vytvořte pravou stranu výrazu:

    1.  Klikněte na **Pravá strana**.

    2.  Vyberte strategii **Chybějící hodnota**. Tento výběr nastavuje, jak systém vyhodnotí ověřovací pravidlo, pokud chybí data.

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Option</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>Skip if any value is missing</p></td>
        <td><p>The validation rule will be skipped if any of the values which compose the expression are missing. This is the default option.</p>
        <p>Always select this option you use the <strong>Exclusive pair</strong> or <strong>Compulsory pair</strong> operator.</p></td>
        </tr>
        <tr class="even">
        <td><p>Skip if all values are missing</p></td>
        <td><p>The validation rule will be skipped only if all of the operands which compose it are missing.</p></td>
        </tr>
        <tr class="odd">
        <td><p>Never skip</p></td>
        <td><p>The validation rule will never be skipped in case of missing data, and all missing operands will be treated effectively as a zero.</p></td>
        </tr>
        </tbody>
        </table>

    3.  Vyberte **Posuvné okno**, pokud chcete zobrazit data ve vztahu k srovnávanému období. Viz také [O pravidlech ověřování](https://docs.dhis2.org/master/en/user/html/manage_validation_rule.html#about_validation_rule).

    4.  Zadejte **Popis**.

    5.  Vytvořte výraz založený na dostupných datových prvcích, programových objektech, organizačních jednotkách, počtech a konstantách.

        V pravém podokně poklepejte na datové objekty, které chcete zahrnout do výrazu. Kombinujte s matematickými operátory umístěnými pod levým podoknem.

    6.  Klikněte **Uložit**.

11. (Volitelné) Vyberte, pro které **úrovně organizačních jednotek** má být toto pravidlo vyhodnoceno. Ponecháte-li toto pole prázdné, bude ověřovací pravidlo vyhodnoceno na všech úrovních.

12. (Volitelné) Klikněte na **Přeskočit toto pravidlo během ověřování formuláře**, abyste zabránili spuštění tohoto pravidla při zadávání dat

13. Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu ověřovacích pravidel { #create_validation_rule_group }

1.  Otevřete aplikaci **Údržba** a klikněte na **Ověření** \> **Skupina pravidel ověření**.

2.  Klikněte na tlačítko Přidat.

3.  Zadejte **Název**.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  (Volitelné) Zadejte **Popis**.

6.  Poklepejte na **Pravidla ověření**, která chcete skupině přiřadit.

7.  Klikněte **Uložit**.

### Vytvořte nebo upravte oznámení o ověření { #create_validation_notification }

1.  Otevřete aplikaci **Údržba** a klikněte na **Ověření** \> **Oznámení o ověření**.

2.  Klikněte na tlačítko Přidat.

3.  Zadejte **Název**.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  Vyberte **Pravidla ověření**.

6.  Vyberte **Skupiny uživatelů příjemců**.

7.  (Volitelné) Vyberte **Upozornit uživatele pouze v hierarchii**.

    Pokud vyberete tuto možnost, systém bude filtrovat uživatele příjemců. (Systém odvodí uživatele příjemců ze skupin uživatelů příjemců.) Filtr je založen na tom, ke které organizační jednotce uživatel příjemce patří. Uživatelé propojení s organizačními jednotkami, které jsou předky organizační jednotky, kde k porušení došlo, obdrží ověřovací oznámení. Systém bude ignorovat ostatní uživatele a tito uživatelé nebudou dostávat oznámení o ověření.

8.  Vytvořte šablonu zprávy:

    1.  Vytvořte **šablonu subjektu**.

        Poklepáním na parametry v poli **Proměnné šablony** je přidáte do předmětu.

    2.  Vytvořte **šablonu zprávy**.

        Poklepejte na názvy parametrů v poli **Proměnné šablony** a přidejte je do své zprávy.

9.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravovat atributy { #manage_attribute }

### O atributech { #about_attribute }

Atributy metadat můžete použít k přidání dalších informací k objektům metadat. Kromě standardních atributů pro každý z těchto objektů může být užitečné ukládat informace pro další atributy, například metodu shromažďování pro datový prvek.

![](resources/images/maintainence/attribute_create.png)

V aplikaci **Údržba** spravujete následující objekty atributů:

<table>
<caption> Atributy objektů v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce</p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Atribut </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Vytvořte nebo upravte atribut { #create-or-edit-an-attribute }

1.  Otevřete aplikaci **Údržba** a klikněte na **Atribut**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název atributu.

    Každý atribut musí mít jedinečný název

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  Vyberte **typ hodnoty**.

    Pokud hodnota zadaná pro atribut neodpovídá typu hodnoty, zobrazí se varování.

6.  Vyberte **sadu možností**.

7.  Vyberte požadované možnosti, například:

    -   Vyberte **Povinné**, pokud chcete, aby měl objekt vždy dynamický atribut.

    -   Vyberte **Jedinečné**, pokud chcete, aby systém vynutil, aby hodnoty byly jedinečné pro konkrétní typ objektu.

8.  Klikněte **Uložit**.

    Dynamický atribut je nyní k dispozici pro objekty, ke kterým jste jej přiřadili.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte konstanty { #manage_constant }

### O konstantách { #about_constant }

Konstanty jsou statické hodnoty, které lze uživatelům zpřístupnit pro použití v datových prvcích a indikátorech. Některé indikátory, například „Míra roční ochrany párů“, závisí na konstantách, které se obvykle časem nemění.

![](resources/images/maintainence/constant_create.png)

V aplikaci **Údržba** spravujete následující konstantní objekty:

<table>
<caption> Konstanty objektu v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Konstanty</p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Vytvořte nebo upravte konstantu { #create_constant }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Konstantní**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název konstanty.

4.  (Volitelné) Do pole **Krátký název** zadejte zkrácený název konstanty.

5.  (Volitelné) V poli **Kód** přiřaďte kód.

6.  Do pole **Popis** zadejte krátký informativní popis konstanty.

7.  V poli **Hodnota** definujte hodnotu konstanty.

8.  Klikněte **Uložit**.

    Konstanta je nyní k dispozici pro použití.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravovat sady možností { #manage_option_set }

### O sadách možností { #about_option_set }

Sady možností poskytují předdefinovaný rozevírací (výčet) seznam pro použití v DHIS2. Můžete definovat jakýkoli druh možností.

Sada možností s názvem „Typ doručení“ by měla možnosti: „Normální“, „Porušení“, „Cézar“ a „Asistováno“.

![](resources/images/maintainence/option_set_create.png)

<table>
<caption> Sady možností objektů v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> sada možností </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> skupina možností </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
<tr class="odd">
<td> <p> sada skupin možností </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, sdílet, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Vytvořte nebo upravte sadu možností { #create_option_set }

> **Důležité**
>
> Sady možností musí mít kód i název. Můžete změnit názvy, ale nemůžete změnit kódy. Názvy i kódy všech možností musí být jedinečné, a to i v různých sadách možností.

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Sada možností**.

2.  Klikněte na tlačítko Přidat.

3.  Na kartě **Primární podrobnosti** definujte sadu možností:

    1.  Do pole **Název** zadejte název konstanty.

    2.  V poli **Kód** přiřaďte kód.

    3.  Vyberte **typ hodnoty**.

    4.  Klikněte **Uložit**.

4.  U každé možnosti, kterou potřebujete, proveďte následující úkoly:

    1.  Klikněte na kartu **Možnosti**.

    2.  Klikněte na tlačítko Přidat.

    3.  Zadejte **název** a **kód**. Volitelně také vyberte **barva** a **Ikona**, které budou použity pro tuto možnost v aplikacích pro sběr dat.

    4.  Třídit možnosti podle názvu, kódu / hodnoty nebo ručně.

    5.  Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu možností { #create_option_group }

Můžete seskupit a klasifikovat **možnosti** v **sadě možností** pomocí **skupin možností**. Tímto způsobem můžete vytvořit podmnožinu možností v sadě možností. Hlavním účelem je schopnost filtrovat obrovské sady voleb na menší související části.

Možnosti, které jsou seskupeny, lze skrýt nebo zobrazit společně v nástroji pro sledování a zachycení událostí pomocí pravidel programu.

> **Poznámka**
>
> Po vytvoření nelze změnit **Sadu možností** vybranou ve **Skupině možností**.

1. Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Skupina možností**.

2. Klikněte na tlačítko Přidat.

3. Vyplňte formulář:

    1. **Název**
    2. **Krátký název**
    3. **Kód**
    4. **Sada možností**

4. Jakmile je vybrána **sada možností**, můžete přiřadit **možnosti**, které chcete seskupit.

5. Klikněte **Uložit**.

### Vytvořte nebo upravte sadu skupin možností { #create_option_group_set }

**Sady skupin možností** vám umožňují kategorizovat více **skupin možností** do sady. Hlavním účelem sady skupin možností je přidat k vašim zachyceným datům pro analýzu větší dimenzi.

> **Poznámka**
>
> Po vytvoření nelze změnit **sadu možností** vybranou v **skupině možností**.

1. Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Sada skupin možností**.

2. Klikněte na tlačítko Přidat.

3. Vyplňte formulář:

    1. **Název**
    2. **Kód**
    3. **Popis**
    4. **Sada možností**
    5. **Datová dimenze**

       Pokud vyberete **Datová dimenze**, bude sada skupin analytikům k dispozici jako další dimenze kromě standardních dimenzí „Období“ a „Organizační jednotka“.

4. Vyberte skupiny možností a přiřaďte je.

   Dostupné skupiny možností se zobrazují na levém panelu. Skupiny možností, které jsou aktuálně členy sady skupin možností, se zobrazují na pravém panelu.

5. Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte legendy { #manage_legend }

### O legendách { #about_legend }

Můžete vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat legendy, aby mapy, které nastavujete pro své uživatele, byly smysluplné. Mapy vytváříte v aplikaci **Mapy**.

> **Poznámka**
>
> Kontinuální legendy se musí skládat z položek legend, které končí a začínají stejnou hodnotou, například: 0-50 a 50-80. Nenastavujte položky legendy takto: 0-50 a 51-80. Tím se vytvoří mezery ve vaší legendě.

### Vytvořte nebo upravte legendu { #create_legend }

> **Poznámka**
>
> V legendě není povoleno mít mezery.
>
> Není povoleno mít překrývající se položky legendy.

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Legenda**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název legendy.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  Vytvořte položky legendy, které chcete mít ve své legendě:

    1.  Vyberte **Počáteční hodnota** a **Konečná hodnota**.

    2.  Vyberte **Počet položek legendy**.

    3.  Vyberte barevné schéma.

    4.  Klikněte na **Vytvořit položky legendy**.

    > **Tip**
    >
    > Click the options menu to edit or delete a legend item.

6.  (Volitelné) Přidejte další položky legendy:

    1.  Klikněte na tlačítko Přidat.

    2.  Zadejte název a vyberte počáteční hodnotu, koncovou hodnotu a barvu.

    3.  Klikněte **OK**.

7.  (Volitelné) Změňte barevné škály.

    1.  Kliknutím na barevnou stupnici zobrazíte seznam možností barevné stupnice a vyberte barevnou stupnici.

    2.  Chcete-li přizpůsobit barevnou škálu, klikněte na tlačítko Přidat. V dialogovém okně **Upravit položku legendy** klikněte na tlačítko barevné škály a ručně vyberte barvy nebo zadejte hodnoty barev.

8.  Klikněte **Uložit**.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th> Položka legendy </th>
<th> počáteční hodnota </th>
<th> Koncová hodnota </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Nízká chyba </td>
<td> 0 </td>
<td> 50 </td>
</tr>
<tr class="even">
<td> Střední </td>
<td> 50 </td>
<td> 80 </td>
</tr>
<tr class="odd">
<td> Vysoká dobrá </td>
<td> 80 </td>
<td> 100 </td>
</tr>
<tr class="even">
<td> Příliš vysoká </td>
<td> 100 </td>
<td> 1000 </td>
</tr>
</tbody>
</table>

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Změňte nastavení sdílení pro objekty metadat { #change-sharing-settings-for-metadata-objects }

Objektům metadat můžete přiřadit různá nastavení sdílení, například organizační jednotky a trasované atributy entit. Tato nastavení sdílení určují, kteří uživatelé a skupiny uživatelů mohou zobrazit nebo upravit objekt metadat.

Některé objekty metadat také umožňují změnit nastavení sdílení zadávání dat pro objekt. Tato další nastavení určují, kdo může pomocí metadat prohlížet nebo zadávat data do polí formulářů.

> **Poznámka**
>
> Výchozí nastavení je, že každý (**Veřejný přístup**) může najít, zobrazit a upravit objekty metadat.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete upravit.

2.  V seznamu objektů klikněte na místní nabídku a vyberte **Nastavení sdílení**.

3.  (Volitelné) Přidat uživatele nebo skupiny uživatelů: vyhledejte uživatele nebo skupinu uživatelů a vyberte ji. Uživatel nebo skupina uživatelů se přidá do seznamu.

4.  Změňte nastavení sdílení pro skupiny přístupu, které chcete upravit.

    -   **Může upravovat a prohlížet**: Přístupová skupina může prohlížet a upravovat objekt.

    -   **Může pouze zobrazit**: Přístupová skupina může zobrazit objekt.

    -   **Žádný přístup** (platí pouze pro **Veřejný přístup**): Veřejnost nebude mít přístup k objektu.

5.  Změňte nastavení sdílení dat pro skupiny přístupu, které chcete upravit.

    -   **Může zachytit data**: Přístupová skupina může zobrazit a zachytit data pro objekt.

    -   **Can view data**: Přístupová skupina může zobrazit data pro objekt.

    -   **Žádný přístup**: Přístupová skupina nebude mít přístup k datům objektu.

6.  Klikněte na **Zavřít**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

### Přiřaďte legendu indikátoru nebo datovému prvku { #assign-a-legend-to-indicator-or-data-element }

Legendu můžete k indikátoru nebo datovému prvku přiřadit v aplikaci **Údržba**, buď když vytvoříte objekt, nebo jej upravíte. Když poté v aplikaci **Maps** vyberete indikátor nebo datový prvek, systém automaticky vybere přiřazenou legendu.

### Viz také { #see_also_legend }

-   [Použití aplikace GIS] (https://docs.dhis2.org/master/en/user/html/using_gis.html)

## Spravujte prediktory { #manage_predictor }

### O prediktorech { #about-predictors }

Prediktor říká DHIS2, jak generovat datovou hodnotu na základě hodnot dat z minulých období a/nebo období datové hodnoty. Definuje, která minulá období vzorkovat, a jak zkombinovat data za vzniku predikované hodnoty. Prediktor vždy generuje agregovanou datovou hodnotu, ale minulé datové hodnoty použité k výpočtu predikované hodnoty mohou pocházet z agregovaných dat, dat událostí nebo obojího.

Jednoduché použití prediktorů by bylo zkopírovat hodnotu dat za minulé období do nového období, například do dalšího měsíce, nebo do stejného čtvrtletí příštího roku. Složitější použití prediktorů by bylo pro sledování nemocí, aby bylo možné předpovědět, jaká hodnota se očekává v daném týdnu nebo měsíci roku, na základě předchozích hodnot dat. Potom by bylo možné použít ověřovací pravidlo, aby bylo vidět, jak se skutečná hodnota porovnává s očekávanou (predikovanou) hodnotou.

Můžete určit úrovně organizačních jednotek (jednotky), pro které bude prediktor generovat hodnoty. Například při sledování nemocí můžete použít jeden prediktor k udání očekávané hodnoty v každém místním zařízení, vzhledem k množství variací, které byste u jednoho zařízení očekávali, a zároveň použít jiný prediktor k odhadu hodnoty, kterou byste očekávali součtu všech zařízení v okres, vzhledem k (menší) proporcionální variabilitě, kterou byste očekávali při sčítání hodnot pro všechna zařízení v okrese. Můžete také definovat další prediktory na všech vyšších úrovních hierarchie organizačních jednotek, kde můžete očekávat různé proporce variací. Alternativně můžete definovat jeden prediktor pro všechny tyto úrovně a pomocí funkce standardní odchylky určit, jaké hodnoty odchylek byly na každé úrovni naměřeny.

V aplikaci **Údržba** spravujete následující objekty prediktorů:

<table>
<caption> Objekty Prediktoru v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Prediktor </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

### Vzorkování minulých období { #sampling-past-periods }

Prediktory mohou generovat hodnoty dat pro období, která jsou v minulosti, současnosti nebo budoucnosti. Tyto hodnoty jsou založeny na datech z předpokládaného období a/nebo vzorkovaných datech z období předcházejících předpokládanému období.

Pokud potřebujete data pouze ze stejného období, ve kterém se předpověď provádí, nemusíte tuto sekci číst. Tato část popisuje, jak odebrat data z období před předpokládaným obdobím.

#### Sekvenční počet vzorků { #sequential_sample_count }

Počet prediktorů _Sekvenční počet vzorků_ udává počet bezprostředně předchozích období k odebrání vzorku. Pokud je například typ období prediktoru _Týdně_ a _Sekvenční počet vzorků_ je 4, znamená to vzorek čtyř předchozích týdnů bezprostředně předcházejících týdnu předpokládané hodnoty. Předpovídaná hodnota pro 9. týden by tedy použila vzorky z 5., 6., 7. a 8. týdne:

![](resources/images/maintainence/predictor_sequential.png){.center width=50% }

Pokud je typ období prediktoru _Měsíční_ a _Sekvenční počet vzorků_ je 4, znamená to vzorek čtyř předchozích měsíců bezprostředně předcházejících měsíci předpokládané hodnoty. Předpovídaná hodnota pro květen by tedy použila vzorky z týdnů leden, únor, březen a duben:

![](resources/images/maintainence/predictor_sequential_month.png){.center width=51% }

_Sekvenční počet vzorků_ může být větší než počet období v roce. Například pokud chcete vyzkoušet 24 měsíců bezprostředně předcházejících předpovídané hodnotě měsíce, nastavte _Sekvenční počet vzorků_ na 24:

![](resources/images/maintainence/predictor_24_months.png){.center width=57% }

#### Počet postupných přeskočení { #sequential_skip_count }

Počet prediktorů _Sekvenční počet přeskočení_ udává, kolik období by mělo být přeskočeno bezprostředně před obdobím předpokládané hodnoty v rámci _Sekvenčního počtu vzorků_. Toho lze využít například při detekci ohniska k přeskočení jednoho nebo více bezprostředně předcházejících vzorků, které by ve skutečnosti mohly obsahovat hodnoty od začátku ohniska, které se pokoušíte detekovat.

Například pokud _Sekvenční počet vzorků_ je 4, ale _Sekvenční počet přeskočení_ je 2, pak budou dva vzorky bezprostředně předcházející předpovídané období přeskočeny, což bude mít za následek vzorkování pouze dvou období:

![](resources/images/maintainence/predictor_skip.png){.center width=50% }

#### Počet ročních vzorků { #annual_sample_count }

_Roční počet vzorků_ prediktoru udává počet předchozích let, za které by měly být vzorky odebrány ve stejnou roční dobu. Toho lze využít například pro sledování nemocí v případech, kdy se očekávaný výskyt onemocnění v průběhu roku liší a lze jej nejlépe porovnat se stejným relativním obdobím v předchozích letech. Pokud je například _Roční počet vzorků_ 2 (a _Sekvenční počet vzorků_ je nula), pak by byly vzorky odebírány z období bezprostředně předcházejících dvou let, ve stejnou dobu roku.

![](resources/images/maintainence/predictor_annual.png){.center width=53% }

#### Sekvenční a roční počet vzorků se počítá společně { #sequential_annual_sample_count }

Sekvenční a roční počty vzorků můžete použít společně ke shromažďování vzorků z několika sekvenčních období za několik minulých let. Když to uděláte, vzorky budou shromážděny v předchozích letech během období ve stejnou dobu roku jako období předpokládané hodnoty a také v předchozích letech před i po stejné době roku, jak je určeno číslem _Sekvenční počet vzorků_ .

Pokud je například _Sekvenční počet vzorků_ 4 a _Roční počet výběrů_ je 2, budou odebrány vzorky ze 4 období bezprostředně předcházejících období předpokládané hodnoty. Kromě toho budou odebrány vzorky v předchozích 2 letech za odpovídající období a také 4 období na obou stranách:

![](resources/images/maintainence/predictor_sequential_annual.png){.center width=66% }

#### Počty sekvenčních, ročních a přeskočených vzorků dohromady { #sequential_annual_skip_sample_count }

Můžete použít _Sekvenční počet přeskočení_ společně s počty sekvenčních a ročních vzorků. Když toto uděláte, _Sekvenční počet přeskočení_ řekne, kolik období přeskočit ve stejném roce jako období predikované hodnoty. Například pokud _Sekvenční počet vzorků_ je 4 a _Sekvenční počet přeskočení_ je 2, pak budou dvě období bezprostředně předcházející období období předpovídané hodnoty přeskočena, ale dvě období před tím budou vzorkována:

![](resources/images/maintainence/predictor_skip_2_weeks.png){.center width=66% }

Pokud je _Sekvenční počet přeskočení_ stejný nebo větší než _Sekvenční počet vzorků_, pak se za rok obsahující období předpokládané hodnoty nebudou shromažďovat žádné vzorky; vzorkovány budou pouze období z minulých let:

![](resources/images/maintainence/predictor_skip_current_year.png){.center width=66% }

#### Přeskočení Ukázkového testu { #sample_skip_test }

Pomocí _Přeskočení testovacích vzorků_ můžete přeskočit vzorky z určitých období, která by jinak byla zahrnuta, na základě výsledků testování výrazu v těchto obdobích. To by mohlo být použito například při detekci ohniska choroby, kde by test přeskočení vzorku mohl identifikovat předchozí ohniska nemoci, aby byly tyto vzorky vyloučeny z predikce očekávané základní hodnoty bez ohniska nákazy.

_Přeskočení testovacích vzorků_ je výraz, který by měl vrátit hodnotu true nebo false, aby indikoval, zda má být období přeskočeno. Může to být výraz, který testuje jakékoli hodnoty dat v předchozím období. Mohlo by to například otestovat hodnotu dat, která byla explicitně zadána, aby indikovala, že by mělo být přeskočeno předchozí období. Nebo by to mohlo porovnat dříve předpovězenou hodnotu pro období se skutečnou hodnotou zaznamenanou pro dané období, aby bylo možné určit, zda má být toto období přeskočeno.

Žádná období, pro která _Přeskočení testovacích vzorků_ je _true_, nebudou vzorkována. Například:

![](resources/images/maintainence/predictor_sample_skip_test.png){.center width=66% }

### Vytvořte nebo upravte prediktor { #create_predictor }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Predictor**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název prediktoru.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  (Volitelné) Zadejte **Popis**.

6.  Vyberte **výstupní datový prvek**. Hodnoty generované tímto prediktorem se ukládají jako agregovaná data spojená s tímto datovým prvkem a předpokládaným obdobím.

    Hodnota se zaokrouhlí podle typu hodnoty datového prvku: Pokud je typem hodnoty celočíselný typ, předpokládaná hodnota se zaokrouhlí na nejbližší celé číslo. U všech ostatních typů hodnot je číslo zaokrouhleno na čtyři platné číslice. (Pokud jsou však vlevo od desetinného místa více než čtyři číslice, nejsou nahrazeny nulami.)

7.  (Volitelné) Vyberte kombinovanou kategorii **Výstupní kategorie**. Tato rozevírací nabídka se zobrazí, pouze pokud je k vybranému datovému prvku připojena kombinovaná kategorie. Pokud je to váš případ, můžete si vybrat, kterou kombinovanou kategorii chcete použít.

8.  Vyberte **Typ období**.

9.  Přiřaďte jednu nebo více úrovní organizačních jednotek. Výstupní hodnota bude přiřazena organizační jednotce na této úrovni (nebo těchto úrovních). Vstupní hodnoty pocházejí z organizační jednotky, ke které je výstup přiřazen, nebo z jakékoli nižší úrovně pod výstupní organizační jednotkou.

10. Vytvořte **generátor**. Generátor je výraz, který se používá k výpočtu předpokládané hodnoty.

    1.  Zadejte **Popis** výrazu generátoru.

    2.  Vyberte strategii **Chybějící hodnota**. Tento výběr nastavuje, jak systém vyhodnotí ověřovací pravidlo, pokud chybí data.

        | Možnost                         | Popis                                                                                                                                                                                                                     |
        | --- | --- |
        | Pokud nějaká hodnota chybí, přeskočit   | Pravidlo ověření bude přeskočeno, pokud některá z hodnot, které tvoří výraz, chybí. Toto je výchozí možnost. <br><br> Tuto možnost vyberte vždy, použijete-li operátor **Exkluzivní pár** nebo **Povinný pár**. |
        | Pokud všechny hodnoty chybí, přeskočit | Pravidlo ověření bude přeskočeno, pouze pokud chybí všechny hodnoty, které jej tvoří.                                              |
        | Nikdy přeskočit   | Pravidlo ověření nebude nikdy přeskočeno v případě chybějících dat a se všemi chybějícími hodnotami bude zacházeno efektivně jako s nulou.          |

    3.  Zadejte výraz generátoru. Výraz můžete vytvořit výběrem datových prvků pro agregovaná data nebo programových datových prvků, atributů nebo indikátorů. Počty organizačních jednotek ještě nejsou podporovány.

        Chcete-li použít vzorkovaná data z minulého období, měli byste uzavřít všechny položky, které vyberete, do jedné z následujících agregovaných funkcí (tyto názvy funkcí rozlišují velká a malá písmena):
        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Aggregate function</p></th>
        <th><p>Means</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>avg(x)</p></td>
        <td><p>Average (mean) value of x</p></td>
        </tr>
        <tr class="even">
        <td><p>count(x)</p></td>
        <td><p>Count of the values of x</p></td>
        </tr>
        <tr class="odd">
        <td><p>max(x)</p></td>
        <td><p>Maximum value of x</p></td>
        </tr>
        <tr class="even">
        <td><p>median(x)</p></td>
        <td><p>Median value of x</p></td>
        </tr>
        <tr class="odd">
        <td><p>min(x)</p></td>
        <td><p>Minimum value of x</p></td>
        </tr>
        <tr class="even">
        <td><p>percentileCont(p, x)</p></td>
        <td><p>Continuous percentile of x, where p is the percentile as a floating point number between 0 and 1. For example, p = 0 will return the lowest value, p = 0.5 will return the median, p = 0.75 will return the 75th percentile, p = 1 will return the highest value, etc. Continuous means that the value will be interpolated if necessary. For example, percentileCont( 0.5, #{FTRrcoaog83} ) will return 2.5 if the sampled values of data element FTRrcoaog83 are 1, 2, 3, and 4.</p></td>
        </tr>
        <tr class="odd">
        <td><p>stddev(x)</p></td>
        <td><p>Standard deviation of x. This function is eqivalent to stddevSamp. It's suggested that you use the function stddevSamp instead for greater clarity.</p></td>
        </tr>
        <tr class="even">
        <td><p>stddevPop(x)</p></td>
        <td><p>Population standard deviation of x: sqrt( sum( (x - avg(x))^2 ) / n )</p></td>
        </tr>
        <tr class="even">
        <td><p>stddevSamp(x)</p></td>
        <td><p>Sample standard deviation of x: sqrt( sum( (x - avg(x))^2 ) / ( n - 1 ) ). Note that this value is not computed when there is only one sample.</p></td>
        </tr>
        <tr class="odd">
        <td><p>sum(x)</p></td>
        <td><p>Sum of the values of x</p></td>
        </tr>
        </tbody>
        </table>

        Jakékoli položky uvnitř agregační funkce budou vyhodnoceny pro všechna vzorkovaná minulá období a poté kombinovány podle vzorce uvnitř agregační funkce. Jakékoli položky mimo agregační funkci budou vyhodnoceny pro období, ve kterém se provádí předpověď.

        Složitější výrazy můžete vytvořit kliknutím na (nebo zadáním) některého z prvků pod polem výrazu:  ( ) \* / + - Dny. Konstantní čísla lze přidat jejich zadáním. Možnost Dny vloží \[days\] do výrazu, který řeší počet dní v období, od kterého data pocházejí.

        Ve svém výrazu můžete také použít následující neagregující funkce, buď uvnitř agregačních funkcí, nebo obsahující agregační funkce, nebo nezávisle na agregačních funkcích:

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Function</p></th>
        <th><p>Means</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>if(test, valueIfTrue, valueIfFalse)</p></td>
        <td><p>Evaluates <strong>test</strong> which is an expression that evaluates to a boolean value -- see <strong>Boolean expression notes</strong> below. If the test is <strong>true</strong>, returns the <strong>valueIfTrue</strong> expression. If it is <strong>false</strong>, returns the <strong>valueIfFalse</strong> expression.</p></td>
        </tr>
        <tr class="even">
        <td><p>isNull(item)</p></td>
        <td><p>Returns the boolean value <strong>true</strong> if the <strong>item</strong> is null (missing), otherwise returns <strong>false</strong>. The <strong>item</strong> can be any selected item from the right (data element, program data element, etc.).</p></td>
        </tr>
        <tr class="odd">
        <td><p>isNotNull(item)</p></td>
        <td><p>Returns <strong>true</strong> if the <strong>item</strong> value is not missing (not null), otherwise <strong>false</strong>.</p></td>
        </tr>
        <tr class="even">
        <td><p>firstNonNull(item [, item ...])</p></td>
        <td><p>Returns the value of the first <strong>item</strong> that is not missing (not null). Can be provided any number of arguments. Any argument may also be a numeric or string literal, which will be returned if all the previous items have missing values.</p></td>
        </tr>
        <tr class="odd">
        <td><p>greatest(expression [, expression ...])</p></td>
        <td><p>Returns the greatest (highest) value of the expressions given. Can be provided any number of arguments.</p></td>
        </tr>
        <tr class="even">
        <td><p>least(expression [, expression ...])</p></td>
        <td><p>Returns the least (lowest) value of the expressions given. Can be provided any number of arguments.</p></td>
        </tr>
        </tbody>
        </table>

        **Poznámky k logickému výrazu:** Logický výraz musí být vyhodnocen jako **true** nebo **false**. Následující operátory lze použít k porovnání dvou hodnot, jejichž výsledkem je logický výraz: \<, \>, \!=, ==, \>=, a \<=. Následující operátory lze použít ke kombinaci dvou logických výrazů: && (logické AND) a || (logické OR). Unární operátor \! lze použít k negaci logického výrazu.

        Příklady výrazů generátoru:

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Generator expression</p></th>
        <th><p>Means</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>sum(#{FTRrcoaog83.tMwM3ZBd7BN})</p></td>
        <td><p>Sum of the sampled values of data element FTRrcoaog83 and category option combination (disaggregation) tMwM3ZBd7BN</p></td>
        </tr>
        <tr class="even">
        <td><p>avg(#{FTRrcoaog83}) + 2 * stddevSamp(#{FTRrcoaog83})</p></td>
        <td><p>Average of the sampled values of of data element FTRrcoaog83 (sum of all disaggregations) plus twice its sample standard deviation</p></td>
        </tr>
        <tr class="odd">
        <td><p>sum(#{FTRrcoaog83}) / sum([days])</p></td>
        <td><p>Sum of all sampled values of data element FTRrcoaog83 (sum of all disaggregations) divided by the number of days in all sample periods (resulting in the overall average daily value)</p></td>
        </tr>
        <tr class="even">
        <td><p>sum(#{FTRrcoaog83}) + #{T7OyqQpUpNd}</p></td>
        <td><p>Sum of all sampled values of data element FTRrcoaog83 plus the value of data element T7OyqQpUpNd in the period being predicted for</p></td>
        </tr>
        <tr class="odd">
        <td><p>1.2 * #{T7OyqQpUpNd}</p></td>
        <td><p>1.2 times the value of data element T7OyqQpUpNd, in the period being predicted for</p></td>
        </tr>
        <tr class="even">
        <td><p>if(isNull(#{T7OyqQpUpNd}), 0, 1)</p></td>
        <td><p>If the data element T7OyqQpUpNd is null in the period being predicted, then 0, otherwise 1.</p></td>
        </tr>
        <tr class="odd">
        <td><p>percentileCont(0.5, #{T7OyqQpUpNd})</p></td>
        <td><p>Continuous 50th percentile of the sampled values for data element T7OyqQpUpNd. Note that this is the same as median(#{T7OyqQpUpNd})</p></td>
        </tr>
        <tr class="even">
        <td><p>if(count(#{T7OyqQpUpNd}) == 1, 0, stddevSamp(#{T7OyqQpUpNd}))</p></td>
        <td><p>If there is one sample value present for data element T7OyqQpUpNd, then 0, otherwise the sample standard deviation of these sample values. (Note that if no samples are present then the stddevSamp returns no value, so no value is predicted.)</p></td>
        </tr>
        </tbody>
        </table>

11. (Volitelné) Vytvořte **Ukázkový test přeskočení**. Test přeskočení vzorku říká, která předchozí období, pokud existují, ze vzorku vyloučit.

    1.  Zadejte **Popis** testu přeskočení.

    2.  Zadejte výraz testu přeskočení vzorku. Výraz můžete vytvořit výběrem datových prvků pro agregovaná data nebo programových datových prvků, atributů nebo indikátorů. Počty organizačních jednotek ještě nejsou podporovány. Stejně jako u funkce generátoru můžete kliknout (nebo psát) na některý z prvků pod polem výrazu: ( ) \* / + - Dny.

        Neagregující funkce popsané výše mohou být také použity v testech přeskočení.

        Výraz musí být vyhodnocen na booleovskou hodnotu **true** nebo **false**. Viz **Poznámky booleovského výrazu** výše.

        Příklady testovacích výrazů přeskočení:

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Skip test expression</p></th>
        <th><p>Means</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>#{FTRrcoaog83} &gt; #{M62VHgYT2n0}</p></td>
        <td><p>The value of data element FTRrcoaog83 (sum of all disaggregations) is greater than the value of data element M62VHgYT2n0 (sum of all disaggregations)</p></td>
        </tr>
        <tr class="even">
        <td><p>#{uF1DLnZNlWe} &gt; 0</p></td>
        <td><p>The value of data element uF1DLnZNlWe (sum of all disaggregations) is greater than the zero</p></td>
        </tr>
        <tr class="odd">
        <td><p>#{FTRrcoaog83} &gt; #{M62VHgYT2n0} || #{uF1DLnZNlWe} &gt; 0</p></td>
        <td><p>The value of data element FTRrcoaog83 (sum of all disaggregations) is greater than the value of data element M62VHgYT2n0 (sum of all disaggregations) or the value of data element uF1DLnZNlWe (sum of all disaggregations) is greater than the zero</p></td>
        </tr>
        </tbody>
        </table>

12. Zadejte hodnotu **Sekvenční počet vzorků**.

    Jedná se o to, za kolik po sobě jdoucích období by se měl výpočet vrátit zpět v čase, aby byly k dispozici vzorky dat pro výpočty.

13. Zadejte hodnotu **Roční počet vzorků**.

    Jedná se o to, za kolik let by se měl výpočet vrátit zpět v čase, aby byly k dispozici údaje pro výpočty.

14. (Volitelné) Zadejte hodnotu **Sekvenční počet přeskočení**.

    To je to, kolik sekvenčních období, bezprostředně předcházejících období předpovídané hodnoty, by mělo být před vzorkováním přeskočeno.

15. Klikněte **Uložit**.

### Vytvořte nebo upravte skupinu prediktorů { #create_predictor_group }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Skupina Predictor**.

2.  Klikněte na tlačítko Přidat.

3.  Zadejte **název**. Toto pole musí být jedinečné.

4.  (Volitelné) V poli **Kód** přiřaďte kód. Toto pole musí být jedinečné.

5.  (Volitelné) Zadejte **Popis**.

6.  Poklepejte na **Prediktory**, které chcete skupině přiřadit.

7.  Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte nabízené zprávy { #manage_push_report }

### O nabízených zprávách { #about_push_report }

Nabízené zprávy vám umožňují zvýšit povědomí a využití analýzy dat zasláním zpráv s grafy, tabulkami a mapami přímo na e-mailové adresy uživatelů.

-   Nabízená zpráva získává svůj obsah ze stávajících ovládacích panelů.

-   Seznam nabízených zpráv obsahuje seznam položek ovládacího panelu ve stejném pořadí jako na ovládacím panelu.

-   Nabízená zpráva může obsahovat pouze položky ovládacího panelu s grafy, mapami nebo tabulkami.

-   Vytvoříte nabízenou zprávu a její plán v aplikaci **Údržba**.

-   Parametry **Název** a **Zpráva**, které jste nastavili v aplikaci **Údržba**, jsou součástí každého přehledu. **Název**, které uvedete v přehledu, není v přehledu zahrnuto. Místo toho se název používá k identifikaci objektu nabízené analýzy v systému. Tímto způsobem lze sestavu pojmenovat jedna věc a název sestavy může být jiný.

-   Když spustíte úlohu Nabízeného hlášení, systém sestaví seznam příjemců ze skupin uživatelů, které jste vybrali. Systém poté vygeneruje zprávu pro každého člena vybraných skupin uživatelů. Každá z položek ovládacího panelu je generována speciálně pro každého uživatele. To znamená, že data obsažená v hlášení odrážejí data, ke kterým má uživatel přístup. Všichni uživatelé by proto mohli získat stejný přehled (pokud jsou všechna data „statická“) nebo vlastní přehledy (jsou-li všechna data „dynamická“) nebo jejich kombinace.

-   Nabízené zprávy jsou zasílány e-mailem příjemcům, nikoli prostřednictvím interního systému zasílání zpráv DHIS2. Pokud uživatel nemá platný e-mail nebo pokud úloha selže, žádné e-maily se neposílají. V takovém případě je problém zaznamenán na serveru.

> **Poznámka**
>
> Data generovaná v nabízených zprávách jsou veřejná, proto ověřte, zda neobsahujete žádná citlivá data.

![](resources/images/maintainence/push_report_ex.png)

V aplikaci **Údržba** spravujete následující objekty nabízených sestav:

<table>
<caption> Objekty Nabízených hlášení zpráv v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Analýza nabízených hlášení zpráv</p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti, překládat, prohlížet a spouštět </p> </td>
</tr>
</tbody>
</table>

### Vytvořte nebo upravte nabízenou zprávu { #create_push_report }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Nabídnutá Analýza**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název naplánovaného přehledu.

    Tento název není zahrnut v e-mailu se zprávou. Místo toho se název používá k identifikaci objektu nabídnuté analýzy v systému.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  Přidejte zprávě **Nadpis**.

    Tento název je obsažen v e-mailu se zprávou.

6.  (Volitelné) Přidejte **Sdělení**.

    Toto sdělení je obsaženo v e-mailu se zprávou.

7.  Vyberte **Dashboard**, na kterém bude sestava založena.

8.  Vyberte a přiřaďte skupiny uživatelů, kterým chcete zprávu odeslat.

9.  Vyberte **frekvenci plánování**: **Denně**, **Týdně** nebo **Měsíčně**.

    > **Note**
    >
    > If you schedule a push report to "Monthly" and "31", the scheduled report job will not run if the month has less than 31 days.

10. (Volitelné) Výběrem možnosti **Povolit** aktivujete úlohu nabídnuté zprávy.

    Úloha se nespustí, dokud ji neaktivujete.

11. Klikněte **Uložit**.

### Náhled nabízených zpráv { #preview_push_report }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Nabídnutá Analýza**.

2.  V seznamu nabízených hlášení zpráv vyhledejte nabízenou zprávu, jejíž náhled chcete zobrazit.

3.  Klikněte na nabídku možností a vyberte **Náhled**.

    Náhled nové zprávy se otevře v novém okně.

### Spusťte úlohy nabízených zpráv { #run_push_report }

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Nabídnutá Analýza**.

2.  V seznamu nabízených zpráv vyhledejte nabízenou zprávu, kterou chcete spustit.

3.  Klikněte na nabídku možností a vyberte možnost **Spustit**.

    Úloha nabízené zprávy se spustí okamžitě.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte externí vrstvy mapy { #manage_external_maplayer }

### O externích mapových vrstvách { #about_gis_map_layers }

Můžete přizpůsobit GIS zahrnutím mapových vrstev z různých zdrojů a kombinovat je s vašimi vlastními daty v DHIS2. DHIS2 podporuje běžné formáty mapových služeb, jako jsou například Web Map Service (WMS), Tile Map Service (TMS) a dlaždice XYZ.

### Vytvořte nebo upravte externí vrstvu mapy { #create_external_map_layer }

> **Poznámka**
>
> DHIS2 podporuje pouze projekci Web Mercator ([EPSG:3857](https://epsg.io/3857)), takže se ujistěte, že externí služba tuto projekci podporuje.

<table>
<caption> Externí mapové vrstvy objektů v aplikaci Údržba </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Externí mapová vrstva </p> </td>
<td> <p> Vytvářet, upravovat, klonovat, mazat, zobrazovat podrobnosti a překládat </p> </td>
</tr>
</tbody>
</table>

1.  Otevřete aplikaci **Údržba** a klikněte na **Jiné** \> **Externí vrstva mapy**.

2.  Klikněte na tlačítko Přidat.

3.  Do pole **Název** zadejte název, který popisuje obsah externí vrstvy mapy.

    Toto je název, který uvidíte v aplikaci **Mapy**.

4.  (Volitelné) V poli **Kód** přiřaďte kód.

5.  Vyberte formát **Mapové služby**.

    DHIS2 podporuje tři běžné formáty mapových služeb:

    -   Web Map Service (WMS)

        **Formát obrázku**: Formát PNG umožňuje transparentní vrstvy, formát JPG nabízí lepší kompresi a často se načítá rychleji.

        **Vrstvy**: WMS může obsahovat několik jednotlivých vrstev a můžete určit, které chcete zahrnout (oddělené čárkami). Dostupné vrstvy najdete v dokumentu WMS GetCapabilities.

    -   Tile Map Service (TMS)

    -   Dlaždice XYZ (lze použít i pro WMTS)

6.  Zadejte **URL** do mapové služby.

    > **Note**
    >
    > XYZ and TMS URLs must contain placeholders {}, for example: http://{s}.tile.osm.org/{z}/{x}/{y}.png.

7.  (Volitelné) Zadejte **Zdroj** vrstev mapy. Pokud chcete odkazovat na zdroj, může pole obsahovat značky HTML.

    Když používáte externí mapovou službu, je důležité zdůraznit, odkud data pocházejí.

8.  Vyberte **umístění**:

    -   **Spodní - podkladová mapa**: U aplikace Mapy je tato vrstva externí mapy volitelná jako základní mapa (tj. Jako alternativa k základním mapám DHIS2).

    -   **Horní - překrytí**: U aplikace Mapy to umožňuje přidat externí mapu z výběru Přidat vrstvu a umístit ji kdekoli nad základní mapu.

9.  (Volitelné) Přidejte legendu.

    Legendu můžete přidat dvěma způsoby:

    -   Vyberte předdefinovanou **legendu** k popisu barev vrstvy mapy.

        > **Tip**
        >
        > Click **Add new** to create legends that you're missing. In the form that opens, create the legends you need. When you're done, click **Refresh values**.

    -   Zadejte odkaz na legendu externího obrázku do **URL obrázku legendy**.

        Ty jsou často poskytovány pro WMS. Viz pod LegendURL v dokumentu WMS GetCapabilites.

10. Klikněte **Uložit**.

### Klonujte objekty metadat { #clone_metadata }

Klonování datového prvku nebo jiných objektů může ušetřit čas při vytváření mnoha podobných objektů.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete klonovat.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Klonovat**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstraňte objekty metadat { #delete-metadata-objects }

> **Poznámka**
>
> Datový prvek a další objekty datových prvků můžete odstranit, pouze pokud k samotnému datovému prvku nejsou přidružena žádná data.

> **Varování**
>
> Jakákoli sada dat, kterou ze systému odstraníte, je nenávratně ztracena. Odebrány budou také všechny formuláře pro zadávání údajů a formuláře oddílů, které mohly být vyvinuty. Před odstraněním jakékoli datové sady se ujistěte, že jste vytvořili zálohu své databáze, pro případ, že byste ji v určitou dobu potřebovali obnovit.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete odstranit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Odstranit**.

3.  Klikněte na **Potvrdit**.

### Zobrazit podrobnosti o objektech metadat { #display-details-of-metadata-objects }

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete zobrazit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Zobrazit podrobnosti**.

### Přeložte objekty metadat { #translate-metadata-objects }

DHIS2 poskytuje funkce pro překlady obsahu databáze, například datových prvků, skupin datových prvků, indikátorů, skupin indikátorů nebo organizačních jednotek. Tyto prvky můžete přeložit na libovolný počet národních prostředí. Národní prostředí představuje konkrétní geografickou, politickou nebo kulturní oblast.

> **Tip**
>
> Chcete-li aktivovat překlad, otevřete aplikaci **Nastavení systému**, klikněte na \> > **Vzhled** a vyberte jazyk.

1.  Otevřete aplikaci **Údržba** a najděte typ objektu metadat, který chcete přeložit.

2.  V seznamu objektů klikněte na nabídku možností a vyberte **Přeložit**.

    > **Tip**
    >
    > If you want to translate an organisation unit level, click directly on the **Translate** icon next to each list item.

3.  Vyberte národní prostředí.

4.  Zadejte **Název**, **Zkrácený název** a **Popis**.

5.  Klikněte **Uložit**.

## Spravujte SQL pohledy { #maintenance_sql_view }

Funkce SQL pohled DHIS2 interně uloží definici pohledu SQL a poté na vyžádání zhmotní pohled.

Správci databází musí být opatrní při vytváření pohledů databáze přímo v databázi DHIS2. Například když se vygenerují tabulky prostředků, všechny budou nejprve zrušeny a poté znovu vytvořeny. Pokud jakékoli zobrazení SQL závisí na těchto tabulkách, bude vyvolána výjimka narušení integrity a proces bude zrušen.

Pohledy SQL jsou položeny v obráceném abecedním pořadí na základě jejich názvů v DHIS2 a jsou vytvořeny v běžném abecedním pořadí. To vám umožní mít závislosti mezi pohledy SQL, vzhledem k tomu, že pohledy závisí pouze na jiných pohledech, které přicházejí dříve v abecedním pořadí. Například „ViewB“ může bezpečně záviset na „ViewA“. Jinak výsledkem zobrazení v závislosti na jiném zobrazení bude chyba narušení integrity.

### Vytváření nového pohledu SQL { #creating-a-new-sql-view }

Chcete-li vytvořit nový pohled SQL, klikněte na **Aplikace** \> **Údržba** \> **Jiné** \> **SQL Pohled** a klikněte na tlačítko Přidat **+**.

![](resources/images/maintainence/create_sql_view.PNG)

Atribut "Název" pohledu SQL bude použit k určení názvu tabulky, kterou DHIS2 vytvoří, když se pohled zhmotní uživatelem. Atribut "Popis" umožňuje poskytnout popisný text o tom, co pohled SQL ve skutečnosti dělá. Nakonec by měl "dotaz SQL" obsahovat definici pohledu SQL. Jsou povoleny pouze příkazy SQL „SELECT“ a určité citlivé tabulky (tj. Informace o uživateli) nejsou přístupné. Stisknutím tlačítka „Uložit“ uložíte definici pohledu SQL.

### Správa SQL Pohledů { #sql-view-management }

Chcete-li využít pohledy SQL, jednoduše klikněte na pohled a v místní nabídce zvolte možnost „Provést dotaz“. Po dokončení procesu budete informováni, že byla vytvořena tabulka. Bude zadán název tabulky a skládá se z atributu „Popis“ uvedeného v definici pohledu SQL. Jakmile je zobrazení vygenerováno, můžete jej zobrazit opětovným kliknutím na zobrazení a výběrem možnosti „Zobrazit pohled SQL“.

> **Tip**
>
> Pokud máte pohled, který závisí na jiném pohledu, měli byste být opatrní, jak jsou pohledy pojmenovány. Když je analýza spuštěna na serveru DHIS2, musí být všechny pohledy zrušeny a musí být znovu vytvořeny. Při spuštění analýzy se pohledy zruší v abecedním pořadí a poté se znovu vytvoří v opačném abecedním pořadí. Pokud tedy pohled A závisí na pohledu B, musí se zobrazit před pohledem B v abecedním pořadí. Pokud se zobrazí po zobrazení B v abecedním pořadí, může dojít k selhání analýzy, protože zobrazení se závislostmi nebude zrušeno ve správném pořadí.

## Spravujte národní prostředí { #maintenance_locale_management }

V DHIS2 je možné vytvořit vlastní národní prostředí. Kromě národních prostředí dostupných v systému můžete do systému přidat vlastní národní prostředí, například „Angličtina“ a „Zambie“. To by vám umožnilo přeložit objekty metadat do místních jazyků nebo zohlednit nepatrné varianty mezi zeměmi, které používají společnou definici metadat.

![](resources/images/maintainence/locale_management.png)

Národní prostředí se skládá z jazyka a země. Vyberte požadované hodnoty a stiskněte „Přidat“. Toto vlastní národní prostředí bude nyní k dispozici jako jedno z národních prostředí překladu v systému.

## Úpravy více skupin objektů najednou { #edit_multiple_object_groups }

**Editor skupiny metadat** v aplikaci **Údržba** umožňuje upravovat více skupin objektů najednou. Můžete upravit následující typy objektů:

<table>
<caption> Typy objektů v editoru skupin metadat </caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Možnost kategorie </p> </td>
<td> </td>
</tr>
<tr class="even">
<td> <p> skupina možností kategorie </p> </td>
<td> </td>
</tr>
<tr class="odd">
<td> <p> Datový prvek </p> </td>
<td> <p> Přidat jeden datový prvek do více skupin datových prvků </p>
<p> Odebrat jeden datový prvek z více skupin datových prvků </p> </td>
</tr>
<tr class="even">
<td> <p> skupina datových prvků </p> </td>
<td> <p> Přidat více datových prvků do jedné skupiny datových prvků </p>
<p> Odebrat více datových prvků z jedné skupiny datových prvků </p> </td>
</tr>
<tr class="odd">
<td> <p> indikátor </p> </td>
<td> <p> Přidat jeden indikátor do více skupin indikátorů </p>
<p> Odebrat jeden indikátor z více skupin indikátorů </p> </td>
</tr>
<tr class="even">
<td> <p> skupina indikátorů </p> </td>
<td> <p> Přidat více indikátorů do jedné skupiny indikátorů </p>
<p> Odebrání více indikátorů z jedné skupiny indikátorů </p> </td>
</tr>
</tbody>
</table>

### Upravte více objektů ve skupině objektů { #edit-multiple-objects-in-an-object-group }

1.  Otevřete aplikaci **Údržba** a klikněte na **Editor skupiny metadat**.

2.  Klikněte na **Správa položek ve skupině**.

3.  Vyberte typ skupiny objektů, například **Skupiny indikátorů**.

4.  Vyberte skupinu objektů, například **HIV**.

5.  V levém seznamu vyberte objekt(y), které chcete přidat do skupiny objektů, a klikněte na šipku doprava.

6.  V pravém seznamu vyberte objekt(y), které chcete odebrat ze skupiny objektů, a klikněte na šipku doleva.

### Upravte objekt ve více skupinách objektů { #edit-an-object-in-multiple-object-groups }

1.  Otevřete aplikaci **Údržba** a klikněte na **Editor skupiny metadat**.

2.  Klikněte na **Spravovat skupiny pro položku**.

3.  Vyberte typ objektu, například **Indikátory**.

4.  Vyberte objekt, například **ANC LLITN pokrytí**.

5.  V seznamu nalevo vyberte skupinu(y) objektů, do kterých chcete přidat objekt, a klikněte na šipku doprava.

6.  V seznamu napravo vyberte skupinu(y) objektů, ze kterých chcete objekt odebrat, a klikněte na šipku doleva.
