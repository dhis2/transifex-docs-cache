---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/control-data-quality.md"
revision_date: "2021-06-14"
---

# Kontrola kvality dat { #control_data_quality }

## O kontrolách kvality dat { #about_data_quality }

Aplikace **Data Quality** obsahuje nástroje k ověření přesnosti a spolehlivosti dat v systému. Můžete posoudit různé dimenze kvality dat, jak je uvedeno v následující tabulce:

 <table>
 <colgroup>
 <col style="width: 50%" />
 <col style="width: 50%" />
 </colgroup>
 <thead>
 <tr class="header">
 <th> <p> Dimenze </p> </th>
 <th> <p> Popis </p> </th>
 </tr>
 </thead>
 <tbody>
 <tr class="odd">
 <td> <p> Správnost </p> </td>
 <td> <p> Data by měla být v normálním rozsahu pro data shromážděná v tomto zařízení. Ve srovnání s údaji ze souvisejících datových prvků by neměly existovat žádné hrubé nesrovnalosti. </p> </td>
 </tr>
 <tr class="even">
 <td> <p> Úplnost </p> </td>
 <td> <p> Měly být předloženy údaje pro všechny datové prvky pro všechny jednotky vykazující organizace. </p> </td>
 </tr>
 <tr class="odd">
 <td> <p> Konzistence </p> </td>
 <td> <p> Data by měla být v souladu s údaji zadanými během dřívějších měsíců a let, přičemž by měla umožňovat změny s reorganizací, zvýšenou pracovní zátěží atd. a v souladu s dalšími podobnými zařízeními. </p> </td>
 </tr>
 <tr class="even">
 <td> <p> Včasnost </p> </td>
 <td> <p> Všechna data ze všech jednotek zpravodajské organizace by měla být předložena v určený čas. </p> </td>
 </tr>
 </tbody>
 </table>

Kvalitu dat můžete ověřit různými způsoby, například:

-   V bodě zadávání dat může DHIS 2 zkontrolovat zadaná data a zjistit, zda spadají do rozsahu minimálních maximálních hodnot daného datového prvku (na základě všech předchozích registrovaných dat).

-   Definováním ověřovacích pravidel, která lze spustit, jakmile uživatel dokončí zadávání dat. Uživatel může také zkontrolovat zadaná data pro konkrétní období a organizační jednotku(y) podle ověřovacích pravidel a zobrazit porušení těchto ověřovacích pravidel.

-   Analýzou datových sad, tedy zkoumáním mezer v datech.

-   Pomocí datové triangulace, tj. Porovnáním stejných údajů nebo indikátoru z různých zdrojů.

## Analýza ověřovacích pravidel { #validation_rule_analysis }

### O analýze ověřovacích pravidel { #about-validation-rule-analysis }

Ověřovací pravidlo je založeno na výrazu, který definuje vztah mezi hodnotami datových prvků. Výraz tvoří podmínku, která by měla potvrdit, že jsou splněna určitá logická kritéria.

Výraz se skládá z:

-   levá strana

-   pravá strana

-   operátor

Pravidlo ověřování by mohlo tvrdit, že „Podezřelé případy malárie testovány“ \> = „Potvrzené případy malárie“.

Analýza ověřovacích pravidel testuje ověřovací pravidla na základě údajů registrovaných v systému. Porušení ověření se hlásí, když není splněna podmínka definovaná ve výrazu pravidla ověření, což znamená, že je podmínka nepravdivá.

Můžete nakonfigurovat analýzu ověřovacích pravidel tak, aby automaticky odesílala informace o porušeních ověření vybraným skupinám uživatelů. Tyto zprávy se nazývají _validační oznámení_ a vytváříte je v aplikaci **Údržba**. Oznámení o ověření se odesílají prostřednictvím interního systému zpráv DHIS 2.

### Pracovní postup { #workflow }

1.  V aplikaci **Údržba** vytvořte ověřovací pravidla a skupiny ověřovacích pravidel.

