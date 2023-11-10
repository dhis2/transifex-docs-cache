---
revision_date: "2021-08-10"
template: single.html
---

# Shrnutí { #implementation_guide_executive }

## Pozadí { #implementation_guide_executive_background }

Univerzita v Oslu v reakci na rostoucí míru adopce chytrých telefonů v subsaharské Africe a rozvojových zemích, se přidala k jasnému vedoucímu postavení Android Market Share, se rozhodla vybudovat novou aplikaci pro mobilní DHIS 2 pro Android, DHIS 2 Capture Android, která byla vydáno v září 2018. Tato práce vychází z poznatků získaných z předchozích mobilních aplikací DHIS 2 pro Android: Data Capture, Tracker Capture, Event Capture a Dashboard.

Aplikace pro Android DHIS 2 Capture je navržena tak, aby usnadnila práci v nastavení se špatným nebo žádným připojením, protože umožňuje uživateli pracovat offline a synchronizovat data později, když je připojení k dispozici. Usnadňuje sběr dat tím, že přináší všechny datové modely DHIS 2 do jediné konsolidované aplikace. Předpokládá se, že jej budou používat zdravotničtí pracovníci (pracovníci v první linii, poskytovatelé služeb, zaměstnanci zdravotnických středisek…) ve zdravotnických zařízeních a budou se přímo vykonávat na komunitní úrovni.

DHIS 2 Capture Aplikace pro Android se liší od webového DHIS 2. Webový DHIS 2 je určen k použití tam, kde mají uživatelé přístup k větším obrazovkám a dobrému připojení k internetu. Aplikace pro Android byla navržena s ohledem na uživatelskou zkušenost s menšími obrazovkami a se špatným nebo žádným připojením.

