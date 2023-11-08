---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-capture-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Capture { #capture_app }

## O aplikaci Capture { #about_capture_app }

Aplikace Capture slouží jako náhrada za aplikaci Event Capture. V budoucnu je záměrem začlenit aplikaci Tracker Capture a aplikaci Data Entry do aplikace Capture.

V aplikaci Capture registrujete události, ke kterým došlo v konkrétním čase a místě. Událost se může stát v kterémkoli daném okamžiku. To je v rozporu s rutinními daty, která lze zachytit v předdefinovaných pravidelných intervalech. Události se někdy nazývají případy nebo záznamy. V DHIS2 jsou události propojeny s programem. Aplikace Capture vám umožňuje vybrat organizační jednotku a program a určit datum, kdy k události došlo, před zadáním informací o události.

## Zaregistrujte událost { #capture_register_event }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

    Uvidíte pouze programy spojené s vybranou organizační jednotkou a programy, ke kterým máte přístup, a které jsou sdíleny s vaší uživatelskou skupinou prostřednictvím sdílení na úrovni dat.

4. Pokud má program nastavenou kombinaci kategorií, bude nutné vybrat možnost kategorie.

5. Klikněte na **Nový**.

    ![vytvořit novou událost](resources/images/capture_app/create_new_event.png)

6. Vyplňte požadované informace. Pokud je programová fáze programu nakonfigurována k zachycení umístění:

    - Pokud se jedná o pole souřadnicového pole, můžete buď zadat souřadnice přímo, nebo můžete kliknout na ikonu **mapa** nalevo od pole souřadnic. Ten pak otevře mapu, kde můžete vyhledat místo nebo na něj přímo kliknout na mapě.

    - Pokud jde o pole polygon, můžete kliknout na ikonu **mapa** nalevo od pole. Otevře se mapa, kde můžete vyhledat místo a zaznamenat polygon (tlačítko v horním rohu mapy).

7. V případě potřeby můžete přidat komentář kliknutím na tlačítko **Napsat komentář** v dolní části formuláře.

8. V případě potřeby můžete přidat vztah kliknutím na tlačítko **Přidat vztah** ve spodní části formuláře. Další informace najdete v části o **Přidání vztahu**.

9. Klikněte na **Uložit a ukončit** nebo klikněte na šipku vedle tlačítka a vyberte **Uložit a přidat další**.
    - **Uložit a přidat další** uloží aktuální událost a vymaže formulář. Všechny události, které jste zachytili, se zobrazí v seznamu v dolní části stránky. Pokud chcete dokončit zachycení událostí, můžete, pokud je formulář prázdný, klikněte na tlačítko Dokončit nebo pokud váš formulář obsahuje data, klikněte na šipku vedle **Uložit a přidat další** a vyberte **Uložit a ukončit**.

> Poznámka 1: Některé datové prvky v události mohou být povinné (označené červenou hvězdičkou vedle štítku datového prvku). To znamená, že všechny povinné datové prvky musí být vyplněny, než bude uživateli povoleno dokončit událost. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření požadovaných polí v nástroji Trasovač and Zachycení události“.** Pokud má uživatel toto oprávnění, nebude nutné před uložením vyplňovat povinné datové prvky. a červená hvězdička se nezobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

> Poznámka 2: Formulář pro zadávání údajů lze také zobrazit v **zobrazení řádek**. V tomto režimu jsou datové prvky uspořádány vodorovně. Toho lze dosáhnout kliknutím na tlačítko **Přepnout na zobrazení řádků** v pravém horním rohu formuláře pro zadávání údajů. Pokud jste aktuálně v **řádkovém zobrazení**, můžete přepnout na výchozí zobrazení formuláře kliknutím na tlačítko **Přepnout do zobrazení formuláře** v pravém horním rohu formuláře pro zadávání údajů.

## Přidání vztahu { #capture_add_relationship }

Vztahy lze přidat buď během registrace, úpravy nebo prohlížení události. Aktuálně **aplikace Capture** podporuje pouze vztahy _Událost ku instanci trasované entity_.

1. V případě události klikněte na **Přidat vztah**.

2. Vyberte typ vztahu, který chcete vytvořit.

-   Nyní máte dvě možnosti: **Odkaz na existující instanci trasované entity** nebo **Vytvořit novou instanci trasované entity**.

![možnosti vztahu](resources/images/capture_app/relationship_options.png)

### Odkaz na existující instanci trasované entity { #link-to-an-existing-tracked-entity-instance }

3. Klikněte na **Odkaz na existující instanci trasované entity**.

-   Nyní by se vám měly zobrazit některé možnosti hledání **instance trasované entity**. Máte možnost vybrat si **program**. Pokud je vybrán **program**, atributy jsou odvozeny od vybraného **programu**. Pokud není vybrán žádný **program**, budou viditelné pouze atributy, které patří do **Instance trasované entity**.

      ![hledat instanci trasované entity](resources/images/capture_app/search_tei.png)

    -   Pokud je **Instance trasované entity** nebo **program** nakonfigurován s jedinečným atributem, lze tento atribut použít k vyhledání konkrétní **instance trasované entity** nebo **programu**. Tento atribut by měl být uveden samostatně. Po vyplnění pole jedinečného atributu klikněte na tlačítko **Hledat** umístěné přímo pod polem jedinečného atributu.

    -   Pokud má **Instance trasované entity** nebo **program** atributy, pak je lze použít k vyhledávání rozšířením pole **Hledat podle atributů**. Po vyplnění všech požadovaných polí atributů klikněte dole na tlačítko **Hledat podle atributů**. Hledání můžete také omezit nastavením **Rozsah organizační jednotky**. Pokud je nastaveno na _Všechny přístupné_, budete hledat **Instance trasované entity** ve všech organizačních jednotkách, ke kterým máte přístup. Pokud vyberete _Vybrané_, budete vyzváni k výběru organizačních jednotek, ve kterých chcete hledat.

4. Po úspěšném vyhledávání se zobrazí seznam **trasovaných Instancí entity**, které odpovídají kritériím vyhledávání. Chcete-li vytvořit vztah, klikněte na tlačítko **Odkaz** na **Trasovaná instance entity**, ke které chcete vytvořit vztah.

-   Pokud jste nenašli hledanou **instanci trasované entity**, můžete kliknout na tlačítka **Nové hledání** nebo **Upravit hledání**. **Nové hledání** vás přenese na nové prázdné vyhledávání, zatímco **Upravit hledání** vás vrátí zpět k právě provedenému vyhledávání, přičemž budou zachována kritéria vyhledávání.

### Vytvořte novou instanci trasované entity { #create-new-tracked-entity-instance }

3. Klikněte na **Vytvořit novou instanci trasované entity**.

-   Nyní se vám zobrazí formulář pro registraci nové **instance trasované entity**. Můžete si vybrat, zda budete registrovat s programem nebo bez něj. Pokud je vybrán program, bude do uvedeného programu zaregistrována nová **instance trasované entity**. Můžete také změnit **organizační jednotku** odebráním automaticky nastavené jednotky a výběrem nové.

    ![registrovat novou instanci trasované entity](resources/images/capture_app/register_tei.png)

4. Vyplňte požadované (a případně povinné) atributy a podrobnosti registrace.

5. Klikněte na **Vytvořit instanci trasované entity a odkaz**.

> Poznámka: Při vyplňování údajů se můžete setkat s upozorněním, že byl nalezen možný duplikát. Kliknutím na varování zobrazíte tyto duplikáty, a pokud se duplikát shoduje, můžete kliknout na tlačítko **Propojit** a propojit tuto **instanci trasované entity**. Pokud se varování zobrazuje i po dokončení vyplňování dat, tlačítko **Vytvořit sledovanou instanci entity a odkaz** neuvidíte. Místo toho budete stisknuti tlačítkem s názvem **Zkontrolovat duplikáty**. Po kliknutí na toto tlačítko se zobrazí seznam možných duplikátů. Pokud se některý z těchto duplikátů shoduje s instancí **trasované entity**, kterou se pokoušíte vytvořit, můžete kliknout na tlačítko **Odkaz**, pokud ne, kliknutím na tlačítko **Uložit jako novou osobu** zaregistrovat novou **Instance trasované entity**.

## Upravit událost { #capture_edit_event }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Všechny události registrované k vybranému programu se zobrazí v seznamu.

4. Klikněte na událost, kterou chcete upravit.

5. Klikněte na tlačítko **Upravit událost**.

6. Upravte podrobnosti události a klikněte na **Uložit**.

## Smazat událost { #capture_delete_event }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Všechny události registrované k vybranému programu se zobrazí v seznamu.

4. Klikněte na ikonu **trojitá tečka** u události, kterou chcete smazat.

5. V zobrazené nabídce klikněte na **Smazat událost**.

    ![smazat událost](resources/images/capture_app/delete_event.png)

## Upravte rozložení seznamu událostí { #capture_modify_event_list_layout }

Můžete vybrat, které sloupce se mají zobrazit nebo skrýt v seznamu událostí. To může být užitečné například v případě, že máte k programové fázi přiřazen dlouhý seznam datových prvků.

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Všechny události registrované k vybranému programu se zobrazí v seznamu.

4. Klikněte na ikonu **ozubeného kola** v pravém horním rohu seznamu událostí.

5. Vyberte sloupce, které chcete zobrazit, a klikněte na **Uložit**.

    ![upravit seznam událostí](resources/images/capture_app/modify_event_list.png)

> Poznámka: Pořadí datových prvků můžete reorganizovat jejich přetažením do seznamu.

## Filtrování seznamu událostí { #capture_filter_event_list }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Všechny události registrované k vybranému programu se zobrazí v seznamu.

   V horní části seznamu událostí jsou tlačítka se stejnými názvy jako záhlaví sloupců v seznamu.

4. Pomocí tlačítek v horní části seznamu můžete filtrovat podle data sestavy nebo konkrétního datového prvku.

    ![filtrování události](resources/images/capture_app/filter_event.png)

> Poznámka: Datové prvky budou mít mírně odlišný způsob filtrování. Například datový prvek **Počet** zobrazí filtrování, zatímco datový prvek **Text** vás požádá o zadání vyhledávacího dotazu, na který chcete filtrovat.

## Třídit seznam událostí { #capture_sort_event_list }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program. Všechny události registrované k vybranému programu se zobrazí v seznamu.

4. Kliknutím na jedno ze záhlaví sloupců seřadíte seznam u daného datového prvku vzestupně.

   Vedle sloupce se zobrazuje malá šipka nahoru, která ukazuje, že seznam je seřazen vzestupně.

5. Opětovným kliknutím na záhlaví sloupce seřadíte seznam u daného datového prvku v sestupném pořadí.

   Vedle sloupce se zobrazuje malá šipka dolů, která ukazuje, že seznam je seřazen sestupně.

    ![událost řazení](resources/images/capture_app/sort_event.png)

## Stáhněte si seznam událostí { #capture_download_event_list }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program. Všechny události registrované k vybranému programu se zobrazí v seznamu.

4. Klikněte na ikonu **šipka dolů** v pravém horním rohu seznamu událostí.

5. Vyberte formát, který chcete stáhnout.

    ![stáhnout seznam událostí](resources/images/capture_app/download_event_list.png)

> Poznámka: Seznam událostí si můžete stáhnout ve formátech JSON, XML nebo CSV.

## Předdefinovaná zobrazení seznamu { #capture_views }

Můžete nastavit vlastní Pohledy a uložit je pro pozdější použití. Pohledy lze také sdílet s ostatními. Pohled se skládá z filtrů, pořadí sloupců a pořadí řazení událostí.

### Ukládání nového pohledu { #capture_view_save }

1. Vyberte organizační jednotku a program.

2. Nastavit filtry pomocí tlačítek filtru nad seznamem událostí (podrobně popsáno [zde](#capture_filter_event_list)).

![](resources/images/capture_app/view_save_filters.png)

3. Pořadí sloupců nastavíte kliknutím na ikonu ozubeného kola a poté ve vyskakovacím okně určíte rozložení podle svých preferencí (jak upravit rozložení je podrobně popsáno [zde](#capture_modify_event_list_layout)).

![](resources/images/capture_app/view_save_column_order.png)

4. Události seřaďte kliknutím na jedno ze záhlaví sloupců (podrobně popsáno [zde](#capture_sort_event_list)).

![](resources/images/capture_app/view_save_sort_order.png)

5. Otevřete nabídku Další (ikona se třemi tečkami) vpravo a poté vyberte možnost „Uložit aktuální zobrazení ...“

![](resources/images/capture_app/view_save_menu.png)

6. Vyplňte název pohledu a klikněte na Uložit.

![](resources/images/capture_app/view_save_name.png)

### Načítání pohledu { #capture_view_load }

1. Vyberte organizační jednotku a program s předdefinovaným zobrazením.

2. Pohledy by měly být k dispozici nad samotným seznamem událostí. Kliknutím na zobrazení jej načtete.

![](resources/images/capture_app/view_load_unselected.png)

3. Příklad načteného pohledu.

![](resources/images/capture_app/view_load_selected.png)

### Aktualizace pohledu { #capture_view_update }

1. Načtěte pohled, který chcete aktualizovat (viz [načítání pohledu](#capture_view_load)).

2. Proveďte změny filtrů, pořadí sloupců nebo pořadí řazení událostí.

> **Poznámka**
>
> Když má pohled neuložené změny, je k názvu pohledu přidána hvězdička (\*).

3. Otevřete nabídku Další (ikona se třemi tečkami) vpravo a poté vyberte možnost „Aktualizovat zobrazení“.

![](resources/images/capture_app/view_update.png)

### Sdílení pohledu { #capture_view_share }

1. Načtěte pohled, který chcete sdílet (viz [načítání pohledu](#capture_view_load)).

2. Otevřete nabídku Další (ikona se třemi tečkami) vpravo a poté vyberte možnost „Sdílet zobrazení ...“

![](resources/images/capture_app/view_share.png)

3. Proveďte změny. Obvykle byste přidali uživatele / skupiny (1) a / nebo změnili přístupová práva uživatelů / skupin přidaných dříve (2).

![](resources/images/capture_app/view_share_access.png)

### Mazání pohledu { #capture_view_delete }

1. Načtěte pohled, který chcete smazat (viz [načítání pohledu](#capture_view_load)).

2. Otevřete další nabídku (ikona se třemi tečkami) vpravo a poté vyberte možnost „Odstranit zobrazení“.

![](resources/images/capture_app/view_delete.png)

## Přiřazení uživatele { #capture_user_assignment }

Události lze přiřadit uživatelům. Tato funkce musí být povolena pro každý program.

### Přiřazování nových událostí { #capture_user_assignment_new }

1. Vyberte organizační jednotku a program s povoleným přiřazením uživatelů.

2. Klikněte na **Nová událost** v pravém horním rohu.

3. Sekce postupníka najdete v dolní části stránky pro zadávání údajů. Vyhledejte a vyberte uživatele, kterému chcete událost přiřadit. Při uložení události bude postupník zachován.

    ![](resources/images/capture_app/user_assignment_new.png)

    ![](resources/images/capture_app/user_assignment_new_filled.png)

### Změnit přiřazeného { #capture_user_assignment_edit }

1. Vyberte organizační jednotku a program s povoleným přiřazením uživatelů.

2. Klikněte na událost v seznamu

3. V pravém sloupci najdete sekci postupníka.

    ![](resources/images/capture_app/user_assignment_edit.png)

4. Klikněte na tlačítko úprav nebo na tlačítko **Přiřadit**, pokud událost není aktuálně nikomu přiřazena.

    ![](resources/images/capture_app/user_assignment_edit_button.png)

    ![](resources/images/capture_app/user_assignment_edit_add.png)

5. Vyhledejte a vyberte uživatele, kterému chcete událost znovu přiřadit. Úkol se okamžitě uloží.

### Postupník v seznamu událostí { #capture_user_assignment_event_list }

V seznamu událostí budete moci zobrazit postupníka na jednu událost. Kromě toho můžete seznam třídit a filtrovat podle postupníka.

#### Filtrovat podle přiřazeného { #filter-by-assignee }

1. Klikněte na filtr **Přiřazeno k**.

    ![](resources/images/capture_app/user_assignment_event_list.png)

2. Vyberte preferovaný filtr přiřazeného a klikněte na tlačítko Aktualizovat.

    ![](resources/images/capture_app/user_assignment_event_list_options.png)

## Trasovací programy { #capture_tracker_programs }

Aplikace Capture zatím nepodporuje trasovací programy, ale trasovací programy jsou stále uvedeny. Pokud vyberete trasovací program, aplikace vás dovede k aplikaci Tracker Capture, jak je uvedeno níže.

![](resources/images/capture_app/tracker_program.png)
