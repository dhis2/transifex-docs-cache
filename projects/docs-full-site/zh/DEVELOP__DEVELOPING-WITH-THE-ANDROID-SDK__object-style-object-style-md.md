---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/object-style.md" 
---
# 对象样式  { #object-style } 

 <!--DHIS2-SECTION-ID:object-style-->

一些元素包括称为“样式”的属性，该属性定义图标和颜色。这些视觉信息对于快速浏览应用程序非常有用。一些典型的用例：

- 在程序列表中区分不同的程序和trackedEntityType。
- 在带有optionSet的数据输入表单中，显示带有图标和颜色而不是名称的选项。
- 程序中的不同程序阶段。

此属性是可选的，在大多数情况下未定义。对象样式可能具有图标，或颜色或两者兼有。

## 图标 { #icon } 

DHIS2中使用的图标集包含在SDK中。它们位于资源内的“可绘制”文件夹中。目前，它们是预定义的，无法自定义。

```java

// Illustrative code to get the resource id
if (program.style().icon() != null) {
    String iconName = program.style().icon();
    int resourceId = getResources().getIdentifier(iconName, "drawable", getPackageName());
}
```

## 颜色 { #color } 

它包含颜色的十六进制值。它可用于自定义背景，文本颜色，行标题等。

```java
program.style().color();    // For example #9C33FF

```


