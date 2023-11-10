---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/implementation/dhis2-as-data-warehouse.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# DHIS2 comme entrepôt de données { #dhis2-as-data-warehouse } 

Ce chapitre abordera le rôle et la place de l'application DHIS2 dans 
le contexte de l'architecture du système. Il montrera que DHIS2 peut servir 
à la fois d'entrepôt de données et de système opérationnel.

## Les entrepôts de données et les systèmes opérationnels { #data-warehouses-and-operational-systems } 

Un *entrepôt de données* est généralement considéré comme une base de données utilisée à 
des fins d'analyse. Les données sont généralement téléchargées à partir de divers systèmes opérationnels/
transactionnels. Avant d'être chargées dans l'entrepôt de données, les 
données passent généralement par différentes étapes au cours desquelles elles sont nettoyées pour détecter les anomalies 
et les redondances, et transformées pour se conformer à la structure globale de 
la base de données intégrée. Les données sont ensuite mises à disposition pour être utilisées dans 
le cadre d'une analyse, également connue sous des termes tels que*data mining* (extraction de données) et *online 
analytical processing* (traitement analytique en ligne). La conception de l'entrepôt de données est optimisée pour accélérer 
la recherche et l'analyse des données. Pour améliorer les performances, le stockage des données 
est souvent redondant, c'est-à-dire que les données sont stockées à la fois sous 
leur forme la plus granulaire et sous une forme agrégée (résumée).

Un *système transactionnel* (ou *système opérationnel* du point de vue de l'entrepôt 
de données) est un système qui collecte, stocke et modifie des données de bas niveau. 
Ce système est généralement utilisé au quotidien pour la saisie et la validation 
des données. La conception est optimisée pour des performances d'insertion et de mise 
à jour rapides.

![](ressources/images/données_entrepôt.png)

La gestion d'un entrepôt de données présente plusieurs avantages, dont les suivants:

  - *Cohérence:* elle fournit un modèle de données commun pour toutes les données pertinentes
    et agit comme une abstraction sur un nombre potentiellement élevé de sources de données
    et de systèmes d'alimentation, ce qui la rend beaucoup plus facile à exécuter
    l'analyse.

  - *Fiabilité:* Il est détaché des sources d'où proviennent les données
    et n'est donc pas affecté si les données des systèmes opérationnels
    sont purgées ou perdues.

  - *Performance d'analyse:* Il est conçu pour une performance maximale pour
    l'extraction et l'analyse des données, contrairement aux systèmes opérationnels qui
    sont souvent optimisés pour la saisie de données.

Cependant, l'approche axée sur l'entrepôt de données pose également des problèmes
importants : 

  - *Coût élevé:* Le transfert de données provenant de différentes sources
    vers un entrepôt de données commun est très coûteux, en particulier lorsque les 
    systèmes opérationnels ne sont pas de même nature. Souvent, les systèmes existants à long terme
    (appelés systèmes patrimoniaux) imposent de lourdes
    contraintes au processus de transformation des données.

  - *Validité des données:* Le processus de transfert des données dans l'entrepôt de données
    est souvent complexe et n'est donc pas exécuté à intervalles réguliers et en temps
    voulu. Ceci aboutira à ce que les utilisateurs de données disposent de données périmées et 
    non pertinentes, inadaptées à la planification et à la prise de décision
    éclairée.

En raison des défis mentionnés, il est devenu de plus en plus populaire 
de fusionner les fonctions de l'entrepôt de données et du système opérationnel, 
soit dans un système unique qui exécute les deux tâches, soit avec 
des systèmes étroitement intégrés hébergés ensemble. Avec cette approche, le 
système fournit des fonctionnalités pour la saisie et la validation des données ainsi que 
pour l'analyse des données et gère le processus de conversion des données atomiques 
de bas niveau en données agrégées adaptées à l'analyse. Cela impose des normes 
levées au système et à sa conception, car il doit fournir des performances 
appropriées pour ces deux fonctions ; cependant, les progrès réalisés dans le domaine du matériel et du traitement parallèle
rendent cette approche de plus en plus réalisable.

À cet égard, l'application DHIS2 est conçue pour servir d'outil à 
la fois pour la saisie, la validation, l'analyse et la présentation des données. Elle 
fournit des modules pour tous les aspects mentionnés, y compris la fonctionnalité de saisie 
des données et un large éventail d'outils d'analyse tels que les rapports, 
les graphiques, les cartes, les tableaux croisés dynamiques et les tableaux de bord.

