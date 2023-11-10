---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/data-approval.md"
revision_date: "2021-06-14"
---

# Schválení dat { #data_approval }

DHIS2 má volitelnou funkci, která umožňuje autorizovaným uživatelům schvalovat zadaná data. Umožňuje zkontrolovat a schválit data na vybraných úrovních v hierarchii organizačních jednotek, takže schválení sleduje strukturu hierarchie od nižších úrovní po vyšší úrovně.

Data jsou schválena pro kombinaci (a) období, (b) organizační jednotky a (c) pracovního postupu. Data mohou být schválena pro organizační jednotku, pro kterou jsou zadány, a také pro organizační jednotky vyšší úrovně, do kterých jsou data agregována. V rámci nastavení systému můžete vybrat úroveň (úrovně) organizační jednotky, na kterých jsou data schválena. Může být schválen na vyšších úrovních až poté, co byl schválen pro všechny podřazené této organizační jednotky na nižších úrovních pro stejný pracovní postup a období. Když schválíte pracovní postup, schválí se data pro všechny datové sady, které byly k tomuto pracovnímu postupu přiřazeny.

Po schválení kombinace období, organizační jednotky a pracovního toku budou datové sady spojené s tímto pracovním tokem pro dané období a organizační jednotku uzamčeny a jakékoli další zadávání nebo úpravy dat budou zakázány, dokud nebudou nejprve schváleny.

Například následující diagram ukazuje, že data již byla schválena pro organizační jednotky C a D, pro dané období a pracovní postup. Nyní může být schválen pro organizační jednotku B pro stejné období a pracovní postup. Není však připraven ke schválení pro organizační jednotku A. Než bude možné ji schválit pro organizační jednotku A, musí být schválena pro B a pro všechny další podřazené organizační jednotky A pro dané období a pracovní postup.

![Schvalování v organizační
jednotce](resources/images/data_approval/approval_hierarchy.png){.center width=50% }

## Schvalování a přijímání { #data_approvals_approving_accepting }

DHIS2 podporuje dva různé typy schvalovacích procesů: buď jednostupňový proces, kde jsou data schválena na každé úrovni, nebo dvoustupňový proces, kdy jsou data nejprve schválena a poté přijata na každé úrovni. To ilustruje následující diagram:

![Schvalování a
přijímám](resources/images/data_approval/approval_level_steps.png){.center width=69% }

V jednokrokovém procesu jsou data schválena na jedné úrovni a poté schválena na další vyšší úrovni. Dokud nebude schválen na další vyšší úrovni, může být na první úrovni neschválen. (Například pokud byla data schválena moje chyba, umožňuje to schvalovateli vrátit jejich chybu zpět.) Jakmile jsou data schválena na další vyšší úrovni, nemusí být schválena na nižší úrovni, pokud nebudou nejprve schválena na vyšší úrovni.

V dvoustupňovém procesu jsou data schválena na jedné úrovni a poté je schválení přijato na stejné úrovni. Toto přijetí provádí uživatel, který je oprávněn schvalovat data na další vyšší úrovni. Jakmile jsou data přijata, nemusí být změněna nebo neschválena, pokud nebudou nejprve _nepřijata_.

Proces ve dvou krocích DHIS2 nevyžaduje. Je to volitelný krok pro uživatele, který kontroluje data na další vyšší úrovni. Výhodou je uzamčení přijetí z níže uvedené úrovně, takže se recenzent nemusí obávat, že by se data mohla při kontrole kontrolovat zdola. Může jej také použít uživatel vyšší úrovně ke sledování toho, která data nižší úrovně již byla zkontrolována.

Dvoustupňový proces lze aktivovat zaškrtnutím **Před schválením je vyžadováno přijetí** v aplikaci SystemSettings v části Obecné.

## Autority pro schvalování údajů { #data_approvals_authorities }

Ke schválení dat vám musí být přiřazena role obsahující jedno z těchto oprávnění:

