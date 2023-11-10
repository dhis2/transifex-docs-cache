---
revision_date: "2022-02-08"
template: single.html
---

# Co je DHIS2? { #what_is_dhis2 }

Po přečtení této kapitoly budete schopni porozumět:

-   Co je DHIS2 a k jakému účelu slouží ve vztahu ke zdravotnickým informačním systémům (HIS)?

-   Jaké jsou hlavní technologické úvahy při zavádění DHIS2 a jaké jsou možnosti rozšíření DHIS2 o nové moduly?

-   Jaký je rozdíl mezi údaji o pacientech a souhrnnými údaji?

-   Jaké jsou některé výhody a výzvy spojené s používáním bezplatného a otevřeného softwaru (FOSS) pro HIS?

## Pozadí DHIS2 { #mod1_1 }

DHIS2 je nástroj pro shromažďování, ověřování, analýzu a prezentaci souhrnných statistik a údajů o pacientech, přizpůsobených (ale bez omezení) na integrované činnosti správy zdravotních informací. Jedná se spíše o obecný nástroj než o předem nakonfigurovanou databázovou aplikaci s otevřeným metadatovým modelem a flexibilním uživatelským rozhraním, které uživateli umožňuje navrhovat obsah konkrétního informačního systému bez nutnosti programování. DHIS2 je modulární webový softwarový balíček vytvořený pomocí bezplatných a otevřených Java frameworků.

DHIS2 je software s otevřeným zdrojovým kódem vydaný na základě licence BSD a lze jej získat bez nákladů. Běží na jakékoli platformě s nainstalovaným Java Runtime Environment (JRE 7 nebo vyšším).

DHIS2 je vyvíjen programem Health Information Systems Program (HISP) jako otevřený a globálně distribuovaný proces s vývojáři v současné době v Indii, Vietnamu, Tanzanii, Irsku a Norsku. Vývoj koordinuje univerzita v Oslu s podporou NORAD a dalších dárců.

Software DHIS2 se používá ve více než 40 zemích v Africe, Asii a Latinské Americe a mezi země, které přijaly DHIS2 jako svůj celostátní software HIS, patří Keňa, Tanzanie, Uganda, Rwanda, Ghana, Libérie a Bangladéš. Rychle rostoucí počet zemí a organizací zahajuje nová nasazení.

Dokumentace poskytnutá tímto způsobem se pokusí poskytnout komplexní přehled o aplikaci. Vzhledem k abstraktní povaze aplikace nebude tato příručka sloužit jako kompletní podrobný návod, jak aplikaci používat za všech okolností, ale bude se snažit poskytnout ilustrace a příklady toho, jak lze DHIS2 implementovat v různé situace prostřednictvím zobecněných příkladů.

Před implementací DHIS2 v novém nastavení důrazně doporučujeme přečíst si Průvodce implementací DHIS2 (samostatný manuál od tohoto), který je také k dispozici na hlavní stránce DHIS2 [web](http://dhis2.org/documentation/).

## Klíčové vlastnosti a účel DHIS2 { #key-features-and-purpose-of-dhis2 }

Klíčové vlastnosti a účel DHIS2 lze shrnout takto:

-   Poskytnout komplexní řešení pro správu dat založené na principech datového skladu a modulární strukturu, kterou lze snadno přizpůsobit různým požadavkům informačního systému pro správu, což podporuje analýzu na různých úrovních hierarchie organizace.

-   Přizpůsobení a místní nastavení prostřednictvím uživatelského rozhraní. K zahájení používání DHIS2 v novém prostředí (země, region, okres atd.) není nutné žádné programování.

-   Poskytuje nástroje pro zadávání dat, které mohou být buď ve formě standardních seznamů nebo tabulek, nebo je lze přizpůsobit pro replikaci papírových formulářů.

-   Poskytuje různé druhy nástrojů pro ověřování dat a zlepšování kvality dat.

-   Poskytuje snadné použití - sestavy na jedno kliknutí s grafy a tabulkami pro vybrané indikátory, nebo souhrnné sestavy s využitím designu nástrojů pro sběr dat. Povolte integraci s populárními externími nástroji pro návrh sestav (např. JasperReports) a přidejte další vlastní nebo pokročilé sestavy.

-   Flexibilní a dynamická (průběžná) analýza dat v analytických modulech (tj. GIS, kontingenční tabulky, vizualizér dat, zprávy o událostech atd.).

-   Uživatelsky specifický ovládací panel pro rychlý přístup k příslušným nástrojům pro monitorování a hodnocení včetně grafů indikátorů a odkazů na oblíbené zprávy, mapy a další klíčové zdroje v systému.

-   Snadno použitelná uživatelská rozhraní pro správu metadat, např. pro přidávání / úpravy datových sad nebo zdravotnických zařízení. K nastavení systému do nového nastavení není potřeba žádné programování.

-   Funkce pro návrh a úpravu vypočítaných vzorců indikátorů.

-   Modul správy uživatelů pro hesla, zabezpečení a podrobnou kontrolu přístupu (uživatelské role).

-   Zprávy lze zasílat uživatelům systému pro zpětnou vazbu a oznámení. Zprávy lze také doručovat na e-mail a SMS.

-   Uživatelé mohou sdílet a diskutovat o svých datech v grafech a sestavách pomocí interpretací, což umožňuje aktivní komunitu uživatelů založenou na informacích.

-   Funkce exportu a importu dat a metadat, podporující synchronizaci offline instalací a interoperabilitu s jinými aplikacemi.

-   Pomocí webového API DHIS2 umožněte integraci s externím softwarem a rozšíření základní platformy pomocí vlastních aplikací.

-   Další moduly lze vyvíjet a integrovat podle potřeb uživatele, a to buď jako součást uživatelského rozhraní portálu DHIS2, nebo jako volně propojená externí aplikace interagující prostřednictvím webového API DHIS2.

Stručně řečeno, DHIS2 poskytuje komplexní HIS řešení pro potřeby zpráv a analýz uživatelů zdravotních informací na jakékoli úrovni.

## Použití DHIS2 v HIS: sběr, zpracování, interpretace a analýza dat. { #use-of-dhis2-in-his-data-collection-processing-interpretation-and-analysis }

Širší kontext NIS lze komplexně popsat prostřednictvím informačního cyklu uvedeného na obrázku 1.1 níže. Informační cyklus obrazně zobrazuje různé komponenty, fáze a procesy, jejichž prostřednictvím jsou data shromažďována, kontrolována jejich kvalita, zpracovávány, analyzovány a používány.

![Cyklus zdravotních informací](resources/images/dhis2UserManual/dhis2_information_cycle.png)

DHIS2 podporuje různé aspekty informačního cyklu, včetně:

-   Sbírání dat.

-   Provádění kontroly kvality.

-   Přístup k datům na více úrovních.

-   Hlášení.

-   Tvorba grafů a map a dalších forem analýzy.

-   Umožnění srovnání v čase (například v předchozích měsících) a prostoru (například v zařízeních a okresech).

-   Podívejte se na trendy (zobrazení dat v časových řadách a jejich minimální a maximální úrovně).

Jako první krok slouží DHIS2 jako nástroj pro sběr, záznam a kompilaci dat a lze do něj zadávat všechna data (ať už v číslech nebo v textové podobě). Zadávání dat lze provádět v seznamech datových prvků nebo v přizpůsobených uživatelsky definovaných formulářích, které lze vyvinout tak, aby napodobovaly papírové formuláře, aby se usnadnil proces zadávání dat.

Jako další krok lze DHIS2 použít ke zvýšení kvality dat. Nejprve v místě zadávání dat lze provést kontrolu, zda data spadají do přijatelných úrovní minimálních a maximálních hodnot pro jakýkoli konkrétní datový prvek. Taková kontrola například může pomoci identifikovat překlepy v době zadávání dat. Uživatel může dále definovat různá ověřovací pravidla a DHIS2 může data spouštět prostřednictvím ověřovacích pravidel k identifikaci porušení. Tyto typy kontrol pomáhají zajistit, aby data zadaná do systému byla od samého začátku kvalitní a mohla by být vylepšena lidmi, kteří jej nejvíce znají.

Po zadání a ověření dat může DHIS2 pomoci vytvářet různé druhy zpráv. Prvním typem jsou zprávy o rutinách, které lze předdefinovat, takže všechny zprávy, které je třeba generovat, lze provést kliknutím na tlačítko. DHIS2 může dále pomoci při generování analytických zpráv prostřednictvím srovnání například indikátorů napříč zařízeními nebo v průběhu času. Grafy, mapy, zprávy a zdravotní profily patří mezi výstupy, které DHIS2 může produkovat, a ty by měly být rutinně vytvářeny, analyzovány a reagovány zdravotními manažery.

## Technické zázemí { #technical-background }

### DHIS2 jako platforma { #dhis2-as-a-platform }

DHIS2 lze vnímat jako platformu na několika úrovních. Za prvé, aplikační databáze je navržena od základu s ohledem na flexibilitu. Datové struktury, jako jsou datové prvky, organizační jednotky, formuláře a uživatelské role, lze definovat zcela volně prostřednictvím uživatelského rozhraní aplikace. To umožňuje, aby byl systém přizpůsoben mnoha kontextům prostředí a případům použití. Viděli jsme, že DHIS2 podporuje většinu hlavních požadavků na rutinní sběr dat a analýzu, které se objevují v implementacích zemí. Umožňuje také, aby DHIS2 sloužil jako systém pro správu domén jako logistika, laboratoře a finance.

Za druhé, díky modulární konstrukci DHIS2 je možné jej rozšířit o další softwarové moduly nebo prostřednictvím vlastních aplikací. Tyto softwarové moduly / aplikace mohou žít bok po boku s jádrovými moduly DHIS2 a lze je integrovat do portálu a systému nabídek DHIS2. Jedná se o výkonnou funkci, protože v případě potřeby umožňuje rozšířit systém o další funkce, obvykle pro specifické požadavky dané země, jak již bylo uvedeno výše.

Nevýhodou rozšiřitelnosti softwarového modulu je to, že klade několik omezení na vývojový proces. Vývojáři, kteří vytvářejí další funkce, jsou kromě omezení kladených na návrh modulů portálovým řešením DHIS2 omezeni na technologii DHIS2, pokud jde o programovací jazyk a softwarové rámce. Tyto moduly musí být také zahrnuty do softwaru DHIS2, když je software vytvořen a nasazen na webovém serveru, nikoli dynamicky během běhu.

Aby bylo možné překonat tato omezení a dosáhnout volnějšího propojení mezi servisní vrstvou DHIS2 a dalšími softwarovými artefakty, bylo jako součást DHIS2 vyvinuto API založené na REST. Toto webové rozhraní API odpovídá pravidlům architektonického stylu REST. To znamená, že:

-   Webové rozhraní API poskytuje navigovatelné a strojově čitelné rozhraní pro kompletní datový model DHIS2. Například lze přistupovat k úplnému seznamu datových prvků, poté pomocí zadané adresy URL přejít na konkrétní datový prvek, který nás zajímá, a poté pomocí zadané adresy URL přejít na seznam datových sad, jejichž je datový prvek členem.

-   K (Meta)datům se přistupuje prostřednictvím jednotného rozhraní (URL) pomocí jednoduchých požadavků HTTP. Nejsou zapojeny žádné fantastické transportní formáty ani protokoly - pouze dobře otestovaný a dobře srozumitelný protokol HTTP, který je dnes hlavním stavebním kamenem webu. To znamená, že vývojáři třetích stran mohou vyvíjet software pomocí datového modelu a dat DHIS2, aniž by znali specifickou technologii DHIS2 2 nebo dodržovali konstrukční omezení DHIS2.

-   Veškerá data včetně metadat, zpráv, map a grafů, která jsou v terminologii REST známá jako zdroje, lze načíst ve většině populárních formátů reprezentace dnešního webu, jako jsou XML, JSON, PDF a PNG. Tyto formáty jsou široce podporovány v aplikacích a programovacích jazycích a poskytují vývojářům třetích stran širokou škálu možností implementace.

### Pochopení nezávislosti platformy { #understanding-platform-independence }

Všechny počítače mají operační systém (OS), který jej spravuje, a programy, které jej spouští. Operační systém slouží jako střední vrstva mezi softwarovou aplikací, jako je DHIS2, a hardwarem, jako je CPU a RAM. DHIS2 běží na virtuálním počítači Java, a proto může běžet na jakémkoli operačním systému, který podporuje Javu. Nezávislost na platformě znamená, že softwarová aplikace může běžet na JAKÉMKOLI OS - Windows, Linux, Macintosh atd. DHIS2 je nezávislý na platformě, a proto jej lze použít v mnoha různých kontextech v závislosti na přesných požadavcích použitého operačního systému.

DHIS2 navíc podporuje tři hlavní systémy systémů pro správu databází (DBMS). DHIS2 používá framework abstrakce databáze Hibernate a je kompatibilní s následujícími databázovými systémy: PostgreSQL, MySQL a H2. PostgreSQL a MySQL jsou vysoce kvalitní databáze připravené na produkci, zatímco H2 je užitečná databáze v paměti pro malé aplikace nebo vývojové aktivity.

A konečně, a to je možná nejdůležitější, protože DHIS2 je aplikace založená na prohlížeči, jediným skutečným požadavkem na interakci se systémem je webový prohlížeč. DHIS2 podporuje většinu webových prohlížečů, i když v současné době se doporučuje buď Google Chrome, Mozilla Firefox nebo Opera.

### Strategie nasazení - online vs. offline { #deployment-strategies-online-vs-offline }

DHIS2 je aplikace podporující síť a lze k ní přistupovat přes internet, místní intranet i místně nainstalovaný systém. Alternativy nasazení pro DHIS2 jsou v této kapitole definovány jako i) offline nasazení ii) online nasazení a iii) hybridní nasazení. Význam a rozdíly budou popsány v následujících částech.

#### Offline nasazení { #offline-deployment }

Offline nasazení znamená, že je pro koncové uživatele nainstalováno více samostatných offline instancí, obvykle na úrovni okresu. Systém je primárně udržován koncovými uživateli / okresními zdravotníky, kteří zadávají data a generují zprávy ze systému běžícího na jejich lokálním serveru. Systém bude také obvykle udržován národním týmem superuživatelů, kteří pravidelně navštěvují okresní nasazení. Data jsou v hierarchii posouvána nahoru koncovými uživateli, kteří vytvářejí soubory pro výměnu dat, které jsou zasílány elektronicky e-mailem nebo fyzicky poštou nebo osobním cestováním. (Upozorňujeme, že krátké připojení k internetu vyžadované pro odesílání e-mailů nesplňuje podmínky pro definování jako online). Tento styl nasazení má zjevnou výhodu, že funguje, když není k dispozici vhodné připojení k internetu. Na druhé straně jsou s tímto stylem významné výzvy, které jsou popsány v následující části.

-   **Hardware:** Provoz samostatných systémů vyžaduje instalaci pokročilého hardwaru z hlediska serverů a spolehlivého napájení, obvykle na úrovni okresů, po celé zemi. To vyžaduje odpovídající financování nákupu a plánu dlouhodobé údržby.

-   **Softwarová platforma:** Místní instalace vyžaduje značnou potřebu údržby. Ze zkušeností jsou největší výzvou viry a další malware, které z dlouhodobého hlediska mají tendenci infikovat místní instalace. Hlavním důvodem je, že koncoví uživatelé využívají paměťové karty pro přenos souborů a dokumentů pro výměnu dat mezi soukromými počítači, jinými pracovními stanicemi a systémem, ve kterém je aplikace spuštěna. Udržování antivirového softwaru a aktualizací operačních systémů v off-line prostředí je náročné a koncoví uživatelé často přijímají špatné postupy z hlediska bezpečnosti. Preferovaným způsobem, jak tento problém překonat, je spustit dedikovaný server pro aplikaci, kde nejsou povoleny žádné paměťové karty, a používat operační systém založený na Linuxu, který není tak náchylný k virovým infekcím jako MS Windows.

-   **Softwarová aplikace:** Schopnost distribuovat nové funkce a opravy chyb softwaru se zdravotními informacemi uživatelům je nezbytná pro údržbu a zdokonalování systému. Spoléhání se na to, že koncoví uživatelé budou provádět upgrady softwaru, vyžaduje rozsáhlé školení a vysokou úroveň kompetencí na jejich straně, protože upgrade softwarových aplikací může být technicky náročný úkol. Spoléhání se na národní tým superuživatelů při údržbě softwaru znamená hodně cestování.

-   **Údržba databáze:** Předpokladem efektivního systému je, aby všichni uživatelé zadávali data pomocí standardizované sady metadat (datové prvky, formuláře atd.). Stejně jako v předchozím bodě o upgradech softwaru vyžaduje distribuce změn v souboru metadat do mnoha offline instalací kompetenci koncového uživatele, pokud jsou aktualizace zasílány elektronicky nebo dobře organizovaný tým superuživatelů. Nedodržení synchronizace sady metadat bude mít za následek ztrátu schopnosti přesouvat data z okresů a / nebo nekonzistentní národní databáze, protože data zadaná například na úrovni okresů nebudou kompatibilní s daty na národní úrovni.

#### Online nasazení { #online-deployment }

Nasazení online znamená, že na serveru připojeném k Internetu je nastavena jedna instance aplikace. Všichni uživatelé (klienti) se připojují k on-line centrálnímu serveru přes internet pomocí webového prohlížeče. Tento styl nasazení je stále více možný díky zvýšené dostupnosti globálního (mobilního) internetového pokrytí a snadno dostupným a levným cloudovým výpočetním prostředkům. Tento vývoj umožňuje přístup k online serverům i ve venkovských oblastech pomocí mobilních internetových modemů (označovaných také jako _dongly_).

Tento styl nasazení online má obrovské pozitivní důsledky pro proces implementace a údržbu aplikace ve srovnání s tradičním samostatným stylem offline:

-   **Hardware:** Hardwarové požadavky na straně koncového uživatele jsou omezeny na přiměřeně moderní počítač / notebook a připojení k internetu prostřednictvím pevné linky nebo mobilního modemu. Není potřeba specializovaný server pro každého uživatele, postačí jakýkoli počítač s internetovým připojením. Pro online nasazení bude vyžadován server, ale protože existuje pouze jeden (nebo několik) serverů, které je třeba obstarat a udržovat, je to podstatně jednodušší (a levnější), než je údržba mnoha samostatných serverů v odlišných umístěních. Vzhledem k tomu, že cloudové výpočetní prostředky neustále stabilně snižují cenu a zároveň zvyšují výpočetní výkon, je nastavení výkonného serveru v cloudu mnohem levnější než nákup hardwaru.

-   **Softwarová platforma:** Koncoví uživatelé potřebují k připojení k on-line serveru pouze webový prohlížeč. Všechny dnes populární operační systémy jsou dodávány s webovým prohlížečem a neexistují žádné zvláštní požadavky na typ nebo verzi. To znamená, že pokud dojde k vážným problémům, jako jsou virové infekce nebo poškození softwaru, můžete se vždy uchýlit k přeformátování a instalaci operačního systému počítače nebo k získání nového počítače / notebooku. Uživatel může pokračovat v zadávání dat tam, kde byl ponechán, a žádná data nebudou ztracena.

-   **Softwarová aplikace:** Styl nasazení centrálního serveru znamená, že aplikaci lze upgradovat a udržovat centralizovaným způsobem. Když jsou vydány nové verze aplikací s novými funkcemi a opravami chyb, lze je nasadit na jediný online server. Všechny změny se poté projeví na straně klienta při příštím připojení koncových uživatelů přes internet. To samozřejmě má obrovský pozitivní dopad na proces zlepšování systému, protože nové funkce mohou být uživatelům distribuovány okamžitě, všichni uživatelé budou přistupovat ke stejné verzi aplikace a chyby a problémy lze třídit a nasazovat za běhu.

-   **Údržba databáze:** Podobně jako v předchozím bodě lze změny metadat provádět na on-line serveru centralizovaným způsobem a automaticky se rozšíří na všechny klienty při příštím připojení k serveru. Tím se efektivně odstraní obrovské problémy související s udržováním upgradované a standardizované sady metadat související s tradičním stylem nasazení offline. Je to mimořádně výhodné například během počáteční fáze vývoje databáze a během ročních procesů revize databáze, protože koncoví uživatelé budou mít přístup ke konzistentní a standardizované databázi, i když ke změnám dochází často.

Tento přístup může být problematický v případech, kdy je připojení k internetu nestabilní nebo chybí po dlouhou dobu. DHIS2 má však určité funkce, které vyžadují, aby připojení k internetu bylo k dispozici pouze po část času, aby systém správně fungoval, například offline zadávání dat. Obecně však DHIS2 vyžaduje nějaké připojení k internetu, ale toto je stále snadnější problém vyřešit i na vzdálených místech.

#### Hybridní nasazení { #hybrid-deployment }

Z dosavadní diskuse si člověk uvědomí, že styl nasazení online je příznivý oproti stylu offline, ale vyžaduje slušné připojení k internetu tam, kde bude použit. Je důležité si všimnout, že uvedené styly mohou existovat společně v běžném nasazení. Je naprosto možné mít online i offline nasazení v jedné zemi. Obecným pravidlem by bylo, že okresy a zařízení by měly do systému přistupovat on-line přes internet, kde existuje dostatečné připojení k internetu, a off-line systémy by měly být nasazeny do okresů, kde tomu tak není.

Přesné definování slušného připojení k internetu je těžké, ale zpravidla by rychlost stahování měla být minimálně 10 Kbyte/s pro klienta a minimálně 1 Mbit/s (vyhrazená) šířka pásma pro server.

V tomto ohledu jsou modemy mobilního internetu, které lze připojit k počítači nebo notebooku a přistupovat k mobilní síti, mimořádně schopným a proveditelným řešením. Pokrytí mobilního internetu po celém světě rychle roste, často poskytuje vynikající připojení za nízké ceny a je skvělou alternativou k místním sítím a špatně udržovaným pevným internetovým linkám. Kontakt s národními společnostmi v oblasti mobilních sítí ohledně předplacených služeb a potenciálních výhod velké objednávky může být užitečným úsilím. Při rozhodování, jaký přístup k nasazení zvolit, protože by se mohl lišit a pokrýt různé části země, by mělo být prozkoumáno pokrytí sítě každého provozovatele sítě v příslušné zemi.

#### Server hosting { #server-hosting }

Přístup online nasazení vyvolává otázku, kde a jak hostovat server, na kterém bude spuštěna aplikace DHIS2. Obvykle existuje několik možností:

1.  Interní hosting v rámci ministerstva zdravotnictví

2.  Hostování v rámci vládního datového centra

3.  Hostování prostřednictvím externí hostingové společnosti

Hlavním důvodem pro výběr první možnosti je často politická motivace k „fyzickému vlastnictví“ databáze. Mnozí to považují za důležité pro „vlastnictví“ a kontrolu dat. Existuje také přání vybudovat místní kapacitu pro správu serveru související s udržitelností projektu. Často jde o iniciativy dárců, protože jsou vnímány jako konkrétní a užitečné poslání.

Pokud jde o druhou možnost, na některých místech je vybudováno vládní datové centrum s cílem podporovat a zlepšovat využívání a přístupnost veřejných dat. Dalším důvodem je, že šíření interních serverových prostředí je velmi náročné na zdroje a je efektivnější vytvořit centralizovanou infrastrukturu a kapacitu.

Pokud jde o externí hosting, v poslední době dochází k posunu směrem k outsourcingu provozu a správy počítačových zdrojů u externího poskytovatele, kde jsou tyto zdroje přístupné přes síť, populárně označované jako „cloud computing“ nebo „software jako služba“. K těmto zdrojům se obvykle přistupuje přes internet pomocí webového prohlížeče.

Primárním cílem nasazení online serveru je zajistit dlouhodobě stabilní a vysoce výkonnou dostupnost zamýšlených služeb. Při rozhodování, kterou možnost zvolit pro prostředí serveru, je třeba vzít v úvahu mnoho aspektů:

1.  Lidská kapacita pro správu a provoz serveru. Musí existovat lidské zdroje s obecnými dovednostmi ve správě serveru a ve specifických technologiích používaných pro aplikaci poskytující služby. Příkladem takových technologií jsou webové servery a platformy pro správu databází.

2.  Spolehlivá řešení pro automatické zálohování, včetně lokálního off-serveru a vzdáleného zálohování.

3.  Stabilní konektivita a velká šířka pásma sítě pro provoz na server a ze serveru.

4.  Stabilní napájení včetně záložního řešení.

5.  Zabezpečené prostředí pro fyzický server, pokud jde o problémy, jako je přístup, krádež a požár.

6.  Přítomnost plánu obnovy po havárii. Tento plán musí obsahovat realistickou strategii, která zajistí, že služba bude trpět pouze krátkými prostoji v případě selhání hardwaru, výpadku sítě a dalších.

7.  Proveditelný, výkonný a robustní hardware.

Všechny tyto aspekty musí být pokryty, aby se vytvořilo vhodné hostitelské prostředí. Hardwarový požadavek je záměrně kladen na poslední místo, protože existuje jasná tendence věnovat mu příliš mnoho pozornosti.

Když se podíváme zpět na tři hlavní možnosti hostování, zkušenosti z implementačních misí v rozvojových zemích naznačují, že všechny aspekty hostingu jsou zřídka přítomny v možnosti jedna a dvě na proveditelné úrovni. Dosažení přijatelné úrovně ve všech těchto aspektech je náročné z hlediska lidských zdrojů i peněz, zejména ve srovnání s náklady na možnost tři. Má tu výhodu, že se přizpůsobuje zmíněným politickým aspektům a budování místních kapacit pro správu serverů, na druhou stranu to lze zajistit alternativními způsoby.

