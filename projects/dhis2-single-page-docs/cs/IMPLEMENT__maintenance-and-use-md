---
revision_date: "2021-09-15"
template: single.html
---

# Uživatelé a uživatelské role { #users-and-user-roles }

## O správě uživatelů { #about_user_userrole }

Více uživatelů může přistupovat k DHIS2 současně a každý uživatel může mít různá oprávnění. Tato oprávnění můžete doladit tak, aby určití uživatelé mohli zadávat pouze data, zatímco ostatní mohli generovat pouze zprávy.

- Můžete vytvořit tolik uživatelů, uživatelských rolí a skupin uživatelů, kolik potřebujete.

- Můžete přiřadit konkrétní oprávnění skupinám uživatelů nebo jednotlivým uživatelům prostřednictvím rolí uživatelů.

- Můžete vytvořit více uživatelských rolí, z nichž každá má svá vlastní oprávnění.

- Uživatelům můžete přiřadit uživatelské role a udělit jim příslušná oprávnění.

- Každého uživatele můžete přiřadit k organizačním jednotkám. Poté může uživatel zadat data pro přiřazené organizační jednotky.

Tabulka: Termíny a definice správy uživatelů

| Období | Definice | Příklad |
| --- | --- | --- |
| Autorita | Povolení provádět jeden nebo několik konkrétních úkolů | Vytvořit nový datový prvek <br> <br> Aktualizovat organizační jednotku <br> <br> Zobrazit sestavu |
| Uživatel | Uživatelský účet DHIS2 osoby | admin <br> <br> traore <br> <br> host |
| Uživatelská role | Skupina autorit | Referent pro zadávání dat <br> <br> Správce systému <br> <br> Přístup k programu předporodní péče |
| Uživatelská skupina | Skupina uživatelů | Zaměstnanci Keni <br> <br> Příjemci zpětné vazby <br> <br> Koordinátoři programu HIV |

V aplikaci **Uživatelé** spravujete uživatele, uživatelské role a skupiny uživatelů.

Tabulka: Objekty v aplikaci Uživatelé

| Typ objektu | Dostupné funkce |
| --- | --- |
| Uživatel | Vytvářet, upravovat, zvát, klonovat, deaktivovat, zobrazovat podle organizační jednotky, mazat a zobrazovat podrobnosti |
| Uživatelská role | Vytvářet, upravovat, sdílet, mazat a zobrazovat podrobnosti |
| Uživatelská skupina | Vytvářet, upravovat, připojit se, opouštět, sdílet, mazat a zobrazovat podrobnosti |

### O uživatelích { #about-users }

Každý uživatel v DHIS2 musí mít uživatelský účet, který je identifikován uživatelským jménem. Měli byste zaregistrovat křestní jméno a příjmení každého uživatele a také kontaktní informace, například e-mailovou adresu a telefonní číslo.

Je důležité, abyste zaregistrovali správné kontaktní informace. DHIS2 používá tyto informace k přímému kontaktování uživatelů, například k odesílání e-mailů k upozornění uživatelů na důležité události. Kontaktní informace můžete také použít ke sdílení například ovládacích  panelů a kontingenčních tabulek.

Uživatel v DHIS2 je přidružen k organizační jednotce. Měli byste přiřadit organizační jednotku, kde uživatel pracuje.

Když vytvoříte uživatelský účet pro okresního správce záznamů , měli byste mu jako organizační jednotku přiřadit okres, kde pracuje.

Přiřazená organizační jednotka ovlivňuje, jak může uživatel používat DHIS2:

- V aplikaci **Zadávání dat** může uživatel zadat data pouze za organizační jednotku, ke které je přidružena, a za organizační jednotky pod hierarchií. Například okresní záznamník bude moci registrovat údaje pouze za svůj okres a zařízení pod tímto okresem.

- V aplikaci **Uživatelé** může uživatel vytvořit nové uživatele pouze pro organizační jednotku, ke které je přidružena, kromě organizačních jednotek pod hierarchií.

- V aplikaci **Zprávy** si uživatel může prohlížet pouze zprávy pro svou organizační jednotku a níže uvedené. (To je něco, co považujeme za otevřenou vlastnost, která umožní srovnávací zprávy.)

Důležitou součástí správy uživatelů je kontrola, kterým uživatelům je povoleno vytvářet nové uživatele, s kterými orgány. V DHIS2 můžete určit, kteří uživatelé mohou provádět tento úkol. Klíčovým principem je, že uživatel může udělit pouze oprávnění a přístup k souborům dat, ke kterým má přístup sám uživatel. Počet uživatelů na národní, krajské a okresní úrovni je často relativně malý a mohou je vytvářet a spravovat správci systému. Pokud velká část zařízení zadává data přímo do systému, může se počet uživatelů stát nepraktickým. Doporučuje se tento úkol delegovat a decentralizovat na okresní úředníky, zefektivní to proces a lépe podpoří uživatele zařízení.

### O uživatelských rolích { #about-user-roles }

Role uživatele v DHIS2 je skupina oprávnění. Oprávnění znamená oprávnění k provádění jednoho nebo více konkrétních úkolů.

Role uživatele může obsahovat oprávnění k vytvoření nového datového prvku, aktualizaci organizační jednotky nebo zobrazení sestavy.

Uživatel může mít více uživatelských rolí. Pokud ano, oprávnění uživatele budou součtem všech oprávnění a datových sad v rolích uživatelů. To znamená, že můžete uživatelské role kombinovat a porovnávat pro speciální účely místo vytváření pouze nových.

