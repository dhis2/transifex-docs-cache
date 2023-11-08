---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/edit/master/chapters/introduction.md" 
---
# Úvod

Trasovač je aplikace v rámci platformy DHIS2, která umožňuje zaznamenávat a používat jednotlivá dlouhodobá data. Funkce Trasovače pokrývá široké spektrum potřeb, od sledování kvality a dostupnosti vodních zdrojů, přes sběr docházky studentů ve třídě, až po sběr údajů o pacientech do sdíleného zdravotního záznamu. Pro účely této příručky bude mnoho příkladů pocházet ze zdravotnických systémů, ačkoli Trasovač je široce používán také pro vzdělávací systémy, environmentální systémy, logistiku a další.

Mnoho zemí a programů využívá zvýšenou dostupnost sítě a rozsáhlou přítomnost mobilních zařízení a dalšího hardwaru k posouvání informačních systémů blíže úrovni, kde se generují primární data. Data na úrovni jednotlivců přidávají do informačních systémů podrobnost a nuance, poskytují příležitosti pro analýzu ad hoc, přesouvají indikátory v průběhu času a zlepšují kvalitu dat. Kromě užitečnosti pro podávání zpráv a analýzu lze údaje na úrovni jednotlivců také použít k eliminaci nadbytečnosti hlášení, posílení postavení zaměstnanců na nižší úrovni lepšími nástroji pro rozhodování a umístění klienta do středu informačního systému. Stručně řečeno, data na úrovni jednotlivce jsou nejmenší datovou jednotkou a jako taková mohou být v mnoha ohledech upravena tak, aby uspokojila různé konkurenční potřeby národních informačních systémů.

Účelem této příručky je pomoci určit, zda je Trasovač vhodný pro případ možného použití, a poskytnout praktické pokyny, které vám pomohou naplánovat úspěšné implementace. Použití nástroje Trasovač ve velkém měřítku zavádí další faktory, které by měly být plánovány nad rámec toho, co již může existovat pro existující agregovanou instanci DHIS2. Příležitosti a potenciální výhody informačních systémů se zvyšují, jak systém přechází od agregovaných dat → sledovaná anonymní data → data od identifikovatelných osob → data pacientů v reálném čase v místě péče. Ti, kdo plánují implementaci Trasovače, by si měli uvědomit, že výzvy narůstají spolu s výhodami.

Tento průvodce implementací poskytne doporučení, která vám pomohou:

-  určit, zda Trasovač dokáže řešit vaše potřeby
-  vyhodnotit připravenost vašeho nastavení na zavedení sběru dat na individuální úrovni
-  pochopit, jak se implementace nástroje Trasovače liší od agregátu DHIS2
-  ocenit obavy specifické pro datové systémy na úrovni jednotlivců, včetně ochrany soukromí a zabezpečení
-  přezkoumat poučení a osvědčené postupy odvozené z případů použití v reálném světě
-  plánovat zavedení svých programu(ů) Trasovače v požadovaném měřítku
-  nastavit infrastrukturu, která bude v průběhu času udržovat program Trasovač

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

## K čemu lze Tracker použít?

Stejně jako u zbytku platformy DHIS2 má Trasovač obecný datový model, který umožňuje jeho konfiguraci uživatelem pro mnoho různých účelů. Trasovač ve své nejzákladnější podobě umožňuje uživateli definovat konkrétní druh věcí (osoba, komodita, laboratorní vzorek, spádová oblast atd.), které chce v průběhu času sledovat (trasovaná entita), definovat data, která chtějí shromažďovat informace o této entitě (datové prvky), umístit datové prvky v určitém pořadí a s jakýmikoli doprovodnými podmínkami nebo logikou (program, pravidla programu) a určit analytiku, která by měla být vytvořena (indikátory programu, zprávy o událostech, vizualizace dat atd. .)

Příkladem jednoduchého programu Trasovače může být program pro sběr informací o případech malárie v místě péče. Trasovanou entitou by byla osoba definovaná atributy, jako je křestní jméno, příjmení, datum narození nebo vesnice. Program by obsahoval datové prvky, jako jsou příznaky, použitý test a výsledek, poskytované ošetření atd. Tyto datové prvky mohou mít předem nakonfigurované možnosti pro možné reakce, jako jsou možné testy, nebo logiku, která pomáhá zajistit kvalitu dat, jako je to možné minimální a maximální hodnoty pro daný datový prvek. Shromážděné údaje by byly viditelné pro klinického uživatele jako součást sdíleného zdravotního záznamu pacienta s malárií, ale mohly by být použity také ke generování měsíčních zpráv požadovaných národním programem kontroly malárie, poskytování podpory při rozhodování klinickému lékaři, generování SMS připomenutí pacienta na podporu dodržování léčby nebo naplnění klinického panelu obsahujícího klíčové indikátory výkonu. Pro všechny tyto účely byly údaje shromážděny pouze jednou - během návštěvy pacienta -, ale byly opakovaně použity pro různé potřeby.

DHIS2 také podporuje sběr jednotlivých dat bez dlouhodobého trasování pomocí aplikací Zachycení dat a Události. Na krátkodobé trasování bude v této dokumentaci odkazováno také a následuje většinu stejného datového modelu jako trasovač, s výjimkou definování trasované entity, která není požadovanou součástí krátkodobého trasování. Příkladem takového programu událostí může být hlášení stejných údajů o malárii od jednotlivců jako v předchozím programu (trasovaná entita), ale bez propojení těchto údajů s konkrétním pacientem. Data by se tak nestala součástí sdíleného zdravotního záznamu (nebo by se možná nepoužila ke generování připomenutí SMS zpráv pacientovi nebo jiných funkcí, které se spoléhají na sledování entity v průběhu času), ale mohla by se použít i různá další použití dat stále lze využít.

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


## Ukázkové uživatelské případy použití trasovače

V této příručce budeme odkazovat na příklady použití, abychom uvedli skutečné příklady plánovacích principů, rozhodovacích bodů, využití softwaru a dat, společných překážek a problémů a poznatků získaných v různých fázích procesu plánování a implementace Trasovače. Zde je uvedeno krátké úvodní shrnutí těchto jednotlivých případů použití. Podrobnější informace o některých případech použití naleznete na webu www.dhis2.org.

### Předkonfigurované trasovací balíčky

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

### Botswana: Program výživy a imunizace

Botswana vytvořila kombinovaný program výživy a imunizace poskytující klíčové služby malým dětem, které dostávají výživovou pomoc, a zároveň zajišťuje, aby děti dosahovaly svých růstových ukazatelů a dostávaly celou sadu vakcín. Ve spolupráci s týmem Botswany byla vylepšena platforma Trasovače tak, aby vytvářela standardizovaná z-skóre poskytující rychlé hodnocení hmotnosti ku výšce, hmotnosti ku věku a výšky ku věku.

### Ghana: HIV / ART a další moduly eTracker

Od roku 2012 vede Ghana Health Services průkopnický program v oblasti hlášení údajů na úrovni pacientů prostřednictvím programů DHIS2 Tracker („eTrackers“). Od roku 2019 používali 8 různých modulů eTracker. Ukázkovým příkladem je jejich HIV / ART eTracker, který sleduje jednotlivé pacienty prostřednictvím testování a léčby a usnadňuje zdravotnickým pracovníkům identifikaci a sledování neplatičů a zároveň podporuje tok hlášení agregovaných údajů o HIV, který v Ghaně probíhá od roku 2006.

### Palestina: elektronická registrace zdraví matek a dětí

Každá žena v Palestině má přidělenou kliniku primární zdravotní péče a pokud tato klinika neposkytuje služby, které potřebuje, je požádána, aby navštívila kliniku vyšší úrovně. Tento systém doporučení vyžaduje eRegistry, která kontroluje přístup k souborům klinických pacientů, podporuje kontinuitu péče napříč různými místy zdravotní péče, umožňuje zadávání dat z několika různých bodů a poskytuje analytiku, která pomáhá řídit rozhodnutí podle pokynů předporodní péče Palestiny. Naše spolupráce s Palestinou začala v roce 2014. Vývoj a implementace eRegistry zdraví matek a dětí (MCH) zahrnovaly iterativní přístup a dynamický dialog mezi vývojáři, tvůrci politik, úředníky v oblasti veřejného zdraví a poskytovateli zdravotní péče. Tato implementace zahrnuje rozsáhlé využití automatizovaných SMS zpráv ke komunikaci s pacienty a také ovládací panely pro zlepšení kvality pro měření výkonu klinik a podporu poskytování kvalitní péče.

### Zimbabwe: Národní program kontroly malárie

Implementace nástroje DHIS2 Android Tracker v Zimbabwe začala v roce 2014 jako projekt spolupráce mezi Národním programem pro kontrolu malárie (NMCP) a univerzitou v Oslu a od té doby byla rozšířena tak, aby pokrývala téměř polovinu více než 60 okresů v zemi. Tato implementace zahrnuje offline sběr dat, podrobné údaje o poloze a sběr a analýzu dat téměř v reálném čase a je příkladem práce s více zúčastněnými stranami na globální úrovni s cílem vyvinout program s potenciálem pro expanzi napříč geografickými regiony a oblastmi onemocnění.



