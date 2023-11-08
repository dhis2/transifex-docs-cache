---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/deployment-strategies.md"
revision_date: "2021-06-14"
---

# Strategie nasazení { #deployment-strategies }

DHIS2 je aplikace podporující síť a lze k ní přistupovat přes internet, místní intranet a jako lokálně nainstalovaný systém. Alternativy nasazení pro DHIS2 jsou v této kapitole definovány jako i) offline nasazení ii) online nasazení a iii) hybridní nasazení. Význam a rozdíly budou popsány v následujících částech.

## Offline nasazení { #offline-deployment }

Nasazení offline znamená, že je pro koncové uživatele nainstalováno více samostatných instancí offline, obvykle na úrovni okresu. Systém je primárně udržován koncovými uživateli / okresními zdravotníky, kteří zadávají data a generují zprávy ze systému běžícího na jejich lokálním serveru. Systém bude také obvykle udržován národním týmem superuživatelů, kteří pravidelně navštěvují okresní nasazení. Data jsou v hierarchii posouvána nahoru koncovými uživateli, kteří vytvářejí soubory pro výměnu dat, které jsou zasílány elektronicky e-mailem nebo fyzicky poštou nebo osobním cestováním. (Upozorňujeme, že krátké připojení k internetu vyžadované pro odesílání e-mailů nesplňuje podmínky pro definování jako online). Tento styl nasazení má zjevnou výhodu, že funguje, když není k dispozici vhodné připojení k internetu. Na druhé straně jsou s tímto stylem významné výzvy, které jsou popsány v následující části.

- Hardware: Provoz samostatných systémů vyžaduje pokročilý hardware, pokud jde o servery a spolehlivé napájení, které je třeba instalovat, obvykle na úrovni okresů, po celé zemi. To vyžaduje odpovídající financování nákupu a plánu dlouhodobé údržby.

- Softwarová platforma: Místní instalace znamenají významnou potřebu údržby. Ze zkušeností je největší výzvou viry a další malware, které z dlouhodobého hlediska mají tendenci infikovat místní instalace. Hlavním důvodem je, že koncoví uživatelé využívají paměťové karty pro přenos souborů a dokumentů pro výměnu dat mezi soukromými počítači, jinými pracovními stanicemi a systémem, ve kterém je aplikace spuštěna. Udržování antivirového softwaru a aktualizací operačních systémů v offline prostředí je náročné a koncoví uživatelé často přijímají špatné postupy z hlediska bezpečnosti. Upřednostňovaným způsobem, jak tento problém překonat, je spustit dedikovaný server pro aplikaci, kde nejsou povoleny žádné paměťové karty, a používat operační systém založený na Linuxu, který není tak náchylný k virovým infekcím jako MS Windows.

- Softwarová aplikace: Schopnost distribuovat nové funkce a opravy chyb v softwaru pro informace o zdraví uživatelům je nezbytná pro údržbu a zdokonalování systému. Spoléhání se na to, že koncoví uživatelé budou provádět upgrady softwaru, vyžaduje rozsáhlé školení a vysokou úroveň kompetencí na jejich straně, protože upgrade softwarových aplikací může být technicky náročný úkol. Spoléhání se na národní tým superuživatelů při údržbě softwaru znamená hodně cestování.

- Údržba databáze: Předpokladem efektivního systému je, aby všichni uživatelé zadávali data pomocí standardizované sady metadat (datové prvky, formuláře atd.). Stejně jako v předchozím bodě o upgradech softwaru vyžaduje distribuce změn v souboru metadat do mnoha offline instalací kompetence koncového uživatele, pokud jsou aktualizace zasílány elektronicky nebo dobře organizovaný tým superuživatelů. Nedodržení synchronizace souboru metadat bude mít za následek ztrátu schopnosti přesouvat data z okresů a / nebo nekonzistentní národní databáze, protože data zadaná například na úrovni okresu nebudou kompatibilní s daty na národní úrovni.

## Online nasazení { #online-deployment }

Nasazení online znamená, že na serveru připojeném k Internetu je nastavena jedna instance aplikace. Všichni uživatelé (klienti) se připojují k online centrálnímu serveru přes internet pomocí webového prohlížeče. Tento styl nasazení v současné době těží z obrovských investic a rozšíření mobilních sítí v rozvojových zemích. To umožňuje přístup k online serverům i ve venkovských oblastech pomocí mobilních internetových modemů (označovaných také jako _dongles_).

