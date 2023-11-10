---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/modules-and-repositories.md" 
---
# Moduly a úložiště

<!--DHIS2-SECTION-ID:modules_and_repositories-->

Objekt `D2` je vstupním bodem pro interakci s SDK. Sada SDK vynutí, aby objekt `D2` byl v aplikaci singleton.

Moduly jsou vrstvou pod `D2`. Fungují jako wrapper pro související funkce. Modul obsahuje některá související úložiště a může vystavovat některé služby a pomocníky.

Úložiště fungují jako fasáda pro DB (nebo v některých případech pro webové API). Nabízejí možnosti čtení metadat a čtení / zápis pro data.

## Řešení návratových typů: RxJava

<!--DHIS2-SECTION-ID:dealing_with_rxjava-->

Sada SDK používá jako preferovaný návratový typ pro všechny metody třídy RxJava (pozorovatelné, jednoduché, dokončitelné, Flowable). Důvody pro výběr tříd RxJava jsou hlavně dva:

- **Pro usnadnění asynchronního zpracování vrácených objektů.** Většina akcí v SDK je časově náročná a musí být provedena v sekundárním vlákně. Tyto návratové typy přinutí aplikaci vypořádat se s tímto asynchronním chováním.
- **Chcete-li upozornit na postup.** Metody jako metadata nebo synchronizace dat mohou trvat několik minut. Z pohledu uživatele je velmi užitečné mít pocit pokroku.

To neznamená, že aplikace jsou nuceny používat RxJava ve svém kódu: jsou nuceny vypořádat se pouze s asynchronním chováním některých metod. SDK obvykle vystavuje *blokující* verzi každé metody.

Například stejný dotaz pomocí RxJava a AsyncTask:

*Používání RxJava*

```java
d2.programModule().programs()
    .subscribeOn(Schedulers.io())
    .observeOn(AndroidSchedulers.mainThread())
    .get()
    .subscribe(programs -> {}); //List<Program>
```

*Používání AsyncTask*

```java
new AsyncTask<Void, Void, List<Program>>() {
    protected List<Program> doInBackground() {
        return d2.programModule().programs().blockingGet();
    }

    protected void onPostExecute(List<Program> programs) {

    }
}.execute();
```

Přístup do databáze je časově náročný a doporučuje se to provést v samostatném vlákně pomocí kterékoli z doporučených metod. Postupy, které zahrnují přístup k webovému rozhraní API, jako je přihlášení, stahování nebo nahrávání metadat nebo dat, **musí** být spuštěny v samostatném vlákně, jinak Android vyvolá chybu.

## Budování dotazů

<!--DHIS2-SECTION-ID:query_building-->

Úložiště nabízejí syntaxi stavitele s ověřením v době kompilace pro přístup k prostředkům. Typický dotaz se skládá z některých modifikátorů (filtr, pořadí, vnořená pole) a končí akcí (get, count, getPaged, ...).

```java
// Generic syntax
d2.<module>.<repository>
    .[ filter | orderBy | nested fields ]
    .<action>;

// An example for events
d2.eventModule().events()
    .byOrganisationUnitUid().eq("DiszpKrYNg8")
    .byEventDate().after(Date("2019-05-05"))
    .orderByEventDate(DESC)
    .withTrackedEntityDataValues()
    .get();
```

### Filtry

<!--DHIS2-SECTION-ID:filters-->

Úložiště vystavují seznam dostupných filtrů s předponou klíčového slova „by“. Seznam operátorů filtrů dostupných pro každý filtr závisí na typu hodnoty filtru: například typ hodnoty `Date` nabídne operátory jako `after`, `before`, `inPeriods`, zatímco typ hodnoty `Boolean` bude nabídka `isFalse` nebo` isTrue`.

K jednomu dotazu lze v libovolném pořadí připojit několik filtrů. Filtry se globálně spojují pomocí operátoru „AND“. To znamená, že dotaz jako

```java
d2.eventModule().events()
    .byOrganisationUnitUid().eq("DiszpKrYNg8")
    .byEventDate().after(Date("2019-05-05"))
    ...
```

vrátí události přiřazené organizační jednotce "DiszpKrYNg8" **AND**, jehož eventDate je po "2019-05-05".

### Řadit podle

<!--DHIS2-SECTION-ID:order_by-->

Modifikátory řazení mají předponu klíčové slovo „orderBy“.

K jednomu dotazu lze připojit několik modifikátorů „orderBy“. Pořadí modifikátorů „orderBy“ v dotazu určuje prioritu objednávky. To znamená, že dotaz jako

```java
d2.eventModule().events()
    .orderByEventDate(DESC)
    .orderByLastUpdated(DESC)
    ...
```

na prvním místě seřadí následující EventDate a poté následující LastUpdated.

### Zahrnout vnořená pole

<!--DHIS2-SECTION-ID:nested_fields-->

Úložiště vracejí třídy, které nejsou přesnou shodou databázových tabulek: jsou to složitější objekty, které mohou zahrnovat některé vlastnosti získané z jiných tabulek. Například třída `Event` má vlastnost nazvanou` trackedEntityDataValues`, která obsahuje seznam TrackedEntityDataValues. Hlavním důvodem pro výběr tohoto druhu objektů je absorbovat složitost práce s tabulkami odkazů, takže se aplikace nemusí starat o vytváření vazeb mezi objekty.

Z důvodu problémů s výkonem není tento druh vlastností ve výchozím nastavení zahrnut: musí být dotazovány explicitně. V úložištích mají vlastnosti, které nejsou ve výchozím nastavení zahrnuty a je třeba je dotazovat, předponu klíčového slova "with".

Několik vlastností lze připojit ke stejnému dotazu v libovolném pořadí. Například dotaz jako

```java
d2.programModule().programs()
    .withTrackedEntityType()
    ...
```

vrátí vnořený objekt `TrackedEntityType`.

## Pomocníci

<!--DHIS2-SECTION-ID:helpers-->

Sada SDK obsahuje některé pomocníky v balíčku `org.hisp.dhis.android.core.arch.helpers`. Lze je snadno najít v Android Studio vyhledáním `Helper` v názvech tříd. Zahrnují některé užitečné metody k provádění běžných operací:

- `AccessHelper`: související s objektem přístupu (nastavení sdílení).
- `CollectionsHelper`: společné operace se sbírkami.
- `CoordinateHelper`, `GeometryHelper`: manipulace s geoprostorovými daty.
- `FileResizeHelper`,` FileResourceDirectoryHelper`: manipulace se zdroji souboru.
- `UidsHelper`: běžné operace s kolekcemi objektů s uid.
- `UserHelper`: operace související s ověřením uživatele.

## Seznam modulů

<!--DHIS2-SECTION-ID:module_list-->

Moduly systému:

- importModule
- maintenanceModule
- systemInfoModule
- settingModule
- wipeModule

Moduly velkých bloků:

- metadataModule
- aggregatedDataModule

Konkrétní moduly:

- categoryModule
- constantModule
- dataElementModule
- dataSetModule
- dataValueModule
- enrollmentModule
- eventModule
- fileResourceModule
- indicatorModule
- legendSetModule
- noteModule
- organisationUnitModule
- optionModule
- periodModule
- programModule
- relationshipModule
- smsModule
- trackedEntityModule
- userModule
- validationModule


