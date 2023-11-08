---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/dhis2-as-a-platform.md"
revision_date: "2021-06-14"
---

# DHIS2 jako platforma { #dhis2-as-a-platform }

DHIS2 lze vnímat jako platformu na několika úrovních. Za prvé, aplikační databáze je navržena od základu s ohledem na flexibilitu. Datové struktury, jako jsou datové prvky, organizační jednotky, formuláře a uživatelské role, lze definovat zcela volně prostřednictvím uživatelského rozhraní aplikace. Díky tomu je možné systém přizpůsobit mnoha místním kontextům a případům použití. Viděli jsme, že DHIS2 podporuje většinu hlavních požadavků na rutinní sběr dat a analýzu, které se objevují v implementacích zemí. Umožňuje také DHIS2 sloužit jako systém pro správu domén, jako jsou logistika, laboratoře a finance.

Za druhé, díky modulární konstrukci DHIS2 je možné jej rozšířit o další softwarové moduly. Tyto softwarové moduly mohou žít bok po boku s jádrovými moduly DHIS2 a lze je integrovat do portálu a systému nabídek DHIS2. Jedná se o výkonnou funkci, protože v případě potřeby umožňuje rozšířit systém o další funkce, obvykle pro specifické požadavky dané země, jak již bylo uvedeno výše.

Nevýhodou rozšiřitelnosti softwarového modulu je to, že klade několik omezení na vývojový proces. Vývojáři, kteří vytvářejí další funkce, jsou kromě omezení kladených na návrh modulů portálovým řešením DHIS2 omezeni na technologii DHIS2, pokud jde o programovací jazyk a softwarové rámce. Tyto moduly musí být také zahrnuty do softwaru DHIS2, když je software vytvořen a nasazen na webovém serveru, nikoli dynamicky během běhu.

Za účelem překonání těchto omezení a dosažení volnějšího propojení mezi vrstvou služby DHIS2 a dalšími softwarovými artefakty se vývojový tým DHIS2 rozhodl vytvořit webové rozhraní API. Toto webové rozhraní API odpovídá pravidlům architektonického stylu REST. To znamená, že:

- Webové rozhraní API poskytuje navigovatelné a strojově čitelné rozhraní pro kompletní datový model DHIS2. Například je možné přistupovat k úplnému seznamu datových prvků, poté pomocí zadaného hypertextového odkazu přejít na konkrétní datový prvek, který nás zajímá, a poté pomocí zadaného hypertextového odkazu přejít na seznam formulářů, jejichž je tento datový prvek součástí. Např. klienti budou přechody stavu provádět pouze pomocí hypertextových odkazů, které jsou dynamicky vloženy do odpovědí.

- K datům se přistupuje prostřednictvím jednotného rozhraní (URL) pomocí známého protokolu. Nejsou zapojeny žádné fantastické transportní formáty ani protokoly - pouze dobře otestovaný a dobře srozumitelný protokol HTTP, který je dnes hlavním stavebním kamenem webu. To znamená, že vývojáři třetích stran mohou vyvíjet software pomocí datového modelu a dat DHIS2, aniž by věděli o specifické technologii DHIS2 nebo dodržovali konstrukční omezení DHIS2.

- Veškerá data včetně metadat, zpráv, map a grafů, která jsou v terminologii REST známá jako zdroje, lze načíst ve většině populárních formátů reprezentace dnešního webu, jako jsou HTML, XML, JSON, PDF a PNG. Tyto formáty jsou široce podporovány v aplikacích a programovacích jazycích a poskytují vývojářům třetích stran širokou škálu možností implementace.

![](resources/images/implementation_guide/dhis_platform.png)

Existuje několik scénářů, kdy se k webovému rozhraní API DHIS2 mohou připojit další softwarové artefakty.

## Webové portály { #web-portals }

Nejprve mohou být webové portály postaveny na vrcholu webového rozhraní API. Webový portál je v tomto ohledu web, který funguje jako přístupový bod k informacím z potenciálně velkého počtu zdrojů dat, které obvykle sdílejí společné téma. Úlohou webového portálu je zajistit, aby tyto zdroje dat byly snadno přístupné strukturovaným způsobem pod společným dojmem a poskytováním komplexního zobrazení dat pro koncové uživatele.

Úložiště agregovaných dat: Webový portál zaměřený na doménu zdraví může používat DHIS2 jako hlavní zdroj agregovaných dat. Portál se může připojit k webovému API a komunikovat s příslušnými prostředky, jako jsou mapy, grafy, zprávy, tabulky a statické dokumenty. Tyto datové pohledy mohou dynamicky vizualizovat agregovaná data na základě dotazů na dimenzi organizační jednotky, indikátoru nebo období. Portál může přidávat hodnotu k přístupnosti informací několika způsoby. Může být strukturován uživatelsky přívětivým způsobem a zpřístupňovat data nezkušeným uživatelům. Může poskytnout různé přístupy k datům, včetně:

