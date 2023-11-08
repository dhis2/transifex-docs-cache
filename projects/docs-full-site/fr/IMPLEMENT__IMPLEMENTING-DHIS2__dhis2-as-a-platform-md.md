---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/implementation/dhis2-as-a-platform.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# DHIS2 en tant que plateforme { #dhis2-as-a-platform } 

Le DHIS2 peut être perçu comme une plate-forme à plusieurs niveaux. Tout d'abord, la
base de données de l'application est conçue de manière à être flexible. 
Les structures de données telles que les éléments de données, les unités d'organisation, les formulaires et
les rôles des utilisateurs peuvent être définis en toute liberté par l'interface utilisateur
de l'application. Cela permet d'adapter le système à une
multitude de contextes locaux et de cas d'utilisation. Nous avons vu que le DHIS2
prend en charge la plupart des principales exigences de saisie et d'analyse de données de routine
qui apparaissent dans les mises en œuvre nationales. Il permet également à DHIS2
de servir de système de gestion pour des domaines tels que la logistique, les laboratoires et
les finances.

Deuxièmement, grâce à sa conception modulaire, le système DHIS2 peut être étendu par
des modules logiciels supplémentaires. Ces modules des logicielles peuvent cohabiter avec
les modules de base du système DHIS2 et peuvent être intégrés dans le portail et le
système de menu du système DHIS2. Il s'agit d'une fonction puissante car elle permet
d'étendre le système avec des fonctionnalités supplémentaires si nécessaire, 
généralement pour des besoins spécifiques à un pays, comme indiqué précédemment.

L'inconvénient de l'extensibilité du module logiciel est qu'elle impose
plusieurs contraintes au processus de développement. Les développeurs qui créent
les fonctionnalités supplémentaires sont limités à la technologie DHIS2 en termes de
langage de programmation et de cadres logiciels, en plus des
contraintes imposées à la conception des modules par la solution de portail DHIS2.
En outre, ces modules doivent être inclus dans le logiciel DHIS2 lorsque le
logiciel est construit et déployé sur le serveur web, et non de manière dynamique pendant
l'exécution.

Afin de surmonter ces limitations et de parvenir à un couplage plus souple
entre la couche de service DHIS2 et les artefacts logiciels supplémentaires, 
l'équipe de développement du DHIS2 a décidé de créer une API Web. Cette API Web
est conforme aux règles du style architectural REST. Cela implique
que :

  - L'API Web fournit une interface navigable et lisible par machine pour 
    le modèle de données complet du DHIS2. Par exemple, on peut accéder à la liste complète 
    des éléments de données, puis naviguer à l'aide de l'hyperlien fourni vers
    un élément de données particulier qui nous intéresse, puis naviguer à l'aide de
    l'hyperlien fourni vers la liste des formulaires dont cet élément de données fait 
    Par exemple, les clients n'effectueront des transitions d'état qu'en utilisant les
    hyperliens qui sont intégrés dynamiquement dans les réponses.

  - L'accès aux données s'effectue par le biais d'une interface uniforme (URL) utilisant un
    protocole bien connu. Il n'y a pas de formats ou de protocoles de transport fantaisistes,
    mais simplement le protocole HTTP, qui a été testé et qui est bien compris,
    et qui est le principal élément constitutif du Web aujourd'hui. Cela 
    signifie que les développeurs tiers peuvent mettre au point des logiciels utilisant le
    modèle de données et les données DHIS2 sans connaître la technologie spécifique de DHIS2
    ou se conformer aux contraintes de conception de DHIS2.

  - Toutes les données, y compris les métadonnées, les rapports, les cartes et les graphiques, appelés 
    ressources dans la terminologie REST, peuvent être récupérées dans la plupart des
    formats de représentation populaires du web d'aujourd'hui, tels que HTML,
    XML, JSON, PDF et PNG. Ces formats sont largement pris en charge par
    les applications et les langages de programmation et offrent aux développeurs tiers
    un vaste champ d'options de mise en œuvre.

![](resources/images/dhis_platform.png)

Il existe plusieurs scénarios dans lesquels des artefacts logiciels supplémentaires peuvent 
se connecter à l'API Web DHIS2.

## Portails Web { #web-portals } 

Tout d'abord, les portails Web peuvent être construits au-dessus de l'API Web. Un portail Web, à 
cet effet, est un site Web qui fonctionne comme un point d'accès 
aux informations provenant d'un grand nombre potentiel de sources de données qui
partagent généralement un thème commun. Le rôle du portail web est de rendre
ces sources de données facilement accessibles de manière structurées sous une 
apparence commune et de fournir une vue d'ensemble des données aux
utilisateurs finaux.