Výzkum ukazuje, že mobilní aplikaci eHealth lze snadno integrovat do péče, což zvyšuje produktivitu. Aplikace by měla usnadňovat sledování klientů, hlášení dat a rozhodování. Proveditelnost a použitelnost aplikace však může být negativně ovlivněna velkým objemem příjemců, nedostatkem zaměstnanců a problémy se softwarem a zařízeními. Monitorování v reálném čase, investice do programu a správné lidské zdroje budou potřebné pro úspěšnou integraci datových aplikací mobilních klientů pro zdravotnické pracovníky v první linii ve venkovských podmínkách a podmínkách chudých na zdroje [Rothstein JD1 et al. 2014](https://www.hindawi.com/journals/ijta/2016/2515420/).

## Cíle { #implementation_guide_executive_objectives }

Cílem tohoto dokumentu je poskytnout soubor pokynů pro nasazení aplikace Mobile DHIS 2 Capture pro Android. Kroky nasazení, které budou podrobněji popsány dále v dokumentu, zahrnují:

1. Aspekty bezpečnosti a ochrany údajů
2. Požadavky na mobilní zařízení
3. Instalace a nastavení
4. Testování (interní testování a akceptační test uživatele)
5. Testování v terénu a pilotní nasazení
6. Škálování (distribuce aplikací, správa mobilních zařízení, školení)
7. Zavádění

Je také zahrnuta mapa dokumentu, která seskupuje sekce dokumentu do fází projektu mobilní implementace. Všechny zde představené aspekty by měly být zváženy na začátku projektu a podle toho plánovány. Toto znázornění ilustruje, ve které fázi projektu budou mít zásadní význam. Která shrnula jeho klíčové aspekty a usnadňuje sledování těchto pokynů ve vašem projektu. Je důležité zdůraznit, že _cyklus reprezentovaný v mapovém dokumentu_ považuje proces shromažďování požadavků za dokončený. Mapu dokumentů najdete v první části.

V poslední části je zahrnut kontrolní seznam, který shrnuje jeho klíčové aspekty a usnadňuje sledování těchto pokynů ve vašem projektu.

## Cílové publikum { #implementation_guide_executive_target_audience }

Tento dokument je určen pro ty, kteří vedou proces nasazení od jeho raných fází, a měl by být sdílen s těmi, kteří jsou do procesu zapojeni.

# Mapa dokumentů { #implementation_guide_document_map }

![](resources/images/implementation-guide-document_map.png){ .center width=75% }

# Přehled DHIS 2 Capture pro Android { #implementation_guide_overview }

Tento dokument se zaměřuje na mobilní implementaci, která využívá novou aplikaci pro Android DHIS 2 Capture. Další informace o různých aplikacích DHIS 2 pro Android najdete v [App Store](https://www.dhis2.org/app-store) a v [Dokumentaci](https://www.dhis2.org/android-documentation) na webových stránkách. Předchozí sada vyvinutých aplikací DHIS 2 pro Android je aktuálně na plánovaném ukončení podpory a pouze s podporou opravné údržby:

- Aplikace Ovládací panel: Podpora byla ukončena od března 2020
- Aplikace Trasovač a Události: zastaralé od června 2020
- Aplikace Sběr dat: Plánované ukončení podpory od září 2020

Nová aplikace pro Android DHIS 2 Capture umožňuje offline sběr dat ve všech datových modelech DHIS 2\*. Data a metadata se automaticky synchronizují, kdykoli je přístup k internetu, přičemž se vždy zachovávají nejdůležitější data pro přihlášeného uživatele v místním zařízení.

## Snazší přihlášení a vylepšená ochrana dat { #implementation_guide_overview_easier }

URL serveru lze nastavit pomocí QR kódu. Aplikace si také zapamatuje dříve použité adresy URL a uživatelská jména. Jakmile je uživatel přihlášen, lze pomocí čtyřmístného kódu PIN zabezpečit aplikaci měkkým odhlášením.

## Konfigurovatelné téma aplikace a ikona { #implementation_guide_overview_configurable }

Vzhled aplikace, včetně ikony a barvy, je určen konfigurací serveru. Pomocí widgetu aplikace můžete vytvořit zástupce aplikace s logem vaší instituce na domovské obrazovce mobilního zařízení.

![](resources/images/implementation-guide-login.gif){ .center width=25% }

## Atraktivní, uživatelsky přívětivá navigace { #implementation_guide_overview_attractive }

Všechny programy a datové sady\* přístupné přihlášenému uživateli jsou integrovány do nové domovské obrazovky. Každý program nebo datová sada bude zobrazena s příslušnou ikonou a barvou.

![](resources/images/implementation-guide-user_friendly.gif){ .center width=25% }

## Plně funkční v režimu offline: inteligentní synchronizace { #implementation_guide_overview_fully_functional }

Místní databáze v mobilním zařízení uchovává synchronizovanou kopii programů a datových sad DHIS 2 dostupných pro přihlášeného uživatele. Nejrelevantnější data se také automaticky synchronizují.

- Trasované entity: ve výchozím nastavení až 500 aktivních registrací s upřednostňováním naposledy aktualizovaných uživatelských organizačních jednotky(ek) pro sběr dat.
- Události a datové sady: ve výchozím nastavení nejnovějších 1 000 událostí nebo 500 datových sad.

> **Poznámka** Tyto parametry lze konfigurovat

## Ovládací panel trasovače { #implementation_guide_overview_tracker_dashboard }

Výkonný datový model trasovače DHIS 2 byl plně implementován na malé obrazovce. Ovládací panel trasovače zahrnuje zpětnou vazbu, vztahy, indikátory a poznámky.

Aplikace implementuje logiku trasovače podporou většiny pravidel programu, což umožňuje přidávat, plánovat nebo odkazovat na nové události v závislosti na konfiguraci serveru.

![](resources/images/implementation-guide-tracker_search.png){ .center width=25% }

## Integrované vyhledávání pro trasovač { #implementation_guide_overview_integrated_search }

Než bude možné přidat novou trasovanou entitu, aplikace automaticky provede vyhledávání. Pokud je offline, hledání je v místní synchronizované databázi. a když bude online, navrhne záznamy ke stažení na základě konfigurace vyhledávání organizační jednotky uživatele. Tato funkce minimalizovala potenciální duplikáty, i když je uživatel offline.

## Zadání obrazových dat { #implementation_guide_overview_pictorial }

Zadávání dat ožívá - k ilustraci odpovědí na otázky lze použít ikony a barvy. K dispozici pro datové prvky s přidruženými sadami možností v programech pro jednotlivé události i pro sledování.

![](resources/images/implementation-guide-pictorial_entry.gif){ .center width=25% }

## Úplnost události { #implementation_guide_overview_event_completeness }

Během zadávání dat bude aplikace zobrazovat informace o aktuálním stavu dokončení programové fáze. Užitečné pro komplexní průzkumy s více oddíly.

# Požadavky na server DHIS 2 { #implementation_guide_dhis2_server }

Nová aplikace pro Android DHIS 2 Capture vyžaduje instanci DHIS 2 2.29 nebo vyšší spuštěnou na webovém serveru. Instance DHIS 2 může být umístěna na místním serveru, virtuálním počítači nebo ji lze zakoupit jako software jako služba (spravovaný hosting). Další informace o různých možnostech hostování DHIS 2 naleznete na adrese [https://www.DHIS2.org/hosting](https://www.dhis2.org/hosting).

Tato část poskytuje základní pokyny, jak nakonfigurovat server DHIS 2, který budete muset udělat v prvních dvou scénářích (v místním prostředí a ve virtuálním počítači). Ve třetím scénáři spravovaného hostování byste měli informovat svého poskytovatele, že budete nasazovat aplikaci pro Android, a vést otevřenou diskusi o nejlepších způsobech konfigurace serveru. Měli byste začít sdílením těchto pokynů se svým poskytovatelem spravovaného hostingu.

Server DHIS 2 musí být navržen a nakonfigurován s ohledem na: tok sběru dat, očekávanou analýzu dat a očekávané vizuální uživatelské rozhraní. Pro nasazení DHIS 2 budou zapotřebí minimálně tři servery: _Testovací_, _Produkční_ a _Školící_.

_Testovací_ server bude server, na kterém můžete změnit konfigurace serveru a otestovat výsledky těchto konfigurací. Jakmile budete spokojeni s konfigurací, školení uživatelů by mělo probíhat v jiném prostředí než _Produkční_. Dedikovaný server _Školící_ je ideálním prostředím, ve kterém budete školit své uživatele. Pro všechny účastníky vytvoříte uživatele DHIS 2 a zajistíte, aby všichni těmto změnám rozuměli a cítili se v nich dobře. Posledním krokem, jakmile otestujete konfigurace a proškolíte uživatele, bude nasazení konfigurace do prostředí _Produkční_. Nikdy byste neměli provádět změny konfigurace nebo trénovat své uživatele přímo do prostředí _Produkční_.

DHIS 2 je licencován pod [BSD](http://www.linfo.org/bsdlicense.html), což je licence s otevřeným zdrojovým kódem, a každý si jej může nainstalovat a používat zdarma. Správa instance DHIS 2 však zahrnuje více než nastavení výkonného webového serveru. Nasazení spolehlivého a škálovatelného systému zahrnuje alespoň tyto aspekty:

- Lidské zdroje se znalostmi příslušných technologií, jako jsou webové servery a databázové systémy.
- Spolehlivé zálohování vašeho systému včetně bezpečného úložiště na vzdáleném serveru.
- Použití SSL (HTTPS / šifrování) k zabezpečení soukromých informací, jako jsou hesla, v bezpečí.
- Monitorování prostředků serveru a výkonu aplikace.
- Stabilní a vysokorychlostní připojení k internetu.
- Stabilní napájecí zdroj včetně záložního napájecího řešení.
- Zabezpečené prostředí serveru, aby se zabránilo neoprávněnému přístupu, krádeži a požáru.
- Výkonný hardware s potenciálem škálování spolu se zvýšeným využitím systému.

Aplikace DHIS 2 Capture pro Android běží na mobilních zařízeních, včetně smartphonů, tabletů a Chromebooků. Je důležité sledovat počet programů, počet datových prvků a počet pravidel programu, která jsou uživateli na těchto mobilních zařízeních k dispozici. Měli byste také počítat s dostatkem času na vytvoření potřebných překladů pro vaši konfiguraci metadat. V případě dialogů, nabídek a dalších výzev aplikace, pokud aplikace není přeložena do jazyka, který potřebujete, zašlete nám prosím zprávu v [komunitě DHIS 2](https://community.dhis2.org) a my vám dáme vědět, jak přispět k překladu aplikace.

> **Pozor**
>
> Kromě zde uvedených požadavků na server DHIS2 si uvědomte, že aplikace DHIS2 pro Android může vyžadovat připojení k dalším službám a při zablokování těchto služeb nemusí aplikace plně fungovat. To může platit v implementacích, kde můžete používat přísná pravidla brány firewall, jako je například prostředí URL s nulovou sazbou na základě dohody s poskytovatelem ISP. V těchto případech možná budete chtít zahrnout do seznamu povolených adres URL následující:
>
> - Váš URL server DHIS2
> - [Adresy mapových schránek](https://docs.mapbox.com/help/troubleshooting/firewalls/)
> - Veřejný a/nebo soukromý server Matomo pro statistiky, jak je vysvětleno v [průvodci](https://docs.dhis2.org/en/full/implement/dhis2-android-configuration-guide.html#capture_app_andoid_settings_webapp)

# Zabezpečení dat a soukromí { #implementation_guide_datasec }

S novou aplikací DHIS 2 pro Android Capture budou uživatelé shromažďovat jednotlivá data v místě poskytování služby, což je nejnižší úroveň přímého sběru dat, protože zahrnuje přímého příjemce. Zachycení dat tímto způsobem umožňuje analytiku směrem nahoru bez kompromisů v podrobnostech, umožňuje analytiku směrem k sobě, snižuje chyby a umožňuje post hoc analýzu odpovídat na otázky identifikované po sběru dat a návrhu systému. Jednotlivá data však přinášejí informačním systémům další výzvy, včetně hledisek bezpečnosti a ochrany soukromí, připravenosti a kapacity, protože sběrateli dat s nižší gramotností v oblasti IT jsou poskytovány digitální nástroje a další komplikace, pokud jde o analytiku, úložiště a odezvu systému.

Existuje široká shoda ohledně potřeby poskytnout komplexní praxi zabezpečení dat. Tato komplexní bezpečnostní praxe by měla zahrnovat pouze _důvěryhodnost_ a _integritu_, ale také _dostupnost dat_. Harvardská humanitární iniciativa [uvedla](https://hhi.harvard.edu/publications/signal-code-ethical-obligations-humanitarian-information-activities), že samotné informace, včetně jejich generování, komunikace a přijímání, jsou základní humanitární potřebou, které by měla být poskytována ochrana stejná s jinými tradičními potřebami, jako je jídlo, voda, přístřeší a lékařská péče. The Roadmap for Health Measurement anccountability (MA4Health), [uvedl](https://www.healthdatacollaborative.org/fileadmin/uploads/hdc/Documents/the-roadmap-for-health-measurement-and-accountability.pdf), že „ Veřejné zdraví a klinickou péči nelze poskytovat bezpečně, vysoce kvalitně a nákladově efektivním způsobem bez bezproblémové, udržitelné a bezpečné výměny dat a informací na všech úrovních zdravotnického systému. “ Zachycování a ukládání údajů umožňujících identifikaci osob přesto přináší riziko a přiměřenou povinnost důsledných postupů v oblasti ochrany osobních údajů.

University of Oslo se zavázala k následujícímu:

1. Zajištění toho, aby proces vývoje a vydání softwaru DHIS 2 podléhal transparentnímu a přísnému plánu ověřování zabezpečení;
2. Prostřednictvím přístupu akčního výzkumu se univerzita snaží učit solidaritou s ostatními;
3. Snaha o rozvoj, učení a sdílení relevantních, aktuálních a užitečných informací a nástrojů na podporu správné bezpečnostní praxe;
4. Přístup ke všem zdravotním informacím v průběhu naší praxe se bude řídit přísnou a vzájemnou dohodou;
5. Využití akcí univerzity k poskytnutí dobrého příkladu bezpečnostní praxe.

Může existovat napětí mezi potřebou identifikovatelných údajů ve zdravotnickém systému a právem pacienta na soukromí. Vzhledem k tomu, že neexistují jasné právní předpisy upravující shromažďování a ukládání údajů umožňujících identifikaci osob, existují důležité koncepty, které by vlastníci a implementátoři systému měli pochopit a podporovat. Obsahují:

**Právo na přístup**

: Právo na přístup bude definováno předpisy o ochraně údajů každé země. Obecně to zahrnuje informace o účelech zpracování, kategoriích zpracovávaných osobních údajů, příjemcích nebo kategoriích příjemců, době uchovávání, informacích o právech subjektu údajů, jako je oprava, výmaz nebo omezení zpracování, právo vznést námitku, informace o existenci automatizovaného rozhodovacího procesu, včetně profilování atd. Pamatujte na předpisy specifické pro vaši oblast a ujistěte se, že jste připraveni vyhovět, než začnete shromažďovat údaje.

**Právo na výmaz**

: Právo na výmaz je definováno také předpisy o ochraně údajů každé země. Obecně platí, že osobní údaje musí být vymazány okamžitě, pokud již nejsou potřebné pro jejich původní účel zpracování, nebo pokud subjekt údajů odvolal svůj souhlas a pro zpracování neexistuje žádný jiný právní důvod. Opět se prosím ujistěte, že rozumíte předpisům ve vaší konkrétní oblasti a že jste připraveni vyhovět.

**Minimalizace dat**

: Základní myšlenka minimalizace dat spočívá v tom, že zpracování dat by mělo používat pouze tolik dat, kolik je požadováno pro splnění daného úkolu. Rovněž z toho vyplývá, že údaje shromážděné pro jeden účel nelze bez dalšího souhlasu použít k jinému účelu než k původnímu zpracování.

**Pseudonymizace**

: Jedná se o postup správy dat, díky kterému jsou osobní údaje méně identifikovatelné a zároveň jsou vhodné pro analýzu a zpracování. Toho lze dosáhnout nahrazením hodnoty některých datových polí jedním nebo více umělými identifikátory nebo pseudonymy. Pseudonymizovaná data lze obnovit, aby byly jednotlivci znovu identifikovatelní, zatímco anonymizovaná data nelze nikdy obnovit do původního stavu. V závislosti na předpisech platných ve vaší oblasti můžete definovat strategii pseudonymizace, která odpovídá předpisům a vašim potřebám.

**Trasovatelnost**

: Abychom mohli efektivně využívat data, musíme zajistit jejich integritu. Aby byla zajištěna jeho integrita, je důležité tyto údaje sledovat, když jsou shromažďovány, zpracovávány a přesunuty. Musíte rozumět: „co“, „kdy“, „proč“ a „kdo“. Organizace, které využívají výhodu sledovatelnosti, jsou schopny rychleji vyhledávat data a jsou schopny lépe podporovat požadavky na zabezpečení a ochranu osobních údajů.

Na základě předpisů vašeho území a složitosti vašeho projektu, včetně úrovně potenciálního rizika, musíte zavést vhodná technická a organizační opatření, jako je pseudonymizace, minimalizace dat, protokoly auditu, omezení vyhledávání, granulární sdílení atd., A integrovat nezbytná ochranná opatření pro zpracování údajů, aby byly splněny požadavky předpisů, které se vztahují na váš region.

Adekvátní přístup k zabezpečení / ochraně soukromí pro jakoukoli implementaci DHIS2, která zachycuje osobně identifikovatelná data, by zahrnoval vytvoření jasné zásady pojmenování jednotlivce (osob) s plným přístupem do systému, s odpovědností zajistit následující. U jakékoli technické podpory pro databáze obsahující citlivá data by pro všechny třetí strany měl být vyžadován podepsaný zákon o mlčenlivosti s jasným konečným datem.

|  | Možná praktická implementace |
| --- | --- |
| **Právo na přístup a právo na výmaz** | Poskytování přístupu k pacientovi jeho záznamu elektronicky za účelem jeho kontroly nebo odstranění není v DHIS 2 (2.32) k dispozici. Měli byste zajistit, abyste zavedli jiné metody, kterými může pacient požadovat kopii svého záznamu, aby jej mohl zkontrolovat a požádat o změny nebo o jeho vymazání. Pokud jeho odstranění není možné, měli byste záznam anonymizovat odstraněním / nahrazením všech identifikovatelných datových bodů. |
| **Minimalizace dat** | Zajistěte, aby existoval platný důvod pro shromažďování osobních identifikovatelných údajů. Neshromažďujte zbytečné podrobnosti, které neslouží praktickému účelu, pokud jde o analýzu dat nebo potřebu dokonalosti záznamu pacienta. Pokud je například potřeba následného sledování pacienta určena pozitivním výsledkem testu, neshromažďujte jméno pacienta, pokud je výsledek negativní. |
| **Pseudonymizace** | Zvažte použití alternativních hodnot pro záznam informací o určitých postupech nebo podmínkách pacienta. Například můžete mít seznam lékařských procedur / osobního chování / akcí uveden jako barevný seznam. To umožňuje provádět analytiku, aniž byste odhalili, co by mohlo být na daném území stigmatizovanou procedurou / akcí / chováním. |
| **Trasovatelnost** | DHIS 2 poskytuje podrobný protokol auditu pro každý datový bod. To zahrnuje sledování dat zachycených prostřednictvím jejích webových nástrojů (od 2.22), stejně jako importovaných nebo přes Android (od verze 2.27). Aktuálně (2.32) DHIS 2 neposkytuje možnost exportu úplného odstranění / anonymizace, protože odstranění hodnoty zachová předchozí data v protokolu auditu. Z tohoto důvodu by jakékoli sdílení exportovaných dat externím stranám mělo zahrnovat ruční odstranění citlivých / identifikovatelných dat. |

Praktická doporučení týkající se konfigurace DHIS 2, aby byla zaručena ochrana a zabezpečení dat, najdete v části [Úvahy o zabezpečení a ochraně dat](#configuration_security).

# Specifikace mobilního zařízení { #implementation_guide_mobile_specs }

Pokud váš projekt plánuje provést velkou akvizici zařízení, je dobré co nejvíce oddálit většinu akvizice. Cílem je získat nejlepší zařízení, které si můžete dovolit. Technologie, zejména mobilní zařízení, se vyvíjí velmi rychle. Daný model se obvykle obnovuje v ročním cyklu, což spotřebitelům poskytuje meziroční přístup k významným technickým vylepšením, ale s podobným cenovým bodem. Další doporučení týkající se akvizic najdete v části [<span class="underline">Rozšíření</span>](#scale-up).

Specifikace mobilních zařízení pro použití nasazení aplikace DHIS 2 pro Android jsou uvedeny v následující tabulce. Vezměte prosím na vědomí, že tato doporučení jsou velmi obecná, protože vaše zařízení bude výkonně ovlivněno vaší konfigurací. Například mít sledovací program se stovkami programových pravidel bude vyžadovat výkonnější zařízení než v implementaci, kde shromažďujete pouze malou sadu agregovaných dat.

Obecně řečeno, když si musíte vybrat různé verze Androidu, zaměřte se na vyšší. Nákup zařízení od známých značek může být také indikátorem lepšího poprodejního servisu, jako jsou opravy a / nebo aktualizace.

 <table>
 <thead>
 <tr class="header">
 <th> </th>
 <th> <b> mobilní telefony </b> </th>
 <th> <b> tablety </b> </th>
 <th> <b> Chromebooky </b> </th>
 </tr>
 </thead>
 <tbody>
 <tr>
 <td> <b> Stavba </b> </td>
 <td colspan="3"> Pravděpodobně nejdůležitější funkce: toto zařízení bude dělat hodně práce v terénu a musí vydržet více než 2 roky </td>
 </tr>
 <tr>
 <td> <b> značka </b> </td>
 <td colspan="3"> Pokud budete zodpovědní za správu mnoha zařízení, je snazší držet se jedné značky </td>
 </tr>
 <tr>
 <td> <b> OS </b> </td>
 <td colspan="2">
Minimum Supported: Android 4.4 (to be deprecated April 2022) <br />
Minimum Doporučeno pro nová zařízení: <b> Android 7.X </b> <br />
Doporučeno pro nová zařízení: <b> Android 8.X </b> nebo lepší
 </td>
 <td> Zařízení Chrome OS lze aktualizovat na nejnovější verzi systému Chrome OS alespoň 5 let po vydání. Zkontrolujte <a href="https://support.google.com/chrome/a/answer/6220366?hl=en"> <span class="underline"> zde </span> </a> </td>
 </tr>
 <tr>
 <td> <b> procesor </b> </td>
 <td colspan="2"> Doporučeno: 4 jádra, 1,2 GHz </td>
 <td> různé </td>
 </tr>
 <tr>
 <td> <b> RAM </b> </td>
 <td>
Minimum: 1 GB <br />
Doporučeno: 2 Gb nebo více
 </td>
 <td>
Minimum: 1,5 GB <br />
Doporučeno: 3Gb nebo více
 </td>
 <td>
Minimum: 4 GB <br />
Doporučeno: 4 až 8 GB
 </td>
 </tr>
 <tr>
 <td> <b> Úložiště </b> </td>
 <td colspan="2">
Minimum: 8 GB <br />
Doporučeno: 32 GB <br />
Aplikace DHIS 2 nevyužívá mnoho místa. Ukládání osobních obrázků a videí však zabírá spoustu místa
 </td>
 <td>
Minimum: 16 GB <br />
Doporučeno: 32-128 GB
 </td>
 </tr>
 <tr>
 <td> <b> Velikost obrazovky </b> </td>
 <td>
Minimum: 4 "<br />
Doporučeno: od 5,5 "
 </td>
 <td> Minimum: 7 "</td>
 <td> 11 "- 14" </td>
 </tr>
 <tr>
 <td> <b> Fotoaparát </b> </td>
 <td colspan="2">
Minimum: 5Mpx, s bleskem <br />
Doporučeno: minimálně 8 Mpx, flash
 </td>
 <td> volitelně </td>
 </tr>
 <tr>
 <td>
 <b> Příslušenství </b>
* Pouzdro, klávesnice, externí napájení *
 </td>
 <td colspan="2">
Zvažte vhodný vnější kryt a chránič obrazovky. U tabletů zvažte externí klávesnici pro ovládání na stole <br />
Zvažte napájení externí powerbanky (10 000 mAh - 20 000 mAh)
 </td>
 <td>
USB 3G / 4G modem <br />
Myš <br />
Webová kamera
 </td>
 </tr>
 <tr>
 <td> <b> Připojení </b> </td>
 <td colspan="2">
Rádio 4G (LTE) / 3G, <b> odemčené </b>. Pokud importujete zařízení, zkontrolujte kompatibilitu frekvenčních pásem s místními mobilními operátory <br />
Bluetooth 4.0 nebo lepší. WiFi 2,4 GHz &amp; 5 GHz
 </td>
 <td>
Bluetooth 4.0 nebo lepší. WiFi 2,4 GHz &amp; 5 GHz <br />
Externí USB 3G / 4G klíč nebo Wifi hotspot <br />
 </td>
 </tr>
 </tbody>
 </table>

> **Poznámka**
>
> Vezměte prosím na vědomí, že mobilní aplikace DHIS2 aktuálně spoléhá na některé (Služby Google Play)[https://developers.google.com/android/guides/overview], a proto nebude fungovat na zařízeních, která tuto službu nepoužívají. To je běžné u posledních telefonů Huawei a zařízení AOSP.

Tento soubor zde již není udržován, ale je zahrnut v (Průvodci správou systému)[https://github.com/dhis2/dhis2-docs/tree/master/src/commonmark/en/content/sysadmin]

# Konfigurace DHIS2 pro použití aplikace pro Android { #implementation_guide_dhis2_config }

Tato kapitola obsahuje základní aspekty konfigurace pro úspěšné používání aplikace pro Android, které vám pomohou pochopit důsledky používání mobilní komponenty DHIS 2. Pro úplnou a úspěšnou implementaci si prosím přečtěte podrobnou a aktualizovanou  [<span class="underline">dokumentaci</span>](https://www.dhis2.org/android-documentation) pro získání všech informací o konfiguraci serveru DHIS 2 pro použití s aplikací DHIS 2 pro Android Capture.

Aspekty nastavení nové aplikace pro Android DHIS 2 Capture obsažené v tomto dokumentu jsou:

- Aspekty související se zabezpečením
- Vytvoření uživatele systému Android
- Vizuální konfigurace
- Nastavení pravidel programu
- Definování indikátorů a legend programu
- Vyhrazená ID

## Aspekty související se zabezpečením { #implementation_guide_dhis2_config_sec }

### Používání sdílení DHIS 2 a omezení sdílení { #implementation_guide_dhis2_config_sec_sharing }

V této části budeme sdílet několik tipů, jak používat sdílení a omezení sdílení DHIS 2, abychom zajistili, že pouze ti správní uživatelé budou mít přístup k záznamům s identifikovatelnými informacemi.

Zde je praktický příklad granulárního sdílení a omezení vyhledávání v kontextu Centra zdravotní péče pro péči o matku a novorozence:

Uživatelská role porodní asistentky:

- Může vyhledávat ve třech programech ve všech organizačních jednotkách v okrese
- Může zapsat nové těhotné ženy do programu ANC
- Může přidávat / upravovat události do fáze programu klinického hodnocení
- Může zobrazit všechna data ANC ve vlastní organizační jednotce

Role uživatele Lab tech

- Může prohledávat jednu organizační jednotku programu v okrese
- Může přidávat / upravovat události do fáze laboratorního programu
- Nemůže zobrazit fázi klinického hodnocení

Role uživatele supervizora Ministerstva Zdravotnictví

- Lze zobrazit pouze ovládací panel

Je velmi důležité mít v rámci své strategie ochrany údajů standardní operační postupy (SOP).

SOP je sada podrobných pokynů sestavených vaší organizací, které vám pomohou provádět složité rutinní operace, jako jsou ty související s bezpečností dat.

SOP pomáhají vaší organizaci dosáhnout efektivity, kvality a konzistence při dodržení předpisů o ochraně dat.

Při definování vašich SOP pro ochranu údajů byste měli řešit otázky jako:

- Jaké jsou příslušné stávající právní předpisy?
- Kdo je jmenovaný kontrolor? Zpracovatel? Pověřenec pro ochranu osobních údajů?
- Kdo má za úkol kontrolovat protokoly auditu?
- Jaký je váš postup při odstraňování starých uživatelů?
- Přinesete si vlastní zařízení?
- Zabezpečení hardwaru?
- Dohody o vzájemné mlčenlivosti

Zde uvádíme některé SOP Best Practices převzaté z [DHIS 2 Community Health Information System Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/CHIS+Guidelines+En.pdf) dokumentu vydaného univerzitou v Oslu:

1. Harmonizujte více programů do jednoho protokolu pro sběr dat.
2. Vypracovat SOP pro každý jednotlivý komunitní projekt, zejména pokud existuje více toků dat.
3. Proměňte SOP na ilustrované plakáty a nechte zaměstnance zařízení umístit je na své zdi pro veřejné prohlížení.
4. Vytiskněte SOP a ujistěte se, že všichni komunitní zdravotní pracovníci, zaměstnanci zařízení a zaměstnanci okresů mají kopie
5. Zúčastněné strany podepíší SOP po dokončení školení.
6. Účast zúčastněných stran na vytváření a schvalování SOP. SOP musí institucionalizovat osvědčené postupy a pracovní postup aktérů v CHIS. Zahrnout do procesu vývoje SOP zastoupení všech příslušných zúčastněných stran.
7. Zajistěte, aby byly zachyceny všechny datové prvky a indikátory. CHW by měli jasně chápat význam a měření každého datového prvku a indikátoru, aby se odstranila nejednoznačnost
8. Na školení používejte pokyny pro sběr dat. K vybudování odpovědnosti musí komunitní zdravotní pracovníci a zaměstnanci zařízení vědět, že jsou součástí většího systému. Potřebují vědět, jak se jejich data používají pro plánování na vyšších úrovních a konkrétní akce na nižších úrovních.
9. Nechte komunitním zdravotním pracovníkům vysvětlit pokyny pro sběr dat. Tato metoda zpětného učení je účinná praxe učení dospělých. Vysvětlení pokynů pro sběr dat zvyšuje důvěryhodnost komunitních zdravotních pracovníků u výboru pro zdraví.
10. Vytvářejte snadno použitelné pokyny v místním jazyce. komunitní zdravotní pracovníci a zaměstnanci zařízení potřebují průvodce a pokyny, co mají dělat. Zvažte vytvoření plakátů nebo malých laminovaných přenosných pokynů pro sběr dat pro komunitní zdravotní pracovníky a zařízení, která budou umístěna na zeď nebo s sebou, a která na základě pokynů pro sběr dat stanoví jejich roli a odpovědnosti.
11. Nechte podepsat pokyny pro komunitní zdravotní pracovníky, zařízení, zaměstnance okresu a národní zaměstnance. Toto je symbolické opatření „závazku“. Cílem je, aby si je přečetli, pochopili své odpovědnosti za podávání zpráv definované v pokynech pro sběr dat a budou tyto povinnosti plnit.
12. Produkujte jednoduchá videa nebo mluvené slovo a nahrávejte je do telefonů. Odpovědnosti a akce pro každou událost jsou usnadněny jednoduchým videem nebo zvukovým průvodcem v místním jazyce, na které se mohou zaměstnanci zařízení a komunitní zdravotní pracovníci obrátit.

### Praktické pokyny pro zabezpečení dat { #implementation_guide_dhis2_config_sec_practical }

Zajištění toho, aby osobní údaje uložené v mobilních zařízeních byly přístupné pouze oprávněnému zdravotnickému personálu, začíná poučením uživatelů o tom, jak tyto údaje používat, a zajištěním jejich nepřetržitého zabezpečení. Níže uvedené pokyny jsou výňatkem z příručky PSI „Monitorovací a vyhodnocovací standardní operační postupy pro zachování a zachování důvěrnosti údajů o klientech“.

![](resources/images/implementation-guide-image31.png){ .center }

Při konfiguraci úrovně přístupu uživatele hrají důležitou roli správci systému tím, že zajišťují, že jejich přístup k datům je vhodný a nikdy zbytečně nepřiměřený. Pokyny níže jsou také součástí příručky PSI „Zachování údajů o klientech v bezpečí a důvěrných správců“

.![](resources/images/implementation-guide-image13.png){ .center }

## Vytvoření uživatele systému Android { #implementation_guide_dhis2_config_creating_user }

### Vytvořit roli { #implementation_guide_dhis2_config_creating_user_role }

Před vytvořením uživatele musíte nejdříve definovat roli uživatele DHIS 2. Aplikace DHIS 2 pro Android Capture nevyžaduje žádné z orgánů, které jsou zapouzdřeny v uživatelské roli. Zabezpečení programu nebo datové sady DHIS 2 je nastaveno jako přístup k datům programu nebo datové sady.

Pro účely řešení problémů s laděním webu u vašich uživatelů se doporučuje vytvořit a přiřadit uživatelskou roli s funkcí zachycování dat, která by měla zahrnovat:

- Aplikace Tracker Capture, aplikace pro zachycení událostí a / nebo aplikace pro zadávání dat
- Ovládací panel (pro přihlášení)
- Cache Cleaner (budete muset vyčistit mezipaměť)

![](resources/images/implementation-guide-image3.png)

> **Poznámka**
>
> Když uživatelé zadají TEI a když není synchronizováno se serverem, budou moci odstranit TEI a zápis, i když jim nebyly přiděleny konkrétní oprávnění. Toto je záměrné a umožňuje uživatelům vrátit se zpět v případě, že zadali nesprávná data (TEI a/nebo zápis), a tak zabránit jejich dosažení na server a vyžadovat jiného uživatele s vyššími oprávněními k vyřešení problému.

### Vytvořit uživatele { #implementation_guide_dhis2_config_creating_user_user }

Za druhé, měli byste vytvořit uživatele, pro kterého budete muset přidat některé základní podrobnosti, jako je uživatelské jméno a přiřadit mu roli.

- Uživatelské jméno: name.android
- Příklad: belen.android
- Přiřazení role uživatele: přiřaďte roli, kterou jste vytvořili v prvním kroku.

### Přiřadit organizační jednotky { #implementation_guide_dhis2_config_creating_user_assign }

Třetím krokem je přiřadit organizační jednotky uživateli, kterého jste právě vytvořili.

Existují tři typy přiřazení organizačních jednotek:

- **Zachycení dat:** Datové sady a program vytváření TEI, zápisy a události. Data předem stažená v aplikaci při prvním přihlášení budou ta, která patří k těmto organizačním jednotkám.
  - Od mobilních uživatelů se neočekává přístup k hierarchii org. jednotek celé země. Maximální počet organizačních jednotek je obtížné nastavit, protože aplikace nestanoví limit, ale prostředky v zařízení (paměť, procesor). Dalo by se říci, že 250 organizačních jednotek by mělo být bezpečných, ale přesto věříme, že je to velmi velké číslo pro případ použití v mobilu.
- **Výstup dat:** pro analýzu dat. Nelze použít v systému Android.
- **Vyhledání org. jednotek:** Rozšiřte vyhledávání TEI (je-li online) o další organizační jednotky. Jednotlivé záznamy lze stáhnout pro offline použití.
  - Při konfiguraci vyhledávání org. jednotek se ujistěte, že vaše zachycené org. jednotky jsou obsaženy ve vašich vyhledávaných org. jednotkách. Aby to bylo možné, musí být vybrány zachycené org. jednotky stejně jako vyhledávané org. jednotky.

![](resources/images/implementation-guide-image39.png){ .center width=80% }

## Vizuální konfigurace: Porozumění tomu, co se vykresluje a proč { #implementation_guide_dhis2_config_visual_config }

Zobrazené informace a způsob jejich zobrazení lze konfigurovat správcem systému. K dispozici je knihovna ikon s více než čtyřmi stovkami obrázků. Ikony lze přiřadit k většině objektů metadat: Možnosti, Datové prvky, Atributy, Programy / Sady dat. Během procesu synchronizace metadat se obrázky nestahují - stáhne se pouze název ikony. Všechny ikony již existují jako vysoce efektivní vektorové obrázky v APK aplikace.

V budoucnu budete moci nahrát svůj vlastní jako gif / jpeg / png (50k nebo méně - TBC). Nevýhodou této možnosti bude čas a doba synchronizace na základě propustnosti dat, protože aplikace bude muset stahovat obrázky během synchronizace metadat.

Zde je příklad toho, jak metadatům přiřadit ikony a barvy:

![](resources/images/implementation-guide-image10.png)

Následující tabulka ukazuje, kde dnes můžete ikony používat:

|  | **Přiřadit** | **Vykreslení v Androidu** | **Vykreslení na Webu** |
| --- | :-: | :-: | :-: |
| TrackedEntityType | ✅ 2.30 | brzy |  |
| Program | ✅ 2.30 | ✅ | ✅(jednoduché události, 2.30) |
| Fáze programu | ✅ 2.30 | ✅ | ✅(jednoduché události, 2.30) |
| DataSet | ✅ 2.31 | brzy |  |
| Datový prvek | ✅ 2.30 | - |  |
| Atribut | ✅ 2.30 | - |  |
| Indikátor | ✅ 2.32 | brzy |
| Indikátor Programu | ✅ 2.32 | brzy |  |
| Sada možností | ✅ 2.30 | ✅ | ✅(jednoduché události, 2.31) |

Pro fáze programu lze sekce vykreslit ve třech režimech: Listing, Sequential a Matrix. Výsledky těchto režimů jsou uvedeny níže:

![](resources/images/implementation-guide-image4.png){ .center }

Správce systému může rozhodnout o nejlepším způsobu vykreslení informací v každé části programové fáze nastavením typu mobilního vykreslení, jak je znázorněno na následujícím obrázku.

![](resources/images/implementation-guide-image15.png){ .center }

## Nastavení pravidel programu { #implementation_guide_dhis2_config_setting_pr }

Doporučujeme otestovat aplikaci pro Android paralelně s konfigurací pravidel vašeho programu, abyste se ujistili, že se vaše změny na serveru správně projeví a fungují v aplikaci.

První věcí, kterou musíte udělat při nastavování pravidel programu, je definovat kontext a prioritu pro provádění pravidla. Kontext definuje provedení pravidla pro konkrétní program a volitelně pro konkrétní fázi. Priorita definuje příkaz k provedení pravidel, což pomáhá, když provedení jednoho nebo více pravidel závisí na výsledku jiných pravidel.

![](resources/images/implementation-guide-image41.png){ .center }

Jakmile je definován kontext a priorita, je čas napsat výraz pravidla programu pomocí vestavěných proměnných, proměnných (atributy TEI / datové prvky PS) a funkcí. Proměnné musí definovat správce, aby bylo možné vyhodnotit informace zadané pro atribut TEI nebo datový prvek fáze programu.

![](resources/images/implementation-guide-image40.png){ .center }

Poté musíme rozhodnout o akci nebo akcích, které mají být provedeny, když je výraz pravidla programu pravdivý

![](resources/images/implementation-guide-image38.png){ .center }

Při nastavování pravidel programu byste si měli být vědomi toho, co podporuje aplikace DHIS 2 pro Android. Aktualizovaný seznam můžete zkontrolovat v [konfiguračním průvodci](https://docs.dhis2.org/master/en/dhis2_android_capture_app/about-this-guide.html).

## Definování indikátorů a legend programu { #implementation_guide_dhis2_config_defining_prog_ind }

Indikátory, které se mají zobrazit v aplikaci, lze vypočítat na základě dat ze zápisu sledované instance subjektu (TEI). Pamatujte, že výpočty budou platit v doméně TEI a aktuálního zápisu.

Typy agregace nejsou k dispozici, při výpočtu indikátoru lze použít pouze poslední hodnotu. Ve výpočtech lze použít všechny DE a konstanty. Proměnné jsou podporovány podle následující tabulky:

![](resources/images/implementation-guide-image37.png){ .center }

Aktualizované informace o tom, co je podporováno při použití indikátorů programu, můžete zkontrolovat v [konfiguračním průvodci](https://docs.dhis2.org/master/en/dhis2_android_capture_app/program-indicators.html). Hranice analytického období nejsou podporovány ani plánovány pro budoucí podporu, protože se vztahují na více TEI.

Chcete-li v aplikaci zobrazit indikátor programu, musíte v průvodci konfigurací indikátoru serveru DHIS 2 zaškrtnout políčko „Zobrazit ve formuláři“.

![](resources/images/implementation-guide-image20.png)

Jakmile svůj indikátor navrhnete, můžete mu přiřadit legendu. Na serveru DHIS 2 přejděte do části Údržba > Ostatní > Legendy a vytvořte novou legendu.

|  |  |
| --- | --- |
| ![](resources/images/implementation-guide-image9.png) { .center } | ![](resources/images/implementation-guide-image16.png) { .center } |

Jakmile legendu vytvoříte, můžete ji přiřadit indikátoru. Alternativně můžete přiřadit již existující legendu. Přímo pod zaškrtávacím políčkem pro zobrazení indikátoru v aplikaci najdete sekci pro vyhledávání a přiřazení legendy.

|  |  |
| --- | --- |
| ![](resources/images/implementation-guide-image32.png){ .center } | ![](resources/images/implementation-guide-image26.png){ .center } |

## Vyhrazená ID { #implementation_guide_dhis2_config_reserved_id }

Pokud pracujete s programy pro trasování a používáte automaticky generované jedinečné atributy sledované entity (viz [dokumentace DHIS 2](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#create_tracked_entity_attribute)) , je důležité pochopit, jak se aplikace zabývá generováním hodnot. Hodnoty se stahují předem ze serveru, takže jsou k dispozici, když aplikace pracuje offline. Tyto hodnoty jsou na straně serveru označeny jako rezervované.

Při první synchronizaci uživatele aplikace stáhne 100 hodnot, které budou na straně serveru označeny jako rezervované. Od tohoto bodu začne uživatel používat hodnoty, když se vytvářejí nové trasované instance entit.

Pokaždé, když uživatel použije hodnotu (zaregistruje instanci sledované entity), aplikace:

1. Zkontrolujte, zda zbývá dostatek zbývajících hodnot, a podle potřeby doplňte (pokud je k dispozici méně než 50 hodnot).
2. Přiřaďte první dostupnou hodnotu instanci trasované entity a odeberte ji ze seznamu dostupných hodnot.

Kdykoli se aplikace synchronizuje, bude:

1. Odstraňte rezervované hodnoty, jejichž platnost vypršela.
2. Zkontrolujte, zda zbývá dostatek zbývajících hodnot, a podle potřeby doplňte (pokud je k dispozici méně než 50 hodnot).

Hodnota je považována za „prošlou“, když je splněna jedna z následujících podmínek:

- „expiryDate“ je po splatnosti. Ve výchozím nastavení server nastavuje dobu platnosti na 2 měsíce.
- Pokud je atributový vzor závislý na čase, tj. Obsahuje segment \`CURRENT_DATE(format)\`, aplikace vypočítá další datum vypršení platnosti na základě tohoto vzoru.

> **Pozor**
>
> Pokud používáte automaticky generované jedinečné hodnoty, které obsahují data jako součást vzoru, expiryDate těchto hodnot bude spojeno s tímto vzorem data, což může mít za následek neočekávané chování, pokud vzor není dobře definován.
>
> _Příklad_: Hodnota _UniqueID_ byla nakonfigurována se vzorem jako CURRENT_DATE(MM)-SEQUENTIAL(###)  a dnes je 31. ledna, aplikace by stáhla 100 hodnot (od 01-001 do 01-101), aby umožnila aplikace pracující offline a s dostatečným počtem hodnot, ale zítra, 1. února, by aplikace neměla žádné dostupné hodnoty, protože všechny by byly označeny jako prošlé a tak by zobrazila takovou zprávu.

V aplikaci může uživatel také zkontrolovat dostupné hodnoty a znovu je vyplnit v nabídce nastavení.

|  |  |
| --- | --- |
| ![](resources/images/implementation-guide-image14.jpg){ .center width=50%} | ![](resources/images/implementation-guide-image22.jpg){ .center width=50%} |

Když aplikaci dojde hodnoty a server nemůže poskytnout další, obdrží uživatel ve formuláři pro zadávání dat zprávu, že již nejsou k dispozici žádné další hodnoty. Měli byste to opravit na straně serveru.

# Instalace nové aplikace DHIS 2 Capture { #implementation_guide_installing }

Zde lze aplikaci stáhnout a nainstalovat ze dvou míst:

- [**Google Play:**](https://play.google.com/store/apps/details?id=com.dhis2&hl=en_US) - Tato verze neumožňuje vysílání obrazovky ani pořizování snímků obrazovky.
- [**GitHub**](https://github.com/dhis2/dhis2-android-capture-app/releases) - There are two versions available in Github:
  - Produkční verze _no_sms_: Stejná verze než Google Play, neumožňuje vysílání obrazovky ani pořizování snímků obrazovky
  - Produkční verze: Stejná verze než Google Play, ale včetně možnosti SMS (aktuálně blokovaná Google Play), neumožňuje vysílání na obrazovce ani pořizování snímků obrazovky
  - Tréninková verze: S vysíláním obrazovky a možností pořizovat snímky obrazovky (ten s příponou \_training.apk)

> **Poznámka**
>
> Při instalaci tréninkového souboru APK možná budete muset povolit instalace 3rd, třetích stran

Přečtěte si prosím část o distribuci aplikací, abyste pochopili důsledky používání různých distribučních kanálů.

## Migrace ze starých aplikací { #implementation_guide_installing_migrating }

Než začnete s instalací nové aplikace pro Android DHIS 2 Capture v terénu, je důležité si uvědomit, že pokud vaši uživatelé již používají starou generaci DHIS 2 Android Event Capture nebo Tracker Capture, měli by postupovat podle těchto kroků:

1. Synchronizujte data aktuální aplikace DHIS 2, kterou používáte
2. Stáhněte si a nainstalujte novou aplikaci DHIS 2 pro Android Capture
3. Přihlaste se pomocí svých přihlašovacích údajů.

> **Varování**
>
> Odstranění aplikace bez synchronizace může způsobit ztrátu informací.

## Přihlaste se do aplikace { #implementation_guide_installing_login }

K přihlášení budete potřebovat URL serveru DHIS 2, uživatelské jméno a heslo právě vytvořeného uživatele. Pro účely testování můžete také použít testovací servery a přihlašovací údaje:

| URL | Uživatel | Heslo |
| --- | --- | --- |
| Nejnovější verze DHIS 2 <br /> [https://play.dhis2.org/android-current](https://play.dhis2.org/android-current) | android | Android123 |
| Předchozí verze DHIS 2 <br /> [https://play.dhis2.org/android-previous1](https://play.dhis2.org/android-previous1) | android | Android123 |
| Druhá předchozí verze DHIS 2 <br /> [https://play.dhis2.org/android-previous2](https://play.dhis2.org/android-previous2) | android | Android123 |

# Testování { #implementation_guide_testing }

Nyní, když byl server DHIS 2 původně nakonfigurován a aplikaci jste nainstalovali do jednoho nebo více zařízení, jste připraveni zahájit testování. Při plánování testování si musíte být vědomi nadcházejících verzí. Je důležité být součástí komunity na [https://community.dhis2.org/](https://community.dhis2.org/) a používat [JIRA](http://jira.dhis2.org/), nástroj pro správu softwaru, který UiO využívá. To vám umožní dozvědět se o otevřených problémech, pokud jde o funkce a opravy chyb, které jsou naplánovány pro budoucí vydání.

Doporučujeme otestovat aplikaci pro Android paralelně s vaší konfigurací, abyste se ujistili, že se vaše změny na serveru správně projeví a fungují v aplikaci. To je zvláště důležité během konfigurace pravidel programu. Kromě tohoto testování krok za krokem existují různé typy testování, které byste měli provést před spuštěním aplikace.

Existuje počáteční sada testů, které by měly být prováděny interně s menšími skupinami, aby bylo zajištěno, že konfigurace jsou provedeny správně, funkčnost je na místě a že vzhled a chování je adekvátní. V rámci této počáteční fáze testování budete provádět tzv. Interní testování, po kterém bude následovat testování UAT (User Acceptance Testing). Dále v této části rozvedeme, co tyto typy testů znamenají a jak je provádět. Poté provedete testování v terénu a pilotujete. V této fázi testování provedete sadu testů s většími skupinami, abyste mimo jiné zaručili, že vaše pracovní toky, vaše infrastruktura a architektura jsou správné. Dále v této části se budeme dále zabývat těmito typy testů a jejich prováděním.

Následující grafy ukazují, že další kroky jsou iterativní povahy, včetně nových konfigurací serveru založených na výsledcích testování. S největší pravděpodobností provedete několik kol testování a překonfigurování, než budete připraveni na zvětšení a spuštění.

|  |  |
| --- | --- |
| ![](resources/images/implementation-guide-image35.png){ .center } | ![](resources/images/implementation-guide-image7.png){ .center } |
| ![](resources/images/implementation-guide-image36.png){ .center } | ![](resources/images/implementation-guide-image5.png){ .center } |

## Obecná doporučení pro testování aplikace pro Android { #implementation_guide_testing_general }

Než půjdeme do různých fází testování, představíme několik obecných doporučení, která lze použít k testování aplikace pro Android. Obecně lze jakýkoli proces testování shrnout do následujících kroků:

![](resources/images/implementation-guide-image21.png){ .center width=80% }

1. **Posouzení**. Prvním krokem je zkontrolovat informace o samotné aplikaci tak, že přejdete na [<span class="underline">https://www.DHIS 2.org/android-documentation</span>](https://www.dhis2.org/android-documentation). Dokumentace vám poskytne informace o tom, proč a co nebo vaše testování. Mělo by vám pomoci určit, zda aplikace splňuje vaše požadavky, co může a nemůže dělat, a pomoci vám analyzovat nesrovnalosti. Mělo by vám také pomoci identifikovat nové funkce a nastavení, podporované funkce.

2. **Plán**. V tomto kroku musíte určit čas testování pochopením časové osy vlastní implementace. V rámci této plánovací fáze musíte vytvořit podrobný seznam požadavků a klasifikovat je jako povinné (MUSÍ mít) nebo dobré mít.

3. **Design**. V tomto kroku musíte vyvinout testovací případy, rozhodnout o počtu testovacích interakcí a nástrojích, které budete pro testování používat. ![](resources/images/implementation-guide-image28.png){ .center width=80% }

   - **Příklad testovacích nástrojů - Jira** ![](resources/images/implementation-guide-image2.png)
   - **Příklad testovacího nástroje - Excel** ![](resources/images/implementation-guide-image17.png)

   - Každý testovací případ by měl obsahovat následující části. Úroveň podrobností a obsah testu, který má být proveden, bude záviset na úrovni profilu zkušeností uživatele.
     - Identifikace: Číslo cyklu / ID, ID testu, verze, shrnutí testu.
     - Popis: podrobnosti, kroky k zopakování
     - Zpráva o stavu: Datum provedení, provedeno, očekávaný vs. skutečný výsledek, ID zprávy o stavu provedení.

4. **Provádění**. Během provádění testování mějte na paměti dva důležité problémy:
   - Konfigurace metadat: Ověřte nastavení programu na webu a v dokumentaci zjistěte chování funkcí v aplikaci. To pomůže identifikovat skutečné chyby versus problémy odvozené z konfigurace nebo nepodporovaných funkcí.
   - Matice dokončení: Zkontrolujte svůj pokrok podle termínů, které jste navrhli ve fázi plánování. Také se ujistěte, že jsou důsledně pořizovány poznámky, aby bylo možné nahlásit chybu.
5. **Zpráva**. Vaše zpráva musí mít tři důležité vlastnosti
   - Hlášená chyba musí být reprodukovatelná
   - Informace musí být konkrétní a informativní
   - Zpráva musí oddělit fakta od spekulací ![](resources/images/implementation-guide-image1.png) { .center width=80% }
   - Níže uvedená tabulka shrnuje dobré Hlášení chyb s několika příklady: ![](resources/images/implementation-guide-image34.png) { .center width=80% }

## Interní testování a testování UAT { #implementation_guide_testing_internal }

**Co testujete**

Testujete konfiguraci serveru DHIS 2 a samotnou aplikaci pro Android.

![](resources/images/implementation-guide-image12.png){ .center width=40% }

**Co hledáte?**

Pravidla programu, formuláře, vizuální uživatelské rozhraní, indikátory ... Chyby, vylepšení, nové požadavky atd.

**Jak?**

Metody a období pro testování se liší od skupiny ke skupině, ale musí to být iterativní, flexibilní a musí to být provedeno v raných fázích procesu nasazení. Musíte věnovat čas rozhodování o tom, kdo se testu zúčastní, vypracovat plán testu a mít strategii pro získání zpětné vazby. K hlášení a sledování chyb a problémů jsou k dispozici různé nástroje. V závislosti na složitosti vašeho testu můžete použít [trello](https://trello.com/), [JIRA](https://www.atlassian.com/software/jira) atd.

Nastavení správného základu pro vaše interní testování zvýší kvalitu a efektivitu testovacích relací. Tato doporučení platí pro jakýkoli z různých testů, které budete muset provést.

### Testování UAT { #implementation_guide_testing_uat }

**Co testujete**
Testujete konfiguraci systému (vstup), své vizuální uživatelské rozhraní a ikony, použitelnost a vaše výstupy. V této fázi můžete také otestovat uživatelskou zkušenost s různými zařízeními (smartphone, tablet, externí klávesnice, chromebook).

![](resources/images/implementation-guide-image6.png){ .center width=40% }

**Co hledáte?**

Úpravy v předchozích položkách a problémy s hardwarem. Je vhodný čas začít identifikovat šampiony, kteří pomohou v budoucích fázích. Hlavním účelem UAT je přimět lidi z různých prostředí ve shodě s konfigurací k provedení testování v terénu. Úspěch této fáze určí přesun do další fáze, testování v terénu

**Jak?**

Používejte řízené prostředí. Najděte uživatele s malou zkušeností této technologie, kteří nemusí být nutně integrováni do pracovních postupů. Vaši uživatelé by mohli být: 1) Expert v oblasti zdraví, 2) Úředník v terénu, 3) Uživatel v terénu.

Velikost skupiny se bude lišit v závislosti na typu projektu, pro který aplikaci implementujete. Průměrná velikost testovací skupiny UAT by měla být mezi 5 a 10 lidmi.

Při rozhodování o tom, kdo se vašeho testu zúčastní, zvažte všechny různé typy uživatelů a jejich role. S ohledem na to vyberte své testery. Svým testerům byste měli poskytnout správné pokyny a návody. Musí být dobře informováni o metodách, které budete používat pro testování, o očekáváních a celkových cílech a cílech testování. Doporučuje se, je-li to možné, uspořádat testovací schůzky s jedním nebo dvěma vedoucími, kde si testeři mohou navzájem pomáhat a mají možnost klást otázky a získat pomoc přímo na místě od vedoucích. Dalším důležitým aspektem, který je třeba vzít v úvahu, jsou testovací data. Na svém testovacím serveru musíte mít dostatek dat, abyste mohli testovat různé testovací případy.

## Testování v terénu / Pilot { #implementation_guide_testing_field }

**Co testujete**

- Testujete své SoP a pracovní postupy.
- Testujete svoji infrastrukturu / architekturu.
- Testujete různá zařízení.
- Testujete své tréninkové postupy a materiály.

![](resources/images/implementation-guide-image25.png){ .center width=40% }

**Co hledáte?**

- Úpravy v předchozích položkách.
- Vhodnost vybraných zařízení pro pracovní prostor a prostředí.
- Vyhodnoťte své řešení
- Určete šampiony.

**Jak?**

20-30 uživatelů. Doporučeno 2 měsíce (plánujte dopředu!). Rozhodněte o distribuci (umístění). Nevybírejte nejjednodušší nebo nejsložitější. Snažte se o to, aby vaše řešení bylo jednoduché.

**Úvahy o hodnocení vašeho pilota**

Měli byste definovat své indikátory pro hodnocení vašich výsledků a rozhodnout se pro strategii pilotování vašeho systému. Současný systém a nový systém můžete používat paralelně po dobu několika měsíců nebo jej jednoduše vyměnit. Obě strategie mají výhody i nevýhody a před pilotováním byste je měli pečlivě analyzovat se svým týmem.

Některé výhody paralelního současného a nového systému jsou:

- Můžete mít důkazy o tom, jak se nový systém vylepšuje ve srovnání se starým z hlediska včasnosti nebo například kvality dat, tyto parametry závisí na účelu vašeho konkrétního projektu.
- Pokud něco funguje podle očekávání, máte svůj předchozí systém jako záložní mechanismus
- Buduje důvěru uživatelů, když porovnávají oba výsledky.

Některé nevýhody jsou:

- Nastavujete mechanismus dvojitého hlášení, duplikuje čas a úroveň úsilí vašich uživatelů. IT je důležité to řešit citlivě a v případě potřeby připravit potenciální podporu lidských zdrojů.
- Možnost uživatelů porovnávat oba systémy paralelně by mohla být dvojsečným mečem, protože uživatelé mají tendenci odolávat změnám.

# Rozšiřování škálováním { #implementation_guide_scale_up }

## Akvizice { #implementation_guide_scale_up_acquisitions }

Nyní, když jste provedli veškeré své testování a svůj pilotní projekt, jste připraveni rozšířit své nasazení, pro které budete muset provést pořízení hardwaru a nezbytných služeb. Budete se muset rozhodnout ohledně:

- Nákup zařízení vs BYOD (přineste si vlastní zařízení)
- Distribuce aplikace (nyní a později)
- Telekomunikační smlouvy

**Nákup zařízení vs. BYOD (přineste si vlastní zařízení)**

Zpočátku byste si měli koupit různá zařízení, abyste uživatelům umožnili je vyhodnotit a poskytnout vám zpětnou vazbu. Jakmile je rozhodnuto o zařízení, které budete používat, měli byste si koupit pouze 10 nebo méně jednotek, nebo cokoli, co je potřeba pro testování a pilotní fázi. Teprve když se pilot blíží ke konci, měli byste si koupit vybavení pro zavádění dalších 6 měsíců. U některých velmi velkých projektů bude národní zavedení trvat roky a váš plán získávání hardwaru by se měl v průběhu let rozšiřovat. Doporučení týkající se technických specifikací zařízení jsou v kapitole [Specifikace mobilních zařízení](#mobile_specs).

Měli byste zvážit proveditelnost použití zásady BYOD - tento formát umožňuje uživatelům přinést si svá vlastní zařízení, pokud splňují minimální technickou normu, kterou pro svůj projekt definujete. Obvykle nabídnete nějaký druh pobídky, pravděpodobně ve formě eCash nebo telefonního kreditu. Výhody tohoto přístupu jsou zřejmé: vyhýbá se velkým počátečním nákladům na pořízení a snižuje náklady na správu a logistiku. Na druhou stranu vás čeká výzva velmi heterogenního hardwarového prostředí, což znamená různá zařízení a verze OS Android. To ovlivní hlavně proces ladění.

**Distribuce aplikace** (nyní a později)

Aplikace DHIS 2 pro Android má nové vydání každých pár týdnů. Každá nová verze obsahuje opravy chyb a může obsahovat nové funkce. Mohlo by to také obsahovat nové chyby. Nové verze jsou publikovány v GitHubu i v obchodu Google Play. Github je pouze úložiště: stáhnete si konkrétní soubor APK a nainstalujete ho do svého zařízení. K instalaci souboru APK budete muset povolit použití oprávnění třetích stran. Jakmile se APK stáhne z GitHubu nebo jiným způsobem, nainstalovaná verze se nikdy automaticky neaktualizuje. Na druhou stranu, pokud instalujete z Google Play, obvykle se automaticky aktualizuje na nejnovější verzi. V případě potřeby je možné deaktivovat automatickou aktualizaci v gPlay.

Jakmile dokončíte své testovací a školicí materiály a spustíte zavádění, nechcete, aby se verze aplikace u žádného z uživatelů změnila, pokud novou verzi znovu neotestujete. Změny verze mohou zahrnovat upravené uživatelské rozhraní, chybné chování nebo nekompatibilitu s verzí serveru DHIS 2. Chcete nové verze důkladně otestovat, než je pošlete svým uživatelům, abyste se ujistili, že nová verze nezpůsobí vaší konfiguraci žádné problémy, vyžaduje přeškolení, vyžaduje změny vaší konfigurace.

Stručně řečeno, u jakékoli instalace, která zahrnuje značný počet zařízení, byste se měli vyhnout používání Google Play a místo toho použít řešení pro správu mobilních zařízení (MDM), o kterém pojednáváme v [této kapitole](#scale_up_mdmt). Pokud nemáte přístup k této možnosti, můžete zvážit použití Google Play, ale měli byste deaktivovat automatickou aktualizaci pro aplikaci DHIS 2 pro Android. Postup, jak to provést, se mění podle verze systému Android - google „jak zakázat automatickou aktualizaci systému Android pomocí aplikace v Andrid X.X“.

**Telekomunikační smlouvy**

Pokud vaše instalace plánuje zahrnout použití SMS pro přenos vybraných záznamů prostřednictvím SMS, když mobilní data nejsou k dispozici, budete muset uzavřít smlouvu s místním agregátorem, který vám může poskytnout příchozí číslo pro příjem SMS. Měli byste nakonfigurovat svůj server tak, aby přijímal a odesílal SMS - viz připojení [dokumentace DHIS 2](https://docs.dhis2.org/master/en/user/html/mobile_sms_service.html#) o připojeních SMS. Abyste mohli předpovědět měsíční náklady, budete muset odhadnout počet zpráv za měsíc.

Proces výběru a podpisu smlouvy s poskytovatelem SMS se v jednotlivých zemích liší a závisí na postupech nákupu vaší organizace.

### Plánování velkých akvizic { #implementation_guide_scale_up_planning }

Každý projekt bude vyžadovat kombinaci typů zařízení: telefony, tablety a Chromebooky. Většina mobilních zařízení bude pravděpodobně přidělena vyhrazenému uživateli. Je třeba vzít v úvahu povahu práce. Například komunitní pracovníci budou používat chytré telefony nebo tablety. Zdravotničtí pracovníci, kteří pracují v zařízení, však mohou upřednostňovat tablet s externí klávesnicí nebo Chromebook.

Skutečné získávání ve velkém by mělo být co nejvíce odloženo. Zpočátku je doporučeno zakoupit co nejméně zařízení pro testování konfigurace a poskytnout určitou úroveň výběru budoucím uživatelům. Jakmile je dohodnuto rozhodnutí přejít na pilotní projekt, měl by být druhý nákup v ideálním případě omezen na zařízení potřebná pro pilota. Pokud plán zavádění trvá déle než rok, měla by být akvizice zařízení také rozdělena do několika období: výrobci neustále nabízejí lepší zařízení za stejnou cenu v cyklech, které se pohybují mezi 12-18 měsíci.

Příklad celkového pořízení 100 až 1000 zařízení.

| Měsíc projektu | Fáze | Získávání | # zařízení |
| --- | --- | --- | --- |
| 2. měsíc | Návrh a počáteční konfigurace | Vyberte 3 nebo 4 možné tvarové faktory. Nakupujte od jednoho nebo dvou výrobců | 2-8 |
| 4-6 měsíců | Pilot | Kupte pouze zařízení potřebná k dokončení pilotního projektu | 10-30 |
| 6-12. měsíc | Zavádění - fáze 1 | První hromadné získávání | 50-500 |
| Měsíc X | Zavádění fáze X | --> | 50-500 |
| 36-48 měsíc | Výměna upgradu | Vyměňte zařízení | X |

## Správa mobilních zařízení { #implementation_guide_scale_up_mdm }

Správa mobilních zařízení označuje software používaný ke správě mobilních zařízení. Software MDM budete potřebovat, když budete muset podporovat stovky zařízení a bude nutné řídit distribuci souborů apk mezi zařízeními, poskytovat technickou podporu a prosazovat institucionální zásady. Většina možností je nabízena jako služby s měsíčním poplatkem. Některé bezplatné aplikace nabízejí režim veřejného terminálu, ale za základní vzdálenou správu si účtují měsíční poplatek.

Požadované funkce softwaru MDM lze klasifikovat jako základní a pokročilé. Zde je seznam požadovaných funkcí:

- Základní vlastnosti:
  - Vyžaduje heslo pro zámek obrazovky
  - Poskytování autorizovaných aplikací
  - Zamkněte zařízení a vymažte informace, pokud dojde ke ztrátě nebo odcizení
  - Ovládejte aktualizaci aplikace pro Android
  - Vynutit zásady zálohování
- Pokročilé funkce:
  - Vynutit zásady síly hesla
  - Prosazovat zásady používání sítě
  - Sledovat polohu zařízení
  - Omezený přístup k nastavením a funkcím (příklad - wifi / síť, snímání obrazovky)

Při rozhodování, který je nejlepší software MDM pro vaše potřeby, byste se měli pokusit odpovědět na následující otázky:

- Kolik zařízení musím spravovat?
- Jak často mám fyzický přístup k zařízení?
- Které funkce opravdu potřebuji?
- Které zásady musím implementovat
- Jak těžké bude instalace a údržba
- Jak to ovlivní uživatelskou zkušenost?
- Musíme povolit BYO? (BYO: Přineste si vlastní zařízení).
- Jak to ovlivní zařízení?

Na další stránce najdete seznam dostupného softwaru MDM (mějte prosím na paměti, že ceny a podmínky se budou časem měnit).

- Mobilock Free (nelze aktualizovat software)
- SOTI (MobiControl) (může být drahý - 2,20 $ / zařízení / měsíc)
- Miradore (bez vzdálené podpory)
- Applock (nelze ovládat aktualizaci softwaru)
- AcDisplay (nelze ovládat aktualizaci softwaru)
- F-Droid (nelze omezit spotřebu dat)
- APPDroid (nelze omezit spotřebu dat)
- Master List (nelze ovládat aktualizaci softwaru)
- Firebase (nelze omezit spotřebu dat)
- Intunes (uživatelé musí být součástí nasazení MS Office 365)
- MobileIron (může být drahý - 3,15 USD / zařízení / měsíc \+ 2,368 USD za nasazení)
- IBM Maas360 (příliš drahé - 1,60 USD / zařízení / měsíc \+ 0,50 USD / zařízení / měsíc pro vzdálenou podporu, pro 3.000 zařízení)
- AirWatch (nereaguje a může být drahý - 3,80 USD / zařízení / měsíc pro 3000 zařízení po dobu 3 let)
- XenMobile (Citrix) (může být drahý - 2,03 USD / zařízení / měsíc pro 3000 zařízení)
- Good for Enterprise (Blackberry) (může být drahé - 2 USD / zařízení / měsíc \+ 2,5K USD za nasazení)

> **Poznámka**
>
> Další informace o tomto tématu naleznete v [Pokynech pro správu mobilních zařízení](https://docs.dhis2.org/en/implement/managing-mobile-devices/considerations.html).

## Výcvik { #implementation_guide_scale_up_training }

Důležitým krokem před zahájením, je školení uživatelů a v případě potřeby školení týmů poskytujících podporu uživatelům. Existuje mnoho tréninkových strategií, kterými se můžete řídit, a bude to záviset na velikosti skupiny, kterou je třeba trénovat, na jejich úrovni dovedností, dostupném časovém rámci, rozpočtu atd. Je důležité, abyste při navrhování věnovali čas a energii svou tréninkovou strategii a věnujte dostatek času splnění vašich tréninkových cílů. Dobře vyškolení a informovaní uživatelé sníží úzkost uživatelů a problémy s adaptací a také zvýší kvalitu shromážděných dat.

### Technické přípravy na školení { #implementation_guide_scale_up_techinical_prep }

Při přípravě na školení se ujistěte, že byly splněny všechny praktické technické požadavky. To zahrnuje připravenost tabletů / mobilních zařízení s nainstalovanou novou aplikací pro Android DHIS 2 Capture. V závislosti na dostupnosti připojení k internetu v oblasti, kde trénink provádíte, můžete mít všechny tablety předem synchronizované se serverem, abyste měli dostatek dat a správnou konfiguraci pro školení. Před provedením školení, by měla být cvičení testována, aby bylo zajištěno, že vše funguje. Odstraňte problémy zjištěné během testování, aby se neobjevily během tréninku. Možná budete chtít provést druhé kolo testu, abyste zjistili případné problémy které jste nezachytili v prvním kole.

Pokud se školení provádí s předem synchronizovanými daty a konfigurací, na konci školení nezapomeňte umožnit účastníkům vyzkoušet aplikaci, která přistupuje ke vzdálenému serveru DHIS 2. To poskytne účastníkům možnost vyzkoušet si synchronizaci v reálném životě, která může zahrnovat zpoždění v síti. Bez zpoždění mohou později interpretovat zpoždění sítě jako poruchy svého zařízení.

### Rozpočet na školení { #implementation_guide_scale_up_budget }

Následuje několik pokynů k přípravě rozpočtu, které jsou převzaty z [pokynů DHIS 2 Community Health Information System Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/CHIS+Guidelines+En.pdf) vydané Univerzitou v Oslu:

- Dodržujte zásady organizace při používání schválených rozpočtových šablon a sazeb (nepřímé, DSA atd.) Pro všechny výdaje, včetně:
  - Cestovní náklady (např. palivo, pronájem auta, ubytování)
  - Osobní náklady (např. diety, náklady na jídlo)
  - Místo konání (např. konferenční prostor, čajové přestávky)
  - Materiály (např. tisk, hardware, projektory)
  - Různé předměty
- Sestavte rozpočet na základě výpočtů potřebných materiálů v listu, jednotkových nákladů na tento materiál a počtu potřebných jednotek. Můžete také zabudovat další multiplikátory pro ilustraci počtu jednotek na účastníka. To umožňuje flexibilitu při aktualizaci rozpočtu, pokud se změní jednotkové náklady nebo se zvýší nebo sníží počet účastníků.
- Předpokládané výdaje rozpočtu v místní měně s integrovaným konverzním kurzem (který lze podle potřeby aktualizovat) pro převod na požadovanou měnu vaší organizace nebo financujícího subjektu. (2).

### Školicí program { #implementation_guide_scale_up_agenda }

Dokumenty [DHIS 2 Community Health Information System Guidelines](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/CHIS+Guidelines+En.pdf), dokument napsaný od University of Oslo doporučuje zvážit:

1. Požadovaný typ sezení (kulatý stůl, jednotlivé stoly atd.).
2. Technologické požadavky (všechny počítače, šířka pásma Wi-Fi atd.),
3. Financování příspěvků na konferenční centrum, jídlo a nápoje účastníků
4. Trenéři potřebují prostor, aby mohli chodit, aby mohli každého účastníka pozorovat a pomáhat mu.

Uvědomte si počet účastníků, které na každém školení očekáváte, protože bude nutné poskytnout dostatečné materiály a prostor. Prostor pro akce by měl být dostatečně velký pro skupinu a také vhodný pro plánované aktivity.

### Školicí materiály { #implementation_guide_scale_up_materials }

Ve stejném dokumentu najdeme také doporučení pro školicí materiály, které zde uvádíme. Materiály, které budete potřebovat pro vaše školení, budou záviset na vašich aktivitách. Abyste se ujistili, že plánujete všechno, projděte si s partnerem svou tréninkovou agendu a prodiskutujte, co se bude dělat pro každou část školení, a vezměte na vědomí potřebné materiály.

Program školení by měl být definován s dostatečným předstihem před zahájením školení a zahrnut do distribuovaných materiálů.

Uživatelská dokumentace by měla být přibalena v Minimálních příručkách. Tyto příručky vysvětlují konkrétní pracovní úkol (např. Zadávání měsíčních údajů z registru zdraví vesnic nebo porovnání zdraví ve vaší vesnici se sousedními vesnicemi). Po vysvětlení pracovního úkolu poskytuje Minimální Příručka číslované podrobné pokyny se snímky obrazovky, aby uživatelé rozpoznali, co mají dělat. Mějte na paměti, že Minimální příručky NEVYSVĚTLUJÍ funkčnost aplikace, jednu po druhém, jako typická uživatelská příručka dodavatele. Vzhledem k tomu, že uživatelé dávají přednost zkoušení a ne čtení, měly by být příručky co nejkratší a zároveň obsahovat všechny kroky.

# Zavádění { #implementation_guide_rollout }

V této fázi byste měli být připraveni zavést zařízení a aplikaci pro vaše koncové uživatele. V tomto kroku se budete muset připravit na přerušení a koordinovat uvedení do provozu, budete se muset rozhodnout, zda ponecháte paralelní systémy pro případ, že používáte jiné aplikace nebo provedete přímou náhradu. Pokud jde o papírové a manuální procesy, budete se také muset rozhodnout, zda je chcete eliminovat, replikovat nebo ponechat duplikát. Nezapomeňte si pečlivě vybrat čas, kdy chcete začít pracovat naostro. Vyberte si čas, kdy budou týmy k dispozici, abyste strávili čas navíc a úsilí přizpůsobením se používání nové aplikace, a také se ujistěte, že během počátečních fází bude k dispozici další podpora.

![](resources/images/implementation-guide-image27.png){ .center width=60% }

Dále uvádíme doporučení pro tuto fázi implementace z dokumentu DHIS 2 Community Health Information System Guidelines document vypracovaného od University of Oslo.

Koncoví uživatelé nově zavedené aplikace by měli mít jeden přístupový bod podpory. V ideálním případě může jejich nadřízený poskytnout tento jeden bod podpory. Vzhledem k tomu, že uživatelé znají svého nadřízeného a získávají podporu pro další problémy, mít nadřízené podporující aplikaci je výhodou.

Možná už máte zaveden víceúrovňový systém podpory pro webový DHIS 2 a možná jej můžete použít také k poskytnutí podpory s aplikací. Víceúrovňový znamená, že jednoduché problémy mohou řešit nadřízení supervizoři a složitější nebo složitější problémy se posouvají nahoru, dokud se nedostanou k někomu, kdo je schopen je řešit. Drtivá většina problémů vyžadujících podporu budou jednoduché problémy, které by měla být schopna řešit první úroveň podpory. Tato první vrstva je často přímým nadřízeným uživatele. Tato úroveň by měla být schopna řešit jednoduché problémy s hardwarem a softwarem. Pokud nadřízení nedokážou problém vyřešit, bude jej muset eskalovat na vyšší úroveň. Požadavky druhého stupně jsou často řešeny správci informačních systémů na okresní úrovni nebo na nižší než národní úrovni, kteří jsou vyškoleni v oblasti správy problémů s konfigurací systému a všech pokročilých problémů týkajících se uživatelského rozhraní, importu a exportu dat. Požadavky třetí úrovně jsou obvykle řešeny osobami podpory IT na centrální úrovni. Měli by být schopni reagovat na jakékoli požadavky na údržbu typu back-end.

Počet úrovní podpory se může lišit v závislosti na složitosti a velikosti vašeho projektu. Bez ohledu na počet úrovní je zásadní, aby žádosti o podporu mohl odesílat jakýkoli uživatel přímo prostřednictvím webu, telefonu nebo e-mailu. Jakmile bude technickému týmu zaslána žádost o podporu, měla by potvrdit přijetí žádosti v krátké době, například 12 hodin (2).

Nyní byste měli mít plán, jak budete trasovat zařízení, která rozdáváte svým týmům. Tady je několik doporučených postupů, které byste měli sledovat při trasování zařízení (2):

- Očíslujte každou schránku na telefon (tablet) a dvě kopie smlouvy o telefonu (tj. \#1 na krabici a na obou formulářích o dohodě) a předejte obě dohlížejícímu pracovníku komunitního zdravotnického personálu, aby vyplnil formuláře oproti podrobnostem daného telefonu.
- Zajistěte, aby se telefony a krabice nemísily.
- Posbírejte formuláře dohody a nechte si podepsat radu a obě kopie opatřit razítkem. Jedna kopie zůstane u okresu a druhá bude vrácena partnerovi a uchována v souboru okresní schránky v kanceláři.
- Pomocí generátoru QR kódu vygenerujte QR kód s informacemi o telefonu (číslo, CHW, číslo SIM, okres atd.). Tento QR kód pak můžete vytisknout na odolný štítek a nalepit jej na zadní stranu telefonu nebo uvnitř telefonu v přihrádce na baterie.
- Pokud poskytujete SIM karty s telefony, zdokumentujte přidruženou SIM kartu a telefon.
- Chcete-li zabránit neoprávněné manipulaci se SIM kartou dodávanou s telefonem, přilepte SIM kartu do telefonu tak, že vložíte SIM kartu do telefonu a nanesete lepidlo na zadní stranu.

Měli byste také uvažovat o vlastnictví a používání zařízení. V době předání zařízení (telefonů, tabletů atd.) Uživatelům je důležité objasnit „vlastnictví“ zařízení spolu s povinnostmi péče, údržby a ztráty. Často dochází k nejasnostem ohledně toho, zda zařízení vlastní instituce nebo jednotlivec, a jaké jsou příslušné odpovědnosti. Pokud se však od koncových uživatelů očekává, že budou používat osobní zařízení, je o to důležitější vyjasnit si otázky týkající se nákladů na čas běhu / data spolu s mechanismem náhrady (2).

# Kontrolní seznam mobilní implementace { #implementation_guide_checklist }

| Úkol | Dokončeno |
| --- | :-: |
| Analýza technologických požadavků na aplikace a servery pro Android | ☐ |
| Strategie pro zabezpečení dat a soukromí | ☐ |
| Nastavení a konfigurace serveru DHIS 2 | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;DHIS 2 instance serveru | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Datové prvky, sady možností, programy ... | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Visuální konfigurace | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Definování indikátorů a legend programu | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Nastavení pravidel programu | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Vytvoření uživatele systému Android | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Nastavení sdílení a bezpečnostní aspekty | ☐ |
| Instalace a nastavení aplikace | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Instalace aplikace | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Přihlášení do aplikace | ☐ |
| Testování | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Interní testování | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;testování UAT | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Testování v terénu / pilotní provoz | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Pilot | ☐ |
| Rozšiřování škálováním | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;akvizice hardwaru | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Strategie distribuce aplikací | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Strategie správy mobilních zařízení | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Telekomunikační smlouvy | ☐ |
| Výcvik | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Technické přípravy | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp; Rozpočet | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Agenda a Účastníci | ☐ |
| &nbsp;&nbsp;&nbsp;&nbsp;Materiály | ☐ |
| Představit plán | ☐ |