Role uživatele je přidružena ke kolekci datových sad. To ovlivňuje aplikaci **Data Entry**: uživatel může zadávat data pouze pro datové sady registrované pro jeho uživatelskou roli. To může být užitečné, když například chcete povolit příslušníkům zdravotnických programů zadávat údaje pouze pro své příslušné formuláře pro zadávání údajů.

Doporučení:

- Vytvořte jednu uživatelskou roli pro každou pozici v organizaci.

- Souběžně s definováním toho, který uživatel provádí jednotlivé úlohy v systému, vytvářejte uživatelské role.

- Poskytněte rolím uživatelů pouze přesná oprávnění, která potřebují k výkonu své práce, ne více. Oprávnění k provedení úkolu by měl mít pouze ten, kdo má úkol provést.

### O skupinách uživatelů { #about-user-groups }

Uživatelská skupina je skupina uživatelů. Skupiny uživatelů používáte, když nastavujete sdílení objektů nebo oznámení, například nabízené zprávy nebo oznámení programu.

Viz také: 

[Sdílení](https://ci.dhis2.org/docs/master/en/user/html/sharing.html)

[Spravovat oznámení programu](https://docs.dhis2.org/master/en/user/html/manage_program_notification.html)

[Spravovat nabízené zprávy push](https://docs.dhis2.org/master/en/user/html/manage_push_report.html)

## Pracovní postup { #user_mgt_workflow }

1.  Definujte pozice, které potřebujete pro svůj projekt, a určete, jaké úkoly budou různé pozice provádět.

2.  Pro každou pozici vytvořte zhruba jednu uživatelskou roli.

3.  Vytvářejte uživatele.

4.  Přiřaďte uživatelům uživatelské role.

5.  Přiřaďte uživatele k organizačním jednotkám.

6.  (Volitelné) Seskupte uživatele do skupin uživatelů.

7.  Sdílejte datové sady s uživateli nebo skupinami uživatelů prostřednictvím dialogu Sdílení v části Správa datových sad v aplikaci Údržba

> **Tip**
>
> Aby uživatelé mohli zadávat data, musíte je přidat na úrovni organizační jednotky a sdílet s nimi datovou sadu.

## Příklad: správa uživatelů ve zdravotním systému { #user_mgt_example }

V systému zdraví jsou uživatelé logicky seskupeni s ohledem na úkol, který vykonávají, a na pozici, kterou zaujímají.

1.  Definujte, kteří uživatelé by měli mít roli správce systému. Často jsou součástí národní divize HIS a měli by mít v systému plnou autoritu.

2.  Pro každou pozici vytvořte zhruba jednu uživatelskou roli.

Příklady běžných  pozic jsou:

| Pozice | Typické úkoly | Doporučené autority | Komentář |
| --- | --- | --- | --- |
| Správci systému | Nastavte základní strukturu (metadata) systému. | Přidejte, aktualizujte a odstraňte základní prvky systému, například datové prvky, ukazatele a datové soubory. | Metadata by měli upravovat pouze správci systému. <br> Pokud povolíte uživatelům mimo tým systémových administrátorů upravovat metadata, může to vést k problémům s koordinací. <br> <br> Aktualizace systému by měli provádět pouze správci systému. |
| Národní zdravotní manažeři <br> <br> Zdravotní manažeři provincie | Monitorujte a analyzujte data | Přístup k modulu přehledů, aplikacím **Mapy**, **Kvalita dat** a ovládacímu panelu. | Nepotřebujete přístup k zadávání dat, úpravě datových prvků nebo souborů dat. |
| Úředníci divize národního zdravotnického informačního systému (HISO) <br> <br> Okresní zdravotničtí pracovníci a informační důstojníci (DHRIO) <br> <br> Zdravotní záznamy a informační pracovníci zařízení (HRIO) | Zadejte data, která pocházejí ze zařízení, která toho nejsou schopna přímo <br> <br> Monitorujte, vyhodnocujte a analyzujte data | Přístup ke všem aplikacím pro analýzu a ověřování <br> <br> Přístup k aplikaci **Zadávání dat**. | - |
| Referenti pro zadávání dat | - | - | - |

# Pokyny pro offline zadávání dat pomocí DHIS 2 { #offline_data_entry }

<!--DHIS2-SECTION-ID:offline_data_entry-->

De facto standardní způsob nasazení DHIS 2 se stal _online_, což znamená, že na serveru připojeném k Internetu je nastavena jedna instance aplikace a všichni uživatelé se k aplikaci připojují pomocí webového prohlížeče přes internet. To bylo možné díky stálému zvyšování dostupnosti internetu (většinou mobilního internetu), nabídce snadno dostupných a levných cloudových výpočetních zdrojů v kombinaci se skutečností, že DHIS 2 nevyžaduje významnou šířku pásma. Tento vývoj umožňuje přístup k online serverům i ve venkovských oblastech pomocí mobilních internetových modemů (označovaných také jako dongly).

Tento styl nasazení online má obrovské pozitivní důsledky pro proces implementace a údržbu aplikace ve srovnání s tradičním samostatným stylem offline:

**Hardware**: Hardwarové požadavky na straně koncového uživatele jsou omezeny na přiměřeně moderní počítač / notebook a internet <!--Uveďte telefon, protože Android je uveden jako
alternativní? --> připojení prostřednictvím pevné linky nebo mobilního modemu. Není potřeba specializovaný server pro každého uživatele, postačí jakýkoli počítač s internetovým připojením. Pro online nasazení bude vyžadován server, ale protože existuje pouze jeden (nebo několik) serverů, které je třeba pořídit a udržovat, je to podstatně jednodušší (a levnější), než je údržba mnoha samostatných serverů v odlišných umístěních. Vzhledem k tomu, že cloudové výpočetní prostředky neustále stabilně snižují cenu a zároveň zvyšují výpočetní výkon, je nastavení výkonného serveru v cloudu mnohem levnější než nákup hardwaru.

**Softwarová platforma**: Koncoví uživatelé potřebují k připojení k on-line serveru pouze webový prohlížeč. Všechny dnes populární operační systémy jsou dodávány s webovým prohlížečem a neexistují žádné zvláštní požadavky na typ nebo verzi <!--Nejsem si jistý, zda je to pravda, alespoň v praxi -->. To znamená, že pokud dojde k vážným problémům, jako jsou virové infekce nebo poškození softwaru, můžete se vždy uchýlit k přeformátování a instalaci operačního systému počítače nebo k získání nového počítače / notebooku. Uživatel může pokračovat v zadávání dat tam, kde byl zastaven a žádná data nebudou ztracena.

**Softwarová aplikace**: Styl nasazení centrálního serveru znamená, že aplikaci lze upgradovat a udržovat centralizovaným způsobem. Když jsou vydány nové verze aplikací s novými funkcemi a opravami chyb, lze je nasadit na jediný online server. Všechny změny se poté projeví na straně klienta při příštím připojení koncových uživatelů přes internet. To má evidentně obrovský pozitivní dopad na proces zlepšování systému, protože nové funkce mohou být uživatelům distribuovány okamžitě, všichni uživatelé budou mít přístup ke stejné verzi aplikace a chyby a problémy bude možné vyřešit a nasadit za běhu <!-- Bugs can be deployed on-the-fly! --> .

**Údržba databáze**: Podobně jako v předchozím bodě lze změny metadat provádět na on-line serveru centralizovaným způsobem a automaticky se rozšíří na všechny klienty při příštím připojení k serveru. Tím se efektivně odstraní obrovské problémy související s udržováním upgradované a standardizované sady metadat související s tradičním stylem nasazení offline. Je to mimořádně výhodné například během počáteční fáze vývoje databáze a během ročních procesů revize databáze, protože koncoví uživatelé budou mít přístup ke konzistentní a standardizované databázi, i když ke změnám dochází často.

Ačkoli lze implementaci DHIS 2 označit jako online, stojí za zmínku, že takové nasazení nemusí být čistě online a může se jednat o místní variace v závislosti na místních omezeních. Například zatímco většina uživatelů v zemích má snadný přístup ke své národní instanci DHIS 2 pomocí svého mobilního internetu nebo lepší možnosti připojení <!-- Jiné? Opravené nemusí být lepší ... -->, někteří se bohužel stále potýkají s přístupem do systému buď pro zadávání dat, nebo pro analýzu na místech, kde je připojení k internetu nestabilní nebo chybí v dlouhých časových obdobích. A pro tyto uživatele, kteří se potýkají s problémy, je třeba najít alternativní způsoby interakce se systémem.

Cílem tohoto pokynu je poskytnout rady, jak zmírnit dopad nedostatku spolehlivého internetu v náročných podmínkách.

## Případy a odpovídající řešení { #offline_data_entry_cases }

<!--DHIS2-SECTION-ID:offline_data_entry_cases-->

V této části prozkoumáme možné náročné případy a popíšeme možné způsoby, jak je řešit nebo v krátkodobém horizontu minimalizovat jejich účinky na uživatele a celý systém. Je zřejmé, že možná řešení navrhovaná v těchto pokynech by měla být přizpůsobena v každém kontextu s přihlédnutím k mnoha dalším parametrům, jako je bezpečnost, místní postupy a pravidla atd. Účelem tohoto pokynu není předepisovat neprůstřelná řešení, která mohou fungovat všude, ale navrhnout způsoby řešení problémů s připojením na některých místech v zemi.

Identifikujeme tři (3) hlavní scénáře:

1. Omezená dostupnost internetu a formulářů pro zadávání údajů jsou malé
1. Omezená dostupnost internetu a formuláře pro zadávání údajů jsou obrovské
1. Internet není vůbec k dispozici

Uznáváme, že tyto scénáře jsou velmi zjednodušující, protože v praxi může mít zdravotnické zařízení například jeden malý týdenní formulář pro sledování nemocí, jeden velký formulář pro měsíční zprávu o pokroku a středně velký formulář pro zdravotní program. Díky tomu je počet možných scénářů pro dané nastavení větší než to, co je zde vysvětleno. Bude proto na každém implementačním týmu, aby diskutoval se zúčastněnými stranami o jednoduchých rozhodnutích, která budou řešit všechny scénáře v daném prostředí. Ve většině případů bude mít přibližně 80 až 95% okresů <!-- Máme pro to zdroj? --> (nebo zdravotnických zařízení, pokud se údaje zadávají na této úrovni) stejnou konfiguraci ohledně dostupnosti internetu a pouze zbývajících 5 až 20% bude potřebovat alternativní způsoby, jak získat svá data v DHIS 2.

### 1. Omezená dostupnost internetu (nestabilita signálu nebo omezená mobilní data) a formuláře pro zadávání dat jsou malé { #offline_data_entry_cases_small }

<!--DHIS2-SECTION-ID:offline_data_entry_cases_small-->

Omezenou dostupností internetu myslíme případ, kdy:

- Proveditelný, výkonný a robustní hardware.
- síť je dobrá, ale kolísá nebo je k dispozici pouze v daném období dne
- síťový signál je slabý, ale čas od času se zlepšuje, aby bylo možné připojení k DHIS 2

A pod malým formulářem pro zadávání dat máme na mysli formulář pro zadávání dat, který má méně než sto <!-- Kdybych uhodl, co to znamená „Malý“, řekl bych
10-20 --> polí.

Pokud je tedy připojení k internetu omezené a formuláře pro zadávání dat jsou malé, existují dvě možnosti řešení problému s připojením: aplikace pro sběr dat přes Android a možnost zadávání webových dat offline.

#### Použití aplikace pro sběr dat Android: { #use-of-android-data-capture-app }

<!-- Musíte se ujistit, že je to aktualizováno s vydáním nové
aplikace -->

Aplikace Data Capture pro DHIS 2 umožňuje uživatelům zadávat data na server DHIS 2 pomocí zařízení Android. Aplikace stáhne instance formulářů, které jsou vyžadovány k zadání dat ze serveru, a uloží je do zařízení. To znamená, že uživatelé mohou zadat data offline pro zařízení, ke kterým jsou přiřazeni, a poté je nahrát na server DHIS 2, když mají pokrytí sítě.

Za tímto účelem budou uživatelé požádáni o přechod na Google Play ze svého zařízení Android a zadání záznamu dat DHIS 2 a získání následující obrazovky.

Poté nainstalujte aplikaci s názvem **Sběr dat pro DHIS 2**.

![](resources/images/image5.png)

Jakmile je aplikace nainstalována a spuštěna, bude uživatel požádán o poskytnutí adresy URL svého národního DHIS 2, uživatelského jména a hesla a klepnutí na PŘIHLÁSIT se.

<table style="border:1px;">
<tr>
<td style="width:40%;padding: 5 20 5 20;border:1px;">

![](resources/images/offline_data_entry/image4.jpg)
</td>
<td style="width:40%;padding: 5 20 5 20;border:0px;">
</td>
</tr>
</table>

Po úspěšném přihlášení aplikace automaticky stáhne formuláře a organizační jednotky, ke kterým je uživatel přiřazen, a uloží je lokálně pro zadávání dat. Od této chvíle nebude jakékoli následné použití aplikace pro zadávání dat vyžadovat připojení k internetu, protože instance formulářů jsou již uloženy místně. Připojení k internetu bude potřeba pouze k synchronizaci dat se serverem. To lze provést, když je internet k dispozici místně.

<table style="border:0px;">
<tr>
<td style="width:40%;padding: 5 20 5 20 ;border:0px;">

![](resources/images/image9.jpg)

</td>
<td style="width:40%;padding: 5 20 5 20 ;border:0px;">

![](resources/images/image7.jpg)

</td>
</tr>
</table>

Na straně správy systému organizování formuláře pro zadávání dat do sekcí v DHIS 2 umožní plynulejší a příjemnější zážitek ze zadávání dat.

Pokud jde o synchronizaci, když není v případě potřeby k dispozici připojení k internetu, uživatel vezme mobilní zařízení do okresu - během schůzky v okresu - nebo do nejbližší oblasti, kde je k dispozici internet.

#### Využití možnosti offline modulu pro zadávání webových dat DHIS 2 v režimu offline { #use-of-the-offline-capability-of-dhis-2-web-data-entry-module }

Modul pro zadávání webových dat je modul uvnitř DHIS 2, který umožňuje zadávání dat pomocí webového prohlížeče. V DHIS 2 je běžný způsob zadávání dat online. Má však také schopnost „offline“, která podporuje pokračování zadávání dat, i když je internet přerušen. To znamená, že pokud chce uživatel okamžitě zadávat data na konci měsíce, musí se nejprve připojit k internetu, přihlásit se k DHIS 2 a otevřít formuláře pro zadávání dat alespoň pro jedno ze zařízení, ke kterým je přiřazen . Od tohoto kroku může odpojit internet a pokračovat v zadávání dat pro všechna svá zařízení a po dobu, kterou chce, pokud není ve webovém prohlížeči zavřeno okno webové stránky pro zadávání dat. Po dokončení zadávání dat může zavřít prohlížeč a vypnout počítač. Zadaná data budou uložena lokálně do mezipaměti prohlížeče a při příštím připojení online a přihlášení do DHIS 2 bude vyzván ke kliknutí na tlačítko pro jejich nahrání.

V tomto případě je možné použít buď aplikaci pro zadávání dat pro Android nebo částečně offline webovou funkci v DHIS 2 nebo obojí v závislosti na velikosti formulářů pro zadávání dat. <!-- Není jasné, na co odkazuje „V tomto případě“ --> Vymazání mezipaměti prohlížeče však povede ke ztrátě lokálně uložených dat. Proto se doporučuje nevymazat mezipaměť, aniž byste se ujistili, že jsou synchronizována data uložená místně.

Když je uživatel přihlášen a internet je přerušen (úmyslně nebo ne)

![](resources/images/image1.png) <!-- PALD: This screenshot was
taken when the home icon ()top left corner) was broken. I suggest we replace this image! -->

Když je internet zpět a uživatel se přihlásí k DHIS 2

![](resources/images/image6.png)

### 2. Omezená dostupnost internetu a formuláře pro zadávání údajů jsou obrovské { #offline_data_entry_cases_huge }

<!--DHIS2-SECTION-ID:offline_data_entry_cases_huge-->

<!-- Existuje ještě možnost zadávání dat PDF? Kde byste mohli vygenerovat formuláře pro zadávání dat založené na formátu PDF, které lze spravovat offline a poté je nahrát?-->

Když je internet, ale dostupnost je omezená, ale formulář pro zadávání dat obsahuje několik stovek polí, omezuje to možná řešení. V tomto případě se nedoporučuje používat Android capture ze dvou důvodů:

- může pravidelně havarovat, protože není navržen pro zpracování formulářů velmi velké velikosti <!-- Možná bychom tento bod mohli potlačit.. -->
- může to být pro uživatele zdlouhavé a vyčerpávající, protože obrazovka je malá a neumožňuje rychlé zadávání dat

Jedinou dostupnou možností je tedy použít výše popsanou offline funkci modulu pro zadávání dat na webu nebo se přesunout na nejbližší místo, kde je k dispozici internet, když si uživatel nemůže dovolit čekat, až bude v jeho oblasti k dispozici internet.

### 3. Internet není vůbec k dispozici { #offline_data_entry_cases_no_available }

<!--DHIS2-SECTION-ID:offline_data_entry_cases_no_available-->

V tomto případě existují tři možnosti:

- Použití aplikace Android Capture pro místní zadávání dat a synchronizaci dat na vyšší úrovni, kde je k dispozici internet, pokud se tam uživatel pravidelně účastní schůzek. To je možné pouze v případě, že formuláře jsou malé
- Přesuňte se na nejbližší místo (je-li dostupné) nebo využijte příležitost pravidelného setkání na vyšší úrovni a pořiďte data pomocí modulu pro zadávání webových dat. V takovém případě může uživatel v závislosti na připojení k internetu pracovat buď online, nebo použít funkci offline popsanou v části [výše](#offline_data_entry_cases_small).
- Zeptejte se na vyšší úrovni, kde je k dispozici internet, abyste zadávali data bez ohledu na velikost formuláře. Přestože k tomuto zadávání údajů dochází na vyšší úrovni, lze údaje stále zadávat pro každé zdravotnické zařízení.

<!-- Vypadá to přirozeně s nějakým závěrem nebo
shrnutí -->

# Přehled nástrojů pro analýzu dat { #data-analysis-tools-overview }

Tato kapitola nabízí přehled dostupných nástrojů pro analýzu dat poskytovaných serverem DHIS2 spolu s popisem účelu a výhod každého z nich. Pokud hledáte podrobného průvodce, jak používat jednotlivé nástroje, doporučujeme po dokončení této kapitoly pokračovat ve čtení uživatelské příručky. Následující seznam ukazuje různé nástroje:

1.  Standardní zprávy

2.  Zprávy datových sad

3.  Zprávy o úplnosti dat

4.  Statické zprávy

5.  Zprávy o distribuci organizační jednotky

6.  Zprávy tabulky

7.  Grafy

8.  Webová kontingenční tabulka

9.  GIS

10. Kontingenční tabulky My Datamart a Excel

## Nástroje pro analýzu dat { #data-analysis-tools }

V následující části je uveden popis každého nástroje.

### Standardní zprávy { #standard-reports }

Standardní zprávy jsou zprávy s předdefinovanými vzory. To znamená, že zprávy  jsou snadno přístupné několika kliknutími a mohou je využívat uživatelé na všech úrovních zkušeností. Zpráva může obsahovat statistiky ve formě tabulek a grafů a lze ji přizpůsobit tak, aby vyhovovala většině požadavků. Řešení zpráv v DHIS2 je založeno na JasperReports a zprávy jsou nejčastěji navrženy pomocí návrháře sestav iReport. I když je návrh sestavy pevný, lze data do sestavy dynamicky načítat na základě jakékoli organizační jednotky v rámci hierarchie as různými časovými obdobími.

### Zprávy datových sad { #data-set-reports }

Hlášení zprávy datové sady zobrazují design formulářů pro zadávání dat jako zprávu naplněnou agregovanými daty (na rozdíl od zachycených dat na nízké úrovni). Tato zpráva je snadno přístupná pro všechny typy uživatelů a poskytuje rychlý přístup k souhrnným datům. Často existuje starší požadavek na prohlížení formulářů pro zadávání dat jako zpráv, které tento nástroj účinně zajišťuje. Zpráva datové sady podporuje všechny typy formulářů pro zadávání dat, včetně sekcí a vlastních formulářů.

### Zpráva o úplnosti dat { #data-completeness-report }

Zpráva o úplnosti údajů vytváří statistické údaje o míře úplnosti formulářů pro zadávání údajů. Statistické údaje lze analyzovat na jednotlivé datové soubory nebo na seznam organizačních jednotek se společným nadřazeným v hierarchii. Poskytuje procentní hodnotu pro celkovou úplnost a pro úplnost včasných podání. Jako základ pro statistiku lze použít různé definice úplnosti: Nejprve na základě počtu souborů dat označených ručně jako úplných uživatelem zadávajícím data. Druhý na základě toho, zda jsou pro datový soubor vyplňovány všechny datové prvky definované jako povinné. Za třetí na základě procenta počtu vyplněných hodnot nad celkovým počtem hodnot v datové sadě.

### Statické zprávy { #static-reports }

Statické sestavy poskytují dvě metody propojení s existujícími prostředky v uživatelském rozhraní. Nejprve poskytuje možnost propojení se zdrojem na internetu prostřednictvím adresy URL. Zadruhé poskytuje možnost nahrávat soubory do systému a odkazovat na ně. Typ souborů k nahrání může být jakýkoli druh dokumentu, obrázku nebo videa. Užitečnými příklady dokumentů, na které lze odkazovat, jsou zdravotní průzkumy, politické dokumenty a roční plány. Adresy URL mohou odkazovat na příslušné webové stránky, jako je domovská stránka Ministerstva zdravotnictví, zdroje informací souvisejících se zdravím. Kromě toho může být použit jako rozhraní k webovým analytickým nástrojům třetích stran tím, že ukazuje na konkrétní zdroje. Jedním příkladem je nasměrování adresy URL na sestavu obsluhovanou platformou BIRT reporting.

### Zprávy o distribuci organizační jednotky { #organisation-unit-distribution-reports }

Zpráva distribuce organizační jednotky poskytuje statistiky o zařízeních (organizačních jednotkách) v hierarchii na základě jejich klasifikace. Klasifikace je založena na skupinách organizačních jednotek a sadách skupin. Zařízení lze například klasifikovat podle typu přiřazením k příslušné skupině ze skupiny nastavené pro typ organizační jednotky. Zpráva distribuce vytváří počet zařízení pro každou třídu a lze ji vygenerovat pro všechny organizační jednotky a pro všechny sady skupin v systému.

### Zprávy tabulky { #report-tables }

Tabulky sestav jsou sestavy založené na agregovaných datech v tabulkovém formátu. Tabulku sestav lze použít jako samostatnou sestavu nebo ji lze použít jako zdroj dat pro propracovanější standardní návrh sestavy. Tabulkový formát lze překládat do tabulek s libovolným počtem dimenzí, které se zobrazují jako sloupce. Může obsahovat agregovaná data indikátoru a datového prvku i údaje o úplnosti datových sad. Může obsahovat relativní období, která umožňují opakované použití sestavy v průběhu času. Může obsahovat uživatelem volitelné parametry pro organizační jednotky a období, aby bylo možné znovu použít sestavu pro všechny organizační jednotky v hierarchii. Tabulka sestavy může být omezena na nejlepší výsledky a tříděna vzestupně nebo sestupně. Po vygenerování lze data tabulky sestavy stáhnout jako PDF, sešit Excel, soubor CSV a sestavu Jasper.

### Grafy { #charts }

Komponenta grafu nabízí širokou škálu grafů, včetně standardních pruhových, spojnicových a koláčových grafů. Grafy mohou obsahovat indikátory, datové prvky, období a organizační jednotky na ose x a y, stejně jako pevnou vodorovnou cílovou čáru. Grafy lze zobrazit přímo nebo jako součást ovládacího panelu, jak bude vysvětleno později.

### Webové kontingenční tabulky { #web-pivot-tables }

Webová kontingenční tabulka nabízí rychlý přístup ke statistickým údajům v tabulkovém formátu a poskytuje možnost „otočit“ libovolný počet dimenzí, jako jsou indikátory, datové prvky, organizační jednotky a období, aby se zobrazily na sloupcích a řádcích za účelem vytvoření přizpůsobených pohledů. Každou buňku v tabulce lze vizualizovat jako sloupcový graf.

### GIS { #gis }

Modul GIS umožňuje vizualizovat agregovaná data na mapách. Modul GIS může poskytovat tematické mapování polygonů, jako jsou provincie a okresy, a bodů, jako jsou zařízení, v samostatných vrstvách. Uvedené vrstvy lze zobrazit společně a kombinovat s vlastními překryvy. Taková zobrazení mapy lze snadno navigovat zpět v historii, uložit pro snadný přístup v pozdější fázi a uložit na disk jako obrazový soubor. Modul GIS poskytuje automatické a pevné zalomení tříd pro tematické mapování, předdefinované a automatické sady legend, schopnost zobrazit štítky (názvy) pro geografické prvky a schopnost měřit vzdálenost mezi body na mapě. Mapování lze zobrazit pro jakýkoli indikátor nebo datový prvek a pro jakoukoli úroveň v hierarchii organizační jednotky. K dispozici je také speciální vrstva pro zobrazení zařízení na mapě, kde každá z nich je podle svého typu reprezentována symbolem.

### Kontingenční tabulky My Datamart a Excel { #my-datamart-and-excel-pivot-tables }

Účelem nástroje My Datamart je poskytnout uživatelům plný přístup k agregovaným datům i na nespolehlivých připojeních k internetu. Tento nástroj se skládá z odlehčené klientské aplikace, která je nainstalována v počítači uživatelů. Připojuje se k online centrálnímu serveru, na kterém běží instance DHIS2, stahuje agregovaná data a ukládá je do databáze v místním počítači. Tuto databázi lze použít k připojení nástrojů třetích stran, jako jsou kontingenční tabulky MS Excel, což je výkonný nástroj pro analýzu a vizualizaci dat. Toto řešení implikuje, že k synchronizaci databáze klientů s centrální online databází je potřeba jen krátká doba připojení k internetu a že po dokončení tohoto procesu budou data k dispozici nezávisle na připojení. Přečtěte si kapitolu věnovanou tomuto nástroji, kde najdete podrobné informace.

# Lokalizace DHIS 2 { #localization-of-dhis-2 }

## Koncepty lokalizace DHIS 2 { #localization-intro }

Lokalizace zahrnuje přizpůsobení aplikace konkrétnímu místu. Při implementaci DHIS 2 v dané zemi by měly být přiděleny odpovídající zdroje k překladu a lokalizaci aplikace, je-li to požadováno. Je třeba vzít v úvahu překlad prvků uživatelského rozhraní, zpráv, rozvržení, formátů data a času, měny a dalších aspektů. Kromě překladu samotného uživatelského rozhraní je třeba za překlad také považovat obsah metadat obsažený v databázi.

Překlady rozhraní jsou kompilovány do samotného systému, takže k novým překladům lze přistupovat pouze pomocí novější verze DHIS 2. Překlady databází jsou naopak specifické pro vaši implementaci a lze je přidat k vaší existující instanci DHIS 2.

Tyto dva aspekty jsou spravovány nezávisle a níže jsou uvedeny procesy a nástroje.

## Lokalizace uživatelského rozhraní { #user-interface-localization }

### Přehled { #overview }

DHIS 2 podporuje internacionalizaci (i18n) uživatelského rozhraní pomocí řetězců vlastností Java a souborů PO. Soubory vlastností Java se používají, když zprávy pocházejí z back-endového serveru Java, zatímco soubory PO se používají pro aplikace front-end napsané v JavaScriptu. Aplikace DHIS 2 pro Android používají konkrétní formát XML.

> **Poznámka**
>
> Překladatel se nemusí starat o různé formáty zdrojových souborů; překladatelská platforma skryje podrobnosti a zobrazí pouze řetězce, které vyžadují překlad.
> Například obrázek níže ukazuje zdrojový a cílový řetězec při překladu zdroje do francouzštiny.
>
> ![](resources/images/translation_ui.jpg)

U všech zpráv v DHIS 2 by měl vždy existovat anglický řetězec. Když uživatel vybere daný jazyk a v tomto jazyce je k dispozici překlad, překlad se zobrazí. Pokud však řetězec v požadovaném jazyce chybí, použijí se záložní pravidla. V případech, kdy dva dané překlady, například portugalština a brazilská portugalština, sdílejí společné zprávy, není nutné provést úplný překlad do alternativního jazyka. Přeloženy by měly být pouze zprávy, které se liší.
Záložní pravidla se poté použijí následujícím způsobem (za předpokladu, že uživatel zvolil jako svůj jazyk brazilskou portugalštinu:

1.  Zobrazit zprávu v brazilské portugalštině, pokud existuje.

2.  Pokud neexistuje v alternativním jazyce, použijte portugalskou zprávu, pokud existuje.

3.  Pokud není žádná zpráva v základním jazyce ani v alternativním jazyce, zvolte konečný záložní jazyk, angličtinu.

> **Důležité**
>
> Existuje celá řada zdrojových řetězců, například "dd MMM yyyy 'do '", které se používají pro formátování data a času v různých částech DHIS 2. Část hodnoty by se neměla překládat, protože se ve skutečnosti používá speciální pole pro formátování pomocí Java nebo JavaScriptu k interpolaci nebo formátování řetězce. V tomto příkladu by část hodnoty, kterou **lze** přeložit, byla „do“, například do „a“ ve španělštině. Speciální řetězec, který by se **neměl** překládat, je „dd MMM yyyy“. Pokud jsou tyto řetězce šablony formátu data přeloženy, může to mít za následek chyby v aplikaci!

> **Důležité**
>
> Některé speciální proměnné (např. {0}) používají složené závorky. To označuje proměnnou, která bude aplikací nahrazena číslem nebo jinou hodnotou. Tuto proměnnou notaci musíte umístit do správné polohy a určitě ji neměnit.

### Překladová platforma { #translation-server }

DHIS2 nyní používá [transifex](www.transifex.com) jako naši hlavní platformu pro správu překladů. K prostředkům DHIS2 můžete přistupovat na [translate.dhis2.org](https://translate.dhis2.org) nebo přímo na https://www.transifex.com/hisp-uio/public.

### Jak mohu přispět k překladům? { #how-do-i-contribute-to-translations }

#### Zaregistrujte se jako překladatel { #register-as-a-translator }

Prvním krokem je získání přístupu k projektu. Existují dva způsoby, jak toho dosáhnout:

1. Přejděte na platformu a vytvořte si účet s transifexem, poté - požádejte o přístup k naší organizaci „HISP UiO“ jako člen překladatelského týmu „DHIS 2 Core Apps“.
    Transifex má několik užitečných pokynů zde: [Začínáme jako překladatel](https://docs.transifex.com/getting-started-1/translators)

1. Pošlete e-mail týmu DHIS 2 na translate@dhis2.org a požádejte o přístup.
   Uveďte: - jméno, e-mailovou adresu a jazyk překladu uživatele (uživatelů), ke kterému byste chtěli mít přístup, a - trochu informací o tom, proč máte zájem přispívat k překladům DHIS 2

#### Úprava překladu { #edit-translations }

Jakmile budete mít přístup jako překladatel, můžete začít překládat prostřednictvím webového editoru transifex.

Transifex má užitečného průvodce zde: [Translations Online with the Web Editor](https://docs.transifex.com/translation/translating-with-the-web-editor)

Pokud je to možné, projekty představují aplikace DHIS 2 jedna k jedné. Například projekt **APP: Data Visualizer** obsahuje překladové řetězce pro aplikaci Data Visualizer.

Naše projekty transifexu pro uživatelské rozhraní DHIS2 začínají jednou z následujících možností:

- **APP:** označuje, že projekt obsahuje řetězce pro konkrétní aplikaci
- **APP-COMPONENT:** označuje, že projekt je knihovnou komponent používaných aplikacemi
- **ANDROID:** označuje, že projekt je aplikací Andriod

Kromě toho **APP: Zdroje na straně serveru** obsahuje některé řetězce, které používá několik aplikací; a to:

- "Vstup dat"
- "Údržba"
- „Kontingenční tabulky“
- „Zprávy“

> **Tip**
>
> Abychom zajistili úplné překlady pro konkrétní aplikaci, např. „Tracker Capture“, musíte se ujistit, že překlady jsou kompletní v:
>
> - Projekt aplikace: **APP: Tracker Capture**
> - Jakékoli projekty začínající **APP-COMPONENTS**
> - **APP: Server-Side Resources**, pokud je požadováno. Pro Tracker Capture to není **nutné**.

V rámci projektů máme prostředky, které představují lokalizační soubory ve zdrojovém kódu. Aby bylo možné podporovat více verzí DHIS2, se stejnými lokalizačními soubory je _version_ přidružen ke každé instanci souboru. Takže pro **APP: Data Visualizer** vypadá seznam zdrojů ve webovém editoru takto:

![](resources/images/implementation_guide/transifex_data_vis.jpg)

tj. pro aplikaci existuje pouze jeden zdrojový soubor (`en.pot`), ale přidali jsme verze od verze 2.31 (v31) až po nejnovější vývoj (master). Verze se zobrazuje v poli „Kategorie“ a je také viditelná jako předpona názvu zdroje, např. `v31--en-pot`.

> **Poznámka**
>
> Obecně požadujeme, aby se překladatelé zaměřili na zdroj "**master**"; obvykle obsahuje všechny řetězce z předchozích verzí, a když jsou přidány překlady, platforma vyplní odpovídající překlady i v předchozích verzích.

### Kdy budou v systému k dispozici nové překlady? { #when-will-new-translations-be-available-in-the-system }

Máme průběžnou službu každou noc, která stahuje nové překlady z platformy transifex a otevírá pull požadavek na aktualizaci zdrojového kódu.

Služba prochází všemi projekty a podporovanými jazyky a provádí následující:

1. Vytáhne lokalizační soubory z transifexu (**kde jsou překlady hotové z více než z 20%**)
2. Vyvolá požadavek na stažení zdrojového kódu, pokud jsou nalezeny změny pro jazyk

Pull requesty jsou zkontrolovány a sloučeny do kódové základny jako součást procesu normálního vývoje.

> **Informace**
>
> Překlady přidané na transifex budou obecně v dalším dostupném stabilním vydání pro všechny podporované verze DHIS 2
>
> _Pokud se potřebujete ujistit, že vaše překlady budou v příštím stabilním vydání, kontaktujte nás (translate@dhis2.org) a vysvětlete své potřeby a my vám dáme vědět, co můžeme udělat._

> **Tip**
>
> Překlady, které přidáte do transifexu, by ve většině případů měly být viditelné ve všech vývojových demo verzích na našem Play serveru (https://play.dhis2.org) během několika dní.

### Jak přidám nový jazyk? { #how-do-i-add-a-new-language }

Kontaktujte nás prosím e-mailem translate@dhis2.org nebo na [Community of Practice](https://community.dhis2.org/c/translation) a přidáme tento jazyk k projektům na transifexu.

Jakmile budou prostředky pro tento jazyk přeloženy na více než 20%, začnou se stahovat do systému. Poté se stanou viditelnými ve vývojových demo verzích a budou k dispozici v budoucích verzích.

> **Poznámka**
>
> DHIS 2 spravuje národní prostředí metadat (databáze) nezávisle na uživatelském rozhraní. _Viz následující část._

## Překlady metadat / databází { #metadata-database-translations }

Kromě překladu uživatelského rozhraní podporuje DHIS 2 také lokalizaci obsahu metadat v databázi. Jednotlivé objekty je možné překládat prostřednictvím aplikace **Údržba**, ale za účelem lepší podpory standardního pracovního postupu překladu byla pro tento účel vyvinuta specializovaná aplikace.

Nová národní prostředí metadat lze přidat v aplikaci **Údržba > Národní prostředí**.

### Aplikace Překlady DHIS 2 { #translations-app }

Aplikaci DHIS 2 **Překlady** lze použít k překladu všech metadat (datové prvky, kategorie, organizační jednotky atd.) Do jakéhokoli národního prostředí, které je v databázi.

Začněte jednoduše výběrem aplikace **Překlady** z nabídky nejvyšší úrovně.

![](resources/images/translations_app.png)

1.  Z rozbalovací nabídky **Objekt** vyberte typ objektu, který chcete přeložit, například „Datové prvky“.

2.  Ujistěte se, že jste nastavili **Cílové národní prostředí** na správný jazyk.

3.  Vyberte konkrétní objekt, který chcete přeložit, a přeložit každou z vlastností (Název, Zkrácený název, Popis atd.). Tyto vlastnosti se u jednotlivých objektů liší.

4.  Po dokončení překladu konkrétního objektu uložte změny stisknutím tlačítka „Uložit“.

> **Poznámka**
>
> Konkrétní výraz můžete vyhledat pomocí funkce vyhledávání v pravém horním rohu aplikace.