-   **Schválit data** - Můžete schválit data pro organizační jednotky, ke kterým jste přiřazeni. Toto oprávnění vám neumožňuje schvalovat data pro nižší úrovně pod organizační(mi) jednotkou(ami), ke kterým jste přiřazeni. To je užitečné k oddělení uživatelů oprávněných schvalovat na jedné úrovni od uživatelů oprávněných schvalovat na níže uvedených úrovních.

-   **Schválení dat na nižších úrovních** - Umožňuje schválit data pro všechny nižší úrovně pod organizačními jednotkami, které jsou vám přiřazeny. To je užitečné, pokud jste například uživatelem na úrovni okresu, jehož role zahrnuje schvalování dat pro všechna zařízení v tomto okrese, ale ne pro samotný okres. Pokud je vám přiděleno toto, stejně jako autorita _Schvaluje data_, můžete schválit data na úrovni organizační(ch) jednotek, kterým jste byli přiřazeni, a na jakékoli níže uvedené úrovni.

-   **Přijímá data na nižších úrovních** - Umožňuje přijímat data na úrovni těsně pod organizační(mi) jednotkami, které vám byly přiřazeny. Toto oprávnění lze udělit stejným uživatelům, kteří schvalují data. Nebo to může být dáno různým uživatelům, pokud chcete mít některé uživatele, kteří přijímají data z níže uvedené úrovně, a jinou sadu uživatelů, kteří schvalují data, aby přešli na další úroveň výše.

## Konfigurace schválení dat { #data_approvals_configuration }

V sekci aplikace _Údržba_ v části _Úroveň schválení dat_ můžete určit úrovně, na kterých chcete schválit data v systému. Klikněte na tlačítko Přidat nový na této stránce a vyberte úroveň organizační jednotky, na které chcete schválení. Bude přidán do seznamu nastavení schválení. Můžete nakonfigurovat systém pro schvalování dat na každé úrovni organizační jednotky nebo pouze na vybraných úrovních organizační jednotky.

Všimněte si, že když přidáte novou úroveň schválení, můžete volitelně zvolit sadu skupin možností kategorie. Tato funkce je popsána dále v této kapitole.

Také v údržbě pod _Data schválení pracovního toku_, můžete definovat pracovní postupy, které se použijí pro schválení dat. Každý pracovní postup lze přidružit k jedné, nebo více úrovním schválení. Jakékoli dva pracovní toky mohou fungovat na všech stejných úrovních schválení, jako jsou ostatní, některé na stejné a některé jiné úrovni nebo zcela odlišné úrovně.

Pokud chcete, aby byla data pro datovou sadu schválena podle pracovního postupu, přiřaďte pracovní postup k datové sadě, když přidáte nebo upravíte datovou sadu. Pokud nechcete, aby data pro datovou sadu podléhala schválení, nepřiřazujte této sadě dat žádný pracovní postup. U datových sad, které chcete schvalovat současně, je přiřaďte ke stejnému pracovnímu postupu. U datových sad, které chcete schválit nezávisle, přiřaďte každé datové sadě vlastní pracovní postup.

V části _Nastavení systému_ -> _Analytika_ můžete určit, která neschválená data (pokud existují) se objeví v analytice. Viz část „Nastavení Analytiky“ v této uživatelské příručce. Všimněte si, že uživatelé, kteří jsou přiřazeni k organizačním jednotkám, kde jsou data připravena ke schválení, mohou tato data vždy zobrazit v analytice, stejně jako uživatelé přiřazení k organizačním jednotkám na vyšší úrovni, pokud mají oprávnění _Schválit na nižších úrovních_ nebo _Zobrazit neschválené oprávnění k datům_.

## Viditelnost dat { #data_approvals_data_visibility }

