---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/manage-users-user-roles-and-user-groups.md"
revision_date: "2021-06-14"
---

# Spravujte uživatele, uživatelské role a skupiny uživatelů { #manage_user_role_group }

## O správě uživatelů { #about_user_userrole }

Více uživatelů může přistupovat k DHIS2 současně a každý uživatel může mít různá oprávnění. Tato oprávnění můžete doladit tak, aby určití uživatelé mohli zadávat pouze data, zatímco ostatní mohli generovat pouze zprávy.

-   Můžete vytvořit tolik uživatelů, uživatelských rolí a skupin uživatelů, kolik potřebujete.

-   Můžete přiřadit konkrétní oprávnění skupinám uživatelů nebo jednotlivým uživatelům prostřednictvím rolí uživatelů.

-   Můžete vytvořit více uživatelských rolí, z nichž každá má svá vlastní oprávnění.

-   Uživatelům můžete přiřadit uživatelské role a udělit jim příslušná oprávnění.

-   Každého uživatele můžete přiřadit k organizačním jednotkám. Poté může uživatel zadat data pro přiřazené organizační jednotky.

<table>
<caption> Podmínky a definice správy uživatelů </caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Termín </p> </th>
<th> <p> Definice </p> </th>
<th> <p> Příklad </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> úřad </p> </td>
<td> <p> Oprávnění k provádění jednoho nebo několika konkrétních úkolů </p> </td>
<td> <p> Vytvořit nový datový prvek </p>
<p> Aktualizace organizační jednotky </p>
<p> Zobrazit zprávu </p> </td>
</tr>
<tr class="even">
<td> <p> Uživatel </p> </td>
<td> <p> Uživatelský účet DHIS2 osoby </p> </td>
<td> <p> admin </p>
<p> traore </p>
<p> host </p> </td>
</tr>
<tr class="odd">
<td> <p> Role uživatele </p> </td>
<td> <p> Skupina orgánů </p> </td>
<td> <p> Úředník pro zadávání dat </p>
<p> správce systému </p>
<p> Přístup k programu předporodní péče </p> </td>
</tr>
<tr class="even">
<td> <p> Skupina uživatelů </p> </td>
<td> <p> Skupina uživatelů </p> </td>
<td> <p> zaměstnanci Keni </p>
<p> příjemci zpětné vazby </p>
<p> programoví koordinátoři HIV </p> </td>
</tr>
</tbody>
</table>

V aplikaci **Uživatelé** spravujete uživatele, uživatelské role a skupiny uživatelů.

<table>
<caption> Objekty v aplikaci Uživatelé </caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Typ objektu </p> </th>
<th> <p> Dostupné funkce </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> Uživatel </p> </td>
<td> <p> Vytvořit, upravit, pozvat, klonovat, deaktivovat, zobrazit podle organizační jednotky, odstranit a zobrazit podrobnosti </p> </td>
</tr>
<tr class="even">
<td> <p> Role uživatele </p> </td>
<td> <p> Vytvářet, upravovat, sdílet, mazat a zobrazovat podrobnosti </p> </td>
</tr>
<tr class="odd">
<td> <p> Skupina uživatelů </p> </td>
<td> <p> Vytvořit, upravit, připojit, opustit, sdílet, mazat a zobrazit podrobnosti </p> </td>
</tr>
</tbody>
</table>

### O uživatelích { #about-users }

Každý uživatel v DHIS2 musí mít uživatelský účet, který je identifikován uživatelským jménem. Měli byste zaregistrovat křestní jméno a příjmení každého uživatele a také kontaktní informace, například e-mailovou adresu a telefonní číslo.

Je důležité, abyste zaregistrovali správné kontaktní informace. DHIS2 používá tyto informace k přímému kontaktování uživatelů, například k odesílání e-mailů k upozornění uživatelů na důležité události. Kontaktní informace můžete také použít ke sdílení například ovládacích  panelů a kontingenčních tabulek.

Uživatel v DHIS2 je přidružen k organizační jednotce. Měli byste přiřadit organizační jednotku, kde uživatel pracuje.

Když vytvoříte uživatelský účet pro okresního správce záznamů , měli byste mu jako organizační jednotku přiřadit okres, kde pracuje.

