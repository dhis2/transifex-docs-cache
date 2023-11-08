---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/about-demo-server-live-package-and-database-design.md"
revision_date: "2021-06-14"
---

# O demo serveru, živém balíčku a designu databáze { #moare_about_dhis2_server_database }

## Použití demo serveru DHIS2 { #using-the-dhis2-demo-server }

Tým DHIS2 udržuje ukázkový server na adrese <https://play.dhis2.org/demo>. Toto je zdaleka nejjednodušší způsob, jak vyzkoušet DHIS2. Jednoduše otevřete odkaz ve svém webovém prohlížeči a přihlaste se pomocí uživatelského jména = admin a hesla = district.

> **Poznámka**
>
> Všechny změny na tomto serveru jsou mazány každou noc, takže na tomto serveru neukládejte žádné důležité práce. Je pouze pro demonstrační účely\!

## Použití živého balíčku DHIS2 { #mod2_1 }

### Spuštění balíčku DHIS2 Live { #starting-the-dhis2-live-package }

Balíček DHIS2 Live je nejjednodušší způsob, jak začít s DHIS2 na místním počítači. DHIS2 Live je vhodný pro samostatnou instalaci a ukázky. Jednoduše si stáhněte aplikaci [zde](http://www.dhis2.org/downloads). Jakmile je soubor stažen, můžete jednoduše dvakrát kliknout na stažený soubor a začít používat DHIS2.

#### Předpoklady pro DHIS2 Live { #prerequisites-for-dhis2-live }

Musíte si být jisti, že máte v počítači nainstalovanou aktuální verzi prostředí Java Runtime. V závislosti na operačním systému existují různé způsoby instalace prostředí Java. Čtenář je odkazován na tuto [webovou stránku](http://java.sun.com/javase/downloads/index.jsp), kde najdete podrobné informace o instalaci Java.

#### Začínáme prázdnou databází { #starting-up-with-a-blank-database }

Živý balíček je dodáván s demo databází, stejně jako to, co vidíte na [online demo](http://apps.dhis2.org/demo/) (které je založeno na národní Sierra Leone HMIS), a pokud chcete začněte s prázdným systémem / databází a vytvořte si vlastní systém, pak musíte udělat následující:

1\) Zastavte živý DHIS2, pokud běží. Klikněte pravým tlačítkem na ikonu na liště a vyberte Konec. Ikona v liště je zelený symbol v pravém dolním rohu obrazovky (v systému Windows), který by měl říkat „Server DHIS2 spuštěn“, když umístíte kurzor myši na ikonu.

2\) Otevřete složku, kde je nainstalován živý balíček DHIS2, a najděte složku s názvem „conf“.

3\) V conf / otevřete soubor s názvem „hibernate.properties“ v textovém editoru (poznámkový blok apod.) A proveďte následující úpravy: vyhledejte řetězec 'jdbc:h2:./database/dhis2' a nahraďte 'dhis2' část s jakýmkoli názvem, který chcete dát své databázi (např. dhis2_test).

4\) Uložte a zavřete soubor hibernate.properties.

5\) Spusťte DHIS2 Live poklepáním na soubor dhis2-live.exe v instalační složce DHIS2 Live nebo pomocí zástupce na ploše nebo odkazu nabídky, který jste nastavili.

6\) Počkejte, až se otevře okno prohlížeče a zobrazí se přihlašovací obrazovka, a poté se přihlaste pomocí uživatelského jména: admin a hesla: okres

7\) Nyní uvidíte zcela prázdný systém DHIS2 a měli byste začít přidáním svých uživatelů, organizační hierarchie, datových prvků a datových sad atd. Pokyny, jak to provést, najdete v dalších částech uživatelské příručky.

### Stahování a instalace verze serveru { #downloading-and-installing-the-server-version }

