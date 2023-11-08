---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/configure-report-functionality.md"
revision_date: "2021-06-14"
---

# Nakonfigurujte funkčnost sestavy { #setting_up_reporting }

## Zdroje dat pro hlášení { #reporting_data_sources }

### Druhy dat a agregace { #types-of-data-and-aggregation }

Ve větším obraze terminologie HIS se všechna data v DHIS2 obvykle nazývají agregovaná, protože se jedná o agregáty (např. měsíční souhrny) lékařských záznamů nebo jakési servisní registry hlášené ze zdravotnických zařízení. Agregace uvnitř DHIS2, která je zde předmětem, se zabývá tím, jak jsou surová data zachycená v DHIS2 (prostřednictvím zadávání nebo importu dat) dále agregována v čase (např. z měsíčních na čtvrtletní hodnoty) nebo nahoru v organizační hierarchii (např. ze zařízení na okresní hodnoty).

#### Terminologie { #terminology }

-   _Raw data_ odkazuje na data, která jsou registrována do DHIS2 buď prostřednictvím zadávání dat, nebo importu dat a nebyla zpracována procesem agregace DHIS2. Všechna tato data jsou uložena v tabulce (nebo objektu Java, chcete-li) s názvem DataValue.

-   _Aggregovaná data_ odkazuje na data, která byla agregována serverem DHIS2, což znamená, že již nejde o nezpracovaná data, ale o nějaký druh agregace nezpracovaných dat.

-   _Hodnoty indikátoru_ lze také chápat jako agregovaná data, ale jsou speciální tím, že se počítají na základě uživatelem definovaných vzorců (faktor \* čitatel / jmenovatel). Hodnoty indikátoru jsou tedy zpracovaná data, nikoli surová data, a jsou umístěny v tabulce / objektu agregované hodnoty indikátoru. Indikátory se počítají na jakékoli úrovni organizační hierarchie a tyto výpočty jsou pak založeny na agregovaných hodnotách dat dostupných na každé úrovni. Atribut level v tabulce aggregateddatavalue odkazuje na organizační úroveň organizace, pro kterou byla hodnota vypočítána.

-   _Období a Typ období_ se používají k určení časové dimenze nezpracovaných nebo agregovaných hodnot a data lze agregovat z jednoho typu období do druhého, např. z měsíčního na čtvrtletní nebo denní na měsíční. Každá datová hodnota má jedno období a toto období má jeden typ období. Např. datové hodnoty pro období leden, únor a březen 2009 lze všechny typy měsíčních období agregovat společně na agregovanou hodnotu dat s obdobím 1. čtvrtletí 2009 a obdobím Čtvrtletně.

#### Základní pravidla agregace { #basic-rules-of-aggregation }

##### Co se sčítá { #what-is-added-together }

Data (raw) lze registrovat na jakékoli organizační úrovni, např. v národní nemocnici na úrovni 2, ve zdravotnickém zařízení na úrovni 5 nebo ve větším PHC na úrovni 4. To se liší od země k zemi, ale DHIS2 je flexibilní v tom, že umožňuje zadávání dat nebo import dat na jakékoli úrovni. To znamená, že organizační jednotky, které samy mají podřízené, mohou registrovat data, někdy stejné datové prvky jako jejich podřízené jednotky. Základní pravidlo agregace v DHIS2 je, že _všechna nezpracovaná data se agregují dohromady_, což znamená, že data registrovaná v zařízení na úrovni 5 se přidají k datům registrovaným pro PHC na úrovni 4.

Je na uživateli / administrátorovi / návrháři systému, aby se ujistil, že nedochází k duplikaci zadávání dat a že např. data zadaná na úrovni 4 nejsou o stejných službách / návštěvách, jaké hlásí děti organizačních jednotek na úrovni 5.

> **POZNÁMKA**
>
> V některých případech chcete mít duplikování dat v systému, ale kontrolovaným způsobem. Např. když máte dva různé zdroje dat pro odhady populace, jak údaje o populaci povodí úrovně 5, tak další zdroj údajů o populaci pro úroveň 4 na základě údajů ze sčítání (protože součet spádové oblasti na úrovni 5 není vždy stejný jako údaje ze sčítání na úrovni 4). Pak můžete určit pomocí pokročilého nastavení agregace (viz dále dolů), že by systém měl např. nepřidávat údaje o populaci úrovně 5 do údajů o populaci úrovně 4 a agregáty údajů o úrovni 3,2,1 populace jsou založeny pouze na datech úrovně 4 a nezahrnují data úrovně 5.

##### Jak se data sčítají { #how-data-gets-added-together }

Způsob agregace dat závisí na dimenzi agregace (viz dále dolů).

Podél dimenze na úrovni organizační jednotky jsou vždy shrnuta data; tj. jednoduše sečteno. Nezapomeňte, že hrubá data nikdy nejsou procenta, a proto je lze sečíst dohromady. S hodnotami indikátorů, které mohou být procenty, se zachází odlišně (přepočítávají se na každé úrovni, nikdy se nesčítají).

Podél časové dimenze existuje několik možností, dva nejběžnější způsoby agregace jsou součet a průměr. Uživatel může určit pro každý datový prvek, kterou metodu použít, nastavením operátoru agregace (viz dále dolů). Měsíční servisní data se obvykle sčítají v průběhu času, např. počet vakcín podaných za rok je součtem vakcín podaných za každý měsíc daného roku. Pro populaci, vybavení, zaměstnance a další druhy takzvaných semipermanentních dat se často používá průměrná metoda, jako např. „počet sester“ pracujících v zařízení za rok by nebyl součtem dvou čísel uvedených v šestiměsíční zprávě o personálním obsazení, ale spíše průměrem těchto dvou čísel. Další podrobnosti dále v části „operátory agregace“.

#### Dimenze agregace { #dimensions-of-aggregation }

##### Organizační jednotky a úrovně { #organisational-units-and-levels }

Organizační jednotky se používají k reprezentaci dimenze „kde“ spojené s datovými hodnotami. V DHIS2 jsou organizační jednotky uspořádány do hierarchie, která obvykle odpovídá hierarchické povaze organizace nebo země. Úrovně organizačních jednotek odpovídají odlišným úrovním v hierarchii. Například, země může být rozdělena do krajů, pak okresů, pak zařízení a pak sub-center. Tato organizační hierarchie by měla pět úrovní. V rámci každé úrovně by existovala řada organizačních jednotek. Během procesu agregace se data agregují z nižších úrovní organizační jednotky na vyšší úrovně. V závislosti na provozovateli agregace mohou být data „sčítána“ nebo „zprůměrována“ na dané úrovni organizační jednotky, aby se odvodil souhrnný součet za všechny organizační jednotky, které jsou obsaženy na úrovni organizační jednotky vyšší úrovně. Například pokud je v kraji deset okresů a operátor agregace pro daný datový prvek byl definován jako „SUM“, souhrnný součet za kraj by se vypočítal jako součet hodnot jednotlivých deseti okresů obsažených v tom kraji.

##### Období { #period }

Období se používají k vyjádření dimenze „kdy“ spojené s datovými hodnotami. Data lze snadno agregovat z týdnů na měsíce, z měsíců na čtvrtletí a ze čtvrtletí na roky. DHIS2 používá známá pravidla toho, jak jsou tyto různé intervaly obsaženy v jiných intervalech (například je známo, že čtvrtletí 2010 obsahuje leden 2010, únor 2010 a březen 2010), aby agregoval data z menších časových intervalů, např. týdny, do delších časových intervalů, např. měsíce.

##### Datové prvky a kategorie { #data-elements-and-categories }

Dimenze datového prvku určuje „co“ se zaznamenává konkrétní datovou hodnotou. Kategorie datových prvků jsou ve skutečnosti zdegenerované dimenze dimenze datových prvků a používají se k rozložení dimenze datových prvků do jemnějších kategorií. Kategorie datových prvků, například „Věk“ a „Pohlaví“, se používají k záznamu konkrétního datového prvku, obvykle pro různé skupiny populace. Tyto kategorie lze poté použít k výpočtu celkového součtu pro kategorii a součtu všech kategorií.

#### Agregační operátory, metody agregace { #aggregation-operators-methods-for-aggregation }

##### Součet { #sum }

Operátor 'sum' jednoduše vypočítá součet všech datových hodnot, které jsou obsaženy v konkrétní agregační matici. Pokud jsou například data zaznamenávána na měsíční bázi na úrovni okresů a jsou agregována do čtvrtletních součtů krajů, budou k získání souhrnného součtu sečteny všechny údaje obsažené ve všech okresech pro daný kraj a všechny týdny pro dané čtvrtletí.

##### Průměr { #average }

Když je vybrán operátor průměrné agregace, vypočítá se nevážený průměr všech hodnot dat v dané agregační matici.

Je důležité pochopit, jak DHIS2 zachází s hodnotami null v kontextu průměrného operátora. Je poměrně běžné, že některé organizační jednotky nezasílají data pro určité datové prvky. V kontextu průměrného operátora je průměr výsledkem počtu datových prvků, které jsou skutečně přítomny (tedy NE NULL) v dané agregační matici. Pokud v daném kraji existuje 12 okresů, ale pouze 10 z nich poskytlo údaje, bude průměrný souhrn výsledkem těchto deseti hodnot, které jsou ve skutečnosti v databázi, a nebude brát v úvahu chybějící hodnoty.

