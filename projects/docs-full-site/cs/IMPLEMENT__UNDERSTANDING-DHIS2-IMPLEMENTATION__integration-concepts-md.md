---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/integration-concepts.md"
revision_date: "2021-06-14"
---

# Koncepty integrace { #integration }

DHIS2 je otevřená platforma a její implementátoři aktivně přispívají k iniciativám interoperability, jako je openHIE. Databáze aplikací DHIS2 je navržena s ohledem na flexibilitu. Datové struktury, jako jsou datové prvky, organizační jednotky, formuláře a uživatelské role, lze definovat zcela volně prostřednictvím uživatelského rozhraní aplikace. Díky tomu je možné systém přizpůsobit mnoha místním kontextům a případům použití. DHIS2 podporuje mnoho požadavků na rutinní sběr a analýzu dat, které se objevují v implementacích zemí, a to jak pro scénáře HMIS, tak jako základní systém sběru a správy dat v doménách, jako je [logistika, správa laboratoře a finance](#Integration_and_interoperability).

## Integrace a interoperabilita { #Integration_and_interoperability }

Na základě svého přístupu k platformě je DHIS2 schopen přijímat a hostovat data z různých zdrojů dat a sdílet je s jinými systémy a mechanismy hlášení. Důležitým rozlišením konceptů integrace je rozdíl mezi integrací dat a interoperabilitou systémů:

- Když mluvíme o **integraci**, myslíme na proces zpřístupnění různých informačních systémů jako jednoho, zpřístupnění elektronických dat všem relevantním uživatelům, jakož i na harmonizaci definic a dimenzí, aby bylo možné data kombinovat v užitečné způsoby.

- Souvisejícím konceptem je **interoperabilita**, což je jedna strategie k dosažení integrace. DHIS2 považujeme za interoperabilní s jinými softwarovými aplikacemi kvůli jeho schopnosti vyměňovat si data. Například DHIS2 a OpenMRS jsou interoperabilní, protože umožňují vzájemné sdílení definic dat a dat. Interoperabilita závisí na standardech pro datové formáty, rozhraní, kódy a terminologie. V ideálním případě by se jednalo o mezinárodně dohodnuté standardy, ale v praxi se mohou skládat také ze standardů de facto (které mají široké přijetí a použití, ale nejsou nutně formálně schváleny v organizaci pro vývoj standardů) a dalších místních dohod v konkrétním kontextu.

DHIS2 se často používá jako integrovaný datový sklad, protože obsahuje (agregovaná) data z různých zdrojů, jako je [zdraví matek a dětí, malárie, údaje ze sčítání lidu a údaje o zásobách a lidských zdrojích](#Objectives_of_integration). Tyto zdroje dat sdílejí stejnou platformu DHIS2 a jsou k dispozici všechny ze stejného místa. Tyto subsystémy jsou tedy považovány za integrované do jednoho systému.

Interoperabilita navíc integruje zdroje dat z jiných softwarových aplikací. Například pokud jsou data ze sčítání uložena ve specializovaném [civilním registru nebo v systému důležitých událostí](#Health_information), interoperabilita mezi touto databází a DHIS2 by znamenala, že data ze sčítání budou také přístupná v DHIS2.

A konečně nejzákladnější integrační aktivitou (která není vždy zohledněna v diskusi o interoperabilitě) je možnost integrovat data ze stávajících papírových systémů nebo paralelních vertikálních systémů do DHIS2. Data budou zadávána přímo do DHIS2, aniž by procházela jinou softwarovou aplikací. Tento proces je založen na vytváření konzistentních definic indikátorů a může již výrazně snížit fragmentaci a vylepšit analýzu dat prostřednictvím integrovaného úložiště dat.

## Cíle integrace { #Objectives_of_integration }

Ve většině zemí najdeme mnoho různých **izolovaných** zdravotnických informačních systémů, které způsobují mnoho problémů se správou informací. Informační systém veřejného zdraví zaznamenal v posledních letech explozivní a často nekoordinovaný růst. Díky moderní informační technologii je implementace řešení ICT4D méně nákladná, což může vést k velké rozmanitosti řešení. Ohromujícím příkladem bylo prohlášení moratoria mHealth od ugandského Ministerstva Zdravotnictví v roce 2012 jako reakce na lavinu kolem [50 řešení mHealth](http://www.ictworks.org/2012/02/22/ugandan-mhealth-moratorium-good-thing) které byly realizovány v průběhu několika let. Většina z těchto řešení byla samostatnými řešeními, které nesdílely svá data s národními systémy a zřídka byla vyvinuta nad rámec pilotního stavu.

To může vést k závěru, že všechny systémy by měly být propojeny, nebo že **interoperabilita je sama o sobě cílem**. DHIS2 se však často používá v kontextech, kde je slabá infrastruktura a kde jsou zdroje pro spolehlivý provoz i základních systémů vzácné. Fragmentace je v této souvislosti vážným problémem, avšak přístupy interoperability mohou vyřešit pouze některé problémy fragmentace - a přístupy interoperability často vedou k další vrstvě složitosti.

> **Příklad**
>
> **Složitost logistických řešení v Ghaně**
> V oblasti logistiky nebo řízení dodavatelského řetězce lze často v jedné zemi nalézt velké množství paralelních, překrývajících se nebo konkurenčních softwarových řešení. Jak bylo uvedeno ve [studii JSI v roce 2012](http://docplayer.net/23773118-Ghana-landscape-analysis-of-supply-chain-management-software-tools-in-use.html), bylo zdokumentováno osmnáct (18!) různých softwarových nástrojů používaných v rámci dodavatelského řetězce veřejného zdraví jen v Ghaně.

Interoperabilita systémů se proto jeví jako jedna z možností, jak odstranit fragmentaci a nadbytečnost a poskytnout úředníkům v oblasti veřejného zdraví stručný a vyvážený obraz z dostupných zdrojů údajů. Úsilí o připojení mnoha redundantních softwarových řešení by však bylo velmi vysoké, a proto se jeví jako sporné. V prvním kroku by se mělo zaměřit na **snížení počtu paralelních systémů** a identifikaci nejrelevantnějších systémů, poté je možné tyto relevantní systémy integrovat.

Na tomto pozadí chceme definovat hlavní cíle integračních přístupů DHIS2:

- **Výpočet indikátorů**: Mnoho indikátorů vychází z čitatelů a jmenovatelů z různých zdrojů dat. Mezi příklady patří úmrtnost, včetně některých údajů o úmrtnosti jako čitatele a údajů o populaci jako jmenovatele, míry pokrytí zaměstnanců a vytížení zaměstnanců (údaje o lidských zdrojích a údaje o populaci a počtu zaměstnanců), míry očkování a podobně. Pro výpočet potřebujete data čitatele i jmenovatele, a proto by měla být integrována do jednoho datového skladu. Čím více zdrojů dat je integrováno, tím více indikátorů lze vygenerovat z centrálního úložiště.

- **Omezuje ruční zpracování** a zadávání dat: S různými daty na stejném místě není nutné ručně extrahovat a zpracovávat indikátory ani znovu zadávat data do datového skladu. Zejména interoperabilita mezi systémy různých datových typů (jako jsou registry pacientů a agregovaný datový sklad) umožňuje softwaru pro subsystémy elektronicky počítat i sdílet data. To snižuje množství ručních kroků při zpracování dat, což zvyšuje kvalitu dat.

- **Snižuje nadbytečnost**: Různé paralelní systémy často zachycují překrývající se a nadbytečná data. Například budou datové prvky související s HIV / AIDS zachyceny jak několika obecnými poradenskými a testovacími programy, tak specializovaným programem HIV / AIDS. Harmonizace nástrojů pro sběr dat těchto programů sníží celkovou zátěž koncových uživatelů. To znamená, že takové zdroje dat lze integrovat do DHIS2 a harmonizovat s existujícími datovými prvky, což zahrnuje jak požadavky na zadávání údajů, tak analýzu dat.

- Zlepšit **organizační aspekty**: Pokud lze se všemi údaji zacházet na jedné jednotce na ministerstvu zdravotnictví, namísto různých subsystémů udržovaných několika zdravotními programy, lze tuto jednotku profesionalizovat. Se zaměstnanci, jejichž jedinou odpovědností je správa, zpracování a analýza dat, lze rozvíjet specializovanější dovednosti a racionalizovat zpracování informací.

- Integrace **vertikálních programů**: Typická oblast vládního zdraví má mnoho existujících hráčů a systémů. Integrovaná databáze obsahující data z různých zdrojů se stává cennější a užitečnější než fragmentovaná a izolovaná. Například pokud je analýza epidemiologických údajů kombinována se specializovanými údaji [HIV / AIDS, TBC, finančními údaji a údaji o lidských zdrojích nebo je-li imunizace kombinována s logistickými / skladovými](#nn) údaji, poskytne úplnější obraz situace.

DHIS2 může pomoci zefektivnit a **zjednodušit architekturu systému**, a to po následujících otázkách, jako například: Jaký je cíl integračního úsilí? Může DHIS2 pomoci snížit počet systémů? Může integrace DHIS2 pomoci poskytnout relevantní informace o správě při nižších nákladech, vyšší rychlosti a lepší kvalitě dat než stávající systémy? Je DHIS2 nejlepším nástrojem k nahrazení jiných systémů, nebo je vhodnější jiné řešení vhodné pro daný účel, které může spolupracovat s DHIS2? Více praktických informací o definování těchto cílů naleznete v [_KROK 1 v 6-stupňovém implementačním pokynu_](https://www.dhis2.org/downloads).

## Výměna zdravotních informací { #Health_information }

Vzhledem k tomu, že existují různé případy použití zdravotnických informací, existují různé typy softwarových aplikací fungujících ve zdravotnictví. Termín architektura pro informace o zdraví používáme k popisu plánu nebo přehledu různých softwarových aplikací, jejich konkrétního použití a datových připojení. Architektura funguje jako plán ke koordinaci vývoje a interoperability různých subsystémů v rámci většího zdravotního informačního systému. Je vhodné vypracovat plán, který pokrývá všechny komponenty, včetně oblastí, na kterých aktuálně není spuštěn žádný software, aby bylo možné adekvátně vidět požadavky, pokud jde o sdílení dat. Tyto požadavky by poté měly být součástí specifikací softwaru, jakmile je vyvinut nebo zakoupen.

**[výměna informací o otevřeném zdraví (openHIE)](https://ohie.org/)** je interoperabilní interpretace této architektury, přičemž v ní často hraje významnou roli HMIS nebo DHIS2. Rámec openHIE byl vyvinut s jasným zaměřením na země s nízkým nastavením zdrojů prostřednictvím účasti několika institucí a rozvojových partnerů, včetně programu HISP z Osla.

Níže uvedený schematický přehled ukazuje hlavní prvky rámce openHIE, které obsahují vrstvu komponent, vrstvu služeb interoperability a externí systémy. Vrstva komponent openHIE pokrývá metadata nebo referenční data (terminologie, klienti, zařízení), osobní údaje (zaměstnanci, historie pacientů) a národní zdravotní statistiky. Účelem je zajistit dostupnost stejných metadat ve všech systémech, které se účastní odpovídající výměny dat (např. Definice indikátorů, pojmenování zařízení, kódování a klasifikace). V některých případech, jako v případě registru hlavního zařízení, mohou být data použita také k poskytování informací široké veřejnosti prostřednictvím webového portálu. Zatímco vrstva interoperability zajišťuje zprostředkování dat mezi různými systémy, vrstva externích systémů obsahuje několik subsystémů, mnoho na úrovni služeb, s často se překrývajícím funkčním rozsahem.

Existují různé přístupy k definování architektury eHealth. V kontextu tohoto pokynu DHIS2 rozlišujeme přístupy založené na připojení 1:1 versus přístupy založené na připojení n:n (mnoho k mnoha).

### _1:1_ integrace { #integrationSection }

V mnoha zemích je národní systém HMIS často prvním systémem zavedeným do velkého počtu zařízení a ke správě velkého množství dat na měsíční nebo čtvrtletní bázi. Když země začnou dále rozvíjet architekturu svých zdravotních systémů, bude DHIS2 často propojen s některými jinými systémy. Toto připojení se často provádí přímo pomocí jednoduchého skriptu, který automatizuje přenos dat.

Mluvíme o připojení 1:1, protože je omezeno na dva systémy. V případě integrace LMIS / HMIS jeden LMIS přenese data do DHIS2, jak je definováno ve skriptu. Tento praktický přístup často představuje první krok a je jedním z nejběžnějších případů použití na cestě k interoperabilní architektuře openHIE. Tato jednoduchost však přináší i nevýhody: V případě, že by druhý logistický systém chtěl přenést data do DHIS2 (např. Údaje o zboží pro konkrétní program nemoci), musel by být pro provedení tohoto úkolu napsán druhý skript. Tyto dva skripty by pak běžely nezávisle na druhém, což mělo za následek dvě samostatná připojení 1:1.

### _n:n_ integrace { #nn }

Jiný přístup je založen na umístění účelového softwaru, který slouží jako **vrstva interoperability** nebo přístup BUS, řízení přenosu dat mezi několika systémy na obou stranách (n:n). To by mohl být případ, kdybyste například chtěli sbírat data o stavu zásob prostřednictvím různých aplikací LMIS a poté je sdílet s centrálním skladem LMIS, HMIS a některým systémem programů vertikálních nemocí. Referenční software openHIE pro převzetí této role je ["OpenHIM"](http://openhim.org), ale pro tento účel byly také použity systémy jako ["MOTECH"](https://motechproject.org/) jak bude diskutováno níže.

I když tento přístup může vyústit ve vyšší počáteční úsilí, slibuje, že usnadní další projekt integrace, protože vrstva interoperability je doplněna o definice a mapování, které lze znovu použít pro připojení dalších systémů.

V praxi tento přístup přináší určité výzvy. Aktivace API vyžaduje značné úsilí kvalifikovaných zdrojů a s každou novou verzí jakéhokoli zapojeného systému vyžadují toky dat opětovné testování a v případě potřeby úpravy. Aby byly tyto implementační projekty úspěšné, musí obvykle projít řadou [_komplexních kroků_](https://www.dhis2.org/downloads), jako je dohoda o přístupu interoperability zakotveném v národní strategii elektronického zdravotnictví, definice datových standardů a udržitelné struktury údržby a dosažení konsensu zúčastněných stran o politikách vlastnictví a sdílení údajů. Spojení dat a systémů může mít dlouhodobé důsledky - vytváří nové role, úlohy a úkoly, které dříve neexistovaly a pro které nemusí být plánovány (správa metadat, správa komplexního systému, vyjednavači hranic atd.).

> **Příklad**
>
> **Střední vrstva Grameen DHIS2/CommCare v Senegalu**
> V [Integration concepts](#integration) slouží [MOTECH](https://motechproject.org/) jako technická střední vrstva mezi LMIS pro mobilní sběr dat na úrovni zdravotnického zařízení ([CommCare](http:// www.commcarehq.org)) a DHIS2, umožňující definovat mapování dat, transformační pravidla a kontroly kvality dat. Rozhraní je nastaveno tak, aby přenášelo data z CommCare Supply do DHIS2, kdykoli jsou data v zařízení uložena do formuláře CommCare. Pro každou komoditu jsou z CommCare do DHIS2 přenášeny údaje o spotřebě, dostupných zásobách, ztrátách a vyprodání zásob.
> Vyšší počáteční investice senegalského přístupu naznačují ambicióznější dlouhodobou systémovou architekturu, která předvídá, že platforma MOTECH může v budoucnu sloužit k uspokojení dalších úkolů v oblasti interoperability. Nevidíme však žádnou z aktivit země pevně zakotvenou v učebnicové architektuře eHealth, která by jasně definovala oblasti priorit, vedoucí systémy pro každou prioritu a vztahy a výsledná API mezi těmito různými komponentami. Někdo může namítnout, že projekty interoperability jsou postaveny na slabém základě, pokud neexistuje předchozí konsenzus o architektonickém hlavním plánu. Na druhé straně je také cenné umožnit organický rozvoj systémových iniciativ, pokud jsou zakořeněny v dobře podložených potřebách země.

### Architektura, standardy a mapování { #architecture-standards-and-mapping }

Důležitým prvkem architektury eHealth je zahrnutí **mezinárodních standardů eHealth**. Standardy jsou obzvláště relevantní pro připojení n:n, méně pro přímé připojení (1:1).

Některé standardy jsou na technické úrovni (např. Přenosové metody), jiné na obsahové stránce (např. Základní indikátory WHO 100). Postupné sladění národních systémových iniciativ s těmito standardy může poskytnout zemím přístup k osvědčeným řešením, těžit z lékařských a technologických inovací.

> **Příklad**
>
> **Ghana EPI**
> Případ Ghany ilustruje, jak požadavky WHO na podávání zpráv EPI slouží k definování standardních dat v DHIS2. Tato standardizace na datové a terminologické úrovni je základem systémové integrace. V oblasti DHIS2 pokračují práce s WHO na vývoji standardizovaných datových sad, které by v budoucnu mohly otevřít nové příležitosti pro interoperabilitu a zvýšení efektivity tím, že nabídnou určitou konzistenci metadat napříč systémy, a také povzbudí země, aby znovu využívaly stávající řešení.

Na úrovni **jazyka** je třeba být ohledně definic konzistentní. Pokud máte dva zdroje dat pro stejná data, musí být srovnatelné. Pokud například shromažďujete údaje o malárii ze standardních klinik i z nemocnic, musí tato data popisovat totéž, pokud je třeba je kombinovat pro součty a indikátory. Pokud nemocnice hlásí případy malárie podle pohlaví, ale ne podle věkové skupiny, a jiné kliniky hlásí podle věkové skupiny, ale ne podle pohlaví, nelze tato data analyzovat podle jedné z těchto dimenzí (i když lze vypočítat celkový počet případů). Je tedy třeba dohodnout se na jednotných definicích.

Kromě jednotných definic v různých subsystémech musí být přijaty **standardy pro výměnu dat**, pokud mají být data sdílena elektronicky. Různé softwarové aplikace by to potřebovaly, aby si rozuměly. DHIS2 podporuje několik datových formátů pro import a export, včetně nejdůležitějšího standardu ADX. Podporují to i další softwarové aplikace, což umožňuje sdílení definic dat a agregaci dat mezi nimi. Pro DHIS2 to znamená, že podporuje import agregovaných dat, která jsou dodávána jinými aplikacemi, jako jsou [OpenMRS](http://openmrs.org) (pro správu pacientů) a [iHRIS](https://www.ihris.org/) (pro řízení lidských zdrojů).

Rozhodujícím prvkem architektury je, jak organizovat **mapování** dat. Metadata různých systémů se obvykle neshodují přesně. Pokud Ministerstvo zdravotnictví nevynucuje následnou zásadu standardů dat, budou mít různé systémy pro zařízení různé kódy a štítky. jeden systém jej může nazvat _Oddělení nemocnice - 123_, druhý systém jej může označovat jako Centrum pro léčbu malárie - 15. Aby bylo možné přenášet data, je třeba někde uložit informace, které tyto dvě zařízení odpovídajícím způsobem popisují.

V případě připojení 1:1 je třeba toto mapování provést a udržovat pro každé připojení, v případě přístupu interoperability n:n lze jednu stranu definic znovu použít.

Abyste zajistili plynulý tok dat, musíte mít jasnou odpovědnost na obou stranách systému ohledně údržby a odstraňování problémů s daty. Například je třeba předem definovat standardní postupy pro činnosti, jako je přidání, přejmenování, dočasná deaktivace nebo odebrání zařízení v jednom ze dvou systémů. Změny v databázových polích, která jsou zahrnuta v přeneseném datovém záznamu, musí být také systematicky koordinovány.

## Agregovaná a transakční data { #aggregate-and-transactional-data }

DHIS2 rozšiřuje svůj dosah do mnoha zdravotnických systémů. Počínaje známým základem agregovaných datových souborů pro rutinní data, zahrnoval data týkající se pacientů a poté data v oblasti HR, financí, logistiky a řízení laboratoře, směřující k provozním nebo transakčním datům.

Můžeme rozlišovat mezi transakčními a agregovanými údaji. **Transakční systém** (nebo operační systém z pohledu datového skladu) je systém, který shromažďuje, ukládá a upravuje data na podrobné úrovni. Tento systém se obvykle používá pro každodenní zadávání a ověřování údajů. Design je optimalizován pro rychlé vkládání a aktualizaci výkonu. DHIS2 může obsahovat agregovaná data z externích zdrojů dat, obvykle agregovaná v dimenzi prostoru (hierarchie organizačních jednotek), časové dimenzi (za více období) a pro vzorce indikátorů (matematické výrazy včetně datových prvků).

Když se podíváme na transakční systém, jako je logistický software pro celý dodavatelský řetězec nebo jeho části, je třeba učinit jedno zásadní rozhodnutí: Potřebujete sledovat všechny podrobné transakce na všech úrovních, včetně operací, jako jsou vrácení, převod mezi zařízeními, čtení čárových kódů, správa šarží a expirace? Nebo můžete získat většinu svých potřebných výsledků přehledu rozhodnutí pomocí agregovaných dat?

Dodavatelské řetězce mohou být často dobře sledovány a do určité míry spravovány, pokud jsou spolehlivě k dispozici údaje tam, kde a kdy jsou potřebná pro provozní rozhodnutí a pro účely monitorování. Hlavní ukazatele *příjem, spotřeba a stav zásob na konci roku období* lze spravovat bez elektronických transakcí a často stačí k získání celkového obrazu výkonu systému a může snížit potřebu systémových investic.

Buďme realističtí ohledně toho, jaké údaje je třeba shromažďovat, jak často a kdo je bude používat, je důležité, abyste nevytvářeli systémy, které by selhaly kvůli nedostatečnému použití nebo nerealistickým očekáváním, jak budou data použita. Systémy pro správu digitální logistiky mohou dobře fungovat, pokud jsou plně integrovány do rutinních pracovních toků a jsou navrženy tak, aby usnadnily nebo zefektivnily práci uživatelů.

> **Poznámka**
>
> Očekávání, že podrobnější údaje povedou k lepšímu řízení logistiky, není vždy splněno. Ambiciózní pokus o pravidelné shromažďování údajů o logistických transakcích má někdy za následek nižší kvalitu dat, například proto, že záznam dat, ke kterému může dojít denně, namísto měsíčně nebo čtvrtletně, není prováděn spolehlivě. Na druhou stranu, pokud je transakční systém dobře udržován a monitorován, mohou podrobnější údaje pomoci identifikovat nepřesnosti a problémy s kvalitou dat, snížit plýtvání (kvůli vypršení platnosti nebo selhání CCE), podpořit odvolání, řídit výkon a vést ke zlepšení dodavatelského řetězce a rozhodování. Analýza podrobných dat může pomoci odhalit hlavní příčiny některých problémů a z dlouhodobého hlediska zlepšit kvalitu dat.

DHIS2 může ve scénářích interoperability převzít různé role. Běžným scénářem interoperability je, aby DHIS2 přijímal agregovaná data z operačního systému, v takovém případě operační systém sečte transakce před jejich předáním do DHIS2. DHIS2 však může být do určité míry nakonfigurován také k ukládání podrobných transakčních dat, jejich přijímání z externích systémů nebo přímým zadáváním dat v DHIS2.

Na tomto základě se pokusíme vytvořit srovnávací přehled, který porovnává agregovanou správu dat DHIS2 se správou dat externího specializovaného systému. To může sloužit jako hrubá orientace, ale není statické, protože s téměř každým vydáním se rozšiřují možnosti DHIS2 a jeho interpretace implementátory.

| Plocha | Agregát DHIS2 | Externí specializované systémy |
| --- | --- | --- |
| Logistika | Souhrnná data, např. úrovně zásob zařízení na konci měsíce lze odesílat prostřednictvím DHIS2. DHIS2 může vytvářet jednoduché zprávy o stavu zásob a spotřebě. | Řízení dodavatelského řetězce podporuje operace logistického systému a může sledovat podrobné pohyby zásob (výdej, opětovné zásobování, přidělování, plýtvání) a zaznamenávat podrobnosti, jako jsou čísla výrobních šarží. Systémy SCM vytvářejí prognózy, doplňování a propracované kontrolní zprávy, které umožňují sledování stavu zásob v reálném čase, upozornění (nízké zásoby, řízení pracovního toku, selhání CCE atd.), podporované odhady a nouzové objednávky. |
| Finance | Souhrnná data, např. o celkových výdajích nebo hotovosti lze zaslat prostřednictvím DHIS2. DHIS2 může vytvářet jednoduché přehledy financí, např. o zbývajících rozpočtech. | Systémy pro správu financí umožňují plně dohledatelné zaznamenávání finančních transakcí podle zákonných požadavků, včetně sestavování rozpočtu, převodů, zrušení, vrácení peněz atd. Vícedimenzionální označování transakcí umožňuje analytické zprávy. |
| Trasování pacientů | Údaje týkající se nemocí nebo programů shromažďuje server DHIS2, program DHIS2 Trasovač také umožňuje zjednodušený podélný pohled na lékařské záznamy, včetně anamnézy pacientů a vícestupňových klinických cest. | Specializované systémy pro správu nemocnic dokážou pokrýt a optimalizovat složité pracovní toky mezi různými odděleními (např. Recepce, přepážky plateb, oddělení, OPD, IPD, laboratoř, zobrazování, sklad, správa financí a lidských zdrojů, údržba zdravotnických prostředků atd.). |
| Lidské zdroje | DHIS2 shromažďuje indikátory týkající se lidských zdrojů, například plánované pozice a volná místa na zařízení. | Specializovaný systém řízení lidských zdrojů může sledovat podrobné informace o stavu a změny zdravotnického pracovníka (akreditace, povýšení, volno, změna pozice, změna místa, další školení atd.). Dodává se s předem navrženými zprávami jak pro provozní dohled, tak pro plánování. |

## Různé scénáře integrace DHIS2 { #different-dhis2-integration-scenarios }

Různé výše popsané cíle vedou k různým scénářům integrace. DHIS2 může v architektuře systému převzít více **rolí**:

- Vstup dat: zadávání dat (offline, mobilní), import dat (transakční data, agregovaná data)

- Ukládání, vizualizace a analýza dat pomocí vestavěných nástrojů (DWH, zprávy, GIS)

- Sdílení dat s externími nástroji (např. DVDMT), prostřednictvím webových rozhraní API, webových aplikací

  V následujících odstavcích pojednáváme o přístupu k datům a sdílení dat, poté představíme příklad vertikální integrace, kde DHIS2 často převezme všechny tyto role.

  Role DHIS2 pro ukládání, vizualizaci a analýzu dat je popsána samostatně v [sekci datového skladu](https://docs.dhis2.org/master/en/implementer/html/ch05.html).

### Zadávání dat { #data-input }

Existuje několik aspektů, jak DHIS2 zachází se zadáváním dat. Na nejzákladnější úrovni slouží DHIS2 k nahrazení nebo alespoň zrcadlení papírových formulářů pro sběr dat a integraci dat elektronicky. To povede k **manuálnímu zadávání dat** aktivitám na úrovni zařízení nebo na úrovni správy zdravotnictví. Další možností vstupu je **import dat**. DHIS2 umožňuje importovat data prostřednictvím uživatelského rozhraní, což je metoda vyžadující malé technické znalosti, ale je třeba ji provádět ručně pokaždé, když je potřeba data zpřístupnit. Podrobný popis funkcí importu naleznete v [uživatelských příručkách DHIS2](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#import).

> **Tip**
>
> Postup ručního zadávání dat a importu vyžaduje relativně malé technické úsilí. Mohou být také dočasně použity k pilotnímu přístupu k integraci dat. To umožňuje uživateli testovat indikátory a zprávy, aniž by musel používat vyhrazené technické zdroje pro vývoj funkcí automatizované interoperability, a to buď prostřednictvím připojení 1:1 nebo n:n.

### Sdílení dat { #data-sharing }

Existují tři scénáře sdílení, (1) jednoduchý [_export dat_](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#export), (2) [_DHIS2 aplikace a (3) externí aplikace nebo weby připojující se k webovému rozhraní DHIS_](https://docs.dhis2.org/master/en/developer/html/dhis2_developer_manual_full.html). Podobně jako funkce importu popsané v části zadávání dat, nejpřístupnějším způsobem sdílení dat je použití funkcí exportu dat, které jsou k dispozici v uživatelské nabídce, což vyžaduje malé technické znalosti.

Díky své modulární konstrukci lze DHIS2 rozšířit o **další softwarové moduly, které lze stáhnout z DHIS2** [_App store_](https://www.dhis2.org/appstore). Tyto softwarové moduly mohou žít bok po boku s jádrovými moduly DHIS2 a lze je integrovat do portálu a systému nabídek DHIS2. Jedná se o výkonnou funkci, protože v případě potřeby umožňuje rozšířit systém o další funkce, obvykle pro specifické požadavky dané země, jak již bylo uvedeno výše.

Nevýhodou rozšiřitelnosti softwarového modulu je to, že klade několik omezení na vývojový proces. Vývojáři, kteří vytvářejí další funkce, jsou kromě omezení kladených na návrh modulů portálovým řešením DHIS2 omezeni na technologii DHIS2, pokud jde o programovací jazyk a softwarové rámce. Tyto moduly musí být také zahrnuty do softwaru DHIS2, když je software vytvořen a nasazen na webovém serveru, nikoli dynamicky během běhu.

Za účelem překonání těchto omezení a dosažení volnějšího propojení mezi servisní vrstvou DHIS2 a dalšími softwarovými artefakty se vývojový tým DHIS2 rozhodl vytvořit **webové API**. Toto webové rozhraní API odpovídá pravidlům architektonického stylu REST. To znamená, že:

- Webové rozhraní API poskytuje navigovatelné a strojově čitelné rozhraní pro kompletní datový model DHIS2. Například je možné přistupovat k úplnému seznamu datových prvků, poté pomocí zadaného hypertextového odkazu přejít na konkrétní datový prvek, který nás zajímá, a poté pomocí zadaného hypertextového odkazu přejít na seznam formulářů, jejichž je tento datový prvek součástí. Např. klienti budou přechody stavu provádět pouze pomocí hypertextových odkazů, které jsou dynamicky vloženy do odpovědí.

- K datům se přistupuje prostřednictvím jednotného rozhraní (URL) pomocí známého protokolu. Nejsou zapojeny žádné fantastické transportní formáty ani protokoly - pouze dobře otestovaný a dobře srozumitelný protokol HTTP, který je dnes hlavním stavebním kamenem webu. To znamená, že vývojáři třetích stran mohou vyvíjet software pomocí datového modelu a dat DHIS2, aniž by věděli o specifické technologii DHIS2 nebo dodržovali konstrukční omezení DHIS2.

- Veškerá data včetně metadat, zpráv, map a grafů, která jsou v terminologii REST známá jako zdroje, lze načíst ve většině populárních formátů reprezentace dnešního webu, jako jsou HTML, XML, JSON, PDF a PNG. Tyto formáty jsou široce podporovány v aplikacích a programovacích jazycích a poskytují vývojářům třetích stran širokou škálu možností implementace.

K tomuto webovému API lze přistupovat z jiného externího informačního systému. Úsilí potřebné pro vývoj nových informačních systémů a jejich údržbu v průběhu času je často do značné míry podceňováno. Místo toho, aby bylo možné začít úplně od začátku, lze na webové rozhraní API postavit novou aplikaci.

Externí systémy mohou nabídnout různé možnosti vizualizace a prezentace dat DHIS2, např. ve formě ovládacích panelů, GIS a grafů komponent. Webové portály zaměřené na doménu zdraví mohou používat DHIS2 jako hlavní zdroj agregovaných dat. Portál se může připojit k webovému API a komunikovat s příslušnými prostředky, jako jsou mapy, grafy, zprávy, tabulky a statické dokumenty. Tyto datové pohledy mohou dynamicky vizualizovat agregovaná data na základě dotazů na dimenzi organizační jednotky, indikátoru nebo období. Portál může přidávat hodnotu k přístupnosti informací několika způsoby. Může být strukturován uživatelsky přívětivým způsobem a zpřístupňovat data nezkušeným uživatelům. Příkladem toho je [Tanzanijský webový portál HMIS](https://appstore.hisptanzania.org/).

## Model vyspělosti DHIS2 { #dhis2-maturity-model }

S ohledem na všechny výše uvedené prvky v architektuře systému a datových typech mají implementátoři DHIS2 několik možností, jak přistupovat k implementacím:

- Zaměření na transakční nebo agregovaná data

- Zaměření na integraci dat nebo interoperabilitu systémů

Vzhledem k úsilí potřebnému k zavedení interoperability systémů se mnoho ministerstev zdravotnictví vydává za pragmatickou zkratku pro integraci dat, jako jsou základní údaje o úrovni zásob, **přímo do jejich stávajícího národního DHIS2**. Jako rychle se rozvíjející platforma přidává DHIS2 v posledních letech mnoho funkcí, zejména v DHIS2 Trackeru. Na příkladu logistických dat jsou aktuálně k dispozici následující hlavní funkce:

- Formulář pro zadávání dat odrážející široce používaný papírový formulář Report and Requisition (R & R). Zadávání dat pomocí zařízení je možné prostřednictvím stolního prohlížeče nebo mobilní aplikace, a to i v režimu offline. Tyto elektronické formuláře mohou zaměstnanci vyplňovat na základě papírových karet, které jsou obvykle umístěny vedle komodity ve skladišti.

- DHIS2 pak může vytvářet zprávy pro monitorování výkonu na centrální úrovni, což dává správcům komodit a programů pochopení fungování logistického systému. V závislosti na tom, jak logistický systém funguje, mohou tato data také podporovat operativní rozhodování, i když více nejprve by měla být provedena kompletní analýza logistických obchodních procesů a uživatelů.

- Skladové údaje lze transformovat do logistických indikátorů, které lze uvést do kontextu s dalšími indikátory programu, například křížové odkazy na počet pacientů léčených specifickou patologií a odpovídající spotřebu léků.

Ačkoli každá země, na kterou se podíváme v případech použití, má vlastní vývojovou cestu směrem k systémové integraci, některé běžné poznatky lze vyvodit z jejich zkušeností. Níže uvedený model zralosti popisuje evoluční přístup k řešení problémů s integrací a interoperabilitou, což umožňuje různým zúčastněným stranám v národním zdravotním systému rozvíjet profesionální analytické návyky a zvyky využití dat.

Model zralosti navrhuje přechod od agregovaných dat k transakčním datům a od samostatných k interoperabilním systémům (na příkladu logistických dat).

1.  DHIS2 je často jedním z prvních systémů, které pokrývají správu zdravotnictví a několik úrovní zařízení v zemi. Nejprve jsou zahrnuty základní indikátory onemocnění (například odpovídající 100 základním zdravotním indikátorům WHO).

2.  Ve druhé fázi se různé zúčastněné strany snaží doplnit údaje o nemoci a poskytování služeb, které hlásí, základními údaji LMIS. To lze provést agregovaně v DHIS2, např. zahrnutím úrovní zásob a spotřeby do pravidelných zpráv. To poskytne informace na vysoké úrovni o výkonu logistického systému, ale může nebo nemusí poskytnout dostatečné informace k podpoře vylepšených operací logistického systému.

3.  V dospělejší fázi může existovat legitimní potřeba specializovaných logistických systémů, zvláště když se chce, aby velmi detailní transakční pohled měl podrobnější kontrolu (např. Vrácení, převody mezi zařízeními, čísla šarží a expirace atd.). DHIS2 Tracker může nabídnout některé funkce správy dat související s událostmi nebo pacienty, ale nemůže vždy dosáhnout stupně podpory pracovního toku poskytované jinými, více specializovanými řešeními.

4.  Ve vyspělém technologickém a manažerském prostředí mohou být logistické transakce sdíleny na DHIS2 v agregované podobě, od samostatného k integrovanému scénáři.

## Kroky implementace pro úspěšnou integraci dat a systému { #implementation-steps-for-successful-data-and-system-integration }

Účelem tohoto podrobného průvodce implementací DHIS2 je poskytnout metodologii pro implementátory k vytvoření a podpoře scénáře integrace DHIS2. Průvodce je založen na osvědčených postupech a získaných zkušenostech. Průvodce se zasazuje o iterativní a agilní přístup zaměřený na zemi, který začíná shromažďováním uživatelských příběhů a funkčních požadavků. Průvodce je zamýšlen jako rámec, který lze přizpůsobit konkrétnímu kontextu každé země. Obsah popisuje konkrétní příklady pro každý krok s podrobným popisem uživatelských příběhů, specifikací dat, pracovních pomůcek a kontrolních seznamů pro vedení používání referenčního implementačního softwaru. Základní struktura, včetně 6 kroků, je založena na [metodice implementace OpenHIE](https://wiki.ohie.org/display/documents/OpenHIE+Planning+and+Implementation+Guides):

**Krok 1**: Identifikace zúčastněných stran a motivace pro vylepšená data zařízení

**Krok 2**: Specifikace registru zařízení dokumentu a uživatelské příběhy

**Krok 3**: Nastavení počáteční instance

**Krok 4**: Identifikujte mezery a iterativní vývoj pomocí uživatelských testů

**Krok 5**: Škálování implementace registru

**Krok 6**: Poskytujte průběžnou podporu

Kromě těchto kroků souvisejících s interoperabilitou je také zajímavé odkázat zpět na některé obecné zkušenosti s implementací DHIS2 a osvědčené postupy uvedené v oddílech [Doporučení pro národní implementace HIS](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e86) a [Nastavení nové databáze](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e250). Typický implementační přístup DHIS2, který je také zásadní pro projekty interoperability, je **participativní** přístup. Tento přístup zdůrazňuje zahrnutí hned od začátku projektu [místní tým](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e255) s různými schopnostmi a pozadím převzít odpovědnost co nejdříve to je možné.

### Krok 1: Definujte strategii, zúčastněné strany a cíle využití dat { #step-1-define-strategy-stakeholders-and-data-usage-objectives }

V prvním kroku budou definovány cíle integračního projektu. Jako u každého technologického projektu by měla existovat jasná **shoda ohledně strategických a funkčních cílů**. Technologické inovace a proveditelnost by neměly být jedinou hnací silou, ale spíše jasně definovaným organizačním cílem. Proto je tento krok určen také k zodpovězení otázky: „Proč chceme propojit systémy nebo integrovat data z různých zdrojů pomocí DHIS2?“

Na praktické úrovni to vede k otázkám týkajícím se přístupu k integraci dat, například:

- Chcete eliminovat papírové formuláře nebo dokonce odstranit soubory dat, které jsou nadbytečné nebo již nejsou potřeba?

- Můžete integrovat (agregovaná) data do DHIS2?

- Můžete integrovat podrobná (např. na úrovni pacienta nebo transakční) data do DHIS2 pomocí funkcí trasovače DHIS2?

- Pokud chcete vytvořit spojení pro výměnu dat mezi DHIS2 a jiným systémem, jak definujete vlastnictví a odpovědnosti?

Činnosti k zodpovězení této otázky jsou popsány níže a položí základy pro projekt interoperability DHIS2.

#### Identifikujte zúčastněné strany a motivace { #identify-stakeholders-and-motivations }

Je povahou projektů interoperability mít více než jednu zúčastněnou stranu. Zúčastněné strany z různých oblastí se musí dohodnout na společném systémovém přístupu, například tým odpovědný za národní HMIS (např. Oddělení M\&E nebo oddělení plánování) a logistické oddělení v případě implementace LMIS. Tyto dvě hlavní oblasti mají často dílčí rozdělení, např. v logistické oblasti jednotka nákupu, jednotka skladování, jednotka dopravy. Kromě toho budou mít zúčastněné strany z programů zaměřených na konkrétní choroby vlastní režimy a správci komodit. Kromě těchto místních aktérů jsou do rozhodovacího procesu často zapojeni také mezinárodní partneři (agentury, dárci, iNGO, poradenské společnosti).

Je proto zajímavé podívat se na hlavní motivace zúčastněných stran a na to, jak zmírnit rizika vyplývající z potenciálně odlišných zájmů.

- Centrální oddělení MZ, jako je **M\&E&**plánování, jsou často hlavními zúčastněnými stranami pro standardizaci indikátorů a IT systémů

- **Centrální IT oddělení** mají obecný zájem na (často místně řízených) technologických volbách a vlastnictví, nákupu hardwaru a softwaru. Často řeší problémy se sítí a hardwarem, ale nemají zkušenosti s komplexními webovými architekturami a výměnami dat.

- **Specializované programy zaměřené na nemoci** jsou často pod tlakem, aby poskytovaly velmi specifické ukazatele programu, a to jak pro vlastní řízení, tak také v reakci na dárcovské přístupy. Mohou se také cítit pohodlněji při ovládání svého správného IT systému, aby si byli jisti, že jejich potřeby jsou upřednostňovány.

- **Specializované funkční oblasti** (jako jsou lidské zdroje, logistika, správa nemocnic) jsou často v sendvičové pozici a musí uspokojovat informační potřeby několika různých zúčastněných stran, přičemž se snaží dosáhnout provozní efektivity s omezenými zdroji.

Identifikováním toho, kdo má zájem poskytnout nebo využít data, mohou hlavní implementátoři začít vytvářet projektový tým, který bude informovat o návrhu a implementaci. Jedna metoda pro charakterizaci zúčastněných stran zahrnuje seskupení zúčastněných stran podle jejich funkčních rolí. Stávající infrastruktura a postupy jsou také důležité pro pochopení možností správy a kurátorství. Pochopení zúčastněných stran a jejich odpovídajících systémů je prvním kritickým krokem.

#### Inventář systému eHealth { #ehealth-system-inventory }

Je důležité získat jasný přehled o celkovém prostředí systémů IT. To může pomoci zajistit, aby se investice do interoperability prováděly za účelem posílení hlavních systémů a aby investice přispěly k **zjednodušení** architektury systému. Například pokud inventarizace systému ukáže, že existuje spousta nadbytečných funkčních systémů, např. více než 10 různých logistických systémů nebo modulů v zemi by se projekt interoperability měl pokusit přispět k střednědobé nebo dlouhodobé racionalizaci této situace. To by mohlo znamenat účast na národním procesu hledání konsensu, který by identifikoval řešení, která jsou do budoucna nejvhodnější, identifikovala národní „šampióny“ pro každou specializaci a vypracovala plán pro sladění těchto systémů nebo dat a odstranění nevyužitých nebo nadbytečných systémů.

Také v této souvislosti je zajímavé analyzovat, zda lze jednoduché indikátory shromažďovat a spravovat v samotném DHIS2 a jak to může doplňovat snahy o zlepšení logistického systému (jak je to později vysvětleno v [příkladu LMIS](#lm)). Jakmile budou identifikovány stabilní a udržitelné systémy, může začít plánování výměny dat s DHIS2.

#### Prozkoumejte příležitosti a výzvy { #explore-opportunities-and-challenges }

Motivace vedoucí k implementaci lze podrobně popsat vnímanými příležitostmi nebo výzvami, kterým zúčastněné strany čelí. To může zahrnovat touhu sdílet data napříč systémy souvisejícími se zdravotnickými zařízeními pro správu, monitorování a hodnocení dodavatelského řetězce, poskytování zdravotních služeb a mnoho dalších systémů. Příběhy uživatelů a případy použití budou podrobně zdokumentovány v průběhu kroku 2, ale je také nutná vize motivace k interakci s partnery na vysoké úrovni.

#### Organizace a lidské zdroje { #organisation-and-hr }

Na začátku projektu by měly být zavedeny jasné národní politiky týkající se integrace dat, vlastnictví dat, rutiny pro sběr, zpracování a sdílení dat. Během integrace často dojde k určitému období narušení normálního toku dat, takže u mnoha bude nutné posuzovat dlouhodobé vyhlídky na efektivnější systém proti krátkodobému narušení. Integrace je tedy často postupný proces, kdy je třeba přijmout opatření, aby k tomu došlo co nejplynuleji.

> **Příklad**
>
> **Ghana CHIM**
>
> - **Spolupráce zúčastněných stran**: Ghanské _centrum pro správu zdravotnických informací_ (CHIM) má jasnou pozici vůči vertikálním programům a dalším partnerům se správnými softwarovými iniciativami. CHIM zavádí DHIS2 jako atraktivní možnost sběru dat, která podporuje ostatní zúčastněné strany GHS, aby se připojili k DHIS2 a pracovali na společné strategii interoperability, rozvíjející DHIS2 podle potřeb zúčastněných stran. **To zahrnuje také smlouvy o sdílení dat**.
> - **Silný pocit vlastnictví systému**: CHIM má silné odhodlání vybudovat v týmu CHIM nezbytné know-how pro konfiguraci a údržbu systému. Tým CHIM se skládá z pracovníků zdravotnických informací, kteří kombinují dovednosti v oblasti veřejného zdraví a správy dat.

Rovněž jasně definované **postupy údržby a aktualizace systému** mohou určitě pomoci při správě interoperability.

> **Příklad**
>
> **Ghana CHIM**
> Například v případě Ghana DHIS2 je zaveden jasný roční cyklus aktualizace systému: Ke konci každého roku jsou vytvořeny nové indikátory a jsou vydány odpovídající papírové formuláře. Zaměstnanci absolvují školení a jsou připraveni na zadávání dat. Do tohoto cyklu aktualizace byl zahrnut nový formulář pro data EPI a pracovníci EPI byli v rámci procesu připraveni na zadávání dat. Tento systematický postup umožňuje GHS rychle reagovat na potřeby zúčastněných stran, jako je program EPI, a vyhovět jejich potřebám v oblasti dat a výkaznictví s omezenými a předvídatelnými investicemi. Staví CHIM do pozice, kdy může přispět k racionalizaci a zjednodušení národní architektury zdravotnického systému a postupně integrovat správu dat pro **vertikálnější programy**, a to jak na straně zadávání dat, tak na straně analýzy.

Klíčovým principem pro HISP je zapojit místní tým do budování systému od samého začátku, v případě potřeby s vedením externích odborníků, a nezdržovat přenos znalostí na konci implementace. Vlastnictví pochází především ze stavby systému a vlastnictví každého kroku tohoto procesu.

### Krok 2: Specifikace a požadavky na dokument { #step-2-document-specifications-and-requirements }

- Shromážděte existující metadata

- Specifikace dat dokumentu

- Dokumentujte příběhy uživatelů

### Krok 3: Proveďte specifikace a identifikujte mezery { #step-3-carry-out-specifications-and-identify-gaps }

- Implementujte specifikace

- Identifikujte a piroritizujte neúplné uživatelské příběhy

### Krok 4: Iterace a uživatelské testování { #step-4-iteration-and-user-testing }

- Agilní a iterativní vývoj

- Uživatelské testování

- Shromažďujte, slučujte a nahrávejte data

### Krok 5: Škálování { #step-5-scale-up }

- Potvrďte uživatelské role a odpovědnosti

- Školení uživatelů

- Kritické integrace

### Krok 6: Trvalá podpora { #title_nxr_lxp_41b }

Zatímco během fáze implementace by měla být k dispozici dočasná podpůrná struktura, poté je třeba zřídit trvalou podpůrnou strukturu. Hlavní výzvou je mít jasnou odpovědnost. V ideální situaci máme co do činění se dvěma stabilními systémy, z nichž každý již má svou jasně definovanou podpůrnou strukturu.

Ve skutečnosti však bude možná potřeba se vyrovnat s opakujícími se výzvami: Mnoho systémů veřejného zdraví prochází dynamickým vývojem, což vede ke změnám v potřebách sběru dat nebo výpočtu indikátorů.

Interoperabilita bývá zdlouhavým technickým a organizačním nábojem. Všechny tři popsané iniciativy spotřebovaly značné úsilí kvalifikovaných **zdrojů** k aktivaci API. S každou novou verzí jakéhokoli zapojeného systému navíc vyžadují datové toky opětovné testování a v případě potřeby úpravy. Aby byly tyto implementační projekty úspěšné, musí obvykle projít řadou složitých kroků, například dohodou o přístupu interoperability zakotvenou v národní strategii elektronického zdravotnictví, definicí datových standardů a strukturou udržitelné údržby a dosažením konsensu zúčastněných stran o vlastnictví dat. a zásady sdílení. Spojení dat a systémů může mít dlouhodobé důsledky - vytváří **nové role, úkoly a kategorie práce**, které je třeba plánovat (správa metadat, správa komplexního systému, vyjednavači hranic atd.). Řešením by mohla být diskuse o nových odpovědích předem, jejich přiřazení k popisu práce, týmům a konkrétním pozicím.

#### Odpovědnost za metadata { #metadata-responsibility }

Další důležitou oblastí je **správa metadat**, zejména ve scénářích sekundárního použití dat. V samostatném nastavení lze spravovat metadata, jako jsou kódy zařízení nebo komodit, bez velkého zohlednění potřeb ostatních zúčastněných stran. Ale v prostředí interoperability budou mít změny metadat účinky mimo jednotlivý systém. Řízení metadat lze vysoce formalizovat prostřednictvím registrů nebo manuálněji prostřednictvím lidských procesů.

Aby bylo možné určit vhodný přístup, je užitečné odhadnout očekávané _ úsilí údržby metadat_ a důsledky nesynchronizovaných metadat napříč různými systémy. V případě integrací LMIS / DHIS2 existují potenciálně tisíce identifikátorů zařízení, které by mohly být synchronizovány. Normálně se však identifikátory zařízení nemění často, protože fyzická infrastruktura většiny systémů veřejného zdraví je relativně konstantní. Pokud jde o komodity, ačkoli se režimy a prioritní léky mohou v průběhu času měnit, počet souborů dat je relativně malý: Seznam komodit programu často obsahuje méně než 20 produktů. Proto často může být praktické ručně aktualizovat komoditu a neinvestovat do řešení interoperability, jako je automatizovaná synchronizace metadat.

## Specifické případy použití integrace a interoperability { #specific-integration-and-interoperability-use-cases }

DHIS2 rozšiřuje svůj dosah do mnoha zdravotnických systémů. Počínaje známým základem agregovaných datových souborů pro rutinní data zahrnula data související s pacienty a poté data v oblasti HR, financí, logistiky a laboratorního managementu. To je v souladu s vývojem DHIS2 v mnoha nastaveních zemí, kde implementátoři posouvají použití nad původně zamýšlený rozsah.

To se odráží také v celkové architektuře systému. Vzhledem k tomu, že rozšiřující se funkce DHIS2 snižuje nutnost zavádění nebo údržby jiných specializovaných systémů, počet potenciálních datových rozhraní klesá. Tato **snížená složitost** v architektuře systému je jistě výhodou pro Health System s omezenými zdroji.

Již několik let DHIS2 organicky rozšiřuje své aktivity v oblasti správy dat, což umožňuje skutečnému použití vést k někdy nepředvídaným řešením. Existují však také limity, kde se využití DHIS2 jeví jako užitečné. V následujících částech budou popsány speciální systémy.

### Správa logistiky { #lm }

**a) Úvod**

Systémy pro správu logistiky **(LMIS)** nebo systémy pro řízení dodavatelského řetězce **(SCM)** slouží k nahrazení papírových systémů za účelem zvýšení standardizace, transparentnosti, včasnosti nákupu, efektivity, bezpečnosti, efektivity nákladů a snížení odpadu. Národní SCMS / LMIS mohou pokrývat takové funkce, jako je plánování komodit, rozpočtování, nákup, skladování, distribuce a doplňování základních léků a spotřebního materiálu.

**b) Implementace LMIS v DHIS2**

Dodavatelské řetězce lze často dobře ovládat pouze souhrnnými údaji, pokud jsou údaje poskytovány spolehlivě ze všech příslušných úrovní a sledovány. Hlavní indikátory příjmu, spotřeby a stavu zásob na konci období lze zvládnout bez elektronických transakcí a často postačují k získání celkového obrazu, což snižuje potřebu systémových investic. Jako rychle se rozvíjející platforma přidává DHIS2 v posledních letech mnoho funkcí, zejména v DHIS2 Tracker. V současné době jsou k dispozici následující hlavní funkce:

- Formulář pro zadávání dat odrážející široce používaný papírový formulář Report and Requisition (R & R). Zadávání dat pomocí zařízení je možné prostřednictvím stolního prohlížeče nebo mobilní aplikace, a to i v režimu offline. V online režimu může formulář vypočítat návrhy žádostí a nabídnout správci zařízení, aby požadavek upravil a komentoval jej. Tyto elektronické formuláře mohou zaměstnanci vyplňovat na základě papírových karet, které jsou obvykle umístěny vedle komodity ve skladišti.

- DHIS2 pak může vytvářet zprávy pro centrální rozhodování, což dává správcům komodit a programů možnost přijímat nebo upravovat návrhy doručení.

- Skladové údaje lze transformovat do logistických indikátorů, které lze uvést do kontextu s dalšími indikátory programu, například křížové odkazy na počet pacientů léčených specifickou patologií a odpovídající spotřebu léků.

**c) Možnosti interoperability**

LMIS je oblast, kde lze v jedné zemi najít množství paralelních, překrývajících se nebo konkurenčních softwarových řešení. Jak bylo zjištěno ve studii JSI z roku 2012 (Ghana Ministry of Health, July 2013: Landscape Analysis of Supply Chain Management Tools in Use), bylo dokumentováno osmnáct (18\!) různých softwarových nástrojů, které se používají v rámci dodavatelského řetězce veřejného zdraví jen v samotné Ghaně.

Ačkoli vás základní konfigurace LMIS založená na agregovaných datech může dostat velmi daleko, v některých případech je transakční LMIS nezbytný, pokud potřebujete sledovat takové podrobné operace jako vrácení, přenos mezi zařízeními, čtení čárových kódů, dávkování a vypršení platnosti. Také některé specializované funkce řídícího pracoviště, jako je vytváření prognóz, doplňování a zpracování kontrolních zpráv, se často provádějí ve specializovaných nástrojích.

DHIS2 má integrovaná agregovaná data z externích systémů, jako jsou openLMIS a CommCare, prostřednictvím automatizovaných datových rozhraní. Výsledkem je, že skladová data jsou k dispozici ve sdílených ovládacích panelech, zobrazujících zdravotní služby a skladová data vedle sebe.