Přiřazená organizační jednotka ovlivňuje, jak může uživatel používat DHIS2:

-   V aplikaci **Zadávání dat** může uživatel zadat data pouze za organizační jednotku, ke které je přidružena, a za organizační jednotky pod hierarchií. Například okresní záznamník bude moci registrovat údaje pouze za svůj okres a zařízení pod tímto okresem.

-   V aplikaci **Uživatelé** může uživatel vytvořit nové uživatele pouze pro organizační jednotku, ke které je přidružena, kromě organizačních jednotek pod hierarchií.

-   V aplikaci **Zprávy** si uživatel může prohlížet pouze zprávy pro svou organizační jednotku a níže uvedené. (To je něco, co považujeme za otevřenou vlastnost, která umožní srovnávací zprávy.)

Důležitou součástí správy uživatelů je kontrola, kterým uživatelům je povoleno vytvářet nové uživatele, s kterými orgány. V DHIS2 můžete určit, kteří uživatelé mohou provádět tento úkol. Klíčovým principem je, že uživatel může udělit pouze oprávnění a přístup k souborům dat, ke kterým má přístup sám uživatel. Počet uživatelů na národní, krajské a okresní úrovni je často relativně malý a mohou je vytvářet a spravovat správci systému. Pokud velká část zařízení zadává data přímo do systému, může se počet uživatelů stát nepraktickým. Doporučuje se tento úkol delegovat a decentralizovat na okresní úředníky, zefektivní to proces a lépe podpoří uživatele zařízení.

### O uživatelských rolích { #about-user-roles }

Role uživatele v DHIS2 je skupina oprávnění. Oprávnění znamená oprávnění k provádění jednoho nebo více konkrétních úkolů.

Role uživatele může obsahovat oprávnění k vytvoření nového datového prvku, aktualizaci organizační jednotky nebo zobrazení sestavy.

Uživatel může mít více uživatelských rolí. Pokud ano, oprávnění uživatele budou součtem všech oprávnění a datových sad v rolích uživatelů. To znamená, že můžete uživatelské role kombinovat a porovnávat pro speciální účely místo vytváření pouze nových.

Role uživatele je přidružena ke kolekci datových sad. To ovlivňuje aplikaci **Data Entry**: uživatel může zadávat data pouze pro datové sady registrované pro jeho uživatelskou roli. To může být užitečné, když například chcete povolit příslušníkům zdravotnických programů zadávat údaje pouze pro své příslušné formuláře pro zadávání údajů.

Doporučení:

-   Vytvořte jednu uživatelskou roli pro každou pozici v organizaci.

-   Souběžně s definováním toho, který uživatel provádí jednotlivé úlohy v systému, vytvářejte uživatelské role.

-   Poskytněte rolím uživatelů pouze přesná oprávnění, která potřebují k výkonu své práce, ne více. Oprávnění k provedení úkolu by měl mít pouze ten, kdo má úkol provést.

### O skupinách uživatelů { #about-user-groups }

Uživatelská skupina je skupina uživatelů. Skupiny uživatelů používáte, když nastavujete sdílení objektů nebo oznámení, například nabízené zprávy nebo oznámení programu.

Viz také: 

