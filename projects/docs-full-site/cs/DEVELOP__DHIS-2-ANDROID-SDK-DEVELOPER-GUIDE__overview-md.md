---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/overview.md" 
---
# Přehled

<!--DHIS2-SECTION-ID:overview-->

DHIS2 Android SDK je knihovna, která abstrahuje složitost interakce s webovým rozhraním DHIS2. Jeho cílem je být výchozím bodem pro vytváření aplikací pro Android pro DHIS2, které pokrývají některé úkoly, které by měla implementovat libovolná aplikace pro Android, jako jsou metadata a synchronizace dat.

Hlavní cíle:

- **Abstraktní webové API DHIS2**. Není třeba provádět dotazy API na serveru. Sada SDK obsahuje metody interakce s webovým rozhraním API.
- **Pracujte offline**. Implementuje zjednodušenou verzi modelu DHIS2, která je zachována v místní databázi (SQLite). Zajišťuje, že všechna metadata potřebná k provádění úkolů zadávání dat jsou kdykoli k dispozici pro sestavení formulářů zadávání dat. Data jsou uložena lokálně a nahrána na server, když je k dispozici připojení.
- **Zajistěte kompatibilitu DHIS2**. Zapouzdřuje změny mezi verzemi DHIS2, takže se o ně aplikace nemusí starat. V případě, že SDK zavádí některé změny pro přizpůsobení nové verzi DHIS2, může aplikace tyto změny bezpečně detekovat v době kompilace.

## Přehled technologií

<!--DHIS2-SECTION-ID:technology_overview-->

SDK je napsán v prostředí Java 8 pomocí snížené podmnožiny funkcí povolených v minimální verzi rozhraní Android API. SDK používá některé součásti specifické pro Android, například knihovny k vytvoření stránkovaného seznamu (LiveData, PagedList) nebo k přístupu do systému souborů. Z tohoto důvodu je v současné době **SDK možné spustit pouze v prostředí Android**.

K usnadnění asynchronního zpracování některých metod používá [RxJava](https://github.com/ReactiveX/RxJava). I když je volitelný, doporučujeme tento přístup zajistit neblokující volání.

Další knihovny interně používané SDK jsou: [Dagger](https://github.com/google/dagger) pro vkládání závislostí, [Jackson](https://github.com/FasterXML/jackson) pro analýzu JSON, [Retrofit](https://square.github.io/retrofit/) a [OkHttpClient](https://square.github.io/okhttp/) pro komunikaci API nebo [SQLBrite](https://github.com/square/sqlbrite) pro migraci databáze.


