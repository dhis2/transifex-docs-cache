---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/edit/master/docs/src/commonmark/en/content/capture-app/recommendations-for-a-dhis2-mobile-deployment.md" 
---
# Doporučení pro mobilní nasazení DHIS 2  { #recommendations } 

<!-- DHIS2-SECTION-ID:recommendations -->

Pokud plánujete nasadit aplikaci DHIS2 pro Android v terénu, důrazně vám doporučujeme přečíst si [Pokyny pro implementaci pro mobilní zařízení](https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/about-this-guide.html) které publikoval UiO. Zahrnuje kapitoly o technologických požadavcích, aspektech zabezpečení a konfigurace a testování a zavedení doporučení. Níže najdete stručně představené klíčové aspekty, doporučujeme přečíst si rozšířený dokument.

## Specifikace mobilních zařízení { #recommendations_mdm } 

<!-- DHIS2-SECTION-ID:recommendations_mdm -->

Aplikace pro Android je kompatibilní a podporovaná pro DHIS 2 verze 2.30, 2.31, 2.32, 2.33, 2.34 a 2.35. A s 2.29 nemá žádné zlomové změny.

Vyžaduje zařízení se systémem Android v4.4 nebo novějším.

V [konkrétní části pokynů pro implementaci pro mobilní zařízení](https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/mobile-device-specifications.html) najdete doporučení pro nové akvizice mobilních zařízení pro nasazení systému Dhis2 pro Android.

## Testování a pilotování { #recommendations_testing } 

<!-- DHIS2-SECTION-ID:recommendations_testing -->

Pokud plánujete nasadit aplikaci DHIS 2 pro Android v terénu, měli byste nejprve provést celé kolo testování aplikace ve vaší vlastní konfiguraci.

Tato aplikace byla důkladně testována na demo serverech a během testování beta verze byla testována také na některých skutečných konfiguracích. Víme však, že každá konfigurace DHIS 2 je v mnoha směrech speciální a může způsobit nesrovnalosti, které nejsme schopni identifikovat.

Důrazně doporučujeme před pilotováním provést komplexní testování aplikace na vašem vlastním serveru.

## Jak migrovat do aplikace Android Capture { #recommendations_migrate } 

<!-- DHIS2-SECTION-ID:recommendations_migrate -->

Pokud jste připraveni na nasazení nové aplikace pro Android v terénu a vaši uživatelé již používají Zachycení Událostí nebo Tracker Capture, měli byste postupovat podle těchto kroků:

1.  Synchronizujte data aktuální aplikace, kterou používáte

    > **Warning**
    >
    > Deleting the app without syncing can cause information loss.

2.  Stáhněte a nainstalujte si aplikaci DHIS 2 pro Android
3.  Přihlašte se pomocí vašich přihlašovacích údajů a všechna data budou synchronizována.


