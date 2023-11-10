---
revision_date: "2021-09-07"
template: single.html
---

# Instalace { #installation }

Kapitola instalace obsahuje informace o tom, jak nainstalovat DHIS2 v různých kontextech, včetně online centrálního serveru, offline lokální sítě, samostatné aplikace a samostatného balíčku s názvem DHIS2 Live.

## Úvod { #install_introduction }

DHIS2 běží na všech platformách, pro které existuje Java JDK, která zahrnuje nejpopulárnější operační systémy jako Windows, Linux a Mac. DHIS2 běží na databázovém systému PostgreSQL. DHIS2 je zabalen jako standardní Java Web Archive (soubor WAR), a proto běží na libovolných kontejnerech Servlet, jako jsou Tomcat a Jetty.

Tým DHIS2 doporučuje operační systém Ubuntu 18.04 LTS, databázový systém PostgreSQL a kontejner Tomcat Servlet jako preferované prostředí pro serverové instalace.

Tato kapitola poskytuje průvodce nastavením výše uvedeného technologického zásobníku. Mělo by se však číst jako průvodce pro uvedení do provozu a nikoli jako vyčerpávající dokumentace pro uvedené prostředí. Pro důkladné čtení odkazujeme na oficiální dokumentaci Ubuntu, PostgreSQL a Tomcat.

Balíček `dhis2-tools` Ubuntu automatizuje mnoho úloh popsaných v níže uvedené příručce a je doporučen pro většinu uživatelů, zejména pro ty, kteří nejsou obeznámeni s příkazovým řádkem nebo správou serverů. Je to podrobně popsáno v samostatné kapitole této příručky.

## Specifikace serveru { #install_server_specifications }

DHIS2 je aplikace náročná na databázi a vyžaduje, aby měl váš server odpovídající množství paměti RAM, počet jader CPU a rychlý disk. Tato doporučení by měla být považována za obecná pravidla, nikoli za přesná měřítka. DHIS2 se lineárně mění podle velikosti RAM a počtu jader CPU, takže čím více si můžete dovolit, tím lépe bude aplikace fungovat.

-   _RAM:_ Alespoň 1 GB paměti na 1 milion zaznamenaných datových záznamů za měsíc nebo na 1000 souběžných uživatelů. Alespoň 4 GB pro malou instanci, 12 GB pro střední instanci.

-   _CPU cores:_ 4 CPU cores for a small instance, 8 CPU cores for a medium or large instance.

-   _Disk:_ Ideálně použijte SSD. Jinak použijte disk s rychlostí 7200 ot./min. Minimální rychlost čtení je 150 Mb/s, 200 Mb/s je dobrá, 350 Mb/s nebo lepší je ideální. Pokud jde o místo na disku, doporučuje se minimálně 60 GB, ale bude zcela záviset na množství dat obsažených v tabulkách hodnot dat. Tabulky Analytics vyžadují značné množství místa na disku. Plánujte dopředu a zajistěte, aby váš server mohl být upgradován s větším množstvím místa na disku, jakmile to bude potřeba.

## Softwarové požadavky { #install_software_requirements }

Pozdější verze DHIS2 vyžadují pro provoz následující verze softwaru.

-   Operační systém, pro který existuje Java JDK nebo JRE verze 8 nebo 11. Doporučuje se Linux.
-   Java JDK. Doporučuje se OpenJDK.
    -   Pro DHIS 2 verze 2.35 a novější se doporučuje JDK 11 a je vyžadován JDK 8 nebo novější.
    -   Pro verze DHIS 2 starší než 2.35 je vyžadován JDK 8.
-   Databáze PostgreSQL verze 9.6 nebo novější. Doporučuje se novější verze PostgreSQL, například verze 13.
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

### Instalace Java { #install_java_installation }

Doporučený Java JDK pro DHIS 2 je OpenJDK 11. OpenJDK je licencován pod licencí GPL a lze jej provozovat zdarma. Můžete jej nainstalovat pomocí následujícího příkazu:

```
sudo apt-get install openjdk-11-jdk
```

Pokud dáváte přednost OpenJDK 8 (pro verze starší než 2.35), můžete jej nainstalovat pomocí tohoto příkazu:

```
sudo apt-get install openjdk-8-jdk
```

Ověřte správnost instalace zadáním:

```
java -version
```

### Konfigurace DHIS2 { #install_database_configuration }

Informace o připojení k databázi jsou poskytovány DHIS2 prostřednictvím konfiguračního souboru s názvem `dhis.conf`. Vytvořte tento soubor a uložte jej do adresáře `DHIS2\_HOME`. Jako příklad může být toto umístění:

```sh
/home/dhis/config/dhis.conf
```

Konfigurační soubor pro PostgreSQL odpovídající výše uvedenému nastavení má tyto vlastnosti:

```properties
# ----------------------------------------------------------------------
# Database connection
# ----------------------------------------------------------------------

# JDBC driver class
connection.driver_class = org.postgresql.Driver

# Database connection URL
connection.url = jdbc:postgresql:dhis2

# Database username
connection.username = dhis

# Database password
connection.password = xxxx

# ----------------------------------------------------------------------
# Server
# ----------------------------------------------------------------------

# Enable secure settings if deployed on HTTPS, default 'off', can be 'on'
# server.https = on

# Server base URL
# server.base.url = https://server.com/
```

Důrazně doporučujeme povolit nastavení `server.https` a nasazení DHIS 2 pomocí šifrovaného protokolu HTTPS. Toto nastavení umožní např. zabezpečené cookies. Je-li toto nastavení povoleno, je vyžadováno nasazení HTTPS.

Nastavení `server.base.url` odkazuje na adresu URL, na kterou koncoví uživatelé v síti přistupují k síti.

Konfigurační soubor podporuje proměnné prostředí. To znamená, že můžete nastavit určité vlastnosti jako proměnné prostředí a nechat je vyřešit, např. jako je tento, kde `DHIS2\_HOME` je název proměnné prostředí:

```properties
connection.password = ${DB_PASSWD}
```

Všimněte si, že tento soubor obsahuje heslo pro vaši databázi DHIS2 v čistém textu, takže je třeba jej chránit před neoprávněným přístupem. Chcete-li to provést, vyvolejte následující příkaz, který zajistí, že jej bude moci číst pouze uživatel _dhis_:

```sh
chmod 600 dhis.conf
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
export JAVA_HOME='/usr/lib/jvm/java-11-openjdk-amd64/'
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

Dalším krokem je stažení souboru DHIS2 WAR a jeho umístění do adresáře webových aplikací Tomcat. Soubory DHIS2 WAR si můžete stáhnout z následujícího umístění:

```sh
https://releases.dhis2.org/
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

## Konfigurace OpenID Connect (OIDC) { #install_oidc_configuration }

DHIS2 podporuje vrstvu identity OpenID Connect (OIDC) pro jednotné přihlášení (SSO). OIDC je standardní ověřovací protokol, který umožňuje uživatelům přihlásit se k poskytovateli identity (IdP), jako je Google. Poté, co se uživatelé úspěšně přihlásí ke svému IdP, budou automaticky přihlášeni k DHIS2.

Tato část poskytuje obecné informace o používání DHIS2 s OIDC a možnosti konfigurace pro IdP a DHIS2. Tok autentizace bude vypadat následovně.

1. Uživatel se pokusí přihlásit k serveru DHIS2 z klientského počítače.

2. DHIS2 přesměruje požadavek na ověření na bránu IdP.

3. Uživatel je vyzván k zadání přihlašovacích údajů a úspěšně se autentizuje u poskytovatele identity. Poskytovatel identity odpoví přesměrováním URL zpět na DHIS2. Adresa URL přesměrování obsahuje autorizační kód uživatele.

4. Klient je přesměrován na DHIS2 a předloží autorizační kód.

5. DHIS2 představuje autorizační kód klienta IdP spolu s jeho vlastními pověřeními klienta.

