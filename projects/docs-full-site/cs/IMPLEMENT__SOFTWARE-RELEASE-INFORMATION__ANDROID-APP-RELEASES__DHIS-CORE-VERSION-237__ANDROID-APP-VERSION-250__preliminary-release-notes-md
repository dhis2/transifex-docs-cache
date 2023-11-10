---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/2.5/android-releases/2.5/ReleaseNote-2.5.0.md"
revision_date: "2021-11-23"
---

# DHIS2 Android App verze 2.5 Poznámky k vydání { #dhis2-android-app-version-25-release-notes }

<!-- BEGIN-WEBSITE-SYNC-ID:android -->

<!-- Analytics -->

## MÍSTNÍ ANALYTIKA { #local-analytics }

**Offline analýza programů/datových sad v aplikaci:** Aplikace pro Android nyní může vykreslovat analýzy, které byly vytvořeny v aplikaci Data Visualizer v DHIS2. Zobrazení analýzy vyžaduje konfiguraci pomocí webové aplikace Nastavení systému Android, kde si administrátoři budou moci vybrat grafy a tabulky, které se zobrazí koncovým uživatelům. Tyto vizualizace lze vykreslit na domovské obrazovce aplikace, na obrazovce datové sady a na úrovni programů. Všechny analýzy jsou agregovány v zařízení pomocí místních dat. Funkce Analyticis je 100% funkční offline.

Analýzy podporované v aplikaci pro Android jsou:

-   Kontingenční tabulky
-   Sloupcový graf
-   Spojnicový graf
-   Výsečový graf
-   Radarová mapa
-   Jedna hodnota

Všechny tyto vizualizace lze organizovat a zobrazovat ve skupinách. Skupiny se také konfigurují pomocí webové aplikace Nastavení systému Android. Pro každý objekt vizualizace bude uživatel moci v aplikaci filtrovat podle:

-   Období: Denně, Týdně, Měsíčně, Ročně, Toto čtvrtletí, Poslední čtvrtletí, Poslední 4 čtvrtletí a čtvrtletí tohoto roku.
-   Organizační jednotka: Vyberte „Vše“ pro zobrazení všech organizačních jednotek dostupných uživateli nebo „Výběr“ pro určení jedné nebo více organizačních jednotek.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2557) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Home.png) | [Snímek obrazovky 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Filtering.png) | [Snímek obrazovky 3](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Groups.png) | [Snímek obrazovky 4](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Local+Analytics+-+Android+Settings+Webapp.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#local-analytics-new-25)

## UŽIVATELSKÉ ZKUŠENOSTI ZADÁVÁNÍ DAT { #data-entry-user-experience }

**Redesign datové sady** Rozvržení pro zadávání dat datových sad bylo přepracováno pro integrovanější uživatelské prostředí a čisté uživatelské rozhraní. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4382) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Data+Sets+New+style.png)

**Exportovat / sdílet QR a čárové kódy:** Datové prvky nebo text typu atributů lze nakonfigurovat jako QR nebo čárové kódy. S novou možností exportu / sdílení budou uživatelé moci zobrazit čárový nebo QR kód v obrázku, aby jej bylo možné sdílet pro tisk, pořídit snímek obrazovky nebo jej zobrazit na obrazovce pro skenování. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3891) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Export+Share+QR+Code.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render_qr)

**Vylepšené vykreslování pro zadávání dat pomocí ikon:** Když je typ vykreslování sekcí programu použit v kombinaci s ikonami, sekce s jedním datovým prvkem a přidruženou sadou možností vykreslí přiřazené ikony vedle možností, aby se zjednodušilo zadávání dat. Rozvržení a design této obrazovky byly přepracovány a vylepšeny pro lepší uživatelský zážitek. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4027) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Visual+Data+Entry.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_rendering_type)

**Personalizované zobrazení kalendáře:** V aplikaci DHIS2 Android Capture mohou uživatelé přepínat výběr data z číselníku na zobrazení kalendáře. V této verzi si aplikace bude pamatovat poslední vizualizaci vybranou uživatelem a použije ji, až bude uživatel příště potřebovat vybrat datum. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2402) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Calendar.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#personalized-calendar-view-new-25)

**Důvod zobrazení pro data, která nelze upravovat:** Data mohou být v DHIS2 zablokována z mnoha důvodů, mimo jiné kvůli omezením přístupu nebo vypršení platnosti. Pokud událost, TEI nebo soubor dat nelze upravovat, uživatel bude moci najít důvod v sekci „Podrobnosti“. Možné důvody jsou:

-   Dokončení akce
-   Dokončení zápisu
-   Událost vypršela
-   Uzavřená organizační jednotka
-   Organizační jednotka mimo rozsah zachycení
-   Žádný přístup k zachycení dat v programu nebo datové sadě
-   Žádný přístup k možnosti kategorie v programu nebo datové sadě [Jira](https://jira.dhis2.org/browse/ANDROAPP-3565) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Non+Editable+Data.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#reason-for-non-editable-data-new-25)

**Upravte možnosti ovládacího panelu TEI podle konfigurace programu:** Možnosti nabízené na ovládacím panelu TEI budou přizpůsobeny konkrétní konfiguraci programu.

-   Karta Vztahy nebude viditelná, pokud nejsou nakonfigurovány vztahy programu.
-   Tlačítko Vytvořit událost bude skryté, když uživatel nemůže vytvořit další události na základě konfigurace trasovače.
-   Záložka Indikátory nebude viditelná, pokud program nemá nakonfigurovány žádné indikátory programu.
-   Filtr organizačních jednotek nebude viditelný, pokud má uživatel nakonfigurovanou pouze jednu organizační jednotku. [Jira](https://jira.dhis2.org/browse/ANDROAPP-4097) | [Jira 2](https://jira.dhis2.org/browse/ANDROAPP-3129) | [Jira 3](https://jira.dhis2.org/browse/ANDROAPP-4099) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/features-supported.html#tei-dashboard-navigation-panel-new-25)

## MAPY { #maps }

**Obecná uživatelská zkušenost s Mapami:** Po třech verzích od doby, kdy byly mapy zahrnuty do aplikace DHIS2 pro Android, jsme zkontrolovali a vylepšili uživatelskou zkušenost na základě zpětné vazby od komunity.
[Jira](https://jira.dhis2.org/browse/ANDROAPP-4024) | [Dokumentace]()

**Vycentrování pozice uživatele:** Pokud uživatel udělí aplikaci oprávnění k poloze, mapa zobrazí aktuální polohu znázorněnou jako modrý bod. Mapy v aplikaci DHIS2 Android Capture App nyní obsahují možnost vycentrovat mapu na místo uživatele. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3583) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-User+position.png)

## VLASTNOSTI TRASOVAČE { #tracker-features }

**Přidat podporu pro vztahy Event - TEI:** Aplikace nyní umožňuje uživatelům přidávat vztahy z jednotlivých událostí (Event programs) to TEIs. There is a new tab in the event dashboard, named relationships, that is active when it is configured in the server. This version does not allow relationships from TEIs to events or using events that belong to an enrollment. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2275) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Event+TEI+Relationships.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/features-supported.html#event-tei-relationships-new-25)

**NOVÝ filtr pro TEI označené jako následné:** V programech Tracker umožňuje filtr 'Následné' uživateli odfiltrovat TEI, které byly označeny jako 'Následné'. TEI mohou být označeny k sledování v TEI Dashbaord. [Jira](https://jira.dhis2.org/browse/ANDROAPP-3304) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.5/Android-2-5-Follow+Up+Filter.png) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#follow-up-new-25)

## DALŠÍ VLASTNOSTI { #other-features }

**Jazyk rozhraní založený na uživatelském jazyce DHIS2:** Jazyk rozhraní bude odpovídat jazyku nastavenému v uživatelské konfiguraci DHIS2. Pokud jazyk není v aplikaci dostupný, vybere se jazyk zařízení. Pokud není k dispozici žádná z jazykových konfigurací, aplikace se nastaví na angličtinu. Překlady nastavené v DHIS2 pro metadata se také zobrazí podle jazyka v uživatelské konfiguraci. [Jira](https://jira.dhis2.org/browse/ANDROAPP-2925) | [Dokumentace](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#interface-language-new-25)

## ÚDRŽBA { #maintenance }

**Kvalita / Zabezpečení / Výkon:** Seznam problémů souvisejících s kvalitou, zabezpečením a výkonem naleznete v tomto [jira filtru](https://jira.dhis2.org/issues/?filter=12204).

**Oprava chyb:** Seznam chyb opravených v této verzi naleznete po otevření tohoto [jira filtru](https://jira.dhis2.org/issues/?filter=12203).

## INFORMACE O VYDÁNÍ { #release-info }

| Informace o vydání | Odkaz |
| --- | --- |
| Stáhněte si aplikaci z Google Play nebo Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Dokumentace | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Podrobnosti o každé funkci v JIRA (vyžaduje přihlášení) | [2.5 Vlastnosti ](https://jira.dhis2.org/issues/?filter=12300) |
| Přehled opravených chyb na JIRA (vyžaduje přihlášení) | [2.5 Chyby](https://jira.dhis2.org/issues/?filter=12203) |
| Demo instance (uživatel / heslo) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Přihlašovací údaje: android / Android123 |
| Komunita DHIS 2 | [https://community.dhis2.org Mobilní komunita ](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Zdrojový kód na Githubu | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Zdrojový kód SDK na Githubu | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |

<!-- END-WEBSITE-SYNC-ID:android -->
