---
edit_url: "https://github.com/dhis2/dhis2-android-docs/blob/main/content/implementation-guide/scale-up.md"
revision_date: '2022-01-07'
tags:
- Implementace
---

# Rozšiřování škálováním { #implementation_guide_scale_up }

## Akvizice { #implementation_guide_scale_up_acquisitions }


Nyní, když jste provedli veškeré své testování a svůj pilotní projekt, jste připraveni rozšířit své nasazení, pro které budete muset provést pořízení hardwaru a nezbytných služeb. Budete se muset rozhodnout ohledně:

- Nákup zařízení vs BYOD (přineste si vlastní zařízení)
- Distribuce aplikace (nyní a později)
- Telekomunikační smlouvy

**Nákup zařízení vs. BYOD (přineste si vlastní zařízení)**

Zpočátku byste si měli koupit různá zařízení, abyste uživatelům umožnili je vyhodnotit a poskytnout vám zpětnou vazbu. Jakmile je rozhodnuto o zařízení, které budete používat, měli byste si koupit pouze 10 nebo méně jednotek, nebo cokoli, co je potřeba pro testování a pilotní fázi. Teprve když se pilot blíží ke konci, měli byste si koupit vybavení pro zavádění dalších 6 měsíců. U některých velmi velkých projektů bude národní zavedení trvat roky a váš plán získávání hardwaru by se měl v průběhu let rozšiřovat. Doporučení týkající se technických specifikací zařízení jsou v kapitole [Specifikace mobilních zařízení](#mobile_specs).

Měli byste zvážit proveditelnost použití zásady BYOD - tento formát umožňuje uživatelům přinést si svá vlastní zařízení, pokud splňují minimální technickou normu, kterou pro svůj projekt definujete. Obvykle nabídnete nějaký druh pobídky, pravděpodobně ve formě eCash nebo telefonního kreditu. Výhody tohoto přístupu jsou zřejmé: vyhýbá se velkým počátečním nákladům na pořízení a snižuje náklady na správu a logistiku. Na druhou stranu vás čeká výzva velmi heterogenního hardwarového prostředí, což znamená různá zařízení a verze OS Android. To ovlivní hlavně proces ladění.

**Distribuce aplikace** (nyní a později)

Aplikace DHIS 2 pro Android má nové vydání každých pár týdnů. Každá nová verze obsahuje opravy chyb a může obsahovat nové funkce. Mohlo by to také obsahovat nové chyby. Nové verze jsou publikovány v GitHubu i v obchodu Google Play. Github je pouze úložiště: stáhnete si konkrétní soubor APK a nainstalujete ho do svého zařízení. K instalaci souboru APK budete muset povolit použití oprávnění třetích stran. Jakmile se APK stáhne z GitHubu nebo jiným způsobem, nainstalovaná verze se nikdy automaticky neaktualizuje. Na druhou stranu, pokud instalujete z Google Play, obvykle se automaticky aktualizuje na nejnovější verzi. V případě potřeby je možné deaktivovat automatickou aktualizaci v gPlay.

Jakmile dokončíte své testovací a školicí materiály a spustíte zavádění, nechcete, aby se verze aplikace u žádného z uživatelů změnila, pokud novou verzi znovu neotestujete. Změny verze mohou zahrnovat upravené uživatelské rozhraní, chybné chování nebo nekompatibilitu s verzí serveru DHIS 2. Chcete nové verze důkladně otestovat, než je pošlete svým uživatelům, abyste se ujistili, že nová verze nezpůsobí vaší konfiguraci žádné problémy, vyžaduje přeškolení, vyžaduje změny vaší konfigurace.

Stručně řečeno, u jakékoli instalace, která zahrnuje značný počet zařízení, byste se měli vyhnout používání Google Play a místo toho použít řešení pro správu mobilních zařízení (MDM), o kterém pojednáváme v [této kapitole](#scale_up_mdmt). Pokud nemáte přístup k této možnosti, můžete zvážit použití Google Play, ale měli byste deaktivovat automatickou aktualizaci pro aplikaci DHIS 2 pro Android. Postup, jak to provést, se mění podle verze systému Android - google „jak zakázat automatickou aktualizaci systému Android pomocí aplikace v Andrid X.X“.

**Telekomunikační smlouvy**

Pokud vaše instalace plánuje zahrnout použití SMS pro přenos vybraných záznamů prostřednictvím SMS, když mobilní data nejsou k dispozici, budete muset uzavřít smlouvu s místním agregátorem, který vám může poskytnout příchozí číslo pro příjem SMS. Měli byste nakonfigurovat svůj server tak, aby přijímal a odesílal SMS - viz připojení [dokumentace DHIS 2](https://docs.dhis2.org/master/en/user/html/mobile_sms_service.html#) o připojeních SMS. Abyste mohli předpovědět měsíční náklady, budete muset odhadnout počet zpráv za měsíc.

Proces výběru a podpisu smlouvy s poskytovatelem SMS se v jednotlivých zemích liší a závisí na postupech nákupu vaší organizace.

### Plánování velkých akvizic { #implementation_guide_scale_up_planning }

Každý projekt bude vyžadovat kombinaci typů zařízení: telefony, tablety a Chromebooky. Většina mobilních zařízení bude pravděpodobně přidělena vyhrazenému uživateli. Je třeba vzít v úvahu povahu práce. Například komunitní pracovníci budou používat chytré telefony nebo tablety. Zdravotničtí pracovníci, kteří pracují v zařízení, však mohou upřednostňovat tablet s externí klávesnicí nebo Chromebook.

Skutečné získávání ve velkém by mělo být co nejvíce odloženo. Zpočátku je doporučeno zakoupit co nejméně zařízení pro testování konfigurace a poskytnout určitou úroveň výběru budoucím uživatelům. Jakmile je dohodnuto rozhodnutí přejít na pilotní projekt, měl by být druhý nákup v ideálním případě omezen na zařízení potřebná pro pilota. Pokud plán zavádění trvá déle než rok, měla by být akvizice zařízení také rozdělena do několika období: výrobci neustále nabízejí lepší zařízení za stejnou cenu v cyklech, které se pohybují mezi 12-18 měsíci.

Příklad celkového pořízení 100 až 1000 zařízení.

|Měsíc projektu|Fáze|Získávání|# zařízení|
|---|---|---|---|
|2. měsíc|Návrh a počáteční konfigurace|Vyberte 3 nebo 4 možné tvarové faktory. Nakupujte od jednoho nebo dvou výrobců|2-8|
|4-6 měsíců|Pilot|Kupte pouze zařízení potřebná k dokončení pilotního projektu|10-30|
|6-12. měsíc|Zavádění - fáze 1|První hromadné získávání|50-500|
|Měsíc X|Zavádění fáze X|-->|50-500|
|36-48 měsíc|Výměna upgradu|Vyměňte zařízení|X|

## Správa mobilních zařízení { #implementation_guide_scale_up_mdm }


Správa mobilních zařízení označuje software používaný ke správě mobilních zařízení. Software MDM budete potřebovat, když budete muset podporovat stovky zařízení a bude nutné řídit distribuci souborů apk mezi zařízeními, poskytovat technickou podporu a prosazovat institucionální zásady. Většina možností je nabízena jako služby s měsíčním poplatkem. Některé bezplatné aplikace nabízejí režim veřejného terminálu, ale za základní vzdálenou správu si účtují měsíční poplatek.

Požadované funkce softwaru MDM lze klasifikovat jako základní a pokročilé. Zde je seznam požadovaných funkcí:

- Základní vlastnosti:
  - Vyžaduje heslo pro zámek obrazovky
  - Poskytování autorizovaných aplikací
  - Zamkněte zařízení a vymažte informace, pokud dojde ke ztrátě nebo odcizení
  - Ovládejte aktualizaci aplikace pro Android
  - Vynutit zásady zálohování
- Pokročilé funkce:
  - Vynutit zásady síly hesla
  - Prosazovat zásady používání sítě
  - Sledovat polohu zařízení
  - Omezený přístup k nastavením a funkcím (příklad - wifi / síť, snímání obrazovky)

Při rozhodování, který je nejlepší software MDM pro vaše potřeby, byste se měli pokusit odpovědět na následující otázky:

- Kolik zařízení musím spravovat?
- Jak často mám fyzický přístup k zařízení?
- Které funkce opravdu potřebuji?
- Které zásady musím implementovat
- Jak těžké bude instalace a údržba
- Jak to ovlivní uživatelskou zkušenost?
- Musíme povolit BYO? (BYO: Přineste si vlastní zařízení).
- Jak to ovlivní zařízení?

Na další stránce najdete seznam dostupného softwaru MDM (mějte prosím na paměti, že ceny a podmínky se budou časem měnit).

- Mobilock Free (nelze aktualizovat software)
- SOTI (MobiControl) (může být drahý - 2,20 $ / zařízení / měsíc)
- Miradore (bez vzdálené podpory)
- Applock (nelze ovládat aktualizaci softwaru)
- AcDisplay (nelze ovládat aktualizaci softwaru)
- F-Droid (nelze omezit spotřebu dat)
- APPDroid (nelze omezit spotřebu dat)
- Master List (nelze ovládat aktualizaci softwaru)
- Firebase (nelze omezit spotřebu dat)
- Intunes (uživatelé musí být součástí nasazení MS Office 365)
- MobileIron (může být drahý - 3,15 USD / zařízení / měsíc \+ 2,368 USD za nasazení)
- IBM Maas360 (příliš drahé - 1,60 USD / zařízení / měsíc \+ 0,50 USD / zařízení / měsíc pro vzdálenou podporu, pro 3.000 zařízení)
- AirWatch (nereaguje a může být drahý - 3,80 USD / zařízení / měsíc pro 3000 zařízení po dobu 3 let)
- XenMobile (Citrix) (může být drahý - 2,03 USD / zařízení / měsíc pro 3000 zařízení)
- Good for Enterprise (Blackberry) (může být drahé - 2 USD / zařízení / měsíc \+ 2,5K USD za nasazení)

> **Poznámka**
>
> Další informace o tomto tématu naleznete v [Pokynech pro správu mobilních zařízení](https://docs.dhis2.org/en/implement/managing-mobile-devices/considerations.html).

## Výcvik { #implementation_guide_scale_up_training }


Důležitým krokem před zahájením, je školení uživatelů a v případě potřeby školení týmů poskytujících podporu uživatelům. Existuje mnoho tréninkových strategií, kterými se můžete řídit, a bude to záviset na velikosti skupiny, kterou je třeba trénovat, na jejich úrovni dovedností, dostupném časovém rámci, rozpočtu atd. Je důležité, abyste při navrhování věnovali čas a energii svou tréninkovou strategii a věnujte dostatek času splnění vašich tréninkových cílů. Dobře vyškolení a informovaní uživatelé sníží úzkost uživatelů a problémy s adaptací a také zvýší kvalitu shromážděných dat.

### Technické přípravy na školení { #implementation_guide_scale_up_techinical_prep }


Při přípravě na školení se ujistěte, že byly splněny všechny praktické technické požadavky. To zahrnuje připravenost tabletů / mobilních zařízení s nainstalovanou novou aplikací pro Android DHIS 2 Capture. V závislosti na dostupnosti připojení k internetu v oblasti, kde trénink provádíte, můžete mít všechny tablety předem synchronizované se serverem, abyste měli dostatek dat a správnou konfiguraci pro školení. Před provedením školení, by měla být cvičení testována, aby bylo zajištěno, že vše funguje. Odstraňte problémy zjištěné během testování, aby se neobjevily během tréninku. Možná budete chtít provést druhé kolo testu, abyste zjistili případné problémy které jste nezachytili v prvním kole.

Pokud se školení provádí s předem synchronizovanými daty a konfigurací, na konci školení nezapomeňte umožnit účastníkům vyzkoušet aplikaci, která přistupuje ke vzdálenému serveru DHIS 2. To poskytne účastníkům možnost vyzkoušet si synchronizaci v reálném životě, která může zahrnovat zpoždění v síti. Bez zpoždění mohou později interpretovat zpoždění sítě jako poruchy svého zařízení.

### Rozpočet na školení { #implementation_guide_scale_up_budget }


Následuje několik pokynů k přípravě rozpočtu, které jsou převzaty z [pokynů DHIS 2 Community Health Information System Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/CHIS+Guidelines+En.pdf) vydané Univerzitou v Oslu:

- Dodržujte zásady organizace při používání schválených rozpočtových šablon a sazeb (nepřímé, DSA atd.) Pro všechny výdaje, včetně:
  - Cestovní náklady (např. palivo, pronájem auta, ubytování)
  - Osobní náklady (např. diety, náklady na jídlo)
  - Místo konání (např. konferenční prostor, čajové přestávky)
  - Materiály (např. tisk, hardware, projektory)
  - Různé předměty
- Sestavte rozpočet na základě výpočtů potřebných materiálů v listu, jednotkových nákladů na tento materiál a počtu potřebných jednotek. Můžete také zabudovat další multiplikátory pro ilustraci počtu jednotek na účastníka. To umožňuje flexibilitu při aktualizaci rozpočtu, pokud se změní jednotkové náklady nebo se zvýší nebo sníží počet účastníků.
- Předpokládané výdaje rozpočtu v místní měně s integrovaným konverzním kurzem (který lze podle potřeby aktualizovat) pro převod na požadovanou měnu vaší organizace nebo financujícího subjektu. (2).

### Školicí program { #implementation_guide_scale_up_agenda }


Dokumenty [DHIS 2 Community Health Information System Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/CHIS+Guidelines+En.pdf), dokument napsaný od University of Oslo doporučuje zvážit:

1. Požadovaný typ sezení (kulatý stůl, jednotlivé stoly atd.).
2. Technologické požadavky (všechny počítače, šířka pásma Wi-Fi atd.),
3. Financování příspěvků na konferenční centrum, jídlo a nápoje účastníků
4. Trenéři potřebují prostor, aby mohli chodit, aby mohli každého účastníka pozorovat a pomáhat mu.

Uvědomte si počet účastníků, které na každém školení očekáváte, protože bude nutné poskytnout dostatečné materiály a prostor. Prostor pro akce by měl být dostatečně velký pro skupinu a také vhodný pro plánované aktivity.

### Školicí materiály { #implementation_guide_scale_up_materials }


Ve stejném dokumentu najdeme také doporučení pro školicí materiály, které zde uvádíme. Materiály, které budete potřebovat pro vaše školení, budou záviset na vašich aktivitách. Abyste se ujistili, že plánujete všechno, projděte si s partnerem svou tréninkovou agendu a prodiskutujte, co se bude dělat pro každou část školení, a vezměte na vědomí potřebné materiály.

Program školení by měl být definován s dostatečným předstihem před zahájením školení a zahrnut do distribuovaných materiálů.

Uživatelská dokumentace by měla být přibalena v Minimálních příručkách. Tyto příručky vysvětlují konkrétní pracovní úkol (např. Zadávání měsíčních údajů z registru zdraví vesnic nebo porovnání zdraví ve vaší vesnici se sousedními vesnicemi). Po vysvětlení pracovního úkolu poskytuje Minimální Příručka číslované podrobné pokyny se snímky obrazovky, aby uživatelé rozpoznali, co mají dělat. Mějte na paměti, že Minimální příručky NEVYSVĚTLUJÍ funkčnost aplikace, jednu po druhém, jako typická uživatelská příručka dodavatele. Vzhledem k tomu, že uživatelé dávají přednost zkoušení a ne čtení, měly by být příručky co nejkratší a zároveň obsahovat všechny kroky.

