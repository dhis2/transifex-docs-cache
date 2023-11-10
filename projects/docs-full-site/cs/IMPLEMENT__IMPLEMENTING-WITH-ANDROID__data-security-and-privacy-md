---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/data-security-and-privacy.md"
revision_date: "2021-03-29"
---

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