Pokud je povolena možnost _Skrýt neschválená data v analytice_, data budou skryta před zobrazením uživateli přidruženými k vyšším úrovním. Při určování, zda by měl být datový záznam skrytý pro konkrétního uživatele, systém přidruží uživatele k určité úrovni schválení a porovná jej s úrovní, až na kterou byl datový záznam schválen. Uživatel je přidružen k úrovni schválení, která odpovídá úrovni organizační(ch) jednotek, s nimiž je propojena, nebo pokud na této úrovni neexistuje žádná úroveň schválení, další úroveň schválení spojená s úrovní organizační jednotky pod sebou. Uživateli bude umožněno zobrazit data, která byla schválena, a to až na úroveň bezprostředně pod její přidruženou úrovní schválení. Důvodem je to, že uživatel musí být schopen zobrazit data, která byla schválena níže, aby je mohl nakonec zobrazit a schválit sám.

Všimněte si, že pokud byl uživateli udělena autorita _Zobrazit neschválená data_ nebo _VŠE_ , bude moci zobrazit data bez ohledu na stav schválení.

_Zvažme následující příklad:_ Existují čtyři úrovně organizační jednotky s úrovněmi schválení spojenými s úrovní 2 a 4. _Uživatel A_ na úrovni země (1) bude spojen s úrovní schválení 1, protože úroveň schválení existuje na stejné úrovni jako na úrovni organizační jednotky. _Uživatel B_ je spojen s úrovní schválení 2, protože neexistuje žádná úroveň schválení přímo spojená s úrovní její organizační jednotky a úroveň schválení 2 je přímá úroveň níže. _Uživatel C_ je spojen s úrovní schválení 2. _Uživatel D_ je pod všemi úrovněmi schválení, což znamená, že vidí všechna data zadaná na nebo pod úrovní své organizační jednotky.

![Skrytí neschválených
dat](resources/images/data_approval/approval_data_hiding.png){.center}

V tomto příkladu pojďme zvážit některé scénáře:

-   Data se zadávají na úrovni zařízení: Data může zobrazit pouze _Uživatel D_, protože data ještě nebyla vůbec schválena.

-   Data jsou schválena od _Uživatele D_ na úrovni zařízení: Data se stanou viditelnými pro uživatele C a uživatele B, protože data jsou nyní schválena na jejich úrovni.

-   Data jsou schválena od _Uživatele C_ na úrovni okresu: Data se stanou viditelnými pro uživatele A, protože data jsou nyní schválena na úrovni bezprostředně pod sebou.

## Schvalování dat { #data_approvals_approving_data }

Chcete-li schválit data, přejděte na _Zprávy_ a vyberte _Schválení Dat_. Když toto hlášení zobrazuje data, která jsou nakonfigurována ke schválení, zobrazuje stav schválení dat v hlášení. Stav schválení bude jeden z následujících:

-   **Čekání na schválení organizačních jednotek na nižší úrovni** - Tato data ještě nejsou připravena ke schválení, protože je třeba je nejprve schválit pro všechny podřazené organizační jednotky této organizační jednotky, pro stejný pracovní postup a období.

-   **Připraveno ke schválení** - Tato data nyní mohou být schválena autorizovaným uživatelem.

-   **Schváleno** - Tyto údaje již byly schváleny.

-   **Schváleno a přijato** - Tyto údaje již byly schváleny a také přijaty.

Pokud jsou data, která prohlížíte, ve stavu schválení, na kterém lze jednat, a pokud máte dostatečné oprávnění, bude vám ve formuláři _Schválení Dat_ k dispozici jedna nebo více z následujících akcí:

-   **Schválit** - Schválit data, která dosud nebyla schválena, nebo která byla dříve schválena a pak byla neschválena.

-   **Neschválit** - Vraťte se k neschválenému stavu, který byl autorizován nebo přijat.

-   **Přijmout** - Přijmout data, která byla schválena.

-   **Nepřijmout** - Návrat do nepřijatých (ale stále schválených) údajů o stavu, které byly přijaty.

