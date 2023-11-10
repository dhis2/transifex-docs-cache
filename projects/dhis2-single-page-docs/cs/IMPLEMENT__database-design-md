---
revision_date: "2021-09-15"
template: single.html
---

# Kvalita dat { #data-quality }

Tato kapitola pojednává o různých aspektech souvisejících s kvalitou dat.

## Měření kvality dat { #measuring-data-quality }

Jsou data úplná? Je shromažďováno včas? Je to správně? Toto jsou otázky, které je třeba položit při analýze dat. Špatná kvalita dat může mít mnoho podob; nejen nesprávné údaje, ale také nedostatek úplnosti nebo příliš stará data (pro smysluplné použití).

## Důvody špatné kvality dat { #reasons-for-poor-data-quality }

Existuje mnoho možných důvodů pro nekvalitní data, včetně:

- Nadměrné vybrané množství; příliš mnoho údajů, které se mají shromáždit, vede ke kratší době a „zkratkám“ k dokončení hlášení

- Mnoho manuálních kroků; pohyblivé postavy, shrnutí atd. mezi různými papírovými formuláři

- Nejasné definice; nesprávná interpretace vyplňovaných polí

- Nedostatečné využívání informací: žádná pobídka ke zlepšování kvality

- Fragmentace informačních systémů; může vést ke zdvojení hlášení

## Zlepšení kvality dat { #improving-data-quality }

Zlepšení kvality dat je dlouhodobý úkol a mnoho opatření má organizační povahu. Kvalita dat by však měla být problémem od začátku jakéhokoli procesu implementace a existují věci, které lze řešit najednou, například kontroly v DHIS2. Některá důležitá opatření ke zlepšení kvality dat jsou:

- Změny formulářů pro sběr dat, harmonizace formulářů

- Podporovat využití informací na místní úrovni, kde se shromažďují údaje

- Vývoj rutin kontroly kvality dat

- Zahrňte do školení kvalitu dat

- Implementujte kontroly kvality dat v DHIS2

## Použití DHIS2 ke zlepšení kvality dat { #using-dhis2-to-improve-data-quality }

DHIS2 má několik funkcí, které mohou pomoci při zlepšování kvality dat; validace během zadávání dat, aby se zajistilo, že jsou data zachycena ve správném formátu a v přiměřeném rozsahu, uživatelsky definovaná pravidla pro ověřování založená na matematických vztazích mezi zachycenými daty (např. mezisoučty vs. součty), funkce odlehlé analýzy a zprávy o pokrytí a úplnost údajů. Více nepřímo přispívá několik principů návrhu DHIS2 ke zlepšení kvality dat, například myšlenka harmonizace dat do jednoho integrovaného datového skladu, podpora přístupu na úrovni dat k datům a analytickým nástrojům na místní úrovni a nabídka široké škály nástrojů pro analýzu dat a šíření. Díky strukturovanějším a harmonizovanějším procesům sběru dat a silnějšímu využívání informací na všech úrovních se kvalita dat zlepší. Zde je přehled funkcí, které přímo cílí na kvalitu dat:

### Ověření vstupu dat { #data-input-validation }

Nejzákladnějším typem kontroly kvality dat v DHIS2 je zajistit, aby zachycená data byla ve správném formátu. DHIS2 dá uživatelům zprávu, že zadaná hodnota není ve správném formátu a neuloží hodnotu, dokud nebude změněna na přijatelnou hodnotu. Např. text nelze zadat do číselného pole. Různé typy datových hodnot podporovaných v DHIS2 jsou vysvětleny v uživatelské příručce v kapitole o datových prvcích.

### Minimální a maximální rozsahy { #min-and-max-ranges }

Pro zamezení psaní chyb během zadávání dat (např. psaní „1000“ místo „100“), DHIS2 zkontroluje, zda je zadávaná hodnota v rozumném rozsahu. Tento rozsah je založen na dříve shromážděných datech stejného zdravotnického zařízení pro stejný datový prvek a skládá se z minimální a maximální hodnoty. Jakmile uživatel zadá hodnotu mimo, bude uživatel upozorněn, že hodnota není přijata. Aby bylo možné vypočítat přiměřené rozsahy, potřebuje systém nejméně šest měsíců (období) dat.

