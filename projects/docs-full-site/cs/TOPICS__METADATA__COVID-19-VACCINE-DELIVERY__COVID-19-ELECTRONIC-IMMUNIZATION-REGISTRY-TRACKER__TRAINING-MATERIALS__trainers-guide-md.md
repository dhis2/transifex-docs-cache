---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/training/covac_data_entry_trainers_guide.md"
revision_date: "2021-09-17"
---

# COVAC – Příručka trenéra zadávání dat { #covac-data-entry-trainers-guide }

**DHIS2 Immunization Toolkit**

**Registr očkování proti COVID-19**

## Poznámky k přípravě { #preparation-notes }

Chcete-li upravit tuto příručku, budete muset zkontrolovat místní SOP, které jsou na místě, a upravit jakýkoli pracovní postup nebo funkce diskutované v pořadí, v jakém s nimi bude uživatel pracovat.

1. Pokud se jedná o postup zadávat tyto údaje z papírového formuláře, bude užitečné mít vyplněnou kopii formuláře, který by normálně používali jako referenci. Může to být pouze formulář, který jste sami vyplnili, nebo může být kopii formuláře ze skutečné realizace, který jste obdrželi od Ministerstva zdravotnictví.

2. Pokud zadávají data v reálném čase, není nezbytně nutné mít formuláře, ale měli byste si připravit podrobnosti příkladu, který můžete ve svých příkladech sledovat.

3. U cvičení a aktivit během dema zajistěte, aby byly k dispozici kopie formulářů nebo případových studií, které mohou účastníci použít k registraci svých vlastních případů.

4. Vaše tréninková databáze by měla mít vyplněny některé existující případy, které pomohou podpořit předvádění funkcí vyhledávání, filtrování a ovládacího panelu

5. Pokud předvádíte funkčnost pracovních seznamů, budete muset zadat data, která splňují kritéria každého z demonstrovaných filtrů.

6. Chcete-li demonstrovat funkce zpráv o nadcházejících a opožděných událostech, budete muset naplánovat případy pro jejich druhou dávku (ale nevyplňovat údaje pro jejich druhou dávku). Mělo by se jednat o kombinaci jednotlivců naplánovaných na předchozí i nadcházející dny ode dne samotného školení, abyste mohli předvést obě zprávy.

## Průvodce krok za krokem { #step-by-step-guide }

1. Přihlaste se do systému DHIS2 pomocí Uživatelského jména a hesla

2. Přejděte na zachycení trasovače

3. Prohlédněte si výběr organizační jednotky a programu a vyberte zdravotnické zařízení, ve kterém budete pracovat

4. Stručně popište první seznam stránek, pokud se objeví, ale pamatujte, že se k tomu vrátíme později

### Registrace (nové pouzdro) { #registration-new-case }

1. Kdykoli budeme mít nového člověka, který je očkován, budeme ho muset zaregistrovat v DHIS2. Vyberte Registrovat pro registraci nové osoby, která dostává vakcínu

2. Zkontrolujte stránku zápisu, kterou jste nakonfigurovali. Popište atributy, které používáte, a proč tam jsou. Všimněte si, že tyto atributy vám umožňují sledovat tuto osobu, když prochází programem, včetně jejího pozdějšího nalezení, což bude také ukázáno. Atributy obsažené ve standardním balíčku vakcíny COVID-19 jsou popsány v dokumentu návrhu systému.

    A. Popište datum zápisu, které se nazývá „Datum registrace“

    b. Popište proces generování místního ID a jedinečného ID generovaného systémem. Místní ID je přiděleno lokálně, zatímco jedinečný systémový identifikátor je generován systémem. Další podrobnosti naleznete v dokumentu návrhu systému.

3. Zadejte data pro atributy. Pokud používáte papírový formulář, použijte jej jako referenci k popisu toho, jak se každý detail z formuláře vyplní do DHIS2. Po zadání a vysvětlení podrobností pro registraci vyberte **Uložit a pokračovat**.

STOP

### Cvičení 1 – Zaregistrujte nový případ { #exercise-1-register-a-new-case }

### Ovládací panel trackeru { #tracker-dashboard }

