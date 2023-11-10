---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/setting-up-a-new-database.md"
revision_date: "2021-06-14"
---

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
