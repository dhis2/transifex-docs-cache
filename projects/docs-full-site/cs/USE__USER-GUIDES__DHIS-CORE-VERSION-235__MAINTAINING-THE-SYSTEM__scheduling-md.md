---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/scheduling.md"
revision_date: "2021-06-14"
---

# Plánování { #scheduling }

Plánovač je aplikace pro správu úloh na pozadí v DHIS2. Úlohy na pozadí mohou provádět řadu úkolů, například spouštět analytiku, synchronizovat data a metadata nebo odeslat zprávu s analýzou push. Aplikace poskytuje možnost vytvářet, upravovat a mazat takové úlohy.

Plánovač je dodáván s DHIS2 a je přístupný prostřednictvím nabídky aplikace.

![](resources/images/scheduler/overview.png)

Úvodní stránka aplikace Plánovač zobrazuje přehled stávajících úloh. Ve výchozím nastavení jsou předdefinované systémové úlohy skryty. Chcete-li je zobrazit, přepněte možnost _Zobrazit systémové úlohy_ v pravém horním rohu.

Když vytvoříte nebo upravíte úlohu, bude znovu naplánována podle vybraných předvoleb. Chcete-li spustit úlohu na vyžádání, stiskněte zelený trojúhelník označený „Spustit nyní“. Tato akce je k dispozici pouze pro povolené úlohy.

## Vytváření úloh { #scheduling_create_job }

1.  Otevřete aplikaci **Plánovač** a klikněte na tlačítko Přidat v pravém dolním rohu.

2.  Vyberte vhodný **název** pro novou úlohu.

3.  Vyberte frekvenci běhu úlohy, tj. Kdy a jak často by úloha měla běžet.

    1.  Můžete buď vybrat předdefinovanou frekvenci z rozevírací nabídky, nebo

    2.  Úloze můžete dát vlastní **výraz Cron**, pokud chcete konkrétní plán, pomocí [Jarní plánování](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/scheduling/support/CronSequenceGenerator.html) syntaxe.
    3.  Povolením možnosti **Průběžné provádění** bude úloha spuštěna neustále. Jinými slovy, jakmile úloha skončí, bude naplánováno její okamžité opětovné spuštění. Výběr této možnosti zakáže ostatní pole.

4.  V rozbalovací nabídce vyberte **typ úlohy**, který chcete naplánovat.

5.  Pokud je typ úlohy přizpůsobitelný, níže se zobrazí část **Parametry**. Tyto další možnosti určují podrobnosti naplánované úlohy a budou se velmi lišit v závislosti na typu úlohy.

6.  Stisknutím tlačítka **Přidat úlohu** potvrďte vytvoření úlohy. Nově vytvořená úloha by nyní měla být uvedena v přehledu úloh, protože není povoleno nastavení **Zobrazit systémové úlohy**.

![](resources/images/scheduler/add_new_job.png)

Úlohy jsou ve výchozím nastavení povoleny.

## Konfigurace úlohy { #scheduling_configure_job }

Se správnými oprávněními můžete upravit podrobnosti o úlohách vytvořených uživateli. U systémových úloh lze změnit pouze plán (výraz cron).

Chcete-li rychle povolit nebo zakázat spuštění úlohy vytvořené uživatelem, použijte sloupec **Povoleno** na vstupní stránce aplikace Plánovač. Systémové úlohy jsou vždy povoleny.

Další konfigurace úlohy:

1.  Vyberte úlohu na vstupní stránce, odhalte **atributy** a podle toho je změňte. V předchozí části najdete podrobnosti plánování.

2.  Pokud typ úlohy podporuje další možnosti, bude k dispozici také část **Parametry**.

3.  Po dokončení změny uložte stisknutím tlačítka **Uložit změny**.

## Mazání úlohy { #dataAdmin_scheduler_delete }

1.  Vyberte úlohu, kterou chcete odstranit.

2.  Stiskněte tlačítko **Odstranit** v pravém dolním rohu.

3.  Potvrďte dalším stisknutím tlačítka **Odstranit** ve vyskakovacím okně.

![](resources/images/scheduler/delete_job.png)

## Typy pracovních míst { #job-types }

Následující část popisuje různé typy úloh.

### Tabulka zdrojů { #scheduling_resource_table }

Úloha tabulky prostředků je zodpovědná za generování a aktualizaci tabulek databáze prostředků. Tyto tabulky používají různé komponenty v DHIS 2 a jsou určeny ke zjednodušení dotazů na databázi.

Všimněte si, že při zadávání kterékoli z úloh analytické tabulky mohou být tabulky zdrojů součástí procesu a není nutné specifikovat také úlohu tabulky zdrojů.

### Tabulka Analytiky { #scheduling_analytics_table }

Úloha analytických tabulek je zodpovědná za generování a aktualizaci analytických tabulek. Analytické tabulky se používají jako základ pro dotazy na analýzu dat v DHIS2. Aplikace, jako je ovládací panel, vizualizér a mapy, načítají data z těchto tabulek prostřednictvím analytického API DHIS2 a je nutné je aktualizovat, aby byla dostupná analytická data. Tento proces můžete naplánovat tak, aby se pravidelně spouštěl prostřednictvím typu úlohy analytické tabulky.

Úloha analytické tabulky se ve výchozím nastavení naplní daty pro všechny roky a datové prvky. K dispozici jsou následující parametry:

-   **Last years:** Počet posledních let pro naplnění analytických tabulek. Jako příklad, pokud zadáte 2 roky, proces aktualizuje data za poslední dva roky, ale neaktualizuje starší data. Tento parametr je užitečný ke zkrácení času potřebného na dokončení procesu, a je vhodný, pokud se starší data nezměnila a při aktualizaci nejnovějších dat je žádoucí.
-   **Přeskočit tabulky zdrojů:** Přeskočí tabulky zdrojů během procesu aktualizace analytické tabulky. To snižuje čas potřebný k dokončení procesu, ale vede ke změnám metadat, které se v analytických datech neprojeví.
-   **Přeskočit typy tabulek:** Přeskočit jeden nebo více typů analytické tabulky. To snižuje čas potřebný k dokončení procesu, ale vede k tomu, že tyto datové typy nebudou v analytických datech aktualizovány.

### Kontinuální analytická tabulka { #scheduling_continuous_analytics_table }

Úloha analytických tabulek je zodpovědná za generování a aktualizaci analytických tabulek. Analytické tabulky se používají jako základ pro dotazy na analýzu dat v DHIS2. Aplikace, jako je ovládací panel, vizualizér a mapy, načítají data z těchto tabulek prostřednictvím analytického API DHIS2 a je nutné je aktualizovat, aby byla dostupná analytická data. Tento proces můžete naplánovat tak, aby se pravidelně spouštěl prostřednictvím typu úlohy analytické tabulky.

Kontinuální úloha analytické tabulky je založena na dvou fázích:

-   _Poslední aktualizace:_ Aktualizace nejnovějších dat, kde nejnovější odkazuje na data, která byla přidána, aktualizována nebo odstraněna od poslední aktualizace nejnovějších dat nebo úplných dat. K tomuto procesu musíte často.
-   _Úplná aktualizace:_ Aktualizace všech dat za všechny roky. Tento proces proběhne jednou denně.

Kontinuální úloha analytické tabulky často aktualizuje nejnovější data. Proces nejnovějších dat využívá speciální databázový oddíl, který slouží pouze k uložení nejnovějších dat. Tento oddíl lze rychle aktualizovat kvůli relativně malému množství dat. Velikost oddílu se bude zvětšovat, dokud nebude provedena úplná aktualizace. Jednou denně budou aktualizována všechna data za všechny roky. Tím se vymaže nejnovější oddíl.

Úloha analytické tabulky se ve výchozím nastavení naplní daty pro všechny roky a datové prvky. K dispozici jsou následující parametry:

-   **Hodina dne úplné aktualizace:** Hodina dne, kdy bude provedena úplná aktualizace. Jako příklad, pokud zadáte 1, bude úplná aktualizace provedena v 1:00.
-   **Last years:** Počet posledních let pro naplnění analytických tabulek. Jako příklad, pokud zadáte 2 roky, proces aktualizuje data za poslední dva roky, ale neaktualizuje starší data. Tento parametr je užitečný ke zkrácení času potřebného na dokončení procesu, a je vhodný, pokud se starší data nezměnila a při aktualizaci nejnovějších dat je žádoucí.
-   **Přeskočit tabulky zdrojů:** Přeskočí tabulky zdrojů během procesu aktualizace analytické tabulky. To snižuje čas potřebný k dokončení procesu, ale vede ke změnám metadat, které se v analytických datech neprojeví.

### Synchronizace dat { #scheduling_data_sync }

DHIS2 poskytuje synchronizaci dat mezi vzdáleně distribuovanými instancemi a centrální instancí DHIS2. To může být užitečné např. když jste nasadili více samostatných instancí DHIS2, které jsou požadovány k odeslání datových hodnot do centrální instance DHIS2. Podporována jsou jak data trasovače, tak synchronizace agregovaných dat.

Toto jsou kroky k povolení synchronizace dat:

-   Přejděte na Nastavení synchronizace, zadejte adresu URL vzdáleného serveru, uživatelské jméno a heslo. Stisknutím tlačítka TAB automaticky uložíte nové heslo. Obnovte stránku a zkontrolujte, zda jsou vyplněné hodnoty stále přítomny. Všimněte si, že pole pro heslo bude po aktualizaci prázdné, protože tato hodnota je šifrována, takže ji můžete považovat za uloženou.

-   Pomocí aplikace Plánovač vytvořte novou úlohu pomocí typu úlohy „Události programů Synchronizace Dat“ nebo „Trasovač programů Synchronizace Dat“. Po dokončení se ujistěte, že je povoleno. (Poznámka: Pokud byla úloha „Program Synchronzace Dat“, dostupná v předchozích verzích, nastavena v aplikaci Plánovač dříve, byla automaticky nahrazena dvěma novými úlohami „Události programů Synchronizace Dat“ a „Trasovač programů Synchronizace Dat“ se stejnými nastavení.)

Některé aspekty funkce synchronizace dat je třeba mít na paměti:

-   Místní instance DHIS2 uloží heslo uživatelského účtu na vzdálené instanci šifrované v místní databázi. Vzdálený účet se používá k ověření při přenosu dat. Z bezpečnostních důvodů nezapomeňte nastavit _encryption.password_ konfigurační parametr v _hibernate.properties_ na silné heslo.

-   Nasazení vzdáleného serveru na SSL / HTTPS se důrazně doporučuje, protože uživatelské jméno a heslo se odesílají prostým textem pomocí základního ověřování a mohou být zachyceny útočníkem.

-   Synchronizace dat používá k identifikaci metadat vlastnost UID datových prvků, kombinací možností kategorie a organizačních jednotek. Synchronizace tedy závisí na harmonizaci těchto tří metadatových objektů v místní a vzdálené instanci, aby správně fungovala.

-   Při prvním spuštění synchronizační úlohy DHIS2 bude obsahovat všechna dostupná data. Následné úlohy synchronizace budou zahrnovat pouze data přidaná a změněná od poslední úspěšné úlohy. Úloha synchronizace je považována za úspěšnou, pouze pokud byla všechna data úspěšně uložena na vzdáleném serveru (všechna úspěšně synchronizovaná data zůstanou na přijímající instanci, bez ohledu na to, zda úloha nakonec selže). O tom, zda byla úloha úspěšná nebo ne, lze rozhodnout ze souhrnu importu vráceného z centrálního serveru.

-   Úloha počáteční synchronizace může trvat značné množství času, což může zpomalit vaši instanci, v závislosti na tom, kolik dat se synchronizuje. Může být dobrý nápad nakonfigurovat úlohu tak, aby se spouštěla, když je málo uživatelů online, a později ji změnit podle svých vlastních preferencí. Pokud nechcete nebo nepotřebujete synchronizovat všechna data, máte možnost <a href="#skip_changed_before">přeskočit některá synchronizovaná data</a>.

    Když DHIS2 synchronizuje trasovací data, určuje sadu dat k synchronizaci na základě poslední synchronizace. Každá z trasované instance entity a události má své vlastní záznamy o tom, kdy byly naposledy úspěšně synchronizovány.

-   Systém spustí synchronizační úlohu na základě pravidel nastavených v konfiguraci úlohy. Pokud se synchronizační úloha spustí, když není žádné připojení ke vzdálenému serveru, bude to opakovat až třikrát, než se přeruší. Úloha bude spuštěna znovu v naplánovaném čase.

-   Server zpracovává každou sadu programů samostatně, což znamená, že jednu sadu programů lze úspěšně synchronizovat, zatímco druhá selže. Selhání nebo úspěch jednoho neovlivní druhého, protože čas poslední úspěšné synchronizace je sledován jednotlivě pro každou položku, jak již bylo zmíněno dříve.

-   Atributy TrackedEntityInstances (TrackedEntityAttribute) a datové prvky ProgramStages (ProgramStageDataElement), které mají zapnutou možnost „Přeskočit synchronizaci“, nebudou synchronizovány. Tato funkce vám umožňuje rozhodnout se nesynchronizovat některá citlivá nebo nerelevantní data a ponechat je pouze lokálně.

-   Mělo by se použít oprávnění `Ignorovat ověření požadovaných polí v nástroji Trasovač a Zachycení Události` (`F\_IGNORE\_TRACKER\_REQUIRED\_VALUE\_VALIDATION`) pokud existuje požadavek, aby některý povinný atribut / datový prvek současně měl Vlastnost „Přeskočit synchronizaci“ je zapnutá. Takové nastavení povede k selhání ověření na centrálním serveru, protože daný atribut / datový prvek nebude v užitečném obsahu přítomen.

    Ověření se nezdaří u uživatele s tímto oprávněním. Oprávnění by mělo být přiděleno uživateli na centrálním serveru, který bude použit pro synchronizační úlohu.