[Sdílení](https://ci.dhis2.org/docs/master/en/user/html/sharing.html)

[Spravujte oznámení programu](https://docs.dhis2.org/master/en/user/html/configure_tracker_program_in_Maintenance_app.html#create-a-program-stage-notification)

[Spravovat nabízené zprávy push](https://docs.dhis2.org/master/en/user/html/manage_push_report.html)

## Pracovní postup { #user_mgt_workflow }

1.  Definujte pozice, které potřebujete pro svůj projekt, a určete, jaké úkoly budou různé pozice provádět.

2.  Pro každou pozici vytvořte zhruba jednu uživatelskou roli.

3.  Vytvářejte uživatele.

4.  Přiřaďte uživatelům uživatelské role.

5.  Přiřaďte uživatele k organizačním jednotkám.

6.  (Volitelné) Seskupte uživatele do skupin uživatelů.

7.  Sdílejte datové sady s uživateli nebo skupinami uživatelů prostřednictvím dialogu Sdílení v části Správa datových sad v aplikaci Údržba

> **Tip**
>
> Aby uživatelé mohli zadávat data, musíte je přidat na úrovni organizační jednotky a sdílet s nimi datovou sadu.

## Správa uživatelů { #mgt_user }

### Vytvořit uživatele { #create_user }

![](resources/images/dhis2UserManual/select_user_menu.png)

1.  Otevřete aplikaci **Uživatelé** a klikněte na **+** na kartě **Uživatelé**.

2.  Vyberte, zda chcete vyplnit všechny osobní informace o uživateli, nebo pozvete uživatele e-mailem a vyplňte ostatní informace o uživateli:

-   **Vytvořit účet s údaji o uživateli** ![](resources/images/dhis2UserManual/user_management_details.png) Tuto možnost vyberte, pokud si přejete zadat všechny přihlašovací údaje nového uživatele jako uživatelské jméno, heslo atd. Za těchto podmínek budou pole uživatelské jméno, heslo, příjmení, jméno, a role jsou povinné. <br/> <br/> Po vytvoření uživatele je účet připraven k použití s uživatelským jménem a heslem, které zadáte. <br/> <br/>
-   **Pozvánka k vytvoření účtu e-mailem** ![](resources/images/dhis2UserManual/user_management_invite.png) Tuto možnost vyberte, pokud chcete uživateli poslat pozvánku e-mailem. Poté se musí vrátit do DHIS2 a dokončit nastavení svého uživatelského účtu. Účet, který uživatel dokončí nastavení, bude omezen podle toho, jak účet nakonfigurujete.

> **Poznámka**
>
> Aby bylo možné tuto funkci používat, měl by mít systém platnou konfiguraci e-mailu v SystemSettings - \> E-mail

Zadejte e-mailovou adresu, na kterou má být pozvánka odeslána. Pokud chcete, můžete také zadat uživatelské jméno, které bude mít účet. Pokud necháte uživatelské jméno prázdné, může si uživatel při odpovědi na pozvání zvolit své vlastní uživatelské jméno (pokud již není převzato pro jiného uživatele.) <br/><br/> Po vytvoření uživatele systém odešle e-mail na adresu, kterou jste uvedli. Obsahuje jedinečný webový odkaz, pomocí kterého se uživatel může vrátit do systému a aktivovat svůj účet zadáním zbytku svých uživatelských informací. Uživatel musí dokončit nastavení účtu do 4 dnů, poté pozvání pozbude platnosti.

3. (Volitelné) Zadejte hodnoty pro pole **Deklarace mapování OIDC, identifikátor LDAP, číslo mobilního telefonu, WhatsApp, Facebook Messenger, Skype, Telegram a Twitter**.

4. Vyberte **jazyk rozhraní**. <br/> Můžete vybrat jazyk, do kterého byly přeloženy pevné prvky uživatelského rozhraní DHIS2.

5. Vyberte **jazyk databáze**. <br/> Můžete vybrat jazyk, do kterého byly v databázi přeloženy položky dodávané implementací, například názvy datových prvků nebo názvy na úrovni organizačních jednotek.

6. V části **Dostupné role** poklepejte na uživatelské role, které chcete uživateli přiřadit.

7. Vyberte **Jednotky organizace sběru dat a údržby**. <br/> ![](resources/images/dhis2UserManual/user_management_fewer_options.png) <br/> Organizační jednotky sběru dat a údržby řídí, pro které organizační jednotky může uživatel zadávat data. Každému uživateli musíte přiřadit alespoň jednu organizační jednotku pro sběr dat a údržbu. <br/> <br/> Uživatelé budou mít přístup do všech dílčích organizačních jednotek přidělených organizačních jednotek. Pokud jste například přiřadili uživatele k okresu, který má v okrese několik zařízení, bude mít uživatel přístup k údajům okresu a také ke všem zařízením obsaženým v okrese.

8. (Volitelné) Vyberte **Výstupní a analytické organizační jednotky**. <br/> <br/> Výstupní a analytické organizační jednotky řídí, pro které organizační jednotky může uživatel zobrazit agregovaná data v analytických aplikacích, například **kontingenční tabulka** a **GIS** aplikace. Uživateli můžete přiřadit libovolný počet datových výstupních a analytických organizačních jednotek. <br/> <br/> Uživatelé budou mít přístup ke všem podřízeným organizačním jednotkám přiřazených organizačních jednotek. Neměli byste vybírat potomky organizační jednotky, kterou jste již vybrali. Pokud jste například přiřadili uživatele do okresu, neměli byste vybírat zařízení v tomto okrese. <br/> <br/>

> **Poznámka**
>
> Přiřazení datových a analytických organizačních jednotek je u organizační jednotky volitelné. Pokud nezadáte žádnou organizační jednotku, bude mít uživatel přístup k celé hierarchii organizačních jednotek pro prohlížení agregovaných dat. Stejně jako u organizačních jednotek pro sběr dat byste _neměli vybírat následné organizační jednotky jednotky, kterou jste již vybrali_. <br/><br/> Na analytických aplikacích můžete na několika místech vybrat dimenzi organizační jednotky „uživatelská organizační jednotka“. Tento mechanismus se nejprve pokusí použít organizační jednotky zobrazení dat spojené s aktuálním uživatelem. Pokud není nalezen, použije organizační jednotky pro sběr a údržbu dat. Pokud byl uživatel přiřazen k více organizačním jednotkám, může použití „uživatelské organizační jednotky“ vést k nepředvídatelnému chování. <br/><br/>

9. Klikněte na **Zobrazit další možnosti** a zobrazí se další tři pole. (Volitelné) <br/><br/>

10. V **Hledat organizační jednotky** vyberte organizační jednotky, ve kterých chcete, aby uživatel mohl vyhledávat. <br/><br/>

11. (Volitelné) V části **Dostupné skupiny uživatelů** poklepejte na skupiny uživatelů, které chcete uživateli přiřadit. <br/><br/>

12. (Volitelné) V části **Dostupná omezení dimenze pro analýzu dat** poklepejte na dimenze, které chcete uživateli přiřadit. <br/><br/> Hodnoty, které uživatel vidí v aplikacích pro analýzu dat, můžete omezit výběrem dimenzí, které omezí jeho zobrazení.

> **Příklad**
>
> Řekněme, že jste definovali _Implementující Partner_ jako sadu skupin možností kategorií a že jste s tímto uživatelem sdíleli pouze jednoho nebo více konkrétních implementujících partnerů (skupiny možností kategorií). Pokud se chcete ujistit, že uživatel v analytice nevidí součty, které obsahují hodnoty z jiných skupin, přiřaďte uživateli _Implementující Partner_. <br/> <br/> Tím se zajistí, že všechna data viditelná pro uživatele prostřednictvím analytických aplikací budou filtrována, aby byly vybrány pouze skupina(y) možností kategorie implementujícího partnera, které jsou uživateli viditelné. <br/> <br/>

13. Klikněte **Uložit**.

### Upravte uživatelské objekty { #edit-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete upravit.

2.  V seznamu objektů klikněte přímo na příslušný objekt nebo klikněte na ikonu nabídky a vyberte **Upravit**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Zakázat uživatele { #disable_user }

Uživatele můžete deaktivovat. To znamená, že uživatelský účet není odstraněn, ale uživatel se nemůže přihlásit nebo používat DHIS2.

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatel**.

2.  V seznamu klikněte na ikonu nabídky příslušného záznamu uživatele a vyberte **Zakázat**.

3.  Potvrďte kliknutím na **OK**.

> **Varování**
>
> Pokud používáte aplikaci [Android Capture App](https://www.dhis2.org/android), deaktivace uživatele způsobí, že aplikace smaže místní data uložená v telefonu při příštím pokusu o on-line přihlášení . Ujistěte se, že když používáte funkci _disable user_, všechna data byla synchronizována se serverem. Nebo že používáte tuto funkcionalitu k zajištění vymazání dat v případě ztráty zařízení.

### Zobrazit profil uživatele { #display-a-users-profile }

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatel**.

2.  V seznamu klikněte na ikonu nabídky příslušného uživatele a vyberte **Profil**.

### Filtrovat uživatele podle organizační jednotky { #filter-users-by-organisation-unit }

Můžete zobrazit všechny uživatele, kteří byli přiřazeni ke konkrétní organizační jednotce.

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatelé**.

2.  Nad seznamem uživatelů klikněte na vstup filtru **Organizační jednotka**.

3.  Zobrazí se vyskakovací okno, ve kterém můžete vybrat organizační jednotky, podle kterých chcete filtrovat.

Seznam uživatelů bude filtrován tak, aby zahrnoval pouze uživatele, kteří byli přiřazeni k vybraným organizačním jednotkám.

### Klonovat uživatele { #clone_user }

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatel**.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného uživatele a vyberte **Replikovat**.

3.  Zadejte nové uživatelské jméno a heslo pro klonovaný uživatelský účet.

4.  Klikněte na **Replikovat**.

5.  V seznamu objektů klikněte na uživatele, kterého jste právě vytvořili, a klikněte na **Upravit**.

6.  Upravte požadované možnosti.

7.  Klikněte **Uložit**.

### Změňte heslo uživatele { #user_manage_password }

Chcete-li změnit heslo uživatele:

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatel**.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného uživatele a vyberte **Upravit**.

3.  Zadejte nové heslo a znovu jej zadejte.

4.  Klikněte **Uložit**.

#### Požadavky na heslo { #password-requirements }

Při vytváření nového hesla platí následující pravidla. Heslo musí:

-   Obsahovat alespoň 8 znaků. Toto číslo lze konfigurovat pomocí systémového nastavení „Minimální počet znaků v hesle“, které může mít až 14 znaků.

-   Nesmí obsahovat více než 40 znaků.

-   Obsahuje alespoň jeden speciální znak (nealfanumerický znak).

-   Obsahuje alespoň jeden znak velkých písmen.

-   Obsahují alespoň jeden znak malých písmen.

-   Obsahuje alespoň jednu číslici (číslo).

-   Neobsahuje uživatelské jméno nebo e-mailovou adresu uživatelského účtu.

-   Neobsahuje obecná slova jako _system_, _admin_, _user_, _login_ a _manager_.

-   Nesmí být jedním z předchozích 24 hesel, která uživatel použil. To neplatí v případě, že super uživatel resetuje heslo pro jiného uživatele.

### Odstranit uživatelské objekty { #delete-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete odstranit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Odstranit**.

3.  Potvrďte kliknutím na **OK**.

### Zobrazit podrobnosti o uživatelských objektech { #display-details-of-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete zobrazit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Zobrazit podrobnosti**.

### Zakázat dvoufaktorové ověřování pro uživatele { #disable-two-factor-authentication-for-a-user }

Pokud uživatel povolil dvoufaktorové ověřování a poté ztratí přístup ke svému ověřovacímu zařízení (např. Dojde ke ztrátě nebo rozbití smartphonu), nebude se již moci do systému přihlásit. Chcete-li tento problém vyřešit, může správce uživatelů pro postiženého uživatele deaktivovat dvoufaktorové ověřování, aby měl uživatel znovu přístup do systému pouze pomocí hesla.

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatelé**.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného uživatele a vyberte **Zakázat dvoufaktorové ověřování**.

3.  Potvrďte kliknutím na **OK**

> **Poznámka**
>
> Možnost zakázat dvoufaktorové ověřování bude k dispozici pouze uživatelům, kteří si nastavili dvoufaktorové ověřování prostřednictvím aplikace profil uživatele.

## Spravujte uživatelské role { #mgt_userrole }

### Vytvořte uživatelskou roli { #create_userrole }

![](resources/images/dhis2UserManual/role_maintenance_page.png)

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Uživatelská role**.

2.  Klikněte na **Přidat nový**.

3.  Zadejte **název**, například „Super uživatel“ nebo „Správce uživatelů“.

4.  Zadejte **popis**.

5.  V části **Autority** vyberte oprávnění, která chcete udělit uživatelské roli. Můžete také použít vstupy filtru nad částí oprávnění k vyhledání konkrétního oprávnění.

6.  Klikněte na **Přidat**.

### Upravte uživatelské objekty { #edit-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete upravit.

2.  V seznamu objektů klikněte přímo na příslušný objekt nebo klikněte na ikonu nabídky a vyberte **Upravit**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstranit uživatelské objekty { #delete-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete odstranit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Odstranit**.

3.  Potvrďte kliknutím na **OK**.

### Zobrazit podrobnosti o uživatelských objektech { #display-details-of-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete zobrazit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Zobrazit podrobnosti**.

### Změňte nastavení sdílení pro uživatelské objekty { #change-sharing-settings-for-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete upravit.

2.  V seznamu objektů klikněte na příslušný objekt a vyberte **Nastavení sdílení**.

3.  (Volitelné) Vyhledejte skupinu uživatelů, vyberte ji a poté klikněte na ikonu plus. Skupina uživatelů je přidána do seznamu.

4.  (Volitelné) Vyberte **Externí přístup (bez přihlášení)**.

5.  Změňte nastavení skupin uživatelů, které chcete upravit.

-   **Žádný**
-   **Může zobrazit**: Objekt může zobrazit každý ve skupině uživatelů
-   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý ve skupině uživatelů

6.  Klikněte **Uložit**.

## Spravujte skupiny uživatelů { #mgt_usergroup }

### Vytvořte skupinu uživatelů { #create_usergroup }

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Skupina uživatelů**.

2.  Klikněte na **Přidat nový**.

3.  Do pole **Název** zadejte název skupiny uživatelů.

4.  V části **Dostupní uživatelé** poklepejte na uživatele, které chcete přidat do skupiny uživatelů.

5.  V části **Dostupné skupiny uživatelů** poklepejte na skupiny uživatelů, které chcete do skupiny uživatelů přidat.

6.  Klikněte na **Přidat**.

### Připojte se ke skupinám uživatelů { #join_usergroup }

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Skupina uživatelů**.

2.  V seznamu klikněte na příslušnou skupinu uživatelů a vyberte **Připojit se ke skupině**.

### Opusťte skupiny uživatelů { #leave_usergroup }

1.  Otevřete aplikaci **Uživatelé** a klikněte na **Skupina uživatelů**.

2.  V seznamu klikněte na příslušnou skupinu uživatelů a vyberte **Opustit skupinu**.

### Upravte uživatelské objekty { #edit-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete upravit.

2.  V seznamu objektů klikněte přímo na příslušný objekt nebo klikněte na ikonu nabídky a vyberte **Upravit**.

3.  Upravte požadované možnosti.

4.  Klikněte **Uložit**.

### Odstranit uživatelské objekty { #delete-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete odstranit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Odstranit**.

3.  Potvrďte kliknutím na **OK**.

### Zobrazit podrobnosti o uživatelských objektech { #display-details-of-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete zobrazit.

2.  V seznamu objektů klikněte na ikonu nabídky příslušného objektu a vyberte **Zobrazit podrobnosti**.

### Změňte nastavení sdílení pro uživatelské objekty { #change-sharing-settings-for-user-objects }

1.  Otevřete aplikaci **Uživatelé** a najděte typ uživatelského objektu, který chcete upravit.

2.  V seznamu objektů klikněte na příslušný objekt a vyberte **Nastavení sdílení**.

3.  (Volitelné) Vyhledejte skupinu uživatelů, vyberte ji a poté klikněte na ikonu plus. Skupina uživatelů je přidána do seznamu.

4.  (Volitelné) Vyberte **Externí přístup (bez přihlášení)**.

5.  Změňte nastavení skupin uživatelů, které chcete upravit.

-   **Žádný**
-   **Může zobrazit**: Objekt může zobrazit každý ve skupině uživatelů
-   **Může upravovat a prohlížet**: Objekt může zobrazit a upravovat každý ve skupině uživatelů

6.  Klikněte **Uložit**.

## Decentralizovat správu uživatelů { #decentralize-user-management }

DHIS2 podporuje koncept správy uživatelů označovaný jako _spravovaní uživatelé_, který umožňuje výslovně definovat, kterým uživatelům by mělo být umožněno spravovat nebo upravovat které uživatele. „Správa uživatele“ znamená, že ho můžete zobrazit a upravit. Základní koncept pro správu uživatelů je, že můžete vidět a upravovat uživatele, kterým jste udělili všechna oprávnění; jinými slovy můžete upravit uživatele, kteří mají podmnožinu vašich vlastních autorit. Koncept spravovaných uživatelů vám dává nad tím větší kontrolu.

Koncept spravovaných uživatelů umožňuje definovat, kteří uživatelé by měli být schopni spravovat které uživatele. To se konfiguruje prostřednictvím skupin uživatelů a členství v těchto skupinách. Skupinu uživatelů lze nakonfigurovat tak, aby mohla spravovat další skupiny uživatelů ze standardního uživatelského rozhraní pro přidání a aktualizaci. Důsledkem je, že konkrétní uživatel může spravovat všechny uživatele, kteří jsou členy skupin uživatelů, které lze spravovat skupinou uživatelů, jejíž je uživatel členem. Jinými slovy, uživatele mohou spravovat všichni členové skupin uživatelů, kteří spravují skupiny uživatelů, jejichž jsou členy.

Chcete-li povolit tento koncept, měli byste uživatelům udělit oprávnění k „Přidat / aktualizovat uživatele ve spravovaných skupinách“ a _neudělit_ přístup ke standardnímu oprávnění „Přidat / aktualizovat uživatele“. Důsledkem konceptu spravovaných uživatelů je, že při vytváření uživatele pouze pomocí možnosti „Přidat / aktualizovat uživatele ve spravovaných skupinách“ musí být uživatel vytvořen jako člen alespoň jedné skupiny uživatelů, kterou může aktuální uživatel spravovat. Pokud ne, aktuální uživatel by okamžitě ztratil přístup k vytvářenému uživateli. Toto je ověřeno systémem.

Když je systému uděleno oprávnění „Přidat / aktualizovat uživatele ve spravovaných skupinách“, systém umožňuje uživateli přidávat členy do skupin uživatelů, ke kterým má přístup jen pro čtení. Účelem je umožnit decentralizovanou správu uživatelů. Můžete definovat rozsah skupin uživatelů, kde mohou ostatní uživatelé přidávat nebo odebírat členy, ale nemůžete odebírat ani měnit název skupiny.

## Příklad: správa uživatelů ve zdravotním systému { #user_mgt_example }

V systému zdraví jsou uživatelé logicky seskupeni s ohledem na úkol, který vykonávají, a na pozici, kterou zaujímají.

1.  Definujte, kteří uživatelé by měli mít roli správce systému. Často jsou součástí národní divize HIS a měli by mít v systému plnou autoritu.

2.  Pro každou pozici vytvořte zhruba jednu uživatelskou roli.

Příklady běžných  pozic jsou:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th> <p> Pozice </p> </th>
<th> <p> Typické úkoly </p> </th>
<th> <p> doporučená oprávnění </p> </th>
<th> <p> Komentář </p> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> <p> správci systému </p> </td>
<td> <p> Nastaví základní strukturu (metadata) systému. </p> </td>
<td> <p> Přidat, aktualizovat a odstranit základní prvky systému, například datové prvky, indikátory a datové sady. </p> </td>
<td> Metadata by měli upravovat pouze správci systému.

<p> Pokud povolíte uživatelům mimo tým správce systému upravovat metadata, může to vést k problémům s koordinací. </p>
<p> Aktualizace systému by měli provádět pouze správci systému. </p> </td>
</tr>
<tr class="even">
<td> <p> národní zdravotní manažeři </p>
<p> manažeři zdraví provincie </p> </td>
<td> <p> sledovat a analyzovat data </p> </td>
<td> <p> Přístup k modulu sestav, <strong> GIS </strong>, <strong> Data Quality </strong> a ovládací panel. </p> </td>
<td> <p> Nepotřebujete přístup pro zadávání dat, úpravy datových prvků nebo datových sad. </p> </td>
</tr>
<tr class="odd">
<td> <p> úředníci divize národního zdravotnického informačního systému (HISO) </p>
<p> Okresní zdravotní a informační úředníci (DHRIO) </p>
<p> Pracovníci zdravotnických záznamů a informací o zdraví zařízení (HRIO) </p> </td>
<td> <p> Zadejte data pocházející ze zařízení, která to nemohou přímo provést </p>
<p> Monitorujte, vyhodnocujte a analyzujte data </p> </td>
<td> <p> přístup ke všem aplikacím pro analýzu a ověřování </p>
<p> Přístup k aplikaci Data <strong> </strong>. </p> </td>
<td> <p> - </p> </td>
</tr>
<tr class="even">
<td> <p> úředníci pro zadávání dat </p> </td>
<td> <p> - </p> </td>
<td> <p> - </p> </td>
<td> <p> - </p> </td>
</tr>
</tbody>
</table>
