---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/edit/master/docs/src/commonmark/en/content/mdm/considerations.md" 
---
# Úvahy  { #considerations } 

V tomto dokumentu budou pojmy MDM a EMM použity zaměnitelně. To není úplně přesné, ale slouží to ke zjednodušení dokumentu. MDM samo o sobě nezohledňuje nasazení aplikací, zatímco EMM zahrnuje mnohem více možností, které nejsou v rozsahu tohoto dokumentu. Proto lze říci, že tento dokument pokrývá někde mezi těmito dvěma pojmy.

![MDM/EMM rozdíly](../content/mdm/resources/images/image7.png)

## Proč MDM pro DHIS2? { #why-an-mdm-for-dhis2 } 

Správa mobilních zařízení označuje software používaný ke správě mobilních zařízení. Pravděpodobně budete chtít používat software MDM, když budete muset podporovat stovky zařízení a bude nutné řídit distribuci aplikace DHIS2 mezi zařízeními, poskytovat technickou podporu a vynucovat institucionální zásady.


Například pokud máte projekt, kde bude distribuováno 1000 zařízení Android (komunitní pracovníci) pomocí mobilních dat k odeslání informací na centrální server DHIS2, může vám MDM pomoci:

* Možnost vydat novou verzi aplikace DHIS2 pro Android kdykoli budete chtít. Všimněte si, že ve výchozím nastavení mohou být zařízení nakonfigurována na automatickou aktualizaci nebo budete možná muset požádat o manuální aktualizaci od uživatele. MDM vám dává možnost vybrat si, zda chcete zařízení v daném okamžiku aktualizovat, nebo raději čekat (například dokud neprovedete školení vysvětlující nové možnosti aplikace).
* Vyhledejte a sledujte zařízení v případě ztráty nebo je na dálku otřete v případě, že mohou obsahovat citlivé informace. Přestože aplikace pro Android DHIS2 již obsahuje bezpečnostní opatření, pokud jsou telefony používány ke shromažďování některých obrázků z aplikace (například jednotlivců, lékařských zpráv atd.), Může představovat ohrožení soukromí / bezpečnostní riziko.
* Zakažte použití mobilních dat pro libovolnou aplikaci kromě aplikace pro Android DHIS2 nebo zakažte možnost používat bezdrátový hotspot, aby se datové balíčky zakoupené projektem spotřebovaly pouze pro DHIS2.

## Jak funguje MDM? { #how-does-an-mdm-work } 

Tato část vysvětluje opravdu stručně, jak MDM / EMM funguje a jak může ovlivnit současnou infrastrukturu implementace DHIS2.


V implementaci bez MDM komunikují zařízení jedinečně a přímo se serverem DHIS2, jak je znázorněno na obrázku níže.

![Standardní komunikační proces mezi aplikací DHIS 2 pro Android a serverem DHIS 2](../content/mdm/resources/images/image9.png)

Přidání MDM ovlivní infrastrukturu, protože bude přidán nový server. Tento server může být buď v lokálních prostorách (pokud to řešení podporuje), nebo v cloudu. Ačkoli se to nedoporučuje ve skutečně konkrétních případech (malá nasazení nebo omezení rozpočtu), server používaný k hostování DHIS2 lze také použít, takže bude potřeba pouze jeden server.

Přidání MDM také vyžaduje přidání pozice manažera MDM, což znamená, že k nastavení a správě tohoto MDM je třeba přiřadit osobu. Tento správce implementuje konkrétní konfiguraci na serveru MDM a možná bude nutné nakonfigurovat mobilní zařízení.

![MDM je přidán do infrastruktury](../content/mdm/resources/images/image12.png)

Konfigurace implementovaná na serveru MDM je načítána zařízeními, což znamená použití specifických zásad na zařízení, která mohou omezovat způsob, jakým lze zařízení používat. V případě potřeby může také umožnit vzdálené sledování nebo vymazání zařízení.

![Zařízení nyní komunikují se dvěma různými servery: DHIS 2 a MDM](../content/mdm/resources/images/image6.png)

Obrázek níže představuje tyto kroky kombinované do jednoho grafu.

![Komunikace v implementaci DHIS 2 s MDM](../content/mdm/resources/images/image5.png)


