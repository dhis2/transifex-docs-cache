---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/ch_wash_aggregate_design.md"
revision_date: "2021-10-19"
---

# CH - Voda, sanitace a hygiena { #ch-wash-aggregate-design }

## 1. Datové sady { #1-datasets }

### 1.1. Souhrn konfigurace { #11-configuration-summary }

Souhrnný modul CH - Voda, sanitace a hygiena (WASH) obsahuje:

1. **roční soubor dat** pro sledování klíčových ročních informací
2. **Základní indikátory** pro datovou sadu
3. Předdefinovaný přístrojový panel **CH - WASH**

Doporučuje se, aby byly datové sady přiřazeny k organizačním jednotkám **na nejnižší úrovni** zdravotnického systému, které je možné pro hlášení dat, jako jsou vesnice nebo jakékoli vhodné vymezení komunity podle místního kontextu.

### 1.2. Datové prvky { #12-data-elements }

Níže uvedená tabulka shrnuje datové prvky přítomné v modulu WASH. Sloupce „Skupiny datových prvků“ a „Soubory dat“ poskytují další informace o tom, kde lze v ostatních modulech CHIS nalézt stejné DE. To by mělo usnadnit mapování balíčku mezi všemi jeho moduly a navigaci v souborech dat a zároveň se vyhnout shromažďování a zadávání dat stejných DE na více místech. V tomto případě nejsou DE v modulu WASH sdíleny s žádným jiným modulem.

Všechny DE v modulu WASH se používají při sestavování indikátorů.

| Název | Popis | Datové sady | DE skupiny |
| --- | --- | --- | --- |
| CH001a - Domácnosti ve spádové oblasti | Domácnosti ve spádové oblasti | CH – Složení populace (roční) | CH - Složení populace, CH - Čistá energie, CH - Ochrana dětí a mezilidské násilí, CH - Voda, sanitace a hygiena (WASH), CH - Nepřenosné nemoci |
| CH010 - Domácnosti s přístupem k lepšímu zdroji vody | Domácnosti s přístupem k lepšímu zdroji vody | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH011 - Přístup domácností k pitné vodě do 30 minut | Domácnosti, které nepotřebují přístup k pitné vodě déle než 30 minut | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH012 - Domácnosti s pitnou vodou na místě | Domácnosti s pitnou vodou na místě | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH013a - Provedené zkoušky vody - výsledky zkoušek | Vodní zkoušky provedené v povodí podle výsledků zkoušek | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH013b - Provedené zkoušky vody - typ zdroje | Testy vody prováděné v povodí podle typu zdroje | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH014 - Domácnosti s nedostatkem pitné vody | Domácnosti, které v případě potřeby neměly dostatečné množství pitné vody | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH015a - Domácnosti s pevným zařízením na mytí rukou v místě | Domácnosti s přístupem k zařízení na mytí rukou s vodou a mýdlem dostupným v místě - opraveno | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH015b - Domácnosti s mobilním zařízením na mytí rukou v místě | Domácnosti s přístupem k zařízení na mytí rukou s vodou a mýdlem k dispozici v místě - mobilní | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH016 - Domácnosti s přístupem k lepším hygienickým zařízením | Domácnosti s přístupem k lepším hygienickým zařízením | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH017 - Domácnosti sdílející používaná hygienická zařízení | Domácnosti sdílející hygienická zařízení, která používají | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH018a - Domácnosti s sanitárním zařízením na místě nikdy nevyprazdňované | Domácnosti využívající sanitární zařízení na místě, která byla někdy vyprázdněna | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH018b - Domácnosti s sanitárním zařízením a skladem | Domácnosti využívající sanitární zařízení s vlastním skladem | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH018c - Domácnosti se sanitárním zařízením, které se nikdy nevyprazdňuje podle režimu vyprazdňování | Domácnosti využívající sanitární zařízení na místě, která byla někdy vyprázdněna podle vyprazdňovacího režimu | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH018d - Domácnosti s sanitárním zařízením a skladováním podle režimu vyprazdňování | Domácnosti s hygienickým zařízením v místě se skladováním podle režimu vyprazdňování | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH019a - Ženy s vlastním mytím a výměnným prostorem během menstruace | Ženy a dívky, které mají soukromé místo k mytí a převlékání během menstruace | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH019b - Ženy a dívky dotazované během návštěv v domácnosti | Ženy a dívky dotazované během návštěv domácností | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |
| CH020 - Ženy používající hygienické prostředky během menstruace | Ženy a dívky používající hygienické materiály během menstruace | CH - Voda, sanitace a hygiena (ročně) | CH - Voda, sanitace a hygiena (WASH) |

