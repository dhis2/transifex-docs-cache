---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/tutorials/analysing-postgresql-logs-using-pgbadger.md"
revision_date: '2021-06-14'
tags:
- Návody
title: Analýza protokolů PostgreSQL pomocí pgbadger
---

# Analýza protokolů PostgreSQL pomocí pgbadger { #analysing-postgresql-logs-using-pgbadger }

**Jako správce systému DHIS 2 je velmi důležité vědět, co se děje s vaší databází PostgreSQL. Pohled na protokoly PostgreSQL vám poskytne vodítko, avšak prosté procházení protokolů pomocí textového editoru je obtížné, protože protokoly se stávají velmi velkými se spoustou opakujícího se obsahu. Tento výukový program vysvětluje, jak vám nástroj pro analýzu protokolů pgbadger PostgreSQL může pomoci získat užitečné informace z vašich protokolů.**

Nástroj pro analýzu protokolů pgbadger PostgreSQL se snadno instaluje (vyžaduje pouze perl) a je snadno srozumitelný. Umožňuje vám analyzovat soubory protokolu z příkazového řádku pomocí jednoduchých příkazů.

Nejprve se ujistěte, že máte nainstalovaný perl (na Debian / Ubuntu Linux):

```
sudo apt-get install perl
```

Poté stáhněte pgbadger ze stránky vydání GitHub, rozbalte jej a nainstalujte (upravte verzi v názvu souboru):

```
tar xvf pgbadger-6.4.tar.gz
cd pgbadger-6.4
perl Makefile.PL
make && sudo make install
```

Budete muset upravit konfigurační soubor PostgreSQL tak, aby poskytoval pgbadger informace, které potřebuje. Nejprve musíte nastavit nastavení „log_line_prefix“:

```
log_line_prefix = '%t [%p]: [%l-1] '
```

Zadruhé byste měli povolit "log_min_duration_statement". Toto nastavení způsobí, že PostgreSQL zaznamená všechny příkazy, které běží déle než zadaná hodnota v milisekundách, kde hodnota 0 zaznamená vše. Ujistěte se, že je „log_statement“ nastaveno na „none“, jinak nastavení „log_min_duration_statement“ nic nezaznamená (stejně je „none“ výchozí hodnota).

```
log_statement = 'none'
log_min_duration_statement = 0
```

Zatřetí byste měli povolit protokolování kontrolních bodů, zámků a dalších, abyste získali maximální hodnotu z analýzy protokolu:

```
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on
log_temp_files = 0
log_autovacuum_min_duration = 0
```

Fragment konfigurace můžete také získat zde. Aby se změny projevily, nemusíte restartovat PostgreSQL, jednoduše se přihlaste do příkazového řádku psql a spusťte následující (stejným způsobem, jako spouštíte příkazy SQL):

```
select pg_reload_conf();
```

Samozřejmě, že protokolování všech příkazů má dopad na výkon vašeho systému, takže jej můžete povolit na dostatečně dlouhou dobu, aby vám poskytlo protokoly v hodnotě 50 až 200 Mb, a poté jej znovu deaktivovat.

Nyní s DHIS 2 již víme, že generování analytické tabulky a proces indexování má některé velmi dlouhodobé dotazy. Nechceme, aby jim pgbadger vzali veškerou pozornost, takže vytvoříme nový soubor protokolu, kde tyto příkazy vynecháme pomocí následujícího příkazu v terminálu:

```
cat pg.log | grep -viE "create index|insert into analytics|vacuum analyze analytics" > pg_clean.log
```

Nyní jsme připraveni provést analýzu. Vyvolejte:

```
pgbadger -j 4 pg_clean.log
```

Zde parametr „-j“ označuje počet CPU, které chcete pro proces použít - ve výchozím nastavení používá 1, ale umožnění většího počtu procesorů proces hodně zrychluje. Nakonec „pg_clean.log“ odkazuje na váš soubor protokolu.

Všimněte si, že pokud používáte Amazon RDS (hosting spravované databáze), nedovolí vám to změnit nastavení „log_line_prefix“. Místo toho můžete spustit pgbadger s volbou "-p", která vám umožní zadat vlastní předponu pro analýzu:

```
pgbadger -j 4 -p '%t:%r:%u@%d:[%p]:' pg_clean.log
```

Nástroj pgbdager nyní vytvoří pěknou prezentaci analýzy v souboru HTML s názvem „out.html“. Stačí otevřít soubor ve webovém prohlížeči podle vašeho výběru.

Nejzajímavější částí může být položka nabídky „Top“. Poskytuje velmi užitečné statistiky včetně jednotlivých nejpomalejších dotazů a normalizovaných časově nejnáročnějších dotazů, nejčastějších dotazů a nejpomalejších dotazů. Zde „normalizováno“ znamená, že parametry dotazu SQL jsou ignorovány. To je užitečné k pochopení, které dotazy jsou nejpomalejší. Bez normalizace by váš jediný nejpomalejší dotaz zcela dominoval statistikám, pokud by byl spuštěn s mnoha různými parametry dotazu.

Z analýzy na konkrétní instanci DHIS 2 jsem se dozvěděl, že funkce ověřování způsobuje docela dlouhotrvající dotazy, které lze optimalizovat. Doporučujeme vám analyzovat vlastní instanci DHIS 2 a zjistit, které dotazy trvají dlouho. Na základě toho můžete optimalizovat databázi pomocí indexů nebo poskytnout zpětnou vazbu vývojovému týmu DHIS 2 ohledně potenciálních úzkých míst a náročných dotazů.

![](resources/images/pgbadger.png)

Příjemné sledování!