2.  (Volitelné) V aplikaci **Údržba** vytvořte ověřovací oznámení.

3.  Spusťte analýzu ověřovacích pravidel, buď automaticky, nebo ručně.

    -   V aplikaci **Plánovač** naplánujete automatické spuštění analýzy ověřovacích pravidel pro všechna ověřovací pravidla obsažená v jedné nebo několika skupinách ověřovacích pravidel. Poté, co systém provede analýzu, uvidíte v ověřovacích oznámeních zaslaných prostřednictvím interního systému zasílání zpráv DHIS 2 porušení ověření (pokud existují).

    -   V aplikaci **Kvalita dat** spustíte analýzu ověřovacích pravidel ručně pro vybraná ověřovací pravidla. Po dokončení procesu analýzy se zobrazí seznam porušení ověření (pokud existuje).

### Naplánujte automatické spuštění analýzy ověřovacích pravidel { #schedule-a-validation-rule-analysis-to-run-automatically }

> **Poznámka**
>
> Součástí analýzy ověřovacích pravidel budou pouze ověřovací pravidla, která jsou zahrnuta v jednom nebo několika ověřovacích oznámeních. Pokud pro ověřovací pravidlo neexistuje odpovídající oznámení o ověření, žádné oznámení nebude odesláno.

> **Poznámka**
>
> Při automatickém spouštění analýzy ověřovacích pravidel budou během tohoto běhu přetrvávat všechny výsledky, které ještě nejsou trvalé. Trvalé výsledky lze aktuálně získat pouze prostřednictvím rozhraní API. Další informace o tom, jak lze přistupovat k trvalému porušení pravidel ověření, najdete v příručce pro vývojáře.

1.  Ověřte, že jste vytvořili všechna pravidla ověření, skupiny pravidel ověření a oznámení o ověření, která potřebujete.

2.  Otevřete aplikaci **Plánovač** a klikněte na tlačítko Přidat v pravém dolním rohu.

3.  Vyberte vhodný Název pro novou úlohu.

4.  V rozevírací nabídce vyberte **Monitorování** Typu úlohy.

5.  Vyberte frekvenci běhu úlohy, tj. Kdy a jak často by úloha měla běžet.

6.  Vyplňte část **Parametry**, včetně skupin pravidel ověření.

