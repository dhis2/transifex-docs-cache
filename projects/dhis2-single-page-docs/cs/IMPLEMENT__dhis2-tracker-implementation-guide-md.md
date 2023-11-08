---
revision_date: "2021-01-14"
template: single.html
---

# Cílové publikum { #target-audience }

Cílovým publikem pro tuto příručku jsou ti, kteří se zajímají, zda je DHIS2 Tracker vhodný pro jejich potřeby, a pro ty, kteří pracují s plánováním, rozpočtováním nebo správou implementace Trasovače. To zahrnuje potenciální vlastníky systémů, projektové manažery, osoby s rozhodovací pravomocí a dárce a také osoby odpovědné za konfiguraci, školení a podporu. Pokyny v tomto dokumentu byly odvozeny z řady existujících případů použití, na které se v celém textu odkazuje. Mělo by se na něj odkazovat ve spojení se zbytkem dokumentace na adrese docs.dhis2.org.

Doporučené změny a vylepšení této příručky lze provést podle postupu popsaného [v DHIS2 github](https://github.com/dhis2/dhis2-docs/blob/master/src/commonmark/en/content/common/submitting-a-doc-fix.md).

# Úvod { #introduction }

Trasovač je aplikace v rámci platformy DHIS2, která umožňuje zaznamenávat a používat jednotlivá dlouhodobá data. Funkce Trasovače pokrývá široké spektrum potřeb, od sledování kvality a dostupnosti vodních zdrojů, přes sběr docházky studentů ve třídě, až po sběr údajů o pacientech do sdíleného zdravotního záznamu. Pro účely této příručky bude mnoho příkladů pocházet ze zdravotnických systémů, ačkoli Trasovač je široce používán také pro vzdělávací systémy, environmentální systémy, logistiku a další.

Mnoho zemí a programů využívá zvýšenou dostupnost sítě a rozsáhlou přítomnost mobilních zařízení a dalšího hardwaru k posouvání informačních systémů blíže úrovni, kde se generují primární data. Data na úrovni jednotlivců přidávají do informačních systémů podrobnost a nuance, poskytují příležitosti pro analýzu ad hoc, přesouvají indikátory v průběhu času a zlepšují kvalitu dat. Kromě užitečnosti pro podávání zpráv a analýzu lze údaje na úrovni jednotlivců také použít k eliminaci nadbytečnosti hlášení, posílení postavení zaměstnanců na nižší úrovni lepšími nástroji pro rozhodování a umístění klienta do středu informačního systému. Stručně řečeno, data na úrovni jednotlivce jsou nejmenší datovou jednotkou a jako taková mohou být v mnoha ohledech upravena tak, aby uspokojila různé konkurenční potřeby národních informačních systémů.

Účelem této příručky je pomoci určit, zda je Trasovač vhodný pro případ možného použití, a poskytnout praktické pokyny, které vám pomohou naplánovat úspěšné implementace. Použití nástroje Trasovač ve velkém měřítku zavádí další faktory, které by měly být plánovány nad rámec toho, co již může existovat pro existující agregovanou instanci DHIS2. Příležitosti a potenciální výhody informačních systémů se zvyšují, jak systém přechází od agregovaných dat → sledovaná anonymní data → data od identifikovatelných osob → data pacientů v reálném čase v místě péče. Ti, kdo plánují implementaci Trasovače, by si měli uvědomit, že výzvy narůstají spolu s výhodami.

Tento průvodce implementací poskytne doporučení, která vám pomohou:

- určit, zda Trasovač dokáže řešit vaše potřeby
- vyhodnotit připravenost vašeho nastavení na zavedení sběru dat na individuální úrovni
- pochopit, jak se implementace nástroje Trasovače liší od agregátu DHIS2
- ocenit obavy specifické pro datové systémy na úrovni jednotlivců, včetně ochrany soukromí a zabezpečení
- přezkoumat poučení a osvědčené postupy odvozené z případů použití v reálném světě
- plánovat zavedení svých programu(ů) Trasovače v požadovaném měřítku
- nastavit infrastrukturu, která bude v průběhu času udržovat program Trasovač

Průvodce je rozdělen do dvou základních částí:

- **Je můj projekt připraven pro Trasovač?** popisuje pět důležitých kontextových faktorů, kterým je třeba dobře rozumět pro vaše nastavení, než budete pokračovat v plánování implementace Trasovače

  - Institucionální odkup a podpora
  - Financování
  - Legislativa a zásady
  - Kapacita a kompetence
  - Infrastruktura

- **Vytváření programu(ů) Trasovače** poskytuje konkrétní pokyny a doporučení pro devět různých aspektů implementace Trasovače

  - Určení rozsahu
  - Proces návrhu a konfigurace
  - Určení rámce M&E
  - Zadávání dat v reálném čase vs. sekundárně
  - Mobilní vs. web
  - Budování podpůrné HR infrastruktury
  - Hostování
  - Školení a zavádění
  - Souvislost Trasovače s vaším agregovaným systémem

Odkazy na konkrétní plánovací nástroje jsou uvedeny v celém dokumentu a v příloze.

## K čemu lze Tracker použít? { #what-can-tracker-be-used-for }

Stejně jako u zbytku platformy DHIS2 má Trasovač obecný datový model, který umožňuje jeho konfiguraci uživatelem pro mnoho různých účelů. Trasovač ve své nejzákladnější podobě umožňuje uživateli definovat konkrétní druh věcí (osoba, komodita, laboratorní vzorek, spádová oblast atd.), které chce v průběhu času sledovat (trasovaná entita), definovat data, která chtějí shromažďovat informace o této entitě (datové prvky), umístit datové prvky v určitém pořadí a s jakýmikoli doprovodnými podmínkami nebo logikou (program, pravidla programu) a určit analytiku, která by měla být vytvořena (indikátory programu, zprávy o událostech, vizualizace dat atd. .)

Příkladem jednoduchého programu Trasovače může být program pro sběr informací o případech malárie v místě péče. Trasovanou entitou by byla osoba definovaná atributy, jako je křestní jméno, příjmení, datum narození nebo vesnice. Program by obsahoval datové prvky, jako jsou příznaky, použitý test a výsledek, poskytované ošetření atd. Tyto datové prvky mohou mít předem nakonfigurované možnosti pro možné reakce, jako jsou možné testy, nebo logiku, která pomáhá zajistit kvalitu dat, jako je to možné minimální a maximální hodnoty pro daný datový prvek. Shromážděné údaje by byly viditelné pro klinického uživatele jako součást sdíleného zdravotního záznamu pacienta s malárií, ale mohly by být použity také ke generování měsíčních zpráv požadovaných národním programem kontroly malárie, poskytování podpory při rozhodování klinickému lékaři, generování SMS připomenutí pacienta na podporu dodržování léčby nebo naplnění klinického panelu obsahujícího klíčové indikátory výkonu. Pro všechny tyto účely byly údaje shromážděny pouze jednou - během návštěvy pacienta -, ale byly opakovaně použity pro různé potřeby.

DHIS2 také podporuje sběr jednotlivých dat bez dlouhodobého trasování pomocí aplikací Zachycení dat a Události. Na krátkodobé trasování bude v této dokumentaci odkazováno také a následuje většinu stejného datového modelu jako trasovač, s výjimkou definování sledované entity, která není požadovanou součástí krátkodobého trasování. Příkladem takového programu událostí může být hlášení stejných údajů o malárii od jednotlivců jako v předchozím programu (trasovaná entita), ale bez propojení těchto údajů s konkrétním pacientem. Data by se tak nestala součástí sdíleného zdravotního záznamu (nebo by se možná nepoužila ke generování připomenutí SMS zpráv pacientovi nebo jiných funkcí, které se spoléhají na sledování entity v průběhu času), ale mohla by se použít i různá další použití dat stále lze využít.

Jak je patrné z výše uvedených příkladů, Trasovač a sběr jednotlivých dat se zcela liší od tradičních agregovaných reportů pro Health Management Information Systems (HMIS). Pouze jedno z výše popsaných potencionálních použití je uspokojeno agregovaným sběrem dat - měsíčním vykazováním - zatímco použití pro pacienta, kliniku a zdravotní zařízení je možné pouze prostřednictvím sběru jednotlivých údajů.

I pokud jde o rutinní podávání zpráv, sběr individuálních údajů přináší příležitosti pro lepší interpretaci a analýzu údajů a - což je zásadní - pro přijetí opatření. Například souhrnná zpráva může ukázat, že celkové pokrytí imunizací je 80%, ale postrádá podrobnosti o tom, zda zbývajících 20% odráží chyby v hlášení, neúmyslné vyloučení určitých jednotlivců (geografických nebo skupin) nebo jiných faktorů. Souhrnný počet také neumožňuje specifickou identifikaci neočkovaných dětí, na které by bylo možné navázat prostřednictvím cíleného informačního programu. Souhrnná čísla v tomto příkladu řeší základní potřebu ministerstev zdravotnictví hlásit národní pokrok v globálním indikátoru, ale nikoli potřeby manažerů nebo poskytovatelů imunizačních programů, aby přijali konkrétní opatření ke zlepšení pokrytí.

Jednou ze základních výhod používání Trasovače jako vašeho systému na individuální úrovni je jeho sladění se stávajícím agregovaným systémem DHIS2, který se již pro jiné HMIS používá ve většině zemí s nižšími a středními příjmy. Na rozdíl od samostatného elektronického lékařského záznamu (EMR) nebo jiné aplikace Trasovač podporuje shromažďování strukturovaných dat, která se mohou nativně agregovat směrem nahoru a posílat je do národního HMIS, čímž se sekundární vstup dat a agregace nahradí primárními zdrojovými daty.

Jako základní součást platformy DHIS2 je Trasovač dvakrát ročně aktualizován spolu se zbytkem softwaru DHIS2. Podněty pro vylepšení Trasovače pocházejí z implementací v reálných zemích a jsou v souladu s globálními doporučeními, zejména s [Směrnicemi WHO o digitálních intervencích pro posílení zdravotnických systémů](https://www.who.int/reproductivehealth/publications/digital-interventions-health-system-strengthening/en/). Z deseti doporučených intervencí má Trasovač specifické funkce, které podporují následující:

- Oznámení o narození
- Oznámení o úmrtí
- Oznámení o zásobách a správa komodit
- Cílená komunikace s klienty
- Podpora rozhodování zdravotnických pracovníků
- Digitální trasování zdravotního stavu a služeb klienta v kombinaci s podporou rozhodování
- Digitální trasování v kombinaci s podporou rozhodování a cílené komunikace s klienty
- Digitální poskytování obsahu školení a vzdělávání pro zdravotnické pracovníky

Plné využití těchto funkcí vyžaduje, aby shromážděná data byla systematická a jednotná. Ve zdravotnictví jsou pro programy Tracker zvláště vhodné služby primárního a veřejného zdraví, které jsou silně řízeny pevnými pokyny a pracovními postupy. Například v Antenatal Care (ANC) má většina zemí pokyny s algoritmy pro screening a správu pacientů v reakci na nálezy testů, které mohou být začleněny do Tracker pro sledování rutinního klinického pracovního postupu, podporující jak poskytovatele péče, tak potřeby hlášení. Ve složitějších oblastech zdravotní péče s méně zdokumentovanými a dobře definovanými rozhodovacími algoritmy (například v doporučující nemocnici) může být Tracker nejlépe použit pro jednoduchý sběr dat, což umožňuje lékaři určit nejlepší využití dat pro třídění pacientů a umožnění použití standardizovaných datových prvků pro další hlášení nebo jiné účely.

## Ukázkové uživatelské případy použití trasovače { #example-tracker-use-cases }

V této příručce budeme odkazovat na příklady použití, abychom uvedli skutečné příklady plánovacích principů, rozhodovacích bodů, využití softwaru a dat, společných překážek a problémů a poznatků získaných v různých fázích procesu plánování a implementace Trasovače. Zde je uvedeno krátké úvodní shrnutí těchto jednotlivých případů použití. Podrobnější informace o některých případech použití naleznete na webu www.dhis2.org.

### Předkonfigurované trasovací balíčky { #pre-configured-tracker-packages }

V rámci [nástroje WHO pro analýzu a využití údajů o zdravotnických zařízeních](https://www.who.int/healthinfo/tools_data_analysis_routine_facility/en/) byly vytvořeny předkonfigurované programy Tracker, které pokrývají řadu zdravotních témat. Tyto balíčky jsou zamýšleny jako výchozí bod pro národní programy, které umožňují další konfiguraci tak, aby odpovídala místnímu kontextu, při zachování globálních standardů pro indikátory a praxi. Lze je přidat do stávajících systémů DHIS2, a to buď společně, nebo jednotlivě. K těmto balíčkům lze přistupovat na výše uvedeném odkazu a také na adrese who.dhis2.org. Aktuální předkonfigurované balíčky pokrývají následující témata:

- Nepříznivé události pro imunizaci
- Oznámení o narození, mrtvém porodu a úmrtí pro civilní registrace a důležité statistiky
- Příčina úmrtí (včetně kódů ICD-10 ze seznamu úmrtnosti při zahájení)
- Vyšetřování místa rozmnožování malárie
- Diagnostika, léčba, případ a vyšetřování malárie
- Vyšetřování ohniska malárie
- Kampaně hromadné imunizace
- Rutinní imunizační registr
- Dohled nad případy tuberkulozy

Další balíčky, které jsou stále ve vývoji, jsou přístupné na https://who.dhis2.org/documentation/work_in_progress.html.

### Botswana: Program výživy a imunizace { #botswana-nutrition-and-immunization-program }

Botswana vytvořila kombinovaný program výživy a imunizace poskytující klíčové služby malým dětem, které dostávají výživovou pomoc, a zároveň zajišťuje, aby děti plnily své růstové indikátory a dostávaly celou sadu vakcín. Ve spolupráci s týmem Botswany byla vylepšena platforma Tracker tak, aby vytvářela standardizovaná z-skóre poskytující rychlé hodnocení váhy pro výšku, hmotnosti pro věk a výšky pro věk.

### Ghana: HIV / ART a další moduly eTracker { #ghana-hivart-and-other-etracker-modules }

Od roku 2012 vede Ghana Health Services průkopnický program v oblasti hlášení údajů na úrovni pacientů prostřednictvím programů DHIS2 Tracker („eTrackers“). Od roku 2019 používali 8 různých modulů eTracker. Ukázkovým příkladem je jejich HIV / ART eTracker, který sleduje jednotlivé pacienty prostřednictvím testování a léčby a usnadňuje zdravotnickým pracovníkům identifikaci a sledování neplatičů a zároveň podporuje tok hlášení agregovaných údajů o HIV, který v Ghaně probíhá od roku 2006.

### Palestina: elektronická registrace zdraví matek a dětí { #palestine-maternal-and-child-health-eregistry }

Každá žena v Palestině má přidělenou kliniku primární zdravotní péče a pokud tato klinika neposkytuje služby, které potřebuje, je požádána, aby navštívila kliniku vyšší úrovně. Tento systém doporučení vyžaduje eRegistry, která kontroluje přístup k souborům klinických pacientů, podporuje kontinuitu péče napříč různými místy zdravotní péče, umožňuje zadávání dat z několika různých bodů a poskytuje analytiku, která pomáhá řídit rozhodnutí podle pokynů předporodní péče Palestiny. Naše spolupráce s Palestinou začala v roce 2014. Vývoj a implementace eRegistry zdraví matek a dětí (MCH) zahrnovaly iterativní přístup a dynamický dialog mezi vývojáři, tvůrci politik, úředníky v oblasti veřejného zdraví a poskytovateli zdravotní péče. Tato implementace zahrnuje rozsáhlé využití automatizovaných SMS zpráv ke komunikaci s pacienty a také ovládací panely pro zlepšení kvality pro měření výkonu klinik a podporu poskytování kvalitní péče.

### Zimbabwe: Národní program kontroly malárie { #zimbabwe-national-malaria-control-program }

Implementace nástroje DHIS2 Android Tracker v Zimbabwe začala v roce 2014 jako projekt spolupráce mezi Národním programem pro kontrolu malárie (NMCP) a univerzitou v Oslu a od té doby byla rozšířena tak, aby pokrývala téměř polovinu více než 60 okresů v zemi. Tato implementace zahrnuje offline sběr dat, podrobné údaje o poloze a sběr a analýzu dat téměř v reálném čase a je příkladem práce s více zúčastněnými stranami na globální úrovni s cílem vyvinout program s potenciálem pro expanzi napříč geografickými regiony a oblastmi onemocnění.

# Je můj projekt připraven pro Trasovač? { #is-my-project-ready-for-tracker }

## Připravenost na otázky a klíčové úvahy { #readiness-questions-and-key-considerations }

Tato část má za cíl popsat některé klíčové podmínky prostředí, které by měly být dobře pochopeny před pokračováním v implementaci Trasovače. Vzhledem k tomu, že mnoho zemí, kde se Trasovač zavádí, již používá DHIS2 pro národní HMIS nebo jiné agregované účely, je důležité zdůraznit některé klíčové rozdíly mezi systémy DHIS2 Trasovačem a Aggregate, aby bylo možné vhodně plánovat změny, které bude pravděpodobně třeba provést kolem implementace a správy.

Programy Trasovače často rozšiřují dosah informačního systému a rozšiřují jej na uživatele, kteří dříve nepoužívali žádný elektronický informační systém. Jednotlivá data v zásadě vyžadují další úvahy týkající se ochrany a zabezpečení dat. Tyto dva faktory znamenají, že implementace Trasovače obvykle vyžadují:

- rozsáhlejší tréninkové úsilí mezi kádry pracovníků, které by také mohlo mít vysokou míru fluktuace;
- zvýšený důraz na přijetí uživatelem a mapování na stávající pracovní postupy;
- další hardware pro sběr dat, včetně správy tohoto hardwaru v průběhu času;
- spolehlivé pokrytí sítě a / nebo strategie řešení přerušovaného připojení;
- zvýšené povědomí o soukromí a bezpečnosti a jeho kapacita;
- větší kapacita pro IT podporu, která může řešit problémy na mnohem větší uživatelské základně; distribuováno přes větší geografii.

Tato a další doporučení budou podrobněji popsána v následujících částech. Následující série otázek může být užitečná při prvotním hodnocení připravenosti na novou implementaci Trasovače. **Zejména pokud váš případ použití zahrnuje shromažďování údajů umožňujících zjištění totožnosti (souvisejících se zdravím nebo jinak), měli byste si nejprve přečíst a zvážit následující otázky.**

- Existuje _politická a institucionální vůle_ podniknout implementaci hromadného sběru dat na úrovni jednotlivců na úrovni služby?

- Je možné poskytnout systém pro skutečný sběr dat v místě péče, aniž by to poskytovatelům péče způsobilo další zátěž?

- Jaká je v této souvislosti _přidaná hodnota_ a _myslitelné využití_ údajů na úrovni pacienta? Jaké jsou konkrétní otázky, na které mohou odpovědět pouze tyto údaje?

- Jak budou data použita k přijímání věcných rozhodnutí poskytovateli péče, manažery a politiky?

- Existují zákony, předpisy pro shromažďování, ukládání a používání údajů na osobní a osobní identifikaci? Existují případně mechanismy, které zajistí, že tyto zákony budou v blízké budoucnosti zavedeny?

- Existuje dostatečné a trvalé financování, zdroje a lidské kapacity pro návrh, implementaci (počítač a internet), školení, údržbu, správu dat a monitorování systému?

- Existuje způsob, jak jednoznačně identifikovat klienty v nastavení zdravotního systému?

- Jak jsou v současné době shromažďovány a distribuovány identifikovatelné záznamy o pacientech na papíře?

- Existují klinické pokyny / klinické intervence nebo alespoň nějaká forma pokynů pro klinickou praxi? Existuje seznam položek hlášení v HMIS a jejich podrobné definice?

- Jak jsou aktuálně shromažďována, spravována a sdílena data na úrovni zařízení a na úrovni pacienta v systému zdravotnictví?

_Reference_:

1.  mERA checklist: [https://www.bmj.com/content/352/bmj.i1174](https://www.bmj.com/content/352/bmj.i1174)
2.  Zásady digitálního rozvoje
3.  Informatika veřejného zdraví - perspektiva rozvojové země: [https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&](https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&)

## Obecné úvahy { #general-considerations }

### Institucionální odkup a podpora { #institutional-buy-in-and-support }

**Zajistěte, aby existoval institucionální odkup a podpora od samého začátku projektu** pro vytvoření dlouhodobého závazku. Projekt trasovače úzce souvisí s praxí a správou dat a bude vyžadovat čas, pozornost a zdroje. Změní pracovní postupy na úrovni terénu pro pozitivní, pokud bude provedeno dobře, a negativně, pokud bude provedeno špatně. Proto je zásadní, aby měl projekt pevnou podporu klíčových zúčastněných stran, jako jsou programoví manažeři, IT oddělení, vedoucí oddělení atd. Od počátku by měla být do navrhování cílů a rozsahu zapojena různorodá pracovní skupina klíčových zúčastněných stran a uživatelů. systému a tato pracovní skupina bude zmocněna přijímat rozhodnutí, jako je nahrazení některých úrovní papírového výkaznictví nebo přizpůsobení procesů dohledu tak, aby reagovaly na nové klíčové indikátory výkonu umožněné sběrem a analýzou údajů na jednotlivé úrovni.

Určete divizi / oddělení v zájmové organizaci zdravotnictví (jako je ministerstvo zdravotnictví, ústav veřejného zdraví atd.) S potenciálem udržitelného růstu pro bydlení a tým dlouhodobého základního administrativního rozvoje. Zapojte příslušná oddělení, která by měla být zapojena, například pracovníky se sběrem a správou dat a IT, stejně jako tvůrci zdravotní politiky a implementátoři, kteří mohou poskytnout informace o pracovních postupech zdravotnických pracovníků. Získejte souhlas s tím, že pracovní skupina by se neměla rozpustit na konci rozšiřování, ale měla by se transformovat na dlouhodobé správce a systémové manažery. Předtím, než se rozhodnete pro rozsáhlý projekt Trasování, zvažte prostředí financování velkých a dlouhodobých investic potřebných pro udržitelnost, zejména s pořízením zařízení, průběžnými náklady na síť a školením, a to jak na začátku projektu, tak rutinním školením v průběhu času noví uživatelé. Jsou cíle a alokace zdrojů z mechanismů financování sladěny se skupinou odpovědnou za implementaci trasovače? Nahradí zavedení nástroje Trasování náklady v jiných oblastech, jako je tisk formulářů hlášení, které lze přeprogramovat, jakmile bude systém přijat a bude fungovat dobře?

Zvažte, jak může trasovač ovlivnit a potenciálně přinést vylepšení na všech úrovních, nejen pro koncové uživatele. Například program Trasovač, který odpovídá klinickému pracovnímu postupu pro antiretrovirovou léčbu, může být navržen tak, aby přinesl výhody osobě léčené prostřednictvím připomenutí jmenování a sdíleného klinického záznamu mezi místy ART. Mohlo by to přinést výhody poskytovateli péče automatizováním některých aspektů jejich hlášení a poskytováním podpory rozhodování. Mohlo by to přinést výhody supervizorovi poskytnutím konkrétních informací o výkonu a výzvách založených na datech; a mohla by přinést výhody manažerům programů přidáním nejen dat v reálném čase, ale také zavedením nových typů indikátorů, jako jsou ty, které jsou založeny na včasnosti nebo kvalitě, díky příležitostem, které představují data na jednotlivé úrovni.

Návrh těchto výsledků nejenže významně zvyšuje hodnotu systému, pomáhá zajistit absorpci a spokojenost uživatelů a může přinést významné zlepšení v poskytování zdravotní péče. Tyto druhy funkcí mohou také pomoci zajistit odkup dárců a financování mezi dárci, protože systém může uspokojit více cílů.

_Reference_:

- [Zásady sladění dárců pro digitální zdraví](https://www.ictworks.org/principles-donors-digital-health/#.XXtj2SiF7mE)
- [Zásady pro digitální rozvoj](https://digitalprinciples.org/)

### Financování { #funding }

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

_Reference_:

- Školící balíček - školení ([http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf](http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf))
- Registry pro hodnocení výsledků pacientů: Uživatelská příručka [Internet]. 3. vydání. [https://www.ncbi.nlm.nih.gov/books/NBK208631/](https://www.ncbi.nlm.nih.gov/books/NBK208631/)

### Legislativa a zásady { #legislation-and-policies }

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

_Reference_:

- [Sada nástrojů pro vedení správy](http://eregistries.org/wp-content/uploads/2017/08/eregistries-governance-toolkit.pdf)
- [Sada nástrojů pro analýzu situace](http://eregistries.org/wp-content/uploads/2017/06/Situation-Analysis.pdf)
- [Frost MJ, Tran JB, Khatun F, Friberg IK, Rodriguez, DC: Co je zapotřebí k tomu, aby se stal účinným národním správcem integrace digitálního zdraví pro systémy zdravotnictví posilující v zemích s nízkými a středními příjmy? Global Health: Science and Practice 2018, Vol 6, Supplement 1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6203416/pdf/S18.pdf)
- [Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF: eRegistries: governance pro elektronické registry zdraví matek a dětí. Těhotenství a porod BMC 2016, 16 (1): 279](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035445/)
- [Kloss L, Brodnik, M, Rinsehart-Thompson, L: Přístup a zveřejňování osobních zdravotních informací: Náročná krajina ochrany osobních údajů v letech 2016-2018. Ročenka lékařské informatiky IMIA 2018, 60-66](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6115206/?report=reader#!po=43.3333)
- The 2012 WHO and the International Telecommunication Union (ITU) National eHealth Strategy Toolkit http://apps.who.int/iris/handle/10665/75211
- The 2015 Roadmap for Health Measurement and Accountability https://www.who.int/hrh/documents/roadmap4health-measurement_accountability.pdf?ua=1Foundations

### Kapacita a kompetence { #capacity-and-competence }

Vzhledem ke zvýšenému dosahu Trasovače, a to jak z hlediska uživatelů, tak podpory IT, je důležité **posoudit a zajistit dostatečnou kapacitu a příslušnou kompetenci** pro plánování, návrh, vývoj, podporu a používání sledovacího programu. Je možné, že v zemi existují oblasti, kde je Trasovač vhodný, a další oblasti, kde tomu tak není, na základě kapacity zamýšlených uživatelů a jejich přístupu k příslušnému hardwaru a síti. V mnoha případech je výhodné zavést Trasovač ve fázích, spíše než se pokusit zavést jej jako rutinní systém v oblastech nebo s uživateli, kteří nejsou připraveni. Před vytvořením zaváděcího plánu by mělo být provedeno posouzení, které povede k rozšíření a dosahu systému na základě přiměřenosti.

Klíčová pracovní skupina zúčastněných stran popsaná v části **Institucionální odkup a podpora** by měla být zapojena již brzy, aby bylo možné posoudit, na jaký kádr uživatelů bude systém zaměřen, a určit, které oddělení bude odpovědné za dlouhodobou podporu kdo bude mít za úkol poskytovat školení, zpočátku i v průběhu času atd.

Může být vyžadováno další školení pro IT jednotku, zvýšení jejich kapacity pro správnou správu osobně identifikovatelných dat nebo poskytnutí podpory pro jakýkoli nový poskytovaný hardware.

Nástroje a ovládací panely nakonfigurované ve službě Trasovač by měly být navrženy s předpokládanými uživateli, aby bylo zajištěno, že jsou vhodné a přijatelné.

Školení pro uživatele mohou vyžadovat nejen konkrétní učební osnovy pro systém, ale také všeobecné školení o používání, údržbě a odstraňování problémů s hardwarem a přístupem k síti. Měly by být vyvinuty a zavedeny jednoduché pracovní pomůcky a přístup k prvotřídní IT podpoře, aby se zvýšil počet potřeb uživatelů, které lze řešit mimo tým na centrální úrovni.

_Reference a zdroje_:

- Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF: eRegistries: governance for electronic maternal and child health registries. BMC pregnancy and childbirth 2016, 16(1):279
- [Učební balíček vývoje softwaru](http://eregistries.org/learning-packages/)
- [Sada nástrojů pro správu řízení](http://eregistries.org/learning-packages/)
- [Principles of Digital Development](https://digitalprinciples.org/)

### Infrastruktura { #infrastructure }

Je důležité zajistit vhodnou a dostatečnou infrastrukturu, která se může pro Trasovač lišit od ostatních existujících digitálních systémů. Existují tři skupiny potřebné infrastruktury:

**Elektřina a síť** V oblastech, kde je síť stabilní, je vhodné použít Trasovač přes prohlížeč notebooku nebo stolního počítače. Data z klienta prohlížeče jsou odesílána okamžitě na server, bez mezipaměti prohlížeče bez místního úložiště. To zajišťuje věrnost dat a využívá sílu výpočtu na straně serveru. V oblastech s přerušovanou nebo nízkou konektivitou je aplikace DHIS2 pro Android povinna využívat Trasovač, protože vytváří místní kopii databáze a umožňuje uživateli pokračovat v práci bez přímého připojení k centrálnímu serveru. Projekty založené na systému Android přinášejí další požadavky, pokud jde o přístup k elektřině pro nabíjení; Náklady na SMS a data; atd. Další informace najdete v [pokynech pro implementaci aplikace DHIS2 pro Android](https://www.dhis2.org/android-documentation).

**Servery a hostování** S nárůstem počtu uživatelů nemusí být stávající hostingové řešení pro agregát DHIS2 adekvátní a implementace založené na Androidu přinášejí serverovým zdrojům ještě větší zátěž. Zatímco u systémů hlášení založených na měsíčních intervalech je občas přijatelné očekávat možnosti hostování s nízkým výkonem, programy Trasovač, které podporují každodenní pracovní procesy nebo klinické pracovní postupy, vyžadují neustálou dobu provozuschopnosti a pohotovou podporu IT, pokud nastanou problémy. Je obzvláště důležité vytvořit rutinní zálohu dat Trasovače na samostatnou stránku, aby bylo možné rychle vyřešit ztrátu kritických dat na primárním serveru. Proveďte vyhodnocení současných přístupů k hostování, včetně hardwaru i dostupných lidských zdrojů, a vytvořte přístup pro vaši implementaci Trasovače. Doporučuje se, aby byly programy Trasovače obsahující osobně identifikovatelná data hostovány v odděleném prostředí od agregovaného systému, aby byla zajištěna větší bezpečnost. Ačkoli mnoho zemí v současné době hostí lokální instalace DHIS2, stojí za zvážení možnosti cloudového hostování pro programy Trasovače, kde lze v průběhu času zajistit standardní hardwarovou a technickou podporu.

**Hardware pro koncové uživatele** Vzhledem k širokému přijetí projektů digitálního zdraví je možné, že stávající hardware dostupný pro cílové uživatele je dostatečný pro novou implementaci sledovače. Mělo by být provedeno posouzení, aby se zkontrolovala dostupnost počítačů a zařízení Android a určilo, kde může být nezbytný další hardware. Měly by být uzavřeny dlouhodobé dohody o údržbě a výměně hardwaru, aby byla zajištěna udržitelnost systému Trasovač po dobu životnosti původně zakoupeného hardwaru.

### Bezpečnostní aspekty { #security-considerations }

Bezpečnost je především o lidech. Lidé, kteří jsou subjekty shromažďovaných údajů, lidé, kteří údaje používají, lidé, kteří jsou odpovědní za provádění technických opatření, a lidé, jejichž odpovědností je řídit bezpečnost konkrétního projektu trasovače.

Nestačí předpokládat, že techničtí implementátoři vynaloží maximální úsilí, aby byl systém co nejbezpečnější (i když obecně doufáme, že ano). Aby bylo možné splnit jakoukoli úroveň shody s předpisy a vyhnout se právnímu riziku, je obvykle nutné být schopen prokázat, že byly přijaty přiměřené kroky k zabezpečení systému. Minimálně to znamená, že:

1.  V organizaci je definována role, jejíž odpovědností je zabývat se otázkami souvisejícími se zabezpečením. Může to být hlavní bezpečnostní pracovník, inspektor ochrany údajů nebo jiné označení. Důležité je, že existuje jednotlivec, o jehož práci se musí zajímat a být odpovědný za řešení bezpečnostních hledisek. V ideálním případě se nejedná o technickou roli, ale o roli bližší vrcholovému vedení.
2.  Kolem programu pro trasování by měl být nějaký dokumentovaný plán zabezpečení. Toto se někdy označuje jako bezpečnostní pozice. Měl by označovat zásady, které jsou pro organizaci důležité, procesy, které jsou zavedeny k průběžné identifikaci, monitorování a zmírňování rizik, a různé další artefakty a procesy, jako jsou zásady přijatelného používání (pro zaměstnance), dohody o mlčenlivosti ( pro dodavatele), zásady přístupu, plány zálohování a obnovy po katastrofě, minimální standardy pro nasazení a konfiguraci softwaru atd.

V některých organizacích je role bezpečnostního důstojníka již zavedena a dobře definována. V mnoha dalších jde o rozvíjející se potřebu, která se projevuje v prostředí charakterizovaném absencí silné regulace, slabými institucionálními a řídícími strukturami IT a nedostatkem vhodného školení. Existují standardy a metodiky, které mohou být užitečné při utváření takové role, jako je řada ISO27000 (včetně užitečných bezplatných [online materiálů](https://www.iso27001security.com/html/toolkit.html) a šablon). Nejedná se o položku často viděnou v oblasti financování a návrhů rozpočtu, ale školení v oblasti řízení bezpečnosti by mohlo být jednou z důležitějších položek, které je třeba vzít v úvahu a stanovit rozpočet.

Neúplný seznam úkolů s vysokou prioritou, které je třeba zvážit:

1.  Ujistěte se, že nastavení softwaru je technicky silné, zdokumentované a nejlépe automatizované. Jak to udělat, je trochu věc názoru a jsou i různé nápady osvědčených postupů. Pro správce systému je návštěva serverové akademie dobrým způsobem, jak se setkat s kolegy a vyměňovat si nápady. Komunikujte také s komunitou administrátorů serveru prostřednictvím komunity praxe. Existuje také telegramová skupina správců systému (připojit se, poslat e-mail Lamin - laminbjawara@gmail.com).
2.  ujistěte se, že máte tým (minimálně 2) sysadminů, kteří jsou zodpovědní za každodenní údržbu systému. V závislosti na jedné „technické“ osobě je jedno z největších identifikovaných rizik v mnoha implementacích.
3.  Jak je uvedeno výše, někdo MUSÍ být odpovědný za bezpečnost. Tato role by měla:

- hlásit se přímo vedení (nejen podivná věc)
- spravovat celkové riziko (registr rizik je váš přítel)
- ujistt se, že sysadminové dělají svou práci
- být si vědom místních zákonů, omezení a SOP týkajících se nakládání s údaji a ochrany osobních údajů. V případě jejich nepřítomnosti nebo tam, kde jsou nedostatečné, vypracujte a dodržujte místní pokyny pro správnou praxi.

4. ujistěte se, že existuje plán zálohování, včetně off-site, který je pravidelně testován. Jedním z nejčastějších bezpečnostních problémů, kterým země čelí, byla přímá neodstranitelná ztráta dat,
5. ujistěte se, že jsou systémy pravidelně auditovány (může to být „oficiální“ od generálního auditora nebo peer-to-peer v naší komunitě). Toto je nejlepší způsob, jak vedení zajistit, aby sysadminové vykonávali svou práci (výše)

# Vytváření trasovacích program(ů) { #building-your-tracker-programs }

Účelem této části je poskytnout přehled na vysoké úrovni o úvahách, které povedou k úspěchu v implementaci Trasovač, seskupené podle témat a s odkazy na konkrétní nástroje.

Tato část se bude zabývat:

1. Měřítko
2. Návrh a konfigurace
3. Real-time vs. sekundární zadávání dat
4. Mobilní vs. web
5. Vytvoření základního týmu
6. Hostování
7. Výcvik
8. Zveřejnění

## Určení měřítka { #determining-scale }

Protože je Tracker zaměřen na nejnižší úrovně systému, mohou systémy Trackeru znamenat dramatické zvýšení počtu uživatelů, požadavků na technickou a organizační podporu zařízení. Země mají často omezený personál kvalifikovaný k nasazení a s prací jsou spojeny náklady.

Měřítko může odkazovat na několik dimenzí; programové měřítko, funkční měřítko nebo zeměpisné měřítko.

Geografické škálování tak může vyžadovat čas a zdroje. Existují různé strategie pro geografické měřítko, tj. Pokrývají úplně jeden region nebo začínají „malé“ ve více regionech současně a paralelně se škálovávají mírně pomalejším tempem.

Když začnete měnit měřítko, věci se stanou rychleji; více lidí na tom bude pracovat a bude potřebovat podporu. Proto se ujistěte, že tým je vybaven tak, aby zvládl zvýšený objem a rychlost, přičemž vezměte v úvahu následující:

**Dokončete a pilotujte trasovač, než jej rozšíříte**
Před pokusem o škálování shromážděte důkazy a prokažte dopad. Zvažte snížení investic do funkcí, které neprokazují dopad, nebo funkcí náročných na zdroje, které mají omezený dopad. Měli byste mít finální design / konfiguraci, která bude uživatelsky testována a pilotována a bude produkovat cílené výsledky, pokud jde o správu informací a požadované zprávy, než začnete škálovat. Když začnete měnit měřítko, není čas experimentovat. Jinými slovy, otestujte svůj design a proveďte nastavení se 100, nikoli 5000 uživateli.

**Správa**
Než se pokusíte škálovat, ujistěte se, že existují solidní procesy správy a jasné rozdělení odpovědností. Ujistěte se, že tento proces auditujete, abyste zajistili dodržování procesu správy. Správné řízení je také klíčem k zajištění flexibility a přizpůsobivosti vašeho projektu sledování, například rutiny pro přidávání nových sad možností nebo nové kliniky. Kdo činí tato rozhodnutí a jak je dokumentujete a jak je sdělujete uživatelům?

**Náklady / finanční aspekty**
Zvažte svůj model financování, včetně možností generování výnosů, modelů sociálního podnikání, nákladů na uživatele a finančních cest k udržení iniciativy. Škálování vede ke zvýšení provozních nákladů, pokud jde o podporu, zařízení a konektivitu.

**Škálování infrastruktury**
Se zvýšeným rozsahem musíte zvládnout více připojení, které zase vyžadují zvýšení zdrojů v paměti, výpočetní výkon, úložiště a připojení.

Část procesu změny měřítka zajišťuje, že máte zdravý plán pro rychlé zotavení, protože na systému závisí více lidí.

**Revidujte proces od pilotního projektu**
Škálování nelze často provést pomocí přesně stejného nástroje a přístupu jako v pilotním projektu, zejména pokud jde o úroveň lidských zdrojů a odborných znalostí potřebných pro výcvik a podporu k dosažení úrovně využití dosažené v pilotním projektu. V důsledku toho zkontrolujte svůj přístup k nástrojům a implementaci a zvažte, jaké aspekty lze přepracovat a zjednodušit, abyste dosáhli svého hlavního cíle

_Reference_:

- Zásady digitálního rozvoje

_Nástroje_:

- Hodnocení připravenosti

## Proces návrhu a konfigurace { #design-and-configuration-process }

**Úzce zapojte uživatele do designu a konfigurace vašeho programu Trasovač**, abyste zajistili, že vylepšuje a podporuje jejich práci. Aby bylo možné vyvinout program Trasovač, je třeba definovat, která data se mají zadat, definovat pracovní postup a definovat pravidla programu. Všechna tato rozhodnutí o definici by měla být učiněna v úzké spolupráci s uživateli, protože přímo souvisejí - a mohou ovlivnit - to, jak dělají svou práci.

Doporučujeme zahájit proces návrhu položením následujících otázek pro zahájení diskuse:

1. Jaký je účel údajů, které shromažďujete? Jak hodláte používat data?
2. Kdo bude mít z implementace Trasovače prospěch?
3. Jak budou uživatelé zadávající data těžit z implementace Trasovače?
4. Shromažďujete v současné době tato data dnes? Jak?
5. Existují datové prvky, které aktuálně shromažďujete a které nepotřebujete?

DEFINUJTE ÚČEL, CÍL A OBLAST PŮSOBNOSTI

Jasný účel a dobře definované cíle jsou klíčem k dosažení společného porozumění rozsahu a omezení projektu a ke schopnosti interně i externě komunikovat proces vývoje a spuštění programu Tracker.

- Definujte primární a sekundární účely programu Trasovač.
- Identifikujte sledované entity, rozsah sběru dat a zdravotní kádry zapojené do sběru dat.
- Určete, jak jednoznačně identifikovat členy cílové populace (např. Použití jedinečných identifikačních čísel nebo kombinace atributů).
- Vyjasněte počáteční očekávání mezi základním týmem a dalšími zúčastněnými stranami a uživateli systému.
- Brainstormujte a diskutujte o klíčových problémech a oblastech zájmu, kterým je třeba se během vývojové fáze věnovat.
- Připravte se na provedení vývojové fáze: Vytvořte časovou osu a začleňte pohotovostní plány pro neočekávané události, které způsobí zpoždění. Formulujte očekávané problémy a diskutujte o tom, jak je zmírnit.

FORMATIVNÍ FÁZE

Získejte jasné pochopení zdravotnického systému (nebo jiného systému, který bude program Trasovač pokrývat, pro implementace mimo zdraví), abyste pochopili „bolestivé body“ současného systému, identifikovali příležitosti ke zlepšení a nakonec vyvinuli užitečný a vhodný systém to řeší tyto problémy a příležitosti. Patří sem porozumění zdravotníkům, údaje, které shromažďují, jejich klinické pracovní postupy a jejich systémy dohledu a podávání zpráv.

- Připravte se a proveďte návštěvy v terénu s cílem zmapovat klinické pracovní postupy a požadavky na dohled a hlášení za účasti všech kádrů zdravotnických pracovníků, kteří by Trasovač používali.
- Připravujte a pořádejte schůzky zúčastněných stran za účelem informování, zkoumání a získávání zpětné vazby.
- Ověřte stávající národní (klinické) pokyny týkající se rozsahu Trasovače.
- Mapujte existující pracovní postup dokumentace: Zdokumentujte, co pracovníci aktuálně dělají, a zajistěte, aby váš návrh podporoval jejich pracovní postupy, místo aby byl těžkopádnější.
- Mapujte indikátory a související datové body pro hlášení.
- Zvažte, zda je třeba revidovat pokyny nebo body hlášení. Pokud ano, připravte paralelní plány revize pokynů a podávání zpráv.

FÁZE ROZVOJE

- Získejte přehled o aktuálních klinických pokynech, intervencích, indikátorech a algoritmech.
- Na základě současných pokynů - stejně jako indikátorů a datových bodů pro podávání zpráv - formulujte algoritmy a datové body pro elektronické trasování.
- Definujte cílové skupiny a úroveň složitosti podpory rozhodování. Podle úrovně podpory pracovního postupu vytvořte pravidla pro podporu a sdělte to vývojářům softwaru ve formátu dohodnutých požadavků.
- Povolte iterativní proces kontroly a zajistěte, aby překlad vývojářů odpovídal potřebám poskytovatelů zdravotní péče.

PŘIZPŮSOBENÍ A ZKUŠEBNÍ FÁZE

Tato fáze představuje iterativní proces práce se zúčastněnými stranami, vývojáři softwaru, implementátory a uživateli a začlenění jejich zpětné vazby.

- Vytvořte strukturovaný a snadno přístupný digitální systém pro komplexní a okamžité kanály zpětné vazby mezi hlavní pracovní skupinou.
- Zajistěte, aby byl vývoj obsahu v souladu s očekáváním zúčastněných stran, uživatelů systému a poskytovatelů finančních prostředků.
- Udržujte pokračující otevřené diskuse o překladu, používání informačních tlačítek atd., Abyste předešli nesprávné interpretaci.
- Ujistěte se, že existují nepřetržité paralelní procesy, které zahrnují a podporují tok informací mezi všemi skupinami uživatelů v těchto fázích.
- Definujte milníky pro vývojáře, implementátory a uživatele.
- Vytvořte strukturovaný a snadno přístupný online digitální systém pro komplexní a podrobnou zpětnou vazbu od koncových uživatelů.

Odkaz na dokumentaci k návrhu balíčku WHO

## Určení rámce M&E { #determining-your-me-framework }

Intro  
Jak vypadá vyspělá implementace trasovače?  
Udržujte a vyhodnocujte sběr dat  
Udržujte a vyhodnocujte postupy používání dat  
Udržujte a vyhodnocujte krok s novými verzemi DHIS 2  
Udržujte a vyhodnocujte správce uživatelů  
Udržujte a vyhodnocujte bezpečnost  
Udržujte a vyhodnocujte hosting  
Udržujte a vyhodnocujte podporu uživatelů  
Udržujte a vyhodnocujte školení

## Zadávání sekundárních dat v reálném čase { #real-time-vs-secondary-data-entry }

**Pečlivě vyhodnoťte, zda mají být data zadávána v reálném čase**, protože to má několik důsledků pro strukturu projektu. Trasovače se používají ke sledování jednotlivců prostřednictvím definovaných programů s přidruženými datovými prvky a pravidly. Data mohou být shromážděna zdravotnickým personálem během konzultace (bod péče v reálném čase) nebo na konci dne (nebo když mají čas na jejich zadání). Dva různé přístupy mají přirozeně důsledky pro to, k čemu se Trasovač používá: Pokud jsou data zadána v místě péče - během konzultace - je možné poskytnout podporu rozhodování a ověřit data a vyhnout se dvojímu zadávání dat. Zavádí však také výzvy, pokud jde o konektivitu, použitelnost, zvýšený počet zařízení atd.

Zadávání dat v reálném čase také vyžaduje, aby nastavení trasovače odpovídalo klinickému pracovnímu postupu (jiná doména). Proto je zásadní mít jasné SOP pro záložní papírové soubory, snadnou navigaci k vyhledání klientů a mechanismy prevence chyb (například pravidla, která znemožňují zadání data v budoucnu).

Odkaz na dokumentaci k návrhu balíčku WHO

## Mobilní vs. web { #mobile-vs-web }

**Zvažte, jak a kdy mohou lidé provádějící zadávání dat přistupovat k internetu** Existují kontexty nebo místa, kde je přístup k online centrálnímu serveru DHIS2 přes počítač náročný nebo dokonce nemožný. Aplikace DHIS2 Android Capture byla navržena a vyvinuta tak, aby na tyto situace reagovala. Zavedení mobilních zařízení do implementace DHIS2 však ovlivní váš projekt na mnoha úrovních, takže jde o rozhodnutí, které je třeba učinit informovaným a vědomým způsobem.

**Web nebo mobil?**
Při zvažování mobilní komponenty pro implementaci Trasovač je třeba vzít v úvahu dva hlavní aspekty: dostupnost internetu a mobilitu vašich zdravotních pozic. Může být nutné, aby daná implementace nástroje Trasovač řešila pouze jeden z těchto dvou aspektů nebo obojí současně. Pokusíme se je definovat a pomůžeme vám analyzovat vaši situaci v této části.

- **Mobilita**: Existují týmy, které poskytují své služby na různých místech prostřednictvím mobilní jednotky. V místech navštívených mobilní jednotkou by mohlo existovat zařízení s odpovídající pracovní stanicí pro sběr dat, ale někdy se zadávání dat provádí v dynamičtějším prostředí nebo ve vozidle samotném. V těchto případech není vždy snadné přenášet notebook a může být vhodnější použít mobilní zařízení.
- **Dostupnost internetu**: Existuje mnoho míst, kde je přístup k internetu náročný. Různé možné scénáře lze shrnout do dvou hlavních případů: _Internetové připojení je nestabilní nebo omezené_ a _Internetové připojení není k dispozici_.

  - Pokud je _Internetové připojení nestabilní nebo omezené_ scénář omezený na určité okamžiky dne, je možné zvážit použití dat pro mobilní zařízení nebo web. Zadávání dat na webu DHIS2 umožňuje pokračovat v zadávání dat, když je internet přerušen. Zadaná data budou uložena lokálně do mezipaměti webového prohlížeče a při příštím připojení online k datům budou automaticky nahrána. Je důležité si uvědomit, že tato offline podpora závisí na úložišti webového prohlížeče a bude fungovat, pouze když bude okno prohlížeče otevřené. Pokud uživatel sbírá data offline a zavře okno, kde pracuje, když je stále offline, data budou bohužel ztracena. Offline podpora _vyrovnává_ dopad občasných přerušení internetového připojení k zajištění plynulé a stabilní pracovní zkušenosti, ale není to úplné offline řešení.

  - Když _Internetové připojení není k dispozici_, měli byste zvážit použití aplikace DHIS2 Android Capture, která poskytuje plnou offline podporu pro sběr dat. Tuto aplikaci lze používat s mobilními zařízeními i tablety a je také možné ji spustit na jiných zařízeních, jako jsou Chromebooky. Aplikace Android Capture může být tedy vhodná pro ty případy, kdy máte problémy s dostupností internetu, ale ne s problémy s mobilitou jednotlivců provádějících sběr dat.

**Důsledky používání aplikace pro Android**
Aplikace DHIS2 Android Capture usnadňuje offline použití sběru dat Trasovače, ale přináší s sebou i důsledky, které je třeba vzít v úvahu od raných fází projektu. Mít mobilní komponentu ve vaší implementaci může mimo jiné ovlivnit vaše plánování, rozpočet, školení, konfiguraci a strategii nasazení.

- **Konfigurace DHIS2:** Při konfiguraci Trasovače pro použití s mobilními zařízeními musíte věnovat zvláštní pozornost konfiguraci mobilních uživatelů, jejich přístupu k zadávání dat a organizačním jednotkám. Obvykle se předpokládá, že mobilní uživatelé budou fyzicky shromažďovat data v nejvzdálenějších a nepřístupných oblastech, a proto se od mobilního uživatele neočekává, že bude shromažďovat data z vysokého počtu zařízení, jako je hierarchie organizačních jednotek v celé zemi. I když v aplikaci není povolen maximální počet organizačních jednotek, velká čísla mohou mít vliv na výkon v závislosti na prostředcích v zařízení (paměť, procesor). Obecně by mělo být bezpečných méně než 250 organizačních jednotek, ale to je stále velmi velké číslo pro typický případ mobilního použití.
  Je také velmi důležité věnovat pozornost konfiguraci pravidel programu a indikátorů programu. Aplikace pro Android si klade za cíl podporovat všechny webové funkce Trasovače, ale některé z nich se mohou v Androidu chovat trochu jinak, nebo mohou být v plánu vývoje aplikace čekajícího na implementaci. Podrobný seznam chování pravidel programu a indikátorů programu v systému Android najdete v oddílech _Programová pravidla_ a _Programové indikátory_ v části [Dokumentace k aplikaci Android](<[https://www.dhis2.org/android-documentation](https://www.dhis2.org/android-documentation)>).

- **Vizuální reprezentace sběru dat:** Uživatelský zážitek z aplikace pro Android byl navržen tak, aby byl velmi vizuální a intuitivní. Ikony a barvy lze použít ke konfiguraci formulářů pro zadávání údajů a způsobu jejich zobrazení. Vizuální reprezentace je konfigurovatelná správcem systému. K dispozici je knihovna ikon s více než čtyřmi stovkami obrázků a paleta barev a ikony i barvy lze přiřadit k většině objektů metadat: Možnosti, Datové prvky, Atributy, Programy / Sady dat. Další informace o vizuální konfiguraci DHIS2 najdete v části _Visual Configurations_ v [Dokumentace k aplikaci Android](<[https://www.dhis2.org/android-documentation](https://www.dhis2.org/android-documentation)>).
- **Testování:** Testování je velmi důležitá fáze v jakékoli implementaci DHIS2. Aplikaci pro Android byste měli testovat souběžně s konfigurací serveru, abyste se ujistili, že se veškerá konfigurace provedená na serveru správně odráží a funguje v aplikaci. To je zvláště důležité během konfigurace pravidel programu. Další informace o různých typech testování a o tom, jak naplánovat fáze testování pro váš projekt, najdete v části _Testing_ v [DHIS2 Mobile Implementation Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf).
- **Zabezpečení:** V závislosti na vaší konfiguraci trasovače můžete ukládat osobní údaje na mobilní zařízení a může existovat napětí mezi potřebou identifikovatelných údajů zdravotního systému a právem pacienta na soukromí. Je nesmírně důležité zajistit, aby osobní údaje byly přístupné pouze oprávněným zdravotnickým pracovníkům. Řádná správa osobních údajů je zásadní součástí vzdělávání uživatelů a je nezbytné zavést SOP, které popisují bezpečnostní opatření, která mají být použita, a zajistit, aby tyto SOP byly sdíleny a dodržovány všemi uživateli. Správci systému také hrají důležitou roli při konfiguraci úrovně přístupu uživatele, protože zajišťují, že přístup k datům je vhodný pro každého uživatele a nikdy není zbytečně nadměrný. Doporučení pro adekvátní přístup k zabezpečení a ochraně osobních údajů pro jakoukoli implementaci mobilních zařízení DHIS2 najdete v části _Data Security and Privacy_ v [DHIS 2 Mobile Implementation Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf). 
  K VYŘEŠENÍ; přidat odkaz na sekci zabezpečení v tomto dokumentu!
- **Nákup mobilních zařízení:** Nákup mobilních zařízení je klíčovým aspektem mobilního nasazení a je třeba jej vzít v úvahu při plánování, rozpočtování a logistice. Dobrou strategií je získat to nejlepší a nejnovější zařízení, které si můžete dovolit, takže vydrží déle po celou dobu životnosti vašeho projektu. V tomto smyslu je dobrým zvykem co nejvíce oddálit většinu akvizice (jinými slovy všechna zařízení, která nejsou vyžadována pro počáteční testování a pilotní fázi), namísto nákupu všech zařízení v rané fázi plánovacího procesu. Technologie - a zejména mobilní zařízení - se vyvíjejí velmi rychle. Daný model se obvykle obnovuje v ročním cyklu, což spotřebitelům umožňuje meziroční přístup k významným technickým vylepšením za podobný cenový bod. Specifikace mobilních zařízení, která lze použít s aplikací DHIS2 Capture pro Android, najdete [zde](https://docs.google.com/document/d/1jZjw-hb1W8sszkPU9yPWrPoow91gEkTb0nyZJh3IJQQ/edit).
  Po provedení všech testů a dokončení pilotního projektu jste připraveni rozšířit své nasazení získáním hardwaru a nezbytných služeb. Pokyny k akvizici mobilních zařízení najdete v části _Scale Up_ v [DHIS2 Mobile Implementation Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf). Níže shrnujeme klíčové aspekty, které je třeba v této fázi zvážit:

  1. Nákup zařízení proti BYOD (přineste si vlastní zařízení): Výhodou BYOD je, že se vyhne velkým počátečním nákladům na pořízení a sníží administrativní náklady a logistické aspekty. Na druhou stranu použití modelu BYOD vede k výzvě správy velmi heterogenního hardwarového prostředí, což znamená různá zařízení a verze Android OS, což může vést k tomu, že různí koncoví uživatelé budou mít různé možnosti pro zachycení a kontrolu dat a nakonec mohou výzvy s upgradem základní instance Trasovače, protože novější verze mohou mít omezenou zpětnou kompatibilitu se staršími verzemi aplikací. Primární výhodou nákupu zařízení pro koncové uživatele je jednotnost zařízení a verzí aplikací, ale tento přístup zvyšuje náklady na hardware a zahrnuje logistické výzvy související s distribucí mobilních zařízení a jejich údržbou a výměnou v průběhu času.

  2. Distribuce aplikace: Aplikaci Android Capture můžete nainstalovat ručně pomocí souboru APK dostupného v [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) nebo použít [Google Play](https://play.google.com/store/apps/details?id=com.dhis2) obchod. S Google Play je snazší aktualizovat aplikaci na všech vašich zařízeních, ale jste nuceni automaticky instalovat všechny aktualizace aplikace. Instalace souboru APK vám umožňuje určit, kdy a kterou verzi aktualizovat, vyžaduje však složitější proces aktualizace všech vašich zařízení a nedoporučuje se pro projekty, které nepoužívají software Mobile Device Management (viz další položka).

  3. Telekomunikační smlouvy: Proces výběru a podpisu smlouvy s mobilním poskytovatelem se v jednotlivých zemích liší a bude také záviset na postupech nákupu vaší organizace.

- **Správa a údržba zařízení:** Správa mobilních zařízení (MDM) označuje software používaný ke správě mobilních zařízení. Software MDM je nezbytný pro podporu stovek zařízení, řízení distribuce souborů APK ve všech těchto zařízeních, poskytování technické podpory a vynucování institucionálních zásad. Více informací o požadovaných funkcích MDM, dostupných možnostech a pokynech pro výběr správného MDM pro váš projekt najdete v části _Mobile Device Management_ v [DHIS2 Mobile Implementation Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf).

## Lidské zdroje a IT podpora { #human-resources-and-it-support }

Bez správných lidí na palubě nebude žádná implementace nástroje Trasovač časem úspěšná. Před zahájením projektu sledovače je důležité zajistit, aby byl k dispozici správný personál se správnou kompetencí.

Při vytváření týmu je třeba vzít v úvahu několik faktorů:

1. Zaměřte se na dlouhodobé zapojení. Lidé, kteří budou v průběhu času udržovat implementaci Tracker, by měli být od začátku součástí projektu

2. Zdroje v jednotlivých zemích na všech úrovních (zdravotního) systému musí být zapojeny od samého začátku. Předání historie projektu, rozhodnutí a zavedených postupů od externích konzultantů po stálé zaměstnance jsou často náročné.

3. Pokud již máte agregovanou instanci DHIS2, pamatujte, že lidé, kteří spravují agregaci, nejsou automaticky „kvalifikovaní“ pro projekt Trasovače, protože Trasovač se liší od agregovaných reportů.

| Role                      | Odpovědnosti / úkoly                      |
| :------------------------ | ------------------------------------------- |
| Projektový manažer           | Spravujte projekt Trasovač                  |
| Konfigurační / vývojoví vedoucí   | Vedou vývojové práce                       |
| Bezpečnostní manažer          | Odpovědný za bezpečnost, zásady ++         |
| Školící manažer          | Organizuje školení                           |
| Testovací vedoucí                 | Provádí testovací práci                              |
| Školitelé                  | Provádí školení s koncovými uživateli             |
| Vedení podpory              | Provádí technckou podporu                        |
| Distribuovaný podpůrný personál | Přijímají žádosti o podporu a pomáhají uživatelům |

### Jednotka podpory IT { #it-support-unit }

Podpora by měla být k dispozici v blízkosti uživatele, což často vyžaduje vytvoření nové struktury podpory IT na úrovni okresů nebo podoblastí. Pokud se Trasovač používá v reálném čase, měla by být vždy během pracovní doby k dispozici technická podpora k řešení a hlášení problémů. Pokud bude Trasovač podporovat klinická rozhodnutí, měli by pracovníci IT rozumět klinickému pracovnímu toku a jeho zastoupení v technickém systému. Tým podpory IT Trasovače proto může mít různé sady dovedností a pozadí než ostatní pracovníci zdravotnických informací a může to být zcela nový a odlišný kádr pracovníka ve vašem zdravotním systému.

**Struktura a správa týmu**

Každý člen jednotky podpory IT by měl být proškolen před setkáním s prvním koncovým uživatelem a musí prokázat vysokou úroveň znalostí o systému a jeho fungování. Jednotka podpory IT se často skládá ze stejných lidí, kteří vedou školení koncových uživatelů. Přinejmenším by měl být během školení seznámen koncový uživatel s podpůrným personálem, aby od začátku rozvíjel vztah a důvěru. Velkou součástí práce podpůrného personálu je „podpůrný dohled“ nad prací. Efektivní podpůrný personál musí být také dobře informovaný, respektovaný a respektující, ale obecně není v pozici přímé autority nad koncovým uživatelem, protože by to mohlo snížit ochotu uživatele klást technické otázky a hlásit problémy se systémem.

Jakmile je tým na místě, lze vytvořit interní pracovní hierarchii, od zvýšení technické schopnosti v hierarchii (např. Správce systému v horní části hierarchie) a zvýšení přístupu ke koncovým uživatelům v hierarchii (např. Přímý nadřízený nad koncovým uživatelem, pracovníci terénní podpory). Během této fáze personální organizace je třeba vyvinout standardní operační postupy pro podávání zpráv a reakci na problémy od koncových uživatelů.

**Základní nástroje pro jakoukoli jednotku podpory IT**

- Dokument Často kladené otázky (FAQ): Jednoduchý dokument zobrazující v grafice nebo v místním jazyce standardní operační postupy pro zadávání dat a co dělat v případě chyb. Časté dotazy by měly být distribuovány během všech školení a měly by být pravidelně aktualizovány jednotkou podpory IT a sdíleny s koncovými uživateli, jak se vyvíjí systém Trasovač.

- Správa mobilních zařízení: K ochraně dat na úrovni pacientů je nutné implementovat samostatný systém správy případů, který sleduje, kteří uživatelé mají přístup ke kterému zařízení, aby mohli identifikovat ztracená / odcizená zařízení a sledovat případ. Tento systém může být stejně jednoduchý jako tabulka, ale ve větších a složitějších případech lze ke sledování umístění zařízení použít systém MDM na podnikové úrovni a v případě potřeby může vzdáleně vymazat jednotlivé zařízení.

- Správa uživatelů: Jednotka podpory IT by měla být schopna dokumentovat a spravovat základní úkoly správy systému, jako je vytváření nových uživatelských účtů, deaktivace neaktivních uživatelských účtů nebo resetování hesel.

- Monitorovací platforma pro sledování klíčových systémových indikátorů: Tyto klíčové indikátory zahrnují nové registrace podle organizační jednotky, neaktivní uživatele, prostoje serveru atd. Minimálně by jednotka podpory IT měla mít přístup k agregovaným indikátorům na vyhrazeném ovládacím panelu DHIS2, kde mohou zobrazit pokrok v provádění podle času a regionu.

- Platforma pro správu případů pro registraci chybových tiketů: Tyto platformy (např. JIRA) umožňují členům personálu IT podpory zadávat, upravovat, přiřazovat, sledovat a řešit chyby a další tikety a umožnit supervizorům dohled nad důležitými faktory souvisejícími se službou, jako je počet otevřených tiketů a nevyřešených chyb, průměrná doba odezvy atd.

- Platforma pro správu znalostí: Toto je úložiště, kde se zaměstnanci mohou učit z předchozích ticketů (čímž se buduje znalostní báze). Jednotka podpory IT chápe skutečnou zkušenost uživatele s Trasovačem lépe než kterýkoli jiný implementátor nebo správce systému a jejich perspektiva může být neocenitelná pro přizpůsobení Trasovače, aby lépe vyhovoval potřebám uživatele. Znalostní platforma - ať už elektronická, nebo pravidelná setkání zaměstnanců - může sdílet společné zkušenosti, frustrace nebo nápady na potenciální zlepšení

- Horká linka pro hlášení chyb: Tato horká linka může mít mnoho podob. Může to být například telefonní číslo pro zaměstnance podpory, které je sdíleno s každým uživatelem, nebo e-mailová adresa, na kterou mohou uživatelé posílat poznámky a snímky obrazovky. Bez ohledu na formát musí existovat SOP pro zadávání chyb hlášených prostřednictvím horké linky do výše zmíněné platformy pro správu případů.

- Veřejné skupiny chatu: Mnoho týmů podpory zjistí, že vytváření skupin chatu mezi zaměstnanci a koncovými uživateli může podporovat učení typu peer-to-peer (např. Whatsapp nebo Wechat pro sdílení snímků obrazovky, hlasových zpráv nebo kreativních řešení běžných problémů).

_Reference_:

- [Principles of Digital Development](https://digitalprinciples.org/)

## Hostování { #hosting }

Samotný program pro sledování a shromážděná data musí být hostován na serveru. To lze provést místně (například na ministerstvu), prostřednictvím místního profesionálního poskytovatele služeb nebo v cloudu. Různé možnosti mají klady a zápory, např. hostování implementace trasovače v cloudu znamená, že se administrátor nemusí starat o kapacitu serveru, prostoje atd., ale zároveň mohou existovat legislativní problémy s hostováním dat mimo hranice země, pokud nemáte místního poskytovatele. Bez ohledu na strategii hostování - bezpečnost je klíčovým hlediskem. To zahrnuje správu identit, autentizaci a autorizaci (omezující přístup k datům nebo službám), jakož i ochranu serverů.

Dále se musíte rozhodnout, zda chcete konfigurovat trasovač v samostatné nebo stejné instanci jako váš agregovaný systém. Velkou výhodou jedné instance je možnost přímo generovat sestavy z údajů trasovače. Mít dva ve stejné instanci však vyžaduje přísnější SOP pro správu uživatelských účtů, aby bylo zajištěno správné omezení přístupu k údajům o pacientovi.

10 zásad pro hostování a bezpečnost

1. Operační systém je LTS (vydání dlouhodobé servisní podpory)
2. Existuje automatický proces aplikace bezpečnostních záplat OS
3. Hostitelský firewall nakonfigurován tak, aby umožňoval minimální přístup
4. Přístup je přes ssh podle dohodnutých zásad - klíče, žádný přístup root atd
5. Verze DHIS2 není za poslední verzí více než 3 verzí. Existuje postup pro pravidelné použití vydání oprav.
6. Automatizovaný zálohovací systém je zaveden a pravidelně testován, včetně off-site.
7. Ovládací prvky přístupu k databázi Postgresql umožňují minimální přístup
8. Web-proxy server je správně (ssllabs test A+) nakonfigurován pomocí SSL
9. Data databáze jsou na samostatném datovém oddílu (umožňující šifrování v klidu, nastavení výkonu)
10. Monitorovací a výstražný systém je na místě (široká škála možností v závislosti na prostředí. Např. Boombox může být v pořádku s e-mailem + logwatch + munin)

Dostatek / stabilní elektřiny pro nabíjení zařízení
V případě systému Android - síť s určitou dobou provozuschopnosti, aby se mohla synchronizovat.
V případě webové aplikace - stabilní síť

2. Servery / síť / hosting

3. Hardware

Zkušenosti ukazují, že potřebujete X počet zařízení na uživatele

Pro zálohování potřebujete X % zařízení

Zařízení se musí cyklicky měnit

- Databázový diagram (včetně virtuálních strojů a fyzických sítí)
- Minimální specifikace pro hardware…
  - Servery
  - osobní počítače
  - Android / M### Hosting & Securityobile
  - Další připojená zařízení (např. Čtečky otisků prstů)
- Jiná infrastruktura

  - Přístup k síti
  - Přístup k elektřině
  - Náklady na SMS a data
  - Sdílené zdroje s jinými projekty nebo ministerstvy (např. Vládní smlouva s poskytovatelem SMS brány)

- Cloudové vs. místně hostované: Závisí na regulačním prostředí PII
- Správa a udržitelnost IT systémů.
- O plánech zabezpečení a protokolech existuje dokumentace. Jak na vysoké úrovni (bez žargonu, ale s uvedením zásad), tak i na technických postupech. Obzvláště důležité pro lokálně hostované systémy bez kultury „zabezpečení na prvním místě“.
- Jeden člověk musí být odpovědný za vývoj, údržbu a implementaci bezpečnostního plánu. Další správce zabezpečení se zavázal identifikovat a zmírnit rizika. Obě role vyžadují zkušenosti, kapacitu a motivaci.
- Zajistěte, aby existovala dokumentovaná sada technických kontrol
- Zajistěte, aby u těchto kontrol existoval proces auditu
- SOP pro provozní, síťové a fyzické zabezpečení (zamykání počítačů, silná hesla, šifrování dat atd.)
- SOP pro monitorování a reakci v případě výpadku systému nebo narušení systému
- Plán obnovy po katastrofě a rutinní cvičení
- Odstraňování problémů - proces „externího řešení“ v případě naléhavé krize, kdy situaci nelze vyřešit lokálně.
- Jaký je postup pro udělení přístupu k databázi nebo ssh na servery?
- Kontrola přístupu a pravidla
- Kam by měla spadat správa IT systému, do jakého rámce?

_Reference_:

- Bezpečnostní pokyny pro implementátory v jednotlivých zemích

## Školení a zavádění { #training-and-rollout }

**Plán vysoce kvalitního průběžného školení.** Budování kapacit je zásadní pro úspěch programu Tracker, který musí být vysoce kvalitní a musí pravidelně pokračovat po celou dobu životnosti programu. Nestačí poskytnout školení uživatelů pouze jednou - váš tréninkový plán by měl zajistit počáteční a opakovací školení v průběhu času. Uživatelé aplikace Frontline Tracker jsou obvykle terénní zdravotničtí pracovníci, kterým může být technologie méně pohodlná než zaměstnancům okresu, kteří pracují častěji s agregovanými daty. Silný důraz na školení bude zahrnovat čas na seznámení účastníků s nástroji a také na to, jak integrovat Tracker do jejich pracovního postupu.

Klíčovým principem je **vývoj školicího materiálu ve spolupráci s uživateli.** Úzká spolupráce s uživateli při navrhování školicího materiálu vám umožní pochopit, jaké koncepty uživatelé obtížně pochopí, takže můžete svůj materiál a načasování vylepšit tréninkovou agendu. Proveďte úvodní celý tréninkový běh se skupinou skutečných uživatelů a dolaďte svůj kurz.

Určete vhodný tréninkový přístup: Existuje několik možností, jak trénovat (např. Video, online test, on-site, schůzky), které lze použít jednotlivě nebo ve vzájemném spojení.

**Zapojte do školení zdravotnický personál**, nejen IT pracovníky, abyste vysvětlili a zdůraznili zdravotní důvody procesů zadávání dat. To je zvláště důležité pro konfigurace, které zahrnují podporu rozhodování. To pomáhá koncovým uživatelům lépe pochopit, proč je program Tracker významný, což může vést k úplnějšímu a přesnějšímu zadávání dat, a tedy větší pravděpodobnosti, že program uspěje ve svých cílech. Revidujte materiál na základě zpětné vazby od účastníků kurzu nebo pokud existují revize programu Tracker, které způsobují nepřesnost starých výcvikových materiálů.

**Logistika**
Naplánujte školení uživatelů Tracker jako sérii tréninkových kroků, aby po nějaké době dostali opakovací školení. Opakovací tréninkový plán by měl být v ideálním případě v souladu s cykly revizí softwaru Tracker, aby se koncovým uživatelům usnadnilo zavádění změn a nových funkcí v programu.

Uvědomte si, že zaškolení velké skupiny uživatelů (zejména rozmístěných ve velké zeměpisné oblasti) bude často vyžadovat, abyste nejprve vyškolili ostatní školitele (na školení školitelů nebo TO), abyste pomohli rozšířit kapacitu školení. Sledujte, kteří uživatelé Trasovače byli vyškoleni v tabulkovém procesoru, seznamu nebo jiné centralizované databázi, a vytvořte SOP pro aktualizaci tohoto seznamu, když se přidají noví zaměstnanci nebo když stávající členové opustí nebo jsou přemístěni. Novým / neškoleným zaměstnancům by mělo být co nejdříve poskytnuto školení. Pečlivě si vyberte místo školení. Školení může probíhat buď na místě (v pracovním prostředí uživatelů nebo v jeho blízkosti) nebo na centralizovaných školeních, která přinášejí větší skupiny uživatelů z různých pracovišť na jedno centralizované místo. Oba přístupy mají pozitivní i negativní aspekty. Bez ohledu na to, kde se školení koná, osoba odpovědná za plánování školení bude muset zorganizovat logistické podrobnosti, jako je místo konání, doprava, jídlo a pití, počítače, přístup k internetu atd.

Pokud je to možné, zaškolte uživatele na zařízeních, která budou při své práci používat. Nepodceňujte čas, za který se lidé přihlásí a seznámí se se zařízením - na začátku tréninkového programu může trvat hodně času, než budou všichni účastníci připraveni z technického hlediska. Doporučuje se mít k dispozici několik členů školicího týmu, kteří vám pomohou řešit tyto problémy hned, jak se objeví. Naplánujte následné pravidelné školení / školení na místě / udržovací školení

**Školení v nastavení nízké šířky pásma**
Pokud je připojení k internetu ve vašem tréninkovém místě příliš pomalé, nespolehlivé nebo vůbec neexistuje, budete muset nainstalovat místní instanci Trasovače a nakonfigurovat ji pro trénink na stroji / lokálním serveru a nastavit ji pro školení tak, aby účastníci mohli připojit prostřednictvím běžného prostředí místní sítě, adresy IP nebo klienta localhost. I v nastavení, kde je přístup k internetu obecně dobrý, může mít velký počet uživatelů přístup k instanci Trasovač na webu prostřednictvím jedné WiFi sítě nebo přístupového bodu k internetu, což může vést k problémům se sítí. Proto je obecně vhodné mít v těchto případech k dispozici instanci školení jako zálohu.

## Vztah Trasovače k vašemu agregovanému datovému systému { #relating-tracker-to-your-aggregate-data-system }

**Při navrhování trasovače nezapomeňte pokrýt základní požadavky na hlášení z HMIS**, abyste zabránili dvojímu hlášení. Data zadaná do trasovače tvoří základ pro generování souhrnných čísel. Např. 4 záznamy pacientů = 2 se stavem X a 2 se stavem Y. Trasovač by měl spíše podporovat agregační systém, než aby byl pro sběratele dat další zátěží. Návrh systému by měl brát v úvahu, jak splnit požadavky na agregovaná data pomocí dat zadaných pomocí trasovače.

Existují různé možnosti, které je třeba zvážit, a to buď prostřednictvím automatizace, nebo ručně pomocí nástrojů. Pro zajištění kvality a úplnosti dat a proces autorizace dat potřebujete jasný pracovní tok, nástroje a model řízení. Jinými slovy, kdo může schvalovat a zpracovávat data od jednotlivců po agregovaná data a jak k tomu dochází.

Když navrhujete integraci s HMIS, ujistěte se, že je proces agregace dobře promyšlený.

- přezkoumat indikátory
- vytvářet zprávy
- vytvořit model řízení kvality dat a publikování
- zajistit, aby procesy revize dat fungovaly (kdo vlastní proces a data a co se stane, pokud zjistíte vadná data po termínech)

Je důležité zajistit, aby poskytovatelé péče porozuměli indikátorům a byli schopni vstupovat do způsobu jejich výpočtu. Zapojte do procesu ministerstvo / tvůrce politik, aby porozuměli zásadním rozdílům mezi tím, jak se hlášení odehrálo dříve, než nyní, ve sledovači nebo v eRegistry.

Přísun dat do HMIS
Data, která se zadávají do trasovače, tvoří základ pro generování agregovaných čísel. Např. 4 záznamy pacientů = 2 se stavem X a 2 se stavem Y. Trasovač by měl spíše podporovat agregační systém, než aby byl pro sběratele dat další zátěží. Návrh systému by měl brát v úvahu, jak splnit požadavky na agregovaná data pomocí dat zadaných pomocí trasovače. Jinými slovy by se měl pracovní postup vyhnout další práci pro vaše zdravotnické pracovníky. Neměli by muset agregovat data ručně a zadávat ručně do HMIS.

Rozdíl mezi agregovaným systémem sběru dat, kde se konečná čísla zadávají do online formulářů pro podávání zpráv oproti sledovači / eRegistry, která provádí automatické podávání zpráv

Podstatně větší úsilí v designu softwaru, které pokrývá všechny potřeby hlášení a indikátorů

Je důležité definovat indikátory a porozumět tomu, co se má měřit: co je čitatel, co jmenovatel

Výchozí jmenovatel v elektronické registraci: pacienti / klienti

Odstranění tradičních papírových sestav může být časově náročné, změna chování nějakou dobu trvá

Je důležité zajistit, aby poskytovatelé péče porozuměli indikátorům a byli schopni vstupovat do způsobu jejich výpočtu

Zapojte do procesu ministerstvo / tvůrce politik, aby porozuměli zásadním rozdílům mezi tím, jak se hlášení v eRegistry odehrálo dříve a nyní

> _Reference_:
>
> Venkateswaran M: Atributy a důsledky údajů ze zdravotnických informačních systémů pro předporodní péči - zdravotní stav, výkon a politika zdravotního systému, disertační práce, University of Bergen
>
> Venkateswaran M, Mørkrid K, Khader KA, Awwad T, Friberg IK, Ghanem B, Hijaz T, Frøen JF: Porovnání individuálních klinických údajů z prenatálních záznamů s rutinními indikátory zdravotnických informačních systémů pro předporodní péči na Západním břehu: kříž -sekcionální studie. PloS one 2018, 13 (11): e0207813
