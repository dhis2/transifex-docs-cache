---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/value-types-supported.md"
revision_date: "2021-05-07"
---

# Podporované typy hodnot { #capture_app_value_types }

Následuje úplný seznam všech typů hodnot dostupných v DHIS 2 a poznámky o tom, zda byly nebo nebyly tyto implementovány v aplikaci Android Capture.

Jakékoli problémy spojené s používáním konkrétní funkce v systému Android jsou zvýrazněny vykřičníkem \!.

|  |  |
| :-: | :-- |
| ![](resources/icons/icon-complete.png) | Typ hodnoty implementován |
| ![](resources/icons/icon-incomplete.png) | Typ hodnoty není implementován, ale bude bezpečně ignorován (pokud není povinný) |
| ![](resources/icons/icon-wip.png) | Probíhající práce. Funkce ještě není zcela implementována nebo již bylo hlášeno neočekávané chování |

| Typ hodnoty | Popis typu hodnoty | Program s registrací | Program s registrací | Program bez registrace | Datová sada | Poznámky k provádění |
| :-- | :-- | :-: | :-: | :-: | :-: | :-- |
|  |  | **Atributy** | **Datové prvky** | **Datové prvky** | **Datové prvky** |
| Čas | Pouze čas | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Datum a čas | Datum a čas | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Datum | Pouze datum | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Věk | Umožňuje zadat buď věk v letech / měsících / dnech, nebo datum narození (oba jsou uloženy jako datum narození) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Telefonní číslo | Platné telefonní číslo | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| E-mail | E-mailová adresa v platném formátu | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Ano/ne | Booleovský ano / ne (nebo bez odpověďi) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Pouze ano | Ano nebo ne | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |
| Číslo | Jakékoli platné číslo, včetně desetinných míst | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Celé číslo | Libovolné celé číslo (celá čísla, žádná desetinná místa) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Kladné celé číslo | Pouze kladná celá čísla (žádné nulové nebo záporné hodnoty) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Kladné nebo nulové celé číslo | Pouze nula nebo kladná celá čísla (žádné záporné hodnoty) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Záporné celé číslo | Pouze záporná celá čísla (žádná nula nebo kladné hodnoty) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Procento | Libovolná desetinná hodnota mezi 0 a 100 | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Jednotkový interval | Libovolná desetinná hodnota mezi 0 a 1 | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Text | Text (délka textu až 50 000 znaků) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Dlouhý text | Text (bez omezení délky) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Písmeno | Jediné písmeno | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| Soubor | Umožňuje nahrávání souborů v různých formátech (vyžaduje konfiguraci příslušného úložiště) | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-incomplete.png) |  |
| Organizační jednotka | Umožňuje výběr organizační jednotky DHIS2 jako zvolené hodnoty | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-incomplete.png) |  |
| Tracker Associate | Umožňuje výběr existujícího Trasovače 'trasované instance entity' (např. Osoby) jako hodnoty | ![](resources/icons/icon-incomplete.png) | ![](resources/icons/icon-incomplete.png) | ![](resources/icons/icon-incomplete.png) | ![](resources/icons/icon-incomplete.png) |  |
| Uživatelské jméno | Umožňuje výběr platného uživatelského jména DHIS2 jako hodnoty | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-wip.png) | ![](resources/icons/icon-incomplete.png) |
| Koordinát | Umožňuje ruční zadání zeměpisných souřadnic (neumožňuje automatické zachycení souřadnic) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| URL | Umožňuje ruční zadání adresy URL. | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) |  |
| obrázek | Umožňuje nahrávání obrázků. | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-complete.png) | ![](resources/icons/icon-incomplete.png) |  |
