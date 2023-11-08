---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/db-interaction.md" 
---
# Interação direta com o banco de dados

<!--DHIS2-SECTION-ID:db_interaction-->

Os métodos de repositório cobrem a maioria das necessidades do aplicativo. Mas, em alguns casos, o aplicativo pode querer interagir diretamente com o banco de dados.

O SDK expõe um objeto DatabaseAdapter para executar instruções brutas no banco de dados. Além disso, as classes de modelo do SDK incluem métodos auxiliares para criar instâncias de um `Cursor`.

Por exemplo, leia a lista de constantes usando repositórios e interagindo diretamente com o banco de dados.

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

As classes `TableInfo` incluem algumas informações úteis sobre a estrutura da tabela, como nomes de tabelas e colunas.


