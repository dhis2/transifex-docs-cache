---
edit_url: "https://github.com/dhis2-metadata/GNRC-Common_Metadata_Library/blob/master/docs/common-metadata-library.md"
revision_date: "2022-03-02"
---

# Společná knihovna metadat { #common-metadata-library }

## Úvod { #introduction }

Tento dokument popisuje balíček metadat, který poskytuje základní linii základních metadat DHIS2 pro použití ve více programech Tracker. Zahrnutá metadata nejsou specifická pro program/případ užití, ale obecně se očekává, že budou sdílena napříč sledovacími programy jako součást harmonizovaného HMIS.

Jednou z klíčových výhod DHIS2 je, že jej lze použít pro více zdravotních programů v rámci jediné harmonizované instance. Existuje několik praktických důvodů, proč sdílet metadata mezi trasovacími programy:

-   Pro omezení duplicitního zadávání dat a zlepšení datových toků, např. kde lze údaje o osobě zaznamenané v jednom programu přenést do jiného programu;
-   Zlepšení analytických schopností napříč programy opětovným použitím společných metadat a souvisejících kódů pro základní atributy, jako je Pohlaví;
-   Usnadnit údržbu metadat v systému

Balíčky metadat DHIS2 jsou navrženy a harmonizovány způsobem, který umožňuje importovat více balíčků do stejné instance DHIS2. To lze provést za účelem propojení jednotlivých zápisů do různých programů nebo vytvoření synergií napříč toky podávání zpráv pro různé oblasti zdraví. Pacient může být například zařazen do programů sledování případů HIV i TBC, ale pohlaví pacienta je zaznamenáno pouze jednou v době první registrace. K tomu potřebují programy sdílet stejná metadata pro atribut trasované entity (Pohlaví) plus související sadu možností a možnosti (Muž, Žena a Neznámý).

Import těchto společných metadat společně jako základního balíčku zajišťuje, že Jedinečná ID, názvy a kódy objektů (např. atributy sledovaných entit, sady možností, možnosti a datové prvky. Pokud je navíc v rámci stejné instance vyvinut vlastní program, mohl by znovu použít tato metadata ze základního balíčku, a tím zavést konfiguraci nového programu, zabránit kolizím jmenného prostoru a dalším komplikacím během importu/exportu metadat a usnadnit výměnu dat mezi platformami. To se stává zvláště důležité při zarovnávání implementací sledovače, které mohou existovat přes více instancí do sdíleného, harmonizovaného prostředí.

## Přehled návrhu systému { #system-design-overview }

Společná metadata sledování jsou zpřístupněna jako instalovatelné soubory metadat, které lze importovat do nové nebo existující instance DHIS2. Tyto instalovatelné soubory obsahují metadata, která jsou v souladu s několika běžnými případy použití pro DHIS2 Tracker:

1. Core Case Profile

Používají se ve všech sledovacích programech WHO na sledování případů: imunizace, HIV, malárie, TBC, VPD a sledování na základě případů COVID-19. Profil Core Case Profile byl vyvinut prostřednictvím interní harmonizace WHO konvencí pojmenování pro registry založené na jednotlivých případech a agregované datové sady na úrovni zařízení ve všech programech WHO, které používají DHIS2 od září 2020. Tato knihovna bude každoročně revidována pro možné revize. To zahrnuje:

-   Typ trasované entity (osoba)
-   Atributy trasované entity
-   Možnosti
-   Sady možností

2. Knihovna obecných metadat DHIS2 Tracker

Knihovna obecných metadat Common Tracker Metadata obsahuje všechny výše uvedené objekty WHO Core Case Profile plus další společná metadata, jako jsou datové prvky, sady možností a možnosti. Tato knihovna není vyčerpávající, ale obsahuje koncepty metadat, které jsou zahrnuty v oficiálních balíčcích DHIS2 trackerů a jsou dostatečně obecné na to, aby je bylo možné sdílet napříč programy (např. sady možností pro seznam zemí nebo datový prvek pro „datum úmrtí“ ). Knihovna má poskytovat výběr společných metadat, která mohou implementátoři použít podle svého uvážení při vývoji sledovacích programů. Tato knihovna bude častěji aktualizována a rozšiřována na půlroční bázi, jak se budou vyvíjet a nasazovat balíčky metadat.

Všechna metadata v knihovně Common Tracker Metadata Library obsahují skupiny metadat obsahující předponu GN (pro Obecné. Předpona pomáhá implementátorovi nebo správci systému sdělit, že objekt metadat je sdílen mezi programy, a před provedením změn je třeba zvážit dopad napříč programy /úpravy sdílených metadat.

-   Typ trasované entity (osoba)
-   Atributy trasované entity
-   Sady možností, včetně kódů zemí ISO 3166-1 alpha-2
-   Možnosti
-   Datové prvky
-   Vlastní atributy spojené s výše uvedeným (např. LOINC, Snomed, ICD-11)

![Diagram sdílených metadat](resources/images/metadata-diagram-en.png)

Výše uvedené schéma ukazuje několik bodů o modulární struktuře balíčku.

DHIS2 Common Tracker Library obsahuje kromě dalších objektů metadat celý profil WHO Core Case Profile.

Balíček metadat DHIS2 může využívat metadata nalezená v profilu Core Case Profile, v rámci širší knihovny Common Tracker Library nebo jeho vlastní metadata specifická pro program (viz balíček HIV CS).

Vlastní, místně navržený sledovací program může také využívat metadata nalezená v profilu Core Case Profile, v rámci širší Common Tracker Library nebo vyvíjet vlastní metadata specifická pro daný program.

Představte si scénář, kde je výše uvedený program NTD Surveillance vyvíjen nezávisle. Implementátoři se pak rozhodnou importovat balíček HIV CS do stejné instance DHIS2. Během importu metadat by docházelo k řadě konfliktů, protože objekty v každém programu mají stejný název a různé UID (telefonní číslo, národní ID a zemi narození). Pokud by byl profil Core Case Profile importován před konfigurací vlastního programu NTD, bylo by zapotřebí méně práce s konfigurací nových metadat a méně kolize při importu balíčku HIV CS.

Nakonec si uvědomte, že předpona GEN nebude viditelná pro koncové uživatele vašich programů. Tato metadata jsou přeložena pro XYZ různých národních prostředí a lze je dále překládat do dalších místních jazyků, aniž by to narušovalo základní UID, názvy a kódy.