### Pravidla ověřování { #validation-rules }

Pravidlo ověření je založeno na výrazu, který definuje vztah mezi řadou datových prvků. Výraz má levou a pravou stranu a operátor, který definuje, zda první musí být menší než, rovný nebo větší než druhý. Výraz tvoří podmínku, která by měla tvrdit, že jsou splněna určitá logická kritéria. Například validační pravidlo by mohlo tvrdit, že celkový počet vakcín podaných kojencům je menší nebo roven celkovému počtu kojenců. Levá a pravá strana musí vracet číselné hodnoty.

Pravidla ověřování lze definovat prostřednictvím uživatelského rozhraní a později je spustit pro kontrolu existujících údajů. Při spouštění ověřovacích pravidel může uživatel určit organizační jednotky a období, za která budou data kontrolována, protože spuštění kontroly všech existujících dat bude trvat dlouho a nemusí být relevantní. Po dokončení kontrol bude uživateli předložena zpráva s porušením ověřování s vysvětlením, které hodnoty dat je třeba opravit.

Kontroly pravidel ověřování jsou také zabudovány do procesu zadávání dat, takže když uživatel vyplní formulář, lze pravidla spustit a zkontrolovat data pouze v tomto formuláři před uzavřením formuláře.

### Analýza odlehlých hodnot { #outlier-analysis }

Analýza odlehlých hodnot založená na směrodatné odchylce poskytuje mechanismus pro odhalení hodnot, které jsou číselně vzdálené od zbytku dat. Odlehlé hodnoty se mohou vyskytnout náhodně, ale často označují chybu měření nebo těžce sledovanou distribuci (vedoucí k velmi vysokým číslům). V prvním případě si je přejete zahodit, zatímco v druhém případě byste měli být opatrní při používání nástrojů nebo interpretací, které předpokládají normální distribuci. Analýza je založena na standardním normálním rozdělení.

### Zprávy o úplnosti a včasnosti { #completeness-and-timeliness-reports }

Zprávy o úplnosti budou ukazovat, kolik datových souborů (formulářů) bylo odesláno organizační jednotkou a obdobím. K výpočtu úplnosti můžete použít jednu ze tří různých metod; 1) na základě tlačítka úplnosti při zadávání dat, 2) na základě sady definovaných povinných datových prvků nebo 3) na základě celkových registrovaných hodnot dat pro datovou sadu.

Zprávy o úplnosti také ukazují, které organizační jednotky v oblasti hlásí včas, a procento včasných zařízení pro hlášení v dané oblasti. Výpočet včasnosti je založen na nastavení systému s názvem Dny po skončení období, aby bylo možné včas zaslat údaje.

# Organizační jednotky { #organisation-units }

V DHIS2 je umístění dat, geografický kontext, představováno jako organizační jednotky. Organizačními jednotkami mohou být buď zdravotnické zařízení nebo oddělení / podjednotky poskytující služby, nebo správní jednotka představující geografickou oblast (např. Zdravotní obvod).

Organizační jednotky jsou umístěny v hierarchii, označované také jako strom. Hierarchie bude odrážet administrativní strukturu zdravotnictví a její úrovně. Typickými úrovněmi v takové hierarchii jsou národní, provinční, okresní a zařízení. V DHIS2 existuje jediná organizační hierarchie, takže způsob, jakým je to definováno a mapováno na realitu, vyžaduje pečlivé zvážení. Které geografické oblasti a úrovně jsou definovány v hlavní organizační hierarchii, budou mít zásadní dopad na použitelnost a výkon aplikace. Kromě toho existují způsoby řešení alternativních hierarchií a úrovní, jak je vysvětleno v části s názvem Skupiny organizačních jednotek a skupiny dále.

## Návrh hierarchie organizačních jednotek { #organisation-unit-hierarchy-design }

Proces navrhování rozumné hierarchie organizačních jednotek má mnoho aspektů:

