---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/conceptual-design-principles.md"
revision_date: "2021-06-14"
---

# Zásady koncepčního návrhu { #conceptual-design-principles }

Tato kapitola poskytuje úvod k některým klíčovým principům koncepčního designu, které stojí za softwarem DHIS2. Porozumění těmto zásadám a jejich znalost pomůže implementátorovi lépe využívat software při přizpůsobování místní databáze. Zatímco tato kapitola představuje principy, následující kapitoly budou podrobně popisovat, jak se tyto principy promítají do procesu návrhu databáze.

V této kapitole budou představeny následující principy koncepčního návrhu:

- Všechna metadata lze přidávat a upravovat prostřednictvím uživatelského rozhraní

- Flexibilní datový model podporuje různé zdroje dat, které mají být integrovány do jednoho datového úložiště

- Vstup dat \!= Výstup dat

- Analýza a podávání zpráv na základě indikátorů

- Udržujte v databázi rozčleněná data zařízení

- Podpora analýzy dat na jakékoli úrovni ve zdravotním systému

V následující části je každý princip popsán podrobněji.

## Všechna metadata lze přidávat a upravovat prostřednictvím uživatelského rozhraní { #all-meta-data-can-be-added-and-modified-through-the-user-interface }

Aplikace DHIS2 přichází se sadou obecných nástrojů pro sběr, ověřování, vykazování a analýzu dat, ale obsah databáze, např. jaká data se mají shromažďovat, odkud pocházejí a na jakém formátu budou záviset na kontextu použití. Tyto metadata je třeba před použitím naplnit do aplikace, což lze provést prostřednictvím uživatelského rozhraní a nevyžaduje žádné programování. To umožňuje přímější zapojení doménových odborníků, kteří rozumějí podrobnostem HIS, které software bude podporovat.

Software odděluje klíčová metadata, která popisují nezpracovaná data uložená v databázi, což jsou kritická metadata, která by se neměla v průběhu času příliš měnit (aby nedošlo k poškození dat), a meta jako indikátory na vyšší úrovni, pravidla ověřování , a skupiny pro agregaci, stejně jako různá rozvržení pro sběrné formuláře a sestavy, které nejsou tak kritické a lze je v průběhu času změnit bez zásahu do nezpracovaných dat. Jelikož lze tato metadata vyšší úrovně přidávat a upravovat v průběhu času bez zásahu do nezpracovaných dat, je podporován nepřetržitý proces přizpůsobení. Typicky se nové funkce přidávají v průběhu času, když se místní implementační tým naučí zvládat více funkcí a uživatelé postupně prosazují pokročilejší analýzu dat a výstupy hlášení.

## Flexibilní datový model podporuje různé zdroje dat, které mají být integrovány do jednoho datového úložiště { #a-flexible-data-model-supports-different-data-sources-to-be-integrated-in-one-single-data-repository }

Návrh DHIS2 sleduje integrovaný přístup k HIS a podporuje integraci mnoha různých zdrojů dat do jedné databáze, někdy označované jako integrované úložiště dat nebo datový sklad.

Skutečnost, že DHIS2 je nástroj podobný kostře bez předdefinovaných formulářů nebo zpráv, znamená, že může podporovat mnoho různých agregovaných zdrojů dat. Neexistuje nic, co by použití omezovalo pouze na oblast zdraví, ačkoli použití v jiných sektorech je stále velmi omezené. Pokud jsou data shromažďována orgunitem (organizační jednotkou), která je popsána jako datový prvek (případně s některými kategoriemi rozčlenění) a lze je reprezentovat předdefinovanou periodou, lze je shromažďovat a zpracovávat v DHIS2. Díky této flexibilitě je DHIS2 mocným nástrojem pro nastavení integrovaných systémů, které spojují nástroje pro sběr, indikátory a zprávy z různých zdravotnických programů, oddělení nebo iniciativ. Jakmile jsou data definována a poté shromážděna nebo importována do databáze DHIS2, mohou být analyzována v korelaci s jakýmikoli jinými daty ve stejné databázi, bez ohledu na to, jak a kým byla shromážděna. Kromě podpory integrované analýzy a vykazování dat tento integrovaný přístup také pomáhá racionalizovat sběr dat a omezit duplikaci.

## Vstup dat \!= Výstup dat { #data-input-data-output }

