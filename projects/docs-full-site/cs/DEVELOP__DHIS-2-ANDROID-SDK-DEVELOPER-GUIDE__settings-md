---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/settings.md" 
---
# Nastavení

<!--DHIS2-SECTION-ID:settings-->

Nastavení se stáhne při každé synchronizaci metadat. Existují různé druhy nastavení:

```java
d2.settingModule()
```

- **Nastavení systému**: vlastnosti celého systému, jako je například `flag` nebo `style`.
- **Uživatelská nastavení**: uživatelská nastavení, například `keyDbLocale` nebo` keyUiLocale`.
- **Aplikace Nastavení**: tato nastavení nabízejí další kontrolu nad chováním aplikace. Více o tom v následující části.



## Aplikace Nastavení

<!--DHIS2-SECTION-ID:settings_app-->

Instance DHIS2 může zahrnovat webovou aplikaci nazvanou „Nastavení systému Android“, která umožňuje dálkové ovládání určitých parametrů v aplikaci. Instalace a konfigurace této aplikace je volitelná.

Tato sada SDK stáhne tuto konfiguraci při každé synchronizaci metadat a uchová ji v databázi. Některé z těchto parametrů jsou SDK automaticky spotřebovány (tučně).

Všeobecné:

- Frekvence synchronizace metadat / dat: tato hodnota musí být spotřebována aplikací a použita ke spuštění synchronizace v SDK.
- Mobilní konfigurace: číslo brány, číslo odesílatele. Musí být spotřebovány aplikací a použity ke konfiguraci modulu SMS v SDK.
- **Rezervované hodnoty**: počet hodnot atributů k rezervaci.
- **Šifrovat databázi**: zda má nebo nemá být šifrována místní databáze.

**Programy:** tato část ovládá parametry synchronizace dat programu. Má část definující globální nebo výchozí parametry, které se mají použít při synchronizaci všech programů. Navíc umožňuje nastavit konkrétní nastavení pro konkrétní programy. Všechny tyto parametry jsou spotřebovány SDK a použity v procesu synchronizace.

**Datové Sady:** tato část řídí agregované parametry synchronizace dat. Má část definující globální nebo výchozí parametry, které se mají použít při synchronizaci všech datových sad. Dále umožňuje nastavit konkrétní nastavení pro konkrétní datové sady. Všechny tyto parametry jsou spotřebovány SDK a použity v procesu synchronizace.

```java
// General settings
d2.settingModule().generalSetting().get();

// Program settings
d2.settingModule().programSetting().get();

// DataSet settings
d2.settingModule().dataSetSetting().get();
```

I když tyto parametry jsou automaticky spotřebovávány sadou SDK, aplikace může přepsat některé z těchto hodnot v procesu synchronizace. Může například definovat jiný limit TEI nebo události nebo jinou strategii stahování (limitByOrgUnit, limitByProgram).