1. Po uložení podrobností budete konfrontováni s _*ovládacím panelem trackeru*_. To je často ohromující, ale zajistěte, aby bylo k dispozici výchozí rozložení, aby všichni viděli totéž.
2. Doporučuje se nejprve přeskočit všechny ostatní widgety a zaměřit se na _widget pro zadávání dat_. Po zadání některých údajů se můžete vrátit k ostatním widgetům.
    1. Rychle zrekapitulujte fáze, které jsou v programu (jmenovitě 'Očkování') s odkazem na jakoukoli prezentaci (prezentace) na pozadí nebo ukázky, které jste již provedli.
    2. Vysvětlete, že stejné informace se shromažďují během jejich 1^st^ a 2^nd^ dávky. Brzy se vrátíme k 2. dávce.

## Vstup dat { #data-entry }

### Očkování - 1^st^ dávka { #vaccination-1st-dose }

1. Fáze očkování se generuje automaticky. Abyste viděli zbytek formuláře, budete muset ručně vyplnit datum, kdy je dávka podána.
2. Existuje řada programových pravidel, která se používají ke skrytí/zobrazení polí na stránce pro zadávání dat. Popište tato pravidla účastníkovi. Logiku ve formuláři pro zadávání dat naleznete v souboru kontroly metadat.
3. Po vysvětlení umístění skrytých polí a jejich spouštěčů resetujte formulář odstraněním těchto hodnot (nebo odstraňte událost a vytvořte novou). Nyní byste měli vidět formulář pro fázi Očkování v původním rozložení.
4. Vezměte si svůj příklad, který jste připravili, a zadejte podrobnosti do první fáze
5. Pokud jste spokojeni se zadanými údaji, můžete **dokončit** událost.
6. Budou zde tlačítka pro **smazání** události nebo tisk formuláře. Existuje několik tlačítek pro odstranění události, registrace a entity. Uživatelé mohou mít oprávnění provádět pouze určité akce odstranění. Prohlížejte pouze funkce odstranění, které jsou relevantní pro skupinu, se kterou pracujete.
7. Po dokončení akce budete požádáni, abyste naplánovali 2. dávku. Naplánujte to na základě „doporučeného data další dávky“ vašeho očkovacího produktu

STOP

### Cvičení 2 – Vyplňte podrobnosti o 1^st^ dávce a naplánujte si 2^nd^ dávku { #exercise-2-fill-in-1st-dose-details-and-schedule-the-2nd-dose }

### Vyhledávání { #searching }

1. Přihlaste se jako uživatel pro zadávání dat. Přejděte zpět k zachycení trackeru a vyberte zařízení, ve kterém se případ, který chcete aktualizovat, nachází
2. Existuje několik filtrů, které jsou dostupné při pohledu na úvodní stránku se seznamem řádků v rámci zachycení trackeru. To zahrnuje předem definované seznamy, které byly předloženy jako součást očkovacího balíčku. Všechny tyto filtry jsou užitečné a můžete je nyní popsat.
3. Po koncepčním vysvětlení těchto případů si povšimněte, že nakonec projdeme a dokončíme případy na konci tohoto dema. Ukažte jim, jak filtry fungují, aby zmenšily seznam řádků v jejich zařízení, a také otevřete aktivní vs. dokončený případ, abyste jim ukázali, jak se bude zadávání dat a ovládací panel trasování lišit.
4. K dispozici je také funkce vyhledávání, která nám umožní najít naše případy. Vyberte Hledat a zadejte podrobnosti o existujícím případu. Tím se pouzdro zvedne a můžete je vybrat, aby se přenesly na řídicí panel trackeru. To je užitečné, pokud potřebujete najít konkrétní případ pro jakýkoli účel.
5. Než budete pokračovat, najděte **předchozí případ**, který jste právě zadali s uživatelem vašeho zařízení

STOP

### Cvičení 3 – Projděte si funkci vyhledávání a filtrování a najděte případ { #exercise-3-review-the-search-and-filter-functionality-to-find-a-case }

### Očkování - 2^nd^ dávka { #vaccination-2nd-dose }

