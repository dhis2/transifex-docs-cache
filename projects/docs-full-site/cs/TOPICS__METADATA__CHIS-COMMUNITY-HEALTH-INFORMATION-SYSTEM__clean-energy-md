---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/ch_ene_aggregate_design.md"
revision_date: "2021-10-19"
---

# CH - Čistá energie { #ch-ene-aggregate-design }

## 1. Datové sady { #1-datasets }

### 1.1. Souhrn konfigurace { #11-configuration-summary }

Modul agregátu CH - Clean energy (CE) obsahuje:

1. Roční soubor údajů pro sledování klíčových ročních informací o čisté energii
2. Základní indikátory pro datovou sadu
3. Předdefinovaný přístrojový panel „CH - Clean energy“.

Doporučuje se, aby byly datové sady přiřazeny organizačním jednotkám na nejnižší úrovni zdravotnického systému, která je možná pro hlášení dat, jako jsou vesnice nebo jakékoli vhodné vymezení komunity podle místního kontextu.

### 1.2. Datové prvky { #12-data-elements }

Níže uvedená tabulka shrnuje datové prvky obsažené v modulu CE. Sloupce „Skupiny datových prvků“ a „Soubory dat“ poskytují další informace o tom, kde lze v ostatních modulech CHIS nalézt stejné DE. To by mělo usnadnit mapování balíčku mezi všemi jeho moduly a navigaci v souborech dat a zároveň se vyhnout shromažďování a zadávání dat stejných DE na více místech.

Všechny DE v modulu CE se používají při sestavování indikátorů.

| Název | Popis | Datové sady | DE skupiny |
| --- | --- | --- | --- |
| CH021 - Domácnosti spoléhající na čistou energii při vaření | Domácnosti, které jsou primárně závislé na čistých palivech a technologiích pro vaření | CH - Čistá energie (roční), CH - Nepřenosné nemoci (roční) | CH - Nepřenosné nemoci, CH - Čistá energie |
| CH022 - Domácnosti spoléhající na čistou energii pro osvětlení | Domácnosti, které jsou primárně závislé na čistých palivech a technologiích pro osvětlení | CH - Čistá energie (roční) | CH - Čistá energie |
| CH023 - Domácnosti spoléhající na čistou energii pro vytápění | Domácnosti primárně závislé na čistých palivech a technologiích pro vytápění | CH - Čistá energie (roční) | CH - Čistá energie |

## 2. Podrobnosti datové sady { #2-dataset-details }

### 2.1. Čistá energie { #21-clean-energy }

Sekce je nastavena tak, aby shromažďovala informace potřebné k identifikaci různých zdrojů energie využívané ve zkoumaných domácnostech k vaření, vytápění a osvětlení. Údaje o vaření jsou rozčleněny podle zdroje (solární, elektrický sporák, potrubí zemního plynu, bioplyn, LPG/plyn na vaření, kapalné palivo, jiné). Údaje o vytápění jsou rozčleněny podle typu (ústřední vytápění, sporák, tepelné čerpadlo, jiné). Údaje o osvětlení jsou rozčleněny podle zdroje energie (elektřina, solární energie, dobíjecí svítilna, mobil, svítilna/svítilna, baterka na baterie, bioplynová lampa, LPG lampa, jiné).

![Čistá energie](resources/images/chis-ene-y-001.png)

## 3. Pravidla ověření { #3-validation-rules }

Pro modul Clean Energy nejsou konfigurována žádná ověřovací pravidla.

## 4. Analytika a indikátory { #4-analytics-and-indicators }

Stejně jako u DE jsou v tabulce pod sloupcem „Skupiny indikátorů“ uvedeny informace o tom, zda se indikátor nachází v jiných skupinách, než je skupina indikátorů CE.

