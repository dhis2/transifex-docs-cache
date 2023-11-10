---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/object-style.md" 
---
# Estilo de objeto  { #object-style } 

<!--DHIS2-SECTION-ID:object-style-->

Alguns elementos incluem uma propriedade chamada "estilo" que define um ícone e uma cor. Essas informações visuais são muito úteis para navegar rapidamente pelo aplicativo. Alguns casos de uso típicos:

- Distinguir programas diferentes e trackedEntityTypes em uma lista de programas.
- Em formulários de entrada de dados com um optionSet, mostra as opções com ícones e cores em vez de nomes.
- Estágios de programa diferentes dentro de um programa.

Esta propriedade é opcional e não é definida na maioria dos casos. Um estilo de objeto pode ter um ícone, uma cor ou ambos.

## Ícone { #icon } 

O conjunto de ícones usados no DHIS2 está incluído no SDK. Eles estão localizados dentro dos recursos, na pasta "drawable". Atualmente, eles são predefinidos e não podem ser personalizados.

```java

// Illustrative code to get the resource id
if (program.style().icon() != null) {
    String iconName = program.style().icon();
    int resourceId = getResources().getIdentifier(iconName, "drawable", getPackageName());
}
```

## Cor { #color } 

Ele contém o valor hexadecimal para a cor. Ele pode ser usado para personalizar o fundo, a cor do texto, os títulos das linhas, etc.

```java
program.style().color();    // For example #9C33FF

```


