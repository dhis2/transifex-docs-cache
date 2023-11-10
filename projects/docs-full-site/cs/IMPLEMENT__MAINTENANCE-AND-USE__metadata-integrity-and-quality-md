---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/metadata-assessment/content/maintenance_use/metadata_quality_assessment.md"
revision_date: "2022-04-04"
---

# Integrita a kvalita metadat { #metadata-integrity-and-quality }

Zatímco kvalita metadat může být do jisté míry subjektivní, existuje řada klíčových principů, které lze objektivně posoudit a měly by být univerzálně dodržovány během implementací DHIS2. Za účelem posouzení kvality metadat lze provést posouzení metadat. V tomto kontextu můžeme metadatové hodnocení definovat jako kontrolu kvality konfigurace konkrétní implementace. I když jde o široký rozsah, naším cílem je rozdělit proces hodnocení na zvládnutelné části, které lze v průběhu času kontrolovat, stanovovat priority a opravovat. Pravidelné hodnocení metadat a průběžná údržba je důležitou součástí dlouhodobé konfigurace a údržby DHIS2. Zatímco konfigurační úlohy lze často provádět rychle pomocí řady různých mechanismů, bez řádné koordinace může nastat řada problémů, kterým může konfigurace systému DHIS2 v průběhu času čelit. Některé příklady účinků těchto konfiguračních problémů zahrnují:

-   Neschopnost najít správné položky při vytváření datových výstupů
-   Neschopnost správně rozčlenit data při vytváření datových výstupů
-   Nemožnost přístupu ke správným položkám při zadávání dat nebo vytváření datových výstupů
-   Problémy s kvalitou dat (některé příklady: významné nepřesnosti v dlouhodobých trendech údajů a četnosti vykazování, schopnost ukládat neplatné hodnoty dat, více proměnných představujících stejný koncept ukládající různé hodnoty dat)
-   Potíže s identifikací správných položek pro použití při konfiguraci mechanismů výměny dat
-   Chyby při upgradu verzí DHIS2
-   Spravovat obrovské množství neplatných metadat

Účelem této příručky je poskytnout nástroje a postupy k identifikaci problémů s metadaty. Vyvíjí se samostatná příručka o údržbě metadat, která pojednává o konfiguračních postupech, které mohou vést k problémům s kvalitou metadat, a pojednává o tom, jak se jim lze vyhnout, např. tím, že se vyhnete konfigurační práci v produkčních systémech a zavedete SoP pro modifikace metadat. A konečně, budoucí část Práce s metadaty poskytne návod, jak řešit problémy s metadaty, jako je odstranění objektů, které se již nepoužívají.

Údržba metadat a hodnocení metadat by měly být chápány jako související procesy, které se vzájemně doplňují.

1. Reaktivní proces: V důsledku problémů s konfigurací bude nutné systém DHIS2 odpovídajícím způsobem zkontrolovat a vyčistit.
2. Proaktivní proces: Aby se předešlo problémům s konfigurací, lze zavést procesy tak, aby konfigurace DHIS2 zůstala v průběhu času robustní.

![models_of_management](resources/images/models_of_management.png)

## Posouzení integrity a kvality metadat { #metadata_assessment_overview }