| Název | Popis | Čitatel | Jmenovatel | Skupiny indikátorů |
| --- | --- | --- | --- | --- |
| CH021b – Domácnosti spoléhající na čistou energii při vaření – Solární | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření – solární energii | Domácnosti vaření se solárním systémem | 1 | CH - Čistá energie |
| CH021c - Domácnosti spoléhající na čistou energii při vaření - Elektrický sporák | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - elektrický sporák | HHs vaření s elektrickým sporákem | 1 | CH - Čistá energie |
| CH021d - Domácnosti spoléhající se na čistou energii při vaření - Potrubní zemní plyn | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - Potrubní zemní plyn | HHs vaření s potrubím zemního plynu | 1 | CH - Čistá energie |
| CH021e - Domácnosti spoléhající na čistou energii při vaření - Bioplyn | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - Bioplyn | HHs vaření s bioplynem | 1 | CH - Čistá energie |
| CH021f - Domácnosti spoléhající na čistou energii při vaření - LPG | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - LPG / plyn na vaření | Domácnosti vaření s LPG | 1 | CH - Čistá energie |
| CH021g - Domácnosti spoléhající na čistou energii při vaření - Tekuté palivo | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - kapalné palivo (nikoli petrolej) | Domácnosti vaření s kapalným palivem | 1 | CH - Čistá energie |
| CH021h – Domácnosti spoléhající na čistou energii při vaření – Jiné | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření - Ostatní | Domácnosti vařen s ostatními palivy | 1 | CH - Čistá energie |
| CH021 – Domácnosti, které při vaření spoléhají na čistou energii (%) | Podíl domácností primárně závislých na čistých palivech a technologiích pro vaření | Domácnosti, které se při vaření spoléhají na čistá paliva a technologie | Domácnosti ve spádové oblasti | CH - Čistá energie, CH - Nepřenosné nemoci |
| CH022b – Domácnosti spoléhající na čistou energii pro osvětlení – Elektřina | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Elektřina | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení Elektřina | 1 | CH - Čistá energie |
| CH022c - Domácnosti spoléhající na čistou energii pro osvětlení - Solární energie | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Solární energie | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení Solární energie | 1 | CH - Čistá energie |
| CH022d - Domácnosti spoléhající na čistou energii pro osvětlení - Dobíjecí baterka | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Dobíjecí baterka | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení Dobíjecí baterka | 1 | CH - Čistá energie |
| CH022e - Domácnosti spoléhající na čistou energii pro osvětlení - Mobilní | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Mobilní | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení Mobile | 1 | CH - Čistá energie |
| CH022f - Domácnosti spoléhající na čistou energii pro osvětlení - Svítilna nebo lucerna | Podíl domácností primárně závislých na čistých palivech a technologiích pro svícení – pochodeň nebo lucerna | Domácnosti, které se spoléhají na čistá paliva a technologie pro zapalování pochodně nebo svítilny | 1 | CH - Čistá energie |
| CH022g - Domácnosti spoléhající na čistou energii pro osvětlení - Svítilna na baterie | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Svítilna na baterie | Domácnosti, které se spoléhají na čistá paliva a technologie pro svícení Baterkou napájenou baterií | 1 | CH - Čistá energie |
| CH022h - Domácnosti spoléhající na čistou energii pro osvětlení - Bioplynová lampa | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Bioplynová lampa | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení bioplynové lampy | 1 | CH - Čistá energie |
| CH022 – Domácnosti spoléhající na čistou energii pro osvětlení (%) | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení | HH, které se spoléhají na čistá paliva a technologie pro osvětlení | Domácnosti ve spádové oblasti | CH - Čistá energie |
| CH022i - Domácnosti spoléhající na čistou energii pro osvětlení - LPG lampa | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - LPG lampa | HHs, které se spoléhají na čistá paliva a technologii pro osvětlení LPG lamp | 1 | CH - Čistá energie |
| CH022l – Domácnosti spoléhající na čistou energii pro osvětlení – Ostatní | Podíl domácností primárně závislých na čistých palivech a technologiích pro osvětlení - Ostatní | Domácnosti, které se spoléhají na čistá paliva a technologie pro osvětlení Jiné | 1 | CH - Čistá energie |
| CH023b - Domácnosti spoléhající na čistou energii pro vytápění - Ústřední vytápění | Počet domácností primárně závislých na čistých palivech a technologiích pro vytápění - Ústřední vytápění | HHs, které se spoléhají na čistá paliva a technologie pro vytápění - Ústřední vytápění | 1 | CH - Čistá energie |
| CH023c - Domácnosti spoléhající na čistou energii pro vytápění - Kamna | Počet domácností primárně závislých na čistých palivech a technologiích pro vytápění - Kamna | HH, které se spoléhají na čistá paliva a techniku pro vytápění - kamna | 1 | CH - Čistá energie |
| CH023d - Domácnosti spoléhající na čistou energii pro vytápění - Tepelné čerpadlo | Počet domácností primárně závislých na čistých palivech a technologiích pro vytápění - Tepelné čerpadlo | Domácnosti, které se spoléhají na čistá paliva a technologie pro vytápění - Tepelné čerpadlo | 1 | CH - Čistá energie |
| CH023e – Domácnosti spoléhající na čistou energii pro vytápění – Jiné | Počet domácností primárně závislých na čistých palivech a technologiích pro vytápění - Ostatní | HH, které se spoléhají na čistá paliva a technologie pro vytápění – jiné | 1 | CH - Čistá energie |
| CH023 – Domácnosti, které se při vytápění spoléhají na čistou energii (%) | Podíl domácností primárně závislých na čistých palivech a technologiích pro vytápění | Domácnosti, které se při vytápění spoléhají na čistá paliva a technologii | Domácnosti ve spádové oblasti | CH - Čistá energie |

## 5. Ovládací panely { #5-dashboards }

Modul obsahuje předdefinovaný dashboard nazvaný „CH - Čistá energie“.

Předdefinované položky analyzují a vizualizují hlavní oblasti datové sady, i když řídicí panel by měl být upraven tak, aby lépe odrážel místní aktivity.

![Ovládací panely](resources/images/chis-ene-db-001.png)
