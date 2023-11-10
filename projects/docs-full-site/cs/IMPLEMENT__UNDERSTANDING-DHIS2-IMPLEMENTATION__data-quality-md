---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/implementation/data-quality.md"
revision_date: "2021-06-14"
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
