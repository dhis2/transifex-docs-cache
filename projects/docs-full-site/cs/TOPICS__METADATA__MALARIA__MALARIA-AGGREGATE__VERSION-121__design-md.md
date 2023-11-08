---
edit_url: "https://github.com/dhis2-metadata/MAL_AGG/blob/master/docs/mal_agg-design-1.2.1.md"
revision_date: "2022-07-18"
---

# Návrh agregátního systému malárie { #malaria-aggregate-system-design }

## Úvod { #introduction }

Tento dokument popisuje návrh systému pro konfigurační balíček malárie pro agregované hlášení a zaměřuje se na to, jak byla v DHIS2 navržena část konfigurace shromažďování dat (tj. Datové sady a datové prvky). To je do značné míry založeno na pokynech _[Sledování nemocí pro kontrolu malárie](https://apps.who.int/iris/bitstream/handle/10665/44851/9789241503341_eng.pdf;jsessionid=7D2258370F31444A72815B5CFB2E1FE8?ua=1?sequence=1)_.

## Datová sada malárie a design datových prvků { #malaria-data-set-and-data-element-design }

Program malárie se skládá ze 3 různých souborů dat, které lze kdykoli použít na základě potřeb programu:

1. Roční údaje o malárii
2. Snížení zátěže malárií
3. Odstranění malárie

Tyto datové sady obsahují doporučené datové prvky ke shromažďování pro každou z těchto samostatných aktivit. Kromě toho existuje skupina datových prvků `Malárie nepřiřazená`, která se skládá z dalších datových prvků, které by mohly být potenciálně přiřazeny k datovým sadám _Snížení zátěže malárie_ a _Eliminace malárie_.

_Roční datová sada malarie_ se doporučuje ve všech nastaveních. Soubory dat _Eliminace malárie _ a  _Snížení zátěže malárie_ lze použít buď samostatně, nebo ve vzájemném spojení v závislosti na typu reakcí na veřejné zdraví prováděných v konkrétní zeměpisné oblasti (např. v jednom okrese lze použít soubor údajů o snížení zátěže, zatímco v jiném lze použít soubor údajů o eliminaci malárie).

### Roční údaje o malárii { #malaria-annual-data }

Soubor ročních údajů o malárii obsahuje informace o následujících třech hlavních položkách:

1. Financování (současné financování i potřeba financování)
2. Distribuce moskytier a ochrana zbytkovým postřikem uvnitř budov
3. Obyvatelstvo v ohrožení

Jak název napovídá, tyto informace se shromažďují pouze jednou ročně. Tato sada dat obsahuje převážně plochou strukturu; pouze s jedním datovým prvkem (celkový počet obyvatel) rozděleným podle věku. Toto rozčlenění je dosti vysvětlující, protože je efektivnější rozčlenit tento datový prvek populace podle možností tří věkových kategorií, než vytvořit 3 datové prvky samostatně.

### Snížení zátěže malárií { #malaria-burden-reduction }

Soubor údajů o snížení zátěže malárií je rozdělen do sedmi částí:

1. Ambulantní údaje
2. Laboratoř
3. Zásahy
4. Léčba
5. Přerušovaná preventivní léčba v těhotenství (IPTp)
6. Těhotná žena
7. Není skladem

Jedná se o měsíční soubor dat, který je určen pro oblasti, kde je prioritou snižování zátěže malárií. Tabulka níže pojednává o struktuře datových prvků, které se objevují v různých částech, a také o důvodech použité struktury.

| Sekce | Aplikovaná struktura | Rozčlenění | Odůvodnění |
| :-- | :-- | :-- | :-- |
| Ambulantní údaje | Rozděleno | Věk (0-4, 5-14, 15+ let) | Kombinace věkových kategorií drasticky snižuje počet datových prvků. Součty všech těchto datových prvků lze také použít pro účely analýzy. |
| Laboratoř | Rozděleno | Věk (0-4, 5-14, 15+ let) / pohlaví (muž, žena) | Kombinace kategorie věk / pohlaví drasticky snižuje počet datových prvků. Součty všech těchto datových prvků lze také použít pro účely analýzy; což vám umožní zpracovat věkovou i pohlavní dimenzi a umístit je tam, kde je to požadováno. |
| Zásahy | Plochý | Nedostupné | Nejsou nutná žádná rozčlenění |
| Léčba | Plochý | Nedostupné | Několik datových prvků v této části je vzájemně podmnožinou. Vytvářet z nich součty by nemělo smysl. Tím se zvyšuje počet datových prvků, což také usnadňuje interpretaci výstupu. |
| Přerušovaná preventivní léčba v těhotenství (IPTp) | Plochý | Nedostupné | I když by se dalo argumentovat, že se zde používá kombinace kategorií, aby se vytvořil celkový počet podaných dávek, pochopení rozdělení počtu dávek podle jejich rozvrhu má přednost, proto se nepoužívá žádná kombinace kategorií. |
| Těhotná žena | Plochý | Nedostupné | Všechny datové prvky v této části mají různé definice. Nejsou nutná žádná členění. |
| Není k dispozici | Plochý | Nedostupné | Tyto datové prvky jsou typu ano / ne. Nejsou nutná žádná členění. |

#### Další datové prvky (snížení zátěže) { #additional-data-elements-burden-reduction }

Existuje celá řada dalších datových prvků, které by mohly být potenciálně použity v souboru dat o snižování zátěže malárií, avšak aktuálně k němu nejsou přiřazeny. Tyto datové prvky lze nalézt ve skupině datových prvků `Nepřiřazená malárie`.

-   Migrující a mobilní populace (MMP) pozitivní
-   Případy malárie testovány na úrovni komunity
-   Případy potvrzené malárií (Mic + RDT)
-   Plasmodium falciparum (Mic + RDT)
-   Případy malárie jsou na úrovni komunity pozitivní
-   Testováno na migrující a mobilní populaci (MMP)
-   Trasování migrující a mobilní populace (MMP) po dobu 14 dnů
-   Smíšené druhy malárie (Mic + RDT)
-   Plasmodium vivax (Mic + RDT)
-   Případy testované na malárii (Mic + RDT)
-   Případy malárie léčené na úrovni komunity
-   Smíšené / jiné druhy malárie (Mic + RDT)

### Odstranění malárie { #malaria-elimination }

Soubor údajů o eliminaci malárie je rozdělen do sedmi částí; tři z nich jsou identické se souborem údajů o snížení zátěže malárií (v seznamu označeno \*)

1. Hospitalizovaní a úmrtí na malárii 
2. Laboratoř\*
3. Vyšetřování případů
4. Léčba\*
5. Foci Investigation
6. Klasifikace ohnisek a reakce
7. Není skladem\*

Toto je měsíční soubor dat určený pro oblasti, kde je prioritou eliminace malárie.

| Sekce | Aplikovaná struktura | Rozčlenění | Odůvodnění |
| :-- | :-- | :-- | :-- |
| Hospitalizovaní a úmrtí na malárii  | Rozděleno | Věk (0-4, 5-14, 15+ let) | Kombinace věkových kategorií snižuje počet datových prvků. Pro účely analýzy lze také použít součty pro dva datové prvky. |
| Laboratoř | Rozděleno | Věk (0-4, 5-14, 15+ let) / pohlaví (muž, žena) | Kombinace kategorie věk / pohlaví drasticky snižuje počet datových prvků. Součty všech těchto datových prvků lze také použít pro účely analýzy. |
| Vyšetřování případů | Rozděleno | Věk (0-4, 5-14, 15+ let) / pohlaví (muž, žena) | Kombinace kategorie věk / pohlaví drasticky snižuje počet datových prvků. Součty všech těchto datových prvků lze také použít pro účely analýzy. |
| Léčba | Plochý | Nedostupné | Několik datových prvků v této části je vzájemně podmnožinou. Vytvářet z nich součty by nemělo smysl. Tím se zvyšuje počet datových prvků, což také usnadňuje interpretaci výstupu. |
| Foci Investigation | Plochý | Nedostupné | Několik datových prvků v této části je vzájemně podmnožinou. Vytvářet z nich součty by nemělo smysl. Tím se zvyšuje počet datových prvků, což také usnadňuje interpretaci výstupu |
| Klasifikace ohnisek a reakce |  | Klasifikace ohnisek (aktivní, zbytková, vyčištěná) | Kombinace kategorií klasifikace ohnisek umožňuje zjednodušenou klasifikaci datových prvků na základě 3 možností kategorií ohnisek. Součet této kombinace kategorií při použití na datové prvky je také užitečný pro analýzu. |
| Není k dispozici | Plochý | Nedostupné | Tyto datové prvky jsou typu ano / ne. Nejsou nutná žádná členění. |

#### Další datové prvky (eliminace) { #additional-data-elements-elimination }

Existuje celá řada dalších datových prvků, které by mohly být potenciálně použity v datové sadě pro eliminaci malárie, avšak aktuálně jí nejsou přiřazeny. Tyto datové prvky lze nalézt ve skupině datových prvků `Nepřiřazená malárie`.

-   Malárie testována přes hranice
-   Případy malárie oznámené v časovém rámci (N1) pokynu (24 hodin)
-   Případy malárie vyšetřované v (N2)\* časovém rámci směrnice
-   Malárie pozitivní z přeshraničních oblastí sledována po dobu 14 dnů
-   Pozitivní na malárii z přeshraničních území
-   Jiné druhy malárie (mikroskopie)

## Pravidla pro ověřování malárie { #malaria-validation-rules }

Pravidla pro ověřování malárie jsou rozdělena do tří skupin:

1. Malárie: snížení zátěže
2. Malárie: eliminace
3. Malárie: jiné

Program malárie se skládá z mnoha ověřovacích pravidel v rámci těchto tří skupin. Podrobný popis těchto pravidel naleznete zde:

-   [Snížení zátěže malárií](https://who.dhis2.net/webdocs/malaria/malaria_elimination_reference.html)
-   [Eliminace malárie](https://who.dhis2.net/webdocs/malaria/malaria_elimination_reference.html)

## Výstupy malárie { #malaria-outputs }

Mezi výstupy malárie zahrnuté v agregovaném balíčku patří:

-   Indikátory malárie
-   Analytické výstupy malárie
    -   Grafy
    -   Kontingenční tabulky
    -   Mapy
-   Ovládací panely malárie
    -   Snížení zátěže malárií
    -   Odstranění malárie
    -   Kontrola kvality malárie

Podrobný přehled těchto položek, včetně jejich názvů a popisů, najdete v referenční příručce _Malaria metadata reference._ Jsou k dispozici zde:

-   [Snížení zátěže malárií](https://who.dhis2.net/webdocs/malaria/malaria_elimination_reference.html)
-   [Eliminace malárie](https://who.dhis2.net/webdocs/malaria/malaria_elimination_reference.html)
