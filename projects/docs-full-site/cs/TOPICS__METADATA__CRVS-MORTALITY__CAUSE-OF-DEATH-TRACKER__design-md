---
edit_url: "https://github.com/dhis2-metadata/CRVS_COD/blob/master/docs/crvs_cod-design.md"
revision_date: "2022-05-27"
---

# WHO Příčina úmrtí – návrh systému trasování a událostí { #crvs-cod-design }

## Celkový návrh { #overall-design }

Systém trasování příčin úmrtí od WHO je nakonfigurován tak, aby efektivně shromažďoval a spravoval data související s příčinami úmrtí. Je založen na Mezinárodním lékařském osvědčení o příčině úmrtí a ICD-10.

Existují dva programy, které zahrnují jeho design a mohou být použity v závislosti na potřebách země / organizace, která shromažďuje tato data.

1. Příčina úmrtí (anonymní) - program pro zachycení událostí bez registrace
2. Příčina úmrtí (tracker) - program s registrací

Anonymní program je program událostí, zatímco registrační program je program pro trasování. Oba tyto programy sdílejí stejné datové prvky, návrh vlastního formuláře, indikátory programu, pravidla programu atd.

Níže je uvedeno srovnání těchto dvou programů převzaté z průvodce implementací

### Příčina úmrtí (anonymní) - program události { #cause-of-death-anonymous-event-program }

| Klady | Zápory |
| --- | --- |
| Jednoduchá struktura / datový model | Nelze zaznamenat identifikátory způsobem, kde lze vynutit jedinečnost a zašifrovat atributy osob. |
| Používá aplikaci Zachycení Události, která podporuje offline zadávání dat ve webovém prohlížeči. | Z důvodu nedostatku identifikátorů je nalezení a úprava stávajících údajů obtížné. |
| Uživatelsky přívětivá obrazovka pro zadávání dat, např. týkající se zobrazení upozornění na ověření dat. |

### Příčina úmrtí (registrace) - program trackeru { #cause-of-death-registration-tracker-program }

| Klady | Zápory |
| --- | --- |
| Podporuje použití jedinečných identifikátorů a osobních atributů. To je nutné například při zvažování interoperability s jinými systémy CRVS a při hledání a úpravách dat. | Žádná podpora pro offline zadávání dat ve webovém prohlížeči. |
| Při zahrnutí identifikátorů osob se data a systém stanou citlivějšími. | Méně uživatelsky přívětivá obrazovka pro zadávání dat, např. týkající se zobrazení validačních varování. |

Jakou verzi zvolit, záleží na konkrétní situaci, ale v mnoha nastaveních bude pravděpodobně důležitá offline schopnost programu událostí. Všimněte si, že proměnné (datové prvky) používané oběma programy jsou stejné a data z těchto dvou jsou tedy srovnatelná, pokud by jedna přešla z používání jedné verze na druhou.

## Pracovní postup příčiny úmrtí { #cause-of-death-workflow }

