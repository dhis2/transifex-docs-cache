---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/blob/master/docs/content/developer/maps.md"
revision_date: '2022-12-06'
tags:
- Vývoj
---

# Mapy { #android_sdk_maps }

> **Pozor**
>
> Toto je experimentální funkce a v budoucích verzích se může změnit.

SDK má MapModule pro stahování a přístup k informacím souvisejícím s mapami v DHIS2.

Ve výchozím nastavení má DHIS2 některé základní mapy:

- OpenStreetMaps
- Bing: Aby fungovaly, je nutné nastavit klíč bing API na serveru.

Tyto mapové vrstvy se stahují v samostatném volání:

```java
d2.mapsModule().mapLayersDownloader().downloadMetadata()
```

Poté lze k mapovým vrstvám přistupovat pomocí odpovídajícího úložiště sbírky, jako obvykle:

```java
d2.mapsModule().mapLayers()
        .byName().eq("map_layer")
        .withImageryProviders()
        .get()
```

Tyto mapové vrstvy obsahují užitečné informace pro jejich zobrazení pomocí SDK pro mapy, zejména:

- imageUrl: může to vypadat jako `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`.
- subdomény: poskytovatelé map obvykle nabízejí seznam subdomén, například `["a", "b", "c", "d"]`.
- subdomainPlaceholder: token, který musí být nahrazen v imageUrl, v tomto případě `{s}`.

Je jednoduché získat seznam imageUrl iterací seznamu subdomén a jeho nahrazením v adrese URL pomocí zástupného symbolu.

