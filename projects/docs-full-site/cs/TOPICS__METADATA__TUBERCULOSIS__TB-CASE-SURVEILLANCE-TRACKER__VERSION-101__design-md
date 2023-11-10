---
edit_url: "https://github.com/dhis2-metadata/TB_CS/blob/master/docs/tb_cs-design-1.0.1.md"
revision_date: "2022-09-13"
---

# Program sledování případů TB (Tracker) { #tb-case-surveillance-program-tracker }

## Shrnutí { #summary }

Balíček digitálních dat TB Case Surveillance Tracker pro DHIS2 vychází z [rámce WHO pro záznam a podávání zpráv od roku 2013.](https://www.who.int/tb/publications/definitions/en/) Poskytuje sadu doporučených metadata (datové prvky, programová pravidla atd.), která umožňují elektronické zachycování dat sledování TB jednotlivců/případů. Metadata sledovače jsou nakonfigurována tak, aby zajišťovala agregované standardní čtvrtletní indikátory hlášení TB o oznámeních, výstupech prvního řádku a výstupech druhého řádku, jak jsou definovány v [Definice WHO a rámec hlášení pro TB (2013)](https://www.who.int/tb/publications/definitions/en/) lze automaticky generovat z jednotlivých zachycených dat. Sledovač sledování případů TB **není** určen k podpoře správy pacienta nebo péče o pacienta. To vyžaduje podrobnější analýzu rolí, odpovědností, pracovních toků a rozhodování v prostředí, ve kterém by takové systémy byly implementovány.

## Účel a zamýšlené publikum { #purpose-intended-audience }

Tento dokument popisuje koncepční návrh, obsah a funkce standardního sledovacího programu DHIS2 pro případové sledování tuberkulózy (TB) na základě technických pokynů WHO a požadavků metadat.

Tento dokument je určen pro publikum odpovědné za implementaci datových systémů TB a / nebo HMIS v zemích, včetně:

1. Správci systému / kontaktní místa HMIS: osoby odpovědné za instalaci balíčků metadat, návrh a údržbu datových systémů HMIS a / nebo TB
2. Kontaktní místa programu TB odpovědná za dohled nad shromažďováním, správou, analýzou a vykazováním údajů národního programu TB
3. Specialisté na podporu implementace, např. ti, kteří poskytují technickou pomoc programu TB nebo základní jednotce HMIS na podporu a údržbu DHIS2 jako národního zdravotnického informačního systému a / nebo datového systému TB

Dokument návrhu systému vysvětluje, jak byl program trackeru nakonfigurován tak, aby splňoval požadavky na zadávání dat a analýzu a podporoval typický pracovní postup. Dokument neobsahuje vyčerpávající seznam všech zachycených metadat. Tento dokument také nezohledňuje zdroje a infrastrukturu potřebnou k implementaci takového systému, jako jsou servery, napájení, připojení k internetu, zálohování, školení a podpora uživatelů. Další informace o technických aspektech programu TB informujících o návrhu tohoto systému jsou k dispozici v _[publikace WHO o elektronickém záznamu a hlášení pro péči a kontrolu tuberkulózy](http://www.who.int/tb/publications/electronic_recording_reporting/en/)_. Supplementary implementation guidance for DHIS2 can be found in the [General DHIS2 Implementation Guide](https://docs.dhis2.org/en/implement/configuring-the-android-app/about-this-guide.html) a [příručka pro implementaci trasovače DHIS2](https://docs.dhis2.org/en/implement/understanding-dhis2-implementation/a-quick-guide-to-dhis2-implementation.html)

## Pozadí { #background }

Spolehlivé epidemiologické údaje jsou vyžadovány od zaměstnanců na všech úrovních národního programu tuberkulózy, aby mohli plánovat a poskytovat účinné služby péče a kontroly tuberkulózy a také sledovat provádění programových akcí. Systém sledování na základě případů má jasné výhody oproti agregovanému systému sběru dat. Podobně jako agregovaný systém dozoru lze zachytit, ověřit, agregovat, vypočítat a zobrazit **_ minimální sadu_** epidemiologických indikátorů, ale lze je rozdělit podle **libovolné kombinace** času, místa / oblasti, věku, pohlaví, případu typ, předchozí historie léčby, stav HIV, stav rezistence na léky a léčebné režimy. To nám pomáhá hlouběji porozumět epidemiologii TB a sledovat změny v čase.

Očekává se, že elektronická data založená na konkrétních případech vyústí v **lepší kvalitu dat**, protože počet kroků zadávání dat je snížen, do systému lze zabudovat automatické výpočty a validace, mohou být opraveny nekonzistentní, chybné nebo neúplné údaje rychle dokončeno pro jednotlivý záznam a lze provést odstranění duplikace k odstranění duplicitních záznamů. Systém dozoru na základě případu by měl rovněž umožnit propojení záznamů dozoru se stejným případem, i když je v průběhu léčby případ TBC přenesen nebo odeslán mezi zařízeními.

Na národní úrovni lze případová data rutinně porovnávat s jinými zdroji dat, jako jsou databáze o HIV nebo cukrovce, k měření zátěže komorbidit a zlepšení péče o pacienta, nebo k jiným zdrojům dat TBC ke kvantifikaci úrovně nedostatečné hlášení případů TBC NTP. Porovnání klinických údajů o TB s údaji o genotypizaci TB z laboratoře může také vést k detekci a vyšetřování ohnisek pro opatření v oblasti veřejného zdraví.

Nakonec lze data založená na konkrétních případech použít v epidemiologických observačních výzkumných studiích podporujících přijímání informovaných rozhodnutí o programových změnách na základě vědeckých důkazů. Získaná data by neměla překročit stanovené účely.

Viz zásada 2.4, strana 16, _Policy on the Protection of personal Data of Persons of Concern to UNHCR_ ([http://www.refworld.org/docid/55643c1d4.html](http://www.refworld.org/docid/55643c1d4.html))

## Přehled návrhu systému { #system-design-overview }

### Případ použití { #use-case }

Trasovač případů TB umožňuje registraci a dlouhodobé trasování případů TB od oznámení až po konečný výsledek případu, včetně laboratorních výsledků. Program zachycuje minimální soubor datových bodů požadovaných pro epidemiologickou analýzu údajů ze sledování případů, jak je popsáno v základní části. Patří mezi ně základní a demografické informace o případu, rizikové faktory, laboratorní výsledky, klasifikace typů rezistence na léky, poskytnuté léčebné režimy a výsledek případu. Tento program pro trasování _není_ určen k podpoře klinické správy ani péče o pacienta. Program slouží jako elektronický registr, který podporuje decentralizovaný elektronický sběr dat o trasování případů až na úroveň zdravotnických zařízení; části sledovacího programu jsou také nakonfigurovány tak, aby umožňovaly zadávání dat přímo v laboratořích. V závislosti na infrastruktuře a dostupnosti zdrojů v zemi lze zadávání dat provádět také na okresních nebo vyšších úrovních na základě papírových registrů.

Pracovní postupy v jednotlivých zemích se mohou lišit a program sledování případů by měl být podle potřeby přizpůsoben místnímu kontextu. Například tento návrh předpokládá, že případ je poprvé zapsán do elektronického registru založeného na DHIS2, když jsou při klinické návštěvě k dispozici základní informace a rizikové faktory. Fáze programu však lze znovu uspořádat v kontextech, kdy lze případ nejprve zadat do elektronického systému, jakmile bude k dispozici laboratorní výsledek, a zpětně zadat základní informace.

### Struktura programu { #program-structure }

Struktura programu v DHIS2 je následující:

![Návrh systému](resources/images/TB_CS_System_Design.png)

## Konfigurace trasovacího programu { #tracker-program-configuration }

### Detaily programu { #program-details }

**Typ trasované entity** pro tento program je „osoba“. Sledované typy entit jsou často sdíleny napříč programy v integrované instanci DHIS2. Program je nakonfigurován tak, aby **vyžadoval, aby uživatel vyhledal minimálně 1 atribut** před registrací nového TEI.

#### Přístup { #access }

Úroveň **přístupu** je konfigurována jako **chráněná** za účelem ochrany osobních údajů před neoprávněným přístupem. Uživatel může vyhledávat a číst instance sledovaných entit, které jsou ve vlastnictví organizační jednotky, ke které je uživateli přiřazeno shromažďování dat. přístup. Pokud uživatel hledá TEI, který existuje mimo jeho organizační jednotku, pro kterou uživatel nemá oprávnění pro sběr dat, je uživateli nabídnuta možnost přístupu k záznamu pacienta nejprve zaznamenáním důvodu. Tento přístup k soukromí je známý jako „rozbití skla“, protože umožňuje uživateli vykonávat svou práci bez svolení nebo pomoci zvenčí, ale ponechává jasnou stopu, kterou je třeba auditovat. Jakmile uživatel uvede důvod pro rozbití skla, pak získejte dočasné vlastnictví instance sledované entity (viz [Tracker User Guide](https://docs.dhis2.org/en/implement/configuring-the-android-app/features-supported.html#breaking-the-glass) pro více informací.)

### Detaily zápisu { #enrollment-details }

**Datum zápisu** je chápáno jako „datum diagnostiky TBC“. TEI může mít více registrací, protože je možné, že případ vstoupí do systému více než jednou (tj. Obnoví se a stane se znovu případem). V situacích, kdy byl případ dříve zapsán do sledovače sledování případů TB, je možné zobrazit historii zápisu pomocí [Widget pro zápis](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/tracker-capture.html#manage_tracked_entity_instance_enrollment).

### Atributy { #attributes }

Když je případ zapsán ke sledování TB případu jako trasovaná instance entity (TEI), jsou zaznamenány atributy TEI, aby se vytvořil profil případu. Všimněte si, že pokud je program TB tracker nainstalován společně s dalšími programy v instanci DHIS2, mohou být tyto společné atributy sdíleny mezi různými programy (např. Křestní jméno, příjmení, datum narození).

### Fáze 1: Registrace TB { #stage-1-tb-registration }

Fáze registrace TB zachycuje základní informace, rizikové faktory a komorbidity včetně stavu HIV. Toto je neopakovatelná programová fáze. Zatímco většina informací o základní fázi by měla být dokončena při prvním zaregistrování případu, lze tuto fázi aktualizovat kdykoli během registrace, pokud jsou k dispozici nové informace (zejména aktualizace místa onemocnění nebo stavu HIV).

**Datum události** pro registraci TB je datum záznamu (nebo hlášení) dat v DHIS2.

Událost registrace TB se automaticky vygeneruje po fázi registrace.

![Zápis](resources/images/TB_CS_Enrollment.png)

Datový prvek **[Aktuální adresa (na mapě)]** je nakonfigurován jako typ „souřadnice“, aby umožnil geoprostorovou analýzu v aplikaci Mapy.

Datový prvek **[Historie předchozí léčby]** se řídí standardními definicemi WHO:

|  |  |
| :-- | :-- |
| **Nový** | Noví pacienti nikdy nebyli léčeni na TB nebo užívali léky proti TB po dobu kratší než 1 měsíc |
| **relaps** | Dříve léčení pacienti dostávali v minulosti 1 měsíc nebo více léků proti TB. Pacienti s relapsem byli již dříve léčeni na TB, byli prohlášeni za vyléčeni, nebo léčba byla dokončena na konci jejich posledního průběhu léčby a nyní jim je diagnostikována opakovaná epizoda TB (buď skutečný relaps, nebo nová epizoda TB způsobená reinfekcí). |
| **Léčba po selhání léčby první linie** | Dříve léčení pacienti dostávali v minulosti 1 měsíc nebo více léků proti TB. Léčbou po selhání jsou pacienti, kteří byli dříve léčeni na TB a jejichž léčba selhala na konci jejich posledního průběhu léčby. |
| **Léčba po selhání léčby druhé linie** | Dříve léčení pacienti dostávali v minulosti 1 měsíc nebo více léků proti TB. Léčbou po selhání jsou pacienti, kteří byli dříve léčeni na TB a jejichž léčba selhala na konci jejich posledního průběhu léčby. |
| **Léčba po ztrátě k následnému trasování** | Dříve léčení pacienti dostávali v minulosti 1 měsíc nebo více léků proti TB. Léčba po ztrátě u následných pacientů byla dříve léčena na TB a na konci jejich poslední léčby byla prohlášena za ztracenou při následném trasování. (Tito byli dříve známí jako léčba po selhání pacientů. |
| **Ostatní dříve léčení** | Dříve léčení pacienti dostávali v minulosti 1 měsíc nebo více léků proti TB. Dalšími dříve léčenými pacienty jsou ti, kteří již byli dříve léčeni na TB, ale jejichž výsledek po posledním průběhu léčby není znám nebo není doložen. |
| **Neznámý** | Pacienti s neznámou předchozí anamnézou léčby TB nespadají do žádné z uvedených kategorií. |

V této fázi bylo nakonfigurováno několik **pravidel programu**, aby se zlepšila kvalita dat a usnadnilo zadávání dat. Pokud případ není uveden s diagnózou HIV a nebyl testován více než 6 měsíců, programové pravidlo zobrazí následující varování, které vás vyzve k opětovnému testování:

![Varování proti opětovnému testování HIV](resources/images/TB_CS_HIV_Warning.png)

### Fáze 2: Laboratorní výsledky { #stage-2-laboratory-results }

Tato fáze je opakovatelná. Data mohou zadávat kliničtí pracovníci, zaměstnanci zařízení, zaměstnanci laboratoře nebo zaměstnanci okresní TB v závislosti na kontextu země. **Datum události** je „datum odběru vzorku“.

Výsledky pro více typů testů pro stejnou kolekci vzorků lze zadat v jedné události.

Balíček TB Case Surveillance Tracker umožňuje sběr dat pro 14 typů diagnostických testů. Datové prvky zachycené pro každý typ testu jsou specifické pro test, včetně toho, jaký typ testu byl proveden, datum laboratorních výsledků, číslo vzorku a případ, zda byla detekována rezistence. Příslušné testy lze zahrnout nebo vyloučit z fáze Laboratorní výsledky v DHIS2 v závislosti na jejich dostupnosti v národní referenční laboratoři (NRL) v implementující zemi. Podobně lze seznam léků pro fenotypový DST upravit podle léků první a druhé linie příslušných pro danou zemi. V obou případech se to děje prostřednictvím konstant během počáteční konfigurace balíčku. (Viz část [Konstanty](#Constants))

Níže je uveden příklad formuláře pro zadávání údajů pro vybrané typy testů:

![Mikroskopie stěru sputa](resources/images/TB_CS_SSM.png)

![Xpert MTB/RIF](resources/images/TB_CS_Xpert.png)

![DST](resources/images/TB_CS_DST.png)

![LPA](resources/images/TB_CS_LPA.png)

Data zadaná v laboratorní fázi se používají k výpočtu klasifikace případů a odolnosti pomocí pravidel programu, která lze také zobrazit ve widgetu Horní lišta a Widget zpětné vazby v aplikaci Zachycení Trasování. Program používá datové prvky automaticky vyplněné pravidly programu, včetně DE „klasifikace odolnosti“ na základě laboratorních výsledků. DE také zahrnují datum, kdy byla detekována rezistence na rifampicin, kdy byla rezistence „poprvé detekována“ v případě více testů v sekci Stav. Tato data jsou vyžadována pro výpočty konkrétních indikátorů.

### Fáze 3: Léčba { #stage-3-treatment }

Fáze léčby je opakovatelná fáze, která by měla být omezena na dvě události, aby se zohlednila _jediná_ změna režimu léčby. Pravidla programu se používají k zajištění toho, že stejný režim nelze zadat dvakrát. **Datum události** je „**datum zahájení léčby**“. Pokud dojde ke změně léčebného režimu, zaznamená se druhá událost a datum zahájení léčby odráží zahájení nového léčebného režimu. „Očekávané datum zahájení léčby“ je automaticky naplánováno tři dny od registrace; lze jej přeplánovat ručně.

![Léčba](resources/images/TB_CS_Treatment.png)

#### Sekce: Klasifikace typu TB rezistence na léky { #section-tb-drug-resistance-type-classification }

Tato část umožňuje uživateli přepsat DE [Klasifikace rezistence], která byla automaticky vygenerována programovým pravidlem na základě laboratorních výsledků v systému. Lékař / klinik může například určit jiný stav klasifikace než ten, který se automaticky vypočítá podle vzorců obsažených v tomto programu.

![Přiřazení klasifikace odolnosti](resources/images/TB_CS_Treatment_classification.png)

#### Sekce: Léčebný režim { #section-treatment-regimen }

Program podporuje léčebné režimy první a druhé linie s úplným seznamem léků, které lze upravit podle národní dostupnosti a pokynů pro léčbu. Použití konstant pomáhá implementátorovi povolit / zakázat zobrazování ošetření pro uživatele zadávajícího data.

#### Data zahájení léčby { #start-dates-for-treatment }

Zachycení dat zahájení léčby je důležité, protože výsledky pro případy léčby druhé linie jsou hodnoceny na základě data zahájeného v léčbě druhé linie; zatímco výsledky pro případy léčby první linie jsou hodnoceny na základě zápisu (datum diagnózy). Data zahájení léčby v první linii a v druhé linii se automaticky počítají na základě pravidel programu a v této fázi jsou zahrnuta jako datové prvky, aby bylo zajištěno, že mohou být správně použity pro analýzu (např. pro výpočet počtu dní zpoždění při léčbě).

#### Termíny konce platnosti výsledku { #outcome-due-dates }

„Konečný Výsledek“ DE automaticky vypočítá datum pomocí pravidla programu založeného na typu léčby (první nebo druhá linie) a datu zahájení léčby. Pokud je zvolen léčebný režim, vypočítá se datum „Konečný Výsledek“ a přiřadí se podle délky dané léčby (u léčby první linie je datum splatnosti naplánováno na 9 měsíců od data zahájení léčby; u léčby druhé linie je datum výsledku je naplánováno na 24 měsíců od data zahájení léčby).

![Datum platnosti výsledku](resources/images/TB_CS_Outcome_due.png)

### Fáze 4: Výsledek { #stage-4-outcome }

#### Datum výsledku a datum vypršení platnosti { #outcome-date-and-due-date }

Výsledná fáze je dokončena na konci zápisu. **Datum události** pro tuto fázi programu je pojato jako „datum výsledku“. **Termín** události je konfigurován s popisem „očekávané datum výsledku. Ve výchozím nastavení je termín platnosti pro část s výsledky naplánován na 180 dní po datu zápisu.“ Aktuální funkcionalita DHIS2 v 2.33 neumožňuje přiřadit vypočítanou DE „vypršení platnosti“ z fáze léčby jako datum platnosti pro fázi výsledek. Datum platnosti fáze Výsledek lze změnit ručně, ale lze jej změnit pouze jednou. Pro uživatele to lze provést po zahájení léčby a vygenerování DE ve fázi léčby „Výsledek platnosti“. Když je fáze výsledku opožděná (aktuální datum je pozdější než vypočítaný DE „Výsledek platnosti“ z fáze léčby, zobrazí se v Widgetu zpětné vazby zpráva.

#### Výsledek léčby { #treatment-outcome }

Když je výsledek vybrán jako součást sady možností, pravidla programu ukazují uživateli definici výsledku WHO, což pomůže zajistit, aby byly zaznamenány správné definice výsledků. Tato programová pravidla berou v úvahu typ léčby (první nebo druhá linie), aby se zobrazila správná definice výsledku.

Výsledky „vyléčené“, „dokončené“ a „nehodnocené“ lze navíc zadat až po uplynutí 6 měsíců od data registrace (datum diagnózy). Výsledek léčby „selhal“ lze zadat pouze 5 měsíců po datu registrace (datum diagnózy).

![Výsledek](resources/images/TB_CS_Outcome.png)

#### Denotifikace případu TB { #denotifying-a-tb-case }

Tato fáze také umožňuje uživateli „denotifikovat“ případ TB. Například pokud jsou laboratorní výsledky pro klinicky diagnostikovaný případ TB negativní, může uživatel denotifikovat případ, protože to není TB. Denotifikaci lze také použít, pokud je v systému nalezen duplicitní případ. Když je zaškrtnuto „Denotifikovat případ“ DE, je uživatel vyzván k výběru důvodu pro denotifikaci ze sady možností a poskytnutí dalších důkazů pro denotifikaci nebo poskytnutí duplicitního čísla záznamu TB v případě duplikace. **_Pokud byl případ z jakéhokoli důvodu denotifikován, je případ vyloučen z analýzy případů TB._**

#### Dokončení výstupní fáze { #completing-outcome-stage }

Výzva **Vyberte výsledek nebo určete, zda nejde o případ TB.** Zobrazí se vedle výsledku léčby vyvolaného pravidlem programu. Není možné, aby uživatel dokončil fázi Výsledek bez zadání výsledku nebo označení případu. Fáze Výsledek je nakonfigurována tak, aby blokovala zadávání dat po dokončení fáze.

![Dokončení konečné fáze](resources/images/TB_CS_Complete_outcome.png)

### Pravidla programu { #program-rules }

Pravidla programu se v programu TB Case Surveillance Program hojně používají k zobrazení / skrytí datových prvků za účelem optimalizace formuláře pro zadávání dat, zobrazení varování / zpětné vazby uživateli zadávání dat a automatickému výpočtu a přiřazování hodnot dat datovým prvkům. Níže jsou popsána vybraná pravidla programu pro pochopení konfigurace tohoto programu pro TB Case Surveillance. Úplný seznam pravidel programu najdete v referenčním souboru metadat.

#### Omezit počet ošetření { #limit-number-of-treatment-events }

Pro sledování případu TB by měla být zachycena pouze jedna událost léčby pro každou změnu léčebného režimu (např. Z první linie do druhé linie). Pravidla programu se používají k omezení počtu událostí na jednu změnu léčebného režimu. Aby bylo zajištěno, že stejný režim nelze zadat dvakrát, událost, která má léčbu první linie, umožní výběr režimu léčby druhé linie pouze u druhé události a naopak.

#### Omezit možnosti výsledku a zobrazit definice výsledku { #limit-outcome-options-and-show-outcome-definitions }

Ve fázi Výsledku jsou pravidla programu nakonfigurována tak, aby zobrazovala varování, které poskytuje uživateli zadávání dat definici výsledku případu WHO v závislosti na tom, zda byla poskytnuta léčba první nebo druhé linie.

|  |  |
| :-- | :-- |
| **Výsledek** | **Vyléčeno** |
| Definice (léčba první linie) | Plicní pacient s bakteriologicky potvrzenou TBC na začátku léčby, který byl negativní v posledním měsíci léčby a alespoň jedním předcházejícím nálezem stěrem nebo bakteriální kultivací. |
| Definice (léčba druhé linie) | Léčba dokončená podle doporučení národní politiky bez důkazů o selhání A tři nebo více po sobě jdoucích kultur odebraných s alespoň 30denním odstupem jsou po intenzivní fázi negativní. Pokud léčba selhala, nedostatek konverze na konci intenzivní fáze znamená, že se pacient nezmění během maximální doby trvání intenzivní fáze aplikované programem. Pokud není stanovena maximální doba trvání, navrhuje se 8-měsíční přerušení. U režimů bez jasného rozdílu mezi intenzivní fází a fází pokračování se doporučuje přerušení 8 měsíců po zahájení léčby, aby se určilo, kdy budou platit kritéria pro Vyléčen, Léčba dokončena a Léčba selhala. |
| Pravidla programu | 1. Možnost není k dispozici pro výsledky, které jsou zaznamenány do 6 měsíců po registraci. 2. Možnost není k dispozici pro klinicky diagnostikované případy. 3. Možnost není k dispozici pro případy mimoplicních TB podstupujících léčbu druhé linie (zobrazí se chybová zpráva). |
| **Výsledek** | **Dokončeno** |
| Definice (léčba první linie) | Pacient s TB, který dokončil léčbu bez důkazů o selhání, ale bez záznamu prokazujícího, že výsledky stěru nebo kultivace sputa v posledním měsíci léčby a alespoň při jedné předchozí příležitosti byly negativní, buď proto, že nebyly provedeny testy, nebo proto, že výsledky nebyly k dispozici. |
| Definice (léčba druhé linie) | Léčba dokončená podle doporučení národní politiky bez důkazů o selhání, ALE žádný záznam o tom, že tři nebo více po sobě jdoucích kultur odebraných s odstupem alespoň 30 dnů jsou po intenzivní fázi negativní. Pokud léčba selhala, nedostatek konverze na konci intenzivní fáze znamená, že se pacient nezmění během maximální doby trvání intenzivní fáze aplikované programem. Pokud není stanovena maximální doba trvání, navrhuje se 8-měsíční přerušení. U režimů bez jasného rozdílu mezi intenzivní fází a fází pokračování se doporučuje přerušení 8 měsíců po zahájení léčby, aby se určilo, kdy budou platit kritéria pro Vyléčen, Léčba dokončena a Léčba selhala. |
| Pravidla programu | Tato možnost není k dispozici pro výsledky, které jsou zaznamenány do 6 měsíců po registraci. |
| **Výsledek** | **Selhalo** |
| Definice (léčba první linie) | Pacient s TB, jehož stěr nebo kultivace sputa jsou pozitivní v 5. měsíci nebo později během léčby. |
| Definice (léčba druhé linie) | Léčba ukončena nebo potřeba trvalé změny režimu alespoň dvou anti-TB léků z důvodu: nedostatečné konverze do konce intenzivní fáze nebo bakteriologické reverze v pokračovací fázi po konverzi na negativní, nebo důkazu další získané rezistence na fluorochinolony, nebo injekční léky druhé linie, nebo nežádoucí reakce na léky (ADR). Pokud léčba selhala, nedostatek konverze na konci intenzivní fáze znamená, že se pacient nezmění během maximální doby trvání intenzivní fáze aplikované programem. Pokud není stanovena maximální doba trvání, navrhuje se 8měsíční přerušení. U režimů bez jasného rozdílu mezi intenzivní fází a fází pokračování se doporučuje přerušení 8 měsíců po zahájení léčby, aby se určilo, kdy budou platit kritéria pro Vyléčen, Léčba dokončena a Léčba selhala. Pojmy „konverze“ a „reverze“ kultury, jak jsou zde používány, jsou definovány následovně: Konverze (na negativní): kultura se považuje za převedenou na negativní, když se zjistí, že dvě po sobě jdoucí kultury, s odstupem alespoň 30 dnů, jsou negativní . V takovém případě se jako datum převodu použije datum odběru vzorků první negativní kultury. Reverze (na pozitivní): kultura se považuje za navrácenou na pozitivní, když se po počáteční konverzi zjistí, že dvě po sobě jdoucí kultury, odebrané s alespoň 30denním odstupem, jsou pozitivní. Pro účely definice Léčba selhala se o reverzi uvažuje, pouze pokud k ní dojde v pokračovací fázi. |
| Pravidla programu | Možnost není k dispozici pro výsledky, které jsou zaznamenány do 5 měsíců po registraci. |
| **Výsledek** | **Zemřel** |
| Definice (léčba první linie) | Pacient s TB, který z jakéhokoli důvodu zemřel před zahájením léčby nebo v jejím průběhu. |
| Definice (léčba druhé linie) | Pacient, který během léčby z jakéhokoli důvodu zemřel. |
| Pravidla programu | -/- |
| **Výsledek** | **Ztraceno pro následný krok** |
| Definice (léčba první linie) | Pacient s TB, který nezačal léčbu nebo jehož léčba byla přerušena na 2 po sobě jdoucí měsíce nebo déle. |
| Definice (léčba druhé linie) | Pacient, jehož léčba byla přerušena na 2 po sobě jdoucí měsíce nebo déle. |
| Pravidla programu | -/- |
| **Výsledek** | **Neohodnoceno** |
| Definice (léčba první linie) | Pacient s TB, u kterého není přiřazen žádný výsledek léčby. To zahrnuje případy „převedené“ na jinou léčebnou jednotku i případy, u nichž není výsledek léčby zpravodajské jednotce znám. |
| Definice (léčba druhé linie) | Pacient, kterému není přiřazen žádný výsledek léčby. (To zahrnuje případy „převedené“ na jinou léčebnou jednotku, jejichž výsledek léčby není znám). |
| Pravidla programu | Tato možnost není k dispozici pro výsledky, které jsou zaznamenány do 6 měsíců po registraci. |

#### Automaticky přiřazené hodnoty datových prvků { #auto-assigned-data-element-values }

Hodnoty dat (možnosti v sadě možností) se automaticky přiřadí datovým prvkům Klasifikace případů a Klasifikace odporu při zadávání dat v laboratorní fázi. Tyto datové prvky klasifikace se také zobrazují na horní liště jako součást ovládacího panelu TEI pro snadný přístup, když má uživatel otevřené aplikace pro zadávání dat pro danou TEI v aplikaci Tracker Capture.

**_Klasifikace případů (DE)_**

Tento datový prvek je automaticky naplněn pravidly programu na základě následujících kritérií. Klasifikaci případů je přiřazena hodnota „klinicky diagnostikována“, dokud nebudou při registraci do programu zadána laboratorní data.

|  |  |
| :-- | :-- |
| Klinicky diagnostikováno | Výchozí stav klasifikace při registraci případu v TB Case Surveillance. |
| Bakteriologicky potvrzeno | Pokud jsou v DHIS2 zadány laboratorní výsledky pro následující typy testů: _Pozitivní výsledky pro mikroskopii nebo kultivaci sputa_; _MTB / Odolnost vůči drogám zjištěná rychlými diagnostickými testy WHO nebo LPA_. Program nebrání uživatelům v zadávání výsledků DST před zadáním výsledků předchozích testů v Laboratorní fázi. Zadání **pouze** výsledků DST nezmění metodu potvrzení z „Klinicky diagnostikováno“ na „Bakteriologicky potvrzeno“, protože testování DST závisí na kultuře. |

**_Klasifikace rezistence (DE)_**

Tento datový prvek je automaticky naplněn pravidly programu na základě následujících kritérií. V praxi však může uživatel zadávající údaje klasifikaci ručně změnit (např. Pokud lékař / klinický lékař určil, že jde o DR).

|  |  |
| :-- | :-- |
| DS (citlivý na léky) | Výchozí klasifikace při registraci případu v TB Case Surveillance. Klasifikaci je automaticky přiřazena možnost ‘DS (citlivý na léky)‘, dokud nejsou zadány další laboratorní údaje. |
| DR (rezistentní na léky) | Rezistence na jakékoliv léky |
| Mono Res (Mono-rezistentní) | Odolnost pouze k jednomu léku první linie proti TB |
| Poly Res (Poly rezistentní) | Rezistence na více než jeden lék proti TB první linie, jiný než isoniazid a rifampicin |
| RR (rezistentní na Rifampicin) | Rezistence na rifampicin zjištěná pomocí fenotypových nebo genotypových metod, s rezistencí nebo bez rezistence na jiné léky proti TB. Zahrnuje jakoukoli rezistenci na rifampicin ve formě mono-rezistence, poly-rezistence, MDR nebo XDR. |
| MDR (rezistentní k více lékům) | Rezistence alespoň na isoniazid a rifampicin |
| XDR (Extenzivně rezistentní vůči lékům) | Rozsáhlá rezistence na léčiva (XDR): kromě rezistence na více léků rezistence na jakékoli fluorochinolony (levofloxacin nebo moxifloxacin a jedno injekční léčivo druhé linie (amikacin) |
| RR/MDR | Ne laboratorně potvrzené případy, které začaly léčbou druhé linie (více informací v části Léčba). |

**_Zahájení léčby a data platnosti výsledku_**

Pravidla programu se používají k přiřazení data události fáze léčebného programu jako DE pro „zahájení léčby v první linii“ a „zahájení léčby v druhé linii.“ Kromě toho je DE „očekávané datum výsledku“ doplněno pravidlem programu a zahrnuty do obou fází léčby a výsledků. U léčby první linie je očekávané datum výsledku 9 měsíců od data zahájení léčby. U léčby druhé linie je očekávané datum výsledku 24 měsíců od zahájení léčby. Data se také používají pro analýzu. Například počet dní zpoždění léčby se vypočítá na základě času mezi diagnózou a zahájením léčby.

#### Ilustrativní scénáře { #illustrative-scenarios }

V souvislosti s TB Case Surveillance platí kombinace programových pravidel pro různé případové scénáře následující:

|  |  |  |
| :-- | :-- | :-- |
| **Nebyly zaznamenány žádné laboratorní výsledky ani léčba případu** | Dostupné výsledky ve fázi Výsledek: zemřel, ztracen pro následný účel. | Pokud případ není TB, je možné případ „denotifikovat“ ve fázi Výsledek. Tím odstraníte případ z analytických procesů. |
| **Nebyly zaznamenány žádné laboratorní výsledky.** Případ je umístěn na léčbu první linie a nebyla zaregistrována žádná předchozí léčebná událost. | Datum zahájení léčby v první linii je zaznamenáno ve stavové sekci. Očekávané datum výsledku léčby (9 měsíců od data zahájení léčby) je také zobrazeno v sekci Stav ve fázi léčby. | Při přidání druhé události ošetření bude uživateli zabráněno vybrat léčbu první linie v režimu léčby. |
| **Byly zaznamenány laboratorní výsledky a byla zjištěna rezistence na léky.** Případ je umístěn na léčbu první linie a nebyla zaregistrována žádná předchozí léčebná událost. | Datum zahájení léčby v první linii je zaznamenáno ve stavové sekci. Očekávané datum výsledku léčby (9 měsíců od data zahájení léčby) je také zobrazeno v sekci stavu. Ve Widgetu zpětné vazby se zobrazí varovná zpráva: _**Byla zjištěna rezistence na léky a pacient je léčen v první linii.**_ | Při přidání druhé události ošetření bude uživateli zabráněno vybrat léčbu první linie v režimu léčby. |
| **Nebyly zaznamenány žádné laboratorní výsledky a nebyla zaznamenána žádná předchozí léčba, ale případ je umístěn na léčbu druhé linie** | Případ je registrován jako klinicky diagnostikovaný případ RR / MDR. Datum zahájení léčby druhé linie je zaznamenáno v sekci stavu. Očekávané datum výsledku léčby (24 měsíců od data zahájení léčby) je zobrazeno v sekci stavu. | Jakmile jsou laboratorní výsledky zadány do fáze Laboratorní výsledky, systém je automaticky znovu přiřazen. Při přidání druhé události ošetření je uživateli zabráněno vybrat léčbu druhé linie v režimu léčby. |
| **Laboratorní výsledky byly zaznamenány v DHIS2 a byla zjištěna rezistence na léky.** Není registrována žádná předchozí léčebná událost. Případ je umístěn na léčbu druhé linie | Datum zahájení léčby druhé linie je zaznamenáno v sekci stavu. Očekávané datum výsledku léčby (24 měsíců od data zahájení léčby) je zobrazeno v sekci stavu. | Když přidáte druhou událost ošetření, bude uživateli zabráněno vybrat léčbu druhé linie v režimu léčby. |
| **U DHIS2 nebyly zaznamenány žádné laboratorní výsledky.** Předchozí léčbou byla léčba první linie. Případ je umístěn na léčbu druhé linie. | Datum zahájení léčby druhé linie je zaznamenáno v sekci stavu. Očekávané datum výsledku léčby (24 měsíců od data zahájení léčby) je zobrazeno v sekci stavu. | Není možné vytvářet nové události léčby. |
| **Laboratorní výsledky byly zaznamenány v DHIS2 a byla zjištěna rezistence na léky.** Předchozí léčbou byla léčba první linie. Případ je umístěn na léčbu druhé linie. | Datum zahájení léčby druhé linie je zaznamenáno v sekci stavu. Očekávané datum výsledku léčby (24 měsíců od data zahájení léčby) je zobrazeno v sekci stavu. | Není možné vytvářet nové události léčby. |

### Widget horní lišty { #top-bar-widget }

Widget horní lišty v aplikaci Tracker Capture je užitečný pro uživatele zadávajícího data, aby měl přehled o informacích o TEI (případ) při každém otevření registrace TEI pro tento program.

Níže uvedená tabulka shrnuje indikátory a proměnné programu zobrazené ve Widgetu horní lišty a způsob jejich výpočtu. „Typ“ označuje, zda je konkrétní proměnná konfigurována jako indikátor programu se zapnutou možností „zobrazit ve formuláři“, nebo zda je vypočítána a zobrazena pomocí pravidel programu.

| Proměnná | Typ | Výpočet |
| :-- | :-- | :-- |
| Aktuální věk (roky) | Indikátor programu | Počet let mezi aktuálním datem a atributem trasované entity „Datum narození (věk)“. |
| Měsíce od zápisu | Indikátor programu | Počet měsíců od registrace do programu (datum oznámení) do aktuálního data. |
| Léčebný režim | Pravidlo programu | Zobrazení aktuálního (posledního) zaznamenaného léčebného režimu (počáteční první linie, opakovaná léčba první linie, druhá linie) |
| Klasifikace případu | Pravidlo programu | Pokud v laboratorní fázi není zaznamenán žádný pozitivní výsledek kultivace, rozmazání nebo Xpert MTB, klasifikace je „klinicky diagnostikováno“. Pokud je u některého z testů zaznamenán pozitivní výsledek, klasifikace je „Bakteriologicky potvrzeno“. |
| Klasifikace rezistence | Pravidlo programu | Na základě výsledků Xpert RIF a jakýchkoli výsledků rezistence ve fázi programu DST je případ klasifikován jako citlivý na léky (DS) nebo s různými typy rezistence na léky (DR, RR, MDR, XDR). Případ je klasifikován jako případ „Nelaboratorně potvrzeno DR“, pokud je vybrán na stránce léčby A nebyly zaznamenány žádné výsledky rezistence na léky. |
| Rezistence | Pravidlo programu | Uvádí léky, u nichž byla pomocí testování XIFT RIF nebo DST detekována rezistence na léky. |

### Widget zpětné vazby { #feedback-widget }

Následující zpětnovazební zprávy jsou nakonfigurovány tak, aby se zobrazovaly v Widgetu zpětné vazby, pokud jsou splněny určité podmínky, jak je uvedeno v tabulce níže:

| Zpráva | Stav |
| :-- | :-- |
| Byla zjištěna rezistence na léky a pacient je léčen v první linii. | Pacient je na léčbě první linie, přestože má laboratorní / DST výsledky indikující rezistenci na léky. |
| GeneXpert MTB nebyl detekován. Toto nemusí být případ TB. | Výsledky Xpert MTB jsou „Nezjištěno“, což naznačuje, že se nejedná o případ TB |
| Nebyla zjištěna žádná rezistence na léky, ale pacient je léčen v druhé linii. | Pacient je léčen v druhé linii, aniž by laboratorní / DST výsledky ukazovaly na lékovou rezistenci. |
| Lze přidat pouze dvě události léčby. | Uživatel přidá třetí událost ošetření. Podporovány jsou pouze dva, aby se zohlednil počáteční režim léčby, a jedna změna režimu. |
| Výsledek je po datu platnosti. | Pokud je aktuální datum pozdější než vypočítaný DE „Výsledek v čase vypršení“ v sekci ošetření, pak se zpráva zobrazí v widgetu zpětné vazby. |
| Okamžitě vyplňte výsledek léčby. | Zaškrtávací políčko „Není TB“ je vyplněno, což znamená, že případ není TB a registrace by měla být uzavřena. |
| Byl zaznamenán pozitivní výsledek stěru. Zkontrolujte hlášené „Místo choroby“. | Byl zaznamenán pozitivně zkreslený výsledek, ale hodnota zadaná pro „Místo onemocnění“ nezahrnuje „Plicní“. |

## Další funkce { #additional-features }

### Konstanty { #constants }

Balíček TB Case Surveillance Tracker obsahuje sadu testů a seznam léků, které může implementující země upravit podle národního kontextu (např. Jaké léky a testy se v zemi používají / jsou k dispozici). Použití konstant umožňuje správci systému v implementující zemi snadno „zapnout“ nebo „vypnout“ typy léků a testy v závislosti na dostupnosti v zemi. Když je kompletní balíček nainstalován do instance DHIS2, jsou v systému zahrnuty všechny datové prvky pro všechny testy a léky obsažené v tomto balíčku. Ve výchozím nastavení jsou všechny konstanty nastaveny na '1' (povolení příslušných datových prvků pro zadávání dat) a lze je nakonfigurovat na '2' implementátorem nebo správcem systému podle kontextu země, pokud to není nutné (deaktivace souvisejících datových prvků pro data vstup). Pokud bude test nebo lék později v zemi k dispozici, může administrátor jednoduše znovu povolit datové prvky změnou konstanty z hodnoty „2“ na hodnotu „1“.

![Konstanty](resources/images/TB_CS_Constants.png)

## Indikátory analýzy a programu { #analytics-and-program-indicators }

### Hlášení případových dat do agregovaných hlášení TB { #reporting-case-based-data-into-aggregate-tb-reports }

Trasovací systém TB založený na případech zachycuje data, která lze přenést do standardních, souhrnných zpráv (tj. Měsíčně, čtvrtletně nebo častěji podle země). Souhrnný návrh systému TB v DHIS2 je přístupný na [who.dhis2.org/documentation/#tb](https://who.dhis2.org/documentation/#tb).

Balíček obsahuje sadu programových indikátorů, které jsou mapovány na odpovídající datové prvky a kombinace možností kategorií datových sad v souhrnném balíčku TB. Mapování je založeno na kódech objektů metadat.

Vlastní atribut **Datový prvek pro export souhrnných dat** `vudyDP7jUy5` obsahuje referenční kód prvků agregovaných dat. Pole **Kombinace možností kategorie pro agregovaný export** obsahuje referenční kódy kombinací možností kategorií.

Navrhovaný přenos hodnot z trasovače na agregát je založen na následujících požadavcích GET a POST API:

1. Zdrojový požadavek:  `../api/analytics/dataValueSet.json?dimension=dx:` "{program indicator uid/s}" `&dimension=pe:` "{relative period/s}" `&dimension=ou:` {organisation unit level} `&outputIdScheme=ATTRIBUTE:` {"custom attribute:`vudyDP7jUy5`"}
2. Cílový požadavek: `..api/dataValueSets?dataElementIdScheme=CODE&categoryOptionComboIdScheme=CODE&importStrategy=CREATE_AND_UPDATE&mergeMode=REPLACE&dryRun=false`

Balíček navíc přichází se sadou indikátorů, které lze přenést do formuláře zprávy GTB.

### Ovládací panel { #dashboard }

Pomocí indikátorů programu byla znovu vytvořena podmnožina vizualizací dat z balíčku WHO Aggregate TB Package. Tyto vizualizace zobrazují data z programu Trasovač. Tyto vizualizace byly WHO vybrány jako nejužitečnější pro častější monitorování na úrovni zařízení, např. mezi odesláním měsíčních / čtvrtletních souhrnných zpráv do HMIS. Tyto vizualizace mohou také podporovat uživatele na úrovni zařízení nebo okresu k porovnání dat sledování případů TB zachycených v programu Trasovač s agregovanými daty odeslanými do HMIS.

## Skupiny uživatelů { #user-groups }

Balíček TB Case Surveillance Tracker Package obsahuje následující skupiny uživatelů:

-   TB Admin: umí editovat / prohlížet metadata; žádný přístup k datům [všechny fáze programu]
-   TB Data capture: dokáže zobrazit metadata, může zachytit data [všechny fáze programu]
-   TB Access: lze zobrazit metadata, lze zobrazit data [všechny fáze programu]
-   TB Lab data capture:  lze zobrazit metadata, lze zachycovat data [Pouze TB registrační fáze a Laboratorní fáze]

## Reference { #references }

-   _Definice a rámec pro podávání zpráv o tuberkulóze (revize z roku 2013, aktualizovaná v prosinci 2014)._ ([http://www.who.int/tb/publications/definitions/en](http://www.who.int/tb/publications/definitions/en))
-   _Porozumění a použití údajů o tuberkulóze._ ([http://www.who.int/tb/publications/understanding_and_using_tb_data/en](http://www.who.int/tb/publications/understanding_and_using_tb_data/en))
-   _Standardy a měřítka pro sledování tuberkulózy a životně důležité registrační systémy: Kontrolní seznam a uživatelská příručka._ ([http://www.who.int/tb/publications/standardsandbenchmarks/en](http://www.who.int/tb/publications/standardsandbenchmarks/en))
-   _Hodnocení případového modulu Uganda DHIS2 MDR-TB (zpráva Araxe Hovhanisyana po posouzení a návštěvě provedené v červnu 2017)_
-   _Hodnocení případového trasovače Ghana DHIS2 (zpráva Araxa Hovhanisyana po vyhodnocení a návštěvě provedené v srpnu 2018)_
-   _Hodnocení případového trackeru Tanzanie (ETL) (zpráva Laury Andersonové, Tomase Matase a Debory Pedrazzoli po hodnocení a návštěvě provedené v červenci 2018)_
-   _Elektronické záznamy a hlášení pro péči a kontrolu tuberkulózy_ ([http://www.who.int/tb/publications/electronic_recording_reporting/en](http://www.who.int/tb/publications/electronic_recording_reporting/en))
-   _Digitální zdraví pro strategii Ukončení TB: vývoj prioritních produktů a jejich fungování_ ([http://erj.ersjournals.com/content/48/1/29](http://erj.ersjournals.com/content/48/1/29)), zejména položka 2.2 (Digitální oznámení případů TB) v online dodatku  ([http://erj.ersjournals.com/content/erj/suppl/2016/05/26/13993003.00424-2016.DC1/ERJ-00424-2016_supplement.pdf](http://erj.ersjournals.com/content/erj/suppl/2016/05/26/13993003.00424-2016.DC1/ERJ-00424-2016_supplement.pdf))
-   _Principles for digital development_ ([https://digitalprinciples.org/](https://digitalprinciples.org/)), in particular the sections on ‘Design With the User’ ([https://digitalprinciples.org/principle/design-with-the-user/](https://digitalprinciples.org/principle/design-with-the-user/)), ‘Be Data Driven’ ([https://digitalprinciples.org/principle/be-data-driven/](https://digitalprinciples.org/principle/be-data-driven/)) and ‘Address Privacy and Security’ ([https://digitalprinciples.org/principle/address-privacy-security/](https://digitalprinciples.org/principle/address-privacy-security/))
-   _Politika ochrany osobních údajů dotčených osob UNHCR_ ([http://www.refworld.org/docid/55643c1d4.html](http://www.refworld.org/docid/55643c1d4.html)), zejména kapitola 2.
-   _Etické pokyny pro implementaci strategie End TB_ [http://www.who.int/tb/publications/2017/ethics-guidance](http://www.who.int/tb/publications/2017/ethics-guidance)), strany 40-41 a 53-54 o ochraně soukromí a bezpečnosti.
-   _WHO pokyny k etickým otázkám při dozoru nad veřejným zdravím_ ([http://www.who.int/ethics/publications/public-health-surveillance](http://www.who.int/ethics/publications/public-health-surveillance))