#### Pokročilé nastavení agregace (úrovně agregace) { #advanced-aggregation-settings-aggregation-levels }

##### Úrovně agregace { #aggregation-levels }

Normálním pravidlem systému je agregovat všechna nezpracovaná data společně při přechodu nahoru v organizační hierarchii a systém předpokládá, že zadávání dat nebude duplikováno zadáním stejných služeb poskytovaných stejným klientům na úrovni obou zařízení a také zadáním 'agregovaného' (součet všech zařízení) čísla na vyšší úrovni. To má usnadnit agregaci, když jsou poskytovány stejné služby, ale různým klientům / populacím spádových zařízení v zařízeních na úrovni 5 a PHC (nadřazený stejných zařízení) na úrovni 4. Tímto způsobem zařízení na úrovni 5 a PHC na úrovni 4 může sdílet stejné datové prvky a jednoduše sčítat jejich počty, aby poskytly celkový počet služeb poskytovaných v zeměpisné oblasti.

Někdy taková agregace není žádoucí, jednoduše proto, že by to znamenalo duplikování dat o stejné populaci. To je případ, kdy máte dva různé zdroje dat pro dvě různé úrovně organizačních jednotek. Např. populace spadající pod zařízení může pocházet z jiného zdroje než okresní populace, a proto součet populací pod zařízením neodpovídá populaci okresu poskytované např. údaje ze sčítání. Pokud tomu tak je, skutečně bychom chtěli duplikovaná data v systému, aby každá úroveň mohla mít co nejpřesnější čísla, ale pak nechceme agregovat tyto zdroje dat dohromady.

V sekci Datové prvky můžete upravit datové prvky a pro každý z nich určit, jak se provádí agregace pro každou úroveň. V případě popsaném výše musíme systému sdělit, aby nezahrnoval údaje o zařízení o populaci v žádné z agregací nad touto úrovní, jako výše, v tomto případě okresy zaregistrovaly svou populaci přímo jako surová data. Údaje o obyvateli okresu by pak měly být použity na všech výše uvedených úrovních včetně úrovně okresů, zatímco úroveň zařízení by měla používat vlastní data.

##### Jak upravit agregaci datových prvků { #how-to-edit-data-element-aggregation }

To se ovládá pomocí něčeho, co se nazývá agregační úrovně, a na konci obrazovky úpravy datových prvků je zaškrtávací políčko s názvem Úrovně agregace. Pokud zaškrtnete tuto možnost, zobrazí se seznam dostupných a vybraných úrovní agregace. Výchozí je, že nejsou definovány žádné úrovně agregace, pak budou všechna nezpracovaná data v hierarchii přidána dohromady. Chcete-li určit pravidlo popsané výše a vzhledem k hierarchii Země, Kraje, Okresu, Zařízení: vyberte jako úrovně agregace Zařízení a Okres. V zásadě si vyberete, kde máte data. Výběr zařízení znamená, že zařízení bude používat data ze zařízení (vzhledem k tomu, že se jedná o nejnižší úroveň). Výběr okresu znamená, že surová data na úrovni okresu budou použita při agregaci dat na úrovni okresu (proto na této úrovni nedojde k žádné agregaci) a data zařízení nebudou součástí agregovaných hodnot okresu. Při agregaci dat na úrovni Kraje se použijí prvotní data na úrovni okresu, protože se jedná o nejvyšší dostupnou agregační úroveň. Rovněž pro agregáty na úrovni země budou použita nezpracovaná data okresu. Jen pro zopakování, pokud bychom nespecifikovali, že úroveň okresu je agregační úrovní, pak by se údaje o zařízení a údaje o okresech sečetly dohromady a způsobily duplicitní (zdvojnásobení) údaje o populaci pro okresy a všechny výše uvedené úrovně.

### Zdrojové tabulky { #resource-tables }

Tabulky zdrojů poskytují další informace o rozměrech dat ve formátu, který je vhodný pro kombinaci externích nástrojů s tabulkou hodnot dat. Spojením tabulky hodnot dat s těmito tabulkami zdrojů lze snadno agregovat podél dimenze kategorie datových prvků nebo dimenzí datových prvků / indikátorů / skupin organizačních jednotek. Např. označením všech datových hodnot možností kategorie muž nebo žena a poskytnout to v samostatném sloupci 'pohlaví' lze získat mezisoučty mužů a žen na základě hodnot dat, které se shromažďují pro kombinace možností kategorie jako (muž, \<5) a (muž,\> 5) . V části Kontingenční tabulky najdete další příklady toho, jak je lze použít. Struktura organizačních jednotek je další důležitá tabulka v databázi, která pomáhá zajistit hierarchii organizačních jednotek spolu s daty. Spojením tabulky struktury organizačních jednotek s tabulkou datových hodnot můžete získat řádky datových hodnot s úplnou hierarchií, např. ve formuláři: OU1, OU2, OU3, OU4, DataElement, Period, Value (Sierra Leone, Bo, Badija, Ngelehun CHC, BCG \ <1, Jan-10, 32) Tento formát výrazně usnadňuje např. kontingenční tabulky nebo jiné nástroje OLAP pro agregaci dat v hierarchii.

### Zprávy tabulky { #reportTable }

Tabulky zpráv jsou definované zprávy s křížovými tabulkami, které lze použít jako základ pro další zprávy, jako jsou kontingenční tabulky aplikace Excel nebo jednoduše stáhnout jako list aplikace Excel. Účelem tabulek zpráv je poskytnout konkrétní pohled na požadovaná data, například „Měsíční národní ukazatele ANC“. Tato tabulka zpráv může poskytnout všechny ukazatele ANC pro zemi, agregované podle měsíce pro celou zemi. Tato data lze samozřejmě načíst z hlavního datamartu, ale tabulky sestav obecně fungují rychleji a uživatelům poskytují dobře definované pohledy na data.

## Jak vytvořit tabulky zpráv { #reporting_creating_tables }

Chcete-li vytvořit novou tabulku zpráv, přejděte do části Tabulky zpráv modulu Zprávy (Zprávy -\> Tabulka zpráv). Nad seznamem standardních zpráv použijte tlačítka „Přidat tabulku přehledu“ nebo „Přidat tabulku dimenzí datového prvku“. K uchování dat o datových prvcích, indikátorech nebo úplnosti datové sady lze použít běžnou tabulku sestav, zatímco tabulky dimenzí Dataelement se používají k zahrnutí kategorií datových prvků do tabulek sestav. Vytváření tabulek se provádí stejným způsobem, avšak jedinou výjimkou je výběr dat.

Chcete-li vytvořit tabulku sestav, začněte provedením několika obecných možností pro tabulku, z nichž nejdůležitější je dimenze křížové tabulky. Poté si vyberete, které datové prvky, indikátory, datové sady nebo dimenze datových prvků chcete zahrnout. Nakonec v tabulce sestav vyberete, které organizační jednotky a časová období se mají použít. Každý z těchto kroků je podrobně popsán níže.

### Obecné možnosti { #reporting_general_options }

![](resources/images/dhis2_creating_reporting/general_options.jpg)

**Dimenze křížové karty**

Můžete přepínat mezi tabulkami jednu nebo více z následujících dimenzí: datový prvek / indikátor, organizační jednotka a období, což znamená, že sloupce budou vytvářeny na základě hodnot vybraných dimenzí, např. pokud jsou vybrány indikátory, zobrazí se v tabulce názvy sloupců odrážející názvy vybraných indikátorů.

Pokud například provádíte křížovou kontrolu u indikátorů a období, v záhlavích sloupců bude uvedeno „\<indicator title\>\<period\>“. Organizační jednotky budou uvedeny jako řádky. Vysvětlení viz screenshot:

![](resources/images/dhis2_creating_reporting/crosstab_ind-per.jpg)

Pokud přepnete mezi indikátory a organizačními jednotkami, bude v záhlaví sloupce tabulky uvedeno "\<indicator title\>\<organisation unit\>“. Období budou nyní uvedeny jako řádky. Vysvětlení viz screenshot:

![](resources/images/dhis2_creating_reporting/crosstab_ind-org.jpg)

Všimněte si, že zde provedené možnosti týkající se dimenzí kontingenčních tabulek mohou mít důsledky pro to, jaké možnosti jsou k dispozici při pozdějším použití tabulky sestav jako zdroje dat, například pro standardní sestavy.

**Pořadí řazení**

Ovlivňuje sloupec zcela vpravo v tabulce, umožňuje zvolit řazení od nejnižší k nejvyšší nebo nejvyšší k nejnižší.

**Horní limit**

Horní limit umožňuje nastavit maximální počet řádků, které chcete zahrnout do tabulky hlášení.

**Zahrnout regresi**

Tím se přidají další sloupce s regresními hodnotami, které lze zahrnout do návrhu hlášení, např. v řádkových grafech.

### Výběr dat { #reporting_selecting_data }

![](resources/images/dhis2_creating_reporting/select_data.jpg)

**Indikátory / datové prvky**

Zde vyberete datové prvky / indikátory, které chcete zahrnout do sestavy. Pomocí skupinového filtru můžete snáze najít to, co hledáte, a dvakrát kliknout na položky, které chcete zahrnout, nebo pomocí tlačítek přidat / odebrat prvky. Ve stejné sestavě můžete mít datové prvky i indikátory.

