---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/android-releases/2.6/ReleaseNote-2.6.0.md"
revision_date: "2022-04-18"
---

# DHIS2 Android App verze 2.6 Poznámky k vydání { #dhis2-android-app-version-26-release-notes }

## FUNKCE PODPORY IMPLEMENTACE { #implementation-support-features }

**Podpora více uživatelů offline:** Aplikace pro Android nyní může pracovat až se 3 různými uživateli, když je offline. Uživatelé budou muset mít přístup k internetu pro první přihlášení ke každému účtu a poté budou moci přepínat účty bez nutnosti přístupu k internetu. Uživatelé budou moci spravovat uživatelské účty a v případě potřeby účty mazat. Po dosažení maximálního počtu účtů bude nutné smazat jeden ze stávajících účtů a přihlásit se k novému.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-653) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users.png) | [Snímek obrazovky 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users-2.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_multiuser)

**Odstraňování problémů s konfigurací:** Tato funkce je určena pro správce. Aplikace pro Android obsahuje na obrazovce nastavení možnost pro ověření některých aspektů konfigurace DHIS2.

-   Jazyk: uživatel bude moci změnit jazyk uživatelského rozhraní aplikace a identifikovat štítky, tlačítka nebo výzvy s chybami nebo bez překladu.
-   Ověření programových pravidel: tento validátor zkontroluje programová pravidla v zařízení a zobrazí nekonzistence v konfiguraci.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-1655) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting.png) | [Snímek obrazovky 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting-2.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_configuration_troubleshooting)

## OFFLINE ANALYTIKA { #offline-analytics }

**Podpora legend pro tabulky v analýze:** Legendy se zobrazují v kontingenčních tabulkách povolením funkce „Použít legendy pro barvu grafu“ v aplikaci Data Visualizer. Aplikace pro Android obarví buňky buď pomocí předem definované legendy pro datovou položku, nebo pomocí jedné legendy pro celou kontingenční tabulku, v závislosti na nastavení na webu.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4500) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Legend-Sets.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_pivot_legends)

## VLASTNOSTI TRASOVAČE { #tracker-features }

**Rozbijte sklo:** Pokud je program nakonfigurován s úrovní přístupu "Chráněno" a vyhledávání se provádí mimo rozsah uživatele, zobrazí se uživateli dialogové okno s žádostí o důvod přístupu, aby dočasně přepsal oprávnění vlastníka. programu. To znamená, že uživatel získá přístup k datům souvisejícím s programem.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-657) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Break-the-glass.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_breaking_the_glass)

**Nastavte povinné vyhledávání TEI na konfigurovatelné:** Vyhledávání TEI před vytvořením nyní není povinné. Pomocí aplikace Android Settings App (v2.2.0) je možné nakonfigurovat uživatelský tok pro vytváření TEI. Pokud je tato funkce povolena, aplikace pro Android zobrazí po otevření programu tlačítko „vytvořit nový“ a vyhledávání bude volitelné.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4545) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Mandatory-TEI-Search-Config.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_configurable_search)

**Oddělené toky vyhledávání offline/online:** Aby se zlepšila doba odezvy ve výsledcích vyhledávání, aplikace pro Android nyní nejprve vyhledává offline a zobrazuje výsledky při online vyhledávání jako druhý krok, který je pro uživatele transparentní. Vyhledávání mimo program se nabízí jako druhý krok, když atributy použité při vyhledávání obsahují alespoň jeden atribut Tracked Entity Type (TET)

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4023) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Search-flow.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_offline_online_search)

## ZADÁVÁNÍ DAT A FUNKCE SYNCHRONIZACE { #data-entry-and-sync-features }

**Skenujte a zobrazte QR kódy datové matice GS1:** Pokud je typ vykreslování atributu nebo datového prvku nakonfigurován jako kód QR, aplikace pro Android bude moci číst a zpracovávat řetězec jako kódy matice dat GS1. V kombinaci s použitím funkcí d2 v pravidlech programu lze různá pole kódu GS1 uložit do různých datových prvků nebo atributů (d2:extractDataMatrixValue(klíč, dataMatrixText)).

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4329) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-GS1-Data-matrix.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_gs1)

**Umožněte uživateli „obnovit data“, aby získal poslední aktualizovaná data ze serveru:** Uživatelé nyní mohou před zadáním nových dat načíst nejnovější data ze serveru. Nyní je umístěno tlačítko pro obnovení, které spustí podrobnou synchronizaci na následujících obrazovkách:

-   Domácí strana
-   Hledání
-   Ovládací panel TEI
-   Seznam programu akce
-   Podrobnosti o události
-   Výpis datové sady
-   Podrobnosti datové sady

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4331) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Refresh-data.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_refresh_data)

**Vykreslování ikon v registračních formulářích:** Vstup dat založený na ikonách lze nyní použít v registračních formulářích. Když sekce registrace obsahuje jeden nebo více atributů sledované entity se sadami možností a přiřazenými ikonami, aplikace je dokáže zobrazit jako matici nebo sekvenci na základě typu vykreslování sekce. V předchozích částech aplikace byla tato funkce dostupná pouze pro datové prvky.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4258) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Render-icons-in-enrollment-forms.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_icon_lib)

**Vylepšení ukládání a dokončení toku v událostech:** Při ukládání registrace nebo události se zobrazí nová dialogová okna. Tlačítko „Znovu otevřít“ se nyní nachází na obrazovce s podrobnostmi a bude dostupné pouze v případě, že má uživatel správné oprávnění („Nedokončené události“) znovu otevřít dokončenou událost. Koncept a dialog „dokončování“ jsou nyní intuitivnější a uživatelsky přívětivější.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4610) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Save-and-complete-flow.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Nový design pro varování/chyby a dialogová okna dokončení:** Chybové a varovné zprávy byly vylepšeny, aby uživateli poskytovaly více a lepších informací. Nové dialogy při ukládání umožňují uživateli změny zahodit, uložit a opravit později nebo průběžně upravovat formulář pro opravu hodnot v závislosti na konfiguraci.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4591) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Warnings-errors-dialogs.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_common_features_errors)

**Vylepšete návrh rozpětí sloupců datových sad:** Šipky pro změnu rozměrů jsou nyní pevně dané v levém horním rohu obrazovky.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3016) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Dataset-span.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/datasets-features.html#capture_app_data_sets_row)

**Zobrazit nápovědu k vybraným organizačním jednotkám při otevírání hierarchie organizačních jednotek:** Pokud je vybrána organizační jednotka, při zobrazení hierarchie budou všechny vzestupné (nadřazené) organizační jednotky zobrazeny tučně, aby se uživatel mohl lépe orientovat v předchozím výběru.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2520) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Ou-hint.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_orgunit)

**Zlepšete prevenci duplikace jedinečných identifikátorů:** Při vyhledávání podle jedinečných atributů a následném vytváření nové registrace, pokud vyhledávání vrátí výsledek, aplikace neuchová hodnoty jedinečných atributů v registračním formuláři.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4250) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_search)

**Skrýt tlačítko uložit, pokud formulář nelze upravovat:** Pokud vypršela platnost události nebo má práva pouze prohlížet, tlačítko 'uložit' bude skryto.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4613) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Zarovnat spodní lištu navigace událostí:** Karta podrobností v navigační liště událostí byla vylepšena, aby poskytovala lepší uživatelský dojem.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3651) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/program-features.html#navigation-bar)

**Vylepšení návrhu datového prvku „Pouze ano“:** Štítek „Ano“ vedle zaškrtávacího políčka nebo přepínače byl odstraněn.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4493) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render)

## ÚDRŽBA { #maintenance }

**Kvalita / Zabezpečení / Výkon:** Seznam problémů souvisejících s kvalitou, zabezpečením a výkonem naleznete v tomto [jira filtru] (https://jira.dhis2.org/issues/?filter=12363).

**Oprava chyb:** Seznam chyb opravených v této verzi naleznete otevřením tohoto [jira filtru](https://jira.dhis2.org/issues/?filter=12364).

## INFORMACE O VYDÁNÍ { #release-info }

| Informace o vydání | Odkaz |
| --- | --- |
| Stáhněte si aplikaci z Google Play nebo Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Dokumentace | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Podrobnosti o každé funkci v JIRA (vyžaduje přihlášení) | [2.6 Funkce ](https://jira.dhis2.org/issues/?filter=12365) |
| Přehled opravených chyb na JIRA (vyžaduje přihlášení) | [2.6 Chyby](https://jira.dhis2.org/issues/?filter=12364) |
| Demo instance (uživatel / heslo) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Přihlašovací údaje: android / Android123 |
| Komunita DHIS 2 | [https://community.dhis2.org Mobilní komunita ](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Zdrojový kód na Githubu | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Zdrojový kód SDK na Githubu | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |
