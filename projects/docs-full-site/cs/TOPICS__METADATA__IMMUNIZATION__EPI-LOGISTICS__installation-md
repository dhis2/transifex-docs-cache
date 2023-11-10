---
edit_url: "https://github.com/dhis2-metadata/GEN_DOCS/blob/master/docs/agg-installation.md"
revision_date: '2022-11-11'
tags:
- Metadata
---

# Průvodce instalací agregačního balíčku { #aggregate-package-installation }

## Přehled { #overview } 

Tento dokument je určen k tomu, aby provedl administrátory procesem instalace konfiguračních balíčků pro DHIS2 pro agregované hlášení zpráv. Je vyžadováno dobré porozumění DHIS2.

Konfigurační balíčky pro DHIS2 se skládají ze souboru metadat ve formátu [JSON] (https://en.wikipedia.org/wiki/JSON), který lze importovat do instance DHIS2, a také z průvodní dokumentace. Balíček poskytuje předdefinovaný standardní obsah podle doporučení WHO. Tento dokument se týká kompletních balíčků, které obsahují konfigurace sběru dat (datové sady, datové prvky, pravidla ověřování) a také analýzy a ovládací panely (oblíbené grafy, mapy a kontingenční tabulky). Toto je určeno pro použití tam, kde není nakonfigurován žádný sběr dat v DHIS2, nebo pokud nahrazujete / revidujete stávající obsah, aby odpovídal doporučením WHO.

Konfigurační balíčky se skládají z následujících součástí:

* datové soubory s datovými prvky;
* objekty metadat specifické pro balíček (prediktory, konstanty, skupiny organizačních jednotek atd.);
* soubor indikátorů;
* analytické výstupy (kontingenční tabulky, vizualizace dat a oblíbené GIS);
* sada ovládacích panelů.

Všechny tyto komponenty jsou propojené, tj. Indikátory vycházejí ze zahrnutých datových prvků, analytické výstupy vycházejí ze zahrnutých indikátorů a ovládací panely jsou tvořeny zahrnutými analytickými výstupy.

## Instalace { #installation } 

Instalace modulu se skládá ze dvou kroků:

1. [Příprava](#preparation-the-metadata-file) souboru metadat s DHIS2 metadaty.
2. [Import](#import-a-metadata-file-into-dhis2) souboru metadat do DHIS2.
3. [Konfigurace](#additional-configuration) importovaná metadata.
4. [Provádění](#examples-of-other-modifications) úprav specifických pro balíček.

Tato část se zabývá prvními dvěma kroky přípravy a importu souboru metadat do DHIS2, zatímco postup konfigurace je popsán v další části. Před zahájením procesu instalace a konfigurace v DHIS2 se doporučuje nejprve si přečíst obě části. Kromě zde popsaných obecných kroků mají některé konfigurační balíčky přílohy k instalační příručce, které popisují konkrétní problémy. Ty jsou uvedeny v příslušné sekci [zde](https://dhis2.org/who-package-downloads).

Postup popsaný v tomto dokumentu by měl být testován v testovacím / fázovacím prostředí před opakováním nebo přenesením do produkční instance DHIS2.

Více konfiguračních balíčků

Některé konfigurační balíčky mají překrývající se metadata, například indikátory. To znamená, že v některých situacích mohou být změny metadat konfiguračních balíčků, které byly dříve importovány, přepsány při importu jiného balíčku. Tomu se lze vyhnout importováním metadat „pouze nová“ místo „nových a aktualizací“, ale mějte na paměti, že u obou přístupů budou nutné ruční úpravy. Minimálně musíte zajistit, aby byla metadata používaná více programy [sdílena](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/users-roles-and-groups.html#mgt_usergroup) s příslušnými skupinami uživatelů pro oba programy.

## Požadavky { #requirements } 

K instalaci konfiguračního balíčku je vyžadován uživatelský účet správce v DHIS2 s oprávněními k přidávání / úpravám (veřejných) objektů metadat, mimo jiné včetně: (ale nejen)

* datové prvky (včetně kategorií)
* datové sady
* indikátory
* typy indikátorů
* ovládací panely
* datový vizualizér, kontingenční tabulka a oblíbené GIS

Úplný seznam objektů obsažených v modulu (pro které správce potřebuje oprávnění ke správě) najdete v referenčním dokumentu metadat pro konkrétní konfigurační balíček.

V případech, kdy jsou nutné úpravy souboru metadat .json konfiguračního balíčku [(viz níže)](https://who.dhis2.org/documentation/installation_guide_complete.html#preparing-the_metadata-file), [textový editor ](https://en.wikipedia.org/wiki/Text_editor) je potřeba - tyto úpravy by neměly být prováděny s textovým procesorem, jako je Microsoft Word.

Konfigurační balíček lze nainstalovat do DHIS2 prostřednictvím aplikace DHIS2 Health App nebo ručně prostřednictvím souboru .json s metadaty DHIS2 pomocí aplikace [Import / Export](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/maintaining-the-system/importexport-app.html) aplikace DHIS2. Postup popsaný ve zbytku této části platí pro proces ručního importu metadat.

Sekce [Konfigurace](https://who.dhis2.org/documentation/installation_guide_complete.html#configuration) platí pro obě metody.

## Příprava souboru metadat { #preparing-the-metadata-file } 

**POZNÁMKA**: Pokud instalujete balíček na novou instanci DHIS2, můžete přeskočit část „Příprava souboru metadat“ a okamžitě přejít do části „[Import souboru metadat do DHIS2](#import-a-metadata-file-into-DHIS2). “

I když to není vždy nutné, může být často výhodné provést určité úpravy souboru metadat před jeho importem do DHIS2.

## Výchozí dimenze dat { #default-data-dimension } 

V dřívějších verzích DHIS2 byl automaticky vygenerován UID výchozí datové dimenze. Zatímco tedy všechny instance DHIS2 mají výchozí možnost kategorie, kategorii datových prvků, kombinaci kategorií a kombinaci možností kategorie, UID těchto výchozích hodnot se mohou lišit. Novější verze DHIS2 mají pevně zakódované UID pro výchozí dimenzi a tyto UID se používají v konfiguračních balíčcích.

Aby nedocházelo ke konfliktům při importu metadat, je vhodné vyhledat a nahradit celý soubor .json pro všechny výskyty těchto výchozích objektů a nahradit identifikátory UID souboru .json identifikátory UID databáze, do které bude soubor importován. Tabulka 1 ukazuje UID, která by měla být nahrazena, a také koncové body API pro identifikaci stávajících UID.

|Objekt|UID|Koncový bod API|
|--|--|--|
|Kategorie|GLevLNI9wkl|../api/categories.json?filter=name:eq:default|
|Možnost kategorie|xYerKDKCefk|../api/categoryOptions.json?filter=name:eq:default|
|Kombinace kategorií|bjDvmb4bfuf|../api/categoryCombos.json?filter=name:eq:default|
|Kombinace možností kategorie|HllvX50cXC0|../api/categoryOptionCombos.json?filter=name:eq:default|

Například pokud importujete konfigurační balíček do [https://play.dhis2.org/demo](https://play.dhis2.org/demo), UID výchozí kombinace možností kategorie lze identifikovat pomocí [https://play.dhis2.org/demo/api/categoryOptionCombos.json?filter=name:eq:default](https://play.dhis2.org/demo/api/categoryOptionCombos.json?filter=name:eq:default) jako `bRowv6yZOF2`. Poté můžete v souboru .json vyhledat a nahradit všechny výskyty souboru `HllvX50cXC0` výrazem `bRowv6yZOF2`. Tato operace hledání a nahrazení musí být provedena pomocí editoru prostého textu, nikoli pomocí textového editoru, jako je Microsoft Word.

## Typy indikátorů { #indicator-types } 

Typ indikátoru je další typ objektu, který může způsobit konflikt importu, protože se v různých databázích DHIS2 používají určité názvy (např. „Procento“). Vzhledem k tomu, že typy indikátorů jsou definovány jednoduše podle jejich faktoru a bez ohledu na to, zda jsou či nejsou jednoduchými čísly bez jmenovatele, jsou jednoznačné a lze je nahradit pomocí vyhledávání a nahrazení UID. Tím se vyhnete možným konfliktům při importu a vyhnete se vytváření duplicitních typů indikátorů. Tabulka 2 ukazuje identifikátory UID, které lze nahradit, a také koncové body API pro identifikaci stávajících identifikátorů UID.

|Objekt|UID|Koncový bod API|
|--|--|--|
|Pouze čitatel (číslo)|kHy61PbChXr|../api/indicatorTypes.json?filter=number:eq:true&filter=factor:eq:1|
|Procento|hmSnCXmLYwt|../api/indicatorTypes.json?filter=number:eq:false&filter=factor:eq:100|

**Poznámka 1**: nahrazením identifikátorů UID, jak je popsáno, a importem souboru .json, bude název (včetně všech překladů) příslušných typů indikátorů aktualizován na názvy obsažené v konfiguračních balíčcích.

**Poznámka 2**: Alternativním přístupem k opětovnému použití existujících typů indikátorů je import těch, které jsou obsaženy v konfiguračním balíčku, a odstranění stávajících, které se překrývají. To by vyžadovalo aktualizaci všech indikátorů, které používají tyto existující typy indikátorů, na nově importované typy indikátorů, než bude možné typy indikátorů odstranit.

## Import souboru metadat do DHIS2 { #importing-a-metadata-file-into-dhis2 } 

Soubor metadat .json je importován prostřednictvím aplikace [Import / Export](#import_export) systému DHIS2. Před pokusem o skutečný import metadat je vhodné použít funkci „suchý běh“ k identifikaci problémů. Pokud „suchý běh“ hlásí nějaké problémy nebo konflikty, přečtěte si níže uvedenou část [Konflikty importu manipulace](#handling-import-conflict).

Pokud import „na sucho“ / „ověření“ funguje bez chyby, zkuste importovat metadata. Pokud import proběhne bez chyb, můžete přejít k [konfiguraci](#additional-configuration) modulu. V některých případech se konflikty importu nebo problémy nezobrazí během „suchého běhu“, ale zobrazí se při pokusu o skutečný import. V tomto případě bude v souhrnu importu uvedeny všechny chyby, které je třeba vyřešit.

### Řešení konfliktů importu { #handling-import-conflicts } 

**POZNÁMKA** Pokud importujete do nové instance DHIS2, nebudete se muset starat o konflikty importu, protože v databázi, do které importujete, není nic, co by mohlo být v konfliktu. Postupujte podle pokynů k importu metadat, poté pokračujte k části „[Další konfigurace](#additional-configuration)“.

Může nastat řada různých konfliktů, i když nejběžnější je, že v konfiguračním balíčku jsou objekty metadat se jménem, zkratkou a / nebo kódem, který již v cílové databázi existuje. Existuje několik alternativních řešení těchto problémů s různými výhodami a nevýhodami. Který z nich je vhodnější, bude záviset například na typu objektu, pro který dojde ke konfliktu.

#### Alternativa 1 { #alternative-1 } 

Přejmenujte existující objekt, u kterého došlo ke konfliktu. Výhodou tohoto přístupu je, že není nutné upravovat soubor .json, protože změny se místo toho provádějí prostřednictvím uživatelského rozhraní DHIS2. Pravděpodobně to bude méně náchylné k chybám. To také znamená, že konfigurační balíček je ponechán tak, jak je, což může být výhodou, například když se použije školicí materiál a dokumentace založená na konfiguračním balíčku.

#### Alternativa 2 { #alternative-2 } 

Přejmenujte objekt, u kterého došlo ke konfliktu v souboru .json. Výhodou tohoto přístupu je, že stávající metadata DHIS2 jsou ponechána tak, jak jsou. To může být faktor, když existuje školicí materiál nebo dokumentace, jako jsou SOP datových slovníků propojených s daným objektem, a to nezahrnuje žádné riziko záměny uživatelů úpravou metadat, se kterými jsou obeznámeni. Úprava objektu souboru .json současně znamená, že používání přidružené dokumentace a školicího materiálu se může stát komplikovanějším.

Všimněte si, že pro alternativu 1 i 2 může být modifikace stejně jednoduchá jako přidání malého pre / post-fix k názvu, aby se minimalizovalo riziko záměny.

#### Alternativa 3 { #alternative-3 } 

Třetím a komplikovanějším přístupem je úprava souboru .json pro opětovné použití existujících metadat. Například v případech, kdy indikátor pro určitý koncept již existuje (např. „Pokrytí ANC 1“), může být tento indikátor odstraněn ze souboru .json a všechny odkazy na jeho UID nahrazeny odpovídajícím indikátorem, který je již v databázi. Velkou výhodou tohoto .json (který se neomezuje na případy přímého konfliktu importu) je vyhnout se vytváření duplicitních metadat v databázi. Obvykle se však nedoporučuje z několika důvodů:

* vyžaduje odborné znalosti struktury podrobných metadat DHIS2
* přístup nefunguje u všech typů objektů. Zejména určité typy objektů mají závislosti, které se tímto způsobem komplikovaně řeší, například v souvislosti s rozčleněními.
* stejně jako u alternativy 2 to znamená, že výsledek instalace není zcela v souladu se standardní konfigurací a školicí materiál a dokumentace vyvinutá pro tuto konfiguraci nemusí být bez úprav použitelné.
* budoucí aktualizace konfiguračního balíčku budou komplikované.

## Další konfigurace { #additional-configuration } 

Po úspěšném importu všech metadat by měl být modul použitelný pouze s několika drobnými dalšími úpravami. Kromě toho, v závislosti zcela na instanci DHIS2, do které byl modul importován, může být nutná nebo výhodná nějaká další konfigurace a modifikace. Tato část nejprve projde nezbytnými konfiguračními kroky, poté zmíní některé další typy úprav nebo konfigurace, které mohou být relevantní.

## Požadovaná konfigurace { #required-configuration } 

Než lze konfigurační balíčky použít pro sběr dat, jsou nutné dva kroky.

* Přiřaďte datovou sadu (datové sady) k příslušným organizačním jednotkám
* Sdílejte datovou sadu (datové sady) s příslušnými skupinami uživatelů
* Přidejte své(ho) uživatele do příslušných skupin uživatelů

Datové soubory by měly být přiřazeny organizačním jednotkám (zařízením), u nichž se očekává, že budou podávat zprávy o tomto konkrétním datovém souboru.

Sady dat a možnosti kategorií by měly být sdíleny také s příslušnými skupinami (skupinou) uživatelů pracovníků, kteří jsou odpovědní za zadávání údajů pro tyto soubory dat.

### Sdílení { #sharing } 

Nejprve budete muset pomocí funkce *Sdílení* DHIS2 konfigurovat, kteří uživatelé (skupiny uživatelů) by měli vidět metadata a data spojená s programem a kdo může registrovat / zadávat data do programu. Sdílení by mělo být nakonfigurováno pro následující:

* Datové prvky / skupiny datových prvků
* Indikátory / skupiny indikátorů
* Datové Sady
* Ovládací panely

Mezi skupiny uživatelů, které jsou obvykle součástí balíčku, patří:

* {Package Name} přístup
* {Package Name} admin
* {Package Name} sběr dat

Doporučujeme poskytnout těmto skupinám následující přístup

|Objekt|Uživatelská skupina|||
|--|--|--|--|
||_{Package Name} přístup_|_{Package Name} admin_|_{Package Name} sběr dat_|
|_Datové prvky / skupina datových prvků_|Metadata : lze zobrazit <br> Data: lze zobrazit|Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit|Metadata : lze zobrazit <br> Data: lze zobrazit|
|_Indikátory / skupina indikátorů_|Metadata : lze zobrazit <br> Data: lze zobrazit|Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit|Metadata : lze zobrazit <br> Data: lze zobrazit|
|_Datové sady_|Metadata : lze zobrazit <br> Data: lze zobrazit|Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit|Metadata: lze zobrazit <br> Data: lze zachytit a zobrazit|
|_Ovládací panely_|Metadata : lze zobrazit <br> Data: lze zobrazit|Metadata: lze upravovat a prohlížet <br> Data: lze zobrazit|Metadata : lze zobrazit <br> Data: lze zobrazit|

### Duplikovaná metadata { #duplicated-metadata } 

I když byla metadata úspěšně importována bez jakýchkoli konfliktů při importu, mohou být v metadatech duplikáty - ať už jde o graf, indikátor, datový prvek nebo kategorii datových prvků, které již existují. Jak bylo uvedeno v části výše o řešení konfliktů, je třeba mít na paměti důležitý problém, že při rozhodování o změnách metadat v DHIS2 je třeba zohlednit i další dokumenty a zdroje, které jsou různými způsoby spojeny s existujícími metadaty a metadata, která byla importována prostřednictvím konfiguračního balíčku. Vyřešení duplikátů tedy není jen otázkou „vyčištění databáze“, ale také zajištěním toho, aby se tak dělo například bez narušení potenciálu integrace s jinými systémy, možnosti použít školicí materiál, porušení SOP atd. To bude velmi závislé na kontextu.

Je třeba mít na paměti jednu důležitou věc, že DHIS2 má nástroje, které mohou skrýt některé složitosti možných duplikací v metadatech. Například tam, kde existují kategorie duplicitních datových prvků, mohou být tyto duplicity pro koncové uživatele skryty prostřednictvím skupin skupin možností možností nebo mohou být skryty určité objekty metadat pro skupiny uživatelů prostřednictvím sdílení.

Doporučuje se neodstraňovat ani nenahrazovat indikátory obsažené v konfiguračních balíčcích, přestože stejný indikátor již existuje, aby bylo možné uchovat analytické výstupy (které vycházejí výhradně z indikátorů). To umožní opětovné použití školicích materiálů založených na konfiguračních balíčcích.

## Příklady dalších úprav { #examples-of-other-modifications } 

Kromě požadované konfigurace existuje řada dalších úprav a konfigurace, které mohou být relevantní v závislosti na konkrétní situaci. Nebude možné poskytnout pokyny a doporučení, která pokrývají všechny různé scénáře, ale zde je uvedena krátká diskuse o některých běžných problémech.

### Překlady { #translations } 

Je možné, že bude třeba přidat další překlady, pokud jsou zapotřebí jiné jazyky než ty, které jsou součástí.

### Přidání dalších proměnných { #adding-additional-variables } 

Konfigurační balíčky obsahují klíčové doporučené datové prvky a indikátory. V některých případech však může být nutné přidat další proměnné, které by vyhovovaly informačním potřebám jednotlivých zemí. Ty by mohly být přidány do zahrnutých datových sad.

### Aktualizace rozložení formulářů pro podávání zpráv { #updating-layout-of-reporting-forms } 

Pro usnadnění práce personálu provádějícího zadávání dat v DHIS2 je někdy žádoucí přidat vlastní formulář pro zadávání dat, který odpovídá formátu papírových formulářů používaných na primární úrovni.

## Údržba { #maintenance } 

Konfigurační balíčky nevyžadují žádnou zvláštní údržbu, protože jsou tvořeny standardními objekty metadat DHIS2. Před upgradem na nové verze DHIS2 je však důležité otestovat všechny funkce systému obecně na pracovním / testovacím serveru před upgradem produkčních instancí systému.

