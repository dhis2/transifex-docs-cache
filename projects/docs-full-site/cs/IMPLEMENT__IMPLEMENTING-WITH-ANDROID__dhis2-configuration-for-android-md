---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/dhis2-configuration-for-android.md"
revision_date: "2021-07-27"
---

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

Pokud pracujete s programy pro trasování a používáte automaticky generované jedinečné atributy trasované entity (viz [dokumentace DHIS 2](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#create_tracked_entity_attribute)) , je důležité pochopit, jak se aplikace zabývá generováním hodnot. Hodnoty se stahují předem ze serveru, takže jsou k dispozici, když aplikace pracuje offline. Tyto hodnoty jsou na straně serveru označeny jako rezervované.

Při první synchronizaci uživatele aplikace stáhne 100 hodnot, které budou na straně serveru označeny jako rezervované. Od tohoto bodu začne uživatel používat hodnoty, když se vytvářejí nové trasované instance entit.

Pokaždé, když uživatel použije hodnotu (zaregistruje instanci trasované entity), aplikace:

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
