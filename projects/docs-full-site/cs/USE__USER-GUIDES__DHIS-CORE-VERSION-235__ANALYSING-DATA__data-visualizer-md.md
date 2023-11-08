---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/data-visualizer.md"
revision_date: "2021-06-14"
---

# Použití aplikace Data Visualizer { #data_visualizer }

![](resources/images/data-visualizer/data-visualizer-overview.png)

## Vytváření a úpravy vizualizací { #creating-and-editing-visualizations }

Když otevřete aplikaci datového vizualizéru z nabídky dhis2, zobrazí se vám prázdná tabulka a můžete hned začít vytvářet vizualizaci.

![](resources/images/data-visualizer/data-visualizer-new.png)

### Vyberte typ vizualizace { #select-visualization-type }

Vyberte požadovaný typ vizualizace z nabídky v levém horním rohu. Pro každý typ vizualizace existuje stručný popis s návrhy, kde použít hlavní dimenze v rozložení.

![](resources/images/data-visualizer/data-visualizer-visualization-type.png)

| Typ vizualizace | Popis |
| --- | --- |
| Sloupec | Zobrazí informace jako svislé obdélníkové sloupce s délkami úměrnými hodnotám, které představují. <br> <br> Příklad: porovnání výkonu různých okresů. <br> <br> Omezení rozložení: přesně 1 dimenze jako série, přesně 1 dimenze jako kategorie. |
| Skládaný sloupec | Zobrazuje informace jako svislé obdélníkové sloupce, kde jsou pruhy představující více kategorií naskládány na sebe. <br> <br> Příklad: zobrazení trendů nebo součtů souvisejících datových prvků. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Pruh | Stejné jako sloupce, pouze s vodorovnými pruhy. |
| Skládaný pruh | Stejné jako skládaný sloupec, pouze s vodorovnými pruhy. |
| Čára | Zobrazuje informace jako řadu bodů spojených přímkami. Označuje se také jako časová řada. <br> <br> Příklad: vizualizace trendů v datech indikátoru v časových intervalech. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Plocha | Je založen na čáře (výše), s mezerou mezi osou a čarou vyplněnou barvami a řádky naskládanými na sebe. <br> <br> Příklad: porovnání trendů souvisejících indikátorů. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Skládaná plocha | Stejné jako Plocha, ale oblasti různých položek dimenzí jsou naskládány na sebe. <br> <br> Příklad: porovnání trendů souvisejících indikátorů. <br> <br> Omezení rozložení: stejné jako plocha. |
| Koláč | Kruh rozdělený na sektory (nebo plátky). <br> <br> Příklad: vizualizace podílu dat pro jednotlivé datové prvky ve srovnání s celkovým součtem všech datových prvků. <br> <br> Omezení rozložení: přesně 1 dimenze jako série, nemá žádnou kategorii. |
| Radar | Zobrazuje data na osách počínaje od stejného bodu. Také známé jako pavoučí graf. <br> <br> Omezení rozložení: stejné jako sloupec. |
| Gauge | Polokruh, který zobrazuje jednu hodnotu, obvykle ze 100% (počáteční a koncová hodnota je konfigurovatelná). <br> <br> Omezení rozvržení: přesně 1 dimenze s přesně 1 položkou jako série, datová dimenze je uzamčena do řady. |
| Rok po roce (řádek) | Užitečné, pokud chcete porovnat jeden rok dat s jinými roky dat. Založeno na kalendářních letech. <br> <br> Omezení rozvržení: dimenze období je deaktivována. |
| Rok po roce (sloupec) | Stejné jako meziročně (řádek), pouze se sloupci. |
| Jedna hodnota | Zobrazí jednu hodnotu přijatelným způsobem na ovládacím panelu. <br> <br> Omezení rozložení: stejné jako Gauge. |
| Kontingenční tabulka | Shrnuje data rozsáhlejší tabulky a může zahrnovat součty, průměry nebo jiné statistiky, které kontingenční tabulka seskupuje smysluplným způsobem. <br> <br> Omezení rozložení: žádné. |

