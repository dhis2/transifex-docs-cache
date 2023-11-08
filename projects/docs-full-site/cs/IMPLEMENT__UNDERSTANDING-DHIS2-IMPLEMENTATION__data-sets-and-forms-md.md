---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/data-sets-and-forms.md"
revision_date: "2021-06-14"
---

# Datové sady a formuláře { #data-sets-and-forms }

Tato kapitola pojednává o souborech dat a formulářích, o tom, jaké typy formulářů jsou k dispozici, a popisuje osvědčené postupy pro proces přechodu z papírového na elektronické formuláře.

## Co je to datová sada? { #what-is-a-data-set }

Veškeré zadávání dat v DHIS2 je organizováno pomocí datových sad. Datová sada je kolekce datových prvků seskupených dohromady pro sběr dat a v případě distribuovaných instalací také definují bloky dat pro export a import mezi instancemi DHIS2 (např. z místní instalace okresního úřadu na národní server). Datové sady nejsou přímo spojeny s datovými hodnotami, pouze prostřednictvím jejich datových prvků a frekvencí, a jako takové lze datovou sadu upravovat, mazat nebo přidávat kdykoli bez ovlivnění nezpracovaných dat již zachycených v systému, ale například změny samozřejmě ovlivní, jak budou sbírána nová data.

Datová sada má typ období, který řídí frekvenci sběru dat, která může být denní, týdenní, měsíční, čtvrtletní, šestiměsíční nebo roční. Oba datové prvky, které mají být zahrnuty do datové sady, a typ období je definován uživatelem spolu s názvem, zkráceným názvem a kódem. Pokud jsou ve formuláři pro shromažďování (a nejen v sestavách) potřebná vypočítaná pole, pak lze k datové sadě přiřadit také indikátory, ale lze je použít pouze ve vlastních formulářích (viz dále dolů).

Aby bylo možné použít datovou sadu ke shromažďování dat pro konkrétní organizační jednotku, musí uživatel přiřadit organizační jednotku k datové sadě. Tento mechanismus řídí, které organizační jednotky mohou použít které datové soubory, a zároveň definuje cílové hodnoty pro úplnost dat (např. Kolik zdravotnických zařízení v okrese má každý měsíc předávat datový soubor RCH).

Datový prvek může patřit do více datových sad, ale to vyžaduje pečlivé přemýšlení, protože to může vést k překrývajícím se a nekonstantním shromažďováním údajů, pokud např. datové soubory mají různé frekvence a používají je stejné organizační jednotky.

## Co je formulář pro zadávání údajů? { #what-is-a-data-entry-form }

Jakmile přiřadíte datovou sadu organizační jednotce, bude tato datová sada zpřístupněna v Data Entry (v části Služby) pro organizační jednotky, kterým jste ji přiřadili, a pro platná období podle typu období datové sady. Poté se zobrazí výchozí formulář pro zadávání dat, což je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s kategoriemi, jako jsou věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři založeném na kategoriích. Kromě výchozího formuláře pro zadávání údajů založeného na seznamu existují další dvě alternativy, formulář založený na oddílech a vlastní formulář.

### Druhy formulářů pro zadávání údajů { #types-of-data-entry-forms }

DHIS2 v současné době obsahuje tři různé typy formulářů, které jsou popsány níže.

#### Výchozí formuláře { #default-forms }

Výchozí formulář pro zadávání dat je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s jinou než výchozí kombinací kategorií, například věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři na základě různých možností / dimenzí. Pokud v datové sadě použijete více než jednu kombinaci kategorií, dostanete ve výchozí podobě jednu tabulku na kombinaci kategorií s různými záhlavími sloupců pro možnosti.

#### Sekce formulářů { #section-forms }

Sekce formulářů umožňují o něco větší flexibilitu, pokud jde o používání tabulkových formulářů, a jejich design je rychlý a jednoduchý. Formulář pro zadávání dat bude často potřebovat více tabulek s podnadpisy a někdy budete muset deaktivovat (šedě) několik polí v tabulce (např. Některé kategorie se nevztahují na všechny datové prvky), obě tyto funkce jsou podporovány v sekcích formulářů. Po definování datové sady můžete definovat jeho sekce s podmnožinami datových prvků, nadpisem a možnými šedými poli v tabulce oddílu. Lze také definovat pořadí sekcí v datové sadě. V Zadávání dat můžete nyní začít používat sekce formuláře (který by se měl automaticky zobrazit, když jsou pro vybranou sadu dat k dispozici sekce). Většina tabulkových formulářů pro zadávání údajů by měla být možná se sekcemi formulářů. Využití sekcí nebo výchozích formulářů usnadňuje život, protože není nutné udržovat návrh pevného formuláře, který obsahuje odkazy na datové prvky. Pokud tyto dva typy formulářů nesplňují vaše požadavky, třetí možností je zcela flexibilní, i když časově náročnější, připravte vlastní formulář pro zadávání dat.

