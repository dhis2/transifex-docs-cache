---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/ch_epi_aggregate_design.md"
revision_date: "2021-10-19"
---

# CH - Imunizace { #ch-epi-aggregate-design }

## 1. Datové sady { #1-datasets }

### 1.1. Souhrn konfigurace { #11-configuration-summary }

Souhrnný modul CH - imunizace obsahuje:

1. **měsíční soubor dat** s klíčovými datovými prvky pro imunizaci
2. **roční soubor dat** pro sledování klíčových ročních informací o aktivitách v oblasti imunizace
3. **Základní indikátory** pro oba soubory dat
4. Předdefinovaný ovládací panel **CH - Immunizace**

Doporučuje se, aby byly datové sady přiřazeny k organizačním jednotkám **na nejnižší úrovni** zdravotnického systému, které je možné pro hlášení dat, jako jsou vesnice nebo jakékoli vhodné vymezení komunity podle místního kontextu.

## 1.2. Datové prvky { #12-data-elements }

Níže uvedená tabulka shrnuje datové prvky přítomné v modulu imunizace. Sloupce „Skupiny datových prvků“ a „Soubory dat“ poskytují další informace o tom, kde lze v ostatních modulech CHIS nalézt stejné DE. To by mělo usnadnit mapování balíčku mezi všemi jeho moduly a navigaci v souborech dat a zároveň se vyhnout shromažďování a zadávání dat stejných DE na více místech.

Všechny DE v modulu Imunizace se používají při sestavování indikátorů.

| Název | Popis | Datové sady | DE skupiny |
| --- | --- | --- | --- |
| CH095a - Lidé, kteří nemají aktuální informace o doporučeném očkování | Osoby, které nemají aktuální informace o očkování a doporučené | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH095b - Lidé zkontrolovaní na očkování | Lidé zkontrolovaní na očkování kvůli dokončení očkování | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH095c - Ženy, které nemají aktuální informace o doporučeném očkování | Ženy, které nemají aktuální informace o očkování | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH095d - Těhotné ženy kontrolované na očkování | Těhotné ženy zkontrolované na dokončené očkování | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH096a - Doporučené neočkované děti (0-4 roky). | Děti 0-4 roky, jejichž rodiče uvedli, že nikdy nebyli očkováni, a které jsou doporučeny | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH096b - Děti (0-4 roky) zkontrolované na očkování | Děti (0-4 roky) zkontrolovány na dokončení očkování | CH – ICCM (měsíční), CH – imunizace (roční) | CH - Imunizace, CH - ICCM |
| CH100a - Děti (0-23 m) s očkováním proti obrně | Způsobilé děti 0-23 měsíců, které dostaly rutinní požadované dávky vakcíny proti obrně podle národního plánu | CH – ICCM (měsíčně), CH – imunizace (měsíčně) | CH - Imunizace, CH - ICCM |
| CH100b - Děti (0-23 m) způsobilé pro OPV v cílové populaci | Děti (0-23 m) způsobilé pro OPV v cílové populaci | CH – ICCM (měsíčně), CH – imunizace (měsíčně) | CH - Imunizace, CH - ICCM |
| CH097a - Novorozenci se známkami a příznaky tetanu | Novorozenci se známkami a příznaky tetanu | CH – Imunizace (měsíční) | CH - Imunizace |
| CH097b - Novorozenci s potvrzenými známkami a příznaky tetanu | Novorozenci s potvrzenými známkami a příznaky tetanu | CH – Imunizace (měsíční) | CH - Imunizace |
| CH098a - Děti (0-14 let) podezřelé z AFP | Děti < 15 let s podezřením na akutní obrnu | CH – Imunizace (měsíční) | CH - Imunizace |
| CH098b - Děti (0-14 let) podezřelé z AFP | Doporučeno dětem < 15 let s podezřením na akutní obrnu | CH – Imunizace (měsíční) | CH - Imunizace |
| CH099a - Lidé se známkami a příznaky spalniček nebo zarděnek | Lidé se známkami a příznaky spalniček nebo spalniček zarděnek | CH – Imunizace (měsíční) | CH - Imunizace |
| CH099b - Lidé se známkami spalniček nebo zarděnek | Odkazovali lidé se známkami spalniček nebo zarděnek | CH – Imunizace (měsíční) | CH - Imunizace |

## 2. Podrobnosti datové sady { #2-dataset-details }

### 2.1. Měsíční datový soubor imunizace { #21-monthly-immunization-dataset }

#### 2.1.1. Novorozenecký tetanus { #211-neonatal-tetanus }

Sekce je nastavena tak, aby shromažďovala základní informace o novorozencích vykazujících příznaky nebezpečí novorozeneckého tetanu podle výsledku (mrtvých nebo živých).

![Novorozenecký tetanus](resources/images/chis-epi-m-001.png)

#### 2.1.2. Spalničky a zarděnky { #212-measles-and-rubella }

Sekce je zaměřena na sběr základních informací o dětech < 15 let s nebezpečnými příznaky spalniček a/nebo zarděnek podle věkových skupin (0-4 roky. 5-9 let, 10-14 let, věk neznámý).

![Spalničky a zarděnky](resources/images/chis-epi-m-002.png)