**Datové sady**

Zde vyberete datové sady, které chcete zahrnout do sestavy. Zahrnutí datové sady vám poskytne data o úplnosti dat dané sady, nikoli data o jejích datových prvcích. Poklepejte na položky, které chcete zahrnout, nebo použijte tlačítka.

### Výběr parametrů sestavy { #selecting_reporting_params }

![](resources/images/dhis2_creating_reporting/relative_options.jpg)

Existují dva způsoby, jak vybrat organizační jednotky, které mají být zahrnuty do sestavy, a jaká časová období by měla být zahrnuta: relativní nebo pevná. Pevné organizační jednotky a / nebo období znamená, že při vytváření tabulky sestav vyberete jednotky / období, která chcete zahrnout do tabulky sestav. Pomocí relativních období můžete vybrat čas a / nebo jednotky jako parametry při naplnění tabulky sestavy, například při spuštění standardní sestavy nebo vytváření grafu. Je také možná kombinace, například přidat do sestavy některé organizační jednotky trvale a nechat uživatele, aby si vybrali další. Níže jsou popsány parametry zprávy. Obecně platí, že používání pevných organizačních jednotek a / nebo časových období je zbytečným omezením.

**Pevné organizační jednotky**

Chcete-li přidat pevné organizační jednotky, klikněte na „Přepnout pevné organizační jednotky“. Zobrazí se panel, kde si můžete vybrat organizační jednotky, které chcete vždy zahrnout do hlášení. Pokud ponecháte toto pole prázdné, uživatelé při spuštění hlášení pomocí použití parametrů hlášení vyberou organizační jednotky. Pomocí rozevírací nabídky můžete filtrovat organizační jednotky podle úrovně, dvakrát na ně kliknout nebo pomocí tlačítek přidat / odebrat.

**Pevná období**

Chcete-li přidat pevná období, klikněte na „Přepnout pevné organizační jednotky“. Zobrazí se panel, kde si můžete vybrat období, která chcete vždy zahrnout do hlášení. Necháte-li toto pole prázdné, uživatelé vyberou období při spuštění hlášení pomocí parametrů hlášení. Pomocí rozevírací nabídky vyberte typ období (týden, měsíc atd.), Pomocí tlačítek Předchozí a Další vyberte rok a poklepejte nebo pomocí tlačítek přidat / odebrat.

**Relativní období**

Místo použití pevných / statických období jako 'Jan-2010' nebo 'Q1-2010', lze k vytvoření opakovaně použitelných tabulek hlášení použít obecnější období. u měsíčních přehledů období „Měsíc hlášení“ jednoduše vybere aktuální měsíc hlášení vybraný uživatelem při spuštění přehledu. Všimněte si, že všechna relativní období jsou relativní k „vykazovanému měsíci“. Měsíc hlášení je buď vybrán uživateli, jinak je použit aktuální měsíc. Zde je popis možných relativních období:

-   _Měsíc hlášení:_

    Použijte pro měsíční přehledy. V sestavě bude použit měsíc vybraný v parametru měsíce hlášení.

-   _Měsíce / čtvrtletí letos_:

    To poskytne jednu hodnotu za měsíc nebo čtvrtletí v roce. To se dobře hodí pro standardní měsíční nebo čtvrtletní zprávy, kde je třeba uvést všechny měsíce / čtvrtletí. Období, která stále nemají žádná data, budou prázdná, ale vždy si zachovají stejný název sloupce.

-   _Tento rok:_

    Jedná se o kumulativní výsledek v daném roce, který agreguje období od začátku roku do a včetně vybraného vykazovaného měsíce.

-   _Měsíce / čtvrtletí minulý rok_:

    To poskytne jednu hodnotu za měsíc nebo za čtvrtletí loňského roku, ve srovnání s vykazovaným měsícem. To se dobře hodí pro standardní měsíční nebo čtvrtletní zprávy, kde je třeba uvést všechny měsíce / čtvrtletí. Období, která stále nemají žádná data, budou prázdná, ale vždy si zachovají stejný název sloupce.

-   _Minulý rok:_

    Jedná se o kumulativní loňský rok ve srovnání s vykazovaným měsícem, který agreguje všechna období z minulého roku.

**Příklad - relativní období**

Řekněme, že jsme vybrali tři ukazatele: A, B a C a při vytváření tabulky zprávy jsme se také rozhodli použít relativní období „Měsíc hlášení“ a „Tento rok“. Pokud je vykazovaným měsícem (vybraným automaticky nebo uživatelem) například květen 2010, v tabulce přehledu se vypočítají hodnoty pro tři vybrané ukazatele za květen 2010 (= „vykazovaný měsíc“) a kumulované hodnoty pro tři vybrané ukazatele zatím v roce 2010 (= zatím „letos“).

U každé z organizačních jednotek tedy skončíme se šesti hodnotami: „Ukazatel A květen 2010“, „Ukazatel B květen 2010“ „Ukazatel C květen 2010“, „Ukazatel A dosud v roce 2010“, „Ukazatel B dosud v roce 2010 “a„ indikátor C dosud v roce 2010 “.

**Parametry hlášení**

Díky parametrům hlášení jsou hlášení obecnější a opakovaně použitelné v čase a pro různé organizační jednotky. Tyto parametry se zobrazí při generování tabulky zpráv nebo spuštění hlášení založené na tabulce zpráv. Uživatelé si vyberou, co chtějí v přehledu vidět. Existují čtyři možné parametry hlášení a můžete vybrat žádný, všechny nebo libovolnou kombinaci.

-   _Měsíc hlášení:_

    To rozhoduje o tom, který měsíc bude použit, když systém vybírá relativní období. Pokud políčko není zaškrtnuto, uživatel nebude při generování zprávy požádán o vykazovaný měsíc - poté bude použit aktuální měsíc.

-   _Hlavní nadřazená organizační jednotka:_

    Vyberte hlavní nadřazené všech podřazených organizačních jednotek a jejich podřazených, které chcete v přehledu uvést. Např. vybraný region spustí použití samotného regionu, celého jeho okresu a všech jejich podoblastí.

-   _Nadřazená organizační jednotka:_

    Vyberte nadřazené všech podřazených organizačních jednotek, které chcete v přehledu uvést. Např. vybraný okres spustí použití samotného okresu a všech jeho podřazených / podoblastí.

-   _Organizační jednotka:_

    Tím se v přehledu spustí použití této organizační jednotky. Nejsou uvedeny žádné podřazené.

**Příklad - parametry sestavy**

Pokračujeme příkladem v relativních obdobích výše, řekněme, že kromě „měsíce hlášení“ jsme při vytváření tabulky hlášení vybrali jako parametr hlášení „Nadřazená organizační jednotka“. Když spouštíme tabulku hlášení, budeme vyzváni k výběru organizační jednotky. Řekněme, že jsme jako organizační jednotku vybrali „Region R“. „Region R“ má podřazené „okres X“ a „okres Y“.

Když je hlášení spuštěno, systém agreguje data pro „Okres X“ a „Okres Y“. Data budou agregována od nejnižší úrovně, kde byla shromážděna. Hodnoty pro okresy budou dále agregovány, aby poskytly agregovanou hodnotu pro „Region R“.

Tabulka sestavy tedy vygeneruje šest hodnot uvedených v předchozím příkladu pro „Okres X“, „Okres Y“ a „Region R“.

### Tabulky dimenzí datových prvků { #reporting_de_dimension_tables }

Tyto tabulky umožňují použití kategorií datových prvků v tabulkách sestav. Od tabulek běžných sestav existují dva rozdíly. První je, že není možné vybrat dimenze kontingenčních tabulek, protože ve sloupcích budou vždy disagregace z kombinací kategorií. Druhým je skutečný výběr dat. Do každé sestavy lze přidat pouze jednu kombinaci kategorií a lze vybrat pouze datové prvky ze stejné kombinace kategorií.

Mezisoučty a součet budou také zahrnuty v tabulce, např. kombinace pohlaví (muž, žena) + EPI age(\<1, \>1) by poskytla následující sloupce: male+\<1, male+\>1, Female+\<1, female+\>1, male, female,\<1, \>1, total.

**Výběr dat**

![](resources/images/dhis2_creating_reporting/catcombo.jpg)

Pomocí rozevírací nabídky vyberte kombinace kategorií. Budou uvedeny datové prvky využívající tuto kombinaci kategorií. Poklepáním přidáte do přehledu nebo použijte tlačítka.

### Tabulka zpráv - osvědčené postupy { #reporting_best_practices }

Aby tabulky přehledů byly opakovaně použitelné v průběhu času a napříč organizacemi, mohou mít parametry. Jsou povoleny čtyři typy parametrů; organizační jednotky, nadřazená organizační jednotka (pro výpis organizačních jednotek v jedné oblasti), nadřazená organizační jednotka a vykazovaný měsíc. Jako vedlejší poznámku je možné zmínit, že se snažíme toto rozšíření rozšířit o čtvrtletí a rok vykazování, nebo o to, aby byl parametr období obecnější s ohledem na typ období. Schopnost použít období jako parametr umožňuje opakovaně použitelnou tabulku zpráv v průběhu času a jako taková dobře zapadá do potřeb zpráv, jako jsou měsíční, čtvrtletní nebo roční zprávy. Když uživatel spustí sestavu v DHIS2, musí uživatel zadat hodnoty pro tabulky zpráv, které jsou s tímto hlášením propojeny. Nejprve se znovu vygeneruje tabulka zprávy (odstraní se a znovu se vytvoří s aktualizovanými daty) a poté se hlášení spustí (na pozadí, v engine Jasper).

