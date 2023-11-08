---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/testing.md"
revision_date: "2021-05-10"
---

# Testování { #implementation_guide_testing }

Nyní, když byl server DHIS 2 původně nakonfigurován a aplikaci jste nainstalovali do jednoho nebo více zařízení, jste připraveni zahájit testování. Při plánování testování si musíte být vědomi nadcházejících verzí. Je důležité být součástí komunity na [https://community.dhis2.org/](https://community.dhis2.org/) a používat [JIRA](http://jira.dhis2.org/), nástroj pro správu softwaru, který UiO využívá. To vám umožní dozvědět se o otevřených problémech, pokud jde o funkce a opravy chyb, které jsou naplánovány pro budoucí vydání.

Doporučujeme otestovat aplikaci pro Android paralelně s vaší konfigurací, abyste se ujistili, že se vaše změny na serveru správně projeví a fungují v aplikaci. To je zvláště důležité během konfigurace pravidel programu. Kromě tohoto testování krok za krokem existují různé typy testování, které byste měli provést před spuštěním aplikace.

Existuje počáteční sada testů, které by měly být prováděny interně s menšími skupinami, aby bylo zajištěno, že konfigurace jsou provedeny správně, funkčnost je na místě a že vzhled a chování je adekvátní. V rámci této počáteční fáze testování budete provádět tzv. Interní testování, po kterém bude následovat testování UAT (User Acceptance Testing). Dále v této části rozvedeme, co tyto typy testů znamenají a jak je provádět. Poté provedete testování v terénu a pilotujete. V této fázi testování provedete sadu testů s většími skupinami, abyste mimo jiné zaručili, že vaše pracovní toky, vaše infrastruktura a architektura jsou správné. Dále v této části se budeme dále zabývat těmito typy testů a jejich prováděním.

Následující grafy ukazují, že další kroky jsou iterativní povahy, včetně nových konfigurací serveru založených na výsledcích testování. S největší pravděpodobností provedete několik kol testování a překonfigurování, než budete připraveni na zvětšení a spuštění.

|  |  |
| --- | --- |
| ![](resources/images/implementation-guide-image35.png){ .center } | ![](resources/images/implementation-guide-image7.png){ .center } |
| ![](resources/images/implementation-guide-image36.png){ .center } | ![](resources/images/implementation-guide-image5.png){ .center } |

## Obecná doporučení pro testování aplikace pro Android { #implementation_guide_testing_general }

Než půjdeme do různých fází testování, představíme několik obecných doporučení, která lze použít k testování aplikace pro Android. Obecně lze jakýkoli proces testování shrnout do následujících kroků:

![](resources/images/implementation-guide-image21.png){ .center width=80% }

1. **Posouzení**. Prvním krokem je zkontrolovat informace o samotné aplikaci tak, že přejdete na [<span class="underline">https://www.DHIS 2.org/android-documentation</span>](https://www.dhis2.org/android-documentation). Dokumentace vám poskytne informace o tom, proč a co nebo vaše testování. Mělo by vám pomoci určit, zda aplikace splňuje vaše požadavky, co může a nemůže dělat, a pomoci vám analyzovat nesrovnalosti. Mělo by vám také pomoci identifikovat nové funkce a nastavení, podporované funkce.

2. **Plán**. V tomto kroku musíte určit čas testování pochopením časové osy vlastní implementace. V rámci této plánovací fáze musíte vytvořit podrobný seznam požadavků a klasifikovat je jako povinné (MUSÍ mít) nebo dobré mít.

3. **Design**. V tomto kroku musíte vyvinout testovací případy, rozhodnout o počtu testovacích interakcí a nástrojích, které budete pro testování používat. ![](resources/images/implementation-guide-image28.png){ .center width=80% }

   - **Příklad testovacích nástrojů - Jira** ![](resources/images/implementation-guide-image2.png)
   - **Příklad testovacího nástroje - Excel** ![](resources/images/implementation-guide-image17.png)

   - Každý testovací případ by měl obsahovat následující části. Úroveň podrobností a obsah testu, který má být proveden, bude záviset na úrovni profilu zkušeností uživatele.
     - Identifikace: Číslo cyklu / ID, ID testu, verze, shrnutí testu.
     - Popis: podrobnosti, kroky k zopakování
     - Zpráva o stavu: Datum provedení, provedeno, očekávaný vs. skutečný výsledek, ID zprávy o stavu provedení.

4. **Provádění**. Během provádění testování mějte na paměti dva důležité problémy:
   - Konfigurace metadat: Ověřte nastavení programu na webu a v dokumentaci zjistěte chování funkcí v aplikaci. To pomůže identifikovat skutečné chyby versus problémy odvozené z konfigurace nebo nepodporovaných funkcí.
   - Matice dokončení: Zkontrolujte svůj pokrok podle termínů, které jste navrhli ve fázi plánování. Také se ujistěte, že jsou důsledně pořizovány poznámky, aby bylo možné nahlásit chybu.
5. **Zpráva**. Vaše zpráva musí mít tři důležité vlastnosti
   - Hlášená chyba musí být reprodukovatelná
   - Informace musí být konkrétní a informativní
   - Zpráva musí oddělit fakta od spekulací ![](resources/images/implementation-guide-image1.png) { .center width=80% }
   - Níže uvedená tabulka shrnuje dobré Hlášení chyb s několika příklady: ![](resources/images/implementation-guide-image34.png) { .center width=80% }

## Interní testování a testování UAT { #implementation_guide_testing_internal }

**Co testujete**

Testujete konfiguraci serveru DHIS 2 a samotnou aplikaci pro Android.

![](resources/images/implementation-guide-image12.png){ .center width=40% }

**Co hledáte?**

Pravidla programu, formuláře, vizuální uživatelské rozhraní, indikátory ... Chyby, vylepšení, nové požadavky atd.

**Jak?**

Metody a období pro testování se liší od skupiny ke skupině, ale musí to být iterativní, flexibilní a musí to být provedeno v raných fázích procesu nasazení. Musíte věnovat čas rozhodování o tom, kdo se testu zúčastní, vypracovat plán testu a mít strategii pro získání zpětné vazby. K hlášení a sledování chyb a problémů jsou k dispozici různé nástroje. V závislosti na složitosti vašeho testu můžete použít [trello](https://trello.com/), [JIRA](https://www.atlassian.com/software/jira) atd.

Nastavení správného základu pro vaše interní testování zvýší kvalitu a efektivitu testovacích relací. Tato doporučení platí pro jakýkoli z různých testů, které budete muset provést.

### Testování UAT { #implementation_guide_testing_uat }

**Co testujete**
Testujete konfiguraci systému (vstup), své vizuální uživatelské rozhraní a ikony, použitelnost a vaše výstupy. V této fázi můžete také otestovat uživatelskou zkušenost s různými zařízeními (smartphone, tablet, externí klávesnice, chromebook).

![](resources/images/implementation-guide-image6.png){ .center width=40% }

**Co hledáte?**

Úpravy v předchozích položkách a problémy s hardwarem. Je vhodný čas začít identifikovat šampiony, kteří pomohou v budoucích fázích. Hlavním účelem UAT je přimět lidi z různých prostředí ve shodě s konfigurací k provedení testování v terénu. Úspěch této fáze určí přesun do další fáze, testování v terénu

**Jak?**

Používejte řízené prostředí. Najděte uživatele s malou zkušeností této technologie, kteří nemusí být nutně integrováni do pracovních postupů. Vaši uživatelé by mohli být: 1) Expert v oblasti zdraví, 2) Úředník v terénu, 3) Uživatel v terénu.