Možnost tři - externí hosting - má tu výhodu, že podporuje všechny zmíněné aspekty hostingu za velmi přijatelnou cenu. Několik poskytovatelů hostingu - virtuálních serverů nebo softwaru jako služby - nabízí spolehlivé služby pro provozování většiny druhů aplikací. Příkladem takových poskytovatelů jsou [Linode](http://www.linode.com) a [Amazon Web Services](http://aws.amazon.com). Správa těchto serverů probíhá přes síťové připojení, což je nejčastěji případ správy lokálních serverů. Fyzické umístění serveru se v tomto případě stává irelevantní, protože tito poskytovatelé nabízejí služby ve většině částí světa. Toto řešení se stále více stává standardním řešením pro hostování aplikačních služeb. Aspekt budování místní kapacity pro správu serveru je s touto možností kompatibilní, protože místní tým ICT může mít za úkol udržovat externě hostovaný server, ale nemusí být zatížen obavami z omezení napájení a šířky pásma, které obvykle existují mimo hlavní datová centra .

Přístup ke kombinování výhod externího hostování s potřebou místního hostingu a fyzického vlastnictví spočívá v použití externího poskytovatele hostingu pro primární transakční systém při zrcadlení tohoto serveru na nekritický lokálně hostovaný server, který se používá jen pro čtení. účely, jako je analýza dat a přístup přes intranet.

## Rozdíl mezi agregovanými a pacientskými daty v HIS { #difference-between-aggregated-and-patient-data-in-a-his }

_Data pacienta_ jsou data vztahující se k jednomu pacientovi, jako je jeho / její diagnóza, jméno, věk, dřívější anamnéza atd. Tato data jsou obvykle založena na interakci jednoho pacienta se zdravotníkem. Například, když pacient navštíví kliniku zdravotní péče, mohou být zaznamenány různé podrobnosti, jako je teplota pacienta, jeho hmotnost a různé krevní testy. Pokud by byl u tohoto pacienta diagnostikován „nespecifikovaný nedostatek vitaminu B12“ odpovídající ICD-10 kódu D51.9, mohla by se tato konkrétní interakce nakonec zaznamenat jako instance „anémie“ v agregovaném systému. Data založená na pacientovi jsou důležitá, pokud chcete dlouhodobě sledovat postup pacienta v průběhu času. Například pokud chceme sledovat, jak se pacient drží a reaguje na proces léčby tuberkulózy (obvykle probíhá po dobu 6-9 měsíců), potřebovali bychom údaje o pacientovi.

_Aggregovaná data_ je konsolidace dat vztahujících se k více pacientům, a proto jej nelze vysledovat zpět ke konkrétnímu pacientovi. Jsou to pouze počty, jako je výskyt malárie, tuberkulózy nebo jiných nemocí. Rutinní data, se kterými se zdravotnické zařízení zabývá, jsou obvykle tento druh agregovaných statistik a používají se pro generování rutinních zpráv a indikátorů a nejdůležitější je strategické plánování v rámci zdravotního systému. Souhrnná data nemohou poskytnout typ podrobných informací, které mohou údaje na úrovni pacientů poskytnout, ale jsou zásadní pro plánování a vedení výkonu systémů zdravotní péče.

Mezi těmito dvěma údaji máte případová data nebo anonymní data „pacientů“. O konkrétní zdravotní události lze shromáždit mnoho podrobností, aniž by bylo nutné identifikovat pacienta, kterého se to týká. Ambulantní nebo ambulantní návštěvy, nový případ cholery, úmrtí matky atd. Jsou běžné případy použití, kdy by člověk chtěl shromáždit mnohem více podrobností, než jen přidat k celkovému počtu případů nebo návštěv. Tyto údaje se často shromažďují v řádkových polích formulářů nebo v podrobnějších formulářích auditu. Liší se od agregovaných dat v tom smyslu, že obsahuje mnoho podrobností o konkrétní události, zatímco agregovaná data by počítala, kolik událostí určitého typu, např. kolik ambulantních návštěv s hlavní diagnózou „malárie“ nebo kolik úmrtí matek, kde se zesnulý neúčastnil ANC, nebo kolik ohnisek cholery u dětí do 5 let. V DHIS2 jsou tato data shromažďována prostřednictvím programů typu single event bez registrace.

Údaje o pacientech jsou vysoce důvěrné, a proto musí být chráněny, aby je nemohl získat nikdo jiný než lékaři. Pokud jsou na papíru, musí být řádně uložen na bezpečném místě. U počítačů potřebují data pacientů zabezpečené systémy s hesly, omezeným přístupem a protokoly auditu.

Obavy o bezpečnost agregovaných dat nejsou tak zásadní jako pro údaje o pacientech, protože je obvykle nemožné určit konkrétní osobu podle souhrnné statistiky. Data však mohou být i nadále zneužívána a dezinterpretována ostatními a neměla by být distribuována bez zavedených odpovídajících zásad šíření dat.

## Free and Open Source Software (FOSS): výhody a výzvy { #free-and-open-source-software-foss-benefits-and-challenges }

Software nese pokyny, které sdělují počítači, jak má pracovat. Lidem vytvořená a člověkem čitelná forma těchto pokynů se nazývá zdrojový kód. Než může počítač skutečně provést pokyny, musí být zdrojový kód přeložen do strojově čitelného (binárního) formátu, který se nazývá objektový kód. Veškerý distribuovaný software obsahuje objektový kód, ale FOSS zpřístupňuje také zdrojový kód.

Vlastníci proprietárního softwaru licencují svůj objektový kód chráněný autorskými právy uživateli, což uživateli umožňuje spustit program. Programy FOSS na druhé straně licencují objekt i zdrojový kód, což uživateli umožňuje spouštět, upravovat a případně redistribuovat programy. Díky přístupu ke zdrojovému kódu mají uživatelé svobodu spouštět program pro jakýkoli účel, redistribuovat, zkoumat, přizpůsobovat se, učit se, upravovat software podle svých potřeb a vydávat vylepšení pro veřejnost pro dobro komunity. Některý FOSS je tedy také známý jako svobodný software, kde „svobodný“ odkazuje v první řadě na výše uvedené svobody spíše než zdarma v peněžním smyslu slova.

V sektoru veřejného zdraví může mít FOSS potenciálně řadu výhod, včetně:

-   Nižší náklady, protože nezahrnuje placení neúnosných nákladů na licenci.

-   Vzhledem k tomu, že se informační potřeby ve zdravotnictví neustále mění a vyvíjejí, je třeba, aby měl uživatel svobodu provádět změny podle požadavků uživatele. V proprietárních systémech je to často omezené.

-   Přístup ke zdrojovému kódu umožňující integraci a interoperabilitu. Ve zdravotnictví je interoperabilita mezi různými softwarovými aplikacemi stále důležitější, což znamená umožnit dvěma nebo více systémům komunikovat metadata a data. Tato práce je mnohem jednodušší a někdy závisí na zdrojovém kódu, který je k dispozici vývojářům, kteří vytvářejí integraci. Tato dostupnost často není možná v případě proprietárního softwaru. A když to je, přichází to s vysokými náklady a smluvními závazky.

-   Aplikace FOSS jako DHIS2 jsou obvykle podporovány globální sítí vývojářů, a mají tak přístup k nejmodernějším znalostem výzkumu a vývoje.

# Použití aplikace Zadávání dat { #data_entry_app }

## O aplikaci Zadávání dat { #about_data_entry_app }

Aplikace **Zadávání dat** je místo, kde ručně zadáváte agregovaná data v DHIS2. Registrujete data pro organizační jednotku, období a sadu datových prvků (datovou sadu) najednou. Soubor dat často odpovídá nástroji pro sběr dat v papírové podobě. Sady dat konfigurujete v aplikaci **Údržba**.

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

Když zavřete organizační jednotku, nemůžete registrovat ani upravovat data této organizační jednotky v aplikaci **Zadávání dat**.

## Zadejte data do formuláře pro zadávání údajů { #enter_data_in_data_entry_form }

![](resources/images/data_entry/data_entry_overview.png)

1.  Otevřete aplikaci **Zadávání dat**.

2.  Ve stromu organizační jednotky vlevo vyberte organizační jednotku.

3.  Vyberte **datovou sadu**.

4.  Vyberte **Období**.

    Dostupná období jsou řízena typem období souboru dat (frekvence hlášení). Kliknutím na **Předchozí rok** nebo **Příští rok** můžete přeskočit o rok zpět nebo vpřed.

    > **Note**
    >
    > Depending on how you've configured the data entry form, you might have to enter additional information before you can open the date entry form. This can for example be a project derived from a category combination.

5.  Zadejte údaje do formuláře pro zadávání údajů.

    -   Zelené pole znamená, že systém uložil hodnotu.

    -   Šedé pole znamená, že je pole deaktivováno a nemůžete zadat hodnotu. Kurzor automaticky přeskočí na další otevřené pole.

    -   Chcete-li přejít na další pole, stiskněte klávesu Tab nebo klávesu šipka dolů.

    -   Chcete-li se vrátit zpět na předchozí pole, stiskněte Shift + Tab nebo klávesu Šipka nahoru.

    -   Pokud zadáte neplatnou hodnotu, například znak v poli, který přijímá pouze číselné hodnoty, zobrazí se vyskakovací okno, které vysvětluje problém, a pole bude zbarveno žlutě (neuloženo), dokud hodnotu neopravíte.

    -   Pokud jste pro pole definovali rozsah minimální maximální hodnoty a zadáte hodnotu, která je mimo tento rozsah, zobrazí se vyskakovací zpráva, která říká, že hodnota je mimo rozsah. Hodnota zůstane neuložená, dokud nezměníte hodnotu nebo neaktualizujete rozsah hodnot a poté znovu nezadáte hodnotu.

6.  Po vyplnění formuláře klikněte na **Spustit ověření** v pravém horním rohu nebo pod formulářem pro zadávání údajů.

    Všechna ověřovací pravidla, která zahrnují datové prvky v aktuálním formuláři pro zadávání dat (datová sada), se poté spustí s novými daty. Pokud nedojde k žádnému porušení pravidel ověřování, zobrazí se zpráva s názvem _Obrazovka zadávání dat úspěšně prošla ověřením_. Pokud dojde k porušení ověřování, budou uvedena v seznamu.

    ![](resources/images/dhis2UserManual/Validation_Rule_Result.png)

7.  (Volitelné) Opravte porušení ověření.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros.

8.  Až chyby opravíte a zadávání dat dokončíte, klikněte na **Dokončit**.

    Systém tyto informace používá při generování zpráv o úplnosti pro okres, kraj, provincii nebo národní úroveň.

## Označte datovou hodnotu pro další sledování { #mark_data_for_followup_in_data_entry_form }

![](resources/images/data_entry/data_entry_section_history.png)

Pokud máte například podezřelou hodnotu, kterou musíte dále prozkoumat, můžete si ji ponechat v systému, ale označit ji pro další sledování. V aplikaci **Data Quality** můžete spustit následnou analýzu a zobrazit a opravit všechny označené hodnoty.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, kterou chcete označit pro další sledování.

4.  Klikněte na ikonu hvězdičky.

## Upravte hodnoty dat v vyplněném formuláři pro zadávání údajů { #edit_data_value_in_completed_form }

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Klikněte na **Neúplné**.

4.  Změňte příslušné hodnoty dat.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros,

5.  Klikněte na **Dokončit**.

## Zobrazte historii datové hodnoty { #display_data_value_history }

![](resources/images/data_entry/data_entry_section_history.png)

Můžete zobrazit posledních 12 hodnot registrovaných pro pole.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, pro kterou chcete zobrazit historii.

4.  Klikněte na **Historie datových prvků**.

## Zobrazte kontrolní stopu datových hodnot { #display_data_value_audit_trail }

![](resources/images/data_entry/data_entry_audit_trail.png)

Kontrolní záznam auditu umožňuje zobrazit další hodnoty dat, které byly zadány před aktuální hodnotou. Kontrolní záznam auditu také ukazuje, kdy byla změněna hodnota dat a který uživatel provedl změny.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, pro kterou chcete zobrazit záznam o auditu.

4.  Klikněte na **Audit trail**.

## Vytvořte rozsah minimální maximální hodnoty ručně { #change_min_max_range_manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  V aplikaci **Zadávání dat** otevřete formulář pro zadávání údajů.

2.  Poklepejte na pole, pro které chcete nastavit rozsah minimální a maximální hodnoty.

3.  Zadejte **minimální limit** a **maximální limit**.

4.  Klikněte **Uložit**.

    Pokud hodnoty nespadají do nového rozsahu hodnot při příštím zadávání dat, zobrazí se buňka pro zadávání dat s oranžovým pozadím.

5.  (Volitelné) Napište komentář, který vysvětlí příčinu nesrovnalosti, například událost v zařízení, která mohla vygenerovat velký počet klientů.

6.  (Volitelné) Klikněte na **Uložit komentář**.

> **Tip**
>
> Kliknutím na ikonu hvězdičky označte hodnotu pro další sledování.

## Zadejte data offline { #enter_data_offline }

Aplikace **Zadání Dat** funguje, i když během zadávání dat nemáte stabilní připojení k internetu. Pokud nemáte připojení k internetu, zadaná data se uloží do místního počítače. Když je připojení k internetu zpět, aplikace odešle data na server. Celková využití šířky pásma je snížena, protože formuláře pro zadávání dat se již načtou ze serveru pro každé vykreslení.

> **Poznámka**
>
> Chcete-li použít tuto funkci, musíte se k serveru přihlásit, když jste připojeni k internetu.

-   Když jste připojeni k internetu, aplikace zobrazí tuto zprávu v horní části formuláře pro zadávání dat:

    ![](resources/images/data_entry/data_entry_online1.png)

-   Pokud se vaše internetové připojení během zadávání dat přeruší, aplikace to zjistí a zobrazí tuto zprávu:

    ![](resources/images/data_entry/data_entry_offline1.png)

    Nyní budou vaše data uložena lokálně. Můžete pokračovat v zadávání dat jako obvykle.

-   Jakmile zadáte všechna potřebná data a aplikace zjistí, že je připojení k Internetu zpět, zobrazí se tato zpráva:

    ![](resources/images/data_entry/data_entry_offline_upload.png)

    Kliknutím na **Odeslat** synchronizujete data se serverem.

-   Když se data úspěšně synchronizují se serverem, zobrazí se tato potvrzovací zpráva:

    ![](resources/images/data_entry/data_entry_offline_upload_success1.png)

## Povolte zadávání dat jednotky s více organizacemi { #data_entry_multiple_organisation_units }

![](resources/images/data_entry/data_entry_multiple_org_unit.png)

Může být užitečné zadat data pro více organizačních jednotek do stejného formuláře pro zadávání dat, například pokud je ve formuláři několik datových prvků a v hierarchii je obrovské množství organizačních jednotek. V takovém případě můžete povolit zadávání dat jednotky s více organizacemi.

> **Poznámka**
>
> Zadávání dat jednotky s více organizacemi funguje pouze pro sekce formuláře.

1.  Otevřete aplikaci **Nastavení systému**.

2.  Vyberte **Povolit formuláře více organizačních jednotek**.

3.  V aplikaci **Zadávání dat** vyberte organizační jednotku bezprostředně nad organizační jednotkou, pro kterou chcete v hierarchii organizační jednotky zadat data.

    Datové prvky se ve formuláři zobrazí jako sloupce a organizační jednotky jako řádky.

    > **Note**
    >
    > The data entry forms should still be assigned to the facilities that you actually enter data for, that is the organisation units now appearing in the form.

## Viz také { #data_entry_app_see_also }

-   [Ovládání kvality dat](https://docs.dhis2.org/master/en/user/html/control_data_quality.html)

-   [Správa datových souborů a formulářů pro zadávání dat](https://docs.dhis2.org/master/en/user/html/manage_data_set.html)

-   [Použití aplikace Údržba](https://docs.dhis2.org/master/en/user/html/maintenance_app.html)

# Použití aplikace Capture { #capture_app }

## O aplikaci Capture { #about_capture_app }

> **Poznámka**
>
> Aplikace Capture slouží jako náhrada za aplikaci Event Capture. V budoucnu bude do aplikace Capture začleněna také aplikace Tracker Capture a aplikace Data Entry.

V aplikaci Capture registrujete události, ke kterým došlo v konkrétním čase a místě. Událost se může stát v kterémkoli daném okamžiku. To je v rozporu s rutinními daty, která se snímají v předdefinovaných pravidelných intervalech. Události se někdy nazývají případy nebo záznamy. V DHIS2 jsou události propojeny s programem. Aplikace Capture vám umožňuje vybrat organizační jednotku a program a určit datum, kdy došlo k události, před zadáním informací o události.

## Zaregistrujte událost { #capture_register_event }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Uvidíte pouze programy přidružené k vybrané organizační jednotce a programy, ke kterým máte přístup, a které jsou sdíleny s vaší skupinou uživatelů prostřednictvím sdílení na úrovni dat.

4. Pokud má program nastavenou kombinaci kategorií, bude nutné vybrat možnost kategorie.

5. Klikněte na **Nový**.

    ![vytvořit novou událost](resources/images/capture_app/create_new_event.png)

6. Vyplňte požadované informace. Pokud je programová fáze programu nakonfigurována k zachycení umístění:

    - Pokud se jedná o pole souřadnicového pole, můžete buď zadat souřadnice přímo, nebo můžete kliknout na ikonu **mapa** nalevo od pole souřadnic. Ten pak otevře mapu, kde můžete vyhledat místo nebo na něj přímo kliknout na mapě.

    - Pokud jde o pole polygon, můžete kliknout na ikonu **mapa** nalevo od pole. Otevře se mapa, kde můžete vyhledat místo a zachytit polygon (tlačítko v pravém horním rohu mapy).

7. V případě potřeby můžete přidat komentář kliknutím na tlačítko **Napsat komentář** v dolní části formuláře.

8. V případě potřeby můžete přidat vztah kliknutím na tlačítko **Přidat vztah** ve spodní části formuláře. Další informace najdete v části o **Přidání vztahu**.

9. Klikněte na **Uložit a ukončit** nebo klikněte na šipku vedle tlačítka a vyberte **Uložit a přidat další**.

    - **Uložit a přidat další** uloží aktuální událost a vymaže formulář. Všechny události, které jste zachytili, se zobrazí v seznamu v dolní části stránky. Pokud chcete dokončit zachycení událostí, můžete, pokud je formulář prázdný, klikněte na tlačítko Dokončit nebo pokud váš formulář obsahuje data, klikněte na šipku vedle **Uložit a přidat další** a vyberte **Uložit a ukončit**.

> **Poznámka**
>
> Některé datové prvky v události mohou být povinné (označené červenou hvězdičkou vedle štítku datového prvku). Než bude uživateli povoleno dokončit událost, musí být vyplněny všechny povinné datové prvky. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření povinných polí v nástroji Tracker and Event Capture“.** Pokud má uživatel toto oprávnění, povinné datové prvky nebudou vyžadovány a červená hvězdička nebude se zobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

> **Tip**
>
> Formulář pro zadávání údajů lze zobrazit také v **zobrazení řádku**. V tomto režimu jsou datové prvky uspořádány vodorovně. Toho lze dosáhnout kliknutím na tlačítko **Přepnout na zobrazení řádků** v pravém horním rohu formuláře pro zadávání údajů. Pokud jste aktuálně v **řádkovém zobrazení**, můžete přepnout na výchozí zobrazení formuláře kliknutím na tlačítko **Přepnout do zobrazení formuláře** v pravém horním rohu formuláře pro zadávání údajů.

## Zaregistrujte instanci trasované entity { #register-a-tracked-entity-instance }

Existují dva různé způsoby, jak lze zaregistrovat instanci trasované entity v organizační jednotce. Prvním způsobem je registrace instance sledované entity bez registrace do sledovacího programu. Druhou možností je registrace instance trasované entity v programu a její registrace.

### Bez zápisu do programu { #without-a-program-enrollment }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Klikněte na tlačítko „Nový“.

    ![obrázek](resources/images/capture_app/register-without-enrollment-new-button.png)

    Nyní budete přesměrováni na registrační stránku. Na této stránce uvidíte rozbalovací nabídku podobnou té na obrázku níže. Z rozbalovací nabídky můžete vybrat typ sledované entity, např. Budova, Osoba atd.

    ![obrázek](resources/images/capture_app/register-without-enrollment-dropdown-menu.png)

4. Vyberte typ trasované entity, pro který chcete vytvořit novou instanci.

    ![obrázek](resources/images/capture_app/register-without-enrollment-dropdown-menu-with-arrow.png)

5. V okamžiku, kdy vyberete typ trasované entity, se na obrazovce zobrazí formulář.

    Zobrazí se sekce "Profil". V této části můžete přidat data relevantní pro instanci sledované entity. Sekce profilu obsahuje především všechny atributy sledované entity spojené s typem sledované entity.

    ![obrázek](resources/images/capture_app/register-without-enrollment-form.png)

6. Vyplňte požadované informace.

   Pokud je typ trasované entity nakonfigurován tak, aby zachytil umístění:

    - Pokud se jedná o pole souřadnicového pole, můžete buď zadat souřadnice přímo, nebo můžete kliknout na ikonu **mapa** nalevo od pole souřadnic. Ten pak otevře mapu, kde můžete vyhledat místo nebo na něj přímo kliknout na mapě.

    - Pokud jde o pole polygon, můžete kliknout na ikonu **mapa** nalevo od pole. Otevře se mapa, kde můžete vyhledat místo a zachytit polygon (tlačítko v pravém horním rohu mapy).

7. Kliknutím na tlačítko **Uložit nový** zaregistrujte instanci trasované entity.
8. Nyní se zobrazí výzva k ovládacímu panelu instance trasované entity.

   Ovládací panel zobrazí relevantní informace o nově vytvořené instanci trasované entity.

### Se zápisem do programu { #with-a-program-enrollment }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte trasovací program podle vašeho výběru podobný obrázku níže.

    ![vytvořit novou událost](resources/images/capture_app/register-and-enroll-program-selection.png)

4. Klikněte na rozbalovací tlačítko „Nový“ a poté na první možnost.

    První možnost bude vypadat podobně jako na obrázku níže. Text v našem příkladu je „Program New person in Child programme“. Kliknutím na tuto možnost budete vyzváni na stránku registrace a registrace programu, který jste vybrali. ![vytvořit novou událost](resources/images/capture_app/register-and-enroll-dropdown-button-new-person-in-program.png)

5. Nyní uvidíte formulář podobný obrázku níže.

    Formulář bude mít dvě části. První část má název „Zápis“. Zde přidáte všechny informace relevantní pro registraci do tohoto programu. Druhá sekce má nadpis „Profil“, do které přidáte data relevantní k instanci trasované entity. Sekce profilu obsahuje především všechny atributy trasované entity spojené s programem nebo typem trasované entity.

    ![vytvořit novou událost](resources/images/capture_app/register-and-enroll-form.png)

6. Vyplňte požadované informace pro obě části. Pokud je typ sledované entity nakonfigurován tak, aby zachytil umístění:

    - Pokud se jedná o pole souřadnicového pole, můžete buď zadat souřadnice přímo, nebo můžete kliknout na ikonu **mapa** nalevo od pole souřadnic. Ten pak otevře mapu, kde můžete vyhledat místo nebo na něj přímo kliknout na mapě.

    - Pokud jde o pole polygon, můžete kliknout na ikonu **mapa** nalevo od pole. Otevře se mapa, kde můžete vyhledat místo a zachytit polygon (tlačítko v pravém horním rohu mapy).

7. Kliknutím na tlačítko **Uložit nový** zaregistrujte instanci sledované entity.
8. Nyní se zobrazí výzva k ovládacímu panelu instance trasované entity.

   Ovládací panel zobrazí relevantní informace o nově vytvořené instanci trasované entity.

> **Poznámka**
>
> Některé datové prvky v události mohou být povinné (označené červenou hvězdičkou vedle štítku datového prvku). Než bude uživateli povoleno dokončit událost, musí být vyplněny všechny povinné datové prvky. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření povinných polí v nástroji Tracker and Event Capture“.** Pokud má uživatel toto oprávnění, povinné datové prvky nebudou vyžadovány a červená hvězdička nebude se zobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

> **Tip**
>
> Formulář pro zadávání údajů lze zobrazit také v **zobrazení řádku**. V tomto režimu jsou datové prvky uspořádány vodorovně. Toho lze dosáhnout kliknutím na tlačítko **Přepnout na zobrazení řádků** v pravém horním rohu formuláře pro zadávání údajů. Pokud jste aktuálně v **řádkovém zobrazení**, můžete přepnout na výchozí zobrazení formuláře kliknutím na tlačítko **Přepnout do zobrazení formuláře** v pravém horním rohu formuláře pro zadávání údajů.

### Zápis s automaticky generovanými událostmi { #enrollment-with-auto-generated-events }

Program lze nakonfigurovat tak, aby měl nula nebo více fází programu, které jsou automaticky generovány při novém zápisu. Tyto fáze budou automaticky generovány na základě konfigurace metadat, jak je vysvětleno níže.

Chcete-li nakonfigurovat automatické generování události, musíte provést následující kroky.

1. Otevřete aplikaci údržby

2. Vyberte kartu Program ![](resources/images/capture_app/auto-generated-01.png)

3. Vyberte program Trasování  - Tracker![](resources/images/capture_app/auto-generated-02.png)

4. Vyberte kartu Fáze programu ![](resources/images/capture_app/auto-generated-03.png)

5. Klikněte na scénu, kterou chcete nakonfigurovat ![](resources/images/capture_app/auto-generated-04.png)

6. Označte scénu jako automaticky generovanou ![](resources/images/capture_app/auto-generated-05.png)

Nyní bude pro každý nový zápis do tohoto programu automaticky vygenerována jedna událost. Jeden program může mít také více fází označených jako automaticky generované. Pro všechny automaticky generované události

a) organizační jednotka bude stejná, za jakou se uživatel hlásí, během registrace a

b) všechny akce budou součástí aktuálního zápisu.

Na základě konfigurace může být stav automaticky generované události buď AKTIVNÍ nebo PLÁNOVANÝ.

#### Aktivní typ události { #active-type-of-event }

Pokud je ve fázi vybráno "Otevřít formulář pro zadávání dat po zápisu", bude událost vygenerována do stavu AKTIVNÍ. Kromě data splatnosti se pro událost vypočítá také její datum provedení. Generování probíhá buď na základě data registrace nebo data incidentu. Datum přehledu můžete vybrat z rozbalovací nabídky "Datum přehledu k použití". ![](resources/images/capture_app/auto-generated-06.png)

Jak je znázorněno na obrázku, máte tři možnosti: a) Datum události b) Datum zápisu nebo c) Žádná hodnota. Výběr data hlášení jako "Datum incidentu" znamená, že datum provedení události i datum splatnosti budou stejné jako datum incidentu. Výběr data hlášení jako „Datum zápisu“ nebo „Žádná hodnota“ znamená, že datum provedení události i datum vypršení platnosti budou stejné jako datum zápisu.

#### Typ plánu události { #schedule-type-of-event }

Pokud není zaškrtnuto políčko "Otevřít záznam dat po zápisu", znamená to, že vygenerovaná událost bude PLÁNOVANOU událostí. Naplánovaná událost nemá datum provedení, ale pouze datum vypršení. Datum vypršení těchto budoucích událostí se počítá buď na základě data registrace nebo data incidentu. Pokud je zaškrtnutý příznak níže, referenčním datem je datum zápisu, pokud příznak není zaškrtnutý, použije se datum incidentu. ![](resources/images/capture_app/auto-generated-07.png)

Pokud není uvedeno žádné datum incidentu, referenční datum se vrátí k datu zápisu bez ohledu na to, zda je zaškrtnutý příznak výše.

U událostí typu SCHEDULE může uživatel také nakonfigurovat "Plánované dny od začátku". Což znamená, že pokud má etapa číslo v části „Plánované dny od začátku“, referenční datum se o toto číslo zvýší. V níže uvedeném příkladu prodlužujeme splatnost o 30 dní. ![](resources/images/capture_app/auto-generated-08.png)

Pokud „Plánované dny od začátku“ neobsahuje číslo nebo obsahuje 0, použije se referenční datum, aniž by se k němu přidávaly dny.

### Možná detekce duplikátů { #possible-duplicates-detection }

V obou případech registrace instance trasované entity (s registrací nebo bez registrace) vás systém upozorní na možné duplikáty. Upozorňujeme, že aby se zobrazilo varování o duplikátech, je třeba správně nakonfigurovat programy prostřednictvím aplikace pro údržbu.

Chcete-li nakonfigurovat program prostřednictvím aplikace Údržba, budete muset:

1. Otevřete aplikaci údržby. ![](resources/images/capture_app/duplicates-maintenance-config-00.png)

2. V sekci program vyberte svůj program. Pro tento příklad vybereme Child Program. ![](resources/images/capture_app/duplicates-maintenance-config-01.png)

3. Vyberte kartu Atributy. ![](resources/images/capture_app/duplicates-maintenance-config-02.png)

4. Povolte vyhledávání duplicit kontrolou atributů programu jako prohledávatelné ![](resources/images/capture_app/duplicates-maintenance-config-03.png)

Atributy, které jste vybrali jako „Prohledávatelné“, budou atributy, které systém použije k detekci možných duplikátů.
Vysvětlíme to na příkladu, který demonstruje detekci možných duplikátů při zápisu dítěte do Programu dětí.

1. Otevřete aplikaci **Capture**. ![](resources/images/capture_app/duplicates-on-creation-00.png)

2. Vyberte svou organizační jednotku a program z nabídky nahoře. ![](resources/images/capture_app/duplicates-on-creation-01.png)

3. Klikněte na "Nový" -> "Nová osoba v dětském programu" ![](resources/images/capture_app/duplicates-on-creation-02.png)

4. Do formuláře vyplňte křestní jméno. **Pamatujte si, že křestní jméno, které jsme v aplikaci pro údržbu zaškrtli jako „Vyhledatelné“.** Je to proto, že jsme zaškrtli křestní jméno jako „Vyhledatelné“, takže systém začne hledat možné duplikáty, které se shodují se jménem Sarah jako vy viz obrázek níže. ![](resources/images/capture_app/duplicates-on-creation-03.png)

5. Klikněte na odkaz s textem "Možné duplikáty" ![](resources/images/capture_app/duplicates-on-creation-04.png)

6. Podívejte se na možné duplikáty ![](resources/images/capture_app/duplicates-on-creation-05.png)

> **Tip**
>
> Detekci duplikátů pro sledované typy entit můžete nakonfigurovat stejným způsobem jako u programů.

### Provádění pravidel programu { #program-rules-execution }

V obou případech registrace instance trasované entity (s registrací nebo bez registrace) systém spustí pravidla programu, která jste nakonfigurovali. Pravidla lze konfigurovat v aplikaci pro údržbu.

Chcete-li vidět provádění pravidla při registraci instance trasované entity, budete muset provést následující kroky.

1. Nakonfigurujte pravidlo v aplikaci pro údržbu. Pro příklad níže jsme nakonfigurovali pravidlo, které vyvolá varování, když je datum narození méně než rok.

2. Otevřete aplikaci **Capture**. ![](resources/images/capture_app/duplicates-on-creation-00.png)

3. Vyberte svou organizační jednotku a program z nabídky nahoře. ![](resources/images/capture_app/program-rules-on-creation-00.png)

4. Doplňte datum narození s hodnotou, která je kratší než rok. V našem případě je to 27. ledna 2021. ![](resources/images/capture_app/program-rules-on-creation-01.png)

5. Nyní budete moci vidět varování vytvořené pravidlem programu pod polem data narození. ![](resources/images/capture_app/program-rules-on-creation-02.png)

## Přidání vztahu { #capture_add_relationship }

Vztahy lze přidat buď během registrace, úpravy nebo prohlížení události. Aktuálně **aplikace Capture** podporuje pouze vztahy _Událost ku instanci trasované entity_.

1. V případě události klikněte na **Přidat vztah**.

2. Vyberte typ vztahu, který chcete vytvořit.

Nyní máte dvě možnosti:

-   **Odkaz na existující instanci trasované entity** nebo

-   **Vytvořit novou instanci trasované entity**.

![možnosti vztahu](resources/images/capture_app/relationship_options.png)

### Odkaz na existující instanci trasované entity { #link-to-an-existing-tracked-entity-instance }

1. Klikněte na **Odkaz na existující instanci trasované entity**.

-   Zobrazí se některé možnosti hledání **instance trasované entity**. Máte možnost vybrat si **program**. Pokud je vybrán **program**, atributy jsou odvozeny od vybraného **programu**. Pokud není vybrán žádný **program**, budou viditelné pouze atributy, které patří do **Instance trasované entity**.

      ![hledat instanci trasované entity](resources/images/capture_app/search_tei.png)

    -   Pokud je **Instance trasované entity** nebo **program** nakonfigurován s jedinečným atributem, lze tento atribut použít k vyhledání konkrétní **instance trasované entity** nebo **programu**. Tento atribut by měl být uveden samostatně. Po vyplnění pole jedinečného atributu klikněte na tlačítko **Hledat** umístěné přímo pod polem jedinečného atributu.

    -   Pokud má **Instance trasované entity** nebo **program** atributy, pak je lze použít k vyhledávání rozšířením pole **Hledat podle atributů**. Po vyplnění všech požadovaných polí atributů klikněte dole na tlačítko **Hledat podle atributů**. Hledání můžete také omezit nastavením **Rozsah organizační jednotky**. Pokud je nastaveno na _Všechny přístupné_, budete hledat **Instance trasované entity** ve všech organizačních jednotkách, ke kterým máte přístup. Pokud vyberete _Vybrané_, budete vyzváni k výběru organizačních jednotek, ve kterých chcete hledat.

2. Po úspěšném vyhledávání se zobrazí seznam **trasovaných Instancí entity**, které odpovídají kritériím vyhledávání. Chcete-li vytvořit vztah, klikněte na tlačítko **Odkaz** na **Trasovaná instance entity**, ke které chcete vytvořit vztah.

-   Pokud jste nenašli hledanou **instanci trasované entity**, můžete kliknout na tlačítka **Nové hledání** nebo **Upravit hledání**. **Nové hledání** vás přenese na nové prázdné vyhledávání, zatímco **Upravit hledání** vás vrátí zpět k právě provedenému vyhledávání, přičemž budou zachována kritéria vyhledávání.

### Vytvořte novou instanci trasované entity { #create-new-tracked-entity-instance }

1. Klikněte na **Vytvořit novou instanci trasované entity**.

-   Nyní se vám zobrazí formulář pro registraci nové **instance trasované entity**. Můžete si vybrat, zda budete registrovat s programem nebo bez něj. Pokud je vybrán program, bude do uvedeného programu zaregistrována nová **instance trasované entity**. Můžete také změnit **organizační jednotku** odebráním automaticky nastavené jednotky a výběrem nové.

    ![registrovat novou instanci trasované entity](resources/images/capture_app/register_tei.png)

2. Vyplňte požadované (a případně povinné) atributy a podrobnosti registrace.

3. Klikněte na **Vytvořit instanci trasované entity a odkaz**.

> **Poznámka**
>
> Při vyplňování údajů se můžete setkat s upozorněním, že byl nalezen možný duplikát. Kliknutím na varování můžete tyto duplikáty zobrazit. Pokud je duplikát shodný, můžete kliknout na tlačítko **Propojit** a propojit tuto **instanci trasované entity**. Pokud se varování zobrazuje i po dokončení vyplňování dat, tlačítko **Vytvořit instanci trasované entity a propojit** neuvidíte. Místo toho se vám zobrazí tlačítko s názvem **Zkontrolovat duplikáty**. Po kliknutí na toto tlačítko se zobrazí seznam možných duplikátů. Pokud se některý z těchto duplikátů shoduje s **instancí trasované entity**, kterou se pokoušíte vytvořit, můžete kliknout na tlačítko **Propojit**, pokud ne, kliknutím na tlačítko **Uložit jako novou osobu** zaregistrovat novou **Instanci trasované entity**.

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

> **Tip**
>
> Pořadí datových prvků můžete reorganizovat jejich přetažením do seznamu.

## Filtrování seznamu událostí { #capture_filter_event_list }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte program.

   Všechny události registrované k vybranému programu se zobrazí v seznamu.

   V horní části seznamu událostí jsou tlačítka se stejnými názvy jako záhlaví sloupců v seznamu.

4. Pomocí tlačítek v horní části seznamu můžete filtrovat podle data sestavy nebo konkrétního datového prvku.

    ![filtrování události](resources/images/capture_app/filter_event.png)

> **Poznámka**
>
> Různé typy datových prvků jsou přizpůsobeny různými způsoby. Například datový prvek **Číslo** zobrazí filtrování, zatímco datový prvek **Text** vás požádá o zadání vyhledávacího dotazu, na který chcete filtrovat.

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

> **Poznámka**
>
> Seznam událostí si můžete stáhnout ve formátech JSON, XML nebo CSV.

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

    > **Note**
    >
    > An asterisk(\*) is appended to the view name when the view has unsaved changes.

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

## Vyhledejte instance trasovaných entit { #search-for-tracked-entity-instances }

### V rozsahu programu { #in-program-scope }

1. Otevřete aplikaci **Capture**.

2. Vyberte program.

   Uvidíte pouze programy přidružené k vybrané organizační jednotce a programy, ke kterým máte přístup, a které jsou sdíleny s vaší skupinou uživatelů prostřednictvím sdílení na úrovni dat.

3. Pokud má program nastavenou kombinaci kategorií, bude nutné vybrat možnost kategorie.

4. Klikněte na tlačítko Najít.

5. V rozbalovací nabídce klikněte na první možnost.

    ![](resources/images/capture_app/search-by-attributes-find-button.png)

   Tyto kroky vás přenesou na stránku vyhledávání. Tam na základě konfigurace vaší organizace uvidíte různé atributy, pomocí kterých můžete vyhledávat. Příklad toho, jak to vypadá, je následující.

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-0.png)

   Chcete-li provést vyhledávání nyní:

6. Vyplňte atributy, pomocí kterých chcete hledat.

7. Klikněte na tlačítko **Hledat podle atributů**.

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-1.png)

8. Výsledky vyhledávání se zobrazí následovně.

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-2.png)

   V tomto seznamu vidíte položky, které odpovídají vašemu vyhledávání. U každého záznamu můžete mít celkem tři možnosti.

   a. Kliknutím na tlačítko "Zobrazit ovládací panel" můžete zobrazit ovládací panel pro **Instanci trasované entity**

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-5.png)

   b. Aktivní registraci **instance trasované entity** můžete zobrazit kliknutím na tlačítko „Zobrazit aktivní registraci“

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-3.png)

   c. Můžete znovu zapsat **instanci trasované entity** do aktuálního programu, ve kterém hledáte.

    ![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-4.png)

#### Zpětné vyhledávání { #fallback-search }

Proveďte úplné vyhledávání, jak je popsáno výše. Pokud má vyhledávání, které jste provedli, výsledky, zobrazí se. Skutečná **instance trasované entity**, kterou hledáte, však může být v jiném programu. V takovém případě možná budete chtít rozšířit vyhledávání na další programy. Toto se nazývá zpětné vyhledávání.

Chcete-li provést zpětné vyhledávání, jednoduše stiskněte tlačítko ve spodní části s nápisem „Hledat ve všech programech“.

> **Poznámka**
>
> Zpětné vyhledávání je možné pouze při vyhledávání v rámci programu.

![](resources/images/capture_app/search-by-attributes-fallback-overview-0.png)

### V oboru typu sledované entity { #in-tracked-entity-type-scope }

1. Otevřete aplikaci **Capture**.

2. Kliknutím na tlačítko **Najít** otevřete vyhledávací stránku.

3. Klikněte na rozevírací nabídku a vyberte typ entity, kterou chcete vyhledat.

    ![](resources/images/capture_app/search-by-attributes-domain-selector-overview-0.png)

4. Proveďte výběr ze seznamu.

    ![](resources/images/capture_app/search-by-attributes-domain-selector-overview-1.png)

   Na základě konfigurace vaší organizace uvidíte různé atributy, pomocí kterých můžete vyhledávat. Příklad toho, jak to vypadá, je následující.

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-0.png)

   Chcete-li provést vyhledávání nyní:

5. Vyplňte atributy, pomocí kterých chcete hledat.

6. Klikněte na tlačítko Hledat podle atributů.

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-1.png)

7. Výsledky vyhledávání se zobrazí následovně.

    ![](resources/images/capture_app/search-by-attributes-on-scope-tetype-overview-2.png)

   V tomto seznamu vidíte položky, které odpovídají vašemu vyhledávání. U každého záznamu máte možnost kliknout na tlačítko „Zobrazit ovládací panel“ a zobrazit ovládací panel pro **trasovanou entitu**.

### Příliš mnoho výsledků { #too-many-results-functionality }

Program nebo typ trasované entity, který prohledáváte, může být konfigurován s omezením počtu výsledků, které jsou z vyhledávání vráceny. Pokud vaše výsledky vyhledávání překročí tento limit, zobrazí se varovná zpráva, jako je ta níže.

![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-too-many-results-message.png)

### Stránkování { #pagination }

Stránka s výsledky zobrazuje až pět výsledků najednou. Měli byste se pokusit použít konkrétní vyhledávací kritéria, aby nebylo příliš mnoho shod. Pokud však existuje více než pět výsledků, můžete zobrazit další výsledky pomocí tlačítka **>** na konci stránky.

![](resources/images/capture_app/search-by-attributes-on-scope-program-overview-pagination.png)

## Seznam trasovaných instancí entit zapsaných v programu { #list-tracked-entity-instances-enrolled-in-program }

1. Otevřete aplikaci **Capture**.

2. Vyberte organizační jednotku.

3. Vyberte trasovací program.

4. Program může mít přidružené kategorie (příkladem takové kategorie by byl implementující partner). Pokud je to váš případ, vyplňte je.

### Filtrovat seznam { #filter-the-list }

Filtrujte jej pomocí tlačítek nad samotným seznamem.

![](resources/images/capture_app/tei_list_filters.png)

Příkladem může být filtrování seznamu tak, aby se zobrazovaly pouze trasované instance entit, kde vám byla přiřazena událost: Klikněte na filtr „Přiřazeno k“ (1), vyberte „Já“ (2) a poté „Použít“ změny (3).

![](resources/images/capture_app/tei_list_filter_example.png)

### Seřadit seznam { #sort-the-list }

Kliknutím na jedno z hlaviček sloupců seřadíte seznam podle tohoto sloupce. Vedle záhlaví sloupce se zobrazuje malá šipka, která označuje aktuální pořadí řazení. Opětovným kliknutím přepnete mezi vzestupným a sestupným pořadí.

![](resources/images/capture_app/tei_list_sort_order.png)

### Upravte rozložení seznamu { #modify-the-list-layout }

Můžete vybrat, které sloupce se mají v seznamu zobrazit, a také reorganizovat pořadí sloupců.

Klikněte na ikonu **ozubeného kola** v pravém horním rohu seznamu. Zaškrtněte políčka u sloupců, které chcete zobrazit (1), a přeuspořádejte sloupce přetažením (2).

![](resources/images/capture_app/tei_list_column_layout.png)

### Načítání předdefinovaného zobrazení seznamu { #loading-a-predefined-list-view }

Předdefinovaná zobrazení seznamu najdete nad filtry seznamu. Kliknutím načtete pohled.

![](resources/images/capture_app/tei_list_predefined_views.png)

## Informace o implementátorovi / správci { #implementer_info }

### Ukládání metadat do mezipaměti { #metadata_caching }

Z důvodu výkonu aplikace Capture ukládá do paměti metadata v klientském prohlížeči. Když se na serveru aktualizují metadata, je třeba změny šířit na klienty, kteří již metadata uložili do mezipaměti. V závislosti na změně se to děje jedním ze tří způsobů:

1. Pokud je změna vázána na program, budete muset zvýšit verzi programu pro daný program. Například pokud změníte datové prvky v programu nebo v pravidle programu, je třeba zvýšit verzi vázaného programu.

2. Pokud změna NENÍ vázána na program, budete muset zvýšit JAKOUKOLI verzi programu, aby se změna mohla rozšířit na klienty. Příkladem jsou změny konstant, úrovní organizačních jednotek nebo skupin organizačních jednotek.