- _Zahrnout všechna vykazující zdravotnická zařízení:_ Do systému by měla být zahrnuta všechna zdravotnická zařízení, která přispívají k národnímu sběru dat. Měla by být začleněna zařízení všech druhů vlastnictví, včetně soukromých, veřejných, nevládních organizací a zařízení zaměřených na víru. Soukromá zařízení často představují polovinu z celkového počtu zařízení v zemi a jsou jim ukládány zásady pro vykazování údajů, což znamená, že začlenění údajů z těchto zařízení je nezbytné pro získání realistických souhrnných národních údajů.

- _Zvýrazněte správní hierarchii zdravotnictví:_ Země má obvykle několik správních hierarchií, které často nejsou dobře koordinovány ani harmonizovány. Při zvažování toho, co je třeba zdůraznit při návrhu databáze DHIS2, je třeba mít na paměti, které oblasti jsou nejzajímavější a budou nejčastěji požadovány pro analýzu dat. DHIS2 primárně spravuje údaje o zdravotním stavu a provádí analýzu na základě správní administrativní struktury. To znamená, že i když je možné provést úpravy v oblastech, jako jsou finance a místní správa, výchozím bodem hierarchie organizačních jednotek DHIS2 by měly být oblasti  zdravotnické administrativy.

<!-- konec seznamu -->

- _Omezení počtu úrovní hierarchie organizačních jednotek:_ Chcete-li uspokojit požadavky na analýzu pocházející z různých organizačních orgánů, jako jsou místní samospráva a ministerstvo financí, je lákavé zahrnout všechny tyto oblasti jako organizační jednotky do databáze DHIS2. Kvůli úvahám o výkonu by se však měli pokusit omezit úrovně hierarchie organizačních jednotek na co nejmenší počet. Hierarchie se používá jako základ pro agregaci dat, která mají být prezentována v kterémkoli z nástrojů pro vykazování, takže při vytváření agregovaných dat pro vyšší úrovně musí aplikace DHIS2 hledat a sčítat data registrovaná pro všechny organizační jednotky umístěné dále dolů hierarchie. Zvýšení počtu organizačních jednotek bude mít tedy nepříznivý dopad na výkon aplikace a příliš velký počet by se v tomto ohledu mohl stát významným problémem.

  Kromě toho je ústřední část většiny analytických nástrojů v DHIS2 založena na dynamickém výběru „nadřazené“ organizační jednotky těch, které mají být zahrnuty. Například by člověk chtěl vybrat kraj  a do zprávy zahrnout okresy patřící k tomuto kraji. Pokud je úroveň okresu z hlediska analýzy nejzajímavější úrovní a existuje několik úrovní hierarchie mezi touto a úrovní kraje, bude tento druh zprávy nepoužitelný. Při vytváření hierarchie je třeba se zaměřit na úrovně, které se budou často používat v sestavách a analýze dat, a vynechat úrovně, které se zřídka nebo nikdy nepoužívají, protože to bude mít dopad na výkon i použitelnost aplikace.

- _Vyhýbejte se vzájemným vztahům jeden-k-jednomu:_ Dalším zásadním principem pro návrh hierarchie je vyhnout se spojování úrovní, které mají blízké poměry nadřazený - podřazený, což znamená, že například okres (nadřazený) by měl mít v průměru více než jednu místní radu (podřazenou) na níže uvedené úrovni, než má smysl přidat do hierarchie úroveň místní rady. Poměry nadřazený-podřazený od 1:4 nebo více jsou mnohem užitečnější pro účely analýzy dat, protože je možné začít se dívat např. jak jsou data okresu distribuována v různých podoblastech a jak se liší. Taková hloubková rozcvičení nejsou příliš užitečná, pokud má níže uvedená úroveň stejnou cílovou populaci a stejné zdravotnické zařízení sloužící nadřazeným.

  Přeskočení geografických úrovní při mapování reality do hierarchie organizačních jednotek DHIS2 může být obtížné a může snadno vést k odporu mezi určitými zúčastněnými stranami, je však třeba mít na paměti, že ve skutečnosti existují způsoby, jak vytvářet zprávy založené na geografických úrovních, které nejsou součástí organizační hierarchie v DHIS2, jak bude vysvětleno v následující části.

## Skupiny organizačních jednotek a sady skupin { #organisation-unit-groups-and-group-sets }