Velikost skupiny se bude lišit v závislosti na typu projektu, pro který aplikaci implementujete. Průměrná velikost testovací skupiny UAT by měla být mezi 5 a 10 lidmi.

Při rozhodování o tom, kdo se vašeho testu zúčastní, zvažte všechny různé typy uživatelů a jejich role. S ohledem na to vyberte své testery. Svým testerům byste měli poskytnout správné pokyny a návody. Musí být dobře informováni o metodách, které budete používat pro testování, o očekáváních a celkových cílech a cílech testování. Doporučuje se, je-li to možné, uspořádat testovací schůzky s jedním nebo dvěma vedoucími, kde si testeři mohou navzájem pomáhat a mají možnost klást otázky a získat pomoc přímo na místě od vedoucích. Dalším důležitým aspektem, který je třeba vzít v úvahu, jsou testovací data. Na svém testovacím serveru musíte mít dostatek dat, abyste mohli testovat různé testovací případy.

## Testování v terénu / Pilot { #implementation_guide_testing_field }

**Co testujete**

- Testujete své SoP a pracovní postupy.
- Testujete svoji infrastrukturu / architekturu.
- Testujete různá zařízení.
- Testujete své tréninkové postupy a materiály.

![](resources/images/implementation-guide-image25.png){ .center width=40% }

**Co hledáte?**

- Úpravy v předchozích položkách.
- Vhodnost vybraných zařízení pro pracovní prostor a prostředí.
- Vyhodnoťte své řešení
- Určete šampiony.

**Jak?**

20-30 uživatelů. Doporučeno 2 měsíce (plánujte dopředu!). Rozhodněte o distribuci (umístění). Nevybírejte nejjednodušší nebo nejsložitější. Snažte se o to, aby vaše řešení bylo jednoduché.

**Úvahy o hodnocení vašeho pilota**

Měli byste definovat své indikátory pro hodnocení vašich výsledků a rozhodnout se pro strategii pilotování vašeho systému. Současný systém a nový systém můžete používat paralelně po dobu několika měsíců nebo jej jednoduše vyměnit. Obě strategie mají výhody i nevýhody a před pilotováním byste je měli pečlivě analyzovat se svým týmem.

Některé výhody paralelního současného a nového systému jsou:

- Můžete mít důkazy o tom, jak se nový systém vylepšuje ve srovnání se starým z hlediska včasnosti nebo například kvality dat, tyto parametry závisí na účelu vašeho konkrétního projektu.
- Pokud něco funguje podle očekávání, máte svůj předchozí systém jako záložní mechanismus
- Buduje důvěru uživatelů, když porovnávají oba výsledky.

Některé nevýhody jsou:

- Nastavujete mechanismus dvojitého hlášení, duplikuje čas a úroveň úsilí vašich uživatelů. IT je důležité to řešit citlivě a v případě potřeby připravit potenciální podporu lidských zdrojů.
- Možnost uživatelů porovnávat oba systémy paralelně by mohla být dvojsečným mečem, protože uživatelé mají tendenci odolávat změnám.
