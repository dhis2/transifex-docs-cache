---
revision_date: "2021-09-15"
template: single.html
---

# Stručný průvodce implementací DHIS2 { #a-quick-guide-to-dhis2-implementation }

Jakákoli implementace okresního zdravotnického informačního softwaru (DHIS2) by se měla zaměřit na vytvoření udržitelných systémů, které jsou flexibilní pro měnící se potřeby ve zdravotnictví. Je důležité si uvědomit, že to bude trvat mnoho let, s nepřetržitými strukturami pro budování kapacit, sdílení osvědčených postupů a inovace. Tento rychlý průvodce poskytne velmi hrubý přehled o různých aspektech implementace DHIS2.

## Plánování a organizace { #planning-and-organizing }

### Potřebné struktury { #structures-needed }

- Ke správě národního HMIS bude zapotřebí základního týmu DHIS (DCT) se 4-5 osobami. Jejich povinnosti a požadované dovednosti by měly být jasně definovány. DCT se bude účastnit akademií DHIS2, organizovat školení a podporu koncových uživatelů pro různé skupiny uživatelů v zemi.

- K řízení koordinace mezi zdravotními programy, dalšími informačními systémy a rozvojovými partnery a univerzitami bude zapotřebí technický řídící výbor nebo ekvivalentní výbor. Budou vést integrační úsilí a rozhodovat o celkové architektuře informačních systémů.

### Integrační úsilí { #integration-efforts }

- V průběhu implementace je třeba vyvíjet současné úsilí o integraci informačního systému a výměnu dat. Hlavní zásadou této práce by mělo být vytvoření systému zaměřeného na rozhodování a zaměřeného na indikátory.

### Vybavení a internet { #equipment-and-internet }

- Je třeba posoudit stanovení potřeb hardwaru. Stolní počítače, notebooky, tablety, mobilní telefony mají různé kvality a obvykle bude třeba podporovat kombinaci těchto různých technologií.

- Je třeba kriticky posoudit alternativy serverů a hostování, pokud jde o kapacitu, infrastrukturní omezení, právní rámec, otázky bezpečnosti a důvěrnosti.

- Bude potřeba připojení k internetu pro všechny uživatele. Mobilní internet bude vhodný pro většinu uživatelů provádějících sběr dat a pravidelnou analýzu.

- Pokud je to vhodné, měly by být prozkoumány možnosti pro uživatele mobilních telefonů, hromadné SMS zprávy atd.

### Zaváděcí strategie { #roll-out-strategy }

- DCT zde bude hrát klíčovou roli a každý člen by měl mít jasnou odpovědnost za zavádění: uživatelská podpora, školení uživatelů, spolupráce se zdravotními programy atd.

- Je třeba vytvořit širší podpůrné struktury, které budou poskytovat podporu, dohled a komunikaci s globální / regionální sítí expertních uživatelů a vývojářů.

- Využití informací musí být od začátku oblastí zájmu a musí být součástí jak počátečního návrhu systému, tak prvního kola školení uživatelů. Sběr dat a kvalita dat se zvýší pouze se skutečnou hodnotou informací. Zasedání okresní revize a obdobná opatření by měla být podporována vhodnými informačními produkty a školením.

- Školení bude obvykle největší investicí v čase a vyžaduje struktury pro nepřetržité příležitosti. Naplánujte dlouhodobý tréninkový přístup zajišťující nepřetržitý proces umožnění novým uživatelům a novým funkcím systému.

- Dohled a hodnocení kvality údajů by měly být prováděny často.

## Přizpůsobení DHIS2 { #adapting-dhis2 }

### Rozsah systému { #scope-of-system }

- Na základě rozhodnutí, která by měl systém podporovat (rozsah systému); pro agregaci, trasovač a / nebo události DHIS2 bude potřeba úpravy a přizpůsobení platformy. Každá akce bude vyžadovat zvláštní kompetence a měla by být vedena DCT.

- Je zapotřebí posouzení zamýšlených uživatelů a příjemců, například pokud jde o jejich informační potřeby a hardwarové a síťové potřeby.

- Je důležité porozumět širší architektuře HIS („ekosystém HIS“); jaké další systémy existují a jak by měly interagovat s DHIS2? Zvažte, jaké budou potřeby interoperability mezi elektronickými systémy.

- Pokud existují potřeby, které DHIS2 aktuálně nepodporuje, je nutné posouzení dalšího vývoje softwaru. Lze je řešit lokálně vývojem vlastní webové aplikace nebo vstupem do procesu celkového plánu vývoje základní platformy organizovaného UiO.

### Nastavení DHIS2 { #setting-up-dhis2 }

- Zpravodajské jednotky: implementace různých zpravodajských jednotek (poskytovatelů služeb) a hierarchií, včetně seskupení.

- Potřeby shromažďování údajů: Které indikátory jsou potřebné, jaké datové proměnné budou použity při jejich výpočtu a jak by měla být tato data shromažďována? Navrhujte datové prvky, kategorie rozčlenění, datové sady a formuláře pro sběr.

- Informace k akci (indikátory, ovládací panely, další výstupy): jaké jsou informační produkty, které budou různí uživatelé potřebovat? Tabulky, grafy, mapy, ovládací panely. Rutiny pro šíření a sdílení.