6. IdP vrátí přístupový token a ID token do DHIS2. DHIS2 provádí ověření tokenu IdP (JWT). Token ID je sada párů klíčů atributů pro uživatele. Klíčové páry se nazývají nároky.

7. DHIS2 identifikuje uživatele z IdP claims a dokončí požadavek na autentizaci z kroku 1. DHIS2 hledá uživatele, který odpovídá claim `e-mail` od IdP. DHIS2 lze nakonfigurovat tak, aby pro tento proces používal různé claims.

8. DHIS2 autorizuje uživatele.

### Požadavky na OIDC { #requirements-for-oidc }

#### Účet IdP { #idp-account }

Musíte mít přístup k poskytovateli identity (IdP), který podporuje DHIS2.

Aktuálně jsou podporováni následující poskytovatelé identity:

-   Google
-   Azure AD
-   WSO2
-   Generický poskytovatel

#### Místní uživatelský účet { #local-user-account }

Musíte explicitně vytvořit uživatele v instanci DHIS2. Jejich import z externího adresáře, jako je Active Directory, není aktuálně podporován. Správa uživatelů s externím úložištěm identit není s OIDC podporována.

#### Nároky IdP a mapování uživatelů { #idp-claims-and-mapping-of-users }

Pro přihlášení k DHIS2 musí být daný uživatel zřízen v IdP a poté namapován na uživatelský účet v DHIS2. OIDC používá metodu, která se spoléhá na deklarace sdílení atributů uživatelských účtů s jinými aplikacemi. Deklarace zahrnují atributy uživatelských účtů, jako je e-mail, telefonní číslo, jméno atd. DHIS2 se spoléhá na deklarace IdP, aby mapovala uživatelské účty z IdP na ty, které jsou hostovány na DHIS2. Ve výchozím nastavení DHIS2 očekává, že IdP předá požadavek _email_. V závislosti na vašem IdP možná budete muset nakonfigurovat DHIS2 tak, aby používal jinou deklaraci IdP.

Pokud používáte Google nebo Azure AD jako poskytovatele identity, je výchozím chováním použití e-mailové deklarace k mapování identit poskytovatele identity na uživatelské účty DHIS2.

Aby se uživatel DHIS2 mohl přihlásit pomocí IdP, musí být zaškrtnuto políčko uživatelského profilu _Pouze externí ověřování (OpenID nebo LDAP)_ a pole _OpenID_ musí odpovídat claim (nároku na mapování) vrácenému IdP. E-mail ve výchozím nastavení používá Google i Azure AD.

### Nakonfigurujte poskytovatele identity pro OIDC { #configure-the-identity-provider-for-oidc }

Toto téma poskytuje informace o konfiguraci poskytovatele identity (IdP) pro použití OIDC s DHIS2. Toto je jeden krok ve vícekrokovém procesu. Následující témata poskytují informace o konfiguraci a používání OIDC s DHIS2.

#### Nakonfigurujte poskytovatele identity { #configure-the-idp }

Než budete moci použít OIDC s DHIS2, musíte mít účet u podporovaného poskytovatele identity (IdP) a projekt nebo aplikaci s IdP. Při konfiguraci DHIS2 musíte poskytnout následující informace:

-   **ID klienta poskytovatele:** Toto je identifikátor, který IDP přidělil vaší aplikaci.

-   **Tajemství klienta u Poskytovatele:** Tato hodnota je tajná a měla by být udržována v bezpečí.

#### URL přesměrování { #redirect-url }

Někteří poskytovatelé IdP budou vyžadovat adresu URL přesměrování pro vaši instanci DHIS2. Svou adresu URL pro poskytovatele identity můžete vytvořit pomocí následující syntaxe:

```
(protocol):/(your DHIS2 host)/oauth2/code/(IdP code)
```

Příklad vypadá takto:

```
https://dhis2.org/oauth2/code/google
```

#### Příklad procesu IdP (Google) { #example-idp-process-google }

Následující postup poskytuje přehled kroků, které provádíte s poskytovatelem. Postup například popisuje použití Google jako poskytovatele identity. Každý poskytovatel má však poněkud odlišný tok, takže specifika kroků (a jejich pořadí) se mohou lišit v závislosti na vašem poskytovateli.

