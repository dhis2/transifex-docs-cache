---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/dhis2-server-requirements.md"
revision_date: "2021-08-10"
---

# Požadavky na server DHIS 2 { #implementation_guide_dhis2_server }

Nová aplikace pro Android DHIS 2 Capture vyžaduje instanci DHIS 2 2.29 nebo vyšší spuštěnou na webovém serveru. Instance DHIS 2 může být umístěna na místním serveru, virtuálním počítači nebo ji lze zakoupit jako software jako služba (spravovaný hosting). Další informace o různých možnostech hostování DHIS 2 naleznete na adrese [https://www.DHIS2.org/hosting](https://www.dhis2.org/hosting).

Tato část poskytuje základní pokyny, jak nakonfigurovat server DHIS 2, který budete muset udělat v prvních dvou scénářích (v místním prostředí a ve virtuálním počítači). Ve třetím scénáři spravovaného hostování byste měli informovat svého poskytovatele, že budete nasazovat aplikaci pro Android, a vést otevřenou diskusi o nejlepších způsobech konfigurace serveru. Měli byste začít sdílením těchto pokynů se svým poskytovatelem spravovaného hostingu.

Server DHIS 2 musí být navržen a nakonfigurován s ohledem na: tok sběru dat, očekávanou analýzu dat a očekávané vizuální uživatelské rozhraní. Pro nasazení DHIS 2 budou zapotřebí minimálně tři servery: _Testovací_, _Produkční_ a _Školící_.

_Testovací_ server bude server, na kterém můžete změnit konfigurace serveru a otestovat výsledky těchto konfigurací. Jakmile budete spokojeni s konfigurací, školení uživatelů by mělo probíhat v jiném prostředí než _Produkční_. Dedikovaný server _Školící_ je ideálním prostředím, ve kterém budete školit své uživatele. Pro všechny účastníky vytvoříte uživatele DHIS 2 a zajistíte, aby všichni těmto změnám rozuměli a cítili se v nich dobře. Posledním krokem, jakmile otestujete konfigurace a proškolíte uživatele, bude nasazení konfigurace do prostředí _Produkční_. Nikdy byste neměli provádět změny konfigurace nebo trénovat své uživatele přímo do prostředí _Produkční_.

DHIS 2 je licencován pod [BSD](http://www.linfo.org/bsdlicense.html), což je licence s otevřeným zdrojovým kódem, a každý si jej může nainstalovat a používat zdarma. Správa instance DHIS 2 však zahrnuje více než nastavení výkonného webového serveru. Nasazení spolehlivého a škálovatelného systému zahrnuje alespoň tyto aspekty:

- Lidské zdroje se znalostmi příslušných technologií, jako jsou webové servery a databázové systémy.
- Spolehlivé zálohování vašeho systému včetně bezpečného úložiště na vzdáleném serveru.
- Použití SSL (HTTPS / šifrování) k zabezpečení soukromých informací, jako jsou hesla, v bezpečí.
- Monitorování prostředků serveru a výkonu aplikace.
- Stabilní a vysokorychlostní připojení k internetu.
- Stabilní napájecí zdroj včetně záložního napájecího řešení.
- Zabezpečené prostředí serveru, aby se zabránilo neoprávněnému přístupu, krádeži a požáru.
- Výkonný hardware s potenciálem škálování spolu se zvýšeným využitím systému.

Aplikace DHIS 2 Capture pro Android běží na mobilních zařízeních, včetně smartphonů, tabletů a Chromebooků. Je důležité sledovat počet programů, počet datových prvků a počet pravidel programu, která jsou uživateli na těchto mobilních zařízeních k dispozici. Měli byste také počítat s dostatkem času na vytvoření potřebných překladů pro vaši konfiguraci metadat. V případě dialogů, nabídek a dalších výzev aplikace, pokud aplikace není přeložena do jazyka, který potřebujete, zašlete nám prosím zprávu v [komunitě DHIS 2](https://community.dhis2.org) a my vám dáme vědět, jak přispět k překladu aplikace.

> **Pozor**
>
> Kromě zde uvedených požadavků na server DHIS2 si uvědomte, že aplikace DHIS2 pro Android může vyžadovat připojení k dalším službám a při zablokování těchto služeb nemusí aplikace plně fungovat. To může platit v implementacích, kde můžete používat přísná pravidla brány firewall, jako je například prostředí URL s nulovou sazbou na základě dohody s poskytovatelem ISP. V těchto případech možná budete chtít zahrnout do seznamu povolených adres URL následující:
>
> - Váš URL server DHIS2
> - [Adresy mapových schránek](https://docs.mapbox.com/help/troubleshooting/firewalls/)
> - Veřejný a/nebo soukromý server Matomo pro statistiky, jak je vysvětleno v [průvodci](https://docs.dhis2.org/en/full/implement/dhis2-android-configuration-guide.html#capture_app_andoid_settings_webapp)
