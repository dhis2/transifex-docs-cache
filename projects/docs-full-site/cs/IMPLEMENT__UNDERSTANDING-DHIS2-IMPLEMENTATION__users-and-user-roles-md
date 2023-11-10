---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/users-and-user-roles.md"
revision_date: "2021-06-14"
---

# Uživatelé a uživatelské role { #users-and-user-roles }

## O správě uživatelů { #about_user_userrole }

Více uživatelů může přistupovat k DHIS2 současně a každý uživatel může mít různá oprávnění. Tato oprávnění můžete doladit tak, aby určití uživatelé mohli zadávat pouze data, zatímco ostatní mohli generovat pouze zprávy.

- Můžete vytvořit tolik uživatelů, uživatelských rolí a skupin uživatelů, kolik potřebujete.

- Můžete přiřadit konkrétní oprávnění skupinám uživatelů nebo jednotlivým uživatelům prostřednictvím rolí uživatelů.

- Můžete vytvořit více uživatelských rolí, z nichž každá má svá vlastní oprávnění.

- Uživatelům můžete přiřadit uživatelské role a udělit jim příslušná oprávnění.

- Každého uživatele můžete přiřadit k organizačním jednotkám. Poté může uživatel zadat data pro přiřazené organizační jednotky.

Tabulka: Termíny a definice správy uživatelů

| Období | Definice | Příklad |
| --- | --- | --- |
| Autorita | Povolení provádět jeden nebo několik konkrétních úkolů | Vytvořit nový datový prvek <br> <br> Aktualizovat organizační jednotku <br> <br> Zobrazit sestavu |
| Uživatel | Uživatelský účet DHIS2 osoby | admin <br> <br> traore <br> <br> host |
| Uživatelská role | Skupina autorit | Referent pro zadávání dat <br> <br> Správce systému <br> <br> Přístup k programu předporodní péče |
| Uživatelská skupina | Skupina uživatelů | Zaměstnanci Keni <br> <br> Příjemci zpětné vazby <br> <br> Koordinátoři programu HIV |

V aplikaci **Uživatelé** spravujete uživatele, uživatelské role a skupiny uživatelů.

Tabulka: Objekty v aplikaci Uživatelé

| Typ objektu | Dostupné funkce |
| --- | --- |
| Uživatel | Vytvářet, upravovat, zvát, klonovat, deaktivovat, zobrazovat podle organizační jednotky, mazat a zobrazovat podrobnosti |
| Uživatelská role | Vytvářet, upravovat, sdílet, mazat a zobrazovat podrobnosti |
| Uživatelská skupina | Vytvářet, upravovat, připojit se, opouštět, sdílet, mazat a zobrazovat podrobnosti |

### O uživatelích { #about-users }

Každý uživatel v DHIS2 musí mít uživatelský účet, který je identifikován uživatelským jménem. Měli byste zaregistrovat křestní jméno a příjmení každého uživatele a také kontaktní informace, například e-mailovou adresu a telefonní číslo.

Je důležité, abyste zaregistrovali správné kontaktní informace. DHIS2 používá tyto informace k přímému kontaktování uživatelů, například k odesílání e-mailů k upozornění uživatelů na důležité události. Kontaktní informace můžete také použít ke sdílení například ovládacích  panelů a kontingenčních tabulek.

Uživatel v DHIS2 je přidružen k organizační jednotce. Měli byste přiřadit organizační jednotku, kde uživatel pracuje.

Když vytvoříte uživatelský účet pro okresního správce záznamů , měli byste mu jako organizační jednotku přiřadit okres, kde pracuje.

Přiřazená organizační jednotka ovlivňuje, jak může uživatel používat DHIS2:

- V aplikaci **Zadávání dat** může uživatel zadat data pouze za organizační jednotku, ke které je přidružena, a za organizační jednotky pod hierarchií. Například okresní záznamník bude moci registrovat údaje pouze za svůj okres a zařízení pod tímto okresem.

- V aplikaci **Uživatelé** může uživatel vytvořit nové uživatele pouze pro organizační jednotku, ke které je přidružena, kromě organizačních jednotek pod hierarchií.

- V aplikaci **Zprávy** si uživatel může prohlížet pouze zprávy pro svou organizační jednotku a níže uvedené. (To je něco, co považujeme za otevřenou vlastnost, která umožní srovnávací zprávy.)