Modul Příčina úmrtí používá rámec založený na metodě ICD (International Classification of Diseases) pro záznam údajů o příčině úmrtí. Jako hlavní zdroj informací v tomto procesu slouží [mezinárodní lékařské osvědčení o příčině úmrtí](http://apps.who.int/iris/handle/10665/40557). Aby mohly být informace zadány do DHIS2, musí být nejprve vyplněno lékařské osvědčení o příčině úmrtí (bude to pravděpodobně manuální proces a nebude vyplněno přímo v DHIS2). Tyto informace budou poté zadány do DHIS2 pomocí jednoho z vybraných typů programů. Samotný formulář pro zadávání údajů je replikou papírového lékařského osvědčení o příčině smrti. Více informací / pozadí tohoto certifikátu najdete ve výcvikové příručce ICD SMoL.

![Pracovní postup](resources/images/CoD_Workflow.png)

## Přehled programu { #program-overview }

Verze modulu událostí a trasovače WHO příčiny úmrtí sestává pouze z jedné programové fáze, protože jsou si velmi podobné svým designem; přičemž klíčovou změnou designu je schopnost registrovat atributy v programu založeném na sledování. Modul Příčina úmrtí používá vlastní formulář, aby splnil konstrukční požadavky, aby přesně odrážel papírovou formu ve webovém prohlížeči, nicméně byly také vytvořeny oddíly pro případ, že je použito mobilní zařízení. Tuto strukturu lze vidět na obrázku níže.

![Přehled programu](resources/images/CoD_Program_overview.png)

Popisy těchto programů jsou podrobněji popsány v následujících částech.

### Program událostí - Příčina úmrtí (anonymní) { #event-program-cause-of-death-anonymous }

| Fáze | Popis |
| --- | --- |
| Příčina úmrtí (anonymní) | Obsahuje všechny informace potřebné k zaznamenání informací souvisejících s lékařským osvědčením o příčinách smrti. Používá vlastní rozložení formuláře, aby odráželo papírový certifikát, s částmi dostupnými pro použití na mobilních zařízeních. |

### Tracker Program - příčina úmrtí (registrace) { #tracker-program-cause-of-death-registration }

| Fáze | Popis |
| --- | --- |
| Registrace / Atributy | Registrace se skládá z jediného atributu, ID generovaného systémem. To lze použít k jednoznačné identifikaci úmrtí a v případě potřeby k nalezení v systému, ale ve většině případů by bylo nahrazeno stávajícími schématy identifikace, např. národní ID. Lze jej také použít jako odkaz na jiné systémy (např. Civilní registrace). |
| Příčina úmrtí (registrace) | Obsahuje všechny informace potřebné k zaznamenání informací souvisejících s lékařským osvědčením příčinou úmrtí. Používá vlastní rozložení formuláře, aby odráželo papírový certifikát, s částmi dostupnými pro použití na mobilních zařízeních. Toto je neopakovatelná fáze; jakmile budou zaregistrovány podrobnosti o úmrtí, nebudou přidány žádné další události. |

Úplný seznam a popis programu, fází programu a datových prvků použitých v tomto návrhu najdete v úplném odkazu na metadata.

## Pravidla programu { #program-rules }

Více o pravidlech programu si můžete přečíst zde:

[Konfigurace pravidel programu](#webapi_nti_program_rules)

Pravidla programu jsou kritickou součástí modulu příčiny úmrtí v programech pro trasování i události. Pravidla programu se nepoužívají pouze ke snížení chyb při zadávání dat pomocí pole skrytí a zobrazování chybových / varovných akcí, ale také k přiřazení a kódování základní příčiny smrti pomocí úplných kódů ICD-10 SMoL a ICD-10; považována za klíčovou vlastnost tohoto modulu za účelem získání kvalitnějších údajů o úmrtnosti. Úplný seznam a popis pravidel programu pro tento program naleznete v podrobném seznamu metadat zde

### Skrýt pole { #hide-field }

Akce skrytého pole se používá k vyšednutí / deaktivaci polí (jedná se o akci skrytého pravidla, která se aplikuje na vlastní formulář; zatímco nemůže skrýt pole kvůli vlastnímu designu, může pole zšednout, takže s ním nelze pracovat). Můžete to vidět v níže uvedeném příkladu

![Skrýt pole](resources/images/CoD_Date_of_birth_hidden.png)

S datem narození nelze pracovat, protože datum narození není známo; není však skrytý před zraky.

Všimněte si, že na mobilním zařízení bude pole skryto, protože formulář bude výchozí pro návrh sekce, který byl popsán výše.

### Zobrazit varování / Zobrazit chybu { #show-warningshow-error }

Ve formuláři je integrována řada chybových / varovných zpráv, které upozorňují na pravděpodobné problémy se zadáváním údajů. Tyto zprávy se okamžitě zobrazí v programu událostí, když zjistí problém

![Varování](resources/images/CoD_show_warning.png)

![Chyba ověření](resources/images/CoD_validation_error.png)

U trasovacího programu se zobrazí pouze po dokončení události.

![Chyba / varování](resources/images/CoD_error_and_warning.png)

Rozdíly v zobrazování těchto chyb / zpráv byly diskutovány jako potenciální klad / zápor pro každý z těchto návrhů a měly by být zváženy před implementací.

### Přiřadit { #assign }

Akce přiřadit pravidlo se používá k určení hodnot pro následující 4 datové prvky:

-   Věk v letech
-   Základní příčina úmrtí
-   Kód ICD-10 SMoL
-   Plný kód ICD-10

Přiřazení hodnoty pro věk v letech je založeno na informacích o datech narození a úmrtí nebo odhadovaném věku, zatímco poslední 3 datové prvky jsou založeny na výběru základní příčiny smrti. Další informace o výběru této příčiny jsou k dispozici prostřednictvím výcvikových zdrojů SMoL WHO: [https://www.who.int/healthinfo/civil_registration/smol/en/.](https://www.who.int/healthinfo/civil_registration/smol/en/.)

K přiřazení různých hodnot 3 datovým prvkům se používá interakce 2 sad možností spolu s kódem obsahujícím více částí. V tomto konkrétním případě je datový prvek, který identifikuje příčinu smrti (například příčina smrti C ve formuláři je identifikována jako základní příčina), propojen se sadou možností „ICD SMoL - místní slovník.“ Tato sada možností obsahuje prosté anglické výrazy pro různé faktory, které by mohly být identifikovány pro příčinu smrti A, B, C nebo D v lékařském osvědčení o příčině smrti. Tato sada možností také obsahuje kódy možností pro každou možnost, která je rozdělena na 3 části; to je to, co se používá k přiřazení hodnot k samostatným datovým prvkům uvedeným výše.

![ICD SMOL](resources/images/CoD_ICD_SMOL.png)

Upozorňujeme, že kód je oddělen oddělovačem “|” k označení samostatných částí kódu. Části jsou odděleny takto:

1. Kód 1: Kód IoC-10 SMoL
2. Kód 2: Úplný kód ICD-10
3. Kód 3: Kód použitý k jedinečné identifikaci možnosti

Kód SMoL použitý v rámci „ICD SMoL - místní slovník“ identifikuje, co bude použito jako případná základní příčina úmrtí podle zkráceného seznamu v ICD-10 SMoL. Ve výše uvedeném příkladu vidíte, že v sadě možností „ICD-SMoL - místní slovník“ může existovat více možností, které používají stejný kód SMoL, protože všechny tyto termíny odpovídají stejné příčině úmrtí, která bude použita pro statistické účely v SMoL seznamu.

V tomto příkladu řekněme, že jsme identifikovali akutní nekrózu jater jako naši základní příčinu úmrtí (všimněte si, že to vysvětluje design a nemusí nutně odrážet skutečný příklad), což odpovídá kódu IoC-10 SMoL 5-74 a ICD-10 plný kód K720.

![ICD SMOL](resources/images/CoD_medical_data.png)

Když to bylo zadáno:

1. Vezme první část kódu v sadě možností „ICD SMoL - místní slovník“ (5-74) a přiřadí ji datovému prvku „základní příčina smrti“. Tento datový prvek je také propojen se sadou možností „ICD-SMoL“. Tato sada možností je zkráceným seznamem příčin smrti, které lze použít k získání kvalitnějších údajů o příčinách smrti.
2. Kód 5-74 v sadě možností „ICD-SMoL“ odpovídá hodnotě „Další nemoci trávicího systému“.

    ![Jiné nemoci](resources/images/CoD_other_diseases.png)

   Vidíme, že se to objeví ve formuláři pro zadávání dat přiřazenému tomuto datovému prvku ve spodní části obrazovky

    ![Výsledky](resources/images/CoD_results_underlying.png)

3. Vezme první část kódu v sadě možností „ICD SMoL - místní slovník“ (5-74) a přiřadí ji datovému prvku „ICD-10 SMoL“. Toto je pouze datový prvek ve formátu prostého textu, takže kód se zobrazí přesně tak, jak je zapsán v sadě možností.
4. Vezme druhou část kódu v sadě možností „ICD SMoL - místní slovník“ (K720) a přiřadí ji datovému prvku „ICD-10“. Toto je pouze datový prvek ve formátu prostého textu, takže kód se zobrazí přesně tak, jak je zapsán v sadě možností.

![Výsledky](resources/images/CoD_results_complete.png)

Toto je obecný proces, který se používá k automatickému kódování identifikovaných základních příčin úmrtí v této podobě a usnadnění jednoho z klíčových požadavků tohoto modulu. Použitím této metodiky je příčina úmrtí správně kódována a lze ji následně podle potřeby agregovat.

## Programové Indikátory { #program-indicators }

Více o indikátorech programu si můžete přečíst zde:

[Konfigurace indikátorů programu](l#configure_program_indicator)

S programem je spojena řada indikátorů programu. Celý seznam lze zobrazit v podrobném popisu metadat zde:

Indikátory programu které se u tohoto programu obvykle používají:

1. Seskupte podobné nemoci dohromady podle přiřazeného kódu SMoL ICD-10
2. Skupiny úmrtí společně podle věkových skupin

## Externí analýza dat (ANACOD) { #external-data-analysis-anacod }

Data zachycená programem Příčina úmrtí lze také exportovat pro externí analýzu pomocí nástroje od WHO [Úrovně analýzy a příčina úmrtí (ANACOD)](https://www.who.int/healthinfo/anacod/en/). Elektronický nástroj ANACOD poskytuje postupný přístup, který umožňuje uživatelům rychle provést komplexní analýzu údajů o úrovních úmrtnosti a příčinách úmrtí. Nástroj automaticky zkontroluje, zda data neobsahují chyby, uvádí je do tabulky, prezentuje výsledky ve formě snadno použitelných tabulek a grafů a poskytuje příležitost porovnat zjištění s nálezy z jiných skupin zemí.

Chcete-li exportovat data o zemi do nástroje ANACOD, použijete zobrazení SQL v DHIS2. Zobrazení SQL jsou zahrnuta v balíčku metadat podle roku (‘CoD: ANACOD Export [YYYY]‘). Pro vytvoření podrobných výstupů v rámci ANACOD podle roku jsou pro každý rok vyžadována nová zobrazení SQL. Budete muset věnovat zvláštní pozornost aktualizaci skriptů, protože nové verze DHIS2 mohou změnit podkladové tabulky SQL, ke kterým se přistupuje, a generovat zobrazení kompatibilní s ANACOD. Zobrazení SQL zůstane na ukázce DHIS2 WHO aktuální a lze jej použít jako referenci, pokud váš pohled přestane fungovat při upgradu na novější verzi DHIS2.

## Reference { #references }

-   WHO Start-up Mortality List (SMoL-ICD-10): [https://www.who.int/healthinfo/civil_registration/smol/en/](https://www.who.int/healthinfo/civil_registration/smol/en/.)
-   WHO Analysis Levels and Cause of Death (ANACOD): [https://www.who.int/healthinfo/anacod/en/](https://www.who.int/healthinfo/anacod/en/)
