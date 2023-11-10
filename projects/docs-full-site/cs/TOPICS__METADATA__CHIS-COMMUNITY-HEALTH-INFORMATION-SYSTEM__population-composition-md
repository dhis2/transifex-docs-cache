---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/ch_pop_aggregate_design.md"
revision_date: "2021-10-19"
---

# CH - Složení populace { #ch-pop-aggregate-design }

## 1. Datové sady { #1-datasets }

### 1.1. Souhrn konfigurace { #11-configuration-summary }

Souhrnný modul CH - Složení populace (POP) obsahuje:

1. **roční soubor dat** pro sledování klíčových datových prvků POP
2. **Základní indikátory POP**
3. Předdefinovaný ovládací panel **„CH – Složení populace“**

Doporučuje se, aby byly datové sady přiřazeny k organizačním jednotkám **na nejnižší úrovni** zdravotnického systému, které je možné pro hlášení dat, jako jsou vesnice nebo jakékoli vhodné vymezení komunity podle místního kontextu.

### 1.2. Datové prvky { #12-data-elements }

Níže uvedená tabulka shrnuje datové prvky přítomné v modulu AH. Sloupce „Skupiny datových prvků“ a „Soubory dat“ poskytují další informace o tom, kde lze v ostatních modulech CHIS nalézt stejné DE. To by mělo usnadnit mapování balíčku mezi všemi jeho moduly a navigaci v souborech dat a zároveň se vyhnout shromažďování a zadávání dat stejných DE na více místech. Vzhledem k tomu, že RP populace jsou velmi spjaty s činnostmi, které jsou prováděny, měly by být RV upraveny nebo by měly být přidány nové, aby lépe odrážely činnosti. Vezměte prosím na vědomí, že někteří jmenovatelé populace se nacházejí i v jiných modulech (např. ženy a dívky zkoumané v rámci návštěv domácností, screenované děti <5y, People (> 18m) ve spádové oblasti) a je na uživateli, aby se rozhodl, zda si je chce ponechat ve aktuální modul, nebo chtějí-li je přesunout do modulu POP.

Všechny DE v modulu POP se používají při sestavování indikátorů.

| Název | Popis | Datové sady | DE skupiny |
| --- | --- | --- | --- |
| CH002a - Živě narozená v komunitě | Živě narozené děti v komunitě | CH - Občanská evidence a životní statistika (ročně), CH - Složení populace (ročně) | CH - Složení populace, CH - Zdraví novorozenců, CH - Civilní registrace a vitální statistika |
| CH002b – Živě narození v komunitě (podle věku matky) | Živě narozené děti v komunitě podle věku matky | CH - Občanská evidence a životní statistika (ročně), CH - Složení populace (ročně) | CH - Občanská evidence a vitální statistika, CH - Složení populace |
| CH001a - Domácnosti ve spádové oblasti | Domácnosti ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Čistá energie, CH - Ochrana dětí a mezilidské násilí, CH - Voda, sanitace a hygiena (WASH), CH - Nepřenosné nemoci |
| CH001b – Domácnosti s dětmi (0-4 roky) | Domácnosti ve spádové oblasti s dětmi ve věku 0-4 let | CH – Složení populace (roční) | CH - Složení populace |
| CH003 - Kojenci (0-11 m) ve spádové oblasti | Kojenci ve věku 0-11 měsíců | CH – Složení populace (roční) | CH - Složení populace, CH - Imunizace, CH - Nepřenosné nemoci, CH - Zdraví dítěte, CH - Duševní zdraví |
| CH004 - Děti (1-4 roky) ve spádové oblasti | Děti ve věku 1-4 let ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Imunizace, CH - Nepřenosné nemoci, CH - Zdraví dítěte, CH - Duševní zdraví |
| CH005 - Děti (5-9 let) ve spádové oblasti | Děti ve věku 5-9 let ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Nepřenosné nemoci, CH - Zdraví dítěte |
| CH006 - Mladí dorostenci (10-14 let) ve spádové oblasti | Mladí dorostenci ve věku 10-14 let ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Zdraví dospívajících, CH - Nepřenosné nemoci |
| CH007 - Starší dorost (15-19 let) ve spádové oblasti | Starší dorost ve věku 15-19 let ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Nepřenosné nemoci, CH - Duševní zdraví |
| CH008 - Těhotné ženy ve spádové oblasti | Těhotné ženy ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace |
| CH009 - Dospělí 20+ let ve spádové oblasti | Dospělí ve věku 20+ let ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Nepřenosné nemoci, CH - Duševní zdraví |