### Vyberte dimenze { #select-dimensions }

Z nabídky dimenzí vlevo můžete vybrat dimenze, které chcete zobrazit ve vizualizaci, včetně dat, období, organizačních jednotek a dynamických dimenzí. Lze je přidat kliknutím na dimenzi, přetažením dimenze do oblasti rozložení nebo umístěním kurzoru nad dimenzi a použitím její kontextové nabídky (tři tečky).

![](resources/images/data-visualizer/data-visualizer-dimensions.png)

Stejně jako v nabídce dimenzí můžete v oblasti rozvržení také změnit výběr kliknutím na dimenzi, přetažením dimenze nebo pomocí kontextové nabídky dimenze (tři tečky).

![](resources/images/data-visualizer/data-visualizer-layout-area.png)

-   **Série**: Série je sada spojitých souvisejících prvků (například období nebo datové prvky), které chcete vizualizovat, abyste zdůraznili trendy nebo vztahy v jejích datech. Také se nazývá sloupce pro vizualizace kontingenčních tabulek.

<!-- konec seznamu -->

-   **Kategorie**: Kategorie je sada prvků (například indikátorů nebo organizačních jednotek), pro které chcete porovnat její data. Také se nazývá řádky pro vizualizace kontingenčních tabulek.

<!-- konec seznamu -->

-   **Filtr**: Výběr filtru vyfiltruje data zobrazená ve vizualizaci. Všimněte si, že pokud použijete dimenzi dat jako filtr, můžete určit pouze jeden indikátor nebo datovou sadu jako položku filtru, zatímco u jiných typů dimenzí můžete vybrat libovolný počet položek.

### Vyberte položky dimenze { #data_vis_select_dim_items }

Dimenze odkazuje na prvky, které popisují hodnoty dat v systému. V systému jsou tři hlavní dimenze:

-   **Data**: Zahrnuje datové prvky, indikátory a datové sady (míry hlášení), popisující jevy nebo událost dat.

<!-- konec seznamu -->

-   **Období**: Popisuje, kdy k události došlo.

<!-- konec seznamu -->

-   **Organizační jednotky**: Popisuje, kde k události došlo.

Data Visualizer je vysoce flexibilní, pokud jde o to, že vám umožňuje používat tyto dimenze jako serie, kategorie a filtr.

Chcete-li vybrat položky pro dimenzi, otevřete modální okno dimenze kliknutím na dimenzi. Toto okno se také automaticky otevře při přidání kóty bez vybraných položek do rozvržení. Dvojitým kliknutím na položku nebo výběrem položky jedním kliknutím a pomocí šipek uprostřed vyberte položky, které chcete přidat do vizualizace. Pořadí vzhledu bude stejné jako pořadí, ve kterém jsou vybrány. U vybraných položek lze změnit jejich pořadí přetažením v sekci Vybrané.

![](resources/images/data-visualizer/data-visualizer-dimension-modal.png)

#### Vyberte období { #select-periods }

Při výběru období musíte zvolit mezi pevnými obdobími a relativními obdobími. Lze je také kombinovat. Překrývající se období jsou filtrována tak, aby se objevila pouze jednou. U relativních období jsou názvy relativní k aktuálnímu datu, např. pokud je aktuální měsíc březen a je vybrán **minulý měsíc**, ve vizualizaci se zobrazí měsíc únor.

![](resources/images/data-visualizer/data-visualizer-period-dimension-modal.png)

#### Vyberte organizační jednotky { #select-organisation-units }

Dialog organizačních jednotek je flexibilní a nabízí v zásadě tři způsoby výběru organizačních jednotek:

-   Explicitní výběr: Použijte **strom** k explicitnímu výběru organizačních jednotek, které chcete zobrazit ve vizualizaci. Pokud kliknete pravým tlačítkem na organizační jednotku, můžete snadno vybrat všechny organizační jednotky pod ní.

