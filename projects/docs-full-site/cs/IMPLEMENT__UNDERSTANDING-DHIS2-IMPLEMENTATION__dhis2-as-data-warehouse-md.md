---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/dhis2-as-data-warehouse.md"
revision_date: "2021-06-14"
---

# DHIS2 jako datový sklad { #dhis2-as-data-warehouse }

Tato kapitola pojednává o roli a místě aplikace DHIS2 v kontextu architektury systému. Ukáže, že DHIS2 může sloužit jak pro datový sklad, tak pro operační systém.

## Datové sklady a operační systémy { #data-warehouses-and-operational-systems }

_Datový sklad_ se běžně chápe jako databáze používaná pro analýzu. Typicky se data nahrávají z různých provozních / transakčních systémů. Před načtením dat do datového skladu obvykle procházejí různými fázemi, kde jsou vyčištěny z důvodu anomálií a redundance a transformovány tak, aby odpovídaly celkové struktuře integrované databáze. Data jsou poté zpřístupněna pro použití analýzou, také známá pod pojmy jako *data mining* a _online analytical processing_. Návrh datového skladu je optimalizován pro rychlost načítání a analýzy dat. Pro zlepšení výkonu je datové úložiště často nadbytečné v tom smyslu, že data jsou uložena jak ve své nejpodrobnější podobě, tak v agregované (souhrnné) formě.

_Transakční systém_ (nebo _operační systém_ z pohledu datového skladu) je systém, který shromažďuje, ukládá a upravuje data na nízké úrovni. Tento systém se obvykle používá pro každodenní zadávání a ověřování údajů. Design je optimalizován pro rychlé vkládání a aktualizaci výkonu.

![](resources/images/implementation_guide/data_warehouse.png)

Údržba datového skladu má několik výhod, z nichž některé jsou:

- _Konzistence:_ Poskytuje společný datový model pro všechna relevantní data a funguje jako abstrakce nad potenciálně vysokým počtem zdrojů dat a napájecích systémů, což výrazně usnadňuje provádění analýzy.

- _Reliability:_ Je oddělena od zdrojů, ze kterých data pocházejí, a proto není ovlivněna, pokud jsou data v operačních systémech vymazána nebo ztracena.

- _Analyzační výkon:_ Je navržen pro maximální výkon při načítání a analýze dat na rozdíl od operačních systémů, které jsou často optimalizovány pro sběr dat.

S přístupem k datovému skladu však existují také významné výzvy:

- _Vysoké náklady:_ S přesunem dat z různých zdrojů do společného datového skladu jsou spojeny vysoké náklady, zvláště když si operační systémy nejsou podobné povahy. Dlouhodobě existující systémy (označené jako starší systémy) často kladou velká omezení procesu transformace dat.

- _Platnost dat:_ Proces přesunu dat do datového skladu je často složitý, a proto se často neprovádí v pravidelných a včasných intervalech. To pak ponechá uživatelům dat zastaralé a irelevantní údaje, které nejsou vhodné pro plánování a informované rozhodování.

Kvůli zmíněným výzvám je v poslední době stále populárnější sloučit funkce datového skladu a operačního systému, a to buď do jednoho systému, který plní oba úkoly, nebo s úzce integrovanými systémy hostovanými společně. S tímto přístupem systém poskytuje funkce pro sběr a ověřování dat, jakož i analýzu dat a spravuje proces převodu nízkoúrovňových atomových dat na agregovaná data vhodná pro analýzu. Toto nastavuje vysoké standardy pro systém a jeho design, protože musí poskytovat odpovídající výkon pro obě tyto funkce; pokrok v hardwaru a paralelním zpracování však takový přístup stále více umožňuje.

V tomto ohledu je aplikace DHIS2 navržena tak, aby sloužila jako nástroj pro sběr, ověřování, analýzu a prezentaci dat. Poskytuje moduly pro všechny zmíněné aspekty, včetně funkčnosti zadávání dat a široké řady analytických nástrojů, jako jsou sestavy, grafy, mapy, kontingenční tabulky a ovládací panel.

DHIS2 je navíc součástí sady interoperabilních zdravotnických informačních systémů, které pokrývají širokou škálu potřeb a jsou veškerým open-source softwarem. DHIS2 implementuje standard pro výměnu dat a metadat v oblasti zdraví zvaný SDMX-HD. Existuje mnoho příkladů operačních systémů, které také implementují tento standard a mohou potenciálně přenášet data do DHIS2:

- iHRIS: Systém pro správu údajů o lidských zdrojích. Příklady údajů, které jsou relevantní pro národní datový sklad zachycený tímto systémem, jsou „počet lékařů“, „počet sester“ a „celkový počet zaměstnanců“. Tato data je zajímavé porovnat například s výkonem okresu.

- OpenMRS: Systém lékařských záznamů používaný v nemocnici. Tento systém může potenciálně agregovat a exportovat údaje o nemocnicích lůžkových pacientů do národního datového skladu.

- OpenELIS: Laboratorní podnikový informační systém. Tento systém může generovat a exportovat údaje o počtu a výsledcích laboratorních testů.

![](resources/images/implementation_guide/dhis_data_warehouse.png)

## Strategie agregace v DHIS2 { #aggregation-strategy-in-dhis2 }

Analytické nástroje v DHIS2 načítají agregovaná data z tabulek _data mart_. Datový trh je úložiště dat optimalizované pro splnění nejběžnějších požadavků uživatelů na analýzu dat. Datový trh DHIS2 obsahuje data agregovaná v *prostorové dimenzi* (hierarchie organizační jednotky), _časové dimenzi_ (více období) a pro _indikátorové vzorce_ (matematické výrazy včetně datových prvků). Načítání dat přímo z datových trhů poskytuje dobrý výkon i v prostředích s vysokou souběžností, protože většinu požadavků na analýzu lze uspokojit jediným jednoduchým databázovým dotazem proti datovému trhu. Agregační modul v DHIS2 je schopen zpracovávat nízkoúrovňová data v milionech a spravovat většinu databází na národní úrovni a lze říci, že poskytuje _přístup téměř v reálném čase_ k agregovaným datům.

DHIS2 umožňuje nastavení naplánovaných agregačních úkolů, které obvykle každou noc obnoví a naplní datový trh agregovanými daty. Můžete si vybrat mezi agregací dat za posledních 12 měsíců každou noc nebo agregací dat za posledních 6 měsíců každou noc a posledních 6 až 12 měsíců každou sobotu. Naplánované úlohy lze konfigurovat v části „Plánování“ v modulu „Správa dat“. Rovněž je možné provádět libovolné úlohy datových trhů v části „Datový trh“ v modulu „Zprávy“.

## Přístup k ukládání dat { #data-storage-approach }

Existují dva hlavní přístupy k ukládání dat v datovém skladu, a to přístup _normalized_ a _dimensional_. DHIS2 půjčuje trochu od prvního, ale většinou od druhého. V dimenzionálním přístupu jsou data rozdělena na _dimensions_ a _facts_. Fakta obecně odkazují na transakční číselná data, zatímco dimenze jsou referenční data, která dávají datům kontext a význam. Přísná pravidla tohoto přístupu usnadňují uživatelům pochopit strukturu datového skladu a zajišťují dobrý výkon, protože k vytvoření smysluplné analýzy je nutné zkombinovat několik tabulek, zatímco na druhé straně by systém mohl být méně flexibilní a obtížnější změnit.

V DHIS2 fakta odpovídají objektu datové hodnoty v datovém modelu. Hodnota dat zachycuje data jako čísla, ano / ne nebo text. _Povinné dimenze_, které dávají význam faktům, jsou _datový prvek_, _hierarchie organizačních jednotek_ a _období_ dimenze. Tyto dimenze jsou označovány jako povinné, protože musí být poskytnuty pro všechny uložené datové záznamy. DHIS2 má také vlastní dimenzionální model, který umožňuje reprezentovat jakýkoli druh rozměrnosti. Tento model musí být definován před sběrem dat. DHIS2 má také flexibilní model skupin a skupinových sad, který umožňuje přidat vlastní dimenzi k povinným dimenzím poté, co proběhne sběr dat. Více o dimenzi v DHIS2 se dočtete v kapitole se stejným názvem.

![](resources/images/implementation_guide/dimensional_approach.png)
