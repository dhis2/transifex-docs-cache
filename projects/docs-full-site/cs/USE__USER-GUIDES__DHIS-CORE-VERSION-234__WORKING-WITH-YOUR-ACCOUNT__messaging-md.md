---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/messaging.md"
revision_date: "2021-06-14"
---

# Zprávy { #messages }

## O zprávách a zpětných vazbách { #about-messages-and-feedback-messages }

![](resources/images/messaging/view_inbox.png)

V rámci DHIS2 můžete odesílat zprávy a zpětné vazby uživatelům, skupinám uživatelů a organizačním jednotkám. Když odešlete zprávu se zpětnou vazbou, bude směrována na konkrétní skupinu uživatelů nazvanou skupina příjemců zpětné vazby. Pokud jste členem této skupiny uživatelů, máte přístup k nástrojům pro zpracování zpětné vazby. Během čekání na informace můžete například nastavit stav příchozí zpětné vazby na „Nevyřízeno“.

Kromě zpráv mezi uživateli a zpětné vazby, vám systém v závislosti na vaší konfiguraci pošle také zprávy generované systémem. Tyto zprávy by mohly být spuštěny různými událostmi, včetně selhání úloh systému nebo pozadí a výsledků analýzy ověření. Pro výsledky ověření jsou k dispozici také nástroje pro zpracování zpětné vazby a priorita bude nastavena na důležitost porušeného pravidla ověření.

Chcete-li aplikaci navštívit, klikněte na **ikonu zprávy v pruhu záhlaví** nebo vyhledejte aplikaci **Oznamování** ve vyhledávacím poli.

> **Poznámka**
>
> Zprávy a zprávy se zpětnou vazbou nejsou odesílány na e-mailové adresy uživatelů, zprávy se zobrazují pouze v rámci DHIS2.
>
> S verzí 2.30 jsme představili novou aplikaci pro zasílání zpráv, která nabízí bohatší možnosti zasílání zpráv. konkrétně:
>
> - Přepněte mezi zobrazením seznamu a kompaktním zobrazením kliknutím na ikonu v pravém horním rohu.
>
> - Zobrazení seznamu je zjednodušené a poskytuje dobrý přehled o všech zprávách a je zvláště vhodné pro zpětnou vazbu a zprávy o ověření.
> - Kompaktní zobrazení je moderní způsob zobrazení zpráv, kde má uživatel více informací v jednom zobrazení, takže prohlížení a odpovídání na několik zpráv je jednodušší.
>
> První snímek obrazovky v této části zobrazuje seznam, zatímco snímek obrazovky v části **Přečíst zprávu** zobrazuje kompaktní zobrazení.
>
> - Je přidáno nové vyhledávací pole, které uživateli umožňuje vyhledávat zprávy. Vyhledávání filtruje zprávy podle různých atributů zpráv; předmět, text a odesílatelé. To znamená, že můžete zúžit seznam konverzací zpráv zadáním vyhledávání.
>
> - Je přidána funkce automatického obnovení, takže aplikace načítá nové zprávy v nastaveném intervalu, každých 5 minut. Tato funkce je ve výchozím nastavení zakázána.
>
> - Ke každé konverzaci zpráv můžete přidat účastníky do konverzace. To je velmi užitečné, pokud chcete vložit informace o konkrétní konverzaci nebo pokud by někdo měl také vidět informace. Není možné odstranit účastníky z konverzace.

## Vytvořte zprávu { #create-a-message }

![](resources/images/messaging/create_private_message.png)

1.  Klikněte na **Vytvořit**.

2.  Definujte, komu chcete zprávu přijmout. Můžete odeslat zprávu organizačním jednotkám, uživatelům a skupinám uživatelů.

    -   V poli **Komu** můžete vyhledat organizační jednotky, uživatele a skupiny uživatelů a vybrat požadované příjemce.

3.  Zadejte předmět a zprávu.

4.  Klikněte na **Odeslat**

## Přečtěte si zprávu { #read-a-message }

![](resources/images/messaging/read_message.png)

1.  Vlevo vyberte vhodný typ zprávy.

2.  Klikněte na zprávu.

    Pokud je zpráva součástí konverzace, uvidíte všechny zprávy v této konverzaci.

## Vytvořte zpětnou vazbu { #create-a-feedback-message }

1.  Postupujte podle pokynů pro vytváření zprávy, místo zadávání příjemců vyberte pouze **Zpětná vazba**.

2.  Zpráva bude vytvořena jako zpětná vazba a zobrazí se ve složce **Tiket** všech zadaných uživatelů.