Tabulky hlášení se mohou skládat z hodnot vztahujících se k datovým prvkům, indikátorům nebo úplnosti dat, což souvisí s úplností vykazování napříč organizacemi za daný měsíc. Zprávy o úplnosti budou popsány v samostatné části.

V tabulce hlášení zpráv jsou tři dimenze, které identifikují data; indikátory nebo datové prvky, organizace a období. Pro každou z těchto dimenzí může uživatel vybrat, které hodnoty metadat zahrnout do hlášení. Uživatel musí vybrat jeden nebo více datových prvků nebo indikátorů, které se mají zobrazit v hlášení. Výběr organizační jednotky lze nahradit parametrem, a to buď konkrétní organizační jednotkou, nebo nadřazenou organizační jednotkou (v sestavě se objeví samostatně a všechny její podřízené položky). Pokud je vybrána jedna, nebo více organizačních jednotek a nepoužívá se žádný parametr organizační jednotky, je hlášení zprávy statické s ohledem na to, které organizační jednotky mají být zahrnuty, což je ve většině případů zbytečné omezení pro hlášení zprávy.

**Používání relativních období**

Výběr období je pokročilejší, protože kromě konkrétních období jako Jan-09, Q1-08, 2007 obsahuje i tzv. Relativní období. Protože se zpráva obvykle spouští rutinně v průběhu času, konkrétní období jako Jan-09 není v sestavě příliš užitečné. Místo toho, pokud chcete navrhnout měsíční zprávu, měli byste použít relativní období zvané měsíc hlášení. Potom musíte také zahrnout měsíc hlášení jako jeden z parametrů hlášení, abyste systému dali vědět, co přesně je měsíc hlášení v době generování hlášení. K dispozici je mnoho dalších relativních období a všechna se vztahují k parametru sestavy měsíc hlášení. Např. relativní období nazvané Za tento rok, označuje kumulativní hodnotu za rok vč. vykazovaný měsíc. Pokud chcete přehled trendů s více obdobími namísto jednoho agregovaného období, můžete vybrat např. „měsíce v tomto roce“, které vám poskytnou hodnoty pro každý měsíc v daném roce. Podobnou zprávu můžete udělat se čtvrtletími Cílem je podpořit co nejvíce obecných typů hlášení pomocí relativních období, takže pokud máte jiné potřeby v hlášeních, navrhněte v seznamu adres nová relativní období a mohou být přidána do možností tabulky hlášení.

**Dimenze křížové karty**

Křížová tabulka je velmi výkonná funkce v designu hlášení, protože typická datová tabulka DHIS2 s odkazy na období, datový prvek / indikátor a organizační jednotku velmi ztěžuje pokročilejší design hlášení, protože nemůžete dát např. konkrétní ukazatele, období nebo organizace na konkrétních sloupcích. Např. křížovou tabulkou dimenze indikátoru v tabulce zpráv indikátorů získáte názvy indikátorů v záhlavích sloupců v hlášení, kromě sloupce odkazujícího na organizační jednotku a dalšího období odkazujícího na sloupec. S takovým designem tabulky můžete přetahovat názvy indikátorů do konkrétních sloupců nebo pozic grafů v softwaru iReport. Podobně můžete procházet záložky na organizačních jednotkách nebo bodech, aby jejich názvy byly konkrétně dostupné pro návrh hlášení. Např. křížovým procházením období a výběrem dvou relativních období „měsíc hlášení“ a „Tento rok“ můžete navrhovat hlášení s posledním měsícem a kumulativní roční hodnotou pro daný měsíc, protože budou k dispozici jako záhlaví sloupců v přehledu tabulky. Je také možné kombinovat dva rozměry v křížových tabulkách, např. období a indikátor, který umožňuje např. podívat se na tři vybrané ukazatele pro dvě konkrétní relativní období. To by např. umožňují vytvořit tabulkovou nebo grafovou zprávu s pokrytím BCG, DPT3 a spalničkami, a to jak za poslední měsíc, tak kumulativní pokrytí doposud v roce.

Celkově lze říci, že kombinací funkcí křížových tabulátorů, relativních období a parametrů tabulky sestavy byste měli mít nástroj na podporu většiny scénářů hlášení. Pokud ne, rádi bychom obdrželi návrhy na další vylepšení tabulek zpráv. Jak již bylo zmíněno, začali jsme se zabývat jemnějšími parametry pro dimenzi období, protože „Měsíc hlášení“ nepokrývá dostatečně, nebo alespoň není dostatečně intuitivní, pokud jde o např. čtvrtletní zprávy.

## Hlášení výsledku tabulky { #reporting_table_outcomes }

Když je spuštěna tabulka hlášení zpráv, systém vypočítá hodnoty pro konkrétní indikátory / datové prvky / datové sady, organizační jednotky a období. Data budou prezentována v DHIS2 v rozložení tabulky. Záhlaví sloupců budou odpovídat dimenzi křížových karet, kterou jste vybrali. Níže je uvedena ukázková tabulka hlášení zpráv ukazující pokrytí ANC pro okres v Gambii. Zde jsou indikátory a tečky křížově umístěné na kartách, jak je patrné ze záhlaví sloupců.

![](resources/images/dhis2_creating_reporting/crosstab_ind-per.jpg)

Nad tabulkou je šest tlačítek; pět tlačítek pro stahování a jedno tlačítko Zpět. Kliknutím na tlačítko Zpět se jednoduše vrátíte zpět na předchozí obrazovku. Funkce pěti tlačítek pro stahování je uvedena pod snímkem obrazovky:

![](resources/images/dhis2_creating_reporting/report-table_output.png)

**Pět tlačítek pro stahování**

-   _Stáhnout jako Excel:_

    Stáhne vygenerovaný soubor aplikace Excel, který můžete otevřít v aplikaci Excel.

-   _Stáhnout jako CSV:_

    Stáhne vygenerovaný soubor .csv. CSV znamená **C**omma **S**eparated **V**alues. Je to textový soubor s příponou .csv. Každý řádek v souboru odpovídá jednomu řádku v tabulce, zatímco sloupce jsou odděleny středníky (;). Soubor lze otevřít v textovém editoru i v programu tabulkového procesoru (například Excel).

-   _Stáhnout jako PDF:_

    Stáhne vygenerovaný soubor PDF. Data budou prezentována v podobném rozvržení jako vygenerovaná tabulka, kterou již prohlížíte v DHIS2.

-   _Stáhnout jako zprávu:_

    Stáhne „stylizovaný“ soubor PDF. Kromě prezentace dat v rozložení tabulky tento soubor také představuje graf, který zobrazuje agregovaná data ze všech vybraných období a nadřazené organizační jednotky vybrané pro tabulku sestavy. Zpráva je generována pomocí modulu zpráv Jasper.

-   _Stáhnout jako JRXML:_

    Stáhne soubor návrhu pro vygenerovaný Report popsaný v předchozí odrážce. Soubor návrhu (s příponou .jrxml) lze otevřít v softwaru Jasper iReport Designer. Pokud plánujete navrhovat standardní zprávy, je to výchozí bod.

## Standardní zprávy { #reporting_standard_reports }

### Co je standardní zpráva? { #what-is-a-standard-report }

Standardní hlášení je ručně vytvořená zpráva, která prezentuje data v ručně určeném rozvržení. Standardní hlášení zpráv mohou být založeny na tabulkách hlášení nebo dotazech SQL. Oba přístupy jsou popsány v následujících částech. Hlavní výhodou použití tabulek hlášení je jednoduchost - nejsou vyžadovány žádné speciální vývojové dovednosti. V případech, kdy máte zvláštní požadavky nebo potřebujete využít další části databáze DHIS2, můžete použít standardní zprávu založenou na SQL. V každém případě budete moci využít parametry reportu k vytváření dynamických reportů. Následující průvodce použije přístup k tabulce hlášení, zatímco přístup SQL je vysvětlen ke konci.

### Navrhování standardních zpráv v iReportu { #designing-standard-reports-in-ireport }

Jasper iReport Designer je nástroj pro vytváření zpráv, které lze v DHIS2 použít jako standardní zprávy. Tento nástroj umožňuje vytváření standardních šablon zpráv, které lze snadno exportovat z DHIS2 s aktuálními daty. Proces vytváření hlášení zpráv zahrnuje čtyři hlavní kroky:

1.  V protokolu DHIS2 musí být vytvořena tabulka zpráv s indikátory / datovými prvky / datovými sadami, které mají být v hlášení zpráv použity.

2.  Musíte spustit tabulku zpráv a stáhnout soubor návrhu (klikněte na tlačítko „Stáhnout jako JRXML“).

3.  Otevřete stažený soubor .jrxml pomocí bezplatného softwaru Jasper iReport Designer a upravte rozložení sestavy.

4.  Upravenou zprávu lze poté nahrát do DHIS2 a použít ji jako standardní zprávu.

