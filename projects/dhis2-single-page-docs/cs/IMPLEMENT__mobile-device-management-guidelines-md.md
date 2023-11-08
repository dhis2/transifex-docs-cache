---
revision_date: "2021-05-10"
template: single.html
---

# O této příručce { #about*this_guide* }

<!--DHIS2-SECTION-ID:about_this_guide_-->

Dokumentace DHIS 2 je společným úsilím a byla vyvinuta vývojovým týmem a uživateli. Zatímco se průvodce snaží být kompletní, mohou existovat určité funkce, které byly vynechány nebo které je ještě třeba zdokumentovat. Tato část vysvětluje některé konvence, které se v celém dokumentu používají.

DHIS 2 je aplikace založená na prohlížeči. V mnoha případech byly pro lepší přehlednost zahrnuty snímky obrazovky. Jsou zobrazeny zástupce různých funkcí, například **Datový prvek** \> **Skupina datových prvků**. Symbol „\>“ označuje, že byste měli kliknout na **Datový prvek** a poté kliknout na **Skupina datových prvků** v uživatelském rozhraní.

K zvýraznění důležitých částí textu nebo konkrétních typů textu, například zdrojového kódu, byly použity různé styly textu. Níže jsou vysvětleny všechny konvence použité v dokumentu.

> **Poznámka**
>
> Poznámka obsahuje další informace, které je třeba vzít v úvahu, nebo odkaz na další informace, které mohou být užitečné.

> **Tip**
>
> Tip může být užitečnou radou, například jak provádět konkrétní úkol efektivněji.

> **Důležité**
>
> Důležité informace by neměly být ignorovány a obvykle označují něco, co vyžaduje aplikace.

> **Pozor**
>
> Informace obsažené v těchto částech by měly být pečlivě zváženy, a pokud nebudou dodržovány, mohou mít za následek neočekávané výsledky analýzy, výkonu nebo funkčnosti.

> **Varování**
>
> Pokud nebudou informace obsažené v těchto částech zohledněny, mohou mít za následek trvalou ztrátu dat nebo ovlivnit celkovou použitelnost systému.

> **Dokončeno**
>
> Informace obsažené v těchto částech naznačují, že se jedná o problémy, které byly plně implementovány.

> **Neúplné**
>
> Informace obsažené v těchto částech naznačují, že se jedná o problémy, které nejsou implementovány a budou ignorovány.

> **Not_applicable**
>
> Informace obsažené v těchto částech naznačují, že se jedná o problémy, které nelze použít.

> **Work_in_progress**
>
> Informace obsažené v těchto částech naznačují, že se jedná o problémy nebo chování, které nejsou zcela implementovány nebo již byly hlášeny neočekávané chování.

    Výpisy programů obvykle obsahují určitý typ počítačového kódu.
    Budou zobrazeny se stínovaným pozadím a jiným písmem.

`Příkazy budou zobrazeny tučně a budou představovat příkaz, který je třeba provést v operačním systému nebo v databázi.`