## Přílohy { #attachments }

S verzí 2.31 jsme představili přílohy ke zprávám. Při vytváření konverzace se zprávou nebo odpovědi na ni máte možnost přidat přílohy. V současné době neexistují žádná omezení týkající se typu nebo velikosti souboru.

## Spravujte zprávy o ověření a zpětné vazbě { #manage-validation-and-feedback-messages }

> **Poznámka**
>
> Zprávy se zpětnou vazbou a přístup k rozšířeným nástrojům pro manipulaci uvidíte pouze v případě, že jste členem skupiny uživatelů, která je nastavena pro zpracování zpráv se zpětnou vazbou.
>
> S novou aplikací spravujete rozšířené nástroje pro lístky a ověřovací zprávy prostřednictvím nabídky ikon, která se zobrazí při prohlížení zprávy nebo kontrole zpráv v seznamu konverzací.

### Všechny zprávy vybrány { #all-messages-selected }

![Všechny zprávy vybrány](resources/images/messaging/view_validation_select_all.png)

### Vybrány všechny zprávy a výběr rozšířené volby { #all-messages-selected-and-extended-choice-picker-selected }

![Vybrány všechny zprávy a vybrán rozšířený výběr](resources/images/messaging/view_validation_select_all_icon_menu.png)

Do složky **Tiket** budete dostávat zprávy zpětné vazby a do složky **Validace** zprávy o ověření. Pro zpětnou vazbu a ověřovací zprávy máte kromě možností zpráv také následující možnosti:

<table style="width:100%;">
<caption> Nástroje pro zpracování zpětné vazby </caption>
<colgroup>
<col width="23%" />
<col width="76%" />
</colgroup>
<thead>
<tr class="header">
<th> Funkce </th>
<th> Popis </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> <strong> priorita </strong> </p> </td>
<td> <p> můžete označit zpětné vazby / ověřovací zprávy s různými prioritami: <strong> Žádné </strong>, <strong> nízké</strong>, <strong> střední </strong> nebo <strong> vysoké</strong>. </p>
<p> Nastavení priority usnadňuje trasování, kterou zpětnou vazbu potřebujete vyřešit jako první, a která zpětná vazba může čekat. </p> </td>
</tr>
<tr class="even">
<td> <p> <strong> stav </strong> </p> </td>
<td> <p> Všechny zpětnovazební / ověřovací zprávy získají stav <strong> Otevřít </strong>, když jsou vytvořeny. </p>
<p> Chcete-li sledovat existující zpětnovazební zprávy, můžete změnit stav na <strong> Nevyřízené </strong>, <strong> Neplatné </strong> nebo <strong>Vyřešené</strong>.</p>
<p> Zprávy zpětné vazby / ověřování můžete filtrovat na základě jejich stavu pomocí dvou rozbalovacích nabídek na vnitřní liště záhlaví. </p> </td>
</tr>
<tr class="odd">
<td> <p> <strong> Přiřazeno k </strong> </p> </td>
<td> <p> Zprávu se zpětnou vazbou můžete přiřadit kterémukoli členovi skupiny uživatelů, který je nastaven pro zpracování zpráv se zpětnou vazbou. </p>
<p> Ověřovací zprávu můžete přiřadit kterémukoli uživateli v systému. </p>
<p> <strong> - </strong> znamená, že jste ke zpětné vazbě nepřiřadili uživatele. </p> </td>
</tr>
<tr class="even">
<td> <p> <strong> interní odpověď </strong> </p> </td>
<td> <p> Když pracujete v týmu pro zpracování zpětné vazby, možná budete chtít diskutovat o zpětné vazbě před odesláním odpovědi odesílateli. Tuto diskusi můžete udržovat ve stejné konverzaci zpráv jako samotná zpětná vazba. </p>
<p> Chcete-li odeslat odpověď, která ve skupině uživatelů pro zpracování zpětné vazby, klikněte na <strong>VNITŘNÍ ODPOVĚĎ.</strong> </p> </td>
</tr>
</tbody>
</table>

## Nakonfigurujte funkci zpětné vazby { #configure-feedback-message-function }

Chcete-li nakonfigurovat funkci zpětné vazby, musíte:

1.  Vytvořte skupinu uživatelů (například „Příjemci zpětné vazby“), která obsahuje všechny uživatele, kteří by měli dostávat zpětné vazby.

2.  Otevřete aplikaci **Nastavení systému** a klikněte na **Obecné** \> **Příjemci zpětné vazby** a vyberte skupinu uživatelů, kterou jste vytvořili v předchozím kroku.
