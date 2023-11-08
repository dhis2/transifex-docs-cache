---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/data-elements-and-custom-dimensions.md"
revision_date: "2021-06-14"
---

# Datové prvky a vlastní dimenze { #data-elements-and-custom-dimensions }

Tato kapitola nejprve pojednává o důležitém stavebním prvku systému: datovém prvku. Za druhé pojednává o modelu kategorie a o tom, jak jej lze použít k dosažení vysoce přizpůsobené struktury metadat pro ukládání dat.

## Datové prvky { #data-elements }

Datový prvek je společně s organizační jednotkou nejdůležitějším stavebním kamenem databáze DHIS2. Představuje dimenzi _co_ a vysvětluje, co se shromažďuje nebo analyzuje. V některých kontextech se to označuje jako indikátor, ale v DHIS2 se tento meta-datový prvek sběru a analýzy dat označuje jako datový prvek. Datový prvek často představuje počet některých událostí a jeho název popisuje, co se počítá, např. „Podané dávky BCG“ nebo „Případy malárie“. Když jsou data shromažďována, ověřována, analyzována nebo prezentována, jsou to datové prvky nebo výrazy vytvořené s datovými prvky, které popisují, pro jaký jev, událost nebo případ jsou data registrována. Proto se datové prvky stávají důležitými pro všechny aspekty systému a rozhodují nejen o tom, jak jsou data sbírána, ale ještě důležitější je, jak jsou data reprezentována v databázi a jak lze data analyzovat a prezentovat.

Důležitým principem při navrhování datových prvků je myslet na datové prvky jako na samostatný popis jevu nebo události a nikoli jako na pole ve formuláři pro zadávání dat. Každý datový prvek žije v databázi samostatně, zcela odděleně a nezávisle na formuláři kolekce. Je důležité vzít v úvahu, že datové prvky se používají přímo v sestavách, grafech a dalších nástrojích pro analýzu dat, ve kterých kontext v daném formuláři pro zadávání dat není přístupný ani relevantní. Jinými slovy musí být možné jasně určit, jakou událost datový prvek představuje, pouze při pohledu na jeho název. Na základě toho lze odvodit obecné pravidlo, které říká, že název datového prvku musí být schopen samostatně stát a popsat hodnotu dat i mimo kontext jeho kolekce.

Například datový prvek zvaný „malárie“ může být výstižný, je-li vidět ve formuláři pro zadávání údajů, který zachycuje údaje o očkování, ve formě, která zachycuje zásoby očkování, a ve formě pro údaje o ambulantních pacientech. Při zobrazení v sestavě je však mimo kontext formuláře pro zadávání dat nemožné rozhodnout, jakou událost tento datový prvek představuje. Pokud by se datový prvek nazýval „případy malárie“, „přijaté dávky zásob malárie“ nebo „podané dávky malárie“, bylo by z pohledu uživatele jasné, co se zpráva snaží vyjádřit. V tomto případě máme co do činění se třemi různými datovými prvky se zcela odlišnou sémantikou.

## Kategorie a vlastní dimenze { #categories-and-custom-dimensions }

Určité požadavky na sběr dat vyžadují podrobný rozpis dimenze popisující počítanou událost. Například bychom chtěli shromáždit počet „případů malárie“ rozdělených podle pohlaví a věkových skupin, například „žen“, „mužů“ a „\< 5 let” a “\> 5 let“. Charakterizuje to to, že rozdělení se obvykle opakuje pro řadu „základních“ datových prvků: Například bychom chtěli toto rozdělení znovu použít pro další datové prvky, jako jsou „TB“ a „HIV“. Aby byla metadata dynamičtější, znovu použitelná a vhodná pro analýzu, má smysl definovat zmíněné nemoci jako datové prvky a vytvořit samostatný model pro atributy rozdělení. Toho lze dosáhnout použitím modelu kategorie, který je popsán v následujícím textu.

Model kategorie má tři hlavní prvky, které je nejlépe popsat pomocí výše uvedeného příkladu:

1.  Možnost kategorie, která odpovídá „ženám“, „mužům“ a „\< 5 let” a “\> 5 let“.

