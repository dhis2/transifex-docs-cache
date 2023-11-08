---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/organisation-units.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Unités d’Organisation { #organisation-units } 

Dans le DHIS2, l'emplacement des données, le contexte géographique, est 
représenté par des unités organisationnelles. Les unités organisationnelles peuvent être soit 
un établissement de santé ou un département/sous-unité fournissant des services, soit une 
unité administrative représentant une zone géographique (par ex, un 
district de santé).

Les unités d'organisation sont situées dans une hiérarchie, également appelée 
arbre. La hiérarchie reflète la structure administrative de la santé et 
ses niveaux. Les niveaux typiques d'une telle hiérarchie sont le niveau national, 
le niveau de la province, le niveau du district et le niveau de l'établissement. Dans le DHIS2, il n'existe qu'une seule 
hiérarchie organisationnelle. Par conséquent, la manière dont elle est définie et mappée à la 
réalité doit faire l'objet d'une attention particulière. Les zones géographiques et les niveaux 
définis dans la hiérarchie organisationnelle principale auront un impact majeur 
sur la facilité d'utilisation et les performances de l'application. En outre, il existe 
des moyens d'aborder des hiérarchies et des niveaux alternatifs, comme expliqué 
dans la section intitulée Groupes d'unités d'organisation et ensembles de groupes plus 
bas.

## Conception de la hiérarchie de l'unité d'organisation { #organisation-unit-hierarchy-design } 

Le processus de conception d'une hiérarchie d'unités d'organisation efficace comporte de nombreux 
aspects :

  - *Englobe tous les établissements de santé déclarants:* Tous les établissements de santé 
    qui contribuent à la collecte de données nationales doivent être inclus 
    dans le système. Les établissements de tous types d'appartenance doivent être
    inclus, y compris les établissements privés, publics, les ONG et les établissements confessionnels.
    Souvent, les établissements privés représentent la moitié du nombre total
    d'établissements dans un pays et se voient imposer des politiques de communication des données,
    ce qui signifie qu'il est nécessaire d'incorporer les données de ces
    établissements pour obtenir des chiffres agrégés nationaux
    réalistes.

  - *Mettre l'accent sur la hiérarchie administrative en matière de santé:* Un pays possède généralement 
    plusieurs hiérarchies administratives qui ne sont souvent ni bien
    coordonnées ni harmonisées. Lors de la conception de la base
    de données DHIS2, il convient de garder à l'esprit les domaines les plus
    intéressants et ceux qui seront le plus souvent demandés pour l'analyse des
    données. DHIS2 gère principalement des données sur la santé et effectue 
    des analyses basées sur la structure administrative de la santé. Cela signifie que
    même si des ajustements peuvent être apportés pour tenir compte de domaines tels que
    les finances et l'administration locale, le point de départ de la hiérarchie des unités 
    d'organisation du DHIS2 devrait être les régions administratives
    de la santé.

<!-- end list -->

  - *Limiter le nombre de niveaux hiérarchiques des unités d'organisation:* Pour répondre 
    aux besoins d'analyse provenant de divers organismes tels que le
    gouvernement local et le trésor, il est tentant d'inclure 
    tous ces domaines en tant qu'unités d'organisation dans la base de données DHIS2.
    Cependant, pour des raisons de performance, il convient d'essayer de limiter
    les niveaux de la hiérarchie des unités d'organisation au plus petit nombre possible.
    La hiérarchie est utilisée comme base pour l'agrégation des données 
    à présenter dans l'un ou l'autre des outils de rapport, de sorte que lors de la production 
    de données agrégées pour les niveaux supérieurs, l'application DHIS2 doive
    rechercher et additionner les données enregistrées pour toutes les unités
    d'organisation situées plus bas dans la hiérarchie. L'augmentation du nombre
    d'unités d'organisation aura donc un impact négatif sur les performances
    de l'application et un nombre excessivement élevé pourrait devenir un
    problème important à cet effet.

    Par ailleurs, la plupart des outils d'analyse de DHIS2 
    reposent sur la sélection dynamique de l'unité d'organisation "mère"
    de celles qui doivent être incluses. Par exemple, il est
    possible de sélectionner une province et d'inclure dans le rapport les districts appartenant à cette
    province. Si le niveau du district est le plus 
    utile du point de vue de l'analyse et qu'il existe plusieurs niveaux 
    hiérarchiques entre ce niveau et celui de la province, ce 
    type de rapport sera inutilisable. Lors de la constitution de la 
    hiérarchie, il convient de se concentrer sur les niveaux qui seront 
    fréquemment utilisés dans les rapports et l'analyse des données et de laisser de côté les niveaux
    qui sont rarement ou jamais utilisés, car cela aura un impact à la fois 
    sur les performances et la maniabilité de l'application.

  - *Éviter les relations individuelles:* Un autre principe directeur pour
    la définition de la hiérarchie est d'éviter de relier des niveaux qui ont des 
    rapports parents-enfants presque individuels, ce qui signifie que, par exemple, un district
    (parent) devrait avoir en moyenne plus d'une collectivité locale (enfant)
    au niveau inférieur avant qu'il ne soit logique d'ajouter un niveau de collectivité locale
    à la hiérarchie. Les rapports parents-enfants de 1:4 ou plus sont beaucoup plus
    utiles pour l'analyse des données, car ils permettent d'examiner, par exemple,
    comment les données d'un district sont réparties dans les différents sous-domaines et 
    comment elles varient. De tels exercices d'approfondissement ne sont pas très utiles lorsque 
    le niveau inférieur a la même population cible et les mêmes
    établissements de santé que le parent.

    L'omission de niveaux géographiques lors du mapping de la réalité sur la hiérarchie des unités d'organisation de DHIS2
    peut s'avérer difficile et susciter la
    résistance de certaines parties prenantes, mais il faut garder à l'esprit
    qu'il existe des moyens de produire des rapports basés sur
    des niveaux géographiques qui ne font pas partie de la hiérarchie 
    organisationnelle de DHIS2, comme il sera expliqué dans la section suivante.

## Groupes d'unités d'Organisation et ensembles de groupe { #organisation-unit-groups-and-group-sets } 

Dans  DHIS2, les unités d'organisation peuvent être regroupées en groupes d'unités d'organisation, 
et ces groupes peuvent être organisés en ensembles de groupes. Combinés, ils 
peuvent imiter une hiérarchie organisationnelle alternative qui peut être utilisée lors 
de la création de rapports et d'autres résultats de données. Outre le fait qu'ils représentent 
des lieux géographiques alternatifs ne faisant pas partie de la hiérarchie principale, ces 
groupes sont utiles pour attribuer des systèmes de classification aux établissements de 
santé, par exemple sur la base du type ou de la propriété des établissements. Un nombre 
quelconque d'ensembles de groupes et de groupes peut être défini dans l'application 
via l'interface utilisateur, et tous ces ensembles sont définis localement pour chaque 
base de données DHIS2.

Un exemple illustre le mieux ce point : En règle générale, on souhaite fournir 
une analyse basée sur la propriété des établissements. Dans ce cas, il 
faudra créer un groupe pour chaque type de propriété, par exemple " Ministère de la santé ", 
" privé " et " ONG ". Tous les établissements figurant dans la base de données doivent alors 
être classés et affectés à l'un de ces trois groupes. Ensuite, 
l'on créera un ensemble de groupes appelé "Propriété" auquel les trois 
groupes ci-dessus sont assignés, comme illustré dans la figure 
ci-dessous.

![](resources/images/organisation_unit_hiearchy.png)

De même, il est possible de créer un ensemble de groupes pour un niveau administratif 
supplémentaire, par ex. les collectivités locales. Toutes les collectivités locales doivent être 
définies en tant que groupes d'unités d'organisation, puis affectées à un ensemble de groupes 
appelé "Collectivités locales". La dernière étape consiste à affecter tous les établissements 
de santé à un et un seul des groupes de collectivités locales. Cela permet 
au DHIS2 de produire des rapports agrégés pour chaque collectivité locale (en additionnant 
les données de tous les établissements de santé assignés) sans devoir 
inclure le niveau de la collectivité locale dans la hiérarchie organisationnelle principale. 
La même approche peut être suivie pour tout niveau administratif ou géographique 
supplémentaire nécessaire, en définissant un groupe par niveau 
supplémentaire. Avant de passer à la conception de ce niveau dans le DHIS2, il est nécessaire d'établir un mapping entre 
les zones du niveau géographique supplémentaire et les établissements de santé 
de chaque zone.

Une propriété essentielle du concept d'ensemble de groupes dans DHIS2 à comprendre est 
*l'exclusivité*, qui implique qu'une unité d'organisation ne peut être membre que 
d'un seul des groupes d'un ensemble de groupes. Une violation de cette règle entraînerait 
une duplication des données lors de l'agrégation des données sur les établissements de santé par les 
différents groupes, car un établissement affecté à deux groupes dans le même ensemble de groupes 
erait compté deux fois.

À partir de cette structure, DHIS2 peut fournir des données agrégées pour chacun 
des types de propriété des unités d'organisation grâce au "Rapport sur les groupes d'unités 
d'organisation" dans le module "Rapports" ou grâce à l'outil tiers "tableau croisé dynamique" 
d'Excel. Par exemple, il est possible de visualiser et de comparer les taux d'utilisation 
agrégés selon les différents types de propriété (par exemple, le ministère de la santé, le secteur privé, 
les ONG). En outre, DHIS2 peut fournir des statistiques sur la répartition des 
établissements dans le "Rapport sur la répartition des unités d'organisation" du module "Rapports". 
Par exemple, il est possible de voir combien d'établissements existent sous une 
unité d'organisation donnée dans la hiérarchie pour chacun des différents 
types de propriété. Dans le module SIG, étant donné que les coordonnées des établissements de santé 
ont été enregistrées dans le système, il est possible de visualiser 
l'emplacement des différents types d'établissements de santé (avec des symboles différents 
pour chaque type) et de combiner ces informations avec une autre 
couche cartographique montrant les indicateurs, par ex. par district.