Nejnovější stabilní verzi serveru lze stáhnout z této [webové stránky] (http://stable.dhis2.org/). Podrobné informace o jeho instalaci naleznete v kapitole o instalaci v implementační příručce.

## Přihlášení k DHIS2 { #mod2_2 }

Bez ohledu na to, zda jste nainstalovali verzi serveru nebo verzi pro stolní počítače Live, k přihlášení k aplikaci použijete webový prohlížeč. DHIS2 by měl být kompatibilní s většinou moderních webových prohlížečů, i když budete muset zajistit, aby byl povolen Java Script.

Chcete-li se přihlásit do aplikace, zadejte <http://localhost:8080/dhis>, pokud používáte živý balíček DHIS2, nebo nahraďte `localhost` názvem nebo IP adresou serveru, na kterém je verze serveru nainstalována.

Jakmile spustíte DHIS2, ať už online nebo offline, zobrazí se na zobrazené obrazovce výzva k zadání registrovaného uživatelského jména a hesla. Po zadání požadovaných informací se přihlaste do aplikace kliknutím na tlačítko přihlášení. Výchozí uživatelské jméno a heslo jsou „admin“ a „district“. Měly by být změněny ihned po prvním přihlášení.

![](resources/images/getting_started/login.png)

V dialogovém okně „Změnit jazyk“ v dolní části obrazovky můžete vybrat jazyk, ve kterém chcete DHIS2 zobrazit. Některé jazyky nemusí být k dispozici.

Pokud jste zapomněli heslo, můžete kliknout na odkaz „Zapomněli jste heslo?“. Musíte být informováni DHIS2 o své e-mailové adrese a server musí být správně nakonfigurován pro odesílání e-mailů.

Pokud si chcete vytvořit vlastní účet (a správce serveru to umožňuje), jednoduše klikněte na „Vytvořit účet“ a postupujte podle uvedených pokynů.

Jakmile se přihlásíte k DHIS2, podívejte se do specifických částí této příručky, kde najdete různé dostupné funkce.

## Odhlášení z DHIS2 { #mod2_4 }

Stačí kliknout na profil a kliknout na „Odhlásit“ v pravém horním rohu nabídky DHIS2.

## Stručný úvod do návrhu databáze DHIS2 { #database_design }

DHIS2 poskytuje výkonnou sadu nástrojů pro sběr, ověřování, vykazování a analýzu dat, ale obsah databáze, např. co sbírat, kdo by to měl sbírat a na jakém formátu bude záviset na kontextu použití. Abyste však s DHIS2 mohli dělat cokoli, musíte nejprve vytvořit metadata. Meta data nebo data o datech popisují, co by se mělo shromažďovat (datové prvky a kategorie), kde by se měly shromažďovat (organizační jednotky) a jak často by se měly shromažďovat (období). Tato metadata je třeba před použitím použít v databázi DHIS2. To lze provést prostřednictvím uživatelského rozhraní a nevyžaduje žádné programovací ani hluboké technické dovednosti softwaru, ale vyžaduje dobré porozumění procesům, které se snažíte shromažďovat ve formě dat.

Tato část poskytne velmi rychlý a krátký úvod do návrhu databáze DHIS2 a hlavně vysvětlí různé kroky potřebné k přípravě nového systému DHIS2 pro použití. Jak provést každý krok je vysvětleno v jiných kapitolách a osvědčené postupy týkající se výběru designu budou vysvětleny v příručce implementátorů. Zde je třeba postupovat takto:

1\. Nastavte hierarchii organizace

2\. Definujte datové prvky

3\. Definujte datové sady a formuláře pro zadávání dat

4\. Definujte pravidla ověřování

5\. Definujte indikátor

6\. Definujte tabulky zpráv a zprávy o návrhu

7\. Nastavte modul GIS

8\. Navrhujte grafy a přizpůsobte ovládací panel

### Organizační hierarchie { #the-organisational-hierarchy }

Hierarchie organizace definuje organizaci používající DHIS2, zdravotnická zařízení, administrativní oblasti a další geografické oblasti používané při sběru a analýze dat. Tato dimenze dat je definována jako hierarchie s jednou kořenovou jednotkou (např. Ministerstvo zdravotnictví) a libovolným počtem úrovní a uzlů pod ní. Každý uzel v této hierarchii se v DHIS2 nazývá organizační jednotka.

Návrh této hierarchie určí geografické analytické jednotky, které mají uživatelé k dispozici při shromažďování a agregaci dat v této struktuře. Současně může existovat pouze jedna organizační hierarchie, takže je třeba pečlivě zvážit její strukturu. Další hierarchie (např. Paralelní administrativní seskupení, například „Vlastnictví zařízení“) lze modelovat pomocí organizačních skupin a sad skupin, avšak hierarchie organizace je hlavním prostředkem agregace dat v geografické dimenzi. Obvykle mají národní organizační hierarchie v oblasti veřejného zdraví 4-6 úrovní, ale je podporován libovolný počet úrovní. Hierarchie je postavena na vztazích nadřazený-podřazený, např. Země nebo Ministerstvo Zdravotnictví (root) může mít např. 8 nejvyšších jednotek (krajů) a každý kraj (na úrovni 2) může mít jako své podřazené 10-15 okresů. Normálně budou zdravotnická zařízení umístěna na nejnižší úrovni, ale mohou být umístěna také na vyšších úrovních, např. zemská nebo krajská nemocnice, takže jsou podporovány zkosené organizační stromy (např. běžný uzel může být umístěn na úrovni 2, zatímco většina ostatních běžných uzlů je na úrovni 5).

Typicky existuje geografická hierarchie definovaná zdravotním systémem. např. kde se nacházejí správní úřady (např. MZ, provincie, okres), ale často existují další správní hranice v zemi, které mohou nebo nemusí být přidány, v závislosti na tom, jak její hranice zlepší analýzu dat. Při navrhování hierarchie může počet podřízených pro jakoukoli organizační jednotku naznačovat užitečnost struktury, např. mít jeden nebo více vztahů 1-1 mezi dvěma úrovněmi není příliš užitečné, protože hodnoty budou stejné pro podřízenou i nadřazenou úroveň. Na druhé straně velmi vysoký počet podřízených uprostřed hierarchie (např. 50 okresů v provincii) by mohl vyžadovat přidání další úrovně, aby se zvýšila užitečnost analýzy dat. Na nejnižší úrovni budou mít zdravotnická zařízení často velký počet podřízených (10-60), ale u ostatních úrovní výše v hierarchii cca. Doporučuje se 5-20 podřízených. Příliš málo nebo příliš mnoho podřízených může znamenat, že by měla být úroveň odebrána nebo přidána.

Všimněte si, že je možné snadno provést změny v vyšších úrovních hierarchie v pozdější fázi, jediným problémem je změna organizačních jednotek, které shromažďují data (listové uzly), např. rozdělení nebo sloučení zdravotnických zařízení. Agregace v hierarchii se provádí kdykoli na základě aktuální hierarchie a vždy bude odrážet nejnovější změny organizační struktury. V kapitole Organizační jednotky se dozvíte, jak vytvářet organizační jednotky a budovat hierarchii.

### Datové prvky { #data-elements }

Datový prvek je možná nejdůležitějším stavebním kamenem databáze DHIS2. Představuje dimenzi „CO“, vysvětluje, co se shromažďuje nebo analyzuje. V některých kontextech se to označuje jako indikátor, ale v DHIS2 nazýváme tuto jednotku sběru a analýzy _data element_. Datový prvek často představuje počet něčeho a jeho název popisuje, co se počítá, např. „Podané dávky BCG“ nebo „Případy malárie“. Když jsou data shromažďována, ověřována, analyzována, hlášena nebo prezentována, jsou to datové prvky nebo výrazy postavené na datových prvcích, které popisují, CO z těchto dat. Datové prvky se tak stávají důležitými pro všechny aspekty systému a rozhodují nejen o tom, jak jsou data shromažďována, ale ještě důležitější je, jak jsou hodnoty dat reprezentovány v databázi, která opět rozhoduje o tom, jak lze data analyzovat a prezentovat.

K této dimenzi „WHAT“ je možné přidat další podrobnosti prostřednictvím dimenze rozčlenění nazývané kategorie datových prvků. Některé běžné kategorie jsou věk a pohlaví, ale uživatel může přidat libovolnou kategorii a propojit ji s konkrétními datovými prvky. Kombinace názvu datového prvku a jeho přiřazené kategorie definuje nejmenší jednotku sběru a analýzy dostupnou v systému, a proto popisuje nezpracovaná data v databázi. Agregace lze provést při oddálení této dimenze, ale není možné žádné další rozbalení, takže návrh datových prvků a kategorií definuje podrobnosti analýzy dostupné systému (na WHAT dimenzi). Změny datových prvků a kategorií v pozdější fázi procesu mohou být komplikované, protože změní význam datových hodnot již zachycených v databázi (pokud existují). Tento krok je tedy jedním z rozhodnějších a pečlivějších kroků v procesu návrhu databáze.

Jedním z osvědčených postupů při navrhování datových prvků je myslet na datové prvky jako na jednotku analýzy dat a ne pouze jako na pole ve formuláři pro sběr dat. Každý datový prvek žije sám v databázi, zcela oddělen od formuláře pro sběr a sestavy a další výstupy jsou založeny na datových prvcích a výrazech / vzorcích složených z datových prvků, nikoli na formulářích pro sběr dat. Proces by tedy měly řídit potřeby analýzy dat, nikoli vzhled formulářů pro sběr dat. Jednoduchým pravidlem je, že název datového prvku musí být schopen samostatně stát a popisovat datovou hodnotu i mimo kontext jeho kolekce. Např. název datového prvku, jako je „Celkový počet doporučení“, má smysl, když se na něj díváme ve formě „RCH“ nebo „OPD“, ale sám o sobě jednoznačně nepopisuje jevy (na koho jsou odkazováni?), a měl by místo toho se bude nazývat „Celkový počet doporučení od mateřství“ nebo „Celkový počet doporučení od OPD“. Dva různé datové prvky s různým významem, i když pole v papírové podobě může říkat pouze „Celkový počet doporučení“, protože uživatel formuláře bude vždy vědět, odkud tato doporučení pocházejí. V databázi nebo úložišti datových prvků tento kontext již není platný, a proto jsou názvy datových prvků při popisu dat tak důležité.

Běžné vlastnosti datových prvků lze modelovat pomocí tzv. Skupin datových prvků. Skupiny jsou zcela flexibilní v tom smyslu, že jsou definovány uživatelem, jak jejich názvy, tak jejich členstvím. Skupiny jsou užitečné jak pro procházení, tak pro prezentaci souvisejících dat, ale lze je také použít k agregaci datových prvků dohromady. Skupiny jsou volně spojeny s datovými prvky a nejsou přímo vázány na datové hodnoty, což znamená, že je lze upravit a přidat kdykoli, aniž by došlo k narušení nezpracovaných dat.

### Datové sady a formuláře pro zadávání údajů { #datasets-and-data-entry-forms }

Veškeré zadávání dat v DHIS2 je organizováno pomocí datových sad. Datová sada je kolekce datových prvků seskupených dohromady pro sběr dat a v případě distribuovaných instalací také definují bloky dat pro export a import mezi instancemi DHIS2 (např. Z místní instalace okresního úřadu na národní server). Datové sady nejsou přímo propojeny s hodnotami dat, pouze prostřednictvím jejich datových prvků a frekvencí, a jako takové lze datovou sadu upravovat, mazat nebo přidávat kdykoli bez ovlivnění nezpracovaných dat již zachycených v systému, ale takové změny samozřejmě ovlivní, jak budou shromažďovány nové údaje.

Datová sada má typ období, který řídí frekvenci sběru dat, která může být denní, týdenní, měsíční, čtvrtletní, šestiměsíční nebo roční. Oba datové prvky, které mají být zahrnuty v datové sadě, a typ období je definován uživatelem spolu s názvem, krátkým názvem a kódem.

Chcete-li použít datovou sadu ke shromažďování dat pro konkrétní organizační jednotku, musíte organizační jednotku přiřadit datové sadě a tento mechanismus řídí, které organizační jednotky mohou použít které datové sady, a zároveň definuje cílové hodnoty pro úplnost dat (např. Kolik je zdravotnická zařízení v okrese, u nichž se očekává, že budou údaje RCH předkládat každý měsíc).

Datový prvek může patřit do více datových sad, ale to vyžaduje pečlivé přemýšlení, protože to může vést k překrývajícím se a nekonstantním shromažďováním údajů, pokud např. datové sady mají různé frekvence a používají je stejné organizace.

#### Formuláře pro zadávání údajů { #data-entry-forms }

Jakmile přiřadíte datovou sadu organizační jednotky, bude tato datová sada zpřístupněna v Zadání Dat (v části Služby) pro organizační jednotky, ke kterým jste ji přiřadili, a pro platná období podle typu období datové sady. Poté se zobrazí výchozí formulář pro zadávání dat, což je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s kategoriemi, jako jsou věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři na základě kategorií. Kromě výchozího formuláře pro zadávání údajů založeného na seznamu existují další dvě alternativy, formulář založený na oddílech a vlastní formulář.

##### Sekce formulářů { #section-forms }

Formuláře oddílů umožňují o něco větší flexibilitu, pokud jde o používání tabulkových formulářů, a jejich design je rychlý a jednoduchý. Formulář pro zadávání dat bude často vyžadovat více tabulek s podnadpisy a někdy je třeba deaktivovat (šedě) několik polí v tabulce (např. Některé kategorie se nevztahují na všechny datové prvky), obě tyto funkce jsou podporovány ve formulářích sekcí . Po definování datové sady můžete definovat její sekce s podmnožinami datových prvků, nadpisem a možnými šedými poli v tabulce sekce. Lze také definovat pořadí sekcí v datové sadě. V Zadávání dat můžete nyní začít používat formulář Sekce (měl by se zobrazit automaticky, když jsou pro vybranou datovou sadu k dispozici sekce). V pravém horním rohu obrazovky pro zadávání dat můžete přepínat mezi výchozím a oddílovým formulářem. Většina tabulkových formulářů pro zadávání dat by měla být možná s formuláři oddílů a čím více můžete použít formuláře oddílů (nebo výchozí formuláře), tím je to pro vás jednodušší. Pokud tyto dva typy formulářů nesplňují vaše požadavky, třetí možností je zcela flexibilní, i když časově náročnější, vlastní formulář pro zadávání dat.

##### Vlastní formuláře { #custom-forms }

Pokud je formulář, který chcete navrhnout, příliš komplikovaný pro výchozí formuláře nebo formuláře oddílů, poslední možností je použít vlastní formulář. To zabere více času, ale dává vám plnou flexibilitu, pokud jde o design. V DHIS2 je integrovaný editor HTML (FcK Editor) pro návrháře formulářů a můžete buď navrhnout formulář v uživatelském rozhraní, nebo jej vložit přímo do HTML pomocí okna Zdroj v editoru. Ve vlastním formuláři můžete vložit statický text nebo datová pole (spojená s datovými prvky + kategorií) na libovolné místo ve formuláři a máte úplnou svobodu navrhnout rozvržení formuláře. Jakmile byl do datové sady přidán vlastní formulář, bude k dispozici při zadávání dat a automaticky se použije. V pravém horním rohu obrazovky pro zadávání dat můžete přepnout zpět na výchozí a sekce (pokud existují).

### Pravidla ověřování { #validation-rules }

Jakmile nastavíte část systému pro zadávání dat a začnete shromažďovat data, je čas definovat kontroly kvality dat, které pomohou zlepšit kvalitu shromažďovaných údajů. Můžete přidat libovolný počet pravidel ověřování, která se skládají z výrazů na levé a pravé straně, které jsou opět složeny z datových prvků, s operátorem mezi oběma stranami. Typická pravidla porovnávají mezisoučty s celkovými součty. Např. pokud máte dva datové prvky „HIV testy provedeny“ a „výsledek testu HIV pozitivní“, pak víte, že ve stejné formě (pro stejné období a organizační jednotku) musí být celkový počet testů vždy stejný nebo vyšší než počet pozitivní testy. Tato pravidla by měla být absolutními pravidly, což znamená, že jsou matematicky správná, nikoli pouze předpoklady nebo „většinou správné“. Pravidla lze spouštět při zadávání dat, po vyplnění každého formuláře nebo jako dávkový proces na více formulářích současně, např. pro všechna zařízení za předchozí vykazovaný měsíc. Výsledky testů zobrazí seznam všech porušení a podrobné hodnoty pro každou stranu výrazu, kde došlo k porušení, aby bylo snadné vrátit se k zadávání dat a opravit hodnoty.

### Indikátory { #indicators }

Indikátory představují pravděpodobně nejvýkonnější funkci analýzy dat DHIS2. Zatímco datové prvky představují hrubá data (počty), které se shromažďují, indikátory představují vzorce poskytující míru pokrytí, míru výskytu, poměry a další analytické jednotky založené na vzorcích. Indikátor je tvořen faktorem (např. 1, 100, 100, 100 000), čitatelem a jmenovatelem, oba dva jsou výrazy založené na jednom nebo více datových prvcích. Např. indikátor „pokrytí BCG \ <1 rok“ je definován vzorec s faktorem 100, čitatelem („dávky BCG dětem do 1 roku“) a jmenovatelem („cílová populace do 1 roku“). Indikátor „Míra předčasného odchodu DPT1 do DPT3“ je vzorec 100% x („Podané dávky DPT1“ - „Podané dávky DPT3“) / („Podané dávky DPT1“).

Většina modulů zpráv v DHIS2 podporuje datové prvky i indikátory a můžete je také kombinovat ve vlastních sestavách, ale důležitým rozdílem a silou indikátorů oproti nezpracovaným datům (hodnoty datových prvků dat) je schopnost porovnávat data napříč různými geografickými oblastmi (např. vysoce osídlené vs venkovské oblasti), protože cílovou populaci lze použít ve jmenovateli.

Indikátory lze přidávat, upravovat a mazat kdykoli bez zásahu do datových hodnot v databázi.

### Tabulky zpráv a reportů { #report-tables-and-reports }

Standardní zprávy v DHIS2 představují velmi flexibilní způsob prezentace shromážděných dat. Data lze agregovat podle jakékoli organizační jednotky nebo úrovně organizace, podle datového prvku, podle indikátorů a také v průběhu času (např. Měsíčně, čtvrtletně, ročně). Tabulky sestav jsou vlastní zdroje dat pro standardní sestavy a lze je flexibilně definovat v uživatelském rozhraní a později k nim přistupovat externí návrháři sestav, jako je iReport nebo prostřednictvím vlastních sestav HTML. Tyto návrhy sestav lze poté nastavit jako snadno dostupné přehledy na jedno kliknutí s parametry, aby uživatelé mohli spouštět stejné přehledy, např. každý měsíc při zadávání nových údajů a také relevantní pro uživatele na všech úrovních, protože v době spuštění sestavy lze vybrat organizační jednotku.

### GIS { #gis }

V integrovaném modulu GIS můžete snadno zobrazit svá data na mapách, a to jak na polygonech (oblasti), tak jako body (zdravotnická zařízení), a to buď jako datové prvky nebo indikátory. Poskytnutím souřadnic vašich organizačních jednotek do systému to s tímto modulem můžete urychlit. Podrobnosti o tom, jak začít, najdete v části GIS.

### Grafy a ovládací panel { #charts-and-dashboard }

Jedním z nejjednodušších způsobů, jak zobrazit údaje indikátorů, jsou grafy. Snadno použitelný grafový dialog vás provede vytvořením různých typů grafů s údaji o indikátorech, organizačních jednotkách a obdobích podle vašeho výběru. Tyto grafy lze snadno přidat do jedné ze čtyř částí grafu na vašem ovládacím panelu a snadno se zpřístupní hned po přihlášení. Nezapomeňte nastavit modul ovládacího panelu jako vstupní modul v uživatelských nastaveních.
