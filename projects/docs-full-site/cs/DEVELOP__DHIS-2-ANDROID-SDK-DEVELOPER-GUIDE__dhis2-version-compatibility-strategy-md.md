---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/compatibility-strategy.md" 
---
# Strategie kompatibility verzí DHIS2

<!--DHIS2-SECTION-ID:compatibility_strategy-->

Sada SDK zaručuje kompatibilitu s nejnovějšími třemi vydáními DHIS 2 (viz [Kompatibilita](#compatibility)). V případě, že SDK je stále kompatibilní s předchozími verzemi DHIS2 a nebyly zjištěny žádné zásadní problémy, lze kompatibilitu rozšířit na předchozí verze.

Aby se zabránilo náhodnému přihlášení do nepodporovaných instancí DHIS 2, SDK blokuje připojení k verzi, která ještě není podporována nebo která byla zastaralá.

Pokud jde o datový model a kompatibilitu, hlavním přístupem je rozšíření datového modelu, aby bylo možné podporovat všechny verze DHIS 2. Obvykle se stává, že nové verze DHIS 2 zavádějí další funkce a neodstraňují stávající, takže podpora nové verze DHIS 2 obvykle znamená použití nejnovějšího datového modelu.

Obecným pravidlem je, že se SDK snaží vyhnout prolomení změn ve svém API a nové funkce jsou pro uživatele volitelné. Toto pravidlo se dodržuje co nejvíce, ale existují případy, kdy podpora starých a nových API, aby nedošlo k rozbití, má velmi vysoké náklady. V tomto scénáři může **SDK zavést nejnovější změny, aby byly kompatibilní s novou verzí DHIS 2**.

Tady najdete několik příkladů změn v SDK a efekt v aplikaci.

## Příklad: drobná změna

Do verze 2.30 měl programový model booleovský atribut zvaný „captureCoordinates“. Tento atribut označuje, zda musí být v tomto programu uloženy souřadnice (bod). Od 2.30 byl tento atribut nahrazen „featureType“ se 4 možnými hodnotami: NONE, POINT, POLYGON, MULTI_POLYGON.

*Změny v SDK:*

Od 2.30 SDK používá atribut „featureType“. Pokud je verze serveru nižší než 2,30, SDK mapuje hodnotu „captureCoordinates“ na:

- false - ŽÁDNÝ
- true - POINT

*Změny v aplikaci:*

Aplikace je nyní nucena používat "featureType". Úpravy v kódu jsou celkem jednoduché.

## Příklad: velká změna

Od verze 2.30 trpěl relační model hlubokým refaktorem, aby umožňoval vztahy mezi událostí, registrací a trackedEntityInstances. SDK přijala model pro 2.30 a vystavuje tento model aplikaci. Při interakci s API se SDK interně překládá mezi oběma modely.

*Změny v aplikaci:*

Tato změna znamená, že aplikace musí přijmout jiný model a změny nejsou tak jednoduché.


