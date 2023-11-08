---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/new-android-specific-features.md"
revision_date: "2021-07-29"
---

# Obecné funkce { #capture_app_generic }

## Přihlášení { #capture_app_generic_login }

Existují dva způsoby přístupu k aplikaci:

1. Ručně: Uživatel musí zadat odpovídající adresu URL serveru, který má být použit, a zadat uživatelské jméno a heslo.

   > **Note**
   >
   > Take note that login is only possible with servers from version 2.29.

2. QR: Uživatel může místo psaní adresy URL použít QR kód. Uživatelské jméno a heslo je nutné zadat ručně.

   > **Note**
   >
   > After the first login, the app will suggest URL and username of all successful connections.
   >
   > You are able to make an _offline_ login only if using the same user as the last online session.

![](resources/images/capture-app-image62.PNG){ width=25%}
![](resources/images/capture-app-image63.jpg){ width=25%}

> **Upozornění**
>
> Ve verzích DHIS2 až do 2.30, pokud se uživatel pokusí o on-line přihlášení a jeho účet byl deaktivován, jak je vysvětleno v [DHIS 2 Manual – Disable User](https://docs.dhis2.org/master/en/user /html/dhis2_user_manual_en_full.html#disable_user) všechna data budou z telefonu vymazána. Ujistěte se, že před deaktivací uživatele byla všechna data synchronizována nebo že tuto funkci používáte ke vzdálenému vymazání citlivých dat v případě ztráty zařízení.
>
> Kvůli změně přihlašovacího API není tato funkce dostupná ve verzích 2.31 a vyšších.

## Obnova účtu { #capture_app_generic_recovery }

Uživatelé budou moci obnovit své vlastní heslo, pokud mají povolené nastavení: Povoleno Obnovení uživatelského účtu.

![](resources/images/capture-app-image64.PNG){ width=25%}

## Blokování relace (PIN) { #capture_app_generic_PIN }

Uživatel je schopen relaci uzamknout pomocí 4-místného kódu PIN. To umožňuje přesunout se do jiných aplikací v telefonu, aniž byste odstranili místní data. Pokud uživatel zapomene číslo PIN, je k dispozici také přihlášení zadáním přihlašovacích údajů.

![](resources/images/capture-app-image65.PNG){width=25%}
![](resources/images/capture-app-image63.jpg){width=25%}

## Otisk prstu { #capture_app_generic_fingerprint }

Pokud je funkce v zařízení aktivována, může uživatel používat snímač otisků prstů.

- Když je povolen snímač otisků prstů, a ne PIN, pokaždé, když se aplikace zavře, přejde na pozadí nebo je zařízení blokováno, relace bude uzamčena. Jakmile je aplikace znovu otevřena, uživatel musí klepnutím na ikonu otisku prstu aktivovat snímač.
- Pokud je nastaven PIN a otisk prstu, bude při uzamčení relace a opětovném otevření aplikace uživatelem PIN vyzván.

![](resources/images/capture-app-image104.jpg){width=25%}
![](resources/images/capture-app-image105.jpg){width=25%}

## Pokyny / informační tlačítka { #capture_app_generic_instructions }

Kontextový průvodce je k dispozici v podrobnostech události a na obrazovce řídicího panelu TEI.

![](resources/images/capture-app-image42.jpg){width=25%}
![](resources/images/capture-app-image66.png){width=25%}

> **Tip**
>
> Uživatel je schopen znovu otevřít pokyny <!-- PALD: unnecessary: (trigger)--> kliknutím na tři tečky v pravém horním rohu obrazovky.

## Filtr { #capture_app_generic_filter }

<!-- PALD alternative: "Filtr umožňuje zúžit data dostupná z ..." -->

Aplikace má nové a vylepšené filtry pro všechny obrazovky se seznamem (domov, seznam událostí, vyhledávání tei a datové sady).

Filtrovat podle období, org. Jednotka, stav synchronizace, stav události, kombinace možností kategorie a „přiřazeno ke mně“.

![](resources/images/capture-app-image19.png){ width=25%}
![](resources/images/capture-app-image97.png){ width=25%}
![](resources/images/capture-app-image123.png){ width=25%}
![](resources/images/capture-app-image134.png){ width=25%}

Filtry se přizpůsobí různým programům a souborům dat.

1. Program bez registrace: Datum, Org. jednotka, stav synchronizace, stav události a kombinace kategorií.
2. Program s registrací: Datum akce, Datum přihlášení, Org. Unit, Sync, Enrollment Status, Event Status a Assigned to me. Ikona filtru se zobrazí pouze v případě, že je k dispozici seznam událostí (funkce zobrazení seznamu na úvodní stránce nebo vyhledávání)
3. Datové Sady: období, Org. jednotka a Stav synchronizace.

### Přiřazeno ke mně { #capture_app_generic_filter_assigned }

Je možné filtrovat události na základě jejich přiřazení aktuálnímu uživateli. Filtr „Přiřazeno mně“ byl přidán do seznamu jednotlivých událostí, seznamu TEI a ovládacího panelu TEI a zobrazení mapy. Zobrazí se pouze v případě, že je aktivní program nakonfigurován pro přiřazování událostí uživatelům.

### Datum události / datum / období { #capture_app_generic_filter_date }

Filtrujte události, TEI (na základě jejich událostí) a datové sady, jsou k dispozici následující časové úseky:

- Dnes
- Tento týden
- Tento měsíc
- Včera
- Minulý týden
- Minulý měsíc
- Zítra
- Příští týden
- Příští měsíc
- Od-do
- Jiný (otevře výběr data)
- Kdykoli

### Org. Jednotka { #capture_app_generic_filter_orgunit }

Umožňuje uživateli zadat vyhledávání nebo vybrat organizační jednotku ze stromu.

### Synchronizace { #capture_app_generic_filter_sync }

Filtrovat podle

- Synchronizované (události, TEI, datové sady)
- Nesynchronizováno
- Chyba synchronizace
- SMS synchronizováno

### Stav události { #capture_app_generic_filter_event }

Filtrovat Události podle:

- Otevřít
- Plánování
- Po vypršení termínu
- Dokončeno
- Přeskočeno

Je povolen výběr více stavů. Jakmile otevřete TEI, filtr se zachová na ovládacím panelu a zobrazí pouze události se zvoleným stavem.

Zobrazené události jsou staré až 5 let.

### Datum registrace { #capture_app_generic_filter_date_enroll }

„Datum zápisu“ se použije k datu zápisu TEI do programu. Pokud existuje více než jedno datum zápisu, mělo by seřadit výsledky podle nejnovějšího. Je-li k dispozici, zobrazí se štítek tohoto filtru.

### Stav zápisu { #capture_app_generic_filter_enroll_status }

Filtr 'Stav registrace' nabízí tři možnosti: Aktivní, Dokončeno, Zrušeno. V daném okamžiku lze vybrat pouze jednu možnost. Pokud filtrujete podle „dokončeno“ a TEI má více než jednu registraci, aplikace otevře „aktivní“ registraci. Chcete-li zobrazit dokončený, vyberte nabídku se třemi tečkami v pravém horním rohu řídicího panelu a vyberte „registrace programu“.

### Filtrování přidáno do ovládacího panelu TEI: { #capture_app_generic_filter_tei }

Na ovládací panel TEI byly přidány filtry. Je možné filtrovat události registrace instance trasované entity podle období, organizační jednotky, stavu synchronizace, stavu události a přiřazení uživatele.

![](resources/images/capture-app-image114.png){ width=25%}

## Řazení { #capture_app_generic_sorting }

Třídění bylo integrováno do nabídky filtrů.

Tlačítko řazení bude na pruzích filtrů s následujícím chováním:

- Najednou platí pouze jedno třídění. Pokud uživatel klikne na jiné, předchozí je deaktivováno.
- Ikona aplikovaného třídění ukazuje, že je aktivní, ostatní jsou neaktivní.
- Opakovaná kliknutí mění směr řazení na opačné.

![](resources/images/capture-app-image135.png){ width=25%}

### Data (období, datum, datum události nebo datum registrace) { #capture_app_generic_sorting_dates }

- Datum události předchází datu vypršení, datum vypršení použijte pouze v případě, že neexistuje datum události.
- Řazení od nejnovějšího ke staršímu. Budoucí události (s vypršením) jsou na prvním místě.

### Organizační jednotky { #capture_app_generic_sorting_orgunits }

- Seznam bude řazen v abecedním pořadí podle názvu organizační jednotky.

### Stav zápisu { #capture_app_generic_sorting_enrollment }

- Seznam bude seřazen v abecedním pořadí podle názvu stavu.

![](resources/images/capture-app-image123.png){ width=25%}

## Synchronizovat informace { #capture_app_generic_sync_info }

Umožňuje uživateli zkontrolovat informace o synchronizaci pro konkrétní program. Nyní synchronizované záznamy nebudou zobrazovat žádnou ikonu. Zobrazí se pouze nesynchronizované, chybové nebo SMS ikony.

![](resources/images/capture-app-image67.png){ width=20%}
![](resources/images/capture-app-image69.png){ width=20%}

### Granulární synchronizace { #capture_app_generic_sync_granular }

Umožňuje synchronizovat jednotlivé záznamy (Program, Událost, TEI, DataSet, DataValues) se serverem.

![](resources/images/capture-app-image89.png){ width=25%}
![](resources/images/capture-app-image161.png){ width=25%}

### SMS Sync { #capture_app_generic_sync_sms }

Pokud neexistuje internetové datové připojení, umožňuje odeslat záznam prostřednictvím několika SMS zpráv. Záznam je označen jako „SMS synchronizováno“.

![](resources/images/capture-app-image91.png){ width=25%}

> **Tip**
>
> Upravte parametry týkající se SMS brány v Nastavení SMS (nabídka Nastavení)

![](resources/images/capture-app-image90.png){ width=25%}

> **Poznámka**
>
> Všimněte si, že aby bylo možné využívat funkce synchronizace SMS, musí být služby SMS povoleny na straně serveru, jak je popsáno v [oficiální dokumentaci](https://docs.dhis2.org/master/en/dhis2_user_manual_en/mobile.html#sms-service). Další informace o tom, jak používat různé brány, najdete také v [Pokyny pro implementaci systému Android](https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/about-this-guide.html).

## Org. jednotka { #capture_app_generic_orgunit }

![](resources/images/capture-app-image30.png){ width=25%}

Zobrazí se strom celé organizační jednotky. Organizační jednotky, které nejsou k dispozici pro zadávání údajů, budou zbarveny šedě. Uživatel musí zaškrtnout políčko a vybrat požadovanou organizační jednotku.

> **Pozor**
>
> Od mobilních uživatelů se neočekává přístup k organizační jednotce hierarchie celé země. Maximální počet organizačních jednotek je obtížné nastavit, protože aplikace nestanoví limit, ale prostředky v zařízení (paměť, procesor). Dalo by se říci, že 250 organizačních jednotek by mělo být bezpečných, ale přesto věříme, že je to velmi velké číslo pro případ použití v mobilu.

## Datové sady { #capture_app_generic_datasets }

Uživatel nyní může zadat agregovaná data pro organizační jednotku, období a sadu datových prvků a odeslat je na server.

![](resources/images/capture-app-image87.png){ width=25%}
![](resources/images/capture-app-image93.png){ width=25%}
![](resources/images/capture-app-image92.png){ width=25%}

## Rozlišování datových sad, trasovacích programů a programů událostí { #capture_app_generic_differentiating }

![](resources/images/capture-app-image87.png){ width=25%}

> **Tip**
>
> Snadným způsobem, jak je odlišit, je pohled na slovo v levém dolním rohu. Slovo „Událost“ bude v programech událostí vždy. V nástroji pro trasování se zobrazí název typu trasované entity (osoba, pacient, budova atd.). U souborů dat se vedle počtu záznamů zobrazí slovo „DataSets“.

## Sdílení dat { #capture_app_generic_shargin }

![](resources/images/capture-app-image72.png){ width=25%}
![](resources/images/capture-app-image73.png){ width=25%}

## Zachycení souřadnic { #capture_app_generic_capture_coord }

### Souřadnice TEI { #capture_app_generic_capture_coord_tei }

Zachyťte souřadnice TEI v registračním formuláři. Povolte tuto funkci v typu funkce TET.

![](resources/images/capture-app-image94.png){ width=25%}

### Polygony { #capture_app_generic_capture_coord_polygons }

Aplikace nyní podporuje formát geoJSON a uživatel je schopen zachytit polygony.

![](resources/images/capture-app-image95.png){ width=25%}

## Obrázky { #capture_app_generic_images }

Image ValueType byl implementován na straně aplikace. To umožňuje vybrat obrázek pro datový prvek nebo atribut a odeslat jej na server. U TEI se jako profilový obrázek TEI použije první datový prvek / atribut s tímto typem hodnoty a označený jako zobrazený v seznamu.

![](resources/images/capture-app-image99.png){ width=25%}
![](resources/images/capture-app-image98.png){ width=25%}
![](resources/images/capture-app-image100.png){ width=25%}

Otevřete profilový obrázek TEI kliknutím na něj.

![](resources/images/capture-app-image138.png){ width=25%}

## Zobrazovat události a TEI v mapách { #capture_app_generic_display_events }

Pokud má fáze programu nebo typ trasované entity typ funkce (a pro programy s registrací je povolena možnost displayFrontPageList), lze výpisy přepnout na zobrazení informací v mapě. Přepněte kliknutím na ikonu mapy na navigačním panelu.

![](resources/images/capture-app-image101.png){ width=25%}
![](resources/images/capture-app-image102.png){ width=25%}

Pokud má TEI profilový obrázek, zobrazí jej mapa. ![](resources/images/capture-app-image103.png){ width=25%}
