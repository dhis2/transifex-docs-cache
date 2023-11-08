---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/mobile-device-specs.md"
revision_date: "2021-07-09"
---

# Specifikace mobilního zařízení { #implementation_guide_mobile_specs }

Pokud váš projekt plánuje provést velkou akvizici zařízení, je dobré co nejvíce oddálit většinu akvizice. Cílem je získat nejlepší zařízení, které si můžete dovolit. Technologie, zejména mobilní zařízení, se vyvíjí velmi rychle. Daný model se obvykle obnovuje v ročním cyklu, což spotřebitelům poskytuje meziroční přístup k významným technickým vylepšením, ale s podobným cenovým bodem. Další doporučení týkající se akvizic najdete v části [<span class="underline">Rozšíření</span>](#scale-up).

Specifikace mobilních zařízení pro použití nasazení aplikace DHIS 2 pro Android jsou uvedeny v následující tabulce. Vezměte prosím na vědomí, že tato doporučení jsou velmi obecná, protože vaše zařízení bude výkonně ovlivněno vaší konfigurací. Například mít sledovací program se stovkami programových pravidel bude vyžadovat výkonnější zařízení než v implementaci, kde shromažďujete pouze malou sadu agregovaných dat.

Obecně řečeno, když si musíte vybrat různé verze Androidu, zaměřte se na vyšší. Nákup zařízení od známých značek může být také indikátorem lepšího poprodejního servisu, jako jsou opravy a / nebo aktualizace.

 <table>
 <thead>
 <tr class="header">
 <th> </th>
 <th> <b> mobilní telefony </b> </th>
 <th> <b> tablety </b> </th>
 <th> <b> Chromebooky </b> </th>
 </tr>
 </thead>
 <tbody>
 <tr>
 <td> <b> Stavba </b> </td>
 <td colspan="3"> Pravděpodobně nejdůležitější funkce: toto zařízení bude dělat hodně práce v terénu a musí vydržet více než 2 roky </td>
 </tr>
 <tr>
 <td> <b> značka </b> </td>
 <td colspan="3"> Pokud budete zodpovědní za správu mnoha zařízení, je snazší držet se jedné značky </td>
 </tr>
 <tr>
 <td> <b> OS </b> </td>
 <td colspan="2">
Minimum Supported: Android 4.4 (to be deprecated April 2022) <br />
Minimum Doporučeno pro nová zařízení: <b> Android 7.X </b> <br />
Doporučeno pro nová zařízení: <b> Android 8.X </b> nebo lepší
 </td>
 <td> Zařízení Chrome OS lze aktualizovat na nejnovější verzi systému Chrome OS alespoň 5 let po vydání. Zkontrolujte <a href="https://support.google.com/chrome/a/answer/6220366?hl=en"> <span class="underline"> zde </span> </a> </td>
 </tr>
 <tr>
 <td> <b> procesor </b> </td>
 <td colspan="2"> Doporučeno: 4 jádra, 1,2 GHz </td>
 <td> různé </td>
 </tr>
 <tr>
 <td> <b> RAM </b> </td>
 <td>
Minimum: 1 GB <br />
Doporučeno: 2 Gb nebo více
 </td>
 <td>
Minimum: 1,5 GB <br />
Doporučeno: 3Gb nebo více
 </td>
 <td>
Minimum: 4 GB <br />
Doporučeno: 4 až 8 GB
 </td>
 </tr>
 <tr>
 <td> <b> Úložiště </b> </td>
 <td colspan="2">
Minimum: 8 GB <br />
Doporučeno: 32 GB <br />
Aplikace DHIS 2 nevyužívá mnoho místa. Ukládání osobních obrázků a videí však zabírá spoustu místa
 </td>
 <td>
Minimum: 16 GB <br />
Doporučeno: 32-128 GB
 </td>
 </tr>
 <tr>
 <td> <b> Velikost obrazovky </b> </td>
 <td>
Minimum: 4 "<br />
Doporučeno: od 5,5 "
 </td>
 <td> Minimum: 7 "</td>
 <td> 11 "- 14" </td>
 </tr>
 <tr>
 <td> <b> Fotoaparát </b> </td>
 <td colspan="2">
Minimum: 5Mpx, s bleskem <br />
Doporučeno: minimálně 8 Mpx, flash
 </td>
 <td> volitelně </td>
 </tr>
 <tr>
 <td>
 <b> Příslušenství </b>
* Pouzdro, klávesnice, externí napájení *
 </td>
 <td colspan="2">
Zvažte vhodný vnější kryt a chránič obrazovky. U tabletů zvažte externí klávesnici pro ovládání na stole <br />
Zvažte napájení externí powerbanky (10 000 mAh - 20 000 mAh)
 </td>
 <td>
USB 3G / 4G modem <br />
Myš <br />
Webová kamera
 </td>
 </tr>
 <tr>
 <td> <b> Připojení </b> </td>
 <td colspan="2">
Rádio 4G (LTE) / 3G, <b> odemčené </b>. Pokud importujete zařízení, zkontrolujte kompatibilitu frekvenčních pásem s místními mobilními operátory <br />
Bluetooth 4.0 nebo lepší. WiFi 2,4 GHz &amp; 5 GHz
 </td>
 <td>
Bluetooth 4.0 nebo lepší. WiFi 2,4 GHz &amp; 5 GHz <br />
Externí USB 3G / 4G klíč nebo Wifi hotspot <br />
 </td>
 </tr>
 </tbody>
 </table>

> **Poznámka**
>
> Vezměte prosím na vědomí, že mobilní aplikace DHIS2 aktuálně spoléhá na některé (Služby Google Play)[https://developers.google.com/android/guides/overview], a proto nebude fungovat na zařízeních, která tuto službu nepoužívají. To je běžné u posledních telefonů Huawei a zařízení AOSP.