Référentiel de données agrégées : Un portail web destiné au domaine de la santé
peut utiliser le DHIS2 comme source principale de données agrégées. Le portail peut
se connecter à l'API Web et communiquer avec des ressources importantes telles que
les cartes, les graphiques, les rapports, les tableaux et documents statiques. Ces vues de données peuvent
afficher dynamiquement des données agrégées basées sur des requêtes sur la
dimension unité d'organisation, indicateur ou période. Le portail peut apporter une 
valeur ajoutée à l'accessibilité de l'information de plusieurs façons. Il peut être
structuré de manière conviviale et rendre les données accessibles aux
utilisateurs inexpérimentés. Il peut fournir différentes approches relatives aux données,
notamment :

  - Thématique - regroupement d'indicateurs par thème. Des exemples de ces thèmes sont 
    la vaccination, les soins maternels, les maladies à déclaration obligatoire et la
    santé environnementale.

  - Géographique - regroupement des données par province. Cela permettra de comparer facilement
    les performances et la charge de travail.

Application composite : Le portail Web n'est pas limité à la consommation de données provenant d'une seule
API Web.- Il peut être connecté à un nombre illimité d'API et être utilisé pour fusionner 
des données provenant de systèmes auxiliaires dans le domaine de la santé. S'il est disponible
le portail peut intégrer des données spécialisées provenant de systèmes logistiques
de suivi et de gestion des médicaments ARV, de systèmes financiers gérant 
les paiements aux établissements de santé et des systèmes de laboratoire qui suivent les tests de laboratoire 
pour les maladies transmissibles. Les données provenant de toutes ces sources pourraient être
présentées de manière cohérente et significative afin de fournir un meilleur aperçu de
la situation du domaine de la santé.

Dépôt de documents : Le portail web peut faire office de référentiel documentaire en 
lui-même (également appelé système de gestion de contenu). 
Les documents pertinents tels que les rapports publiés, les données d'enquête, les plans
opérationnels annuels et les FAQ peuvent être téléchargés et gérés en termes de propriété, 
de contrôle des versions et de classification. Le portail devient ainsi un point central
pour le partage de documents et la collaboration. L'émergence de
solutions  de dépôt et de CMS de haute qualité et à code source ouvert, telles que Alfresco et 
Drupal rend cette approche plus réalisable et plus convaincante.

Gestion des connaissances : La gestion des connaissances fait référence aux pratiques permettant d'identifier,
de matérialiser et de partager les connaissances et l'expérience. Dans notre contexte, elle
concerne tous les aspects de la mise en œuvre et de l'utilisation des systèmes d'information,
tels que :

  - la conception de la base de données

  - l'utilisation du système d'information et guides méthodologiques

  - les directives pour la conduite de formations destinées aux utilisateurs finaux

  - l'utilisation des données, leur analyse et interprétation

Les connaissances et l'apprentissage dans ces domaines peuvent être matérialisés sous
forme de manuels, d'articles, de livres, de jeux de diapositives, de vidéos, de textes d'aide intégrés au système, 
de sites d'apprentissage en ligne, de forums, de FAQ, etc. Tous ces
artefacts peuvent être publiés et rendus accessibles à partir du portail web.

Forum : Le portail peut fournir un forum pour accueillir des discussions entre
utilisateurs professionnels. Le sujet peut aller de l'aide à l'exécution d'opérations 
de base dans le système d'information de santé à des discussions sur
l'analyse et l'interprétation des données. Un tel forum peut servir de
source d'information interactive et évoluer naturellement vers des 
archives précieuses.

## Applications { #apps } 

Deuxièmement, les clients logiciels tiers fonctionnant sur des appareils tels que les téléphones
mobiles, les smartphones et les tablettes peuvent se connecter à l'API Web DHIS2 et
lire et écrire dans les ressources pertinentes. Par exemple, les développeurs tiers peuvent créer un client fonctionnant sur le système d'exploitation Android
sur des appareils mobiles destinés aux agents de santé communautaires qui ont besoin de garder
une trace des personnes à visiter, enregistrer les données vitales pour chaque rencontre et
recevoir des rappels des dates d'échéance pour les soins aux patients tout en se déplaçant librement
dans la communauté. Une telle application client pourrait interagir avec
les ressources de patients et de plans d'activité exposées par l'API Web du DHIS2. Le
développeur n'aura pas besoin d'une connaissance approfondie de l'implémentation 
interne du DHIS2, mais plutôt des compétences de base en programmation HTTP/Web et
quelques connaissances du modèle de données DHIS2. La compréhension du modèle de données DHIS2
est facilitée par la nature navigable de l'API Web.

## Systèmes d'information { #information-systems } 

Troisièmement, les développeurs de systèmes d'information visant à créer de nouvelles façons 
d'afficher et de présenter des données agrégées peuvent utiliser l'API Web du DHIS2.
comme couche de service de leur système. L'effort nécessaire pour développer de
nouveaux systèmes d'information et les maintenir dans le temps est souvent grandement
sous-estimés. Au lieu de partir de zéro, une nouvelle application peut
être construite au-dessus de l'API Web. L'attention des développeurs peut être orientée
vers la création de nouvelles représentations et visualisations de données, innovantes et créatives, 
sous la forme, par exemple, de tableaux de bord, de SIG et de composants 
graphiques.

