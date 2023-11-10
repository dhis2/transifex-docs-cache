---
edit_url: "https://github.com/dhis2-metadata/AEFI-TRK-Adverse_Events_Following_Immunization/blob/master/training/aefi_trainers_guide.md"
revision_date: "2021-09-23"
---

# AEFI - Příručka trenéra zadávání údajů { #aefi-data-entry-trainers-guide }

**DHIS2 Immunization Toolkit**

**Nežádoucí účinky po imunizaci (AEFI)**

## Poznámky k přípravě { #preparation-notes }

Chcete -li tuto příručku upravit, budete muset zkontrolovat zavedené místní SOP a upravit jakýkoli pracovní postup nebo funkce popsané v pořadí, v jakém s nimi bude uživatel interagovat.

1. Vytvořte si účet se stejnou úrovní přístupu jako uživatelé, kterým předvádíte (tj. Pokud mohou pouze vyhledávat a zadávat v rámci jednoho zařízení, ať má váš uživatel stejné oprávnění)

    Další podrobnosti o uživatelích a skupinách uživatelů naleznete v [dokumentu návrhu systému](#aefi-tracker-system-design) a instalační příručce. Vytvořte 3 uživatele pro demo následovně:

    - Osoba zadávající počáteční údaje AEFI do DHIS2 (buď zaměstnanci zařízení, nebo zaměstnanci okresu zadávající údaje pro všechna zařízení ve svém okrese v závislosti na místním pracovním toku). V tomto dokumentu je budeme označovat jako „uživatele zařízení“
    - Uživatel na první úrovni rozhodování (okres / kraj). (poznámka: tento uživatel může být stejný jako osoba zadávající počáteční data AEFI do DHIS2)
    - Uživatel na národní úrovni

    Zajistěte přiřazení těchto uživatelů k příslušným skupinám uživatelů. To jim umožní přístup k zadávání dat podle potřeby a oznámení.

    > **Note**
    >
    > Demonstrating multiple users
    >
    > When working with multiple users it can be difficult for those watching the demo to follow along if each user is not clearly identified. Additionally, switching between users without clearing cache can result in a previous user’s settings being displayed within the window of the new user that you log in with (ex. org units, dashboards, program stages, etc.). Please consider the following when working with multiple users:
    >
    > - Open separate browsers (for example, regular chrome, chrome in incognito and one firefox window -- add more modes/windows (firefox in private mode, edge, edge in private mode, etc.) depending on the amount of users you are showing).
    > - Log in to each user you will be testing before starting your demo. Since each browser is its own window, create a duplicate tab within each browser.
    > - Your session may time out causing you to log out from DHIS2 within one of the windows for a user you had previously logged in with, reload your duplicate tab to check this and log in to carry forward from wherever your user was logged in previously if needed.
    > - Consider using a note of some kind that overlays itself on top of the windows you are using to perform the demo. Enter the name/type of user you are showing as you move between the different users so each user is visible to those reviewing the demo. An example app is simple sticky notes (<https://www.simplestickynotes.com/>). When working with these apps have them set to appear “Always on top.” Here is an example of such an overlay:

    ![Uživatel zařízení](resources/images/aefi_trainers_guide_01_en.png)

2. Pokud se jedná o postup pro zadávání těchto údajů z listinné podoby, bude užitečné mít vyplněnou kopii formuláře, který by normálně používali jako referenci. Může to být jen formulář, který jste například sami vyplnili nebo můžete být kopií formuláře ze skutečné implementace, který jste obdrželi od ministerstva zdravotnictví. Při hledání nebo vyplňování vzorových formulářů z implementace vaší země bude užitečné odkázat na příběh AEFI a formuláře hlášení zahrnuté v balíčku školení.
3. Pokud zadávají data v reálném čase, není nutné mít formuláře, ale měli byste připravit podrobnosti o příkladu, který můžete sledovat ve svých příkladech. Odkazování na příběh AEFI bude užitečné při vývoji případových studií pro zadávání dat v reálném čase.
4. Pro cvičení a drobné aktivity během ukázky zajistěte, aby byly k dispozici kopie formulářů nebo případových studií, které mohou účastníci použít k registraci vlastních případů.
5. Vaše tréninková databáze by měla mít vyplněny některé existující případy, které pomohou podpořit předvádění funkcí vyhledávání, filtrování a ovládacího panelu
6. Pokud demonstrujete funkčnost pracovních seznamů, budete potřebovat podmnožinu událostí, které jste vytvořili a přiřadili uživateli, kde můžete tuto funkci ukázat
7. S tímto programem jsou spojena upozornění. K demonstraci toho můžete použít zasílání zpráv DHIS2; pokud to však chcete demonstrovat prostřednictvím e-mailu nebo SMS, ujistěte se, že jste to nakonfigurovali a otestovali v instanci, kterou bude používat školitel i účastník.

## Pozadí { #background }

1. Tento program je zaměřen na zachycení dat pro jakoukoli nežádoucí příhodu po imunizaci
2. Očekává se, že školitel poskytne konkrétní základní informace o AEFI publiku na základě pozadí jednotlivců, které instruuje. WHO nabízí materiály o AEFI zde: <http://gvsi-aefi-tools.org/aefidata/training/resources_didactic_sessions.html> . Vysvětlení tohoto pracovního postupu by mělo proběhnout před praktickými sezeními o zadávání dat do DHIS2, pokud je to nutné.

## Průvodce krok za krokem { #step-by-step-guide }

1. Přihlaste se do systému DHIS2 pomocí Uživatelského jména a hesla
2. Přejděte na zachycení trasovače
3. Zkontrolujte výběr organizační jednotky a programu a vyberte zařízení, ve kterém budete pracovat
4. Stručně popište první seznam stránek, pokud se objeví, ale pamatujte, že se k tomu vrátíme později.

### Registrace { #registration }

1. Kdykoli budeme mít novou nežádoucí příhodu, budeme muset případ zaregistrovat. Vyberte Registrovat pro registraci nové nežádoucí příhody
2. Zkontrolujte stránku zápisu, kterou jste nakonfigurovali. Popište atributy, které používáte, a proč tam jsou. Všimněte si, že tyto atributy vám umožňují sledovat tuto osobu, když prochází programem, včetně jejího pozdějšího nalezení, což bude také ukázáno. Atributy obsažené ve standardním konfiguračním balíčku AEFI jsou popsány v dokumentu návrhu systému.
    1. Popište datum zápisu, které se nazývá ‚Datum, kdy pacient oznámil událost zdravotnímu systému‘ ve standardní konfiguraci (poznámka pro školitele: toto může být pojmenováno jinak na základě vaší vlastní konfigurace; zde použijte datum zápisu založené na vaší konfiguraci) . Toto je datum hlášení v DHIS2. Datum zahájení AEFI je reprezentováno „Datem AEFI Started“ a bude uvedeno později ve formuláři pro zadávání dat.
    2. Popište proces generování AEFI Case ID a Unique System Identifier. ID případu AEFI je místně přiřazeno, zatímco jedinečný systémový identifikátor je generován systémem. Další podrobnosti naleznete v dokumentu návrhu systému.
    3. V závislosti na vašem standardním postupu můžete vytvářet nové entity pro vracený případ nebo pouze nový zápis. Můžete se k tomu vrátit později, až budou s programem spokojeni.
3. Zadejte data pro atributy. Pokud používáte papírový formulář, použijte jej jako referenci k popisu toho, jak se každý detail z formuláře vyplní do DHIS2. Po zadání a vysvětlení podrobností pro registraci vyberte Uložit a pokračovat.

STOP

#### Cvičení 1 – Zaregistrujte nový případ { #exercise-1-register-a-new-case }

### Ovládací panel trackeru { #tracker-dashboard }

1. Po uložení podrobností budete konfrontováni s ovládacím panelem trackeru. To je často ohromující, ale doufejme, že je k dispozici výchozí rozložení, takže všichni vidí to samé.
2. Doporučuje se nejprve přeskočit všechny ostatní widgety a zaměřit se na widget pro zadávání dat. Po zadání některých údajů se můžete vrátit k ostatním widgetům.
    1. Rychle zrekapitulujte fáze, které jsou v programu (jmenovitě fáze „AEFI“, „První rozhodovací úroveň“ a „Národní úroveň“), s odkazem na jakoukoli prezentaci(e) nebo demo ukázky, které jste již provedli.
    2. Vysvětlete, jak mají různí uživatelé přístup k různým fázím a nastavení sdílení s nimi spojené.
        1. Uživatel zařízení – fáze zadávání dat AEFI
        2. Uživatel okresu – stupeň prvního rozhodování
        3. Uživatel na národní úrovni – Stupeň na národní úrovni

Budete to muset podrobně popsat, až budete probírat proces zadávání dat.

### Vstup dat { #data-entry }

#### Fáze 1 – Podrobnosti o vakcíně a AEFI { #stage-1-vaccine-and-aefi-details }

1. Fáze AEFI se generuje automaticky a datum sestavení zprávy (datum události) se také automaticky vyplní na základě data registrace. Můžete vysvětlit předpoklad, že se jedná o výchozí datum sestavení sestavy, ale lze ji upravit podle skutečného data sestavování sestavy.
2. Existuje řada programových pravidel, která se používají ke skrytí/zobrazení polí na stránce pro zadávání dat. Popište tato pravidla účastníkovi. Logiku ve formuláři pro zadávání dat naleznete v souboru kontroly metadat.
3. Před zadáním dat z vašeho příkladu (buď papírového formuláře nebo živého případu) si projděte všechny spouštěče pro pravidla vašeho programu, aby účastník pochopil, kde na papírovém formuláři vidí skrytá pole (nebo položky, které musí shromáždit v reálném čase) a kde jsou umístěny. Například ve fázi AEFI jsou pravidla spuštěna pro:
    1. Je pacientka těhotná?
    2. Je pacientka kojící?
    3. \> 3 dny (závažná místní reakce)
    4. Za nejbližší kloub
    5. Záchvaty
    6. Pokud zemřel, datum úmrtí:
    7. Byla požadována pitva?
4. Po vysvětlení umístění skrytých polí a jejich spouštěčů resetujte formulář odstraněním těchto hodnot (nebo odstraňte událost a vytvořte novou). Nyní byste měli vidět formulář pro fázi AEFI v původním rozložení. Protože formulář pro zadávání dat je uživatelský formulář, část textu zůstává viditelná, ale pole pro zadávání dat / zaškrtávací políčka jsou skryta, dokud nejsou vyžadována podle logiky definované pravidlem.
5. Vezměte si svůj příklad, který jste připravili, a zadejte podrobnosti do první fáze (měly by proto být zadány všechny informace až po „první rozhodovací úroveň“).
6. Pokud jste spokojeni se zadanými údaji, můžete událost dokončit.
7. Budou zde tlačítka pro smazání události nebo tisk formuláře. Existuje několik tlačítek pro odstranění události, registrace a entity. Uživatelé mohou mít oprávnění provádět pouze určité akce odstranění. Prohlížejte pouze funkce odstranění, které jsou relevantní pro skupinu, se kterou pracujete.
8. Vysvětlete systém oznamování zavedený pro tento program. Po dokončení zadávání dat ve fázi AEFI budou odeslána dvě oznámení.

    1. Jeden z prvních uživatelů na úrovni rozhodování „Dobrý den, fáze AEFI byla dokončena pro (ID případu) v (zařízení). Proveďte prosím další kroky k ověření formuláře oprávněným personálem.“ Bude to vypadat nějak takto (poznámka pro školitele: zpráva se může lišit v závislosti na tom, jak je nakonfigurována ve vašem systému)

    ![Zpráva ze systému](resources/images/aefi_trainers_guide_02_en.png)

    2. Další bude zaslána všem uživatelům přiřazeným k této organizační jednotce „Událost AEFI hlášena pro (jméno dítěte). Bude to vypadat nějak takto (poznámka pro školitele: zpráva se může lišit v závislosti na tom, jak je nakonfigurována ve vašem systému)

    ![Zpráva ze systému](resources/images/aefi_trainers_guide_03_en.png)

    3. Toto upozornění můžete vysvětlit tím, že dokončíte událost ve fázi a poté zkontrolujete své zprávy nebo e-mail v závislosti na tom, jak jste nakonfigurovali odesílání upozornění. Budete muset být přihlášeni jako uživatel, který obdrží toto upozornění (možná v samostatném okně).
    4. Ujistěte se, že jste přiřazeni ke správné organizační jednotce a skupině uživatelů, abyste mohli přijímat tato oznámení.

STOP

##### Cvičení 2 – Vyplňte podrobnosti AEFI JAKO UŽIVATEL ZAŘÍZENÍ { #exercise-2-fill-in-aefi-details-as-the-facility-user }

#### Vyhledávání { #searching }

1. Přihlaste se jako uživatel první rozhodovací úrovně (okres / kraj). Přejděte zpět k zachycení trackeru a vyberte zařízení, ve kterém se případ, který chcete aktualizovat, nachází
2. Existuje několik filtrů, které jsou dostupné při pohledu na úvodní stránku se seznamem řádků v rámci zachycení trackeru. Dva, které budou obzvláště užitečné, jsou dokončené vs aktivní registrace a také vlastní pracovní seznam. V tomto bodě budete chtít vysvětlit, co je aktivní a dokončená registrace. Aktivní = stále potřebuje data, Dokončeno = všechny podrobnosti o případu včetně jejich výsledku byly zadány.
3. Po koncepčním vysvětlení těchto případů si povšimněte, že nakonec projdeme a dokončíme případy na konci tohoto dema. Ukažte jim, jak filtry fungují, aby zmenšily seznam řádků v jejich zařízení, a také otevřete aktivní vs. dokončený případ, abyste jim ukázali, jak se bude zadávání dat a ovládací panel trasování lišit.
4. K dispozici je také funkce vyhledávání, která nám umožní najít naše případy. Vyberte Hledat a zadejte podrobnosti o existujícím případu. Tím se pouzdro zvedne a můžete je vybrat, aby se přenesly na řídicí panel trackeru. To je užitečné, pokud potřebujete najít konkrétní případ pro jakýkoli účel.
5. Pokud země používá nebo plánuje používat také očkovací program, můžete ukázat vyhledávání v očkovacím programu a poté zapsat případ do programu AEFI.
6. Než budete pokračovat, najděte předchozí případ, který jste právě zadali s uživatelem vašeho zařízení

STOP

##### Cvičení 3 – Prohlédněte si oznámení a funkce vyhledávání a filtrování, abyste našli případ { #exercise-3-review-notifications-and-the-search-and-filter-functionality-to-find-a-case }

#### Fáze 2 – První úroveň rozhodování { #stage-2-first-decision-making-level }

1. Budete muset změnit uživatele na první rozhodovací úroveň (okres / provincie) v závislosti na směrnicích dané země. Bude to uživatel, který se podívá na formulář pro zadávání dat AEFI a rozhodne, zda je nutné vyšetřování nebo ne. Měly by být použity k nalezení případu, jak je popsáno výše.
2. Fáze První úrovně rozhodování se negeneruje automaticky. Proto budete muset vytvořit novou událost a vybrat datum události. Ukažte účastníkům, jak vytvořit novou událost, a vyberte datum. Může se stát, že toto datum bude stejné jako fáze zápisu a AEFI.
3. Projděte si všechna pole, která jsou k dispozici v této části zadávání dat, a vysvětlete je. Ještě jednou si projděte pravidla programu a také jejich spouštěče –
    1. Například platí pravidlo, že pokud je potřeba vyšetřování, teprve potom je vidět plánované datum a je potřeba ho zadat pro vyšetřování.
4. Vyplňte pole
5. Po zadání těchto údajů dokončete událost.
6. Zkontrolujte oznámení spojená s touto fází

    1. Je-li nutné šetření, bude uživateli na úrovni zařízení zasláno oznámení s předmětem: Potřebné šetření AEFI.

    ![Zpráva ze systému](resources/images/aefi_trainers_guide_04_en.png)

    2. Pokud ne, je uživateli na národní úrovni zasláno jiné oznámení s předmětem: AEFI první kontrola rozhodovací úrovně dokončena

![Zpráva ze systému](resources/images/aefi_trainers_guide_05_en.png)

3. Ujistěte se, že máte uživatele, který je přiřazen ke správné skupině uživatelů, abyste mohli přijímat tato oznámení.

##### Cvičení 4 – Vyplňte první úroveň rozhodování JAKO UŽIVATEL OKRESU a zkontrolujte oznámení o vyšetřování { #exercise-4-fill-in-first-decision-making-level-as-the-district-user-and-review-the-investigation-notification }

#### Fáze 3 – Národní úroveň { #stage-3-national-level }

Budete muset změnit uživatele na uživatele na národní úrovni, který nakonec schválí zjištění případu a provede posouzení kauzality.

1. Najděte případ, na kterém jste pracovali, pomocí vyhledávání nebo seznamu/filtrů na titulní stránce a vyberte fázi programu na národní úrovni
2. Stupeň národní úrovně se negeneruje automaticky. Proto budete muset vytvořit novou událost a vybrat datum události. Ukažte účastníkům, jak vytvořit novou událost, a v případě potřeby vyberte datum. Může se stát, že toto datum bude stejné jako fáze zápisu a AEFI.
3. Projděte si všechna pole, která jsou k dispozici v této části zadávání dat, a vysvětlete je. Projděte si programová pravidla pro ovládání polí a také jejich spouštěče-
    1. Existují například pravidla pro „Klasifikace a podklasifikace konečného posouzení příčinné souvislosti“
4. Pomocí příkladu, který jste připravili, vyplňte informace pro žádost.
5. Po zadání těchto údajů dokončete událost.
6. Zkontrolujte oznámení související s touto fází
    1. Po dokončení kontroly bude na národní úroveň zasláno oznámení s předmětem „Kontrola národní úrovně AEFI dokončena“ (poznámka pro školitele: předmět a zpráva se mohou lišit, pokud se změní ve vaší konfiguraci)

![Zpráva ze systému](resources/images/aefi_trainers_guide_06_en.png)

2. Ujistěte se, že máte uživatele, který je přiřazen ke správné skupině uživatelů, abyste mohli obdržet toto oznámení.

##### Cvičení 5 – Vyplňte národní úroveň JAKO NÁRODNÍ UŽIVATEL a zkontrolujte konečné národní oznámení { #exercise-5-fill-in-the-national-level-as-the-national-user-and-review-the-final-national-notification }

#### Zkontrolujte ovládací panel trackeru { #review-the-tracker-dashboard }

1. Zůstanete-li na ovládacím panelu případu, pro který jste nevyplnili všechna data, nyní by bylo vhodné prozkoumat některé z dalších widgetů dostupných na ovládacím panelu trackeru. Užitečné widgety by byly zejména widget pro registraci, widget na horní liště a widget profilu.
2. Můžete také uživatelům ukázat, jak upravit a uložit výchozí rozvržení ovládacím panelu sledování tak, aby vyhovovalo jejich individuálním potřebám, pokud je to podporováno v jejich implementaci (poznámka: uživatel k tomu bude potřebovat přístup a může existovat výchozí rozvržení, které uloží admin, který přepíše jejich změny)

#### Dokončení zápisu programu { #completing-the-program-enrollment }

1. V tomto programu, když jste dokončili událost, to znamená, že jste také dokončili zadávání dat pro tuto fázi (protože žádná z fází v tomto programu není opakovatelná). K tomuto procesu by nyní mělo dojít u každé ze 3 fází tohoto programu, protože jste účastníkům dali pokyn, aby během ukázky a jejich cvičení na konci každé fáze vybrali tlačítko „dokončit“.
2. Když byly všechny události v programu označeny jako dokončené, mělo by to také znamenat, že zadávání dat pro tuto registraci je dokončeno. V tomto bodě vysvětlete, co znamená dokončení zápisu.
3. Na základě vašeho standardního postupu také definujte, co se stane, pokud by se to znovu objevilo jako nový případ (co se stane, když má stejná osoba další AEFI? vytvořili byste nový případ, nebo jen znovu zapsali tuto osobu do programu AEFI?). V případě potřeby můžete zvážit podrobnější prozkoumání.
4. Dokončete registraci svého případu a prohlédněte si fáze, abyste viděli, jaký to má účinek (už nemůžete upravovat žádná data v událostech, nemůžete již nedokončit žádnou z událostí)
5. Vraťte se ke svému pracovnímu seznamu a aktualizujte jej pomocí filtru pro dokončené zápisy. Případ, na kterém jste pracovali, by nyní měl být na začátku seznamu.

STOP

##### Cvičení 6 – Dokončete zápis { #exercise-6-complete-the-enrollment }

##### Cvičení 7 – Proveďte všechny probírané koncepty { #exercise-7-perform-all-concepts-discussed }

Zaregistrujte nový případ, zadejte data do každé fáze, zkontrolujte oznámení, použijte vyhledávání/filtry k nalezení případu, aktualizujte případ, dokončete zápisy
