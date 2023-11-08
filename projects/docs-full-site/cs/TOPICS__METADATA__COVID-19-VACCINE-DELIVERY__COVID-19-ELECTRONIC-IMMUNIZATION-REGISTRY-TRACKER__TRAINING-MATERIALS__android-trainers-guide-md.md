---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/training/covac_android_trainers_guide.md"
revision_date: "2021-09-17"
---

# COVAC – Příručka pro školitele Androidu { #covac-android-trainers-guide }

**Aplikace DHIS2 pro Android**

**DHIS2 Immunization Toolkit**

**Registr očkování proti COVID-19**

## Poznámky k přípravě { #preparation-notes }

Chcete-li upravit tuto příručku, budete muset zkontrolovat místní SOP, které jsou na místě, a upravit jakýkoli pracovní postup nebo funkce diskutované v pořadí, v jakém s nimi bude uživatel pracovat.

1. Pokud se jedná o postup zadávat tyto údaje z papírového formuláře, bude užitečné mít vyplněnou kopii formuláře, který by normálně používali jako referenci. Může to být pouze formulář, který jste sami vyplnili, nebo může být kopii formuláře ze skutečné realizace, který jste obdrželi od Ministerstva zdravotnictví.
2. Pokud zadávají data v reálném čase, není nezbytně nutné mít formuláře, ale měli byste si připravit podrobnosti příkladu, který můžete ve svých příkladech sledovat.
3. U cvičení a aktivit během dema zajistěte, aby byly k dispozici kopie formulářů nebo případových studií, které mohou účastníci použít k registraci svých vlastních případů.
4. Vaše školicí databáze by měla mít vyplněné některé existující případy, které vám pomohou demonstrovat funkce vyhledávání a filtrování
5. Pokud demonstrujete funkčnost filtru, budete muset zadat data, která splňují kritéria každého z demonstrovaných filtrů
6. Chcete-li demonstrovat nadcházející a opožděné funkce filtru, budete muset naplánovat případy buď pro jejich první nebo druhou dávku (ale nevyplňovat údaje pro jejich dávku). Mělo by se jednat o kombinaci jednotlivců naplánovaných na předchozí i nadcházející dny ode dne samotného školení, abyste mohli předvést oba typy filtrů.

## Průvodce krok za krokem { #step-by-step-guide }

Přihlaste se do systému DHIS2 z aplikace pro Android pomocí uživatelského jména a hesla

1. Prohlédněte si výběr organizační jednotky a programu a vyberte zdravotnické zařízení, ve kterém budete pracovat
2. Stručně popište první seznam stránek, pokud se objeví, ale pamatujte, že se k tomu vrátíme později

### Přístup k programu { #accessing-the-program }

1. Když se poprvé přihlásíte do DHIS2, dostanete se na domovskou obrazovku se seznamem všech vašich datových sad a/nebo programů
2. K programu, se kterým pracujete, se dostanete jeho výběrem z této domovské obrazovky

### Registrace nové osoby { #registering-a-new-person }

1. Po výběru programu budete přesměrováni na hlavní obrazovku vyhledávání/registrace v aplikaci pro Android
2. Chcete-li někoho zaregistrovat v systému Android, musíte nejprve provést vyhledávání. Důvodem je snížení duplicit. Zadejte podrobnosti o osobě a proveďte vyhledávání
3. Pokud vyhledávání nepřinese žádné výsledky, zaregistrujte novou osobu.
4. Chcete-li přejít na stránku registrace, vyberte organizační jednotku a datum registrace osoby
    - Popište datum zápisu, které se nazývá ‚Datum registrace‘ _[poznámka pro školitele: nahraďte jménem z vaší konfigurace]_
5. Zkontrolujte podrobnosti o registraci, které jste nakonfigurovali. Popište atributy, které používáte, a proč tam jsou. Všimněte si, že tyto atributy vám umožňují sledovat tuto osobu, když prochází programem, včetně jejího pozdějšího nalezení, což bude také ukázáno. Atributy obsažené ve standardním balíčku vakcíny COVID-19 jsou popsány v dokumentu návrhu systému. Atributy, do kterých byly zadány údaje při vyhledávání, budou přeneseny při registraci.
    - Popište proces generování místního ID a jedinečného ID generovaného systémem. Místní ID je přiděleno místně, zatímco jedinečný systémový identifikátor je generován systémem. Další podrobnosti naleznete v dokumentu návrhu systému.[poznámka pro školitele: pokud změníte způsob, jakým tato ID fungují, nahraďte prosím popis zde]
6. Zadejte data pro atributy. Pokud používáte papírový formulář, použijte jej jako referenci k popisu toho, jak se každý detail z formuláře vyplní do DHIS2. Po zadání a vysvětlení podrobností pro registraci vyberte Uložit

STOP