#### 2.1.3. Akutní obrna { #213-acute-flaccid-paralysis }

Sekce shromažďuje údaje o známkách akutní obrny u dětí do 15 let podle věkových skupin (0-4 roky. 5-9 let, 10-14 let, neznámý věk).

![Akutní obrna](resources/images/chis-epi-m-003.png)

#### 2.1.4. OPV { #214-opv }

Sekce shromažďuje údaje o typu vakcíny proti dětské obrně a dávkách podaných způsobilým dětem do 2 let podle typu OPV a dávky (0 až 4).

![OPV](resources/images/chis-epi-m-004.png)

### 2.2. Roční datový soubor imunizace { #22yearly-immunization-dataset }

#### 2.2.1. Neúplný plán imunizace { #221-incomplete-immunization-schedule }

Sekce shromažďuje údaje o dětech do 5 let (0-11m, 1-4 roky), lidech nad 5 let a těhotných ženách, jejichž očkovací kalendář není aktuální podle jejich národní směrnice.

![OPV](resources/images/chis-epi-y-001.png)

## 3. Pravidla ověření { #3-validation-rules }

Pro datové sady imunizace nejsou nastavena žádná ověřovací pravidla.

## 4. Analytika a indikátory { #4-analytics-and-indicators }

Stejně jako u DE jsou v tabulce pod sloupcem „Skupiny indikátorů“ uvedeny informace o tom, zda se indikátor nachází v jiných skupinách, než je skupina indikátorů imunizace.

| Název | Popis | Čitatel | Jmenovatel | Skupiny indikátorů |
| --- | --- | --- | --- | --- |
| CH003 - Kojenci ve věku 0-11 měsíců ve spádové oblasti | Počet kojenců ve spádové oblasti (0 až méně než 1 rok) | Kojenci ve věku 0-11 měsíců ve spádové oblasti | 1 | CH - Imunizace, CH - Složení populace |
| CH004 - Děti ve věku 1-4 let ve spádové oblasti | Počet dětí ve spádové oblasti (1 až méně než 5 let) | Děti ve věku 1-4 let ve spádové oblasti | 1 | CH - Imunizace, CH - Složení populace |
| CH095 – Doporučení lidé, kteří nemají aktuální očkování (%) | Podíl osob, které nemají aktuální očkování a jsou doporučeny | Není aktuální s očkováním a doporučeno | Osoby, které byly zkontrolovány | CH - Imunizace, CH - ICCM |
| CH096b - Děti (0-4 roky) neočkované | Počet dětí (0-4 roky), jejichž rodiče uvedli, že nikdy nebyly očkovány | Děti (0-4 roky) nikdy neočkované | 1 | CH - Imunizace |
| CH096 – Děti (0-4 roky) neočkované doporučené (%) | Podíl dětí ve věku 0-4 let, jejichž rodiče uvedli, že nebyly nikdy očkovány, a které jsou doporučeny | Děti (0-4 roky) nikdy neočkované a doporučené | Děti (0-4 roky), u kterých byla provedena kontrola očkování | CH - Imunizace, CH - ICCM |
| CH097 - Novorozenci se známkami a příznaky tetanu | Detekce a hlášení novorozeneckého tetanu | Novorozenci se známkami a příznaky tetanu | 1 | CH - Imunizace |
| CH098 - Děti (0-14 let) podezřelé z AFP | Detekce a hlášení akutní ochablé paralýzy u dětí (0-4 let) | Děti (0-14 let) se známkami AFP | 1 | CH - Imunizace |
| CH099 - Lidé se známkami a příznaky spalniček / zarděnek | Detekce a hlášení vyrážky a horečky u spalniček nebo spalniček / zarděnek | Osoby se známkami spalniček nebo spalniček zarděnek | 1 | CH - Imunizace |
| CH100b – Děti (0-23 let) způsobilé pro vakcínu proti obrně | Počet způsobilých dětí 0-23 let pro vakcínu proti obrně podle národního plánu | Děti 0-23 m | 1 | CH - Imunizace |
| CH100 – Děti (0-59 m) očkované proti dětské obrně (%) | Podíl způsobilých dětí (0-59 m), které dostaly běžné požadované dávky vakcíny proti obrně podle národního plánu | Děti (0-59 m), kterým byly podávány běžné dávky dětské obrny | Děti (0-59 m) v cílové populaci | CH - Imunizace, CH - ICCM |

## 6. Ovládací panely { #6-dashboards }

Modul obsahuje předdefinovaný dashboard nazvaný „CH - Immunization“.

Řídicí panel je rozdělen na dvě části na základě periodicity datových sad.

První část je pro měsíční ukazatele. Předdefinované položky analyzují a vizualizují hlavní oblasti datové sady, i když ovládací panel by měl být upraven tak, aby lépe odrážel místní aktivity.

![Ovládací panely](resources/images/chis-epi-db-001.png)

Druhá část dashboardu je věnována ročnímu souboru dat (Annual Household Assessment Indicators). Předdefinované položky analyzují a vizualizují hlavní oblasti datové sady, i když ovládací panel by měl být upraven tak, aby lépe odrážel místní aktivity.

![Ovládací panely](resources/images/chis-epi-db-002.png)