2.  Kategorie, která odpovídá „pohlaví“ a „věkové skupině“.

3.  Kombinace kategorií, která by měla být ve výše uvedeném příkladu pojmenována „pohlaví a věková skupina“ a měla by jí být přiřazena obě výše zmíněné kategorie.

Tento model kategorie je ve skutečnosti samostatný, ale je v DHIS2 volně spojený s datovým prvkem. Volně spojený v tomto ohledu znamená, že existuje asociace mezi kombinací datového prvku a kategorie, ale toto přidružení lze kdykoli změnit bez ztráty jakýchkoli dat. Nedoporučuje se to však často měnit, protože databáze je obecně méně hodnotná, protože snižuje kontinuitu dat. Všimněte si, že neexistuje žádný pevný limit na počet možností kategorie v kategorii nebo počet kategorií v kombinaci kategorií, ale existuje přirozené omezení, kde se struktura stává chaotickou a nepraktickou.

Dvojici kombinací datových prvků a kategorií lze nyní použít k reprezentaci jakékoli úrovně rozdělení. Je důležité si uvědomit, že to, co se ve skutečnosti děje, je, že datům je přiřazena řada vlastních dimenzí. Stejně jako datový prvek představuje povinnou dimenzi k datovým hodnotám, kategorie k němu přidávají vlastní dimenze. Ve výše uvedeném příkladu nyní můžeme pomocí výstupních nástrojů DHIS2 provádět analýzu založenou na „pohlaví“ i „věkové skupině“ pro tyto datové prvky, stejně jako lze provádět analýzu na základě datových prvků, organizačních jednotek a období .

Tento model kategorie lze použít jak v návrzích formulářů pro zadávání dat, tak v analýzách a tabulkových sestavách. Pro účely analýzy DHIS2 automaticky vytvoří dílčí součty a součty pro každý datový prvek spojený s kombinací kategorií. Pravidlem pro tento výpočet je, že všechny možnosti kategorií by měly být součtem smysluplného součtu. Výše uvedený příklad ukazuje tak smysluplný součet, protože při shrnutí „případů malárie“ zachycených pro „ženy \< 5 let”, “muže \< 5 let”, “ženy \> 5 let“ a „muže \> 5 let“ získáme celkový počet „případů malárie“.

Pro účely shromažďování dat může DHIS2 automaticky generovat tabulkové datové vstupní formuláře, kde jsou datové prvky reprezentovány jako řádky a kombinace možností kategorií jsou reprezentovány jako sloupce. To v mnoha situacích povede k poutavým formám s minimálním úsilím. Je třeba poznamenat, že to však představuje dilema, protože tyto dva problémy někdy nejsou kompatibilní. Například je možné rychle vytvořit formuláře pro zadávání dat pomocí kategorií, které nedodržují pravidlo smysluplného součtu. Považujeme to však za lepší alternativu než zachování dvou nezávislých a samostatných modelů pro zadávání a analýzu dat.

Důležitým bodem modelu kategorie je to, že hodnoty dat jsou trvalé a přidružené ke kombinaci možností kategorie. To znamená, že přidání nebo odebrání kategorií z kombinace kategorií způsobí, že tyto kombinace budou neplatné, a k opravě je nutné provést operaci s nízkou úrovní databáze. Doporučuje se proto zamyšleně zvážit, která rozdělení jsou požadována, a příliš často je neměnit.

## Skupiny datových prvků { #data-element-groups }

Běžné vlastnosti datových prvků lze modelovat pomocí tzv. Skupin datových prvků. Skupiny jsou zcela flexibilní v tom smyslu, že jejich jména a členství jsou definovány uživatelem. Skupiny jsou užitečné jak pro procházení, tak pro prezentaci souvisejících dat a lze je také použít k agregaci hodnot zachycených pro datové prvky ve skupině. Skupiny jsou volně spojeny s datovými prvky a nejsou přímo vázány na datové hodnoty, což znamená, že je lze kdykoli upravit a přidat bez ovlivnění dat na nízké úrovni.