3. Výjimkou z výše uvedených dvou pravidel jsou sady možností. Sady možností mají svou vlastní vlastnost verze, tj. Zvýšení verze sady možností by mělo zajistit, že se metadata sady možností rozšíří na klienty.

## Ovládací panel zápisu { #enrollment-dashboard }

### Přístup k ovládacímu panelu zápisu přes adresu URL { #reaching-the-enrollment-dashboard-via-url }

Na ovládací panel zápisu se dostanete buď zadáním do adresního řádku prohlížeče, nebo pomocí uživatelského rozhraní aplikace Capture. V této části se zaměřujeme na první případ použití, kdy do adresního řádku zadáte nebo vložíte adresu URL, ke které chcete získat přístup.

![](resources/images/capture_app/enrollment-dash-01.png)

Jedním ze způsobů, jak se dostat na ovládací panel registrace a zobrazit zápis konkrétní instance trasované entity, je použití _pouze_ id zápisu. Například odkaz .../dhis-web-capture/#/?enrollmentId=wBU0RAsYjKE vás přenese na ovládací panel pro zápis s id `wBU0RAsYjKE`.

Horní část ovládacího panelu definuje váš kontext. Například na obrázku níže je kontext následující, vybraný program je "Child Programme", organizační jednotka je "Ngelehun CHC", vybraná osoba je "Anna Jones" a vybraná registrace je "2017-11-16 11 :38".

![](resources/images/capture_app/enrollment-dash-02.png)

Kontext můžete změnit kliknutím na tlačítko „x“.

![](resources/images/capture_app/enrollment-dash-03.png)

#### Zrušení výběru programu { #deselecting-the-program }

Když zrušíte výběr programu, uvidíte následující

![](resources/images/capture_app/enrollment-dash-05.png)

##### Výběr programu se zápisy { #selecting-a-program-with-enrollments }

Když jsou výběry programu _a_ zápisu prázdné, musíte nejprve vybrat program. Pokud má instance trasované entity (v tomto případě „Anna Jones“) zápis ve vybraném programu, zobrazí se následující zpráva.

![](resources/images/capture_app/enrollment-dash-09.png)

##### Výběr programu s nulovým počtem zápisů { #selecting-a-program-with-zero-enrollments }

Pokud instance trasované entity (v tomto případě „Anna Jenkins“) nemá zápisy ve vybraném programu, zobrazí se zpráva vysvětlující, že pro daný program nejsou žádné zápisy. Budete mít také možnost zapsat „Annu Jenkins“ do tohoto programu.

![](resources/images/capture_app/enrollment-dash-10.png)

##### Výběr programu události { #selecting-an-event-program }

Když vyberete program události, uvidíte následující. (Pamatujte si, že programy událostí nemají v systému zápisy, ale pouze trasovací programy).

![](resources/images/capture_app/enrollment-dash-11.png)

Budete mít také možnost buď vytvořit novou událost pro vybraný program, nebo zobrazit pracovní seznamy pro vybraný program.

##### Výběr programu s jiným typem trasované entity { #selecting-a-program-with-a-different-tracked-entity-type }

Když je vámi vybraným typem sledované entity osoba, jako v našem příkladu s Annou Jenkinsovou, a vyberete program, který není typu osoba, ale například typu případu malárie, uvidíte následující.

![](resources/images/capture_app/enrollment-dash-12.png)

Máte také možnost zaregistrovat instanci trasované entity do programu, který jste vybrali.

#### Zrušení výběru organizační jednotky { #deselecting-the-organisation-unit }

Když zrušíte výběr organizační jednotky, uvidíte následující

![](resources/images/capture_app/enrollment-dash-06.png)

#### Zrušení výběru instance trasované entity { #deselecting-the-tracked-entity-instance }

Když zrušíte výběr instance trasované entity, v tomto případě „Anna Jones“ se dostanete do pracovních seznamů v tomto programu Tracker.

![](resources/images/capture_app/enrollment-dash-07.png)

#### Zrušení výběru zápisu { #deselecting-the-enrollment }

Když zrušíte výběr zápisu, uvidíte následující

![](resources/images/capture_app/enrollment-dash-08.png)

# Použití aplikace Event Capture { #event_capture_app }

## O aplikaci Zachycení Události { #about_event_capture_app }

![](resources/images/event_capture/event_list.png)

V aplikaci **Zachycení Události** registrujete události, ke kterým došlo v konkrétním čase a místě. Událost se může stát v kterémkoli daném okamžiku. To je v rozporu s rutinními daty, která lze zachytit v předdefinovaných pravidelných intervalech. Události se někdy nazývají případy nebo záznamy. V DHIS2 jsou události propojeny s programem. Aplikace **Zachycení Události** vám umožňuje vybrat organizační jednotku a program a určit datum, kdy k události došlo, před zadáním informací o události.

Aplikace **Zachycení Události** funguje online i offline. Pokud připojení k internetu poklesne, můžete pokračovat v zachycování událostí. Události budou uloženy lokálně ve vašem webovém prohlížeči (klientovi). Po obnovení připojení vás systém požádá o nahrání lokálně uložených dat. Systém poté odešle data na server, kde jsou data uložena.

> **Poznámka**
>
> Pokud zavřete webový prohlížeč v režimu offline, není možné znovu otevřít nové okno webového prohlížeče a pokračovat v pracovní relaci. Data se však budou i nadále ukládat lokálně a lze je nahrát na server, až bude zařízení příště online a vy se přihlásíte na server.

-   Uvidíte pouze programy přidružené k organizační jednotce, kterou jste vybrali, a programy, ke kterým máte přístup prostřednictvím své uživatelské role.

-   Během registrace jsou podporovány chybové i varovné zprávy přeskočení logiky i ověření.

-   Když zavřete organizační jednotku, nemůžete registrovat ani upravovat události v této organizační jednotce v aplikaci **Zachycení Události**. Stále můžete zobrazit a filtrovat seznam událostí a zobrazit podrobnosti události.

-   Je podporováno vyhodnocení výrazu za běhu. Pokud má program definované indikátory a v okamžiku, kdy jsou vyplněny všechny hodnoty související s výrazem indikátoru, systém vypočítá indikátor a zobrazí výsledek.

    ![](resources/images/event_capture/event_editing.png)

-   **Řazení:** Toho lze dosáhnout kliknutím na ikonu řazení v záhlaví každého sloupce. Červená ikona řazení implikuje aktuální sloupec řazení. Funkce řazení však funguje pouze na zobrazené stránce. V současné době není možné provádět třídění ze strany serveru.

-   **Filtrování:** Toto se provádí kliknutím na malou ikonu vyhledávání zobrazenou napravo od záhlaví každého sloupce. Kliknutím na ni získáte vstupní pole pro zadání kritérií filtrování. Systém začne používat filtr v okamžiku, kdy uživatel začne psát. Během filtrování je možné definovat počáteční a koncové datum pro datové prvky typu data a dolní a horní limity pro typy čísel. Filtrování na straně serveru momentálně není podporováno.

## Zaregistrujte událost { #event_capture_register_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Uvidíte pouze programy přidružené k vybrané organizační jednotce a programy, ke kterým máte přístup prostřednictvím své uživatelské role.

4.  Klikněte na **Registrovat událost**.

5.  Vyberte datum.

6.  Vyplňte požadované informace.

    Pokud je programová fáze programu nakonfigurována tak, aby zachytávala souřadnice GPS, můžete souřadnice zadat dvěma způsoby:

    -   Zadejte hodnoty přímo do příslušných polí.

    -   Vyberte místo na mapě. Možnost Mapa také zobrazuje polygony a body definované pro organizační jednotky.

7.  Klikněte na **Uložit a přidat nové** nebo **Uložit a vrátit se**.

> Poznámka: Některé datové prvky v události mohou být povinné (označené červenou hvězdou vedle štítku datového prvku). To znamená, že všechny povinné datové prvky musí být vyplněny, než bude uživateli povoleno událost uložit. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření požadovaných polí v nástroji Trasovač and Zachycení Události“.** Pokud má uživatel toto oprávnění, nebude nutné před uložením vyplňovat povinné datové prvky a červená hvězda se nezobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

## Upravit událost { #event_capture_edit_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost, kterou chcete upravit, a vyberte **Upravit**.

5.  Upravte podrobnosti události a klikněte na **Aktualizovat**.

## Úpravy událostí v mřížce { #event_capture_edit_event_grid }

Funkce **Upravit v mřížce** umožňuje upravit vybranou událost v tabulce, ale pouze ty sloupce (datové prvky) viditelné v mřížce. Pokud potřebujete více sloupců, použijte **Zobrazit / skrýt sloupce** a určete, které sloupce se mají v seznamu zobrazit.

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost, kterou chcete upravit, a vyberte **Upravit v mřížce**.

5.  Upravte podrobnosti události.

6.  Kliknutím na jinou událost režim úprav zavřete.

## Sdílejte události v režimu úprav { #event_capture_share_event_edit_mode }

Událost můžete sdílet v režimu úprav prostřednictvím její webové adresy.

1.  Otevřete aplikaci **Zachycení Události**.

2.  V režimu úprav otevřete událost, kterou chcete sdílet.

3.  Zkopírujte adresu URL.

    Ujistěte se, že adresa URL obsahuje parametry „event“ a „ou“ (organizační jednotka).

4.  Vložte adresu URL do metody sdílení podle vašeho výběru, například e-mail nebo zprávu v rámci DHIS2.

    Pokud nejste přihlášeni k DHIS2, když kliknete na odkaz, budete požádáni, abyste tak učinili, a poté přejdete na ovládací panel.

## Zobrazit historii auditu událostí { #event_capture_view_event_audit_history }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost a vyberte **Historie auditu**.

## Smazat událost { #event_capture_delete_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost a vyberte **Odebrat**.

5.  Kliknutím na **Odstranit** potvrďte odstranění.

## Upravte rozložení seznamu událostí { #event_capture_modify_event_list_layout }

Můžete vybrat, které sloupce se mají zobrazit nebo skrýt v seznamu událostí. To může být užitečné například v případě, že máte k programové fázi přiřazen dlouhý seznam datových prvků. Jakmile upravíte rozložení, uloží se do vašeho uživatelského profilu. Pro různé programy můžete mít různá rozvržení.

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na ikonu **Zobrazit / skrýt sloupce**.

5.  Vyberte sloupce, které chcete zobrazit, a klikněte na **Zavřít**.

## Vytiskněte seznam událostí { #event_capture_print_event_list }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na **Vytisknout seznam**.

## Stáhněte si seznam událostí { #event_capture_download_event_list }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na ikonu **Stáhnout** a vyberte formát.

    Seznam událostí si můžete stáhnout ve formátech XML, JSON nebo CSV.

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

Hledání se používá k hledání TEI v organizačních jednotkách, ke kterým má uživatel přístup k vyhledávání. To lze použít, pokud chcete najít TEI, ale nevíte, do které organizační jednotky nebo programu byl TEI zapsán. Existují dva způsoby, jak to udělat: S kontextem programu i bez něj. Je třeba nakonfigurovat vyhledávací pole. Pro konfiguraci vyhledávání v kontextu programu se to provádí samostatně pro každý program v aplikaci pro údržbu programu. Pro konfiguraci vyhledávání bez kontextu programu se to provádí jednotlivě pro každý typ sledované entity v aplikaci pro údržbu typu sledované entity.

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

Zápis do programu lze znovu otevřít, pokud byl zápis dokončen. Není však možné znovu otevřít zápis, pokud ve stejném programu probíhá další aktivní zápis (protože se nemůžete přihlásit do programu, pokud již pro daný program existuje jiná aktivní zápis).

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

# Schválení dat { #data_approval }

DHIS2 má volitelnou funkci, která umožňuje autorizovaným uživatelům schvalovat zadaná data. Umožňuje zkontrolovat a schválit data na vybraných úrovních v hierarchii organizačních jednotek, takže schválení sleduje strukturu hierarchie od nižších úrovní po vyšší úrovně.

Data jsou schválena pro kombinaci (a) období, (b) organizační jednotky a (c) pracovního postupu. Data mohou být schválena pro organizační jednotku, pro kterou jsou zadány, a také pro organizační jednotky vyšší úrovně, do kterých jsou data agregována. V rámci nastavení systému můžete vybrat úroveň (úrovně) organizační jednotky, na kterých jsou data schválena. Může být schválen na vyšších úrovních až poté, co byl schválen pro všechny podřazené této organizační jednotky na nižších úrovních pro stejný pracovní postup a období. Když schválíte pracovní postup, schválí se data pro všechny datové sady, které byly k tomuto pracovnímu postupu přiřazeny.

Po schválení kombinace období, organizační jednotky a pracovního toku budou datové sady spojené s tímto pracovním tokem pro dané období a organizační jednotku uzamčeny a jakékoli další zadávání nebo úpravy dat budou zakázány, dokud nebudou nejprve schváleny.

Například následující diagram ukazuje, že data již byla schválena pro organizační jednotky C a D, pro dané období a pracovní postup. Nyní může být schválen pro organizační jednotku B pro stejné období a pracovní postup. Není však připraven ke schválení pro organizační jednotku A. Než bude možné ji schválit pro organizační jednotku A, musí být schválena pro B a pro všechny další podřazené organizační jednotky A pro dané období a pracovní postup.

![Schvalování v organizační
jednotce](resources/images/data_approval/approval_hierarchy.png){.center width=50% }

## Schvalování a přijímání { #data_approvals_approving_accepting }

DHIS2 podporuje dva různé typy schvalovacích procesů: buď jednostupňový proces, kde jsou data schválena na každé úrovni, nebo dvoustupňový proces, kdy jsou data nejprve schválena a poté přijata na každé úrovni. To ilustruje následující diagram:

![Schvalování a
přijímám](resources/images/data_approval/approval_level_steps.png){.center width=69% }

V jednokrokovém procesu jsou data schválena na jedné úrovni a poté schválena na další vyšší úrovni. Dokud nebude schválen na další vyšší úrovni, může být na první úrovni neschválen. (Například pokud byla data schválena moje chyba, umožňuje to schvalovateli vrátit jejich chybu zpět.) Jakmile jsou data schválena na další vyšší úrovni, nemusí být schválena na nižší úrovni, pokud nebudou nejprve schválena na vyšší úrovni.

V dvoustupňovém procesu jsou data schválena na jedné úrovni a poté je schválení přijato na stejné úrovni. Toto přijetí provádí uživatel, který je oprávněn schvalovat data na další vyšší úrovni. Jakmile jsou data přijata, nemusí být změněna nebo neschválena, pokud nebudou nejprve _nepřijata_.

Proces ve dvou krocích DHIS2 nevyžaduje. Je to volitelný krok pro uživatele, který kontroluje data na další vyšší úrovni. Výhodou je uzamčení přijetí z níže uvedené úrovně, takže se recenzent nemusí obávat, že by se data mohla při kontrole kontrolovat zdola. Může jej také použít uživatel vyšší úrovně ke sledování toho, která data nižší úrovně již byla zkontrolována.

Dvoustupňový proces lze aktivovat zaškrtnutím **Před schválením je vyžadováno přijetí** v aplikaci SystemSettings v části Obecné.

## Autority pro schvalování údajů { #data_approvals_authorities }

Ke schválení dat vám musí být přiřazena role obsahující jedno z těchto oprávnění:

-   **Schválit data** - Můžete schválit data pro organizační jednotky, ke kterým jste přiřazeni. Toto oprávnění vám neumožňuje schvalovat data pro nižší úrovně pod organizační(mi) jednotkou(ami), ke kterým jste přiřazeni. To je užitečné k oddělení uživatelů oprávněných schvalovat na jedné úrovni od uživatelů oprávněných schvalovat na níže uvedených úrovních.

-   **Schválení dat na nižších úrovních** - Umožňuje schválit data pro všechny nižší úrovně pod organizačními jednotkami, které jsou vám přiřazeny. To je užitečné, pokud jste například uživatelem na úrovni okresu, jehož role zahrnuje schvalování dat pro všechna zařízení v tomto okrese, ale ne pro samotný okres. Pokud je vám přiděleno toto, stejně jako autorita _Schvaluje data_, můžete schválit data na úrovni organizační(ch) jednotek, kterým jste byli přiřazeni, a na jakékoli níže uvedené úrovni.

-   **Přijímá data na nižších úrovních** - Umožňuje přijímat data na úrovni těsně pod organizační(mi) jednotkami, které vám byly přiřazeny. Toto oprávnění lze udělit stejným uživatelům, kteří schvalují data. Nebo to může být dáno různým uživatelům, pokud chcete mít některé uživatele, kteří přijímají data z níže uvedené úrovně, a jinou sadu uživatelů, kteří schvalují data, aby přešli na další úroveň výše.

## Konfigurace schválení dat { #data_approvals_configuration }

V sekci aplikace _Údržba_ v části _Úroveň schválení dat_ můžete určit úrovně, na kterých chcete schválit data v systému. Klikněte na tlačítko Přidat nový na této stránce a vyberte úroveň organizační jednotky, na které chcete schválení. Bude přidán do seznamu nastavení schválení. Můžete nakonfigurovat systém pro schvalování dat na každé úrovni organizační jednotky nebo pouze na vybraných úrovních organizační jednotky.

Všimněte si, že když přidáte novou úroveň schválení, můžete volitelně zvolit sadu skupin možností kategorie. Tato funkce je popsána dále v této kapitole.

Také v údržbě pod _Data schválení pracovního toku_, můžete definovat pracovní postupy, které se použijí pro schválení dat. Každý pracovní postup lze přidružit k jedné, nebo více úrovním schválení. Jakékoli dva pracovní toky mohou fungovat na všech stejných úrovních schválení, jako jsou ostatní, některé na stejné a některé jiné úrovni nebo zcela odlišné úrovně.

Pokud chcete, aby byla data pro datovou sadu schválena podle pracovního postupu, přiřaďte pracovní postup k datové sadě, když přidáte nebo upravíte datovou sadu. Pokud nechcete, aby data pro datovou sadu podléhala schválení, nepřiřazujte této sadě dat žádný pracovní postup. U datových sad, které chcete schvalovat současně, je přiřaďte ke stejnému pracovnímu postupu. U datových sad, které chcete schválit nezávisle, přiřaďte každé datové sadě vlastní pracovní postup.

V části _Nastavení systému_ -> _Analytika_ můžete určit, která neschválená data (pokud existují) se objeví v analytice. Viz část „Nastavení Analytiky“ v této uživatelské příručce. Všimněte si, že uživatelé, kteří jsou přiřazeni k organizačním jednotkám, kde jsou data připravena ke schválení, mohou tato data vždy zobrazit v analytice, stejně jako uživatelé přiřazení k organizačním jednotkám na vyšší úrovni, pokud mají oprávnění _Schválit na nižších úrovních_ nebo _Zobrazit neschválené oprávnění k datům_.

## Viditelnost dat { #data_approvals_data_visibility }

Pokud je povolena možnost _Skrýt neschválená data v analytice_, data budou skryta před zobrazením uživateli přidruženými k vyšším úrovním. Při určování, zda by měl být datový záznam skrytý pro konkrétního uživatele, systém přidruží uživatele k určité úrovni schválení a porovná jej s úrovní, až na kterou byl datový záznam schválen. Uživatel je přidružen k úrovni schválení, která odpovídá úrovni organizační(ch) jednotek, s nimiž je propojena, nebo pokud na této úrovni neexistuje žádná úroveň schválení, další úroveň schválení spojená s úrovní organizační jednotky pod sebou. Uživateli bude umožněno zobrazit data, která byla schválena, a to až na úroveň bezprostředně pod její přidruženou úrovní schválení. Důvodem je to, že uživatel musí být schopen zobrazit data, která byla schválena níže, aby je mohl nakonec zobrazit a schválit sám.

Všimněte si, že pokud byl uživateli udělena autorita _Zobrazit neschválená data_ nebo _VŠE_ , bude moci zobrazit data bez ohledu na stav schválení.

_Zvažme následující příklad:_ Existují čtyři úrovně organizační jednotky s úrovněmi schválení spojenými s úrovní 2 a 4. _Uživatel A_ na úrovni země (1) bude spojen s úrovní schválení 1, protože úroveň schválení existuje na stejné úrovni jako na úrovni organizační jednotky. _Uživatel B_ je spojen s úrovní schválení 2, protože neexistuje žádná úroveň schválení přímo spojená s úrovní její organizační jednotky a úroveň schválení 2 je přímá úroveň níže. _Uživatel C_ je spojen s úrovní schválení 2. _Uživatel D_ je pod všemi úrovněmi schválení, což znamená, že vidí všechna data zadaná na nebo pod úrovní své organizační jednotky.

![Skrytí neschválených
dat](resources/images/data_approval/approval_data_hiding.png){.center}

V tomto příkladu pojďme zvážit některé scénáře:

-   Data se zadávají na úrovni zařízení: Data může zobrazit pouze _Uživatel D_, protože data ještě nebyla vůbec schválena.

-   Data jsou schválena od _Uživatele D_ na úrovni zařízení: Data se stanou viditelnými pro uživatele C a uživatele B, protože data jsou nyní schválena na jejich úrovni.

-   Data jsou schválena od _Uživatele C_ na úrovni okresu: Data se stanou viditelnými pro uživatele A, protože data jsou nyní schválena na úrovni bezprostředně pod sebou.

## Schvalování dat { #data_approvals_approving_data }

Chcete-li schválit data, přejděte na _Zprávy_ a vyberte _Schválení Dat_. Když toto hlášení zobrazuje data, která jsou nakonfigurována ke schválení, zobrazuje stav schválení dat v hlášení. Stav schválení bude jeden z následujících:

-   **Čekání na schválení organizačních jednotek na nižší úrovni** - Tato data ještě nejsou připravena ke schválení, protože je třeba je nejprve schválit pro všechny podřazené organizační jednotky této organizační jednotky, pro stejný pracovní postup a období.

-   **Připraveno ke schválení** - Tato data nyní mohou být schválena autorizovaným uživatelem.

-   **Schváleno** - Tyto údaje již byly schváleny.

-   **Schváleno a přijato** - Tyto údaje již byly schváleny a také přijaty.

Pokud jsou data, která prohlížíte, ve stavu schválení, na kterém lze jednat, a pokud máte dostatečné oprávnění, bude vám ve formuláři _Schválení Dat_ k dispozici jedna nebo více z následujících akcí:

-   **Schválit** - Schválit data, která dosud nebyla schválena, nebo která byla dříve schválena a pak byla neschválena.

-   **Neschválit** - Vraťte se k neschválenému stavu, který byl autorizován nebo přijat.

-   **Přijmout** - Přijmout data, která byla schválena.

-   **Nepřijmout** - Návrat do nepřijatých (ale stále schválených) údajů o stavu, které byly přijaty.

Chcete-li zrušit schválení dat pro danou organizační jednotku, musíte mít oprávnění schvalovat data pro tuto organizační jednotku nebo schvalovat data pro organizační jednotku vyšší úrovně, do které jsou tato data agregována. Důvod je následující: Pokud kontrolujete data ke schválení na vyšší organizační jednotce, měli byste zvážit, zda jsou data na nižších organizačních jednotkách přiměřená. Pokud všechna data nižší úrovně vypadají dobře, můžete data schválit na vyšší úrovni. Pokud některá data nižší úrovně vypadají podezřele, můžete data na nižší úrovni zrušit. To umožňuje, aby byla data znovu zkontrolována na nižší úrovni, v případě potřeby opravena a znovu schválena prostřednictvím úrovní organizační jednotky podle hierarchie.

## Schvalování podle sady skupin možností { #data_approvals_approving_by_cogs }

Při definování úrovně schválení určíte úroveň organizační jednotky, na které budou data schválena. Můžete také volitelně určit skupinu skupin možností možností. To je užitečné, pokud používáte skupiny možností kategorií k definování dalších dimenzí svých dat a chcete, aby schválení byla založena na těchto dimenzích. Následující příklady ilustrují, jak toho lze dosáhnout v rámci jedné skupiny skupin možností možností a pomocí více skupin skupin možností možností.

### Schvalování podle jedné sady skupin možností { #approving-by-one-category-option-group-set }

Předpokládejme například, že definujete sadu možností skupiny, která bude zastupovat nevládní organizace, které slouží jako partneři v oblasti zdravotní péče v jedné nebo více organizačních jednotkách. Každá skupina možností kategorie v této sadě představuje jiného partnera. Skupina možností kategorie pro partnera 1 může seskupovat možnosti kategorie (například kódy účtů financování), které tento partner používá jako dimenzi dat. Data zadaná partnerem 1 jsou tedy přiřazena možnosti kategorie ve skupině možností kategorie partner 1. Zatímco data zadaná partnerem 2 jsou přidělena možnosti kategorie ve skupině možností kategorie Partner 2:

<table align="center">
<caption> Příklad skupin kategorií možností </caption>
<thead>
<tr class="header">
<th> Sada skupin možností skupin </th>
<th> skupina možností kategorie </th>
<th> Možnosti kategorie </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Partner </td>
<td> Partner 1 </td>
<td> účet 1A, účet 1B </td>
</tr>
<tr class="even">
<td> Partner </td>
<td> Partner 2 </td>
<td> účet 2A, účet 2B </td>
</tr>
</tbody>
</table>

Každý partner mohl zadávat údaje pro své účty nezávisle na sobě, pro stejné nebo různé pracovní postupy, ve stejných nebo různých zařízeních. Například data lze zadávat a / nebo agregovat na následujících úrovních pro každého partnera, nezávisle na sobě:

![Příklad volby kategorie
skupiny](resources/images/data_approval/approval_partner_example.png){.center}

> **Tip**
>
> Funkci sdílení u možností kategorií a skupin možností kategorií můžete použít k zajištění toho, aby uživatel mohl zadávat data (a / nebo zobrazit data) pouze pro určité možnosti kategorií a skupiny. Pokud nechcete, aby uživatelé viděli data agregovaná nad rámec jejich přiřazených možností kategorií a / nebo skupin možností kategorií, můžete při přidávání nebo aktualizaci uživatele přiřadit _Vybraná omezení dimenze pro analýzu dat_.

Volitelně můžete definovat úrovně schválení pro data partnerů v rámci kterékoli nebo všech těchto úrovní organizační jednotky. Můžete například definovat některou nebo všechny následující úrovně schválení:

<table align="center">
<caption> Příklad Možnosti kategotie Skupin Nastavení úrovně schválení </caption>
<thead>
<tr class="header">
<th> Úroveň schválení </th>
<th> úroveň organizační jednotky </th>
<th> Sada skupin možností skupin </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> 1 </td>
<td> Země </td>
<td> Partner </td>
</tr>
<tr class="even">
<td> 2 </td>
<td> Okres </td>
<td> Partner </td>
</tr>
<tr class="odd">
<td> 3 </td>
<td> Zařízení </td>
<td> Partner </td>
</tr>
</tbody>
</table>

## Schvalování několika sadami skupin možností { #approving_by_multiple_category_option_group_sets }

Můžete také definovat úrovně schválení pro různé sady skupin možností kategorií. V pokračování příkladu předpokládejme, že máte různé agentury, které spravují financování různým partnerům. Například prostředky agentury A účty 1A a 2A, zatímco prostředky agentury B účty 1B a 2B. Mohli byste nastavit skupiny možností kategorií pro Agenturu A a Agenturu B a udělat je obě součástí sady skupin možností kategorií s názvem Agentura. Takže byste měli:

<table align="center">
<caption> Příklad sady skupin možností skupin s více kategoriemi </caption>
<thead>
<tr class="header">
<th> Sada skupin možností skupin </th>
<th> skupina možností kategorie </th>
<th> Možnosti kategorie </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Partner </td>
<td> Partner 1 </td>
<td> účet 1A, účet 1B </td>
</tr>
<tr class="even">
<td> Partner </td>
<td> Partner 2 </td>
<td> účet 2A, účet 2B </td>
</tr>
<tr class="odd">
<td> Agentura </td>
<td> Agentura A </td>
<td> účet 1A, účet 2A </td>
</tr>
<tr class="even">
<td> Agentura </td>
<td> Agentura B </td>
<td> účet 1B, účet 2B </td>
</tr>
</tbody>
</table>

Nyní předpokládejme, že na úrovni země chcete, aby každý partner schválil údaje zadané tímto partnerem. Jakmile je toto schválení hotové, chcete, aby každá agentura poté schválila data z účtů, které tato agentura spravuje. Nakonec chcete schválit údaje na úrovni zemí napříč všemi agenturami. Můžete to udělat definováním následujících úrovní schválení:

<table align="center">
<caption> Příklad Více skupin možností Skupina nastavení úrovní schválení </caption>
<thead>
<tr class="header">
<th> Úroveň schválení </th>
<th> úroveň organizační jednotky </th>
<th> Sada skupin možností kategorií</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> 1 </td>
<td> Země </td>
<td> </td>
</tr>
<tr class="even">
<td> 2 </td>
<td> Země </td>
<td> Agentura </td>
</tr>
<tr class="odd">
<td> 3 </td>
<td> Země </td>
<td> Partner </td>
</tr>
</tbody>
</table>

Pro stejnou úroveň organizační jednotky lze definovat více úrovní schválení. V našem příkladu by partner 1 schvaloval data pro celou zemi na úrovni schválení 3 z možností kategorií Účet 1A a Účet 1B. Dále by Agentura A schválila celostátní údaje na úrovni schválení 2 z možností kategorie Účet 1A (po schválení Partnerem 1) a Účet 2A (po schválení Partnerem 2.) A konečně, po schválení všemi agenturami mohou celorepubliková data být schválen na úrovni schválení 1 ve všech volbách kategorie. Všimněte si, že úroveň schválení 1 neurčuje sadu skupin možností kategorií, což znamená, že slouží ke schválení dat napříč všemi možnostmi kategorií.

Tento příklad má být pouze ilustrativní. Můžete definovat tolik skupin možností kategorií, kolik potřebujete, a tolik úrovní schválení, kolik potřebujete, na stejné úrovni organizační jednotky pro různé sady skupin možností kategorií.

Pokud máte více úrovní schválení pro různé skupiny skupin voleb možností na stejné úrovni organizační jednotky, můžete změnit pořadí schválení v sekci _Nastavení_ v části _Nastavení schválení systému_. Stačí kliknout na úroveň schválení, kterou chcete přesunout, a vybrat _Posunout nahoru_ nebo _Posunout dolu_. Pokud máte úroveň schválení bez nastavených skupin skupin možností, musí to být nejvyšší úroveň schválení pro tuto úroveň organizační jednotky.

# Správa ovládacích panelů { #dashboard }

## O ovládacích panelech { #about-dashboards }

Panely jsou určeny k poskytnutí rychlého přístupu k různým analytickým objektům (mapy, grafy, zprávy, tabulky atd.) Jednotlivému uživateli. Panely lze sdílet se skupinami uživatelů. Panely lze také tisknout.

Uživatel nebo správce by mohl vytvořit ovládací panel s názvem „Předporodní péče“, který by mohl obsahovat všechny relevantní informace o předporodní péči. Tento ovládací panel lze poté sdílet se skupinou uživatelů nazvanou „Řízení ANC“, která může sestávat ze všech uživatelů ovládacího programu ANC. Všichni uživatelé v této skupině by pak mohli zobrazit stejný ovládací panel.

## Ovládací panel a ovládací lišta { #dashboards_setup }

Ovládací panely obsahují název, popis a libovolný počet položek ovládacího panelu. Položky ovládacího panelu mohou být mnoha různých typů, včetně grafů, map, sestav, tabulek, zdrojů, zpráv a textových položek. Nad ovládacím panelem je lišta nástrojů, která zobrazuje všechny vaše dostupné ovládací panely, včetně vyhledávacího pole ovládacího panelu, a tlačítko **+** pro vytvoření nového ovládacího panelu.

Ovládací panel má dva režimy: prohlížení a úpravy / vytváření. Při prvním přihlášení k serveru DHIS2 se v režimu zobrazení zobrazí naposledy použitý ovládací panel, pokud jste na stejném počítači jako předtím. Pokud používáte jiný počítač, zobrazí se první ovládací panel s hvězdičkou. Pokud zde nejsou žádné ovládací panely označené hvězdičkou, zobrazí se první ovládací panel (abecedně). Ovládací panely označené hvězdičkou se v seznamu ovládacích panelů zobrazují vždy jako první.

Snímek obrazovky níže ukazuje panel s názvem „Předporodní péče“, který byl naplněn grafy a mapami.

![](resources/images/dashboard/dashboard-view-mode.png)

### Responzivní zobrazení na malých obrazovkách { #responsive-view-on-small-screens }

Při prohlížení ovládacích panelů na malých obrazovkách (například mobilní telefon v orientaci na výšku) se ovládací panel přizpůsobí obrazovce a zobrazí všechny položky v jediném sloupci. Některé možnosti, včetně úprav, filtrování a sdílení, nebudou k dispozici.

![](resources/images/dashboard/dashboard-small-screen.png)

### Hledání v seznamu ovládacích panelů { #searching-in-the-list-of-dashboards }

Konkrétní ovládací panel můžete vyhledat pomocí vyhledávacího pole v levé horní části ovládacího panelu s názvem „Hledat ovládací panel“. Při hledání se nerozlišují velká a malá písmena a při psaní se seznam ovládacích panelů filtruje dolů na ty, které odpovídají vašemu hledanému textu.

### Přizpůsobení výšky ovládací lišty { #customizing-the-height-of-the-control-bar }

Konkrétní výšku ovládací lišty ovládacích panelů můžete nastavit kliknutím dolů a přetažením za spodní okraj ovládacího panelu. Po dokončení přetažení se nastaví nová výška. Kliknutím na **Zobrazit více** se ovládací panel rozbalí na maximální výšku (10 „řádků“). Kliknutím na **Zobrazit méně** se obnoví výška na vaši vlastní výšku.

## Vytvoření ovládacího panelu { #creating-a-dashboard }

Chcete-li vytvořit nový ovládací panel, kliknutím na zelené tlačítko **+** v levém rohu ovládacího panelu přejděte do režimu vytváření. Přidejte název do pole názvu a volitelně popis do pole popisu. Pokud nepřidáte název, bude mít ovládací panel automaticky název „Nepojmenovaný panel.“

![](resources/images/dashboard/dashboard-add-new.png)

**Režim vytvoření:**

![](resources/images/dashboard/dashboard-create-mode.png)

### Přidávání položek na ovládací panel { #adding-items-to-the-dashboard }

Přidejte položky na ovládací panel prohledáváním selektoru položek v pravé horní části oblasti ovládacího panelu. Dostupné položky zahrnují:

-   Vizualizace

-   Mapy

-   Zprávy o událostech

-   Grafy událostí

-   Zpráva

-   Zdroje

-   Aplikace

-   E-mail

-   Textová pole

-   Distanční prvek

Seznam položek v rozevírací nabídce zpočátku zobrazuje 10 vizualizací (grafy a tabulky) a 5 z každé z ostatních kategorií na základě zadaného hledaného textu. V rozbalovací nabídce najdete také e-mail, textová pole a distanční prvky. Chcete-li zobrazit více položek, klikněte na **Zobrazit více** a seznam pro tento typ se rozšíří na 25 položek. Pokud stále nenajdete požadovanou položku, zkuste zadat konkrétnější hledaný text.