#### Vlastní formuláře { #custom-forms }

Pokud je formulář, který chcete navrhnout, příliš komplikovaný pro výchozí formuláře nebo formuláře oddílů, poslední možností je použít vlastní formulář. To zabere více času, ale dává vám plnou flexibilitu, pokud jde o design. V DHIS2 je v návrháři formulářů zabudovaný editor HTML (CK Editor), který umožňuje buď navrhnout formulář v grafickém uživatelském rozhraní, nebo přímo vložit do html (pomocí okna „source“ v editoru). Ve vlastním formuláři můžete vložit statický text nebo datová pole (spojená s datovými prvky

- kombinace možností kategorie) na libovolné pozici ve formuláři a máte úplnou svobodu navrhnout rozvržení formuláře. Po přidání vlastního formuláře do datové sady bude k dispozici v Data Entry a automaticky použit.

Při použití vlastního formuláře je možné použít vypočítaná pole k zobrazení např. průběžné součty nebo jiné výpočty založené na datech zachycených ve formuláři. To může např. být užitečné při řešení skladových nebo logistických formulářů, které vyžadují zůstatek položky, položky potřebné pro další období atd. Aby to uživatel mohl udělat, musí nejprve definovat vypočítané výrazy jako indikátory a poté tyto indikátory přiřadit k dané datové sadě. V návrháři vlastních formulářů pak může uživatel přiřadit indikátory formuláři stejným způsobem, jak jsou přiřazeny datové prvky. Omezení vypočítaného výrazu spočívá v tom, že všechny datové prvky použité ve výrazu musí být k dispozici ve stejné datové sadě, protože výpočty se provádějí za běhu uvnitř formuláře a nejsou založeny na hodnotách dat, které jsou již uloženy v databázi.

## Od papírového k elektronickému formuláři - poučení { #from-paper-to-electronic-form-lessons-learned }

Při zavádění elektronického zdravotnického informačního systému je nahrazovaným systémem často hlášení v papírové podobě. Proces přechodu na elektronický sběr a analýzu dat má určité problémy. Následující části navrhují osvědčené postupy, jak je překonat.

### Identifikujte samostatné datové prvky { #identify-self-contained-data-elements }

Návrh datové sady DHIS2 je obvykle založen na některých požadavcích z papírové formy, která se již používá. Logika papírových formulářů není stejná jako datový prvek a model datové sady DHIS, např. pole v tabulkové papírové formě je často popisováno jak záhlavími sloupců, tak textem na každém řádku, a někdy také některým úvodním záhlavím tabulky, které poskytuje více kontextu. V databázi je to zachyceno pro jeden atomární datový prvek bez odkazu na pozici ve formátu vizuální tabulky, takže je důležité zajistit, aby datový prvek s volitelnými kategoriemi datových prvků zachytil plný význam každého jednotlivého pole v papírová forma.

### Nechte výpočty a opakování na počítači - zachyťte pouze nezpracovaná data { #leave-calculations-and-repetitions-to-the-computer-capture-raw-data-only }

Další důležitou věcí, kterou je třeba mít na paměti při navrhování datových sad, je to, že datová sada a odpovídající formulář pro zadávání dat (což je datová sada s rozvržením) je nástrojem pro sběr dat, nikoli nástrojem pro sestavy nebo analýzy. Existují i jiné mnohem propracovanější nástroje pro výstup a vykazování dat v DHIS2 než formuláře pro zadávání dat. Papírové formuláře jsou často navrženy s ohledem na sběr dat i na vykazování, a proto můžete vidět věci, jako jsou kumulativní hodnoty (kromě měsíčních hodnot), opakování ročních dat (stejné údaje o populaci vykazované každý měsíc) nebo dokonce hodnoty indikátorů, jako jsou jako míry pokrytí ve stejné formě jako měsíční nezpracovaná data. Když každý měsíc ukládáte nezpracovaná data do databáze DHIS2 a máte veškerý potřebný výpočetní výkon v rámci počítačového nástroje, není třeba (ve skutečnosti by to bylo špatné a pravděpodobně by to způsobilo nekonzistenci) registrovat ručně vypočítané hodnoty, jako je ty zmíněné výše. Chcete pouze zachytit nezpracovaná data ve svých datových sadách / formulářích a nechat výpočty na počítači a prezentovat tyto hodnoty nástrojům pro vytváření zpráv v DHIS. Díky funkčnosti přehledů sady dat všechny formuláře tabulkových sekcí automaticky získají další sloupce zcela vpravo a poskytnou mezisoučet a celkové hodnoty pro každý řádek (datový prvek).
