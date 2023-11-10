---
edit_url: "https://github.com/dhis2/dhis2-android-docs/blob/main/content/mdm/choosing-an-mdm.md"
revision_date: '2022-01-07'
tags:
- Implementace
---

# Výběr MDM / EMM { #mdm_choosing }

Při rozhodování, které řešení MDM zvolit, je důležité definovat, která sada funkcí bude považována za nezbytnou a které za hezké mít. To se může mezi implementacemi hodně lišit; v níže uvedeném seznamu jsme však identifikovali některé funkce jako povinné z důvodu povahy DHIS2. I když to může být přezkoumáno v závislosti na implementaci, mělo by to být považováno za naše doporučení.

Další podrobnosti najdete v příloze A - Správa mobilních zařízení.

Požadované funkce a jejich důvod:

* Android jako podporovaná platforma:

  To se může zdát zřejmé, ale některá řešení MDM jsou zaměřena na jiné typy zařízení, jako je iOS nebo Windows. V tuto chvíli je aplikace DHIS2 pro Android kompatibilní pouze se zařízeními Android a podporuje od verze 4.4 (nedoporučuje se) a vyšší (doporučujeme od verze 7).

* Správa distribuce aplikace(í):

  Implementace DHIS2 potřebují otestovat a vyškolit uživatele před vydáním nové verze aplikace. Protože většina implementací nainstaluje aplikaci DHIS2 pro Android z obchodu Google Play, je možné při publikování aktualizace zařízení aktualizovat, aniž by byl projekt připraven, pokud není k dispozici žádný jiný mechanismus pro správu aktualizací.

* Informace o zařízení:

  Implementace DHIS2 potřebují udržovat soupis svých zařízení, aby mohly řešit problémy nebo aktualizovat svá zařízení. Všechna zvažovaná řešení MDM zahrnují tuto základní funkci, ale je zde uvedena pouze pro případ, že existuje řešení, které to nemusí zahrnovat.

* Vynucení hesla:

  Ve většině (ne-li všech) implementacích DHIS2 jsou citlivé informace uloženy v aplikaci. Proto vynucování zásad hesla na zařízení může zabránit nežádoucímu přístupu k těmto datům.


    Všimněte si, že navzdory tomu, že aplikace DHIS2 pro Android umožňuje nastavit heslo pro řízení přístupu, protože informace v zařízení ještě nejsou zašifrovány (únor 2020), mohl by je útočník stále extrahovat.

* Vzdálené vymazání:

  Ve většině (ne-li všech) implementacích DHIS2 jsou v aplikaci uloženy citlivé informace. Pokud například dojde ke ztrátě nebo odcizení zařízení, může zajistit, aby bylo možné jej vzdáleně vymazat, zabránit úniku citlivých dat.


Funkce které je pěkné mít a jejich důvod:

* Režim veřejného terminálu (tj. režim jedné aplikace)

  Některé implementace DHIS2 mohou vyžadovat uzamčení zařízení do jedné aplikace (DHIS2 Android Capture App), aniž by uživateli umožnily přístup k jakékoli jiné aplikaci nebo nastavení. Kiosková politika by toho dosáhla.

* Správa telefonu

  V některých implementacích DHIS2 může být nutné poskytovat zařízení se SIM kartami, aby bylo zajištěno datové připojení přes mobilní síť (2G-5G). To může vyžadovat, aby zařízení používala konkrétní volací služby za účelem dobíjení datových balíčků nebo omezenou podporu volání atd.

* Omezení aplikace / nastavení

  Některé implementace DHIS2 mohou vyžadovat, aby uživatelé mohli používat nejen jednu, ale několik aplikací (tj. Zařízení, které je třeba použít pro DHIS2 a snímání obrázků).

* Správa sítě

  Některé implementace DHIS2 mohou vyžadovat, aby zařízení nepoužívala datovou síť nebo se omezovala na konkrétní domény (brána firewall) nebo aby vždy používala pouze konkrétní bezdrátové sítě nebo dynamicky nastavovala bezdrátové sítě atd.

* Správa uživatelů

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