Chcete-li zrušit schválení dat pro danou organizační jednotku, musíte mít oprávnění schvalovat data pro tuto organizační jednotku nebo schvalovat data pro organizační jednotku vyšší úrovně, do které jsou tato data agregována. Důvod je následující: Pokud kontrolujete data ke schválení na vyšší organizační jednotce, měli byste zvážit, zda jsou data na nižších organizačních jednotkách přiměřená. Pokud všechna data nižší úrovně vypadají dobře, můžete data schválit na vyšší úrovni. Pokud některá data nižší úrovně vypadají podezřele, můžete data na nižší úrovni zrušit. To umožňuje, aby byla data znovu zkontrolována na nižší úrovni, v případě potřeby opravena a znovu schválena prostřednictvím úrovní organizační jednotky podle hierarchie.

## Schvalování podle sady skupin možností { #data_approvals_approving_by_cogs }

Při definování úrovně schválení určíte úroveň organizační jednotky, na které budou data schválena. Můžete také volitelně určit skupinu skupin možností možností. To je užitečné, pokud používáte skupiny možností kategorií k definování dalších dimenzí svých dat a chcete, aby schválení byla založena na těchto dimenzích. Následující příklady ilustrují, jak toho lze dosáhnout v rámci jedné skupiny skupin možností možností a pomocí více skupin skupin možností možností.

### Schvalování podle jedné sady skupin možností { #approving-by-one-category-option-group-set }

Předpokládejme například, že definujete sadu možností skupiny, která bude zastupovat nevládní organizace, které slouží jako partneři v oblasti zdravotní péče v jedné nebo více organizačních jednotkách. Každá skupina možností kategorie v této sadě představuje jiného partnera. Skupina možností kategorie pro partnera 1 může seskupovat možnosti kategorie (například kódy účtů financování), které tento partner používá jako dimenzi dat. Data zadaná partnerem 1 jsou tedy přiřazena možnosti kategorie ve skupině možností kategorie partner 1. Zatímco data zadaná partnerem 2 jsou přidělena možnosti kategorie ve skupině možností kategorie Partner 2:

<table align="center">
<caption> Příklad skupin kategorií možností </caption>
<thead>
<tr class="header">
<th> Sada skupin možností skupin </th>
<th> skupina možností kategorie </th>
<th> Možnosti kategorie </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Partner </td>
<td> Partner 1 </td>
<td> účet 1A, účet 1B </td>
</tr>
<tr class="even">
<td> Partner </td>
<td> Partner 2 </td>
<td> účet 2A, účet 2B </td>
</tr>
</tbody>
</table>

Každý partner mohl zadávat údaje pro své účty nezávisle na sobě, pro stejné nebo různé pracovní postupy, ve stejných nebo různých zařízeních. Například data lze zadávat a / nebo agregovat na následujících úrovních pro každého partnera, nezávisle na sobě:

![Příklad volby kategorie
skupiny](resources/images/data_approval/approval_partner_example.png){.center}

> **Tip**
>
> Funkci sdílení u možností kategorií a skupin možností kategorií můžete použít k zajištění toho, aby uživatel mohl zadávat data (a / nebo zobrazit data) pouze pro určité možnosti kategorií a skupiny. Pokud nechcete, aby uživatelé viděli data agregovaná nad rámec jejich přiřazených možností kategorií a / nebo skupin možností kategorií, můžete při přidávání nebo aktualizaci uživatele přiřadit _Vybraná omezení dimenze pro analýzu dat_.

Volitelně můžete definovat úrovně schválení pro data partnerů v rámci kterékoli nebo všech těchto úrovní organizační jednotky. Můžete například definovat některou nebo všechny následující úrovně schválení:

<table align="center">
<caption> Příklad Možnosti kategotie Skupin Nastavení úrovně schválení </caption>
<thead>
<tr class="header">
<th> Úroveň schválení </th>
<th> úroveň organizační jednotky </th>
<th> Sada skupin možností skupin </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> 1 </td>
<td> Země </td>
<td> Partner </td>
</tr>
<tr class="even">
<td> 2 </td>
<td> Okres </td>
<td> Partner </td>
</tr>
<tr class="odd">
<td> 3 </td>
<td> Zařízení </td>
<td> Partner </td>
</tr>
</tbody>
</table>

