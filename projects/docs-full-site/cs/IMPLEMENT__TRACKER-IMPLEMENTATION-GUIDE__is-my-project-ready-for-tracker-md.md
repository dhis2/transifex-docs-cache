---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/edit/master/chapters/is-my-project-ready-for-tracker.md" 
---
# Je můj projekt připraven pro Trasovač?

## Připravenost na otázky a klíčové úvahy

Tato část má za cíl popsat některé klíčové podmínky prostředí, které by měly být dobře pochopeny před pokračováním v implementaci Trasovače. Vzhledem k tomu, že mnoho zemí, kde se Trasovač zavádí, již používá DHIS2 pro národní HMIS nebo jiné agregované účely, je důležité zdůraznit některé klíčové rozdíly mezi systémy DHIS2 Trasovačem a Aggregate, aby bylo možné vhodně plánovat změny, které bude pravděpodobně třeba provést kolem implementace a správy.

Programy Trasovače často rozšiřují dosah informačního systému a rozšiřují jej na uživatele, kteří dříve nepoužívali žádný elektronický informační systém. Jednotlivá data v zásadě vyžadují další úvahy týkající se ochrany a zabezpečení dat. Tyto dva faktory znamenají, že implementace Trasovače obvykle vyžadují:

- rozsáhlejší tréninkové úsilí mezi kádry pracovníků, které by také mohlo mít vysokou míru fluktuace;
- zvýšený důraz na přijetí uživatelem a mapování na stávající pracovní postupy;
- další hardware pro sběr dat, včetně správy tohoto hardwaru v průběhu času;
- spolehlivé pokrytí sítě a / nebo strategie řešení přerušovaného připojení;
- zvýšené povědomí o soukromí a bezpečnosti a jeho kapacita;
- větší kapacita pro IT podporu, která může řešit problémy na mnohem větší uživatelské základně; distribuováno přes větší geografii.

Tato a další doporučení budou podrobněji popsána v následujících částech. Následující série otázek může být užitečná při prvotním hodnocení připravenosti na novou implementaci Trasovače. **Zejména pokud váš případ použití zahrnuje shromažďování údajů umožňujících zjištění totožnosti (souvisejících se zdravím nebo jinak), měli byste si nejprve přečíst a zvážit následující otázky.**

- Existuje *politická a institucionální vůle* provést implementaci hromadného sběru dat na úrovni jednotlivců v místě poskytování služby?

- Je možné poskytnout systém pro skutečný sběr dat v místě péče, aniž by to poskytovatelům péče způsobilo další zátěž?

- Jaká je v tomto kontextu *přidaná hodnota* a *smysluplné využití* údajů na úrovni pacientů? Jaké jsou konkrétní otázky, na které mohou odpovědět pouze tyto údaje?

- Jak budou data použita k přijímání věcných rozhodnutí poskytovateli péče, manažery a politiky?

- Existují zákony, předpisy pro shromažďování, ukládání a používání údajů na osobní a osobní identifikaci? Existují případně mechanismy, které zajistí, že tyto zákony budou v blízké budoucnosti zavedeny?

- Existuje dostatečné a trvalé financování, zdroje a lidské kapacity pro návrh, implementaci (počítač a internet), školení, údržbu, správu dat a monitorování systému?

- Existuje způsob, jak jednoznačně identifikovat klienty v nastavení zdravotního systému?

- Jak jsou v současné době shromažďovány a distribuovány identifikovatelné záznamy o pacientech na papíře?

- Existují klinické pokyny / klinické intervence nebo alespoň nějaká forma pokynů pro klinickou praxi? Existuje seznam položek hlášení v HMIS a jejich podrobné definice?

- Jak jsou aktuálně shromažďována, spravována a sdílena data na úrovni zařízení a na úrovni pacienta v systému zdravotnictví?

*Reference*:

1.  mERA checklist: [https://www.bmj.com/content/352/bmj.i1174](https://www.bmj.com/content/352/bmj.i1174)
2.  Zásady digitálního rozvoje
3.  Informatika veřejného zdraví - perspektiva rozvojové země: [https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&](https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&)


## Obecné úvahy

### Institucionální odkup a podpora

**Zajistěte, aby existoval institucionální odkup a podpora od samého začátku projektu** pro vytvoření dlouhodobého závazku. Projekt trasovače úzce souvisí s praxí a správou dat a bude vyžadovat čas, pozornost a zdroje. Změní pracovní postupy na úrovni terénu pro pozitivní, pokud bude provedeno dobře, a negativně, pokud bude provedeno špatně. Proto je zásadní, aby měl projekt pevnou podporu klíčových zúčastněných stran, jako jsou programoví manažeři, IT oddělení, vedoucí oddělení atd. Od počátku by měla být do navrhování cílů a rozsahu zapojena různorodá pracovní skupina klíčových zúčastněných stran a uživatelů. systému a tato pracovní skupina bude zmocněna přijímat rozhodnutí, jako je nahrazení některých úrovní papírového výkaznictví nebo přizpůsobení procesů dohledu tak, aby reagovaly na nové klíčové indikátory výkonu umožněné sběrem a analýzou údajů na jednotlivé úrovni.

Určete divizi / oddělení v zájmové zdravotní organizaci (jako je ministerstvo zdravotnictví, ústav veřejného zdraví atd.) S potenciálem udržitelného růstu pro bydlení a tým dlouhodobého základního administrativního rozvoje. Zapojte příslušná oddělení, která by měla být zapojena, například pracovníky se shromažďováním a správou dat a IT, stejně jako tvůrci zdravotní politiky a implementátoři, kteří mohou poskytnout informace o pracovních postupech zdravotnických pracovníků. Získejte souhlas s tím, že pracovní skupina by se neměla rozpustit na konci rozšiřování, ale měla by se transformovat na dlouhodobé správce a systémové manažery.

Předtím, než se rozhodnete pro rozsáhlý projekt Trasovač, zvažte prostředí financování velkých a dlouhodobých investic potřebných pro udržitelnost, zejména s pořízením zařízení, průběžnými náklady na síť a školením, a to jak na začátku projektu, tak rutinním školením v průběhu času noví uživatelé. Jsou cíle a alokace zdrojů z mechanismů financování sladěny se skupinou odpovědnou za implementaci trasovače? Nahradí zavedení nástroje Trasovač náklady v jiných oblastech, jako je tisk formulářů pro hlášení, které lze přeprogramovat, jakmile bude systém přijat a bude fungovat dobře?

Zvažte, jak může trasovač ovlivnit a potenciálně přinést vylepšení na všech úrovních, nejen pro koncové uživatele. Například program Trasovač, který odpovídá klinickému pracovnímu postupu pro antiretrovirovou léčbu, může být navržen tak, aby přinesl výhody osobě léčené prostřednictvím připomenutí jmenování a sdíleného klinického záznamu mezi místy ART. Mohlo by to přinést výhody poskytovateli péče automatizováním některých aspektů jejich hlášení a poskytováním podpory rozhodování. Mohlo by to přinést výhody supervizorovi poskytnutím konkrétních informací o výkonu a výzvách založených na datech; a mohla by přinést výhody manažerům programů přidáním nejen dat v reálném čase, ale také zavedením nových typů indikátorů, jako jsou ty, které jsou založeny na včasnosti nebo kvalitě, díky příležitostem, které představují data na jednotlivé úrovni.

Návrh těchto výsledků nejenže významně zvyšuje hodnotu systému, pomáhá zajistit absorpci a spokojenost uživatelů a může přinést významné zlepšení v poskytování zdravotní péče. Tyto druhy funkcí mohou také pomoci zajistit odkup dárců a financování mezi dárci, protože systém může uspokojit více cílů.



*Reference*:

 - [Zásady vyladění dárců pro digitální zdraví](https://www.ictworks.org/principles-donors-digital-health/#.XXtj2SiF7mE)
  - [Zásady digitálního rozvoje](https://digitalprinciples.org/)


### Financování

**Zajistěte udržitelné financování rozvoje, implementace, školení a trvalé podpory** tak, aby vydrželo po celou dobu životního cyklu projektů trasovacích systémů. Implementace trasovače vyžaduje financování v následujících fázích:

- Shromažďování a vývoj požadavků
- Školení základního IT týmu, administrativních pracovníků a programových manažerů, zejména pokud jsou obeznámeni pouze s agregovaným vykazováním
- Nákup a výměna zařízení a zálohovací řešení (alternativní zařízení a papírové)
- Rozvinutí / škálování
- Školení koncových uživatelů, včetně diet a platů pracovníků
- Náklady na připojení (internet) a SMS, trasování může vyžadovat investice do infrastruktury, aby byla udržena v terénu
- IT podpora na úrovni koncových uživatelů
- Hostování
- Průběžné hodnocení a údržba trasovacího programu
- Udržovací výcvik(y)

Zkušenosti ze stávajících implementací trasovacího zařízení ukazují na zahájení a zavedení projektů Trasovače jako na fázi nejvíce náročnou na zdroje. Složitý program Trasovač, který modeluje klinické pracovní postupy a nahrazuje hlášení v papírové podobě, může trvat rok, než se navrhne a získá řádný odkup a podpora. Národní školení tisíců uživatelů jsou náročná na zdroje. Poskytování nového hardwaru, jako jsou zařízení Android nebo notebooky, vyžaduje značné investice. Najímání a školení dalších zaměstnanců v oddělení IT pro správu velkého nárůstu uživatelů vyžaduje zvýšené rozpočty.

Postupem času největší náklady souvisejí s aktualizačním školením a trvalou podporou uživatelů. Pro zajištění udržitelné implementace sledovače je zásadní, aby bylo zajištěno financování nejen prostřednictvím škálování, ale také pro pokrytí běžných nákladů v budoucnu. Projekty obvykle nejsou udržitelné, pokud nejsou vyčleněny dostatečné finanční prostředky pro dostatečně obsazený tým IT a / nebo průběžnou údržbu a udržovací školení.

Náklady spojené se zavedením jednotlivých systémů lze do jisté míry vyrovnat vylepšenými procesy; snížení rozpočtů na tisk a přepravu papírových formulářů; lepší dodržování pokynů a mechanismů doporučení; atd. Digitalizace současných pracovních procesů je dlouhodobou investicí a od začátku by měly být vytvářeny plány, které by takové projekty považovaly za změnu rutinní praxe vyžadující trvalou podporu.

*Reference*:

 - Školící balíček - školení ([http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf](http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf))
 - Registry pro hodnocení výsledků pacientů: Uživatelská příručka [Internet]. 3. vydání. [https://www.ncbi.nlm.nih.gov/books/NBK208631/](https://www.ncbi.nlm.nih.gov/books/NBK208631/)

### Legislativa a zásady

Před nasazením aplikace Trasovač je důležité zkontrolovat příslušné právní předpisy a zásady ochrany osobních údajů a správy dat na místní, národní a mezinárodní úrovni. Shromažďování jednotlivých údajů se kategoricky liší od agregovaných údajů a vyžaduje větší pozornost soukromí a bezpečnosti. Při neexistenci jasných vnitrostátních zásad je třeba vypracovat a odsouhlasit pokyny pro zabezpečení a důvěrnost údajů - technické i administrativní. Správné postupy, které musí být jasné a zdokumentované, se pohybují od přístupu k datům, přes požadavky na hostování až po praxi uživatelů.

Mnoho druhů údajů o zdravotním stavu jednotlivce může mít vážné následky, pokud nebude chráněno soukromí. Například v zemích, kde je nezákonné nebo kulturně nepřijatelné být svobodnou těhotnou ženou, by porušení těchto informací mohlo vést k újmě pro jednotlivce a rodinu. Pokud si klient není jistý, že jeho data budou řádně chráněna, nemusí být u svého poskytovatele péče otevřený ohledně jeho zdravotních problémů, což snižuje kvalitu léčby. Osobně identifikovatelné údaje lze těžit pro politické účely nebo pro identifikaci jednotlivců v systematicky marginalizovaných skupinách.

Existuje několik konkrétních oblastí, které by měly být přezkoumány během plánovací fáze implementace Trasovače. Jak je uvedeno v [eRegistries Situation Analysis Tool](http://eregistries.org/wp-content/uploads/2017/06/Situation-Analysis.pdf), je třeba se zaměřit na pět oblastí:

1. pochopení právního prostředí
2. stávající řízení týkající se zdravotních registrů
3. pokyny, legislativa a současné postupy spojené se sběrem a ukládáním údajů
4. požadavky na dohled a podávání zpráv
5. potenciální a stávající etické a sociální důsledky

Politiky se mohou mezi jednotlivými zeměmi drasticky lišit a je nesmírně důležité je hodnotit lokálně na začátku každého projektu Trasování. Je také zásadní získat místní podporu zásad ochrany osobních údajů. Zkušenosti ukazují, že i dobře vytvořený právní dokument vytvořený externě, bez místního odkupu, lze odložit a nepoužívat, protože místní organizace se na jeho vývoji nepodílely a nebyl přeložen do místního jazyka. Implementace Trasovače by měla zohledňovat koncové(ho) uživatele ve všech aspektech - včetně legislativy a zásad.

Údaje na úrovni jednotlivce mají významnou hodnotu pro budoucí výzkum a analýzu, dlouho poté, co jsou shromážděny. [Článek IMIA Yearbook of Medical Informatics 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6115206/?report=reader#!po=43.3333) ukazuje, že počet zdravotních záznamů počet žádostí o přístup roste. Abychom do budoucna zajistili řádnou správu citlivých údajů, měli bychom zvážit zavedení postupů pro dohody o sdílení údajů, pokud již nejsou místně stanoveny. To pomůže zachovat systematický a spravedlivý přístup k žádostem o informace a jejich použití - ať už od výzkumné organizace, dárce nebo jiné zúčastněné strany. V situacích, kdy neexistují žádné nebo jen omezené pokyny, se doporučuje řešit obavy uvedené v [eRegistries Governance Toolkit](http://eregistries.org/wp-content/uploads/2017/08/eregistries-governance-toolkit.pdf) a získáte odpovídající vládní odkup pro rutinní zásady týkající se sdílení a přístupu k datům.

Správné plánování projektu bude zahrnovat čas a zdroje pro identifikaci základních zásad, postupů a protokolů pro ochranu soukromí a zabezpečení. Sada eRegistries Governance Toolkit poskytuje praktické pokyny, jak postupovat vpřed těmito kroky. Důkladný přezkum s místními zúčastněnými stranami o tom, jaké údaje budou shromažďovány a jak by mohly být zneužity, mohou pomoci posunout proces vpřed. Je také důležité určit časový rámec, abyste mohli znovu navštívit svůj plán ochrany osobních údajů, jak se zásady v průběhu času mění. Průběžné informování o těchto změnách vám pomůže lépe plánovat navigaci ve vývoji, implementaci a údržbě Trasovače.

Konkrétní podrobnosti o funkcích ochrany osobních údajů softwaru Trasovač a pokyny pro správnou konfiguraci najdete v [uživatelských a implementačních průvodcích DHIS2](https://docs.dhis2.org/2.33/en/index.html).

*Reference*:

 - [Sada nástrojů pro správu a řízení](http://eregistries.org/wp-content/uploads/2017/08/eregistries-governance-toolkit.pdf)
 - [Sada nástrojů pro analýzu situace](http://eregistries.org/wp-content/uploads/2017/06/Situation-Analysis.pdf)
 - [Frost MJ, Tran JB, Khatun F, Friberg IK, Rodriguez, DC: What Does It Take to Be an Effective National Steward of Digital Health Integration for Health Systems Strengthening in Low-and Middle-Income Countries? Global Health: Science and Practice 2018, Vol 6, Supplement 1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6203416/pdf/S18.pdf)
 - [Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF: eRegistries: governance for electronic maternal and child health registries. BMC pregnancy and childbirth 2016, 16(1):279](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035445/)
 - [Kloss L, Brodnik, M, Rinsehart-Thompson, L: Access and Disclosure of Personal Health Information: A Challenging Privacy Landscape in 2016-2018. IMIA Yearbook of Medical Informatics 2018, 60-66](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6115206/?report=reader#!po=43.3333)
 -  The 2012 WHO and the International Telecommunication Union (ITU) National eHealth Strategy Toolkit http://apps.who.int/iris/handle/10665/75211
 - The 2015 Roadmap for Health Measurement and Accountability https://www.who.int/hrh/documents/roadmap4health-measurement_accountability.pdf?ua=1Foundations


### Kapacita a kompetence

Vzhledem ke zvýšenému dosahu Trasovače, a to jak z hlediska uživatelů, tak podpory IT, je důležité **posoudit a zajistit dostatečnou kapacitu a příslušnou kompetenci** pro plánování, návrh, vývoj, podporu a používání sledovacího programu. Je možné, že v zemi existují oblasti, kde je Trasovač vhodný, a další oblasti, kde tomu tak není, na základě kapacity zamýšlených uživatelů a jejich přístupu k příslušnému hardwaru a síti. V mnoha případech je výhodné zavést Trasovač ve fázích, spíše než se pokusit zavést jej jako rutinní systém v oblastech nebo s uživateli, kteří nejsou připraveni. Před vytvořením zaváděcího plánu by mělo být provedeno posouzení, které povede k rozšíření a dosahu systému na základě přiměřenosti.

Klíčová pracovní skupina zúčastněných stran popsaná v části **Institucionální odkup a podpora** by měla být zapojena již brzy, aby bylo možné posoudit, na jaký kádr uživatelů bude systém zaměřen, a určit, které oddělení bude odpovědné za dlouhodobou podporu kdo bude mít za úkol poskytovat školení, zpočátku i v průběhu času atd.

Může být vyžadováno další školení pro IT jednotku, zvýšení jejich kapacity pro správnou správu osobně identifikovatelných dat nebo poskytnutí podpory pro jakýkoli nový poskytovaný hardware.

Nástroje a ovládací panely nakonfigurované ve službě Trasovač by měly být navrženy s předpokládanými uživateli, aby bylo zajištěno, že jsou vhodné a přijatelné.

Školení pro uživatele mohou vyžadovat nejen konkrétní učební osnovy pro systém, ale také všeobecné školení o používání, údržbě a odstraňování problémů s hardwarem a přístupem k síti. Měly by být vyvinuty a zavedeny jednoduché pracovní pomůcky a přístup k prvotřídní IT podpoře, aby se zvýšil počet potřeb uživatelů, které lze řešit mimo tým na centrální úrovni.


*Reference a zdroje*:

- Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF: eRegistries: governance for electronic maternal and child health registries. BMC pregnancy and childbirth 2016, 16(1):279
- [Výukový balíček pro vývoj softwaru](http://eregistries.org/learning-packages/)
- [Sada nástrojů pro správu a řízení](http://eregistries.org/learning-packages/)
- [Zásady digitálního rozvoje](https://digitalprinciples.org/)


### Infrastruktura

Je důležité zajistit vhodnou a dostatečnou infrastrukturu, která se může pro Trasovač lišit od ostatních existujících digitálních systémů. Existují tři skupiny potřebné infrastruktury:

**Elektřina a síť** V oblastech, kde je síť stabilní, je vhodné použít Trasovač přes prohlížeč notebooku nebo stolního počítače. Data z klienta prohlížeče jsou odesílána okamžitě na server, bez mezipaměti prohlížeče bez místního úložiště. To zajišťuje věrnost dat a využívá sílu výpočtu na straně serveru. V oblastech s přerušovanou nebo nízkou konektivitou je aplikace DHIS2 pro Android povinna využívat Trasovač, protože vytváří místní kopii databáze a umožňuje uživateli pokračovat v práci bez přímého připojení k centrálnímu serveru. Projekty založené na systému Android přinášejí další požadavky, pokud jde o přístup k elektřině pro nabíjení; Náklady na SMS a data; atd. Další informace najdete v [pokynech pro implementaci aplikace DHIS2 pro Android](https://www.dhis2.org/android-documentation).

**Servery a hostování** S nárůstem počtu uživatelů nemusí být stávající hostingové řešení pro agregát DHIS2 adekvátní a implementace založené na Androidu přinášejí serverovým zdrojům ještě větší zátěž. Zatímco u systémů hlášení založených na měsíčních intervalech je občas přijatelné očekávat možnosti hostování s nízkým výkonem, programy Trasovač, které podporují každodenní pracovní procesy nebo klinické pracovní postupy, vyžadují neustálou dobu provozuschopnosti a pohotovou podporu IT, pokud nastanou problémy. Je obzvláště důležité vytvořit rutinní zálohu dat Trasovače na samostatnou stránku, aby bylo možné rychle vyřešit ztrátu kritických dat na primárním serveru. Proveďte vyhodnocení současných přístupů k hostování, včetně hardwaru i dostupných lidských zdrojů, a vytvořte přístup pro vaši implementaci Trasovače. Doporučuje se, aby byly programy Trasovače obsahující osobně identifikovatelná data hostovány v odděleném prostředí od agregovaného systému, aby byla zajištěna větší bezpečnost. Ačkoli mnoho zemí v současné době hostí lokální instalace DHIS2, stojí za zvážení možnosti cloudového hostování pro programy Trasovače, kde lze v průběhu času zajistit standardní hardwarovou a technickou podporu.

**Hardware pro koncové uživatele** Vzhledem k širokému přijetí projektů digitálního zdraví je možné, že stávající hardware dostupný pro cílové uživatele je dostatečný pro novou implementaci sledovače. Mělo by být provedeno posouzení, aby se zkontrolovala dostupnost počítačů a zařízení Android a určilo, kde může být nezbytný další hardware. Měly by být uzavřeny dlouhodobé dohody o údržbě a výměně hardwaru, aby byla zajištěna udržitelnost systému Trasovač po dobu životnosti původně zakoupeného hardwaru.

### Bezpečnostní aspekty

Bezpečnost je především o lidech. Lidé, kteří jsou subjekty shromažďovaných údajů, lidé, kteří údaje používají, lidé, kteří jsou odpovědní za provádění technických opatření, a lidé, jejichž odpovědností je řídit bezpečnost konkrétního projektu trasovače.

Nestačí předpokládat, že techničtí implementátoři vynaloží maximální úsilí, aby byl systém co nejbezpečnější (i když obecně doufáme, že ano). Aby bylo možné splnit jakoukoli úroveň shody s předpisy a vyhnout se právnímu riziku, je obvykle nutné být schopen prokázat, že byly přijaty přiměřené kroky k zabezpečení systému. Minimálně to znamená, že:

1.  V organizaci je definována role, jejíž odpovědností je zabývat se otázkami souvisejícími se zabezpečením. Může to být hlavní bezpečnostní pracovník, inspektor ochrany údajů nebo jiné označení. Důležité je, že existuje jednotlivec, o jehož práci se musí zajímat a být odpovědný za řešení bezpečnostních hledisek. V ideálním případě se nejedná o technickou roli, ale o roli bližší vrcholovému vedení.
2.  Kolem programu pro trasování by měl být nějaký dokumentovaný plán zabezpečení. Toto se někdy označuje jako bezpečnostní pozice. Měl by označovat zásady, které jsou pro organizaci důležité, procesy, které jsou zavedeny k průběžné identifikaci, monitorování a zmírňování rizik, a různé další artefakty a procesy, jako jsou zásady přijatelného používání (pro zaměstnance), dohody o mlčenlivosti ( pro dodavatele), zásady přístupu, plány zálohování a obnovy po katastrofě, minimální standardy pro nasazení a konfiguraci softwaru atd.

V některých organizacích je role bezpečnostního důstojníka již zavedena a dobře definována. V mnoha dalších jde o rozvíjející se potřebu, která se projevuje v prostředí charakterizovaném absencí silné regulace, slabými institucionálními a řídícími strukturami IT a nedostatkem vhodného školení. Existují standardy a metodiky, které mohou být užitečné při utváření takové role, jako je řada ISO27000 (včetně užitečných bezplatných [online materiálů](https://www.iso27001security.com/html/toolkit.html) a šablon). Nejedná se o položku často viděnou v oblasti financování a návrhů rozpočtu, ale školení v oblasti řízení bezpečnosti by mohlo být jednou z důležitějších položek, které je třeba vzít v úvahu a stanovit rozpočet.

Neúplný seznam úkolů s vysokou prioritou, které je třeba zvážit:
1.  Ujistěte se, že nastavení softwaru je technicky silné, zdokumentované a nejlépe automatizované. Jak to udělat, je trochu věc názoru a jsou i různé nápady osvědčených postupů. Pro správce systému je návštěva serverové akademie dobrým způsobem, jak se setkat s kolegy a vyměňovat si nápady. Komunikujte také s komunitou administrátorů serveru prostřednictvím komunity praxe. Existuje také telegramová skupina správců systému (připojit se, poslat e-mail Lamin - laminbjawara@gmail.com).
2. ujistěte se, že máte tým (minimálně 2) sysadminů, kteří jsou zodpovědní za každodenní údržbu systému. V závislosti na jedné „technické“ osobě je jedno z největších identifikovaných rizik v mnoha implementacích.
3.  Jak je uvedeno výše, někdo MUSÍ být odpovědný za bezpečnost. Tato role by měla:
- hlásit se přímo vedení (nejen podivná věc)
- spravovat celkové riziko (registr rizik je váš přítel)
- ujistt se, že sysadminové dělají svou práci
- buďte si vědomi místních zákonů, omezení a SOP týkajících se zacházení s údaji a ochrany osobních údajů. V jejich nepřítomnosti nebo tam, kde jsou
neadekvátní, rozvoj a údržba místních pokynů pro správnou praxi.
4. ujistěte se, že existuje plán zálohování, včetně off-site, který je pravidelně testován. Přímo neodstranitelná ztráta dat byla
nejběžnější bezpečnostní problém, kterému země čelí,
5.  ujistěte se, že jsou systémy pravidelně auditovány (může to být „oficiální“ od generálního auditora nebo peer-to-peer v naší komunitě). Toto je nejlepší způsob, jak vedení zajistit, aby sysadminové vykonávali svou práci (výše)




