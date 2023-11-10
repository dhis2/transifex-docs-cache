---
edit_url: "https://github.com/dhis2-metadata/C19_CS/blob/master/docs/covid19_upgrade_notes_02_to_03.md"
revision_date: "2021-03-23"
---

# Poznámky k upgradu { #upgrade-notes }

> **_ POZNÁMKA _**: Tento dokument je pouze pro ty, kteří instalují novou verzi (v0.3.x) uvedeného balíčku oproti předchozí verzi (v0.2/v0.1). Pokud instalujete na novou instanci, přečtěte si úplné pokyny k instalaci.
>
> Úplné pokyny k instalaci:
>
> [Sledování na základě případů a sledování kontaktů](covid-19-tracker-installation.html)
>
> [Program událostí sledování](covid-19-events-installation.html)
>
> [Hlášení agregovaného sledování](covid-19-aggregate-installation.html)

## Balíček sledování a trasování kontaktů, Program sledování událostí { #case-based-surveillance-contact-tracing-package-surveillance-event-program }

Tyto balíčky (v0.3.3 / v.0.3.2) můžete nainstalovat přímo na dříve existující balíček. To by mělo být provedeno v testovacím / vývojovém prostředí jako vždy.

1. Přejmenujte aktuální typ indikátoru „procenta“ (například [smazat] - procento)
2. Pokud instalujete více balíků, importujte nové balíčky v následujícím pořadí
    1. Dohled na základě případů: + Registrace kontaktů a sledování: v0.3.3 jsou součástí jednoho balíčku
    2. Program Sledování Událostí: v0.3.2
3. Odstraňte typ procentního indikátoru, který jste přejmenovali

Pokud instalujete pouze jeden z balíčků a ne oba, můžete po přejmenování indikátoru importovat jeden balíček, než pokračovat v odstraňování předchozího typu indikátoru po jeho importu.

To je postarat se o zarovnání typů ID indikátorů napříč agregovacími a trasovacími balíčky.

## Souhrnné přehledové zprávy { #aggregate-surveillance-reporting }

Tento balíček (v0.3.2) můžete nainstalovat přímo na dříve existující balíček (v0.1). To by mělo být provedeno v testovacím / vývojovém prostředí jako vždy.

1. Při importu tohoto balíčku použijte spíše režim sloučení „Nahradit“ než „Sloučit“. Sloučit je výchozí režim, takže jej budete muset při importu změnit, nebo jej nastavit, pokud importujete přes API.

![Režim sloučení: Nahradit](resources/images/merge-mode-replace.png "Režim sloučení zvolit Nahradit")

1. Po importu tohoto balíčku proveďte následující:
    1. Spusťte aplikaci Datová Administrace
    2. Přejděte na „Údržba“
    3. Vyberte „Vymazat mezipaměť aplikací“ a „Znovu načíst aplikace“
    4. Vyberte možnost „Provést údržbu“
