---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/offline-data-entry.md"
revision_date: "2021-06-14"
---

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

![](resources/images/offline_data_entry/image5.png)

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

![](resources/images/offline_data_entry/image9.jpg)
</td>
<td style="width:40%;padding: 5 20 5 20 ;border:0px;">

![](resources/images/offline_data_entry/image7.jpg)
</td>
</tr>
</table>

Na straně správy systému organizování formuláře pro zadávání dat do sekcí v DHIS 2 umožní plynulejší a příjemnější zážitek ze zadávání dat.

Pokud jde o synchronizaci, když není v případě potřeby k dispozici připojení k internetu, uživatel vezme mobilní zařízení do okresu - během schůzky v okresu - nebo do nejbližší oblasti, kde je k dispozici internet.

#### Využití možnosti offline modulu pro zadávání webových dat DHIS 2 v režimu offline { #use-of-the-offline-capability-of-dhis-2-web-data-entry-module }

Modul pro zadávání webových dat je modul uvnitř DHIS 2, který umožňuje zadávání dat pomocí webového prohlížeče. V DHIS 2 je běžný způsob zadávání dat online. Má však také schopnost „offline“, která podporuje pokračování zadávání dat, i když je internet přerušen. To znamená, že pokud chce uživatel okamžitě zadávat data na konci měsíce, musí se nejprve připojit k internetu, přihlásit se k DHIS 2 a otevřít formuláře pro zadávání dat alespoň pro jedno ze zařízení, ke kterým je přiřazen . Od tohoto kroku může odpojit internet a pokračovat v zadávání dat pro všechna svá zařízení a po dobu, kterou chce, pokud není ve webovém prohlížeči zavřeno okno webové stránky pro zadávání dat. Po dokončení zadávání dat může zavřít prohlížeč a vypnout počítač. Zadaná data budou uložena lokálně do mezipaměti prohlížeče a při příštím připojení online a přihlášení do DHIS 2 bude vyzván ke kliknutí na tlačítko pro jejich nahrání.

V tomto případě je možné použít buď aplikaci pro zadávání dat pro Android nebo částečně offline webovou funkci v DHIS 2 nebo obojí v závislosti na velikosti formulářů pro zadávání dat. <!-- Není jasné, na co odkazuje „V tomto případě“ --> Vymazání mezipaměti prohlížeče však povede ke ztrátě lokálně uložených dat. Proto se doporučuje nevymazat mezipaměť, aniž byste se ujistili, že jsou synchronizována data uložená místně.

Když je uživatel přihlášen a internet je přerušen (úmyslně nebo ne)

![](resources/images/offline_data_entry/image1.png) <!-- PALD: This screenshot was 
taken when the home icon ()top left corner) was broken. I suggest we replace this image! -->

Když je internet zpět a uživatel se přihlásí k DHIS 2

![](resources/images/offline_data_entry/image6.png)

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