![](resources/images/dashboard/dashboard-item-selector.png)

Jakmile vyberete položku, přidá se do levé horní části ovládacího panelu. Přidané položky lze přesouvat pomocí myši kliknutím na položku a jejím přetažením do požadované polohy. Lze jej také změnit pomocí myši kliknutím na táhlo tažení v pravém dolním rohu položky a přetažením na požadovanou velikost.

#### Distanční prvky { #spacer-items }

Ovládací panel je konfigurován s nastavením „antigravitační“ pro umisťování položek. To znamená, že položky budou „stoupat“ nahoru, dokud nenarazí na jinou položku. Chcete-li vynutit prázdný svislý prostor mezi položkami (jako prázdný řádek), můžete na ovládací panel přidat mezerové položky. Jsou viditelné pouze v režimu úprav / vytváření. V režimu zobrazení se nezobrazují, ale zabírají definované místo.

Distanční prvek v režimu **úpravy / vytvoření**:

![](resources/images/dashboard/dashboard-spacer-edit-mode.png)

Distanční prvek v **režimu zobrazení**:

![](resources/images/dashboard/dashboard-spacer-view-mode.png)

### Odebírání položek { #removing-items }

Odeberte položky kliknutím na červený koš v pravé horní části položky. Uvědomte si, že díky „antigravitačnímu“ nastavení  na ovládacím panelu se při odebrání jedné položky, ostatní položky, které jsou umístěny pod odstraněnou položkou, „posunou“ nahoru.

### Náhled před tiskem { #print-preview }

Kliknutím na tlačítko **Náhled tisku** zobrazíte, jak by ovládací panel vypadal v rozvržení pro tisk.

![](resources/images/dashboard/dashboard-edit-print-preview.png)

Kliknutím na **Ukončit náhled tisku** se vrátíte k úpravám ovládacího panelu.

Některé položky mohou být přesunuty dolů, aby nedocházelo ke zlomení stránek. Položky lze také zkrátit tak, aby se vešly na jednu stránku. Zkrácené položky zobrazují v pravém horním rohu v náhledu informační ikonu. Tato ikona je ve skutečném tisku odstraněna.

### Omezení filtrů ovládacího panelu { #restricting-dashboard-filters }

Ve výchozím nastavení budou uživatelé moci filtrovat položky ovládacího panelu podle jakékoli dimenze definované ve vašem systému. Nastavení filtru ovládacího panelu lze upravit pro daný ovládací panel kliknutím na **Nastavení filtru**.

![](resources/images/dashboard/dashboard-filter-settings-button.png)

Chcete-li omezit dostupné filtry, můžete kliknout na **Povolit filtrování pouze podle vybraných dimenzí** a vybrat filtry, které chcete na ovládacím panelu povolit. Když je ovládací panel v režimu zobrazení, uživatelé si budou moci vybrat pouze z vybraných filtrů. Období a organizační jednotka budou vybrány ve výchozím nastavení, ale lze je v případě potřeby odebrat.

![](resources/images/dashboard/dashboard-filter-settings.png)

Chcete-li uložit aktualizace nastavení filtru, musíte nejprve kliknutím na **Potvrdit** zavřete nastavení filtru a poté kliknutím na **Uložit změny** uložte změny ovládacího panelu.

### Ukládání ovládacího panelu { #saving-the-dashboard }

Při vytváření nebo úpravách ovládacího panelu se změny uloží pouze po kliknutí na tlačítko **Uložit změny** na panelu úprav v horní části stránky. Pokud změny nechcete uložit, klikněte vpravo nahoře na tlačítko **Ukončit bez uložení**. Poté se vrátíte do režimu zobrazení pomocí ovládacího panelu, který jste si předtím prohlíželi.

## Úpravy existujícího ovládacího panelu { #editing-an-existing-dashboard }

Pokud máte přístupová práva k úpravám aktuálně aktivního ovládacího panelu, v režimu zobrazení bude vpravo od názvu panelu tlačítko **Upravit**. Kliknutím na toto tlačítko vstoupíte do režimu úprav.

![](resources/images/dashboard/dashboard-title-bar.png)

Informace o přidávání a odebírání položek z ovládacího panelu najdete v předchozí části o vytváření ovládacích panelů.

![](resources/images/dashboard/dashboard-edit-mode.png)

### Překlad názvu a popisu ovládacího panelu { #translating-dashboard-title-and-description }

V režimu úprav můžete přidat překlady názvu a popisu panelu. Dialog poskytuje seznam jazyků, do kterých se má překlad přeložit, a zobrazuje původní název ovládacího panelu pod vstupním polem názvu.

![](resources/images/dashboard/dashboard-translation-dialog.png)

1.  Klikněte na tlačítko **PŘEKLAD** umístěné nad ovládacím panelem

2.  Vyberte jazyk, do kterého chcete přidat překlad.

3.  Přidejte název a / nebo popis a klikněte na **ULOŽIT**

## Odstranění ovládacího panelu { #deleting-a-dashboard }

Pokud máte přístup k odstranění panelu, bude v režimu úprav nad panelem tlačítko **Odstranit**. Nejprve se zobrazí dialogové okno s potvrzením, že chcete odstranit ovládací panel.

## Zobrazení ovládacího panelu { #viewing-a-dashboard }

V režimu zobrazení můžete přepínat zobrazování popisu, označovat hvězdičkou ovládací panel, aplikovat filtry, tisknout ovládací panel a sdílet ovládací panel s dalšími uživateli a skupinami.

### Ukázat popis { #show-description }

Chcete-li přepnout popis, klikněte na tlačítko **...Více** a vyberte **Zobrazit popis** (nebo **Skrýt popis**). Toto nastavení bude zapamatováno pro všechny ovládací panely, které otevřete. Toto nastavení platí pro vás, ne pro ostatní uživatele.

![](resources/images/dashboard/dashboard-title-bar-show-description.png)

### Ovládací panely označené hvězdičkou { #starred-dashboards }

Ovládací panely označené hvězdičkou jsou uvedeny nejprve v seznamu ovládacích panelů. Chcete-li ovládací panel označit hvězdičkou, klikněte na tlačítko s hvězdičkou vpravo od názvu. Hvězdu můžete také přepnout z nabídky **...Více**. Když je hvězda „vyplněna“, znamená to, že je ovládací panel označen hvězdičkou. Označení ovládacího panelu hvězdičkou se týká pouze vás, nikoli ostatních uživatelů.

### Filtrování ovládacího panelu { #filtering-a-dashboard }

Na panel lze použít více filtrů pro změnu dat zobrazených v různých položkách panelu. Filtry se aplikují na každou položku ovládacího panelu stejným způsobem: každý přidaný filtr přepíše původní hodnotu pro danou dimenzi v původním grafu, tabulce nebo mapě (vizualizace). V závislosti na instanci DHIS2 je možné filtrovat podle organizačních jednotek, období a dalších dynamických dimenzí.

Chcete-li přidat filtr, klikněte na tlačítko **Přidat filtr** a vyberte dimenzi:

![Přidání filtru](resources/images/dashboard/dashboard-filters.png)

Otevře se dialogové okno, kde lze provést výběr filtru.

![Výběr filtru organizační jednotky](resources/images/dashboard/dashboard-orgunit-filter-dialog.png)

Kliknutím na **Potvrdit** v dialogovém okně použijete filtr na aktuální ovládací panel.

Filtry se neukládají, takže při přepnutí na jiný ovládací panel se ztratí. Odznaky filtru se zobrazují nad položkami ovládacího panelu, což znamená, že to, co se zobrazuje v položkách ovládacího panelu, není původní vizualizace, ale manipulovaná, kde filtry přepisují hodnoty uložených dimenzí.

![Aktuální filtry zobrazené jako odznaky nad ovládacím panelem](resources/images/dashboard/dashboard-filter-badges.png)

Kliknutím na odznaky filtru lze otevřít dialogová okna výběru filtrů, což umožňuje úpravy filtrů. Filtr lze odebrat kliknutím na tlačítko **Odebrat** na odznaku. Kdykoli je filtr přidán, upraven nebo odstraněn, položky ovládacího panelu se znovu načtou a zobrazí aktualizovaná data. Odznaky filtru jsou vždy viditelné v horní části stránky při posouvání obsahu ovládacího panelu.

Ve výchozím nastavení mohou uživatelé filtrovat položky řídicího panelu podle libovolné dimenze definované ve vašem systému. Chcete-li omezit dostupné filtry, podívejte se na [Omezení filtrů ovládacího panelu](#restricting-dashboard-filters).

### Tisk ovládacího panelu { #printing-a-dashboard }

Z nabídky **...Více** můžete vytisknout aktivní ovládací panel. Existují dva styly tisku na palubní desce: rozložení palubní desky a jedna položka na stránku. U obou stylů je přidána titulní stránka, která zobrazuje název ovládacího panelu, popis (pokud je zapnuto nastavení Zobrazit popis) a všechny použité filtry ovládacího panelu.

![](resources/images/dashboard/dashboard-print-menu.png)

Pro nejlepší výsledky tisku:

-   použijte Chrome nebo Edge
-   před tiskem počkejte, až se načtou všechny položky na ovládacím panelu
-   použijte nastavení A4 na šířku s nastavenými výchozími okraji

#### Tisk rozvržení ovládacího panelu { #print-dashboard-layout }

Tisk rozvržení panelu bude přibližně odpovídat rozvržení panelu, jak je zobrazeno v prohlížeči. Pamatujte, že v rozložení bude možná nutné provést určité úpravy, aby nedocházelo ke zlomení stránek: pozice některých položek může být upravena dolů a položky, které jsou vyšší než jedna stránka, jsou zkráceny.

Kliknutím na tlačítko **Tisk** v pravém horním rohu spustíte funkci tisku prohlížeče.

![](resources/images/dashboard/dashboard-print-layout.png)

#### Vytiskněte jednu položku na stránku { #print-one-item-per-page }

Tento styl tisku vytiskne každou položku ovládacího panelu na samostatnou stránku, čímž maximalizuje využití papíru.

Kliknutím na tlačítko **Tisk** v pravém horním rohu spustíte funkci tisku prohlížeče.

![](resources/images/dashboard/dashboard-print-oipp.png)

## Položky ovládacího panelu s grafy, kontingenčními tabulkami nebo mapami { #dashboard-items-with-charts-pivot-tables-or-maps }

Položky ovládacího panelu s grafy, kontingenční tabulkou nebo mapami mohou mít v pravém horním rohu položky tlačítko kontextové nabídky s dalšími možnostmi zobrazení v závislosti na nastavení systému, která byla pro danou instanci nakonfigurována. Pokud byla deaktivována všechna příslušná systémová nastavení, nebude zde tlačítko kontextové nabídky. Zde jsou možné možnosti nabídky:

### Přepínání mezi vizualizacemi { #switching-between-visualizations }

Mezi těmito vizualizacemi lze přepínat položky ovládacího panelu zobrazující grafy, kontingenční tabulky a mapy. Klikněte na tlačítko kontextové nabídky položky a vyberte požadované zobrazení (např. **Zobrazit jako tabulku**, **Zobrazit jako mapu**, **Zobrazit jako graf**):

![](resources/images/dashboard/dashboard-item-menu.png)

### Zobrazit položku na celé obrazovce { #view-item-in-fullscreen }

Chcete-li zobrazit graf, tabulku nebo mapu na celé obrazovce, klikněte na možnost **Zobrazit celou obrazovku**. Chcete-li ukončit režim celé obrazovky, můžete buď stisknout klávesu **esc**, nebo kliknout na tlačítko ukončení v pravém horním rohu zobrazení na celou obrazovku.

### Otevřít v aplikaci { #open-in-app }

Chcete-li otevřít vizualizaci v příslušné aplikaci (např. Data Visualizer, Maps), klikněte na možnost **Otevřít v aplikaci [název aplikace]**.

## Zobrazit výklady a podrobnosti { #show-interpretations-and-details }

Kliknutím na **Zobrazit interpretace a podrobnosti** můžete psát interpretace pro graf, kontingenční tabulku, mapu, zprávu událostí a položky grafu událostí:

![](resources/images/dashboard/dashboard-item-menu-interpretations.png)

> **Poznámka**
>
> Tato možnost může být ve vašem systému zakázána, pokud není zaškrtnuto systémové nastavení _Povolit uživatelům zobrazovat oblíbené interpretace a podrobnosti ovládacího panelu_.)

Položka bude svisle rozbalena směrem dolů a zobrazí se popis, interpretace a odpovědi. Můžete olajkovat interpretaci, odpovědět na interpretaci a přidat svůj vlastní výklad. Můžete upravovat, sdílet nebo mazat své vlastní výklady a odpovědi, a pokud máte přístup moderátora, můžete smazat výklady ostatních.

Pole popisu a interpretace je možné formátovat pomocí **bold**, _italic_ pomocí značek stylu Markdown \* a \_ pro **tučné** a _zkosené_. Textové pole pro psaní nových interpretací má panel nástrojů pro přidávání formátovaného textu. K dispozici jsou také klávesové zkratky: Ctrl / Cmd + B a Ctrl / Cmd + I. Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: :) :-) :( :-(: +1: -1. URL jsou automaticky detekovány a převedeny na odkaz, na který lze kliknout.

Interpretace jsou seřazeny podle data v sestupném pořadí, nejnovější jsou zobrazeny nahoře. Odpovědi na interpretaci jsou řazeny vzestupně podle data, přičemž nejstarší jsou zobrazeny nahoře.

![](resources/images/dashboard/dashboard-interpretations.png)

## Sdílení ovládacího panelu { #dashboard_sharing }

Chcete-li sdílet ovládací panel se skupinami uživatelů, kliknutím na tlačítko **SDÍLET** napravo od názvu ovládacího panelu zobrazíte možnosti nastavení sdílení na ovládacím panelu. Pokud chcete sdílet ovládací panel s konkrétními uživateli nebo skupinami uživatelů, zadejte název do vstupního pole a přidejte je do nastavení sdílení ovládacího panelu.

![](resources/images/dashboard/dashboard-sharing-dialog.png)

Všechny ovládací panely mají ve výchozím nastavení nastaveny dvě skupiny sdílení.

-   Externí přístup (bez přihlášení)

    Pokud je tato možnost vybrána, poskytuje přístup k ovládacímu panelu jako externí prostředek prostřednictvím rozhraní API. To je užitečné, když vytváříte externí webový portál, ale chcete volat informace z ovládacího panelu, který jste vytvořili interně v DHIS2. Ve výchozím nastavení není tato možnost vybrána. Další informace najdete v části [Prohlížení reprezentací analytických prostředků](https://docs.dhis2.org/master/en/developer/html/webapi_viewing_analytical_resource_representations.html#) v příručce pro vývojáře.

-   Veřejný přístup (s přihlášením)

    Tato možnost umožňuje odeslání vybraného ovládacího panelu všem uživatelům v rámci vaší instance DHIS2. To lze také skrýt z veřejného pohledu výběrem možnosti „Žádný“, což je výchozí možnost pro nové ovládací panely.

Skupinám uživatelů, které byly přidány ručně, lze v rámci ovládacího panelu přiřadit dva typy oprávnění

-   Může zobrazit

    Poskytuje skupině uživatelů práva pouze k zobrazení na ovládací panel.

-   Může upravovat a prohlížet

    Umožňuje skupinám uživatelů kromě zobrazení také upravit ovládací panel. Úpravy umožňují změnu rozvržení, změnu velikosti a odebrání položek, přejmenování / odstranění ovládacího panelu atd.

Uživatelům můžete poskytnout adresu URL ovládacího panelu, což jim umožní přejít přímo na ovládací panel. Chcete-li získat adresu URL ovládacího panelu, stačí otevřít ovládací panel v režimu zobrazení a zkopírovat adresu URL prohlížeče. Například adresa URL ovládacího panelu Antatatal Care v play.dhis2.org/demo je:

https://play.dhis2.org/demo/dhis-web-dashboard/\#/nghVC4wtyzi

# Použití aplikace Data Visualizer { #data_visualizer }

![](resources/images/data-visualizer/data-visualizer-overview.png)

## Vytváření a úpravy vizualizací { #creating-and-editing-visualizations }

Když otevřete aplikaci datového vizualizéru z nabídky dhis2, zobrazí se vám prázdná tabulka a můžete hned začít vytvářet vizualizaci.

![](resources/images/data-visualizer/data-visualizer-new.png)

### Vyberte typ vizualizace { #select-visualization-type }

Vyberte požadovaný typ vizualizace z nabídky v levém horním rohu. Pro každý typ vizualizace existuje stručný popis s návrhy, kde použít hlavní dimenze v rozložení.

![](resources/images/data-visualizer/data-visualizer-visualization-type.png)

| Typ vizualizace | Popis |
| --- | --- |
| Sloupec | Zobrazí informace jako svislé obdélníkové sloupce s délkami úměrnými hodnotám, které představují. <br> <br> Příklad: porovnání výkonu různých okresů. <br> <br> Omezení rozložení: přesně 1 dimenze jako série, přesně 1 dimenze jako kategorie. |
| Skládaný sloupec | Zobrazuje informace jako svislé obdélníkové sloupce, kde jsou pruhy představující více kategorií naskládány na sebe. <br> <br> Příklad: zobrazení trendů nebo součtů souvisejících datových prvků. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Pruh | Stejné jako sloupce, pouze s vodorovnými pruhy. |
| Skládaný pruh | Stejné jako skládaný sloupec, pouze s vodorovnými pruhy. |
| Čára | Zobrazuje informace jako řadu bodů spojených přímkami. Označuje se také jako časová řada. <br> <br> Příklad: vizualizace trendů v datech indikátoru v časových intervalech. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Plocha | Je založen na čáře (výše), s mezerou mezi osou a čarou vyplněnou barvami a řádky naskládanými na sebe. <br> <br> Příklad: porovnání trendů souvisejících indikátorů. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Skládaná plocha | Stejné jako Plocha, ale oblasti různých položek dimenzí jsou naskládány na sebe. <br> <br> Příklad: porovnání trendů souvisejících indikátorů. <br> <br> Omezení rozložení: stejné jako plocha. |
| Koláč | Kruh rozdělený na sektory (nebo plátky). <br> <br> Příklad: vizualizace podílu dat pro jednotlivé datové prvky ve srovnání s celkovým součtem všech datových prvků. <br> <br> Omezení rozložení: přesně 1 dimenze jako série, nemá žádnou kategorii. |
| Radar | Zobrazuje data na osách počínaje od stejného bodu. Také známé jako pavoučí graf. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Gauge | Polokruh, který zobrazuje jednu hodnotu, obvykle ze 100% (počáteční a koncová hodnota je konfigurovatelná). <br> <br> Omezení rozvržení: přesně 1 dimenze s přesně 1 položkou jako série, datová dimenze je uzamčena do řady. |
| Rok po roce (řádek) | Užitečné, pokud chcete porovnat jeden rok dat s jinými roky dat. Založeno na kalendářních letech. <br> <br> Omezení rozvržení: dimenze období je deaktivována. |
| Rok po roce (sloupec) | Stejné jako meziročně (řádek), pouze se sloupci. |
| Jedna hodnota | Zobrazí jednu hodnotu přijatelným způsobem na ovládacím panelu. <br> <br> Omezení rozložení: stejné jako Gauge. |
| Kontingenční tabulka | Shrnuje data rozsáhlejší tabulky a může zahrnovat součty, průměry nebo jiné statistiky, které kontingenční tabulka seskupuje smysluplným způsobem. <br> <br> Omezení rozložení: žádné. |
| Rozptyl | Bodové grafy umožňují uživatelům mapovat organizační jednotky jako body proti dvěma proměnným pro jediné pevné nebo relativní období. <br> <br> Omezení rozvržení: každá přesně 1 položka jako vertikální a horizontální, rozměr dat je uzamčen na vertikální a horizontální, organizační jednotka je uzamčena na body. |

### Vyberte dimenze { #select-dimensions }

Z nabídky dimenzí vlevo můžete vybrat dimenze, které chcete zobrazit ve vizualizaci, včetně dat, období, organizačních jednotek a dynamických dimenzí. Lze je přidat kliknutím na dimenzi, přetažením dimenze do oblasti rozložení nebo umístěním kurzoru nad dimenzi a použitím její kontextové nabídky (tři tečky).

![](resources/images/data-visualizer/data-visualizer-dimensions.png)

Stejně jako v nabídce dimenzí můžete v oblasti rozvržení také změnit výběr kliknutím na dimenzi, přetažením dimenze nebo pomocí kontextové nabídky dimenze (tři tečky).

![](resources/images/data-visualizer/data-visualizer-layout-area.png)

-   **Série**: Série je sada spojitých souvisejících prvků (například období nebo datové prvky), které chcete vizualizovat, abyste zdůraznili trendy nebo vztahy v jejích datech. Také se nazývá sloupce pro vizualizace kontingenčních tabulek.

<!-- konec seznamu -->

-   **Kategorie**: Kategorie je sada prvků (například indikátorů nebo organizačních jednotek), pro které chcete porovnat její data. Také se nazývá řádky pro vizualizace kontingenčních tabulek.

<!-- konec seznamu -->

-   **Filtr**: Výběr filtru vyfiltruje data zobrazená ve vizualizaci. Všimněte si, že pokud použijete dimenzi dat jako filtr, můžete určit pouze jeden indikátor nebo datovou sadu jako položku filtru, zatímco u jiných typů dimenzí můžete vybrat libovolný počet položek.

### Vyberte položky dimenze { #data_vis_select_dim_items }

Dimenze odkazuje na prvky, které popisují hodnoty dat v systému. V systému jsou tři hlavní dimenze:

-   **Data**: Zahrnuje datové prvky, indikátory a datové sady (míry hlášení), popisující jevy nebo událost dat.

<!-- konec seznamu -->

-   **Období**: Popisuje, kdy k události došlo.

<!-- konec seznamu -->

-   **Organizační jednotky**: Popisuje, kde k události došlo.

Data Visualizer je vysoce flexibilní, pokud jde o to, že vám umožňuje používat tyto dimenze jako serie, kategorie a filtr.

Chcete-li vybrat položky pro dimenzi, otevřete modální okno dimenze kliknutím na dimenzi. Toto okno se také automaticky otevře při přidání kóty bez vybraných položek do rozvržení. Dvojitým kliknutím na položku nebo výběrem položky jedním kliknutím a pomocí šipek uprostřed vyberte položky, které chcete přidat do vizualizace. Pořadí vzhledu bude stejné jako pořadí, ve kterém jsou vybrány. U vybraných položek lze změnit jejich pořadí přetažením v sekci Vybrané.

#### Vyberte datové položky { #select-data-items }

Při výběru datových položek existují různé způsoby, jak filtrovat zobrazené položky. Pomocí vyhledávacího pole v horní části se provede globální vyhledávání podle názvu položky v aktuálně vybraném **Datovém typu**. Výběrem **Typ dat** z rozevíracího seznamu lze položky filtrovat podle typu a podtypu, přičemž dostupný podtyp závisí na zvoleném typu dat. Vyhledávání podle jména a filtrování typu/podtypu lze také kombinovat pro podrobnější filtr. Typ každé zobrazené položky je označen příslušnou ikonou na položce. Umístěním kurzoru na položku lze také zobrazit název typu.

![](resources/images/data-visualizer/data-visualizer-dimension-modal.png)

#### Vyberte období { #select-periods }

Při výběru období musíte zvolit mezi pevnými obdobími a relativními obdobími. Lze je také kombinovat. Překrývající se období jsou filtrována tak, aby se objevila pouze jednou. U relativních období jsou názvy relativní k aktuálnímu datu, např. pokud je aktuální měsíc březen a je vybrán **minulý měsíc**, ve vizualizaci se zobrazí měsíc únor.

![](resources/images/data-visualizer/data-visualizer-period-dimension-modal.png)

#### Vyberte organizační jednotky { #select-organisation-units }

Dialog organizačních jednotek je flexibilní a nabízí v zásadě tři způsoby výběru organizačních jednotek:

-   Explicitní výběr: Použijte **strom** k explicitnímu výběru organizačních jednotek, které chcete zobrazit ve vizualizaci. Pokud kliknete pravým tlačítkem na organizační jednotku, můžete snadno vybrat všechny organizační jednotky pod ní.

-   Úrovně a skupiny: Rozbalovací nabídky **Úroveň** a **Skupina** jsou pohodlným způsobem, jak vybrat všechny jednotky v jedné nebo více skupinách organizačních jednotek nebo na konkrétních úrovních. Příklad: vyberte _Chiefdom_ (úroveň 3) a získejte všechny organizační jednotky na této úrovni.

    Vezměte prosím na vědomí, že jakmile je vybrána alespoň jedna úroveň nebo skupina, strom organizačních jednotek nyní funguje jako hranice pro úrovně / skupiny. Příklad: pokud ve stromu vyberete _Chiefdom_ (úroveň 3) a _Kailahun_ organizační jednotku (na úrovni 2), získáte všechny jednotky chiefdom v okrese Kailahun.

-   Organizační jednotky uživatele:

    -   Organizační jednotka uživatele: Toto je způsob, jak dynamicky vybrat organizační jednotky, ke kterým je přihlášený uživatel přidružen.

    -   Uživatelské dílčí jednotky: Vybírá dílčí jednotky organizační jednotky uživatele.

    -   Uživatelské jednotky druhé podúrovně sub-x2-units: Vybírá jednotky o dvě úrovně pod organizační jednotkou uživatele.

![](resources/images/data-visualizer/data-visualizer-organisation-unit-dimension-modal.png)

### Dva grafy kategorií { #two-category-charts }

Většina typů vizualizace grafů může zobrazit dvě kategorie. Přepnutím z kontingenční tabulky na sloupec, sloupec, oblast (a jejich skládané verze) a řádek zachováte první dvě dimenze v kategorii, jakákoli další dimenze se přesune do filtru. Štítky pro první dimenzi v kategorii jsou zobrazeny v horní části grafu a štítky pro druhou dimenzi v dolní části. Výsledná vizualizace se skládá ze samostatných grafů, jednoho pro každou položku v první dimenzi.

![](resources/images/data-visualizer/data-visualizer-two-category.png)

## Změňte zobrazení vaší vizualizace { #change-the-display-of-your-visualization }

Zobrazení vizualizace lze změnit povolením / zakázáním a konfigurací několika možností. Každý typ vizualizace může mít jinou sadu dostupných možností. Možnosti jsou uspořádány na kartách v **dialogovém okně Možnosti** a v sekcích na každé kartě.

1.  Kliknutím na **Možnosti** otevřete **Možnosti dialogového okna**.

2.  Přejděte na karty v dialogovém okně a zobrazte dostupné možnosti.

3.  Podle potřeby nakonfigurujte požadované možnosti.

4.  Klepnutím na tlačítko **Aktualizovat** provedete změny ve vizualizaci.

### Seznam dostupných možností { #list-of-available-options }

| Možnost | Popis |
| --- | --- |
|  | **karta Data** |
| Typ agregace | Definuje, jak budou datové prvky nebo indikátory agregovány ve vizualizaci. Některé z typů agregace jsou Podle datového prvku, Počet, Min a Max. |
| Základní linie | Zobrazí vodorovnou čáru na dané hodnotě domény. Užitečné například, když chcete vizualizovat, jak se váš výkon vyvíjel od začátku procesu. |
| Mezisoučty sloupců | Zobrazí dílčí součty v kontingenční tabulce pro každou dimenzi. <br> Pokud vyberete pouze jednu dimenzi, dílčí součty budou pro tyto sloupce skryty. Je to proto, že hodnoty se budou rovnat mezisoučtům. |
| Součty sloupců | Zobrazí celkové hodnoty v kontingenční tabulce pro každý sloupec a také celkové hodnoty pro všechny hodnoty v tabulce. |
| Kumulativní hodnoty | Zobrazí kumulativní hodnoty ve vizualizacích Sloupec, Skládaný sloupec, Pruh, Skládaný pruh, Čára a Plocha |
| Vlastní pořadí řazení | Řídí pořadí řazení hodnot. |
| Štítky dimenzí | Zobrazuje názvy dimenzí jako součást kontingenční tabulky. |
| Skrýt prázdné kategorie | Skryje položky kategorie bez dat z vizualizace. <br> **před první**: skryje chybějící hodnoty pouze před první hodnotou <br> **po poslední**: skryje chybějící hodnoty pouze po poslední hodnotě <br> **před první a po poslední**: skryje chybějící hodnoty pouze před první value a po poslední hodnotě <br> **Vše**: skryje všechny chybějící hodnoty <br> To je užitečné například při vytváření vizualizací sloupců a pruhů. |
| Skrýt prázdné sloupce | Skryje prázdné sloupce z kontingenční tabulky. To je užitečné, když se podíváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
| Skrýt prázdné řádky | Skryje prázdné řádky z kontingenční tabulky. To je užitečné, když se podíváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
| Typ čísla | Nastaví typ hodnoty, kterou chcete zobrazit v kontingenční tabulce: Hodnota, Procento řádku nebo Procento sloupce. <br> Možnosti Procento řádku a Procento sloupce znamenají, že místo agregované hodnoty budete zobrazovat hodnoty jako procenta z celkového počtu řádků nebo procenta z celkového počtu sloupců. To je užitečné, když chcete vidět příspěvek datových prvků, kategorií nebo organizačních jednotek k celkové hodnotě. |
| Zahrnout pouze dokončené události | Zahrnuje do procesu agregace pouze dokončené události. To je užitečné například k vyloučení dílčích událostí ve výpočtech indikátorů. |
| Mezisoučty řádků | Zobrazí dílčí součty v kontingenční tabulce pro každou dimenzi. <br> Pokud vyberete pouze jednu dimenzi, dílčí součty budou pro tyto řádky skryty. Je to proto, že hodnoty se budou rovnat mezisoučtům. |
| Součty řádků | Zobrazí celkové hodnoty v kontingenční tabulce pro každý řádek a také celkové hodnoty pro všechny hodnoty v tabulce. |
| Přeskočit zaokrouhlování | Přeskočí zaokrouhlování datových hodnot a nabízí úplnou přesnost datových hodnot. Může být užitečné pro finanční data, kde je vyžadována přesná částka. |
| Skládané hodnoty se přidávají až do 100% | Zobrazí 100% skládané hodnoty ve skládaných sloupcích a skládaných pruzích vizualizací. |
| Cílová čára | Zobrazí vodorovnou čáru na dané hodnotě domény. Užitečné například, když chcete porovnat svůj výkon s aktuálním cílem. |
| Trendová čára | Zobrazí trendovou čáru, která vizualizuje, jak se vaše data vyvíjejí v průběhu času. Například pokud se výkon zlepšuje nebo zhoršuje. Užitečné, když jsou jako kategorie vybrány období. |
| Hodnotové štítky | Zobrazuje hodnoty nad řadou ve vizualizaci. |
|  | Karta Osy |
| Rozsah os | Definuje maximální a minimální hodnotu, která bude viditelná na ose rozsahu. |
| Název osy | Sem zadejte nadpis a zobrazí se štítek vedle osy x nebo y. Užitečné, když chcete vizualizaci poskytnout kontextové informace, například o měrné jednotce. |
| Desetinná místa | Definuje počet desetinných míst, která budou použita pro hodnoty osy rozsahu. |
| Kroky | Definuje počet značek, které budou viditelné na ose rozsahu. |
|  | **karta Legenda** |
| Zobrazit legendu | Použije na hodnoty legendu, což znamená, že na hodnoty můžete použít barvu. Legendy nakonfigurujete v aplikaci `Údržba`. |
| Typ legendy | Řídí, která legenda se použije. <br> `Použít předdefinovanou legendu pro datovou položku` aplikuje legendu na každý datový prvek nebo indikátor jednotlivě na základě legendy přiřazené každému z nich v aplikaci `Údržba`. <br> `Vybrat jednu legendu pro celou vizualizaci` aplikuje jednu legendu na všechny datové položky vybrané v rozevíracím seznamu dostupných legend. |
| Styl legendy | Řídí, kde se použije barva z legendy, buď na text, nebo na pozadí. Tuto možnost můžete použít pro rychlé přehledy, abyste na první pohled identifikovali vysoké a nízké hodnoty. Nelze použít pro vizualizace typu `Jedna hodnota`, `Sloupec` nebo `Pruh`. |
|  | **Záložka Serie** |
|  | Na této záložce jsou nastaveny možnosti pro přidání více os a změnu zobrazení různých sérií. Podrobný popis toho, jak to funguje, naleznete v příslušných částech níže. |
|  | **karta Styl** |
| Oddělovač skupin číslic | Určuje, který znak použít k oddělení skupin číslic nebo „tisíců“. Můžete jej nastavit na Čárku, Mezerník nebo Žádný. |
| Hustota zobrazení | Řídí velikost buněk v kontingenční tabulce. Můžete jej nastavit na Komfortní, Normální nebo Kompaktní. <br> Kompaktní je užitečné, pokud chcete na obrazovku prohlížeče umístit velké tabulky. |
| Zobrazit hierarchii organizačních jednotek | Zobrazuje název všech předků organizačních jednotek, například „Sierra Leone / Bombali / Tamabaka / Sanya CHP“ pro „Sanya CHP“. <br> Organizační jednotky jsou poté seřazeny podle abecedy, která uspořádá organizační jednotky podle hierarchie. <br> Když stáhnete kontingenční tabulku s organizačními jednotkami jako řádky a vybrali jste Zobrazit hierarchii organizačních jednotek, každá úroveň organizační jednotky se vykreslí jako samostatný sloupec. To je užitečné například při vytváření kontingenčních tabulek aplikace Excel v místním počítači. |
| Velikost písma | Řídí velikost písma textu kontingenční tabulky. Můžete jej nastavit na Velký, Normální nebo Malý. |
| Název grafu / tabulky | Řídí nadpis, který se zobrazí nad vizualizací. <br> Automaticky generováno používá výchozí nadpis vygenerovaný z dimenzí / filtrů vizualizace. <br> None odstraní název. <br> Možnost Vlastní umožňuje zadat vlastní název. |
| Podtitul grafu / tabulky | Řídí titulky, které se zobrazují nad vizualizací. <br> Automaticky generováno používá výchozí titulky generované z dimenzí / filtrů vizualizace. <br> None odstraní titulky. <br> Možnost Vlastní umožňuje zadat vlastní titulky. |
| Zobrazit klíč legendy | Zapíná a vypíná legendu a ponechává více prostoru pro samotnou vizualizaci. |
| Mezi pruhy / sloupci není mezera | Odebere mezeru mezi sloupci nebo pruhy ve vizualizaci. Užitečné pro zobrazení vizualizace jako křivky EPI. |
| Hodnotové štítky | Zobrazuje hodnoty nad řadou ve vizualizaci. |
| Název grafu / tabulky | Řídí nadpis, který se zobrazí nad vizualizací. <br> Automaticky generováno používá výchozí nadpis vygenerovaný z dimenzí / filtrů vizualizace. <br> None odstraní název. <br> Možnost Vlastní umožňuje zadat vlastní název. |
| Sada barev | Řídí barvy použité v grafu. Zobrazí se seznam dostupných barevných sad s náhledem barev. K dispozici je také možnost „Mono vzory“, která místo plných barev používá barevné vzory. |
|  | **karta Mezní hodnoty** |
| Mezní minimální / maximální hodnoty | Umožňuje filtrování dat na straně serveru. <br> Můžete dát systému pokyn, aby vracel pouze záznamy, u nichž je agregovaná hodnota dat stejná, větší než, větší nebo stejná, menší nebo menší nebo rovna určitým hodnotám. <br> Pokud jsou použity obě části filtru, je možné odfiltrovat řadu datových záznamů. |
|  | **karta Parametry** |
| Vlastní pořadí řazení | Řídí pořadí řazení hodnot. |
| Zahrnout kumulativní | Zahrnuje sloupec s kumulativními hodnotami do kontingenční tabulky. |
| Zahrnout regresi | Zahrnuje sloupec s hodnotami regrese do kontingenční tabulky. |
| Organizační jednotka | Řídí, zda se má uživatel při vytváření standardní zprávy v aplikaci Zprávy vyzvat k zadání organizační jednotky. |
| Nadřazená organizační jednotka | Řídí, zda se má uživatel při vytváření standardní sestavy v aplikaci Zprávy vyzvat k zadání nadřazené organizační jednotky. |
| Období hlášení | Určuje, zda se má uživatel při vytváření standardního přehledu v aplikaci Zprávy vyzvat k zadání období přehledu. |
| Horní limit | Řídí maximální počet řádků, které mají být zahrnuty do kontingenční tabulky. |
|  | **Karta Odlehlé hodnoty** |
| Metoda detekce odlehlých hodnot | Analýza odlehlých hodnot je proces, který zahrnuje identifikaci anomálních pozorování v souboru dat. V Data Visualizer jsou odlehlé hodnoty detekovány nejprve normalizací dat do lineární regresní přímky a poté analýzou vzdálenosti každého bodu od regresní přímky. V současné době jsou podporovány tři metody. **Interquartile Range (IQR)** je založeno na rozdělení souboru dat do kvartilů, zatímco **Modified z-score** je založeno na střední absolutní odchylce (MAD). IQR a MAD jsou považovány za dvě nejběžnější robustní měřítka. **Standardní z-skóre** je založeno na směrodatné odchylce, a proto je považováno za méně robustní, protože je výrazně ovlivněno odlehlými hodnotami. |
| Faktor prahové hodnoty | Číslo, kterým se násobí odlehlé prahové hodnoty. Řídí citlivost prahového rozsahu. Výchozí faktory jsou 1,5 pro IQR a 3 pro z-skóre. |

### Vlastní styl pro text a legendy v grafech { #custom-styling-for-text-and-legend-in-charts }

Pomocí nástroje pro stylování textu lze přizpůsobit následující možnosti: `Název grafu`, `Podtitul grafu`, `Zobrazit klíč legendy`, `Cílová čára`, `Základní čára`, `Název os` a  `Visačky` pro obě svislé i vodorovné osy. Nástroj pro úpravu textu umožňuje zvolit velikost písma, barvu a variantu kurzívou / tučným písmem. Je také možné zvolit umístění textu.

![](resources/images/data-visualizer/data-visualizer-text-styling-tool.png)

## Přidání přiřazených kategorií { #adding-assigned-categories }

Přiřazené kategorie je složená dimenze, která představuje přidružené kombinace možností kategorií ke kombinaci kategorií vybraného datového prvku. To lze přidat přetažením dimenze **Přiřazené kategorie** z nabídky dimenzí na levé straně a do rozložení vizualizace:

![](resources/images/data-visualizer/data-visualizer-assigned-categories.png)

Dalším způsobem přidávání přiřazených kategorií je přístup k možnosti **Přidat přiřazené kategorie** z kontextové nabídky dimenze`Data` (není k dispozici pro `Gauge`, `Rok za rokem` nebo `Jedna hodnota`).

## Přidání dalších os { #adding-more-axes }

Při kombinaci dat s různými měřícími stupnicemi získáte smysluplnější vizualizaci tím, že budete mít více než jednu osu. U `Column`, `Bar`, `Area` a `Line`  můžete kliknout na kartu **Serie** v dialogovém okně `Options`. Pokud je tato možnost zakázána, ujistěte se, že dimenze `Data` je na ose `Series` a že byly přidány alespoň dvě položky.

K dispozici jsou čtyři osy, dvě na levé straně (osa 1 a 3) grafu a dvě na pravé straně (osa 2 a 4). Každá osa má jinou barvu a položky grafu budou odpovídajícím způsobem vybarveny.

Poznámka: Pokud se používá více os, některé možnosti jako `Čáry`,` Svislá (y) osa` a `Sada barev` na ostatních záložkách možností budou deaktivovány.

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis.png)

## Použití více typů vizualizace { #using-multiple-visualization-types }

Je možné kombinovat graf `Sloupec` s položkami `Řádek` a naopak. To provedete kliknutím na kartu **Série** v dialogu `Možnosti` a změnou `Typu vizualizace`. To lze také kombinovat s použitím více os (jak je popsáno v části výše).

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis-multi-type.png)

Výsledkem je graf, který kombinuje typy `Sloupec` a `Řádek`.

![](resources/images/data-visualizer/data-visualizer-multi-type-chart.png)

## Procházení dat { #data-drilling }

Tato funkce je povolena pro typ vizualizace `Kontingenční tabulka` a umožňuje procházet dál data kliknutím na hodnotovou buňku v tabulce. Otevře se kontextové menu s různými možnostmi.

Data můžete procházet podle organizační jednotky, což znamená procházení stromu organizačních jednotek nahoru a dolů. Procházení dat ovlivňuje výběr aktuální kóty v oblasti rozvržení.

![](resources/images/data-visualizer/data-visualizer-pt-drill.png)

## Spravujte uložené vizualizace { #manage-saved-visualizations }

Uložení vizualizací usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli nebo je zobrazit na ovládacím panelu.

### Otevřete vizualizaci { #open-a-visualization }

1.  Klikněte na **Soubor** \> **Otevřít**.

2.  Do vyhledávacího pole zadejte název vizualizace nebo kliknutím na šipky **<** a **>** přejděte mezi různými stránkami. Výsledek lze také filtrovat podle typu a vlastníka pomocí odpovídajících nabídek v pravém horním rohu.

3.  Klikněte na název toho, co chcete otevřít.

![](resources/images/data-visualizer/data-visualizer-open-dialog.png)

### Uložte vizualizaci { #save-a-visualization }

1. a) Klikněte na **Soubor** \> **Uložit**.

