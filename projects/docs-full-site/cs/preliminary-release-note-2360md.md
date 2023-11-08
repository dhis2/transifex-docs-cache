# Poznámka k verzi DHIS verze 2.36

Tento dokument zdůrazňuje klíčové vlastnosti počátečního vydání DHIS2 verze 2.36. Tato verze je plně kompatibilní s aplikací DHIS2 [Android Capture App](https://www.dhis2.org/android-2-4) verze 2.4.


## ANALYTICKÉ VLASTNOSTI



  - *Přiblížení* kliknutím a tažením kurzoru přes oblast, kterou chcete přiblížit. To je často nutné, abyste viděli více podrobností v oblastech, kde je seskupeno mnoho organizačních jednotek.
  - *Detekce odlehlých hodnot* lze provést buď pomocí standardního z-skóre, upraveného z-skóre nebo mezikvartilového rozsahu prostřednictvím nabídky možností. Lze také použít extrémní svislou (osa y) a vodorovnou (osa x) prahovou čáru. S podporou WHO se jedná o velmi jasný a účinný způsob identifikace odlehlých hodnot, které často představují problémy s kvalitou dat. Odlehlé hodnoty, které s největší pravděpodobností vyhodí národní statistiky, můžete identifikovat pomocí detekce odlehlé hodnoty v kombinaci s extrémními prahovými hodnotami X a Y.

[Screenshot]() | [Docs]()

**Režim prezentace na celou obrazovku položky oblídacího panelu:** Rozbalte libovolnou položku na panelu (graf, mapa nebo kontingenční tabulka) na velikost celé obrazovky. To je skvělé pro prezentaci dat na virtuálních nebo osobních schůzkách přímo z ovládacího panelu.

[Screenshot]() | [Docs]()

**Legendy sloupcového a pruhového grafu:** Změňte barvu pruhu nebo sloupce na základě předdefinované legendy. To usnadňuje zvýraznění nedostatečného a nadměrného výkonu pomocí pruhových a sloupcových grafů.

[Screenshot]() | [Docs]()



[Screenshot]() | [Docs]()



[Screenshot]() | [Docs]()



[Screenshot]() | [Docs]()



[Screenshot]() | [Docs]()



[Screenshot]() | [Docs]()


## VLASTNOSTI TRASOVÁNÍ A UDÁLOSTÍ



[Jira]()



[]() | [Jira]()



[Dokumenty]() | [Jira]()

## VLASTNOSTI PLATFORMY







[Docs]()



[](https://jira.dhis2.org/browse/DHIS2-5587)



[Jira](https://jira.dhis2.org/browse/DHIS2-8089)



[Docs]()



[Docs]()

**Výkon kontroly integrity dat:** Výkon kontrol integrity dat (v aplikaci pro správu dat) byl vylepšen a probíhá mnohem rychleji.

[Docs]()

**Zakázat provádění programových pravidel:** V `dhis.conf` je k dispozici nová konfigurační vlastnost pro zakázání/povolení provádění programových pravidel na straně serveru.

[Docs]()

## VLASTNOSTI API



[](https://jira.dhis2.org/browse/DHIS2-102579)

**Sledování hodnoty dat:** Pro označení hodnot dat pro sledování je k dispozici nový koncový bod.

[Dokumenty](https://docs.dhis2.org/master/en/dhis2_developer_manual/web-api.html#follow-up)

**Časové pásmo serveru:** Informace o časovém pásmu serveru jsou přidány do koncového bodu `/api/system/info`.

[Docs]()

**Odstranit výsledky ověření:** Pro odstranění výsledků ověření je k dispozici nový koncový bod.



## INFORMACE O VYDÁNÍ


|Informace o vydání|Odkaz|
| --- | --- |
|Stáhněte si verzi a ukázkovou databázi|https://www.dhis2.org/downloads|
|Dokumentace|[https://www.dhis2.org/documentation](https://docs.dhis2.org/)|
|Poznámky k upgradu|[Poznámky k upgradu na GitHubu](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Podrobnosti o jednotlivých funkcích JIRA||
|Přehled opravených chyb na JIRA||
|Zdrojový kód na Githubu|https://github.com/dhis2|
|Ukázková instance|https://play.dhis2.org/2.36/|
|Docker||
|Komunita DHIS 2|https://community.dhis2.org/|