- Tematické - seskupení indikátorů podle tématu. Příklady takových témat jsou očkování, péče o matku, nemoci podléhající hlášení a zdraví životního prostředí.

- Geografické - seskupení údajů podle provincií. To umožní snadné srovnání výkonu a vytížení.

Mash-up: Webový portál se neomezuje pouze na konzumaci dat z jediného webového rozhraní API - lze jej připojit k libovolnému počtu rozhraní API a použít k propojení dat z pomocných systémů v doméně stavu. Pokud je k dispozici, portál může získávat specializovaná data ze sledování logistických systémů a správy léků ARV, z finančních systémů spravujících platby zdravotnickým zařízením a ze laboratorních systémů sledujících laboratorní testy na přenosné nemoci. Data ze všech těchto zdrojů mohou být prezentována uceleným a smysluplným způsobem, aby poskytly lepší přehled o situaci v oblasti zdraví.

Úložiště dokumentů: Webový portál může sám o sobě fungovat jako úložiště dokumentů (označovaný také jako systém správy obsahu). Mohou být nahrány a spravovány příslušné dokumenty, jako jsou publikované zprávy, údaje z průzkumů, roční operační plány a časté dotazy, pokud jde o vlastnictví, kontrolu verzí a klasifikaci. Díky tomu je portál ústředním bodem pro sdílení dokumentů a spolupráci. Díky vzniku vysoce kvalitních řešení open source úložiště / CMS, jako jsou Alfresco a Drupal, je tento přístup proveditelnější a přesvědčivější.

Znalostní management: KM odkazuje na postupy pro identifikaci, materializaci a distribuci vhledů a zkušeností. V našem kontextu se týká všech aspektů implementace a používání informačního systému, jako jsou:

- Návrh databáze

- Využití informačního systému a postupy

- Pokyny pro školení koncových uživatelů

- Využití, analýza a interpretace dat

Znalosti a učení v těchto oblastech lze zhmotnit ve formě příruček, článků, knih, sad snímků, videí, textu nápovědy vloženého do systému, online výukových stránek, fór, často kladených otázek a dalších. Všechny tyto artefakty mohou být publikovány a zpřístupněny z webového portálu.

Fórum: Portál může poskytnout fórum pro pořádání diskusí mezi profesionálními uživateli. Předmět se může pohybovat od nápovědy k provádění základních operací ve zdravotnickém informačním systému až po diskuse nad tématy analýzy dat a interpretace. Takové fórum může fungovat jako interaktivní zdroj informací a přirozeně se vyvinout v hodnotný archiv.

## Aplikace { #apps }

Za druhé, softwaroví klienti třetích stran běžící na zařízeních, jako jsou mobilní telefony, chytré telefony a tablety, se mohou připojit k webovému rozhraní DHIS2 a číst a zapisovat do příslušných zdrojů. Například vývojáři třetích stran mohou vytvořit klienta běžícího v operačním systému Android na mobilních zařízeních zaměřeného na komunitní zdravotnické pracovníky, kteří potřebují sledovat lidi, které mají navštívit, registrovat důležitá data pro každé setkání a dostávat upomínky na termíny splatnosti pro pacienta pečujte při volném cestování v komunitě. Taková klientská aplikace může interagovat s prostředky pacienta a plánu aktivit vystavenými webovým API DHIS2. Vývojář nebude závislý na hlubokém vhledu do interní implementace DHIS2, spíše jen na základní dovednosti v programování HTTP / Web a trochu znalostí datového modelu DHIS2. Pochopení datového modelu DHIS2 usnadňuje navigační povaha webového rozhraní API.

## Informační systémy { #information-systems }

Za třetí, vývojáři informačních systémů, kteří se zaměřují na vytváření nových způsobů vizualizace a prezentace agregovaných dat, mohou využívat webové rozhraní API DHIS2 jako servisní vrstvu svého systému. Úsilí potřebné pro vývoj nových informačních systémů a jejich údržbu v průběhu času je často do značné míry podhodnoceno. Místo toho, aby bylo možné začít úplně od začátku, lze na webové rozhraní API postavit novou aplikaci. Pozornost vývojářů lze zaměřit na vytváření nových, inovativních a kreativních reprezentací a vizualizací dat, v podobě např. ovládací panely, GIS a komponenty grafů.