Chcete-li zobrazit náhled hlášení zprávy během návrhu v iReportu, musíte skutečně nahrát soubor do DHIS2, abyste viděli, jak vypadá.

Tyto čtyři kroky budou podrobně popsány v následujících částech. Obecně platí, že když vytváříte standardní hlášení zprávy, měli byste mít jasnou představu o tom, jak by to mělo vypadat, než dokonce vytvoříte tabulku hlášení, protože to, jak je tabulka hlášení navržena, má důsledky pro to, jak lze hlášení formátovat v iReportu. Například to, jaké dimenze kontingenčních tabulek jsou vybrány v tabulce hlášení, má důsledky pro to, jaké kontingenční tabulky jsou k dispozici pro standardní hlášení, a má důsledky pro to, jaké typy grafů můžete vytvořit.

#### Stáhněte a otevřete návrhový soubor { #download-and-open-the-design-file }

> **POZNÁMKA**
>
> Pokud jste ještě nevytvořili tabulku hlášení, musíte tak učinit. Viz část "Jak vytvořit tabulky hlášení".\*

Vyhledejte požadovanou tabulku přehledů a spusťte ji kliknutím na zelený kruh s bílou šipkou uvnitř. Když se zobrazí zpráva, stáhněte soubor návrhu kliknutím na tlačítko „Stáhnout jako JRXML“. Poté tento soubor otevřete v softwaru Jasper iReport Designer.

#### Úprava hlášení zprávy { #editing-the-report }

Nyní jste připraveni upravit rozložení hlášení. Hlavní okno iReport se skládá z „Inspektoru zprávy“ nalevo, dokumentu se zprávou uprostřed, z oblasti „Paleta“ na pravé horní straně a z „Vlastnosti“ na pravé dolní straně. "Inspektor zprávy" se používá k výběru a zkoumání různých vlastností zprávy a při výběru položky v inspektoru se panel "Vlastnosti" změní na vlastnosti zobrazení týkající se výběru. "Paleta" se používá pro přidávání různých prvků, např. textová pole, obrázky a grafy k dokumentu.

![](resources/images/dhis2_creating_reporting/ireport/iReport-window.png)

> **POZNÁMKA**
>
> Pokud nevidíte postranní panel Paleta nebo Vlastnosti, můžete je povolit pomocí položky nabídky „Okno“ na panelu nabídek.

Dokument iReport je rozdělen do sedmi hlavních pruhů rozdělených oddělovači rozložení (modré čáry). Tyto řádky se používají k rozhodnutí, jak velká by každá z oblastí měla být v hlášení zprávy.

Všechny oblasti mají různé účely:

-   Nadpis - oblast názvu zprávy

-   Záhlaví stránky - oblast pro záhlaví stránky

-   Záhlaví sloupce - oblast pro záhlaví sloupců (pro tabulku)

-   Detail 1 - oblast, kde budou umístěna data aktuální zprávy

-   Zápatí sloupce - oblast pro vytvoření zápatí tabulky

-   Zápatí stránky - oblast pro zápatí stránky

-   Shrnutí - prvky v této oblasti budou umístěny na konec zprávy

Ve výchozím nastavení uvidíte, že data mají pouze pruhy Název, Záhlaví sloupce a Detail 1. U většiny zpráv je to v pořádku. Pruh nadpisu je vhodné pro titul a např. graf. Datová pole zadaná do oblasti Detail 1 budou iterována, aby vytvořila tabulku. Například pokud je pole s názvem "dataelementname" umístěno v pruhu Detail 1, budou zde uvedeny všechny datové prvky v tabulce hlášení. O něco níže se vrátíme ke správě datových polí.

Nevyužité pruhy v hlášení jsou zkráceny, aby se přidal další prostor pro data hlášení. Výšku pruhu však můžete libovolně zvyšovat / snižovat. Existují dva způsoby, jak toho dosáhnout. První způsob je jednoduše přetáhnout modrou pásku, jak je znázorněno níže.

![](resources/images/dhis2_creating_reporting/ireport/17_drag.jpg)

Druhým způsobem, jak upravit výšku pruhu, je vybrat pruh v „Inspektoru zprávy“ a poté upravit hodnotu „Výška pruhu“ v oblasti „Detail 1 - vlastnosti“ v pravém dolním rohu.

![](resources/images/dhis2_creating_reporting/ireport/18_adjust.jpg)

Protože pole jsou již v sestavě přítomna, pravděpodobně nebudete chtít dělat nic jiného, než jen opravit rozložení a přetáhnout pole. Můžete také změnit velikost polí přetažením postranních, horních nebo dolních čar. Chcete-li změnit text v záhlavích sloupců, jednoduše dvakrát klikněte na pole a text změňte.

Chcete-li přidat pole do tabulky, jednoduše jej přetáhněte do pruhu Detail 1 z "Inspektoru zprávy". Záhlaví sloupce bude přidáno automaticky.

Poklepáním na pole lze text upravit. Formát textu, například velikost, písmo a zarovnání, lze upravit pomocí nástrojů nad dokumentem.

![](resources/images/dhis2_creating_reporting/ireport/21_title_edit.jpg)

> **POZNÁMKA**
>
> Pole začínající na "$F" představují hodnoty, které jsou načteny z databáze při každém spuštění sestavy. Hodnoty se zde budou lišit, takže tato pole neměňte, pokud zde nechcete statickou hodnotu!

#### Text { #text }

V iReportu existují dva typy textu: «Textové štítky» a «Textová pole» (datová pole). Fungují různými způsoby a měly by být použity pro různé účely. Hlavním bodem je, že textová pole jsou pouze zástupné symboly, které budou při spuštění sestavy vyplněny správným textem z tabulky sestavy, zatímco textové štítky zůstanou stejné, jaké jsou při spuštění sestavy.

##### Statický text { #static-text }

Statický text jsou popisky prostého textu, které lze normálně upravovat. Existují dva způsoby, jak upravit textové štítky:

-   Poklepáním do textového pole

-   Pomocí vlastností statického textu v panelu Vlastnosti

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_01.jpg)

##### Textová pole { #text-fields }

Textová pole jsou vzorce, které se vyplní z tabulky sestavy při spuštění sestavy. Na rozdíl od statického textu je nelze běžným způsobem upravovat. Lze s nimi však manipulovat různými způsoby, aby bylo zajištěno, že bude vytvořen požadovaný výstup. Existují tři způsoby, jak upravit textová pole:

-   Klikněte pravým tlačítkem na textové pole a vyberte Upravit výraz

-   Poklepáním na textové pole (nedoporučuje se, protože se tím nespustí editor výrazů)

-   Pomocí vlastností textového pole na panelu Vlastnosti

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_04.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_06.jpg)

Textová pole mohou představovat buď čísla, nebo text, takže je lze použít jak pro zobrazení například názvů okresů, tak pro číselné hodnoty. Je proto důležité, aby se třída Expression, která je vidět ve vlastnostech textového pole, shodovala s výrazem textového pole. Pro výchozí textová pole v souboru .jrxml staženém z DHIS2 to není problém, ale je to důležité při vytváření nových textových polí. Dvě nejdůležitější třídy výrazů jsou java.lang.Double pro čísla a java.lang.String pro text.

###### Příklad { #example }

Řekněme například, že máte čtvrtletní přehled, do kterého chcete přidat nový sloupec s ročním součtem. Proto přidáte nové statické textové pole do pásma záhlaví sloupce a textové pole do pásma podrobností. Ve výchozím nastavení jsou nová textová pole nastavena na java.lang.String (text). Sloupec ročního součtu však bude vyplněn čísly. Proto musíme změnit třídu Expression pro nové textové pole na java.lang.Double:

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_07.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_08.jpg)

Když upravujeme výraz textového pole, vidíme okno editoru výrazů se všemi dostupnými sloupci z tabulky sestavy. Vidíme zde, že každý z nich je označen tím, o jaký typ jde - text nebo číslo. Musíme se tedy ujistit, že třída výrazů, kterou zvolíme pro textové pole, odpovídá skutečnému výrazu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_10.jpg)

### Filtrování řádků tabulky { #filtering-the-table-rows }

Ve výchozí tabulce exportované z DHIS2 jsou některé řádky, které by bylo lepší vynechat z tabulky, a některé, které by bylo lepší mít na konci. Například při vytváření tabulky založené na tabulce zpráv s parametrem «nadřazená organizační jednotka» může mít výchozí tabulka řádek s národní úrovní někde mezi všemi regiony. V iReportu to lze změnit tak, aby se ve spodní části tabulky zobrazila «nadřazená organizační jednotka». Jedná se o dva kroky, které budou vysvětleny níže. Upozorňujeme, že toto nebude fungovat, pokud existuje pouze jedna organizační jednotka, a proto je nejužitečnější při použití parametrů «nadřazená organizační jednotka» nebo «hlavní nadřazená organizační jednotka» v tabulce sestavy.

#### Skrytí «parametrické organizační jednotky» z tabulky { #hiding-the-parameter-organisation-unit-from-the-table }

„parametr Organizační jednotky“ vylučujeme z tabulky pomocí vlastnosti v pásmu Podrobnosti s názvem „Tisknout při výrazu“. Chcete-li nastavit výraz Print when, začněte výběrem pásma Detail v inspektoru Zpráv a potom upravte výraz Print when expression v panelu vlastností.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_11.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_12.jpg)

