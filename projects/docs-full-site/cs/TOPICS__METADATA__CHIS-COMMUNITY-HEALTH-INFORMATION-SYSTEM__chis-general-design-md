---
edit_url: "https://github.com/dhis2-metadata/CHIS-AGG-Community_Health_Information_System/blob/master/docs/chis_aggregate_design.md"
revision_date: "2022-01-06"
---

# Komunitní zdravotnický informační systém (CHIS) – dokument o návrhu systému { #chis-system-design }

## 1. Úvod { #1-introduction }

Standardizovaný a fungující komunitní zdravotnický informační systém (CHIS) je klíčový pro monitorování zdraví, potřeb a postupů na úrovni komunity. Balíček metadat komunitních zdravotních informačních systémů (CHIS) je navržen tak, aby usnadnil zachycení a analýzu základní sady ukazatelů pro komunitní zdravotnické služby. Balíček metadat CHIS doprovází [Analýza a použití komunitních dat WHO: Pokyny pro monitorování komunitních zdravotních služeb](https://www.healthdatacollaborative.org/working-groups/community-data/guidance-for-community-health-worker-strategic-information-and-service-monitoring/). Pokyny reagují na rezoluci Světového zdravotnického shromáždění WHA72.3 z roku 2019, která požaduje a) sladění dat a digitálního úsilí s cílem optimalizovat programy komunitních zdravotních pracovníků (CHW) ab) vytvoření silnější důkazní základny pro dopad CHW.

Tento balíček byl navržen v reakci na potřebu sladit úsilí o posílení komunitních programů, sledovat jejich dopad a provádět na důkazech založené politické úpravy podle skutečných potřeb cílových komunit. Návrh systému byl založen na letech spolupráce mezi HISP a MZ implementací DHIS2 pro správu dat komunitních zdravotních služeb. [Praktický průvodce](https://drive.google.com/file/d/0B5Jsq_TjUPGjdFNVTzZNYnhlYzQ/view?resourcekey=0-mU2mmaaahcyHEaJ7e2_aqg) je k dispozici také pro národní a místní tvůrce rozhodnutí.

podílí se na návrhu, plánování, nasazení, správě a rozšiřování úspěšného CHIS založeného na DHIS2. Tato příručka (vyvinutá organizacemi HISP UiO, Akros Zambia a Health Data Collaborative) doplňuje normativní pokyny WHO o hloubkový přehled klíčových otázek, které by měly být zváženy při řešení problémů souvisejících s řízením, návrhem, vývojem a používáním CHIS.

## 2. Přehled návrhu systému { #2-system-design-overview }

### 2.1. Modulární struktura { #21-modular-structure }

Komunitní zdravotničtí pracovníci (CHW) jsou zodpovědní za širokou škálu úkolů a činností v závislosti na zemích a kontextech. Z tohoto důvodu byly balíček CHIS a pokyny WHO/UNICEF uspořádány s **modulárním přístupem**. Takový návrh umožňuje větší flexibilitu, protože může být upraven pro použití v rámci země podle úrovně vyspělosti CHIS a šíře služeb poskytovaných na úrovni komunity.

Balíček CHIS obsahuje **21 modulů** a **37 datových sad** s měsíční a/nebo roční periodicitou sběru dat.

1. [Zdraví dospívajících (měsíční a roční)](#ch-ado-aggregate-design)
2. [Zdraví dětí (měsíční a roční)](#ch-cdh-aggregate-design)
3. [Ochrana dětí a mezilidské násilí (měsíční a roční)](#ch-cpiv-aggregate-design)
4. [Občanská registrace a zásadní statistiky (měsíční a roční)](#ch-crvs-aggregate-design)
5. [Čistá energie (roční)](#ch-ene-aggregate-design)
6. [Komunitní dohled (měsíčně)](#ch-cbs-aggregate-design)
7. [HIV (měsíční a roční)](#ch-hiv-aggregate-design)
8. [Integrovaná komunitní správa případů (měsíčně)](#ch-iccm-aggregate-design)
9. [Imunizace (měsíční a roční)](#ch-epi-aggregate-design)
10. [Malárie (měsíční a roční)](#ch-mal-aggregate-design)
11. [Zdraví matek (měsíční a roční)](#ch-mat-aggregate-design)
12. [Duševní zdraví (měsíční a roční)](#ch-men-aggregate-design)
13. [Nepřenosné nemoci (měsíční a roční)](#ch-ncd-aggregate-design)
14. [Zdraví novorozenců (měsíční a roční)](#ch-nbh-aggregate-design)
15. [Zanedbané tropické nemoci (měsíční a roční)](#ch-ntd-aggregate-design)
16. [Výživa (měsíční a roční)](#ch-nut-aggregate-design)
17. [Služby zaměřené na lidi (měsíční a roční)](#ch-pcs-aggregate-design)
18. [Složení populace (roční)](#ch-pop-aggregate-design)
19. [Sexuální a reprodukční zdraví (měsíční a roční)](#ch-srh-aggregate-design)
20. [Tuberkulóza (měsíční a roční)](#ch-tb-aggregate-design)
21. [Voda, sanitace a hygiena (ročně)](#ch-wash-aggregate-design)

Princip flexibility se odráží také v přítomnosti **stejných datových prvků a indikátorů v různých modulech**. Ty byly rozděleny podle teoretické možnosti přítomnosti určitých aktivit spojených s konkrétními moduly.

Například datový prvek „_CH041a – Osoby hodnocené pro poruchy MNS/stavy MH_“ patří do sekce hodnocení potřeb duševního zdraví v komunitě. Jelikož aktivita může být součástí různých aktivit, je zahrnuta do šesti modulů (Psychické zdraví, Zanedbané tropické nemoci, Zdraví matek, Zdraví dospívajících, HIV, Tuberkulóza). V závislosti na povaze služeb poskytovaných sítěmi CHW lze tento datový prvek přerozdělit, upravit nebo odstranit. Protože mapování rozsáhlého balíčku, jako je balíček CHIS, může být matoucí, dokument o návrhu systému pro každý modul uvádí moduly a datové sady, kde lze nalézt stejný DE a/nebo indikátor.

Tento balíček obsahuje metadata pro měsíční a roční reporty agregovaných dat a analýzy. Proto **nezahrnuje** metadata na individuální úrovni. Tento balíček metadat není určen k podpoře individuálních konzultací ze strany CHW, ale k usnadnění rutinního souhrnného hlášení do HMIS.

### 2.2. Pracovní postup { #22-workflow }

Typy služeb, které komunitní zdravotní pracovníci poskytují v komunitách, jsou mezi zeměmi vysoce heterogenní. Každý modul obsahuje seznam standardizovaných ukazatelů, které mají být přezkoumány, přizpůsobeny a přijaty podle funkcí CHW ve zdravotním systému země, zátěže jejich práce a vyspělosti CHIS. Pokyny WHO/UNICEF navrhují **vícestupňový přístup** pro mapování národních strategií a identifikaci modulů/ukazatelů potřebných pro monitorování a hodnocení aktivit komunity, jak je znázorněno níže:

![pracovní postup CHIS](resources/images/chis-workflow.png)

### 2.3. Zamýšlení uživatelé { #23-intended-users }

Balíček byl vyvinut s ohledem na následující uživatelské profily:

1. **Národní a subnárodní programoví manažeři** zodpovědní za analýzu dat a monitorování výkonu
2. **Okresní manažeři a nadřízení** zodpovědní za řízení a monitorování komunitních aktivit
3. **Komunitní zdravotničtí pracovníci** poskytující zdravotní služby, provádění komunitních hodnocení, shromažďování a hlášení dat o komunitních zdravotních aktivitách

## 3. Skupiny uživatelů { #3-user-groups }

V rámci konfigurace balíčku byly vytvořeny skupiny uživatelů, které se používají ke správě nastavení sdílení v metadatech pro všechny moduly. Mezi základní metadata, která používají tato nastavení sdílení, patří zejména datové sady, řídicí panel, indikátory a datové prvky. Mezi 3 vytvořené uživatelské skupiny patří:

1. **Správce CHIS** – uživatelé v této skupině mají přístup k zobrazení/úpravám metadat a přístup pouze k zobrazení datových hodnot v souborech dat
2. **Přístup CHIS** – uživatelé v této skupině mají přístup pouze k metadatům a hodnotám dat v sadách dat
3. **CHIS Capture** – uživatelé v této skupině mají přístup pouze k zobrazení metadat a přístup k zobrazení/úpravě hodnot dat v sadách dat

I když je důležité tyto userGroups při instalaci tohoto balíčku udržovat, můžete je zkontrolovat v souladu s jakýmkoli existujícím nastavením nebo zásadou userGroups v instanci hostitele.

## 4. Poděkování { #4-acknowledgements }

Balíček CHIS byl vyvinut ve spolupráci s **UNICEF** a **WHO** s podporou **Globálního fondu pro boj s AIDS, tuberkulózou a malárií**.

## 5. Reference { #5-references }

[Analýza a využití dat komunitních zdravotnických služeb. Pokyny pro komunitní zdravotnické pracovníky, strategické informace a monitorování služeb.](https://www.healthdatacollaborative.org/fileadmin/uploads/hdc/Documents/Working_Groups/Community_Data/210305_UNICEF_CHW_Guidance_EN.pdf). Březen 2021. Vydal Dětský fond OSN (UNICEF)

[Pokyny pro komunitní zdravotnické informační systémy DHIS2](https://drive.google.com/file/d/0B5Jsq_TjUPGjdFNVTzZNYnhlYzQ/view?resourcekey=0-mU2mmaaahcyHEaJ7e2_aqg). 2017. Program zdravotnických informačních systémů University of Oslo
