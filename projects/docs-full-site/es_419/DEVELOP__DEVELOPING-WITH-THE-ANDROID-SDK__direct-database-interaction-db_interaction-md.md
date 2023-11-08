---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/db-interaction.md" 
---
# Interacción directa con la base de datos  { #db_interaction } 

<!--DHIS2-SECTION-ID:db_interaction-->

Los métodos del repositorio cubren la mayoría de las necesidades de la aplicación. Pero en algunos casos la aplicación puede querer interactuar directamente con la base de datos.

El SDK expone un objeto DatabaseAdapter para ejecutar instrucciones en bruto en la base de datos. Además, las clases del modelo SDK incluyen métodos auxiliares para crear instancias a partir de un `Cursor`.

Por ejemplo, leer la lista de constantes utilizando repositorios e interactuando directamente con la base de datos.

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

Las clases `TableInfo` incluyen información útil sobre la estructura de la tabla, como los nombres de tablas y columnas.


