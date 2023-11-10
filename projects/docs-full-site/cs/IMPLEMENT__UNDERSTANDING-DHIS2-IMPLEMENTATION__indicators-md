---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/indicators.md"
revision_date: "2021-06-14"
---

# Indikátory { #indicators }

Tato kapitola se zabývá následujícími tématy:

- Co je indikátor

- Účel indikátorů

- Sběr dat na základě indikátorů

- Správa indikátorů v DHIS2

Následující text popisuje tato témata podrobněji.

## Co je indikátor? { #what-is-an-indicator }

V DHIS2 je indikátor klíčovým prvkem analýzy dat. Indikátor je vypočítaný vzorec založený na kombinaci datových prvků, možností kategorií, případně konstant a faktoru. Existují dva typy indikátorů, ty se jmenovatelem a ty, které jmenovatele nemají. Vypočítané součty, které mohou být složeny z více datových prvků, nemají jmenovatele. Indikátory pokrytí (poměry, procenta atd.) Se skládají ze dvou vzorců datových prvků, jeden představuje čitatele a druhý představuje jmenovatele.

Indikátory jsou tedy tvořeny vzorci datových prvků a dalších komponent a jsou vždy násobeny faktorem (např. 1, 100, 100, 100 000). Faktor je v podstatě číslo, které se vynásobí výsledkem čitatele děleného jmenovatelem. Konkrétním příkladem je ukazatel „Pokrytí BCG <1 rok“ je definován vzorcem s faktorem 100 (pro získání procenta), čitatelem („dávky BCG podávané dětem do 1 roku“) a jmenovatelem ( "Cílová populace do 1 roku"). Ukazatel "míra výpadků DPT1 až DPT3" je vzorec 100 % x ("podané dávky DPT1" - "podané dávky DPT3") / ("podané dávky DPT1").

Tabulka: Příklady indikátorů

| Indikátor | Vzorec | Čitatel | Jmenovatel | Faktor |
| --- | --- | --- | --- | --- |
| Plně imunizovaní <1 rok | Plně imunizováno / Populace < 1 rok x 100 | Plně imunizováno | Populace < 1 | 100 (procento) |
| Úmrtnost matek | Úmrtí matek / živě narození x 100 000 | Mateřská úmrtí | Živě narozené | 100 000 (MMR se měří na 100 000) |
| Kumulativní počet osob zapsaných do péče | Kumulativní počet osob zapsaných do péče x 1 | Kumulativní počet zapsaných do péče (muž, věk<18) +Kumulativní počet zapsaných do péče (muž, věk 18+) +Kumulativní počet zapsaných do péče (žena, věk<18) +Kumulativní počet zapsaných do péče (žena, věk 18+) | Žádný | 1 |

## Účel indikátorů { #purpose-of-indicators }

Indikátory, které jsou definovány čitateli i jmenovateli, jsou obvykle pro analýzu užitečnější. Jelikož se jedná o proporce, jsou srovnatelné napříč časem a prostorem, což je velmi důležité, protože jednotky analýzy a srovnání, například okresy, se liší velikostí a časem se mění. Okres s populací 1000 lidí může mít méně případů dané choroby než okres s populací 10 000. Hodnoty výskytu dané choroby však budou srovnatelné mezi oběma okresy z důvodu použití příslušných populací pro každý okres.

Indikátory tak umožňují srovnání a jsou hlavním nástrojem pro analýzu dat. DHIS2 by měl poskytovat relevantní indikátory pro analýzu pro všechny zdravotní programy, nejen pro nezpracovaná data. Většina modulů zpráv v DHIS2 podporuje datové prvky i indikátory a můžete je také kombinovat ve vlastních sestavách.

## Sběr dat na základě indikátorů { #indicator-driven-data-collection }

Protože indikátory jsou vhodnější pro analýzu ve srovnání s datovými prvky, měl by být hlavní hnací silou pro sběr údajů výpočet indikátorů. Obvyklou situací je, že se shromažďuje velké množství dat, ale nikdy se nepoužije v žádném indikátoru, což významně snižuje použitelnost dat. Zachycené datové prvky by měly být zahrnuty do indikátorů používaných pro správu, nebo by pravděpodobně neměly být shromažďovány vůbec.

Pro účely implementace by měl být definován a implementován seznam indikátorů používaných pro správu v DHIS2. Pro účely analýzy by se školení mělo zaměřit na používání indikátorů a na to, proč jsou pro tento účel vhodnější než datové prvky.

## Správa indikátorů { #managing-indicators }

Indikátory lze v DHIS2 kdykoli přidat, odstranit nebo upravit, aniž by to mělo vliv na data. Indikátory se neukládají jako hodnoty v DHIS2, ale jako vzorce, které se počítají, kdykoli je uživatel potřebuje. Změna vzorců tedy povede pouze k tomu, že při použití indikátoru pro analýzu budou požadovány různé datové prvky, aniž by došlo ke změnám hodnot podkladových dat. Informace o správě indikátorů najdete v kapitole o indikátorech v uživatelské dokumentaci DHIS2.