Nyní by se mělo zobrazit okno editoru výrazů. Musíme udělat, abychom vytvořili výraz, který zkontroluje, zda generovaný řádek je řádek s organizační jednotkou zadanou jako parametr. Tabulka sestavy obsahuje sloupec, který můžeme pro tento účel použít, nazvaný organisation_unit_is_parent. Chcete-li vyloučit řádek s organizační jednotkou parametrů, poklepejte na organisation_unit_is_parent v seznamu a zkopírujte jej do oblasti výrazu, poté na konec přidejte `.equals("No")` aby kód byl:

```
$F{organisation_unit_is_parent}.equals("No")
```

To řekne stroji na produkování hlášení, aby tiskl pouze řádky tabulky, kde organizační jednotka není nadřazenou organizační jednotkou.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_14.jpg)

#### Ve spodní části tabulky je uvedena „param organizační jednotka“ { #putting-the-param-organisation-unit-at-the-bottom-of-the-table }

Místo úplného odebrání „organizační jednotky param“ z tabulky je také možné umístit ji na spodní (nebo horní) část tabulky. To se provádí pomocí funkce třídění vysvětlené v následující části a výběrem nejprve seřadit podle „organisation_unit_is_parent“. Kromě toho lze přidat další možnosti řazení, například pro vytvoření seznamu, kde je organizační jednotka param ve spodní části tabulky a nad ní jsou abecedně uvedeny další organizační jednotky.

#### Skrytí dalších řádků { #hiding-other-rows }

Pomocí editoru výrazů je také možné vyloučit z tabulky další řádky kromě nadřazené organizační jednotky, jak bylo vysvětleno výše. Například v Ghaně mají všechny regiony «falešný okres», což je název regionu v hranatých závorkách. To lze také vyloučit z tabulky pomocí příkazu Print when, který byl zaveden výše. Chcete-li to provést, zobrazte okno editoru výrazů podle výše uvedených pokynů. Poté pomocí výrazů Java otestujeme, zda má být řádek skryt.

##### Příklad - odstranění řádků s organizačními jednotkami začínajícími \[ { #example-removing-rows-with-organisation-units-starting-with }

Příklad - odstranění řádků s organizačními jednotkami začínajícími \[

```
($F{organisationunitname}.charAt( 0 ) != '[')
```

Díky tomu sestava přeskočí všechny řádky, kde je první znak názvu organizační jednotky \[.

Je také možné kombinovat několik z těchto výrazů. K tomu vložíme výrazy do závorek se dvěma znaky && mezi nimi. Například k vytvoření tabulky, která ponechá obě organizační jednotky, jejichž název začíná na \[, a nadřazenou organizační jednotku, můžeme použít následující výraz:

```
($F{organisationunitname}.charAt( 0 ) != '[')&&$F{organisation_unit_is_parent}.equals("No")
```

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_29.jpg)

### Řazení { #sorting }

Často budete vytvářet sestavy, kde v prvním sloupci jsou názvy organizačních jednotek. Může však být problém, že seznam organizačních jednotek není seřazen abecedně. To lze opravit v iReportu několika jednoduchými kroky.

V inspektoru zpráv klikněte pravým tlačítkem na název zprávy (ve výchozím nastavení je to dpt) a vyberte Upravit dotaz.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_21.jpg)

Objeví se okno dotaz Zprávy. Klikněte na tlačítko Možnosti řazení.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_22.jpg)

Zobrazí se okno řazení, jak je uvedeno níže. Zde můžeme přidat naše možnosti řazení. Klikněte na tlačítko Přidat pole. Zobrazí se další malé okno s rozevírací nabídkou, kde můžete vybrat možnost Seřadit podle názvu organizace podle toho, zda má být tabulka seřazena podle názvu podle abecedy.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_23.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_24.jpg)

Kliknutím na OK - Zavřít - OK zavřete tři okna. Tabulka by nyní měla být tříděna.

### Změna názvů indikátorů / datových prvků { #changing-indicatordata-element-names }

Ve výchozím nastavení používají sestavy z DHIS2 krátké názvy indikátorů a datových prvků v sestavách a grafech. V některých případech nejsou pro třetí strany zrovna smysluplné, ale u některých prací jim mohou být prostřednictvím iReportu přidělena vlastní jména. To je užitečné například v případě, že vytváříte přehled s indikátory jako řádky a období jako sloupec, nebo pro grafy s indikátory.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_000.jpg)

Chcete-li změnit názvy indikátoru nebo datového prvku, musíme upravit jeho «výraz» nebo vzorec, například kliknutím pravým tlačítkem na textové pole a výběrem možnosti Upravit výraz vyvoláte editor výrazů.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_32.jpg)

Dále musíme vložit nějaký Java kód. V následujícím příkladu nahradíme krátký název tří indikátorů jejich vlastními názvy. Kód vyhledá krátký název a poté jej nahradí vlastním jménem.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_34.jpg)

```
($F{indicatorname}.equals("Bed Util All")) ? "Bed Utilisation - All Wards"
:
($F{indicatorname}.equals("Bed Util Mat")) ? "Bed Utilisation - Maternity"
:
($F{indicatorname}.equals("Bed Util Ped")) ? "Bed Utilisation - Paediatric"
:
$F{indicatorname}
```

Z toho vidíme vzor, který je opakovaně použitelný pro obecnější případy.

-   Pro každý indikátor nebo datový prvek, pro který chceme změnit název, potřebujeme jeden řádek

-   Každý řádek je oddělen dvojtečkou :

-   Dokončíme výraz s «pravidelným» řádkem

Každý řádek má stejný formát, kde červený text je zkratka, modrý text je místo toho, co chceme vložit.

![](resources/images/dhis2_creating_reporting/ireportadv/ireport_screen_0.jpg)

Stejné výrazy lze použít například při názvech indikátorů podél osy kategorie grafu.

### Sčítání vodorovných součtů { #adding-horizontal-totals }

Pomocí editoru výrazů je možné do tabulky přidat sloupec se součty pro každý řádek. V následujícím příkladu vytvoříme tabulku se třemi měsíci jako sloupce a také sloupec se součty za tři měsíce.

Začneme přetažením textového štítku do záhlaví tabulky a změnou jeho textu na „Celkem“ a přetažením textového pole do řádku podrobností.

Jak bylo popsáno v části „Textové pole“, musíme změnit vlastnosti nového textového pole, aby bylo možné zobrazit čísla. Chcete-li to provést, změňte „Třídu výrazů“ v panelu vlastností na „java.lang.Double“.

Klikněte pravým tlačítkem na textové pole a vyberte možnost „Upravit výraz“. Zobrazí se editor výrazů. Jako výraz chceme shrnout všechny sloupce. V tomto případě máme tři hodnotové výrazy, které chceme shrnout: „září“, „říjen 2010“, „listopad 2010“. Název těchto polí se bude lišit v závislosti na dimenzi křížové tabulky, kterou jste vybrali v tabulce přehledů. V našem případě je výraz, který děláme

```
$f{September}+$f{October 2010}+$f{November 2010}
```

Každý řádek tabulky bude mít sloupec součty vpravo.

### Skupiny tabulek { #groups-of-tables }

Existují případy, kdy může být užitečné mít v jedné sestavě několik tabulek. To lze provést pomocí skupin zpráv. Pomocí této funkce lze například vytvořit sestavu jednu tabulku pro každý indikátor nebo jednu tabulku každé organizační jednotky. V následujícím textu projdeme kroky potřebné k vytvoření zprávy se třemi indikátory, z nichž každý je uveden v jedné tabulce. Je důležité, aby tabulka sestavy nebyla porovnána s indikátory, když chceme vytvořit skupiny tabulek na základě indikátorů.

V našem příkladu bude mít soubor .jrxml stažený z DHIS2 ve výchozím nastavení jeden sloupec pro organizační jednotku a pro indikátory (za předpokladu, že jsme jako jedinou dimenzi křížové tabulky vybrali období). Začneme odstraněním sloupce indikátoru, protože to v našem případě není nutné, a znovu zarovnáme další pole tak, aby se vešly do sestavy.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_36.jpg)

Dále vytvoříme skupinu Report. Přejděte na inspektora zpráv, klikněte pravým tlačítkem na název zprávy (výchozí je dpt) a zvolte Přidat skupinu zpráv.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_38.jpg)

Zobrazí se okno s průvodcem skupinou sestav. Vyberte název skupiny, v tomto případě zvolíme «Indikátor». V rozevírací nabídce můžeme vybrat, ze kterých sloupců v tabulce sestavy chceme, aby byly skupiny založeny. Pokud bychom tedy chtěli jednu tabulku pro každou organizační jednotku, vybrali bychom název organizační jednotky jako objekt sestavy, do kterého se seskupí. Jelikož se ale v tomto příkladu seskupujeme podle indikátorů, zvolili jsme si indikátor. Poté klikněte na další.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_39.jpg)

Dalším krokem je výběr, zda chceme pro každou skupinu sestav samostatné záhlaví skupiny a pásmo zápatí skupiny. V tomto případě jsme se rozhodli zahrnout obojí. Klikněte na Dokončit a skupiny skupin by se měly objevit v sestavě.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_40.jpg)