Par ailleurs, DHIS2 fait partie d'une suite de systèmes d'information de santé interopérables
qui couvrent un large éventail de besoins et sont tous des 
logiciels libres. DHIS2 met en œuvre la norme d'échange de données et de 
métadonnées dans le domaine de la santé appelée SDMX-HD. Il existe de nombreux 
exemples de systèmes opérationnels qui mettent également en œuvre cette norme et 
qui peuvent potentiellement alimenter le DHIS2 en données :

  - iHRIS : Système de gestion des données relatives aux ressources humaines. Voici quelques exemples
    de données pertinentes pour un entrepôt de données national, saisies par 
    ce système : "nombre de médecins", "nombre d'infirmières" et "nombre total 
    de membres du personnel". Ces données sont intéressantes pour comparer, par exemple,
    les performances des districts.

  - OpenMRS : Système de dossiers médicaux utilisé à l'hôpital. Ce système
    peut potentiellement agréger et exporter des données sur les maladies des patients hospitalisés vers un
    entrepôt de données national.

  - OpenELIS : Système d'information d'entreprise de laboratoire. Ce système peut
    générer et exporter des données sur le nombre et les résultats des tests de laboratoire.

![](resources/images/dhis_data_warehouse.png)

## Stratégie d'agrégation dans DHIS2{ #aggregation-strategy-in-dhis2 } 

Les outils d'analyse du DHIS2 lisent des données agrégées à partir de tables *data mart*. 
Un data mart est un magasin de données optimisé pour répondre aux demandes les plus 
courantes des utilisateurs en matière d'analyse de données. La base de données DHIS2 
contient des données agrégées dans la* dimension spatiale* (la hiérarchie des unités 
d'organisation), la *dimension temporelle* (sur plusieurs périodes) et pour les *formules 
d'indicateurs* (expressions mathématiques comprenant des éléments de données). L'extraction 
de données directement à partir des datamarts offre de bonnes performances, même dans 
les environnements à forte concentration de données, car la plupart des demandes d'analyse peuvent être 
satisfaites par une simple et unique interrogation de la base de données à partir du datamart. Le 
moteur d'agrégation du DHIS2 est capable de traiter les données de bas niveau par 
millions et de gérer la plupart des bases de données nationales, et 
l'on peut dire qu'il fournit un *accès en temps quasi réel* aux données agrégées.

DHIS2 permet de définir des tâches d'agrégation programmées qui, en règle générale, 
actualisent et alimentent le datamart avec des données agrégées chaque 
nuit. Vous pouvez choisir d'agréger les données des 12 derniers mois 
chaque nuit ou d'agréger les données des 6 derniers mois chaque nuit et les 
données des 6 à 12 derniers mois chaque samedi. Les tâches planifiées peuvent être 
configurées sous "Planification" dans le module "Administration des données". Il est 
également possible d'exécuter des tâches arbitraires sous "Data mart" dans 
le module "Rapports".

## Approches pour le stockage de données { #data-storage-approach } 

Il existe deux approches principales pour le stockage des données dans un entrepôt 
de données, à savoir l'approche *normalisée* et l'approche *dimensionnelle*. Le DHIS2 s'inspire un peu 
de la première, mais surtout de la seconde. Dans l'approche dimensionnelle, 
les données sont divisées en *dimensions* et en *faits*. Les faits font généralement 
référence à des données numériques transactionnelles, tandis que les dimensions sont les données de référence 
qui donnent un contexte et une signification aux données. Les règles strictes de 
cette approche permettent aux utilisateurs de comprendre facilement la structure de l'entrepôt de 
données et offrent de bonnes performances étant donné que peu de tables doivent être 
combinées pour produire une analyse significative, alors qu'elles 
pourraient rendre le système moins flexible et plus difficile à modifier.

Dans DHIS2, les faits correspondent à l'objet valeur de données dans le modèle de 
données. La valeur des données saisit les données sous forme de nombres, de oui/non ou de texte. 
Les *dimensions obligatoires* qui donnent un sens aux faits sont les dimensions *élément 
de données*, *hiérarchie de l'unité d'organisation* et *période*. Ces 
dimensions sont qualifiées d'obligatoires car elles doivent être fournies pour 
tous les enregistrements de données stockées. Le DHIS2 dispose également d'un modèle dimensionnel personnalisé qui 
permet de représenter n'importe quel type de dimensionnalité. Ce modèle 
doit être défini avant la saisie des données. DHIS2 dispose également d'un modèle flexible 
de groupes et d'ensembles de groupes qui permet d'ajouter une dimensionnalité 
personnalisée aux dimensions obligatoires après la saisie des données. 
Pour en savoir plus sur la dimensionnalité dans le DHIS2, voir le chapitre 
du même nom.

![](resources/images/dimensional_approach.png)