V DHIS2 lze organizační jednotky seskupit do skupin organizačních jednotek a tyto skupiny lze dále uspořádat do skupinových sad. Společně mohou napodobovat alternativní organizační hierarchii, kterou lze použít při vytváření sestav a dalších datových výstupů. Kromě reprezentace alternativních geografických poloh, které nejsou součástí hlavní hierarchie, jsou tyto skupiny užitečné pro přiřazování klasifikačních schémat zdravotnickým zařízením, např. na základě typu nebo vlastnictví zařízení. Prostřednictvím uživatelského rozhraní lze v aplikaci definovat libovolný počet skupin a skupin a všechny jsou definovány lokálně pro každou databázi DHIS2.

To nejlépe ilustruje příklad: Typicky by člověk chtěl poskytnout analýzu založenou na vlastnictví zařízení. V takovém případě by se vytvořila skupina pro každý typ vlastnictví, například „MZ“, „Soukromé“ a „Nevládní organizace“. Všechna zařízení v databázi musí být poté klasifikována a přiřazena k jedné a pouze jedné z těchto tří skupin. Dále by se vytvořila skupina nazvaná „Vlastnictví“, ke které jsou přiřazeny tři výše uvedené skupiny, jak je znázorněno na obrázku níže.

![](resources/images/organisation_unit_hiearchy.png)

Podobným způsobem lze vytvořit sadu skupin pro další úroveň správy, např. místní rady. Všechny místní rady musí být definovány jako skupiny organizačních jednotek a poté přiřazeny do sady skupin zvané „Místní rada“. Posledním krokem je pak přiřazení všech zdravotnických zařízení k jedné a pouze jedné ze skupin místní rady. To umožňuje DHIS2 vytvářet souhrnné zprávy každou místní radou (sčítání dat pro všechna přiřazená zdravotnická zařízení), aniž by bylo nutné zahrnout úroveň místní rady do hlavní organizační hierarchie. Stejný přístup lze použít pro jakoukoli další administrativní nebo geografickou úroveň, která je potřeba, s jednou skupinou nastavenou na další úroveň. Před pokračováním a návrhem v DHIS2 je třeba zmapovat oblasti další geografické úrovně a zdravotnická zařízení v každé oblasti.

Klíčovou vlastností konceptu skupinové sady v DHIS2 je _exkluzivita_, což znamená, že organizační jednotka může být členem přesně jedné ze skupin ve skupinové sadě. Porušení tohoto pravidla by vedlo k duplikaci dat při agregaci dat zdravotnických zařízení různými skupinami, protože zařízení přiřazené dvěma skupinám ve stejné skupinové sadě by se započítávalo dvakrát.

S touto strukturou může DHIS2 poskytovat agregovaná data pro každý z typů vlastnictví organizačních jednotek prostřednictvím zprávy „Sestava skupiny organizačních jednotek“ v modulu „Zprávy“ nebo prostřednictvím nástroje třetí strany v kontingenční tabulce. Lze například zobrazit a porovnat míry využití, agregované podle různých typů vlastnictví (např. Ministerstvo zdravotnictví, soukromý, nevládní organizace). Kromě toho může DHIS2 poskytovat statistiky distribuce zařízení v „Zpráva o distribuci organizační jednotky“ v modulu „Zprávy“. Například je možné zobrazit, kolik zařízení existuje v rámci dané organizační jednotky v hierarchii pro každý z různých typů vlastnictví. V modulu GIS, vzhledem k tomu, že v systému byly registrovány souřadnice zdravotnických zařízení, lze zobrazit umístění různých typů zdravotnických zařízení (s různými symboly pro každý typ) a také kombinovat tyto informace s další mapovou vrstvou zobrazující indikátory, např. podle okresů.

# Datové prvky a vlastní dimenze { #data-elements-and-custom-dimensions }

Tato kapitola nejprve pojednává o důležitém stavebním prvku systému: datovém prvku. Za druhé pojednává o modelu kategorie a o tom, jak jej lze použít k dosažení vysoce přizpůsobené struktury metadat pro ukládání dat.

## Datové prvky { #data-elements }