Pokud nahrajete a spustíte přehled, vytvoří se pro každý indikátor jedna tabulka. Nebude to však vypadat moc dobře, protože nad každou tabulkou nebude žádný řádek záhlaví - pouze jedna záhlaví v horní části každé stránky. Rovněž neexistuje žádný údaj o tom, která tabulka ukazuje, který indikátor. V následujícím textu to opravíme.

Místo toho, abychom měli v záhlaví sloupce řádek s nadpisem, můžeme jej místo toho přesunout do záhlaví skupiny. Tím se nadpis zobrazí nad každou jednotlivou tabulkou. Dále můžeme do každé tabulky přidat záhlaví s názvem indikátoru.

Přesuňte záhlaví sloupců z pásma záhlaví sloupce do pásma záhlaví skupiny indikátorů.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_41.jpg)

Dále přidejte textové pole do pásma záhlaví skupiny indikátorů a upravte jeho výraz tak, aby zobrazoval název indikátoru.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_42.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_44.jpg)

Zpráva by nyní měla mít tři tabulky, jednu pro každý indikátor. Každá tabulka bude mít záhlaví s názvem indikátoru a také řádek záhlaví tabulky.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_45.jpg)

#### Třídění a seskupování { #sorting-and-grouping }

Pokud používáte seskupování, je třeba při třídění dodržovat určitá opatření. Je pozoruhodné, že při přidávání parametrů řazení musí být na prvním místě jakýkoli parametr použitý jako základ pro seskupení. Pokud tedy seskupujete sestavu podle indikátoru a chcete řadit organizační jednotky podle abecedy, musíte se rozhodnout nejprve seřadit podle indikátoru a poté podle názvu organizační jednotky, jak je znázorněno níže. Pokyny, jak přidat řazení, najdete výše v části řazení.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_59.jpg)

## Grafy { #charts }

Ve výchozím nastavení je do souboru .jrxml, který je stažen z DHIS 2, zahrnut 3D sloupcový graf. Je nastaven tak, že se používají pouze data z «parametrické organizační jednotky» (často rodič nebo prarodič). Obvykle je to dobré řešení. Protože se jedná o výchozí nastavení, začneme tím, že se podíváme na pruhové grafy, než se podíváme na spojnicové grafy.

### Lištové grafy { #bar-charts }

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_54.jpg)

Sloupcové grafy jsou výchozím typem grafu v DHIS2. V této části se podíváme na to, jak vytvořit sloupcové grafy, jako je ten výše, porovnávající hodnotu jednoho indikátoru v několika okresech. Chcete-li upravit výchozí graf v iReportu, klikněte na něj pravým tlačítkem a vyberte Data grafu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_46.jpg)

Objeví se okno. Ve výchozím nastavení je výraz Filtr vyplněn, takže se zobrazí pouze data pro nadřazenou organizační jednotku. Pokud to z nějakého důvodu nechcete, jednoduše odstraňte text v textovém poli. V tomto případě nechceme filtr, protože vytváříme graf znázorňující srovnání napříč okresy. Chcete-li pokračovat, klikněte na kartu podrobností.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_47.jpg)

V části Podrobnosti uvidíte seznam sérií pro graf. Ve výchozím nastavení je pro každý křížový sloupec vytvořena jedna řada. V tomto případě se díváme na údaje pro jeden indikátor za celý rok 2010, a to pro řadu okresů. Indikátor je podél dimenze křížové tabulky.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_48.jpg)

Chcete-li v sérii provést změny, vyberte ji a klikněte na Upravit. Objeví se další okno, kde jsou čtyři oblasti, které lze upravit. První tři jsou povinné, ale do jedné z prvních dvou stačí přidat prázdnou nabídku («»).

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_500.jpg)

První pole je textové pole, do kterého lze vložit nebo upravit název série. Toto je pole, které bude použito k vyplnění textu v poli legendy (viz níže).

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_50.jpg)

Pokud však chcete mít název každého pruhu podél osy x grafu namísto použití legendy, lze to provést přidáním libovolného textu, který chcete zobrazit v poli Výraz kategorie, nebo vložením výrazu do nechat jej automaticky vyplnit při spuštění hlášení. V tomto případě chceme mít jeden pruh pro každou organizační jednotku. Proto upravíme výraz kategorie kliknutím na tlačítko vpravo.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_49.jpg)

Jako výraz jsme vybrali organisationunitname, jak je uvedeno níže.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_490.jpg)

Po dokončení by měl editor sérií vypadat níže. Kliknutím na OK a potom Zavřít zavřete okno Podrobnosti grafu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_501.jpg)

Pokud do oblasti výrazu Kategorie přidáte dobrý popis, můžete pole legendy vynechat. To se provádí na panelu Vlastnosti zprávy v iReportu, kde můžete také upravit mnoho dalších podrobností grafu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_51.jpg)

Můžeme také přidat název do grafu, například název indikátoru. To se také děje na panelu Vlastnosti grafu v části výraz nadpisu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_55.jpg)

Zobrazí se okno editoru výrazů, kde můžete zadat název. Název musí být v uvozovkách, jak je uvedeno níže.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_56.jpg)

Graf je nyní připraven.

### Čárové grafy { #line-charts }

Čárové grafy mohou být užitečné za mnoha okolností. Chcete-li však vytvořit spojnicový graf, musí být pro něj vhodná data sestavy (tabulka sestavy). Pokud tedy chcete vytvořit spojnicový graf, je důležité, aby tabulka sestavy neměla v dimenzi křížové tabulky období. Příklady, kde je to užitečné, jsou situace, kdy vytváříte zprávu pro jednu organizační jednotku s jedním nebo více indikátory nebo pokud vytváříte zprávu s jedním indikátorem a jednou nebo více organizačními jednotkami.

Níže projdeme kroky potřebné k vytvoření zprávy s čárovým grafem ukazujícím vývoj tří indikátorů za jeden rok pro jednu organizační jednotku. Začneme vytvořením tabulky přehledu s níže uvedenými možnostmi:

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_57.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_60.jpg)

Když otevřeme výsledný soubor .jrxml v iReportu, je zahrnut výchozí spojnicový graf. Protože chceme vytvořit spojnicový graf, odstraníme tento graf a přetáhneme nový prvek grafu do sestavy z panelu Paleta.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_61.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_62.jpg)

Jakmile přetáhneme prvek Graf do sestavy, zobrazí se okno. Vybereme spojnicový graf, jak je znázorněno níže.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_63.jpg)

Zobrazí se průvodce grafem. V prvním kroku klikněte na Další, v dalším na Dokončit - data přidáme později.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_64.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_65.jpg)

Dále upravte velikost a umístění grafu v sestavě. Potom přidáme jednu datovou řadu pro každý z našich tří indikátorů. Klikněte pravým tlačítkem na graf a vyberte Data grafu. Pokud vytváříte graf s jedním indikátorem a několika organizačními jednotkami, pravděpodobně budete chtít vytvořit výraz filtru, aby se v grafu používala pouze data z parametru / nadřazené organizační jednotky. Chcete-li to provést, přidejte tento řádek do oblasti Filtr výrazu:

`$F{organisation_unit_is_parent}.equals("Yes")`

V našem příkladu máme pouze na organizační jednotce, takže to není nutné. Dále kliknutím na kartu podrobností zobrazte seznam sérií v grafu. Prozatím je tento seznam prázdný, ale pro každý z našich tří indikátorů přidáme jednu řadu. Chcete-li přidat sérii, klikněte na tlačítko Přidat.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_66.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_67.jpg)

V okně, které se objeví, zadejte název prvního z indikátorů v okně Výraz série. Nezapomeňte uvést jméno do uvozovek. Ve výrazu kategorie (podél osy x) chceme měsíce, takže pomocí tlačítka vedle pole otevřete editor výrazů a přidáme název období.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_69.jpg)

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_68.jpg)

Ve výrazu hodnoty přidáme skutečné hodnoty dat pro náš první indikátor. Použijte k tomu znovu editor výrazů. Po dokončení by okno mělo vypadat jako níže, pouze s různými názvy podle indikátoru.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_70.jpg)

Potom můžete klepnutím na OK zavřít okno. Stejným postupem přidejte řadu pro další indikátory.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_71.jpg)

Zavřete okno a data pro spojnicový graf by měla být připravena. Mohou však být zapotřebí další úpravy - většinu najdete v panelu Vlastnosti spojnicového grafu. Například při vytváření grafu měsíc po měsíci, jak máme v příkladu, často neexistuje dostatek místa pro názvy měsíců podél osy kategorie. To lze opravit otočením štítků například o -40 stupňů pomocí vlastnosti Kategorie Osa Zaškrtněte Otočení štítku.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_72.jpg)

Mnoho dalších možností je k dispozici k tvorbě grafu požadovaného vzhledu.

![](resources/images/dhis2_creating_reporting/ireportadv/irep_screen_73.jpg)

## Přidání zprávy do DHIS2 { #adding-the-report-to-dhis2 }

Nyní můžeme přepnout na DHIS2 a importovat naši zprávu. Přejděte na modul Report v DHIS2 a vyberte „Standardní zpráva“. Na obrazovce „Standardní zpráva“ klikněte na „Přidat nový“ nebo upravte stávající.

