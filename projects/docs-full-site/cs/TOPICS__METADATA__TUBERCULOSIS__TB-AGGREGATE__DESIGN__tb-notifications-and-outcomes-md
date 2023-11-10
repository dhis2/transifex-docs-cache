---
edit_url: "https://github.com/dhis2-metadata/TB_AGG/blob/master/docs/tb_agg-design.md"
revision_date: "2022-05-25"
---

# Návrh systému agregátu TB { #tb-aggregate-design }

## Úvod { #introduction }

Tento dokument popisuje návrh systému pro konfigurační balíček TB pro agregované hlášení a zaměřuje se na to, jak byla v DHIS2 navržena část konfigurace shromažďování dat (tj. Datové sady a datové prvky).

## Přehled { #overview }

Konfigurační balíček TB pro agregované hlášení je založen na WHO [Definitions and reporting framework for tuberculosis](http://apps.who.int/iris/bitstream/10665/79199/1/9789241505345_eng.pdf). Obsahuje celkem 7 datových sad, jak je popsáno v tabulce 1.

| Název | Periodicita | Účel |
| :-- | :-- | :-- |
| Registrace případu TB | Čtvrtletně | Hlášení nových případů TB (oznámení) |
| Výsledky léčby TBC | Čtvrtletně | Hlášení výsledků léčby u léčby první linie |
| Výsledky léčby TBC - druhá řada | Ročně | Hlášení výsledků léčby léčby druhé linie |
| Detekce a léčba případů RR / MDR-TB | Ročně | Hlášení nových případů tuberkulózy rezistentní na léky |
| **[pouze staré záznamy]** Registrace případu TB podle výsledků rozmazání | Čtvrtletně | Hlášení nových případů TB (oznámení) na základě rámce pro podávání zpráv z roku 2006 |
| **[pouze staré záznamy]** Výsledky léčby tuberkulózy - podle výsledků stěru | Čtvrtletně | Hlášení výsledků léčby první linie na základě rámce pro podávání zpráv z roku 2006 |
| **[pouze staré záznamy]** Výsledky léčby TB - druhý řádek | Ročně | Hlášení výsledků léčby druhé linie na základě rámce pro podávání zpráv z roku 2006 |

Jak název napovídá, poslední 3 ze souborů dat zobrazených ve výše uvedené tabulce jsou zahrnuty pouze za účelem uchování historických údajů podle předchozích pokynů pro vytváření přehledů. To je důležité, protože epidemiologie tuberkulózy se mění relativně pomalu a analýza údajů o tuberkulóze vyžaduje pohled na víceletý trend. Kde je to možné, byly pro nové i staré formuláře použity stejné datové prvky. Indikátory obsažené v konfiguračním balíčku jsou propojeny s datovými prvky z aktuální i staré formy, aby bylo možné porovnat data shromážděná pomocí dvou různých rámců.

**Poznámka:** Tyto datové sady **[pouze staré záznamy]** by se **neměly** používat pro případné zadávání údajů.

## Struktura a design datové sady { #data-set-structure-and-design }

V této části budou pro každý soubor dat představeny hlavní oddíly (tabulky) souborů dat (formuláře pro podávání zpráv) s vysvětlením, jak a proč byly nakonfigurovány.

**[pouze staré záznamy]** nebudeme podrobně popisovat, protože jsou relativně blízké současným formulářům, s výjimkou věkového rozčlenění registračního formuláře případu.

### Registrace případu TB { #tb-case-registration }

#### Registrace případu { #case-registration }

![Registrace případu](resources/images/TB_AGG_image1.png)

Tabulka registrace případů byla nastavena na 12 jednotlivých datových prvků. Tuto tabulku si lze také představit jako tři datové prvky s „předchozím stavem léčby proti TB“ jako kategorií datových prvků. Existuje několik důvodů, proč byla zvolena „plochá“ struktura s jednotlivými datovými prvky:

-   Jak je uvedeno výše, bylo důležité mít strukturu konfiguračního balíčku TB, která umožňuje srovnání s předchozím rámcem vykazování. Použití ploché struktury umožňuje určitá pole (datové prvky) v této části znovu použít v předchozí verzi registračního formuláře případu.
-   Analýza těchto údajů se často provádí na konkrétních kombinacích těchto řádků a sloupců, které byly definovány jako indikátory. Použití kategorie pro status léčby by usnadnilo replikaci výše uvedené tabulky „tak, jak je“, ale zdá se to méně relevantní. V případě potřeby to lze znovu vytvořit pomocí sad skupin datových prvků.
-   Kategorie „předchozí stav léčby proti TB“ by se vztahovala pouze na 3 datové prvky. Při zahrnutí podobného konceptu / klasifikace předchozí léčby je jak soubor údajů pro TB rezistentní vůči lékům, tak předchozí rámec hlášení odlišně strukturován, takže zde nelze použít kategorie.

#### Registrace případu podle věku a pohlaví { #case-registration-by-age-and-sex }

![Registrace případů podle věku a pohlaví](resources/images/TB_AGG_image2.png)

Tato sekce / tabulka byla nakonfigurována jako jeden datový prvek s kombinací kategorií „věk a pohlaví“. I když se věková kategorie vztahuje pouze na jeden datový prvek, umožňuje to maximální flexibilitu analytických nástrojů, jak ukazuje následující příklad:

![Příklad kontingenční tabulky](resources/images/TB_AGG_image3.png)

#### Ověření dat { #data-validation }

Bylo nakonfigurováno ověřovací pravidlo, které kontroluje počet nových a opakovaných nákaz  hlášených v „Registraci případu“ na počet hlášených podle věku a pohlaví.

### Laboratorní aktivita a TB / HIV { #lab-activity-and-tbhiv }

![Laboratorní diagnostická aktivita a TB/HIV](resources/images/TB_AGG_image4.png)

Tyto dvě sekce / tabulky byly nakonfigurovány jako jednotlivé datové prvky.

#### Ověření dat { #data-validation }

Pro tyto kontroly byla nakonfigurována ověřovací pravidla:

-   Laboratorní vyšetření provedena ≥ pozitivní výsledky
-   HIV status známý ≥ status pozitivní
-   Stav HIV pozitivní  ≥ CPT / ART

### Výsledky léčby TBC { #tb-treatment-outcomes }

#### Výsledky léčby { #treatment-outcomes }

![Výsledky léčby](resources/images/TB_AGG_image5.png)

Tabulka výsledků léčby (která se týká pouze léčby první linie) je kategorizována podle typu případu TBC (potvrzeno bakteriologicky, klinicky, dříve léčeno, HIV pozitivní). V tabulce pro každou kategorii pacientů je uveden počet registrovaných případů (tj. Kohorta léčby) a výsledek léčby. Každá kategorie pacientů je v DHIS2 nakonfigurována jako jeden datový prvek pro registrované případy / kohortu a jeden pro výsledky léčby. Datové prvky výsledku léčby mají kategorii „výsledek léčby TB“ u každého ze 6 výsledků léčby.

Nejprve je jasné, že mít **jeden** datový prvek pro každou kategorii případů TB by nedávalo smysl, protože by zahrnovalo jak kohortu, tak počet hlášených výsledků, tj. Součet kategorie by nedělal smysl, což je obecné pravidlo. Tabulka však _může_ být nastavena tak, aby každé pole bylo samostatným datovým prvkem. Důvod, proč byla vybrána kategorie, zahrnuje:

-   Obecná doporučení pro kategorie spočívají v tom, že součet všech možností by měl mít smysl, protože je to součet, který se ve výchozím nastavení zobrazuje v nástrojích pro vytváření sestav. I když součet v tomto případě nemusí být nijak zvlášť užitečný (jedná se v podstatě o celkový počet hodnocených výsledků), jedná se o smysluplné číslo. Pro srovnání, běžným příkladem kategorie, která nejčastěji nedává smysl, jsou „případy a úmrtí“.
-   Při zahrnutí současné a staré formy, první a druhý řádek, se kategorie výsledků léčby vztahuje na 13 kategorií případů. Použití kategorie tak pomáhá snížit počet datových prvků ze 78 na 13.
-   Použití kategorie maximalizuje flexibilitu při analýze dat o výsledku léčby. Například celkový počet výsledků s „úspěšností léčby“ (která je definována jako součet „vyléčených“ a „dokončených léčby“) lze zobrazit jednoduše nastavením filtru se dvěma možnostmi kategorie.

#### Ověření dat { #data-validation }

Byla stanovena ověřovací pravidla, která ověřují, že velikost kohorty (registrované případy) je stejná jako počet hlášených výsledků léčby.

#### TB / HIV { #tbhiv }

![Aktivity TB / HIV](resources/images/TB_AGG_image6.png)

Sekce / tabulka TB / HIV souboru údajů o výsledcích léčby se velmi podobá sekci TB / HIV v registračním formuláři případu. Je zahrnuto, protože často není možné zjistit stav HIV u významné části případů v době sestavování čtvrtletní zprávy o oznámení. Sekce TB / HIV ve zprávě o výsledcích léčby umožňuje sběr úplných informací o stavu HIV. Má podobné proměnné související se stavem HIV, ale používá oddělené datové prvky s postfixem „(podle času výsledku)“. Platí zde stejná pravidla ověřování jako v tabulce TB / HIV v datové sadě registrace případů.

### Výsledky léčby TBC - druhá řada { #tb-treatment-outcomes-second-line }

#### Výsledky léčby { #treatment-outcomes }

![Výsledky léčby](resources/images/TB_AGG_image7.png)

Výsledky léčby pro případy režimu druhé linie byly nakonfigurovány stejným způsobem, jak je popsáno výše, a se stejnými pravidly ověřování.

### Detekce a léčba případů RR / MDR-TB { #rrmdr-tb-case-detection-and-treatment }

#### Detekce případů { #case-detection }

![Detekce případů](resources/images/TB_AGG_image8.png)

Sekce / tabulka detekce případů je konfigurována s jednotlivými datovými prvky.

#### Ověření dat { #data-validation }

Pravidlo ověřování dat kontroluje, zda je počet případů RR-TB nebo MDR-TB větší než počet pouze případů MDR-TB.

#### Léčba { #treatment }

![Léčba](resources/images/TB_AGG_image9.png)

Sekce / tabulka léčby je konfigurována s jednotlivými datovými prvky.

### [pouze staré záznamy] Registrace případu TB podle výsledků stěrů { #old-records-only-tb-case-registration-by-smear-results }

#### Případy podle pohlaví a věku (starší) { #cases-by-sex-and-age-legacy }

![Případy podle pohlaví a věku (legacy)](resources/images/TB_AGG_image10.png)

Datové soubory [pouze staré záznamy] nejsou podrobně diskutovány, ale zvláštní část si zaslouží část / tabulka „případy podle pohlaví a věku“. Předchozí rámec pro hlášení TB (verze z roku 2006) umožňoval určité variace v tom, jak jsou oznámení rozdělena podle věku. V důsledku toho různé země používají několik různých věkových členění. Protože konfigurační balíček TB je navržen pro použití v různých zemích / kontextech, používá sekce „případy podle pohlaví a věku“ kategorii pohlaví, která zahrnuje „neznámé pohlaví“, a věkovou kategorii, která zahrnuje několik různých možností překrývání věku. Zahrnuje například 0-4 roky, 5-14 let _a_ 0-14 let. Toto obecně **není** doporučený přístup, protože 1) celkový součet kategorie nedává smysl a 2) existuje riziko dvojího započítání, pokud jsou použity všechny věkové skupiny. To však bylo provedeno zde z následujících důvodů:

-   Používá se pouze pro historická data, která nejsou určena k ručnímu zadávání (a pokud jsou zadána ručně
-   Jelikož je navržen pro použití s již existujícími daty, neměl by existovat žádný případ, kdy existují data pro některá z překrývajících se
-   Zahrnutí pouze jedné sady možností pro věk a ponechání na každé zemi, aby přidala, jakmile potřebují, by mohlo fungovat, ale vyžadovalo by aktualizace vzorců indikátorů, protože by se vygenerovala nová kombinace možností kategorie.
-   Možnosti jednotlivých kategorií lze znovu použít, a to jak aktuální, tak staré rámce. Při použití skupin možností kategorií je možné definovat věkové členění, které fungují v průběhu času, i když se vykazované věkové skupiny mění.
-   Poměrně velký počet zemí uložil svá historická data do globální databáze DHIS2 udržované WHO GTB, kde se tato kategorie používá (z výše uvedených důvodů). Pokud by byla pro historická data v konfiguračním balíčku TB použita jiná kategorie, přesun těchto dat do národní databáze DHIS2 by byl komplikovanější.