2. Zadejte **Název** a **Popis** pro vaši vizualizaci.

3. Klikněte **Uložit**.

![](resources/images/data-visualizer/data-visualizer-save-dialog.png)

### Přejmenujte vizualizaci { #rename-a-visualization }

1.  Klikněte na **Soubor** \> **Přejmenovat**.

2.  Zadejte nový název nebo popis.

3.  Klikněte na **Přejmenovat**.

![](resources/images/data-visualizer/data-visualizer-rename-dialog.png)

### Odstranit vizualizaci { #delete-a-visualization }

1.  Klikněte na **Soubor** \> **Odstranit**.

2.  Klikněte na **Smazat**.

### Získejte odkaz na vizualizaci { #get-the-link-to-the-visualization }

1. Klikněte na **Soubor** \> **Získat odkaz**.

2. Adresu URL lze zkopírovat prostřednictvím kontextové nabídky prohlížeče, která se otevře kliknutím pravým tlačítkem na odkaz.

![](resources/images/data-visualizer/data-visualizer-delete-dialog.png)

## Vizualizace interpretací { #visualization-interpretations }

Při prohlížení uložené vizualizace můžete rozšířit interpretace na pravé straně kliknutím na tlačítko Interpretace v pravém horním rohu. Zobrazí se také popis vizualizace. Popis podporuje formát RTF.

Nové interpretace lze přidat zadáním textového pole v pravém dolním rohu. Ostatní uživatelé mohou být uvedení jako `@uživatel`. Začněte zadáním znaku `@` plus první písmena uživatelského jména nebo skutečného jména a zobrazí se seznam odpovídajících uživatelů. Uvedení uživatelé obdrží interní zprávu DHIS2 s interpretací nebo komentářem. Interpretace lze také vidět v aplikaci **Ovládací panel**.

Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown `*` a `_` pro **tučně** a _italic_ (klávesové zkratky jsou také k dispozici: `Ctrl`/`Cmd` + `B` and `Ctrl`/`Cmd` + `I`). Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: `:)` `:-)` `:(` `:-(` `:+1` `:-1`. URL jsou automaticky detekovány a převedeny na klikatelný odkaz.

Chcete-li zobrazit vizualizaci podle data konkrétní interpretace, klikněte na interpretaci nebo na její tlačítko `Zobrazit`, Tím se znovu vygeneruje vizualizace s příslušným datem, které je uvedeno vedle názvu vizualizace. Kliknutím na `Zpět na všechny interpretace` se obnoví vizualizace s aktuálním datem.

Chcete-li se přihlásit k odběru uložené vizualizace, klikněte na ikonu zvonku v pravém horním rohu. Poté budete dostávat interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci v této uložené vizualizaci.

![](resources/images/data-visualizer/data-visualizer-view-interpretation.png)

## Sdílet vizualizaci { #share-a-visualization }

Nastavení sdílení lze zobrazit kliknutím na **Soubor** \> **Sdílet**. Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit, dostupná nastavení jsou:

-   **Can edit and view**: Can view and edit the visualization.

-   **Lze jen zobrazit**:  Vizualizaci lze pouze zobrazit.

-   **Žádný přístup**: Nebude mít přístup k vizualizaci. Toto nastavení je použitelné pouze pro **Veřejný přístup** a **Externí přístup**.

Noví uživatelé mohou být přidáni jejich vyhledáním podle jména v části `Přidat uživatele a skupiny uživatelů`.

![](resources/images/data-visualizer/data-visualizer-share-dialog.png)

## Stáhnout { #download }

Vizualizace lze stáhnout pomocí nabídky **Stáhnout**. Všechny typy vizualizace podporují stahování `Grafika` a `Zdroj prostých dat`, s výjimkou typu `Kontingenční tabulka`, který lze stáhnout jako `Rozvržení  tabulky` a `Zdroj prostých dat`.

### `Grafika` ke stažení { #graphics-download }

Stáhne do počítače obrázek (.png) nebo PDF (.pdf).

### Stahování `rozložení tabulky` { #table-layout-download }

Stáhne do počítače soubor Excel (.xls), CSV (.csv) nebo HTML (.html).

### Stažení `Zdroje prostých dat` { #plain-data-source-download }

Zdroj dat vizualizace si můžete stáhnout ve formátu JSON, XML, Excel, CSV, JXRML nebo Raw data SQL s různými identifikačními schématy (ID, kód a název). Datový dokument používá identifikátory položek dimenze a otevře se v novém okně prohlížeče, aby se v adresním řádku zobrazila adresa URL požadavku na webové rozhraní API. To je užitečné pro vývojáře aplikací a dalších klientských modulů založených na webovém rozhraní DHIS2 nebo pro ty, kteří vyžadují zdroj dat plánu, například pro import do statistických balíčků.

**Dostupné formáty**

| Formát | Akce | Popis |
| --- | --- | --- |
| JSON | Klikněte na JSON | Stáhne formát JSON na základě vlastnosti ID, kódu nebo názvu. |
| XML | Klikněte na XML | Stáhne formát XML na základě vlastnosti ID, kódu nebo jména. |
| Microsoft Excel | Klikněte na Microsoft Excel | Stáhne formát Microsoft Excel na základě vlastnosti ID, kódu nebo Názvu. |
| CSV | Klikněte na CSV | Stáhne formát CSV na základě vlastnosti ID, kódu nebo názvu. |
| Sada hodnot dat XML | Klikněte na Pokročilé > XML | Stáhne hodnoty nezpracovaných dat jako XML, na rozdíl od dat, která byla agregována podle různých dimenzí. |
| Sada hodnot dat JSON | Klikněte na Pokročilé > JSON | Stáhne hodnoty nezpracovaných dat jako JSON, na rozdíl od dat, která byla agregována podél různých dimenzí. |
| JRXML | Klikněte na Pokročilé > JRXML | Produkuje šablonu Jasper Report, kterou lze dále přizpůsobit na základě vašich přesných potřeb a použít jako základ pro standardní hlášení v DHIS 2. |
| Nezpracovaná data SQL | Klikněte na Upřesnit > Nezpracovaná data SQL | Poskytuje skutečný příkaz SQL používaný ke generování vizualizace dat. Můžete jej použít jako zdroj dat v sestavě Jasper nebo jako základ pro pohled SQL. |

## Vizualizace jako mapa { #see-visualization-as-map }

Chcete-li vidět, jak by vizualizace vypadala na mapě, vyberte po dokončení vytváření vizualizace typ vizualizace `Otevřít jako mapu`.

![](resources/images/data-visualizer/data-visualizer-open-as-map.png)

# Použití aplikace Mapy { #using_maps }

## O aplikaci Mapy { #about_maps }

Aplikace Mapy je představena ve verzi 2.29 a slouží jako náhrada aplikace GIS. Nabízí intuitivnější a uživatelsky přívětivější rozhraní. Mapovací modul od verze 2.34 je založen na technologii WebGL, která dokáže zobrazit tisíce funkcí na mapě současně.

S aplikací Mapy můžete překrýt více vrstev a vybrat si mezi různými základními mapami. Můžete vytvářet tematické mapy oblastí a bodů, prohlížet zařízení na základě klasifikací a vizualizovat spádové oblasti pro každé zařízení. Můžete přidat štítky do oblastí a bodů a vyhledávat a filtrovat podle různých kritérií. Body můžete přesouvat a nastavovat polohy za chodu. Mapy lze uložit jako oblíbené a sdílet s ostatními uživateli a skupinami nebo stáhnout jako obrázek.

> **Poznámka**
>
> Chcete-li použít předdefinované legendy v aplikaci **Mapy**, musíte je nejprve vytvořit v aplikaci **Údržba**.

![](resources/images/maps/maps_main.png)

-   **Panel vrstev** na levé straně pracovního prostoru zobrazuje přehled vrstev pro aktuální mapu:

    -   V pořadí jak jsou vrstvy přidávány pomocí tlačítka **(+) Přidat vrstvu**, jsou uspořádány a spravovány na tomto panelu.

    -   Na panelu se vždy zobrazuje **základní mapa**. Výchozí základní mapa je OSM Light a je vybrána ve výchozím nastavení. OpenStreetMap Podrobně obsahuje další prvky mapy a názvy míst. K dispozici jsou 4 základní mapy z Bing Maps, které nahrazují Mapy Google poskytované v předchozích verzích. Bing Road a Bing Dark zobrazuje silnice, hranice a místa. Pokud jsou barvy na vrstvách mapy jasné, použijte tmavou verzi. Štítky Bing Aerial a Bing Aerial Labs jsou satelitní a podrobné letecké snímky. Přepínejte mezi nimi výběrem požadovaného obrázku.

    -   Malé tlačítko se šipkou vpravo od panelu vrstvy nahoře umožňuje panel skrýt nebo zobrazit.

<!-- konec seznamu -->

-   Tlačítko **Soubor** vlevo nahoře umožňuje otevírat a ukládat mapy:

    -   Nový

        vymaže všechny existující vrstvy mapy a vytvoří novou mapu.

    -   Otevřít

        zobrazí dialogové okno se seznamem existujících map, kde budou otevřeny, přejmenovány, sdíleny a odstraněny. _Název aktuální mapy je zobrazen v záhlaví nad tlačítkem Soubor_.

    -   Uložit

        uloží všechny změny na aktuální mapu.

    -   Uložit jako

        uloží aktuální mapu pod novým názvem.

    -   Přejmenovat

        umožňuje změnit název a / nebo popis aktuální mapy.

    -   Překládejte

        vám umožní přeložit název a / nebo popis aktuální mapy.

    -   Sdílet

        otevře dialog, kde lze aktuální mapu sdílet se všemi nebo se skupinou uživatelů.

    -   Získat odkaz

        poskytne přímý odkaz na aktuální mapu.

    -   Vymazat

        vymaže aktuální mapu.

<!-- konec seznamu -->

-   Tlačítko **Stáhnout** vedle tlačítka Soubor vám umožňuje stáhnout aktuální mapu jako obrázek PNG.

<!-- konec seznamu -->

-   Tlačítko **Interpretace** vpravo nahoře otevírá panel interpretací na pravé straně pracovního prostoru. Na tlačítko lze kliknout, pouze pokud je mapa uložena.

    -   **Podrobnosti mapy** zobrazuje informace o aktuální mapě.

    -   **Interpretace** vám umožňuje prohlížet, přidávat, upravovat a sdílet interpretace aktuální mapy.

<!-- konec seznamu -->

-   Tlačítka **+** a **-** na mapě umožňují přiblížit a oddálit mapu. Přiblížení kolečka myši je plynulé, což nám umožňuje dokonale přizpůsobit mapu vašemu obsahu.

-   Tlačítko **otočit mapu** (trojúhelníkové šipky) umožňuje otáčet a naklánět mapu a vylepšit tak zobrazení vašich dat. Stisknutím tlačítka (nebo ovládací klávesy na klávesnici) při pohybu myši změňte zobrazení mapy. Klepnutím na tlačítko znovu obnovíte zobrazení.

-   **Celá obrazovka** (čtyři šipky) umožňuje zobrazit mapu na celou obrazovku. Chcete-li ukončit celou obrazovku, klikněte znovu na tlačítko nebo na klávesu Escape na klávesnici.

*   **Přiblížit na obsah** (ohraničený symbol lupy) automaticky upraví úroveň přiblížení a polohu středu mapy tak, aby byla data na mapě zaostřena.

*   **Hledat** (symbol lupy) umožňuje vyhledávat a přeskakovat na místo na mapě.

*   Tlačítko **měřítko** umožňuje měřit vzdálenosti a oblasti na mapě.

*   Kliknutím pravým tlačítkem na mapu zobrazíte zeměpisnou délku a šířku daného místa.

**Základní mapy**

Vrstvy základní mapy jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

![](resources/images/maps/maps_basemap_card.png)

V horní části karty základní mapy zleva doprava jsou:

-   Název vybrané základní mapy

-   Symbol šipky pro sbalení a rozbalení karty základní mapy

Ve středu karty základní mapy je seznam dostupných základních map. Aktuální základní mapa je zvýrazněna.

Pod spodní částí karty základní mapy je:

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

## Vytvořte novou mapu { #using_maps_create_map }

1.  V nabídce **Aplikace** klikněte na **Mapy**. Otevře se okno **DHIS2 Mapy**.

2.  Klikněte na tlačítko (+) Přidat vrstvu vlevo nahoře. Zobrazí se dialogové okno pro výběr vrstvy:

    ![](resources/images/maps/maps_layer_selection.png)

