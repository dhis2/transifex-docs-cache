---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/README.md"
revision_date: "2022-03-23"
---

# 2.38 Poznámky k upgradu { #238-upgrade-notes }

## Podpora Java { #java-support }

Počínaje DHIS 2.38 je vyžadována Java JDK verze 11. To znamená, že při nasazení DHIS 2.38 a novějších již nemůžete používat Java 8.

Java 11 je podporována pro DHIS 2 od verze 2.35. To znamená, že můžete upgradovat svůj server na JDK 11, zatímco stále běží DHIS 2.35 nebo novější v rámci přípravy na upgrade DHIS 2.38. Java 11 se ukázala jako spolehlivá a výrazně rychlejší pro DHIS 2.

Jako vždy doporučujeme používat OpenJDK distribuci Java, vzhledem k povaze bezplatného a otevřeného zdroje. Distribuce OpenJDK 11 jsou dostupné na všech hlavních operačních systémech a jsou výchozím JDK na Ubuntu 20.04 LTS.

## Databáze { #database }

## API { #api }

-   Ruční spouštění úloh pomocí `/api/jobConfigurations/execute` se změnilo z `GET` na požadavek `POST`
-   ID programu je nyní povinné pro fázi programu. Dotčené koncové body: `/programStages`, `/metadata`
-   `GET /systemSettings` vracející JSONP (`Accept=application/javascript`) byl odstraněn
-   Několik koncových bodů API mírně mění svůj kořenový objekt odpovědi, aby byl v souladu s většinou koncových bodů. Kořenový objekt vrácený před verzí 2.38 se stane členem s názvem `response` nového kořenového objektu vráceného verzí 2.38. Spotřebitelé se mohou rozhodnout buď použít `/api/37/...` k získání starého chování, nebo se musí rozbalit na novou odpověď provedením `<root> .response` k vyřešení předchozího kořenového adresáře z odpovědi 2.38.

    > **NOTE**
    >
    > In case of error responses this also entails an HTTP status code change from `200 OK` to `409 Conflict`.

    Dotčené koncové body jsou:

    -   `POST /api/completeDataSetRegistrations` with `JSON`/`XML` (only non `async` affected)
    -   `POST /api/dataValueSets` with `JSON`/`XML`/`ADX`/`CSV` (only non `async` affected)
    -   `POST /api/metadata` with `JSON`/`XML`/`GML`/`CSV` (only non `async` affected)
    -   `POST /api/predictions` (only non `async` affected)
    -   `PUT /api/predictions` (only non `async` affected)
    -   `PUT /api/relationships/{id}`
    -   `PUT /api/users/{uid}` with `JSON`/`XML`

## Autority { #authorities }

## Audit { #audit }
