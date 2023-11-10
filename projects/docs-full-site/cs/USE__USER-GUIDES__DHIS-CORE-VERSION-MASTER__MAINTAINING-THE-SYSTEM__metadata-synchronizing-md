---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/user/configure-metadata-synchronizing.md"
revision_date: "2021-06-14"
tags:
    - Použití
    - Hlavní verze jádra DHIS
---

# Konfigurace synchronizace metadat { #metadata_sync }

## O synchronizaci dat a metadat { #about-data-and-metadata-synchronization }

Můžete synchronizovat data a metadata mezi různými instancemi DHIS2. Vzhledem ke dvěma instancím ve strategii centrálního a místního nasazení lze metadata vytvořená v centrálním systému synchronizovat s místním systémem a data vytvořená v místním systému lze synchronizovat s centrálním systémem. To může být užitečné, pokud máte více samostatných instancí DHIS2 a je třeba vytvořit globální metadata ve všech místních instancích.

![](resources/images/metadata_synchronization/dhis2_architecture.png)

Pokud k vytváření a aktualizaci metadat dochází v centrálním systému a pokud je povolena úloha synchronizace metadat, metadata se synchronizují dolů ke všem místním instancím, které jsou vázány k centrální instanci. Tyto místní instance zase zasílají hodnoty dat, data programu Události a Trasovač a dokončují sady registrace dat do centrální instance. Povolení nebo zakázání verzí synchronizace metadat v místní instanci nebude bránit procesu synchronizace metadat. Je to proto, že synchronizace metadat interaguje s koncovými body verzí centrální instance a ne s koncovými body místní instance.

Každý snímek generovaného exportu metadat je odkazován na verzi metadat. Nová verze metadat obsahuje pouze změny mezi předchozí verzí a aktuální verzí, to znamená, že jde o export mezi dvěma časovými razítky. Všechny verze metadat jsou udržovány v databázi DHIS2 a jsou k dispozici všem místním instancím, které se k ní připojují. Každou z místních instancí můžete naplánovat a stáhnout nové verze metadat. Doporučuje se udržovat velikost verzí metadat malou a logickou.

> **Varování**
>
> Každá instance DHIS2, ať už centrální nebo místní, může vytvářet verze metadat. Místní instance je určena k synchronizaci metadat z centrálního systému a nikoli k vytváření metadat sama o sobě.
>
> Pokud je v místní instanci vytvořena nová verze metadat, nemůže tato instance přijímat nové verze metadat z centrální instance, protože obsah verzí metadat bude mimo synchronizaci.
>
> Pokud jste vytvořili verze metadat v místní instanci, musíte tyto verze ručně odstranit z databáze, než budete moci synchronizovat s centrální instancí.
>
> Předpokládejme, že centrální a místní instance DHIS2 mají stejné snímky metadat až do verze 10. Poté místní instance vytvoří nový snímek s názvem verze 11. Poté centrální instance vytvoří nový snímek s názvem verze 11. Když se místní instance pokusí synchronizovat metadata , verze 11 není stažena. Obsah verze 11 v místní instanci však není totožný s obsahem verze 11 v centrální instanci.

> **Poznámka**
>
> Můžete také použít aplikaci **Import-Export** k ruční synchronizaci metadat.

## Pracovní postup { #workflow }

1.  V centrální instanci nakonfigurujte správu verzí metadat. Měli byste to udělat, jakmile centrální instance obsahuje metadata.

2.  Připojte místní instanci(e) k centrální instanci.

3.  Na místních instanci(ích) nakonfigurujte automatickou synchronizaci.

## Nakonfigurujte verzování metadat na centrální instanci { #configure-metadata-versioning-on-central-instance }

> **Poznámka**
>
> Pro synchronizaci metadat musí mít uživatelský účet centrálního systému následující oprávnění:
>
> **F_METADATA_MANAGE**
>
> Pouze uživatelé s tímto oprávněním pak budou moci vytvářet a stahovat metadata. To má zajistit bezpečnost centrálního systému, kde jsou metadata vytvořena. Místo toho, abyste poskytli pověření uživatele, který má VŠECHNO oprávnění, k instancím pole, musíte vytvořit uživatele, který má pouze toto konkrétní oprávnění.