- Správa uživatelů: Vytvářejte uživatelské role a skupiny, rutiny pro správu uživatelů, definujte přístup k funkcím a vhodné sdílení obsahu.

- Dokument správy DHIS2 (role podle profilu, jak změnit metadata a za jakých podmínek).

### Hostování { #hosting }

- Existuje mnoho různých možností hostování online systému, a to jak z hlediska umístění serveru (např. In-house vs. cloud), tak i toho, kdo má server spravovat (např. In-house vs. outsourcing). Je třeba kriticky posoudit alternativy serverů a hostování, pokud jde o kapacitu, infrastrukturní omezení, právní rámec, otázky bezpečnosti a důvěrnosti. Tato rozhodnutí bude možná nutné revidovat alespoň jednou ročně, protože se časem může změnit složitost serveru, datové typy (např. agregát vs. pacient) a místní kapacita.

## Budování kapacit { #capacity-building }

### DHIS core tým (DCT) { #dhis-core-team-dct }

- DCT bude potřebovat všechny dovednosti nezbytné pro udržitelný a vyvíjející se systém. To zahrnuje technické dovednosti (přizpůsobení DHIS2, údržba serveru), znalosti systému (architektury a principy návrhu), organizační (integrační strategie) a řízení projektu (organizování strukturované podpory a školení).

- Členové DCT by se měli pravidelně (např. dvakrát ročně) účastnit regionální / globální akademie DHIS2, aby zajistili vysoce kvalitní školení, nepřetržitou komunikaci s širší komunitou odborníků a zajistili, aby byl místní tým aktuální s novými funkcemi a vylepšeními v posledních verzích platformy DHIS 2. DCT bude odpovědné za přizpůsobení a kaskádování tohoto regionálního vzdělávacího programu pro širší skupinu uživatelů v dané zemi.

### Strategie pro výcvik v dané zemi { #country-training-strategies }

- DCT by měla nabízet školení v souvislosti s implementací a nepřetržitě poté, aby vyhověla rostoucím požadavkům, aktualizacím systému a fluktuaci zaměstnanců.

- Přizpůsobení a vývoj školicích materiálů a referenčních příruček tak, aby odrážely potřeby místních informací a obsah místního systému, je důležité.

### Příležitosti dalšího vzdělávání { #continuous-training-opportunities }

- Jak uživatelská zkušenost roste, mělo by být nabízeno pokročilejší školení. Školení o používání informací pro okresní lékaře a manažery zdravotnických programů je zásadní již brzy, aby se zúčastněné strany mohly zapojit do využívání informací při rozhodování.

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

![](resources/images/data_input_output.png)

## Analýza a podávání zpráv na základě indikátorů { #indicator-driven-data-analysis-and-reporting }

To, co se výše označuje jako datový prvek, klíčová dimenze, která popisuje, co se shromažďuje, se někdy v jiných nastaveních označuje jako indikátor. V DHIS2 rozlišujeme mezi datovými prvky, které popisují surová data, např. shromažďované počty a indikátory, které jsou založeny na vzorcích a popisují vypočítané hodnoty, např. pokrytí nebo míry výskytu, které se používají pro analýzu dat. Hodnoty indikátorů se neshromažďují jako hodnoty dat (prvků), nýbrž se vypočítávají aplikací na základě vzorců definovaných uživateli. Tyto vzorce jsou tvořeny faktorem (např. 1, 100, 100, 100 000), čitatelem a jmenovatelem, oba dva jsou výrazy založené na jednom nebo více datových prvcích. Např. indikátor „Pokrytí spalničkami \<1 rok“ je definován vzorec s faktorem 100, čitatelem („Dávky spalniček podané dětem do 1 roku“) a jmenovatelem („Cílová populace do 1 roku“). Indikátor „Míra předčasného odchodu DPT1 do DPT3“ je vzorec 100% x („Podané dávky DPT1“ - „Podané dávky DPT3“) / („Podané dávky DPT1“). Tyto vzorce lze přidávat a upravovat prostřednictvím uživatelského rozhraní uživatelem s omezeným zaškolením, protože je jejich nastavení poměrně snadné a nezasahují do datových hodnot uložených v databázi (přidání nebo úprava indikátoru tedy není kritická operace).

Indikátory představují možná nejvýkonnější funkci analýzy dat DHIS2 a všechny nástroje pro podávání zpráv podporují použití indikátorů, např. jak se zobrazuje ve vlastní sestavě na obrázku výše. Schopnost používat údaje o populaci ve jmenovateli umožňuje srovnání zdravotního výkonu napříč geografickými oblastmi s různými cílovými populacemi, což je užitečnější než jen při pohledu na hrubá čísla. Níže uvedená tabulka používá pro různé vakcíny jak hodnoty nezpracovaných dat (Dávky), tak hodnoty indikátorů (Cov). Porovnávání např. dvě první organizační jednotky v seznamu, Taita Taveta County a Kilifi County, na imunizaci DPT-1, vidíme, že zatímco surová čísla (659 vs 2088) naznačují, že v Kilifi je podáno mnohem více dávek, míra pokrytí (92,2% vs. 47,5%) ukazují, že Taita Taveta dělá lepší práci při imunizaci své cílové populace do 1 roku. Při pohledu na poslední sloupec (Immuniz. Compl. %), Který označuje úplnost hlášení imunizačního formuláře za stejné období, vidíme, že čísla jsou víceméně stejná ve dvou srovnávaných krajích, což nám říká, že míry pokrytí lze rozumně porovnat v obou dvou krajích.

![](resources/images/indicator_report.png)

## Udržujte v databázi rozčleněná data zařízení { #maintain-disaggregated-facility-data-in-the-database }

Když jsou data shromážděna a uložena v DHIS2, zůstanou v databázi rozčleněna se stejnou úrovní podrobností, jako byla shromážděna. To je hlavní výhoda toho, že máme databázový systém pro NIS, jak se předpokládá v papírovém nebo dokonce tabulkovém systému. Systém je navržen tak, aby ukládal velké množství dat a vždy umožňoval procházení podrobností na nejjemnější možnou úroveň podrobností, která je omezena pouze tím, jak byla data shromážděna nebo importována do databáze DHIS2. Z pohledu národního NIS je žádoucí udržovat data rozčleněná podle úrovně zdravotnických zařízení, což je často nejnižší úroveň v hierarchii organizačních jednotek. Toho lze dosáhnout i bez počítačového zpracování této úrovně prostřednictvím hybridního systému papíru a počítače. Údaje lze předávat ze zdravotnických zařízení např. okresní úřady v papírové podobě (např. na měsíčních souhrnných formulářích pro jedno konkrétní zařízení) a poté na okresním úřadu zadávají všechna data zařízení do DHIS2 prostřednictvím formulářů pro elektronický sběr dat, po jednom zařízení. To umožní týmům pro správu zdraví v okresech provádět analýzu dat podle zařízení a např. poskytovat výtisky zpětnovazebních zpráv generovaných DHIS2, vč. srovnání zařízení s poplatky za zařízení v jejich okrese.

## Podpora analýzy dat na jakékoli úrovni ve zdravotním systému { #support-data-analysis-at-any-level-in-the-health-system }

Zatímco název DHIS2 označuje zaměření na oblast, aplikace poskytuje stejné nástroje a funkce na všech úrovních zdravotního systému. Ve všech nástrojích pro vytváření přehledů si uživatelé mohou vybrat, která org. jednotka nebo úroveň org jednotek se mají analyzovat, a zobrazená data se automaticky agregují až na vybranou úroveň. DHIS2 používá hierarchii org jednotek při agregaci dat směrem nahoru a poskytuje data libovolné org. jednotce v této hierarchii. Většina sestav je spuštěna takovým způsobem, že uživatelé budou vyzváni k výběru org jednotky a tím k opětovnému použití stejných rozvržení sestav pro všechny úrovně. Nebo je-li to žádoucí, lze rozvržení sestavy přizpůsobit na jakoukoli konkrétní úroveň ve zdravotním systému, pokud se potřeby mezi jednotlivými úrovněmi liší.

V modulu GIS mohou uživatelé analyzovat data např. subnárodní úroveň a poté kliknutím na mapu (např. v regionu nebo kraji) přejít na další úroveň a takto pokračovat až ke zdroji dat na úrovni zařízení. Podobné funkce rozbalení jsou k dispozici v kontingenčních tabulkách aplikace Excel, které jsou propojeny s databází DHIS2.

Aby se urychlil výkon a snížila doba odezvy při poskytování agregovaných datových výstupů, které mohou zahrnovat mnoho výpočtů (např. přidání najednou 8000 zařízení), DHIS2 předpočítá všechny možné agregované hodnoty a uloží je do takzvaného datového trhu. Tento datový trh lze naplánovat tak, aby běžel (re-built) v daném časovém intervalu, např. každou noc.

# Nastavení nové databáze { #setting-up-a-new-database }

Aplikace DHIS2 přichází se sadou nástrojů pro sběr, ověřování, hlášení a analýzu dat, ale obsah databáze, např. jaká data se mají shromažďovat, odkud data pocházejí a jaký formát bude záviset na kontextu použití. Tyto metadata je třeba před použitím naplnit do aplikace, což lze provést prostřednictvím uživatelského rozhraní a nevyžaduje žádné programování. Vyžadují se důkladné znalosti o místním kontextu HIS a porozumění principům návrhu DHIS2 (viz kapitola „Klíčové principy koncepčního návrhu v DHIS2“). Říkáme tomu počáteční návrh nebo přizpůsobení databáze procesu. Tato kapitola poskytuje přehled procesu přizpůsobení a stručně vysvětluje příslušné kroky, aby měl implementátor pocit, co tento proces vyžaduje. Další kapitoly v této příručce poskytují mnohem podrobnější informace o některých konkrétních krocích.

## Strategie pro začátek { #strategies-for-getting-started }

Následující část popisuje seznam tipů, jak začít dobře při vývoji nové databáze.

1.  Rychle naplňte demo databázi, vč. příklady zpráv, grafů, ovládacího panelu, GIS, formulářů pro zadávání dat. Používejte skutečná data, nejlépe celonárodní, ale ne nutně data na úrovni zařízení.

2.  Umístěte demo databázi online. Hostování serveru se serverem externího poskytovatele může být řešením pro urychlení procesu, i když je dočasné. Díky tomu je skvělá platforma pro spolupráci a nástroj pro šíření informací, díky nimž lze získat odkup od zúčastněných stran.

3.  Další fází je propracovanější proces návrhu databáze. Části ukázky lze znovu použít, pokud jsou životaschopné.