#### Cvičení 1 – Vstupte do programu a zaregistrujte novou osobu { #exercise-1-access-the-program-and-register-a-new-person }

### Ovládací panel trackeru { #tracker-dashboard }

1. Po uložení podrobností budete konfrontováni s ovládacím panelem trasovače. V ovládacím panelu trasovače je mnoho různých prvků, které je třeba zkontrolovat; můžete je však zpočátku přeskočit a vrátit se k nim poté, co zadáte některá data
2. Zaměřte se na skutečný prvek programové fáze na ovládacím panelu dané osoby. To vám umožní přidávat nové události a zadávat údaje o osobě.
    - Rychle zrekapitulujte fáze, které jsou v programu (jmenovitě „Očkování“), s odkazem na jakoukoli prezentaci na pozadí nebo ukázku(y), které jste již provedli.
    - Vysvětlete, že stejné informace se shromažďují během jejich 1. a 2. dávky. K 2. dávce se brzy vrátíme.

### Vstup dat { #data-entry }

### Očkování - 1^st^ Dávka { #vaccination-1st-dose }

1. Fáze očkování se generuje automaticky. V závislosti na vaší konfiguraci může nebo nemusí být také generována událost pro 1. dávku. Pokud se negeneruje automaticky, budete muset událost vytvořit. [Poznámka pro školitele: postupujte podle místního postupu založeného na konfiguraci v implementaci, kterou podporujete]
2. Po vygenerování události nebo výběru naplánované/automaticky vytvořené události ve fázi očkování si můžete prohlédnout podrobnosti o 1. dávce.
3. Existuje řada programových pravidel, která se používají ke skrytí/zobrazení polí na stránce pro zadávání dat. Popište tato pravidla účastníkovi. Logiku ve formuláři pro zadávání dat naleznete v souboru kontroly metadat.
4. Po vysvětlení umístění skrytých polí a jejich spouštěčů resetujte formulář odstraněním těchto hodnot (nebo odstraňte událost a vytvořte novou). Nyní byste měli vidět formulář pro fázi Očkování v původním rozložení.
5. Vezměte si svůj příklad, který jste připravili, a zadejte podrobnosti do první fáze.
6. Pokud jste spokojeni se zadanými údaji, můžete událost dokončit.
7. Po dokončení akce budete požádáni o naplánování 2. dávky. Naplánujte si to na základě „doporučeného data další dávky“ vašeho vakcínového produktu.
8. Jakmile je toto naplánováno, měli byste mít dvě akce v rámci fáze očkování. Jednou by mělo být dokončeno a jeden by měl být naplánován; můžete popsat, jak se to zobrazí účastníkům.

STOP

#### Cvičení 2 – Vyplňte podrobnosti o 1^st^ dávce a naplánujte si 2^nd^ dávku { #exercise-2-fill-in-1st-dose-details-and-schedule-the-2nd-dose }

### Synchronizace dat { #synchronizing-data }

1. Nyní by bylo vhodné prodiskutovat strategii synchronizace pro vaši implementaci. Například jaká je výchozí rychlost synchronizace dat (1 hodina, 24 hodin).
2. Ukažte jim, jak ručně synchronizovat data se serverem z domovské stránky systému Android. To nahraje všechna data, která pro daný program zadali, na server
3. Prostřednictvím webového rozhraní jim můžete ukázat TEI, které jste vytvořili na Androidu, abyste si ověřili, že data byla správně synchronizována.
4. Po synchronizaci dat nebude na zařízení Android žádná ikona synchronizace, protože všechna data byla synchronizována. Jakmile začnete zadávat nová data, která ještě nejsou synchronizována, tato ikona se znovu objeví.

### Vyhledávání { #searching }

1. Přihlaste se a vyberte svůj program z domovské stránky systému Android
2. Najděte předchozí případ, do kterého jste právě vstoupili (a naplánovali si pro něj 2. dávku) se svým uživatelem

STOP

#### Cvičení 3 – Synchronizujte data a zkontrolujte funkci vyhledávání, abyste našli případ { #exercise-3-sync-data-and-review-the-search-functionality-to-find-a-case }

### Očkování – 2^nd^ Dávka { #vaccination-2nd-dose }

1. Vyberte plánovanou 2. dávku ve fázi vakcinace
2. Vyberte datum očkování a pokračujte v zadávání podrobností o 2. dávce na základě papírového formuláře nebo případové studie, kterou používáte jako referenční
    - Poznamenejte si všechna další pravidla programu, která spouštějí další prvky v rámci 2. dávky (tj. na základě vaší konfigurace se může zobrazit zpráva pro dokončení programu nebo nové datové prvky související s 1. dávkou atd.)
3. Dokončete zadání

STOP

#### Cvičení 4 – Vyplňte 2^nd^ Podrobnosti o dávce { #exercise-4-fill-in-2nd-dose-details }

