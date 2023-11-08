---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/ch_cbs_aggregate_design.md"
revision_date: "2021-10-19"
---

# CH - Komunitní dohled (CBS) { #ch-cbs-aggregate-design }

## 1. Datové sady { #1-datasets }

### 1.1. Souhrn konfigurace { #11-configuration-summary }

Souhrnný modul CH – komunitní dohled zahrnuje:

1. **měsíční datový soubor** s klíčovými datovými prvky pro CBS
2. **Základní indikátory** pro datovou sadu
3. Předdefinovaný ovládací panel **„CH – komunitní dohled“**

Doporučuje se, aby byly datové sady přiřazeny k organizačním jednotkám **na nejnižší úrovni** zdravotnického systému, které je možné pro hlášení dat, jako jsou vesnice nebo jakékoli vhodné vymezení komunity podle místního kontextu.

## 1.2. Datové prvky { #12-data-elements }

Níže uvedená tabulka shrnuje datové prvky přítomné v modulu CBS. Sloupce „Skupiny datových prvků“ a „Soubory dat“ poskytují další informace o tom, kde lze v ostatních modulech CHIS nalézt stejné DE. To by mělo usnadnit mapování balíčku mezi všemi jeho moduly a navigaci v souborech dat a zároveň se vyhnout shromažďování a zadávání dat stejných DE na více místech. V tomto případě nejsou CBS DE sdíleny s žádným jiným modulem.

Všechny DE v modulu CBS se používají při sestavování indikátorů.

| Název | Popis | Rozčlenění | Datové Sady | Skupiny datových prvků |  |
| --- | --- | --- | --- | --- | --- |
| CH173a - Byl zjištěn případ událostí / výstrahy | Byl zjištěn případ událostí / výstrahy | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |
| CH173b – Zjištěn případ událostí / výstrahy | Zjištěný případ událostí / výstrahy | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |
| CH174a - CBS výstrahy s včasnou reakcí | Výstrahy CBS reagovaly do 24 hodin nebo ve stanoveném časovém období podle protokolu CBS | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |
| CH174b - výstrahy CBS | Upozornění CBS | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |
| CH175a - Komunity v akci po výstrahách | Komunity, ve kterých bylo po upozornění přijato opatření (za měsíc) | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |
| CH175b - Komunity s upozorněním(i) | Komunity, ve kterých došlo alespoň k upozornění (za měsíc) | výchozí | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |  |

## 2. Podrobnosti datových sad { #2-datasets-details }

### 2.1. CBS Dataset { #21-cbs-dataset }

Sekce je nastavena tak, aby shromažďovala informace nezbytné ke sledování znalostí a reakce komunity na výstrahy a události.

![CBS](resources/images/chis-cbs-m-001.png)

## 3. Pravidla ověření { #3-validation-rules }

Pro datové soubory CBS byla nastavena následující pravidla ověřování:

| Název | Popis | Datové sady | DE skupiny |
| --- | --- | --- | --- |
| CH173a - Byl zjištěn případ událostí / výstrahy | Byl zjištěn případ událostí / výstrahy | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |
| CH173b – Zjištěn případ událostí / výstrahy | Zjištěný případ událostí / výstrahy | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |
| CH174a - CBS výstrahy s včasnou reakcí | Výstrahy CBS reagovaly do 24 hodin nebo ve stanoveném časovém období podle protokolu CBS | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |
| CH174b - výstrahy CBS | Upozornění CBS | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |
| CH175a - Komunity v akci po výstrahách | Komunity, ve kterých bylo po upozornění přijato opatření (za měsíc) | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |
| CH175b – Komunity s upozorněním | Komunity, ve kterých došlo alespoň k upozornění (za měsíc) | CH – Komunitní dohled (měsíční) | CH - Komunitní dohled |

## 4. Analytika a indikátory { #4-analytics-and-indicators }

Stejně jako u DE jsou v tabulce pod sloupcem „Skupiny indikátorů“ uvedeny informace o tom, zda se indikátor nachází v jiných skupinách, než je skupina indikátorů CBS.

| Název | Popis | Čitatel | Jmenovatel | Skupiny indikátorů |
| --- | --- | --- | --- | --- |
| CH173 - Byl zjištěn případ událostí / výstrahy | Počet detekovaných událostí / případ výstrah | Byl zjištěn případ událostí / výstrahy | 1 | CH - Komunitní dohled |
| CH174b - výstrahy CBS | Počet výstrah CBS | Upozornění | 1 | CH - Komunitní dohled |
| CH175b - Komunity s výstrahami | Počet komunit s upozorněními | Komunity s upozorněními | 1 | CH - Komunitní dohled |
| CH175 – Komunity v akci po upozorněních (%) | Podíl komunit, ve kterých byla po upozornění přijata opatření (za měsíc) | Po upozornění byla přijata opatření | Komunity s 1+ upozorněním (za měsíc) | CH - Komunitní dohled |

## 5. Ovládací panely { #5-dashboards }

Modul obsahuje předdefinovaný řídicí panel nazvaný „CH - Community-based surveillance“.

Předdefinované položky analyzují a vizualizují hlavní oblasti datové sady, i když řídicí panel by měl být upraven tak, aby lépe odrážel místní aktivity. ![Ovládací panel](resources/images/chis-cbs-db-001.png)
