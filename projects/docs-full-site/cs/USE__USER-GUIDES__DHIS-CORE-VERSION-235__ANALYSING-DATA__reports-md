---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/using-reporting-functionality.md"
revision_date: "2022-02-08"
---

# Funkce hlášení v aplikaci pro přehledy { #using_the_reports_app }

Aplikace zprávy umožňuje konzervované standardní zprávy, zprávy o souborech dat, zprávy o distribuci prostředků a organizačních jednotek.

## Použití standardních zpráv { #standard_reports_in_the_beta_reports_app }

Dostupné přehledy zpřístupníte v části Aplikace-\>Přehledy. V nabídce sestavy na levé liště klikněte na Standardní sestava. V hlavním okně se zobrazí seznam všech předdefinovaných zpráv.

![](resources/images/dhis2UserManual/react_reports_app_standard_reports.png)

Spustíte / zobrazíte přehled kliknutím na ikonu se třemi tečkami přehledu a následným výběrem možnosti „Vytvořit“ z kontextové nabídky. Pokud existují nějaké předdefinované parametry, zobrazí se okno s parametry sestavy, kde musíte vyplnit hodnoty potřebné pro orgunit a / nebo vykazovací měsíc, v závislosti na tom, co bylo definováno v podkladových tabulkách(ce) sestavy. Až budete připraveni, klikněte na „Generovat zprávu“. Zpráva se buď zobrazí přímo ve vašem prohlížeči, nebo bude k dispozici jako soubor PDF ke stažení, v závislosti na nastavení vašeho prohlížeče pro práci se soubory PDF. Soubor můžete uložit a uchovat jej lokálně v počítači pro pozdější použití.

## Použití zpráv datových sad { #dataset_reports_in_the_beta_reports_app }

Zprávy o datových sadách jsou zobrazení obrazovky pro zadávání dat, která jsou vhodná pro tisk, vyplněná buď nezpracovanými nebo agregovanými daty.

K hlášením sady dat máte přístup z Aplikace-\>Zprávy.

Zobrazí se okno Kritéria, kde vyplníte podrobnosti svého přehledu:

**Datová sada:** Datová sada, kterou chcete zobrazit.

**Období zprávy:** Skutečné období, za které chcete data používat. To lze agregovat i jako nezpracovaná období. To znamená, že můžete požádat o čtvrtletní nebo výroční zprávu, i když se soubor dat shromažďuje měsíčně. Typ období datové sady (frekvence shromažďování) je definován v údržbě datové sady. Nejprve vyberte typ období (Měsíční, Čtvrtletní, Roční atd.) v rozevíracím seznamu vedle tlačítek Předchozí a Další a pak vyberte jedno z dostupných období z rozevíracího seznamu níže. Pomocí tlačítek Předchozí a Další skočíte o rok zpět nebo vpřed.

**Použít data pouze pro vybranou jednotku:** Tuto možnost použijte, pokud chcete přehled pro organizační jednotku, která má podřízené, ale chcete pouze data shromážděná přímo pro tuto jednotku a ne data shromážděná jejími podřízenými. Pokud chcete typickou agregovanou zprávu pro organizační jednotku, nechcete zaškrtnout tuto možnost.

**Hlášení Organizační jednotky:** Zde vyberete organizační jednotku, pro kterou chcete hlášení zprávy. To může být na jakékoli úrovni v hierarchii, protože data budou agregována až na tuto úroveň automaticky (pokud nezaškrtnete výše uvedenou možnost).

Po dokončení vyplnění kritérií přehledu kliknete na „Vytvořit“. Zpráva se zobrazí jako HTML ve formátu vhodném pro tisk. Chcete-li sestavu vytisknout nebo uložit (jako HTML), použijte funkci tisku a uložení jako v prohlížeči. Sestavu datové sady můžete také exportovat ve formátech Excel a PDF.

## Použití přehledu četnosti hlášení { #reporting_rate_summary_in_the_beta_reports_app }

