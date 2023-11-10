---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/sysadmin/upgrading.md"
revision_date: "2021-08-18"
---

# Aktualizace { #upgrading-dhis2 }

## Upgrade vs. aktualizace { #upgrading-vs-updating }

Když mluvíme o upgradu DHIS2, obecně máme na mysli jednoduše „přechod na novější verzi“. Mezi _upgrading_ a _updating_ je však důležitý rozdíl.

**Upgrade** : Přechod na novější základní verzi DHIS2 (například z 2.34 na 2.36). Upgrade obvykle vyžaduje plánování, testování, školení (pro nové funkce nebo rozhraní), což může vyžadovat značný čas a úsilí.

**Aktualizace** : Přechod na novější opravu aktuální verze DHIS2 (například z 2.35.1 na 2.35.4). Aktualizace poskytuje hlavně opravy chyb bez změny funkčnosti softwaru. Je to nižší riziko a všem doporučujeme udržovat svou verzi aktuální.

## Než začnete { #upgrading-before-you-begin }

> **Pozor**
>
> Je důležité si uvědomit, že jakmile upgradujete, nebudete moci používat upgradovanou databázi se starší verzí DHIS2. To znamená, že **není možné přejít na nižší verzi**.
>
> Pokud se chcete vrátit ke starší verzi, musíte tak učinit s kopií databáze, která byla vytvořena z této starší verze nebo z předchozí verze. Proto je téměř vždy dobré si před upgradem vytvořit kopii databáze.

## Provádění upgradu { #upgrading-process }

Bez ohledu na to, zda upgradujete nebo aktualizujete, technický proces je víceméně stejný. Budeme tomu říkat pouze upgrade.

### 1 Chraňte svá data { #upgrading-safeguard-your-data }

V závislosti na tom, jaký druh instance DHIS2 máte a k čemu ji používáte, je prvním krokem ujistit se, že můžete obnovit všechna důležitá data, pokud se při upgradu něco pokazí.

To znamená provádění standardních úloh správy systému, jako jsou:

1. Zálohování databáze
2. Testování ve vývojovém prostředí
3. Plánování odstávky (aby se zabránilo zadávání dat během upgradu)
4. atd.

### 2 Upgradujte software { #upgrading-upgrade-the-software }

#### Od verze 2.29 nebo nižší { #upgrading-pre-230 }

Pokud začínáte od verze 2.29 nebo nižší, musíte nejprve upgradovat na verzi 2.30 verzi po verzi ručně, podle poznámek k upgradu, které najdete pod konkrétními čísly verzí na [našem webu vydání](https://github .com/dhis2/dhis2-releases). Když jste ve verzi 2.30, můžete přejít k další sekci.

#### Od verze 2.30 nebo vyšší { #upgrading-post-230 }

Pokud začínáte alespoň od verze 2.30:

1. **Přečtěte si všechny poznámky k upgradu od vaší aktuální verze až po cílovou verzi na [našem webu vydání](https://github.com/dhis2/dhis2-releases).** Ujistěte se, že vaše prostředí splňuje všechny požadavky
2. Pokud jste tak neučinili v kroku 1, vytvořte si kopii databáze
3. Odstraňte z databáze všechny materializované pohledy SQL
4. Zastavte server
5. Nahraďte war soubor cílovou verzí (není potřeba upgradovat na přechodné verze, ve skutečnosti se to nedoporučuje)
6. Spusťte server

Nyní byste měli být připraveni využívat nové opravy a funkce.
