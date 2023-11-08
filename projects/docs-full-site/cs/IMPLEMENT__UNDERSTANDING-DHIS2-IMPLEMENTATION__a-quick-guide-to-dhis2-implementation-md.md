---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/a-quick-guide-to-dhis2-implementation.md"
revision_date: "2021-06-14"
---

# Stručný průvodce implementací DHIS2 { #a-quick-guide-to-dhis2-implementation }

Jakákoli implementace okresního zdravotnického informačního softwaru (DHIS2) by se měla zaměřit na vytvoření udržitelných systémů, které jsou flexibilní pro měnící se potřeby ve zdravotnictví. Je důležité si uvědomit, že to bude trvat mnoho let, s nepřetržitými strukturami pro budování kapacit, sdílení osvědčených postupů a inovace. Tento rychlý průvodce poskytne velmi hrubý přehled o různých aspektech implementace DHIS2.

## Plánování a organizace { #planning-and-organizing }

### Potřebné struktury { #structures-needed }

- Ke správě národního HMIS bude zapotřebí základního týmu DHIS (DCT) se 4-5 osobami. Jejich povinnosti a požadované dovednosti by měly být jasně definovány. DCT se bude účastnit akademií DHIS2, organizovat školení a podporu koncových uživatelů pro různé skupiny uživatelů v zemi.

- K řízení koordinace mezi zdravotními programy, dalšími informačními systémy a rozvojovými partnery a univerzitami bude zapotřebí technický řídící výbor nebo ekvivalentní výbor. Budou vést integrační úsilí a rozhodovat o celkové architektuře informačních systémů.

### Integrační úsilí { #integration-efforts }

- V průběhu implementace je třeba vyvíjet současné úsilí o integraci informačního systému a výměnu dat. Hlavní zásadou této práce by mělo být vytvoření systému zaměřeného na rozhodování a zaměřeného na indikátory.

### Vybavení a internet { #equipment-and-internet }

- Je třeba posoudit stanovení potřeb hardwaru. Stolní počítače, notebooky, tablety, mobilní telefony mají různé kvality a obvykle bude třeba podporovat kombinaci těchto různých technologií.

- Je třeba kriticky posoudit alternativy serverů a hostování, pokud jde o kapacitu, infrastrukturní omezení, právní rámec, otázky bezpečnosti a důvěrnosti.

- Bude potřeba připojení k internetu pro všechny uživatele. Mobilní internet bude vhodný pro většinu uživatelů provádějících sběr dat a pravidelnou analýzu.

- Pokud je to vhodné, měly by být prozkoumány možnosti pro uživatele mobilních telefonů, hromadné SMS zprávy atd.

### Zaváděcí strategie { #roll-out-strategy }

- DCT zde bude hrát klíčovou roli a každý člen by měl mít jasnou odpovědnost za zavádění: uživatelská podpora, školení uživatelů, spolupráce se zdravotními programy atd.

- Je třeba vytvořit širší podpůrné struktury, které budou poskytovat podporu, dohled a komunikaci s globální / regionální sítí expertních uživatelů a vývojářů.

- Využití informací musí být od začátku oblastí zájmu a musí být součástí jak počátečního návrhu systému, tak prvního kola školení uživatelů. Sběr dat a kvalita dat se zvýší pouze se skutečnou hodnotou informací. Zasedání okresní revize a obdobná opatření by měla být podporována vhodnými informačními produkty a školením.

- Školení bude obvykle největší investicí v čase a vyžaduje struktury pro nepřetržité příležitosti. Naplánujte dlouhodobý tréninkový přístup zajišťující nepřetržitý proces umožnění novým uživatelům a novým funkcím systému.

- Dohled a hodnocení kvality údajů by měly být prováděny často.

## Přizpůsobení DHIS2 { #adapting-dhis2 }

### Rozsah systému { #scope-of-system }

- Na základě rozhodnutí, která by měl systém podporovat (rozsah systému); pro agregaci, trasovač a / nebo události DHIS2 bude potřeba úpravy a přizpůsobení platformy. Každá akce bude vyžadovat zvláštní kompetence a měla by být vedena DCT.