V níže uvedené tabulce je několik příkladů DE, které nejsou v modulu POP, ale přesto by mohly být považovány za jmenovatele populace. Jak již bylo zmíněno, je na uživateli, aby upravil moduly tak, aby lépe reprezentovaly místní kontext/aktivity a usnadnily sběr dat o obyvatelstvu.

| Název | Popis | Skupiny datových prvků | Datové sady |  |
| :-: | :-: | :-: | :-: | --- |
| CH101b - Těhotné ženy LWHA při porodu | Těhotné ženy žijící s HIV a porodily v posledních 12 měsících ve spádové oblasti | CH - HIV | CH – HIV (měsíčně) |  |
| CH106b - Lidé se známým HIV statusem ve spádové oblasti | PLWHA, kteří znají svůj HIV status ve spádové oblasti | CH - HIV | CH – HIV (měsíčně) |  |
| CH106d - Klíčová populace se známým HIV statusem ve spádové oblasti | PLWHA, kteří znají svůj HIV status ve spádové oblasti, kteří jsou klíčovou populací | CH - HIV | CH – HIV (měsíčně) |  |
| CH109b - Osoby způsobilé pro ekonomickou podporu ve spádové oblasti | Osoby způsobilé ve spádové oblasti pro ekonomickou (obživu) podporu | CH - Služby zaměřené na člověka, CH - HIV, TBC - Tuberkulóza | CH – HIV (měsíčně), CH – služby zaměřené na lidi (měsíčně), CH – tuberkulóza (měsíčně) |  |
| CH109d - Osoby způsobilé pro ekonomickou podporu ve spádové oblasti | Osoby způsobilé ve spádové oblasti pro ekonomickou (obživu) podporu podle stavu | CH - Služby zaměřené na člověka, CH - HIV, TBC - Tuberkulóza | CH – HIV (měsíčně), CH – služby zaměřené na lidi (měsíčně), CH – tuberkulóza (měsíčně) |  |
| CH111d - Osoby oprávněné k právním službám ve spádové oblasti | Oprávněné osoby ve spádové oblasti pro právní služby podle podmínky | CH - Služby zaměřené na člověka, CH - HIV, TBC - Tuberkulóza | CH – HIV (měsíčně), CH – služby zaměřené na lidi (měsíčně), CH – tuberkulóza (měsíčně) |  |
| CH146 - Lidé prověření na VL a/nebo PKDL | Lidé vyšetřováni na známky a příznaky VL a/nebo PKDL ve spádové oblasti | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |
| CH168c – Asymptomatičtí diabetici dospělí (40+ let) s BMI >= 25 ve spádové oblasti | Asymptomatičtí dospělí ve věku 40+ let s BMI ≥ 25 ve spádové oblasti | CH - Nepřenosné nemoci | CH - Nepřenosné nemoci (roční) |  |
| CH060b -Lidé cílení na odčervovací preventivní chemoterapii | Lidé cílení na preventivní chemoterapii na odčervení | CH - Výživa, CH - Zdraví dospívajících, CH - Zdraví dětí | CH – Zdraví dospívajících (měsíčně), CH – zdraví dětí (měsíčně), CH – Výživa (měsíčně) |  |
| CH141e – Domácnosti zaměřené na zprávy na NTD – správa případů | Domácnosti zaměřené na kampaně sociální mobilizace na NTD – case management | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |
| CH141f – Domácnosti zaměřené na zprávy na NTD – OneHealth | Domácnosti zaměřené na kampaně sociální mobilizace týkající se NTD – jeden přístup ke zdraví | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |
| CH141g - Domácnosti zaměřené na zprávy na NTD - PC | Domácnosti zaměřené na kampaně sociální mobilizace na NTD - PC | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |
| CH141h – Domácnosti zaměřené na zprávy na NTD – VC | Domácnosti zaměřené na kampaně sociální mobilizace na NTD – vektorová kontrola | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |
| CH150b - Domy určené pro měření vektorové redukce | Domy, na které se vztahují opatření ke snížení domácího vektoru | CH - Zanedbané tropické choroby | CH - Zanedbané tropické nemoci (ročně) |  |

## 2. Podrobnosti datové sady { #2-dataset-details }

### 2.1. Roční datová sada POP { #21yearly-pop-dataset }

#### 2.1.1. Domácnosti { #211-households }

Sekce uvádí informace o domácnostech ve spádové oblasti konkrétní komunity.

![Domácnosti](resources/images/chis-pop-001.png)

#### 2.1.2. Živě narození { #212-live-births }

Sekce uvádí živě narozené děti registrované v komunitě podle pohlaví novorozence (muž, žena, otehr, pohlaví neznámé) a podle věku matky (10-14 let, 15-19 let, 20+ let, věk neznámý).