7.  Stisknutím tlačítka **Přidat úlohu** potvrďte vytvoření úlohy. Další informace o přidávání úloh najdete v části [Plánování](data-administration.html#scheduling).

### Spusťte analýzu ověřovacích pravidel ručně { #run-a-validation-rule-analysis-manually }

![](resources/images/data_quality/validation_rule_analysis.png)

1.  Ověřte, že jste vytvořili všechna pravidla ověření, skupiny pravidel ověření a oznámení o ověření, která potřebujete.

2.  Otevřete aplikaci **Kvalita dat** a klikněte na **Analýza ověřovacích pravidel**.

3.  Vyberte **Datum zahájení** a **Datum ukončení**.

4.  Vyberte, kterou **skupinu ověřovacích pravidel** chcete do analýzy zahrnout.

    Můžete vybrat všechna ověřovací pravidla nebo všechna ověřovací pravidla z jedné skupiny ověřovacích pravidel.

5.  (Volitelné) Výběrem možnosti **Odeslat oznámení** spustíte oznámení o ověření.

    > **Note**
    >
    > If you want to send out validation notifications, you must first create them in the **Maintenance** app.

6.  (Volitelné) Vyberte _Přetrvávat nové výsledky_ k přetrvávání všech netrvalých výsledků nalezených během analýzy

7.  Vyberte **nadřazenou organizační jednotku**.

8.  Klikněte na **Ověřit**.

    Trvání procesu analýzy závisí na množství dat, která se analyzují. Pokud nedojde k žádnému porušení pravidel ověřování, zobrazí se zpráva s názvem _Ověření proběhlo úspěšně_. Pokud dojde k porušení ověřování, budou uvedena v seznamu.

    ![](resources/images/data_quality/validation_rule_analysis_result.png)

9.  (Volitelné) Kliknutím na ikonu Zobrazit podrobnosti zobrazíte další informace o porušení ověření. V rozbalovacím okně najdete informace o datových prvcích obsažených v pravidlech ověřování a jejich odpovídajících hodnotách dat. Tyto informace můžete použít k identifikaci zdroje porušení pravidla ověření.

10. (Volitelné) Kliknutím na **Stáhnout jako PDF**, **Stáhnout jako Excel** nebo **Stáhnout jako CSV** stáhnete seznam porušení ověření ve formátech PDF, Excel nebo CSV.

### Viz také { #see-also }

-   [Spravovat pravidla ověřování](https://docs.dhis2.org/master/en/user/html/manage_validation_rule.html)

-   [Aplikace pro správu dat](https://docs.dhis2.org/master/en/user/html/data_admin.html)

## Analýza odlehlé hodnoty směrodatné odchylky { #standard_deviation_analysis }

### O analýze odlehlých hodnot standardní odchylky { #about-standard-deviation-outlier-analysis }

Analýza odlehlé hodnoty směrodatné odchylky identifikuje hodnoty, které jsou číselně vzdálené od zbytku dat, což potenciálně naznačuje, že se jedná o odlehlé hodnoty. Analýza je založena na standardním normálním rozdělení. DHIS 2 vypočítá průměr všech hodnot pro organizační jednotku, datový prvek, kombinaci možností kategorie a kombinaci možností atributů. Odlehlé hodnoty se samozřejmě mohou vyskytnout náhodou, ale mohou potenciálně znamenat chybu měření nebo zadání dat.

> **Poznámka**
>
> Jak je uvedeno výše, tato analýza kvality dat je vhodná pouze pro data, která jsou skutečně normálně distribuována. Data, která mají velké sezónní výkyvy nebo která mohou být distribuována podle jiných statistických modelů (např. Logistických), mohou vést k označení hodnot, které by ve skutečnosti měly být považovány za platné. Doporučuje se proto nejprve ověřit, zda jsou data ve skutečnosti normálně distribuována, před provedením analýzy odchylek od standardní odchylky.

### Spusťte analýzu odlehlé hodnoty standardní odchylky { #run-a-standard-deviation-outlier-analysis }

![](resources/images/data_quality/std_dev_analysis.png)

1.  Otevřete aplikaci **Data Quality** a klikněte na **Std dev outlier analysis**.

2.  Vyberte **Od data** a **Do dne**.

3.  Vyberte datovou sadu(y).

4.  Vyberte **Nadřazená organizační jednotka**.

    Budou zahrnuty všechny podřazené organizační jednotky. Analýza se provádí na nezpracovaných datech „pod“ nadřazenou organizační jednotkou, nikoli na agregovaných datech.

5.  Vyberte počet směrodatných odchylek.

    To se týká počtu směrodatných odchylek, u nichž se údaje mohou odchýlit od průměru, než budou klasifikovány jako odlehlé hodnoty.

6.  Klikněte na **Start**.

    Trvání procesu analýzy závisí na množství dat, která se analyzují. Pokud existují odlehlé hodnoty standardních odchylek, zobrazí se v seznamu.

    ![](resources/images/data_quality/std_dev_analysis_outlier_result.png)

    U každé odlehlé hodnoty uvidíte datový prvek, organizační jednotku, období, minimální hodnotu, skutečnou hodnotu a maximální hodnotu. Minimální a maximální hodnoty se vztahují k hraničním hodnotám odvozeným od počtu standardních odchylek vybraných pro analýzu.

> **Tip**
>
> Kliknutím na ikonu hvězdičky označíte odlehlou hodnotu pro další sledování.

## Analýza odlehlých hodnot Minimum maximum { #min_max_analysis }

### O analýze odlehlých hodnot založených na minimální maximální hodnotě { #about-minimum-maximum-value-based-outlier-analysis }

Kvalitu dat můžete ověřit v okamžiku zadávání dat nastavením rozsahu minimální / maximální hodnoty pro každou hodnotu dat. Rozsahy hodnot můžete definovat ručně nebo je generovat automaticky.

Automaticky generovaný rozsah minimální maximální hodnoty je vhodný pouze pro normálně distribuovaná data. DHIS2 určí aritmetický průměr a standardní odchylku všech hodnot pro daný datový prvek, volbu kategorie, organizační jednotku a kombinaci atributů. Poté systém vypočítá rozsah minimálních maximálních hodnot na základě **Standardního faktoru analýzy dat** uvedeného v aplikaci **Nastavení systému**.

U dat, která jsou velmi zkreslená nebo nafouknutá nulovými daty (jak je tomu často u agregovaných dat), nemusí hodnoty, které automaticky generuje DHIS2, poskytovat přesný rozsah minimálních a maximálních hodnot. To může vést k nadměrně falešné výstraze, například pokud analyzujete hodnoty související se sezónními chorobami.

> **Poznámka**
>
> Rozsahy minimálních maximálních hodnot se počítají napříč všemi možnostmi kombinace atributů pro danou kombinaci datového prvku, možnosti kategorie a organizační jednotky.

### Pracovní postup { #workflow }

1.  Vytvořte rozsah minimální maximální hodnoty, buď automaticky, nebo ručně.

    -   V aplikaci **Administrace Dat** generujete rozsahy hodnot automaticky.

    -   V aplikaci **Zadávání dat** můžete rozsahy hodnot nastavit ručně.

2.  V aplikaci **Kvalita dat** spusťte **Min.-max. Analýza odlehlých hodnot**.

### Nakonfigurujte minimální maximální rámce analýzy { #configure-a-minimum-maximum-outlier-analysis }

#### Automaticky vytvořte rozsah minimální maximální hodnoty { #create-minimum-maximum-value-range-automatically }

![](resources/images/data_quality/generate_min_max.png)

> **Poznámka**
>
> Automaticky generované rozsahy minimálních a maximálních hodnot mohou být užitečné v mnoha situacích, ale před použitím této funkce se doporučuje ověřit, zda jsou data skutečně normálně distribuována.

Vygenerujete rozsahy minimálních maximálních hodnot vypočítané podle sady dat v aplikaci **Data Administration**. Nové rozsahy hodnot přepíší všechny rozsahy hodnot, které systém dříve vypočítal.

1.  Nastavte **směrodatnou odchylku (standardní odchylku) analýzy dat**:

    1.  Otevřete aplikaci **Nastavení systému** a klikněte na **Obecné**.

    2.  Do pole **Analýza dat std dev faktor** zadejte hodnotu.

        Tím se nastaví počet směrodatných odchylek, které se mají použít při analýze odlehlých hodnot. Výchozí hodnota je 2. Vyšší hodnoty označují širší distribuci, což může vést k tomu, že odlehlé hodnoty nebudou analýzou správně označeny.

2.  Otevřete aplikaci **Správa dat** a klikněte na **Generování minimální a maximální hodnoty**.

3.  Vyberte datovou sadu(y).

4.  Vyberte **Organizační jednotku**.

5.  Klikněte na **Generovat**.

    Jsou generovány nové rozsahy minimální maximální hodnoty pro všechny datové prvky ve vybraných souborech dat pro všechny organizační jednotky (včetně podřazených) vybraných organizačních jednotek.

#### Vytvořte rozsah minimální / maximální hodnoty ručně { #create-minimummaximum-value-range-manually }

![](resources/images/data_quality/set_min_max_manually.png)

1.  V aplikaci **Zadávání dat** otevřete formulář pro zadávání údajů.

2.  Poklepejte na pole, pro které chcete nastavit rozsah minimální / maximální hodnoty.

3.  V zobrazeném dialogovém okně zadejte **Minimální limit** a **Maximální limit**.

4.  Klikněte **Uložit**.

    Pokud hodnoty nespadají do nového rozsahu hodnot při příštím zadávání dat, zobrazí se buňka pro zadávání dat s oranžovým pozadím.

5.  (Volitelné) Napište komentář, který vysvětlí příčinu nesrovnalosti, například událost v zařízení, která mohla vygenerovat velký počet klientů.

6.  (Volitelné) Klikněte na **Uložit komentář**.

> **Tip**
>
> Kliknutím na ikonu hvězdičky označte hodnotu pro další sledování.

#### Odstraňte rozsah minimální maximální hodnoty { #delete-minimum-maximum-value-range }

V aplikaci **Správa dat** můžete trvale odstranit všechny rozsahy minimálních maximálních hodnot pro vybrané datové sady a organizační jednotky.

1.  Otevřete aplikaci **Správa dat** a klikněte na **Generování minimální a maximální hodnoty**.

2.  Vyberte datovou sadu(y).

3.  Vyberte **Organizační jednotku**. Pamatujte, že výběr kaskáduje k podřazeným organizačním jednotkám!

4.  Klikněte na **Odebrat**.

### Spusťte analýzu minimálně a maximálně odlehlých hodnot { #run-a-minimum-maximum-outlier-analysis }

![](resources/images/data_quality/min_max_analysis.png)

1.  Ověřte, že jste vytvořili rozsahy minimálních a maximálních hodnot.

2.  Otevřete aplikaci **Data Quality** a klikněte na **Min-max outlier analysis**.

3.  Vyberte **Od data** a **Do dne**.

4.  Vyberte, které datové sady(u) chcete do analýzy zahrnout.

5.  Vyberte **Nadřazená organizační jednotka**.

    Budou zahrnuty všechny podřazené organizační jednotky. Analýza se provádí na nezpracovaných datech „pod“ nadřazenou organizační jednotkou, nikoli na agregovaných datech.

6.  Klikněte na **Start**.

    Trvání procesu analýzy závisí na množství dat, která se analyzují. Pokud dojde k porušení ověřování, budou uvedena v seznamu.

    ![](resources/images/data_quality/min_max_result.png)

7.  (Volitelné) Kliknutím na **Stáhnout jako PDF**, **Stáhnout jako Excel** nebo **Stáhnout jako CSV** stáhnete seznam ve formátech PDF, Excel nebo CSV.

> **Tip**
>
> Kliknutím na ikonu hvězdičky označte hodnotu pro další sledování.

## Následná analýza { #follow_up_analysis }

### O následné analýze { #about-follow-up-analysis }

Následná analýza vytvoří seznam všech datových hodnot označených pro následnou kontrolu. Hodnotu dat můžete označit pro následnou kontrolu v aplikaci **Vstup dat** a v seznamu výsledků získáte odlehlou odchylku se standardní odchylkou nebo minimální maximální odchylku.

### Vytvořte seznam datových hodnot označených pro další sledování { #create-list-of-data-values-marked-for-follow-up }

![](resources/images/data_quality/follow_up_analysis.png)

1.  Otevřete aplikaci **Kvalita dat** a klikněte na **Následná analýza**.

2.  Vyberte datovou sadu nebo více datových sad.

3.  Vyberte nadřazenou **Organizační jednotku**.

    Trvání procesu analýzy závisí na množství dat, která se analyzují. Pokud jsou pro sledování označeny datové hodnoty, zobrazí se v seznamu.

4.  Vyberte **Počáteční datum** a **Koncové datum**, které definují období, která vás zajímají o hledání hodnot, které byly označeny pro sledování.

5.  Stisknutím **Sledovat** vygenerujete seznam hodnot, které byly označeny pro sledování.

6.  (Volitelné) Kliknutím na **Stáhnout jako PDF**, **Stáhnout jako Excel** nebo **Stáhnout jako CSV** stáhnete seznam porušení ověření ve formátech PDF, Excel nebo CSV.

![](resources/images/data_quality/follow_up_analysis_result.png)

> **Tip**
>
> Kliknutím na ikonu hvězdičky odeberete následnou značku z hodnoty dat. Do pole můžete také zadat komentář a uvést další informace týkající se hodnoty