-   Úrovně a skupiny: Rozbalovací nabídky **Úroveň** a **Skupina** jsou pohodlným způsobem, jak vybrat všechny jednotky v jedné nebo více skupinách organizačních jednotek nebo na konkrétních úrovních. Příklad: vyberte _Chiefdom_ (úroveň 3) a získejte všechny organizační jednotky na této úrovni.

    Vezměte prosím na vědomí, že jakmile je vybrána alespoň jedna úroveň nebo skupina, strom organizačních jednotek nyní funguje jako hranice pro úrovně / skupiny. Příklad: pokud ve stromu vyberete _Chiefdom_ (úroveň 3) a _Kailahun_ organizační jednotku (na úrovni 2), získáte všechny jednotky chiefdom v okrese Kailahun.

-   Organizační jednotky uživatele:

    -   Organizační jednotka uživatele: Toto je způsob, jak dynamicky vybrat organizační jednotky, ke kterým je přihlášený uživatel přidružen.

    -   Uživatelské dílčí jednotky: Vybírá dílčí jednotky organizační jednotky uživatele.

    -   Uživatelské jednotky druhé podúrovně sub-x2-units: Vybírá jednotky o dvě úrovně pod organizační jednotkou uživatele.

![](resources/images/data-visualizer/data-visualizer-organisation-unit-dimension-modal.png)

### Dva grafy kategorií { #two-category-charts }

Většina typů vizualizace grafů může zobrazit dvě kategorie. Přepnutím z kontingenční tabulky na sloupec, sloupec, oblast (a jejich skládané verze) a řádek zachováte první dvě dimenze v kategorii, jakákoli další dimenze se přesune do filtru. Štítky pro první dimenzi v kategorii jsou zobrazeny v horní části grafu a štítky pro druhou dimenzi v dolní části. Výsledná vizualizace se skládá ze samostatných grafů, jednoho pro každou položku v první dimenzi.

![](resources/images/data-visualizer/data-visualizer-two-category.png)

## Změňte zobrazení vaší vizualizace { #change-the-display-of-your-visualization }

Zobrazení vizualizace lze změnit povolením / zakázáním a konfigurací několika možností. Každý typ vizualizace může mít jinou sadu dostupných možností. Možnosti jsou uspořádány na kartách v **dialogovém okně Možnosti** a v sekcích na každé kartě.

1.  Kliknutím na **Možnosti** otevřete **Možnosti dialogového okna**.

2.  Přejděte na karty v dialogovém okně a zobrazte dostupné možnosti.

3.  Podle potřeby nakonfigurujte požadované možnosti.

4.  Klepnutím na tlačítko **Aktualizovat** provedete změny ve vizualizaci.

### Seznam dostupných možností { #list-of-available-options }

