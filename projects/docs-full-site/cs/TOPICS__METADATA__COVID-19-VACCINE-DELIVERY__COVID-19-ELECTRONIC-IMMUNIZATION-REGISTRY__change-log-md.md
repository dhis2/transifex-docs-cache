---
edit_url: "https://github.com/dhis2-metadata/CVC_EIR/blob/master/docs/cvc_eir_change_log.md"
revision_date: "2021-12-01"
---

# Protokoly změn { #cvc-eir-change-log }

Pokud jste nainstalovali jeden z nedokončených balíčků před oficiálním vydáním, jedná se o hlavní změny mezi každou iterací:

## Protokol změn pro verzi 0.1 { #change-log-for-version-01 }

1. Indikátory „AEFI podle produktu“: Upravený filtr
2. Vizualizace „COVAC-AEFI podle typu události“: přidána Bellova obrna, lymfadenopatie, neurologická / svalová
3. Přidané vysvětlení pro vypadlé vizualizace
4. Přidána upozornění na SMS
5. Upravená pravidla programu, aby vyhovovala požadavkům systému Android
6. Opraveno několik překlepů
7. Číslo dávky bylo v systému Android změněno na „vykreslení jako čárový kód“
8. Upravená pravidla programu pro přiřazování hodnot základním chorobám od aktivní v celém programu až po aktivní ve fázi očkování

## Protokol změn pro verzi 0.2 { #change-log-for-version-02 }

1. Přidané skupiny uživatelů: Metadata očkování COVID Admin COVID Immunization Data Capture COVID Immunization Data analysis
2. Odstraněna fáze AEFI
3. Odstraněny indikátory AEFI
4. Odstraněny indikátory programu AEFI
5. Ve fázi očkování přidán DE „AEFIS present“

## Protokol změn pro verzi 0.3 { #change-log-for-version-03 }

1. Přidáni výrobci
2. Přidána souhrn sady možností výrobců
3. Přidáno Celkové dávky potřebné pro tuto vakcínu
4. Přidáno programové pravidlo, které skrývá jména výrobců v závislosti na produktu vakcíny
5. Přidáno programové pravidlo, které přiřazuje počet požadovaných celkových dávek
6. Změněno „Dávka podána dne“ na „Dávka podána dne (datum očkování)“
7. Atribut Unique Identifier byl změněn na jedinečný identifikátor EPI, aby odpovídal AEFI

## Protokol změn pro verzi 0.4 { #change-log-for-version-04 }

1. Změněno DE „Typ vakcíny“ na „Vakcína dána“ a změněné názvy zástupných symbolů možností (tj. COVAC1) na názvy produktů a výrobců (tj. „MRNA-1273/Moderna“)
2. Změněno DE „Název vakcíny“ na výrobce vakcín a přidán seznam
3. Přidány Gamaleya a Sinopharm a příslušné produkty (viz tabulka níže)
4. Přidáno programové pravidlo k automatickému naplnění výrobce DE na základě názvu vakcíny
5. Přidáno pravidlo programu pro skrytí možností názvu vakcíny pro Astrazeneca
6. Přidáno pravidlo programu pro automatické naplnění „Toto je poslední dávka“ DE, když je pacientovi podána druhá dávka. (to předpokládá, že všechny současné produkty mají v plánu očkování dvě dávky)
7. Upraven výraz v pravidle programu, který nepřiděluje nové datum pro další dávku po dokončení poslední dávky.
8. Oznámení AEFI změněno z „Prosím zajistěte registraci tohoto nepříznivého účinku ve fázi AEFI“ na „Proveďte prosím vyšetřování AEFI podle oficiálních postupů pro vyšetřování AEFI“
9. Změněné kódy zástupných symbolů

| Název vakcíny | Vaccine Optioncode (old) | Vaccine Option Code (současný) | Název výrobce | Volitelný kód | Věkové doporučení | Interval dávky | Počet dávek |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AZD1222 / AstraZeneca | COVAC1 | astrazeneca | AstraZeneca | astrazeneca | 18 | 10 dní (8-12\*) | 2 |
| AZD1222 / AstraZeneca | COVAC1 | astrazeneca | SKBio Astra Zeneca | skbioastrazeneca | 18 | 10 (8-12\*) | 2 |
| BNT162b2 / COMIRNATY Tozinameran (INN) / BioNTech/Pfizer | COVAC2 | biontechpfizer | Comirnaty, Tozinameran | biontechpfizer | 16 | 21 | 2 |
| mRNA-1273 / Moderna | COVAC3 | moderna | mRNA-1273 | moderna | 18 | 28 | 2 |
| Gamaleya | COVAC4 | gamaleya | Sputnik V | gamaleya | 18 | 21 | 2 |
| SARS-CoV-2 Vaccine (VeroCell), Inactivated / Sinopharm | COVAC5 | sinopharm | Coronavac, BBIBP-CorV | sinopharm | 18 | 21 dní (21-28)\* | 2 |

## Protokol změn pro verzi 0.5 { #change-log-for-version-05 }

1. Změněn COVAX na COVAC
2. Změněno pořadí vlastních pracovních seznamů
3. Přidána předpona „COVAC“ k objektům, které by mohly způsobit problémy s importem u instancí, které mají existující balíčky (Pohlaví, Ano/Ne/Neznámý/, Městský/Venkovský)

## Protokol změn pro verzi 1.1 { #change-log-for-version-11 }

1. Upravené pravidlo programu „Pokud je předchozí vakcína stejná jako aktuální vakcína, skrýt pole vysvětlení“
2. Přidáno pravidlo programu „Skrýt navrhované datum pro další dávku, pokud druhá dávka a očkovací produkt již žádné dávky nemá“
3. Upravený výraz v Pravidle programu „Pokud pacient trpěl základními chorobami, přeneste tuto hodnotu do následující fáze“ a byla přidána akce pro přiřazení hodnoty aktuální proměnné PR.
4. Upravené výrazy v pravidlech programu „Pokud má klient historii XXX, přiřaďte hodnotu aktuální události“
