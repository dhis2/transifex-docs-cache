---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/app-android-settings-configuration.md"
revision_date: "2021-07-20"
---

# Webová aplikace pro nastavení Androidu { #capture_app_andoid_settings_webapp }

## Přehled { #capture_app_andoid_settings_webapp_overview }

Tato část se zaměřuje na implementaci webové aplikace Nastavení Android.

Webová aplikace Android Settings umožňuje správcům konfigurovat synchronizační parametry pro aplikaci DHIS2 Android Capture, zašifrovat místní databázi zařízení Android, přizpůsobit vzhled programů, datových sad a domovské obrazovky a přidat položky TEI Analytics. Konfigurační parametry definované v této webové aplikaci přepíší nastavení všech zařízení Android pomocí aplikace DHIS2 Android Capture.

Upozorňujeme, že v této verzi webové aplikace mohou tyto parametry v konfiguraci definovat pouze uživatelé s oprávněním „VŠE“. Ostatní uživatelé, kteří mají přístup k webové aplikaci, mohou vidět hodnotu parametrů, ale nemohou je upravovat.

> **Upozornění**
>
> Tato verze přichází s vylepšeními a rušivými funkcemi, takže předchozí verze již nejsou podporovány, nastavení v ní uložená budou odstraněna.

## Obecná nastavení { #capture_app_andoid_settings_webapp_general }

Zahrnuje konfigurace, jako je Matomo URL a ID projektu, počet vyhrazených hodnot ke stažení na TEI a šifrování databáze zařízení.

![](resources/images/capture-app-general-settings.png)

**Konfigurace Matomo:** Pokud již máte instanci Matomo, přidejte adresu Matomo URL a ID projektu.

**Konfigurace mobilního telefonu:** Tato část umožňuje uživatelům správce upravovat telefonní číslo odesílatele reklamní brány SMS.

**Rezervované hodnoty:** Tím se určí počet hodnot na atribut TEI vyhrazený ke stažení do zařízení.

**Šifrovat databázi zařízení:**

> **Upozornění**
>
> Toto je kritická akce a ovlivní místní databázi všech zařízení Android synchronizujících se se serverem (neovlivní serverovou databázi DHIS2).
>
> Ve výchozím nastavení není databáze aplikací pro Android šifrována, ale správce může zkontrolovat _Zašifrovat databázi zařízení_, aby zašifrovala metadata a data uložená v každém zařízení. Šifrování databáze bude mít dopad na objem databáze a výkon aplikace pro Android. Upozorňujeme, že v okamžiku výběru nebo zrušení této možnosti nedojde ke ztrátě dat (i když nebyla dříve synchronizována se serverem)

**Zakázat všechna nastavení:** Kliknutím na toto tlačítko uživatel odstraní všechna nastavení konfigurace systému Android. Na aplikaci Android Capture nebude použita žádná konfigurace (pokud je to tento případ, použijí se parametry synchronizace ty, které jsou definovány v aplikaci Android Capture).

## Synchronizace { #capture_app_andoid_settings_webapp_synchronization }

Nabízí další parametry pro řízení synchronizace metadat/dat.

### Globální { #capture_app_andoid_settings_webapp_synchronization_global }

**Metadata sync:** Admin users can choose how often the metadata will sync. např. Synchronizujte metadata každých 24 hodin.

**Synchronizace dat:** Správci mohou zvolit, jak často se budou data synchronizovat. např. Synchronizace dat každých 6 hodin.

![](resources/images/capture-app-sync-global.png)

### Program { #capture_app_andoid_settings_webapp_synchronization_program }

Tato sekce ovládá parametry synchronizace dat programu. Má sekci pro definování globálních nebo výchozích parametrů, které se mají použít při synchronizaci všech programů.

#### Globální nastavení { #capture_app_andoid_settings_webapp_synchronization_program_global }

Globální nastavení platí pro všechny programy, ke kterým má uživatel systému Android přístup.

![](resources/images/capture-app-program-global-settings.png)

**TEI ke stažení:** Maximální počet TEI ke stažení ze serveru.

**Období stahování TEI:** Stáhne TEI, které byly během období aktualizovány. např. TEI, které byly aktualizovány během minulého měsíce

**Událost ke stažení:** Maximální počet událostí ke stažení.

**Období stahování událostí:** Stáhne události, jejichž datum události náleží konkrétnímu období.

#### Specifické nastavení { #capture_app_andoid_settings_webapp_synchronization_program_specific }

Tato část umožňuje uživatelům správce určit chování konkrétního programu při synchronizaci dat. Specifická konfigurace přepíše obecné nastavení pro programy uvedené v této části. Přidání nastavení pro konkrétní program:

- Klikněte na _Přidat nastavení specifické pro program_, zobrazí se dialog.
- Pod nadpisem „Hodnoty na program“ klikněte a najděte seznam programů.
- Kliknutím na program se zobrazí různé parametry ke konfiguraci. Počet parametrů závisí na typu programu (s registrací nebo bez registrace).

**Nastavení programu bez registrace**

![](resources/images/capture-app-program-specific-dialog-without_registration.png)

**Nastavení programu s registrací**

![](resources/images/capture-app-program-specific-dialog-with_registration.png)

V případě, že byla uložena nějaká specifická nastavení, tabulka zobrazí souhrn s konkrétní konfigurací pro každý program a možnostmi, jak tato nastavení upravit nebo smazat.

![](resources/images/capture-app-program-specific-table.png)

> **Pozor**
>
> Použití specifických nastavení pro program může mít neočekávané výsledky v počtu stažených TEI a celkové množství může překročit hodnotu definovanou v Globálním nastavení. To je způsobeno tím, jak aplikace stahuje TEI ze serveru. Klient Android nejprve stáhne maximální počet TEI ze serveru na základě organizačních jednotek, ke kterým má uživatel přístup, a na základě pole lastUpdate. Poté stáhne maximální počet TEI ze specifických programů. Pokud tedy byly TEI stažené z globálního nastavení (500 ve výše uvedeném příkladu) aktualizovány nedávno než kterýkoli z TEI ze specifického programu (500 pro diagnostiku, léčbu a vyšetřování případů malárie), klient Android si nakonec stáhne 1 000 TEI.
>
> Zpočátku to může vypadat zmateně, ale jakmile to pochopíte, lze to použít k zajištění minimálního (a maximálního) počtu TEI pro konkrétní program, který bude stažen, což může být velmi užitečné v konkrétních implementacích.
>
> Představte si implementaci, kde musí být zajištěno, že uživatel Androidu má všechny TEI konkrétního programu na serveru, kde má stejný uživatel přístup k jiným organizačním jednotkám, kde mohou být jiné TEI zapsány v jiném programu. Program se jmenuje Komunitní péče a má 17 TEI, které byly aktualizovány již velmi dávno. Správce může zajistit stažení 17 TEI nastavením čehokoli v Globálním nastavení (v případě potřeby snížení šířky pásma by měla být nastavena velmi nízká hodnota) a alespoň 17 pro konkrétní program, jak ukazuje obrázek níže:
>
> ![](resources/images/capture-app-program-specific-example-web.png)
>
> Když je spuštěna počáteční synchronizace, zařízení Android nejprve stáhne poslední TEI aktualizované na serveru (které podle našeho příkladu nepatří do konkrétního programu) a za druhé až 20 TEI ze specifického programu, což má za následek následující (upozornění všechny TEI pro program byly staženy):
>
> ![](resources/images/capture-app-program-specific-example-mobile1.png)
>
> A když přejdete do nastavení, můžete ocenit, že celkový počet TEI je očekávaných 37, 20 z globálního nastavení a 17 z konkrétního programu.
>
> ![](resources/images/capture-app-program-specific-example-mobile2.png)

#### Resetujte všechny hodnoty { #capture_app_andoid_settings_webapp_synchronization_program_reset_all }

Kliknutím na _Resetovat všechny hodnoty_ obnoví uživatel správce výchozí hodnoty nastavení v sekci programu. Pamatujte, že v tomto případě to neznamená žádná konkrétní nastavení pro každý program.

Chcete-li uložit jakoukoli konfiguraci, musí uživatel správce kliknout na tlačítko _Uložit_ (toto tlačítko je zakázáno pro uživatele, kteří nemají oprávnění 'VŠECHNY')

### Datová sada { #capture_app_andoid_settings_webapp_synchronization_data }

Tato část řídí parametry synchronizace agregovaných dat.

#### Globální nastavení { #capture_app_andoid_settings_webapp_synchronization_data_global }

První část je pro globální nastavení, které platí pro všechny datové sady, ke kterým má uživatel Androidu přístup.

![](resources/images/capture-app-dataset-global-settings.png)

**Počet období:** Maximální počet období ke stažení.

#### Specifická nastavení { #capture_app_andoid_settings_webapp_synchronization_data_specific }

Přidání konkrétního nastavení:

- Klikněte na _Přidat nastavení specifické pro datovou sadu_, zobrazí se dialog se seznamem datových sad.
- Klikněte na datovou sadu a toto pole se automaticky doplní výchozí hodnotou podle typu období datové sady.

![](resources/images/capture-app-dataset-specific-dialog.png)

![](resources/images/capture-app-dataset-specific-table.png)

### Test synchronizace uživatele { #capture_app_andoid_settings_webapp_synchronization_user_sync_test }