Tento online styl nasazení má ve srovnání s tradičním offline samostatným stylem obrovské pozitivní důsledky pro proces implementace a údržbu aplikace:

- Hardware: Hardwarové požadavky na straně koncového uživatele jsou omezeny na přiměřeně moderní počítač / notebook a připojení k internetu prostřednictvím pevné linky nebo mobilního modemu. Není potřeba žádný speciální server, postačí jakýkoli počítač s připojením k internetu.

- Softwarová platforma: Koncoví uživatelé potřebují k připojení k online serveru pouze webový prohlížeč. Všechny dnes populární operační systémy jsou dodávány s webovým prohlížečem a neexistují žádné zvláštní požadavky na typ nebo verzi. To znamená, že pokud dojde k vážným problémům, jako jsou virové infekce nebo poškození softwaru, můžete se vždy uchýlit k přeformátování a instalaci operačního systému počítače nebo k získání nového počítače / notebooku. Uživatel může pokračovat v zadávání dat tam, kde byl ponechán, a žádná data nebudou ztracena.

- Softwarová aplikace: Styl nasazení centrálního serveru znamená, že aplikaci lze upgradovat a udržovat centralizovaným způsobem. Když jsou vydány nové verze aplikací s novými funkcemi a opravami chyb, lze je nasadit na jediný online server. Všechny změny se poté projeví na straně klienta při příštím připojení koncových uživatelů přes internet. To samozřejmě má obrovský pozitivní dopad na proces zlepšování systému, protože nové funkce mohou být uživatelům distribuovány okamžitě, všichni uživatelé budou přistupovat ke stejné verzi aplikace a chyby a problémy lze třídit a nasazovat za běhu.

- Údržba databáze: Podobně jako v předchozím bodě lze změny metadat provádět na online serveru centralizovaným způsobem a automaticky se rozšíří na všechny klienty při příštím připojení k serveru. Tím se efektivně odstraní obrovské problémy související s udržováním upgradované a standardizované sady metadat související s tradičním offline stylem nasazení. Je to mimořádně výhodné například během počáteční fáze vývoje databáze a během každoročních procesů revize databáze, protože koncoví uživatelé budou mít přístup ke konzistentní a standardizované databázi, i když ke změnám dochází často.

Tento přístup může být problematický v případech, kdy je připojení k internetu nestabilní nebo chybí po dlouhou dobu. DHIS2 však má určité funkce, které vyžadují, aby připojení k internetu bylo k dispozici pouze po část času, aby systém správně fungoval, například nástroj MyDatamart uvedený v samostatné kapitole této příručky.

## Hybridní nasazení { #hybrid-deployment }

Z dosavadní diskuse si člověk uvědomí, že styl nasazení online je příznivý oproti stylu offline, ale vyžaduje slušné připojení k internetu, kde bude použit. Je důležité si všimnout, že uvedené styly mohou existovat společně v běžném nasazení. Je naprosto možné mít online i offline nasazení v jedné zemi. Obecným pravidlem by bylo, že okresy a zařízení by měly do systému přistupovat online přes internet, kde existuje dostatečné připojení k internetu, a offline systémy by měly být nasazeny do okresů, kde tomu tak není.

Přesné definování slušného připojení k internetu je těžké, ale zpravidla by rychlost stahování měla být minimálně 10 kB / s a dostupnost by měla být minimálně 70% času.

V tomto ohledu jsou modemy mobilního internetu, které lze připojit k počítači nebo notebooku a přistupovat k mobilní síti, mimořádně schopným a proveditelným řešením. Pokrytí mobilního internetu po celém světě rychle roste, často poskytuje vynikající konektivitu za nízké ceny a je skvělou alternativou k místním sítím a špatně udržovaným pevným internetovým linkám. Kontakt s národními společnostmi v oblasti mobilních sítí, pokud jde o předplacené předplatné a potenciální výhody velké objednávky, může být užitečné. Při rozhodování, jaký přístup k nasazení zvolit, protože by se mohl lišit a pokrýt různé části země, by mělo být prozkoumáno pokrytí sítě každého provozovatele sítě v příslušné zemi.

## Server hosting { #server-hosting }

Přístup online nasazení nastoluje otázku, kde a jak hostovat server, na kterém bude spuštěna aplikace DHIS2. Obvykle existuje několik možností:

1.  Interní hosting v rámci ministerstva zdravotnictví