Datový prvek je společně s organizační jednotkou nejdůležitějším stavebním kamenem databáze DHIS2. Představuje dimenzi _co_ a vysvětluje, co se shromažďuje nebo analyzuje. V některých kontextech se to označuje jako indikátor, ale v DHIS2 se tento meta-datový prvek sběru a analýzy dat označuje jako datový prvek. Datový prvek často představuje počet některých událostí a jeho název popisuje, co se počítá, např. „Podané dávky BCG“ nebo „Případy malárie“. Když jsou data shromažďována, ověřována, analyzována nebo prezentována, jsou to datové prvky nebo výrazy vytvořené s datovými prvky, které popisují, pro jaký jev, událost nebo případ jsou data registrována. Proto se datové prvky stávají důležitými pro všechny aspekty systému a rozhodují nejen o tom, jak jsou data sbírána, ale ještě důležitější je, jak jsou data reprezentována v databázi a jak lze data analyzovat a prezentovat.

Důležitým principem při navrhování datových prvků je myslet na datové prvky jako na samostatný popis jevu nebo události a nikoli jako na pole ve formuláři pro zadávání dat. Každý datový prvek žije v databázi samostatně, zcela odděleně a nezávisle na formuláři kolekce. Je důležité vzít v úvahu, že datové prvky se používají přímo v sestavách, grafech a dalších nástrojích pro analýzu dat, ve kterých kontext v daném formuláři pro zadávání dat není přístupný ani relevantní. Jinými slovy musí být možné jasně určit, jakou událost datový prvek představuje, pouze při pohledu na jeho název. Na základě toho lze odvodit obecné pravidlo, které říká, že název datového prvku musí být schopen samostatně stát a popsat hodnotu dat i mimo kontext jeho kolekce.

Například datový prvek zvaný „malárie“ může být výstižný, je-li vidět ve formuláři pro zadávání údajů, který zachycuje údaje o očkování, ve formě, která zachycuje zásoby očkování, a ve formě pro údaje o ambulantních pacientech. Při zobrazení v sestavě je však mimo kontext formuláře pro zadávání dat nemožné rozhodnout, jakou událost tento datový prvek představuje. Pokud by se datový prvek nazýval „případy malárie“, „přijaté dávky zásob malárie“ nebo „podané dávky malárie“, bylo by z pohledu uživatele jasné, co se zpráva snaží vyjádřit. V tomto případě máme co do činění se třemi různými datovými prvky se zcela odlišnou sémantikou.

## Kategorie a vlastní dimenze { #categories-and-custom-dimensions }

Určité požadavky na sběr dat vyžadují podrobný rozpis dimenze popisující počítanou událost. Například bychom chtěli shromáždit počet „případů malárie“ rozdělených podle pohlaví a věkových skupin, například „žen“, „mužů“ a „\< 5 let” a “\> 5 let“. Charakterizuje to to, že rozdělení se obvykle opakuje pro řadu „základních“ datových prvků: Například bychom chtěli toto rozdělení znovu použít pro další datové prvky, jako jsou „TB“ a „HIV“. Aby byla metadata dynamičtější, znovu použitelná a vhodná pro analýzu, má smysl definovat zmíněné nemoci jako datové prvky a vytvořit samostatný model pro atributy rozdělení. Toho lze dosáhnout použitím modelu kategorie, který je popsán v následujícím textu.

Model kategorie má tři hlavní prvky, které je nejlépe popsat pomocí výše uvedeného příkladu:

1.  Možnost kategorie, která odpovídá „ženám“, „mužům“ a „\< 5 let” a “\> 5 let“.

2.  Kategorie, která odpovídá „pohlaví“ a „věkové skupině“.

3.  Kombinace kategorií, která by měla být ve výše uvedeném příkladu pojmenována „pohlaví a věková skupina“ a měla by jí být přiřazena obě výše zmíněné kategorie.

Tento model kategorie je ve skutečnosti samostatný, ale je v DHIS2 volně spojený s datovým prvkem. Volně spojený v tomto ohledu znamená, že existuje asociace mezi kombinací datového prvku a kategorie, ale toto přidružení lze kdykoli změnit bez ztráty jakýchkoli dat. Nedoporučuje se to však často měnit, protože databáze je obecně méně hodnotná, protože snižuje kontinuitu dat. Všimněte si, že neexistuje žádný pevný limit na počet možností kategorie v kategorii nebo počet kategorií v kombinaci kategorií, ale existuje přirozené omezení, kde se struktura stává chaotickou a nepraktickou.

