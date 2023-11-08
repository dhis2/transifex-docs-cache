---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.33/src/commonmark/en/content/user/relationship-model.md"
revision_date: '2019-04-29'
---

# Vztahový model { #relationship_model } 
<!--DHIS2-SECTION-ID:relationship_model-->

Vztah představuje spojení mezi dvěma entitami v Trasovacím modelu. Vztah je považován za data v DHIS2 a je založen na typu vztahu, podobně jako je instance trasované entity založena na Typu trasované entity.

Vztahy vždy zahrnují dvě entity a tyto entity mohou zahrnovat instance trasovaných entit, registrace a události a jakoukoli jejich kombinaci. Upozorňujeme, že ne všechny tyto kombinace jsou v aktuálních aplikacích k dispozici.

Kromě toho lze vztahy definovat jako jednosměrné nebo obousměrné. Jediným funkčním rozdílem je v současné době to, že k jejich vytváření je nutná různá úroveň přístupu. Jednosměrné vztahy vyžadují, aby měl uživatel přístup k zápisu dat do entity „z“ a přístup ke čtení dat pro entitu „do“, zatímco obousměrné vztahy vyžadují přístup k zápisu dat pro obě strany.

## Typ vztahu { #relationship_model_relationship_type } 
<!--DHIS2-SECTION-ID:relationship_model_relationship_type-->

Typ relace je definice vlastností, které vztah má. Vztahy se vždy skládají ze dvou stran, označovaných jako „od“ a „do“, a to, jaké entity mohou být obsaženy pro každou stranu, určuje typ vztahu. Vlastnosti, které určují, co každý může obsahovat, se nazývají omezení, odConstraint respektive toConstraint. Tato omezení jsou významná při pozdější práci s daty, aby bylo možné pochopit, co vztah může a co nemůže obsahovat.

Každá z omezení definovaných v typu Vztahu se skládá z několika vlastností. Primární vlastnost je vztah entity, který rozhoduje o tom, jaký druh entit může vztah obsahovat. Entity mohou být pro každé omezení jednou z následujících:

* Instance trasované entity
* Zápis
* událost

V závislosti na druhu vztahu entity, kterou vyberete, můžete zvolit další omezení pro každé omezení. Následující tabulka vysvětluje různé kombinace, které můžete konfigurovat:

|                     | Instance trasované entity | Zápis | událost    |
|---------------------|-------------------------|------------|----------|
| Typ trasované entity | Požadované                | Volitelný   | -        |
| Program             | -                       | Požadované   | -        |
| Fáze programu       | -                       | Požadované   | Volitelný |

Tato další omezení budou vyžadovat, aby se entita před vytvořením shodovala se sadou omezení. Například pokud je váš vztah mezi matkou a dítětem, obě omezení by měla jejich požadovaný typ trasovaného subjektu nastavený na Osoba a mohl by volitelně nastavit Zápis do Zdravotního programu Mateřství respektive Dětského Programu. Tímto způsobem je do těchto vztahů povoleno zahrnout pouze Trasované instance entit, které jsou typu Osoba a které jsou zapsány v požadovaném programu.

Kromě omezení, které může mít typ vztahu, lze každý vztah nastavit na obousměrný, pravdivý nebo nepravdivý. Pokud je vlastnost nastavena na hodnotu false, jsou vztahy považovány za jednosměrné. Jak již bylo zmíněno dříve, jediným funkčním rozdílem mezi těmito vztahy je, jak přísný je přístup při jejich vytváření nebo aktualizaci - obousměrný je nejpřísnější. Vztahy jsou také v uživatelském rozhraní prezentovány odlišně na základě toho, zda je vztah obousměrný nebo jednosměrný.

Jedna důležitá věc, kterou je třeba si všimnout u obousměrných vztahů, je, že strany „od“ a „do“ jsou v databázi stále významné, což znamená, že každá entita musí odpovídat omezení pro tuto stranu. Z pohledu uživatele je však každá strana každé entity uložena jako nevýznamná.