- Je zapotřebí posouzení zamýšlených uživatelů a příjemců, například pokud jde o jejich informační potřeby a hardwarové a síťové potřeby.

- Je důležité porozumět širší architektuře HIS („ekosystém HIS“); jaké další systémy existují a jak by měly interagovat s DHIS2? Zvažte, jaké budou potřeby interoperability mezi elektronickými systémy.

- Pokud existují potřeby, které DHIS2 aktuálně nepodporuje, je nutné posouzení dalšího vývoje softwaru. Lze je řešit lokálně vývojem vlastní webové aplikace nebo vstupem do procesu celkového plánu vývoje základní platformy organizovaného UiO.

### Nastavení DHIS2 { #setting-up-dhis2 }

- Zpravodajské jednotky: implementace různých zpravodajských jednotek (poskytovatelů služeb) a hierarchií, včetně seskupení.

- Potřeby shromažďování údajů: Které indikátory jsou potřebné, jaké datové proměnné budou použity při jejich výpočtu a jak by měla být tato data shromažďována? Navrhujte datové prvky, kategorie rozčlenění, datové sady a formuláře pro sběr.

- Informace k akci (indikátory, ovládací panely, další výstupy): jaké jsou informační produkty, které budou různí uživatelé potřebovat? Tabulky, grafy, mapy, ovládací panely. Rutiny pro šíření a sdílení.

- Správa uživatelů: Vytvářejte uživatelské role a skupiny, rutiny pro správu uživatelů, definujte přístup k funkcím a vhodné sdílení obsahu.

- Dokument správy DHIS2 (role podle profilu, jak změnit metadata a za jakých podmínek).

### Hostování { #hosting }

- Existuje mnoho různých možností hostování online systému, a to jak z hlediska umístění serveru (např. In-house vs. cloud), tak i toho, kdo má server spravovat (např. In-house vs. outsourcing). Je třeba kriticky posoudit alternativy serverů a hostování, pokud jde o kapacitu, infrastrukturní omezení, právní rámec, otázky bezpečnosti a důvěrnosti. Tato rozhodnutí bude možná nutné revidovat alespoň jednou ročně, protože se časem může změnit složitost serveru, datové typy (např. agregát vs. pacient) a místní kapacita.

## Budování kapacit { #capacity-building }

### DHIS core tým (DCT) { #dhis-core-team-dct }

- DCT bude potřebovat všechny dovednosti nezbytné pro udržitelný a vyvíjející se systém. To zahrnuje technické dovednosti (přizpůsobení DHIS2, údržba serveru), znalosti systému (architektury a principy návrhu), organizační (integrační strategie) a řízení projektu (organizování strukturované podpory a školení).

- Členové DCT by se měli pravidelně (např. dvakrát ročně) účastnit regionální / globální akademie DHIS2, aby zajistili vysoce kvalitní školení, nepřetržitou komunikaci s širší komunitou odborníků a zajistili, aby byl místní tým aktuální s novými funkcemi a vylepšeními v posledních verzích platformy DHIS 2. DCT bude odpovědné za přizpůsobení a kaskádování tohoto regionálního vzdělávacího programu pro širší skupinu uživatelů v dané zemi.

### Strategie pro výcvik v dané zemi { #country-training-strategies }

- DCT by měla nabízet školení v souvislosti s implementací a nepřetržitě poté, aby vyhověla rostoucím požadavkům, aktualizacím systému a fluktuaci zaměstnanců.

- Přizpůsobení a vývoj školicích materiálů a referenčních příruček tak, aby odrážely potřeby místních informací a obsah místního systému, je důležité.

### Příležitosti dalšího vzdělávání { #continuous-training-opportunities }

- Jak uživatelská zkušenost roste, mělo by být nabízeno pokročilejší školení. Školení o používání informací pro okresní lékaře a manažery zdravotnických programů je zásadní již brzy, aby se zúčastněné strany mohly zapojit do využívání informací při rozhodování.
