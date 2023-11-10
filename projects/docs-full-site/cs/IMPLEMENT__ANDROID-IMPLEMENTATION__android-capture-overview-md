---
edit_url: "https://github.com/dhis2/dhis2-android-docs/blob/main/content/implementation-guide/dhis2-capture-android-overview.md"
revision_date: '2022-01-07'
tags:
- Implementace
---

# Přehled DHIS 2 Capture pro Android { #implementation_guide_overview }

Tento dokument se zaměřuje na mobilní implementaci, která využívá novou aplikaci pro Android DHIS 2 Capture. Další informace o různých aplikacích DHIS 2 pro Android najdete v [App Store](https://www.dhis2.org/app-store) a v [Dokumentaci](https://www.dhis2.org/android-documentation) na webových stránkách. Předchozí sada vyvinutých aplikací DHIS 2 pro Android je aktuálně na plánovaném ukončení podpory a pouze s podporou opravné údržby:

* Aplikace Ovládací panel: Podpora byla ukončena od března 2020
* Aplikace Trasovač a Události: zastaralé od června 2020
* Aplikace Sběr dat: Plánované ukončení podpory od září 2020

Nová aplikace pro Android DHIS 2 Capture umožňuje offline sběr dat ve všech datových modelech DHIS 2\*. Data a metadata se automaticky synchronizují, kdykoli je přístup k internetu, přičemž se vždy zachovávají nejdůležitější data pro přihlášeného uživatele v místním zařízení.

## Snazší přihlášení a vylepšená ochrana dat { #implementation_guide_overview_easier }


URL serveru lze nastavit pomocí QR kódu. Aplikace si také zapamatuje dříve použité adresy URL a uživatelská jména. Jakmile je uživatel přihlášen, lze pomocí čtyřmístného kódu PIN zabezpečit aplikaci měkkým odhlášením.


## Konfigurovatelné téma aplikace a ikona { #implementation_guide_overview_configurable }


Vzhled aplikace, včetně ikony a barvy, je určen konfigurací serveru. Pomocí widgetu aplikace můžete vytvořit zástupce aplikace s logem vaší instituce na domovské obrazovce mobilního zařízení.

![](resources/images/implementation-guide-login.gif){ .center width=25% }

## Atraktivní, uživatelsky přívětivá navigace { #implementation_guide_overview_attractive }


Všechny programy a datové sady\* přístupné přihlášenému uživateli jsou integrovány do nové domovské obrazovky. Každý program nebo datová sada bude zobrazena s příslušnou ikonou a barvou.

![](resources/images/implementation-guide-user_friendly.gif){ .center width=25% }

## Plně funkční v režimu offline: inteligentní synchronizace { #implementation_guide_overview_fully_functional }


Místní databáze v mobilním zařízení uchovává synchronizovanou kopii programů a datových sad DHIS 2 dostupných pro přihlášeného uživatele. Nejrelevantnější data se také automaticky synchronizují.

* Trasované entity: ve výchozím nastavení až 500 aktivních registrací s upřednostňováním naposledy aktualizovaných uživatelských organizačních jednotky(ek) pro sběr dat.
* Události a datové sady: ve výchozím nastavení nejnovějších 1 000 událostí nebo 500 datových sad.

> **Poznámka**
> Tyto parametry jsou konfigurovatelné

## Ovládací panel trasovače { #implementation_guide_overview_tracker_dashboard }


Výkonný datový model trasovače DHIS 2 byl plně implementován na malé obrazovce. Ovládací panel trasovače zahrnuje zpětnou vazbu, vztahy, indikátory a poznámky.

Aplikace implementuje logiku trasovače podporou většiny pravidel programu, což umožňuje přidávat, plánovat nebo odkazovat na nové události v závislosti na konfiguraci serveru.

![](resources/images/implementation-guide-tracker_search.png){ .center width=25% }

## Integrované vyhledávání pro trasovač { #implementation_guide_overview_integrated_search }


Než bude možné přidat novou trasovanou entitu, aplikace automaticky provede vyhledávání. Pokud je offline, hledání je v místní synchronizované databázi. a když bude online, navrhne záznamy ke stažení na základě konfigurace vyhledávání organizační jednotky uživatele. Tato funkce minimalizovala potenciální duplikáty, i když je uživatel offline.

## Zadání obrazových dat { #implementation_guide_overview_pictorial }


Zadávání dat ožívá - k ilustraci odpovědí na otázky lze použít ikony a barvy. K dispozici pro datové prvky s přidruženými sadami možností v programech pro jednotlivé události i pro sledování.

![](resources/images/implementation-guide-pictorial_entry.gif){ .center width=25% }

## Úplnost události { #implementation_guide_overview_event_completeness }


Během zadávání dat bude aplikace zobrazovat informace o aktuálním stavu dokončení programové fáze. Užitečné pro komplexní průzkumy s více oddíly.