3.  Vyberte vrstvu, kterou chcete přidat na aktuální mapu. Možnosti jsou:

    -   [Tematické](#using_maps_thematic_layer)

    -   [Události](#using_maps_event_layer)

    -   [Trasované entity](#using_maps_tracked_entity_layer)

    -   [Zařízení](#using_maps_facility_layer)

    -   [Hranice](#using_maps_boundary_layer)

    Kromě toho existuje několik vrstev poskytovaných aplikací Google Earth Engine a dalšími službami:

    -   Populace

    -   Věkové skupiny obyvatelstva

    -   Nadmořská výška

    -   Srážky

    -   Teplota

    -   Zemský pokryv

    _Překrytí štítky_ je [externí vrstva](#using_maps_external_map_layers) definovaná v aplikaci Údržba.

## Spravujte tematické vrstvy { #using_maps_thematic_layer }

_Tematické mapy_ představují prostorové variace geografických distribucí. Vyberte požadovanou kombinaci indikátoru / datového prvku, období a úrovně organizační jednotky. Pokud má vaše databáze souřadnice a agregované hodnoty dat pro tyto organizační jednotky, zobrazí se na mapě.

> **Poznámka**
>
> Musíte mít vygenerované analytické tabulky DHIS2, abyste měli k dispozici agregované hodnoty dat.

![](resources/images/maps/maps_thematic_mapping.png)

Tematické vrstvy jsou v panelu vrstev reprezentovány vrstvou _karty_, například:

V horní části tematické karty zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název a období spojené s vrstvou

-   Symbol šipky pro sbalení a rozbalení tematické karty

Uprostřed tematické karty je legenda označující rozsahy hodnot zobrazené na vrstvě.

Ve spodní části tematické karty zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte tematickou vrstvu { #create-a-thematic-layer }

Chcete-li vytvořit vrstvu události, vyberte **Thematic** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy Události.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_thematic_layer_dialog_DATA.png)

    -   Vyberte datový typ a poté vyberte skupinu a cílový prvek. Dostupná pole závisí na typu vybrané položky.

    -   Vyberte hodnotu z pole **Typ agregace**, aby se hodnoty dat zobrazily na mapě. Ve výchozím nastavení je vybrána možnost „Podle datového prvku“. Alternativní hodnoty jsou: Count; Průměrný; Součet; Standardní odchylka; Odchylka; Min; Max. Viz také [Agregační operátory](https://dhis2.github.io/dhis2-docs/master/en/user/html/ch10s05.html#d0e8082).

2.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_thematic_layer_dialog_PERIOD.png)

    -   vyberte časové období, během kterého jsou tematická data mapována. Můžete vybrat relativní nebo pevné období.

        -   Relativní období

            V poli **Typ období** vyberte **Relativní** a poté vyberte jedno z relativních období, například **Minulý rok** nebo **Posledních 12 měsíců**, v poli **Období**.

            **Výchozí relativní období pro analýzu** lze nastavit v aplikaci **Nastavení systému**.

            Pokud vyberete relativní období pokrývající více let / měsíců / týdnů / dnů, může být vrstva zobrazena jako

            -   Single (agregát)

                Zobrazit agregované hodnoty pro vybrané relativní období (výchozí).

            -   Časová osa

                Zahrnuje časovou osu, která vám umožní procházet obdobími. Na stejnou mapu lze přidat pouze jednu vrstvu časové osy.

            -   Rozdělit zobrazení mapy

                Zobrazit více map, které vám umožní porovnávat různá období vedle sebe. Podporováno pro relativní období s 12 nebo méně položkami. Nelze kombinovat s jinými typy vrstev.

        -   Pevné období

            V poli **Typ období** vyberte délku období a poté vyberte cíl v poli **Období**.

        -   Datum zahájení / ukončení

            V poli **Typ období** vyberte **Datum zahájení / ukončení** a vyplňte datum zahájení a datum ukončení.

3.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_thematic_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek, úrovně organizačních jednotek v hierarchii, skupiny organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

4.  Na kartě **FILTR**:

    ![](resources/images/maps/maps_thematic_layer_dialog_FILTER.png)

    -   Kliknutím na PŘIDAT FILTR a výběrem dostupné datové položky přidáte do sady dat nový filtr.

        -   V rozevíracím seznamu vyberte datovou dimenzi. Počet zobrazených kót můžete snížit pomocí vyhledávacího pole. Kliknutím na název vyberte dimenzi.

        -   Když je vybrána dimenze, dostanete druhou rozbalovací nabídku s položkami dimenze. Zaškrtněte položky, které chcete do filtru zahrnout.

        Lze přidat více filtrů. Filtr odstraníte kliknutím na tlačítko koše vpravo od filtru.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_thematic_layer_dialog_STYLE.png)

    -   Vyberte buď **Choropleth** nebo **Bublinové mapy**.

        -   Choropleth přiřadí barvu každému tvaru jednotky org podle hodnoty dat. Toto je doporučená technika, pokud jsou data normalizována (na obyvatele).

        -   Bublinová mapa zobrazí hodnoty dat jako proporcionální kruhy. Tuto techniku použijte, pokud data nejsou normalizována (absolutní čísla). Kruhy jsou umístěny ve středu každé organizační jednotky.

    -   Nastavte **Nízký poloměr** a **Vysoký poloměr** pro proporcionální kruhy nebo bodové vybavení. Kruhy budou škálovány mezi nízkým a vysokým poloměrem podle hodnoty dat. Poloměr musí být mezi 0 a 50 px.

    -   **Zobrazit štítky**: Umožňuje zobrazení názvů organizačních jednotek ve vrstvě. Zde lze upravit velikost, váhu, styl a barvu písma.

    -   **Zobrazit žádná data**: Ve výchozím nastavení se organizační jednotky s chybějícími datovými hodnotami na mapě nezobrazí. Toto políčko zaškrtněte, pokud je chcete ukázat s barvou. Kliknutím barvu změníte.

    -   Vyberte typ legendy:

        -   **Automatická barevná legenda**: aplikace pro vás vytvoří legendu podle toho, jakou metodu klasifikace, počet tříd a barevnou škálu vyberete. Nastavte **Klasifikace** buď:

            -   Stejné intervaly

                rozsah každého intervalu bude (nejvyšší hodnota dat - nejnižší hodnota dat / počet tříd)

            -   Stejné počty

                tvůrce legendy se pokusí rozdělit organizační jednotky rovnoměrně.

        -   **Předdefinovaná barevná legenda**: Vyberte mezi předdefinovanými legendami.

        -   **Jednobarevná legenda**: Vyberte barvu bublin nebo kruhů. K dispozici pouze pro bublinové mapy.

6.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte tematickou vrstvu { #modify-a-thematic-layer }

1.  Na panelu vrstev klikněte na ikonu úpravy (tužka) na kartě tematické vrstvy.

2.  Podle potřeby upravte nastavení na libovolné kartě.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty v tematické vrstvě { #filter-values-in-a-thematic-layer }

Tematické vrstvy mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě tematické vrstvy.

![](resources/images/maps/maps_thematic_layer_data_table.png)

Tabulka dat zobrazuje data tvořící tematickou vrstvu.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   HODNOTA

        filtruje hodnoty podle zadaných čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   LEGENDA

        filtrovat podle legendy obsahující daný text

    -   ROZSAH

        filtrovat podle rozsahů obsahujících daný text

    -   ÚROVEŇ

        úroveň filtru podle čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   NADŘAZENÉ

        filtrovat podle nadřazených názvů obsahujících daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

    -   BARVA

        filtruje podle barevných názvů obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte organizační jednotku { #search-for-an-organisation-unit }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých organizačních jednotek.

### Procházejte mezi hierarchiemi organizace { #navigate-between-organisation-hierarchies }

Pokud jsou na mapě viditelné organizační jednotky, můžete v hierarchii snadno procházet nahoru a dolů bez použití uživatelského rozhraní úrovně / nadřazené.

1.  Klepněte pravým tlačítkem na jednu z organizačních jednotek.

2.  Vyberte **Přejít výš o jednu úroveň** nebo **Přejít níž o jednu úroveň**.

    Možnost rozbalení je zakázána, pokud jste na nejnižší úrovni nebo pokud na níže uvedené úrovni nejsou k dispozici žádné souřadnice. Podobně je na nejvyšší úrovni zakázána možnost procházení.

### Odstraňte tematickou vrstvu { #remove-thematic-layer }

Chcete-li vymazat všechna data v tematické vrstvě:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy událostí { #using_maps_event_layer }

Vrstva událostí zobrazuje geografické umístění událostí registrovaných ve sledovači DHIS2. Za předpokladu, že události mají přidružené souřadnice bodu nebo mnohoúhelníku, můžete pomocí této vrstvy přejít z agregovaných dat zobrazených v tematických vrstvách na jednotlivé jednotlivé události nebo případy.

Můžete také zobrazit agregované události v objektu nebo na hranici. Děláte to prostřednictvím tematické vrstvy pomocí datových položek událostí. To je užitečné, pokud máte pouze souřadnice pro organizační jednotku, pod kterou jsou události zaznamenávány.

![](resources/images/maps/maps_event_layer.png)

Vrstvy událostí jsou reprezentovány vrstvou _cards_ v panelu vrstev, například:

V horní části karty události zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název a období spojené s vrstvou

-   Symbol šipky pro sbalení a rozbalení karty události

Uprostřed karty události je legenda označující styl vrstvy.

Ve spodní části karty události zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu události { #maps_create_event_layer }

Chcete-li vytvořit vrstvu událostí, vyberte **Události** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy Události.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_event_layer_dialog_DATA.png)

    -   Vyberte program a poté vyberte fázi programu. Pole **Fáze** se zobrazí pouze po výběru programu.

        Pokud je pro vybraný program k dispozici pouze jeden stupeň, stupeň se automaticky vybere.

    -   Vyberte hodnotu v **souřadnicovém poli** pro polohy zobrazené na mapě. Ve výchozím nastavení je vybrána možnost „Umístění události“. V závislosti na datových prvcích nebo atributech, které patří k programu, jsou k dispozici další souřadnice, například „Pozice domácnosti“.

    -   Ve výchozím nastavení jsou všechny události se souřadnicemi zobrazeny na mapě. Pomocí pole **Stav události** můžete zobrazit pouze události, které mají jeden stav: Aktivní, Dokončeno, Naplánováno, Zpožděno nebo Přeskočeno.

2.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_event_layer_dialog_PERIOD.png)

    -   vyberte časové rozpětí, kdy došlo k událostem. Můžete vybrat pevné období nebo relativní období.

        -   Relativní období

            V poli **Období** vyberte jedno z relativních období, například **Tento měsíc** nebo **Minulý rok**.

            **Výchozí relativní období pro analýzu** lze nastavit v aplikaci **Nastavení systému**.

        -   Pevné období

            V poli **Období** vyberte **Datum zahájení / ukončení** a vyplňte datum zahájení a datum ukončení.

3.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_event_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

4.  Na kartě **FILTR**:

    ![](resources/images/maps/maps_event_layer_dialog_FILTER.png)

    -   Kliknutím na PŘIDAT FILTR a výběrem dostupné datové položky přidáte do sady dat nový filtr.

        -   U datové položky typu _sada možností_ můžete vybrat libovolnou z možností z rozevíracího seznamu pomocí šipky dolů nebo začátkem psaní přímo do pole pro filtrování možností.

        -   U datové položky typu _číslo_ můžete vybrat operátory jako rovná se, nerovná se, větší nebo menší než.

        -   U datové položky typu _boolean_ (ano / ne) můžete zaškrtnout políčko, pokud má být podmínka platná nebo pravdivá.

        -   Pro datovou položku typu _text_ získáte dvě možnosti: **Obsahuje** znamená, že dotaz bude odpovídat všem hodnotám, které obsahují vaši vyhledávací hodnotu, a **Je přesný** znamená, že pouze hodnoty, které jsou zcela identické s vaším vyhledávacím dotazem bude vrácena.

        Lze přidat více filtrů. Filtr odstraníte kliknutím na tlačítko koše vpravo od filtru.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_event_layer_dialog_STYLE.png)

    -   Vyberte **Seskupit události** pro seskupení blízkých událostí (klastr) nebo **Zobrazit všechny události** pro samostatné zobrazení událostí.

    -   Vyberte **barvu** pro událost nebo body klastru.

    -   Vyberte **okruh** (mezi 1 a 20) pro události.

    -   Vyberte **Zobrazit vyrovnávací paměť**, chcete-li zobrazit vizuální vyrovnávací paměť kolem každé události. Zde lze upravit poloměr vyrovnávací paměti. Tato možnost je k dispozici, pouze pokud vyberete **Zobrazit všechny události** výše.

    -   Vyberte **Styl podle datového prvku**, aby se události vybarvily podle hodnoty dat. Pokud také zvolíte seskupení událostí, budou se příchutě zobrazovat jako malé koblihové grafy ukazující distribuci hodnot dat. Možnosti se u různých datových typů liší:

        -   **Sady možností**: Vyberte barvu pro každou možnost v sadě možností. V aplikaci Údržba můžete nastavit výchozí barvy možnosti.

        -   **Čísla**: Numerický datový prvek můžete stylovat [stejným způsobem jako tematické vrstvy](#using_maps_thematic_layer_style) pomocí automatických nebo předdefinovaných legend.

        -   **Booleans**: Vyberte barvu pro true / yes a jinou pro false / no.

6.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte vrstvu události { #modify-an-event-layer }

1.  V panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy událostí.

2.  Podle potřeby upravte nastavení na kartách DATA, OBDOBÍ, FILTR, ORG JEDNOTKA a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Výpis a filtrování událostí { #listing-and-filtering-events }

Vrstvy událostí mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy událostí.

![](resources/images/maps/maps_event_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu událostí.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   ID

        filtrovat podle ID událostí obsahujících daný text

    -   ORG JEDNOTKA

        filtrovat podle názvu organizační jednotky obsahující daný text

    -   UDÁLOST

        filtrovat podle času události obsahujícího daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

    -   **Styl podle datového prvku**: Pokud jsou události stylizovány datovým prvkem (např. Pohlaví), lze filtrovat jak datovou hodnotu, tak barvu.

    -   **Zobrazit ve zprávách**: Datové prvky, u kterých je zaškrtnuto zobrazení ve zprávách, se zobrazí v samostatných sloupcích (viz níže, jak se přidávají).

    -   Hodnoty číselných dat lze filtrovat podle daných čísel a / nebo rozsahů, například: 2,\>3&\<8

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Upravit informace v tabulce dat událostí a vyskakovacích oknech { #modify-information-in-event-data-table-and-popups }

Informace zobrazené ve vyskakovacím okně události můžete upravit.

![](resources/images/maps/maps_eventlayer_eventinfopopup.png)

1.  Otevřete aplikaci **Údržba**.

2.  Vyberte **Program**.

3.  Klikněte na program, který chcete upravit, a vyberte **2 Přiřadit datové prvky**.

4.  U každého datového prvku, který chcete zobrazit ve vyskakovacím okně, vyberte odpovídající **Zobrazit ve zprávách**.

5.  Klikněte **Uložit**.

### Stáhněte si nezpracovaná data vrstvy událostí { #download-raw-event-layer-data }

Nezpracovaná data pro vrstvy událostí lze stáhnout ve formátu GeoJSON pro pokročilejší geoanalýzu a zpracování v desktopovém GIS softwaru, jako je [QGIS](https://www.qgis.org/). Stažená data zahrnují všechny jednotlivé události jako funkce GeoJSON, včetně atributů pro každý datový prvek vybraný pro **Zobrazit v přehledech**.

![](resources/images/maps/maps_data_download_dialog.png)

-   Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Stáhnout data**

-   Vyberte **ID format**, který se má použít jako klíč pro hodnoty datových prvků ve staženém souboru GeoJSON. K dispozici jsou tři možnosti:

    -   **ID** - Použijte jedinečné ID datového prvku
    -   **Název** - Použijte lidsky čitelný Název datového prvku (přeložený)
    -   **Kód** - Použijte kód datového prvku

-   Vyberte, zda **Použít čitelné klíče** pro další atributy Události, jako je fáze programu, zeměpisná šířka, délka, data události a ID organizační jednotky, název a kód. Pokud tato možnost **není** vybrána, tyto hodnoty budou ID vhodné pro počítač namísto názvu čitelného (a přeloženého) pro člověka.

-   Kliknutím na tlačítko **STÁHNOUT** vygenerujte a stáhněte soubor GeoJSON. Data budou vyžádána ze serveru DHIS2 a zpracována mapovou aplikací. Dokončení této operace může trvat několik minut.

-   Po stažení souboru GeoJSON jej lze importovat do většiny standardních softwarových aplikací GIS.

> Uvědomte si, že stažená data neobsahují informace o stylu, protože nejsou nativně podporována formátem GeoJSON. Styly lze volitelně znovu vytvořit v externích aplikacích GIS pomocí atributů každé funkce.

### Vymazat vrstvu událostí { #clear-event-layer }

Postup vymazání všech dat vrstvy událostí na mapě:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy sledovaných entit { #using_maps_tracked_entity_layer }

Vrstva trasovaných entit zobrazuje geografické umístění trasovaných entit registrovaných v DHIS2. Pokud trasované entity mají přidružené souřadnice bodu nebo mnohoúhelníku, můžete je prozkoumat na mapě.

![](resources/images/maps/maps_tracked_entity_layer.png)

Sledované vrstvy entit jsou reprezentovány kartami vrstev v panelu vrstev, například:

V horní části karty trasované entity zleva doprava jsou:

-   Pole pro uchopení myší umožňující přetahování a nové pořadí vrstev.

-   Název a období spojené s vrstvou.

-   Symbol šipky pro sbalení a rozbalení karty trasované entity.

Ve středu karty trasované entity je legenda označující stylování vrstvy.

Ve spodní části karty trasované entity zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu trasované entity { #maps_create_tracked_enity_layer }

Chcete-li vytvořit vrstvu trasované entity, vyberte **Sledované entity** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy trasované entity.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_DATA.png)

    -   Vyberte **Typ trasované entity**, který chcete zobrazit na mapě.

    -   Vyberte **Program**, kam trasované entity patří.

    -   Pomocí pole **Stav programu** vyberte stav registrace sledovaných entit, které chcete zahrnout: Všechny, Aktivní, Dokončeno nebo Zrušeno.

    -   Nastavte stav **Sledování** trasované entity pro daný program.

2.  Na kartě **Vztahy**

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_RELATIONSHIPS.png)

    > **Caution**
    >
    > Displaying tracked entity relationships in Maps is an experimental feature

    -   Pokud byl zároveň vybrán typ trasované entity, můžete zaškrtnout políčko **Zobrazit vztahy trasované entity**

    -   Po zaškrtnutí můžete z rozevíracího seznamu vybrat typ vztahu, který se má zobrazit na mapě. K dispozici jsou pouze vztahy FROM vybraného typu trasované entity.

3.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_PERIOD.png)

    -   Pokud není vybrán žádný program, můžete nastavit počáteční a konečné datum, kdy byly trasované entity naposledy aktualizovány.

    -   Pokud je vybrán program, můžete nastavit období, kdy byly trasované entity naposledy aktualizovány nebo kdy byly zaregistrovány nebo zapsány do programu.

4.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Máte 3 režimy výběru:

        -   **Pouze vybrané**: Zahrnout pouze trasované entity patřící k vybraným organizačním jednotkám.

        -   **Vybrané a níže**: Zahrnuty trasované entity ve vybraných organizačních jednotkách a další přímo pod nimi.

        -   **Vybrané a všechny níže**: Zahrnuty trasované entity a všechny níže vybrané organizační jednotky.

5.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_tracked_entity_layer_dialog_STYLE.png)

    -   Vyberte **barvu** pro body a polygony trasované entity.

    -   Vyberte **velikost bodu** (poloměr mezi 1 a 20) pro body.

    -   Vyberte **Zobrazit vyrovnávací paměť**, chcete-li zobrazit vizuální vyrovnávací paměť kolem každé trasované entity. Zde lze upravit vzdálenost vyrovnávací paměti v metrech.

    -   Pokud byl na kartě relací vybrán typ vztahu, můžete pro vztahy a související trasované entity vybrat **barvu**, **velikost bodu** a **barvu čáry**

6.  Klikněte na **PŘIDAT / AKTUALIZOVAT VRSTVU**.

### Upravte vrstvu trasované entity { #modify-a-tracked-entity-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy trasované entity.

2.  Podle potřeby upravte nastavení na kartách DATA, OBDOBÍ, ORGANIZAČNÍ JEDNOTKA a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Vymazat vrstvu trasované entity { #clear-a-tracked-entity-layer }

Postup vymazání vrstvy trasované entity z mapy:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvy zařízení { #using_maps_facility_layer }

Vrstva zařízení zobrazuje ikony, které představují typy zařízení. Polygony se nezobrazují na mapě, takže se ujistěte, že jste vybrali úroveň organizační jednotky, která má zařízení.

_Polygon je uzavřená oblast na mapě představující zemi, okres nebo park._

![](resources/images/maps/maps_facility_layer.png)

Vrstvy zařízení jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

V horní části karty zařízení zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název **Zařízení**

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Symbol šipky pro sbalení a rozbalení karty zařízení

Uprostřed karty zařízení je legenda označující zastoupení skupiny.

Ve spodní části karty zařízení zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořte vrstvu zařízení { #create-a-facility-layer }

Chcete-li vytvořit vrstvu zařízení, vyberte **Zařízení** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy zařízení.

1.  Na kartě **NASTAVENÍ SKUPIN**:

    ![](resources/images/maps/maps_facility_layer_dialog_GROUPSET.png)

    -   Vyberte ** Skupinovou sadu ** ze seznamu sad skupin organizačních jednotek definovaných pro vaši instanci DHIS2.

2.  Na kartě **ORGANIZAČNÍ JEDNOTKY**

    ![](resources/images/maps/maps_facility_layer_dialog_ORG_UNITS.png)

    -   vyberte úroveň (úrovně) organizační jednotky nebo skupiny (skupin) z polí pro výběr na pravé straně.

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

3.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_facility_layer_dialog_STYLE.png)

    -   vyberte jakýkoli styl, který chcete použít na zařízení.

        -   Zobrazit štítky

            Umožňuje zobrazit štítky na vrstvě. Zde lze upravit velikost, řez a barvu písma.

        -   Zobrazit vyrovnávací paměť

            Umožňuje zobrazit vizuální vyrovnávací paměť na vrstvě kolem každého zařízení. Zde lze upravit poloměr vyrovnávací paměti.

4.  Klikněte na **PŘIDAT VRSTVU**.

### Vytvořte nebo upravte vrstvu zařízení { #create-or-modify-a-facility-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy zařízení.

2.  Podle potřeby upravte nastavení na kartách NASTAVENÍ SKUPIN, ORGANIZAČNÍ JEDNOTKY a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty ve vrstvě zařízení { #filter-values-in-a-facility-layer }

Vrstvy zařízení mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy zařízení.

![](resources/images/maps/maps_facility_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu zařízení.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte zařízení { #search-for-a-facility }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých zařízení.

### Odstraňte vrstvu zařízení { #remove-facility-layer }

Chcete-li vymazat všechna data ve vrstvě zařízení:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

### Spravujte zařízení ve vrstvě { #manage-facilities-in-a-layer }

Můžete mít zařízení ve vrstvách **Zařízení**, **Hranice** a **Tematické**.

#### Přemístěte zařízení { #relocate-a-facility }

1.  Klikněte pravým tlačítkem na zařízení a klikněte na **Přemístit**.

2.  Umístěte kurzor na nové místo.

    Nová souřadnice je uložena trvale. To nelze vrátit zpět.

#### Přehodit zeměpisnou délku a šířku zařízení { #swap-longitude-and-latitude-of-a-facility }

1.  Klikněte pravým tlačítkem na zařízení a klikněte na **Prohodit zeměpisnou délku / šířku**.

    To je užitečné, pokud uživatel při vytváření organizační jednotky převrátil souřadnice zeměpisné šířky a délky.

#### Zobrazit informace o zařízení { #display-facility-information }

Informace o organizační jednotce nastavené správcem můžete zobrazit takto:

<table>
<caption>Zobrazit informace o organizační jednotce</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>Funkce</th>
<th>Akce</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Zobrazit informace pro aktuální období</p></td>
<td><ol type="1">
<li><p>Klikněte na zařízení.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><p>Zobrazit informace za vybrané období</p></td>
<td><ol type="1">
<li><p>Klikněte pravým tlačítkem na zařízení a klikněte na <strong>Zobrazit informace</strong>.</p></li>
<li><p>V sekci <strong>Infrastrukturní data</strong>, vyberte období.</p></li>
</ol>
<blockquote>
<p><strong>Poznámka</strong></p>
<p>Nakonfigurujete zobrazená data infrastruktury v aplikaci <strong>Systémové Nastavení</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Spravujte vrstvy hranic { #using_maps_boundary_layer }

Vrstva hranic zobrazuje hranice a umístění vašich organizačních jednotek. Tato vrstva je zvláště užitečná, pokud jste offline a nemáte přístup k mapám na pozadí.

![](resources/images/maps/maps_bound_layers.png)

Vrstvy hranic jsou reprezentovány vrstvou _karty_ v panelu vrstev, například:

V horní části karty hranic zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název **Hranice**

-   Symbol šipky pro sbalení a rozšíření hraniční karty

Pod spodní hraniční kartou zleva doprava jsou:

-   Tlačítko úprav (tužka) pro otevření dialogového okna konfigurace vrstvy

-   Symbol oka pro přepínání viditelnosti vrstvy

-   Posuvník pro úpravu průhlednosti vrstvy

-   Tlačítko více akcí (tři tečky) s dalšími možnostmi:

    -   Přepínací tlačítko **datová tabulka** pro zobrazení nebo skrytí datové tabulky spojené s vrstvou

    -   **Stáhnout data** vám umožní stáhnout data pro tuto vrstvu ve formátu GeoJSON pro použití v jiném mapovacím softwaru

    -   **Upravit vrstvu** je stejné jako tlačítko Upravit výše

    -   **Odstranit vrstvu** odstraní tuto vrstvu z aktuální mapy.

### Vytvořit vrstvu hranic { #create-a-boundary-layer }

Chcete-li vytvořit vrstvu hranic, zvolte **Hranice** ve výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy hranic.

1.  Na kartě **ORGANIZAČNÍ JEDNOTKY**

    ![](resources/images/maps/maps_boundary_layer_dialog_ORG_UNITS.png)

    -   vyberte úroveň (úrovně) organizační jednotky nebo skupiny (skupin) z polí pro výběr na pravé straně.

    -   Vyberte organizační jednotky, které chcete do vrstvy zahrnout. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

2.  Na kartě **STYLE**:

    ![](resources/images/maps/maps_boundary_layer_dialog_STYLE.png)

    -   vyberte jakýkoli styl, který chcete použít na hranice.

        -   Zobrazit štítky

            Umožňuje zobrazit štítky na vrstvě. Zde lze upravit velikost a řez písma.

        -   Poloměr bodu

            Nastavte základní poloměr, když jsou na vrstvě hranic prezentovány prvky typu bodu, například zařízení.

3.  Klikněte na **PŘIDAT VRSTVU**.

### Upravte vrstvu hranic { #modify-a-boundary-layer }

1.  Na panelu vrstev klikněte na ikonu úprav (tužka) na kartě vrstvy hranic.

2.  Podle potřeby upravte nastavení na kartách ORGANIZAČNÍ JEDNOTKY a STYL.

3.  Klikněte na ** AKTUALIZOVAT VRSTVU **.

### Filtrovat hodnoty ve vrstvě hranic { #filter-values-in-a-boundary-layer }

Vrstvy hranic mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy hranic.

![](resources/images/maps/maps_bound_layer_data_table.png)

Tabulka dat zobrazuje data tvořící vrstvu hranic.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

    -   NÁZEV

        filtrovat podle názvu obsahujícího daný text

    -   ÚROVEŇ

        úroveň filtru podle čísel a / nebo rozsahů, například: 2,\>3&\<8

    -   NADŘAZENÉ

        filtrovat podle nadřazených názvů obsahujících daný text

    -   ID

        filtrovat podle ID obsahujících daný text

    -   TYP

        filtrovat podle typů zobrazení GIS obsahujících daný text

> **Poznámka**
>
> Filtry datové tabulky jsou dočasné a neuloží se s mapovými vrstvami jako součást oblíbené položky.

### Vyhledejte organizační jednotku { #search-for-an-organisational-unit }

Pole filtru NÁZEV v datové tabulce poskytuje efektivní způsob vyhledávání jednotlivých organizačních jednotek zobrazených ve vrstvě hranic.

### Procházejte mezi hierarchiemi organizace { #navigate-between-organisation-hierarchies }

Můžete upravit cíl vrstvy hranic v hierarchii bez použití uživatelského rozhraní úrovně / nadřazené.

1.  Klepněte pravým tlačítkem na jednu z hranic.

2.  Vyberte **Přejít výš o jednu úroveň** nebo **Přejít níž o jednu úroveň**.

    Možnost procházení níže je vypnuta, pokud jste na nejnižší úrovni. Podobně je na nejvyšší úrovni vypnuta možnost procházení na vyšší úroveň.

### Odstranit vrstvu hranic { #remove-boundary-layer }

Chcete-li vymazat všechna data ve vrstvě hranic:

1.  Na kartě vrstvy vlevo klikněte na ikonu _více akcí_ (tři tečky) a poté na **Odebrat vrstvu**.

    Vrstva je odstraněna z aktuální mapy.

## Spravujte vrstvu Earth Engine { #using_maps_gee }

![](resources/images/maps/maps_earth_eng_layer.png)

Vrstvy z Google Earth Engine vám umožňují zobrazovat a agregovat externí data do vašich organizačních jednotek. Použijte vrstvu obyvatelstva pro výpočet počtu lidí žijících v okrese nebo ve vzdálenosti od zdravotnického zařízení. Výšková vrstva umožňuje najít nejnižší, nejvyšší a střední nadmořskou výšku. Pomocí vrstvy krajinného pokryvu můžete zobrazit lesní porost, ornou půdu nebo městské oblasti a vypočítat procento pro každou organizační jednotku.

Podporovány jsou následující vrstvy:

![](resources/images/maps/maps_earth_eng_layer_types.png)

-   **Populace**: Podrobné údaje o populaci z WorldPop ukazující odhadovaný počet lidí žijících v oblasti. K dispozici pro roční období od roku 2000 a dále.

-   **Věkové skupiny obyvatelstva**: Odhadovaný počet lidí žijících v oblasti seskupený podle věku a pohlaví.

-   **Výška**: Nadmořská výška nad hladinou moře.

-   **Srážky**: Hodnoty jsou v milimetrech během období 5 dnů. Aktualizováno měsíčně, během 3. týdne následujícího měsíce. Shromážděno ze satelitů a meteorologických stanic na zemi.

-   **Teplota**: Teploty povrchu země shromážděné ze satelitu. V oblastech s trvalou oblačností se objeví prázdná místa.

-   **Krajinný pokryv**: 17 různých typů krajinného pokryvu shromážděných ze satelitů NASA.

### Vytvořte vrstvu Earth Engine { #create-an-earth-engine-layer }

Chcete-li vytvořit vrstvu Earth Engine, vyberte požadovanou vrstvu z výběru **Přidat vrstvu**. Tím se otevře dialogové okno konfigurace vrstvy.

1.  Na kartě **DATA**:

    ![](resources/images/maps/maps_ee_layer_dialog_DATA.png)

    -   Pro „věkové skupiny populace“ můžete vybrat věk / pohlaví **skupiny**, které chcete zahrnout do agregace dat.

    -   Vyberte **metody agregace**, které chcete použít při výpočtu hodnot pro vybrané organizační jednotky.

        -   **Součet**: Vypočítá celkový počet v rámci každé organizační jednotky. Doporučuje se používat pro vrstvy obyvatelstva.

        -   **Min**: Vrátí minimální hodnotu v jednotce vrstvy zobrazené pod výběrem. Pro vrstvy populace to bude minimum _lidí na hektar_. Pro výškovou vrstvu vrátí nejnižší nadmořskou výšku (metry nad mořem).

        -   **Max**: Vrátí maximální hodnotu v jednotce vrstvy. Pro vrstvy populace to bude minimum _lidí na hektar_. Pro výškovou vrstvu vrátí nejvyšší nadmořskou výšku pro každou organizační jednotku.

        -   **Mean**: Vrátí střední hodnotu v jednotce vrstvy. U vrstev populace to bude průměr _počet lidí na hektar_. U srážkové vrstvy to budou průměrné srážky v milimetrech napříč organizační jednotkou.

        -   **Median**: Vrátí střední hodnotu v jednotce vrstvy. Pro vrstvy populace to bude medián _počet lidí na hektar_. Pro teplotní vrstvu to bude medián °C během dne pro organizační jednotku.

        -   **Standardní odchylka**: Vrátí hodnotu standardní odchylky v jednotce vrstvy.

        -   **Variance**: Vrátí hodnotu rozptylu v jednotce vrstvy.

2.  Na kartě **OBDOBÍ**

    ![](resources/images/maps/maps_ee_layer_dialog_PERIOD.png)

    -   Vyberte období pro zdroj dat. Dostupná období jsou stanovena poskytovatelem dat. Pro vrstvu „věkové skupiny populace“ existuje pouze jedno období, zatímco vrstva „populace“ má k dispozici roční údaje od roku 2000 a dále. Údaje o srážkách jsou k dispozici za období 5 dnů a údaje o teplotě za období 8 dnů.

3.  Na kartě **ORG  JEDNOTKY**:

    ![](resources/images/maps/maps_ee_layer_dialog_ORG_UNITS.png)

    -   Vyberte organizační jednotky, kde chcete zobrazit hodnoty agregovaných dat. Je možné vybrat buď

        -   Jedna nebo více konkrétních organizačních jednotek, úrovně organizačních jednotek v hierarchii, skupiny organizačních jednotek nebo

        -   Relativní úroveň v hierarchii organizační jednotky s ohledem na uživatele. Když vyberete **Organizační jednotku uživatele**, budou se mapová data zobrazovat odlišně pro uživatele na různých úrovních v hierarchii organizační jednotky.

4.  Na kartě **STYL**

    ![](resources/images/maps/maps_ee_layer_dialog_STYLE.png)

    -   Upravte parametry specifické pro typ vrstvy.

    -   Podle potřeby upravte rozsah legendy, kroky a barvy.

    -   Pokud vyberete organizační jednotky, které mají souřadnici jednoho bodu (zařízení), můžete nastavit vyrovnávací paměť poloměru pro výpočet hodnoty dat v rámci. V okruhu 5000 metrů budou agregovány všechny dostupné hodnoty ve vzdálenosti 5 km od zařízení.

5.  Klikněte na **PŘIDAT VRSTVU**.

Kliknutím na regiony nebo zařízení na mapě zobrazíte výsledek agregace pro danou organizační jednotku.

### Výpis hodnot dat { #listing-of-data-values }

Vrstvy Earth Engine mají možnost **datová tabulka**, kterou lze zapnout nebo vypnout na kartě vrstvy.

![](resources/images/maps/maps_ee_layer_data_table.png)

Datová tabulka zobrazuje všechny agregované hodnoty pro vybrané organizační jednotky.

-   kliknutím na název se seřadí tabulka podle tohoto sloupce; přepíná se mezi vzestupným a sestupným řazením.

-   zadáním textu nebo výrazů do polí filtru pod nadpisy použijete tyto filtry na data a zobrazení se upraví podle filtru. Filtry se aplikují následovně:

-   NÁZEV

    filtrovat podle názvu organizační jednotky obsahující daný text

-   ID

    filtrovat podle ID událostí obsahujících daný text

-   TYP

    filtrovat podle typů zobrazení GIS obsahujících daný text

-   HODNOTY AGREGACE

    pro každý z vybraných typů agregace je jeden sloupec

    číselné hodnoty dat lze filtrovat podle daných čísel a / nebo rozsahů, například: 2,\>3&\<8

> **Poznámka**
>
> Filtry datových tabulek jsou dočasné a neukládají se s vrstvami mapy.

## Přidejte externí vrstvy mapy { #using_maps_external_map_layers }

![](resources/images/maps/maps_terrain_imagery.png)

Externí mapové vrstvy jsou reprezentovány buď:

-   Základní mapy

    Ty jsou k dispozici na kartě **základní mapy** v panelu vrstev a jsou vybrány jako všechny ostatní základní mapy.

-   Překryvné vrstvy

    Ty jsou k dispozici ve výběru **Přidat vrstvu**. Na rozdíl od základních map lze překryvy umístit nad nebo pod jakékoli jiné vrstvy překrytí.

Překryvné vrstvy jsou reprezentovány další vrstvou _karty_ v panelu vrstev, například:

V horní části karty překrytí zleva doprava jsou:

-   Pole pro uchopení umožňující přetahování myší a nové pořadí vrstev 

-   Název externí mapové vrstvy

-   Symbol šipky pro sbalení a rozbalení překryvné karty

Uprostřed karty je legenda, pokud ji vrstva má.

Ve spodní části překryvné karty zleva doprava jsou:

-   Posuvník pro úpravu průhlednosti vrstvy

-   Ikona odstranění (koše) pro odstranění vrstvy z aktuální tematické mapy.

## Nabídka Soubor { #using_maps_file_menu }

![](resources/images/maps/maps_file_menu.png)

Ke správě map použijte nabídku **Soubor**. Několik položek nabídky bude deaktivováno, dokud neotevřete nebo neuložíte mapu.

Uložení map usnadňuje jejich pozdější obnovení. Také vám dává příležitost sdílet je s ostatními uživateli jako výklad nebo je umístit na ovládací panel. Všechny typy konfigurací vrstev můžete uložit jako oblíbené.

### Vytvořte novou mapu { #create-a-new-map }

Klikněte na **Soubor** \> **Nový**.

NB\! Toto vymaže aktuální vrstvy mapy, které máte, bez uložení.

### Otevřete novou mapu { #open-a-new-map }

1.  Klikněte na **Soubor** \> **Otevřít**. Otevře se dialogové okno se seznamem map.

2.  Najděte oblíbenou položku, kterou chcete otevřít. Uloženou mapu můžete vyhledat pomocí \< a \> nebo vyhledávacího pole. Seznam je filtrován podle všech znaků, které zadáte. Seznam můžete filtrovat výběrem **Zobrazit vše**, **Vytvořeno mnou** nebo **Vytvořeno ostatními**.

3.  Klikněte na název mapy, kterou chcete otevřít.

### Uložte mapu { #save-a-map }

Když jste vytvořili mapu, je vhodné ji uložit pro pozdější použití:

1.  Klikněte na **Soubor** \> **Uložit**.

2.  Při prvním uložení mapy zadejte **název** (povinné) a **popis** (volitelné).

3.  Klikněte **ULOŽIT**.

### Uložení kopie mapy { #save-a-copy-of-a-map }

1.  Klikněte na **Soubor** \> **Uložit jako ...**

2.  Zadejte **Název** (povinné) a **Popis** (volitelné) pro mapu.

3.  Klikněte **ULOŽIT**.

### Přejmenujte mapu { #rename-a-map }

1.  Klikněte na **Soubor** \> **Přejmenovat**.

2.  Zadejte pro svou mapu nový **Název** nebo **Popis**.

3.  Klikněte na **PŘEJMENOVAT**. Mapa je aktualizována.

### Přeložit mapu { #translate-a-map }

1.  Klikněte na **Soubor** \> **Přeložit**.

2.  Vyberte **národní prostředí** (jazyk), který chcete přeložit.

3.  Zadejte přeložený **Název** a **Popis**. Původní text se zobrazí pod polem.

4.  Klikněte **ULOŽIT**.

### Upravte nastavení sdílení pro mapu { #modify-sharing-settings-for-a-map }

Jakmile mapu vytvoříte a uložíte, můžete mapu sdílet se všemi nebo se skupinou uživatelů. Úprava nastavení sdílení:

1.  Klikněte na **Soubor** \> **Sdílet**. Otevře se dialogové okno nastavení sdílení.

2.  V textovém poli vyhledejte jméno uživatele nebo skupiny, se kterou chcete sdílet své oblíbené, a vyberte jej.

    Vybraný uživatel nebo skupina se přidá do seznamu příjemců.

    Opakováním kroku přidejte další skupiny uživatelů.

3.  Chcete-li povolit externí přístup, zaškrtněte příslušné políčko.

4.  Pro každou skupinu uživatelů zvolte nastavení přístupu. Možnosti jsou:

    -   Žádné (pouze pro výchozí skupiny, protože je nelze odebrat)

    -   Může zobrazit

    -   Může upravovat a prohlížet

5.  Kliknutím na **ZAVŘÍT** dialog zavřete.

### Získejte odkaz na mapu { #get-the-link-to-a-map }

1.  Klikněte na **Soubor** \> **Získat odkaz**. Otevře se dialogové okno odkazu.

2.  Zkopírujte odkaz.

### Odstranění mapy { #delete-a-map }

1.  Klikněte na **Soubor** \> **Odstranit**. Zobrazí se potvrzovací dialog.

2.  Kliknutím na **ODSTRANIT** potvrďte, že chcete oblíbenou položku smazat. Vaše mapa je odstraněna a vrstvy jsou z pohledu vymazány.

## Interpretace map { #mapsInterpretation }

Interpretace je popis mapy v daném období. Tyto informace jsou viditelné v **aplikaci Ovládací panel**. Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací. Na tlačítko lze kliknout, pouze pokud je mapa uložena.

![](resources/images/maps/maps_interpretations_panel.png)

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací.

3.  Klikněte na interpretaci. Vaše mapa zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

### Napište interpretaci pro mapu { #write-interpretation-for-a-map }

Chcete-li vytvořit interpretaci, musíte nejprve vytvořit mapu a uložit ji. Pokud jste svou mapu sdíleli s jinými lidmi, interpretace, kterou napíšete, je viditelná pro tyto lidi.

1.  Otevřete oblíbené s interpretacemi.

2.  Kliknutím na **Interpretace** v pravém horním rohu pracovního prostoru otevřete panel interpretací.

3.  U uživatelů, kteří mají přístup k oblíbeným položkám se zobrazí textové pole se zástupným symbolem „Napsat interpretaci“.

4.  Do textového pole zadejte komentář, otázku nebo interpretaci. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s interpretací nebo komentářem. Interpretaci můžete vidět v **aplikaci Ovládací panel**.

5.  Pokud chcete, aby vaše interpretace měla stejné nastavení sdílení jako mapa, klikněte na **ULOŽIT**.

    Chcete-li pro svou interpretaci změnit nastavení sdílení (viz níže), klikněte na **ULOŽIT & SDÍLET**.

### Změňte nastavení sdílení pro interpretaci { #change-sharing-settings-for-an-interpretation }

1.  Klikněte na interpretaci (viz výše, jak zobrazit interpretaci).

2.  Klikněte na **Sdílet** pod interpretací. Otevře se dialogové okno nastavení sdílení.

3.  Vyhledejte a přidejte uživatele a skupiny uživatelů, se kterými chcete svou mapu sdílet.

4.  Změňte nastavení sdílení pro uživatele, které chcete upravit:

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádný přístup**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro veřejný přístup.

5.  Po aktualizaci nastavení sdílení klikněte na **ZAVŘÍT**.

## Uložte mapu jako obrázek { #using_maps_image_export }

Svou mapu si můžete stáhnout jako obrázek kliknutím na tlačítko Stáhnout v horní nabídce

![](resources/images/maps/maps_download.png)

Stahování map není podporováno v Internet Exploreru nebo Safari, doporučujeme použít Google Chrome nebo Firefox.

1.  Vyberte, zda chcete zahrnout název mapy nebo ne. Tato možnost je k dispozici, pouze pokud je mapa uložena.

2.  Vyberte, zda chcete zahrnout legendu mapy. Legendu můžete umístit do jednoho ze 4 rohů mapy.

3.  Kliknutím na **Stáhnout** si stáhnete mapu.

## Vyhledejte místo { #using_maps_search }

Funkce vyhledávání míst umožňuje vyhledávat téměř jakékoli místo nebo adresu. Tato funkce je užitečná k vyhledání například míst, zařízení, vesnic nebo měst na mapě.

![](resources/images/maps/maps_place_search.png)

1.  Na pravé straně okna Mapy klikněte na ikonu lupy.

2.  Zadejte hledané místo.

    Během psaní se zobrazí seznam shodných míst.

3.  Ze seznamu vyberte umístění. Špendlík označuje polohu na mapě.

## Změřte vzdálenosti a oblasti na mapě { #using_maps_measure_distance }

1.  V levé horní části mapy umístěte kurzor na ikonu **Měření vzdáleností a oblastí** (pravítko) a klikněte na **Vytvořit nové měření**.

2.  Přidejte na mapu body.

3.  Klikněte na **Dokončit měření**.

![](resources/images/maps/maps_measure_distance.png)

## Získejte zeměpisnou šířku a délku na jakémkoli místě { #using_maps_latitude_longitude }

Klikněte pravým tlačítkem na bod na mapě a vyberte **Zobrazit zeměpisnou délku / šířku**. Hodnoty se zobrazí ve vyskakovacím okně.

## Viz také { #see-also }

-   [Spravovat legendy](https://docs.dhis2.org/master/en/user/html/manage_legend.html)

# Analyzujte data v kontingenčních tabulkách { #pivot }

## O aplikaci Kontingenční tabulka { #pivot_about }

S aplikací **Kontingenční tabulka** můžete vytvářet kontingenční tabulky na základě všech dostupných datových dimenzí v DHIS2. Kontingenční tabulka je dynamický nástroj pro analýzu dat, který umožňuje sumarizovat a uspořádat data podle jejich dimenzí. Příklady datových dimenzí v DHIS2 jsou:

-   samotná datová dimenze (například datové prvky, indikátory a události)

-   období (představující časové období pro data)

-   hierarchie organizace (představující geografické umístění dat)

Z těchto dimenzí můžete libovolně vybrat _dimenzionální položky_, které chcete zahrnout do kontingenční tabulky. V DHIS2 můžete vytvořit další dimenze pomocí funkce skupiny. To umožňuje různé cesty agregace, například agregaci podle „partnera“ nebo typu zařízení.

Kontingenční tabulka může uspořádat datové dimenze na _sloupce_, _řádky_ a jako _filtry_. Když umístíte datovou dimenzi na sloupce, v kontingenční tabulce se zobrazí jeden sloupec na položku dimenze. Pokud na sloupce umístíte více datových dimenzí, kontingenční tabulka zobrazí jeden sloupec pro všechny kombinace položek ve vybraných dimenzích. Když umístíte datovou dimenzi na řádky, kontingenční tabulka zobrazí jeden řádek na položku dimenze podobným způsobem. Dimenze, které vyberete jako filtry, nebudou zahrnuty v kontingenční tabulce, ale agregují a filtrují data tabulky na základě vybraných položek filtru.

> **Tip**
>
> - Musíte vybrat alespoň jednu dimenzi na sloupcích nebo řádcích.
>
> - Musíte zahrnout alespoň jednu tečku.
>
> - Sady skupin datových prvků a četnosti přehledů se nemohou objevit ve stejné kontingenční tabulce.
>
> - Kontingenční tabulka nemůže obsahovat více než maximální počet analytických záznamů, který byl zadán v nastavení systému. Maximální počet záznamů může být také omezen maximální RAM, kterou má váš prohlížeč k dispozici. Pokud požadovaný stůl překročí určitou velikost, zobrazí se upozornění. Z této výzvy můžete buď zrušit požadavek, nebo pokračovat ve vytváření tabulky. Zvažte vytvoření menších tabulek namísto jedné tabulky, která zobrazuje všechny vaše datové prvky a indikátory společně.
>
> - Aplikace **Kontingenční tabulka** podporuje rozbalování a zvyšování pro období a organizační jednotku. To znamená, že v kontingenční tabulce můžete například procházet z ročních období na čtvrtletí, měsíce a týdny. Můžete také přejít z globální organizační jednotky do zemí, provincií a zařízení.

## Vytvořte kontingenční tabulku { #pivot_create }

1.  Otevřete aplikaci **Kontingenční tabulka**.

2.  V nabídce vlevo vyberte položky dimenze, které chcete analyzovat, například datové prvky nebo indikátory.

3.  Klikněte na **Rozložení** a uspořádejte datové dimenze jako sloupce, řádky a filtry.

    Pokud chcete, můžete ponechat výchozí výběr.

4.  Klikněte na **Aktualizovat**.

V tomto příkladu jsou indikátory uvedeny jako sloupce a období jako řádky.

![](resources/images/pivot_table/basic_pivot.png)

### Vyberte položky dimenze { #select-dimension-items }

V levé nabídce jsou uvedeny sekce všech dostupných dimenzí dat. V každé sekci můžete vybrat libovolný počet položek dimenze. Jako příklad můžete otevřít sekci pro datové prvky a vybrat libovolný počet datových prvků z dostupného seznamu. Položku můžete vybrat označením a kliknutím na šipku v záhlaví sekce nebo jednoduše poklepáním na položku. Než budete moci v kontingenční tabulce použít datovou dimenzi, musíte vybrat alespoň jednu položku dimenze. Pokud dimenzi uspořádáte jako sloupce nebo řádky, ale nevyberete žádné položky dimenze, bude dimenze ignorována.

K vytvoření kontingenční tabulky musíte vybrat alespoň jeden typ datové dimenze. Dostupné typy jsou popsány v této tabulce:

<table>
<caption> typy datových dimenzí </caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th> Typ datové dimenze </th>
<th> Definice </th>
<th> Příklady </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Indikátory </td>
<td> Indikátor je vypočítaný vzorec založený na datových prvcích. </td>
<td> Pokrytí imunizace v konkrétním okrese. </td>
</tr>
<tr class="even">
<td> Datové prvky </td>
<td> Představuje jev, pro který byla data zachycena. </td>
<td> Počet případů malárie; počet podaných dávek BCG. </td>
</tr>
<tr class="odd">
<td> Datové sady </td>
<td> Kolekce datových prvků seskupených pro sběr dat. Můžete vybrat:
<ul>
<li> <p> <strong> Míry hlášení </strong>: procento skutečných zpráv ve srovnání s očekávaným počtem zpráv </p> </li>
<li> <p> <strong> sazby hlášení včas </strong>: sazby hlášení založené na včasném odeslání formuláře. Včasné podání musí proběhnout do několika dnů po období, za které se podává zpráva. </p> </li>
<li> <p> <strong> skutečné zprávy </strong>: skutečný počet zpráv </p> </li>
<li> <p> <strong> aktuální zprávy včas </strong>: skutečný počet zpráv na základě včasného odeslání formuláře. Včasné podání musí proběhnout do několika dnů po období, za které se podává zpráva. </p> </li>
<li> <p> <strong> Očekávané zprávy </strong>: počet očekávaných zpráv na základě organizačních jednotek, kde byla přiřazena datová sada a četnost hlášení. </p> </li>
</ul> </td>
<td> Míry hlášení pro imunizaci a morbiditu. </td>
</tr>
<tr class="even">
<td> datové položky události </td>
<td> Datový prvek, který je součástí programu představujícího zachycené události. </td>
<td> Průměrná hmotnost a výška dětí ve výživovém programu. </td>
</tr>
<tr class="odd">
<td> Programové indikátory </td>
<td> Vypočítaný vzorec založený na datových prvcích v programu představujících události. </td>
<td> Průměrné skóre BMI u dětí ve výživovém programu. </td>
</tr>
</tbody>
</table>

Tyto dimenze můžete kombinovat a zobrazit například agregovaná data s rychlostí vykazování nebo datové položky událostí společně s indikátory programu, vše ve stejných kontingenčních tabulkách. U datové dimenze „datový prvek“ můžete také vybrat „Součty“ a „Podrobnosti“, což vám umožní zobrazit různé možnosti kombinace kategorií společně na stejné kontingenční tabulce.

U dimenze období si můžete vybrat mezi použitím pevných období nebo relativních období. Příkladem pevného období je „leden 2012“. Chcete-li vybrat pevná období, začněte výběrem typu období ze seznamu typů období. Potom můžete vybrat období ze seznamu dostupných období.

Relativní období jsou období vztahující se k aktuálnímu datu. Příklady relativních období jsou „Poslední měsíc“, „Posledních 12 měsíců“, „Posledních 5 let“. Relativní období lze vybrat zaškrtnutím políček vedle každého období. Hlavní výhodou použití relativních období je to, že když uložíte oblíbenou kontingenční tabulku, zůstane aktualizována nejnovějšími daty, jak plyne čas, aniž byste ji museli neustále aktualizovat.

Pro dimenzi organizační jednotky můžete z hierarchie vybrat libovolný počet organizačních jednotek. Chcete-li vybrat všechny organizační jednotky pod konkrétní nadřazenou organizační jednotkou, klikněte pravým tlačítkem a klikněte na „Vybrat všechny podřízené“. Chcete-li ručně vybrat více organizačních jednotek, klikněte a podržte klávesu **Ctrl** a klikněte na organizační jednotky. Chcete-li dynamicky vložit organizační jednotku nebo jednotky spojené s vaším uživatelským účtem, můžete zaškrtnout „Organizační jednotky uživatele“, „Podřízené org jednotky uživatele“ nebo „Uživatelské jednotky 2. podúrovně“. To je užitečné, když uložíte oblíbenou kontingenční tabulku a chcete ji sdílet s ostatními uživateli, protože při prohlížení oblíbené položky se použijí organizační jednotky propojené s účtem jiného uživatele.

![](resources/images/pivot_table/period_dimension.png)

Dynamické dimenze mohou sestávat ze sad skupin organizačních jednotek, sad skupin datových prvků nebo skupin skupin voleb kategorií, které byly nakonfigurovány s typem „Rozčlenění“. Jakmile budou sady skupin nakonfigurovány, budou k dispozici v kontingenčních tabulkách a lze je použít jako další dimenze analýzy, například k analýze agregovaných dat podle typu organizační jednotky nebo implementujícího partnera. Dynamické dimenze fungují stejně jako pevné dimenze.

> **Tip**
>
> Některé dynamické dimenze mohou obsahovat mnoho položek. To může způsobit problémy s určitými prohlížeči kvůli délce adresy URL, když je vybráno mnoho členů dimenze. Pro dynamické dimenze je k dispozici speciální zaškrtávací políčko „Vše“, které umožňuje implicitně zahrnout všechny dostupné dimenze do kontingenční tabulky, aniž byste museli specifikovat každého člena dimenze.

### Upravit rozložení kontingenční tabulky { #modify-pivot-table-layout }

Po výběru datových dimenzí je čas uspořádat kontingenční tabulku. Kliknutím na „Rozvržení“ v horní nabídce otevřete obrazovku rozvržení. Na této obrazovce můžete umístit své datové dimenze jako sloupce tabulky, řádky nebo filtry kliknutím a přetažením dimenzí ze seznamu dimenzí do příslušného seznamu sloupců, řádků a filtrů. V libovolném ze seznamů můžete nastavit libovolný počet dimenzí. Například můžete kliknout na „Organizační jednotky“ a přetáhnout jej do seznamu řádků, abyste umístili dimenzi organizační jednotky jako řádky tabulky. Uvědomte si, že indikátory, datové prvky a rychlosti vykazování sady dat jsou součástí běžné dimenze „Data“ a budou zobrazeny společně v kontingenční tabulce. Například po výběru indikátorů a datových prvků v levé nabídce můžete přetáhnout „Organizační jednotku“ ze seznamu dostupných dimenzí do seznamu dimenzí řádků a uspořádat je jako řádky v kontingenční tabulce.

![](resources/images/pivot_table/table_layout.png)

Po nastavení kontingenční tabulky můžete její kontingenční tabulku vykreslit kliknutím na „Aktualizovat“ nebo kliknutím na „Skrýt“ skrýt obrazovku rozvržení, aniž by se změny projevily. Protože jsme v našem příkladu vybrali jako řádky dimenzi období i organizační jednotky, kontingenční tabulka vygeneruje všechny kombinace položek v těchto dimenzích a vytvoří takovou tabulku:

![](resources/images/pivot_table/pivot_rows.png)

## Změňte zobrazení kontingenční tabulky { #pivot_change_display }

1.  Otevřete aplikaci **Kontingenční tabulka**.

2.  Vytvořte novou kontingenční tabulku nebo otevřete oblíbenou položku.

3.  Klikněte na **Možnosti**.

4.  Nastavte možnosti podle potřeby.

    <table>
    <caption>Pivot table options</caption>
    <colgroup>
    <col style="width: 21%" />
    <col style="width: 35%" />
    <col style="width: 42%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p>
    <p><strong>Show row totals</strong></p></td>
    <td><p>Displays total values in the table for each row and column, as well as a total for all values in the table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p>
    <p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays subtotals in the table for each dimension.</p>
    <p>If you only select one dimension, subtotals will be hidden for those columns or rows. This is because the values will be equal to the subtotals.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td><p>Shows the dimension names as part of the pivot tables.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide empty columns</strong></p></td>
    <td><p>Hides empty columns from the table. This is useful when you look at large tables where a big part of the dimension items don't have data in order to keep the table more readable.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Skip rounding</strong></p></td>
    <td><p>Skips the rounding of data values, offering the full precision of data values. Can be useful for finance data where the full dollar amount is required.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Aggregation type</strong></p></td>
    <td><p>The default aggregation operator can be over-ridden here, by selecting a different aggregation operator. Some of the aggregation types are <strong>Count</strong>, <strong>Min</strong> and <strong>Max</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Number type</strong></p></td>
    <td><p>Sets the type of value you want to display in the pivot table: <strong>Value</strong>, <strong>Percentage of row</strong> or <strong>Percentage of column</strong>.</p>
    <p>The options <strong>Percentage of row</strong> and<strong>Percentage of column</strong> mean that you'll display values as percentages of row total or percentage of column total instead of the aggregated value. This is useful when you want to see the contribution of data elements, categories or organisation units to the total value.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Measure criteria</strong></p></td>
    <td><p>Allows for the data to be filtered on the server side.</p>
    <p>You can instruct the system to return only records where the aggregated data value is equal, greater than, greater or equal, less than or less or equal to certain values.</p>
    <p>If both parts of the filter are used, it's possible to filter out a range of data records.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Events</strong></p></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful for example to exclude partial events in indicator calculations.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Organisation units</strong></p></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Shows the name of all ancestors for organisation units, for example &quot;Sierra Leone / Bombali / Tamabaka / Sanya CHP&quot; for Sanya CHP.</p>
    <p>The organisation units are then sorted alphabetically which will order the organisation units according to the hierarchy.</p>
    <p>When you download a pivot table with organisation units as rows and you've selected <strong>Show hierarchy</strong>, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Legend</strong></p></td>
    <td><p><strong>Apply legend</strong></p></td>
    <td><p>Applies a legend to the values. This mean that you can apply a colour to the values.</p>
    <p>Select <strong>By data item</strong> to color the table cells individually according to each data element or indicator.</p>
    <p>You configure legends in the <strong>Maintenance</strong> app.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Style</strong></p></td>
    <td><p>Colors the text or background of cells in pivot tables based on the selected legend.</p>
    <p>You can use this option for scorecards to identify high and low values at a glance.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>General</strong></p></td>
    <td><p><strong>Table title</strong></p></td>
    <td><p>Type a title here to display it above the table.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Parameters (for standard reports only)</strong></p></td>
    <td><blockquote>
    <p><strong>Note</strong></p>
    <p>You create standard reports in the <strong>Reports</strong> app.</p>
    <p>In the <strong>Pivot Table</strong> app you set which parameters the system should prompt the user for.</p>
    </blockquote></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Reporting period</strong></p></td>
    <td><p>Controls whether to ask user to enter a report period.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter an organisation unit.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Parent organisation unit</strong></p></td>
    <td><p>Controls whether to ask user to enter a parent organisation unit.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include regression</strong></p></td>
    <td><p>Includes a column with regression values to the pivot table.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Include cumulative</strong></p></td>
    <td><p>Includes a column with cumulative values to the pivot table.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Sort order</strong></p></td>
    <td><p>Controls the sort order of the values.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Top limit</strong></p></td>
    <td><p>Controls the maximum number of rows to include in the pivot table.</p></td>
    </tr>
    </tbody>
    </table>

5.  Klikněte na **Aktualizovat**.

## Spravujte oblíbené položky { #manage-favorites }

Uložení grafů nebo kontingenčních tabulek jako oblíbených usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli jako interpretaci nebo je zobrazit na ovládacím panelu.

Podrobnosti a interpretace vašich oblíbených položek zobrazíte v aplikacích **Kontingenční tabulka**, **Zobrazení dat**, **Zobrazení událostí**, **Zprávy o událostech**. Pomocí nabídky **Oblíbené** můžete spravovat své oblíbené položky.

### Otevřete oblíbenou položku { #open-a-favorite }

1.  Klikněte na **Oblíbené** \> **Otevřít**.

2.  Zadejte název oblíbené položky do vyhledávacího pole nebo kliknutím na **Předchozí** a **Další** zobrazte oblíbené položky.

3.  Klikněte na název oblíbené položky, kterou chcete otevřít.

### Uložit oblíbené { #save-a-favorite }

1.  Klikněte na **Oblíbené** \> **Uložit jako**.

2.  Zadejte **Název** a **Popis** pro vaši oblíbenou položku. Pole popisu podporuje formát RTF, další podrobnosti najdete v části interpretace.

3.  Klikněte **Uložit**.

### Přejmenujte oblíbenou položku { #rename-a-favorite }

1.  Klikněte na **Oblíbené** \> **Přejmenovat**.

2.  Zadejte nový název své oblíbené položky.

3.  Klikněte na **Aktualizovat**.

### Napište interpretaci pro oblíbené { #write-an-interpretation-for-a-favorite }

Interpretace je odkaz na zdroj s popisem dat v daném období. Tyto informace jsou viditelné v aplikaci **Ovládací panel**. Chcete-li vytvořit interpretaci, musíte nejprve vytvořit oblíbenou položku. Pokud jste sdíleli své oblíbené položky s jinými lidmi, interpretace, kterou píšete, je viditelná pro tyto lidi.

1.  Klikněte na **Oblíbené** \> **Napsat výklad**.

2.  Do textového pole zadejte komentář, otázku nebo výklad. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s výkladem nebo komentářem. Výklad můžete vidět v aplikaci **Dashboard**.

    Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown \* a \_ pro **tučné** a _italic_. K dispozici jsou také klávesové zkratky: Ctrl / Cmd + B a Ctrl / Cmd + I. Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: :) :-) :( :-(: +1 :-1. URL jsou automaticky detekovány a převedeny na odkaz, na který lze kliknout.

3.  Vyhledejte skupinu uživatelů, se kterou chcete sdílet své oblíbené, a klikněte na znaménko **+**.

4.  Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit.

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádné**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro **Veřejný přístup**.

5.  Klikněte na **Sdílet**.

### Přihlaste se k odběru oblíbené položky { #subscribe-to-a-favorite }

Když jste přihlášeni k odběru oblíbené položky, dostáváte interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci nebo vytvoří / aktualizuje komentář k interpretaci této oblíbené položky.

1.  Otevřete oblíbenou položku.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Kliknutím na ikonu zvonku vpravo nahoře se přihlásíte k odběru této oblíbené položky.

### Vytvořte odkaz na oblíbenou položku { #create-a-link-to-a-favorite }

1.  Klikněte na **Oblíbené** \> **Získat odkaz**.

2.  Vyberte jednu z následujících možností:

    -   **Otevřít v této aplikaci**: Získáte URL oblíbené položky, kterou můžete sdílet s ostatními uživateli prostřednictvím e-mailu nebo chatu.

    -   **Otevřít ve webovém rozhraní API**: Získáte adresu URL prostředku API. Ve výchozím nastavení se jedná o zdroj HTML, ale můžete změnit příponu souboru na „.json“ nebo „.csv“.

### Odstranit oblíbenou položku { #delete-a-favorite }

1.  Klikněte na **Oblíbené** \> **Odstranit**.

2.  Klikněte **OK**.

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Klikněte na interpretaci. Váš graf zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

## Stáhněte si data z kontingenční tabulky { #pivot_download_data }

### Stáhněte si datový formát rozložení tabulky { #download-table-layout-data-format }

Postup stažení dat v aktuální kontingenční tabulce:

1.  Klikněte na **Stáhnout**.

2.  V části **Rozvržení tabulky** klikněte na formát, který chcete stáhnout: Microsoft Excel, CSV nebo HTML.

    Tabulka dat bude mít jeden sloupec na dimenzi a bude obsahovat názvy položek dimenze.

    > **Tip**
    >
    > When you download a pivot table with organisation units as rows and you've selected **Show hierarchy** in **Table options**, each organisation unit level is rendered as a separate column. This is useful for example when you create Excel pivot tables on a local computer.

> **Tip**
>
> Kontingenční tabulku můžete vytvořit v aplikaci Microsoft Excel ze staženého souboru aplikace Excel.

### Stáhněte si zdrojový formát  plain data { #download-plain-data-source-format }

Můžete si stáhnout data v aktuální kontingenční tabulce v JSON, XML, Excel a CSV jako prosté datové formáty s různými identifikačními schématy (ID, kód a název). Datový dokument používá identifikátory položek dimenze a otevře se v novém okně prohlížeče, aby se v adresním řádku zobrazila adresa URL požadavku na webové rozhraní API. To je užitečné pro vývojáře aplikací a dalších klientských modulů založených na webovém rozhraní DHIS2 nebo pro ty, kteří vyžadují zdroj dat plánu, například pro import do statistických balíčků.

Postup stažení formátů prostého zdroje dat:

1.  Klikněte na **Stáhnout**.

2.  V části **Zdroj prostých dat** klikněte na formát, který chcete stáhnout.

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 18%" />
    <col style="width: 33%" />
    <col style="width: 47%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Action</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>JSON</p></td>
    <td><p>Click <strong>JSON</strong></p></td>
    <td><p>Downloads JSON format based on ID property.</p>
    <p>You can also download JSON format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>XML</p></td>
    <td><p>Click <strong>XML</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download XML format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Microsoft Excel</p></td>
    <td><p>Click <strong>Microsoft Excel</strong></p></td>
    <td><p>Downloads XML format based on ID property.</p>
    <p>You can also download Microsoft Excel format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="even">
    <td><p>CSV</p></td>
    <td>Click <strong>CSV</strong></td>
    <td><p>Downloads CSV format based on ID property.</p>
    <p>You can also download CSV format based on <strong>Code</strong> or <strong>Name</strong> property.</p></td>
    </tr>
    <tr class="odd">
    <td><p>JRXML</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>JRXML</strong></p></td>
    <td><p>Produces a template of a Jasper Report which can be further customized based on your exact needs and used as the basis for a standard report in DHIS2.</p></td>
    </tr>
    <tr class="even">
    <td><p>Raw data SQL</p></td>
    <td><p>Put the cursor on <strong>Advanced</strong> and click <strong>Raw data SQL</strong></p></td>
    <td><p>Provides the actual SQL statement used to generate the pivot table. You can use it as a data source in a Jasper report, or as the basis for an SQL view.</p></td>
    </tr>
    </tbody>
    </table>

### Stáhněte si formát CSV bez vykreslování dat ve webovém prohlížeči { #download-a-csv-format-without-rendering-data-in-the-web-browser }

Data si můžete stáhnout přímo ve formátu CSV, aniž byste je museli vykreslovat ve webovém prohlížeči. To pomáhá snížit veškerá omezení v nastavení systému, která byla nastavena s ohledem na maximální počet analytických záznamů. To vám umožní stáhnout mnohem větší dávky dat, které můžete použít pro pozdější offline analýzu.

Postup stažení dat ve formátu CSV bez předchozího vykreslení dat ve webovém prohlížeči:

1.  Klikněte na šipku vedle **Aktualizovat**.

    ![](resources/images/pivot_table/data_dump.png)

2.  Kliknutím na **CSV** stáhnete formát založený na ID property.

    Soubor se stáhne do vašeho počítače.

    > **Tip**
    >
    > You can also download CSV format based on **Code** or **Name** property.

## Vložit kontingenční tabulku na externí webovou stránku { #pivot_embed }

Některé zdroje související s analýzou v DHIS2, jako jsou kontingenční tabulky, grafy a mapy, lze vložit na libovolnou webovou stránku pomocí zásuvného modulu. Více informací o zásuvných modulech najdete v kapitole Web API v _DHIS2 Developer Manual_.

Chcete-li vygenerovat fragment HTML, který můžete použít k zobrazení kontingenční tabulky na externí webové stránce, postupujte takto:

1.  Klikněte na **Vložit**.

2.  Kliknutím na **Vybrat** zvýrazněte fragment HTML.

## Vizualizujte data kontingenční tabulky jako graf nebo mapu { #pivot_integration }

Když jste vytvořili kontingenční tabulku, můžete přepínat mezi vizualizací kontingenční tabulky, grafu a mapy vašich dat.

### Otevřít kontingenční tabulku jako graf { #open-a-pivot-table-as-a-chart }

1.  Klikněte na **Graf** \> **Otevřít tuto tabulku jako graf**.

    Vaše aktuální kontingenční tabulka se otevře jako graf.

![](resources/images/pivot_table/pivot_integration.png)

### Otevřete výběr kontingenční tabulky jako graf { #open-a-pivot-table-selection-as-a-chart }

Pokud chcete vizualizovat malou část své kontingenční tabulky jako graf, můžete místo otevření celé tabulky kliknout přímo na hodnotu v tabulce.

1.  V kontingenční tabulce klikněte na hodnotu.

        ![](resources/images/pivot_table/pivot_integration_table.png)

2.  Chcete-li ověřit výběr, podržte kurzor nad **Otevřít výběr jako graf**. Zvýrazněná záhlaví dimenzí v tabulce označují, jaká data budou zobrazena jako graf.

3.  Klikněte na **Otevřít výběr jako graf**.

### Otevřete kontingenční tabulku jako mapu { #open-a-pivot-table-as-a-map }

1.  Klikněte na **Graf** \> **Otevřít tuto tabulku jako mapu**

    Vaše aktuální kontingenční tabulka se otevře jako mapa.

### Otevřete výběr kontingenční tabulky jako mapu { #open-a-pivot-table-selection-as-a-map }

1.  V kontingenční tabulce klikněte na hodnotu.

    Zobrazí se nabídka.

2.  Klikněte na **Otevřít výběr jako mapu**.

    Váš výběr se otevře jako mapa.

# Použití aplikace Hlášení o události { #event_reports_app }

## O aplikaci Hlášení o události { #event_reports_about }

![](resources/images/event_report/event_report.png)

S aplikací **Zpráva o události** můžete analyzovat události ve dvou typech přehledů:

-   Agregované zprávy o událostech: Analýza stylu kontingenční tabulky s agregovaným počtem událostí

    Výběrem **Agregované hodnoty** z nabídky vlevo nahoře můžete pomocí aplikace **Zprávy událostí** vytvořit kontingenční tabulky s agregovaným počtem událostí. Zpráva o události je vždy založena na programu. Můžete provést analýzu na základě řady dimenzí. Každá dimenze může mít odpovídající filtr. Rozměry lze vybrat z nabídky vlevo. Podobně jako v aplikaci kontingenčních tabulek mohou být agregované zprávy o událostech omezeny množstvím paměti RAM přístupné prohlížečem. Pokud vámi požadovaná tabulka přesahuje nastavenou velikost, obdržíte varovnou výzvu s dotazem, zda chcete pokračovat.

-   Jednotlivé zprávy o událostech: Seznamy událostí

    Výběrem **Události** z nabídky vlevo nahoře můžete pomocí aplikace **Zprávy o událostech** provádět vyhledávání nebo dotazy na události na základě flexibilní sady kritérií. Zpráva se zobrazí jako tabulka s jedním řádkem na událost. Každá dimenze může být použita jako sloupec v tabulce nebo jako filtr. Každá dimenze může mít kritéria (filtr). Datové prvky sady možností typu umožňují kritéria „in“, kde lze vybrat více možností. Číselné hodnoty lze porovnat s hodnotami filtru pomocí operátorů větší než, rovný nebo menší než.

## Vytvořte zprávu o události { #event_reports_create }

1.  Otevřete aplikaci **Hlášení událostí**.

2.  Vyberte **Agregované hodnoty** nebo **Události**.

3.  V nabídce vlevo vyberte metadata, která chcete analyzovat.

4.  Klikněte na **Rozložení** a uspořádejte dimenze.

    Pokud chcete, můžete ponechat výchozí výběr.

5.  Klikněte na **Aktualizovat**.

## Vyberte položky dimenze { #event_reports_select_dimensions }

Zpráva o události je vždy založena na programu a můžete provádět analýzu na základě řady dimenzí. U programů s kombinacemi kategorií můžete jako dimenze pro tabulky a grafy použít kategorie programů a skupiny skupin voleb možností. Každá položka dimenze může mít odpovídající filtr.

1.  Vyberte datové prvky:

    1.  Klikněte na **Data**.

    2.  Vyberte program a fázi programu.

        Datové prvky spojené s vybraným programem jsou uvedeny v části **Dostupné**. Každý datový prvek funguje jako dimenze.

    3.  Poklepáním na jejich názvy vyberte datové prvky, které potřebujete.

        Datové prvky lze filtrovat podle typu (datové prvky, atributy programu, indikátory programu) a mají předponu, aby byly snadno rozpoznatelné.

        Po výběru datového prvku je viditelný pod **Vybrané datové položky**.

    4.  (Volitelné) Pro každý datový prvek zadejte filtr s operátory, jako je „větší než“, „v“ nebo „rovno“, spolu s hodnotou filtru.

2.  Vyberte období

    1.  Klikněte na **Období**.

    2.  Vyberte jedno nebo několik období.

        Máte tři možnosti období: relativní období, pevná období a datum zahájení / ukončení. Ve stejném grafu můžete kombinovat pevná období a relativní období. Nemůžete kombinovat pevná období a relativní období s daty zahájení a ukončení ve stejném grafu. Překrývající se období jsou filtrována tak, aby se objevila pouze jednou.

        -   Pevná období: V poli **Vyberte typ období** vyberte typ období. Můžete vybrat libovolný počet pevných období z jakéhokoli typu období. Pevná období mohou být například „leden 2014“.

        -   Relativní období: Ve spodní části části **Období** vyberte tolik relativních období, kolik chcete. Názvy jsou relativní k aktuálnímu datu. To znamená, že pokud je aktuální měsíc březen a vyberete **minulý měsíc**, bude do grafu zahrnut i měsíc únor. Relativní období má tu výhodu, že udržuje data v přehledu aktuální podle času.

        -   Datum zahájení / ukončení: V seznamu na kartě **Období** vyberte **Datum zahájení / ukončení**. Tento typ období umožňuje určit flexibilní data pro časové rozpětí ve zprávě.

3.  Vyberte organizační jednotky.

    1.  Klikněte na **Organizační jednotky**

    2.  Klikněte na ikonu ozubeného kolečka.

    3.  Vyberte **režim výběru** a organizační jednotku.

        Existují tři různé režimy výběru:

        <table>
        <caption>Selection modes</caption>
        <colgroup>
        <col style="width: 38%" />
        <col style="width: 61%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Selection mode</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><strong>Select organisation units</strong></p></td>
        <td><p>Lets you select the organisation units you want to appear in the chart from the organization tree.</p>
        <p>Select <strong>User org unit</strong> to disable the organisation unit tree and only select the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-units</strong> to disable the organisation unit tree and only select the sub-units of the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-x2-units</strong> to disable the organisation unit tree and only select organisation units two levels down from the organisation unit that is related to your profile.</p>
        <p>This functionality is useful for administrators to create a meaningful &quot;system&quot; favorite. With this option checked all users find their respective organisation unit when they open the favorite.</p></td>
        </tr>
        <tr class="even">
        <td><p><strong>Select levels</strong></p></td>
        <td><p>Lets you select all organisation units at one or more levels, for example national or district level.</p>
        <p>You can also select the parent organisation unit in the tree, which makes it easy to select for example, all facilities inside one or more districts.</p></td>
        </tr>
        <tr class="odd">
        <td><p><strong>Select groups</strong></p></td>
        <td><p>Lets you select all organisation units inside one or several groups and parent organisation units at the same time, for example hospitals or chiefdoms.</p></td>
        </tr>
        </tbody>
        </table>

4.  Klikněte na **Aktualizovat**.

## Vyberte sérii, kategorii a filtr { #event_reports_select_series_category_filter }

Můžete určit, která datová dimenze se má v kontingenční tabulce zobrazit jako sloupce, řádky a filtry. Každý datový prvek se jeví jako jednotlivé dimenze a lze jej umístit na kteroukoli z os.

> **Poznámka**
>
> Datové prvky typů spojitých hodnot (reálná čísla / desetinná čísla) lze použít pouze jako filtry a budou automaticky umístěny jako filtry v dialogovém okně rozložení. Důvodem je to, že spojité číslo nelze seskupit do rozumných rozsahů a použít na sloupcích a řádcích.

1.  Klikněte na **Rozložení**.

2.  Přetáhněte dimenze do příslušného prostoru.

3.  Klikněte na **Aktualizovat**.

## Změňte zobrazení tabulky { #event_reports_change_display }

Můžete přizpůsobit zobrazení zprávy o události.

1.  Klikněte na **Možnosti**.

2.  Nastavte možnosti podle potřeby. Dostupné možnosti se mezi agregovanými přehledy událostí a jednotlivými přehledy událostí liší.

    <table style="width:100%;">
    <caption>Event reports options</caption>
    <colgroup>
    <col style="width: 22%" />
    <col style="width: 22%" />
    <col style="width: 33%" />
    <col style="width: 22%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    <th><p>Available for report type</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show column totals</strong></p></td>
    <td><p>Displays totals at the end of each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show column sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each column in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show row totals</strong></p></td>
    <td><p>Displays totals at the end of each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Show row sub-totals</strong></p></td>
    <td><p>Displays sub-totals for each row in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Show dimension labels</strong></p></td>
    <td>Displays labels for dimensions.</td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty rows</strong></p></td>
    <td><p>Hides empty rows in the pivot table.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Hide n/a data</strong></p></td>
    <td><p>Hides data tagged as N/A from the chart.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful when you want for example to exclude partial events in indicator calculations.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Limit</strong></p></td>
    <td><p>Sets a limit of the maximum number of rows that you can display in the table, combined with a setting for showing top or bottom values.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Output type</strong></p></td>
    <td><p>Defines the output type. The output types are <strong>Event</strong>, <strong>Enrollment</strong> and<strong>Tracked entity instance</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Program status</strong></p></td>
    <td><p>Filters data based on the program status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong> or <strong>Cancelled</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Event status</strong></p></td>
    <td><p>Filters data based on the event status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong>, <strong>Scheduled</strong>, <strong>Overdue</strong> or <strong>Skipped</strong>.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="odd">
    <td><strong>Organisation units</strong></td>
    <td><p><strong>Show hierarchy</strong></p></td>
    <td><p>Includes the names of all parents of each organisation unit in labels.</p></td>
    <td><p>Aggregated event report</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Style</strong></p></td>
    <td><p><strong>Display density</strong></p></td>
    <td><p>Controls the size of the cells in the table. You can set it to <strong>Comfortable</strong>, <strong>Normal</strong> or <strong>Compact</strong>.</p>
    <p><strong>Compact</strong> is useful when you want to fit large tables into the browser screen.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Font size</strong></p></td>
    <td><p>Controls the size of the table text font. You can set it to <strong>Large</strong>, <strong>Normal</strong> or <strong>Small</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Digit group separator</strong></p></td>
    <td><p>Controls which character to separate groups of digits or &quot;thousands&quot;. You can set it to <strong>Comma</strong>, <strong>Space</strong> or <strong>None</strong>.</p></td>
    <td><p>Aggregated event report</p>
    <p>Individual event report</p></td>
    </tr>
    </tbody>
    </table>

3.  Klikněte na **Aktualizovat**.

## Stáhněte si zdroj dat grafu { #event_reports_download_report }

Zdroj dat za zprávou o události si můžete stáhnout ve formátech HTML, JSON, XML, Microsoft Excel nebo CSV.

1.  Klikněte na **Stáhnout**.

2.  V části **Zdroj prostých dat** klikněte na formát, který chcete stáhnout.

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 27%" />
    <col style="width: 72%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>HTML</p></td>
    <td><p>Creates HTML table based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>JSON</p></td>
    <td><p>Downloads data values in JSON format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>XML</p></td>
    <td><p>Downloads data values in XML format based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>Microsoft Excel</p></td>
    <td><p>Downloads data values in Microsoft Excel format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>CSV</p></td>
    <td><p>Downloads data values in CSV format based on selected meta data</p></td>
    </tr>
    </tbody>
    </table>

## Spravujte oblíbené položky { #manage-favorites }

Uložení grafů nebo kontingenčních tabulek jako oblíbených usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli jako interpretaci nebo je zobrazit na ovládacím panelu.

Podrobnosti a interpretace vašich oblíbených položek zobrazíte v aplikacích **Kontingenční tabulka**, **Zobrazení dat**, **Zobrazení událostí**, **Zprávy o událostech**. Pomocí nabídky **Oblíbené** můžete spravovat své oblíbené položky.

### Otevřete oblíbenou položku { #open-a-favorite }

1.  Klikněte na **Oblíbené** \> **Otevřít**.

2.  Zadejte název oblíbené položky do vyhledávacího pole nebo kliknutím na **Předchozí** a **Další** zobrazte oblíbené položky.

3.  Klikněte na název oblíbené položky, kterou chcete otevřít.

### Uložit oblíbené { #save-a-favorite }

1.  Klikněte na **Oblíbené** \> **Uložit jako**.

2.  Zadejte **Název** a **Popis** pro vaši oblíbenou položku. Pole popisu podporuje formát RTF, další podrobnosti najdete v části interpretace.

3.  Klikněte **Uložit**.

### Přejmenujte oblíbenou položku { #rename-a-favorite }

1.  Klikněte na **Oblíbené** \> **Přejmenovat**.

2.  Zadejte nový název své oblíbené položky.

3.  Klikněte na **Aktualizovat**.

### Napište interpretaci pro oblíbené { #write-an-interpretation-for-a-favorite }

Interpretace je odkaz na zdroj s popisem dat v daném období. Tyto informace jsou viditelné v aplikaci **Ovládací panel**. Chcete-li vytvořit interpretaci, musíte nejprve vytvořit oblíbenou položku. Pokud jste sdíleli své oblíbené položky s jinými lidmi, interpretace, kterou píšete, je viditelná pro tyto lidi.

1.  Klikněte na **Oblíbené** \> **Napsat výklad**.

2.  Do textového pole zadejte komentář, otázku nebo výklad. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s výkladem nebo komentářem. Výklad můžete vidět v aplikaci **Dashboard**.

    Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown \* a \_ pro **tučné** a _italic_. K dispozici jsou také klávesové zkratky: Ctrl / Cmd + B a Ctrl / Cmd + I. Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: :) :-) :( :-(: +1 :-1. URL jsou automaticky detekovány a převedeny na odkaz, na který lze kliknout.

3.  Vyhledejte skupinu uživatelů, se kterou chcete sdílet své oblíbené, a klikněte na znaménko **+**.

4.  Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit.

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádné**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro **Veřejný přístup**.

5.  Klikněte na **Sdílet**.

### Přihlaste se k odběru oblíbené položky { #subscribe-to-a-favorite }

Když jste přihlášeni k odběru oblíbené položky, dostáváte interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci nebo vytvoří / aktualizuje komentář k interpretaci této oblíbené položky.

1.  Otevřete oblíbenou položku.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Kliknutím na ikonu zvonku vpravo nahoře se přihlásíte k odběru této oblíbené položky.

### Vytvořte odkaz na oblíbenou položku { #create-a-link-to-a-favorite }

1.  Klikněte na **Oblíbené** \> **Získat odkaz**.

2.  Vyberte jednu z následujících možností:

    -   **Otevřít v této aplikaci**: Získáte URL oblíbené položky, kterou můžete sdílet s ostatními uživateli prostřednictvím e-mailu nebo chatu.

    -   **Otevřít ve webovém rozhraní API**: Získáte adresu URL prostředku API. Ve výchozím nastavení se jedná o zdroj HTML, ale můžete změnit příponu souboru na „.json“ nebo „.csv“.

### Odstranit oblíbenou položku { #delete-a-favorite }

1.  Klikněte na **Oblíbené** \> **Odstranit**.

2.  Klikněte **OK**.

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Klikněte na interpretaci. Váš graf zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

## Vizualizujte zprávu o události jako graf { #event_reports_open_as_chart }

Když jste vytvořili zprávu o události, můžete ji otevřít jako graf:

Klikněte na **Graf** \> **Otevřít tento graf jako tabulku**.

# Použití aplikace Vizualizér událostí { #event_visualizer_app }

## O aplikaci Vizualizér událostí { #about-the-event-visualizer-app }

![](resources/images/event_visualizer/event_visualizer.png)

S aplikací **Event Visualizer** můžete vytvářet grafy založené na datech událostí.

## Vytvořte graf { #create-a-chart }

1.  \<Otevřete aplikaci **Vizualizér událostí** a vyberte typ grafu.

2.  V nabídce vlevo vyberte metadata, která chcete analyzovat.

3.  Klikněte na **Rozložení** a uspořádejte dimenze.

    Pokud chcete, můžete ponechat výchozí výběr.

4.  Klikněte na **Aktualizovat**.

## Vyberte typ grafu { #select-a-chart-type }

**Vizualizér událostí** aplikace má osm různých typů grafů, každý s různými charakteristikami. Výběr typu grafu:

1.  V **Typ grafu** klikněte na požadovaný typ grafu.

    <table>
    <caption>Chart types</caption>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 66%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Chart type</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Column chart</p></td>
    <td><p>Displays information as vertical rectangular columns with lengths proportional to the values they represent.</p>
    <p>Useful when you want to, for example, compare performance of different districts.</p></td>
    </tr>
    <tr class="even">
    <td><p>Stacked column chart</p></td>
    <td><p>Displays information as vertical rectangular columns, where bars representing multiple categories are stacked on top of each other.</p>
    <p>Useful when you want to, for example, display trends or sums of related data elements.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Bar chart</p></td>
    <td><p>Same as column chart, only with horizontal bars.</p></td>
    </tr>
    <tr class="even">
    <td><p>Stacked bar chart</p></td>
    <td><p>Same as stacked column chart, only with horizontal bars.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Line chart</p></td>
    <td><p>Displays information as a series of points connected by straight lines. Also referred to as time series.</p>
    <p>Useful when you want to, for example, visualize trends in indicator data over multiple time periods.</p></td>
    </tr>
    <tr class="even">
    <td><p>Area chart</p></td>
    <td><p>Is based on line chart, with the space between the axis and the line filled with colors and the lines stacked on top of each other.</p>
    <p>Useful when you want to compare the trends of related indicators.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Pie chart</p></td>
    <td><p>Circular chart divided into sectors (or slices).</p>
    <p>Useful when you want to, for example, visualize the proportion of data for individual data elements compared to the total sum of all data elements in the chart.</p></td>
    </tr>
    <tr class="even">
    <td><p>Radar chart</p></td>
    <td><p>Displays data on axes starting from the same point. Also known as spider chart.</p></td>
    </tr>
    </tbody>
    </table>

2.  Klikněte na **Aktualizovat**.

## Vyberte položky dimenze { #event_visualizer_select_dimensions }

Graf událostí je vždy založen na programu a můžete provádět analýzu na základě řady dimenzí. U programů s kombinacemi kategorií můžete jako dimenze pro tabulky a grafy použít kategorie programů a skupiny skupin voleb možností. Každá položka dimenze může mít odpovídající filtr. Položky dimenze vyberete z nabídky vlevo.

1.  Vyberte datové prvky:

    1.  Klikněte na **Data**.

    2.  Vyberte program a fázi programu.

        Datové prvky spojené s vybraným programem jsou uvedeny v části **Dostupné**. Každý datový prvek funguje jako dimenze.

    3.  Poklepáním na jejich názvy vyberte datové prvky, které potřebujete.

        Datové prvky lze filtrovat podle typu (datové prvky, atributy programu, indikátory programu) a mají předponu, aby byly snadno rozpoznatelné.

        Po výběru datového prvku je viditelný pod **Vybrané datové položky**.

    4.  (Volitelné) Pro každý datový prvek zadejte filtr s operátory, jako je „větší než“, „v“ nebo „rovno“, spolu s hodnotou filtru.

2.  Vyberte období

    1.  Klikněte na **Období**.

    2.  Vyberte jedno nebo několik období.

        Máte tři možnosti období: relativní období, pevná období a datum zahájení / ukončení. Ve stejném grafu můžete kombinovat pevná období a relativní období. Nemůžete kombinovat pevná období a relativní období s daty zahájení a ukončení ve stejném grafu. Překrývající se období jsou filtrována tak, aby se objevila pouze jednou.

        -   Pevná období: V poli **Vyberte typ období** vyberte typ období. Můžete vybrat libovolný počet pevných období z jakéhokoli typu období. Pevná období mohou být například „leden 2014“.

        -   Relativní období: Ve spodní části části **Období** vyberte tolik relativních období, kolik chcete. Názvy jsou relativní k aktuálnímu datu. To znamená, že pokud je aktuální měsíc březen a vyberete **minulý měsíc**, bude do grafu zahrnut i měsíc únor. Relativní období má tu výhodu, že udržuje data v přehledu aktuální podle času.

        -   Datum zahájení / ukončení: V seznamu na kartě **Období** vyberte **Datum zahájení / ukončení**. Tento typ období umožňuje určit flexibilní data pro časové rozpětí ve zprávě.

3.  Vyberte organizační jednotky.

    1.  Klikněte na **Organizační jednotky**

    2.  Klikněte na ikonu ozubeného kolečka.

    3.  Vyberte **režim výběru** a organizační jednotku.

        Existují tři různé režimy výběru:

        <table>
        <caption>Selection modes</caption>
        <colgroup>
        <col style="width: 38%" />
        <col style="width: 61%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><p>Selection mode</p></th>
        <th><p>Description</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><strong>Select organisation units</strong></p></td>
        <td><p>Lets you select the organisation units you want to appear in the chart from the organization tree.</p>
        <p>Select <strong>User org unit</strong> to disable the organisation unit tree and only select the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-units</strong> to disable the organisation unit tree and only select the sub-units of the organisation unit that is related to your profile.</p>
        <p>Select <strong>User sub-x2-units</strong> to disable the organisation unit tree and only select organisation units two levels down from the organisation unit that is related to your profile.</p>
        <p>This functionality is useful for administrators to create a meaningful &quot;system&quot; favorite. With this option checked all users find their respective organisation unit when they open the favorite.</p></td>
        </tr>
        <tr class="even">
        <td><p><strong>Select levels</strong></p></td>
        <td><p>Lets you select all organisation units at one or more levels, for example national or district level.</p>
        <p>You can also select the parent organisation unit in the tree, which makes it easy to select for example, all facilities inside one or more districts.</p></td>
        </tr>
        <tr class="odd">
        <td><p><strong>Select groups</strong></p></td>
        <td><p>Lets you select all organisation units inside one or several groups and parent organisation units at the same time, for example hospitals or chiefdoms.</p></td>
        </tr>
        </tbody>
        </table>

4.  Klikněte na **Aktualizovat**.

## Vyberte sérii, kategorii a filtr { #select-series-category-and-filter }

Můžete určit, která datová dimenze se má zobrazit jako řada, kategorie a filtr. Každý datový prvek se jeví jako jednotlivé dimenze a lze jej umístit na kteroukoli z os. Panely sérií a kategorií mohou mít současně pouze jeden rozměr.

> **Poznámka**
>
> Datové prvky typů spojitých hodnot (reálná čísla / desetinná čísla) lze použít pouze jako filtry a budou automaticky umístěny jako filtry v dialogovém okně rozložení. Důvodem je to, že spojité číslo nelze seskupit do rozumných rozsahů a použít na sloupcích a řádcích.

1.  Klikněte na **Rozložení**.

2.  Přetáhněte dimenze do příslušného prostoru. V každé sekci může být pouze jedna dimenze.

3.  Klikněte na **Aktualizovat**.

## Změňte zobrazení grafu { #event_visualizer_change_display }

Můžete přizpůsobit zobrazení zprávy o události.

1.  Klikněte na **Možnosti**.

2.  Nastavte možnosti podle potřeby.

    <table>
    <caption>Chart options</caption>
    <colgroup>
    <col style="width: 28%" />
    <col style="width: 28%" />
    <col style="width: 42%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Option</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Data</strong></p></td>
    <td><p><strong>Show values</strong></p></td>
    <td><p>Displays values as numbers on top of each series.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Use 100% stacked values</strong></p></td>
    <td><p>Displays 100 % stacked values in column charts.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Use cumulative values</strong></p></td>
    <td><p>Displays cumulative values in line charts.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide n/a data</strong></p></td>
    <td><p>Hides data tagged as N/A from the chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Include only completed events</strong></p></td>
    <td><p>Includes only completed events in the aggregation process. This is useful when you want for example to exclude partial events in indicator calculations.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide empty categories</strong></p></td>
    <td><p>Hides the category items with no data from the chart.</p>
    <p><strong>None</strong>: doesn't hide any of the empty categories</p>
    <p><strong>Before first</strong>: hides missing values only before the first value</p>
    <p><strong>After last</strong>: hides missing values only after the last value</p>
    <p><strong>Before first and after last</strong>: hides missing values only before the first value and after the last value</p>
    <p><strong>All</strong>: hides all missing values</p>
    <p>This is useful for example when you create column and bar charts.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Trend line</strong></p></td>
    <td><p>Displays the trend line which visualizes how your data evolves over time. For example if performance is improving or deteriorating. Useful when periods are selected as category.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Target line value/title</strong></p></td>
    <td><p>Displays a horizontal line and title (optional) at the given domain value. Useful for example when you want to compare your performance to the current target.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Base line value/title</strong></p></td>
    <td><p>Displays a horizontal line and title (optional) at the given domain value. Useful for example when you want to visualize how your performance has evolved since the beginning of a process.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Sort order</strong></p></td>
    <td><p>Allows you to sort the values on your chart from either low to high or high to low.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Output type</strong></p></td>
    <td><p>Defines the output type. The output types are <strong>Event</strong>, <strong>Enrollment</strong> and<strong>Tracked entity instance</strong>.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Program status</strong></p></td>
    <td><p>Filters data based on the program status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong> or <strong>Cancelled</strong>.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Event status</strong></p></td>
    <td><p>Filters data based on the event status: <strong>All</strong>, <strong>Active</strong>, <strong>Completed</strong>, <strong>Scheduled</strong>, <strong>Overdue</strong> or <strong>Skipped</strong>.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Axes</strong></p></td>
    <td><p><strong>Range axis min/max</strong></p></td>
    <td><p>Defines the maximum and minimum value which will be visible on the range axis.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Range axis tick steps</strong></p></td>
    <td><p>Defines the number of ticks which will be visible on the range axis.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Range axis decimals</strong></p></td>
    <td><p>Defines the number of decimals which will be used for range axis values.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Range axis title</strong></p></td>
    <td><p>Type a title here to display a label next to the range axis (also referred to as the Y axis). Useful when you want to give context information to the chart, for example about the unit of measure.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Domain axis title</strong></p></td>
    <td><p>Type a title here to display a label below the domain axis (also referred to as the X axis). Useful when you want to give context information to the chart, for example about the period type.</p></td>
    </tr>
    <tr class="odd">
    <td><p><strong>General</strong></p></td>
    <td><p><strong>Hide chart legend</strong></p></td>
    <td><p>Hides the legend and leaves more room for the chart itself.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide chart title</strong></p></td>
    <td><p>Hides the title (default or custom) of your chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Chart title</strong></p></td>
    <td><p>Type a title here to display a custom title above the chart. If you don't enter a title, the default title is displayed.</p></td>
    </tr>
    <tr class="even">
    <td></td>
    <td><p><strong>Hide chart subtitle</strong></p></td>
    <td><p>Hides the subtitle of your chart.</p></td>
    </tr>
    <tr class="odd">
    <td></td>
    <td><p><strong>Chart subtitle</strong></p></td>
    <td><p>Type a subtitle here to display a custom subtitle above the chart but below the title. If you don't enter a subtitle, no subtitle is displayed in the chart.</p></td>
    </tr>
    </tbody>
    </table>

3.  Klikněte na **Aktualizovat**.

## Stáhněte si graf jako obrázek nebo PDF { #download-a-chart-as-an-image-or-a-pdf }

Jakmile vytvoříte graf, můžete jej stáhnout do místního počítače jako obrázek nebo soubor PDF.

1.  Klikněte na **Stáhnout**.

2.  V části **Grafika** klikněte na **PNG (.png)** nebo **PDF (.pdf)**.

    Soubor se automaticky stáhne do vašeho počítače. Nyní můžete například vložit obrazový soubor do textového dokumentu jako součást zprávy.

## Stáhněte si zdroj dat grafu { #download-chart-data-source }

Zdroj dat za grafem si můžete stáhnout ve formátech HTML, JSON, XML, Microsoft Excel nebo CSV. Datový dokument používá identifikátory položek dimenze a otevře se v novém okně prohlížeče, aby se v adresním řádku zobrazila adresa URL požadavku na webové rozhraní API. To je užitečné pro vývojáře aplikací a dalších klientských modulů založených na webovém rozhraní DHIS2 nebo pro ty, kteří vyžadují zdroj dat plánu, například pro import do statistických balíčků.

Postup stažení formátů prostého zdroje dat:

1.  Klikněte na **Stáhnout**.

2.  V části **Zdroj prostých dat** klikněte na formát, který chcete stáhnout.

    <table>
    <caption>Available formats</caption>
    <colgroup>
    <col style="width: 27%" />
    <col style="width: 72%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><p>Format</p></th>
    <th><p>Description</p></th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>HTML</p></td>
    <td><p>Creates HTML table based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>JSON</p></td>
    <td><p>Downloads data values in JSON format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>XML</p></td>
    <td><p>Downloads data values in XML format based on selected meta data</p></td>
    </tr>
    <tr class="even">
    <td><p>Microsoft Excel</p></td>
    <td><p>Downloads data values in Microsoft Excel format based on selected meta data</p></td>
    </tr>
    <tr class="odd">
    <td><p>CSV</p></td>
    <td><p>Downloads data values in CSV format based on selected meta data</p></td>
    </tr>
    </tbody>
    </table>

## Spravujte oblíbené položky { #manage-favorites }

Uložení grafů nebo kontingenčních tabulek jako oblíbených usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli jako interpretaci nebo je zobrazit na ovládacím panelu.

Podrobnosti a interpretace vašich oblíbených položek zobrazíte v aplikacích **Kontingenční tabulka**, **Zobrazení dat**, **Zobrazení událostí**, **Zprávy o událostech**. Pomocí nabídky **Oblíbené** můžete spravovat své oblíbené položky.

### Otevřete oblíbenou položku { #open-a-favorite }

1.  Klikněte na **Oblíbené** \> **Otevřít**.

2.  Zadejte název oblíbené položky do vyhledávacího pole nebo kliknutím na **Předchozí** a **Další** zobrazte oblíbené položky.

3.  Klikněte na název oblíbené položky, kterou chcete otevřít.

### Uložit oblíbené { #save-a-favorite }

1.  Klikněte na **Oblíbené** \> **Uložit jako**.

2.  Zadejte **Název** a **Popis** pro vaši oblíbenou položku. Pole popisu podporuje formát RTF, další podrobnosti najdete v části interpretace.

3.  Klikněte **Uložit**.

### Přejmenujte oblíbenou položku { #rename-a-favorite }

1.  Klikněte na **Oblíbené** \> **Přejmenovat**.

2.  Zadejte nový název své oblíbené položky.

3.  Klikněte na **Aktualizovat**.

### Napište interpretaci pro oblíbené { #write-an-interpretation-for-a-favorite }

Interpretace je odkaz na zdroj s popisem dat v daném období. Tyto informace jsou viditelné v aplikaci **Ovládací panel**. Chcete-li vytvořit interpretaci, musíte nejprve vytvořit oblíbenou položku. Pokud jste sdíleli své oblíbené položky s jinými lidmi, interpretace, kterou píšete, je viditelná pro tyto lidi.

1.  Klikněte na **Oblíbené** \> **Napsat výklad**.

2.  Do textového pole zadejte komentář, otázku nebo výklad. Můžete také zmínit další uživatele pomocí „@username“. Začněte zadáním znaku „@“ plus první písmena uživatelského jména nebo skutečného jména a na pruhu se zmínkou se zobrazí dostupní uživatelé. Uvedení uživatelé obdrží interní zprávu DHIS2 s výkladem nebo komentářem. Výklad můžete vidět v aplikaci **Dashboard**.

    Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown \* a \_ pro **tučné** a _italic_. K dispozici jsou také klávesové zkratky: Ctrl / Cmd + B a Ctrl / Cmd + I. Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: :) :-) :( :-(: +1 :-1. URL jsou automaticky detekovány a převedeny na odkaz, na který lze kliknout.

3.  Vyhledejte skupinu uživatelů, se kterou chcete sdílet své oblíbené, a klikněte na znaménko **+**.

4.  Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit.

    -   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý.

    -   **Může pouze zobrazit**: Objekt může zobrazit každý.

    -   **Žádné**: Veřejnost nebude mít přístup k objektu. Toto nastavení je použitelné pouze pro **Veřejný přístup**.

5.  Klikněte na **Sdílet**.

### Přihlaste se k odběru oblíbené položky { #subscribe-to-a-favorite }

Když jste přihlášeni k odběru oblíbené položky, dostáváte interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci nebo vytvoří / aktualizuje komentář k interpretaci této oblíbené položky.

1.  Otevřete oblíbenou položku.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Kliknutím na ikonu zvonku vpravo nahoře se přihlásíte k odběru této oblíbené položky.

### Vytvořte odkaz na oblíbenou položku { #create-a-link-to-a-favorite }

1.  Klikněte na **Oblíbené** \> **Získat odkaz**.

2.  Vyberte jednu z následujících možností:

    -   **Otevřít v této aplikaci**: Získáte URL oblíbené položky, kterou můžete sdílet s ostatními uživateli prostřednictvím e-mailu nebo chatu.

    -   **Otevřít ve webovém rozhraní API**: Získáte adresu URL prostředku API. Ve výchozím nastavení se jedná o zdroj HTML, ale můžete změnit příponu souboru na „.json“ nebo „.csv“.

### Odstranit oblíbenou položku { #delete-a-favorite }

1.  Klikněte na **Oblíbené** \> **Odstranit**.

2.  Klikněte **OK**.

### Zobrazit interpretace založené na relativních obdobích { #view-interpretations-based-on-relative-periods }

Zobrazení interpretací pro relativní období, například před rokem:

1.  Otevřete oblíbené s interpretacemi.

2.  Klikněte na **\>\>\>** v pravém horním rohu pracovního prostoru.

3.  Klikněte na interpretaci. Váš graf zobrazuje data a datum podle toho, kdy byla interpretace vytvořena. Chcete-li zobrazit další interpretace, klikněte na ně.

## Vizualizujte graf jako kontingenční tabulku { #visualize-a-chart-as-a-pivot-table }

Když jste vytvořili graf, můžete jej otevřít jako kontingenční tabulku:

Klikněte na **Graf** \> **Otevřít tento graf jako tabulku**.

# Funkce hlášení v aplikaci pro přehledy { #using_the_reports_app }

Aplikace zprávy umožňuje konzervované standardní zprávy, zprávy o souborech dat, zprávy o distribuci prostředků a organizačních jednotek.

## Použití standardních zpráv { #standard_reports_in_the_beta_reports_app }

Dostupné přehledy zpřístupníte v části Aplikace-\>Přehledy. V nabídce sestavy na levé liště klikněte na Standardní sestava. V hlavním okně se zobrazí seznam všech předdefinovaných zpráv.

![](resources/images/dhis2UserManual/react_reports_app_standard_reports.png)

Spustíte / zobrazíte přehled kliknutím na ikonu se třemi tečkami přehledu a následným výběrem možnosti „Vytvořit“ z kontextové nabídky. Pokud existují nějaké předdefinované parametry, zobrazí se okno s parametry sestavy, kde musíte vyplnit hodnoty potřebné pro orgunit a / nebo vykazovací měsíc, v závislosti na tom, co bylo definováno v podkladových tabulkách(ce) sestavy. Až budete připraveni, klikněte na „Generovat zprávu“. Zpráva se buď zobrazí přímo ve vašem prohlížeči, nebo bude k dispozici jako soubor PDF ke stažení, v závislosti na nastavení vašeho prohlížeče pro práci se soubory PDF. Soubor můžete uložit a uchovat jej lokálně v počítači pro pozdější použití.

## Použití zpráv datových sad { #dataset_reports_in_the_beta_reports_app }

Zprávy o datových sadách jsou zobrazení obrazovky pro zadávání dat, která jsou vhodná pro tisk, vyplněná buď nezpracovanými nebo agregovanými daty.

K hlášením sady dat máte přístup z Aplikace-\>Zprávy.

Zobrazí se okno Kritéria, kde vyplníte podrobnosti svého přehledu:

**Datová sada:** Datová sada, kterou chcete zobrazit.

**Období zprávy:** Skutečné období, za které chcete data používat. To lze agregovat i jako nezpracovaná období. To znamená, že můžete požádat o čtvrtletní nebo výroční zprávu, i když se soubor dat shromažďuje měsíčně. Typ období datové sady (frekvence shromažďování) je definován v údržbě datové sady. Nejprve vyberte typ období (Měsíční, Čtvrtletní, Roční atd.) v rozevíracím seznamu vedle tlačítek Předchozí a Další a pak vyberte jedno z dostupných období z rozevíracího seznamu níže. Pomocí tlačítek Předchozí a Další skočíte o rok zpět nebo vpřed.

**Použít data pouze pro vybranou jednotku:** Tuto možnost použijte, pokud chcete přehled pro organizační jednotku, která má podřízené, ale chcete pouze data shromážděná přímo pro tuto jednotku a ne data shromážděná jejími podřízenými. Pokud chcete typickou agregovanou zprávu pro organizační jednotku, nechcete zaškrtnout tuto možnost.

**Hlášení Organizační jednotky:** Zde vyberete organizační jednotku, pro kterou chcete hlášení zprávy. To může být na jakékoli úrovni v hierarchii, protože data budou agregována až na tuto úroveň automaticky (pokud nezaškrtnete výše uvedenou možnost).

Po dokončení vyplnění kritérií přehledu kliknete na „Vytvořit“. Zpráva se zobrazí jako HTML ve formátu vhodném pro tisk. Chcete-li sestavu vytisknout nebo uložit (jako HTML), použijte funkci tisku a uložení jako v prohlížeči. Sestavu datové sady můžete také exportovat ve formátech Excel a PDF.

## Použití přehledu četnosti hlášení { #reporting_rate_summary_in_the_beta_reports_app }

Souhrn četnosti hlášení získáte z nabídky Aplikace  -\> Zprávy. Souhrny četnosti hlášení ukážou, kolik datových sad (formulářů) bylo odesláno organizační jednotkou za období.

Míra vykazování je výpočet založen na registraci kompletní sady dat. Úplná registrace datové sady znamená, že uživatel označí formulář pro zadávání údajů jako úplný, obvykle kliknutím na tlačítko kompletní na obrazovce pro zadávání údajů, čímž systému sdělí, že považuje formulář za úplný. Jedná se o subjektivní přístup k výpočtu úplnosti.

Souhrn rychlosti vykazování pro každý řádek zobrazí řadu opatření:

-   Aktuální zprávy: Udává počet úplných registrací vstupu dat pro příslušnou sadu dat.

-   Očekávané sestavy: Udává, kolik kompletních registrací datových vstupů se očekává Toto číslo je založeno na počtu organizačních jednotek, kterým byla přiřazena příslušná datová sada (povoleno pro zadávání dat).

-   Míra vykazování: Procento zpráv zaregistrovaných jako úplné na základě očekávaného počtu.

-   Zprávy na čas: Stejné jako aktuální zprávy, pouze zprávy registrované jako úplné do maximálního počtu dnů po skončení vykazovaného období. Tento počet dní po vykazovaném období lze definovat pro každou datovou sadu ve správě datové sady.

-   Rychlost hlášení aktuálního času: Stejné jako procento, jako čitatel se používají pouze zprávy registrované jako úplný aktuální čas.

Chcete-li spustit přehled, postupujte takto:

-   Vyberte organizační jednotku ze stromu.

-   Vyberte datovou sadu.

-   Vyberte typ období a období ze seznamu dostupných období pro daný typ období.

-   Zpráva se poté vykreslí. Změňte kterýkoli z výše uvedených parametrů a znovu klikněte na „Získat přehled“. Zobrazí se odpovídající výsledky.

![](resources/images/dhis2UserManual/react_reports_app_reporting_rate_summary.png)

## Použití zdrojů { #resources_in_the_beta_reports_app }

Nástroj prostředků vám umožňuje nahrát oba soubory z místního počítače na server DHIS a přidat odkazy na jiné zdroje na internetu prostřednictvím adres URL. Pokud je pro váš systém nakonfigurováno cloudové úložiště, budou se  ukládat prostředky tam.

Vytvoření nového zdroje:

1.  Otevřete aplikaci **Zprávy** a klikněte na **Zdroj**.

2.  Klikněte na **Přidat nový**.

3.  Zadejte **Název**.

4.  Vyberte **Typ**: **Nahrát soubor** nebo **Externí URL**.

5.  Klikněte **Uložit**.

## Pomocí sestav distribuce organizačních jednotek { #orgunit_distribution_reports_in_the_beta_reports_app }

K přehledům distribuce Org. jednotek můžete přistupovat z nabídky na levé straně v části Aplikace -\>Zprávy.

Zprávy o distribuci organizace jsou zprávy, které ukazují, jak jsou organizace zastoupeny podle různých vlastností, jako je typ a vlastnictví, a podle geografických oblastí.

Výsledek lze prezentovat v tabulkové zprávě nebo v grafu.

**Spuštění přehledu:**

Chcete-li spustit zprávu, nejprve vyberte organizační jednotku ve stromu organizačních jednotek na levé horní straně. Zpráva bude založena na organizačních jednotkách umístěných pod vybranou organizační jednotkou. Vyberte sadu skupin organizačních jednotek, kterou chcete použít, obvykle se jedná o Typ, Vlastnictví, Venkov / Město, ale může to být libovolná uživatelská skupina skupin organozačních jednotek. Kliknutím na Získat zprávu získáte tabulkovou prezentaci nebo Získat graf pro získání stejného výsledku v grafu. Můžete si také stáhnout tabulkovou sestavu jako Excel nebo CSV.

![](resources/images/dhis2UserManual/react_reports_app_org_unit_dist.png)

# Zprávy { #messages }

## O zprávách a zpětných vazbách { #about-messages-and-feedback-messages }

![](resources/images/messaging/view_inbox.png)

V rámci DHIS2 můžete odesílat zprávy a zpětné vazby uživatelům, skupinám uživatelů a organizačním jednotkám. Když odešlete zprávu se zpětnou vazbou, bude směrována na konkrétní skupinu uživatelů nazvanou skupina příjemců zpětné vazby. Pokud jste členem této skupiny uživatelů, máte přístup k nástrojům pro zpracování zpětné vazby. Během čekání na informace můžete například nastavit stav příchozí zpětné vazby na „Nevyřízeno“.

Kromě zpráv mezi uživateli a zpětné vazby, vám systém v závislosti na vaší konfiguraci pošle také zprávy generované systémem. Tyto zprávy by mohly být spuštěny různými událostmi, včetně selhání úloh systému nebo pozadí a výsledků analýzy ověření. Pro výsledky ověření jsou k dispozici také nástroje pro zpracování zpětné vazby a priorita bude nastavena na důležitost porušeného pravidla ověření.

Chcete-li aplikaci navštívit, klikněte na **ikonu zprávy v pruhu záhlaví** nebo vyhledejte aplikaci **Oznamování** ve vyhledávacím poli.

> **Poznámka**
>
> Zprávy a zprávy se zpětnou vazbou nejsou odesílány na e-mailové adresy uživatelů, zprávy se zobrazují pouze v rámci DHIS2.
>
> S verzí 2.30 jsme představili novou aplikaci pro zasílání zpráv, která nabízí bohatší možnosti zasílání zpráv. konkrétně:
>
> - Přepněte mezi zobrazením seznamu a kompaktním zobrazením kliknutím na ikonu v pravém horním rohu.
>
> - Zobrazení seznamu je zjednodušené a poskytuje dobrý přehled o všech zprávách a je zvláště vhodné pro zpětnou vazbu a zprávy o ověření.
> - Kompaktní zobrazení je moderní způsob zobrazení zpráv, kde má uživatel více informací v jednom zobrazení, takže prohlížení a odpovídání na několik zpráv je jednodušší.
>
> První snímek obrazovky v této části zobrazuje seznam, zatímco snímek obrazovky v části **Přečíst zprávu** zobrazuje kompaktní zobrazení.
>
> - Je přidáno nové vyhledávací pole, které uživateli umožňuje vyhledávat zprávy. Vyhledávání filtruje zprávy podle různých atributů zpráv; předmět, text a odesílatelé. To znamená, že můžete zúžit seznam konverzací zpráv zadáním vyhledávání.
>
> - Je přidána funkce automatického obnovení, takže aplikace načítá nové zprávy v nastaveném intervalu, každých 5 minut. Tato funkce je ve výchozím nastavení zakázána.
>
> - Ke každé konverzaci zpráv můžete přidat účastníky do konverzace. To je velmi užitečné, pokud chcete vložit informace o konkrétní konverzaci nebo pokud by někdo měl také vidět informace. Není možné odstranit účastníky z konverzace.

## Vytvořte zprávu { #create-a-message }

![](resources/images/messaging/create_private_message.png)

1.  Klikněte na **Vytvořit**.

2.  Definujte, komu chcete zprávu přijmout. Můžete odeslat zprávu organizačním jednotkám, uživatelům a skupinám uživatelů.

    -   V poli **Komu** můžete vyhledat organizační jednotky, uživatele a skupiny uživatelů a vybrat požadované příjemce.

3.  Zadejte předmět a zprávu.

4.  Klikněte na **Odeslat**

## Přečtěte si zprávu { #read-a-message }

![](resources/images/messaging/read_message.png)

1.  Vlevo vyberte vhodný typ zprávy.

2.  Klikněte na zprávu.

    Pokud je zpráva součástí konverzace, uvidíte všechny zprávy v této konverzaci.

## Vytvořte zpětnou vazbu { #create-a-feedback-message }

1.  Postupujte podle pokynů pro vytváření zprávy, místo zadávání příjemců vyberte pouze **Zpětná vazba**.

2.  Zpráva bude vytvořena jako zpětná vazba a zobrazí se ve složce **Tiket** všech zadaných uživatelů.

## Přílohy { #attachments }

S verzí 2.31 jsme představili přílohy ke zprávám. Při vytváření konverzace se zprávou nebo odpovědi na ni máte možnost přidat přílohy. V současné době neexistují žádná omezení týkající se typu nebo velikosti souboru.

## Spravujte zprávy o ověření a zpětné vazbě { #manage-validation-and-feedback-messages }

> **Poznámka**
>
> Zprávy se zpětnou vazbou a přístup k rozšířeným nástrojům pro manipulaci uvidíte pouze v případě, že jste členem skupiny uživatelů, která je nastavena pro zpracování zpráv se zpětnou vazbou.
>
> S novou aplikací spravujete rozšířené nástroje pro lístky a ověřovací zprávy prostřednictvím nabídky ikon, která se zobrazí při prohlížení zprávy nebo kontrole zpráv v seznamu konverzací.

### Všechny zprávy vybrány { #all-messages-selected }

![Všechny zprávy vybrány](resources/images/messaging/view_validation_select_all.png)

### Vybrány všechny zprávy a výběr rozšířené volby { #all-messages-selected-and-extended-choice-picker-selected }

![Vybrány všechny zprávy a vybrán rozšířený výběr](resources/images/messaging/view_validation_select_all_icon_menu.png)

Do složky **Tiket** budete dostávat zprávy zpětné vazby a do složky **Validace** zprávy o ověření. Pro zpětnou vazbu a ověřovací zprávy máte kromě možností zpráv také následující možnosti:

<table style="width:100%;">
<caption> Nástroje pro zpracování zpětné vazby </caption>
<colgroup>
<col width="23%" />
<col width="76%" />
</colgroup>
<thead>
<tr class="header">
<th> Funkce </th>
<th> Popis </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> <strong> priorita </strong> </p> </td>
<td> <p> můžete označit zpětné vazby / ověřovací zprávy s různými prioritami: <strong> Žádné </strong>, <strong> nízké</strong>, <strong> střední </strong> nebo <strong> vysoké</strong>. </p>
<p> Nastavení priority usnadňuje trasování, kterou zpětnou vazbu potřebujete vyřešit jako první, a která zpětná vazba může čekat. </p> </td>
</tr>
<tr class="even">
<td> <p> <strong> stav </strong> </p> </td>
<td> <p> Všechny zpětnovazební / ověřovací zprávy získají stav <strong> Otevřít </strong>, když jsou vytvořeny. </p>
<p> Chcete-li sledovat existující zpětnovazební zprávy, můžete změnit stav na <strong> Nevyřízené </strong>, <strong> Neplatné </strong> nebo <strong>Vyřešené</strong>.</p>
<p> Zprávy zpětné vazby / ověřování můžete filtrovat na základě jejich stavu pomocí dvou rozbalovacích nabídek na vnitřní liště záhlaví. </p> </td>
</tr>
<tr class="odd">
<td> <p> <strong> Přiřazeno k </strong> </p> </td>
<td> <p> Zprávu se zpětnou vazbou můžete přiřadit kterémukoli členovi skupiny uživatelů, který je nastaven pro zpracování zpráv se zpětnou vazbou. </p>
<p> Ověřovací zprávu můžete přiřadit kterémukoli uživateli v systému. </p>
<p> <strong> - </strong> znamená, že jste ke zpětné vazbě nepřiřadili uživatele. </p> </td>
</tr>
<tr class="even">
<td> <p> <strong> interní odpověď </strong> </p> </td>
<td> <p> Když pracujete v týmu pro zpracování zpětné vazby, možná budete chtít diskutovat o zpětné vazbě před odesláním odpovědi odesílateli. Tuto diskusi můžete udržovat ve stejné konverzaci zpráv jako samotná zpětná vazba. </p>
<p> Chcete-li odeslat odpověď, která ve skupině uživatelů pro zpracování zpětné vazby, klikněte na <strong>VNITŘNÍ ODPOVĚĎ.</strong> </p> </td>
</tr>
</tbody>
</table>

## Nakonfigurujte funkci zpětné vazby { #configure-feedback-message-function }

Chcete-li nakonfigurovat funkci zpětné vazby, musíte:

1.  Vytvořte skupinu uživatelů (například „Příjemci zpětné vazby“), která obsahuje všechny uživatele, kteří by měli dostávat zpětné vazby.

2.  Otevřete aplikaci **Nastavení systému** a klikněte na **Obecné** \> **Příjemci zpětné vazby** a vyberte skupinu uživatelů, kterou jste vytvořili v předchozím kroku.

# Nastavte předvolby uživatelského účtu { #user_account_preferences }

V **Uživatelské nastavení** můžete změnit jazyk zobrazení DHIS2 a jazyk databáze. Jazyk databáze je přeložený obsah metadat, jako jsou datové prvky a indikátory. Můžete také zvolit styl zobrazení a povolit nebo zakázat oznámení SMS a e-mailem. Pokud si přejete, můžete zvolit, aby se v analytických modulech zobrazovalo zkrácené jméno, například „Joe“, a ne celé jméno.

V **Uživatelském profilu** můžete do svého profilu přidat osobní informace, jako je vaše e-mailová adresa, číslo mobilního telefonu, datum narození, profilový obrázek a další. Když odesíláte zprávy, může osoba, která zprávu přijala, vidět tyto podrobnosti profilu. Můžete také zadat názvy účtů pro různé služby přímých zpráv, které systém použije.

V **Nastavení účtu** můžete resetovat heslo a nastavit 2-faktorové ověřování. Nastavení dvoufaktorového ověřování vyžaduje, abyste si do svého mobilního zařízení stáhli aplikaci Google Authenticator.

V části **Zobrazit celý profil** najdete souhrn podrobností svého profilu. Tato část obsahuje několik polí, která sami nemůžete upravovat, například uživatelské role a uživatelské organizační jednotky.

V části **O DHIS2** najdete seznam podrobností o instanci DHIS2.