1.  Na centrální instanci otevřete aplikaci **Nastavení systému** a klikněte na **Synchronizace**.

2.  Přejděte do části **Správa verzí metadat** a vyberte možnost **Povolit správu verzí pro synchronizaci metadat**.

    ![](resources/images/metadata_synchronization/metadata_versioning.png)

3.  (Volitelné) Vyberte **Nesynchronizovat metadata, pokud se liší verze DHIS2**.

4.  Vyberte typ verze metadat: **Nejlepší úsilí** nebo **Atomické**.

    -   _Nejlepší úsilí_ znamená, že pokud import metadat narazí na chybějící odkazy (například chybějící datové prvky při importu skupiny datových prvků), ignoruje chyby a pokračuje v importu.

    -   _Atomic_ znamená vše nebo nic - import metadat se nezdaří, pokud některý z odkazů neexistuje.

        > **Note**
        >
        > Each metadata entity is associated with a "User" object. If this "User" reference is missing while importing metadata version of type ATOMIC, the import will fail at the validation phase itself. This means that the user who creates metadata also needs to synchronize down to local instances to successfully import the metadata version of type ATOMIC.

5.  Klikněte na **Vytvořit novou verzi**. Nová verze je přidána do tabulky verzí.

## Připojte místní instanci k centrální instanci { #connect-local-instance-to-central-instance }

Chcete-li povolit synchronizaci metadat, musíte nakonfigurovat připojení mezi místní instancí a centrální instancí.

1.  V místní instanci otevřete aplikaci **Nastavení systému** a klikněte na **Synchronizace**.

2.  Přidejte podrobnosti místní instance DHIS2 do místní instance:

    -   **URL vzdáleného serveru**

    -   **Uživatelské jméno vzdáleného serveru**

    -   **Heslo vzdáleného serveru**

3.  Přejděte do části **Správa verzí metadat** a vyberte možnost **Povolit správu verzí pro synchronizaci metadat**.

4.  (Volitelné) Vyberte **Nesynchronizovat metadata, pokud se liší verze DHIS2**.

    Schéma metadat se mění mezi verzemi DHIS2, což může způsobit nekompatibilitu různých verzí metadat.

    Je-li tato možnost povolena, tato možnost neumožní synchronizaci metadat, pokud mají centrální a místní instance různé(ou) verze DHIS2. To platí pro synchronizaci metadat prováděnou prostřednictvím uživatelského rozhraní i rozhraní API.

    Jediným okamžikem, kdy může být užitečné tuto možnost deaktivovat, je synchronizace základních entit, například datových prvků, které se ve verzích DHIS2 nezměnily.

5.  (Volitelné) Konfigurujte e-mailová upozornění, abyste uživatele informovali o úspěšné nebo neúspěšné synchronizaci metadat:

    1.  Otevřete aplikaci **Nastavení systému** a klikněte na **E-mail**.

    2.  Zadejte **Název hostitele**, **Port**, **Uživatelské jméno**, **Heslo** and **Odesilatel E-mailu**.

    3.  Klikněte na **Server** a zadejte **e-mail pro systémová oznámení**.

        Na tuto e-mailovou adresu budete dostávat oznámení o stavu synchronizace metadat.

    > **Tip**
    >
    > When you receive email notification about a metadata synchronization failure, check which metadata version that causes the error and resolve it. Then you avoid future errors when the system downloads new metadata versions.

## Nakonfigurujte automatickou synchronizaci metadat na místní instanci { #configure-automatic-metadata-synchronization-on-local-instance }

Jakmile nakonfigurujete automatickou synchronizaci metadat (plánování) na místní instanci (y), spustí plánovač v daném konkrétním čase a synchronizuje (stáhne a importuje) metadata z centrální instance. Od uživatelů v místní instanci (instancích) není vyžadován žádný manuální zásah.

Poté, co plánovač dokončí synchronizaci metadat, bude mít místní instance metadata přesně tak, jak byla vytvořena v centrálním systému.

> **Poznámka**
>
> Hesla uživatelů nejsou synchronizována. Z bezpečnostních důvodů jsou anulovány. Po synchronizaci metadat musí administrátor tato hesla resetovat.