4.  Ujistěte se, že máte místní tým s různými dovednostmi a pozadím: veřejné zdraví, správce dat, IT a řízení projektů.

5.  Fázi přizpůsobení a návrh databáze použijte jako proces učení a školení k budování místní kapacity prostřednictvím učení se praxí.

6.  Národní tým by měl řídit proces návrhu databáze, ale měl by být podporován a veden zkušenými implementátory.

## Řízený nebo otevřený proces? { #controlled-or-open-process }

Protože proces přizpůsobení DHIS2 často je a měl by být procesem spolupráce, je také důležité mít na paměti, které části databáze jsou kritičtější než jiné, např. aby se zabránilo neškolenému uživateli poškodit data. Obvykle je mnohem důležitější přizpůsobit databázi, která již má datové hodnoty, než pracovat s metadaty v „prázdné“ databázi. I když by se to mohlo zdát divné, mnoho přizpůsobení proběhne po zahájení prvního sběru nebo importu dat, např. při přidávání nových ověřovacích pravidel, indikátorů nebo rozvržení sestavy. Nejkritičtější chybou, kterou lze udělat, je upravit metadata, která přímo popisují datové hodnoty, a ty, jak jsme viděli výše, jsou _datové prvky_ a _organizační jednotky_. Při úpravách těchto definic je důležité přemýšlet o tom, jak tato změna ovlivní význam datových hodnot již v systému (shromážděných pomocí starých definic). Doporučuje se omezit, kdo může upravovat tato základní metadata prostřednictvím správy rolí uživatelů, a omezit tak přístup k základnímu týmu přizpůsobení.

Ostatní části systému, které nejsou přímo spojeny s datovými hodnotami, jsou mnohem méně důležité pro hraní, a zde, alespoň v raných fázích, je třeba povzbudit uživatele, aby vyzkoušeli nové věci, aby vytvořili učení. To platí pro skupiny, pravidla ověřování, vzorce indikátorů, grafy a sestavy. To vše lze snadno odstranit nebo upravit později, aniž by to ovlivnilo základní hodnoty dat, a proto nejsou v procesu přizpůsobení kritickými prvky.

Samozřejmě, později v procesu přizpůsobení, když přecházíte do produkční fáze, je třeba ještě opatrněji povolit přístup k úpravám různých metadat, protože jakákoli změna, také u méně kritických metadat, může ovlivnit, jak jsou data agregována dohromady nebo prezentovány ve zprávě (ačkoli základní nezpracovaná data jsou stále bezpečná a správná).

## Kroky pro vývoj databáze { #steps-for-developing-a-database }

Následující část popisuje konkrétní kroky pro vývoj databáze od nuly.

### Organizační hierarchie { #the-organisational-hierarchy }

Hierarchie organizace definuje organizaci používající DHIS2, zdravotnická zařízení, administrativní oblasti a další geografické oblasti používané při sběru a analýze dat. Tato dimenze dat je definována jako hierarchie s jednou kořenovou jednotkou (např. Ministerstvo zdravotnictví) a libovolným počtem úrovní a uzlů níže. Každý uzel v této hierarchii se v DHIS2 nazývá organizační jednotka. Návrh této hierarchie určí geografické analytické jednotky, které mají uživatelé k dispozici při shromažďování a agregaci dat v této struktuře. Současně může existovat pouze jedna organizační hierarchie, takže je třeba pečlivě zvážit její strukturu.

Další hierarchie (např. Paralelní administrativní hranice se sektorem zdravotní péče) lze modelovat pomocí organizačních skupin a sad skupin, ale hierarchie organizace je hlavním prostředkem agregace dat v geografické dimenzi. Obvykle mají národní organizační hierarchie v oblasti veřejného zdraví 4-6 úrovní, ale je podporován libovolný počet úrovní. Hierarchie je postavena na vztazích nadřazený-podřazený, např. Jednotka Země nebo Ministerstvo Zdravotnictví (root) může mít např. 8 podřazených jednotek (krajů) a každý kraj (na úrovni 2) může mít jako své podřazené 10-15 okresů. Normálně budou zdravotnická zařízení umístěna na nejnižší úrovni, ale mohou být umístěna také na vyšších úrovních, např. zemské nebo krajské nemocnice, takže jsou podporovány šikmé organizační stromy (např. koncový uzel  lze umístit na úrovni 2, zatímco většina ostatních koncových uzlů je na úrovni 5).

### Datové prvky { #data-elements }

Datový prvek je možná nejdůležitějším stavebním kamenem databáze DHIS2. Představuje dimenzi _co_, vysvětluje, co se shromažďuje nebo analyzuje. V některých kontextech se to označuje jako indikátor, ale v DHIS2 tuto jednotku sběru a analýzy nazýváme datovým prvkem. Datový prvek často představuje počet něčeho a jeho název popisuje, co se počítá, např. „Podané dávky BCG“ nebo „Případy malárie“. Když jsou data shromažďována, ověřována, analyzována, hlášena nebo prezentována, jsou to datové prvky nebo výrazy postavené na datových prvcích, které popisují, jaké jsou údaje. Datové prvky se tak stávají důležitými pro všechny aspekty systému a rozhodují nejen o tom, jak jsou data shromažďována, ale ještě důležitější je, jak jsou hodnoty dat reprezentovány v databázi, která opět rozhoduje o tom, jak lze data analyzovat a prezentovat.

