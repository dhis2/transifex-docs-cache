---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/data-analysis-tools-overview.md"
revision_date: "2021-06-14"
---

# Přehled nástrojů pro analýzu dat { #data-analysis-tools-overview }

Tato kapitola nabízí přehled dostupných nástrojů pro analýzu dat poskytovaných serverem DHIS2 spolu s popisem účelu a výhod každého z nich. Pokud hledáte podrobného průvodce, jak používat jednotlivé nástroje, doporučujeme po dokončení této kapitoly pokračovat ve čtení uživatelské příručky. Následující seznam ukazuje různé nástroje:

1.  Standardní zprávy

2.  Zprávy datových sad

3.  Zprávy o úplnosti dat

4.  Statické zprávy

5.  Zprávy o distribuci organizační jednotky

6.  Zprávy tabulky

7.  Grafy

8.  Webová kontingenční tabulka

9.  GIS

10. Kontingenční tabulky My Datamart a Excel

## Nástroje pro analýzu dat { #data-analysis-tools }

V následující části je uveden popis každého nástroje.

### Standardní zprávy { #standard-reports }

Standardní zprávy jsou zprávy s předdefinovanými vzory. To znamená, že zprávy  jsou snadno přístupné několika kliknutími a mohou je využívat uživatelé na všech úrovních zkušeností. Zpráva může obsahovat statistiky ve formě tabulek a grafů a lze ji přizpůsobit tak, aby vyhovovala většině požadavků. Řešení zpráv v DHIS2 je založeno na JasperReports a zprávy jsou nejčastěji navrženy pomocí návrháře sestav iReport. I když je návrh sestavy pevný, lze data do sestavy dynamicky načítat na základě jakékoli organizační jednotky v rámci hierarchie as různými časovými obdobími.

### Zprávy datových sad { #data-set-reports }

Hlášení zprávy datové sady zobrazují design formulářů pro zadávání dat jako zprávu naplněnou agregovanými daty (na rozdíl od zachycených dat na nízké úrovni). Tato zpráva je snadno přístupná pro všechny typy uživatelů a poskytuje rychlý přístup k souhrnným datům. Často existuje starší požadavek na prohlížení formulářů pro zadávání dat jako zpráv, které tento nástroj účinně zajišťuje. Zpráva datové sady podporuje všechny typy formulářů pro zadávání dat, včetně sekcí a vlastních formulářů.

### Zpráva o úplnosti dat { #data-completeness-report }

Zpráva o úplnosti údajů vytváří statistické údaje o míře úplnosti formulářů pro zadávání údajů. Statistické údaje lze analyzovat na jednotlivé datové soubory nebo na seznam organizačních jednotek se společným nadřazeným v hierarchii. Poskytuje procentní hodnotu pro celkovou úplnost a pro úplnost včasných podání. Jako základ pro statistiku lze použít různé definice úplnosti: Nejprve na základě počtu souborů dat označených ručně jako úplných uživatelem zadávajícím data. Druhý na základě toho, zda jsou pro datový soubor vyplňovány všechny datové prvky definované jako povinné. Za třetí na základě procenta počtu vyplněných hodnot nad celkovým počtem hodnot v datové sadě.

### Statické zprávy { #static-reports }

Statické sestavy poskytují dvě metody propojení s existujícími prostředky v uživatelském rozhraní. Nejprve poskytuje možnost propojení se zdrojem na internetu prostřednictvím adresy URL. Zadruhé poskytuje možnost nahrávat soubory do systému a odkazovat na ně. Typ souborů k nahrání může být jakýkoli druh dokumentu, obrázku nebo videa. Užitečnými příklady dokumentů, na které lze odkazovat, jsou zdravotní průzkumy, politické dokumenty a roční plány. Adresy URL mohou odkazovat na příslušné webové stránky, jako je domovská stránka Ministerstva zdravotnictví, zdroje informací souvisejících se zdravím. Kromě toho může být použit jako rozhraní k webovým analytickým nástrojům třetích stran tím, že ukazuje na konkrétní zdroje. Jedním příkladem je nasměrování adresy URL na sestavu obsluhovanou platformou BIRT reporting.

### Zprávy o distribuci organizační jednotky { #organisation-unit-distribution-reports }