2.  Hostování v rámci vládního datového centra

3.  Hostování prostřednictvím externí hostingové společnosti

Hlavním důvodem pro výběr první možnosti je často politická motivace k „fyzickému vlastnictví“ databáze. Mnozí to považují za důležité pro „vlastnictví“ a kontrolu dat. Existuje také přání vybudovat místní kapacitu pro správu serveru související s udržitelností projektu. Často jde o iniciativu dárců, protože je vnímána jako konkrétní a užitečné poslání.

Pokud jde o druhou možnost, na některých místech je vybudováno vládní datové centrum s cílem podporovat a zlepšovat využívání a přístupnost veřejných dat. Dalším důvodem je, že šíření interních serverových prostředí je velmi náročné na zdroje a je efektivnější vytvořit centralizovanou infrastrukturu a kapacitu.

Pokud jde o externí hosting, v poslední době dochází k posunu směrem k outsourcingu provozu a správy počítačových zdrojů u externího poskytovatele, kde jsou tyto zdroje přístupné přes síť, populárně označované jako „cloud computing“ nebo „software jako služba“. K těmto zdrojům se obvykle přistupuje přes internet pomocí webového prohlížeče.

Primárním cílem pro nasazení online serveru je poskytnout dlouhodobě stabilní a vysoce výkonnou dostupnost zamýšleným službám. Při rozhodování, kterou možnost zvolit pro prostředí serveru, je třeba vzít v úvahu mnoho aspektů:

1.  Lidská kapacita pro správu a provoz serveru. Musí existovat lidské zdroje s obecnými dovednostmi ve správě serveru a ve specifických technologiích používaných pro aplikaci poskytující služby. Příkladem takových technologií jsou webové servery a platformy pro správu databází.

2.  Spolehlivá řešení pro automatické zálohování, včetně lokálního off-serveru a vzdáleného zálohování.

3.  Stabilní konektivita a velká šířka pásma sítě pro provoz na server a ze serveru.

4.  Stabilní napájení včetně záložního řešení.

5.  Zabezpečené prostředí pro fyzický server, pokud jde o problémy, jako je přístup, krádež a požár.

6.  Přítomnost plánu obnovy po havárii. Tento plán musí obsahovat realistickou strategii, která zajistí, že služba bude trpět pouze krátkými prostoji v případě selhání hardwaru, výpadku sítě a dalších.

7.  Proveditelný, výkonný a robustní hardware.

Všechny tyto aspekty musí být pokryty, aby se vytvořilo vhodné hostitelské prostředí. Hardwarový požadavek je záměrně kladen na poslední místo, protože existuje jasná tendence věnovat mu příliš mnoho pozornosti.

Když se podíváme zpět na tři hlavní možnosti hostování, zkušenosti z implementačních misí v rozvojových zemích naznačují, že všechny aspekty hostingu jsou zřídka přítomny v možnosti jedna a dvě na proveditelné úrovni. Dosažení přijatelné úrovně ve všech těchto aspektech je náročné z hlediska lidských zdrojů i peněz, zejména ve srovnání s náklady na možnost tři. Výhodou je, že vychází vstříc zmíněným politickým aspektům a budování místní kapacity pro správu serverů, na druhou stranu to lze zajistit alternativně.

Možnost tři - externí hosting - má tu výhodu, že podporuje všechny zmíněné aspekty hostingu za velmi přijatelnou cenu. Několik poskytovatelů hostingu - virtuálních serverů nebo softwaru jako služby - nabízí spolehlivé služby pro provozování většiny druhů aplikací. Příkladem takových poskytovatelů jsou webové služby Linode a Amazon. Správa těchto serverů probíhá přes síťové připojení, což je nejčastěji případ správy lokálních serverů. Fyzické umístění serveru se v tomto případě stává irelevantní v tom, že tito poskytovatelé nabízejí služby ve většině částí světa. Toto řešení se stále více stává standardním řešením pro hostování aplikačních služeb. Aspekt budování místní kapacity pro správu serveru je kompatibilní s touto možností, protože místní tým ICT může mít za úkol udržovat externě hostovaný server.

Přístup ke kombinování výhod externího hostování s potřebou místního hostingu a fyzického vlastnictví spočívá v použití externího poskytovatele hostingu pro primární transakční systém při zrcadlení tohoto serveru na nekritický lokálně hostovaný server, který se používá pouze pro čtení. jako je analýza dat a přístup přes intranet.