| Možnost | Popis |
| --- | --- |
|  | **karta Data** |
| Typ agregace | Definuje, jak budou datové prvky nebo indikátory agregovány ve vizualizaci. Některé z typů agregace jsou Podle datového prvku, Počet, Min a Max. |
| Základní linie | Zobrazí vodorovnou čáru na dané hodnotě domény. Užitečné například, když chcete vizualizovat, jak se váš výkon vyvíjel od začátku procesu. |
| Mezisoučty sloupců | Zobrazí dílčí součty v kontingenční tabulce pro každou dimenzi. <br> Pokud vyberete pouze jednu dimenzi, dílčí součty budou pro tyto sloupce skryty. Je to proto, že hodnoty se budou rovnat mezisoučtům. |
| Součty sloupců | Zobrazí celkové hodnoty v kontingenční tabulce pro každý sloupec a také celkové hodnoty pro všechny hodnoty v tabulce. |
| Kumulativní hodnoty | Zobrazí kumulativní hodnoty ve vizualizacích Sloupec, Skládaný sloupec, Pruh, Skládaný pruh, Čára a Plocha |
| Vlastní pořadí řazení | Řídí pořadí řazení hodnot. |
| Štítky dimenzí | Zobrazuje názvy dimenzí jako součást kontingenční tabulky. |
| Skrýt prázdné kategorie | Skryje položky kategorie bez dat z vizualizace. <br> **před první**: skryje chybějící hodnoty pouze před první hodnotou <br> **po poslední**: skryje chybějící hodnoty pouze po poslední hodnotě <br> **před první a po poslední**: skryje chybějící hodnoty pouze před první value a po poslední hodnotě <br> **Vše**: skryje všechny chybějící hodnoty <br> To je užitečné například při vytváření vizualizací sloupců a pruhů. |
| Skrýt prázdné sloupce | Skryje prázdné sloupce z kontingenční tabulky. To je užitečné, když se podíváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
| Skrýt prázdné řádky | Skryje prázdné řádky z kontingenční tabulky. To je užitečné, když se podíváte na velké tabulky, kde velká část položek dimenze nemá data, aby byla tabulka čitelnější. |
| Typ čísla | Nastaví typ hodnoty, kterou chcete zobrazit v kontingenční tabulce: Hodnota, Procento řádku nebo Procento sloupce. <br> Možnosti Procento řádku a Procento sloupce znamenají, že místo agregované hodnoty budete zobrazovat hodnoty jako procenta z celkového počtu řádků nebo procenta z celkového počtu sloupců. To je užitečné, když chcete vidět příspěvek datových prvků, kategorií nebo organizačních jednotek k celkové hodnotě. |
| Zahrnout pouze dokončené události | Zahrnuje do procesu agregace pouze dokončené události. To je užitečné například k vyloučení dílčích událostí ve výpočtech indikátorů. |
| Mezisoučty řádků | Zobrazí dílčí součty v kontingenční tabulce pro každou dimenzi. <br> Pokud vyberete pouze jednu dimenzi, dílčí součty budou pro tyto řádky skryty. Je to proto, že hodnoty se budou rovnat mezisoučtům. |
| Součty řádků | Zobrazí celkové hodnoty v kontingenční tabulce pro každý řádek a také celkové hodnoty pro všechny hodnoty v tabulce. |
| Přeskočit zaokrouhlování | Přeskočí zaokrouhlování datových hodnot a nabízí úplnou přesnost datových hodnot. Může být užitečné pro finanční data, kde je vyžadována přesná částka. |
| Skládané hodnoty se přidávají až do 100% | Zobrazí 100% skládané hodnoty ve skládaných sloupcích a skládaných pruzích vizualizací. |
| Cílová čára | Zobrazí vodorovnou čáru na dané hodnotě domény. Užitečné například, když chcete porovnat svůj výkon s aktuálním cílem. |
| Trendová čára | Zobrazí trendovou čáru, která vizualizuje, jak se vaše data vyvíjejí v průběhu času. Například pokud se výkon zlepšuje nebo zhoršuje. Užitečné, když jsou jako kategorie vybrány období. |
| Hodnotové štítky | Zobrazuje hodnoty nad řadou ve vizualizaci. |
|  | Karta Osy |
| Rozsah os | Definuje maximální a minimální hodnotu, která bude viditelná na ose rozsahu. |
| Název osy | Sem zadejte nadpis a zobrazí se štítek vedle osy x nebo y. Užitečné, když chcete vizualizaci poskytnout kontextové informace, například o měrné jednotce. |
| Desetinná místa | Definuje počet desetinných míst, která budou použita pro hodnoty osy rozsahu. |
| Kroky | Definuje počet značek, které budou viditelné na ose rozsahu. |
|  | **karta Legenda** |
| Zobrazit legendu | Použije na hodnoty legendu. To znamená, že na hodnoty můžete použít barvu. Konfigurujete legendy v aplikaci Údržba. <br> Sekce typu Legenda umožňuje určit, která barva se použije. Vyberte Použít předdefinovanou legendu na datovou položku k barevnému vybarvení datového bodu jednotlivě podle každého datového prvku nebo indikátoru. Vyberte Vybrat jednu legendu pro celou vizualizaci a použijte jednu legendu vybranou v rozevíracím seznamu dostupných legend. <br> Sekce stylu legendy umožňuje ovládat, kde je použita barva, text nebo pozadí na základě vybrané legendy. Tuto možnost můžete použít u výsledkového listu k okamžitému zjištění vysokých a nízkých hodnot. Nelze použít pro vizualizace s jednou hodnotou. |
|  | **Záložka Serie** |
|  | Na této záložce jsou nastaveny možnosti pro přidání více os a změnu zobrazení různých sérií. Podrobný popis toho, jak to funguje, naleznete v příslušných částech níže. |
|  | **karta Styl** |
| Oddělovač skupin číslic | Určuje, který znak použít k oddělení skupin číslic nebo „tisíců“. Můžete jej nastavit na Čárku, Mezerník nebo Žádný. |
| Hustota zobrazení | Řídí velikost buněk v kontingenční tabulce. Můžete jej nastavit na Komfortní, Normální nebo Kompaktní. <br> Kompaktní je užitečné, pokud chcete na obrazovku prohlížeče umístit velké tabulky. |
| Zobrazit hierarchii organizačních jednotek | Zobrazuje název všech předků organizačních jednotek, například „Sierra Leone / Bombali / Tamabaka / Sanya CHP“ pro „Sanya CHP“. <br> Organizační jednotky jsou poté seřazeny podle abecedy, která uspořádá organizační jednotky podle hierarchie. <br> Když stáhnete kontingenční tabulku s organizačními jednotkami jako řádky a vybrali jste Zobrazit hierarchii organizačních jednotek, každá úroveň organizační jednotky se vykreslí jako samostatný sloupec. To je užitečné například při vytváření kontingenčních tabulek aplikace Excel v místním počítači. |
| Velikost písma | Řídí velikost písma textu kontingenční tabulky. Můžete jej nastavit na Velký, Normální nebo Malý. |
| Název grafu / tabulky | Řídí nadpis, který se zobrazí nad vizualizací. <br> Automaticky generováno používá výchozí nadpis vygenerovaný z dimenzí / filtrů vizualizace. <br> None odstraní název. <br> Možnost Vlastní umožňuje zadat vlastní název. |
| Podtitul grafu / tabulky | Řídí titulky, které se zobrazují nad vizualizací. <br> Automaticky generováno používá výchozí titulky generované z dimenzí / filtrů vizualizace. <br> None odstraní titulky. <br> Možnost Vlastní umožňuje zadat vlastní titulky. |
| Zobrazit klíč legendy | Zapíná a vypíná legendu a ponechává více prostoru pro samotnou vizualizaci. |
| Mezi pruhy / sloupci není mezera | Odebere mezeru mezi sloupci nebo pruhy ve vizualizaci. Užitečné pro zobrazení vizualizace jako křivky EPI. |
| Hodnotové štítky | Zobrazuje hodnoty nad řadou ve vizualizaci. |
| Název grafu / tabulky | Řídí nadpis, který se zobrazí nad vizualizací. <br> Automaticky generováno používá výchozí nadpis vygenerovaný z dimenzí / filtrů vizualizace. <br> None odstraní název. <br> Možnost Vlastní umožňuje zadat vlastní název. |
| Sada barev | Řídí barvy použité v grafu. Zobrazí se seznam dostupných barevných sad s náhledem barev. K dispozici je také možnost „Mono vzory“, která místo plných barev používá barevné vzory. |
|  | **karta Mezní hodnoty** |
| Mezní minimální / maximální hodnoty | Umožňuje filtrování dat na straně serveru. <br> Můžete dát systému pokyn, aby vracel pouze záznamy, u nichž je agregovaná hodnota dat stejná, větší než, větší nebo stejná, menší nebo menší nebo rovna určitým hodnotám. <br> Pokud jsou použity obě části filtru, je možné odfiltrovat řadu datových záznamů. |
|  | **karta Parametry** |
| Vlastní pořadí řazení | Řídí pořadí řazení hodnot. |
| Zahrnout kumulativní | Zahrnuje sloupec s kumulativními hodnotami do kontingenční tabulky. |
| Zahrnout regresi | Zahrnuje sloupec s hodnotami regrese do kontingenční tabulky. |
| Organizační jednotka | Řídí, zda se má uživatel při vytváření standardní zprávy v aplikaci Zprávy vyzvat k zadání organizační jednotky. |
| Nadřazená organizační jednotka | Řídí, zda se má uživatel při vytváření standardní sestavy v aplikaci Zprávy vyzvat k zadání nadřazené organizační jednotky. |
| Období hlášení | Určuje, zda se má uživatel při vytváření standardního přehledu v aplikaci Zprávy vyzvat k zadání období přehledu. |
| Horní limit | Řídí maximální počet řádků, které mají být zahrnuty do kontingenční tabulky. |