Dvojici kombinací datových prvků a kategorií lze nyní použít k reprezentaci jakékoli úrovně rozdělení. Je důležité si uvědomit, že to, co se ve skutečnosti děje, je, že datům je přiřazena řada vlastních dimenzí. Stejně jako datový prvek představuje povinnou dimenzi k datovým hodnotám, kategorie k němu přidávají vlastní dimenze. Ve výše uvedeném příkladu nyní můžeme pomocí výstupních nástrojů DHIS2 provádět analýzu založenou na „pohlaví“ i „věkové skupině“ pro tyto datové prvky, stejně jako lze provádět analýzu na základě datových prvků, organizačních jednotek a období .

Tento model kategorie lze použít jak v návrzích formulářů pro zadávání dat, tak v analýzách a tabulkových sestavách. Pro účely analýzy DHIS2 automaticky vytvoří dílčí součty a součty pro každý datový prvek spojený s kombinací kategorií. Pravidlem pro tento výpočet je, že všechny možnosti kategorií by měly být součtem smysluplného součtu. Výše uvedený příklad ukazuje tak smysluplný součet, protože při shrnutí „případů malárie“ zachycených pro „ženy \< 5 let”, “muže \< 5 let”, “ženy \> 5 let“ a „muže \> 5 let“ získáme celkový počet „případů malárie“.

Pro účely shromažďování dat může DHIS2 automaticky generovat tabulkové datové vstupní formuláře, kde jsou datové prvky reprezentovány jako řádky a kombinace možností kategorií jsou reprezentovány jako sloupce. To v mnoha situacích povede k poutavým formám s minimálním úsilím. Je třeba poznamenat, že to však představuje dilema, protože tyto dva problémy někdy nejsou kompatibilní. Například je možné rychle vytvořit formuláře pro zadávání dat pomocí kategorií, které nedodržují pravidlo smysluplného součtu. Považujeme to však za lepší alternativu než zachování dvou nezávislých a samostatných modelů pro zadávání a analýzu dat.

Důležitým bodem modelu kategorie je to, že hodnoty dat jsou trvalé a přidružené ke kombinaci možností kategorie. To znamená, že přidání nebo odebrání kategorií z kombinace kategorií způsobí, že tyto kombinace budou neplatné, a k opravě je nutné provést operaci s nízkou úrovní databáze. Doporučuje se proto zamyšleně zvážit, která rozdělení jsou požadována, a příliš často je neměnit.

## Skupiny datových prvků { #data-element-groups }

Běžné vlastnosti datových prvků lze modelovat pomocí tzv. Skupin datových prvků. Skupiny jsou zcela flexibilní v tom smyslu, že jejich jména a členství jsou definovány uživatelem. Skupiny jsou užitečné jak pro procházení, tak pro prezentaci souvisejících dat a lze je také použít k agregaci hodnot zachycených pro datové prvky ve skupině. Skupiny jsou volně spojeny s datovými prvky a nejsou přímo vázány na datové hodnoty, což znamená, že je lze kdykoli upravit a přidat bez ovlivnění dat na nízké úrovni.

# Datové sady a formuláře { #data-sets-and-forms }

Tato kapitola pojednává o souborech dat a formulářích, o tom, jaké typy formulářů jsou k dispozici, a popisuje osvědčené postupy pro proces přechodu z papírového na elektronické formuláře.

## Co je to datová sada? { #what-is-a-data-set }

Veškeré zadávání dat v DHIS2 je organizováno pomocí datových sad. Datová sada je kolekce datových prvků seskupených dohromady pro sběr dat a v případě distribuovaných instalací také definují bloky dat pro export a import mezi instancemi DHIS2 (např. z místní instalace okresního úřadu na národní server). Datové sady nejsou přímo spojeny s datovými hodnotami, pouze prostřednictvím jejich datových prvků a frekvencí, a jako takové lze datovou sadu upravovat, mazat nebo přidávat kdykoli bez ovlivnění nezpracovaných dat již zachycených v systému, ale například změny samozřejmě ovlivní, jak budou sbírána nová data.