V DHIS2 existují tři dimenze, které popisují agregovaná data shromažďovaná a uložená v databázi; kde - organizační jednotka, co - datový prvek a kdy - období. Organizační jednotka, datový prvek a období tvoří tři základní dimenze, které jsou potřebné k popisu jakékoli datové hodnoty v DHIS2, ať už ve formě sběru dat, grafu, na mapě nebo v agregované souhrnné sestavě. Když jsou data shromažďována v elektronickém formuláři pro zadávání dat, někdy prostřednictvím zrcadlového obrazu papírových formulářů používaných na úrovni zařízení, každé vstupní pole ve formuláři lze popsat pomocí těchto tří dimenzí. Samotný formulář je pouze nástrojem k organizaci sběru dat a nepopisuje jednotlivé hodnoty dat, které jsou shromažďovány a ukládány do databáze. Schopnost samostatně popsat každou hodnotu dat prostřednictvím definice datového prvku (např. „Dávky spalniček podané <1 rok“) poskytuje důležitou flexibilitu při zpracování, ověřování a analýze dat a umožňuje srovnání dat napříč formami sběru a zdravotními programy .

Tento přístup k designu nebo datovému modelu odděluje DHIS2 od mnoha tradičních softwarových aplikací HIS, které považují formuláře pro sběr dat za klíčovou jednotku analýzy. To je typické pro systémy šité na míru potřebám vertikálních programů a tradiční konceptualizaci sběrných formulářů, která je rovněž zprávou nebo výstupem analýzy. Níže uvedený obrázek ukazuje, jak se liší jemnější design DHIS2 postavený na konceptu datových prvků a jak je vstup (sběr dat) oddělen od výstupu (analýza dat), což podporuje flexibilnější a rozmanitější analýzu a šíření dat. Datový prvek „Dávky spalniček podané <1 rok“ se shromažďuje jako součást formuláře pro sběr dětské imunizace, ale lze jej použít jednotlivě k vytvoření indikátoru (vzorce) s názvem „Pokrytí spalniček <1 rok“, kde je kombinován datový prvek s názvem „Populace \<1 rok“, který se shromažďuje prostřednictvím jiného formuláře pro shromažďování. Tuto vypočítanou hodnotu indikátoru lze poté použít při analýze dat v různých nástrojích pro vytváření zpráv v DHIS2, např. sestavy vytvořené na míru s grafy, kontingenčními tabulkami nebo na mapě v modulu GIS.

![](resources/images/implementation_guide/data_input_output.png)

## Analýza a podávání zpráv na základě indikátorů { #indicator-driven-data-analysis-and-reporting }

To, co se výše označuje jako datový prvek, klíčová dimenze, která popisuje, co se shromažďuje, se někdy v jiných nastaveních označuje jako indikátor. V DHIS2 rozlišujeme mezi datovými prvky, které popisují surová data, např. shromažďované počty a indikátory, které jsou založeny na vzorcích a popisují vypočítané hodnoty, např. pokrytí nebo míry výskytu, které se používají pro analýzu dat. Hodnoty indikátorů se neshromažďují jako hodnoty dat (prvků), nýbrž se vypočítávají aplikací na základě vzorců definovaných uživateli. Tyto vzorce jsou tvořeny faktorem (např. 1, 100, 100, 100 000), čitatelem a jmenovatelem, oba dva jsou výrazy založené na jednom nebo více datových prvcích. Např. indikátor „Pokrytí spalničkami \<1 rok“ je definován vzorec s faktorem 100, čitatelem („Dávky spalniček podané dětem do 1 roku“) a jmenovatelem („Cílová populace do 1 roku“). Indikátor „Míra předčasného odchodu DPT1 do DPT3“ je vzorec 100% x („Podané dávky DPT1“ - „Podané dávky DPT3“) / („Podané dávky DPT1“). Tyto vzorce lze přidávat a upravovat prostřednictvím uživatelského rozhraní uživatelem s omezeným zaškolením, protože je jejich nastavení poměrně snadné a nezasahují do datových hodnot uložených v databázi (přidání nebo úprava indikátoru tedy není kritická operace).