1.  V místní instanci otevřete aplikaci **Administrace dat** a klikněte na **Plánování**.

2.  V části **Synchronizace metadat** vyberte **Povoleno**.

3.  Vyberte časové období: **Denně**, **Týdně**, **Měsíčně** nebo **Ročně**.

    ![](resources/images/metadata_synchronization/metadata_sync.png)

4.  Klikněte na **Start**.

## Vytvořte novou verzi metadat ručně na centrální nebo místní instanci { #create-a-new-metadata-version-manually-on-central-or-local-instance }

1.  Otevřete aplikaci **Nastavení systému** a klikněte na **Synchronizace**.

2.  Přejděte do části **Správa verzí metadat** a vyberte možnost **Povolit správu verzí pro synchronizaci metadat**.

3.  (Volitelné) Vyberte **Nesynchronizovat metadata, pokud se liší verze DHIS2**.

4.  Vyberte **Nejlepší úsilí** nebo **Atomický**.

5.  Klikněte na **Vytvořit novou verzi**. Nová verze je přidána do tabulky verzí.

Když je systém _centrální instancí_, uvidíte v tabulce verzí tři sloupce:

![](resources/images/settings/metadata_versioning_table.png)

| Objekt | Popis |
| --- | --- |
| Hlavní verze | Nejnovější verze v systému. |
| Verze | Název verze. Název je automaticky generován systémem. |
| Když | Časové razítko vytvoření verze metadat v centrální instanci. |
| Typ | Typ verze metadat. |

Když je systém _lokální instancí_, uvidíte v tabulce verzí čtyři sloupce:

![](resources/images/settings/metadata_versioning_table_failure_case.png)

| Objekt | Popis |
| --- | --- |
| Hlavní verze | Nejnovější verze centrální instance. <br> <br> **Poznámka** <br> <br> Informace o hlavní verzi jsou nejnovější verzí centrální instance. To je důležité, abyste se podívali na rozdíl mezi verzemi metadat, která existují na centrální a na místní úrovni. |
| Poslední pokus o synchronizaci | Pokud je poslední pokus o synchronizaci neúspěšný, zobrazí se toto. |
| Verze | Název verze. Název je automaticky generován systémem. |
| Když | Časové razítko vytvoření verze metadat v centrální instanci. |
| Typ | Typ verze metadat. |
| Poslední synchronizace | Časové razítko, kdy došlo k poslední synchronizaci této verze v tomto systému. |

## Referenční informace: konfigurační parametry synchronizace metadat { #reference-information-metadata-synchronization-configuration-parameters }

Proces, který provádí synchronizaci metadat, se nazývá Metadata Sync Task. Tento úkol provádí před synchronizací metadat řadu kroků:

-   Odeslat data (agregovaná data a data anonymních událostí) z místní instance do centrální instance.

-   Získá aktuální verzi metadat místní instance. Poté použije tuto informaci o verzi jako základnu k načtení seznamu verzí metadat vytvořených po základně.

-   Pokud jsou v centrální instanci vytvořeny nové verze, provede synchronizaci verzí metadat jednu po druhé. Po každé úspěšné synchronizaci verze metadat v místní instanci bude nakonfigurovanému uživateli (pokud existuje) odeslán e-mail.

Jakmile je úloha synchronizace metadat spuštěna v naplánovaném čase, může se úloha pokusit znovu (pokud některý z kroků selže) na základě konfigurace následujících parametrů definovaných v souboru `dhis.conf`:

| Parametr                                     | Výchozí hodnota |
| --------------------------------------------- | ------------- |
| `metadata.sync.retry`                         | 3             |
| `metadata.sync.retry.time.frequency.millisec` | 30000         |

Každé opakování bude provedeno po zadaném čase (v milisekundách). Pokud kroky stále selžou i po všech opakováních, plánovač zastaví jeho provádění a poté bude nakonfigurovanému uživateli (pokud existuje) odeslána e-mail. Pokud nejsou zadány žádné hodnoty, budou použity výchozí hodnoty.

`metadata.sync.retry` = 5

`metadata.sync.retry.time.frequency.millisec` = 10000
