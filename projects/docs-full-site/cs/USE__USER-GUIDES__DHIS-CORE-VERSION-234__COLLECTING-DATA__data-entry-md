---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-data-entry-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Zadávání dat { #data_entry_app }

## O aplikaci Zadávání dat { #about_data_entry_app }

Aplikace **Zadávání dat** je místo, kde ručně zadáváte agregovaná data v DHIS2. Registrujete data pro organizační jednotku, období a sadu datových prvků (datovou sadu) najednou. Soubor dat často odpovídá nástroji pro sběr dat v papírové podobě. Sady dat konfigurujete v aplikaci **Údržba**.

> **Poznámka**
>
> Pokud má datová sada formulář sekce i vlastní formulář, zobrazí systém během zadávání dat vlastní formulář. Uživatelé, kteří zadávají data, si nemohou vybrat, jaký formulář chtějí použít. Při zadávání dat z webu je pořadí preferencí zobrazení:
>
> 1. Vlastní formulář (pokud existuje)
>
> 2. Formulář sekce (pokud existuje)
>
> 3. Výchozí formulář
>
> Mobilní zařízení nepodporují vlastní formuláře. Při zadávání dat na mobilních zařízeních je pořadí preferencí zobrazení:
>
> 1. Formulář sekce (pokud existuje)
>
> 2. Výchozí formulář

Když zavřete organizační jednotku, nemůžete registrovat ani upravovat data této organizační jednotky v aplikaci **Zadávání dat**.

## Zadejte data do formuláře pro zadávání údajů { #enter_data_in_data_entry_form }

![](resources/images/data_entry/data_entry_overview.png)

1.  Otevřete aplikaci **Zadávání dat**.

2.  Ve stromu organizační jednotky vlevo vyberte organizační jednotku.

3.  Vyberte **datovou sadu**.

4.  Vyberte **Období**.

    Dostupná období jsou řízena typem období souboru dat (frekvence hlášení). Kliknutím na **Předchozí rok** nebo **Příští rok** můžete přeskočit o rok zpět nebo vpřed.

    > **Note**
    >
    > Depending on how you've configured the data entry form, you might have to enter additional information before you can open the date entry form. This can for example be a project derived from a category combination.

5.  Zadejte údaje do formuláře pro zadávání údajů.

    -   Zelené pole znamená, že systém uložil hodnotu.

    -   Šedé pole znamená, že je pole deaktivováno a nemůžete zadat hodnotu. Kurzor automaticky přeskočí na další otevřené pole.

    -   Chcete-li přejít na další pole, stiskněte klávesu Tab nebo klávesu šipka dolů.

    -   Chcete-li se vrátit zpět na předchozí pole, stiskněte Shift + Tab nebo klávesu Šipka nahoru.

    -   Pokud zadáte neplatnou hodnotu, například znak v poli, který přijímá pouze číselné hodnoty, zobrazí se vyskakovací okno, které vysvětluje problém, a pole bude zbarveno žlutě (neuloženo), dokud hodnotu neopravíte.

    -   Pokud jste pro pole definovali rozsah minimální maximální hodnoty a zadáte hodnotu, která je mimo tento rozsah, zobrazí se vyskakovací zpráva, která říká, že hodnota je mimo rozsah. Hodnota zůstane neuložená, dokud nezměníte hodnotu nebo neaktualizujete rozsah hodnot a poté znovu nezadáte hodnotu.

6.  Po vyplnění formuláře klikněte na **Spustit ověření** v pravém horním rohu nebo pod formulářem pro zadávání údajů.

    Všechna ověřovací pravidla, která zahrnují datové prvky v aktuálním formuláři pro zadávání dat (datová sada), se poté spustí s novými daty. Pokud nedojde k žádnému porušení pravidel ověřování, zobrazí se zpráva s názvem _Obrazovka zadávání dat úspěšně prošla ověřením_. Pokud dojde k porušení ověřování, budou uvedena v seznamu.

    ![](resources/images/dhis2UserManual/Validation_Rule_Result.png)

7.  (Volitelné) Opravte porušení ověření.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros.

8.  Až chyby opravíte a zadávání dat dokončíte, klikněte na **Dokončit**.

    Systém tyto informace používá při generování zpráv o úplnosti pro okres, kraj, provincii nebo národní úroveň.

## Označte datovou hodnotu pro další sledování { #mark_data_for_followup_in_data_entry_form }

![](resources/images/data_entry/data_entry_section_history.png)

Pokud máte například podezřelou hodnotu, kterou musíte dále prozkoumat, můžete si ji ponechat v systému, ale označit ji pro další sledování. V aplikaci **Data Quality** můžete spustit následnou analýzu a zobrazit a opravit všechny označené hodnoty.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, kterou chcete označit pro další sledování.

4.  Klikněte na ikonu hvězdičky.

## Upravte hodnoty dat v vyplněném formuláři pro zadávání údajů { #edit_data_value_in_completed_form }

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Klikněte na **Neúplné**.

4.  Změňte příslušné hodnoty dat.

    > **Note**
    >
    > Zero (0) will delete the value if the data element has been configured to not store zeros,

5.  Klikněte na **Dokončit**.

## Zobrazte historii datové hodnoty { #display_data_value_history }

![](resources/images/data_entry/data_entry_section_history.png)

Můžete zobrazit posledních 12 hodnot registrovaných pro pole.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, pro kterou chcete zobrazit historii.

4.  Klikněte na **Historie datových prvků**.

## Zobrazte kontrolní stopu datových hodnot { #display_data_value_audit_trail }

![](resources/images/data_entry/data_entry_audit_trail.png)

Kontrolní záznam auditu umožňuje zobrazit další hodnoty dat, které byly zadány před aktuální hodnotou. Kontrolní záznam auditu také ukazuje, kdy byla změněna hodnota dat a který uživatel provedl změny.

1.  Otevřete aplikaci **Zadávání dat**.

2.  Otevřete existující formulář pro zadávání údajů.

3.  Poklepejte na pole s hodnotou, pro kterou chcete zobrazit záznam o auditu.

4.  Klikněte na **Audit trail**.

## Vytvořte rozsah minimální maximální hodnoty ručně { #change_min_max_range_manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  V aplikaci **Zadávání dat** otevřete formulář pro zadávání údajů.

2.  Poklepejte na pole, pro které chcete nastavit rozsah minimální a maximální hodnoty.

3.  Zadejte **minimální limit** a **maximální limit**.

4.  Klikněte **Uložit**.

    Pokud hodnoty nespadají do nového rozsahu hodnot při příštím zadávání dat, zobrazí se buňka pro zadávání dat s oranžovým pozadím.

5.  (Volitelné) Napište komentář, který vysvětlí příčinu nesrovnalosti, například událost v zařízení, která mohla vygenerovat velký počet klientů.

6.  (Volitelné) Klikněte na **Uložit komentář**.

> **Tip**
>
> Kliknutím na ikonu hvězdičky označte hodnotu pro další sledování.

## Zadejte data offline { #enter_data_offline }

Aplikace **Zadání Dat** funguje, i když během zadávání dat nemáte stabilní připojení k internetu. Pokud nemáte připojení k internetu, zadaná data se uloží do místního počítače. Když je připojení k internetu zpět, aplikace odešle data na server. Celková využití šířky pásma je snížena, protože formuláře pro zadávání dat se již načtou ze serveru pro každé vykreslení.

> **Poznámka**
>
> Chcete-li použít tuto funkci, musíte se k serveru přihlásit, když jste připojeni k internetu.

-   Když jste připojeni k internetu, aplikace zobrazí tuto zprávu v horní části formuláře pro zadávání dat:

    ![](resources/images/data_entry/data_entry_online1.png)

-   Pokud se vaše internetové připojení během zadávání dat přeruší, aplikace to zjistí a zobrazí tuto zprávu:

    ![](resources/images/data_entry/data_entry_offline1.png)

    Nyní budou vaše data uložena lokálně. Můžete pokračovat v zadávání dat jako obvykle.

-   Jakmile zadáte všechna potřebná data a aplikace zjistí, že je připojení k Internetu zpět, zobrazí se tato zpráva:

    ![](resources/images/data_entry/data_entry_offline_upload.png)

    Kliknutím na **Odeslat** synchronizujete data se serverem.

-   Když se data úspěšně synchronizují se serverem, zobrazí se tato potvrzovací zpráva:

    ![](resources/images/data_entry/data_entry_offline_upload_success1.png)

## Povolte zadávání dat jednotky s více organizacemi { #data_entry_multiple_organisation_units }

![](resources/images/data_entry/data_entry_multiple_org_unit.png)

Může být užitečné zadat data pro více organizačních jednotek do stejného formuláře pro zadávání dat, například pokud je ve formuláři několik datových prvků a v hierarchii je obrovské množství organizačních jednotek. V takovém případě můžete povolit zadávání dat jednotky s více organizacemi.

> **Poznámka**
>
> Zadávání dat jednotky s více organizacemi funguje pouze pro sekce formuláře.

1.  Otevřete aplikaci **Nastavení systému**.

2.  Vyberte **Povolit formuláře více organizačních jednotek**.

3.  V aplikaci **Zadávání dat** vyberte organizační jednotku bezprostředně nad organizační jednotkou, pro kterou chcete v hierarchii organizační jednotky zadat data.

    Datové prvky se ve formuláři zobrazí jako sloupce a organizační jednotky jako řádky.

    > **Note**
    >
    > The data entry forms should still be assigned to the facilities that you actually enter data for, that is the organisation units now appearing in the form.

## Viz také { #data_entry_app_see_also }

-   [Ovládání kvality dat](https://docs.dhis2.org/master/en/user/html/control_data_quality.html)

-   [Správa datových souborů a formulářů pro zadávání dat](https://docs.dhis2.org/master/en/user/html/manage_data_set.html)

-   [Použití aplikace Údržba](https://docs.dhis2.org/master/en/user/html/maintenance_app.html)