Indikátory představují možná nejvýkonnější funkci analýzy dat DHIS2 a všechny nástroje pro podávání zpráv podporují použití indikátorů, např. jak se zobrazuje ve vlastní sestavě na obrázku výše. Schopnost používat údaje o populaci ve jmenovateli umožňuje srovnání zdravotního výkonu napříč geografickými oblastmi s různými cílovými populacemi, což je užitečnější než jen při pohledu na hrubá čísla. Níže uvedená tabulka používá pro různé vakcíny jak hodnoty nezpracovaných dat (Dávky), tak hodnoty indikátorů (Cov). Porovnávání např. dvě první organizační jednotky v seznamu, Taita Taveta County a Kilifi County, na imunizaci DPT-1, vidíme, že zatímco surová čísla (659 vs 2088) naznačují, že v Kilifi je podáno mnohem více dávek, míra pokrytí (92,2% vs. 47,5%) ukazují, že Taita Taveta dělá lepší práci při imunizaci své cílové populace do 1 roku. Při pohledu na poslední sloupec (Immuniz. Compl. %), Který označuje úplnost hlášení imunizačního formuláře za stejné období, vidíme, že čísla jsou víceméně stejná ve dvou srovnávaných krajích, což nám říká, že míry pokrytí lze rozumně porovnat v obou dvou krajích.

![](resources/images/implementation_guide/indicator_report.png)

## Udržujte v databázi rozčleněná data zařízení { #maintain-disaggregated-facility-data-in-the-database }

Když jsou data shromážděna a uložena v DHIS2, zůstanou v databázi rozčleněna se stejnou úrovní podrobností, jako byla shromážděna. To je hlavní výhoda toho, že máme databázový systém pro NIS, jak se předpokládá v papírovém nebo dokonce tabulkovém systému. Systém je navržen tak, aby ukládal velké množství dat a vždy umožňoval procházení podrobností na nejjemnější možnou úroveň podrobností, která je omezena pouze tím, jak byla data shromážděna nebo importována do databáze DHIS2. Z pohledu národního NIS je žádoucí udržovat data rozčleněná podle úrovně zdravotnických zařízení, což je často nejnižší úroveň v hierarchii organizačních jednotek. Toho lze dosáhnout i bez počítačového zpracování této úrovně prostřednictvím hybridního systému papíru a počítače. Údaje lze předávat ze zdravotnických zařízení např. okresní úřady v papírové podobě (např. na měsíčních souhrnných formulářích pro jedno konkrétní zařízení) a poté na okresním úřadu zadávají všechna data zařízení do DHIS2 prostřednictvím formulářů pro elektronický sběr dat, po jednom zařízení. To umožní týmům pro správu zdraví v okresech provádět analýzu dat podle zařízení a např. poskytovat výtisky zpětnovazebních zpráv generovaných DHIS2, vč. srovnání zařízení s poplatky za zařízení v jejich okrese.

## Podpora analýzy dat na jakékoli úrovni ve zdravotním systému { #support-data-analysis-at-any-level-in-the-health-system }

Zatímco název DHIS2 označuje zaměření na oblast, aplikace poskytuje stejné nástroje a funkce na všech úrovních zdravotního systému. Ve všech nástrojích pro vytváření přehledů si uživatelé mohou vybrat, která org. jednotka nebo úroveň org jednotek se mají analyzovat, a zobrazená data se automaticky agregují až na vybranou úroveň. DHIS2 používá hierarchii org jednotek při agregaci dat směrem nahoru a poskytuje data libovolné org. jednotce v této hierarchii. Většina sestav je spuštěna takovým způsobem, že uživatelé budou vyzváni k výběru org jednotky a tím k opětovnému použití stejných rozvržení sestav pro všechny úrovně. Nebo je-li to žádoucí, lze rozvržení sestavy přizpůsobit na jakoukoli konkrétní úroveň ve zdravotním systému, pokud se potřeby mezi jednotlivými úrovněmi liší.

V modulu GIS mohou uživatelé analyzovat data např. subnárodní úroveň a poté kliknutím na mapu (např. v regionu nebo kraji) přejít na další úroveň a takto pokračovat až ke zdroji dat na úrovni zařízení. Podobné funkce rozbalení jsou k dispozici v kontingenčních tabulkách aplikace Excel, které jsou propojeny s databází DHIS2.

Aby se urychlil výkon a snížila doba odezvy při poskytování agregovaných datových výstupů, které mohou zahrnovat mnoho výpočtů (např. přidání najednou 8000 zařízení), DHIS2 předpočítá všechny možné agregované hodnoty a uloží je do takzvaného datového trhu. Tento datový trh lze naplánovat tak, aby běžel (re-built) v daném časovém intervalu, např. každou noc.