![Živé narození](resources/images/chis-pop-002.png)

#### 2.1.3. Lidé ve spádové oblasti { #213-people-in-catchment-area }

Sekce informuje o těhotných ženách podle věku (10-14 let, 15-19 let, 20+ let, neznámý věk), o počtu dospělých nad 20 let podle věkových skupin (20-29 let, 30-39 let, 40-49 let, 50-59 let, 60-69 let, 70-79 let, 80+r, věk neznámý) a podle pohlaví (muž, žena, jiné, neznámé pohlaví). A konečně sekce uvádí také údaje o dětech a mladistvých v oblasti podle pohlaví (muž, žena, jiné, neznámé pohlaví).

![Lidé ve spádové oblasti](resources/images/chis-pop-003.png)

## 3. Pravidla ověření { #3-validation-rules }

Pro datovou sadu POP byla nastavena následující pravidla ověření:

| Název | Návod | Operátor | Levá strana | Pravá strana |
| :-: | :-: | :-: | :-: | :-: |
| CH - Živě narozené děti podle věku matky vs. Živě narozené děti v komunitě | Živě narozené děti podle věku matky by měly být menší nebo stejné jako živě narozené děti v komunitě | less_than_or_equal_to | Živě narozené děti podle věku matky | Živě narozené děti v komunitě |
| CH - HHs s dětmi ve věku < 5 let vs. domácnosti ve spádové oblasti | HH s dětmi ve věku < 5 let by měly být menší nebo stejné jako domácnosti ve spádové oblasti | less_than_or_equal_to | HHs s dětmi ve věku < 5 let | Domácnosti ve spádové oblasti |

## 4. Analytika a indikátory { #4-analytics-and-indicators }

Stejně jako u DE je v tabulce pod sloupcem „Skupiny indikátorů“ informace o tom, zda se indikátor nachází v jiných skupinách, než je skupina indikátorů POP.

| Název | Popis | Čitatel | Jmenovatel | Skupiny indikátorů |
| --- | --- | --- | --- | --- |
| CH001 - Domácnosti ve spádové oblasti | Počet domácností ve spádové oblasti | Domácnosti ve spádové oblasti | 1 | CH - Složení populace |
| CH002 - Živě narozená v komunitě | Počet živě narozených dětí | Živě narozené děti v komunitě | 1 | CH - Složení populace, CH - Civilní evidence a vitální statistika |
| CH003 - Kojenci ve věku 0-11 měsíců ve spádové oblasti | Počet kojenců ve spádové oblasti (0 až méně než 1 rok) | Kojenci ve věku 0-11 měsíců ve spádové oblasti | 1 | CH - Imunizace, CH - Složení populace |
| CH004 - Děti ve věku 1-4 let ve spádové oblasti | Počet dětí ve spádové oblasti (1 až méně než 5 let) | Děti ve věku 1-4 let ve spádové oblasti | 1 | CH - Imunizace, CH - Složení populace |
| CH005 - Děti ve věku 5-9 let ve spádové oblasti | Počet dětí ve spádové oblasti (5 až méně než 10 let) | Děti ve věku 5-9 let ve spádové oblasti | 1 | CH - Složení populace |
| CH006 - Mladí adolescenti ve věku 10-14 let ve spádové oblasti | Počet mladých dospívajících ve spádové oblasti (10-14 let) | Mladí adolescenti ve věku 10-14 let | 1 | CH - Složení populace |
| CH007 - Starší dorost ve věku 15-19 let ve spádové oblasti | Počet starších dorostenců ve spádové oblasti (15-19 let) | Starší dorost ve věku 15-19 let | 1 | CH - Složení populace |
| CH008 - Těhotné ženy ve spádové oblasti | Počet těhotných žen ve spádové oblasti | Těhotné ženy ve spádové oblasti | 1 | CH - Složení populace |
| CH009 - Dospělí ve věku 20+ let ve spádové oblasti | Počet dospělých ve spádové oblasti | Dospělí ve věku 20+ let ve spádové oblasti | 1 | CH - Složení populace |
| CH009b - Celková populace v povodí | Celkový počet obyvatel v povodí | Dospělí ve věku 20+ let ve spádové oblasti | 1 | CH - Složení populace |

## 5. Ovládací panel { #5-dashboard }

Modul obsahuje předdefinovaný dashboard nazvaný „CH - Složení populace“. První část Předdefinované položky na dashboardu obsahují data podle sekcí přítomných v datové sadě, ale obsah by měl být přizpůsoben na základě místních aktivit.

![Ovládací panel](resources/images/chis-pop-db-001.png)