1. Zaregistrujte se na vývojářském webu poskytovatele a přihlaste se. Například pro Google můžete přejít do Google [konzole pro vývojáře](https://console.developers.google.com).

2. Vytvořte nový projekt nebo aplikaci.

3. Na ovládacím panelu vývojáře postupujte podle pokynů pro vytvoření ID klienta a tajného klíče OAuth 2.0. Zaznamenejte tyto hodnoty na později.

4. Nastavte své autorizované URI přesměrování na: `(protocol):/(host)/oauth2/code/google` Uchovávejte client secret na bezpečném místě.

Při konfiguraci poskytovatele identity postupujte podle pokynů ke službě IdP:

-   [Google](https://developers.google.com/identity/protocols/oauth2/openid-connect)

-   [Azure AD](https://medium.com/xebia-engineering/authentication-and-authorization-using-azure-active-directory-266980586ab8)

> **Poznámka**
>
> Identifikátory URI autorizovaného přesměrování Azure AD musí mít tuto formu: `(protocol):/(host)/oauth2/code/my_azure_ad_tenant_id`

### Nakonfigurujte DHIS2 pro OIDC { #configure-dhis2-for-oidc }

> **Poznámka**
>
> Než provedete kroky popsané zde, musíte nakonfigurovat poskytovatele identity OIDC (IdP), jak je popsáno v části Konfigurace poskytovatele identity pro OIDC.

Tato část popisuje možnosti konfigurace, které lze nastavit v souboru `dhis.conf`. Nezapomeňte restartovat DHIS 2, aby se změny projevily.

Chcete-li povolit OIDC, začněte nastavením následující vlastnosti v `dhis.conf`.

```properties
oidc.oauth2.login.enabled = on
```

Následující části pokrývají konfiguraci specifickou pro poskytovatele.

#### Google { #google }

```properties
# ----------------------------------------------------------------------
# Příklad konfigurace Google OIDC
# ----------------------------------------------------------------------

# Obecné konfigurační parametry

# Povolit OIDC
oidc.oauth2.login.enabled = on

# Adresa URL instance DHIS 2, nekončete lomítkem, ne všichni IdP podporují odhlášení (kde skončit po volání end_session_endpoint na IdP).
oidc.logout.redirect_url = (protokol)://(host)/(nepovinný kontext aplikace)

# Parametry specifické pro Google:
oidc.provider.google.client_id = my_client_id
oidc.provider.google.client_secret = my_client_secret

# Adresa URL instance DHIS 2, nekončí lomítkem, např.: https://dhis2.org/demo
oidc.provider.google.redirect_url = (protocol)://(host)/(volitelný kontext aplikace)

# Nepovinné, výchozí hodnota je "email".
oidc.provider.google.mapping_claim = email

```

#### Azure AD { #azure-ad }

Všimněte si, že Azure AD podporuje mít více tenantů, proto je schéma číslování `oidc.provider.azure.NUMBER.VARIABLE` níže.

Ujistěte se, že váš účet Azure AD na webu Azure Portal je nakonfigurován s adresou URL přesměrování, jako je  `(protocol):/(host)/oauth2/code/my_azure_ad_tenant_id`. Chcete-li zaregistrovat DHIS 2 jako „aplikaci“ na webu Azure Portal, postupujte takto:

1. Vyhledejte a vyberte  _App registrations_.

2. Klikněte na _New registration_.

3. Do pole _Name_ zadejte popisný název instance DHIS 2.

4. Do pole _Redirect URI_ zadejte adresu URL přesměrování, jak je uvedeno výše.

5. Klikněte na  _Register_.

```properties
# ----------------------------------------------------------------------
# Příklad konfigurace Azure OIDC
# ----------------------------------------------------------------------

# Obecné konfigurační parametry

# Povolit OIDC
oidc.oauth2.login.enabled = on

# Adresa URL instance DHIS 2, nekončete lomítkem, ne všichni IdP podporují odhlášení (kde skončit po volání end_session_endpoint na IdP).
oidc.logout.redirect_url = (protokol)://(host)/(nepovinný kontext aplikace)

# Parametry specifické pro Azure AD:

# První poskytovatel (0)
oidc.provider.azure.0.tenant = my_azure_ad_tenant_id
oidc.provider.azure.0.client_id = my_azure_ad_client_id
oidc.provider.azure.0.client_secret = my_azure_ad_client_secret

# Adresa URL instance DHIS 2, nekončí lomítkem, např.: https://dhis2.org/demo
oidc.provider.azure.0.redirect_url = (protokol)://(host)/(volitelný kontext aplikace)

# Nepovinné, výchozí hodnota je "email".
oidc.provider.azure.0.mapping_claim = email

# Nepovinné, výchozí hodnota je 'true'
oidc.provider.azure.0.support_logout = true

# Druhý poskytovatel (1)
oidc.provider.azure.1.tenant = my_other_azure_ad_tenant_id
...
```

#### Obecní poskytovatelé { #generic-providers }

„Obecného“ poskytovatele lze použít ke konfiguraci jakéhokoli poskytovatele OIDC, který používá „výchozí“ funkce v Spring Security.

V níže uvedeném příkladu nakonfigurujeme norského vládního poskytovatele zdravotních služeb OIDC.

Jméno klienta je zde _helseid_ a automaticky se zobrazí na přihlašovací stránce jako tlačítko se stejným názvem nebo názvem _display_alias_, pokud je definován.

Obecní poskytovatelé DHIS2 používají následující pevně zakódovaná výchozí nastavení pro:

-   Ověření klienta: https://tools.ietf.org/html/rfc6749#section-2.3 > ClientAuthenticationMethod.BASIC

-   Ověřené požadavky: https://tools.ietf.org/html/rfc6750#section-2 > AuthenticationMethod.HEADER

> **Poznámka**
>
> Následující názvy klientů jsou vyhrazeny pro použití negenerických poskytovatelů a nelze je zde použít: „google“, „azure“, „wso2“.

```properties
# ----------------------------------------------------------------------
# Příklad obecné konfigurace OIDC
# ----------------------------------------------------------------------

# Obecné konfigurační parametry

# Povolit OIDC
oidc.oauth2.login.enabled = on

# Adresa URL instance DHIS 2, nekončete lomítkem, ne všichni IdP podporují odhlášení (kde skončit po volání end_session_endpoint na IdP).
oidc.logout.redirect_url = (protocol)://(host)/(optional app context)


# Toto je název zobrazený na přihlašovací stránce DHIS2
oidc.provider.helseid.display_alias = HelseID

oidc.provider.helseid.client_id = CLIENT_ID
oidc.provider.helseid.client_secret = CLIENT_SECRET
oidc.provider.helseid.mapping_claim = helseid://claims/identity/email
oidc.provider.helseid.authorization_uri = https://helseid.no/connect/authorize
oidc.provider.helseid.enable_logout = true
oidc.provider.helseid.token_uri = https://helseid.no/connect/token
oidc.provider.helseid.user_info_uri = https://helseid.no/connect/userinfo
oidc.provider.helseid.jwk_uri = https://helseid.no/.well-known/openid-configuration/jwks
oidc.provider.helseid.end_session_endpoint = https://helseid.no/connect/endsession
oidc.provider.helseid.scopes = helseid://scopes/identity/email
oidc.provider.helseid.redirect_url = {baseUrl}/oauth2/code/{registrationId}

# (Zde můžete odkazovat na url pro libovolné logo, pokud je obsluhováno ze stejné domény jako server DHIS2.)
oidc.provider.helseid.logo_image = ../security/btn_helseid.svg
oidc.provider.helseid.logo_image_padding = 0px 1px

# (Tyto hodnoty se připojí k požadavku, musí to být dvojice klíč/hodnota jako: ..."), A TO V PODOBĚ: "KEY1 VALUE1,KEY2 VALUE2,...")
oidc.provider.helseid.extra_request_parameters = acr_values lvl4

# (Toto je pro volitelnou podporu PKCE viz: https://oauth.net/2/pkce/) Výchozí hodnota je: FALSE
oidc.provider.helseid.enable_pkce = true

```

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

DHIS2 umožňuje šifrování dat. Povolení vyžaduje nějaké další nastavení. Chcete-li zajistit zabezpečení šifrovacího algoritmu, budete muset nastavit heslo v konfiguračním souboru _dhis.conf_ prostřednictvím vlastnosti _encryption.password_:

```properties
encryption.password = xxxx
```

Vlastnost _encryption.password_ je heslo (klíč) použité při šifrování a dešifrování dat v databázi. Pamatujte, že po nastavení a zašifrování dat nesmí být heslo změněno, protože data již nelze dešifrovat.

Heslo musí mít alespoň **24 znaků**. Doporučuje se kombinace čísel a malých a velkých písmen. Šifrovací heslo musí být utajeno.

> **Důležité**
>
> Není možné obnovit šifrovaná data, pokud dojde ke ztrátě nebo změně šifrovacího hesla. Pokud dojde ke ztrátě hesla, ztratí se i šifrovaná data. Naopak šifrování neposkytuje žádné zabezpečení, pokud je heslo ohroženo. Proto je třeba věnovat velkou pozornost uložení hesla na bezpečném místě.

Upozorňujeme, že podpora šifrování závisí na dostupných souborech zásad _Java Cryptography Extension_ (JCE). Ty jsou zahrnuty ve všech verzích OpenJDK a Oracle JDK 8 Update 144 nebo novějších.

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

Doporučený přístup ke shromažďování a vizualizaci těchto metrik je prostřednictvím Prometheus a Grafana.

Další informace najdete na stránce [monitorovací infrastruktura](https://github.com/dhis2/wow-backend/blob/master/guides/monitoring.md) a [instalace programu Prometheus a Grafanal](https://docs.dhis2.org/master/en/dhis2_system_administration_guide/monitoring.html).

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

### Blokování konkrétních verzí aplikací pro Android pomocí nginx { #install_making_resources_available_with_nginx }

V některých scénářích může správce systému chtít blokovat určité klienty Android na základě jeho verze aplikace DHIS2. Například pokud uživatelé v poli neaktualizovali verzi aplikace pro Android na konkrétní verzi a správce systému chce zablokovat jejich přístup, aby vynutil aktualizaci; nebo úplně opačný scénář, když chce správce systému zablokovat nové verze aplikace, protože ještě nebyly testovány. To lze snadno implementovat pomocí specifických pravidel _User-Agent_ v konfiguračním souboru `nginx`.

```text
http {
  ..

  server {
    listen       80;
    server_name  api.somedomain.com;

    ..


    # Block the latest Android App as it has not been tested (August 2020 - Last version is 2.2.1)
    if ( $http_user_agent ~ 'com\.dhis2/1\.2\.1/2\.2\.1/' ) {
        return 403;
    }

    # Block Android 4.4 (API is 19) as all the users should have received the new tablets
    if ( $http_user_agent ~ 'com\.dhis2/.*/.*/Android_19' ) {
        return 403;
    }
    ..

    }

    ..
}
```

> Poznámka
>
> Pro implementaci výše popsané metody mějte na paměti následující:
>
> - Před verzí 1.1.0 nebyl řetězec _User-Agent_ odesílán
> - Od verze 1.1.0 do 1.3.2 se _User-Agent_ řídil vzorem Dhis2/AppVersion/AppVersion/Android_XX
> - Od verze 2.0.0 a vyšší se _User-Agent_ řídí vzorem com.dhis2/SdkVersion/AppVersion/Android_XX
>
> Android_XX označuje úroveň Android API, tj. verzi Androidu, jak je uvedena [zde] (https://developer.android.com/studio/releases/platforms).
>
> nginx používá [PCRE](http://www.pcre.org/) pro párování regulárních výrazů

## Odkaz na konfiguraci DHIS2 { #install_dhis2_configuration_reference }

Následující text popisuje úplnou sadu možností konfigurace pro konfigurační soubor _dhis.conf_. Konfigurační soubor by měl být umístěn v adresáři, na který odkazuje proměnná prostředí _DHIS2_HOME_.

> **Poznámka**
>
> Tento konfigurační soubor byste se neměli pokoušet použít přímo, ale použijte jej jako referenci pro dostupné možnosti konfigurace. Mnoho vlastností je volitelných.

```properties
# ------------------------------------------------- ----------------------
# Připojení k databázi pro PostgreSQL [Povinné]
# ------------------------------------------------- ----------------------

# Hibernace SQL dialekt
connection.dialekt = org.hibernate.dialekt.PostgreSQLDialect

# Třída ovladače JDBC
connection.driver_class = org.postgresql.Driver

# URL připojení k databázi
connection.url = jdbc:postgresql:dhis2

# Uživatelské jméno databáze
connection.username = dhis

# Heslo databáze (citlivé)
připojení.heslo = xxxx

# Maximální velikost fondu připojení (výchozí: 40)
connection.pool.max_size = 40

# ------------------------------------------------- ----------------------
# Připojení k databázi pro PostgreSQL [Volitelné]
# ------------------------------------------------- ----------------------

# Minimální počet připojení, které fond bude udržovat v daném čase (výchozí: 5).
connection.pool.min_size=5

# Počáteční velikost fondu připojení (výchozí: 5)
#Number of Connections se fond pokusí získat při spuštění. Mělo by být mezi minPoolSize a maxPoolSize
connection.pool.initial_size=5

#Určuje, kolik připojení najednou se pokusí získat, když je fond vyčerpán.
connection.pool.acquire_incr=5

#Seconds Připojení může zůstat sdružené, ale nevyužité, než bude vyřazeno. Nula znamená, že nečinná připojení nikdy nevyprší. (výchozí: 7200)
connection.pool.max_idle_time=7200

#Počet sekund, po které by připojení přesahující minPoolSize měla zůstat nečinná ve fondu, než budou vyřazena (výchozí: 0)
connection.pool.max_idle_time_excess_con=0

#Pokud je toto číslo větší než 0, dhis2 otestuje všechna nečinná, sdružená, ale neodhlášená připojení, každých tento počet sekund. (výchozí: 0)
connection.pool.idle.con.test.period=0

#Pokud je pravda, při každé kontrole připojení bude provedena operace k ověření platnosti připojení. (výchozí: false)
connection.pool.test.on.checkout=false

#Pokud je hodnota true, při každém načtení připojení bude asynchronně provedena operace k ověření platnosti připojení. (výchozí: true)
connection.pool.test.on.checkin=true

#Definuje dotaz, který bude proveden pro všechny testy připojení. V ideálním případě není tato konfigurace potřeba, protože ovladač postgresql již poskytuje efektivní testovací dotaz. Konfigurace je vystavena pouze pro vyhodnocení, nepoužívejte ji, pokud k tomu není důvod.
connection.pool.preferred.test.query=select 1

#Nakonfigurujte počet pomocných vláken používaných dhis2 pro operace jdbc. (výchozí: 3)
connection.pool.num.helper.threads=3

# -----------------------------------------------------------------------
# Server [Povinné]
# -----------------------------------------------------------------------

# Základní URL k instanci DHIS 2
server.base.url = https://play.dhis2.org/dev

# Povolit nastavení zabezpečení, pokud je systém nasazen na HTTPS, může být „off“, „on“
server.https = off

# ------------------------------------------------- ----------------------
# Systém [Volitelné]
# ------------------------------------------------- ----------------------

# Systémový režim pouze pro operace čtení databáze, může být „vypnuto“, „zapnuto“
system.read_only_mode = off

# Časový limit relace v sekundách, výchozí hodnota je 3600
system.session.timeout = 3600

# SQL zobrazení chráněných tabulek, může být „on“, „off“
system.sql_view_table_protection = on

# ------------------------------------------------- ----------------------
# Šifrování [Volitelné]
# ------------------------------------------------- ----------------------

# Šifrovací heslo (citlivé)
šifrování.heslo = xxxx

# ------------------------------------------------- ----------------------
# Úložiště souborů [Volitelné]
# ------------------------------------------------- ----------------------

# Poskytovatel úložiště souborů, aktuálně jsou podporovány 'filesystem' a 'aws-s3'
filestore.provider = filesystem

# Název adresáře / bucketu, složka pod DHIS2_HOME v systému souborů, 'bucket' na AWS S3
filestore.container = files

# Umístění datového centra (není vyžadováno)
filestore.location = eu-west-1

# Veřejná identita / uživatelské jméno
filestore.identity = dhis2-id

# Tajný klíč / heslo (citlivé)
filestore.secret = xxxx

# ------------------------------------------------- ----------------------
# LDAP [Volitelné]
# ------------------------------------------------- ----------------------

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

# ------------------------------------------------- ----------------------
# Uzel [Volitelné]
# ------------------------------------------------- ----------------------

# Identifikátor uzlu, volitelný, užitečný v clusterech
node.id = 'node-1'

# ------------------------------------------------- ----------------------
# Monitorování [Volitelné]
# ------------------------------------------------- ----------------------

# Monitorování DHIS2 API
monitoring.api.enabled = on

# Monitorování JVM
monitoring.jvm.enabled = on

# Monitorování fondu připojení k databázi
monitoring.dbpool.enabled = on

# Monitorování hibernace, nepoužívejte ve výrobě
monitoring.hibernate.enabled = off

# Monitorování provozuschopnosti
monitoring.uptime.enabled = on

# Monitorování CPU
monitoring.cpu.enabled = on

# ------------------------------------------------- ----------------------
# Analytics [Volitelné]
# ------------------------------------------------- ----------------------

# Vypršení mezipaměti na straně serveru Analytics během několika sekund
analytics.cache.expiration = 3600

# ------------------------------------------------- ----------------------
# Systémová telemetrie [Volitelné]
# ------------------------------------------------- ----------------------

# Adresa URL pro monitorování systému
system.monitoring.url =

# Uživatelské jméno pro monitorování systému
system.monitoring.username =

# Heslo monitorování systému (citlivé)
heslo.systému.monitoring = xxxx
```

## Seznam změn { #install_changelog }

DHIS2 zapisuje položky do protokolů změn, když byly v systému změněny určité entity. Entity spadají do dvou kategorií: _aggregate_ a _tracker_. Kategorie _aggregate_  zahrnuje změny agregovaných datových hodnot. Kategorie _tracker_ zahrnuje změny instancí programu, položek dočasného vlastnictví programu, hodnot atributů trasovaných entit a hodnot dat trasovaných entit.

Seznam změn pro obě kategorie je ve výchozím nastavení povolen. Pomocí níže popsaných vlastností můžete určit, zda chcete povolit nebo zakázat seznam změn podle kategorie prostřednictvím konfiguračního souboru `dhis.conf`. Možnosti vlastností jsou  `on` (výchozí) a  `off`.

Výhodou protokolu změn je schopnost vidět změny, které byly provedeny v datech. Výhodami deaktivace protokolu změn je malé zlepšení výkonu tím, že se vyhnete nákladům na zápis položek protokolu změn do databáze a méně použitého úložiště databáze. Doporučuje se povolit seznam změn a jeho deaktivaci byste měli věnovat velkou pozornost.

```properties
# Aggregate changelog, can be 'on', 'off'
changelog.aggregate = on

# Tracker changelog, can be 'on', 'off'
changelog.tracker = on
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

# Aktualizace { #upgrading-dhis2 }

## Upgrade vs. aktualizace { #upgrading-vs-updating }

Když mluvíme o upgradu DHIS2, obecně máme na mysli jednoduše „přechod na novější verzi“. Mezi _upgrading_ a _updating_ je však důležitý rozdíl.

**Upgrade** : Přechod na novější základní verzi DHIS2 (například z 2.34 na 2.36). Upgrade obvykle vyžaduje plánování, testování, školení (pro nové funkce nebo rozhraní), což může vyžadovat značný čas a úsilí.

**Aktualizace** : Přechod na novější opravu aktuální verze DHIS2 (například z 2.35.1 na 2.35.4). Aktualizace poskytuje hlavně opravy chyb bez změny funkčnosti softwaru. Je to nižší riziko a všem doporučujeme udržovat svou verzi aktuální.

## Než začnete { #upgrading-before-you-begin }

> **Pozor**
>
> Je důležité si uvědomit, že jakmile upgradujete, nebudete moci používat upgradovanou databázi se starší verzí DHIS2. To znamená, že **není možné přejít na nižší verzi**.
>
> Pokud se chcete vrátit ke starší verzi, musíte tak učinit s kopií databáze, která byla vytvořena z této starší verze nebo z předchozí verze. Proto je téměř vždy dobré si před upgradem vytvořit kopii databáze.

## Provádění upgradu { #upgrading-process }

Bez ohledu na to, zda upgradujete nebo aktualizujete, technický proces je víceméně stejný. Budeme tomu říkat pouze upgrade.

### 1 Chraňte svá data { #upgrading-safeguard-your-data }

V závislosti na tom, jaký druh instance DHIS2 máte a k čemu ji používáte, je prvním krokem ujistit se, že můžete obnovit všechna důležitá data, pokud se při upgradu něco pokazí.

To znamená provádění standardních úloh správy systému, jako jsou:

1. Zálohování databáze
2. Testování ve vývojovém prostředí
3. Plánování odstávky (aby se zabránilo zadávání dat během upgradu)
4. atd.

### 2 Upgradujte software { #upgrading-upgrade-the-software }

#### Od verze 2.29 nebo nižší { #upgrading-pre-230 }

Pokud začínáte od verze 2.29 nebo nižší, musíte nejprve upgradovat na verzi 2.30 verzi po verzi ručně, podle poznámek k upgradu, které najdete pod konkrétními čísly verzí na [našem webu vydání](https://github .com/dhis2/dhis2-releases). Když jste ve verzi 2.30, můžete přejít k další sekci.

#### Od verze 2.30 nebo vyšší { #upgrading-post-230 }

Pokud začínáte alespoň od verze 2.30:

1. **Přečtěte si všechny poznámky k upgradu od vaší aktuální verze až po cílovou verzi na [našem webu vydání](https://github.com/dhis2/dhis2-releases).** Ujistěte se, že vaše prostředí splňuje všechny požadavky
2. Pokud jste tak neučinili v kroku 1, vytvořte si kopii databáze
3. Odstraňte z databáze všechny materializované pohledy SQL
4. Zastavte server
5. Nahraďte war soubor cílovou verzí (není potřeba upgradovat na přechodné verze, ve skutečnosti se to nedoporučuje)
6. Spusťte server

Nyní byste měli být připraveni využívat nové opravy a funkce.

# Monitoring { #monitoring }

## Úvod { #monitoring }

DHIS2 může exportovat metriky kompatibilní s [Prometheus](https://prometheus.io/) pro monitorování uzlů DHIS2.

Tato část popisuje kroky potřebné k instalaci Prometheus a [Grafana](https://grafana.com/) pomocí standardního instalačního postupu (`apt-get`) a Dockeru a konfigurace Grafany tak, aby zobrazovala metriky DHIS2.

Seznam metrik vystavených instancí DHIS2 najdete v příručce pro monitorování na [GitHub](https://github.com/dhis2/wow-backend/blob/master/guides/monitoring.md).

## Nastavení { #monitoring_setup }

V následujících částech je popsáno, jak nastavit Prometheus a Grafanu a jak nastavit Prometheus pro načítání dat z jedné nebo více instancí DHIS2.

### Instalace Prometheus + Grafana na Ubuntu a Debian { #prometheus }

-   Stáhněte si Prometheus z oficiální stránky [download](https://prometheus.io/download/).

-   Nezapomeňte vyfiltrovat operační systém a architekturu procesoru (Linux a amd64).

-   Ujistěte se, že jste vybrali nejnovější stabilní verzi, nikoli „rc“, protože prozatím není považována za dostatečně stabilní.

-   Stáhněte si archiv kliknutím na odkaz nebo pomocí `wget`.

```
wget https://github.com/prometheus/prometheus/releases/download/v2.15.2/prometheus-2.15.2.linux-amd64.tar.gz
```

-   Rozbalte zip soubor

```
tar xvzf prometheus-2.15.2.linux-amd64.tar.gz
```

Archiv obsahuje mnoho důležitých souborů, ale zde jsou hlavní, které potřebujete vědět.

-   `prometheus.yml`: konfigurační soubor pro Prometheus. Toto je soubor, který se chystáte upravit, abyste vylepšili svůj server Prometheus, například abyste změnili interval scrapingu nebo nakonfigurovali vlastní výstrahy;
-   `prometheus`: binární soubor pro váš server Prometheus. Toto je příkaz, který se chystáte spustit pro spuštění instance Prometheus ve vašem Linux boxu;
-   `promtool`: toto je příkaz, který můžete spustit k ověření vaší konfigurace Prometheus.

### Konfigurace Prometheus jako služby { #prometheus_service }

-   Vytvořte uživatele `Prometheus` se skupinou` Prometheus`.

```
useradd -rs /bin/false prometheus
```

-   Přesuňte binární soubory Prometheus do místního adresáře bin

```
cd prometheus-2.15.2.linux-amd64/
cp prometheus promtool /usr/local/bin
chown prometheus:prometheus /usr/local/bin/prometheus
```

-   Vytvořte složku ve složce `/etc` pro Prometheus a přesuňte soubory konzoly, knihovny konzoly a konfigurační soubor prometheus do této nově vytvořené složky.

```
mkdir /etc/prometheus
cp -R consoles/ console_libraries/ prometheus.yml /etc/prometheus
```

Vytvořte datovou složku v kořenovém adresáři se složkou prometheus uvnitř.

```
mkdir -p data/prometheus
chown -R prometheus:prometheus /data/prometheus /etc/prometheus/*
```

### Vytvořte službu Prometheus { #prometheus_create_service }

Chcete-li vytvořit službu Prometheus _systemd_, přejděte do složky `/lib/systemd/system` a vytvořte nový soubor systemd s názvem `prometheus.service`.

```
cd /lib/systemd/system
touch prometheus.service
```

-   Upravte nově vytvořený soubor a vložte do něj následující obsah:

```properties
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=prometheus
Group=prometheus
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path="/data/prometheus" \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries \
  --web.listen-address=0.0.0.0:9090 \
  --web.enable-admin-api

Restart=always

[Install]
WantedBy=multi-user.target
```

-   Uložte soubor a při spuštění povolte službu Prometheus

```
systemctl enable prometheus
systemctl start prometheus
```

-   Vyzkoušejte, zda je služba spuštěna

```
systemctl status prometheus

...
Active: active (running)
```

-   Nyní by mělo být možné získat přístup k uživatelskému rozhraní Prometheus přístupem na stránku `http://localhost:9090`.

### Nastavení reverzní proxy Nginx { #prometheus_nginx }

Prometheus nativně nepodporuje ověřování ani šifrování TLS. Pokud musí být Prometheus vystaven mimo hranice místní sítě, je důležité povolit ověřování a šifrování TLS. Následující kroky ukazují, jak používat Nginx jako reverzní proxy.

-   Nainstalujte Nginx, pokud již není nainstalován

```
apt update
apt-get install nginx
```

Ve výchozím nastavení Nginx začne poslouchat požadavky HTTP ve výchozím portu `http`, což je `80`.

Pokud v počítači již běží instance Nginx a nejste si jisti, na kterém portu naslouchá, spusťte následující příkaz:

```
> lsof | grep LISTEN | grep nginx

nginx   15792   root   8u   IPv4   1140223421   0t0   TCP *:http (LISTEN)
```

Poslední sloupec zobrazuje port používaný Nginxem (`http` -> `80`).

Ve výchozím nastavení je konfigurace Nginx umístěna v `/etc/nginx/nginx.conf`

Ujistěte se, že soubor `nginx.conf` obsahuje sekci `Virtual Host Config`

```
##
# Virtual Host Configs
##

include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;

```

-   Vytvořte nový soubor v souboru  `/etc/nginx/conf.d` s názvem `prometheus.conf`

```
touch /etc/nginx/conf.d/prometheus.conf
```

-   Upravte nově vytvořený soubor a vložte do něj následující obsah:

```
server {
  listen 1234;

  location / {
    proxy_pass           http://localhost:9090/;
  }
}
```

-   Restartujte Nginx a přejděte na http://localhost:1234

```
systemctl restart nginx

# in case of start-up errors
journalctl -f -u nginx.service
```

-   Nakonfigurujte Prometheus pro reverzní proxy pomocí úpravy `/lib/systemd/system/prometheus.service` a přidejte následující argument do seznamu argumentů předaných spustitelnému souboru Prometheus.

```
--web.external-url=https://localhost:1234
```

-   Restartujte službu

```
systemctl daemon-reload
systemctl restart prometheus


# in case of errors
journalctl -f -u prometheus.service
```

### Povolit ověření reverzní proxy { #prometheus_auth }

Tato část ukazuje, jak konfigurovat základní ověřování pomocí serveru reverzní proxy. Pokud potřebujete jiný mechanismus ověřování (jednotné přihlášení atd.), Zkontrolujte příslušnou dokumentaci.

-   Ujistěte se, že je v systému nainstalován `htpasswd`

```
apt-get install apache2-utils
```

-   Vytvořte ověřovací soubor

```
cd /etc/prometheus
htpasswd -c .credentials admin
```

Vyberte silné heslo a zkontrolujte, zda byl předávací soubor správně vytvořen.

-   Upravte dříve vytvořený konfigurační soubor Nginx (`/etc/nginx/conf.d/prometheus.conf`) a přidejte ověřovací informace.

```
server {
  listen 1234;

  location / {
    auth_basic           "Prometheus";
    auth_basic_user_file /etc/prometheus/.credentials;
    proxy_pass           http://localhost:9090/;
  }
}
```

-   Restartujte Nginx

```
systemctl restart nginx

# in case of errors
journalctl -f -u nginx.service
```

-   `http://localhost:1234` by nyní měl vyžadovat zadání uživatelského jména a hesla.

### Instalace Grafany na Ubuntu a Debianu { #grafana }

-   Přidejte klíč `gpg` a nainstalujte balíček OSS Grafana z APT repo

```sh
apt-get install -y apt-transport-https

wget -q -O - "https://packages.grafana.com/gpg.key" | sudo apt-key add -

add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

apt-get update

apt-get install grafana
```

-   Pokud systém používá program `systemd`, automaticky se vytvoří nová služba `grafana-service`. Zkontrolujte soubor `systemd` a získejte přehled o instalaci Grafany

```
cat /usr/lib/systemd/system/grafana-server.service
```

Tento soubor je docela důležitý, protože nabízí informace o nově nainstalované instanci Grafana.

Soubor ukazuje:

**Binární soubor serveru Grafana** je umístěn na adrese  `/usr/sbin/grafana-server`. Soubor, který definuje všechny **proměnné prostředí**, je umístěn na  `/etc/default/grafana-server` **Konfigurační soubor** je dán prostřednictvím proměnné prostřed  `CONF_FILE`. **PID souboru** je také určen proměnnou prostředí `PID_FILE_DIR`. Cesty **protokolování**, **dat **, **pluginů** a **zajišťování** jsou dány proměnnými prostředí.

-   Spusťte server

```
systemctl start grafana-server
```

-   Přejděte na webovou konzolu Grafana: http://localhost:3000

Výchozí přihlašovací jméno pro Grafanu je `admin` a výchozí heslo je také` admin`. Při prvním přístupu budete vyzváni ke změně hesla.

-   Nakonfigurujte Prometheus jako zdroj dat Grafana

Přístup na panel zdrojů dat kliknutím na `Konfigurace`>` Zdroje dat` v levé nabídce.

Klikněte na `Add a datasource`

V dalším okně vyberte datový zdroj Prometheus.

Nakonfigurujte zdroj dat podle nastavení Prometheus (použijte ověřování, TSL atd.)

### Instalace Prometheus + Grafana pomocí Dockeru { #prometheus_grafana_docker }

Tato část popisuje, jak spustit stack Prometheus obsahující Prometheus a Grafanu.

Konfigurace je založena na tomto projektu: https://github.com/vegasbrianc/prometheus

-   Klon tohoto projektu na Github: https://github.com/vegasbrianc/prometheus

-   Spusťte zásobník Prometheus pomocí:

```
docker stack deploy -c docker-stack.yml prom
```

Výše uvedený příkaz může mít za následek následující chybu:

_Tento uzel není správcem swarmu. Pomocí „docker swarm init“ nebo „docker swarm join“ připojte tento uzel ke swarmu a zkuste to znovu_

Pokud k tomu dojde, musíte spustit Swarm. Můžete použít následující příkazový řádek:

```
docker swarm init --advertise-addr <YOUR_IP>
```

Jakmile se tento příkaz úspěšně spustí, měli byste být schopni bez problémů spustit předchozí příkaz.

Stack obsahuje také exportér uzlů pro monitorování Dockeru. Pokud vás monitorování Dockeru nezajímá, můžete komentovat příslušné oddíly v souboru `docker-stack.yml`:

-   `node-exporter`
-   `cadvisor`

-   Zastavení zásobníku Prometheus:

```
docker stack rm prom
```

Soubor konfigurace Prometheus (`prometheus.yml`) je umístěn ve složce `prometheus`.

-   Přejděte na webovou konzolu Grafana na adrese: http://localhost:3000 s uživatelským jménem: `admin` a heslem: `foobar`

### Nakonfigurujte Prometheus tak, aby načítal metriky z jedné nebo více instancí DHIS2 { #prometheus_dhis2 }

Před použitím programu Prometheus je nutné provést základní konfiguraci. Musíme tedy vytvořit konfigurační soubor s názvem `prometheus.yml`

> **Poznámka**
>
> Konfigurační soubor Prometheus je napsán v YAML, což přísně zakazuje používání karet. Pokud je váš soubor nesprávně naformátovaný, Prometheus se nespustí. Při úpravách buďte opatrní.

Konfigurační soubor Prometheus je rozdělen do tří částí: `global`, `rule_files` a `scrape_configs`.

V globální části najdeme obecnou konfiguraci Prometheus: `scrape_interval` definuje, jak často Prometheus škrábne cíle,  `evaluation_interval`  určuje, jak často bude software vyhodnocovat pravidla. Pravidla se používají k vytváření nových časových řad a ke generování výstrah.

Blok `rule_files` obsahuje informace o umístění všech pravidel, která chceme načíst serveru Prometheus.

Poslední blok konfiguračního souboru má název `scape_configs` a obsahuje informace, které prostředky Prometheus sleduje.

A simple DHIS2 Prometheus monitoring file looks like this example:

```yaml
global:
    scrape_interval: 15s
    evaluation_interval: 15s

scrape_configs:
    - job_name: "dhis2"
      metrics_path: "/dhis/api/metrics"
      basic_auth:
          username: admin
          password: district
      static_configs:
          - targets: ["localhost:80"]
```

Globální `scrape_interval` je nastaven na 15 sekund, což je dost pro většinu případů použití.

V části `scrape_configs` jsme definovali exportér DHIS2. Bloky `basic_auth` obsahují pověření požadovaná pro přístup k API `metrics`: zvažte vytvoření uživatele ad-hoc pouze pro přístup ke koncovému bodu `metrics`.

Prometheus může nebo nemusí běžet na stejném serveru jako DHIS2: ve výše uvedené konfiguraci se předpokládá, že Prometheus sleduje pouze jednu instanci DHIS2 běžící na stejném serveru jako Prometheus, takže používáme `localhost`.

### Nakonfigurujte exportér DHIS2 { #dhis2_metrics_conf }

Monitorovací subsystém je ve výchozím nastavení v DHIS2 zakázán.

Aby bylo možné metriky exportovat, musí být každý cluster metrik explicitně povolen. Chcete-li nakonfigurovat DHIS2 na export jedné nebo více metrik, zkontrolujte tento [dokument](https://github.com/dhis2/wow-backend/blob/master/guides/monitoring.md#dhis2-monitoring-configuration).

# Audit { #audit }

## Úvod { #introduction }

DHIS2 podporuje novou auditorskou službu založenou na Apache ActiveMQ Artemis. Artemis je používán jako asynchronní systém zasílání zpráv DHIS2.

Poté, co je entita uložena do databáze, bude auditní zpráva odeslána spotřebitelské službě zpráv Artemis. Zpráva bude poté zpracována v jiném vlákně.

Protokoly auditu lze načíst z databáze DHIS2. V současné době není k dispozici žádné uživatelské rozhraní ani koncový bod API pro načítání záznamů auditu.

## Jedna tabulka auditu { #audit_table }

Všechny položky auditu budou uloženy do jedné tabulky s názvem `audit`

| Sloupec | Typ |  |  |
| --- | --- | --- | --- |
| auditid | celé číslo |  |  |
| audittype | text | READ, CREATE, UPDATE, DELETE, SEARCH |  |
| auditscope | text | METADATA, AGGREGATE, TRACKER |  |
| klass | text | Název Java třídy auditu entity  |  |
| atributy | jsonb | Řetězec Json ukládá atributy entity auditu používané pro vyhledávání. Příklad: {"valueType":"TEXT", "categoryCombo":"SWQW313FQY", "domainType":"TRACKER"} |  |
| data | bytea | Komprimovaný řetězec Json entity auditu. Aktuálně je ve formátu bajtového pole a není čitelný člověkem. |  |
| createdat | časové razítko bez časového pásma |  |  |
| createdby | text |  |  |
| uid | text |  |  |
| code | text |  |  |
|  |  |

Nová služba Audit využívá dva nové koncepty: Rozsahy auditu a Typ auditu.

## Rozsah auditu { #audit_scope }

Rozsah auditu je logická oblast aplikace, kterou lze auditovat. V současné době existují tři rozsahy auditu:

```
Tracker

Metadata

Aggregate
```

-   U Tracker Audit Scope jsou auditovanými objekty: trasovaná instance entity, trasovaná hodnota atributu entity, zápis, událost

-   Pro oblast metadat jsou auditovány všechny objekty „metadat“.

-   U agregovaného rozsahu se auditují objekty agregované datové hodnoty.

## Typ auditu { #audit_type }

Typ auditu je akce, která spouští operaci auditu. V současné době podporujeme následující typy:

```
READ

CREATE

UPDATE

DELETE
```

Jako příklad lze uvést, že když se vytvoří nová instance trasované entity, a pokud je takto nakonfigurována, použije se akce CREATE k vložení nové položky auditu do tabulky auditu db.

> **Pozor**
>
> Typ auditu READ vygeneruje v databázi spoustu dat a může mít dopad na výkon.

## Nastavení { #audit_configuration }

Systém auditu je automaticky nakonfigurován tak, aby auditoval následující rozsahy a typy:

-   CREATE, UPDATE, DELETE

-   METADATA, TRACKER, AGGREGATE

**K aktivaci auditu není nutná žádná akce.** Audit lze stále konfigurovat pomocí „matice auditu“. Matice auditu je řízena 3 vlastnostmi v dhis.conf:

```
audit.metadata

audit.tracker

audit.aggregate
```

Každá vlastnost přijímá seznam platných typů auditu oddělených středníkem:

```
CREATE

UPDATE

DELETE

READ
```

Například, aby bylo možné auditovat pouze vytváření a mazání objektů souvisejících s Trasovačem, měla by být do `dhis.conf` přidána následující vlastnost:

```
audit.tracker = CREATE;DELETE
```

Chcete-li zcela zakázat auditování, je to konfigurace, která se má použít:

```
audit.metadata = DISABLED

audit.tracker = DISABLED

audit.aggregate = DISABLED
```

# Používání komunikačních bran pro hlášení SMS { #sms_report_sending }

DHIS2 podporuje přijímání dat prostřednictvím [SMS](https://docs.dhis2.org/master/en/dhis2_user_manual_en/mobile.html), SMS však musí být pro ochranu informací utajeny. Aplikace DHIS2 pro Android funguje jako transparentní vrstva pro odesílání informací prostřednictvím SMS, kde se uživatel nemusí obávat psaní SMS. Chcete-li odesílat SMS pomocí aplikace pro Android, musí být správně nakonfigurována brána SMS. Tato část vysvětluje různé dostupné možnosti a jak toho dosáhnout.

## Odesílání SMS { #sms_report_sening }

Je důležité nejprve objasnit, že tato část se týká hlavně nastavení **přijímání SMS** (z mobilních zařízení na server DHIS2), které je nezbytné při zvažování použití aplikace k odesílání (synchronizaci) informací zaznamenaných v aplikaci na server DHIS2 prostřednictvím SMS. V aplikaci to lze nastavit v části _Settings_ > _SMS Settings_

Odesílání SMS, tj. Ze serveru DHIS2 na mobilní zařízení, je nastaveno relativně snadno. Pokud je vyžadováno pouze zasílání upozornění na telefony uživatelů z DHIS2, když dojde k určitým událostem (zasílání zpráv, prahové hodnoty atd.), Je vyžadováno pouze odesílání SMS.

To vše lze nakonfigurovat na stránce Konfigurace služby SMS v sekci [Konfigurace mobilních zařízení](https://docs.dhis2.org/master/en/user/html/mobile_sms_service.html).

Podpora běžných poskytovatelů, jako jsou _Bulk SMS_ a _Clickatell_, je v rámci okamžitě dostupných funkcí a oba poskytovatelé podporují odesílání SMS na čísla ve většině zemí.

Rovněž je možné pro odesílání a přijímání SMS použít jinou SMS bránu. Takže i když nastavíte řešení pro příjem SMS níže, je stále možné použít jedno z výše uvedených řešení pro odesílání SMS.

## Používání zařízení Android jako SMS brány { #sms_report_android_gateway }

Nejjednodušším řešením je použití vyhrazeného zařízení Android jako vaší SMS brány. Jakýkoli telefon nebo tablet se systémem Android OS (4.4, Kitkat nebo novější) by měl být v pořádku. Bude vyžadovat stálé připojení k internetu, aby bylo možné přeposílat zprávy na váš server DHIS2, a také bude potřebovat SIM kartu pro příjem příchozích SMS.

Budete si muset stáhnout a nainstalovat aplikaci DHIS2 Android SMS Gateway do mobilního zařízení. Podívejte se na seznam [vydání](https://github.com/dhis2/dhis2-sms-android-gateway/releases), kde si můžete stáhnout nejnovější soubor APK k instalaci. Na stránce samotné aplikace jsou pokyny, ale v zásadě stačí spustit aplikaci a zadat podrobnosti o vašem serveru DHIS2 (URL, uživatelské jméno a heslo).

Jakmile je toto nastaveno a spuštěno, zadejte telefonní číslo tohoto zařízení brány na konfigurační stránce jakéhokoli jiného mobilního zařízení pomocí aplikace DHIS2 Capture. Poté, když jsou SMS zaslány z těchto reportovacích zařízení, budou přijaty na zařízení brány a automaticky přeposlány na server DHIS2, kde budou zpracovány.

**Používání tohoto zařízení brány je perfektní při testování funkčnosti SMS.** Bylo by skvělé, když pilotujete projekty, které vyžadují hlášení pomocí SMS. Pokud je zařízení připojeno k napájecímu zdroji a má stálé připojení k internetu, funguje dobře i pro malé projekty.

Při zvažování přesunu projektu do provozu by však bylo nutné prozkoumat jedno z trvalejších a spolehlivějších řešení pro brány níže.

### Odesílání SMS pomocí brány zařízení Android { #sending-sms-using-an-android-device-gateway }

Tato možnost není aktuálně podporována ani dokumentována.

## Vyhrazené brány SMS { #sms_report_dedicated_gateway }

Tato část pojednává o použití trvalejších a vyhrazených bran SMS a dostupných možnostech. Každá z těchto možností níže bude zahrnovat poskytovatele (nebo sebe), který má připojení SMPP k telefonnímu operátorovi v zemi a pomocí tohoto připojení přijímá příchozí SMS a předává je na váš server DHIS2 přes internet pomocí protokolu HTTP.

Tato řešení mohou používat **dlouhé číslo** nebo **krátký kód**. Dlouhé číslo je standardní číslo mobilního telefonu typu, který používá většina soukromých osob, tj. +61 400123123. Krátký kód je jednoduše krátké číslo, například 311. Nastavení a údržba krátkých kódů je obvykle dražší.

### Zajištění správného formátování příchozích SMS na server DHIS2 { #ensuring-incoming-sms-to-dhis2-server-are-formatted-correctly }

Při odesílání příchozích SMS na server DHIS2 přes API používáte následující adresu URL: _https://<DHIS2_server_url>/api/sms/inbound_

V DHIS2 verze 2.34 a nižší vyžaduje tento koncový bod formát příchozích SMS ve velmi specifickém formátu, tj. Samotná zpráva musí být parametr s názvem text, telefonní číslo odesílatele musí být parametr s názvem originator.

Při použití všech níže uvedených možností brány SMS, když je nakonfigurujete pro přeposílání příchozích SMS na jinou webovou službu, budou mít každý svůj vlastní formát, který se bude lišit od toho, který se očekává v rozhraní DHIS2 API. Z tohoto důvodu je tedy nutné je před odesláním na server DHIS2 přeformátovat.

Jednou z možností je spustit vlastní velmi jednoduchou webovou službu, která jednoduše obdrží příchozí SMS od poskytovatele brány, přeformátuje ji na požadovanou pro DHIS2 a přepošle ji na vaše DHIS2 API. Takovou službu by musel napsat softwarový vývojář.

Ve verzi DHIS2 verze 2.35 se plánuje podpora těchto případů šablonovým systémem pro příchozí SMS, takže můžete určit formát zpráv, které budou odesílány od vašeho poskytovatele. Tímto způsobem můžete nakonfigurovat server DHIS2 tak, aby přijímal příchozí SMS od jakéhokoli jiného poskytovatele brány SMS, a oni mohou přímo odesílat příchozí SMS do rozhraní DHIS2 API, aniž by bylo nutné takovou webovou službu formátování.

### Použití RapidPro { #using-rapidpro }

[RapidPro](https://rapidpro.io/) je služba provozovaná organizací UNICEF ve více než 50 zemích po celém světě. Jedná se o soubor softwaru, který spolupracuje s vnitrostátními telefonními operátory a umožňuje organizacím navrhovat řešení SMS pro jejich projekty, jako jsou zprávy SMS nebo osvětové kampaně.

Služba RapidPro bude zahrnovat připojení SMPP k jednomu nebo více telefonním operátorům v zemi, obvykle prostřednictvím zkráceného kódu, který je potenciálně určen pro práci ve zdravotnictví pro nevládní organizace. Poté je možné přidat webhook, aby byly příchozí SMS přeposílány do jiné webové služby, jako je výše popsaná formátovací webová služba. Pokud se zkrácený kód používá také pro jiné účely, může být nutné přidat telefonní čísla vašich reportovacích zařízení do samostatné skupiny, aby se do webhooku předávaly pouze příchozí SMS z těchto zařízení.

RapidPro je v současné době zřízen a spuštěn ve zhruba polovině zemí, které v současné době používají nebo pilotují DHIS2. Před zvážením jednoho z níže uvedených řešení, které může být finančně i časově nákladné, stojí za to kontaktovat Unicef, abyste zjistili, zda je RapidPro k dispozici a zda jej lze použít pro hlášení zdravotního stavu ve vaší zemi.

### Používání komerčních poskytovatelů SMS bran { #using-commercial-sms-gateway-providers }

Z komerčních poskytovatelů brány SMS zmíněných v části Odesílání SMS výše budou mít obvykle možnost _Send_ SMS ve většině zemí, ale mohou podporovat _receiving_  SMS pouze v omezeném počtu zemí. Většina zemí, které podporují příjem SMS, nejsou země, které používají DHIS2. Ze zemí, které používají DHIS2, je většina již pokryta službou RapidPro spuštěnou v zemi.

Stojí však za to prozkoumat, jaké komerční možnosti jsou pro vaši zemi k dispozici. V některých zemích budou existovat malé národní společnosti, které poskytují služby SMS, budou mít stávající spojení SMPP s poskytovateli telefonů, které můžete použít.

### Přímé používání telefonních operátorů { #using-phone-carriers-directly }

Pokud žádné z výše uvedených řešení není k dispozici, bylo by nutné obrátit se přímo na telefonní operátory ve vaší zemi. První otázka, kterou je třeba se zeptat, by byla, zda jsou si vědomi společností, které s nimi provozují spojení SMPP, na které byste se mohli obrátit.

Pokud ne, jako poslední možnost budete muset zvážit nastavení a udržování vlastního SMPP spojení s poskytovatelem telefonu. Ne všichni poskytovatelé telefonů však mohou takovou službu nabízet.

Budete muset spustit svůj vlastní server se spuštěným softwarem, jako je [Kannel](https://www.kannel.org/), který se připojuje (obvykle přes VPN) ke službě SMPP spuštěné v síti poskytovatelů telefonů. Pokud je toto nastaveno, všechny příchozí SMS pro nakonfigurované dlouhé číslo nebo zkrácený kód se odesílají z operátora telefonu na váš server Kannel a poté můžete tyto zprávy přeposílat výše uvedeným způsobem.

### Příjem zřetězených nebo vícedílných SMS { #receiving-concatenated-or-multipart-sms }

Při synchronizaci dat pomocí SMS s aplikací DHIS2 pro Android používá komprimovaný formát, aby využil co nejméně místa (znaků textu). Navzdory tomu se docela často stane, že zpráva přesáhne limit 160 znaků jedné standardní SMS. Na většině moderních mobilních zařízení budou tyto zprávy stále odesílány jako jedna zřetězená nebo vícedílná SMS a přijaty jako jedna zpráva. Při odesílání mezi dvěma mobilními zařízeními, když se jako brána používá zařízení Android, by toto mělo být zpracováno bez problémů.

Při výběru brány SMS je tedy důležité potvrdit, že použitý telefonní operátor podporuje zřetězené SMS. Většina z nich to bude podporovat, ale je důležité potvrdit, protože funkce SMS nebude fungovat, pokud jsou SMS rozděleny. To se spoléhá na něco, co se nazývá UDH (záhlaví dat uživatele). Při diskusi s poskytovateli se poté zeptejte, zda je podporována.