### Dokončení registrace do programu { #completing-the-program-enrollment }

1. V tomto programu, když jste dokončili událost, to znamená, že jste také dokončili zadávání dat pro tuto fázi (protože žádná z fází v tomto programu není opakovatelná). K tomuto procesu by nyní mělo dojít pro každou ze 2 fází tohoto programu, protože jste účastníkům dali pokyn, aby během ukázky a jejich cvičení na konci každé fáze zvolili tlačítko „dokončit“.
2. Když byly všechny události v programu označeny jako dokončené, mělo by to také znamenat, že zadávání dat pro tuto registraci je dokončeno. V tomto bodě vysvětlete, co znamená dokončení registrace (obdrželi všechny požadované dávky vakcíny)
3. Dokončete registraci svého případu a prohlédněte si fáze, abyste viděli, jaký to má účinek (už nemůžete upravovat žádná data v událostech, nemůžete již nedokončit žádnou z událostí)
4. Vraťte se na úvodní stránku vyhledávání a aktualizujte ji pomocí filtru pro dokončené registrace. Případ, na kterém jste pracovali, by nyní měl být na začátku seznamu.

STOP

#### Cvičení 5 – Dokončete zápis { #exercise-5-complete-the-enrollment }

### Prohlédněte si ovládací panel trasování { #review-the-tracker-dashboard }

1. Zůstaňte na ovládacím panelu případu, pro který jste nyní vyplnili všechna data, a nyní by bylo vhodné zkontrolovat některé další prvky dostupné na ovládacím panelu dané osoby.

#### Cvičení 6 – Proveďte všechny diskutované koncepty { #exercise-6-perform-all-concepts-discussed }

Zaregistrujte nový případ, zadejte data do každé fáze, použijte vyhledávání/filtry k nalezení případu, aktualizujte případ, dokončete registrace

### Použití filtrů { #using-filters }

Sekce vyhledávání/registrace v aplikaci Android Capture vám umožňuje vybrat filtry, které vám umožní vytvářet seznamy pro „nadcházející události“, abyste mohli načíst seznamy lidí, u kterých je naplánováno přijetí druhé dávky, a také „události po splatnosti“. získat seznam lidí, kteří byli naplánováni, ale nedostali svou 2. dávku. Existuje také řada dalších užitečných filtrů, které lze použít z této části aplikace.

### Nadcházející dávky { #upcoming-doses }

> **Poznámka**
>
> Poznámka pro trenéra: Abyste mohli provést tuto ukázku, musíte mít v systému k dispozici naplánované dávky. To bude zahrnovat zapsání lidí do očkovacího programu Covid-19, ve kterém je druhá dávka naplánována na budoucí datum, od kdy provedete toto demo/cvičení.

Chcete-li vytvořit filtr pro načtení osob naplánovaných na druhou dávku:

1. Vyberte tlačítko filtru na obrazovce vyhledávání/registrace aplikace pro Android
2. Vyberte „Plán“ ve skupině filtrů „Stav události“.
3. Ve skupině filtrů „datum události“ vyberte příslušná data
4. Chcete-li filtrovat v rámci konkrétní organizační jednotky, vyberte organizační jednotku jako další filtr
5. Seznam bude načten a okamžitě k dispozici k prohlížení

STOP

#### Cvičení 7 – Spusťte sestavu a zjistěte datum, kdy jsou lidé naplánováni na 2^nd^ dávku { #exercise-7-run-a-report-to-identify-the-date-people-are-scheduled-for-their-2nd-dose }

### Dávky po platnosti { #overdue-doses }

> **Poznámka**
>
> Poznámka pro trenéra: Abyste mohli toto demo/cvičení provést, musíte mít ve vašem systému již dostupné vynechané dávky. To bude zahrnovat zapsání lidí do očkovacího programu Covid-19, ve kterém je druhá dávka naplánována na datum, které JIŽ Uplynulo od provedení tohoto ukázkového/cvičení.

Chcete-li spustit hlášení, abyste získali osoby, které vynechaly druhou dávku:

1. Vyberte tlačítko filtru na obrazovce vyhledávání/registrace aplikace pro Android
2. Ve skupině filtrů „Stav události“ vyberte „Po splatnosti“.
3. Ve skupině filtrů „Stav registrace“ vyberte data „Aktivní“.
4. Chcete-li filtrovat v rámci konkrétní organizační jednotky, vyberte organizační jednotku jako další filtr
5. Seznam bude načten a okamžitě k dispozici k prohlížení

STOP

#### Cvičení 8 – Spusťte hlášení a identifikujte lidi, kteří zmeškali svou 2^nd^ dávku { #exercise-8-run-a-report-to-identify-people-that-have-missed-their-2nd-dose }