### Vlastní styl pro text a legendy v grafech { #custom-styling-for-text-and-legend-in-charts }

Pomocí nástroje pro stylování textu lze přizpůsobit následující možnosti: `Název grafu`, `Podtitul grafu`, `Zobrazit klíč legendy`, `Cílová čára`, `Základní čára`, `Název os` a  `Visačky` pro obě svislé i vodorovné osy. Nástroj pro úpravu textu umožňuje zvolit velikost písma, barvu a variantu kurzívou / tučným písmem. Je také možné zvolit umístění textu.

![](resources/images/data-visualizer/data-visualizer-text-styling-tool.png)

## Přidání přiřazených kategorií { #adding-assigned-categories }

Přiřazené kategorie je složená dimenze, která představuje přidružené kombinace možností kategorií ke kombinaci kategorií vybraného datového prvku. To lze přidat přetažením dimenze **Přiřazené kategorie** z nabídky dimenzí na levé straně a do rozložení vizualizace:

![](resources/images/data-visualizer/data-visualizer-assigned-categories.png)

Dalším způsobem přidávání přiřazených kategorií je přístup k možnosti **Přidat přiřazené kategorie** z kontextové nabídky dimenze`Data` (není k dispozici pro `Gauge`, `Rok za rokem` nebo `Jedna hodnota`).