Souhrn četnosti hlášení získáte z nabídky Aplikace  -\> Zprávy. Souhrny četnosti hlášení ukážou, kolik datových sad (formulářů) bylo odesláno organizační jednotkou za období.

Míra vykazování je výpočet založen na registraci kompletní sady dat. Úplná registrace datové sady znamená, že uživatel označí formulář pro zadávání údajů jako úplný, obvykle kliknutím na tlačítko kompletní na obrazovce pro zadávání údajů, čímž systému sdělí, že považuje formulář za úplný. Jedná se o subjektivní přístup k výpočtu úplnosti.

Souhrn rychlosti vykazování pro každý řádek zobrazí řadu opatření:

-   Aktuální zprávy: Udává počet úplných registrací vstupu dat pro příslušnou sadu dat.

-   Očekávané sestavy: Udává, kolik kompletních registrací datových vstupů se očekává Toto číslo je založeno na počtu organizačních jednotek, kterým byla přiřazena příslušná datová sada (povoleno pro zadávání dat).

-   Míra vykazování: Procento zpráv zaregistrovaných jako úplné na základě očekávaného počtu.

-   Zprávy na čas: Stejné jako aktuální zprávy, pouze zprávy registrované jako úplné do maximálního počtu dnů po skončení vykazovaného období. Tento počet dní po vykazovaném období lze definovat pro každou datovou sadu ve správě datové sady.

-   Rychlost hlášení aktuálního času: Stejné jako procento, jako čitatel se používají pouze zprávy registrované jako úplný aktuální čas.

Chcete-li spustit přehled, postupujte takto:

-   Vyberte organizační jednotku ze stromu.
-   Vyberte datovou sadu.

-   Vyberte typ období a období ze seznamu dostupných období pro daný typ období.

-   Zpráva se poté vykreslí. Změňte kterýkoli z výše uvedených parametrů a znovu klikněte na „Získat přehled“. Zobrazí se odpovídající výsledky.

![](resources/images/dhis2UserManual/react_reports_app_reporting_rate_summary.png)

## Použití zdrojů { #resources_in_the_beta_reports_app }

Nástroj prostředků vám umožňuje nahrát oba soubory z místního počítače na server DHIS a přidat odkazy na jiné zdroje na internetu prostřednictvím adres URL. Pokud je pro váš systém nakonfigurováno cloudové úložiště, budou se  ukládat prostředky tam.

Vytvoření nového zdroje:

1.  Otevřete aplikaci **Zprávy** a klikněte na **Zdroj**.

2.  Klikněte na **Přidat nový**.

3.  Zadejte **Název**.

4.  Vyberte **Typ**: **Nahrát soubor** nebo **Externí URL**.

5.  Klikněte **Uložit**.

## Pomocí sestav distribuce organizačních jednotek { #orgunit_distribution_reports_in_the_beta_reports_app }

K přehledům distribuce Org. jednotek můžete přistupovat z nabídky na levé straně v části Aplikace -\>Zprávy.

Zprávy o distribuci organizace jsou zprávy, které ukazují, jak jsou organizace zastoupeny podle různých vlastností, jako je typ a vlastnictví, a podle geografických oblastí.

Výsledek lze prezentovat v tabulkové zprávě nebo v grafu.

**Spuštění přehledu:**

Chcete-li spustit zprávu, nejprve vyberte organizační jednotku ve stromu organizačních jednotek na levé horní straně. Zpráva bude založena na organizačních jednotkách umístěných pod vybranou organizační jednotkou. Vyberte sadu skupin organizačních jednotek, kterou chcete použít, obvykle se jedná o Typ, Vlastnictví, Venkov / Město, ale může to být libovolná uživatelská skupina skupin organozačních jednotek. Kliknutím na Získat zprávu získáte tabulkovou prezentaci nebo Získat graf pro získání stejného výsledku v grafu. Můžete si také stáhnout tabulkovou sestavu jako Excel nebo CSV.

![](resources/images/dhis2UserManual/react_reports_app_org_unit_dist.png)