Na následující obrazovce je několik akcí, které musíme provést. Nejprve zadejte název nové "Standardní zprávy". Zadruhé, u designu klikněte na „Vybrat soubor“ a najděte soubor .jrxml, který jste upravili v iReportu. Poté vybereme tabulku zpráv, kterou jsme použili jako základ pro zprávu v iReportu. Klikněte na přidat a mělo by se přesunout do oblasti „Vybrané tabulky zpráv“. Nakonec klikněte na Uložit.

![](resources/images/dhis2_creating_reporting/ireport/27_new_std_report.jpg)

Zpráva je nyní k dispozici jako „Standardní zpráva“ v DHIS2:

![](resources/images/dhis2_creating_reporting/ireport/28_done.jpg)

## Několik závěrečných pokynů { #some-final-guidelines }

-   Použijte stejnou verzi zpráv Jasper iReport a DHIS2. Používanou verzi Jasperu najdete na stránce O... v DHIS2.

-   Jako zdroje dat pro návrhy zpráv použijte tabulky zpráv s dimenzemi křížových karet. Díky tomu bude mnohem snazší navrhovat zprávy, kde je třeba na sloupce umístit konkrétní indikátory, body nebo organizační jednotky.

-   Učte se od ostatních, existuje mnoho návrhů zpráv DHIS2 pro Jasper na Launchpadu, viz http://bazaar.launchpad.net/~DHIS2-devs-core/DHIS2/trunk/files/head:/resources/

## Návrh standardních zpráv založených na SQL { #designing-sql-based-standard-reports }

Standardní Hlášení zpráv může být založeno na dotazech SQL. To je užitečné, když potřebujete získat přístup k více tabulkám v databázi DHIS2 a provést vlastní výběr a připojení.

\- Tento krok je volitelný, ale užitečný, když potřebujete ladit své hlášení a když máte přímý přístup k databázi, kterou chcete použít. Klikněte na tlačítko „Nahlásit zdroje dat“, „Nové“, „Připojení databáze JDBC“ a klikněte na „Další“. V tomto okně můžete pojmenovat připojení a vybrat ovladač JDBC. PostgreSQL a MySQL by měly být součástí vaší iReport. Poté zadejte adresu URL připojení JDBC, uživatelské jméno a heslo. Poslední tři odkazují na vaši databázi a lze je načíst z konfiguračního souboru DHIS2 (hibernate.properties). Klikněte na „uložit“. Nyní jste připojili iReport k vaší databázi.

\- Přejděte na standardní přehledy a klikněte na „přidat nový“ a poté „získat šablonu hlášení“. Otevřete tuto šablonu v iReportu. Tato šablona obsahuje řadu parametrů hlášeníí, které lze použít k vytváření dynamických příkazů SQL. Tyto parametry budou nahrazeny na základě parametrů hlášení, které později vybereme a zahrneme do standardní zprávy. Parametry jsou:

-   období - řetězec čárkami oddělených identifikátorů relativních období

-   period_name - název vykazovaného období

-   organisationunits - identifikátor vybraných organizačních jednotek

-   organisationunit_name - název vykazující organizační jednotky

-   organisationunit_level - úroveň vykazující organizační jednotky

-   organisationunit_level_column - název odpovídajícího sloupce v tabulce prostředků \_orgunitstructure

Tyto parametry lze zahrnout do příkazů SQL pomocí syntaxe `$P\!{periods}`, kde "periods" představují parametr období.

\- Chcete-li vytvořit dotaz SQL v iReportu, klikněte na tlačítko „dotaz na hlášení“. Napište nebo vložte svůj dotaz do textové oblasti. Příklad dotazu SQL pomocí parametrů, které vytvoří hlášení zobrazující hodnoty nezpracovaných dat na čtvrté úrovni v hierarchii jednotek org, je:

```
    select district.name as district, chiefdom.name as chiefdom, ou.name as facility,
    bcg.value as bcg, yellowfever.value as yellowfever, measles.value as  measles
    from organisationunit ou
    left outer join _orgunitstructure ous
      on (ou.organisationunitid=ous.organisationunitid)
    left outer join organisationunit district
      on (ous.idlevel2=district.organisationunitid)
    left outer join organisationunit chiefdom
      on (ous.idlevel3=chiefdom.organisationunitid)
    left outer join (
      select sourceid, sum(cast(value as double precision)) as value
      from datavalue
      where dataelementid=359706
      and periodid=$P!{periods}
      group by sourceid) as bcg on bcg.sourceid=ou.organisationunitid
    left outer join (
      select sourceid, sum(cast(value as double precision)) as value
      from datavalue
      where dataelementid=35
      and periodid=$P!{periods}
      group by sourceid) as yellowfever on yellowfever.sourceid=ou.organisationunitid
    where ous.level=4
    and ous.$P!{organisationunit_level_column}=$P!{organisationunits}
    order by district.name, chiefdom.name, ou.name;
```

Všimněte si, jak jsou všechny parametry použity v dotazu, spolu s SQL spojení tabulek prostředků v databázi DHIS2.

\- Nakonec zpět na obrazovce přidání nové zprávy klikneme na „Použít zdroj dat JDBC“. To vám umožní vybrat jakékoli relativní období a parametry sestavy pro vaši sestavu. Relativní období jsou relativní k dnešnímu datu. Parametry sestavy způsobí výzvu během vytváření sestavy a umožní dynamicky vybrat organizační jednotky a období, která se použijí pro sestavu během běhu. U výše uvedeného příkladu musíme v rámci relativních období vybrat „měsíc hlášení“ a v parametrech přehledu „měsíc hlášení“ a „organizační jednotka“. Klikněte na Uložit. Tím se přesměrujete na seznam přehledů, kde jej můžete kliknutím na zelenou ikonu „vytvořit“ vedle svého přehledu, vykreslit.

## Navrhování standardních zpráv založených na HTML { #designing-html-based-standard-reports }

Standardní zprávu lze navrhnout pomocí čistěho HTML a JavaScriptu. To vyžaduje trochu zkušeností s kódováním v uvedených předmětech. Výhodou standardních zpráv založených na HTML je to, že umožňuje maximální flexibilitu. Pomocí HTML můžete navrhnout přesně požadovanou zprávu, umístění tabulek, log a hodnot na stránce podle vašich návrhových potřeb. Standardní návrh zprávy můžete napsat a uložit do běžného textového souboru. Chcete-li nahrát standardní zprávu založenou na HTML do DHIS2, postupujte takto:

-   Přejděte na standardní přehledy a klikněte na „Přidat nový“.

-   Pojmenujte zprávu.

-   Jako typ vyberte „Zpráva HTML“.

-   Pokud chcete, můžete si stáhnout šablonu zprávy kliknutím na „Získat šablonu zprávy HTML“.

-   Vyberte požadovaná relativní období - budou k dispozici v JavaScriptu ve vašem přehledu.

-   Vyberte parametry sestavy - tyto budou k dispozici v JavaScriptu ve vaší sestavě.

Šablona hlášení, kterou si můžete stáhnout po výběru typu hlášení, je užitečným výchozím bodem pro vývoj standardních hlášeníí založených na HTML. Poskytne vám základní strukturu a navrhne, jak můžete v hlášení použít JavaScript a CSS. JavaScript a CSS lze snadno zahrnout pomocí standardních značek skriptů a stylů.

Pokud jste při vytváření standardního přehledu vybrali relativní období, můžete k nim přistupovat v JavaScriptu takto:

    var periods = dhis2.report.periods; // An array with period identifiers
    var period = periods[0];

Pokud jste při vytváření standardní zprávy vybrali parametr hlášení organizační jednotky, můžete k vybrané organizační jednotce přistupovat v JavaScriptu takto:

    var orgUnit = dhis2.report.organisationUnit; // An object
    var id = orgUnit.id;
    var name = orgUnit.name;
    var code = orgUnit.code;

Při navrhování těchto hlášení můžete využít prostředek analytického webového API k načtení agregovaných dat v JavaScriptu. Podrobnější popis najdete v této příručce v kapitole Webové API. Jako úplný, minimální příklad můžete načíst analytická data po načtení hlášení a použít tato data k nastavení vnitřního textu prvku HTML takto:

    <script type="text/javascript">
    $( document ).ready( function() {
        $.get( "../api/analytics?dimension=dx:FnYCr2EAzWS;eTDtyyaSA7f&dimension=pe:THIS_YEAR&filter=ou:ImspTQPwCqd", function( json ) {
            $( "#bcg" ).html( json.rows[0][2] );
            $( "#fic" ).html( json.rows[1][2] );
        } );
    } );
    </script>

    <div>BGG coverage: <span id="bcg"></span></div>
    <div>FIC coverage: <span id="fic"></span></div>

Několik dalších tipů: Chcete-li zahrnout grafiku, můžete převést obrázek na SVG a vložit tento obsah SVG přímo do sestavy - DHIS2 je založen na HTML 5, kde jsou značky SVG platnými značkami. Chcete-li do sestavy zahrnout grafy a mapy, můžete použít zdroje grafů a map ve webovém rozhraní API. Ve své sestavě můžete použít plnou kapacitu webového API z JavaScriptu - může být užitečné přečíst si kapitolu Webové API, abyste získali přehled o všech dostupných zdrojích.
