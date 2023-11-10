---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-tracker-capture-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Tracker Capture { #tracker_capture_app }

## O aplikaci Tracker Capture { #about_tracker_capture_app }

![](resources/images/tracker_capture/tracker-capture-tei-list.png)

Aplikace **Tracker Capture** je pokročilá verze aplikace Event Capture = **Zachycení Události**.

-   **Zachycení Události**: zpracovává jednotlivé události _bez_ registrace

-   **Tracker Capture**: zpracovává více událostí (včetně jedné události) _s_ registrací.

-   Zachytáváte data událostí pro zaregistrovanou instanci trasované entity (TEI).

-   Uvidíte pouze programy přidružené k organizační jednotce, kterou jste vybrali, a programy, ke kterým máte přístup prostřednictvím své uživatelské role.

-   Možnosti, které vidíte ve funkcích vyhledávání a registrace, závisí na vybraném programu. Atributy programu řídí tyto možnosti. Atributy také určují názvy sloupců v seznamu TEI.

    Pokud nevyberete program, systém vybere výchozí atributy.

-   Během registrace jsou podporovány chybové i varovné zprávy přeskočení logiky i ověření.

-   Když zavřete organizační jednotku, nemůžete registrovat ani upravovat události v této organizační jednotce v aplikaci **Tracker Capture**. Stále můžete hledat TEI a filtrovat výsledky hledání. Můžete také zobrazit ovládací panel konkrétního TEI.

## O ovládacích panelech instance trasované entity (TEI) { #about_tracked_entity_instance_dashboard }

![](resources/images/tracker_capture/tei_dashboard.png)

TEI spravujete z ovládacího panelu TEI v aplikaci **Tracker Capture**.

-   Ovládací panel se skládá z widgetů. Přetáhněte widgety a umístěte je v pořadí a na požadované místo.

-   Kliknutím na ikonu špendlíku přilepíte pravý sloupec widgetů na pevnou pozici. To je užitečné zejména při zadávání dat.

    Pokud máte k vyplnění mnoho datových prvků nebo velký formulář, nalepte pravý sloupec widgetu. Pak všechny widgety, které jste umístili do pravého sloupce, zůstanou viditelné při posouvání v části zadávání dat.

-   U každého indikátoru definovaného pro vybraný program bude jeho hodnota vypočítána a zobrazena v widgetu **Indikátory**.

-   Navigace:

    -   **Zpět**: vrací vás zpět na stránku vyhledávání a registrace

    -   Tlačítka Předchozí a Další: přejdete na předchozí nebo následující ovládací panel TEI v seznamu výsledků vyhledávání TEI

    <!-- konec seznamu -->

    -   Pole **Jiné programy**: pokud je TEI zapsán do jiných programů, jsou zde uvedeny. Kliknutím na program změníte program, pro který zadáváte data pro vybraný TEI. Když změníte programy, změní se také obsah widgetů.

## Pracovní postup { #workflow_tracker_capture }

Pracovní proces programu zdraví matek a dětí

![](resources/images/patients_programs/name_based_information_tracking_process.png)

1.  Vytvořte nový nebo najděte stávající TEI.

    Můžete vyhledávat podle definovaných atributů, například jména nebo adresy.

2.  Zaregistrujte TEI do programu.

3.  Na základě služeb programu v době, aplikace vytvoří plán aktivit pro TEI.

4.  TEI poskytuje různé služby v závislosti na programu. Všechny služby jsou zaznamenány.

5.  Informace o jednotlivých případech použijte k vytváření zpráv.

## Propojení s aplikací Tracker Capture { #linking_to_the_tracker_capture_app }

### Odkaz na konkrétní program na domovské obrazovce { #link-to-a-specific-program-on-the-home-screen }

Výběr programu můžete sdílet na domovské obrazovce.

1. Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2. Vyberte program, který chcete propojit.

3. Zkopírujte adresu URL.

    - Zkontrolujte, zda adresa URL obsahuje parametr „program“.

4. Vložte adresu URL do metody sdílení podle vašeho výběru, například e-mail nebo zprávu v rámci DHIS2.

> Poznámka: Pokud program ve vybrané organizační jednotce (která je uložena v místní mezipaměti) neexistuje, systém místo toho vybere první dostupný program pro tuto organizační jednotku. Pokud je místní mezipaměť prázdná / čistá a kořenová organizační jednotka aktuálního uživatele nemá zadaný program, systém zde také vybere první dostupný program pro kořenovou organizační jednotku.

### Propojení s ovládacím panelem TEI { #linking-to-tei-dashboard }

Ovládací panel TEI můžete sdílet prostřednictvím jeho webové adresy.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete ovládací panel, který chcete sdílet.

3.  Zkopírujte adresu URL.

    Ujistěte se, že adresa URL obsahuje parametry „tei“, „program“ a „ou“ (organizační jednotka).

4.  Vložte adresu URL do metody sdílení podle vašeho výběru, například e-mail nebo zprávu v rámci DHIS2.

    Pokud nejste přihlášeni k DHIS2, když kliknete na odkaz, budete požádáni, abyste tak učinili, a poté přejdete na ovládací panel.

## Vytvořte TEI a zapište jej do programu { #create_and_enroll_tracked_entity_instance }

Můžete vytvořit TEI a zapsat jej do programu v jedné operaci:

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Ve stromu organizační jednotky v levém podokně vyberte organizační jednotku.

3.  Vyberte program.

4.  Klikněte na **Registrovat**.

5.  Vyplňte požadované informace.

    Sledovaný typ entity i program lze nakonfigurovat tak, aby používaly typ funkce. To umožňuje zachytit geometrii pro TEI nebo pro zápis. Podporovaný typ funkce je Bod a Polygon. Viz **Jak používat geometrii**.

6.  Pokud je vybraný program nakonfigurován tak, aby během registrace zobrazoval první fázi, budou muset být vyplněna všechna povinná pole ve fázi. Na konci fáze budete také požádáni, zda chcete dokončit fázi, pro kterou jste zadali data . Pokud vyberete možnost **Ano**, bude fáze po uložení mít dokončený stav. Pokud zvolíte **Ne**, bude fáze aktivní.

7.  Pokud je nakonfigurováno vyhledávání programu, bude provedeno vyhledávání na pozadí v prohledávatelných polích, aby se zabránilo registraci duplikátů. Pokud existují odpovídající TEI, zobrazí se na pravé straně formuláře modré pole s možností zobrazit tyto odpovídající TEI.

![](resources/images/tracker_capture/tracker_capture_register_integrated_search.png)

Pokud existují odpovídající TEI, klikněte na **Pokračovat** a před registrací nového zkontrolujte možné duplikáty.

Pokud neexistuje žádný odpovídající TEI, klikněte na **Uložit a pokračovat** nebo **Uložit a přidat nové**

-   **Uložit a pokračovat**: dokončí registraci a otevře ovládací panel registrovaného TEI

-   **Uložit a přidat nový**: dokončí registraci, ale zůstane na stejné stránce. Tuto možnost použijte, pokud se chcete zaregistrovat a zapisovat jeden TEI za druhým bez zadávání údajů.

> Poznámka: Aby bylo možné uložit, musí být vyplněny všechny povinné atributy. Povinné atributy jsou označeny červenou hvězdičkou vedle štítku atributu. Pokud má uživatel oprávnění s názvem **„Ignorovat ověření povinných polí v nástroji Tracker and Event Capture“**, nebude od vás požadováno vyplnění povinných atributů a neuvidí se červená hvězdička vedle štítku atributu. Všimněte si, že super uživatel, který má oprávnění **"VŠE“**, má toto oprávnění automaticky.

## Otevřete existující ovládací panel TEI { #open_existing_tracked_entity_instance_dashboard }

Existuje několik způsobů, jak najít TEI: Použití "Seznamů", které jsou předdefinované seznamy v aktuálním výběru, nebo "Hledat" pro globální vyhledávání.

### Seznamy { #simple_tracked_entity_instance_search }

Seznamy slouží k vyhledání a zobrazení TEI ve vybrané organizační jednotce a programu.

1.  Otevřete aplikaci Tracked Capture

2.  Ve stromu organizační jednotky v levém podokně vyberte organizační jednotku

3.  Vyberte program

4.  Pokud již není vybráno, klikněte na tlačítko „Seznamy“

Pokud není nakonfigurováno, bude k dispozici sada předdefinovaných seznamů:

1.  Libovolný TEI s jakýmkoli stavem registrace

2.  TEI s aktivním zápisem do aktuálního programu

3.  TEI s dokončeným zápisem do aktuálního programu

4.  TEI se zrušeným zápisem do aktuálního programu

![](resources/images/tracker_capture/tracker_capture_lists.png)

Můžete si vybrat, které sloupce se mají zobrazit nebo skrýt v seznamech jednotlivých programů. To bude uloženo ve vašem uživatelském nastavení.

1.  Klikněte na tlačítko s ikonou **mřížky**

2.  Zaškrtněte sloupce, které chcete zahrnout

3.  Klikněte na **Uložit**

K dispozici je také možnost vytvořit vlastní pracovní seznam s vlastními filtry. To lze použít k vytváření vlastních seznamů za běhu.

![](resources/images/tracker_capture/tracker_capture_lists_custom.png)

Seznamy lze také stáhnout nebo vytisknout.

![](resources/images/tracker_capture/tracker_capture_lists_download.png)

#### Vlastní předdefinované seznamy { #custom-predefined-lists }

Pokud má program přidružené nějaké vlastní filtry trasovaných entit, nahradí tyto čtyři předdefinované seznamy uvedené výše. Předem definované seznamy budou, pokud budou dobře nakonfigurovány, účinným způsobem, jak najít nebo pracovat s daty relevantními pro uživatele v daném programu.

Pracovní seznamy lze definovat pomocí široké škály možností, zde je několik příkladů:

-   Zobrazit všechny TEI s alespoň jednou událostí v dané programové fázi
-   má datum splatnosti k aktuálnímu datu.
-   Zobrazit všechny TEI, které mají alespoň jednu událost přiřazenou k
-   přihlášený uživatel.
-   Zobrazit všechny TEI, které jsou aktivní, ale nejsou přiřazeny žádnému uživateli.

![Předdefinované pracovní seznamy v tracker capture](resources/images/tracker_capture/predefined_working_list_based_on_user_assignment.png)

Úplný seznam funkcí podporovaných pro tyto předdefinované filtry instancí trasovaných entit najdete v dokumentaci API.

### Hledání { #advanced_tracked_entity_instance_search }

Hledání se používá k hledání TEI v organizačních jednotkách, ke kterým má uživatel přístup k vyhledávání. To lze použít, pokud chcete najít TEI, ale nevíte, do které organizační jednotky nebo programu byl TEI zapsán. Existují dva způsoby, jak to udělat: S kontextem programu i bez něj. Je třeba nakonfigurovat vyhledávací pole. Pro konfiguraci vyhledávání v kontextu programu se to provádí samostatně pro každý program v aplikaci pro údržbu programu. Pro konfiguraci vyhledávání bez kontextu programu se to provádí jednotlivě pro každý typ trasované entity v aplikaci pro údržbu typu trasované entity.

**Hledání bez kontextu programu:**

1.  Otevřete aplikaci **Tracker Capture**

2.  Klikněte na tlačítko **Hledat**

3.  Prohledávatelná pole se zobrazí ve skupinách. Jedinečné atributy lze prohledávat pouze jednotlivě. Neunikátní atributy lze kombinovat.

4.  Vyplňte kritéria hledání a klikněte na tlačítko s ikonou **hledání**.

**Hledání v kontextu programu:**

1.  Otevřete aplikaci **Tracker Capture**

2.  Vyberte organizační jednotku s programem, ve kterém chcete hledat

3.  Vyberte program

4.  Klikněte na tlačítko **Hledat**

5.  Prohledávatelná pole se zobrazí ve skupinách. Jedinečné atributy lze prohledávat pouze jednotlivě. Neunikátní atributy lze kombinovat.

6.  Vyplňte kritéria hledání a klikněte na tlačítko s ikonou **hledání**

![](resources/images/tracker_capture/tracker_capture_search_screen.png)

Po dokončení vyhledávání se zobrazí výsledek hledání. To, co se zobrazí, závisí na výsledku vyhledávání.

Pro vyhledávání jedinečných atributů:

-   Pokud nebyl nalezen žádný odpovídající TEI, budete mít možnost otevřít registrační formulář.

-   Pokud byl TEI nalezen ve vybrané organizační jednotce, automaticky se otevře ovládací panel TEI.

-   Pokud byl TEI nalezen mimo vybranou organizační jednotku, získáte možnost otevřít TEI.

Pro hledání nejedinečných atributů:

-   Pokud nebudou nalezeny žádné odpovídající TEI, budete mít možnost otevřít registrační formulář.

-   Pokud je nalezena shoda TEI, můžete buď kliknout na kteroukoli TEI v seznamu výsledků, nebo otevřít registrační formulář.

-   Pokud byl nalezen příliš velký počet shod, budete vyzváni k upřesnění kritérií hledání

![](resources/images/tracker_capture/tracker_capture_search_results.png)

Výsledky hledání mají funkci pro označování instancí sledovaných entit jako možných duplikátů, viz další kapitola.

Když se rozhodnete otevřít registrační formulář, vyhledávací hodnoty se automaticky vyplní do registračního formuláře.

### Označení trasované instance entity jako potenciálního duplikátu { #flagging-tracked-entity-instance-as-potential-duplicate }

Při hledání instancí trasované entity v aplikaci pro zachycení trasování, bude mít uživatel někdy podezření, že jeden nebo více vyhledávacích zásahů jsou duplikáty jiných instancí trasované entity. Uživatel má možnost kliknout na odkaz **označit možný duplikát** v pravém sloupci mřížky s výsledky vyhledávání.

Takto označené trasované instance entity budou v databázi DHIS2 označeny jako „možný duplikát“. Příznak označuje, že trasované instance entity je / má duplikát. Přítomnost takového příznaku je uživateli viditelná na dvou místech. Jedním z nich je samotný seznam výsledků (v tomto příkladu je Mark Robinson již označen jako potenciální duplikát):

![Výsledky vyhledávání Tracker capture](resources/images/tracker_capture/tracker_capture_search_results.png)

Druhé místo je v ovládacím panelu instance trasované entity:

![Instance trasované entity označena jako duplicitní](resources/images/tracker_capture/tracked_entity_instance_flagged_as_duplicate.png)

Kromě informování uživatelů o tom, že instance trasované entity může být duplikát, bude příznak použit základním systémem pro hledání a slučování duplikátů v nadcházejících verzích DHIS2.

### Rozbití skla { #break_glass }

Pokud je program nakonfigurován s úrovní přístupu **chráněno** a uživatel vyhledává a nalézá instance trasovaných entit, které jsou vlastněny organizační jednotkou, pro kterou uživatel nemá oprávnění pro sběr dat, je uživateli nabídnuta možnost rozbití skla. Uživatel podá důvod rozbití skla a poté získá dočasné vlastnictví instance trasované entity.

## Zapište existující TEI do programu { #enroll_existing_tracked_entity_instance_in_program }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Vyberte program.

4.  Ve widgetu **Zápis** klikněte na **Přidat nový**.

5.  Vyplňte požadované informace a klikněte na **Zaregistrovat**.

## Zadejte data události pro TEI { #enter_event_data_for_tracked_entity_instance }

### Widgety pro zadávání dat { #widgets-for-data-entry }

####

Na ovládacím panelu TEI zadáváte data událostí do widgetů **Zadání údajů na časové ose** nebo **Zadání údajů v tabulce**.

<table>
<caption> Widgety pro zadávání dat v aplikaci Tracker Capture </caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Název widgetu </p> </th>
<th> <p> Popis </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> <strong> časová osa Zadávání dat </strong> </p> </td>
<td> <p> Pro zadávání dat pomocí výchozích nebo vlastních formulářů. </p>
<p> V závislosti na definici programu, zejména v jednotlivých fázích programu, budou události zobrazeny včas. Kliknutím na kteroukoli z nich se zobrazí odpovídající položka dat. Pokud scéna potřebuje novou událost, zobrazí se ikona plus pro vytvoření nové události. Pro pokračování v zadávání dat je povinné mít datum události. Jakmile je uvedeno datum události, není možné změnit datum platnosti. Předpokládá se, že zadáním data události událost již proběhla. Pokud událost ještě nenastala, je možné změnit datum platnosti - to ve skutečnosti nedělá nic jiného než přeplánování. Tlačítka v dolní části pomáhají změnit stav vybrané události. </p>
<p> Další klíčovou funkcí tohoto widgetu je přidání několika poznámek k události. Záznam dat se obvykle provádí prostřednictvím datových prvků, existují však případy, kdy je nutné zaznamenat další informace nebo komentáře. Zde se hodí část s poznámkami. Nelze však odstranit poznámku. Myšlenka je, že poznámky jsou spíše jako deníky. Během zadávání dat jsou podporovány chybové i varovné zprávy přeskočení logiky i ověření. </p>
<p> Součástí položky Data na časové ose je také možnost porovnat vaše data s předchozími položkami. To lze povolit kliknutím na tlačítko &quot;Switch a porovnat tlačítko form&quot; (dva listy papíru) v pravém horním rohu widgetu Zadávání dat časové osy. </p> </td>
</tr>
<tr class="even">
<td> <p> <strong> zadávání údajů do tabulky </strong> </p> </td>
<td> <p> Pro zadávání dat v tabulkovém stylu. </p>
<p> Widget zobrazuje seznam fází programu jako štítky na levé straně. Události budou uvedeny v tabulce pro opakovatelnou fázi programu a umožňují přímé úpravy hodnot dat událostí. </p> </td>
</tr>
</tbody>
</table>

### Vytváření události { #creating-an-event }

Událost pro TEI můžete vytvořit:

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  V widgetu **Zadání údajů na časové ose** nebo **Zadání údajů v tabulce** klikněte na tlačítko **+**.

4.  Vyberte **Programstage** a nastavte **Datum hlášení**.

    Fáze programu lze nakonfigurovat tak, aby používaly typ funkce. To umožňuje zachytit geometrii události. Podporovaný typ funkce je Bod a Polygon. Viz **Jak používat geometrii**.

5.  Klikněte **Uložit**.

### Naplánujte událost { #schedule-an-event }

Událost můžete naplánovat na budoucí datum:

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  V widgetu **Zadání údajů na časové ose** nebo **Zadání údajů v tabulce** klikněte na ikonu **Kalendář**.

4.  Vyberte **Programová fáze** a nastavte **Naplánovat datum**.

5.  Klikněte **Uložit**.

### Odkázat na událost { #refer-an-event }

Někdy může být nutné odkázat pacienta na jinou **organizační jednotku**. a doporučit TEI:

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zadání dat na časové ose** nebo **Zadání dat do tabulky** klikněte na ikonu **Šipka**.

4.  Vyberte **Programová fáze**, **Organizační jednotka** a nastavte \***\*Datum zprávy\*\***.

5.  Klikněte buď na **Jednorázové odkazování**, které bude odkazovat TEI pouze na jednu jedinou událost, nebo na **Přesunout trvale**, což přesune vlastnictví TEI do vybrané **Organizační jednotky**. Další přístup k TEI bude založen na organizační jednotce vlastnictví.

### Povinné datové prvky v událostech { #mandatory-data-elements-in-events }

Některé datové prvky v události mohou být povinné (označené červenou hvězdičkou vedle štítku datového prvku). To znamená, že všechny povinné datové prvky musí být vyplněny, než bude uživateli povoleno dokončit událost. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření požadovaných polí v nástroji Tracker a Zachycení Události“.** Pokud má uživatel toto oprávnění, nebude nutné před uložením vyplňovat povinné datové prvky. a červená hvězdička se nezobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

## Jak používat geometrii { #how-to-use-geometry }

Typ trasované entity, program a fázi programu lze nakonfigurovat tak, aby používal typ prvku. To umožňuje zachytit geometrii pro TEI, program nebo událost. Podporované typy funkcí jsou Bod a Polygon.

### Zachyťte souřadnici { #capture-coordinate }

**Možnost 1:** Vyplňte do pole zeměpisnou šířku a délku.

**Možnost 2:**

1.  Klikněte na **ikonu mapy**
2.  Vyhledejte požadované místo buď prohledáním, nebo vyhledáním na mapě
3.  Klikněte pravým tlačítkem na požadované místo a vyberte **Nastavit souřadnici**
4.  Dole klikněte na **Zachytit**

### Polygon zachycení { #capture-polygon }

1.  Klikněte na **ikonu mapy**
2.  Vyhledejte požadované místo buď prohledáním, nebo vyhledáním na mapě
3.  Vlevo nahoře na mapě klikněte na **ikonu polygonu**
4.  Nakreslete na mapu polygon. Dokončete propojení posledního bodu s prvním bodem
5.  Dole klikněte na **Zachytit**

![](resources/images/tracker_capture/capture_geometry.png)

Polygony lze také smazat

1.  Klikněte na **ikonu mapy**
2.  Klikněte na **ikonu koše** na levé straně mapy a vyberte **Vymazat vše**

## Jak přiřadit uživatele k události { #how-to-assign-a-user-to-an-event }

V aplikaci Údržba lze nakonfigurovat programovou fázi, která umožňuje přiřazení uživatelů. Pokud je povoleno přiřazení uživatele, budete moci přiřadit uživatele k události.

1. Klikněte na pole **Přiřazený uživatel**.
2. Procházejte nebo vyhledejte uživatele.
3. Klikněte na uživatele.

## Spravujte zápisy TEI { #manage_tracked_entity_instance_enrollment }

Widget Zápis umožňuje přístup k informacím a funkcím pro zápis do vybraného programu.

![Widget pro zápisy](resources/images/tracker_capture/enrollment_widget.png)

### Vlastnictví TEI { #tei-ownership }

Aktuální vlastnictví všech registrací ve vybraném programu se zobrazuje v části „Vlastněno uživatelem“ widgetu registrace. Vlastnictví vždy začíná jako organizační jednotka, která TEI poprvé zapsala do daného programu.

Vlastnictví se může lišit u různých programů TEIS, například jedna klinika může sledovat pacienta s HIV, zatímco jiná klinika sleduje stejného pacienta v MCH.

Chcete-li aktualizovat vlastnictví kombinace TEI / programu, musí uživatel využít funkce doporučení a při odkazování vybrat možnost „Přesunout trvale“.

Uživatel, který má přístup k zachycení do organizační jednotky, která je aktuálním vlastníkem TEI / Programu, bude mít přístup pro zápis do všech zápisů pro danou kombinaci TEI / Programu. Uživatel, který má přístup k vyhledávání v organizační jednotce, která je aktuálním vlastníkem, bude mít přístup k vyhledávání a hledání kombinace TEI / Programu.

### Deaktivujte zápis TEI { #deactivate_tracked_entity_instance_enrollment }

Pokud deaktivujete ovládací panel TEI, stane se TEI „pouze pro čtení“. Nemůžete zadávat data, zapsat TEI nebo upravovat profil TEI.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zápis** klikněte na **Deaktivovat**.

4.  Potvrďte kliknutím na **Ano**.

### Aktivujte zápis TEI { #activate_tracked_entity_instance_enrollment }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zápis** klikněte na **Aktivovat**.

4.  Potvrďte kliknutím na **Ano**.

### Označte zápis TEI jako dokončený { #mark_tracked_entity_instance_enrollment_complete }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zápis** klikněte na **Dokončit**.

4.  Potvrďte kliknutím na **Ano**.

### Znovu otevřete dokončený zápis { #reopen_complete_tracked_entity_instance_enrollment }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zápis** klikněte na **Znovu otevřít**.

4.  Potvrďte kliknutím na **Ano**.

### Zobrazte historii zápisu TEI { #display_tracked_entity_instance_enrollment_history }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Profil** klikněte na ikonu **Historie auditu**.

### Vytvořte poznámku k zápisu TEI { #create_tracked_entity_instance_enrollment_note }

Poznámka k zápisu je užitečná k zaznamenání informací například o tom, proč byl zápis zrušen.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Poznámky** zadejte poznámku a klikněte na **Přidat**.

## Odeslat zprávu TEI { #send_message_to_tracked_entity_instance }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zprávy** a vyberte **SMS** nebo **E-mail**.

4.  Zadejte požadované kontaktní informace.

    Pokud profil TEI obsahuje e-mailovou adresu nebo telefonní číslo, vyplní se tato pole automaticky.

5.  Napište zprávu.

6.  Klikněte na **Odeslat**

## Označte TEI pro další sledování { #mark_tracked_entity_instance_for_follow_up }

Můžete použít označení zápisu TEI pro následné kroky a poté použít tento stav jako filtr při vytváření přehledů **Nadcházející události** a **Události po datu platnosti**. To může být užitečné například pro sledování vysoce rizikových případů během těhotenského programu.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Zápis** klikněte na ikonu **Označit pro následné kroky**.

## Upravte profil TEI { #edit_tracked_entity_instance_profile }

Upravte profil TEI nebo atributy trasované entity ve widgetu **Profil**.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Profil** klikněte na **Upravit**.

4.  Upravte profil a klikněte na **Uložit**.

## Přidejte vztah k TEI { #add_relationship_to_tracked_entity_instance }

Můžete vytvořit vztah od jedné TEI k druhé, například propojením matky a dítěte dohromady, nebo manžela a manželky. V závislosti na tom, jak je nakonfigurován typ vztahu, může vztah dědit atributy.

Předpokládejme, že existují dva programy: Předporodní péče o matku a Imunizace dítěte. Pokud jsou pro oba programy vyžadovány atributy křestního jména, příjmení a adresy, je možné nakonfigurovat atributy příjmení a adresy jako dědičné. Pak během registrace dítěte není nutné tyto dědičné atributy zadávat. Můžete je přidat automaticky na základě hodnoty matky. Pokud chcete mít pro dítě jinou hodnotu, můžete automaticky vygenerovanou hodnotu přepsat.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Ve widgetu **Vztahy** klikněte na **Přidat**.

4.  Vyberte typ vztahu.

5.  Vyhledejte příbuzného a vyberte jej. Hledání se řídí stejným vzorem jako při hledání instancí trasovaných entit z titulní stránky trasovače. Vyhledávání standardně pokrývají rozsah hledání uživatelů.

6.  Vyberte ve vyskakovacím okně trasovanou instanci entity, která odpovídá kritériím vyhledávání.

7.  Klikněte **Uložit**.

> Poznámka: Pokud je vztah obousměrný, vztah se zobrazí v TEI, ve kterém byl vztah vytvořen, a v TEI, ke kterému byl vztah propojen. Pokud je vztah obousměrný, bude mít každý konec vztahu jedinečný název, který se zobrazí v widgetu vztahu ve sloupci „Vztah“.

## Sdílejte ovládací panel TEI { #share_tracked_entity_instance_dashboard }

Ovládací panel TEI můžete sdílet prostřednictvím jeho webové adresy.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete ovládací panel, který chcete sdílet.

3.  Zkopírujte adresu URL.

    Ujistěte se, že adresa URL obsahuje parametry „tei“, „program“ a „ou“ (organizační jednotka).

4.  Vložte adresu URL do metody sdílení podle vašeho výběru, například e-mail nebo zprávu v rámci DHIS2.

    Pokud nejste přihlášeni k DHIS2, když kliknete na odkaz, budete požádáni, abyste tak učinili, a poté přejdete na ovládací panel.

## Deaktivace TEI { #deactivate_tracked_entity_instance }

Pokud deaktivujete TEI, stane se TEI „pouze pro čtení“. Data spojená s TEI nejsou smazána.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  V pravém horním rohu klikněte na tlačítko ![](resources/images/tracker_capture/tc_tei_red_icon.png) \> **Deaktivovat**.

4.  Potvrďte kliknutím na **Ano**.

## Aktivujte TEI { #activate_tracked_entity_instance }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  V horním horním rohu klikněte na tlačítko ![](resources/images/tracker_capture/tc_tei_red_icon.png) \> **Aktivovat**.

4.  Potvrďte kliknutím na **Ano**.

## Smazání TEI { #delete_tracked_entity_instance }

> **Varování**
>
> Když odstraníte TEI, vymažete všechna data spojená s TEI.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  V pravém horním rohu klikněte na tlačítko ![](resources/images/tracker_capture/tc_tei_red_icon.png) \> **Smazat**.

4.  Potvrďte kliknutím na **Ano**.

## Nakonfigurujte ovládací panel TEI { #configure_tracked_entity_instance_dashboard }

### Zobrazení nebo skrytí widgetů { #tracked_entity_instance_dashboard_show_hide_widget }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Klikněte na ikonu **Nastavení** a vyberte **Zobrazit / skrýt widgety**.

4.  Vyberte widgety, které chcete zobrazit nebo skrýt.

5.  Klikněte na **Zavřít**.

### Uložte rozložení ovládacího panelu jako výchozí { #tracked_entity_instance_dashboard_save_layout }

Rozložení ovládacího panelu můžete uložit jako výchozí nastavení pro program.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Klikněte na ikonu **Nastavení** a vyberte **Uložit rozvržení ovládacího panelu jako výchozí**.

### Uzamkněte rozložení ovládacího panelu { #lock-dashboards-layout }

Pokud jste **správce**, máte možnost uzamknout rozložení ovládacího panelu pro všechny uživatele.

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Uspořádejte widgety do požadovaného rozvržení a uložte je jako výchozí (viz část výše).

4.  Klikněte na ikonu **Nastavení** a vyberte **Zamknout rozložení pro všechny uživatele**.

Uživatelé budou i nadále moci dočasně reorganizovat widgety, ale po obnovení stránky se rozložení resetuje na rozložení uložené správcem. Když je rozložení ovládacího panelu uzamčeno, tlačítka pro odebrání widgetu budou skryta.

### Horní lišta { #top-bar }

Horní lišta může být užitečným nástrojem pro rychlé a snadné zobrazení důležitých dat. Chcete-li začít používat horní lištu:

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Otevřete existující ovládací panel TEI.

3.  Klikněte na ikonu **Nastavení** a vyberte **Nastavení horní lišty**.

4.  Klikněte na **Aktivovat horní lištu** a klikněte na data, která chcete zobrazit v horní liště.

![](resources/images/tracker_capture/top_bar.png)

### Změňte režim zobrazení tabulky pro widget **Zadání dat na časovou osu** { #change-table-display-mode-for-timeline-data-entry-widget }

Widget **Timeline Data Entry** má 5 různých režimů zobrazení tabulky, které lze vybrat. Různé možnosti jsou:

-   **Výchozí formulář** - Zobrazí všechny datové prvky svisle.

-   **Porovnat předchozí formulář** - Ukáže předchozí (opakovatelnou) programovou fázi vedle aktuální vybrané programové fáze.

-   **Porovnat všechny formuláře** - Zobrazí všechny předchozí (opakovatelné) fáze programu vedle aktuálně vybrané fáze programu.

-   **Grid form** - Zobrazí datové prvky horizontálně.

-   **POP-over form** - Stejné jako **Grid form**, ale po kliknutí se datové prvky zobrazí ve vyskakovacím okně.

Chcete-li změnit aktuální režim zobrazení, klikněte na druhou ikonu v horní liště widgetů (viz obrázek níže):

![](resources/images/tracker_capture/compareForm.png)

Jakmile je vybrána možnost, výběr je uložen pro tuto zvláštní programovou fázi. To znamená, že můžete mít různé režimy tabulky pro různé fáze programu v programu.

> **Poznámky:**
>
> 1. _Možnosti **Formulář pro porovnání** budou fungovat nejlépe, pokud máte k dispozici více opakovatelných událostí (stejné fáze programu)._
> 2. _Možnosti **Grid form** a **POP-over form** nelze vybrat, pokud programová fáze obsahuje více než 10 datových prvků._
> 3. _Ikona na liště widgetů se bude měnit v závislosti na vybrané možnosti._

## Vytvářejte zprávy { #create_report_tracker_capture }

1.  Otevřete aplikaci Tracker Capture = **Trasovač sběru dat**.

2.  Klikněte na **Zprávy**.

3.  Vyberte typ zprávy.

    <table>
    <caption>Report types in the Tracker Capture app</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Report type</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Program summary</p></td>
    <td><p>A summary report for a particular program, organisation unit and time frame. The report consist of a list of TEIs and their records organised based on program stages.</p></td>
    </tr>
    <tr class="even">
    <td><p>Program statistics</p></td>
    <td><p>A statistics report for a particular program. The report provides for example an overview of drop-outs or completion rates in a given time frame at a particular organisation unit.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Upcoming events</p></td>
    <td><p>A tabular report showing tracked entity instances and their upcoming events for a selected program and time. You can sort the columns and search the values. Show/hide operations are possible on the columns. You can also export the table to Microsoft Excel.</p></td>
    </tr>
    <tr class="even">
    <td><p>Overdue events</p></td>
    <td><p>A list of events for a selected program. The report displays a list of TEIs and their events that are not completed on time. You can sort the columns and search the values You can also export the table to Microsoft Excel.</p></td>
    </tr>
    </tbody>
    </table>

![](resources/images/tracker_capture/program_summary_report.png)

Souhrnná zpráva zobrazuje seznam TEI a jejich záznamů pro program „MNCH / PNC (dospělé ženy)“. Záznamy jsou uspořádány ve formě karet, kde každá karta je programová fáze. Sloupce v tabulce jsou datové prvky, které jsou nakonfigurovány tak, aby se zobrazovaly v sestavách pod definicí fáze programu.