1. Fáze očkování se generuje automaticky. Abyste viděli zbytek formuláře, budete muset ručně vyplnit datum, kdy je dávka podána. Datum, do kterého zadáte, se může lišit od data splatnosti. Vysvětlete účastníkům, proč tomu tak je.
2. Existuje řada programových pravidel, která se používají ke skrytí/zobrazení polí na stránce pro zadávání dat. Popište tato pravidla účastníkovi. Logiku ve formuláři pro zadávání dat naleznete v souboru kontroly metadat.
3. Po vysvětlení umístění skrytých polí a jejich spouštěčů resetujte formulář odstraněním těchto hodnot (nebo odstraňte událost a vytvořte novou). Nyní byste měli vidět formulář pro fázi Očkování v původním rozložení.
4. Vezměte si svůj příklad, který jste připravili, a zadejte podrobnosti do druhé fáze
5. Pokud jste spokojeni se zadanými údaji, můžete **dokončit** událost.
6. Budou zde tlačítka pro **smazání** události nebo tisk formuláře. Existuje několik tlačítek pro odstranění události, registrace a entity. Uživatelé mohou mít oprávnění provádět pouze určité akce odstranění. Prohlížejte pouze funkce odstranění, které jsou relevantní pro skupinu, se kterou pracujete.
7. Po dokončení akce budete požádáni, abyste naplánovali další dávku. Zrušte toto plánování, protože nebudou dostávat žádné další dávky.

STOP

#### Cvičení 4 – Vyplňte 2^nd^ podrobnosti o dávce { #exercise-4-fill-in-2nd-dose-details }

### Zkontrolujte ovládací panel trackeru { #review-the-tracker-dashboard }

1. Zůstanete-li na ovládacím panelu případu, pro který jste nyní vyplnili všechna data, nyní by bylo vhodné prohlédnout si některé z dalších widgetů dostupných na ovládacím panelu trackeru. Užitečnými widgety by byly zejména widget pro zápis, widget na horní liště a widget profilu.
2. Můžete také uživatelům ukázat, jak upravit a uložit výchozí rozvržení ovládacím panelu sledování tak, aby vyhovovalo jejich individuálním potřebám, pokud je to podporováno v jejich implementaci (poznámka: uživatel k tomu bude potřebovat přístup a může existovat výchozí rozvržení, které uloží admin, který přepíše jejich změny)

### Dokončení zápisu programu { #completing-the-program-enrollment }

1. V tomto programu, když jste dokončili událost, to znamená, že jste také dokončili zadávání dat pro tuto fázi (protože žádná z fází v tomto programu není opakovatelná). K tomuto procesu by nyní mělo dojít pro každou ze 2 fází tohoto programu, protože jste účastníkům dali pokyn, aby během ukázky a jejich cvičení na konci každé fáze zvolili tlačítko „dokončit“.

2. Když byly všechny události v programu označeny jako dokončené, mělo by to také znamenat, že zadávání dat pro tuto registraci je dokončeno. V tomto bodě vysvětlete, co znamená dokončení registrace (obdrželi všechny požadované dávky vakcíny)

3. Dokončete registraci svého případu a prohlédněte si fáze, abyste viděli, jaký to má účinek (už nemůžete upravovat žádná data v událostech, nemůžete již nedokončit žádnou z událostí)

4. Vraťte se ke svému pracovnímu seznamu a aktualizujte jej pomocí filtru pro dokončené zápisy. Případ, na kterém jste pracovali, by nyní měl být na začátku seznamu.

STOP

### Cvičení 5 – Dokončete zápis { #exercise-5-complete-the-enrollment }

### Cvičení 6 – Proveďte všechny probírané koncepty { #exercise-6-perform-all-concepts-discussed }

Zaregistrujte nový případ, zadejte data do každé fáze, použijte vyhledávání/filtry k nalezení případu, aktualizujte případ, dokončete registrace

## Zprávy { #reports }

Sekce zpráv aplikace pro zachycení sledování je v tomto scénáři zvláště užitečná, protože mezi 1.^ a 2.^ dávkou očkování proti covidu bude často značný rozdíl. Obzvláště užitečné je demonstrovat u zprávy „nadcházející události“, aby bylo možné získat seznamy lidí, u kterých je naplánováno podání 2^nd^ dávky, a také u zprávy „události po termínu“ získat seznam lidí, kteří byli naplánováni, ale dostali nedostanou svou 2. dávku. Tyto seznamy je také možné získat pomocí filtrů seznamů na úvodní stránce, které jsou k dispozici v balíčku; tyto zprávy však obsahují datum, kdy mají přijít/byly naplánovány, což není dostupné při použití filtrů seznamu na úvodní stránce.

### Nadcházející dávky { #upcoming-doses }

**Poznámka pro trenéra: Abyste mohli provést tuto ukázku, musíte mít ve svém systému k dispozici naplánované dávky. To bude zahrnovat zapsání lidí do očkovacího programu proti Covid-19, ve kterém je druhá dávka naplánována na budoucí datum od provedení této ukázky/cvičení.**