## Schvalování několika sadami skupin možností { #approving-by-multiple-category-option-group-sets }

Můžete také definovat úrovně schválení pro různé sady skupin možností kategorií. V pokračování příkladu předpokládejme, že máte různé agentury, které spravují financování různým partnerům. Například prostředky agentury A účty 1A a 2A, zatímco prostředky agentury B účty 1B a 2B. Mohli byste nastavit skupiny možností kategorií pro Agenturu A a Agenturu B a udělat je obě součástí sady skupin možností kategorií s názvem Agentura. Takže byste měli:

<table align="center">
<caption> Příklad sady skupin možností skupin s více kategoriemi </caption>
<thead>
<tr class="header">
<th> Sada skupin možností skupin </th>
<th> skupina možností kategorie </th>
<th> Možnosti kategorie </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> Partner </td>
<td> Partner 1 </td>
<td> účet 1A, účet 1B </td>
</tr>
<tr class="even">
<td> Partner </td>
<td> Partner 2 </td>
<td> účet 2A, účet 2B </td>
</tr>
<tr class="odd">
<td> Agentura </td>
<td> Agentura A </td>
<td> účet 1A, účet 2A </td>
</tr>
<tr class="even">
<td> Agentura </td>
<td> Agentura B </td>
<td> účet 1B, účet 2B </td>
</tr>
</tbody>
</table>

Nyní předpokládejme, že na úrovni země chcete, aby každý partner schválil údaje zadané tímto partnerem. Jakmile je toto schválení hotové, chcete, aby každá agentura poté schválila data z účtů, které tato agentura spravuje. Nakonec chcete schválit údaje na úrovni zemí napříč všemi agenturami. Můžete to udělat definováním následujících úrovní schválení:

<table align="center">
<caption> Příklad Více skupin možností Skupina nastavení úrovní schválení </caption>
<thead>
<tr class="header">
<th> Úroveň schválení </th>
<th> úroveň organizační jednotky </th>
<th> Sada skupin možností kategorií</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> 1 </td>
<td> Země </td>
<td> </td>
</tr>
<tr class="even">
<td> 2 </td>
<td> Země </td>
<td> Agentura </td>
</tr>
<tr class="odd">
<td> 3 </td>
<td> Země </td>
<td> Partner </td>
</tr>
</tbody>
</table>

Pro stejnou úroveň organizační jednotky lze definovat více úrovní schválení. V našem příkladu by partner 1 schvaloval data pro celou zemi na úrovni schválení 3 z možností kategorií Účet 1A a Účet 1B. Dále by Agentura A schválila celostátní údaje na úrovni schválení 2 z možností kategorie Účet 1A (po schválení Partnerem 1) a Účet 2A (po schválení Partnerem 2.) A konečně, po schválení všemi agenturami mohou celorepubliková data být schválen na úrovni schválení 1 ve všech volbách kategorie. Všimněte si, že úroveň schválení 1 neurčuje sadu skupin možností kategorií, což znamená, že slouží ke schválení dat napříč všemi možnostmi kategorií.

Tento příklad má být pouze ilustrativní. Můžete definovat tolik skupin možností kategorií, kolik potřebujete, a tolik úrovní schválení, kolik potřebujete, na stejné úrovni organizační jednotky pro různé sady skupin možností kategorií.

Pokud máte více úrovní schválení pro různé skupiny skupin voleb možností na stejné úrovni organizační jednotky, můžete změnit pořadí schválení v sekci _Nastavení_ v části _Nastavení schválení systému_. Stačí kliknout na úroveň schválení, kterou chcete přesunout, a vybrat _Posunout nahoru_ nebo _Posunout dolu_. Pokud máte úroveň schválení bez nastavených skupin skupin možností, musí to být nejvyšší úroveň schválení pro tuto úroveň organizační jednotky.