## Přidání dalších os { #adding-more-axes }

Při kombinaci dat s různými měřícími stupnicemi získáte smysluplnější vizualizaci tím, že budete mít více než jednu osu. U `Column`, `Bar`, `Area` a `Line`  můžete kliknout na kartu **Serie** v dialogovém okně `Options`. Pokud je tato možnost zakázána, ujistěte se, že dimenze `Data` je na ose `Series` a že byly přidány alespoň dvě položky.

K dispozici jsou čtyři osy, dvě na levé straně (osa 1 a 3) grafu a dvě na pravé straně (osa 2 a 4). Každá osa má jinou barvu a položky grafu budou odpovídajícím způsobem vybarveny.

Poznámka: Pokud se používá více os, některé možnosti jako `Čáry`,` Svislá (y) osa` a `Sada barev` na ostatních záložkách možností budou deaktivovány.

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis.png)

## Použití více typů vizualizace { #using-multiple-visualization-types }

Je možné kombinovat graf `Sloupec` s položkami `Řádek` a naopak. To provedete kliknutím na kartu **Série** v dialogu `Možnosti` a změnou `Typu vizualizace`. To lze také kombinovat s použitím více os (jak je popsáno v části výše).

![](resources/images/data-visualizer/data-visualizer-series-tab-multi-axis-multi-type.png)

Výsledkem je graf, který kombinuje typy `Sloupec` a `Řádek`.

![](resources/images/data-visualizer/data-visualizer-multi-type-chart.png)

## Procházení dat { #data-drilling }

Tato funkce je povolena pro typ vizualizace `Kontingenční tabulka` a umožňuje procházet dál data kliknutím na hodnotovou buňku v tabulce. Otevře se kontextové menu s různými možnostmi.

Data můžete procházet podle organizační jednotky, což znamená procházení stromu organizačních jednotek nahoru a dolů. Procházení dat ovlivňuje výběr aktuální kóty v oblasti rozvržení.