Reaktivní procesy jsou o hodnocení metadat za účelem identifikace potenciálních problémů a řešení těchto problémů. Může se jednat o náročný proces, který je třeba řádně naplánovat a věnovat čas a zdroje k identifikaci a řešení problémů. Zatímco plánování a provádění hodnocení metadat je stručně diskutováno [níže] (#metadata_assessment_planning), tato příručka se zaměřuje na praktičtější a techničtější aspekty hodnocení metadat a řešení běžných problémů.

Tato příručka se zaměřuje především na dva přístupy k hodnocení metadat:

1. prostřednictvím [ruční kontroly metadat](#metadata_assessment_manual)
2. prostřednictvím [nástroje pro hodnocení metadat](#metadata_assessment_tool), který lze připojit přímo k DHIS2 a provádět kontroly metadat

Oba tyto přístupy jsou popsány níže.

### Plánování a provádění posouzení metadat { #metadata_assessment_planning }

Chcete-li provést hodnocení, možná budete chtít začít tím, že získáte vstup od široké škály zainteresovaných stran. Přitom může být užitečné zdokumentovat rozsah problémů diskutovaných v této příručce vytvořením souhrnných statistik o problémech, které byly identifikovány. To může být velmi užitečné pro prezentaci širokému publiku a může být použito k podpoře buy-in poskytnutím stručných vysvětlení problémů, které byly identifikovány. V **Referenční příručce pro hodnocení metadat** najdete nástroje, které vám pomohou vytvořit rychlé souhrnné počty problémů, které najdete ve své vlastní implementaci, a také nástroje, které generují podrobnější zprávy o každé konkrétní položce, která vyžaduje pozornost. Doporučujeme, aby hodnocení zahrnovalo následující součásti:

1. Definujte rozsah hodnocení a sdílejte jej s příslušnými zúčastněnými stranami
2. Identifikace rozsahu problémů v rámci implementace prostřednictvím generování a dokumentování souhrnných statistik toho, co bylo nalezeno
3. Prezentace těchto zjištění zpět skupině zainteresovaných stran
4. Identifikovat jednotlivé položky, které jsou problematické, a navrhnout strategie, jak je podle potřeby zmírnit nebo opravit
5. Upřesnění a stanovení priorit oprav
6. Implementace těchto oprav ve vývoji následovaná produkčními systémy

## Manuální kontrola metadat { #metadata_assessment_manual }

Použití [nástroje pro hodnocení metadat](#metadata_assessment_tool) a vestavěné [kontroly integrity dat](#data_admin_data_integrity) je účinný způsob identifikace mnoha problémů s metadaty v DHIS2, některé procesy kontroly nelze automatizovat. To zahrnuje přezkoumání:

-   Konvence pojmenování
-   Vzorec indikátoru
-   Duplicitní objekty metadat
-   Duplicitní zdroje dat
-   Konfigurace položky ovládacího panelu
-   Přiřazení organizační jednotky programu a datové sady
-   Sdílení programů a datových sad

### Problémy s dokumentací { #documenting-issues }

Kontrola metadat k identifikaci potenciálních problémů by měla být vždy prováděna s cílem tyto problémy řešit. Opravy lze někdy provést okamžitě, ale v mnoha případech to není možné. Například může být nutné konzultovat s různými zúčastněnými stranami, aby se identifikoval vhodný zdroj dat nebo definice metadat, nebo je řešení problémů technicky komplikované a vyžaduje řádné testování a přezkoumání. Je proto důležité vytvořit mechanismus pro zachycení zjištěných problémů, aby bylo možné je sledovat a vytvořit plán na jejich řešení.

### Konvence pojmenování { #naming-conventions }

Úplný rozpis principů dobrých konvencí pojmenování naleznete v tomto [zdroji](https://docs.dhis2.org/en/topics/metadata/dhis2-who-digital-health-data-toolkit/naming-conventions.html). Pokud je to možné, měli byste zvážit jejich implementaci do systému (systémů), který kontrolujete.

Chcete-li názvy svých metadat aktualizovat hromadně, zvažte použití [editoru metadat DHIS2](https://workspace.google.com/marketplace/app/d2_metadata_review_tool/672531419470). To vám umožní upravit všechna vaše metadata v tabulce Google a synchronizovat vaše informace zpět na server. Úplného průvodce editorem metadat si můžete prohlédnout [zde](https://docs.google.com/document/d/1Y4u78llIOTb5gNPHLJks528kbz8czXH9O6yKMEaLFI0/edit?usp=sharing).

### Vzorec indikátoru { #indicator-formula }

K určení, zda je vzorec ukazatele správný, může být zapotřebí ruční revize vzorce indikátoru. Revize vzorce indikátoru, i když je potenciálně problémem konfigurace, má potenciál ovlivnit kvalitu dat a datové výstupy, pokud se o vzorci vytvoří nesprávné předpoklady. Příklady problémů, které budete chtít zkontrolovat při kontrole vzorce indikátoru, zahrnují:

1. Zajištění toho, že součástí čitatele a jmenovatele jsou správné datové prvky porovnáním datových prvků s popisy čitatele a jmenovatele
2. Zajištění, že byl pro kontrolovaný indikátor vybrán správný typ indikátoru
3. Je-li to možné, kontrola, zda je jmenovatel správně definován (nicméně; může se jednat spíše o problém s kvalitou dat a je ponecháno na podrobnější kontrolu kvality dat)

Můžete použít [editor metadat DHIS2](https://workspace.google.com/marketplace/app/d2_metadata_review_tool/672531419470) ke kontrole některých vzorců, pokud víte, jak se to nastavuje, ale tradičnější způsob indikátorů procházení přes uživatelské rozhraní lze provést pomocí [aplikace prohlížeče metadat WHO](https://apps.dhis2.org/app/af9a31fb-350c-4130-964b-3a413183aa54).

### Duplicitní zdroje dat { #duplicate-data-sources }

Duplicitní zdroje dat vznikají, když máte v systému DHIS2 více proměnných, které vykazují stejný koncept. Obvykle existují 3 typy duplicitních zdrojů dat, které můžete vidět v DHIS2:

-   Duplicitní proměnné ve stejném formuláři sběru dat
-   Duplicitní proměnné mezi různými programy (obvykle na různých formulářích)
-   Duplicitní proměnné v programech (buď ve stejných nebo různých formulářích)

#### Duplicitní proměnné ve stejném formuláři sběru dat { #duplicate-variables-within-the-same-data-collection-form }

K tomu dochází, když jeden nebo více datových prvků poskytuje součet, který je duplikován jedním nebo více jinými datovými prvky ve stejném formuláři. Jako příklad si můžeme prohlédnout formuláře dostupné na obrázku 1.

![duplicate_vars_same_form](resources/images/duplicate_vars_same_form.png) **Obrázek 1**

Když k tomu dojde, je obtížné určit, jaká je správná hodnota.

#### Duplicitní proměnné mezi různými programy { #duplicate-variables-between-different-programs }

K tomu dochází, když máte dva nebo více programů v integrovaném systému, které shromažďují stejné informace (obrázek 2). V některých případech se programy nemohou dohodnout na hodnotě a může být nutné ji zachovat tak, jak je. To se stane problematickým při pokusu o stanovení dohodnuté národní hodnoty, avšak hodnoty se mohou mezi různými programy lišit a nedoporučuje se to udržovat tak, jak je.

![duplicate_vars_different_programs](resources/images/duplicate_vars_different_programs.png) **Obrázek 2**

#### Duplicitní proměnné v programech (buď ve stejných nebo různých formulářích) { #duplicate-variables-within-programs-either-on-the-same-or-different-forms }

K tomu dochází, když jsou stejné informace shromažďovány ve stejném programu (obrázek 3). To může být problematické, protože pokud je to možné, měla by existovat shoda mezi hodnotami (a nemusí tomu tak být, když je tento problém zjištěn)

![duplicate_vars_same_programs](resources/images/duplicate_vars_same_programs.png) **Obrázek 3**

#### Řešení duplicitních zdrojů dat { #resolving-duplicate-data-sources }

Podobně jako u problémů s definováním jmenovatelů může být nutné toto ponechat pro podrobnější kontrolu kvality dat. Vzhledem k tomu, že tato zjištění budou často vyžadovat kontrolu/revizi formuláře napříč různými programy, aby bylo možné racionalizovat tyto duplicitní zdroje dat, tento problém pravděpodobně nevyřeší okamžitá změna konfigurace. Je však důležité tyto problémy identifikovat a pracovat s programy na jejich vyřešení na základě místních postupů.

### Konfigurace položky ovládacího panelu { #dashboard-item-configuration }

Při kontrole položek ovládacího panelu je třeba vzít v úvahu dvě věci:

1. Musí být položka ovládacího panelu sdílena, aby ji mohly zobrazit skupiny uživatelů, se kterými je řídicí panel sdílen?
2. Potřebuje položka ovládacího panelu relativní organizační jednotky nebo období, aby ji bylo možné pravidelně znovu používat / aktualizovat

V případě, že položka ovládacího panelu potřebuje zobrazit údaje za pevně stanovené období nebo organizační jednotku, není třeba na položku aplikovat žádnou relativitu. Pokud by položka měla být rutinně aktualizována novými údaji nebo uživatelé, kterým je dashboard sdílen, nemají přístup k pevným organizačním jednotkám vybraným v rámci položky, pak by tyto položky měly být zkontrolovány a případně aktualizovány správným výběrem relativního období a organizační jednotky.

### Přiřazení organizační jednotky programu a datové sady { #program-and-data-set-organisation-unit-assignment }

Zkontrolujte, zda jsou programy a datové sady přiřazeny pouze organizačním jednotkám, u kterých se očekává, že o nich budou podávat zprávy. U datových sad to může způsobit problémy s úplností hlášení (počet očekávaných hlášení může být vyšší, než by měl být) a potenciálně vkládání dat tam, kde by nemělo být; zatímco v případě programů byste mohli mít sledované subjekty a/nebo události registrované v organizačních jednotkách, neměly by být.

<!--
#### Přesun souhrnných dat { #moving-aggregate-data }


#### Přesun dat Trasovače{ #moving-tracker-data }
-->

### Sdílení programu a datové sady { #program-and-data-set-sharing }

Zkontrolujte, zda byla nastavení metadat a sdílení dat správně použita pro programy i soubory dat. Zejména pokud existují uživatelé nebo skupiny uživatelů, kteří nemohou provádět operace s programy nebo datovými sadami, které by měli umět, může být nutné tato nastavení sdílení upravit.

Podrobnější rozpis použití nastavení sdílení na programy a soubory dat lze nalézt jak v [dokumentaci](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/about-sharing-of-objects.html), tak v řadě videí na [YouTube](https://www.youtube.com/playlist?list=PLo6Seh-066RwslDmyZkiKjejgMCKNaJTC).

### Kontroly související s kategorií { #category-related-checks }

#### Duplicitní možnosti kategorií { #duplicate-category-options }

Možnosti kategorií mohou a měly by být znovu použity ve více kategoriích, aby reprezentovaly stejný koncept (např. věková skupina). Kromě snížení nepořádku a potenciálního matoucího množství možností pro stejný koncept umožňuje tato analýza datovou analýzu, protože datové prvky používající stejnou možnost kategorie mohou být prezentovány společně se stejnou dezagregací ve vizualizačních nástrojích.

Pokud jsou identifikovány duplicitní možnosti kategorií a tyto jsou zahrnuty v kategoriích, které jsou součástí kombinací kategorií již přidružených k datům, _neměli_ byste se je pokoušet deduplikovat. Pokud však jedna z možností kategorie ještě nebyla použita, lze ji odstranit a použít ostatní možnosti.

#### Rozčlenění kategorií { #category-disaggregations }

Možnosti kategorií v kategorii datových prvků by se obecně měly sčítat do smysluplného součtu, jak je popsáno v [části návrhu souhrnného systému] (#categories-and-custom-dimensions). Je to součet kategorie, která se standardně zobrazuje, když se podíváte na hodnotu pro datový prvek rozčleněný tímto datovým prvkem. Příkladem tohoto špatného postupu je vytvoření kategorie pro „ambulantní pacienty“ s možnostmi „Případy“ a „Úmrtí“, která se použije na datové prvky pro různé diagnózy, jako je „Malárie“. Ve výchozím nastavení uživatel při pohledu na datový prvek „Malárie“ získá součet „Případů malárie“ a „Úmrtí na malárii“, což je číslo, které nedává smysl.

Existují určité případy, kdy může mít smysl se od tohoto obecného pravidla odchýlit, zejména když použití takové kategorie může _podstatně_ snížit počet požadovaných datových prvků. V těchto případech by měla být pro kombinaci kategorií, které je kategorie součástí, povolena možnost „Přeskočit celkový počet kategorií v přehledech“.

## Použití nástroje pro hodnocení metadat { #metadata_assessment_tool }

Zatímco pro řadu problémů jsou nutné ruční kontroly, byl také vyvinut [nástroj pro hodnocení metadat](https://github.com/dhis2/metadata-assessment), který automatizuje řadu kontrol kvality dat. To zahrnuje možnost získat souhrnné výsledky (počet porušení) vestavěných [kontrol integrity dat](#data_admin_data_integrity). Nástroj pro hodnocení metadat není v současné době integrován do samotného DHIS2, ale jedná se o samostatný nástroj založený na [R](https://www.r-project.org). Tato část se bude zabývat tím, jak interpretovat a používat výstup nástroje pro hodnocení, zatímco postup stažení, instalace a spuštění nástroje je popsán v [úložišti GitHub](https://github.com/dhis2/metadata-assessment) nástroj. Seznam s popisy kontrol metadat zahrnutých v nástroji je popsán v [příloze A](#metadata_assessment_tool_annex_a).

Nástroj pro hodnocení metadat je založen především na pohledech DHIS2 SQL: nástroj importuje sadu pohledů SQL do hodnocené databáze DHIS2 (dva pro každou metriku kvality dat) a přistupuje k výstupům těchto pohledů SQL prostřednictvím webového rozhraní API a prezentuje uživatelům. Kromě toho tento nástroj předkládá určité výstupy přímo na základě dotazů webového rozhraní API (týkajících se uživatelů) a může také zobrazovat výsledky vestavěných kontrol [integrity dat](#data_admin_data_integrity).

> **Upozornění** Nástroj by neměl být používán přímo v produkčních databázích. Zatímco jedinou změnou, kterou nástroj provede v databázi, je import pohledů SQL, určité kontroly mohou být dlouhodobé a náročné na zdroje a mohou ovlivnit interakci uživatelů se systémem. K dispozici je parametr pro zakázání pomalých dotazů.

### Zpráva { #the-report }

Samotná zpráva je uspořádána do čtyř částí.

#### Souhrnná tabulka { #summary-table }

Souhrnná tabulka „Problémy s metadaty“ poskytuje přehled všech různých metrik kvality metadat a umožňuje řazení a filtrování. To je užitečné pro získání rychlého přehledu o výsledcích (například pokud existují nějaké "kritické" nebo "závažné" problémy) nebo pokud hledáte konkrétní problémy (například pokud existují nějaké problémy týkající se organizačních jednotek).

![Souhrnná tabulka](./resources/images/metadata_assessment_tool_summary_table.png)

#### Uživatelé { #users }

Sekce „Uživatelé“ poskytuje klíčové metriky související s uživateli v systému. Kromě základních informací o celkovém počtu uživatelů a počtu přihlášených uživatelů za určité období obsahuje také informace, které mohou být základem pro změny v postupech správy uživatelů:

-   _Uživatelé, kteří se nikdy nepřihlásili_: velký počet uživatelských účtů, které nebyly nikdy použity, značí problémy s procesem pozvání/vytvoření účtu. Pokud byly tyto účty vytvořeny s výchozím heslem, mohou také představovat bezpečnostní problém.
-   _Procento uživatelů, kteří jsou deaktivováni_: Společně s celkovým počtem uživatelů a uživatelů, kteří se nedávno přihlásili, to může naznačovat, zda jsou uživatelské účty deaktivovány, když uživatelé z různých důvodů již nepotřebují nebo by měli mít přístup do systému. (např. protože opustí svou pozici).
-   _Počet / procento uživatelů, kteří jsou superuživateli_: Pouze hrstka uživatelů by měla mít nanejvýš práva superuživatele (oprávnění „VŠICHNI“).

Kromě toho mohou být užitečné dva grafy zobrazující rozložení v čase, kdy se uživatelé naposledy přihlásili, a rozložení uživatelů v hierarchii organizační jednotky, abyste pochopili, zda je přiřazení a správa uživatelů správně zpracována.

![Uživatelé](./resources/images/metadata_assessment_tool_users.png)

#### Pokyny { #guidance }

Sekce s pokyny uvádí stejné metriky jako souhrnná tabulka (a opakuje se v [příloze A](#metadata_assessment_tool_annex_a)), ale spolu s vysvětlením a doporučeným postupem. Je uspořádána do sekcí podle tématu.

![Pokyny](./resources/images/metadata_assessment_tool_guidance.png)

### Interpretace výsledků { #interpreting-the-results }

Při interpretaci výsledků zprávy je důležité mít na paměti, že ne všechny problémy uvedené ve zprávě jsou nutně skutečné problémy. V tomto ohledu je důležité mít na paměti _závažnost_ různých kontrol:

-   _Info_ označuje, že kontrola je zahrnuta především proto, aby poskytovala užitečné kontextové informace, např. udávající celkový počet určitého typu objektu.
-   _Varování_ se vztahuje na kontroly, které buď poukazují na problémy, které mohou být problematické, nebo naznačují, že metadata nejsou dobře spravována, ale obecně nepovedou k problémům s fungováním systému.
-   _Závažné_ problémy mohou vést k vážným problémům, například analytické výstupy zobrazující nesprávná čísla nebo žádná data.
-   _Kritické_ problémy jsou ty, které téměř jistě způsobí různé problémy, například potenciálně způsobí selhání procesu generování analytické tabulky.

I když každá z různých metrik kvality dat zahrnuje doporučení, jak by se měl konkrétní problém řešit, obecně nezachází do podrobností, technických kroků, které by měly být podniknuty k vyřešení problému. Není možné poskytnout jasné vodítko pro všechny problémy a problémy se liší od zcela základních (jako je seskupování datových prvků) až po velmi složité (například duplicitní kombinace možností kategorií v rámci kombinace kategorií). Obecně se doporučuje, pokud je to možné, řešit problémy prostřednictvím uživatelského rozhraní DHIS2 nebo webového rozhraní API, protože to poskytuje určité ověření provedených změn. Pouze jako poslední možnost by měly být problémy v databázi správně opraveny. Všechny změny kromě nejzákladnějších (jako je seskupování datových prvků) by měly být důkladně otestovány v neprodukčním systému.

Připravuje se samostatná část v implementační příručce, která poskytne další příklady a pokyny k řešení běžných problémů s metadaty, jako jsou dávkové úpravy, mazání datových prvků s daty atd.

## PŘÍLOHA A – metriky nástroje pro hodnocení metadat { #metadata_assessment_tool_annex_a }

Aktualizováno 14.02.2022.

<!-- TODO: add "fixed" section on users? -->
<!-- Extracted from https://github.com/dhis2/metadata-assessment/tree/main/yaml -->

### Kategorie { #categories }

#### Kategorie bez možností kategorií. { #categories-with-no-category-options }

Kategorie by vždy měly mít alespoň jednu možnost kategorie.

**Závažnost**: Varování

**Doporučení:** Jakékoli kategorie bez možností kategorií by měly být ze systému odstraněny, pokud se nepoužívají. V opačném případě by měly být do kategorie přidány vhodné možnosti kategorie.

#### Další výchozí kombinace možností kategorie na základě možnosti kategorie. { #additional-default-category-option-combos-based-on-category-option }

V systému by měla být pouze jedna kombinace možností kategorie „výchozí“. Použití více výchozích kombinací možností kategorií může vést k nesrovnalostem jak v zadávání dat, tak v analytických výstupech.

**Závažnost**: Kritická

**Doporučení:** Všechny odkazy na další výchozí kombinaci možností kategorie by měly být nahrazeny požadovanou výchozí kombinací možností kategorie.

#### Možnosti kategorií bez kategorií. { #category-options-with-no-categories }

Všechny možnosti kategorií by měly patřit alespoň do jedné kategorie.

**Závažnost**: Varování

**Doporučení:** Možnosti kategorií, které nejsou součástí žádné kategorie, by měly být odstraněny nebo případně přidány do příslušné kategorie.

#### Kombinace možností kategorií s nesouvislými přidruženími. { #category-option-combinations-with-disjoint-associations }

Za určitých okolností mohou v systému existovat kombinace možností kategorií, ale nemají žádnou přímou souvislost s možnostmi kategorií, které jsou spojeny s kombinacemi kategorií. K této situaci obvykle dochází, když byly do kategorie přidány možnosti kategorie a poté je kategorie přidána do kombinace kategorií. V tomto okamžiku jsou v systému vytvořeny nové kombinace možností kategorií. Pokud je potom některá z možností kategorie odstraněna v jedné ze základních kategorií, může dojít k tzv. kombinaci možností disjunktní kategorie. Toto je kombinace možností kategorie, která nemá přímou souvislost s možnostmi kategorie v žádné z kategorií.

**Závažnost**: Těžká

**Doporučení:** Kombinace možností nesouvislých kategorií by měly být ze systému odstraněny, pokud je to možné. Pokud jsou však s kombinací možností kategorie spojena nějaká data, bude nutné rozhodnout, jak s těmito daty naložit.

#### Kombinace možností kategorií s nesprávnou mohutností. { #category-option-combinations-with-incorrect-cardinality }

Všechny kombinace možností kategorií by měly mít přesně stejný počet přidružení možností kategorií jako počet kategorií v kombinaci kategorií. Pokud jsou v kombinaci kategorií dvě kategorie, pak by každá kombinace možností kategorie měla mít přesně dvě možnosti kategorií.

**Závažnost**: Těžká

**Doporučení:** Kombinace možností kategorií, které mají nesprávnou mohutnost, budou analytickým systémem DHIS2 ignorovány a měly by být odstraněny.

#### Možnosti kategorií s více než jedním členstvím pro kategorii. { #category-options-with-more-than-one-membership-for-a-category }

Nulla vitae feugiat blandit natoque placerat elementum pharetra senectus et aenean faucibus pellentesque. Quam, donec auctor in et mi penatibus penatibus. Mauris massa mauris sem vehicula eu hac fermentum odio mattis sed. Habitant convallis, pellentesque aenean, a nunc vitae non sapien eu suspendisse. Amet nisi sed quam hac.

**Závažnost**: Těžká

**Recommendation:** Bibendum pellentesque nibh nisl vitae rutrum quis vestibulum feugiat porta et netus parturient mauris. Nec nascetur libero lacinia id vel mauris pulvinar at augue pharetra. Elementum urna eget mauris magnis proin. Risus sed sapien ante himenaeos. Hac vitae vestibulum vestibulum nulla vestibulum ut non consectetur vel lectus ultricies euismod. Suscipit sed sed orci.

#### Kombinace kategorií bez kategorií. { #category-combinations-with-no-categories }

Všechny kombinace kategorií by měly být spojeny s jednou nebo více kategoriemi.

**Závažnost**: Varování

**Doporučení:** Kombinace kategorií bez kategorií nejsou v DHIS2 použitelné. Měly by být buď odstraněny, nebo by měly být do seznamu kategorií přidány správné kategorie.

#### Kombinace možností kategorií bez kombinace kategorií. { #category-options-combinations-with-no-category-combination }

Všechny kombinace možností kategorie by měly být spojeny s kombinací kategorií. V určitých případech, kdy jsou odstraněny kombinace kategorií, může dojít k poškození propojení mezi kombinací možností kategorie a kombinací kategorií.

**Závažnost**: Varování

**Doporučení:** Zkontrolujte, zda jsou s dotyčnými kombinacemi kategorií spojena nějaká data. Data by měla být pravděpodobně odstraněna nebo migrována na platnou kombinaci možností kategorie. Jakákoli data, která jsou spojena s některou z těchto kombinací možností kategorií, nebudou dostupná ani prostřednictvím modulů pro zadávání dat, ani prostřednictvím žádné z analytických aplikací.

#### Duplicitní kombinace možností kategorií v rámci kombinace kategorií. { #duplicated-category-option-combinations-within-a-category-combination }

V rámci každé kombinace kategorií by měla existovat jedinečná sada kombinací možností kategorií. Za určitých okolností mohou v systému existovat duplicitní kombinace možností kategorií. To obvykle vyplývá ze změn kombinací kategorií poté, co byly vytvořeny, nebo přímou manipulací s různými tabulkami kategorií v databázi. To může mít za následek, že se určité kombinace datových prvků / kategorií nezobrazí nebo nebudou dostupné na obrazovkách pro zadávání dat a / nebo v analytických aplikacích.

**Závažnost**: Těžká

**Doporučení:** Duplicitní kombinace možností kategorií v rámci kombinace kategorií budou vyžadovat sloučení kombinací možností kategorií dohromady. To bude vyžadovat přímou manipulaci s databází a mělo by být vždy provedeno nejprve v testovacím prostředí. Teprve poté, co důkladně otestujete svůj postup a budete mít jistotu, že funguje, byste měli provést postup ve svém produkčním prostředí. Implementační tým DHIS2 vytvořil řadu funkcí SQL, které vám pomohou odstranit tyto duplicitní COC z vašeho systému.

#### Kategorie se stejnými možnostmi kategorií { #categories-with-the-same-category-options }

Kategorie s přesně stejnými možnostmi kategorií by měly být považovány za sloučené. Categorie s přesně stejnými možnostmi kategorií mohou uživatelé při analýze snadno zaměnit.

**Závažnost**: Varování

**Doporučení:** Pokud již byly vytvořeny kombinace kategorií s duplicitními kategoriemi, doporučujeme neprovádět žádnou akci, ale spíše zajistit, aby uživatelé pochopili, že mohou existovat dvě duplicitní kategorie.

Pokud se jedna z kategorií nepoužívá v žádné kombinaci kategorií, je třeba zvážit její odstranění ze systému.

### Grafy { #charts }

#### Grafy, které nebyly zobrazeny za posledních 12 měsíců { #charts-which-have-not-been-viewed-in-the-past-12-months }

Grafy by měly být pravidelně prohlíženy v systému. V mnoha případech mohou uživatelé vytvářet grafy pro dočasné účely a pak je nikdy nesmazat. To může nakonec vést k nedostatku pořádku v systému. To může vést k tomu, že v aplikaci vizualizace bude obtížné najít grafy.

**Závažnost**: Varování

**Doporučení:** Nepoužívané grafy může uživatel s dostatečným oprávněním odstranit přímo pomocí aplikace pro vizualizaci dat. Pokud jsou však grafy součástí jakéhokoli ovládacího panelu, bude nutné je také z ovládacího panelu odstranit.

### Ovládací panely { #dashboards }

#### Celkový počet dashboardů v systému { #total-number-of-dashboards-in-the-system }

Celkový počet ovládacích panelů v systému. **Závažnost**: Informace

**Doporučení:** DHIS2 by měl obsahovat užitečné ovládací panely pro uživatele.

#### Ovládací panely s 1 nebo méně zobrazeními za poslední tři roky { #dashboards-with-1-or-fewer-views-over-the-past-three-years }

Ovládací panely, které uživatelé nevidí, mohou indikovat omezené využití dat, že ovládací panely nebyly navrženy se záměrem opětovného použití (například jako součást školení nebo jednorázové analýzy dat), nebo že uživatel vlastnící ovládací panel již není aktivní.

**Závažnost**: Varování

**Doporučení:** Pokud jsou panely relevantní a užitečné, ale nezobrazují se, je třeba se snažit zvýšit využití dat (např. zkontrolovat nastavení sdílení, komunikovat s uživateli, plánovat tréninková cvičení atd.). V ostatních případech by uživatelé s oprávněním superuživatele měli mít možnost odstraňovat ovládací panely vyhledáním názvu nebo v dávkách. Před odebráním ze systému byste se také měli ujistit, že ovládací panel není používán žádnou analýzou push.

#### Panely, které nebyly za poslední rok zobrazeny. { #dashboards-not-viewed-in-the-past-one-year }

Ovládací panely, které uživatelé nevidí, mohou indikovat omezené využití dat, že ovládací panely nebyly navrženy se záměrem opětovného použití (například jako součást školení nebo jednorázové analýzy dat), nebo že uživatel vlastnící ovládací panel již není aktivní.

**Závažnost**: Varování

**Doporučení:** Pokud jsou panely relevantní a užitečné, ale nezobrazují se, je třeba se snažit zvýšit využití dat (např. zkontrolovat nastavení sdílení, komunikovat s uživateli, plánovat tréninková cvičení atd.). V ostatních případech by uživatelé s oprávněním superuživatele měli mít možnost odstraňovat ovládací panely vyhledáním názvu nebo v dávkách. Před odebráním ze systému byste se také měli ujistit, že ovládací panel není používán žádnou analýzou push.

#### Celkový počet panelů bez položek. { #total-number-of-dashboards-with-no-items }

Všechny ovládací panely by měly mít obsah. Panely bez obsahu neslouží žádnému účelu a mohou ztížit nalezení relevantního ovládacího panelu s obsahem.

**Závažnost**: Informace

**Doporučení:** Ovládací panely bez obsahu, který nebyl upraven v posledních, např. Na smazání je třeba zvážit 14 dní.

### Datové prvky (agregát) { #data-elements-aggregate }

#### Celkový počet agregovaných datových prvků { #total-count-of-aggregate-data-elements }

Přehled počtu agregovaných datových prvků v systému. **Závažnost**: Informace

**Doporučení:** DHIS2 by měl obsahovat užitečné datové prvky pro uživatele.

#### Souhrnné datové prvky nepoužívané v žádných oblíbených (přímo nebo prostřednictvím indikátorů) { #aggregate-data-elements-not-used-in-any-favourites-directly-or-through-indicators }

Všechny agregované datové prvky, které jsou zachyceny v DHIS2, by měly být použity k vytvoření určitého typu výstupu analýzy (grafy, mapy, tabulky). To může být jejich použitím přímo ve výstupu nebo jejich přispěním k výpočtu indikátoru, který je použit jako výstup.

**Závažnost**: Varování

**Doporučení:** Datové prvky, které nejsou běžně v analýze přezkoumávány, ať už přímo nebo nepřímo prostřednictvím indikátorů, by měly být přezkoumány, aby se zjistilo, zda je stále třeba shromažďovat. Pokud mají být použity při rutinní kontrole, pak by měly být pomocí nich vytvořeny související výstupy. Pokud tyto datové prvky nebudou použity pro žádný typ kontroly informací, je třeba zvážit jejich archivaci nebo vymazání.

#### Souhrnné datové prvky přiřazené 1 nebo méně organizaci (prostřednictvím datových sad). { #aggregate-data-elements-assigned-to-1-or-less-orgunit-through-data-sets }

Datové prvky, které jsou součástí souhrnné datové sady, by měly být přiřazeny alespoň jedné organizační jednotce.

**Závažnost**: Varování

**Doporučení:** Pokud je datová sada aktivní, zkontrolujte přiřazení organizačních jednotek. Pokud datová sada není aktivní, měla by být datová sada a její související datové prvky odstraněny ze systému.

#### Souhrnné datové prvky, které nejsou v žádné skupině datových prvků. { #aggregate-data-elements-not-in-any-data-element-groups }

Všechny datové prvky by měly být ve skupině datových prvků. To uživatelům umožňuje snáze najít datové prvky v analytických aplikacích a také přispívá k tomu, že mají úplnější sady skupin datových prvků. Operace údržby lze také zefektivnit aplikací hromadných nastavení (např. sdílení) na všechny datové prvky v rámci skupiny datových prvků.

**Závažnost**: Varování

**Doporučení:** Datové prvky, které nejsou ve skupině datových prvků, by měly být přidány do příslušné skupiny datových prvků. Pokud datové prvky nejsou potřeba, měly by být vymazány.

#### Souhrnné datové prvky, které se za posledních 100 dní nezměnily a neobsahují žádné datové hodnoty. { #aggregate-data-elements-that-have-not-been-changed-in-last-100-days-and-do-not-have-any-data-values }

"Opuštěné" datové prvky. Jedná se o datové prvky, které nebyly změněny po dobu alespoň 100 dnů a nejsou s nimi spojeny žádné datové hodnoty. Často jsou výsledkem nových nebo změněných konfigurací, které byly v určitém okamžiku opuštěny.

**Závažnost**: Varování

**Doporučení:** Datové prvky, ke kterým nejsou přidružena žádná data a které se neplánuje začít používat pro sběr dat, by měly být smazány.

#### Agregovat datové prvky BEZ datových hodnot. { #aggregate-data-elements-with-no-data-values }

Datové prvky by měly být obecně vždy spojeny s hodnotami dat. Pokud datové prvky existují v datovém souboru, který je aktivní, ale nejsou k nim přiřazeny žádné datové hodnoty, nemusí být součástí obrazovek pro zadávání dat.

**Závažnost**: Varování

**Doporučení:** Zvažte odstranění datových prvků bez datových hodnot.

#### Agregovat datové prvky bez datových hodnot za poslední 3 období (na základě typu období sady dat). { #aggregate-data-elements-with-no-data-values-in-the-last-3-periods-based-on-data-set-period-type }

Datové prvky bez aktuálních datových hodnot pravděpodobně spadají do jedné ze dvou kategorií: 1) byly použity dříve a obsahují užitečná / relevantní data, 2) nebyly použity žádným smysluplným způsobem (např. hodnoty dat pocházejí z testování během konfigurace nebo malého pilotního projektu) a data nejsou užitečná / relevantní.

**Závažnost**: Varování

**Doporučení:** Pokud datové prvky obsahují užitečná historická data, měly by být uchovány. Zvažte přejmenování datových prvků a / nebo datových sad, aby bylo jasné, že se již nepoužívají ke sběru dat. Datové prvky, které se aktivně nepoužívají a nemají přidružená žádná cenná data.

### Datové prvky (tracker) { #data-elements-tracker }

#### Celkový počet datových prvků trackeru { #total-count-of-tracker-data-elements }

Přehled počtu datových prvků trackeru v systému. **Závažnost**: Informace

**Doporučení:** DHIS2 by měl obsahovat užitečné datové prvky pro uživatele.

#### Datové prvky sledování nejsou v žádné skupině datových prvků. { #tracker-data-elements-not-in-any-data-element-groups }

Všechny datové prvky by měly být ve skupině datových prvků. To uživatelům umožňuje snáze najít datové prvky v analytických aplikacích a také přispívá k tomu, že mají úplnější sady skupin datových prvků. Operace údržby lze také zefektivnit aplikací hromadných nastavení (např. sdílení) na všechny datové prvky v rámci skupiny datových prvků.

**Závažnost**: Varování

**Doporučení:** Datové prvky, které nejsou ve skupině datových prvků, by měly být přidány do příslušné skupiny datových prvků. Pokud datové prvky nejsou potřeba, měly by být vymazány.

### Datové sady { #datasets }

#### Celkový počet souborů dat. { #total-number-of-data-sets }

Celkový počet datových sad v systému. **Závažnost**: Informace

**Doporučení:** DHIS2 by měl obsahovat datové sady, které jsou užitečné pro zadávání dat.

#### Soubory dat, které se za posledních 100 dní nezměnily a jsou přiřazeny 1 nebo méně organizacím. { #data-sets-that-have-not-been-changed-in-last-100-days-and-are-assigned-to-1-or-less-orgunits }

Datové sady by obecně měly být přiřazeny více organizačním jednotkám, pokud jsou používány, nebo by měly být nedávno upraveny (např. posledních 100 dní), pokud jsou ve vývoji. Nepoužívané datové sady představují zbytečný nepořádek v databázi a mohou zmást uživatele a správce. Výjimkou jsou datové soubory, které jsou spojeny s historickými daty, například formuláře hlášení z předchozích let, které se již nepoužívají, a datové soubory, které jsou navrženy tak, aby je bylo možné používat pouze v organizační jednotce (např. na národní úrovni).

**Závažnost**: Varování

**Doporučení:** Datové sady, které se aktivně nepoužívají nebo se nevyvíjejí, by měly být ze systému odstraněny, aby se snížila nepřehlednost systému a velikost metadat. Před odstraněním datových sad ověřte, že datová sada není spojena s historickými daty a není z tohoto důvodu uchovávána.

#### Soubory dat bez hodnot dat za poslední 3 období (na základě typu období souboru dat). { #data-sets-with-no-data-values-in-the-last-3-periods-based-on-data-set-period-type }

Soubory dat, k nimž nejsou přiřazeny žádné nedávné hodnoty dat, pravděpodobně spadají do jedné ze dvou kategorií: 1) byly použity dříve a obsahují užitečná / relevantní data, 2) nebyly použity žádným smysluplným způsobem (např. kmen datových hodnot z testování během konfigurace nebo malého pilotního projektu) a data nejsou užitečná / relevantní.

**Závažnost**: Varování

**Doporučení:** Pokud datové prvky obsahují užitečná historická data, měly by být uchovány. Zvažte přejmenování datových prvků a/nebo datových sad, aby bylo jasné, že se již nepoužívají ke sběru dat. Datové prvky, které se aktivně nepoužívají a nemají přidružená žádná cenná data

#### Sekce datové sady s nesprávným pořadím řazení { #data-set-sections-with-incorrect-sort-order }

Sekce datové sady se používají k seskupení určitých souvisejících sekcí ve formuláři pro zadávání dat sekce. Lze je také objednat. Pořadí sekcí se může poškodit, pokud sekce přidáte nebo odstraníte.

**Závažnost**: Varování

**Doporučení:** Je možné opravit pořadí řazení sekcí datové sady pomocí funkce SQL `fixSortOrder`, která je dostupná v úložišti dhis2-utils Github (https://github.com/dhis2/dhis2-utils/tree/master/resources/sql). Pomocí tohoto skriptu můžete opravit pořadí řazení pro každou dotčenou sekci datové sady.

### Obecné { #general }

#### Názvy identifikovatelných objektů, které mají úvodní mezery. { #names-of-identifiable-objects-which-have-leading-spaces }

Identifikovatelné objekty s názvy by neměly obsahovat úvodní mezery.

**Závažnost**: Varování

**Doporučení:** Tyto objekty může být možné opravit prostřednictvím uživatelského rozhraní DHIS2. Případně je lze opravit přímo v databázi pomocí SQL. Následující SQL můžete použít jako vzor, který vám pomůže vytvořit přesný dotaz, který potřebujete:

```
UPDATE chart as a  SET name = b.name_new from ( SELECT chartid,REGEXP_REPLACE(name,'^\s+','') as
name_new from chart where name ~ '^\s+') b where a.chartid = b.chartid;
```

#### Názvy identifikovatelných objektů, které mají na konci mezery. { #names-of-identifiable-objects-which-have-trailing-spaces }

Identifikovatelné objekty s názvy by neměly obsahovat koncové mezery.

**Závažnost**: Varování

**Doporučení:** Tyto objekty může být možné opravit prostřednictvím uživatelského rozhraní DHIS2. Případně je lze opravit přímo v databázi pomocí SQL. Následující SQL můžete použít jako vzor, který vám pomůže vytvořit přesný dotaz, který potřebujete:

```
UPDATE chart as a  SET name = b.name_new from ( SELECT chartid,REGEXP_REPLACE(name,'\s+$','') as name_new from chart where name ~ '\s+$') b where a.chartid = b.chartid;
```

#### Názvy identifikovatelných objektů, které mají více mezer. { #names-of-identifiable-objects-which-have-multiple-spaces }

Identifikovatelné objekty s názvy by neměly obsahovat úvodní mezery.

**Závažnost**: Varování

**Doporučení:** Tyto objekty může být možné opravit prostřednictvím uživatelského rozhraní DHIS2. Případně je lze opravit přímo v databázi pomocí SQL. Následující SQL můžete použít jako vzor, který vám pomůže vytvořit přesný dotaz, který potřebujete:

```
UPDATE categorycombo as a  SET name = b.name_new from ( SELECT categorycomboid,REGEXP_REPLACE(name,'\s{2,}',' ') as
name_new from categorycombo where name ~ '\s{2,}') b where a.categorycomboid = b.categorycomboid;
```

### Indikátory { #indicators }

#### Celkový počet indikátorů. { #total-count-of-indicators }

Přehled počtu indikátorů v systému. **Závažnost**: Informace

**Doporučení:** DHIS2 by měl obsahovat užitečné indikátory pro uživatele.

#### Indikátory nejsou v žádné skupině. { #indicators-not-in-any-groups }

Všechny indikátory by měly být ve skupině indikátorů. To umožňuje uživatelům snadněji najít indikátory v analytických aplikacích a také přispívá k tomu, že mají úplnější sady skupin indikátorů. Operace údržby lze také zefektivnit aplikací hromadných nastavení (např. sdílení, filtrování) na všechny indikátory ve skupině indikátorů.

**Závažnost**: Varování

**Doporučení:** Ukazatele, které nejsou ve skupině ukazatelů, by měly být přidány do příslušné skupiny ukazatelů. Pokud indikátory nejsou potřeba, měly by být vymazány.

#### Indikátory se nepoužívají v analytických objektech NEBO souborech dat. { #indicators-not-used-in-analytical-objects-or-data-sets }

Všechny ukazatele, které jsou vypočítávány, by měly být použity k vytvoření určitého typu výstupu analýzy (grafy, mapy, tabulky), případně k poskytnutí zpětné vazby při zadávání dat tím, že jsou součástí souboru dat.

**Závažnost**: Varování

**Doporučení:** Ukazatele, které nejsou rutinně přezkoumávány v analýze, ať už ve výstupu nebo souboru dat, by měly být přezkoumány, aby se zjistilo, zda je stále třeba počítat. Pokud mají být použity pro rutinní revizi, pak by měly být pomocí nich vytvořeny související výstupy. Pokud tyto indikátory nebudou použity pro žádný typ kontroly informací, je třeba zvážit jejich archivaci nebo vymazání.

#### Indikátory se nepoužívají v analytických objektech. { #indicators-not-used-in-analytical-objects }

Indikátory by měly být použity k vytvoření určitého typu výstupu analýzy (grafy, mapy, tabulky). Poznámka: Indikátory používané v souborech dat k poskytování zpětné vazby při zadávání dat se nepočítají jako indikátory používané v analytických objektech.

**Závažnost**: Varování

**Doporučení:** Ukazatele, které nejsou běžně v analýze přezkoumávány, by měly být přezkoumány, aby se zjistilo, zda jsou užitečné a potřebné. Pokud mají být použity pro rutinní revizi, pak by měly být pomocí nich vytvořeny související výstupy. Pokud tyto indikátory nebudou použity pro žádný typ kontroly informací a nebudou použity v souborech dat pro zpětnou vazbu během zadávání dat, je třeba zvážit jejich odstranění.

### Sady možností { #option-sets }

#### Nepoužité sady možností. { #ununsed-option-sets }

Sady možností by měly být použity pro určitý účel buď s atributy, datovými prvky nebo komentáři.

**Závažnost**: Varování

**Doporučení:** Zvažte smazání nepoužívaných sad možností, případně se ujistěte, že byly správně přiřazeny.

#### Prázdné sady možností { #empty-option-sets }

Všechny sady možností by obecně měly obsahovat alespoň dvě položky. Prázdné sady možností neslouží žádnému účelu.

**Závažnost**: Varování

**Doporučení:** Možnosti by měly být buď přidány do sady možností, nebo by měla být sada možností odstraněna.

#### Sady možností s možná nesprávným pořadím řazení. { #option-sets-with-possibly-wrong-sort-order }

Sady doplňků obsahují doplňky, které lze objednat. Vlastnost sort_order by měla vždy začínat 1 a mít postupnou sekvenci. Pokud jsou v sadě možností tři možnosti, pořadí řazení by mělo být 1,2,3. Za určitých okolností mohou být možnosti ze sady možností odstraněny a pořadí řazení se může poškodit. To může vést k situaci, kdy nebude možné aktualizovat sadu možností z aplikace pro údržbu, a může to vést k problémům při pokusu o použití sady možností v aplikaci pro zadávání dat.

**Závažnost**: Těžká

**Doporučení:** Pokud je možné otevřít sadu možností v aplikaci pro údržbu, můžete použít sadu možností, která by měla problém vyřešit. Dalším možným řešením je přímo aktualizovat vlastnost sort_order v tabulce `optionset` v databázi, čímž se zajistí, že pro všechny volby v sadě voleb bude přítomna platná sekvence.

### Organizační jednotky { #organisation-units }

#### Organizační jednotky, které nejsou ve všech povinných sadách skupin organizačních jednotek{ #orgunits-that-are-not-in-all-compulsory-orgunit-group-sets }

Všechny skupiny organizačních jednotek, které byly označeny jako povinné, by měly obsahovat všechny organizační jednotky v systému. Pokud jsou některé organizační jednotky vynechány ze skupin v sadě skupin, může to způsobit nesrovnalosti v analytických výstupech, například vynechání dat.

**Závažnost**: Těžká

**Doporučení:** Přidejte všechny organizační jednotky přesně do jedné skupiny v rámci povinné skupiny organizačních jednotek.

#### Organizační jednotky, které mají datum otevření pozdější než datum uzavření. { #organisation-units-which-have-an-opening-date-later-than-the-closed-date }

Pokud bylo pro organizační jednotku definováno datum uzavření, mělo by být vždy po datu otevření (pokud bylo definováno).

**Závažnost**: Těžká

**Doporučení:** Změňte datum otevření nebo uzavření všech dotčených organizačních jednotek tak, aby datum uzavření bylo po datu otevření.

#### Organizační jednotky by neměly mít na konci mezery. { #organisation-units-should-not-have-trailing-spaces }

Koncové prostory v organizačních jednotkách jsou nadbytečné.

**Závažnost**: Varování

**Doporučení:** Pokud je počet dotčených organizačních jednotek malý, je nejjednodušší nápravou je opravit přímo z uživatelského rozhraní. Další možnou možností by bylo nahrazení všech více mezer pomocí SQL.

#### Organizační jednotky se souřadnicemi bodů by měly obsahovat jejich nadřazené jednotky. { #organisation-units-with-point-coordinates-should-be-contained-by-their-parent }

Zařízení jsou často reprezentována jako body v hierarchii DHIS2. Geometrie jejich nadřazených organizačních jednotek by měla obsahovat všechna zařízení, která s nimi byla spojena.

**Závažnost**: Varování

**Doporučení:** Hraniční soubory jsou při nahrávání do DHIS2 často zjednodušeny. Tento proces může vést k tomu, že zařízení, která se nacházejí v blízkosti hranice daného okresu, budou mimo okres, když se hranice zjednoduší. To je považováno spíše za kosmetický problém pro většinu instalací DHIS2, ale může se stát problémem, pokud se pokusíte o geoprostorovou analýzu pomocí hranic a souřadnic bodů.

V případech, kdy zařízení spadá mimo hranice svého rodiče, měli byste potvrdit, že souřadnice jsou správné. Pokud je umístění blízko hranice, možná budete chtít znovu zvážit, jak byly soubory hranic zjednodušeny. V opačném případě, pokud je umístění zařízení zcela nesprávné, mělo by být opraveno.

#### Organizační jednotky umístěné do 100 km od Null Island (0,0). { #organisation-units-located-within-100-km-of-null-island-00 }

Častým problémem při importu souřadnic je zahrnutí souřadnic umístěných kolem bodu [Nulového ostrova](https://en.wikipedia.org/wiki/Null_Island). Toto je bod na zemském povrchu, kde se nultý poledník a rovník protínají se zeměpisnou šířkou 0 a nulovou délkou. Bod se také nachází v současné době uprostřed oceánu. Tento dotaz identifikuje všechny body umístěné do 100 km od bodu, jejichž zeměpisná šířka a délka se rovna nule.

**Závažnost**: Těžká

**Doporučení:** Aktualizujte souřadnice dotčené organizační jednotky na správné místo.

#### Organizační jednotky by neměly mít ve svých názvech více mezer. { #organisation-units-should-not-have-multiple-spaces-in-their-names }

Názvy organizačních jednotek by neměly obsahovat více mezer. Jsou nadbytečné a mohou zkomplikovat umístění organizačních jednotek při jejich prohledávání.

**Závažnost**: Varování

**Doporučení:** Pokud je počet dotčených organizačních jednotek malý, je nejjednodušší nápravou je opravit přímo z uživatelského rozhraní. Další možnou možností by bylo nahrazení všech více mezer pomocí SQL.

#### Organizační jednotky s neplatnou geometrií. { #organisation-units-with-invalid-geometry }

DHIS2 využívá rozšíření databáze PostGIS pro správu geografických informací spojených s organizačními jednotkami. Existují různé důvody, proč mohou být geometrie považovány za neplatné, včetně samozačlenění, průniků a mnohoúhelníků. Podrobnější diskusi na toto téma naleznete v dokumentaci PostGIS.

**Závažnost**: Kritická

**Doporučení:** Aktualizujte geometrii dotčených organizačních jednotek na platnou geometrii. K automatickému vyřešení problému může být možné použít funkci PostGIS `ST_MakeValid`. V jiných případech však může být nutné geometrii upravit v nástroji GIS a poté znovu aktualizovat v DHIS2.

#### Hierarchie organizační jednotky by měla mít jeden kořen. { #the-organisation-unit-hierarchy-should-have-a-single-root }

Každý systém DHIS2 by měl mít jednu kořenovou organizační jednotku. To znamená jednu organizační jednotku, z níž jsou potomky všechny ostatní větve hierarchie.

**Závažnost**: Kritická

**Doporučení:** Jakmile se rozhodnete, která organizační jednotka by měla být skutečným kořenem hierarchie organizačních jednotek, měli byste aktualizovat nadřazenou organizační jednotku. To lze provést pomocí DHIS2 API nebo mou aktualizací hodnoty přímo v tabulce `organisationunit`.

#### Organizační jednotky bez souřadnic. { #organisation-units-with-no-coordinates }

V ideálním případě by všechny organizační jednotky obsažené v hierarchii DHIS2 měly mít platnou sadu souřadnic. Obvykle pro všechny organizační jednotky nad úrovní zařízení by tyto souřadnice měly být polygon, který tvoří hranici organizační jednotky. U zařízení jsou tyto obvykle reprezentovány jako souřadnice bodu.

Z tohoto pravidla samozřejmě mohou existovat výjimky. Mobilní zdravotnická zařízení nemusí mít pevné místo. Komunitní zdravotničtí pracovníci nebo oddělení pod úrovní zařízení také nemusí mít definované nebo definovatelné souřadnice.

Účelem této kontroly je umožnit vám zkontrolovat všechny organizační jednotky, které nemají žádné souřadnice, a rozhodnout, zda by měly být aktualizovány.

**Závažnost**: Varování

**Doporučení:** V případě potřeby aktualizujte geometrii každé organizační jednotky platnou geometrií. Možná budete muset kontaktovat příslušný úřad místní správy, abyste získali kopii hranic okresů, běžně označovaných jako „soubory tvaru“. Další možností je použít volně dostupné hraniční soubory z GADM (https://gadm.org)

Pokud v zařízení chybí souřadnice, je možné je získat od zaměstnanců zařízení pomocí jejich chytrého telefonu, aby je získali. Obrázky z Map Google lze také často použít k odhadu polohy zařízení za předpokladu, že máte dostatečně dobré rozlišení a místní znalosti o tom, kde se nachází.

#### Osiřelé organizační jednotky. { #orphaned-organisation-units }

Osiřelé organizační jednotky jsou takové, které nemají rodiče ani žádné děti. To znamená, že nemají žádný vztah k hierarchii hlavní organizační jednotky. Ty mohou být vytvořeny chybným importem metadat nebo přímou manipulací s databází.

**Závažnost**: Kritická

**Doporučení:** Osiřelé organizační jednotky by měly být přiřazeny nadřazené nebo odstraněny ze systému. Pokud je to možné, doporučuje se pro tento úkol použít DHIS2 API. Pokud to není možné, může být nutné je odstranit pomocí přímého SQL v databázi DHIS2.

#### Organizační jednotky, které patří do více skupin v sadě skupin. { #organisation-units-which-belong-to-multiple-groups-in-a-group-set }

Organizační jednotky by měly patřit přesně do jedné skupiny v rámci každé sady skupin organizačních jednotek, jejímž jsou členem. Pokud organizační jednotka patří do více skupin, povede to v analýze k nepředvídatelným výsledkům.

**Závažnost**: Těžká

**Doporučení:** Pomocí aplikace pro údržbu přiřaďte organizační jednotky v seznamu podrobností přesně jedné skupině v rámci členství v každé sadě skupin.

### Období { #periods }

#### Období se stejným datem začátku a konce { #periods-with-the-same-start-and-end-dates }

Různá období by neměla mít přesně stejné datum začátku a konce.

**Závažnost**: Kritická

**Doporučení:** Všechny odkazy na duplicitní období by měly být ze systému odstraněny a přiřazeny znovu. Doporučuje se použít období se spodní periodou.

#### Období, která jsou více než tři roky v budoucnosti. { #periods-which-are-more-than-three-years-in-the-future }

Období v DHIS2 jsou automaticky generovány systémem. Při zadávání nových údajů do systému se automaticky vytvářejí nová období. V některých případech mohou být při odesílání dat do DHIS2 omylem vytvořena období pro období, která jsou ve vzdálené budoucnosti. Různí klienti pro zadávání dat nemusí řádně ověřovat období, která jsou v budoucnosti, a proto by měla být všechna budoucí období přezkoumána. V některých případech mohou být data platná pro budoucí data, např. cíle, které jsou stanoveny pro příští fiskální rok.

**Závažnost**: Varování

**Doporučení:** Pokud budou v systému v budoucnu existovat nějaká období, měli byste zkontrolovat nezpracovaná data buď přímo v tabulce hodnot dat, nebo alternativně prostřednictvím kontingenčních tabulek, abyste se ujistili, že jsou tato data správná.

V mnoha případech mohou klienti uvažovat o předání dat za leden 2021, ale kvůli chybám při zadávání dat je vybrán leden 2031. Jakákoli data v daleké budoucnosti by tedy měla být prošetřena, aby se zajistilo, že nepocházejí z chyb při zadávání dat.

#### Období, která jsou v dávné minulosti. { #periods-which-are-in-the-distant-past }

Období v DHIS2 jsou automaticky generovány systémem. Při zadávání nových údajů do systému se automaticky vytvářejí nová období. V některých případech mohou být při odesílání dat do DHIS2 omylem vytvořena období pro období, která jsou ve vzdálené minulosti. Různí klienti pro zadávání dat nemusí řádně ověřovat období, která jsou ve vzdálené minulosti, a proto by tato období měla být tříděna, aby se zajistilo, že data proti nim nebyla vložena omylem.

**Závažnost**: Varování

**Doporučení:** Pokud v systému existují nějaká období v dávné minulosti, měli byste zkontrolovat nezpracovaná data buď přímo v tabulce datavalue, nebo alternativně prostřednictvím kontingenčních tabulek, abyste se ujistili, že jsou tato data správná.

V mnoha případech mohou klienti uvažovat o předání dat za leden 2021, ale kvůli chybám při zadávání dat je vybrán leden 2031. Jakákoli data v daleké budoucnosti by tedy měla být prošetřena, aby se zajistilo, že nepocházejí z chyb při zadávání dat.

### Pravidla programu { #program-rules }

#### Pravidla programu bez akce. { #program-rules-with-no-action }

Všechna pravidla programu by měla mít akci.

**Závažnost**: Těžká

**Doporučení:** Pomocí uživatelského rozhraní DHIS2 přiřaďte akci každému pravidlu programu, kterému jedno chybí. Případně, pokud se programové pravidlo nepoužívá, zvažte jeho odstranění.

#### Pravidla programu bez priority. { #program-rules-with-no-priority }

Všem pravidlům programu by měla být přiřazena priorita.

**Závažnost**: Těžká

**Doporučení:** Pomocí uživatelského rozhraní DHIS2 přiřaďte prioritu každému pravidlu programu, kterému jedno chybí.

#### Program pravidel akcí, které by měly odeslat nebo naplánovat zprávu bez šablony zprávy. { #program-rules-actions-which-should-send-or-schedule-a-message-without-a-message-template }

Akce programových pravidel typu „Odeslat zprávu“ nebo „Naplánovat zprávu“ by měly mít přidruženou šablonu zprávy.

**Závažnost**: Těžká

**Doporučení:** Pomocí uživatelského rozhraní DHIS2 přiřaďte šablonu zprávy každé z akcí programových pravidel, které odesílají nebo plánují zprávy, ale nemají přidružení k šabloně zprávy.

### Uživatelé { #users }

#### Počet uživatelů v systému { #number-of-users-in-the-system }

Celkový počet uživatelů v systému.

**Závažnost**: Informace

**Doporučení:** Pouze informace.

#### Uživatelé, kteří se během posledních 30 dnů nepřihlásili { #users-who-have-not-logged-in-during-the-past-30-days }

Všichni uživatelé by se měli pravidelně přihlašovat, ať už za účelem zadávání dat nebo prohlížení analýz. Tato metrika měří počet uživatelů, kteří jsou povoleni, ale během posledních 30 dnů se nepřihlásili.

**Závažnost**: Varování

**Doporučení:** Zkontrolujte, zda by tito uživatelé měli být aktivní, jinak zvažte deaktivaci účtů.

#### Uživatelé, kteří se za poslední rok nepřihlásili, { #users-who-have-not-logged-in-over-the-past-year }

Aktivní uživatelské účty by měli mít pouze uživatelé, kteří běžně přistupují do systému. Uživatelé, kteří se v posledním roce nepřihlásili, nemusí používat nebo potřebovat přístup do systému, mohli opustit svou pozici a měli by, nebo může být účet výsledkem výzvy k registraci účtu, který nebyl použit.

**Závažnost**: Varování

**Doporučení:** Uživatelské účty, které nejsou spojeny se skutečnými, aktivními uživateli, by měly být minimálně deaktivovány, případně smazány.

### Pravidla ověřování { #validation-rules }

#### Všechny výrazy ověřovacích pravidel by měly mít chybějící strategii hodnot. { #all-validation-rule-expressions-should-have-a-missing-value-strategy }

Ověřovací pravidla se skládají z výrazu na levé a pravé straně. V některých systémech nemusí být strategie chybějící hodnoty definována. To může vést k výjimce během analýzy ověřovacích pravidel. Dotčená ověřovací pravidla by měla být opravena vhodnou strategií chybějících hodnot.

**Závažnost**: Těžká

**Doporučení:** Pomocí výsledků zobrazení podrobností SQL identifikujte dotčená ověřovací pravidla a na které straně pravidla nebyla specifikována strategie chybějících hodnot. Pomocí aplikace pro údržbu proveďte příslušné opravy a uložte pravidlo.
