---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/chapters/building-your-tracker-programs.md"
revision_date: "2021-01-14"
---

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
- Identifikujte trasované entity, rozsah sběru dat a zdravotní kádry zapojené do sběru dat.
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