![](resources/images/data-visualizer/data-visualizer-pt-drill.png)

## Spravujte uložené vizualizace { #manage-saved-visualizations }

Uložení vizualizací usnadňuje jejich pozdější vyhledání. Můžete se také rozhodnout je sdílet s ostatními uživateli nebo je zobrazit na ovládacím panelu.

### Otevřete vizualizaci { #open-a-visualization }

1.  Klikněte na **Soubor** \> **Otevřít**.

2.  Do vyhledávacího pole zadejte název vizualizace nebo kliknutím na šipky **<** a **>** přejděte mezi různými stránkami. Výsledek lze také filtrovat podle typu a vlastníka pomocí odpovídajících nabídek v pravém horním rohu.

3.  Klikněte na název toho, co chcete otevřít.

![](resources/images/data-visualizer/data-visualizer-open-dialog.png)

### Uložte vizualizaci { #save-a-visualization }

1. a) Klikněte na **Soubor** \> **Uložit**.

2. Zadejte **Název** a **Popis** pro vaši vizualizaci.

3. Klikněte **Uložit**.

![](resources/images/data-visualizer/data-visualizer-save-dialog.png)

### Přejmenujte vizualizaci { #rename-a-visualization }

1.  Klikněte na **Soubor** \> **Přejmenovat**.

2.  Zadejte nový název nebo popis.

3.  Klikněte na **Přejmenovat**.

![](resources/images/data-visualizer/data-visualizer-rename-dialog.png)

### Odstranit vizualizaci { #delete-a-visualization }

1.  Klikněte na **Soubor** \> **Odstranit**.

2.  Klikněte na **Smazat**.

### Získejte odkaz na vizualizaci { #get-the-link-to-the-visualization }

1. Klikněte na **Soubor** \> **Získat odkaz**.

2. Adresu URL lze zkopírovat prostřednictvím kontextové nabídky prohlížeče, která se otevře kliknutím pravým tlačítkem na odkaz.

![](resources/images/data-visualizer/data-visualizer-delete-dialog.png)

## Vizualizace interpretací { #visualization-interpretations }

Při prohlížení uložené vizualizace můžete rozšířit interpretace na pravé straně kliknutím na tlačítko Interpretace v pravém horním rohu. Zobrazí se také popis vizualizace. Popis podporuje formát RTF.

Nové interpretace lze přidat zadáním textového pole v pravém dolním rohu. Ostatní uživatelé mohou být uvedení jako `@uživatel`. Začněte zadáním znaku `@` plus první písmena uživatelského jména nebo skutečného jména a zobrazí se seznam odpovídajících uživatelů. Uvedení uživatelé obdrží interní zprávu DHIS2 s interpretací nebo komentářem. Interpretace lze také vidět v aplikaci **Ovládací panel**.

Text je možné formátovat pomocí **tučně**, _italic_ pomocí značek stylu Markdown `*` a `_` pro **tučně** a _italic_ (klávesové zkratky jsou také k dispozici: `Ctrl`/`Cmd` + `B` and `Ctrl`/`Cmd` + `I`). Je podporována omezená sada smajlíků, kterou lze použít zadáním jedné z následujících kombinací znaků: `:)` `:-)` `:(` `:-(` `:+1` `:-1`. URL jsou automaticky detekovány a převedeny na klikatelný odkaz.

Chcete-li zobrazit vizualizaci podle data konkrétní interpretace, klikněte na interpretaci nebo na její tlačítko `Zobrazit`, Tím se znovu vygeneruje vizualizace s příslušným datem, které je uvedeno vedle názvu vizualizace. Kliknutím na `Zpět na všechny interpretace` se obnoví vizualizace s aktuálním datem.

Chcete-li se přihlásit k odběru uložené vizualizace, klikněte na ikonu zvonku v pravém horním rohu. Poté budete dostávat interní zprávy, kdykoli se jinému uživateli líbí / vytvoří / aktualizuje interpretaci v této uložené vizualizaci.

