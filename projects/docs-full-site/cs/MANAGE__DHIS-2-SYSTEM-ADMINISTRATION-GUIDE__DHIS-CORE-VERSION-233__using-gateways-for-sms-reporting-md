---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.33/src/commonmark/en/content/sysadmin/SMS-reporting.md"
---

# Používání bran pro SMS hlášení

<!--DHIS2-SECTION-ID:sms_report_sending-->

DHIS2 podporuje přijímání dat prostřednictvím [SMS](https://docs.dhis2.org/master/en/dhis2_user_manual_en/mobile.html), SMS však musí být pro ochranu informací utajeny. Aplikace DHIS2 pro Android funguje jako transparentní vrstva pro odesílání informací prostřednictvím SMS, kde se uživatel nemusí obávat psaní SMS. Chcete-li odesílat SMS pomocí aplikace pro Android, musí být správně nakonfigurována brána SMS. Tato část vysvětluje různé dostupné možnosti a jak toho dosáhnout.

## Odesílání SMS

<!--DHIS2-SECTION-ID:sms_report_sening-->

Je důležité nejprve objasnit, že tato část se týká hlavně nastavení **přijímání SMS** (z mobilních zařízení na server DHIS2), které je nezbytné při zvažování použití aplikace k odesílání (synchronizaci) informací zaznamenaných v aplikaci na server DHIS2 prostřednictvím SMS. V aplikaci to lze nastavit v nabídce *Nastavení* > *Nastavení SMS*

Odesílání SMS, tj. Ze serveru DHIS2 na mobilní zařízení, je nastaveno relativně snadno. Pokud je vyžadováno pouze zasílání upozornění na telefony uživatelů z DHIS2, když dojde k určitým událostem (zasílání zpráv, prahové hodnoty atd.), Je vyžadováno pouze odesílání SMS.

To vše lze nakonfigurovat na stránce Konfigurace služby SMS v sekci [Konfigurace mobilních zařízení](https://docs.dhis2.org/master/en/user/html/mobile_sms_service.html).

Podpora běžných poskytovatelů, jako jsou *Bulk SMS* a *Clickatell*, je ve výchozím nastavení k dispozici a oba poskytovatelé podporují odesílání SMS na čísla ve většině zemí.

Rovněž je možné pro odesílání a přijímání SMS použít jinou SMS bránu. Takže i když nastavíte řešení pro příjem SMS níže, je stále možné použít jedno z výše uvedených řešení pro odesílání SMS.

## Používání zařízení Android jako SMS brány

<!--DHIS2-SECTION-ID:sms_report_android_gateway-->

Nejjednodušším řešením je použití vyhrazeného zařízení Android jako vaší SMS brány. Jakýkoli telefon nebo tablet se systémem Android OS (4.4, Kitkat nebo novější) by měl být v pořádku. Bude vyžadovat stálé připojení k internetu, aby bylo možné přeposílat zprávy na váš server DHIS2, a také bude potřebovat SIM kartu pro příjem příchozích SMS.

Budete si muset stáhnout a nainstalovat aplikaci DHIS2 Android SMS Gateway do mobilního zařízení. Podívejte se na seznam [vydání](https://github.com/dhis2/dhis2-sms-android-gateway/releases), kde si můžete stáhnout nejnovější soubor APK k instalaci. Na stránce samotné aplikace jsou pokyny, ale v zásadě stačí spustit aplikaci a zadat podrobnosti o vašem serveru DHIS2 (URL, uživatelské jméno a heslo).

Jakmile je toto nastaveno a spuštěno, zadejte telefonní číslo tohoto zařízení brány na konfigurační stránce jakéhokoli jiného mobilního zařízení pomocí aplikace DHIS2 Capture. Poté, když jsou SMS zaslány z těchto reportovacích zařízení, budou přijaty na zařízení brány a automaticky přeposlány na server DHIS2, kde budou zpracovány.

**Používání tohoto zařízení brány je perfektní při testování funkčnosti SMS.** Bylo by skvělé, když pilotujete projekty, které vyžadují hlášení pomocí SMS. Pokud je zařízení připojeno k napájecímu zdroji a má stálé připojení k internetu, funguje dobře i pro malé projekty.

Při zvažování přesunu projektu do provozu by však bylo nutné prozkoumat jedno z trvalejších a spolehlivějších řešení pro brány níže.

### Odesílání SMS pomocí brány zařízení Android

Tato možnost není aktuálně podporována ani dokumentována.

## Vyhrazené brány SMS

<!--DHIS2-SECTION-ID:sms_report_dedicated_gateway-->

Tato část pojednává o použití trvalejších a vyhrazených bran SMS a dostupných možnostech. Každá z těchto možností níže bude zahrnovat poskytovatele (nebo sebe), který má připojení SMPP k telefonnímu operátorovi v zemi a pomocí tohoto připojení přijímá příchozí SMS a předává je na váš server DHIS2 přes internet pomocí protokolu HTTP.

Tato řešení mohou používat **dlouhé číslo** nebo **krátký kód**. Dlouhé číslo je standardní číslo mobilního telefonu typu, který používá většina soukromých osob, tj. +61 400123123. Krátký kód je jednoduše krátké číslo, například 311. Nastavení a údržba krátkých kódů je obvykle dražší.

### Zajištění správného formátování příchozích SMS na server DHIS2

Při odesílání příchozích SMS na server DHIS2 přes API používáte následující adresu URL: *https://<DHIS2_server_url>/api/sms/inbound*

V DHIS2 verze 2.34 a nižší vyžaduje tento koncový bod formát příchozích SMS ve velmi specifickém formátu, tj. Samotná zpráva musí být parametr s názvem text, telefonní číslo odesílatele musí být parametr s názvem originator.

Při použití všech níže uvedených možností brány SMS, když je nakonfigurujete pro přeposílání příchozích SMS na jinou webovou službu, budou mít každý svůj vlastní formát, který se bude lišit od toho, který se očekává v rozhraní DHIS2 API. Z tohoto důvodu je tedy nutné je před odesláním na server DHIS2 přeformátovat.

Jednou z možností je spustit vlastní velmi jednoduchou webovou službu, která jednoduše obdrží příchozí SMS od poskytovatele brány, přeformátuje ji na požadovanou pro DHIS2 a přepošle ji na vaše DHIS2 API. Takovou službu by musel napsat softwarový vývojář.

Ve verzi DHIS2 verze 2.35 se plánuje podpora těchto případů šablonovým systémem pro příchozí SMS, takže můžete určit formát zpráv, které budou odesílány od vašeho poskytovatele. Tímto způsobem můžete nakonfigurovat server DHIS2 tak, aby přijímal příchozí SMS od jakéhokoli jiného poskytovatele brány SMS, a oni mohou přímo odesílat příchozí SMS do rozhraní DHIS2 API, aniž by bylo nutné takovou webovou službu formátování.

### Použití RapidPro

[RapidPro](https://rapidpro.io/) je služba provozovaná organizací UNICEF ve více než 50 zemích po celém světě. Jedná se o soubor softwaru, který spolupracuje s vnitrostátními telefonními operátory a umožňuje organizacím navrhovat řešení SMS pro jejich projekty, jako jsou zprávy SMS nebo osvětové kampaně.

Služba RapidPro bude zahrnovat připojení SMPP k jednomu nebo více telefonním operátorům v zemi, obvykle prostřednictvím zkráceného kódu, který je potenciálně určen pro práci ve zdravotnictví pro nevládní organizace. Poté je možné přidat webhook, aby byly příchozí SMS přeposílány do jiné webové služby, jako je výše popsaná formátovací webová služba. Pokud se zkrácený kód používá také pro jiné účely, může být nutné přidat telefonní čísla vašich reportovacích zařízení do samostatné skupiny, aby se do webhooku předávaly pouze příchozí SMS z těchto zařízení.

RapidPro je v současné době zřízen a spuštěn ve zhruba polovině zemí, které v současné době používají nebo pilotují DHIS2. Před zvážením jednoho z níže uvedených řešení, které může být finančně i časově nákladné, stojí za to kontaktovat Unicef, abyste zjistili, zda je RapidPro k dispozici a zda jej lze použít pro hlášení zdravotního stavu ve vaší zemi.

### Používání komerčních poskytovatelů SMS bran

Z komerčních poskytovatelů brány SMS zmíněných v části Odesílání SMS výše budou mít obvykle schopnost *odesílat* SMS ve většině zemí, ale mohou podporovat *příjem* SMS pouze v omezeném počtu zemí. Většina zemí, které podporují příjem SMS, nejsou země, které používají DHIS2. Ze zemí, které používají DHIS2, je většina již pokryta službou RapidPro spuštěnou v zemi.

Stojí však za to prozkoumat, jaké komerční možnosti jsou pro vaši zemi k dispozici. V některých zemích budou existovat malé národní společnosti, které poskytují služby SMS, budou mít stávající spojení SMPP s poskytovateli telefonů, které můžete použít.

### Přímé používání telefonních operátorů

Pokud žádné z výše uvedených řešení není k dispozici, bylo by nutné obrátit se přímo na telefonní operátory ve vaší zemi. První otázka, kterou je třeba se zeptat, by byla, zda jsou si vědomi společností, které s nimi provozují spojení SMPP, na které byste se mohli obrátit.

Pokud ne, jako poslední možnost budete muset zvážit nastavení a udržování vlastního SMPP spojení s poskytovatelem telefonu. Ne všichni poskytovatelé telefonů však mohou takovou službu nabízet.

Budete muset spustit svůj vlastní server se spuštěným softwarem, jako je [Kannel](https://www.kannel.org/), který se připojuje (obvykle přes VPN) ke službě SMPP spuštěné v síti poskytovatelů telefonů. Pokud je toto nastaveno, všechny příchozí SMS pro nakonfigurované dlouhé číslo nebo zkrácený kód se odesílají z operátora telefonu na váš server Kannel a poté můžete tyto zprávy přeposílat výše uvedeným způsobem.

### Příjem zřetězených nebo vícedílných SMS

Při synchronizaci dat pomocí SMS s aplikací DHIS2 pro Android používá komprimovaný formát, aby využil co nejméně místa (znaků textu). Navzdory tomu se docela často stane, že zpráva přesáhne limit 160 znaků jedné standardní SMS. Na většině moderních mobilních zařízení budou tyto zprávy stále odesílány jako jedna zřetězená nebo vícedílná SMS a přijaty jako jedna zpráva. Při odesílání mezi dvěma mobilními zařízeními, když se jako brána používá zařízení Android, by toto mělo být zpracováno bez problémů.

Při výběru brány SMS je tedy důležité potvrdit, že použitý telefonní operátor podporuje zřetězené SMS. Většina z nich to bude podporovat, ale je důležité potvrdit, protože funkce SMS nebude fungovat, pokud jsou SMS rozděleny. To se spoléhá na něco, co se nazývá UDH (záhlaví dat uživatele). Při diskusi s poskytovateli se poté zeptejte, zda je podporována.
