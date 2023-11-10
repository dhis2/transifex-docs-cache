---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/object-style.md" 
---
# Styl objektu

<!--DHIS2-SECTION-ID:object-style-->

Některé prvky zahrnují vlastnost nazvanou "styl", která definuje ikonu a barvu. Tyto vizuální informace jsou velmi užitečné pro rychlou navigaci v aplikaci. Některé typické případy použití:

- Rozlišujte různé programy a trackedEntityTypes v seznamu programů.
- Ve formulářích pro zadávání dat s optionSet zobrazte volby s ikonami a barvami místo jmen.
- Různé programStages v rámci programu.

Tato vlastnost je volitelná a ve většině případů není definována. Styl objektu může mít ikonu nebo barvu nebo obojí.

## Ikona

Sada ikon používaných v DHIS2 je součástí sady SDK. Jsou umístěny v rámci prostředků ve složce „drawable“. V současné době jsou předdefinovány a nelze je přizpůsobit.

```java

// Illustrative code to get the resource id
if (program.style().icon() != null) {
    String iconName = program.style().icon();
    int resourceId = getResources().getIdentifier(iconName, "drawable", getPackageName());
}
```

## Barva

Obsahuje hexadecimální hodnotu barvy. Lze jej použít k přizpůsobení pozadí, barvy textu, nadpisů řádků atd.

```java
program.style().color();    // Na příklad #9C33FF

```