Zpráva distribuce organizační jednotky poskytuje statistiky o zařízeních (organizačních jednotkách) v hierarchii na základě jejich klasifikace. Klasifikace je založena na skupinách organizačních jednotek a sadách skupin. Zařízení lze například klasifikovat podle typu přiřazením k příslušné skupině ze skupiny nastavené pro typ organizační jednotky. Zpráva distribuce vytváří počet zařízení pro každou třídu a lze ji vygenerovat pro všechny organizační jednotky a pro všechny sady skupin v systému.

### Zprávy tabulky { #report-tables }

Tabulky sestav jsou sestavy založené na agregovaných datech v tabulkovém formátu. Tabulku sestav lze použít jako samostatnou sestavu nebo ji lze použít jako zdroj dat pro propracovanější standardní návrh sestavy. Tabulkový formát lze překládat do tabulek s libovolným počtem dimenzí, které se zobrazují jako sloupce. Může obsahovat agregovaná data indikátoru a datového prvku i údaje o úplnosti datových sad. Může obsahovat relativní období, která umožňují opakované použití sestavy v průběhu času. Může obsahovat uživatelem volitelné parametry pro organizační jednotky a období, aby bylo možné znovu použít sestavu pro všechny organizační jednotky v hierarchii. Tabulka sestavy může být omezena na nejlepší výsledky a tříděna vzestupně nebo sestupně. Po vygenerování lze data tabulky sestavy stáhnout jako PDF, sešit Excel, soubor CSV a sestavu Jasper.

### Grafy { #charts }

Komponenta grafu nabízí širokou škálu grafů, včetně standardních pruhových, spojnicových a koláčových grafů. Grafy mohou obsahovat indikátory, datové prvky, období a organizační jednotky na ose x a y, stejně jako pevnou vodorovnou cílovou čáru. Grafy lze zobrazit přímo nebo jako součást ovládacího panelu, jak bude vysvětleno později.

### Webové kontingenční tabulky { #web-pivot-tables }

Webová kontingenční tabulka nabízí rychlý přístup ke statistickým údajům v tabulkovém formátu a poskytuje možnost „otočit“ libovolný počet dimenzí, jako jsou indikátory, datové prvky, organizační jednotky a období, aby se zobrazily na sloupcích a řádcích za účelem vytvoření přizpůsobených pohledů. Každou buňku v tabulce lze vizualizovat jako sloupcový graf.

### GIS { #gis }

Modul GIS umožňuje vizualizovat agregovaná data na mapách. Modul GIS může poskytovat tematické mapování polygonů, jako jsou provincie a okresy, a bodů, jako jsou zařízení, v samostatných vrstvách. Uvedené vrstvy lze zobrazit společně a kombinovat s vlastními překryvy. Taková zobrazení mapy lze snadno navigovat zpět v historii, uložit pro snadný přístup v pozdější fázi a uložit na disk jako obrazový soubor. Modul GIS poskytuje automatické a pevné zalomení tříd pro tematické mapování, předdefinované a automatické sady legend, schopnost zobrazit štítky (názvy) pro geografické prvky a schopnost měřit vzdálenost mezi body na mapě. Mapování lze zobrazit pro jakýkoli indikátor nebo datový prvek a pro jakoukoli úroveň v hierarchii organizační jednotky. K dispozici je také speciální vrstva pro zobrazení zařízení na mapě, kde každá z nich je podle svého typu reprezentována symbolem.

### Kontingenční tabulky My Datamart a Excel { #my-datamart-and-excel-pivot-tables }

Účelem nástroje My Datamart je poskytnout uživatelům plný přístup k agregovaným datům i na nespolehlivých připojeních k internetu. Tento nástroj se skládá z odlehčené klientské aplikace, která je nainstalována v počítači uživatelů. Připojuje se k online centrálnímu serveru, na kterém běží instance DHIS2, stahuje agregovaná data a ukládá je do databáze v místním počítači. Tuto databázi lze použít k připojení nástrojů třetích stran, jako jsou kontingenční tabulky MS Excel, což je výkonný nástroj pro analýzu a vizualizaci dat. Toto řešení implikuje, že k synchronizaci databáze klientů s centrální online databází je potřeba jen krátká doba připojení k internetu a že po dokončení tohoto procesu budou data k dispozici nezávisle na připojení. Přečtěte si kapitolu věnovanou tomuto nástroji, kde najdete podrobné informace.
