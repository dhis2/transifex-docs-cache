---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/support.md"
revision_date: "2021-06-14"
---

# Podpora { #support }

Komunita DHIS2 používá sadu platforem pro spolupráci a koordinaci pro informace a poskytování stahování, dokumentace, vývoje, zdrojového kódu, specifikací funkcí, sledování chyb. Tato kapitola je bude podrobněji popisovat.

## Domovská stránka: dhis2.org { #home-page-dhis2org }

Domovská stránka DHIS2 se nachází na adrese *https://www.dhis2.org/*. Stránka _Downloads_ poskytuje odkazy na stažení souborů DHIS2 WAR, mobilní aplikaci Android Capture, zdrojový kód, vzorové databáze a odkazy na další zdroje a průvodce. Upozorňujeme, že poskytujeme aktualizace oprav údržby pro poslední tři verze DHIS2. Doporučujeme, abyste pravidelně kontrolovali stránku pro stahování a aktualizovali svůj online server nejnovější stabilní opravou pro vaši verzi DHIS2. Informace o verzi a revizi sestavení lze nalézt na stránce _O DHIS2_ uvnitř vaší instance DHIS2.

Navigační nabídka poskytuje jasné popisy obsahu webu a vyhledávací pole v horním záhlaví umožňuje snadné vyhledávání na webu.

## Platforma pro spolupráci: community.dhis2.org { #collaboration-platform-communitydhis2org }

Primární platformou pro spolupráci DHIS2 je _DHIS2 Komunita praxe_. Tato stránka je přístupná na adrese *https://community.dhis2.org/* a je založena na platformě Discourse.

Komunita praxe se používá k usnadnění podpory komunity pro problémy uživatelů DHIS2 a také k pomoci identifikovat potenciální chyby ve stávajících verzích softwaru a požadavky na funkce pro budoucí verze. Je to také místo, kde mohou členové komunity sdílet příběhy, osvědčené postupy a výzvy ze svých implementací DHIS2, spolupracovat s ostatními na projektech a nabízet své služby širší komunitě. Uživatelé si mohou nastavit své účty Komunity praxe na základě individuálních preferencí pro nastavení oznámení a mohou odpovídat na existující témata e-mailem.

Sekce _Podpora_ Komunity praxe zahrnuje všechna témata, která byla vytvořena pomocí předchozí platformy pro spolupráci DHIS2, Launchpad, která již není aktivní.

Chyby zjištěné na webu Komunity praxe by měly být zaslány základnímu týmu DHIS2 na _Jira_

## Hlášení problému { #reporting-a-problem }

Pokud při používání DHIS2 narazíte na problém, proveďte nejprve tyto kroky:

- Úplně vymažte mezipaměť webového prohlížeče (nazývanou také historie nebo data procházení) (můžete použít aplikaci Browser Cache Cleaner v DHIS2; před vymazáním vyberte všechny možnosti).

- Vymazání mezipaměti aplikace DHIS2: Přejděte na Správa dat -> Údržba zaškrtněte "Vymazat mezipaměť aplikace" a klikněte na "PROVEĎTE ÚDRŽBU".

Pokud problém přetrvává, přejděte na Komunitu praxe a pomocí klíčových výrazů vyhledejte témata, která zveřejnili ostatní uživatelé a která popisují podobné problémy, abyste zjistili, zda váš problém již nebyl nahlášen a vyřešen. Pokud nemůžete najít vlákno s podobným problémem, měli byste vytvořit nové téma v kategorii _Podpora_. Členové komunity a tým DHIS2 se pokusí pomoci s vyřešením vašeho problému.

Pokud odpověď, kterou jste obdrželi v Komunitě praxe, naznačuje, že jste identifikovali chybu, měli byste poslat zprávu o chybě na DHIS2 Jira.

## Sledování vývoje: jira.dhis2.org { #development-tracking-jiradhis2org }

_Jira_ je místo pro hlášení problémů a sledování požadavků, pokroku a plánu pro software DHIS2. Stránky DHIS2 Jira jsou přístupné na https://jira.dhis2.org/.

Pokud najdete chybu v DHIS2, můžete ji nahlásit na Jira tak, že přejdete na domovskou stránku DHIS2 Jira, kliknete na _vytvořit_ v horní nabídce, vyberete „chybu“ jako typ problému a vyplníte požadovaná pole.

Aby vývojáři mohli pomoci, potřebujete poskytnout co nejvíce užitečných informací:

- Verze DHIS2: Podívejte se na stránku Nápověda -\> O stránce uvnitř DHIS2 a poskytněte verzi a revizi sestavení.

- Webový prohlížeč včetně verze.

- Operační systém včetně verze.

- Protokol kontejneru servletů / Tomcat: Poskytněte jakýkoli výstup v protokolu Tomcat (obvykle catalina.out) týkající se vašeho problému.

- Konzola webového prohlížeče: Ve webovém prohlížeči Chrome klikněte na F12, poté na „Konzole“ a vyhledejte výjimky související s vaším problémem.

- Akce vedoucí k problému: Popište co nejjasněji, jaké kroky vedou k problému nebo výjimce.

- Popis problému: Popište jasně problém, proč si myslíte, že se jedná o problém a jaké chování byste od systému očekávali.

Vaše hlášení o chybě bude prošetřeno týmem Testing/QA a bude mu přidělen status. Pokud je platný, jeho stav bude nastaven na „TO DO“ a bude viditelný pro vývojový tým při plánování milníků a vydání. Poté jej lze přiřadit vývojáři a opravit. Všimněte si, že opravy chyb jsou začleněny do hlavní větve a větví až tří nejnovějších (podporovaných) verzí DHIS2 - takže více testování a zpětné vazby pro vývojářské týmy vede k vyšší kvalitě vašeho softwaru.

Pokud chcete navrhnout novou funkcionalitu, která bude implementována v DHIS2, měli byste nejprve zahájit diskuzi na Community of Practice, abyste získali zpětnou vazbu na svůj nápad a potvrdili, že funkce, kterou navrhujete, již neexistuje. Po dokončení těchto kroků můžete odeslat požadavek na funkci na DHIS2 Jira kliknutím na „Vytvořit“ v horní nabídce a výběrem „Funkce“ jako typ problému. Váš požadavek na funkci bude posouzen základním vývojovým týmem a bude-li přijat, bude mu přidělena vývojová a uvolněná verze. Uživatelé DHIS2 mohou hlasovat pro vyjádření podpory pro požadavky na funkce, které byly odeslány. Stávající požadavky na funkce lze procházet pomocí funkce "filtr" na Jira.

## Zdrojový kód: github.com/dhis2 { #source-code-githubcomdhis2 }

Různé větve zdrojového kódu včetně větví master a release lze procházet na *https://github.com/dhis2*