Tato část kontroluje množství dat a metadat, které by uživatel synchronizoval se svým zařízením. Tento test můžete spustit u libovolného uživatele, ke kterému máte přístup. Tento test ukazuje počet organizačních jednotek, datových sad, programových pravidel, programů atd., ke kterým má uživatel Android přístup (tedy zdroje, které si aplikace pro Android stáhne), a velikost metadat a stažených dat (přibližný odhad ). Upozorňujeme, že ke spuštění tohoto testu uživatel nemusí mít oprávnění 'ALL'.

![](resources/images/capture-app-user-sync-test.png)

> **Poznámka:**
>
> Hodnoty, které jsou zvýrazněny červeně, jsou způsobeny tím, že hodnota je považována za vyšší než maximální doporučená hodnota.

## Vzhled { #capture_app_andoid_settings_webapp_appearance }

Tato nastavení poskytují kontrolu nad vzhledem formulářů pro zadávání dat a seznamů.

- Filtr: definuje filtry, které lze povolit v různých nabídkách aplikace.
- Kolektor dokončení: zapíná/vypíná číselník dokončení, který ukazuje průběh ve formuláři pro zadávání dat.

Tato nastavení se týkají vizuálních komponent, takže je aplikace musí využívat.

### Domovská obrazovka { #capture_app_andoid_settings_webapp_appearance_home_screen }

Umožňuje administrátorovi povolit nebo zakázat možnost zobrazení filtrů souvisejících s Datum, Organizační jednotka, Stav synchronizace a Přiřazeno mi na domovské obrazovce.

![](resources/images/capture-app-appearance-home.png)

### Program { #capture_app_andoid_settings_webapp_appearance_program }

Umožňuje správci určit, které filtry se mají zobrazit, a povolit nebo zakázat možnost zobrazení procenta dokončení formuláře pro zadávání dat.

#### Globální nastavení { #capture_app_andoid_settings_webapp_appearance_program_global }

Globální nastavení platí pro všechny programy, ke kterým má uživatel systému Android přístup.

![](resources/images/capture-app-appearance-program-global.png)

#### Specifické nastavení { #capture_app_andoid_settings_webapp_appearance_program_specific }

Tato sekce umožňuje administrátorovi přizpůsobit vzhled filtru a procentuálního dokončení. Chcete-li přidat konkrétní nastavení:

- Klikněte na _Přidat nastavení programu_ a objeví se dialogové okno.
- Klikněte na rozevírací seznam, který zobrazí seznam programů.
- Kliknutím na program se zobrazí různé filtry ke konfiguraci. Kombinovaný filtr kategorií závisí na názvu kombinace kategorií.

![](resources/images/capture-app-appearance-program-specific.png)

Pokud byla uložena nějaká specifická nastavení, tabulka shrnuje konkrétní konfiguraci podle programu a možnosti úpravy nebo odstranění těchto nastavení.

![](resources/images/capture-app-appearance-program-table.png)

### Datová sada { #capture_app_andoid_settings_webapp_appearance_data }

Umožňuje správcům povolit/zakázat filtry pro sekci datových souborů

#### Globální nastavení { #capture_app_andoid_settings_webapp_appearance_data_global }

První část je pro globální nastavení, které platí pro všechny datové sady, ke kterým má uživatel Androidu přístup.

![](resources/images/capture-app-appearance-dataset-global.png)

#### Specifické nastavení { #capture_app_andoid_settings_webapp_appearance_data_specific }

Přidání konkrétního nastavení:

- Klikněte na _Přidat nastavení datové sady_. Zobrazí se dialogové okno s rozevíracím seznamem datových sad.
- Klikněte na soubor dat a zobrazí se seznam možností povolení nebo zakázání filtrů.

![](resources/images/capture-app-appearance-dataset-specific.png)

![](resources/images/capture-app-appearance-dataset-table.png)

## Analytika { #capture_app_andoid_settings_webapp_analytics }

Nastavení analytiky definuje analytické položky TEI (grafy, tabulky), které se zobrazí uživateli. Rozsah analýzy je TEI, takže vizualizace se zobrazí na řídicím panelu TEI aplikace pro Android.

Jakákoli položka definovaná v aplikaci nastavení přepíše výchozí chování aplikace pro Android a zobrazí pouze položky definované v aplikaci nastavení. Účelem této části je definovat vizualizace pro zobrazení vývoje datových prvků a indikátorů programu v čase. Na základě toho vezme do úvahy pouze datové prvky, které patří do opakovatelné fáze programu, nebo programové indikátory, jejichž vzorec obsahuje alespoň jeden datový prvek, který patří do opakovatelné fáze programu.

Chcete-li vytvořit položku **TEI Analytika**:

- Klikněte na _Přidat TEI Analytics_. Zobrazí se dialogové okno s malým formulářem.
- Vyberte program a opakovatelnou fázi programu a vyplňte formulář. **Krátký název** je jediné nepovinné pole.
- Pokud byla vybrána jiná vizualizace položky než Výživa WHO, další pole k výběru jsou typ období (měsíční, týdenní, denní), typ prvku (indikátor programu, datový prvek) a prvek, který bude založen na prvku dříve vybraný typ. Pamatujte, že tyto prvky souvisí s programem a opakovatelnou fází programu zvolenou na začátku.

![](resources/images/capture-app-analytics-item.png)

Chcete-li vytvořit položku **WHO Nutrition Analytics**:

- Vyberte program, fázi programu a výživu WHO jako typ vizualizace.
- Vyberte typ vizualizace WHO, kterým může být výška k věku (HFA), hmotnost k věku (WFA) nebo hmotnost k výšce (WFH).
- Vyberte atribut trackedentity, který představuje pohlaví. Poté musíte zadat volbu pro Muž 'Mužský titul' a volbu pro Žena 'Titul pro ženu'. Normálně to budou kódy možností.
- Vyberte datový prvek/indikátor programu, který se zobrazí na vodorovné (x) ose
- Vyberte datový prvek/indikátor programu, který se zobrazí ve vertikální (y) ose

![](resources/images/capture-app-analytics-who-item.png)

Pokud byla vytvořena jakákoli položka TEI Analytics, tabulka zobrazí název položky a název programu a akční tlačítka pro odstranění nebo úpravu této položky.

![](resources/images/capture-app-analytics-table.png)

## Instalace { #capture_app_andoid_settings_webapp_installation }

Uživatel si může snadno nainstalovat webovou aplikaci pro nastavení systému Android, když se přihlásí k serveru DHIS2 a přejde do části **Správa aplikací**.

- Klikněte na **App Store**
- Přejít na _Android Nastavení App_
- Klikněte na _Install V2.0.0_

![](resources/images/capture-app-app-hub-install.png)

## Přihlaste se a proveďte první nastavení { #capture_app_andoid_settings_webapp_login }

Poté, co uživatel poprvé nainstaluje a spustí webovou aplikaci Android Settings, bude webová aplikace vyžadovat nastavení a uložení výchozích hodnot konfigurace. Tím se použijí výchozí nastavení pro všechna zařízení Android připojená k instanci.

![](resources/images/capture-app-first-time-setup.png)

> **Upozornění**
>
> Uvědomte si, že předchozí verze jsou zastaralé, takže začnete s novou výchozí konfigurací.

![](resources/images/capture-app-first-setup-with-deprecation-message.png)

> **Varování**
>
> Pouze uživatelé s oprávněním „VŠE“ budou moci _uložit nebo aktualizovat_ konfiguraci, ale každý uživatel bude mít přístup k zobrazení, jakmile bude vytvořen.

![](resources/images/capture-app-first-setup-no-authorities.png)

## Zadejte a uložte konfigurační parametry { #capture_app_andoid_settings_webapp_enter_and_save }

### Data store { #capture_app_andoid_settings_webapp_datastore }

Veškerá nastavení jsou interně uložena v [Datastore](https://docs.dhis2.org/master/en/developer/html/webapi_data_store.html) ve formátu JSON.

Struktura datového úložiště:

| Položka      | Popis                                 | Datový typ |
| --------- | ------------------------------------------- | --------- |
| Jmenný prostor | Jmenný prostor pro organizaci záznamů       | Řetězec    |
| Klíč       | Klíč pro identifikaci hodnot            | Řetězec    |
| Hodnota     | Hodnota obsahující informace pro záznam | JSON      |

### Uložte konfigurační parametry { #capture_app_andoid_settings_webapp_save_config }

V zápatí formuláře všech sekcí nastavení mohou uživatelé správce najít tlačítko _Uložit_.

![](resources/images/capture-app-save_button.png)

Pouze když uživatel s administrátorem klikne na toto tlačítko, všechny změny provedené v aktuální sekci se uloží do úložiště dat. Tyto změny se použijí na aplikace Android Capture, když synchronizují svou konfiguraci.

**Neuložené změny:**

V případě, že chce uživatel správce přejít do jiné sekce, pokud stále existují nějaké neuložené změny, zobrazí se před přechodem z aktuální sekce výstraha. V případě, že uživatel souhlasí s opuštěním stránky, neuložené změny budou ztraceny.

![](resources/images/capture-app-unsaved-changes.png)

#### Obnovte výchozí hodnoty všech hodnot { #capture_app_andoid_settings_webapp_reset_all }

Správce může nastavení kdykoli obnovit. V zápatí formuláře všech sekcí nastavení je tlačítko _Obnovit výchozí hodnoty všech hodnot_.

![](resources/images/capture-app-reset-default.png)

Výchozí hodnoty budou obnoveny pouze v Datastore a použity po kliknutí na _Uložit_.
