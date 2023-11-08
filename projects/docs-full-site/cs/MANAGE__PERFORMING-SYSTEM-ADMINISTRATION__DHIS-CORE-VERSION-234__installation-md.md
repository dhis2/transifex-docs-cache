---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/sysadmin/installation.md"
revision_date: "2021-09-07"
---

# Instalace { #installation }

Kapitola instalace obsahuje informace o tom, jak nainstalovat DHIS2 v různých kontextech, včetně online centrálního serveru, offline lokální sítě, samostatné aplikace a samostatného balíčku s názvem DHIS2 Live.

## Úvod { #install_introduction }

DHIS2 běží na všech platformách, pro které existuje prostředí Java Runtime Environment verze 8 nebo vyšší, které zahrnuje nejoblíbenější operační systémy jako Windows, Linux a Mac. DHIS2 běží na databázovém systému PostgreSQL. DHIS2 je zabalen jako standardní webový archiv Java (soubor WAR) a běží tedy na jakýchkoli servletových kontejnerech, jako jsou Tomcat a Jetty.

Tým DHIS2 doporučuje jako preferované prostředí pro instalace serveru operační systém Ubuntu 16.04 LTS, databázový systém PostgreSQL a kontejner Servlet Tomcat.

Tato kapitola poskytuje průvodce nastavením výše uvedeného technologického zásobníku. Mělo by se však číst jako průvodce pro uvedení do provozu a nikoli jako vyčerpávající dokumentace pro uvedené prostředí. Pro důkladné čtení odkazujeme na oficiální dokumentaci Ubuntu, PostgreSQL a Tomcat.

Balíček Ubuntu dhis2-tools automatizuje mnoho úkolů popsaných v níže uvedené příručce a je doporučen pro většinu uživatelů, zejména pro ty, kteří neznají příkazový řádek nebo správu serverů. Podrobně je popsán v samostatné kapitole této příručky.

## Specifikace serveru { #install_server_specifications }

DHIS2 je aplikace náročná na databázi a vyžaduje, aby měl váš server odpovídající množství paměti RAM, počet jader CPU a rychlý disk. Tato doporučení by měla být považována za obecná pravidla, nikoli za přesná měřítka. DHIS2 se lineárně mění podle velikosti RAM a počtu jader CPU, takže čím více si můžete dovolit, tím lépe bude aplikace fungovat.

-   _RAM:_ Alespoň 1 GB paměti na 1 milion zaznamenaných datových záznamů za měsíc nebo na 1000 souběžných uživatelů. Alespoň 4 GB pro malou instanci, 12 GB pro střední instanci.

-   _CPU cores:_ 4 CPU cores for a small instance, 8 CPU cores for a medium or large instance.

-   _Disk:_ Ideálně použijte SSD. Jinak použijte disk s rychlostí 7200 ot./min. Minimální rychlost čtení je 150 Mb/s, 200 Mb/s je dobrá, 350 Mb/s nebo lepší je ideální. Pokud jde o místo na disku, doporučuje se minimálně 60 GB, ale bude zcela záviset na množství dat obsažených v tabulkách hodnot dat. Tabulky Analytics vyžadují značné množství místa na disku. Plánujte dopředu a zajistěte, aby váš server mohl být upgradován s větším množstvím místa na disku, jakmile to bude potřeba.

## Softwarové požadavky { #install_software_requirements }

Pozdější verze DHIS2 vyžadují pro provoz následující verze softwaru.

-   Java JDK nebo JRE verze 8 nebo novější.

-   Jakýkoli operační systém, pro který existuje Java JDK nebo JRE verze 8.

-   Databáze PostgreSQL verze 9.6 nebo novější.

-   Rozšíření databáze PostGIS verze 2.2 nebo novější.

-   Kontejner servletu Tomcat verze 8.5.50 nebo novější nebo jiné servletové kontejnery vyhovující Servlet API 3.1.

## Nastavení serveru { #install_server_setup }

Tato část popisuje, jak nastavit instanci serveru DHIS2 na 64bitovém Ubuntu 16.04 s PostgreSQL jako databázovým systémem a Tomcat jako servletovým kontejnerem. Tato příručka není míněna jako průvodce krok za krokem jako takový, ale spíše slouží jako odkaz na to, jak lze DHIS2 nasadit na server. Existuje mnoho možných strategií nasazení, které se budou lišit v závislosti na operačním systému a databázi, kterou používáte, a dalších faktorech. Termín _invoke_ označuje provedení daného příkazu v terminálu.

Pro národní server je doporučená konfigurace čtyřjádrový procesor 2 Ghz nebo vyšší a 12 Gb RAM nebo vyšší. Upozorňujeme, že pro využití více než 4 Gb RAM je vyžadován 64bitový operační systém.

V této příručce předpokládáme, že 8 GB RAM je přiděleno pro PostgreSQL a 8 GB RAM je přiděleno pro Tomcat / JVM a že je použit 64bitový operační systém. _Pokud používáte jinou konfiguraci, upravte odpovídajícím způsobem navrhované hodnoty\!_ Doporučujeme rozdělit dostupnou paměť zhruba rovnoměrně mezi databázi a JVM. Nezapomeňte ponechat část fyzické paměti operačnímu systému, aby mohl provádět své úkoly, například přibližně 2 GB. Kroky označené jako _volitelné_, stejně jako krok pro ladění výkonu, lze provést v pozdější fázi.

### Vytvoření uživatele pro spuštění DHIS2 { #install_creating_user }

Měli byste vytvořit vyhrazeného uživatele pro běh DHIS2.

> **Důležité**
>
> Server DHIS2 byste neměli spouštět jako privilegovaný uživatel, jako je root.

Vytvořte nového uživatele s názvem dhis vyvoláním:

```sh
sudo useradd -d /home/dhis -m dhis -s /bin/false
```

Poté nastavte heslo pro svůj účet:

```sh
sudo passwd dhis
```

Ujistěte se, že jste nastavili silné heslo s alespoň 15 náhodnými znaky.

### Vytvoření konfiguračního adresáře { #install_creating_config_directory }

Začněte vytvořením vhodného adresáře pro konfigurační soubory DHIS2. Tento adresář bude také použit pro aplikace, soubory a soubory protokolu. Příkladem adresáře může být:

```sh
mkdir /home/dhis/config
chown dhis:dhis /home/dhis/config
```

DHIS2 vyhledá proměnnou prostředí s názvem _DHIS2_HOME_ k vyhledání konfiguračního adresáře DHIS2. Tento adresář bude v této instalační příručce označován jako _DHIS2_HOME_. Proměnnou prostředí definujeme v pozdějším kroku procesu instalace.

### Nastavení časového pásma a národního prostředí serveru { #install_setting_server_tz }

Může být nutné překonfigurovat časové pásmo serveru tak, aby odpovídalo časovému pásmu umístění, které bude server DHIS2 pokrývat. Pokud používáte virtuální privátní server, nemusí výchozí časové pásmo odpovídat časovému pásmu vašeho umístění DHIS2. Časové pásmo můžete snadno překonfigurovat vyvoláním níže a podle pokynů.

```sh
sudo dpkg-reconfigure tzdata
```

PostgreSQL je citlivý na národní prostředí, takže možná budete muset nejprve nainstalovat své národní prostředí. Zkontrolujte stávající národní prostředí a pak nainstalujte nové (např. Norské):

```sh
locale -a
sudo locale-gen nb_NO.UTF-8
```

### Instalace PostgreSQL { #install_postgresql_installation }

Nainstalujte PostgreSQL vyvoláním:

```sh
sudo apt-get install postgresql-10 postgresql-contrib-10 postgresql-10-postgis-2.4
```

Vytvořte neprivilegovaného uživatele s názvem _dhis_ vyvoláním:

```sh
sudo -u postgres createuser -SDRP dhis
```

Po výzvě zadejte zabezpečené heslo. Vytvořte databázi vyvoláním:

```sh
sudo -u postgres createdb -O dhis dhis2
```

Vraťte se do relace vyvoláním příkazu `exit` Nyní máte uživatele PostgreSQL s názvem _dhis_ a databázi s názvem _dhis2_.

Rozšíření _PostGIS_ je potřeba, aby fungovalo několik funkcí GIS / mapování. DHIS 2 se pokusí nainstalovat příponu PostGIS během spouštění. Pokud uživatel databáze DHIS 2 nemá oprávnění k vytváření rozšíření, můžete jej vytvořit z konzoly pomocí uživatele _postgres_ pomocí následujících příkazů:

```sh
sudo -u postgres psql -c "create extension postgis;" dhis2
```

Ukončete příkazovou řádku a vraťte se ke svému předchozímu uživateli pomocí _\\q_ následně pak _exit_.

### Ladění výkonu PostgreSQL { #install_postgresql_performance_tuning }

Vyladění PostgreSQL je nezbytné pro dosažení vysoce výkonného systému, ale je volitelné, pokud jde o spuštění DHIS2. PostgreSQL je konfigurován a vyladěn prostřednictvím souboru _postgresql.conf_, který lze upravit takto:

```sh
sudo nano /etc/postgresql/10/main/postgresql.conf
```

a nastavte následující vlastnosti:

```properties
max_connections = 200
```

Určuje maximální počet připojení, které PostgreSQL povolí.

```properties
shared_buffers = 3200MB
```

Určuje, kolik paměti by mělo být přiděleno výhradně pro ukládání do mezipaměti PostgreSQL. Toto nastavení řídí velikost sdílené paměti jádra, která by měla být vyhrazena pro PostgreSQL. Mělo by být nastaveno na přibližně 40% celkové paměti vyhrazené pro PostgreSQL.

```properties
work_mem = 20MB
```

Určuje množství paměti použité pro interní operace řazení a zatřiďování. Toto nastavení je na jedno připojení, na každý dotaz, takže při příliš vysokém zvýšení může být spotřebováno hodně paměti. Správné nastavení této hodnoty je nezbytné pro výkon agregace DHIS2.

```properties
maintenance_work_mem = 512MB
```

Určuje velikost paměti, kterou PostgreSQL může použít pro operace údržby, jako je vytváření indexů, spouštění vacuum, přidávání cizích klíčů. Zvýšení této hodnoty může zlepšit výkon vytváření indexu během procesů generování analytiky.

```properties
effective_cache_size = 8000MB
```

Odhad, kolik paměti je k dispozici pro ukládání do mezipaměti disku operačním systémem (nikoli alokace) a isdb.no, které používá PostgreSQL k určení, zda se plán dotazů vejde do paměti nebo ne. Nastavení na vyšší hodnotu, než je skutečně k dispozici, bude mít za následek špatný výkon. Tato hodnota by měla zahrnovat nastavení shared_buffers. PostgreSQL má dvě vrstvy ukládání do mezipaměti: První vrstva používá sdílenou paměť jádra a je řízena nastavením shared_buffers. PostgreSQL deleguje druhou vrstvu na diskovou mezipaměť operačního systému a velikost dostupné paměti lze určit pomocí nastavení effective_cache_size.

```properties
checkpoint_completion_target = 0.8
```

Nastaví paměť používanou pro ukládání do vyrovnávací paměti během procesu zápisu WAL. Zvýšení této hodnoty může zlepšit propustnost v systémech náročných na zápis.

```properties
synchronous_commit = off
```

Určuje, zda potvrzení transakce počká na zápis záznamů WAL na disk před návratem ke klientovi, či nikoli. Vypnutím tohoto nastavení se výrazně zvýší výkon. To také znamená, že existuje mírné zpoždění mezi transakcí, která je klientovi nahlášena jako úspěšná, a skutečně bezpečnou, ale stav databáze nelze poškodit a je to dobrá alternativa pro systémy náročné na výkon a pro zápis, jako je DHIS2.

```properties
wal_writer_delay = 10000ms
```

Určuje zpoždění mezi operacemi zápisu WAL. Nastavením této hodnoty na vysokou hodnotu se zlepší výkon v systémech náročných na zápis, protože potenciálně mnoho operací zápisu lze provést v rámci jednoho vyprázdnění na disk.

```properties
random_page_cost = 1.1
```

_SSD only._ Nastaví odhad plánovače dotazů na náklady na stránku disku, která není postupně načítána. Nízká hodnota způsobí, že systém upřednostňuje indexové skenování před sekvenčními. Nízká hodnota má smysl pro databáze spuštěné na jednotkách SSD nebo s velkou mezipamětí v paměti. Výchozí hodnota je 4,0, což je přiměřené pro tradiční disky.

```properties
max_locks_per_transaction = 96
```

Určuje průměrný počet zámků objektů přidělených pro každou transakci. Toto je nastaveno hlavně proto, aby bylo možné dokončit upgradovací rutiny, které se dotýkají velkého počtu tabulek.

Restartujte PostgreSQL zadáním následujícího příkazu:

```sh
sudo /etc/init.d/postgresql restart
```

### Konfigurace systému { #install_database_configuration }

Informace o připojení k databázi jsou poskytovány DHIS2 prostřednictvím konfiguračního souboru s názvem _dhis.conf_. Vytvořte tento soubor a uložte jej do adresáře _DHIS2_HOME_. Toto umístění může být například:

```sh
/home/dhis/config/dhis.conf
```

Konfigurační soubor pro PostgreSQL odpovídající výše uvedenému nastavení má tyto vlastnosti:

```properties
# ------------------------------------------------- ---------------------
# Připojení k databázi
# ------------------------------------------------- ---------------------

# Třída ovladače JDBC
connection.driver_class = org.postgresql.Driver

# URL připojení k databázi
connection.url = jdbc:postgresql:dhis2

# Uživatelské jméno databáze
connection.username = dhis

# Heslo databáze
connection.password = xxxx

# ------------------------------------------------- ---------------------
# Server
# ------------------------------------------------- ---------------------

# Povolit nastavení zabezpečení, pokud je nasazeno na HTTPS, výchozí „off“, může být „on“
server.https = on

# Základní URL serveru
server.base.url = https://server.com/
```

Důrazně se doporučuje povolit nastavení `server.https` a nasadit DHIS 2 přes šifrovaný protokol HTTPS. Toto nastavení umožní např. zabezpečené soubory cookie. Pokud je toto nastavení povoleno, je vyžadováno nasazení HTTPS.

Nastavení `server.base.url` odkazuje na adresu URL, na kterou koncoví uživatelé v síti přistupují k síti.

Konfigurační soubor podporuje proměnné prostředí. To znamená, že můžete nastavit určité vlastnosti jako proměnné prostředí a nechat je vyřešit, např. jako je tento, kde `DHIS2\_HOME` je název proměnné prostředí:

```properties
connection.password = ${DB_PASSWD}
```

Všimněte si, že tento soubor obsahuje heslo pro vaši databázi DHIS2 jako prostý text, takže musí být chráněn před neoprávněným přístupem. Chcete-li to provést, vyvolejte následující příkaz, který zajistí, že jej bude moci číst pouze uživatel _dhis_, který soubor vlastní:

```sh
chmod 0600 dhis.conf
```

### Instalace Java { #install_java_installation }

Doporučený Java JDK pro DHIS 2 je OpenJDK 8. OpenJDK je licencován pod licencí GPL a lze jej spustit zdarma. Můžete jej nainstalovat pomocí následujícího příkazu:

```
sudo apt-get install openjdk-8-jdk
```

Ověřte správnost instalace zadáním:

```
java -version
```

### Instalace Tomcat a DHIS2 { #install_tomcat_dhis2_installation }

K instalaci kontejneru servletu Tomcat použijeme balíček uživatelů Tomcat zadáním:

```sh
sudo apt-get install tomcat8-user
```

Tento balíček umožňuje snadno vytvořit novou instanci Tomcat. Instance bude vytvořena v aktuálním adresáři. Vhodným umístěním je domovský adresář uživatele _dhis_:

```sh
cd /home/dhis/
sudo tomcat8-instance-create tomcat-dhis
sudo chown -R dhis:dhis tomcat-dhis/
```

Tím se vytvoří instance v adresáři s názvem _tomcat-dhis_. Upozorňujeme, že balíček tomcat7-user umožňuje vytvářet libovolný počet instancí dhis, pokud je to požadováno.

Dále upravte soubor _tomcat-dhis/bin/setenv.sh_ a přidejte řádky níže. První řádek nastaví umístění vašeho prostředí Java Runtime Environment, druhý vyhradí paměť Tomcat a třetí nastaví umístění, kde DHIS2 bude hledat konfigurační soubor _dhis.conf_. Zkontrolujte správnost cesty binárních souborů Java, protože se mohou u jednotlivých systémů lišit, např. na systémech AMD můžete vidět _/java-8-openjdk-amd64_ Pamatujte, že byste to měli přizpůsobit svému prostředí:

```sh
export JAVA_HOME='/usr/lib/jvm/java-1.8.0-openjdk-amd64/'
export JAVA_OPTS='-Xmx7500m -Xms4000m'
export DHIS2_HOME='/home/dhis/config'
```

Konfigurační soubor Tomcat je umístěn v _tomcat-dhis/conf/server.xml_. Prvkem, který definuje připojení k DHIS, je prvek _Connector_ s portem 8080. V případě potřeby můžete změnit číslo portu v prvku Connector na požadovaný port. Atribut _relaxedQueryChars_ je nezbytný k povolení určitých znaků v adresách URL používaných frontendem DHIS2.

```xml
<Connector port="8080" protocol="HTTP/1.1"
  connectionTimeout="20000"
  redirectPort="8443"
  relaxedQueryChars="[]" />
```

Dalším krokem je stažení souboru DHIS2 WAR a jeho umístění do adresáře webapps Tomcat. Můžete si stáhnout vydání DHIS2 verze 2.31 WAR takto (v případě potřeby nahraďte 2.31 preferovanou verzí):

```sh
wget https://releases.dhis2.org/2.33/dhis.war
```

Alternativně pro vydání oprav je struktura složek založena na ID vydání oprav v podsložce pod hlavním vydáním. Např. si můžete stáhnout vydání DHIS2 verze 2.31.1 WAR takto (nahraďte 2.31 preferovanou verzí a 2.31.1 preferovanou opravou, pokud je to nutné):

```
wget https://releases.dhis2.org/2.33/2.33.1/dhis.war
```

Přesuňte soubor WAR do adresáře webových serverů Tomcat. Chceme zavolat soubor WAR ROOT.war, aby byl k dispozici na localhost přímo bez kontextové cesty:

```sh
mv dhis.war tomcat-dhis/webapps/ROOT.war
```

DHIS2 by nikdy neměl být spuštěn jako privilegovaný uživatel. Po úpravě souboru setenv.sh upravte spouštěcí skript, abyste zkontrolovali a ověřili, že skript nebyl vyvolán jako root.

```sh
#!/bin/sh
set -e

if [ "$(id -u)" -eq "0" ]; then
  echo "This script must NOT be run as root" 1>&2
  exit 1
fi

export CATALINA_BASE="/home/dhis/tomcat-dhis"
/usr/share/tomcat8/bin/startup.sh
echo "Tomcat started"
```

### Spuštění DHIS2 { #install_running_dhis2 }

DHIS2 lze nyní spustit vyvoláním:

    sudo -u dhis tomcat-dhis/bin/startup.sh

> **Důležité**
>
> Server DHIS2 by nikdy neměl být spuštěn jako root nebo jiný privilegovaný uživatel.

DHIS2 lze zastavit zadáním:

    sudo -u dhis tomcat-dhis/bin/shutdown.sh

Ke sledování chování Tomcatu je primárním zdrojem informací protokol. Protokol lze zobrazit pomocí následujícího příkazu:

    tail -f tomcat-dhis/logs/catalina.out

Za předpokladu, že se soubor WAR nazývá ROOT.war, můžete nyní získat přístup k instanci DHIS2 na následující adrese URL:

    http://localhost:8080

## Konfigurace úložiště souborů { #install_file_store_configuration }

DHIS2 je schopen zachytit a uložit soubory. Ve výchozím nastavení budou soubory uloženy v místním systému souborů serveru, který spouští DHIS2 v adresáři _files_ v umístění externího adresáře _DHIS2_HOME_.

Můžete také nakonfigurovat DHIS2 tak, aby ukládal soubory na cloudových poskytovatelích úložiště. AWS S3 je v současné době jediným podporovaným poskytovatelem. Chcete-li povolit cloudové úložiště, musíte ve svém souboru _dhis.conf_ definovat následující další vlastnosti:

```properties
# File store provider. Currently 'filesystem' and 'aws-s3' are supported.
filestore.provider = 'aws-s3'

# Directory in external directory on local file system and bucket on AWS S3
filestore.container = files

# The following configuration is applicable to cloud storage only (AWS S3)

# Datacenter location. Optional but recommended for performance reasons.
filestore.location = eu-west-1

# Username / Access key on AWS S3
filestore.identity = xxxx

# Password / Secret key on AWS S3 (sensitive)
filestore.secret = xxxx
```

Tato konfigurace je příkladem odrážejícím výchozí hodnoty a měla by být změněna tak, aby vyhovovala vašim potřebám. Jinými slovy to můžete úplně vynechat, pokud plánujete použít výchozí hodnoty. Pokud chcete použít externího poskytovatele, je třeba definovat poslední blok vlastností a vlastnost _provider_ je nastavena na podporovaného poskytovatele (aktuálně pouze AWS S3).

> **Poznámka**
>
> Pokud jste nakonfigurovali cloudové úložiště v dhis.conf, všechny soubory, které nahrajete nebo soubory, které systém generuje, budou používat cloudové úložiště.

U produkčního systému by mělo být počáteční nastavení úložiště souborů pečlivě považováno za přesun souborů mezi poskytovateli úložišť, přičemž zachování integrity odkazů na databázi by mohlo být složité. Mějte na paměti, že obsah úložiště souborů může obsahovat citlivé i integrální informace a chránit přístup ke složce a také zajistit, aby se při produkční implementaci doporučil plán zálohování.

> **Poznámka**
>
> AWS S3 je jediný podporovaný poskytovatel, ale v budoucnu bude pravděpodobně přidáno více poskytovatelů, například Google Cloud Store a Azure Blob Storage. Dejte nám vědět, pokud máte případ použití pro další poskytovatele.

## Konfigurace účtu služby Google { #install_google_service_account_configuration }

DHIS2 se může připojit k různým API služeb Google. Například součást DHIS2 GIS může k načítání mapových vrstev využívat API Google Earth Engine. Chcete-li poskytnout přístupové tokeny API, musíte nastavit účet služby Google a vytvořit soukromý klíč:

-   Vytvořte si účet služby Google. Přečtěte si dokumentaci [Google identify platform](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#overview).

-   Navštivte [cloudovou konzoli Google](https://console.cloud.google.com) a přejděte do API Manager \> Credentials \> Create credentials \> Service account key. Vyberte svůj servisní účet a JSON jako typ klíče a klikněte na Vytvořit.

-   Přejmenujte klíč JSON na _dhis-google-auth.json_.

Po stažení souboru klíče vložte soubor _dhis-google-auth.json_ do adresáře DHIS2_HOME (stejné umístění jako soubor _dhis.conf_). Jako příklad může být toto umístění:

    /home/dhis/config/dhis-google-auth.json

## Konfigurace LDAP { #install_ldap_configuration }

DHIS2 je schopen používat server LDAP k ověřování uživatelů. Pro ověřování LDAP je vyžadováno, aby měl odpovídající uživatel v databázi DHIS2 na položku LDAP. Uživatel DHIS2 bude použit k reprezentaci oprávnění / uživatelských rolí.

Chcete-li nastavit ověřování LDAP, musíte nakonfigurovat adresu URL serveru LDAP, uživatele správce a vyhledávací základnu LDAP a filtr vyhledávání. Tuto konfiguraci je třeba provést v hlavním konfiguračním souboru DHIS 2 (dhis.conf). Uživatelé nebo položky LDAP jsou identifikováni rozlišujícími jmény (DN od nynějška). Příklad konfigurace vypadá takto:

```properties
# LDAP server URL
ldap.url = ldaps://domain.org:636

# LDAP manager entry distinguished name
ldap.manager.dn = cn=johndoe,dc=domain,dc=org

# LDAP manager entry password
ldap.manager.password = xxxx

# LDAP base search
ldap.search.base = dc=domain,dc=org

# LDAP search filter
ldap.search.filter = (cn={0})
```

Vlastnosti konfigurace LDAP jsou vysvětleny níže:

-   _ldap.url: _ URL serveru LDAP, u kterého se má ověřovat. K zajištění autentizace se důrazně doporučuje používat SSL / šifrování. Jako příklad URL je _ldaps: //domain.org:636_, kde ldaps odkazuje na protokol, _domain.org_ odkazuje na název domény nebo IP adresu a _636_ odkazuje na port (636 je výchozí pro LDAPS).

-   _ldap.manager.dn: _ Pro připojení k serveru LDAP je pro proces ověření uživatele vyžadován uživatel správce LDAP. Tato vlastnost odkazuje na DN dané položky. Tj. toto není uživatel, který bude ověřen při přihlášení do DHIS2, ale uživatel, který se k ověření připojí k serveru LDAP.

-   _ldap.manager.password:_ Heslo pro uživatele správce LDAP.

-   _ldap.search.base:_ Vyhledávací základna nebo rozlišující název objektu základny vyhledávání, který definuje umístění v adresáři, ze kterého začíná hledání LDAP.

-   _ldap.search.filter: _ Filtr pro porovnávání DN záznamů v adresáři LDAP. Proměnná {0} bude nahrazena uživatelským jménem DHIS2 nebo alternativně identifikátorem LDAP definovaným pro uživatele s dodaným uživatelským jménem.

DHIS2 použije zadané uživatelské jméno / heslo a pokusí se ho ověřit proti položce serveru LDAP, poté vyhledá uživatelské role / oprávnění od odpovídajícího uživatele DHIS2. To znamená, že uživatel musí mít odpovídající položku v adresáři LDAP, stejně jako uživatel DHIS2, aby se mohl přihlásit.

Během ověřování se DHIS2 pokusí vytvořit vazbu na server LDAP pomocí nakonfigurované adresy URL serveru LDAP a DN správce a hesla. Jakmile je vazba hotová, prohledá položku v adresáři pomocí nakonfigurované báze a filtru vyhledávání LDAP.

Proměnná {0} v nakonfigurovaném filtru bude před použitím filtru nahrazena. Ve výchozím nastavení bude nahrazeno zadaným uživatelským jménem. Můžete také nastavit vlastní identifikátor LDAP na příslušném uživatelském účtu DHIS2. To lze provést prostřednictvím uživatelského rozhraní uživatelského modulu DHIS2 na obrazovce přidání nebo úpravy nastavením vlastnosti „Identifikátor LDAP“. Je-li nastaven, nahradí identifikátor LDAP proměnnou {0} ve filtru. Tato funkce je užitečná, když běžný název LDAP není vhodný nebo jej z nějakého důvodu nelze použít jako uživatelské jméno DHIS2.

## Konfigurace šifrování { #install_encryption_configuration }

DHIS2 umožňuje šifrování dat. To však vyžaduje určité dodatečné nastavení. Pro zajištění bezpečnosti šifrovacího algoritmu budete muset nastavit heslo v konfiguračním souboru _dhis.conf_ prostřednictvím vlastnosti _encryption.password_:

```properties
encryption.password = xxxx
```

Vlastnost _encryption.password_ je heslo používané při šifrování a dešifrování dat v databázi. Pamatujte, že heslo se po nastavení a zašifrování dat nesmí měnit, protože data již nelze dešifrovat.

Heslo musí mít alespoň **24 znaků**. Doporučuje se kombinace čísel a malých a velkých písmen. Šifrovací heslo musí zůstat v tajnosti.

> **Důležité**
>
> Upozornění: Pokud dojde ke ztrátě nebo změně šifrovacího hesla, není možné obnovit šifrovaná data. Pokud se ztratí heslo, ztratí se i zašifrovaná data. Šifrování naopak neposkytuje žádné zabezpečení, pokud je heslo prozrazeno. Proto je třeba věnovat velkou pozornost uložení hesla na bezpečném místě.

## Přečtěte si konfiguraci replikace databáze { #install_read_replica_configuration }

DHIS 2 umožňuje využití replik hlavní databáze (hlavní databáze DHIS 2) pouze pro čtení. Účelem čtení replik je zvýšit výkon dotazů na čtení databáze a zvýšit kapacitu nad rámec omezení jedné databáze. Z toho budou těžit operace náročné na čtení, jako jsou analýzy a dotazy na události.

Konfigurace vyžaduje, abyste vytvořili jednu nebo více replikovaných instancí hlavní databáze DHIS 2. PostgreSQL toho dosahuje prostřednictvím konceptu označovaného jako _streaming replication_. Tato příručka se nezabývá konfigurací replik pro čtení pro PostgreSQL.

Číst repliky lze definovat v konfiguračním souboru _dhis.conf_. Můžete zadat až 5 přečtených replik na instanci DHIS 2. Každá přečtená replika je označena číslem od 1 do 5. Pro každou repliku musí být definována adresa URL připojení JDBC. Lze zadat uživatelské jméno a heslo; pokud ne, bude místo toho použito uživatelské jméno a heslo pro hlavní databázi.

Konfigurace pro čtení replik v souboru _dhis.conf_ vypadá níže. Každá replika je specifikována předponou konfiguračního klíče _readN_, kde N odkazuje na číslo repliky.

```properties
# Read replica 1 configuration

# Database connection URL, username and password
read1.connection.url = jdbc:postgresql://127.0.0.11/dbread1
read1.connection.username = dhis
read1.connection.password = xxxx

# Read replica 2 configuration

# Database connection URL, username and password
read2.connection.url = jdbc:postgresql://127.0.0.12/dbread2
read2.connection.username = dhis
read2.connection.password = xxxx

# Read replica 3 configuration

# Database connection URL, fallback to master for username and password
read3.connection.url = jdbc:postgresql://127.0.0.13/dbread3
```

Změny se projeví až po restartování kontejneru servletu. DHIS 2 automaticky distribuuje zátěž mezi přečtené repliky. Pořadí replik nemá žádný význam.

## Konfigurace clusteru webového serveru { #install_web_server_cluster_configuration }

Tato část popisuje, jak nastavit aplikaci DHIS 2 na spuštění v clusteru.

### Přehled clusterování { #install_cluster_configuration_introduction }

Klastrování neboli clustering je běžná technika pro zlepšení škálovatelnosti a dostupnosti systému. Clustering označuje nastavení více webových serverů, jako jsou instance Tomcat, a jejich poskytování jednou aplikací. Clustering umožňuje _škálování_ aplikace v tom smyslu, že je možné přidat nové servery ke zlepšení výkonu. Umožňuje také _vysokou dostupnost_, protože systém může tolerovat případy selhání, aniž by byl systém pro uživatele nepřístupný.

Existuje několik aspektů ke konfiguraci, aby bylo možné spustit DHIS 2 v clusteru.

-   Každá instance DHIS 2 musí specifikovat ostatní členy instance DHIS 2 clusteru v souboru _dhis.conf_.

-   Musí být nainstalováno úložiště dat Redis a musí být poskytnuty informace o připojení pro každou instanci aplikace DHIS 2 v souboru _dhis.conf_.

-   Instance a servery DHIS 2 musí sdílet stejnou složku _files_, která se používá pro nahrávání aplikací a souborů, a to buď prostřednictvím možnosti _AWS S3 cloud filestorage_, nebo prostřednictvím sdílené síťové jednotky.

-   Vyrovnávač zatížení, jako je nginx, musí být nakonfigurován tak, aby distribuoval webové požadavky napříč instancemi clusteru.

### Konfigurace clusteru instance DHIS 2 { #install_cluster_configuration }

Při nastavování více instancí Tomcat je třeba si tyto instance navzájem uvědomovat. Toto povědomí umožní serveru DHIS 2 udržovat mezipaměti místních dat (hibernované) synchronizované a v konzistentním stavu. Když je aktualizace provedena v jedné instanci, musí být mezipaměti v ostatních instancích oznámeny, aby je bylo možné zneplatnit a vyhnout se zastarání.

Nastavení clusteru DHIS 2 je založeno na ruční konfiguraci každé instance. Pro každou instanci DHIS 2 je nutné zadat veřejný _hostname_ a také názvy hostitelů ostatních instancí účastnících se v klastru.

Název hostitele serveru je určen pomocí vlastnosti konfigurace _cluster.hostname_. Další servery, které se účastní klastru, se zadávají pomocí vlastnosti konfigurace _cluster.members_. Vlastnost očekává seznam hodnot oddělených čárkami, kde každá hodnota má formát _host:port_.

Název hostitele musí být viditelný pro zúčastněné servery v síti, aby cluster fungoval. Možná budete muset povolit příchozí a odchozí připojení na nakonfigurovaných číslech portů ve firewallu.

Číslo portu serveru se zadává pomocí vlastnosti konfigurace _cluster.cache.port_. Port vzdáleného objektu používaný pro přijímání volání registru je určen pomocí _cluster.cache.remote.object.port_. Zadání čísel portů je obvykle užitečné pouze v případě, že máte na jednom serveru více instancí clusteru nebo pokud potřebujete explicitně určit porty, aby odpovídaly konfiguraci brány firewall. Při spouštění instancí clusteru na samostatných serverech je často vhodné použít výchozí číslo portu a vynechat vlastnosti konfigurace portů. Pokud je vynechán, bude 4001 přiřazen jako port posluchače a náhodný volný port bude přiřazen jako port vzdáleného objektu.

Níže je popsáno příklad nastavení pro cluster dvou webových serverů. Pro _server A_ dostupný na názvu hostitele _193.157.199.131_ lze v _dhis.conf_ zadat následující:

```properties
# Cluster configuration for server A

# Hostname for this web server
cluster.hostname = 193.157.199.131

# Ports for cache listener, can be omitted
cluster.cache.port = 4001
cluster.cache.remote.object.port = 5001

# List of Host:port participating in the cluster
cluster.members = 193.157.199.132:4001
```

Pro _server B_ dostupný na hostname _193.157.199.132_ lze v _dhis.conf_ zadat následující (všimněte si, jak je vynechána konfigurace portů):

```properties
# Cluster configuration for server B

# Hostname for this web server
cluster.hostname = 193.157.199.132

# List of servers participating in cluster
cluster.members = 193.157.199.131:4001
```

Aby se změny projevily, musíte restartovat každou instanci Tomcat. Tyto dvě instance se nyní navzájem informovaly a DHIS 2 zajistí, že jejich mezipaměti budou synchronizovány.

### Znovu zadejte konfiguraci clusteru sdíleného úložiště dat { #install_cluster_configuration_redis }

V nastavení clusteru je vyžadována instance _Redis_ a bude zpracovávat sdílené relace uživatelů, mezipaměť aplikací a vedení uzlu clusteru.

Pro optimální výkon je třeba na serveru Redis povolit _Redis Keyspace events_ pro _generic commands_ a _expired events_. Pokud používáte server Redis spravovaný cloudovou platformou (například _AWS ElastiCache pro Redis_ nebo _Azure Cache pro Redis_), budete muset povolit upozornění na události klíčového prostoru pomocí příslušných rozhraní cloudové konzoly. Pokud nastavujete samostatný server Redis, povolení oznámení událostí klíčového prostoru lze provést v souboru _redis.conf_ přidáním nebo odkomentováním následujícího řádku:

```
notify-keyspace-events Egx
```

DHIS2 se připojí k Redis, pokud je vlastnost _redis.enabled_ konfigurace v _dhis.conf_ nastavena na _true_ spolu s následujícími vlastnostmi:

-   _redis.host_: Určuje, kde je spuštěn server redis. Výchozí hodnota pro _localhost_. Povinné.

-   _redis.port_: Určuje port, na kterém naslouchá server redis. Výchozí hodnota je _6379_. Volitelné.

-   _redis.password_: Určuje ověřovací heslo. Pokud heslo není požadováno, může být ponecháno prázdné.

-   _redis.use.ssl_: Určuje, zda má server Redis povoleno SSL. Výchozí hodnota je false. Volitelný. Výchozí hodnota je _false_.

Když je povolen Redis, DHIS2 automaticky přiřadí jednu z běžících instancí jako vedoucí clusteru. Vedoucí instance bude použita k provádění úloh nebo naplánovaných úloh, které by měly být spouštěny výhradně jednou instancí. Volitelně můžete nakonfigurovat vlastnost _leader.time.to.live.minutes_ v _dhis.conf_ a nastavit, jak často musí volby vůdce nastat. Poskytuje také indikaci, jak dlouho by trvalo, než by se další vůdce stal vůdcem poté, co byl předchozí vůdce nedostupný. Výchozí hodnota je 2 minuty. Přiřazení odkazu v clusteru se provádí pouze v případě, že je povolen Redis. Níže je uveden ukázkový fragment konfiguračního souboru _dhis.conf_ s povoleným Redisem a nakonfigurovaným časem voleb vedoucího.

```properties
# Redis Configuration

redis.enabled = true

redis.host = 193.158.100.111

redis.port = 6379

redis.password = <your password>

redis.use.ssl = false

# Optional, defaults to 2 minutes
leader.time.to.live.minutes=4
```

### Konfigurace složky souborů { #files-folder-configuration }

DHIS 2 bude ukládat několik typů souborů mimo samotnou aplikaci, například aplikace, soubory uložené v zadávání dat a uživatelské avatary. Při nasazení v clusteru musí být umístění těchto souborů sdíleno ve všech instancích. V místním souborovém systému je umístění:

```
{DHIS2_HOME}/files
```

Zde `DHIS2_HOME` odkazuje na umístění konfiguračního souboru DHIS 2, jak je uvedeno v proměnné prostředí DHIS 2, a `files` je složka souborů bezprostředně níže.

Existují dva způsoby, jak dosáhnout sdíleného umístění:

-   Použijte možnost cloudového úložiště _AWS S3_. Soubory budou uloženy v bucketu S3, který je automaticky sdílen všemi instancemi DHIS 2 v clusteru. Pokyny najdete v sekci _File store configuration_.
-   Nastavte sdílenou složku, která je sdílena mezi všemi instancemi DHIS 2 a servery v klastru. V systému Linux toho lze dosáhnout pomocí _NFS_ (Network File System), což je protokol distribuovaného systému souborů. Mějte na paměti, že by měla být sdílena pouze podsložka `soubory` v rámci `DHIS2_HOME`, nikoli nadřazená složka.

### Konfigurace nástroje pro vyrovnávání zatížení { #install_load_balancing }

S nastaveným clusterem instancí Tomcat běžný přístup pro směrování příchozích webových požadavků na back-endové instance účastnící se v clusteru používá _load balancer_. Nástroj pro vyrovnávání zatížení zajistí, že zatížení bude distribuováno rovnoměrně mezi instance clusteru. Zjistí také, zda se instance stane nedostupnou, a pokud ano, zastaví rutinní požadavky na tuto instanci a místo toho použije jiné dostupné instance.

Vyrovnávání zatížení lze dosáhnout několika způsoby. Jednoduchý přístup používá _nginx_, v takovém případě definujete _upstream_ prvek, který vytvoří výčet umístění instancí back-endu a později tento prvek použijete v _proxy_ umístění bloku.

```text
http {

  # Upstream element with sticky sessions

  upstream dhis_cluster {
    ip_hash;
    server 193.157.199.131:8080;
    server 193.157.199.132:8080;
  }

  # Proxy pass to backend servers in cluster

  server {
    listen 80;

    location / {
      proxy_pass   http://dhis_cluster/;
    }
  }
}
```

DHIS 2 udržuje stav serveru na straně relace uživatele v omezené míře. Použití „sticky sessions“ je jednoduchý přístup k zabránění replikace stavu relace serveru směrováním požadavků od stejného klienta na stejný server. Direktiva _ip_hash_ v upstream prvku to zajišťuje.

Ve výše uvedeném příkladu bylo z důvodu stručnosti vynecháno několik pokynů. Podrobný průvodce najdete v části reverzní proxy.

## Konfigurace mezipaměti Analytiky { #install_analytics_cache_configuration }

DHIS 2 podporuje mezipaměť na straně serveru pro odpovědi analytického rozhraní API, kterou používají všechny analytické webové aplikace. Tato mezipaměť je umístěna v aplikaci DHIS 2, a proto je chráněna vrstvou ověřování a zabezpečení DHIS 2. Můžete nakonfigurovat vypršení platnosti položek v mezipaměti během několika sekund. Chcete-li povolit mezipaměť, můžete definovat vlastnost `analytics.cache.expiration` v souboru `dhis.conf`. Níže uvedený příklad povolil mezipaměť a nastavil vypršení platnosti na jednu hodinu.

```properties
analytics.cache.expiration = 3600
```

## Monitoring { #monitoring }

DHIS 2 může exportovat metriky kompatibilní s Prometheus pro monitorování instancí DHIS2. Monitorovací infrastruktura DHIS2 je navržena k vystavení metrik souvisejících s běhovým modulem aplikace a dalších informací souvisejících s aplikací.

Metriky související s infrastrukturou (například metriky hostitele, Tomcat nebo Postgres) nejsou přímo vystaveny monitorovacím modulem aplikace a je třeba je shromažďovat samostatně. Metriky aktuálně vystavené aplikací jsou:

-   DHIS 2 API (doba odezvy, počet hovorů atd.)
-   JVM (Heap size, Garbage collection, etc.)
-   Hibernate (Queries, cache, etc)
-   C3P0 Database pool
-   Doba provozu aplikace
-   CPU

Monitorování lze povolit v souboru `dhis.conf` s následujícími vlastnostmi (výchozí nastavení je u všech vlastností `off` ):

```properties
monitoring.api.enabled = on
monitoring.jvm.enabled = on
monitoring.dbpool.enabled = on
monitoring.hibernate.enabled = off
monitoring.uptime.enabled = on
monitoring.cpu.enabled = on
```

Doporučený přístup pro shromažďování a vizualizaci těchto metrik je prostřednictvím Prometheus a Grafana. Další informace naleznete v kapitole [monitorovací infrastruktura](https://github.com/dhis2/wow-backend/blob/master/guides/monitoring.md) page and the [Prometheus and Grafana install](https://docs.dhis2.org/master/en/dhis2_system_administration_guide/monitoring.html).

## Konfigurace reverzní proxy { #install_reverse_proxy_configuration }

Reverzní proxy je proxy server, který jedná jménem serveru. Použití reverzního serveru proxy v kombinaci s kontejnerem servletu je volitelné, ale má mnoho výhod:

-   Požadavky lze mapovat a předávat do více kontejnerů servletů. To zlepšuje flexibilitu a usnadňuje spuštění více instancí DHIS2 na stejném serveru. Umožňuje také změnit nastavení interního serveru bez ovlivnění klientů.

-   Aplikaci DHIS2 lze spustit jako uživatel bez oprávnění root na jiném portu než 80, což snižuje důsledky únosu relace.

-   Reverzní proxy server může fungovat jako jeden server SSL a může být nakonfigurován tak, aby kontroloval požadavky na škodlivý obsah, protokoloval požadavky a odpovědi a poskytoval necitlivé chybové zprávy, které zlepší zabezpečení.

### Základní nastavení nginx { #install_basic_nginx_setup }

Doporučujeme použít [nginx](http://www.nginx.org) jako reverzní proxy kvůli jeho nízké paměťové náročnosti a snadnému použití. Chcete-li nainstalovat, zadejte následující:

    sudo apt-get install nginx

nginx lze nyní spustit, znovu načíst a zastavit pomocí následujících příkazů:

    sudo /etc/init.d/nginx start
    sudo /etc/init.d/nginx reload
    sudo /etc/init.d/nginx stop

Nyní, když jsme nainstalovali nginx, budeme pokračovat v konfiguraci regulárního proxy serveru požadavků na naši instanci Tomcat, o kterém předpokládáme, že běží na _http://localhost:8080_. Ke konfiguraci nginx můžete otevřít konfigurační soubor zadáním:

    sudo nano /etc/nginx/nginx.conf

Konfigurace nginx je postavena na hierarchii bloků představujících http, server a umístění, kde každý blok dědí nastavení z nadřazených bloků. Následující fragment kódu nakonfiguruje požadavky nginx na proxy pass (redirect) z portu 80 (což je port, který bude nginx naslouchat ve výchozím nastavení) naší instanci Tomcat. Zahrňte následující konfiguraci do nginx.conf:

```text
http {
  gzip on; # Enables compression, incl Web API content-types
  gzip_types
    "application/json;charset=utf-8" application/json
    "application/javascript;charset=utf-8" application/javascript text/javascript
    "application/xml;charset=utf-8" application/xml text/xml
    "text/css;charset=utf-8" text/css
    "text/plain;charset=utf-8" text/plain;

  server {
    listen               80;
    client_max_body_size 10M;

    # Proxy pass to servlet container

    location / {
      proxy_pass                http://localhost:8080/;
      proxy_redirect            off;
      proxy_set_header          Host               $host;
      proxy_set_header          X-Real-IP          $remote_addr;
      proxy_set_header          X-Forwarded-For    $proxy_add_x_forwarded_for;
      proxy_set_header          X-Forwarded-Proto  http;
      proxy_buffer_size         128k;
      proxy_buffers             8 128k;
      proxy_busy_buffers_size   256k;
      proxy_cookie_path         ~*^/(.*) "/$1; SameSite=Lax";
    }
  }
}
```

Nyní můžete získat přístup k instanci DHIS2 na adrese _http://localhost_. Vzhledem k tomu, že byl nastaven reverzní proxy server, můžeme zlepšit zabezpečení tím, že Tomcat naslouchá pouze místním připojením. V  _/conf/server.xml_ můžete přidat atribut _address_ s hodnotou _localhost_ do elementu Connector pro HTTP 1.1 takto:

```xml
<Connector address="localhost" protocol="HTTP/1.1" />
```

### Povolení SSL s nginx { #install_enabling_ssl_on_nginx }

Za účelem zlepšení zabezpečení se doporučuje nakonfigurovat server se spuštěným serverem DHIS2 tak, aby komunikoval s klienty přes šifrované připojení a aby se klientům identifikoval pomocí důvěryhodného certifikátu. Toho lze dosáhnout pomocí SSL, což je kryptografický komunikační protokol běžící nad TCP / IP. Nejprve nainstalujte požadovanou knihovnu _openssl_:

    sudo apt-get install openssl

Ke konfiguraci nginx pro použití SSL budete potřebovat správný certifikát SSL od poskytovatele SSL. Cena certifikátu se velmi liší v závislosti na síle šifrování. Cenově dostupný certifikát od [Rapid SSL Online](http://www.rapidsslonline.com) by měl sloužit většině účelů. Chcete-li vygenerovat (žádost o podepsání certifikátu), můžete zadat níže uvedený příkaz. Když se zobrazí výzva k zadání _Common Name_, zadejte plně kvalifikovaný název domény webu, který zajišťujete.

    openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr

Když jste obdrželi své soubory certifikátů (.pem nebo .crt), budete je muset umístit společně s vygenerovaným souborem server.key na místo, které je dosažitelné pomocí nginx. Dobrým místem pro to může být stejný adresář, ve kterém je umístěn váš soubor nginx.conf.

Níže je blok serveru nginx, kde jsou soubory certifikátů pojmenovány server.crt a server.key. Vzhledem k tomu, že připojení SSL se obvykle vyskytuje na portu 443 (HTTPS), předáváme požadavky na tomto portu (443) na instanci DHIS2 běžící na  _http://localhost:8080_ První blok serveru přepíše všechny požadavky na připojení k portu 80 a vynutí použití protokolu HTTPS/SSL. To je také nutné, protože DHIS2 interně používá mnoho přesměrování, která musí být předána, aby bylo možné používat HTTPS. Nezapomeňte nahradit _\<server-ip\>_ IP vašeho serveru. Tyto bloky by měly nahradit blok z předchozí části.

```text
http {
  gzip on; # Enables compression, incl Web API content-types
  gzip_types
    "application/json;charset=utf-8" application/json
    "application/javascript;charset=utf-8" application/javascript text/javascript
    "application/xml;charset=utf-8" application/xml text/xml
    "text/css;charset=utf-8" text/css
    "text/plain;charset=utf-8" text/plain;

  # HTTP server - rewrite to force use of SSL

  server {
    listen     80;
    rewrite    ^ https://<server-url>$request_uri? permanent;
  }

  # HTTPS server

  server {
    listen               443 ssl;
    client_max_body_size 10M;

    ssl                  on;
    ssl_certificate      server.crt;
    ssl_certificate_key  server.key;

    ssl_session_cache    shared:SSL:20m;
    ssl_session_timeout  10m;

    ssl_protocols              TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers                RC4:HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers  on;

    # Proxy pass to servlet container

    location / {
      proxy_pass                http://localhost:8080/;
      proxy_redirect            off;
      proxy_set_header          Host               $host;
      proxy_set_header          X-Real-IP          $remote_addr;
      proxy_set_header          X-Forwarded-For    $proxy_add_x_forwarded_for;
      proxy_set_header          X-Forwarded-Proto  https;
      proxy_buffer_size         128k;
      proxy_buffers             8 128k;
      proxy_busy_buffers_size   256k;
      proxy_cookie_path         ~*^/(.*) "/$1; SameSite=Lax";
    }
  }
}
```

Poznamenejte si poslední hodnotu záhlaví `https`, která je vyžadována k informování kontejneru servletu, že požadavek přichází přes HTTPS. Aby Tomcat mohl správně vytvářet záhlaví URL `Location` pomocí HTTPS, musíte také přidat další dva parametry do Connector v souboru Tomcat `server.xml`:

```xml
<Connector scheme="https" proxyPort="443" />
```

### Povolení ukládání do mezipaměti pomocí nginx { #install_enabling_caching_ssl_nginx }

Odpovědi na žádosti o hlášení zpráv, grafy, mapy a další zdroje související s analýzou bude nějakou dobu trvat a může využívat mnoho serverových prostředků. Abychom zlepšili dobu odezvy, snížili zátěž serveru a skryli potenciální výpadky serveru, můžeme v nastavení serveru zavést proxy cache. Obsah v mezipaměti bude uložen v adresáři /var/cache/nginx a bude přiděleno až 250 MB úložiště. Nginx vytvoří tento adresář automaticky.

```text
http {
  ..
  proxy_cache_path  /var/cache/nginx  levels=1:2  keys_zone=dhis:250m  inactive=1d;


  server {
    ..

    # Proxy pass to servlet container and potentially cache response

    location / {
      proxy_pass                http://localhost:8080/;
      proxy_redirect            off;
      proxy_set_header          Host               $host;
      proxy_set_header          X-Real-IP          $remote_addr;
      proxy_set_header          X-Forwarded-For    $proxy_add_x_forwarded_for;
      proxy_set_header          X-Forwarded-Proto  https;
      proxy_buffer_size         128k;
      proxy_buffers             8 128k;
      proxy_busy_buffers_size   256k;
      proxy_cookie_path         ~*^/(.*) "/$1; SameSite=Lax";
      proxy_cache               dhis;
    }
  }
}
```

> **Důležité**
>
> Uvědomte si, že mezipaměť na straně serveru zkratuje funkce zabezpečení DHIS2 v tom smyslu, že požadavky, které narazí na mezipaměť na straně serveru, budou obsluhovány přímo z mezipaměti mimo kontrolu DHIS2 a kontejneru servletu. To znamená, že adresy URL požadavku lze uhodnout a zprávy načíst z mezipaměti neoprávněnými uživateli. Pokud tedy pořizujete citlivé informace, nastavení mezipaměti na straně serveru se nedoporučuje.

### Omezení rychlosti pomocí nginx { #install_rate_limiting }

Některá volání webového rozhraní API v DHIS 2, jako jsou rozhraní API pro `analytics`, jsou náročná na výpočet. Ve výsledku je výhodné hodnotit omezení těchto API, aby všichni uživatelé systému mohli využívat spravedlivý podíl prostředků serveru. Omezení rychlosti lze dosáhnout pomocí `nginx`. Existuje mnoho přístupů k dosažení omezení rychlosti a toto je určeno k dokumentaci přístupu založeného na nginx.

Níže uvedená konfigurace nginx bude hodnotit omezení webového API  `analytics` a má následující prvky na úrovni bloku _http_ a _location_ (konfigurace je zkrácena z důvodu stručnosti):

```text
http {
  ..
  limit_req_zone $binary_remote_addr zone=limit_analytics:10m rate=5r/s;

  server {
    ..

    location ~ ^/api/(\d+/)?analytics(.*)$ {
      limit_req    zone=limit_analytics burst=20;
      proxy_pass   http://localhost:8080/api/$1analytics$2$is_args$args;
      ..
    }
  }
}
```

Různé prvky konfigurace lze popsat jako:

-   _limit_req_zone $binary_remote_addr_: Omezení rychlosti se provádí na IP žádost.
-   _zone=limit_analytics:20m_: Zóna limitu rychlosti pro analytické API, která pojme až 10 MB IP adres požadavku.
-   _rate=20r/s_: Každému IP je uděleno 5 požadavků za sekundu.
-   _location ~ ^/api/(\d+/)?analytics(.\*)$_: Požadavky na koncový bod analytického rozhraní API jsou omezeny.
-   _burst=20_: Skupiny až 20 požadavků budou zařazeny do fronty a obsluhovány později; další požadavky povedou k `503`.

Úplné vysvětlení najdete v [dokumentaci nginx](https://www.nginx.com/blog/rate-limiting-nginx/).

### Zpřístupnění zdrojů pomocí nginx { #install_making_resources_available_with_nginx }

V některých scénářích je žádoucí zpřístupnit určité prostředky veřejně na webu bez nutnosti ověřování. Jedním z příkladů je, když chcete zpřístupnit prostředky související s analýzou dat ve webovém rozhraní API dostupné na webovém portálu. Následující příklad umožní přístup k grafům, mapám, sestavám, tabulkám sestav a prostředkům dokumentů prostřednictvím základního ověřování vložením záhlaví _Authorization_ HTTP do požadavku. Odstraní záhlaví Cookie z požadavku a záhlaví Set-Cookie z odpovědi, aby se zabránilo změně aktuálně přihlášeného uživatele. Doporučuje se vytvořit uživatele pro tento účel pouze s minimálním požadovaným oprávněním. Hodnota Authorization může být vytvořena zakódováním Base64 uživatelského jména připojeného dvojtečkou a heslem a předponou „Basic“, přesněji "Basic base64_encode(username:password)". Zkontroluje metodu HTTP použitou pro požadavky a vrátí _405 Metoda není povolena_, pokud je detekováno cokoli jiného než GET.

Při použití tohoto přístupu může být výhodné nastavit pro tyto veřejné uživatele samostatnou doménu. Je to proto, že nechceme změnit přihlašovací údaje pro již přihlášené uživatele při přístupu k veřejným prostředkům. Například když je váš server nasazen na somedomain.com, můžete nastavit vyhrazenou subdoménu na api.somedomain.com a nasměrovat adresy URL ze svého portálu na tuto subdoménu.

```text
http {
  ..

  server {
    listen       80;
    server_name  api.somedomain.com;

    location ~ ^/(api/(charts|chartValues|reports|reportTables|documents|maps|organisationUnits)|dhis-web-commons/javascripts|images|dhis-web-commons-ajax-json|dhis-web-mapping|dhis-web-visualizer) {
    if ($request_method != GET) {
        return 405;
      }

      proxy_pass         http://localhost:8080;
      proxy_redirect     off;
      proxy_set_header   Host               $host;
      proxy_set_header   X-Real-IP          $remote_addr;
      proxy_set_header   X-Forwarded-For    $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto  http;
      proxy_set_header   Authorization      "Basic YWRtaW46ZGlzdHJpY3Q=";
      proxy_set_header   Cookie             "";
      proxy_hide_header  Set-Cookie;
    }
  }
}
```

## Odkaz na konfiguraci DHIS2 { #install_dhis2_configuration_reference }

Následující text popisuje úplnou sadu možností konfigurace pro konfigurační soubor _dhis.conf_. Konfigurační soubor by měl být umístěn v adresáři, na který odkazuje proměnná prostředí _DHIS2_HOME_.

> **Poznámka**
>
> Tento konfigurační soubor byste se neměli pokoušet použít přímo, ale použijte jej jako referenci pro dostupné možnosti konfigurace. Mnoho vlastností je volitelných.

```properties
# ------------------------------------------------- ---------------------
# Připojení k databázi pro PostgreSQL [Povinné]
# ------------------------------------------------- ---------------------

# Hibernace SQL dialekt
connection.dialekt = org.hibernate.dialekt.PostgreSQLDialect

# Třída ovladače JDBC
connection.driver_class = org.postgresql.Driver

# URL připojení k databázi
connection.url = jdbc:postgresql:dhis2

# Uživatelské jméno databáze
connection.username = dhis

# Heslo databáze (citlivé)
connection.password = xxxx

# Maximální velikost fondu připojení (výchozí: 40)
connection.pool.max_size = 40

# ------------------------------------------------- ---------------------
# Připojení k databázi pro PostgreSQL [Volitelné]
# ------------------------------------------------- ---------------------

# Minimální počet připojení, které fond bude udržovat v daném čase (výchozí: 5).
connection.pool.min_size=5

# Počáteční velikost fondu připojení (výchozí: 5)
# Počet připojení kolik se fond pokusí získat při spuštění. Mělo by být mezi minPoolSize a maxPoolSize
connection.pool.initial_size=5

# Určuje, kolik připojení najednou se pokusí získat, když je fond vyčerpán.
connection.pool.acquire_incr=5

# Počet sekund kdy připojení může zůstat sdružené, ale nevyužité, než bude vyřazeno. Nula znamená, že nečinná připojení nikdy nevyprší. (výchozí: 7200)
connection.pool.max_idle_time=7200

# Počet sekund, po které by připojení překračující minPoolSize měla zůstat nečinná ve fondu, než budou vyřazena (výchozí: 0)
connection.pool.max_idle_time_excess_con=0

# Pokud je toto číslo větší než 0, dhis2 otestuje všechna nečinná, sdružená, ale neodhlášená připojení, každých tento počet sekund. (výchozí: 0)
connection.pool.idle.con.test.period=0

#Pokud je pravda, při každé kontrole připojení bude provedena operace k ověření platnosti připojení. (výchozí: false)
connection.pool.test.on.checkout=false

#Pokud je hodnota true, při každém přihlášení k připojení bude asynchronně provedena operace k ověření platnosti připojení. (výchozí: true)
connection.pool.test.on.checkin=true

#Definuje dotaz, který bude proveden pro všechny testy připojení. V ideálním případě není tato konfigurace potřeba, protože ovladač postgresql již poskytuje efektivní testovací dotaz. Konfigurace je vystavena pouze pro vyhodnocení, nepoužívejte ji, pokud k tomu není důvod.
connection.pool.preferred.test.query=select 1

#Nakonfigurujte počet pomocných vláken používaných dhis2 pro operace jdbc. (výchozí: 3)
connection.pool.num.helper.threads=3

# ------------------------------------------------- ---------------------
# Server [Povinné]
# ------------------------------------------------- ---------------------

# Základní URL k instanci DHIS 2
server.base.url = https://play.dhis2.org/dev

# Povolit nastavení zabezpečení, pokud je systém nasazen na HTTPS, může být „off“, „on“
server.https = off

# ------------------------------------------------- ---------------------
# Systém [Volitelné]
# ------------------------------------------------- ---------------------

# Systémový režim pouze pro operace čtení databáze, může být „off“, „on“
system.read_only_mode = off

# Časový limit relace v sekundách, výchozí hodnota je 3600
system.session.timeout = 3600

# SQL zobrazení chráněných tabulek, může být „on“, „off“
system.sql_view_table_protection = on

# ------------------------------------------------- ---------------------
# Šifrování [Volitelné]
# ------------------------------------------------- ---------------------

# Šifrovací heslo (citlivé)
encryption.password = xxxx

# ------------------------------------------------- ---------------------
# Úložiště souborů [Volitelné]
# ------------------------------------------------- ---------------------

# Poskytovatel úložiště souborů, aktuálně je podporován 'filesystem' a 'aws-s3'
filestore.provider = filesystem

# Název adresáře / bucketu, složka pod DHIS2_HOME v systému souborů, 'bucket' na AWS S3
filestore.container = files

# Umístění datového centra (není vyžadováno)
filestore.location = eu-west-1

# Veřejná identita / uživatelské jméno
filestore.identity = dhis2-id

# Tajný klíč / heslo (citlivé)
filestore.secret = xxxx

# ------------------------------------------------- ---------------------
# LDAP [Volitelné]
# ------------------------------------------------- ---------------------

# URL serveru LDAP
ldap.url = ldaps://300.20.300.20:636

# Rozlišující jméno uživatele správce LDAP
ldap.manager.dn = cn=JohnDoe,ou=Country,ou=Admin,dc=hisp,dc=org

# Uživatelské heslo správce LDAP (citlivé)
ldap.manager.password = xxxx

# LDAP záznam rozlišující jméno vyhledávací základna
ldap.search.base = dc=hisp,dc=org

# Filtr rozlišujícího názvu položky LDAP
ldap.search.filter = (cn={0})

# ------------------------------------------------- ---------------------
# Uzel [Volitelné]
# ------------------------------------------------- ---------------------

# Identifikátor uzlu, volitelný, užitečný v clusterech
node.id = 'node-1'

# ------------------------------------------------- ---------------------
# Analytics [Volitelné]
# ------------------------------------------------- ---------------------

# Vypršení mezipaměti na straně serveru Analytics během několika sekund
analytics.cache.expiration = 3600

# ------------------------------------------------- ---------------------
# Monitorování systému [Volitelné]
# ------------------------------------------------- ---------------------

# Adresa URL pro monitorování systému
system.monitoring.url =

# Uživatelské jméno pro monitorování systému
system.monitoring.username =

# Heslo monitorování systému (citlivé)
system.monitoring.password = xxxx
```

## Protokolování aplikací { #install_application_logging }

Tato část popisuje protokolování aplikací v DHIS 2.

### soubory protokolů { #log-files }

Výstup protokolu aplikace DHIS2 je směrován do více souborů a umístění. Nejprve je výstup protokolu odeslán na standardní výstup. Kontejner servletu Tomcat obvykle vydává standardní výstup do souboru pod položkou „logs“:

    <tomcat-dir>/logs/catalina.out

Zadruhé, výstup protokolu se zapíše do adresáře „logs“ v domovském adresáři DHIS2, jak je definován proměnnými prostředí DHIS2_HOME. K dispozici je hlavní soubor protokolu pro všechny výstupy a samostatné soubory protokolu pro různé procesy na pozadí. Hlavní soubor obsahuje také protokoly procesu na pozadí. Soubory protokolu jsou omezeny na 50 Mb a obsah protokolu je průběžně doplńován.

    <DHIS2_HOME>/logs/dhis.log
    <DHIS2_HOME>/logs/dhis-analytics-table.log
    <DHIS2_HOME>/logs/dhis-data-exchange.log
    <DHIS2_HOME>/logs/dhis-data-sync.log

### Konfigurace protokolu { #log-configuration }

Chcete-li přepsat výchozí konfiguraci protokolu, můžete určit vlastnost systému Java s názvem _log4j.configuration_ a hodnotou ukazující na konfigurační soubor Log4j na cestě ke třídě. Pokud chcete ukázat na soubor v systému souborů (tj. Mimo Tomcat), můžete použít předponu _file_ např. takhle:

```properties
-Dlog4j.configuration=file:/home/dhis/config/log4j.properties
```

Vlastnosti systému Java lze nastavit např. prostřednictvím proměnné prostředí _JAVA_OPTS_ nebo ve spouštěcím skriptu tomcat.

Druhým přístupem k přepsání konfigurace protokolu je zadání vlastností protokolování v konfiguračním souboru _dhis.conf_. Podporované vlastnosti jsou:

```properties
# Max size for log files, default is '100MB'
logging.file.max_size = 250MB

# Max number of rolling log archive files, default is 0
logging.file.max_archives = 2
```

DHIS2 nakonec vyřadí protokolování na standardní out / catalina.out a jako výsledek se doporučuje spoléhat se na protokoly pod DHIS2_HOME.

## Práce s databází PostgreSQL { #install_working_with_the_postgresql_database }

Běžnými operacemi při správě instance DHIS2 jsou výpis a obnova databází. Chcete-li vytvořit výpis (kopii) své databáze, za předpokladu, že je nastavení z instalační části, můžete zadat následující:

    pg_dump dhis2 -U dhis -f dhis2.sql

První argument (dhis2) odkazuje na název databáze. Druhý argument (dhis) odkazuje na uživatele databáze. Posledním argumentem (dhis2.sql) je název souboru kopie. Pokud chcete kopii souboru okamžitě komprimovat, můžete provést:

    pg_dump dhis2 -U dhis | gzip > dhis2.sql.gz

Chcete-li tuto kopii obnovit v jiném systému, musíte nejprve vytvořit prázdnou databázi, jak je popsáno v části instalace. Kopii musíte také rozbalit, pokud jste vytvořili komprimovanou verzi. Můžete zadat:

    psql -d dhis2 -U dhis -f dhis2.sql