Datová sada má typ období, který řídí frekvenci sběru dat, která může být denní, týdenní, měsíční, čtvrtletní, šestiměsíční nebo roční. Oba datové prvky, které mají být zahrnuty do datové sady, a typ období je definován uživatelem spolu s názvem, zkráceným názvem a kódem. Pokud jsou ve formuláři pro shromažďování (a nejen v sestavách) potřebná vypočítaná pole, pak lze k datové sadě přiřadit také indikátory, ale lze je použít pouze ve vlastních formulářích (viz dále dolů).

Aby bylo možné použít datovou sadu ke shromažďování dat pro konkrétní organizační jednotku, musí uživatel přiřadit organizační jednotku k datové sadě. Tento mechanismus řídí, které organizační jednotky mohou použít které datové soubory, a zároveň definuje cílové hodnoty pro úplnost dat (např. Kolik zdravotnických zařízení v okrese má každý měsíc předávat datový soubor RCH).

Datový prvek může patřit do více datových sad, ale to vyžaduje pečlivé přemýšlení, protože to může vést k překrývajícím se a nekonstantním shromažďováním údajů, pokud např. datové soubory mají různé frekvence a používají je stejné organizační jednotky.

## Co je formulář pro zadávání údajů? { #what-is-a-data-entry-form }

Jakmile přiřadíte datovou sadu organizační jednotce, bude tato datová sada zpřístupněna v Data Entry (v části Služby) pro organizační jednotky, kterým jste ji přiřadili, a pro platná období podle typu období datové sady. Poté se zobrazí výchozí formulář pro zadávání dat, což je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s kategoriemi, jako jsou věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři založeném na kategoriích. Kromě výchozího formuláře pro zadávání údajů založeného na seznamu existují další dvě alternativy, formulář založený na oddílech a vlastní formulář.

### Druhy formulářů pro zadávání údajů { #types-of-data-entry-forms }

DHIS2 v současné době obsahuje tři různé typy formulářů, které jsou popsány níže.

#### Výchozí formuláře { #default-forms }

Výchozí formulář pro zadávání dat je jednoduše seznam datových prvků patřících do datové sady spolu se sloupcem pro zadávání hodnot. Pokud vaše datová sada obsahuje datové prvky s jinou než výchozí kombinací kategorií, například věkové skupiny nebo pohlaví, budou automaticky vygenerovány další sloupce ve výchozím formuláři na základě různých možností / dimenzí. Pokud v datové sadě použijete více než jednu kombinaci kategorií, dostanete ve výchozí podobě jednu tabulku na kombinaci kategorií s různými záhlavími sloupců pro možnosti.

#### Sekce formulářů { #section-forms }

Sekce formulářů umožňují o něco větší flexibilitu, pokud jde o používání tabulkových formulářů, a jejich design je rychlý a jednoduchý. Formulář pro zadávání dat bude často potřebovat více tabulek s podnadpisy a někdy budete muset deaktivovat (šedě) několik polí v tabulce (např. Některé kategorie se nevztahují na všechny datové prvky), obě tyto funkce jsou podporovány v sekcích formulářů. Po definování datové sady můžete definovat jeho sekce s podmnožinami datových prvků, nadpisem a možnými šedými poli v tabulce oddílu. Lze také definovat pořadí sekcí v datové sadě. V Zadávání dat můžete nyní začít používat sekce formuláře (který by se měl automaticky zobrazit, když jsou pro vybranou sadu dat k dispozici sekce). Většina tabulkových formulářů pro zadávání údajů by měla být možná se sekcemi formulářů. Využití sekcí nebo výchozích formulářů usnadňuje život, protože není nutné udržovat návrh pevného formuláře, který obsahuje odkazy na datové prvky. Pokud tyto dva typy formulářů nesplňují vaše požadavky, třetí možností je zcela flexibilní, i když časově náročnější, připravte vlastní formulář pro zadávání dat.

#### Vlastní formuláře { #custom-forms }

