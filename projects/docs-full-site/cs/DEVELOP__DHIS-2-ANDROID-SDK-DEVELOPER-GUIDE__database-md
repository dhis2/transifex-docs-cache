---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/database.md" 
---
# Databáze

<!--DHIS2-SECTION-ID:database-->

## Rozsah databáze
Sada SDK uchovává data dvojice [server, uživatel] v izolované databázi.

V tuto chvíli je podporován pouze jeden pár [server, uživatel], takže odhlášení a přihlášení pomocí jiného páru [server, uživatel] vymaže aktuální databázi a vytvoří novou.

## Šifrování
Od verze SDK verze 1.1.0 je možné ukládat data do šifrované databáze. Šifrovací klíč je generován náhodně sadou SDK a udržován v bezpečí.

Stav šifrování (zda je databáze šifrovaná nebo ne) lze nakonfigurovat na úrovni serveru v aplikaci pro Android.
Výchozí stav je false: Pokud aplikace není nainstalována, databáze nebude šifrována.

Během prvního přihlášení pro daný server a uživatele bude stav šifrování stažen z API a bude vytvořena databáze daného typu.

V pozdějších přihlášeních nebo synchronizaci metadat SDK znovu stáhne stav šifrování ze serveru a pokud se změní, zašifruje nebo dešifruje aktuální databázi bez ztráty dat.

### Výkon šifrování
- Velikost databáze: velikost databáze je přibližně stejná, bez ohledu na to, zda je šifrována nebo ne.
- Rychlost: čtení a zápis jsou pomocí šifrované databáze v průměru o 5 až 10% pomalejší.

