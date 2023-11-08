---
revision_date: "2021-09-15"
template: single.html
---

# Průvodce dokumentací DHIS 2 { #doc_guide_chapter }

## DHIS 2 Dokumentace Přehled Systému { #docs_1 }

DHIS 2 je webový systém pro správu informací ve velmi aktivním vývoji s typicky třemi vydáními ročně. Každé vydání obvykle obsahuje řadu nových funkcí a dalších funkcí. Vzhledem k rychlému tempu vývoje, široké uživatelské základně systému a distribuované globální povaze vývoje je vyžadován komplexní dokumentační systém.

V této kapitole popíšeme dokumentační systém DHIS 2 a jak můžete přispět.

## Úvod { #docs_2 }

Dokumentace DHIS 2 je napsána ve formátu [Commonmark](https://commonmark.org) markdown. Jednou z hlavních výhod markdownů je, že je úplné oddělení mezi obsahem a prezentací. Commonmark je silně definovaná a vysoce kompatibilní specifikace markdown. Protože markdown lze transformovat do nejrůznějších formátů (HTML, PDF atd.) A jedná se o textový formát, slouží jako ideální formát pro dokumentaci systému.

Existuje široká škála textových editorů, které lze použít k vytváření souborů markdown. Pro Linux a Windows je [ghostwriter](https://wereturtle.github.io/ghostwriter/) příjemnou volbou; je zdarma a podporuje souběžný náhled a vlastní šablony stylů.

> **TIP**
>
> Pokud máte možnost použít vlastní css ve vašem markdown editoru, nastavte jej na `./src/commonmark/en/resources/css/dhis2.css`, aby odrážel html výstupní styl pro DHIS2!

Jedním z klíčových konceptů, které je třeba mít na paměti při vytváření dokumentace v markdownu nebo jiných prezentačních neutrálních formátech, je to, že nejprve je třeba vzít v úvahu **obsah** dokumentu. **Prezentace** dokumentu proběhne v samostatném transformačním kroku, kdy se zdrojový text vykreslí do různých formátů, například HTML a PDF. Je proto důležité, aby byl dokument dobře organizovaný a strukturovaný a aby byly brány v úvahu vhodné značky a konstrukční prvky.

Osvědčeným postupem je rozdělit dokument do různých sekcí pomocí záhlaví sekcí. Tímto způsobem lze velmi složité kapitoly rozdělit na menší, zvládnutelnější části. Tento koncept je v zásadě stejný jako Microsoft Word nebo jiné programy pro zpracování textu. Při vytváření dokumentu se proces vykreslování automaticky postará o očíslování oddílů.

## Začínáme s GitHub { #docs_3 }

Dokumentační systém DHIS 2 je spravován na [GitHub](https://github.com/dhis2/dhis2-docs) ve vlastním úložišti zdrojového kódu. GitHub je platforma pro spolupráci, která umožňuje více lidem spolupracovat na softwarových projektech. Aby to bylo možné, je nezbytný systém pro správu verzí, aby bylo možné spravovat všechny změny, které může provést více uživatelů. GitHub používá systém správy zdrojů _git_. I když je nad rámec tohoto dokumentu popsat funkčnost _git_, uživatelé, kteří chtějí vytvořit dokumentaci, budou muset získat alespoň základní znalosti o tom, jak systém funguje. V další části je uveden základní průvodce. Čtečka je uvedena v [git manual](https://git-scm.com/book/en/v2), kde najdete další informace.

Chcete-li začít přidávat nebo upravovat dokumentaci, měli byste nejprve provést kontrolu zdrojového kódu. Pokud ještě nemáte účet GitHub, budete si jej muset pořídit. To lze provést [zde](https://github.com/). Jakmile se zaregistrujete na GitHubu, budete muset požádat o přístup do skupiny _dhis2-documenters_, pokud si přejete přímo upravit zdrojový kód dokumentace.

Přihlaste se do GitHubu a poté nahrajte problém [zde](https://github.com/dhis2/dhis2-docs/issues/new). Vaši žádost budou muset schválit správci skupiny. Jakmile vám byl udělen přístup ke skupině, můžete provést změny ve větvi dokumentace a podle potřeby odesílat a přijímat oznámení. Případně můžete klonovat dokumentaci do svého vlastního úložiště, odevzdat změny na vlastní fork a požádat o sloučení vašich změn se zdrojem dokumentace s požadavkem na stažení [zde](https://github.com/dhis2/dhis2-docs/pulls).

## Získání zdroje dokumentu { #docs_4 }

Chcete-li upravit dokumentaci, budete si muset stáhnout zdroj dokumentace do svého počítače. GitHub používá systém pro správu verzí známý jako git. Existují různé metody, jak zajistit, aby Git pracoval na vašem systému, v závislosti na tom, jaký operační systém používáte. Dobrou podrobnou příručku pro operační systémy Microsoft si můžete prohlédnout [zde](https://help.github.com/articles/getting-started-with-github-for-windows). Alternativně, pokud vám vyhovuje používání příkazového řádku, můžete si stáhnout git z [této stránky](http://git-scm.com/download/win) Pokud používáte Linux, budete si muset do svého systému nainstalovat git prostřednictvím správce balíčků nebo ze zdrojového kódu. Velmi důkladný odkaz na to, jak se používá git, je k dispozici v mnoha různých formátech [zde](http://git-scm.com/book).

Jakmile nainstalujete git do svého systému, budete si muset stáhnout zdroj dokumentu. Postupujte podle tohoto postupu:

1.  Ujistěte se, že máte nainstalovaný git.

2.  V systémech Windows navštivte <https://github.com/dhis2/dhis2-docs> a stiskněte „Klonovat na plochu“. Pokud používáte příkazový řádek, stačí zadat `git clone git@github.com:dhis2/dhis2-docs.git`

3.  Proces stahování by měl začít a všechny zdrojové soubory dokumentace se stáhnou do složky, kterou jste určili.

4.  Jakmile budete mít zdroj, nezapomeňte si vytvořit vlastní větev pro úpravy. Jednoduše spusťte `git checkout -b mybranch`, kde _mybranch_ je název větve, kterou chcete vytvořit.

## Úpravy dokumentace { #docs_5 }

Jakmile stáhnete zdroj, měli byste mít v adresáři úložiště řadu složek. Struktura dokumentů je následující:

```
<root>
└── src
    └── commonmark
        └── en
            ├── dhis2_android_user_man_INDEX.md
            ├── dhis2_developer_manual_INDEX.md
            ├── dhis2_end_user_manual_INDEX.md
            ├── dhis2_implementation_guide_INDEX.md
            ├── dhis2_user_manual_en_INDEX.md
            ├── user_stories_book_INDEX.md
            ├── resources
            │   ├── css
            │   │   ├── dhis2.css
            │   │   └── dhis2_pdf.css
            │   └── images
            │       └── dhis2-logo-rgb-negative.png
            └── content
                ├── android
                │   └── resources
                │       └── images
                ├── common
                │   └── bookinfo.yaml
                ├── developer
                │   ├── resources
                │   │   └── images
                ├── implementation
                │   ├── resources
                │   │   └── images
                │   ├── `resources
                │   │   └── images
                ├── stories
                │   ├── resources
                │   │   └── images
                └── user
                    └── resources
                        └── images


```

Soubory `*_INDEX.md` jsou výchozími body pro hlavní dokumenty. Obsahují pouze směrnice `!INCLUDE`.

např. dhis2_android_user_man_INDEX.md:

```
 !INCLUDE "content/common/about-this-guide.md"
 !INCLUDE "content/android/configure-dhis2-programs-to-work-on-android-apps.md"
 !INCLUDE "content/android/android-event-capture-app.md"
 !INCLUDE "content/android/android-aggregate-data-capture-app.md"
 !INCLUDE "content/android/android-tracker-capture-app.md"
```

Směrnice `!INCLUDE` poukazují na "kapitoly" , které se používají k vytvoření příručky.

> **POZNÁMKA**
>
> směrnice `!INCLUDE` nejsou součástí čistého formátu commonmark, ale používají se v předběžném zpracování k vytvoření hlavních dokumentů. Konkrétní formát zde je formát podporovaný mimo rámec markdown-pp, ale v případě potřeby bychom jej mohli změnit na jiný „include“ formát.

Je naprosto platné používat směrnice `!INCLUDE` také v dílčích dokumentech, ale v současné době jsou dokumenty rozděleny pouze na úrovni kapitol.

- Z důvodu konvence umístěte všechny kapitoly do složky v následujícím formátu:

  `./src/commonmark/en/content/XXXX/<chapter>.md`

  kde `XXXX` představuje jednu z tematických složek, které se používají k organizaci dokumentace, a `<chapter>` je název souboru odkazovaný ze souboru `*_INDEX.md` 

### Používání obrázků { #using-images }

Zdroje obrázků by měly být zahrnuty do struktury složek počínaje řetězcem `resources`<!-- prevent processing -->`/images/` vzhledem k aktuálnímu dokumentu. např. pro kapitolu `content/android/android-event-capture-app.md`, jsou obrázky někde pod `content/android/resources`<!-- prevent processing -->`/images/<rest-of-path>`.

To je důležité, protože `resources`<!-- prevent processing -->`/images` se používá k identifikaci obrázků v souborech. Když budou soubory předzpracovány pro generování, budou snímky shromažďovány v rámci `resources`<!-- prevent processing -->`/images/content/android/<rest-of-path>` vzhledem k hlavnímu dokumentu. _Cesty jsou částečně obráceny, aby se zajistilo, že zůstanou jedinečné při shromažďování obrázků z více tematických složek._

### Odkazy na sekce { #name_of_section }

Abychom mohli v dokumentu poskytnout pevné odkazy, můžeme nastavit pevný textový řetězec, který se má použít v jakékoli sekci. U našich dokumentů pro markdown se to provádí přidáním komentáře za nadpisem sekce ve formuláři:

```
<!-- DHIS2-SECTION-ID:name_of_section -->
```

kde `name_of_section` je nahrazeno id, které chcete použít.

Například:

```

## Ověření { #webapi_validation }

Chcete-li vygenerovat shrnutí ověření dat, můžete pracovat ...
```

Nastaví ID sekce nadpisu úrovně 2 **Validace** na „webapi_validation“, na kterou lze v souboru html odkazovat jako na „#webapi_validation“.

Poté, co je vygenerován celý soubor html, je následně zpracován a jako ID sekce je použito první `DHIS2-SECTION-ID` po začátku sekce.

Postupujte podle konvence malých písmen a podtržítků, abyste vytvořili ID, která jsou platná také jako názvy souborů při rozdělení souborů html.

### Tabulky { #tables }

Jako rozšíření k čisté společné značce také podporujeme _GFM tabulky_ (definované znaky `|`), například:

```
| Table Type | Description |
|:--|:----|
|Commonmark (HTML)| Tables described in pure HTML |
|Github Flavour Markdown (GFM)| Tables described with pipes: easier to read/edit, but limited in complexity|
```

který produkuje výstup jako:

| Typ tabulky | Popis |
| :-- | :-- |
| Commonmark (HTML) | Tabulky popsané v čistém HTML |
| Github Flavour Markdown (GFM) | Tabulky popsané pomocí kanálů: snadnější čtení / úpravy, ale omezené na složitost |

U jednoduchých tabulek se s nimi pracuje mnohem pohodlněji. Jsou omezeny na jednotlivé řádky textu (tj. Každý řádek textu musí být na jednom řádku), ale můžete například použít značky `<br>` k vytvoření zalomení řádků a v případě potřeby k efektivnímu rozdělení odstavců do buněk. Můžete také nadále používat tabulky HTML, pokud opravdu potřebujete větší složitost (ale můžete také zvážit, zda existuje lepší způsob prezentace dat).

## DHIS 2 Bibliografie { #dhis-2-bibliography }

Bilbliografické odkazy aktuálně nejsou podporovány v markdown verzi dokumentace DHIS 2.

## Zpracování vícejazyčné dokumentace { #docs_8 }

Dokumentace DHIS 2 byla přeložena do mnoha různých jazyků, včetně francouzštiny, španělštiny a portugalštiny. Pokud chcete vytvořit překlad dokumentace nebo přispět k jednomu ze stávajících překladů, kontaktujte tým dokumentace DHIS 2 na e-mailu uvedeném na konci této kapitoly.

## Potvrzení změn zpět na GitHub { #docs_10 }

Jakmile dokončíte úpravy dokumentu, budete muset změny odeslat zpět na GitHub. Otevřete příkazový řádek v systému Windows nebo shell v systému Linux a přejděte do složky, do které jste umístili dokumentaci. Pokud jste do svého lokálního úložiště přidali nějaké nové soubory nebo složky, budete je muset přidat do stromu zdroje pomocí příkazu `git add `, za kterým následuje název složky nebo souboru, který jste přidali. Nezapomeňte ke svému odevzdání připojit popisný komentář.

`git commit -m "Vylepšená dokumentace importu organizační jednotky pomocí CSV."`

Nakonec byste měli změny poslat zpět do úložiště pomocí `git push origin mybranch`, kde "mybranch" je název větve, kterou jste vytvořili při rezervaci zdroje dokumentu nebo na které rádi pracujete. K tomu budete potřebovat potřebná oprávnění ke commitu do úložiště. Když jste provedli změny, [můžete vydat pull požadavek](https://github.com/dhis2/dhis2-docs/pulls) aby byly sloučeny s hlavní větví. Vaše změny budou zkontrolovány týmem základní dokumentace a otestovány, aby se zajistilo, že neporuší sestavení, a budou také kontrolovány pro kvalitu. Jak již bylo zmíněno dříve, můžete také poslat své změny do svého vlastního úložiště GitHub, pokud nemáte přístup k hlavnímu repo, a odeslat pull žádost pro sloučení vašich změn.

Pokud máte nějaké dotazy nebo nemůžete najít, jak můžete začít, jednoduše položte otázku naší [vývojové komunitě](https://community.dhis2.org/c/development).

## Podpora a rozšíření Markdown { #markdown-support-and-extensions }

Tato část se pokusí zachytit označení a rozšíření, které jsou podporovány pro dokumentaci DHIS 2, a poskytnout náhled použitých stylů.

### h3 Nadpis { #h3-heading }

#### h4 Nadpis { #h4-heading }

##### h5 Nadpis { #h5-heading }

###### h6 Nadpis { #h6-heading }

Základní text.

### Horizontální linky { #horizontal-rules }

```
___

---

***
```

---

---

---

### Zvýraznění { #emphasis }

**Toto je tučný text**

**Toto je tučný text**

_Toto je kurzíva_

_Toto je kurzíva_

~~Přeškrtnutí~~

### Blokové uvozovky { #blockquotes }

=== "Příklady"

    > Blokové uvozovky lze také vnořit ...
    >> ... pomocí dalších znamének větší než umístěné vedle sebe ...
    > > > ... nebo s mezerami mezi šipkami.

=== "Markdown"

    ```
    > Blokové uvozovky lze také vnořit ...
    >> ... pomocí dalších znamének větší než umístěné vedle sebe ...
    > > > ... nebo s mezerami mezi šipkami.
    ```

### Kód { #code }

Vložený `code`

Vložený zvýrazněný kód `#!js var test = 0;` vytvořený uvnitř

```
`#!js var test = 0;`
```

Odsazený kód

    // Nějaký komentář
    line 1 of code
    line 2 of code
    line 3 of code

Blokový kód "fences"

```
Ukázkový text zde ...
```

Zvýraznění syntaxe

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

Dlouhé línie

```
Buffalo buffalo (zvířata zvaná "buffalo" z města Buffalo) [ten] Buffalo buffalo buffalo (že zvířata z města Buffalo) buffalo Buffalo buffalo (šikanuje tato zvířata z tohoto města).
```

### Seznamy { #lists }

Neuspořádané

- Vytvořte seznam novým řádkem s `+`, `-`, or `*`
- Dílčí seznamy se vytvářejí odsazením 2 mezer:

  - Změna znaku značky vynutí nový začátek seznamu:

    - Ac tristique libero volutpat at

    * Facilisis v pretium nisl aliquet

      ```
      an indented code block
      ```

    - Nulla volutpat aliquam velit

- Velmi snadné!

Seřazeno

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

4. Můžete použít sekvenční čísla...
5. ...nebo ponechte všechna čísla jako `1.`

Začnete číslovat s odsazením?:

57. foo
1. bar

Víceúrovňové

1. první položka
2. stále první úroveň
   1. druhá úroveň
   2. stále druhá
      1. třetí úroveň
      ```
      a block of code at the third level
      ```
      2. stále třetí úroveň
   3. druhá úroveň znovu
3. zpět na první úroveň
   1. druhá
      1. Přestaň s tím!

### Tabulky { #tables }

| Návratový parametr | Popis |
| :-- | :-- |
| aoc | Identifikátor kombinace možnosti atributu |
| pe | Identifikátor období |
| ou | Identifikátor organizační jednotky |
| oprávnění | Oprávnění: 'mayApprove', 'mayUnapprove', 'mayAccept', 'mayUnaccept' a 'mayReadData' (stejné definice jako pro získání stavu jediného schválení.) |
| stav | Jeden ze stavů schválení dat (stejný jako u stavu získání jediného schválení.) |
| wf | Identifikátor pracovního postupu schválení dat |

Sloupce zarovnané doprava a na střed

| Návratový parametr | Popis |
| --: | :-: |
| aoc | Identifikátor kombinace možnosti atributu |
| pe | Identifikátor období |
| ou | Identifikátor organizační jednotky |
| oprávnění | Oprávnění: 'mayApprove', 'mayUnapprove', 'mayAccept', 'mayUnaccept' a 'mayReadData' (stejné definice jako pro získání stavu jediného schválení.) |
| stav | Jeden ze stavů schválení dat (stejný jako u stavu získání jediného schválení.) |
| wf | Identifikátor pracovního postupu schválení dat |

### Odkazy { #links }

[link text](http://docs.dhis2.org)

[link with title](http://docs.dhis2./org "title text!")

Automaticky převedený odkaz https://github.com/dhis2

### Obrázky { #images }

Obrázky se zobrazují v plné velikosti s maximální šířkou 100%

```
![](resources/images/dhis2_screenshots.jpg)
```

![](resources/images/dhis2_screenshots.jpg)

Přidání názvu automaticky způsobí vykreslení jako obrázek. Vložené třídy a styly lze přidat do složených závorek.

```
![DHIS2 Screenshots](resources/images/dhis2_screenshots.jpg "The Title"){ .center width=50% }

```

![DHIS2 Screenshots](resources/images/dhis2_screenshots.jpg "The Title"){ .center width=50% }

<!-- Stejně jako odkazy, i obrázky mají syntaxi stylu poznámky pod čarou s odkazem později v dokumentu definujícím umístění URL:

```
![Alternativní text][id]{ width=30% }

[id]: resources/images/dhis2_screenshots.jpg "Název"
```

![Alternativní text][id]{ width=30% }

[id]: resources/images/dhis2_screenshots.jpg "Název" -->

### Připomenutí { #admonitions }

Kromě obecných uvozovek jsou podporovány následující uvozovky s předdefinovanými styly.

#### Poznámka { #note }

=== "Poznámka"

    > **Poznámka**
    >
    > Poznámka obsahuje další informace, které je třeba zvážit, nebo a
    > odkaz na další informace, které mohou být užitečné.

=== "Markdown"

    ```
    > **Note**
    >
    > A note contains additional information which should be considered or a
    > reference to more information which may be helpful.
    ```

#### Tip { #tip }

=== "Tip"

    > **Tip**
    >
    > Tip může být užitečnou radou, například jak provést a
    > konkrétní úkol efektivněji.

=== "Markdown"

    ```
    > **Tip**
    >
    > A tip can be a useful piece of advice, such as how to perform a
    > particular task more efficiently.
    ```

#### Důležité { #important }

=== "Důležité"

    > **Důležité**
    >
    > Důležité informace by neměly být ignorovány a obvykle indikují
    > něco, co vyžaduje aplikace.

=== "Markdown"

    ```
    > **Important**
    >
    > Important information should not be ignored, and usually indicates
    > something which is required by the application.
    ```

#### Pozor { #caution }

=== "Pozor"

    > **Pozor**
    >
    > Informace obsažené v těchto částech by měly být pečlivě
    > zváženo, a pokud nebudete dbát, mohlo by to vést k neočekávaným výsledkům v
    > analýze, výkonu nebo funkčnosti.

=== "Markdown"

    ```
    > **Caution**
    >
    > Information contained in these sections should be carefully
    > considered, and if not heeded, could result in unexpected results in
    > analysis, performance, or functionality.
    ```

#### Varování { #warning }

=== "Varování"

    > **Varování**
    >
    > Informace, které jsou obsaženy v těchto částech, by mohly být výsledkem, pokud nebudou zohledněny
    > při trvalé ztrátě dat, nebo ovlivnění celkové použitelnosti systému.

=== "Markdown"

    ```
    > **Warning**
    >
    > Information contained in these sections, if not heeded, could result
    > in permanent data loss or affect the overall usability of the system.
    ```

#### Probíhající práce { #work-in-progress }

=== "Probíhá práce"

    > **Probíhá práce**
    >
    > Informace obsažené v těchto částech naznačují, že se jedná o problémy nebo chyby, na kterých aktuálně pracujeme.

=== "Markdown"

    ```
    > **Work In Progress**
    >
    > Information contained in these sections, will indicate that these are issues or errors we are currently working on.
    ```

#### Příklad { #example }

=== "Příklad"

    > **Příklad**
    >
    > Způsob, jak věnovat zvláštní pozornost příkladům.
    >
    > Admonitions mohou zahrnovat bloky kódu
    >
    > ```js
    > var foo = function (bar) {
    > return bar++;
    > };
    >
    > console.log(foo(5));
    > ```

=== "Markdown"

    ```
    > **Example**
    >
    > A way to bring special attention to examples.
    >
    > Admonitions can include a code blocks
    >
    > ```js
    > var foo = function (bar) {
    >   return bar++;
    > };
    >
    > console.log(foo(5));
    > ```
    ```

### Smíšený { #miscellaneous }

Může být možné v závislosti na zásuvných modulech / rozšířeních

#### Matematické rovnice { #mathematical-equations }

Bloky musí být uzavřeny do  `\[...\]` nebo `\begin{} ... \end{}`. 
Řádkové bloky musí být uzavřeny do \`#!math ... \` nebo `\(...\)`.

=== "Rovnice"

    \[
    Indicator = {\frac{BcgVaccinationsUnder1Year}{TargetPopulationUnder1Year}} \times 100
    \]

    \[3 < 4\]

    \begin{align}
        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

    The wave equation for \( u \) is

    \begin{equation}
      \frac{\partial^2u}{\partial t^2} = c^2\nabla^2u
    \end{equation}

    where \( \nabla^2 \) is the spatial Laplacian and \( c \) is constant.

    This equation `#!math p(x|y) = \frac{p(y|x)p(x)}{p(y)}` is inline.

    The homomorphism `#!math f` is injective if and only if its kernel is only the
    singleton set `#!math e_G`, because otherwise `#!math \exists a,b\in G` with `#!math a\neq b` such that `#!math f(a)=f(b)`.

=== "Markdown"

    ```
    \[
    Indicator = {\frac{BcgVaccinationsUnder1Year}{TargetPopulationUnder1Year}} \times 100
    \]

    \[3 < 4\]

    \begin{align}
        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

    The wave equation for \( u \) is

    \begin{equation}
      \frac{\partial^2u}{\partial t^2} = c^2\nabla^2u
    \end{equation}

    where \( \nabla^2 \) is the spatial Laplacian and \( c \) is constant.

    This equation `#!math p(x|y) = \frac{p(y|x)p(x)}{p(y)}` is inline.

    The homomorphism `#!math f` is injective if and only if its kernel is only the
    singleton set `#!math e_G`, because otherwise `#!math \exists a,b\in G` with `#!math a\neq b`
    such that `#!math f(a)=f(b)`.
    ```

#### Typografické náhrady { #typographic-replacements }

| Markdown       | Výsledek       |
| -------------- | ------------ |
| `(tm)`         | (tm)         |
| `(c)`          | (c)          |
| `(r)`          | (r)          |
| `c/o`          | c/o          |
| `+/-`          | +/-          |
| `-->`          | -->          |
| `<--`          | <--          |
| `<-->`         | <-->         |
| `=/=`          | =/=          |
| `1/4 atd.`    | 1/4, atd.    |
| `1st 2nd etc.` | 1. 2. atd. |

#### Dolní index / horní index { #subscript-superscript }

    - 19^th^
    - H~2~O

- 19^th^
- H~2~O

++Vložený text++

==Označený text==

#### [Poznámky pod čarou](https://github.com/markdown-it/markdown-it-footnote) { #footnoteshttpsgithubcommarkdown-itmarkdown-it-footnote }

Odkaz pod čarou 1 link[^first].

Odkaz pod čarou 2 [^second].

definice Vložená poznámka pod čarou ^[Text vložené poznámky pod čarou] 

Duplikovaný odkaz pod čarou [^druhý].

[^first]: Poznámka pod čarou **může mít markup**

    a více odstavců.

[^second]: Text poznámky pod čarou.

#### Seznamy definic { #definition-lists }

Termín 1: Definice 1 s líným pokračováním.

Termín 2 s _inline markup_: Definice 2

        {nějaký kód, součást definice 2}

    Třetí odstavec definice 2.

#### Emojies { #emojies }

Několik sad emodži je podporováno zadáním názvu emodži obklopeného dvojtečkami: např. `:smile:`. Níže je uveden seznam běžných sad, ty, které nejsou vykresleny, nejsou aktuálně podporovány.

=== "Lidé"

    :bowtie: :smile: :laughing: :blush: :smiley: :relaxed: :smirk: :heart_eyes: :kissing_heart: :kissing_closed_eyes: :flushed: :relieved: :satisfied: :grin: :wink: :stuck_out_tongue_winking_eye: :stuck_out_tongue_closed_eyes: :grinning: :kissing: :kissing_smiling_eyes: :stuck_out_tongue: :sleeping: :worried: :frowning: :anguished: :open_mouth: :grimacing: :confused: :hushed: :expressionless: :unamused: :sweat_smile: :sweat: :disappointed_relieved: :weary: :pensive: :disappointed: :confounded: :fearful: :cold_sweat: :persevere: :cry: :sob: :joy: :astonished: :scream: :neckbeard: :tired_face: :angry: :rage: :triumph: :sleepy: :yum: :mask: :sunglasses: :dizzy_face: :imp: :smiling_imp: :neutral_face: :no_mouth: :innocent: :alien: :yellow_heart: :blue_heart: :purple_heart: :heart: :green_heart: :broken_heart: :heartbeat: :heartpulse: :two_hearts: :revolving_hearts: :cupid: :sparkling_heart: :sparkles: :star: :star2: :dizzy: :boom: :collision: :anger: :exclamation: :question: :grey_exclamation: :grey_question: :zzz: :dash: :sweat_drops: :notes: :musical_note: :fire: :hankey: :poop: :shit: :+1: :thumbsup: :-1: :thumbsdown: :ok_hand: :punch: :facepunch: :fist: :v: :wave: :hand: :raised_hand: :open_hands: :point_up: :point_down: :point_left: :point_right: :raised_hands: :pray: :point_up_2: :clap: :muscle: :metal: :fu: :walking: :runner: :running: :couple: :family: :two_men_holding_hands: :two_women_holding_hands: :dancer: :dancers: :ok_woman: :no_good: :information_desk_person: :raising_hand: :bride_with_veil: :person_with_pouting_face: :person_frowning: :bow: :couplekiss: :couple_with_heart: :massage: :haircut: :nail_care: :boy: :girl: :woman: :man: :baby: :older_woman: :older_man: :person_with_blond_hair: :man_with_gua_pi_mao: :man_with_turban: :construction_worker: :cop: :angel: :princess: :smiley_cat: :smile_cat: :heart_eyes_cat: :kissing_cat: :smirk_cat: :scream_cat: :crying_cat_face: :joy_cat: :pouting_cat: :japanese_ogre: :japanese_goblin: :see_no_evil: :hear_no_evil: :speak_no_evil: :guardsman: :skull: :feet: :lips: :kiss: :droplet: :ear: :eyes: :nose: :tongue: :love_letter: :bust_in_silhouette: :busts_in_silhouette: :speech_balloon: :thought_balloon:

=== "Příroda"

    :sunny: :umbrella: :cloud: :snowflake: :snowman: :zap: :cyclone: :foggy: :ocean: :cat: :dog: :mouse: :hamster: :rabbit: :wolf: :frog: :tiger: :koala: :bear: :pig: :pig_nose: :cow: :boar: :monkey_face: :monkey: :horse: :racehorse: :camel: :sheep: :elephant: :panda_face: :snake: :bird: :baby_chick: :hatched_chick: :hatching_chick: :chicken: :penguin: :turtle: :bug: :honeybee: :ant: :beetle: :snail: :octopus: :tropical_fish: :fish: :whale: :whale2: :dolphin: :cow2: :ram: :rat: :water_buffalo: :tiger2: :rabbit2: :dragon: :goat: :rooster: :dog2: :pig2: :mouse2: :ox: :dragon_face: :blowfish: :crocodile: :dromedary_camel: :leopard: :cat2: :poodle: :paw_prints: :bouquet: :cherry_blossom: :tulip: :four_leaf_clover: :rose: :sunflower: :hibiscus: :maple_leaf: :leaves: :fallen_leaf: :herb: :mushroom: :cactus: :palm_tree: :evergreen_tree: :deciduous_tree: :chestnut: :seedling: :blossom: :ear_of_rice: :shell: :globe_with_meridians: :sun_with_face: :full_moon_with_face: :new_moon_with_face: :new_moon: :waxing_crescent_moon: :first_quarter_moon: :waxing_gibbous_moon: :full_moon: :waning_gibbous_moon: :last_quarter_moon: :waning_crescent_moon: :last_quarter_moon_with_face: :first_quarter_moon_with_face: :moon: :earth_africa: :earth_americas: :earth_asia: :volcano: :milky_way: :partly_sunny: :octocat: :squirrel:

=== "Objekty"

    :bamboo: :gift_heart: :dolls: :school_satchel: :mortar_board: :flags: :fireworks: :sparkler: :wind_chime: :rice_scene: :jack_o_lantern: :ghost: :santa: :christmas_tree: :gift: :bell: :no_bell: :tanabata_tree: :tada: :confetti_ball: :balloon: :crystal_ball: :cd: :dvd: :floppy_disk: :camera: :video_camera: :movie_camera: :computer: :tv: :iphone: :phone: :telephone: :telephone_receiver: :pager: :fax: :minidisc: :vhs: :sound: :speaker: :mute: :loudspeaker: :mega: :hourglass: :hourglass_flowing_sand: :alarm_clock: :watch: :radio: :satellite: :loop: :mag: :mag_right: :unlock: :lock: :lock_with_ink_pen: :closed_lock_with_key: :key: :bulb: :flashlight: :high_brightness: :low_brightness: :electric_plug: :battery: :calling: :email: :mailbox: :postbox: :bath: :bathtub: :shower: :toilet: :wrench: :nut_and_bolt: :hammer: :seat: :moneybag: :yen: :dollar: :pound: :euro: :credit_card: :money_with_wings: :e-mail: :inbox_tray: :outbox_tray: :envelope: :incoming_envelope: :postal_horn: :mailbox_closed: :mailbox_with_mail: :mailbox_with_no_mail: :door: :smoking: :bomb: :gun: :hocho: :pill: :syringe: :page_facing_up: :page_with_curl: :bookmark_tabs: :bar_chart: :chart_with_upwards_trend: :chart_with_downwards_trend: :scroll: :clipboard: :calendar: :date: :card_index: :file_folder: :open_file_folder: :scissors: :pushpin: :paperclip: :black_nib: :pencil2: :straight_ruler: :triangular_ruler: :closed_book: :green_book: :blue_book: :orange_book: :notebook: :notebook_with_decorative_cover: :ledger: :books: :bookmark: :name_badge: :microscope: :telescope: :newspaper: :football: :basketball: :soccer: :baseball: :tennis: :8ball: :rugby_football: :bowling: :golf: :mountain_bicyclist: :bicyclist: :horse_racing: :snowboarder: :swimmer: :surfer: :ski: :spades: :hearts: :clubs: :diamonds: :gem: :ring: :trophy: :musical_score: :musical_keyboard: :violin: :space_invader: :video_game: :black_joker: :flower_playing_cards: :game_die: :dart: :mahjong: :clapper: :memo: :pencil: :book: :art: :microphone: :headphones: :trumpet: :saxophone: :guitar: :shoe: :sandal: :high_heel: :lipstick: :boot: :shirt: :tshirt: :necktie: :womans_clothes: :dress: :running_shirt_with_sash: :jeans: :kimono: :bikini: :ribbon: :tophat: :crown: :womans_hat: :mans_shoe: :closed_umbrella: :briefcase: :handbag: :pouch: :purse: :eyeglasses: :fishing_pole_and_fish: :coffee: :tea: :sake: :baby_bottle: :beer: :beers: :cocktail: :tropical_drink: :wine_glass: :fork_and_knife: :pizza: :hamburger: :fries: :poultry_leg: :meat_on_bone: :spaghetti: :curry: :fried_shrimp: :bento: :sushi: :fish_cake: :rice_ball: :rice_cracker: :rice: :ramen: :stew: :oden: :dango: :egg: :bread: :doughnut: :custard: :icecream: :ice_cream: :shaved_ice: :birthday: :cake: :cookie: :chocolate_bar: :candy: :lollipop: :honey_pot: :apple: :green_apple: :tangerine: :lemon: :cherries: :grapes: :watermelon: :strawberry: :peach: :melon: :banana: :pear: :pineapple: :sweet_potato: :eggplant: :tomato: :corn:

=== "Místa"

    :house: :house_with_garden: :school: :office: :post_office: :hospital: :bank: :convenience_store: :love_hotel: :hotel: :wedding: :church: :department_store: :european_post_office: :city_sunrise: :city_sunset: :japanese_castle: :european_castle: :tent: :factory: :tokyo_tower: :japan: :mount_fuji: :sunrise_over_mountains: :sunrise: :stars: :statue_of_liberty: :bridge_at_night: :carousel_horse: :rainbow: :ferris_wheel: :fountain: :roller_coaster: :ship: :speedboat: :boat: :sailboat: :rowboat: :anchor: :rocket: :airplane: :helicopter: :steam_locomotive: :tram: :mountain_railway: :bike: :aerial_tramway: :suspension_railway: :mountain_cableway: :tractor: :blue_car: :oncoming_automobile: :car: :red_car: :taxi: :oncoming_taxi: :articulated_lorry: :bus: :oncoming_bus: :rotating_light: :police_car: :oncoming_police_car: :fire_engine: :ambulance: :minibus: :truck: :train: :station: :train2: :bullettrain_front: :bullettrain_side: :light_rail: :monorail: :railway_car: :trolleybus: :ticket: :fuelpump: :vertical_traffic_light: :traffic_light: :warning: :construction: :beginner: :atm: :slot_machine: :busstop: :barber: :hotsprings: :checkered_flag: :crossed_flags: :izakaya_lantern: :moyai: :circus_tent: :performing_arts: :round_pushpin: :triangular_flag_on_post: :jp: :kr: :cn: :us: :fr: :es: :it: :ru: :gb: :uk: :de:

=== "Symboly"

    :one: :two: :three: :four: :five: :six: :seven: :eight: :nine: :keycap_ten: :1234: :zero: :hash: :symbols: :arrow_backward: :arrow_down: :arrow_forward: :arrow_left: :capital_abcd: :abcd: :abc: :arrow_lower_left: :arrow_lower_right: :arrow_right: :arrow_up: :arrow_upper_left: :arrow_upper_right: :arrow_double_down: :arrow_double_up: :arrow_down_small: :arrow_heading_down: :arrow_heading_up: :leftwards_arrow_with_hook: :arrow_right_hook: :left_right_arrow: :arrow_up_down: :arrow_up_small: :arrows_clockwise: :arrows_counterclockwise: :rewind: :fast_forward: :information_source: :ok: :twisted_rightwards_arrows: :repeat: :repeat_one: :new: :top: :up: :cool: :free: :ng: :cinema: :koko: :signal_strength: :u5272: :u5408: :u55b6: :u6307: :u6708: :u6709: :u6e80: :u7121: :u7533: :u7a7a: :u7981: :sa: :restroom: :mens: :womens: :baby_symbol: :no_smoking: :parking: :wheelchair: :metro: :baggage_claim: :accept: :wc: :potable_water: :put_litter_in_its_place: :secret: :congratulations: :m: :passport_control: :left_luggage: :customs: :ideograph_advantage: :cl: :sos: :id: :no_entry_sign: :underage: :no_mobile_phones: :do_not_litter: :non-potable_water: :no_bicycles: :no_pedestrians: :children_crossing: :no_entry: :eight_spoked_asterisk: :eight_pointed_black_star: :heart_decoration: :vs: :vibration_mode: :mobile_phone_off: :chart: :currency_exchange: :aries: :taurus: :gemini: :cancer: :leo: :virgo: :libra: :scorpius: :sagittarius: :capricorn: :aquarius: :pisces: :ophiuchus: :six_pointed_star: :negative_squared_cross_mark: :a: :b: :ab: :o2: :diamond_shape_with_a_dot_inside: :recycle: :end: :on: :soon: :clock1: :clock130: :clock10: :clock1030: :clock11: :clock1130: :clock12: :clock1230: :clock2: :clock230: :clock3: :clock330: :clock4: :clock430: :clock5: :clock530: :clock6: :clock630: :clock7: :clock730: :clock8: :clock830: :clock9: :clock930: :heavy_dollar_sign: :copyright: :registered: :tm: :x: :heavy_exclamation_mark: :bangbang: :interrobang: :o: :heavy_multiplication_x: :heavy_plus_sign: :heavy_minus_sign: :heavy_division_sign: :white_flower: :100: :heavy_check_mark: :ballot_box_with_check: :radio_button: :link: :curly_loop: :wavy_dash: :part_alternation_mark: :trident: :black_square: :white_square: :white_check_mark: :black_square_button: :white_square_button: :black_circle: :white_circle: :red_circle: :large_blue_circle: :large_blue_diamond: :large_orange_diamond: :small_blue_diamond: :small_orange_diamond: :small_red_triangle: :small_red_triangle_down: :shipit:

# Odesílání rychlých oprav dokumentů { #submitting_doc_fixes }

U malých změn v dokumentu je skutečně velmi snadné pro kohokoli odesílat změny, aniž by prošel celým procesem založení problému v JIRA o DHIS 2. To lze provést přímo v [GitHub](https://github.com/dhis2/dhis2-docs) a nevyžaduje žádné znalosti git. _Vše, co potřebujete, je účet GitHub!_.

Tato část je zamýšlena jako návod k provedení jednoduchých změn.

## Kontrola překlepů { #typo-fix-walk-through }

V tomto scénáři čteme dokumentaci a najdeme překlep (slovo _manditory_ by mělo být _mand**a**tory_):

![Překlep v dokumentaci aplikace Capture](resources/images/doc_pr_001.png)

Toto je v kapitole „Používání aplikace Capture“ v uživatelské příručce DHIS 2. Chceme to napravit, takže ...

1.  Přihlásíme se na GitHub: https://github.com/dhis2/dhis2-docs

    Pokud nemáte účet, klikněte na odkaz  `Sign up`  na webu GitHub
    (public accounts are free) ![GitHub sign in](resources/images/doc_pr_001b.png)

2.  Nyní musíme najít kapitolu, kterou chceme změnit. Každá kapitola je jedním souborem v úložišti GitHub a na kapitoly se odkazuje ze souboru „INDEX“, který představuje celý dokument.

    Soubory indexů jsou zde: https://github.com/dhis2/dhis2-docs/tree/master/src/commonmark/en

    ![Indexové soubory dokumentace](resources/images/doc_pr_002.png)

    > You may notice the button near the top right that says "Branch: **master**". This indicates that we are looking at the documents for the master branch (i.e. the documentation for the very latest version of DHIS 2). If we wanted to edit the document for, say, version 2.29 instead, then we would use that button to select branch 2.29!  
    > (_2.29 is the earliest version supported in this markdown format_).

    a. V tomto případě je kapitola, kterou chceme, v Uživatelské příručce, takže otevřeme indexový soubor `dhis2_user_manual_en_INDEX.md`:

    > Pro správné zobrazení rejstříku vyberte režim  `Raw ` nebo  `Upravit`!

    ![Index souboru obsahu](resources/images/doc_pr_003.png)

    Tady vidíme, že na kapitolu „Používání aplikace Capture“ se odkazuje jako na `content/user/using-the-capture-app.md`

3.  Odkaz, který jsme našli výše, je cesta z aktuálního umístění, takže musíme přejít na: [https://github.com/dhis2/dhis2-docs/blob/master/src/commonmark/en/**content/user/using-the-capture-app.md**](https://github.com/dhis2/dhis2-docs/blob/master/src/commonmark/en/content/user/using-the-capture-app.md)

        ![Kapitola aplikace Capture](resources/images/doc_pr_004b.png)

4.  Odtud můžeme zvolit úpravu souboru (_ikona tužky_). Zobrazí se panel úprav:

        Here we have found and highlighted the offending word!
        ![Edit](resources/images/doc_pr_005.png)

        > Don't worry about the blue warning at the top that says we don't have
        write access to the file!

        We can make the change and preview it in the `Preview changes` tab if we want.
        Here is the preview:
        ![Preview](resources/images/doc_pr_006.png)

5.  Nakonec můžeme odeslat naši změnu jako _Pull Request_ (PR). We add a title for the change (and an _optional_ description) and click `Propose file change` ![Submit the change](resources/images/doc_pr_007.png)

    a. Vidíme souhrn našich změn a klikneme na `Create pull request`: ![Odeslat změnu](resources/images/doc_pr_008.png)

6.  Vše hotovo!

Nyní je v systému pull request, který může tým DHIS 2 snadno zkontrolovat a přijmout. ![Odeslat změnu](resources/images/doc_pr_009.png)

Po přijetí se změna objeví v dalším sestavení dokumentace!

# Používání JIRA pro problémy DHIS2 { #jira-gettingstarted }

## Zaregistrujte se do JIRA - je otevřený pro každého\! { #sign-up-to-jira-its-open-to-everyone }

1.  Jděte na: <https://jira.dhis2.org>.

2.  Vytvořte si účet se svým jménem a e-mailovou adresou.

## Nahlásit problém { #report-an-issue }

> **Tip**
>
> Nejste si jisti, zda něco chybí, je to chyba, nebo je zastaralá? Opravdu bychom ocenili, že se na konferenci vývojářů zeptáte ještě před přímým nahlášením chyby. Díky\!

1.  V horním menu klikněte na **Vytvořit**.

2.  Vyberte **projekt** ze seznamu.

3.  Vyberte **typ problému**:

    - **Vylepšení** - pokud nám chcete sdělit něco, co by mohlo být lepší, například použitelnost nebo návrhy.

    - **Nová funkce** - pokud chcete navrhnout funkci.

    - **Úkol** - pokud jste byli požádáni, abyste pracovali na úkolu DHIS2.

    - **Bug** - pokud jste našli něco, co je třeba opravit.

    - **Epic** - pokud chcete odeslat nápad na novou oblast DHIS2, jako je aplikace. Epic se používá pro problémy složitější než nové funkce.

4.  Klikněte na **Vytvořit**.

    > **Tip**
    >
    > To create several issues in one go, select **Create another**.

5.  Vyplňte formulář pro vydání. Dejte nám prosím dostatek kontextu\! Zahrňte protokoly serveru, protokoly konzoly JavaScript, verzi DHIS2 a webový prohlížeč, který používáte.

![](resources/images/jira_create_issue.png)

## Vyhledejte problémy { #search-for-issues }

Klikněte na **Problémy \> Vyhledat problémy**.

Pokud kliknete na **Upřesnit**, můžete si vyhledávací kritéria seřadit pomocí předdefinovaných polí. Do vyhledávacího pole můžete také zadat hledané výrazy. Viz také: [Hledat syntaxi pro textová pole](https://confluence.atlassian.com/jirasoftwareserver072/search-syntax-for-text-fields-829057414.html).

![](resources/images/jira_search_issues.png)

## O filtrech { #about-filters }

Výsledky hledání můžete uložit jako filtry, abyste se k nim dostali rychleji. Filtr je velmi podobný oblíbenému. Vytvořili jsme filtry pro funkce určené pro čísla vydání 2.26, 2.27 a 2.28 a pro všechny otevřené chyby.

## Vytvořte filtr { #create-a-filter }

1.  Chcete-li vytvořit filtr, přejděte do části **Problémy \> Vyhledat problémy**.

2.  Přidejte do vyhledávání filtry, například:

    - **Projekt** - hlavním softwarovým projektem je DHIS 2.

    - **Typ** - můžete filtrovat podle **Standardních typů problémů**, jako jsou Nové funkce, Vylepšení, Chyby nebo Epické, nebo **Typy problémů s podúkolem**.

    - **Stav** - filtrovat podle **Úkolů** (nespuštěno) a **Hotovo**, například.

    - **Verze** - klikněte na **Další \> Všechna kritéria \> Opravit verzi** a filtrujte podle čísla vydání DHIS2.

    - **Interní** - klikněte na **Další \> Interní funkce**, chcete-li z vyhledávání vyloučit nízkoúrovňové (back-endové) funkce.

3.  Klikněte na **Uložit jako**. Toto tlačítko je v horní části podokna Hledat.

    ![](resources/images/jira_save.png)

4.  Zadejte název vyhledávacího filtru a klikněte na **Odeslat**. Váš filtr je nyní k dispozici v **oblíbených filtrech**. Pomocí šipky upravte filtr. Váš filtr je k dispozici také na **System Dashboard**.

    ![](resources/images/jira_favorite_filters.png)

## Přidejte do svého profilu filtr { #add-a-filter-to-your-profile }

Chcete-li do svého profilu přidat filtr, klikněte na **Problémy \> Spravovat filtry** a klikněte na ikonu hvězdičky vedle každého filtru.

![](resources/images/jira_manage_filters.png)

## Odeberte výrazy vyhledávacího filtru z vyhledávání { #remove-search-filter-terms-from-your-search }

Kliknutím na křížek odeberete z vyhledávacího dotazu výrazy, které jste dříve přidali.

![](resources/images/jira_remove_filters.png)

## Komunikujte s námi { #communicate-with-us }

Chcete-li sdílet informace, vyjasnit požadavky nebo prodiskutovat podrobnosti o problému, proveďte to pomocí komentářů k problému.

1.  Vyberte problém, který chcete komentovat.

2.  V zobrazení Detail problému klikněte na **Komentovat** a zadejte svůj text.

    Chcete-li o svém komentáři poslat e-mail ostatním, jednoduše zadejte do pole pro komentář **@Uživatelské jméno**. Na e-mailové adresy uživatelů, které jsou zaregistrovány v jejich účtech JIRA, bude zaslán e-mail.

3.  Klikněte na **Přidat**.

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