Pokud je formulář, který chcete navrhnout, příliš komplikovaný pro výchozí formuláře nebo formuláře oddílů, poslední možností je použít vlastní formulář. To zabere více času, ale dává vám plnou flexibilitu, pokud jde o design. V DHIS2 je v návrháři formulářů zabudovaný editor HTML (CK Editor), který umožňuje buď navrhnout formulář v grafickém uživatelském rozhraní, nebo přímo vložit do html (pomocí okna „source“ v editoru). Ve vlastním formuláři můžete vložit statický text nebo datová pole (spojená s datovými prvky

- kombinace možností kategorie) na libovolné pozici ve formuláři a máte úplnou svobodu navrhnout rozvržení formuláře. Po přidání vlastního formuláře do datové sady bude k dispozici v Data Entry a automaticky použit.

Při použití vlastního formuláře je možné použít vypočítaná pole k zobrazení např. průběžné součty nebo jiné výpočty založené na datech zachycených ve formuláři. To může např. být užitečné při řešení skladových nebo logistických formulářů, které vyžadují zůstatek položky, položky potřebné pro další období atd. Aby to uživatel mohl udělat, musí nejprve definovat vypočítané výrazy jako indikátory a poté tyto indikátory přiřadit k dané datové sadě. V návrháři vlastních formulářů pak může uživatel přiřadit indikátory formuláři stejným způsobem, jak jsou přiřazeny datové prvky. Omezení vypočítaného výrazu spočívá v tom, že všechny datové prvky použité ve výrazu musí být k dispozici ve stejné datové sadě, protože výpočty se provádějí za běhu uvnitř formuláře a nejsou založeny na hodnotách dat, které jsou již uloženy v databázi.

## Od papírového k elektronickému formuláři - poučení { #from-paper-to-electronic-form-lessons-learned }

Při zavádění elektronického zdravotnického informačního systému je nahrazovaným systémem často hlášení v papírové podobě. Proces přechodu na elektronický sběr a analýzu dat má určité problémy. Následující části navrhují osvědčené postupy, jak je překonat.

### Identifikujte samostatné datové prvky { #identify-self-contained-data-elements }

Návrh datové sady DHIS2 je obvykle založen na některých požadavcích z papírové formy, která se již používá. Logika papírových formulářů není stejná jako datový prvek a model datové sady DHIS, např. pole v tabulkové papírové formě je často popisováno jak záhlavími sloupců, tak textem na každém řádku, a někdy také některým úvodním záhlavím tabulky, které poskytuje více kontextu. V databázi je to zachyceno pro jeden atomární datový prvek bez odkazu na pozici ve formátu vizuální tabulky, takže je důležité zajistit, aby datový prvek s volitelnými kategoriemi datových prvků zachytil plný význam každého jednotlivého pole v papírová forma.

### Nechte výpočty a opakování na počítači - zachyťte pouze nezpracovaná data { #leave-calculations-and-repetitions-to-the-computer-capture-raw-data-only }

Další důležitou věcí, kterou je třeba mít na paměti při navrhování datových sad, je to, že datová sada a odpovídající formulář pro zadávání dat (což je datová sada s rozvržením) je nástrojem pro sběr dat, nikoli nástrojem pro sestavy nebo analýzy. Existují i jiné mnohem propracovanější nástroje pro výstup a vykazování dat v DHIS2 než formuláře pro zadávání dat. Papírové formuláře jsou často navrženy s ohledem na sběr dat i na vykazování, a proto můžete vidět věci, jako jsou kumulativní hodnoty (kromě měsíčních hodnot), opakování ročních dat (stejné údaje o populaci vykazované každý měsíc) nebo dokonce hodnoty indikátorů, jako jsou jako míry pokrytí ve stejné formě jako měsíční nezpracovaná data. Když každý měsíc ukládáte nezpracovaná data do databáze DHIS2 a máte veškerý potřebný výpočetní výkon v rámci počítačového nástroje, není třeba (ve skutečnosti by to bylo špatné a pravděpodobně by to způsobilo nekonzistenci) registrovat ručně vypočítané hodnoty, jako je ty zmíněné výše. Chcete pouze zachytit nezpracovaná data ve svých datových sadách / formulářích a nechat výpočty na počítači a prezentovat tyto hodnoty nástrojům pro vytváření zpráv v DHIS. Díky funkčnosti přehledů sady dat všechny formuláře tabulkových sekcí automaticky získají další sloupce zcela vpravo a poskytnou mezisoučet a celkové hodnoty pro každý řádek (datový prvek).

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
