---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/docs/cvc_eir_design.md"
revision_date: "2021-12-01"
---

# Návrh systému elektronického sledování registru Covid-19 { #cvc-eir-tracker-design }

## Úvod { #introduction }

Dokument Návrh imunizačního systému COVID-19 poskytuje přehled koncepčního designu použitého ke konfiguraci programu sledovače DHIS2 sloužícího jako registr elektronické imunizace vakcín COVID-19. Tento dokument je určen k použití implementátory DHIS2 na národní a regionální úrovni, aby mohli podporovat implementaci a lokalizaci balíčku. Při lokalizaci a přizpůsobení tohoto konfiguračního balíčku je třeba vzít v úvahu místní pracovní toky, národní pokyny a příslušné pokyny pro očkovací produkty.

Tento balíček byl vyvinut v reakci na vyjádřenou potřebu zemí a partnerů monitorovat rovnost a zavádění vakcín proti COVID-19 napříč prioritními skupinami a sledovat jednotlivce při dokončení očkovacího plánu.

Cílem tohoto balíčku je zlepšit včasnost, přesnost dat, rozšířit pokrytí, efektivitu a efektivitu dodávání vakcín proti COVID-19. Vychází také z [Pokynů k vývoji národního plánu nasazení a očkování pro vakcíny COVID-19](https://www.who.int/publications/i/item/WHO-2019-nCoV-Vaccine_deployment-2020.1). jako zpětná vazba od úředníků WHO a CDC a obecné standardy a pokyny pro očkování upravené z balíčku imunizačního registru DHIS2

Protože národní směrnice a politiky se budou lišit, měl by být tento balíček přizpůsoben národnímu kontextu.

## Přehled návrhu systému { #system-design-overview }

### Případ použití { #use-case }

Datový model trackeru v DHIS2 umožňuje jednotlivce registrovat a sledovat v průběhu řady zdravotnických služeb. Tento model lze využít ke sledování, jak jednotlivci dokončili očkovací kalendáře podle národních zásad a doporučení produktů, a také zachycovat robustní data na individuální úrovni pro podporu analýzy distribuce vakcíny, absorpce a dokončení podle demografie, základních podmínek a dalších proměnných. .

### Obsah { #content }

Balíček obsahuje:

-   Trasovací program, který registruje jednotlivce a každou očkovací událost
-   Soubor indikátorů programu, který pokrývá požadavky pokynů WHO o zavádění vakcín.
-   Sada programových indikátorů, které se vkládají do souhrnné datové sady pro každodenní monitorování
-   Souhrnný soubor dat pro každodenní sledování
-   Soubor indikátorů založený na agregovaném souboru dat
-   Denní monitorovací panel založený na agregovaném souboru dat

### Určení uživatelé { #intended-users }

Program je navržen tak, aby podporoval uživatele na úrovni kliniky/zařízení, poskytoval zaměstnancům lepší nástroje pro rozhodování a umisťoval klienta do středu informačního systému a zároveň odstraňoval jeho nadbytečnost při podávání zpráv. V závislosti na infrastruktuře a dostupnosti zdrojů v zemi však lze zadávání dat dokončit na úrovni okresu na základě papírových registrů.

-   Kliničtí uživatelé: Program Immunization eRegistry tracker je optimalizován pro zadávání dat v Point of Care.
-   Zaměstnanci zařízení: Data mohou do DHIS2 zadávat také pracovníci zadávající data, pokud není možné zadávat údaje z místa péče. Pracovní seznamy jsou navrženy tak, aby podporovaly pracovníky zařízení při sledování pacientů, kteří potřebují následná opatření nebo kteří mají zpoždění podle očkovacího plánu.
-   Manažeři zařízení, okresní zdravotní úřady a pracovníci národního programu: Data generovaná prostřednictvím programu se vkládají do standardizovaných řídicích panelů, které umožňují sledovat příjem očkovacích látek, výpadky a rozčlenění podle věku / pohlaví / profese

Ilustrativní pracovní postup:

![pracovní postup](resources/images/Covac_workflow.png)

Pracovní postupy se budou v jednotlivých zemích lišit. Návrh programu by měl být přezkoumán a lokalizován podle kontextu. Například pracovní postup na obrázku výše předpokládá, že jednotlivci budou registrováni v DHIS2, když se dostaví na místo očkování, aby dostali svou první dávku. Alternativou, kterou lze zvážit, je předběžná registrace způsobilých jednotlivců do systému jako instance trasovaných entit (např. z existujícího registru zdravotnických pracovníků).

## Konfigurace trasovacího programu { #tracker-program-configuration }

| Struktura | Popis |
| --- | --- |
| Zápis | Pokud osoba v instanci ještě není zaregistrována, je zaregistrována a zapsána do registru imunizace jako TEI (typová osoba typu TEI) a její data jsou zachycena do atributů Registrace jako, které odpovídají stávajícím balíčkům COVID-19 pro DHIS2. Atributy TEI: národní ID, jedinečné ID, křestní jméno, pohlaví, datum narození se odhaduje, datum narození (věk), číslo mobilního telefonu, adresa (aktuální), oblast, povolání |
| Program Fáze 1: Očkování | Toto je opakovatelná fáze. Data pro tuto fázi se zadávají pokaždé, když osoba dostane očkování. Datum události = Datum podání dávky \ Datum vypršení = Umožňuje naplánovat další dávku |
| Oddíl 1.1 Základní zdravotní podmínky | Informace o zdravotním stavu a/nebo již existujících základních stavech, u nichž bylo rozhodnuto vystavit se výrazně vyššímu riziku závažné infekce nebo úmrtí. Balíček obsahuje stejné již existující podmínky používané ve zbytku balíků COVID. |
| Oddíl 1.2 Otázky před imunizací | U první dávky se tato část ptá, zda klient prodělal COVID-19 během posledních 90 dnů. Po druhé dávce se také zeptá, zda existuje a |
| Oddíl 1.3: Očkování | Zaregistruje podrobnosti o poskytnutém typu vakcíny, číslo šarže, datum expirace a navrhované datum dalšího očkování. |

### Datové prvky ve stadiu očkování { #data-elements-in-the-vaccination-stage }

| Datový prvek (název formuláře) | Spojeno s indikátory | Propojeno s certifikáty | Souvisí s pravidly programu |
| --- | --- | --- | --- |
| Dávka podaná v (datum očkování) Není datový prvek | Ano | Ano | Ano |
| Je pacientka těhotná nebo kojící? | Ne | Ne | Ano |
| Těhotenství (týdny) | Ne | Ne | Ano |
| Jakékoli základní zdravotní podmínky? | Ne | Ne | Ano |
| Kardiovaskulární onemocnění, včetně hypertenze | Ne | Ne | Ano |
| Chronická plicní nemoc | Ne | Ne | Ano |
| Diabetes | Ne | Ne | Ano |
| Imunodeficience | Ne | Ne | Ano |
| Malignity | Ne | Ne | Ano |
| Chronické neurologické nebo neuromuskulární onemocnění | Ne | Ne | Ano |
| Nemoc ledvin | Ne | Ne | Ano |
| Ostatní (upřesněte) | Ne | Ne | Ano |
| Byl pacient infikován COVID-19 za posledních 90 dnů? | Ne | Ne | Ano |
| Měl pacient po podání první dávky vakcíny závažnou alergickou reakci (anafylaxi) nebo okamžitou alergickou reakci - i když nebyla závažná? | Ne | Ne | Ano |
| Vakcína podána | Ano | Ano | Ano |
| Název vakcíny | Ano | Ano | Ano |
| Vysvětlete, proč tomuto klientovi byly podány dávky různých produktů | Ne | Ne | Ano |
| Číslo / šarže vakcíny | Ne | Ano | Ne |
| Datum expirace vakcíny | Ne | Ne | Ne |
| Číslo dávky | Ano | Ano | Ano |
| Celkové dávky potřebné pro tento očkovací přípravek | Ne | Ano | Ano |
| Je to poslední dávka? | Ano | Ne | Ano |
| COVAC Navrhované datum pro další dávku | Ne | Ne | Ano |
| „Měl klient po imunizaci nějakou nežádoucí reakci? | Ne | Ne | Ano |

### Vakcinační produkty v programu { #vaccine-products-in-the-program }

Konkrétní produkty COVID-19 dostupné v dané zemi a očkovací schémata se budou v jednotlivých zemích lišit. Tento balíček obsahuje očkovací produkty podle dokumentace dostupné od WHO, která se bude nadále vyvíjet, jak [vakcíny vstoupí na trh.](https://extranet.who.int/pqweb/sites/default/files/documents/Status_COVID_VAX_16Feb2021.pdf)

Aby bylo možné lépe demonstrovat funkčnost, byly tyto zástupné symboly nakonfigurovány na základě pěti stávajících očkovacích produktů, ale je důležité ověřit a nakonfigurovat program na základě národních směrnic pro přijetí produktu.

| Vakcína NÁZEV | Volitelný kód | Výrobce vakcín | Volitelný kód | Věkové doporučení | Interval dávky | Počet dávek |
| --- | --- | --- | --- | --- | --- | --- |
| AZD1222 / AstraZeneca | astrazeneca | AstraZeneca | astrazeneca | 18 | 10 dní (8-12) | 2 |
| AZD1222 / AstraZeneca | astrazeneca | SKBio Astra Zeneca | skbioastrazeneca | 18 | 10 (8-12) | 2 |
| BNT162b2 / COMIRNATY Tozinameran (INN) / BioNTech/Pfizer | biontechpfizer | BioNtech/Pfizer | biontechpfizer | 16 | 21 | 2 |
| mRNA-1273 / Moderna | moderna | Moderna | moderna | 18 | 28 | 2 |
| Sputnik V / Gamaleya | gamaleya | Gamaleya | gamaleya | 18 | 21 | 2 |
| SARS-CoV-2 Vaccine (VeroCell), Inactivated / Sinopharm | sinopharm | Sinopharm | sinopharm | 18 | 21 dní (21-28) | 2 |

### Jak přizpůsobit zástupné symboly dostupným očkovacím produktům? { #how-to-adapt-the-placeholders-to-the-available-vaccine-products }

#### Názvy ve formuláři { #names-in-the-form }

Aby název ve formuláři odpovídal produktům používaným v dané zemi, musíte nejprve upravit sady možností „Výrobci vakcín COVAC“ a „Název vakcíny COVAC“ a změnit možnosti na názvy podle toho, co je pro danou zemi vhodné.

![Sada možností](resources/images/Covac_optionset_1.png)

![Sada možností](resources/images/Covac_optionset_2.png)

#### Automatické přidělování výrobců a značek názvům { #auto-assigning-manufacturers-and-brands-to-names }

Výrobci a značky jsou automaticky přiřazeny, když je produkt vakcíny vybrán prostřednictvím pravidel programu na základě zvolené vakcíny, pokud vakcína nemá k dispozici více než jednoho výrobce, v takovém případě programové pravidlo skryje možnosti, které nejsou relevantní, a úředník bude nutné zvolit správný název výrobce, jako je tomu v případě AstraZeneca.

##### Pravidlo Automatického přiřazení { #auto-assign-rule }

Například pravidlo programu „Přiřadit značku a výrobce k BioNtech/Pfizer“ přiřadí výrobce BioNtech/Pfizer, když je vybráno „Comirnaty, Tozinaran“.

Používá výraz: `d2:hasValue( 'Vaccine_type' ) == true && #{Vaccine_type} == 'BIONTECHPFIZER'`

A akcí tohoto programového pravidla je přiřadit hodnotu datovému prvku „Výrobce vakcíny“ jako „BIONTTECHPFIZER“, což je volitelný kód pro „BioNtech/Pfizer“ a také „BioTech/Pfizer“ pro značku.

##### Pravidlo Skrýt možnosti { #hide-options-rule }

V současnosti platí jediné pravidlo, jako je toto: „Přiřadit možnosti značky/skrýt AstraZeneca“, protože tento produkt má dva různé výrobce (AstraZeneca a SK Bio Astra Zeneca).
To znamená, že místo určení výrobce skryje PR nerelevantní výrobce a umožní úředníkovi vybrat jednoho ze dvou aktuálně dostupných výrobců.

#### Upozornění na věk { #age-alert }

V závislosti na vakcíně mohou existovat nižší věkové hranice. „Pokud očkovací látka podá dávku někomu mimo doporučené věkové rozmezí, vydá se varování. Chcete -li to změnit, změňte prosím pravidla programu:

"Pokud je věk mladší 18 let, varujte, že Astra Zeneca se doporučuje pro osoby starší 18 let."

"Pokud je věk mladší 16 let, varuje, že BiontechPfizer je doporučen pro věk 16 a více." "Pokud je věk mladší 18 let, pak varuje, že je doporučen Moderna pro osoby starší 18 let." "Pokud je věk mladší 18 let, varuje, že Gamaleya je doporučeno pro věk 18 a více “„ Pokud je věk mladší 18 let, varuje, že Sinopharm je doporučen pro věk 18 a více “

Všechna pravidla používají podobný výraz:

`(#{Age_Calculated} < 18 ) && (#{Vaccine_type} =='ASTRAZENECA')`

Kde byste potřebovali upravit číslo, v tomto případě 18, aby odpovídalo potřebnému věku.

Účelem těchto programových pravidel je ukázat varování: „Tento očkovací přípravek je doporučen osobám starším 18 let.“

Toto varování byste měli také upravit tak, aby odpovídalo nejvhodnějším národním směrnicím.

#### Přiřaďte datum pro další dávku { #assign-a-date-for-next-dose }

V současné době neexistuje způsob, jak by tracker mohl přiřadit datum další události na základě datového prvku, takže to, co jsme udělali, je nakonfigurováno, aby tracker automaticky naplánoval další datum očkování 10 dní od první dávky za předpokladu, že nejpoužívanější produkt bude Astra-zeneca. Toto musí být upraveno tak, aby odpovídalo intervalu používanému v zemi změnou nastavení pro fázi programu očkování v aplikaci pro údržbu.

![Nastavení programu](resources/images/Covac_date_setting.png)

Kromě toho existuje také datový prvek, který pomocí pravidel programu automaticky přiřadí doporučené datum v závislosti na očkovacím produktu. Abyste to mohli změnit, je třeba upravit pravidlo programu:

„Přiřaďte navrhované datum pro další dávku AstraZeneca“ (pro každý produkt existuje jedno pravidlo) „.../dhis-web-maintenance/#/edit/programSection/programRule/ZT3tLrXXadf“

Pravidlo programu má dvě akce

Akce jedna: Zobrazit upozornění vedle datového prvku „navrhované datum další dávky“ s textem „Další dávka by měla být podána po 10 dnech“

Upravte tento text tak, aby odpovídal potřebám.

Akce dvě: Přiřaďte hodnotu datovému prvku „navrhované datum pro další dávku“ pomocí výrazu d2:addDays( V{event_date}, 10 )

Upravte číslo 10 počtem dní, které je třeba přiřadit dostupné vakcíně.

#### Poslední dávka { #last-dose }

V současné době existuje datový prvek ano/ne nazvaný „Poslední dávka“, tento prvek se používá k tomu, aby indikátory věděly, kdy produkt dokončil svůj imunizační plán. V současné době mají všechny produkty dvě dávky, a proto jsme to nastavili tak, že jakmile je člověku podána druhá dávka, DE „Poslední dávka“ se automaticky zaškrtne jako „Ano“. Toto DE jsme také schovali pro první dávku.

Chcete-li toto varování upravit, upravte pravidlo programu: „Pokud se jedná o druhou dávku, označte ji jako „poslední dávku“ pro všechny očkovací přípravky“

dhis-web-maintenance/#/edit/programSection/programRule/PJjKiFrvfuN

Výraz: `d2:hasValue( 'Číslo_dávky' ) == true && #{Dose_number} == 'DÁVKA2'`

označuje, že pokud úředník zvolí, že uvedené číslo dávek je druhou dávkou, spustí akci „přiřadit hodnotu“, která přidá hodnotu „pravda“ k datovému prvku „Poslední dávka“ a k proměnné programového pravidla „Poslední_dávka“

Chcete -li to změnit, upravte výraz a odfiltrujte vakcinační produkty, které se nepoužívají/s jiným plánem.

#### Celkový počet dávek { #total-number-of-doses }

Datový prvek „Celkové dávky požadované pro tento očkovací přípravek“ je automaticky vyplněný datový prvek, který zobrazuje množství dávek požadovaných pro očkovací schéma tohoto očkovacího přípravku. V současné době mají všechny vakcíny ve svém schématu dvě dávky. Pro každou vakcínu však existuje individuální pravidlo pro případ, že by se to v budoucnu změnilo:

Chcete -li upravit, upravte odpovídající pravidlo: Přiřaďte číslo dávky přípravku NAMEOFPRODUCT

A výraz: `d2:hasValue( 'Vaccine_type' ) == true && #{Vaccine_type} == 'astrazeneca'`

Pokud program odpovídá filtru, akce přiřadí hodnotu datovému prvku „Celkové dávky“. V současné době všechna pravidla přiřazují hodnotu „2“ a skrývají možnost pro třetí dávku.

#### Úroveň přístupu { #access-level }

Program byl nastaven jako „chráněný“ program, což znamená, že uživatelé mohou vyhledávat v jiných organizačních jednotkách kromě těch, ke kterým mají práva, ale pokud chtějí získat přístup k záznamům v jiném zařízení, musí použít „rozbít sklo“ a ne dolů, proč přistupují k záznamům v jiné organizační jednotce.

Upozorňujeme, že [funkce rozbití skla není v systému Android podporována](https://docs.dhis2.org/2.35/en/dhis2_android_capture_app/programs.html#breaking-the-glass) a uživatelé systému Android nemohou vyhledávat v jiné organizaci jednotky, když je program nastaven jako chráněný.

#### Detaily zápisu { #enrollment-details }

Datum zápisu se rovná „datu registrace“. Záměrem je, aby uživatel zadal datum zápisu, když je osoba zapsána do programu Immunization Registry. Ve většině případů se datum zápisu shoduje s datem prvního očkování, pokud klienti nejsou předem zapsáni v registru očkování.

Protože program používá datum narození k výpočtu ukazatelů programu, je nakonfigurováno jako povinné. Pokud osoba nezná své datum narození, lze použít zaškrtávací políčko „Datum narození je odhadnuto“ a zadat její přibližný věk nebo přibližné datum narození.

Zatímco informace o registraci mají být vyplněny při první registraci případu, hodnoty atributů lze aktualizovat kdykoli během aktivní registrace, pokud jsou k dispozici nové informace (např. kontaktní informace).

#### Identifikátory { #identifiers }

Program je konfigurován se dvěma typy jedinečných identifikátorů. Do programu lze přidat další identifikátory na základě kontextu země.

**Unikátní Identifikátor**: Automaticky generované ID, které je jedinečné pro celý systém (např. použitá instance DHIS2). Tento atribut TEI je nakonfigurován tak, aby generoval hodnotu atributu na základě vzoru. V předchozí verzi balíčku jedinečný identifikátor vygeneroval číslo, které bylo předponou a náhodným znakem, "EPI*" + RANDOM(########)". Nejnovější verze nahradila tento atribut jedním sekvenční vzor, který pomáhá s výkonem pro velké implementace "EPI*" + RANDOM(########)".

**Národní ID**: Toto ID se aktuálně zadává ručně a mělo by být přizpůsobeno místním potřebám ověření.

![Fáze zápisu](resources/images/Covac_enrollment.png)

### Fáze programu 1: Očkování (opakovatelné) { #program-stage-1-vaccination-repeatable }

Oddíl 1.1 Základní podmínky.

![Základní podmínky](resources/images/Covac_underlying.png)

Základní podmínky zde uvedené jsou založeny na pokynech pro balíčky sledování případů COVID a sledování kontaktů a zahrnují také zdravotní stavy, jako je těhotenství a kojení. Možnosti březosti a laktace se objevují pouze u žen. Jakmile je vybrána jedna ze základních podmínek (kromě těhotenství), zůstanou vybrané v následující fázi (protože se jedná o opakovatelnou fázi) a budou uvedeny v rámečku indikátorů.

#### Část 1.2 Předimunizační otázky { #section-12-pre-immunization-questions }

Předimunizační otázky mají být vyplněny během každé „události“, která představuje službu imunizace. Na základě vybraných odpovědí se spouštějí pravidla programu, která poskytují podporu při rozhodování

V současné době jsou tyto dvě otázky:

„Byl pacient infikován COVID-19 během posledních 90 dnů“

Pokud je odpověď ano, objeví se varování: Vakcína je doporučena pro osoby, které jsou prosté infekce COVID-19 po dobu alespoň 90 dnů““

A

„Měl pacient závažnou alergickou reakci (anafylaxe) nebo okamžitou alergickou reakci – i když nebyla závažná – po podání první dávky vakcíny“, která je viditelná pouze pro pacienty, když dostávají druhou (nebo potenciálně , třetí nebo posilovací) dávky. Pokud zvolíte ano, spustí se varování „Dodržujte prosím národní směrnice pro vyšetřování AEFI“

![Předimunizační otázky](resources/images/Covac_preimmunization.png)

#### Část 1.3 Informace o očkování { #section-13-vaccination-information }

Tato část zachycuje poskytované imunizační služby. Zaznamenává:

Podaná vakcína (pomocí sady možností „Název vakcíny“)

Výrobci vakcín (pomocí sady možností „Výrobci vakcín“, automaticky vyplněno)

Značka vakcíny (pomocí sady možností „Značka vakcíny“

Číslo šarže pro tuto dávku

Datum expirace dávky

Číslo dávky (1., 2. nebo posilovací dávka)

Počet celkových dávek požadovaných pro tento vakcínový produkt (automaticky vyplněno)

Datový prvek pro potvrzení, zda se jedná o poslední dávku v léčbě (automaticky vyplněné)

Automaticky vypočítaný datový prvek poskytující návrh na další dávku (automaticky vyplněno)

Datový prvek s dotazem, zda měl klient po očkování nežádoucí reakci (používá se při sledování pacienta bezprostředně po očkování)

Datový prvek pro dokončení identifikace zdravotnického pracovníka

![Sekce očkování](resources/images/Covac_vaccination.png)

Pokud je pacientovi podán jiný typ vakcíny než ten, který byl zaznamenán při prvním očkování, zobrazí se varování: „Typ vakcíny, který jste vybrali, není stejný jako předchozí typ vakcíny, který tato osoba dostala. Poslední, co byly podány, bylo 'NÁZEV PŘEDCHOZÍ PODANÉ VAKCÍNY'“ To také spouští další datový prvek „Vysvětlete prosím, proč byly tomuto klientovi podány dávky různých produktů“

Jakmile klient obdrží první dávku, možnost pro první dávku je v datovém prvku skryta. U produktů, které mají v rozpisu pouze dvě dávky, je třetí skryta. Země si to mohou nakonfigurovat v závislosti na očkovacích produktech, které budou přijímat.

#### Plánování událostí { #scheduling-events }

Fáze je nakonfigurována tak, aby ‚Požádejte uživatele o vytvoření nové události, když je fáze dokončena‘, což spustí vyskakovací okno pro naplánování následné schůzky. „Standardní intervalové dny“ jsou aktuálně nastaveny na 10, takže datum příští schůzky (události) je ve výchozím nastavení naplánováno 10 dní od aktuálního data události, ale lze je upravit v závislosti na použitém produktu.

### Skupiny uživatelů { #user-groups }

Program je zabalen společně se čtyřmi skupinami uživatelů:

-   _COVAC - Covid Immunization Metadata Admin:_ Má právo upravovat metadata balíčku, ale nezadávat data do balíčku
-   _COVAC - Covid Immunization Data Entry:_ Má práva vkládat data do trackeru
-   _COVAC - Covid Immunization Data Analysis:_ Má přístup k ovládacím panelům, ale nemůže zadávat data.
-   _COVAC - Covid-19 Immunization data Admin:_ Toto je skupina správců, kterou sdílí trasovač a agregát. Členové této skupiny mohou prohlížet data v modulu sledování i agregace a zaznamenávat data pouze v agregačním modulu. Tato uživatelská skupina je nastavena pro uživatele, kteří by spouštěli trasovač pro agregaci skriptů a také pro přístup k datové sadě prostřednictvím aplikace pro zadávání dat.

Ty by měly být přizpůsobeny vnitrostátním potřebám.

## Tisk certifikátu { #certificate-printing }

DHIS2 nepodporuje tisk očkovacího certifikátu nebo generování elektronického certifikátu jako základní funkcionalitu, ale několik zemí úspěšně přizpůsobilo platformu tak, aby poskytovala digitální a tištěné certifikáty.

### Upozornění SMS { #sms-notifications }

DHIS2 má modul SMS upozornění, ale pro použití upozornění a SMS brány je třeba nakonfigurovat. Viz dokumentaci k sms branám [zde](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/sms.html)

Program obsahuje výchozí připomenutí 7 dní před plánovaným datem pro očkovací akci:

“Vážený JMÉNO KLIENTA, máte schůzku k odběru vakcíny proti COVID-19 v TERMÍNU  na adrese NÁZEV ZAŔÍZENÍ

A zpráva 3 dny po plánovaném termínu:

„Vážený A{TfdH5KvFmMy}, vaše schůzka pro dávku vakcíny COVID-19 byla na V{due_date}, pokud jste vakcínu nedostali, kontaktujte prosím co nejdříve V{org_unit_name}. Pokud jste dostali vakcínu, ignorujte prosím tuto zprávu“

**POZNÁMKA:** Vzhledem k aktuálním omezením modulu SMS bude zpráva naplánovaná tři dny po termínu odeslána bez ohledu na to, zda k události došlo či nikoliv. Dokud nebude tento problém vyřešen, řešením je nakonfigurovat skript cronjob, který zkontroluje zpožděné události a naplánuje zprávu.

### Pracovní seznamy { #working-lists }

V programu byly nakonfigurovány tři vlastní pracovní seznamy. Tyto seznamy mají usnadnit správu pracovního dne zdravotnických pracovníků v místě péče se seznamy klientů v závislosti na jejich očkovacím kalendáři a upozornit na zpožděné termíny.

Seznamy jsou přizpůsobeny na základě funkce „datum splatnosti“. Datum splatnosti je datum, které je přiřazeno pro další událost a je provedeno, jakmile je dokončena první událost. V současné době systém automaticky vybere termín 10 dní po prvním očkování a úředník nebo lékař by měl toto datum v případě potřeby upravit. Je proto důležité, aby bylo plánování provedeno správně, aby bylo možné používat pracovní seznamy.

Všichni aktivní registrovaní klienti: Klienti, kteří jsou registrováni ve vakcinačním programu COVID, a klienti, jejichž registrace nebyla dokončena. Předpokládá se, že klienti, kteří dostali všechny dávky svých vakcín, budou mít za sebou zařazení do očkovacího programu. Neúplný zápis bude tedy indikovat všechny klienty, kteří nedostali druhou dávku (nebo poslední dávku u vakcín s odlišným schématem) – nezávisle na tom, zda jsou podle plánu nebo po termínu.

Klienti s naplánovanými schůzkami: Ti, kteří mají fázi očkovacího programu naplánovanou do budoucího nebo aktuálního dne

Klienti po platnosti očkovací dávky: Ti, kteří mají domluvenou schůzku v minulosti, a jsou tedy po datu platnosti, aby dostali očkovací dávku.

Dokončení klienti: Ti, jejichž registrace byla dokončena

## Analytika { #analytics }

Pro optimalizaci výkonu pro očekávaná rozsáhlá nasazení a použití strategií administrace vakcín ve stylu velkoobjemových kampaní je tento balíček navržen tak, aby sloužil analytickým objektům a ovládacím panelům prostřednictvím agregovaného datového modelu.

Kromě zajištění maximálního výkonu pro analytické uživatele, kteří přistupují k ovládacím panelům téměř v reálném čase, zatímco objemné zadávání dat prostřednictvím nástroje Tracker pravděpodobně probíhá, má agregace dat sledování a poskytování ovládacích panelů prostřednictvím agregované domény další výhodu zpřístupnění datových dimenzí pro uživatelé analýzy (např. na základě kategorií pro rozčlenění).

Aby bylo možné poskytovat analýzy COVID-19 ze zdrojových dat trasovacího programu COVID-19 EIR, balíček obsahuje následující součásti: Soubor souhrnných dat s datovými prvky a kombinacemi kategorií (které slouží jako cíl pro předávání dat sledování do agregovaného modelu) Ovládací panel založený na agregovaných doménových indikátorech (nahrazuje ovládací panel založený na trackeru (na základě indikátorů programu) v předchozích verzích) Skupina indikátorů programu s atributy mapovanými na cílové agregované DE/COC

### Ovládací panel { #dashboard }

Tento balíček obsahuje zjednodušený panel COVAC Daily Monitoring Dashboard (iBWlFCvvtkH), který usnadňuje každodenní analýzu téměř v reálném čase během činností s dodávkami vakcín ve stylu kampaně. Tento ovládací panel je navržen tak, aby byl co nejlehčí a sloužil základní sadě metrik optimalizovaných pro každodenní monitorování operací s dodávkami vakcín. Indikátory ovládacího panelu byly vybrány jako podmnožina pokynů pro monitorování obsažených v pokynech WHO k vývoji národního plánu nasazení a očkování pro vakcíny COVID-19. [Pokyny WHO k vývoji národního plánu nasazení a očkování pro vakcíny COVID-19](https://www.who.int/publications/i/item/WHO-2019-nCoV-Vaccine_deployment-2020.1). „COVAC Daily Monitoring Dashboard“ ((iBWlFCvvtkH) je nakonfigurován výhradně na základě indikátorů patřících do skupiny indikátorů COVAC – Daily (doQTIS8KJQH). To zemím umožní mapovat indikátory ovládacího panelu na jejich vlastní sadu základních datových prvků, pokud cílový souhrn datová sada a datové prvky jsou přizpůsobeny pro místní implementaci.

Úplný ovládací panel monitorování zahrnující další aspekty pokynů WHO pro monitorování NDVP (jako je pokrytí vakcínami a absorpce cílovými skupinami, ukazatele nežádoucích účinků, dodavatelský a chladící řetězec) naleznete v [COVAC Core Dashboard/Aggregate metadata package](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-aggregate/version-110/design.html).

Pokud vaše instance již má ovládací panel z předchozí verze tohoto balíčku, doporučuje se jej odstranit nebo omezit přístup k němu na několik uživatelů. Pokyny k odstranění ovládacích panelů naleznete v [instalační příručce](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-immunization-registry-tracker/installation.html)

### Soubor souhrnných dat { #aggregate-data-set }

Agregovaná datová sada „COVAC - EIR sledovací data (agregovaná)“ byla nakonfigurována s denní frekvencí jako cíl pro posouvání hodnot dat vypočítaných na základě indikátorů trasovacího programu do agregované domény. Datová sada obsahuje následující datové prvky:

1. Lidé s 1. dávkou
2. Lidé s 2., 3. nebo posilovací dávkou
3. Lidé s poslední doporučenou dávkou
4. Lidé se základními zdravotními podmínkami

![Zadávání souhrnných dat](resources/images/covac_agg_data_entry.png)

Kde to bylo možné, byly kombinace kategorií, kategorie (a jejich přidružené Kombinace možností kategorií a Možnosti kategorií) znovu použity ze stávajícího [COVAC Core Dashboard/Aggregate metadata package](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-aggregate/version-110/design.html) pro usnadnění analýzy napříč datovými prvky z těchto dvou balíčků.

Očekává se, že tyto datové prvky a COC budou naplněny z indikátorů trasovacího programu, jak je popsáno níže.

### Programové Indikátory { #program-indicators }

Skupina programových indikátorů, COVAC-Tracker k agregaci (NXBR4r6MwAO) byla nakonfigurována a namapována (prostřednictvím atributů), aby se usnadnilo přenášení datových hodnot do přidružených cílových agregovaných datových prvků a COC, jak je popsáno výše. Příklad tohoto mapování je následující:

| Indikátor programu (název) | UID indikátoru programu | Odesláno do Aggregate DE (název) | Agregát DE UID | Mapováno na indikátor (název) | UID indikátoru |
| --- | --- | --- | --- | --- | --- |
| Počet lidí, kteří dostali první dávku (ženy 0-59) | RJ6pdxga9Od | COVAC- Lidé s 1. dávkou | RjT7dmzunF4 | COVAC - Lidé s 1. dávkou | GeAtojrj7Yy |
| Počet lidí, kteří dostali první dávku (ženy 60+) | x4L0LuEBHhW | COVAC- Lidé s 1. dávkou | RjT7dmzunF5 | COVAC - Lidé s 1. dávkou | GeAtojrj7Yy |
| Počet lidí, kteří dostali první dávku (muži 0-59) | hqm8znlAzkT | COVAC- Lidé s 1. dávkou | RjT7dmzunF6 | COVAC - Lidé s 1. dávkou | GeAtojrj7Yy |
| Počet lidí, kteří dostali první dávku (muži 60+) | aIIHyDy8AMW | COVAC- Lidé s 1. dávkou | RjT7dmzunF7 | COVAC - Lidé s 1. dávkou | GeAtojrj7Yy |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (ženy 0-59) | xY4T9hHXNji | COVAC - Lidé s 2., 3. nebo posilovací dávkou | zmKNuqgsq8N | COVAC - Lidé s 2., 3. nebo posilovací dávkou | ddZjJCwXf6k |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (ženy 60+) | h9G7i6mQKef | COVAC - Lidé s 2., 3. nebo posilovací dávkou | zmKNuqgsq8N | COVAC - Lidé s 2., 3. nebo posilovací dávkou | ddZjJCwXf6k |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (muži 0-59) | MGjwUUNsE60 | COVAC - Lidé s 2., 3. nebo posilovací dávkou | zmKNuqgsq8N | COVAC - Lidé s 2., 3. nebo posilovací dávkou | ddZjJCwXf6k |
| Počet lidí, kteří dostanou druhou, třetí nebo posilovací dávku (muži 60+) | qh0kIjHZbP8 | COVAC - Lidé s 2., 3. nebo posilovací dávkou | zmKNuqgsq8N | COVAC - Lidé s 2., 3. nebo posilovací dávkou | ddZjJCwXf6k |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového přípravku (ženy 0-59) | Zp39TSOR8eW | COVAC - Lidé s poslední doporučenou dávkou | CB46jykiEye | COVAC - Lidé s poslední doporučenou dávkou | OAZXVEjEEoD |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (ženy 60+) | XFUvVgqPukT | COVAC - Lidé s poslední doporučenou dávkou | CB46jykiEye | COVAC - Lidé s poslední doporučenou dávkou | OAZXVEjEEoD |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (muži 0-59) | FZNIlzPRMmL | COVAC - Lidé s poslední doporučenou dávkou | CB46jykiEye | COVAC - Lidé s poslední doporučenou dávkou | OAZXVEjEEoD |
| Počet lidí, kteří dostali poslední doporučenou dávku příslušného vakcínového produktu (muži 60+) | zovL7DKBRuK | COVAC - Lidé s poslední doporučenou dávkou | CB46jykiEye | COVAC - Lidé s poslední doporučenou dávkou | OAZXVEjEEoD |
| Lidé se základními zdravotními podmínkami | Zn0UuSRYyJw | COVAC - Lidé se základními onemocněními | OUI05zSKrqk | COVAC - Lidé se základními onemocněními | KIgI3EPjs2T |

Další programové indikátory byly nakonfigurovány tak, aby umožňovaly ad hoc analýzu samotných dat trackeru (např. míry pokrytí vypočítané na základě dat trackeru atd.). Tyto programové indikátory se však nepoužívají v řídicím panelu COVAC - Daily Monitoring.

## Přenos agregovaných dat z domény trasování na hodnoty souhrnných dat domény { #transferring-aggregated-tracker-domain-data-to-aggregate-domain-data-values }

Kromě výše uvedených metadat budou implementace vyžadovat mechanismus, který posune hodnoty indikátorů programu z domény sledování do cílové sady souhrnných dat. Více informací o tomto lze nalézt v této kapitole Příručky pro implementaci DHIS2: [Integrating Tracker and Aggregate Data](https://docs.dhis2.org/en/implement/maintenance-and-use/tracker-and-aggregate-data-integration.html#how-to-saving-aggregated-tracker-data-as-aggregate-data-values)

## Pokyny pro implementaci se zařízeními Android { #considerations-for-when-implementing-with-android-devices }

### Úroveň přístupu „chráněno“ { #access-level-protected }

Funkce „rozbití skla“ zatím není v aplikaci DHIS2 Android Capture od verze 2.3 podporována. Pokud je program nakonfigurován jako „Chráněný“, výchozí chování pro Android bude stejné, jako když je program nakonfigurován jako „Uzavřený.“ To znamená, že uživatel Androidu nebude moci číst ani upravovat zápisy TEI mimo jejich organizační jednotka. TEI registrované ve vyhledávací OU budou vráceny vyhledáváním typu TE, ale pokud je program uzavřen nebo chráněn, uživatel nebude moci zobrazit nebo vytvořit novou registraci. Pokud uživatelé systému Android musí mít přístup k TEI mimo svou organizační jednotku pro sběr dat, program by měl být nakonfigurován s úrovní přístupu „Otevřený“. Sledujte stav tohoto problému na [Jira](https://jira.dhis2.org/browse/ANDROAPP-657)

### Datum platnosti dávky { #dose-due-date }

Popis termínu platnosti se na androidu nezobrazuje správně a místo „Datum platnosti dávky“ je uvedeno „Datum platnosti“ [Odkaz na jira](https://jira.dhis2.org/browse/ANDROAPP-3620)

### Rezervní ID { #reserve-ids }

Jedinečný identifikátor pro tento balíček je vygenerován automaticky a používá vzor "CURRENT_DATE(yyyy-MM-dd)-"-"-SEQUENTIAL(#####)". U zařízení Android jsou hodnoty pro tato systémem generovaná UID rezervovány předem pro každé zařízení, aby bylo zajištěno, že hodnoty jsou jedinečné pro celou instanci. To znamená, že hodnota data a pořadového čísla nebude nutně odpovídat dnešnímu datu a chronologickému pořadí, kdy pacient vakcínu dostane. Více informací o tomto naleznete [zde](https://docs.dhis2.org/en/implement/implementing-with-android/dhis2-configuration-for-android.html#configuration_reserved_id)
