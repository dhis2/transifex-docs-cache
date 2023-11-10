---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/db-interaction.md" 
---
# Přímá interakce databáze

<!--DHIS2-SECTION-ID:db_interaction-->

Metody úložiště pokrývají většinu potřeb aplikace. Ale v některých případech může aplikace chtít komunikovat přímo s databází.

Sada SDK zpřístupňuje objekt DatabaseAdapter pro provádění nezpracovaných příkazů v databázi. Třídy modelu SDK také zahrnují pomocné metody pro vytváření instancí z `Cursor`.

Například si přečtěte seznam konstant pomocí úložišť a přímé interakce s databází.

```java
// Using repositories
d2.constantModule().constants().blockingGet() // List<Constant>

// Direct database interaction
String query = "SELECT * FROM " + ConstantTableInfo.TABLE_INFO.name();
try (Cursor cursor = Sdk.d2().databaseAdapter().rawQuery(query)) {
    List<Constant> constantList = new ArrayList<>();
    if (cursor.getCount() > 0) {
        cursor.moveToFirst();
        do {
            collection.add(Constant.create(cursor));
        }
        while (cursor.moveToNext());
    }
    return constantList; // List<Constant>
}
```

Třídy `TableInfo` obsahují některé užitečné informace o struktuře tabulky, například názvy tabulek a sloupců.


