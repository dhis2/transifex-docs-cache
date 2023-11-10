---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.35/src/user/configure-the-gis-app.md"
revision_date: "2021-06-14"
---

# Nakonfigurujte aplikaci Mapy { #gis_creating }

## Kontext { #gis_creating_context }

Nastavení map jednoduše znamená uložení souřadnic organizačních jednotek, které chcete zobrazit na mapě v databázi. Souřadnice jsou často distribuovány v proprietárních formátech a bude nutné je převést do formátu, kterému DHIS2 rozumí. Soubory ESRI shapefiles jsou nejběžnějším formátem vektorových geoprostorových dat pro desktopové aplikace. Tvarové soubory pro vaši zemi najdete [zde](http://www.diva-gis.org/gdata) nebo v mnoha dalších úložištích geoprostorových dat na webu. Aby bylo možné tyto souřadnice v DHIS2 GIS použít, je třeba udělat určité množství práce, konkrétně transformovat data do vhodného formátu a zajistit, aby se názvy obsažené v geoprostorových datech přesně shodovaly se jmény organizačních jednotek, do kterých by měly být uzavřeny.

V současné době lze pomocí aplikace Údržba upravovat pouze organizační jednotky s typy geometrie BOD. Chcete-li upravit geometrie POLYGON, použijte funkci importu GML.

Chcete-li upravit souřadnice BODU organizační jednotky, otevřete aplikaci Údržba a přejděte do sekce Organizační jednotka. Klikněte na organizační jednotku, kterou chcete zobrazit nebo upravit, v levé části obrazovky můžete vyhledat nebo filtrovat seznam. Jakmile je vybrána organizační jednotka, můžete upravit hodnoty **Zeměpisná šířka** a **Zeměpisná délka** a aktualizovat tak BODOVÉ souřadnice. Pokud má organizační jednotka POLYGONOVOU geometrii, nelze souřadnice upravovat.

Pokud se chystáte přidat nebo aktualizovat souřadnice pro velký počet jednotek, nebo pokud potřebujete aktualizovat geometrie polygonů, měli byste použít automatický import GML. Následující část vysvětluje, jak provést import GML.

> **Důležité**
>
> Jediným souřadnicovým referenčním systémem podporovaným DHIS2 je EPSG:4326, známý také jako zeměpisná délka / šířka. Souřadnice musí být uloženy tak, aby zeměpisná šířka (poloha východ / západ) pokračovala směrem k zeměpisné šířce (poloha sever / jih). Pokud jsou vaše vektorová data v jiném CRS než EPSG 4326, budete muset před importem do DHIS2 nejprve konvertovat data.

## Import souřadnic { #gis_creating_setup }

Krok 1 - Zjednodušte / zobecněte své geografické údaje

Hranice v souborech geografických dat jsou obvykle velmi přesné, příliš velké pro potřeby webového GIS. To obvykle nemá vliv na výkon při používání souborů GIS v místním systému, ale je obvykle nutné optimalizovat geografická data pro webový GIS systém DHIS2. Všechna geografická data je třeba stáhnout ze serveru a vykreslit v prohlížeči, takže pokud jsou data příliš složitá, bude výkon DHIS2 GIS negativně ovlivněn. Tento optimalizační proces lze popsat takto:

Souřadnice: Počet platných desetinných míst (např. 23.02937874993774) by měl být zkrácen na méně číslic (např. 23.03). Ačkoli to bude mít za následek určité nepřesnosti na mapě, vzhledem k obvyklému měřítku, ve kterém jsou mapy v DHIS2 vytvářeny (\> 1:50 000), by ztráta přesnosti neměla být patrná. Normálně by za desetinnou čárkou neměly být nutné více než čtyři platné číslice., Polygony: Kromě zkrácení počtu platných číslic by měl být skutečný počet bodů také snížen na optimální úroveň. Nalezení této optimální úrovně může vyžadovat trochu experimentování. Snížení přesnosti bodů i počtu bodů zobecněním povede k degradaci polygonu. Po trochu experimentování však lze nalézt optimální úroveň zobecnění, kde je přesnost polygonu vizuálně přijatelná a výkonnost GIS je optimální.

U polygonů musíme omezit hraniční čáry méně podrobné odstraněním některých bodů čar. Než začnete, vytvořte si zálohu svých obrazců. Jednou z možných metod je použití [MapShaper](http://www.mapshaper.org/), což je online nástroj, který lze použít ke zobecnění geografických dat. Chcete-li použít MapShaper, jednoduše nahrajte svůj shapefile na web. Potom uprostřed dole uvidíte posuvník, který začíná na 0%. Obvykle je přijatelné přetáhnout jej až na přibližně 80%. V levé nabídce můžete zaškrtnout možnost „zobrazit původní řádky“ a porovnat výsledek. Možná budete chtít vyzkoušet jinou metodu zjednodušení. Pokud jste s výsledkem spokojeni, klikněte na „exportovat“ v pravém horním rohu. Pak zkontrolujte první ze čtyř možností s názvem "Shapefile - polygony", klikněte na "vytvořit" a počkejte, až se objeví tlačítka pro stažení. Nyní si stáhněte tyto dva soubory do místního počítače a přepište ty stávající. Přejděte na další krok s vaším novým zjednodušeným souborem shapefile.

Krok 2 - Převeďte soubor shapefile na GML

Doporučený nástroj pro převody geografického formátu se nazývá „ogr2ogr“. To by mělo být k dispozici pro většinu distribucí Linuxu `sudo apt-get install gdal-bin`. Ve Windows přejděte na <http://fwtools.maptools.org/> a stáhněte si „FWTools“, nainstalujte jej a otevřete příkazový shell FWTools. Během převodu formátu chceme také zajistit, aby výstup měl správnou souřadnicovou projekci (zvanou EPSG:4326 s geografickou délkou a šířkou). Podrobnější odkaz na zeměpisné souřadnice najdete na této [stránce] (http://www.epsg-registry.org/). Pokud jste již geograficky promítli geografická data do systému zeměpisné šířky a délky (EPSG:4326), není třeba explicitně definovat výstupní souřadnicový systém za předpokladu, že `ogr2ogr` může určit vstupní prostorový referenční systém. Všimněte si, že většina tvarových souborů používá systém EPSG:4326. Prostorový referenční systém můžete určit provedením následujícího příkazu.

    ogrinfo -al -so filename.shp

Za předpokladu, že projekce je označena jako EPSG:27700 programem `ogrinfo`, můžeme ji převést na EPSG:4326 provedením následujícího příkazu.

    ogr2ogr -s_srs EPSG:27700 -t_srs EPSG:4326 -f GML filename.gml filename.shp

Pokud jsou geografická data již v EPSG:4326, můžete jednoduše transformovat shapefile na GML provedením následujícího příkazu.

    ogr2ogr -f GML filename.gml filename.shp

Vytvořený soubor GML najdete ve stejné složce jako shapefile.

Krok 3 - Připravte soubor GML

Soubor GML bohužel ještě není připraven k importu. Otevřete jej v robustním textovém editoru, jako je Geany (Linux) nebo Notepad++ (Windows). GML je formát založený na XML, což znamená, že poznáte běžnou hierarchii značek XML. V souboru GML je organizační jednotka reprezentována jako \<gml:featureMember\>. Uvnitř členů prvku obvykle najdeme spoustu atributů, ale my importujeme jen jejich souřadnice.

Aby bylo možné importovat geoprostorová data z členů prvku vstupu GML, musí DHIS2 každé z nich porovnat s organizační jednotkou ve své databázi. Jinak řečeno, prvek prvku prvku musí obsahovat odkaz na jeho odpovídající organizační jednotku. Samotná reference musí být jedním ze tří možných identifikátorů DHIS2: **uid**, **code** nebo **name**. Identifikátor výběru musí být poskytnut jako vlastnost pro každý prvek prvku prvku. Dovozce bude hledat vlastnost s místním názvem _Uid_, _Code_ nebo _Name_, např. "ogr:Name" nebo „anyPrefix:Code“.

Pokud členové vašeho prvku již obsahují vlastnost identifikátoru, který chcete použít (například název oblasti), můžete použít vyhledávání a nahrazení v textovém editoru k přejmenování těchto prvků na název, který DHIS2 rozpozná (viz tabulka níže) . Obvykle se jedná o pracovní postup, který je použitelný při použití názvu jako identifikátoru (zdrojový shapefile soubor nebo dokonce GML obvykle obsahuje název každé oblasti, kterou definuje).

<table>
<caption> identifikátory organizační jednotky podporované pro import GML </caption>
<thead>
<tr class="header">
<th> Odpovídající priorita </th>
<th> Identifikátor </th>
<th> Platný zápis písmen </th>
<th> Garantovaná jedinečnost </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td> 1 </td>
<td> Uid </td>
<td> uid, Uid, UID </td>
<td> Ano </td>
</tr>
<tr class="even">
<td> 2 </td>
<td> Kód </td>
<td> kód, kód, KÓD </td>
<td> Ne </td>
</tr>
<tr class="odd">
<td> 3 </td>
<td> Název </td>
<td> name, Name, NAME </td>
<td> Ne </td>
</tr>
</tbody>
</table>

V případě přejmenování vlastností by se obvykle našla značka s názvem něco jako „ogr:DISTRICT_NAME“, „ogr:NAME_1“ a přejmenovala by se na „ogr:Name“. Pokud používáte identifikátory _code_ nebo _uid_ na druhé straně, vyhledání správných hodnot v databázi DHIS2 a procházení souboru GML může být nutné přidat vlastnosti pro každého příslušného člena prvku. V každém z případů je důležité si uvědomit, že použitý identifikátor musí **jednoznačně** identifikovat organizační jednotku (např. pokud jsou v databázi se stejným názvem nebo kódem dvě organizační jednotky, nelze je správně párovat) . Protože _uid_ je jediný zaručeně jedinečný identifikátor, je to nejrobustnější volba. Vzhledem k tomu, že shoda názvu je obvykle jednodušší (vzhledem k tomu, že název je již součástí vašich dat), životaschopným přístupem k řešení konfliktů jedinečnosti může být shoda s libovolnými organizačními jednotkami, které nejsou pojmenovány jednoznačně, na jiném identifikátoru (nejlépe uid) a zbytek na jejich jménech.

Jak je vidět ve výše uvedené tabulce, existuje priorita shody, což znamená, že jsou k dispozici dva nebo více identifikátorů pro stejného člena prvku, shoda bude provedena na identifikátoru s nejvyšší prioritou. Všimněte si také platných vlastností, které lze ve vašem GML použít. Předpona oboru názvů není důležitá, protože se používá pouze místní název.

Častým úskalím provádění přípravy souborů GML jsou chyby při pojmenovávání syntaxí nebo prvků. Proto se prosím ujistěte, že jsou všechny vlastnosti souboru GML spuštěny a ukončeny správně odpovídajícími značkami. Také se ujistěte, že vlastnosti sledují jedno z daných platných pravopisů názvu vlastnosti. Identifikační vlastnosti mají vypadat např. \<ogr:Name\>okres Moyamba\</ogr:Name\>, \<somePrefix:uid\>x7uuia898nJ\</somePrefix:uid\> nebo \<CODE\>OU_12345\</CODE\> Další běžnou chybou není zajištění toho, aby se identifikátor přesně shodoval, zvláště při použití vlastnosti _name_. Všechny shody se provádějí na přesných hodnotách, což znamená, že výraz „Moyamba“ ve zdrojovém souboru GML by nebyl porovnán s výrazem „okres Moyamba“ v databázi.

Stručně se podívejte na identifikátory a porovnejte je s odpovídajícími hodnotami v databázi. Pokud se zdá, že se docela dobře shodují, je na čase provést náhled v modulu import-export.

Přejděte na Služby -\> Import-Export, vyberte "Náhled", vyberte soubor GML a klikněte na "Importovat". Hledejte nové / aktualizované organizační jednotky. Naším záměrem je přidat souřadnice k již existujícím organizačním jednotkám v databázi, takže chceme co nejvíce aktualizací a 0 nových. Ty, které jsou uvedeny jako nové, budou vytvořeny jako kořenové jednotky a zkazí stromy organizačních jednotek v DHIS2. Pokud jsou některé uvedeny jako nové, klikněte na jejich číslo a příslušné organizační jednotky se zobrazí v níže uvedeném seznamu. Pokud ve srovnání s názvy organizačních jednotek v databázi dojde k mírnému překlepu, opravte je a proveďte náhled znovu. Jinak klikněte na tlačítko „zahodit vše“ pod seznamem a poté na tlačítko „Importovat vše“ nad seznamem.

Pokud se proces importu úspěšně dokončí, měli byste nyní být schopni využívat geografická data v DHIS2 GIS. Pokud ne, zkontrolujte rady a vyhledejte běžné chyby, jako například:

\-  duplikáty názvu v souboru GML. Sloupec s názvy v databázi je jedinečný a nepřijímá dvě organizační jednotky se stejným názvem.

\ - Sloupec "krátký název" v tabulce organizační jednotky ve vaší databázi má příliš malou definici varchar. Zvyšte jej na 100.

\- Speciální znaky názvu v souboru GML. Nezapomeňte je převést na odpovídající ekvivalenty XML nebo řídicí sekvence.

\- Špatně naformátovaný vstupní GML, neodpovídající značky