## 2. Podrobnosti datové sady { #2-dataset-details }

### 2.1. Roční datový soubor WASH { #21-yearly-wash-dataset }

#### 2.1.1. Pitná voda { #211-drinking-water }

Sekce vykazuje údaje o přístupu k pitné vodě u hodnocených domácností. Údaje se člení podle typu zdroje vody (potrubní voda, vrty nebo trubkové studny, chráněné kopané studny, chráněné prameny, dešťová voda, balená nebo dodávaná voda – kategorie by měly být přizpůsobeny tak, aby lépe odrážely místní kontext).

![Pitná voda](resources/images/chis-wash-y-001.png)

#### 2.1.2. Kvalita vody { #212-water-quality }

Část se zaměřuje na testy prováděné na vodě. Testy jsou rozčleněny podle výsledků (pozitivní a negativní) a/nebo podle zdroje vody (potrubní voda, vrty nebo trubkové studny, chráněné kopané studny, chráněné prameny, dešťová voda, balená nebo dodávaná voda - kategorie by měly být přizpůsobeny tak, aby lépe zrcadlily místní kontext).

![Kvalita vody](resources/images/chis-wash-y-002.png)

#### 2.1.3. Zařízení na mytí rukou { #213-hand-washing-facilities }

Sekce uvádí přítomnost pevných nebo mobilních zařízení na mytí rukou v domácnostech. Členění zařízení je podle umístění (obydlí, pozemek/dvorek, jinde). Kategorie lze upravovat podle místního kontextu.

![Zařízení na mytí rukou](resources/images/chis-wash-y-003.png)

#### 2.1.4. Vylepšená/sdílená hygiena { #214improvedshared-sanitation }

Sekce poskytuje informace o domácnostech sdílejících zařízení (rozdělené podle typu zařízení) ao domácnostech, které mají přístup k vylepšeným zařízením (v členění podle typu vylepšeného zařízení).

![Vylepšená/sdílená hygiena](resources/images/chis-wash-y-004.png)

#### 2.1.5. Vyprázdnění sanitárních zařízení na místě { #215-emptying-of-on-site-sanitation-facilities }

Sekce uvádí údaje o sanitaci, která se nachází na místě, a o tom, jak jsou vyprázdněny, pokud vůbec. Informace jsou rozčleněny podle způsobu vyprazdňování (poskytovatel služby, zasypaná, nezakrytá jáma, otevřená půda, vodní plocha, jinde – možnosti by měly být přizpůsobeny tak, aby lépe odrážely místní kontext) a podle typu toalety/skladování (latríny, septiky, kompostování WC, dvojité jímky).

![Vyprázdnění sanitárních zařízení na místě](resources/images/chis-wash-y-005.png)

#### 2.1.6. Hygienická zařízení { #216-hygiene-facilities }

Sekce shromažďuje informace o ženách a jejich dostupnosti hygienických prostor a materiálů během menstruace. Údaje o hygienickém produktu jsou členěny podle typu produktu (Vložky - jednorázové, vložky - opakovaně použitelné, utěrky - jednorázové, utěrky - jednorázové, tampony - jednorázové, menstruační kalíšky - opakovaně použitelné, jiné - jednorázové, jiné - opakovaně použitelné, žádné).

![Hygienická zařízení](resources/images/chis-wash-y-006.png)

## 3. Pravidla ověření { #3-validation-rules }

Pro datovou sadu WASH byla nastavena následující pravidla ověřování:

| název | návod | operátor | popis na levé straně | popis na pravé straně |
| --- | --- | --- | --- | --- |
| CH – sanitární zařízení na místě domácností, kt. se nikdy nevyprázdní Vs sanitární zařízení na místě domácností, s úložištěm na místě | Nikdy nevyprázdněná sanitární zařízení domácností na místě by měla být menší nebo rovna sanitárním zařízením domácností na místě skladování | less_than_or_equal_to | Hygienická zařízení na místě domácností, nikdy nebyla vyprázdněna | Domácnosti, v místě sanitární zařízení, v místě skladování |
| CH - Vodní testy provedené podle typu zdroje Vs Vodní testy provedené na základě výsledků testů | Testy vody prováděné podle typu zdroje by měly být menší nebo rovné Testům vody prováděným na základě výsledků testů | less_than_or_equal_to | Testy vody prováděné podle typu zdroje | Testy vody prováděné na základě výsledků testů |
| CH - WYG mají soukromé místo, kde se mohou během menstruace převléknout, oproti ženám a dívkám dotazovaným během návštěv v domácnosti | WYG mají soukromé místo pro převlékání během menstruace by mělo být menší nebo stejné jako u žen a dívek dotazovaných během návštěv v domácnosti | less_than_or_equal_to | WYG mají soukromé místo na převlékání během menstruace | Ženy a dívky dotazované během návštěv domácností |
| CH - WYG používající hygienické materiály během menstruace versus ženy a dívky dotazované během návštěv v domácnosti | WYG používající hygienické materiály během menstruace by měly být menší nebo stejné jako u žen a dívek zkoumaných během návštěv v domácnosti | less_than_or_equal_to | WYG používající hygienické materiály během menstruace | Ženy a dívky dotazované během návštěv domácností |