Důležitou součástí správy uživatelů je kontrola, kterým uživatelům je povoleno vytvářet nové uživatele, s kterými orgány. V DHIS2 můžete určit, kteří uživatelé mohou provádět tento úkol. Klíčovým principem je, že uživatel může udělit pouze oprávnění a přístup k souborům dat, ke kterým má přístup sám uživatel. Počet uživatelů na národní, krajské a okresní úrovni je často relativně malý a mohou je vytvářet a spravovat správci systému. Pokud velká část zařízení zadává data přímo do systému, může se počet uživatelů stát nepraktickým. Doporučuje se tento úkol delegovat a decentralizovat na okresní úředníky, zefektivní to proces a lépe podpoří uživatele zařízení.

### O uživatelských rolích { #about-user-roles }

Role uživatele v DHIS2 je skupina oprávnění. Oprávnění znamená oprávnění k provádění jednoho nebo více konkrétních úkolů.

Role uživatele může obsahovat oprávnění k vytvoření nového datového prvku, aktualizaci organizační jednotky nebo zobrazení sestavy.

Uživatel může mít více uživatelských rolí. Pokud ano, oprávnění uživatele budou součtem všech oprávnění a datových sad v rolích uživatelů. To znamená, že můžete uživatelské role kombinovat a porovnávat pro speciální účely místo vytváření pouze nových.

Role uživatele je přidružena ke kolekci datových sad. To ovlivňuje aplikaci **Data Entry**: uživatel může zadávat data pouze pro datové sady registrované pro jeho uživatelskou roli. To může být užitečné, když například chcete povolit příslušníkům zdravotnických programů zadávat údaje pouze pro své příslušné formuláře pro zadávání údajů.

Doporučení:

- Vytvořte jednu uživatelskou roli pro každou pozici v organizaci.

- Souběžně s definováním toho, který uživatel provádí jednotlivé úlohy v systému, vytvářejte uživatelské role.

- Poskytněte rolím uživatelů pouze přesná oprávnění, která potřebují k výkonu své práce, ne více. Oprávnění k provedení úkolu by měl mít pouze ten, kdo má úkol provést.

### O skupinách uživatelů { #about-user-groups }

Uživatelská skupina je skupina uživatelů. Skupiny uživatelů používáte, když nastavujete sdílení objektů nebo oznámení, například nabízené zprávy nebo oznámení programu.

Viz také: 

[Sdílení](https://ci.dhis2.org/docs/master/en/user/html/sharing.html)

[Spravovat oznámení programu](https://docs.dhis2.org/master/en/user/html/manage_program_notification.html)

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

## Příklad: správa uživatelů ve zdravotním systému { #user_mgt_example }

V systému zdraví jsou uživatelé logicky seskupeni s ohledem na úkol, který vykonávají, a na pozici, kterou zaujímají.

1.  Definujte, kteří uživatelé by měli mít roli správce systému. Často jsou součástí národní divize HIS a měli by mít v systému plnou autoritu.

2.  Pro každou pozici vytvořte zhruba jednu uživatelskou roli.

Příklady běžných  pozic jsou:

| Pozice | Typické úkoly | Doporučené autority | Komentář |
| --- | --- | --- | --- |
| Správci systému | Nastavte základní strukturu (metadata) systému. | Přidejte, aktualizujte a odstraňte základní prvky systému, například datové prvky, ukazatele a datové soubory. | Metadata by měli upravovat pouze správci systému. <br> Pokud povolíte uživatelům mimo tým systémových administrátorů upravovat metadata, může to vést k problémům s koordinací. <br> <br> Aktualizace systému by měli provádět pouze správci systému. |
| Národní zdravotní manažeři <br> <br> Zdravotní manažeři provincie | Monitorujte a analyzujte data | Přístup k modulu přehledů, aplikacím **Mapy**, **Kvalita dat** a ovládacímu panelu. | Nepotřebujete přístup k zadávání dat, úpravě datových prvků nebo souborů dat. |
| Úředníci divize národního zdravotnického informačního systému (HISO) <br> <br> Okresní zdravotničtí pracovníci a informační důstojníci (DHRIO) <br> <br> Zdravotní záznamy a informační pracovníci zařízení (HRIO) | Zadejte data, která pocházejí ze zařízení, která toho nejsou schopna přímo <br> <br> Monitorujte, vyhodnocujte a analyzujte data | Přístup ke všem aplikacím pro analýzu a ověřování <br> <br> Přístup k aplikaci **Zadávání dat**. | - |
| Referenti pro zadávání dat | - | - | - |