Osvědčeným postupem při navrhování datových prvků je myslet na datové prvky jako na jednotku analýzy dat a ne jen jako na pole ve formuláři shromažďování dat. Každý datový prvek žije sám v databázi, zcela oddělen od formuláře pro sběr a sestavy a další výstupy jsou založeny na datových prvcích a výrazech / vzorcích složených z datových prvků, nikoli na formulářích pro sběr dat. Procesem by tedy měly řídit potřeby analýzy dat, nikoli vzhled a chování formulářů pro sběr dat.

### Datové sady a formuláře pro zadávání údajů { #data-sets-and-data-entry-forms }

Veškeré zadávání dat v DHIS2 je organizováno pomocí datových sad. Datová sada je kolekce datových prvků seskupených dohromady pro sběr dat a v případě distribuovaných instalací také definují bloky dat pro export a import mezi instancemi DHIS2 (např. z místní instalace okresního úřadu na národní server). Datové sady nejsou přímo spojeny s datovými hodnotami, pouze prostřednictvím jejich datových prvků a frekvencí, a jako takové lze datovou sadu upravovat, mazat nebo přidávat kdykoli bez ovlivnění nezpracovaných dat již zachycených v systému, ale například změny samozřejmě ovlivní, jak budou sbírána nová data.

Jakmile přiřadíte datovou sadu organizační jednotce, bude tato datová sada zpřístupněna v Zadávání Dat (v části Služby) pro organizační jednotky, kterým jste ji přiřadili, a pro platná období podle typu období datové sady. Poté se zobrazí výchozí formulář pro zadávání dat, což je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s kategoriemi, jako jsou věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři založeném na kategoriích. Kromě výchozího formuláře pro zadávání údajů založeného na seznamu existují další dvě alternativy, formulář založený na oddílech a vlastní formulář. Formáty oddílů umožňují o něco větší flexibilitu, pokud jde o používání tabulkových formulářů, a jejich design je rychlý a jednoduchý. Formulář pro zadávání dat bude často potřebovat více tabulek s podnadpisy a někdy budete muset deaktivovat (šedě) několik polí v tabulce (např. Některé kategorie se nevztahují na všechny datové prvky), obě tyto funkce jsou podporovány ve formulářích sekcí . Pokud je formulář, který chcete navrhnout, příliš komplikovaný pro výchozí formuláře nebo formuláře oddílů, poslední možností je použít vlastní formulář. To zabere více času, ale dává vám plnou flexibilitu, pokud jde o design. V DHIS2 je integrovaný editor HTML (FcK Editor) pro návrháře formulářů a můžete buď navrhnout formulář v uživatelském rozhraní, nebo přímo vložit do html (pomocí okna Zdroj v editoru.

### Pravidla ověřování { #validation-rules }

Jakmile nastavíte část systému pro zadávání dat a začnete shromažďovat data, je čas definovat kontroly kvality dat, které pomohou zlepšit kvalitu shromažďovaných údajů. Můžete přidat libovolný počet pravidel ověřování, která se skládají z výrazů na levé a pravé straně, které jsou opět složeny z datových prvků, s operátorem mezi oběma stranami. Typická pravidla porovnávají mezisoučty s celkovými součty. Např. pokud máte dva datové prvky „HIV testy provedeny“ a „výsledek testu HIV pozitivní“, pak víte, že ve stejné formě (pro stejné období a organizační jednotku) musí být celkový počet testů vždy stejný nebo vyšší než počet pozitivní testy. Tato pravidla by měla být absolutními pravidly, což znamená, že jsou matematicky správná, nikoli pouze předpoklady nebo „většinou správné“. Pravidla lze spouštět při zadávání dat, po vyplnění každého formuláře nebo jako dávkový proces na více formulářích současně, např. pro všechna zařízení za předchozí vykazovaný měsíc. Výsledky testů zobrazí seznam všech porušení a podrobné hodnoty pro každou stranu výrazu, kde došlo k porušení, aby bylo snadné vrátit se k zadávání dat a opravit hodnoty.

### Indikátory { #indicators }

Indikátory představují pravděpodobně nejvýkonnější funkci analýzy dat DHIS2. Zatímco datové prvky představují hrubá data (počty), které se shromažďují, indikátory představují vzorce poskytující míru pokrytí, míru výskytu, poměry a další analytické jednotky založené na vzorcích. Indikátor je tvořen faktorem (např. 1, 100, 100, 100 000), čitatelem a jmenovatelem, oba dva jsou výrazy založené na jednom nebo více datových prvcích. Např. indikátor „pokrytí BCG \ <1 rok“ je definován vzorec s faktorem 100, čitatelem („dávky BCG dětem do 1 roku“) a jmenovatelem („cílová populace do 1 roku“). Indikátor „Míra předčasného odchodu DPT1 do DPT3“ je vzorec 100% x („Podané dávky DPT1“ - „Podané dávky DPT3“) / („Podané dávky DPT1“).

Většina modulů zpráv v DHIS2 podporuje datové prvky i indikátory a můžete je také kombinovat ve vlastních sestavách, ale důležitým rozdílem a silou indikátorů oproti nezpracovaným datům (hodnoty datových prvků dat) je schopnost porovnávat data napříč různými geografickými oblastmi (např. vysoce osídlené vs venkovské oblasti), protože cílovou populaci lze použít ve jmenovateli.

Indikátory lze přidávat, upravovat a mazat kdykoli bez zásahu do datových hodnot v databázi.

### Tabulky zpráv a reportů { #report-tables-and-reports }

Standardní zprávy v DHIS2 představují velmi flexibilní způsob prezentace shromážděných dat. Data lze agregovat podle jakékoli organizační jednotky nebo úrovně organizace, podle datového prvku, podle indikátorů a také v čase (např. měsíčně, čtvrtletně, ročně). Tabulky sestav jsou vlastní zdroje dat pro standardní sestavy a lze je flexibilně definovat v uživatelském rozhraní a později k nim přistupovat externí návrháři sestav, jako je iReport nebo BIRT. Tyto návrhy sestav lze poté nastavit jako snadno dostupné přehledy na jedno kliknutí s parametry, aby uživatelé mohli spouštět stejné přehledy, např. každý měsíc při zadávání nových údajů a také relevantní pro uživatele na všech úrovních, protože v době spuštění sestavy lze vybrat organizační jednotku.

### GIS (Mapy) { #gis-maps }

V integrovaném modulu GIS můžete snadno zobrazit svá data na mapách, a to jak na polygonech (oblasti), tak jako body (zdravotnická zařízení), a to buď jako datové prvky nebo indikátory. Poskytnutím souřadnic vašich organizačních jednotek do systému to s tímto modulem můžete urychlit. Podrobnosti o tom, jak začít, najdete v části GIS.

### Grafy a ovládací panel { #charts-and-dashboard }

Jedním z nejjednodušších způsobů, jak zobrazit údaje indikátorů, jsou grafy. Snadno použitelný dialogový graf vás provede vytvořením různých typů grafů s údaji o indikátorech, organizačních jednotkách a obdobích podle vašeho výběru. Tyto grafy lze snadno přidat do jedné ze čtyř částí grafu na vašem ovládacím panelu a snadno se zpřístupní hned po přihlášení. Nezapomeňte nastavit modul ovládacího panelu jako spouštěcí modul v uživatelském nastavení.

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

# DHIS2 jako datový sklad { #dhis2-as-data-warehouse }

Tato kapitola pojednává o roli a místě aplikace DHIS2 v kontextu architektury systému. Ukáže, že DHIS2 může sloužit jak pro datový sklad, tak pro operační systém.

## Datové sklady a operační systémy { #data-warehouses-and-operational-systems }

_Datový sklad_ se běžně chápe jako databáze používaná pro analýzu. Typicky se data nahrávají z různých provozních / transakčních systémů. Před načtením dat do datového skladu obvykle procházejí různými fázemi, kde jsou vyčištěny z důvodu anomálií a redundance a transformovány tak, aby odpovídaly celkové struktuře integrované databáze. Data jsou poté zpřístupněna pro použití analýzou, také známá pod pojmy jako *data mining* a _online analytical processing_. Návrh datového skladu je optimalizován pro rychlost načítání a analýzy dat. Pro zlepšení výkonu je datové úložiště často nadbytečné v tom smyslu, že data jsou uložena jak ve své nejpodrobnější podobě, tak v agregované (souhrnné) formě.

_Transakční systém_ (nebo _operační systém_ z pohledu datového skladu) je systém, který shromažďuje, ukládá a upravuje data na nízké úrovni. Tento systém se obvykle používá pro každodenní zadávání a ověřování údajů. Design je optimalizován pro rychlé vkládání a aktualizaci výkonu.

![](resources/images/data_warehouse.png)

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

![](resources/images/dhis_data_warehouse.png)

## Strategie agregace v DHIS2 { #aggregation-strategy-in-dhis2 }

Analytické nástroje v DHIS2 načítají agregovaná data z tabulek _data mart_. Datový trh je úložiště dat optimalizované pro splnění nejběžnějších požadavků uživatelů na analýzu dat. Datový trh DHIS2 obsahuje data agregovaná v *prostorové dimenzi* (hierarchie organizační jednotky), _časové dimenzi_ (více období) a pro _indikátorové vzorce_ (matematické výrazy včetně datových prvků). Načítání dat přímo z datových trhů poskytuje dobrý výkon i v prostředích s vysokou souběžností, protože většinu požadavků na analýzu lze uspokojit jediným jednoduchým databázovým dotazem proti datovému trhu. Agregační modul v DHIS2 je schopen zpracovávat nízkoúrovňová data v milionech a spravovat většinu databází na národní úrovni a lze říci, že poskytuje _přístup téměř v reálném čase_ k agregovaným datům.

DHIS2 umožňuje nastavení naplánovaných agregačních úkolů, které obvykle každou noc obnoví a naplní datový trh agregovanými daty. Můžete si vybrat mezi agregací dat za posledních 12 měsíců každou noc nebo agregací dat za posledních 6 měsíců každou noc a posledních 6 až 12 měsíců každou sobotu. Naplánované úlohy lze konfigurovat v části „Plánování“ v modulu „Správa dat“. Rovněž je možné provádět libovolné úlohy datových trhů v části „Datový trh“ v modulu „Zprávy“.

## Přístup k ukládání dat { #data-storage-approach }

Existují dva hlavní přístupy k ukládání dat v datovém skladu, a to přístup _normalized_ a _dimensional_. DHIS2 půjčuje trochu od prvního, ale většinou od druhého. V dimenzionálním přístupu jsou data rozdělena na _dimensions_ a _facts_. Fakta obecně odkazují na transakční číselná data, zatímco dimenze jsou referenční data, která dávají datům kontext a význam. Přísná pravidla tohoto přístupu usnadňují uživatelům pochopit strukturu datového skladu a zajišťují dobrý výkon, protože k vytvoření smysluplné analýzy je nutné zkombinovat několik tabulek, zatímco na druhé straně by systém mohl být méně flexibilní a obtížnější změnit.

V DHIS2 fakta odpovídají objektu datové hodnoty v datovém modelu. Hodnota dat zachycuje data jako čísla, ano / ne nebo text. _Povinné dimenze_, které dávají význam faktům, jsou _datový prvek_, _hierarchie organizačních jednotek_ a _období_ dimenze. Tyto dimenze jsou označovány jako povinné, protože musí být poskytnuty pro všechny uložené datové záznamy. DHIS2 má také vlastní dimenzionální model, který umožňuje reprezentovat jakýkoli druh rozměrnosti. Tento model musí být definován před sběrem dat. DHIS2 má také flexibilní model skupin a skupinových sad, který umožňuje přidat vlastní dimenzi k povinným dimenzím poté, co proběhne sběr dat. Více o dimenzi v DHIS2 se dočtete v kapitole se stejným názvem.

![](resources/images/dimensional_approach.png)

# DHIS2 jako platforma { #dhis2-as-a-platform }

DHIS2 lze vnímat jako platformu na několika úrovních. Za prvé, aplikační databáze je navržena od základu s ohledem na flexibilitu. Datové struktury, jako jsou datové prvky, organizační jednotky, formuláře a uživatelské role, lze definovat zcela volně prostřednictvím uživatelského rozhraní aplikace. Díky tomu je možné systém přizpůsobit mnoha místním kontextům a případům použití. Viděli jsme, že DHIS2 podporuje většinu hlavních požadavků na rutinní sběr dat a analýzu, které se objevují v implementacích zemí. Umožňuje také DHIS2 sloužit jako systém pro správu domén, jako jsou logistika, laboratoře a finance.

Za druhé, díky modulární konstrukci DHIS2 je možné jej rozšířit o další softwarové moduly. Tyto softwarové moduly mohou žít bok po boku s jádrovými moduly DHIS2 a lze je integrovat do portálu a systému nabídek DHIS2. Jedná se o výkonnou funkci, protože v případě potřeby umožňuje rozšířit systém o další funkce, obvykle pro specifické požadavky dané země, jak již bylo uvedeno výše.

Nevýhodou rozšiřitelnosti softwarového modulu je to, že klade několik omezení na vývojový proces. Vývojáři, kteří vytvářejí další funkce, jsou kromě omezení kladených na návrh modulů portálovým řešením DHIS2 omezeni na technologii DHIS2, pokud jde o programovací jazyk a softwarové rámce. Tyto moduly musí být také zahrnuty do softwaru DHIS2, když je software vytvořen a nasazen na webovém serveru, nikoli dynamicky během běhu.

Za účelem překonání těchto omezení a dosažení volnějšího propojení mezi vrstvou služby DHIS2 a dalšími softwarovými artefakty se vývojový tým DHIS2 rozhodl vytvořit webové rozhraní API. Toto webové rozhraní API odpovídá pravidlům architektonického stylu REST. To znamená, že:

- Webové rozhraní API poskytuje navigovatelné a strojově čitelné rozhraní pro kompletní datový model DHIS2. Například je možné přistupovat k úplnému seznamu datových prvků, poté pomocí zadaného hypertextového odkazu přejít na konkrétní datový prvek, který nás zajímá, a poté pomocí zadaného hypertextového odkazu přejít na seznam formulářů, jejichž je tento datový prvek součástí. Např. klienti budou přechody stavu provádět pouze pomocí hypertextových odkazů, které jsou dynamicky vloženy do odpovědí.

- K datům se přistupuje prostřednictvím jednotného rozhraní (URL) pomocí známého protokolu. Nejsou zapojeny žádné fantastické transportní formáty ani protokoly - pouze dobře otestovaný a dobře srozumitelný protokol HTTP, který je dnes hlavním stavebním kamenem webu. To znamená, že vývojáři třetích stran mohou vyvíjet software pomocí datového modelu a dat DHIS2, aniž by věděli o specifické technologii DHIS2 nebo dodržovali konstrukční omezení DHIS2.

- Veškerá data včetně metadat, zpráv, map a grafů, která jsou v terminologii REST známá jako zdroje, lze načíst ve většině populárních formátů reprezentace dnešního webu, jako jsou HTML, XML, JSON, PDF a PNG. Tyto formáty jsou široce podporovány v aplikacích a programovacích jazycích a poskytují vývojářům třetích stran širokou škálu možností implementace.

![](resources/images/dhis_platform.png)

Existuje několik scénářů, kdy se k webovému rozhraní API DHIS2 mohou připojit další softwarové artefakty.

## Webové portály { #web-portals }

Nejprve mohou být webové portály postaveny na vrcholu webového rozhraní API. Webový portál je v tomto ohledu web, který funguje jako přístupový bod k informacím z potenciálně velkého počtu zdrojů dat, které obvykle sdílejí společné téma. Úlohou webového portálu je zajistit, aby tyto zdroje dat byly snadno přístupné strukturovaným způsobem pod společným dojmem a poskytováním komplexního zobrazení dat pro koncové uživatele.

Úložiště agregovaných dat: Webový portál zaměřený na doménu zdraví může používat DHIS2 jako hlavní zdroj agregovaných dat. Portál se může připojit k webovému API a komunikovat s příslušnými prostředky, jako jsou mapy, grafy, zprávy, tabulky a statické dokumenty. Tyto datové pohledy mohou dynamicky vizualizovat agregovaná data na základě dotazů na dimenzi organizační jednotky, indikátoru nebo období. Portál může přidávat hodnotu k přístupnosti informací několika způsoby. Může být strukturován uživatelsky přívětivým způsobem a zpřístupňovat data nezkušeným uživatelům. Může poskytnout různé přístupy k datům, včetně:

- Tematické - seskupení indikátorů podle tématu. Příklady takových témat jsou očkování, péče o matku, nemoci podléhající hlášení a zdraví životního prostředí.

- Geografické - seskupení údajů podle provincií. To umožní snadné srovnání výkonu a vytížení.

Mash-up: Webový portál se neomezuje pouze na konzumaci dat z jediného webového rozhraní API - lze jej připojit k libovolnému počtu rozhraní API a použít k propojení dat z pomocných systémů v doméně stavu. Pokud je k dispozici, portál může získávat specializovaná data ze sledování logistických systémů a správy léků ARV, z finančních systémů spravujících platby zdravotnickým zařízením a ze laboratorních systémů sledujících laboratorní testy na přenosné nemoci. Data ze všech těchto zdrojů mohou být prezentována uceleným a smysluplným způsobem, aby poskytly lepší přehled o situaci v oblasti zdraví.

Úložiště dokumentů: Webový portál může sám o sobě fungovat jako úložiště dokumentů (označovaný také jako systém správy obsahu). Mohou být nahrány a spravovány příslušné dokumenty, jako jsou publikované zprávy, údaje z průzkumů, roční operační plány a časté dotazy, pokud jde o vlastnictví, kontrolu verzí a klasifikaci. Díky tomu je portál ústředním bodem pro sdílení dokumentů a spolupráci. Díky vzniku vysoce kvalitních řešení open source úložiště / CMS, jako jsou Alfresco a Drupal, je tento přístup proveditelnější a přesvědčivější.

Znalostní management: KM odkazuje na postupy pro identifikaci, materializaci a distribuci vhledů a zkušeností. V našem kontextu se týká všech aspektů implementace a používání informačního systému, jako jsou:

- Návrh databáze

- Využití informačního systému a postupy

- Pokyny pro školení koncových uživatelů

- Využití, analýza a interpretace dat

Znalosti a učení v těchto oblastech lze zhmotnit ve formě příruček, článků, knih, sad snímků, videí, textu nápovědy vloženého do systému, online výukových stránek, fór, často kladených otázek a dalších. Všechny tyto artefakty mohou být publikovány a zpřístupněny z webového portálu.

Fórum: Portál může poskytnout fórum pro pořádání diskusí mezi profesionálními uživateli. Předmět se může pohybovat od nápovědy k provádění základních operací ve zdravotnickém informačním systému až po diskuse nad tématy analýzy dat a interpretace. Takové fórum může fungovat jako interaktivní zdroj informací a přirozeně se vyvinout v hodnotný archiv.

## Aplikace { #apps }

Za druhé, softwaroví klienti třetích stran běžící na zařízeních, jako jsou mobilní telefony, chytré telefony a tablety, se mohou připojit k webovému rozhraní DHIS2 a číst a zapisovat do příslušných zdrojů. Například vývojáři třetích stran mohou vytvořit klienta běžícího v operačním systému Android na mobilních zařízeních zaměřeného na komunitní zdravotnické pracovníky, kteří potřebují sledovat lidi, které mají navštívit, registrovat důležitá data pro každé setkání a dostávat upomínky na termíny splatnosti pro pacienta pečujte při volném cestování v komunitě. Taková klientská aplikace může interagovat s prostředky pacienta a plánu aktivit vystavenými webovým API DHIS2. Vývojář nebude závislý na hlubokém vhledu do interní implementace DHIS2, spíše jen na základní dovednosti v programování HTTP / Web a trochu znalostí datového modelu DHIS2. Pochopení datového modelu DHIS2 usnadňuje navigační povaha webového rozhraní API.

## Informační systémy { #information-systems }

Za třetí, vývojáři informačních systémů, kteří se zaměřují na vytváření nových způsobů vizualizace a prezentace agregovaných dat, mohou využívat webové rozhraní API DHIS2 jako servisní vrstvu svého systému. Úsilí potřebné pro vývoj nových informačních systémů a jejich údržbu v průběhu času je často do značné míry podhodnoceno. Místo toho, aby bylo možné začít úplně od začátku, lze na webové rozhraní API postavit novou aplikaci. Pozornost vývojářů lze zaměřit na vytváření nových, inovativních a kreativních reprezentací a vizualizací dat, v podobě např. ovládací panely, GIS a komponenty grafů.

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
