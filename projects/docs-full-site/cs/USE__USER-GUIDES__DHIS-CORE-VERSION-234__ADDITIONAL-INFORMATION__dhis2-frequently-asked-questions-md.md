---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/user/dhis2-frequently-asked-questions.md"
revision_date: "2021-06-14"
---

# DHIS2 Často kladené otázky { #dhis2-frequently-asked-questions }

**Otázka:** Zadal jsem data do formuláře pro zadávání dat, ale nevidím data v žádných přehledech (kontingenční tabulky, grafy, mapy). Proč se zadaná data nezobrazí okamžitě v mých grafech v DHIS2?

**A:** Data, která jsou zadána do DHIS2, musí být nejprve zpracována pomocí „analytiky“. To znamená, že data nejsou v analytických prostředcích (jako jsou sestavy, kontingenční tabulky, vizualizér dat, GIS atd.) Ihned k dispozici po zadání. Pokud je plánování aktivní, analytický proces bude spuštěn automaticky každý den o půlnoci. Poté budou viditelná nová data, která byla zadána od posledního spuštění analytického procesu.

Proces analýzy můžete spustit ručně výběrem položky Zprávy -\> Analýzy v hlavní nabídce a stisknutím tlačítka „Zahájit export“. Tento proces může trvat značné množství času v závislosti na množství dat ve vaší databázi.

Další faktory, které mohou ovlivnit viditelnost údajů, jsou:

-   Schválení dat: Pokud data nebyla schválena na úrovni, která odpovídá úrovni vašich uživatelů, data pro vás nemusí být viditelná.

-   Sdílení meta-datových objektů: Pokud určité meta-datové objekty nebyly sdíleny se skupinou uživatelů, jejichž jste členem, data pro vás nemusí být viditelná.

-   Ukládání analytických údajů do mezipaměti: V mnoha případech správci serveru ukládají do mezipaměti analytické objekty (například kontingenční tabulky, mapy, grafy) na serveru. Pokud jste zadali data, znovu spusťte analytiku a stále nevidíte žádná (aktualizovaná) data, ujistěte se, že vaše data nejsou ukládána do mezipaměti serverem.

**Otázka:** Stáhl jsem si DHIS2 z <https://www.dhis2.org/downloads>, ale když se pokusím vstoupit do systému, potřebuje uživatelské jméno a heslo. Které mám použít?

**Odpověď:** Ve výchozím nastavení bude uživatelské jméno „admin“ a heslo „district“. V uživatelských jménech a heslech se rozlišují velká a malá písmena.