## 4. Analytika a indikátory { #4-analytics-and-indicators }

Stejně jako u DE jsou v tabulce pod sloupcem „Skupiny indikátorů“ uvedeny informace o tom, zda se indikátor nachází v jiných skupinách než ve skupině indikátorů WASH.

| Název | Popis | Čitatel | Jmenovatel | Skupiny indikátorů |
| --- | --- | --- | --- | --- |
| CH010 – Domácnosti s přístupem k lepšímu zdroji vody (%) | Podíl domácností s přístupem k lepšímu zdroji vody | Domácnosti s přístupem k lepšímu zdroji vody | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH011 – Domácnosti s přístupem k pitné vodě do 30 minut (%) | Podíl domácností na době sběru pitné vody = < 30 minut | Domácnosti potřebují < 30 minut na přístup k pitné vodě | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH012 - Domácnosti s pitnou vodou v místě (%) | Podíl domácností s pitnou vodou v místě | Domácnosti, které mají v místě vodu | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH013 - Testy vody ve spádové oblasti -ve na E. coli (%) | Podíl kvality pitné vody u zdrojů negativní pro E. coli | Byly provedeny negativní testy vody | Provedeny vodní testy | CH - Voda, sanitace a hygiena (WASH) |
| CH014 - Domácnosti s nedostatkem pitné vody (%) | Podíl domácností s nedostatkem pitné vody v případě potřeby | Domácnosti, kterým chybí dostatečné množství pitné vody | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH015 – Domácnosti se zařízením na mytí rukou v místě (%) | Podíl domácností s přístupem k zařízení na mytí rukou s vodou a mýdlem dostupným v místě | Zařízení na mytí rukou v domácnostech v místě - opraveno | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH016 – Domácnosti s přístupem k lepším hygienickým zařízením (%) | Podíl domácností využívající zlepšená hygienická zařízení | Domácnosti s přístupem k lepším hygienickým zařízením | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH017 – Domácnosti sdílející používaná hygienická zařízení (%) | Podíl domácností sdílejících sanitárních zařízení | Domácnosti sdílející hygienická zařízení, která používají | Domácnosti ve spádové oblasti | CH - Voda, sanitace a hygiena (WASH) |
| CH018 - Domácnosti s nevyprázdněným hygienickým zařízením v místě  (%) | Podíl domácností s vyprazdňováním sanitárních zařízení v místě (septiků a jímkových latrín) | Hygienická zařízení na místě domácností, nikdy nebyla vyprázdněna | Domácnosti, na místě sanitární zařízení, na místě skladování | CH - Voda, sanitace a hygiena (WASH) |
| CH019 - Ženy s vlastním mytím a převlékacím prostorem během menstruace (%) | Podíl žen se soukromým místem k mytí a převlékání během menstruace | WYG mají soukromé místo na převlékání během menstruace | Ženy a dívky dotazované během návštěv domácností | CH - Voda, sanitace a hygiena (WASH) |
| CH020 – Ženy používající hygienické prostředky během menstruace (%) | Podíl žen používajících hygienické pomůcky během menstruace | WYG používající hygienické materiály během menstruace | Ženy a dívky dotazované během návštěv domácností | CH - Voda, sanitace a hygiena (WASH) |

## 5. Ovládací panely { #5-dashboards }

Modul obsahuje předdefinovaný ovládací panel s názvem „CH - WASH“.

Předdefinované položky na ovládacím panelu zahrnují data podle sekcí přítomných v datové sadě, ale obsah by měl být přizpůsoben na základě místních aktivit.

![WASH Ovládací panel](resources/images/chis-wash-db.png)