![](resources/images/data-visualizer/data-visualizer-view-interpretation.png)

## Sdílet vizualizaci { #share-a-visualization }

Nastavení sdílení lze zobrazit kliknutím na **Soubor** \> **Sdílet**. Změňte nastavení sdílení pro skupiny uživatelů, které chcete upravit, dostupná nastavení jsou:

-   **Can edit and view**: Can view and edit the visualization.

-   **Lze jen zobrazit**:  Vizualizaci lze pouze zobrazit.

-   **Žádný přístup**: Nebude mít přístup k vizualizaci. Toto nastavení je použitelné pouze pro **Veřejný přístup** a **Externí přístup**.

Noví uživatelé mohou být přidáni jejich vyhledáním podle jména v části `Přidat uživatele a skupiny uživatelů`.

![](resources/images/data-visualizer/data-visualizer-share-dialog.png)

## Stáhnout { #download }

Vizualizace lze stáhnout pomocí nabídky **Stáhnout**. Všechny typy vizualizace podporují stahování `Grafika` a `Zdroj prostých dat`, s výjimkou typu `Kontingenční tabulka`, který lze stáhnout jako `Rozvržení  tabulky` a `Zdroj prostých dat`.

### `Grafika` ke stažení { #graphics-download }

Stáhne do počítače obrázek (.png) nebo PDF (.pdf).

### Stahování `rozložení tabulky` { #table-layout-download }

Stáhne do počítače soubor Excel (.xls), CSV (.csv) nebo HTML (.html).

### Stažení `Zdroje prostých dat` { #plain-data-source-download }

Zdroj dat vizualizace si můžete stáhnout ve formátu JSON, XML, Excel, CSV, JXRML nebo Raw data SQL s různými identifikačními schématy (ID, kód a název). Datový dokument používá identifikátory položek dimenze a otevře se v novém okně prohlížeče, aby se v adresním řádku zobrazila adresa URL požadavku na webové rozhraní API. To je užitečné pro vývojáře aplikací a dalších klientských modulů založených na webovém rozhraní DHIS2 nebo pro ty, kteří vyžadují zdroj dat plánu, například pro import do statistických balíčků.

**Dostupné formáty**

| Formát | Akce | Popis |
| --- | --- | --- |
| JSON | Klikněte na JSON | Stáhne formát JSON na základě vlastnosti ID, kódu nebo názvu. |
| XML | Klikněte na XML | Stáhne formát XML na základě vlastnosti ID, kódu nebo jména. |
| Microsoft Excel | Klikněte na Microsoft Excel | Stáhne formát Microsoft Excel na základě vlastnosti ID, kódu nebo Názvu. |
| CSV | Klikněte na CSV | Stáhne formát CSV na základě vlastnosti ID, kódu nebo názvu. |
| Sada hodnot dat XML | Klikněte na Pokročilé > XML | Stáhne hodnoty nezpracovaných dat jako XML, na rozdíl od dat, která byla agregována podle různých dimenzí. |
| Sada hodnot dat JSON | Klikněte na Pokročilé > JSON | Stáhne hodnoty nezpracovaných dat jako JSON, na rozdíl od dat, která byla agregována podél různých dimenzí. |
| JRXML | Klikněte na Pokročilé > JRXML | Produkuje šablonu Jasper Report, kterou lze dále přizpůsobit na základě vašich přesných potřeb a použít jako základ pro standardní hlášení v DHIS 2. |
| Nezpracovaná data SQL | Klikněte na Upřesnit > Nezpracovaná data SQL | Poskytuje skutečný příkaz SQL používaný ke generování vizualizace dat. Můžete jej použít jako zdroj dat v sestavě Jasper nebo jako základ pro pohled SQL. |

## Vizualizace jako mapa { #see-visualization-as-map }

Chcete-li vidět, jak by vizualizace vypadala na mapě, vyberte po dokončení vytváření vizualizace typ vizualizace `Otevřít jako mapu`.

![](resources/images/data-visualizer/data-visualizer-open-as-map.png)