-   Ve specifických případech může být **počáteční synchronizace všech dat nežádoucí**; například když je databáze v místní instanci novou kopií databáze přítomné v centrální instanci, nebo když je upřednostňováno nesynchronizovat stará data ve prospěch počáteční synchronizace, která zabere méně času.

    _SyncSkipSyncForDataChangedBefore_ SettingKey lze použít k přeskočení synchronizace všech dat (datové hodnoty, data programu Události a Trasovač, registrace úplných datových sad), která byla _posledně změněna před stanoveným datem_. V synchronizační úloze se po celou dobu používá klíč `SettingKey`. Pokud tedy potřebujete synchronizovat stará data, měli byste změnit `SettingKey`.

-   Synchronizační úloha Trasovacích programů a Programů Událostí podporuje stránkování, aby se zabránilo vypršení časového limitu a řešení nestabilní sítě. Výchozí velikost stránky pro úlohu „Události programů synchronizace dat“ je nastavena na 60. Výchozí velikost stránky pro úlohu „Synchronizace dat programů sledování“ je nastavena na 20.

    Pokud výchozí hodnoty neodpovídají vašemu účelu, lze vlastní velikost stránky zadat pomocí parametru v konkrétní synchronizační úloze v aplikaci Plánovač.

### Plánování synchronizace metadat { #scheduling_metadata_sync }

DHIS2 poskytuje funkci pro synchronizaci metadat ze vzdálené instance do místní instance DHIS2. To může být užitečné, když jste nasadili více samostatných instancí DHIS2 a potřebujete vytvořit metadata ve všech místních instancích podobných centrální instanci DHIS2.

Toto jsou kroky k povolení synchronizace metadat:

-   Přejděte na Nastavení \> Synchronizace, zadejte adresu URL vzdáleného serveru, uživatelské jméno a heslo a klikněte na Uložit.

-   Přejděte na Správa metadat \> Plánování. V části Strategie nastavení synchronizace metadat na Povoleno vyberte časové období a klikněte na Start.

Mějte na paměti některé aspekty funkce synchronizace metadat:

-   Místní instance DHIS2 uloží heslo uživatelského účtu vzdálené instance do své databáze. Účet vzdáleného uživatele se používá k ověřování při přenosu / stahování dat. Z bezpečnostních důvodů nezapomeňte nastavit _encryption.password_ konfigurační parametr v _hibernate.properties_ na silné heslo.

-   Nasazení vzdáleného serveru na SSL / HTTPS se důrazně doporučuje, protože uživatelské jméno a heslo se odesílají prostým textem pomocí základního ověřování a mohou být zachyceny útočníkem.

-   Také se ujistěte, že vzdálený uživatel nemá VŠECHNA oprávnění, místo toho jednoduše vytvořte uživatele s oprávněním F_METADATA_MANAGE, takže i když tyto údaje zachytí hacker, nemůžete mít plnou kontrolu nad vzdáleným systémem.

-   Synchronizace metadat závisí na podkladové importní vrstvě. Každá verze metadat představuje export metadat mezi dvěma danými časovými značkami. Každá synchronizace verze metadat je pokusem importovat tento snímek metadat do místní instance. Synchronizace verzí je přírůstková. Místní instance se pokusí postupně stáhnout verze metadat z centrální instance. Selhání synchronizace konkrétní verze metadat neumožní synchronizaci pokračovat do dalších verzí. V případě selhání je nutné provést příslušné změny v metadatech na centrální úrovni, aby bylo zajištěno vyřešení chyby. Konfigurace metadat je zásadní a uživatel by měl být při zavádění aktualizací do produkce opatrný. Vždy se doporučuje zavést pracovní prostředí, aby byla zajištěna nezávadnost verzí metadat a jejich následný dopad. Místní instance synchronizuje metadata z první verze, aby byla zachována harmonie a místní a centrální instance budou fungovat odpovídajícím způsobem.

-   Systém se pokusí o synchronizaci v naplánovaném čase. Pokud místní nebo vzdálený server v tuto chvíli nemá funkční připojení k Internetu, synchronizace bude přerušena a znovu proveden pokus podle počtu opakování, jak je uvedeno v souboru _dhis.conf_.

-   Čas poslední úspěšné synchronizace se vzdáleným serverem můžete vidět na obrazovce plánování vedle štítku „Poslední úspěch“.