Odkazy na externí webové stránky nebo křížové odkazy budou zobrazeny modrým textem a podtrženy jako [tady](http://www.dhis2.org).

<!--
Bibliografické odkazy se zobrazí v hranatých závorkách, jako je tento
Store2007. Úplný odkaz je uveden v obsažené bibliografii
na konci tohoto dokumentu.
-->

# Considerations {# mdm_considerations }

V tomto dokumentu budou pojmy MDM a EMM použity zaměnitelně. To není úplně přesné, ale slouží to ke zjednodušení dokumentu. MDM samo o sobě nezohledňuje nasazení aplikací, zatímco EMM zahrnuje mnohem více možností, které nejsou v rozsahu tohoto dokumentu. Proto lze říci, že tento dokument pokrývá někde mezi těmito dvěma pojmy.

![Rozdíly MDM/EMM](resources/images/mdm-image7.png)

## Proč MDM pro DHIS2? {# mdm_considerations_why }

Správa mobilních zařízení označuje software používaný ke správě mobilních zařízení. Pravděpodobně budete chtít používat software MDM, když budete muset podporovat stovky zařízení a bude nutné řídit distribuci aplikace DHIS2 mezi zařízeními, poskytovat technickou podporu a vynucovat institucionální zásady.

Například pokud máte projekt, kde bude distribuováno 1000 zařízení Android (komunitní pracovníci) pomocí mobilních dat k odeslání informací na centrální server DHIS2, může vám MDM pomoci:

- Možnost vydat novou verzi aplikace DHIS2 pro Android kdykoli budete chtít. Všimněte si, že ve výchozím nastavení mohou být zařízení nakonfigurována na automatickou aktualizaci nebo budete možná muset požádat o manuální aktualizaci od uživatele. MDM vám dává možnost vybrat si, zda chcete zařízení v daném okamžiku aktualizovat, nebo raději čekat (například dokud neprovedete školení vysvětlující nové možnosti aplikace).
- Vyhledejte a sledujte zařízení v případě ztráty nebo je na dálku otřete v případě, že mohou obsahovat citlivé informace. Přestože aplikace pro Android DHIS2 již obsahuje bezpečnostní opatření, pokud jsou telefony používány ke shromažďování některých obrázků z aplikace (například jednotlivců, lékařských zpráv atd.), Může představovat ohrožení soukromí / bezpečnostní riziko.
- Zakažte použití mobilních dat pro libovolnou aplikaci kromě aplikace pro Android DHIS2 nebo zakažte možnost používat bezdrátový hotspot, aby se datové balíčky zakoupené projektem spotřebovaly pouze pro DHIS2.

## Jak funguje MDM? {# mdm_considerations_how_it_woks }

Tato část vysvětluje opravdu stručně, jak MDM / EMM funguje a jak může ovlivnit současnou infrastrukturu implementace DHIS2.

V implementaci bez MDM komunikují zařízení jedinečně a přímo se serverem DHIS2, jak je znázorněno na obrázku níže.

![Standardní komunikační proces mezi DHIS 2 Android APP a DHIS 2 serverem](resources/images/mdm-image9.png)

Přidání MDM ovlivní infrastrukturu, protože bude přidán nový server. Tento server může být buď v lokálních prostorách (pokud to řešení podporuje), nebo v cloudu. Ačkoli se to nedoporučuje ve skutečně konkrétních případech (malá nasazení nebo omezení rozpočtu), server používaný k hostování DHIS2 lze také použít, takže bude potřeba pouze jeden server.

Přidání MDM také vyžaduje přidání pozice manažera MDM, což znamená, že k nastavení a správě tohoto MDM je třeba přiřadit osobu. Tento správce implementuje konkrétní konfiguraci na serveru MDM a možná bude nutné nakonfigurovat mobilní zařízení.

![MDM je přidáno do infrastruktury](resources/images/mdm-image12.png)

Konfigurace implementovaná na serveru MDM je načítána zařízeními, což znamená použití specifických zásad na zařízení, která mohou omezovat způsob, jakým lze zařízení používat. V případě potřeby může také umožnit vzdálené sledování nebo vymazání zařízení.

![Zařízení nyní komunikují se dvěma různými servery: DHIS 2 a MDM](resources/images/mdm-image6.png)

Obrázek níže představuje tyto kroky kombinované do jednoho grafu.

![Komunikace v implementaci DHIS 2 s MDM](resources/images/mdm-image5.png)

# Výběr MDM / EMM { #mdm_choosing }

Při rozhodování, které řešení MDM zvolit, je důležité definovat, která sada funkcí bude považována za nezbytnou a které za hezké mít. To se může mezi implementacemi hodně lišit; v níže uvedeném seznamu jsme však identifikovali některé funkce jako povinné z důvodu povahy DHIS2. I když to může být přezkoumáno v závislosti na implementaci, mělo by to být považováno za naše doporučení.

Další podrobnosti najdete v příloze A - Správa mobilních zařízení.

Požadované funkce a jejich důvod:

- Android jako podporovaná platforma:

  To se může zdát zřejmé, ale některá řešení MDM jsou zaměřena na jiné typy zařízení, jako je iOS nebo Windows. V tuto chvíli je aplikace DHIS2 pro Android kompatibilní pouze se zařízeními Android a podporuje od verze 4.4 (nedoporučuje se) a vyšší (doporučujeme od verze 7).

- Správa distribuce aplikace(í):

  Implementace DHIS2 potřebují otestovat a vyškolit uživatele před vydáním nové verze aplikace. Protože většina implementací nainstaluje aplikaci DHIS2 pro Android z obchodu Google Play, je možné při publikování aktualizace zařízení aktualizovat, aniž by byl projekt připraven, pokud není k dispozici žádný jiný mechanismus pro správu aktualizací.

- Informace o zařízení:

  Implementace DHIS2 potřebují udržovat soupis svých zařízení, aby mohly řešit problémy nebo aktualizovat svá zařízení. Všechna zvažovaná řešení MDM zahrnují tuto základní funkci, ale je zde uvedena pouze pro případ, že existuje řešení, které to nemusí zahrnovat.

- Vynucení hesla:

  Ve většině (ne-li všech) implementacích DHIS2 jsou citlivé informace uloženy v aplikaci. Proto vynucování zásad hesla na zařízení může zabránit nežádoucímu přístupu k těmto datům.

      Všimněte si, že navzdory tomu, že aplikace DHIS2 pro Android umožňuje nastavit heslo pro řízení přístupu, protože informace v zařízení ještě nejsou zašifrovány (únor 2020), mohl by je útočník stále extrahovat.

- Vzdálené vymazání:

  Ve většině (ne-li všech) implementacích DHIS2 jsou v aplikaci uloženy citlivé informace. Pokud například dojde ke ztrátě nebo odcizení zařízení, může zajistit, aby bylo možné jej vzdáleně vymazat, zabránit úniku citlivých dat.

Funkce které je pěkné mít a jejich důvod:

- Režim veřejného terminálu (tj. režim jedné aplikace)

  Některé implementace DHIS2 mohou vyžadovat uzamčení zařízení do jedné aplikace (DHIS2 Android Capture App), aniž by uživateli umožnily přístup k jakékoli jiné aplikaci nebo nastavení. Kiosková politika by toho dosáhla.

- Správa telefonu

  V některých implementacích DHIS2 může být nutné poskytovat zařízení se SIM kartami, aby bylo zajištěno datové připojení přes mobilní síť (2G-5G). To může vyžadovat, aby zařízení používala konkrétní volací služby za účelem dobíjení datových balíčků nebo omezenou podporu volání atd.

- Omezení aplikace / nastavení

  Některé implementace DHIS2 mohou vyžadovat, aby uživatelé mohli používat nejen jednu, ale několik aplikací (tj. Zařízení, které je třeba použít pro DHIS2 a snímání obrázků).

- Správa sítě

  Některé implementace DHIS2 mohou vyžadovat, aby zařízení nepoužívala datovou síť nebo se omezovala na konkrétní domény (brána firewall) nebo aby vždy používala pouze konkrétní bezdrátové sítě nebo dynamicky nastavovala bezdrátové sítě atd.

- Správa uživatelů

  Některé implementace DHIS2 mohou vyžadovat, aby zařízení používalo několik uživatelů (dokonce dva uživatelé DHIS2). Funkce správy uživatelů může v tomto scénáři zvýšit úroveň zabezpečení, protože každý uživatel může mít různé přístupové kódy, což umožňuje víceuživatelské účty pro aplikaci DHIS2 Android Capture (aktuálně není nativně podporováno), několik zásad aplikace na uživatele atd.

## Počáteční cena a provozní náklady { #mdm_choosing_initial_price }

Jedním z kritických faktorů, kterým budou projekty čelit při rozhodování, zda chtějí implementovat MDM, je počáteční cena a provozní náklady. MDM může přinést neočekávané náklady, proto se doporučuje vyhodnotit potřebu a zahrnout své náklady co nejdříve do definice projektu a rozpočtu.

Většina řešení MDM uvedených v následujících částech zahrnuje měsíční nebo roční provozní náklady, které by mohly nesmírně zvýšit náklady na projekt v závislosti na počtu zařízení. Proto doporučujeme zvážit některé z následujících tipů:

1. Pokud má projekt kapacitu hostovat řešení MDM na svých serverech, bude obecně představovat lepší možnost než výběr řešení včetně hostování.
2. Někteří dárci mohou požadovat výběr konkrétního řešení MDM, pokud tomu tak je, ujistěte se, že je rozpočet přidělen na budoucí fáze projektu nebo že lze MDM použít zdarma (nebo levněji) s omezenou sadou možností.
3. Většina řešení nabízí různé balíčky jako cenový model, pokud bude řešení používáno hlavně (nebo pouze) ke správě aplikace DHIS2 (instalace a aktualizace), využití bude minimální, takže výběr nejlevnější alternativy bude pravděpodobně stačit.
4. Vzhledem k povaze většiny projektů (zdraví v rozvojových zemích, nevládní organizace, vzdělávání atd.) Bude mnoho poskytovatelů MDM pravděpodobně schopno nabídnout slevu. Vyjednávání před výběrem řešení je vysoce doporučeno, protože při psaní tohoto dokumentu mnoho poskytovatelů projevilo zájem a již nabídlo lepší nabídky, než bylo oznámeno na jejich stránkách.

## BYOD / firemní zařízení { #mdm_choosing_byod }

Dalším klíčovým faktorem při rozhodování, který MDM / EMM použít, je zvážit, zda nasazení bude zahrnovat zásadu BYOD (Bring Your Own Device) nebo bude fungovat pouze s podnikovými zařízeními. To může být kritický faktor, protože většina MDM se bude lišit v zásadách, které lze použít na tyto dva typy zařízení. Mnoho implementací DHIS2 je založeno na pouze podnikových zařízeních, ale v některých implementacích může být možná smíšená politika BYOD-Corporate nebo dokonce úplná BYOD zařízení.

Nastavení BYOD znamená mít MDM, který umožňuje minimální sadu zásad vyhovujících výše uvedeným povinným funkcím. V závislosti na MDM to může vyžadovat pracovní profil, kde by měla být nainstalována aplikace DHIS2. V těchto implementacích může být školení ještě důležitější, aby bylo možné vysvětlit rozdíly mezi profily. Například uživatel s aplikací DHIS2 nainstalovanou ve svém osobním profilu (stejně jako v pracovním profilu) by přidal další rizika zabezpečení dat, protože všechna data uložená v jeho osobním profilu nemohla být vzdáleně vymazána, pokud by došlo ke ztrátě nebo odcizení zařízení .

Firemní nastavení zařízení bude znamenat, že všechna zařízení budou podléhat přísnější sadě zásad (může se u různých zařízení / uživatelů / umístění lišit). Toto je ideální situace z pohledu správy IT, ale ovlivní to flexibilitu a náklady.

# Srovnávací graf { #mdm_comparison }

Následující tabulka (upravená ze [Seznam softwaru pro správu mobilních zařízení](https://en.wikipedia.org/wiki/List_of_Mobile_Device_Management_software)) má za cíl shrnout veškerý obsah tohoto dokumentu a může být užitečný pro rychlý přehled. Doporučuje se však projít si celý dokument, abyste pochopili všechny výhody a nevýhody zde navrženého MDM.

Všechna prezentovaná řešení splňují dříve definované jako požadované funkce:

- Android jako podporovaná platforma
- Minimální funkce:
  - Správa aplikací
  - Vzdálené vymazání
  - Vymáhání bezpečnosti (min. heslo)
- Cena je velmi přibližná, protože závisí na konkrétních konfiguracích.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MDM Název** <br />(testované) | **(C)loudové / (P) Lokální** | **Cena cca** | **Intenzita** | **Slabé stránky** | **Další komentáře** |
| <u>Flyve MDM</u> | C / P | – Zdarma\* (pokud je hostováno) <br /> – 350 $ / měsíc (bez omezení na zařízení) | - Open Source <br />-GLPI plugin | - Sada funkcí | - Pokud se GLPI již používá, může to být opravdu zajímavá možnost <br /> - Podporované funkce mohou být omezením |
| <u>Headwind MDM</u> | C / P | - Zdarma \ * (pokud je hostitelem) <br /> - 1990 USD / 1. rok + 500 USD každý druhý rok | - Open Source <br />- Java App (jako DHIS 2) | Bezplatná verze může některé funkce vynechat |  |
| <u>Entgra EMM</u> | C/P | - Zdarma \ * (pokud je hostován) <br /> - cena za SaaS není diskontována | - Open Source <br /> - aplikace Java (jako DHIS2) |  |  |
| <u>TinyMDM</u> | C | 22 $ / zařízení / rok. | - Snadné použití <br /> - Jednoduché, ale výkonné funkce <br /> - konfigurace Android Zero |  | - Konfigurace Android Zero může pomoci při nasazení na velké množství zařízení.<br /> - Zákaznická podpora nabízí slevu |
| <u>Miradore</u> | C | 24 $ / zařízení / rok | - NFC a hromadné poskytování <br /> - Android Zero | Plný potenciál se zařízeními Samsung | Při testování byla administrátorská konzole trochu pomalá. <br />- Dostupné slevy |
| <u>Scale Fusion</u> | C | 24 - 36 $ / zařízení / rok | - Hromadné poskytování <br /> - Android Zero <br /> - Mnoho funkcí <br /> - Vzdálené odesílání <br /> - Vzdálená podpora chatu a hovorů |  | Dříve známý jako MobiLock |
| <u>Manage Engine</u> | C / P | - 10-24 $ / zařízení / rok <br /> - zdarma pro <25 zařízení | - Mnoho funkcí a možností <br /> - Android Zero <br /> - vzdálený chat a odesílání |  | Lokální verze vyžaduje Windows, což může být silná nebo slabá stránka vzhledem k současné architektuře, i když DHIS2 je podporován pouze v Linuxu, takže by byl nezbytný jiný server. |
| <u>Focus MDM</u> | C | - 12-24 $ / zařízení / rok <br /> - Slevy po 1,5 000 zařízení | - Pěkná konzole <br /> - Android Zero <br /> | - Mnoho funkcí (distribuce aplikací, kiosk atd.) je k dispozici pouze s plnou kontrolou <br /> - Služby Google Play jsou povinné | - Dostupné slevy <br /> |
| **Název MDM** <br /> (**není** testováno) | **(C)loudové / (P) Lokální** | **Cena cca** | **Intenzita** | **Slabé stránky** | **Další komentáře** |
| Air Watch | C | 4 $ / zařízení / měsíc |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| BlackBerry UEM 12.12 | C / P | ? |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| AppTech360 | C / P | 2 $ / zařízení / měsíc |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| Hexnode | C / P | 1 $ / zařízení / měsíc |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| Kaspersky Endpoint Security | C / P | ? |  |  | Vyhovuje požadovaným vlastnostem a vlastnostem které je dobré mít <br /> Možná by stálo za prozkoumání, pokud je toto řešení již zavedeno |
| Ivanti | C | ? |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| MaaS360 | C | 4 $ / zařízení / měsíc |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| MobileIron | C / P | ? |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| Cisco Meraki Systems Manager | C | ? |  |  | Vyhovuje požadovaným vlastnostem a vlastnostem které je dobré mít <br /> Možná by stálo za prozkoumání, pokud je toto řešení již zavedeno pro síťová zařízení |
| SureMDM | C / P | 4 $ / zařízení / měsíc |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| Správa koncových bodů Citrix | C / P | ? |  |  | Vyhovuje požadovaným a hezkým vlastnostem |
| **Název MDM** <br />(Ostatní správci účtů) | **(C)loudové / (P) Lokální** | **Cena cca** | **Intenzita** | **Slabé stránky** | **Další komentáře** |
| Microsoft InTune | C | 6 $ / zařízení / měsíc | Robustní | Opravdu drahé, i když jen jako MDM | To se liší od MDM pro Office 365, který poskytuje menší sadu funkcí (nezahrnuje správu aplikací). <br />Může být ideálním řešením, pokud projekt již používá Microsoft (E3 nebo E5), protože je součástí. Jinak by pravděpodobně nemělo být bráno v úvahu. |
| Správa koncových bodů (Google G Suite) | C | 6 - 25 $ / zařízení / měsíc | - Snadné nasazení <br /> - Robustní | Opravdu drahé, i když jen jako MDM | Může být ideálním řešením, pokud projekt již používá Google G Suite. Jinak by to asi nemělo být zvažováno. |

> **Poznámka**
>
> <u> Podtržené MDM </u> byly testovány pomocí aplikace DHIS2 pro Android, nepodtržené zde byly zahrnuty na základě výzkumu nebo použití s jinou aplikací.
>
> Při použití slova Free \* v nákladech se nepovažuje za provozní náklady online / místní server, protože se má za to, že tyto náklady jsou již součástí implementace DHIS2. I když může být doporučeno mít služby spuštěné na různých serverech.

# Annex A - Mobile Device Management (Previous information) {# mdm_previous }

> **Poznámka**
>
> Jedná se o stejné informace, které lze najít v [Pokyny pro implementaci systému Android] (https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/scale-up.html#mobile-device-management). Podpora této části bude brzy ukončena ve prospěch tohoto dokumentu, ale bude zde uchována pro historické účely.

„_Mobile Device Management označuje software používaný ke správě mobilních zařízení. Software MDM budete potřebovat, když budete muset podporovat stovky zařízení a bude nutné řídit distribuci souborů apk mezi zařízeními, poskytovat technickou podporu a prosazovat institucionální zásady. Většina možností je nabízena jako služby s měsíčním poplatkem. Některé bezplatné aplikace nabízejí režim veřejného terminálu, ale za základní vzdálenou správu si účtují měsíční poplatek_. “

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

# Příloha B - MDM PoC: Flyve MDM { #mdm_flyve }

Tato příloha představuje výsledek testovaného MDM: [https://www.flyve-mdm.com/](https://www.flyve-mdm.com/)

Flyve MDM je založen na [GLPI](https://glpi-project.org/), takže před použitím Flyve MDM potřebuje, aby GLPI fungoval jako subsystém. GLPI _je otevřený zdroj IT Asset Management, systém sledování problémů a systém service desk. Tento software je napsán v PHP a distribuován pod GNU General Public License._

## Instalace a použití { #installation-usage }

Je snadné testovat v místnostech, protože poskytují dockerové kontejnery, které umožňují rychlé testování.

Jedná se o aplikaci JAVA / Tomcat, díky níž je ideální z hlediska kompatibility s DHIS2...

GLPI může na začátku vypadat trochu ohromující, ale může být velmi velkou výhodou, pokud takové řešení již existuje.

Aplikace je k dispozici na F-Droid, takže může usnadnit proces instalace nebo testování.

Seznam podporovaných funkcí naleznete zde: [http://flyve.org/android-mdm-agent/howtos/policies](http://flyve.org/android-mdm-agent/howtos/policies)

## Problémy { #issues }

Nepodporuje režim KIOSK

MDM Dashboard je mnohem hezčí konzole, ale stále se spoléhá na GLPI pod ním.

## Závěr { #conclusion }

V závislosti na nastavení to nemusí stát za to, protože řídící konzole pro správu MDM a GLPI mohou být nepřekonatelné, pokud v tomto softwaru neexistují žádné předchozí zkušenosti. Nedostupnost režimu KIOSK může být příčina nenaplnění obchodu.

Jedná se o Open Source, takže náklady mohou být výrazně sníženy, pokud jsou hostovány samostatně; možná ideální pro opravdu malé implementace nebo k testování schopností MDM před zvětšením kapacity.

# Příloha C - MDM PoC: Headwind { #mdm_headwind }

Tato příloha představuje výsledek testovaného MDM: [https://h-mdm.com/](https://h-mdm.com/)

## Instalace a použití { #installation-usage }

Instalace je opravdu snadná, protože řešení poskytuje instalační skript.

Jedná se o aplikaci JAVA / Tomcat, díky níž je ideální z hlediska kompatibility s DHIS2...

Bezplatná verze může v určitých implementacích stačit, ale pro rozšířené funkce (včetně režimu Kiosk) může být vyžadována profesionální nebo rozšířená verze. Další podrobnosti najdete na [https://h-mdm.com/enterprise/](https://h-mdm.com/enterprise/).

Jedná se o aplikaci JAVA / Tomcat, díky níž je ideální z hlediska kompatibility s DHIS2

Console:

![Headwindg MDM konzole](resources/images/mdm-image10.png)

Telefon:

![Headwindg MDM běžící na Androidu](resources/images/mdm-image14.png){ width=25% }

## Problémy { #issues }

Nebyly nalezeny žádné velké problémy. Podpora skutečně reagovala.

Bezplatná verze nezahrnuje režim Kiosk.

## Závěr { #conclusion }

Zajímavé řešení Open Source (pouze serverová a nikoli klientská verze)

# Příloha D - MDM PoC: Entgra.io { #mdm_entgra }

Tato příloha představuje výsledek testovaného MDM: [https://entgra.io/emm](https://entgra.io/emm)

## Instalace a použití { #installation-usage }

Poskytují dockerové balíčky pro vzdálené nasazení pro testování (nebo dokonce produkci). Pro tento test byla použita platforma SaaS.

Jedná se o aplikaci JAVA / Tomcat, díky níž je ideální z hlediska kompatibility s DHIS2

Pokrývá celou škálu definovaných funkcí, ale definice politiky může být trochu ohromující kvůli množství možností.

Toto řešení umožňuje dálkové ovládání zařízení a správce tak může na dálku vidět obrazovku zařízení. To může být zvláště užitečné pro školení a řešení problémů.

Console

![Konzole Entgra MDM](resources/images/mdm-image11.png)

Telefon

![Entgra MDM běžící na Androidu](resources/images/mdm-image2.png){ width=25% }

## Problémy { #issues }

Umístění zařízení nefungovalo (zdá se, že jde o dočasný problém)

## Závěr { #conclusion }

Fungovalo dobře a podpora reagovala. Skutečnost, že jde o otevřenou zdrojovou aplikaci Java, může usnadnit správu, pokud použijete volbu místností.

# Příloha E - MDM PoC: Miradore { #mdm_miradore }

Tato příloha představuje výsledek testovaného MDM: [https://www.miradore.com/](https://www.miradore.com/)

## Instalace a použití { #installation-usage }

Není třeba instalovat, protože řešením je SAAS

Docela snadné a čisté rozhraní

Console:

![Konzole Miradore MDM](resources/images/mdm-image3.png)

Telefon

![Miradore MDM běžící na Androidu](resources/images/mdm-image1.png){ width=25% }

## Problémy { #issues }

V normálním režimu (BYOD), kdykoli správce MDM odešle požadavek, musí je osoba odpovědná za zařízení schválit, tj. Instalaci aplikace. Vzdálená správa je tedy nějak omezená.

## Závěr { #conclusion }

Toto řešení bylo implementováno v Ghaně (nasazení DHIS2 ministerstvem zdravotnictví s ~2700 zařízeními) a úspěšně fungovalo několik měsíců. Kvůli vysokým nákladům však byla později převedena z komerční na bezplatnou verzi.

# Příloha F - MDM PoC: Manage Engine MDM Plus { #mdm_manage_engine }

Tato příloha představuje výsledek testovaného MDM: [https://www.manageengine.com/mobile-device-management/](https://www.manageengine.com/mobile-device-management/)

## Instalace a použití { #installation-usage }

Žádná instalace jako cloudová služba.

Snadná registrace zařízení.

Toto řešení umožňuje vzdálené hovory a dálkové ovládání zařízení, takže manažer může komunikovat pomocí VoIP a vzdáleně vidět obrazovku zařízení. To může být zvláště užitečné pro školení a odstraňování problémů.

Console:

![Konzola Správa Engine Plus MDM](resources/images/mdm-image16.png)

Telefon

![Manage Engine Plus MDM běžící na Androidu](resources/images/mdm-image15.png){ width=25% }

## Problémy { #issues }

Během testu se nepodařilo nahrát soubory ani aplikace. Zdá se, že jde o dočasný problém.

## Závěr { #conclusion }

Pracoval opravdu dobře.

# Příloha G - MDM PoC: Scale Fusion (MobiLock) { #mdm_scale_fusion }

Tato příloha představuje výsledek testovaného MDM: [https://scalefusion.com/](https://scalefusion.com/)

## Instalace a použití { #installation-usage }

Žádná instalace, protože cloudové řešení bylo testováno.

Spousta možností, možná příliš mnoho, které by vás mohly na začátku zmást.

Registrace agentů byla opravdu snadná, i když pro režim Kiosk bylo povinné šifrování.

Toto řešení umožňuje vzdálené hovory a dálkové ovládání zařízení, takže manažer může komunikovat pomocí VoIP a vzdáleně vidět obrazovku zařízení. To může být zvláště užitečné pro školení a odstraňování problémů.

Console:

![MDM konzole Scale Fusion](resources/images/mdm-image8.png)

Telefon (normální vs. kiosek):

![Scale Fusion MDM běžící na Androidu v normálním režimu](resources/images/mdm-image13.png){ width=25% } ![Scale Fusion MDM běžící v režimu kiosku Android](resources/images/mdm-image4.png){ width=25% }

## Problémy { #issues }

Povinné šifrování pro zařízení Kiosk (pomalé)

## Závěr { #conclusion }

Pěkné řešení, fungovalo dobře a lze jej plně přizpůsobit.
