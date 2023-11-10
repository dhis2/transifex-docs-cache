---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/using-the-event-capture-app.md"
revision_date: "2021-06-14"
---

# Použití aplikace Event Capture { #event_capture_app }

## O aplikaci Zachycení Události { #about_event_capture_app }

![](resources/images/event_capture/event_list.png)

V aplikaci **Zachycení Události** registrujete události, ke kterým došlo v konkrétním čase a místě. Událost se může stát v kterémkoli daném okamžiku. To je v rozporu s rutinními daty, která lze zachytit v předdefinovaných pravidelných intervalech. Události se někdy nazývají případy nebo záznamy. V DHIS2 jsou události propojeny s programem. Aplikace **Zachycení Události** vám umožňuje vybrat organizační jednotku a program a určit datum, kdy k události došlo, před zadáním informací o události.

Aplikace **Zachycení Události** funguje online i offline. Pokud připojení k internetu poklesne, můžete pokračovat v zachycování událostí. Události budou uloženy lokálně ve vašem webovém prohlížeči (klientovi). Po obnovení připojení vás systém požádá o nahrání lokálně uložených dat. Systém poté odešle data na server, kde jsou data uložena.

> **Poznámka**
>
> Pokud zavřete webový prohlížeč v režimu offline, není možné znovu otevřít nové okno webového prohlížeče a pokračovat v pracovní relaci. Data se však budou i nadále ukládat lokálně a lze je nahrát na server, až bude zařízení příště online a vy se přihlásíte na server.

-   Uvidíte pouze programy přidružené k organizační jednotce, kterou jste vybrali, a programy, ke kterým máte přístup prostřednictvím své uživatelské role.

-   Během registrace jsou podporovány chybové i varovné zprávy přeskočení logiky i ověření.

-   Když zavřete organizační jednotku, nemůžete registrovat ani upravovat události v této organizační jednotce v aplikaci **Zachycení Události**. Stále můžete zobrazit a filtrovat seznam událostí a zobrazit podrobnosti události.

-   Je podporováno vyhodnocení výrazu za běhu. Pokud má program definované indikátory a v okamžiku, kdy jsou vyplněny všechny hodnoty související s výrazem indikátoru, systém vypočítá indikátor a zobrazí výsledek.

    ![](resources/images/event_capture/event_editing.png)

-   **Řazení:** Toho lze dosáhnout kliknutím na ikonu řazení v záhlaví každého sloupce. Červená ikona řazení implikuje aktuální sloupec řazení. Funkce řazení však funguje pouze na zobrazené stránce. V současné době není možné provádět třídění ze strany serveru.

-   **Filtrování:** Toto se provádí kliknutím na malou ikonu vyhledávání zobrazenou napravo od záhlaví každého sloupce. Kliknutím na ni získáte vstupní pole pro zadání kritérií filtrování. Systém začne používat filtr v okamžiku, kdy uživatel začne psát. Během filtrování je možné definovat počáteční a koncové datum pro datové prvky typu data a dolní a horní limity pro typy čísel. Filtrování na straně serveru momentálně není podporováno.

## Zaregistrujte událost { #event_capture_register_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Uvidíte pouze programy přidružené k vybrané organizační jednotce a programy, ke kterým máte přístup prostřednictvím své uživatelské role.

4.  Klikněte na **Registrovat událost**.

5.  Vyberte datum.

6.  Vyplňte požadované informace.

    Pokud je programová fáze programu nakonfigurována tak, aby zachytávala souřadnice GPS, můžete souřadnice zadat dvěma způsoby:

    -   Zadejte hodnoty přímo do příslušných polí.

    -   Vyberte místo na mapě. Možnost Mapa také zobrazuje polygony a body definované pro organizační jednotky.

7.  Klikněte na **Uložit a přidat nové** nebo **Uložit a vrátit se**.

> Poznámka: Některé datové prvky v události mohou být povinné (označené červenou hvězdou vedle štítku datového prvku). To znamená, že všechny povinné datové prvky musí být vyplněny, než bude uživateli povoleno událost uložit. Výjimkou je, pokud má uživatel oprávnění s názvem **„Ignorovat ověření požadovaných polí v nástroji Trasovač and Zachycení Události“.** Pokud má uživatel toto oprávnění, nebude nutné před uložením vyplňovat povinné datové prvky a červená hvězda se nezobrazí vedle štítku datového prvku. Všimněte si, že super uživatel, který má oprávnění **„ALL“**, má toto oprávnění automaticky.

## Upravit událost { #event_capture_edit_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost, kterou chcete upravit, a vyberte **Upravit**.

5.  Upravte podrobnosti události a klikněte na **Aktualizovat**.

## Úpravy událostí v mřížce { #event_capture_edit_event_grid }

Funkce **Upravit v mřížce** umožňuje upravit vybranou událost v tabulce, ale pouze ty sloupce (datové prvky) viditelné v mřížce. Pokud potřebujete více sloupců, použijte **Zobrazit / skrýt sloupce** a určete, které sloupce se mají v seznamu zobrazit.

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost, kterou chcete upravit, a vyberte **Upravit v mřížce**.

5.  Upravte podrobnosti události.

6.  Kliknutím na jinou událost režim úprav zavřete.

## Sdílejte události v režimu úprav { #event_capture_share_event_edit_mode }

Událost můžete sdílet v režimu úprav prostřednictvím její webové adresy.

1.  Otevřete aplikaci **Zachycení Události**.

2.  V režimu úprav otevřete událost, kterou chcete sdílet.

3.  Zkopírujte adresu URL.

    Ujistěte se, že adresa URL obsahuje parametry „event“ a „ou“ (organizační jednotka).

4.  Vložte adresu URL do metody sdílení podle vašeho výběru, například e-mail nebo zprávu v rámci DHIS2.

    Pokud nejste přihlášeni k DHIS2, když kliknete na odkaz, budete požádáni, abyste tak učinili, a poté přejdete na ovládací panel.

## Zobrazit historii auditu událostí { #event_capture_view_event_audit_history }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost a vyberte **Historie auditu**.

## Smazat událost { #event_capture_delete_event }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na událost a vyberte **Odebrat**.

5.  Kliknutím na **Odstranit** potvrďte odstranění.

## Upravte rozložení seznamu událostí { #event_capture_modify_event_list_layout }

Můžete vybrat, které sloupce se mají zobrazit nebo skrýt v seznamu událostí. To může být užitečné například v případě, že máte k programové fázi přiřazen dlouhý seznam datových prvků. Jakmile upravíte rozložení, uloží se do vašeho uživatelského profilu. Pro různé programy můžete mít různá rozvržení.

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na ikonu **Zobrazit / skrýt sloupce**.

5.  Vyberte sloupce, které chcete zobrazit, a klikněte na **Zavřít**.

## Vytiskněte seznam událostí { #event_capture_print_event_list }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na **Vytisknout seznam**.

## Stáhněte si seznam událostí { #event_capture_download_event_list }

1.  Otevřete aplikaci **Zachycení Události**.

2.  Vyberte organizační jednotku.

3.  Vyberte program.

    Všechny události registrované k vybranému programu se zobrazí v seznamu.

4.  Klikněte na ikonu **Stáhnout** a vyberte formát.

    Seznam událostí si můžete stáhnout ve formátech XML, JSON nebo CSV.