Chcete-li spustit sestavu pro načtení osob naplánovaných na druhou dávku:

1. V rámci zachycení trackeru vyberte z nabídky na levé straně „přehledy“.
2. Vyberte přehled „nadcházející události“. Tato zpráva vám umožní vytvořit seznam těch, kteří mají podle plánu dostat svou 2. dávku očkování proti COVID-19.
3. Vyplňte parametry pro sestavu:

    1. **Organizační jednotka**: Toto je nadřazená organizační jednotka, která je zahrnuta v přehledu
    2. **Program** : Vyberte program očkování proti covidu 3. **Rozsah organizační jednotky** – jsou 3 možnosti 4. Vybráno : vytvořte zprávu obsahující osoby registrované ve vámi vybrané organizační jednotce 5. Bezprostřední děti : vytvořte sestava obsahující osoby registrované ve vámi vybrané organizační jednotce a úroveň organizační jednotky přímo pod ní 6. Všechny děti : vytvořte sestavu obsahující osoby registrované ve vámi vybrané organizační jednotce a všechny úrovně organizační jednotky pod ní
    3. **Filtr**: umožňuje odfiltrovat osoby, které jste označili pro sledování
    4. **Datum**: umožňuje zadat datum, které chcete zahrnout do zprávy. Všimněte si, že toto je v podstatě datum jejich druhé dávky, takže pokud vyberete „události s termínem dnes“, získáte seznam lidí, kteří mají dnes naplánovanou druhou dávku. To může být užitečné pro načtení denního seznamu záznamů, které mají podat druhou dávku v rámci vakcinačních míst(a), které jste vybrali

4. Výběrem „jít“ spustíte přehled

Protože můžete získat seznam osob naplánovaných na druhou dávku, může být užitečné zahrnout do tohoto seznamu položky, jako je číslo mobilního telefonu a e-mail, pokud chcete těmto jednotlivcům ručně připomenout jejich nadcházející plánovanou návštěvu. Můžete se rozhodnout, jaké atributy se zobrazí na seznamu na úvodní stránce nebo v sestavách, jako jsou tyto, v konfiguraci programu v části atributy. Volba "zobrazit v seznamu" rozhodla, které atributy se v těchto seznamech zobrazí.

STOP

### Cvičení 7 – Spusťte hlášení a zjistěte datum, kdy jsou lidé naplánováni na druhou dávku { #exercise-7-run-a-report-to-identify-the-date-people-are-scheduled-for-their-second-dose }

### Dávky po platnosti { #overdue-doses }

**Poznámka pro trenéra: Abyste mohli provést toto demo/cvičení, musíte mít vynechané dávky již dostupné ve vašem systému. To bude zahrnovat zapsání lidí do očkovacího programu Covid-19, ve kterém je druhá dávka naplánována na datum, které JIŽ Uplynulo od provedení tohoto ukázkového/cvičení.**

Chcete-li spustit hlášení, abyste získali osoby, které vynechaly druhou dávku:

1. V rámci zachycení trackeru vyberte z nabídky na levé straně „přehledy“.
2. Vyberte přehled „události po splatnosti“. Tato zpráva vám umožní vytvořit seznam těch, kteří zmeškali naplánovanou 2. dávku očkování proti COVID-19.
3. Vyplňte parametry pro sestavu:
    1. **Organizační jednotka**: Toto je nadřazená organizační jednotka, která je zahrnuta v přehledu
    2. **Program** : Vyberte program očkování proti covidu
    3. **Rozsah organizační jednotky** -- jsou 3 možnosti
        1. Vybráno : vytvoření přehledu obsahujícího osoby registrované ve vámi vybrané organizační jednotce
        2. Bezprostřední děti: vytvořte zprávu obsahující osoby registrované ve vámi vybrané organizační jednotce a úroveň organizační jednotky přímo pod ní
        3. Všechny děti : vytvořte sestavu obsahující osoby registrované ve vybrané organizační jednotce a všechny úrovně organizační jednotky pod ní
    4. **Filtr**: umožňuje odfiltrovat osoby, které jste označili pro sledování
4. Zpráva se spustí, jakmile tyto parametry vyberete automaticky, a zobrazí se vám datum splatnosti, na které bylo naplánováno, aby dostali svou 2. očkovací dávku.

STOP

### Cvičení 8 – Spusťte hlášení a identifikujte lidi, kteří vynechali svou druhou dávku { #exercise-8-run-a-report-to-identify-people-that-have-missed-their-second-dose }
