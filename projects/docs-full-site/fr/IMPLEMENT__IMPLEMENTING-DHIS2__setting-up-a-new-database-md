---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/implementation/setting-up-a-new-database.md"
revision_date: '2021-09-15'
tags:
- Implémenter
---

# Installation d'une nouvelle base de données { #setting-up-a-new-database }

L'application DHIS2 dispose d'un ensemble d'outils utilisé pour la collecte, la validation, les rapports et l'analyse des données. Cependant, le contenu de la base de données, par exemple les données à collecter, leur provenance et leur format, dépendra du contexte d'utilisation. Pour pouvoir être utilisées, ces métadonnées doivent d'abord être introduites dans l'application. Cela ne nécessite aucune programmation et peut être fait via l'interface utilisateur. Pour cela, il faut avoir une connaissance approfondie du contexte du système d'information sanitaire local, ainsi qu'une compréhension des principes de conception du système DHIS2 (voir chapitre « Principes de conception clé du système DHIS2 »). Nous appelons ce processus initial la conception ou la personnalisation de la base de données. Ce chapitre fournit un aperçu du processus de personnalisation et explique brièvement la marche à suivre, afin de donner à l'implémenteur une idée de ce que ce processus exige. Les autres chapitres de ce manuel vont aborder plus en profondeur certaines étapes spécifiques.

## Stratégies de mise en route { #strategies-for-getting-started } 

La section suivante présente une liste de conseils pour bien commencer le développement d'une nouvelle base de données.

1.  Alimenter rapidement une base de données de démonstration avec des exemples de rapports, de graphiques,
    tableau de bord, SIG, formulaires de saisie de données. Utiliser des données réelles, idéalement
    des données à l’échelle nationale, mais pas nécessairement au niveau des établissements.

2.  Mettre la base de données de démonstration en ligne. L'hébergement du serveur peut être assuré par un opérateur externe,
    ce qui peut accélérer le processus, même si c'est temporaire.
    Cela constitue une plateforme collaborative et
    un outil de diffusion efficaces pour obtenir l’adhésion des parties prenantes.

3.  L'étape suivante est un processus de conception de base de données plus élaboré.
    Certaines parties de la démo peuvent être réutilisées si nécessaire.

4.  Disposer d'une équipe locale avec une variété de compétences et de parcours :
    santé publique, administration de données, informatique et gestion de projet.

5.  Aborder la phase de personnalisation et de conception de la base de données comme un processus d'apprentissage et
    de formation qui vise le renforcement des capacités locales grâce à l’apprentissage par la pratique.

6.  L'équipe du pays doit diriger le processus de conception de la base de données
    mais avec l'assistance d'implémenteurs expérimentés.

## Processus ouvert ou contrôlé? { #controlled-or-open-process } 

Étant donné que le processus de personnalisation de DHIS2 est souvent et doit être un processus collaboratif, il est également important de savoir quelles parties de la base de données sont plus critiques que d'autres, par exemple pour éviter qu'un utilisateur non formé ne corrompe les données. En règle générale, il est beaucoup plus important de personnaliser une base de données qui contient déjà des valeurs de données que de travailler avec des métadonnées sur une base de données "vide". Bien que cela puisse paraître étrange, une bonne partie de la personnalisation a lieu après le début de la collecte ou de l'importation des données, par exemple lors de l'ajout de nouvelles règles de validation, d'indicateurs ou de modèles de rapports. L'erreur la plus grave serait de modifier les métadonnées qui décrivent directement les valeurs des données, à savoir, les *éléments de données* et les *unités d'organisation*, comme nous l'avons vu plus haut. En modifiant ces définitions, il est important de réfléchir à la manière dont cette modification affectera les valeurs de données déjà présentes dans le système (collectées à l'aide des anciennes définitions). Il est recommandé de limiter l'accès à la modification de ces métadonnées fondamentales par le biais des rôles des utilisateurs, afin que l'accès soit réservé à une équipe de personnalisation restreinte.

La manipulation des autres parties du système qui ne sont pas directement liées aux valeurs de données est moins problématique. De plus, ici, du moins dans les premières phases, on devrait encourager les utilisateurs à essayer de nouvelles approches, afin d'améliorer leur apprentissage du système. Cela vaut pour les groupes, les règles de validation, les formules d'indicateurs, les graphiques et les rapports. Tous ces éléments peuvent facilement être supprimés ou modifiés ultérieurement sans affecter les valeurs de données concernées, et ne sont donc pas des éléments essentiels lors du processus de personnalisation de la base de données.

Bien sûr, plus tard dans le processus de personnalisation, notamment lors de la phase de production, il faudra être plus vigilant quant à l'attribution des droits d'accès pour la modification des métadonnées, étant donné que tout changement, même sur les métadonnées les moins critiques, pourrait affecter la façon dont les données sont agrégées ou présentées dans un rapport (bien que les données brutes concernées soient toujours sécurisées et correctes).

## Étapes à suivre pour l'élaboration d'une base de données { #steps-for-developing-a-database } 

La section suivante décrit concrètement les étapes à suivre pour concevoir une base de données de A à Z.

### La hiérarchie organisationnelle { #the-organisational-hierarchy } 

La hiérarchie organisationnelle définit l'organisation qui utilise le DHIS2, les établissements de santé, les zones administratives et les autres zones géographiques qui entre en jeu dans la collecte et l'analyse des données. Cette dimension des données est définie comme une hiérarchie avec une unité racine (par exemple, le ministère de la santé) et plusieurs niveaux et nœuds inférieurs. Chaque nœud de cette hiérarchie est appelé unité d'organisation dans le DHIS2. La conception de cette hiérarchie déterminera les unités géographiques d'analyse disponibles pour les utilisateurs, car les données sont collectées et agrégées selon cette structure. Il ne peut y avoir qu'une seule hiérarchie organisationnelle à la fois, c'est pourquoi sa structure doit être bien pensée.

Des hiérarchies supplémentaires (par exemple, des frontières administratives parallèles au secteur des soins de santé) peuvent être modélisées à l'aide de groupes d'organisations et d'ensembles de groupes, mais la hiérarchie organisationnelle est le principal moyen d'agrégation des données sur la dimension géographique. En règle générale, les hiérarchies organisationnelles nationales dans le domaine de la santé publique comportent 4 à 6 niveaux, mais le nombre de niveaux reste flexible. La hiérarchie est constituée de relations mère-fille, c'est-à-dire qu'un pays ou une unité du ministère de la santé (la racine) peut avoir, par exemple, 8 unités filles (provinces), et chaque province (au niveau 2) peut avoir 10 à 15 districts comme unités filles. Normalement, les établissements de santé sont situés au niveau le plus bas, mais ils peuvent également être situés à des niveaux plus élevés, par exemple des hôpitaux nationaux ou provinciaux, de sorte que des structures organisationnelles asymétriques sont possibles (par exemple, un nœud feuille peut être positionné au niveau 2 alors que la plupart des autres nœuds feuilles se trouvent au niveau 5).

### Éléments de donnée { #data-elements } 

L'élément de donnée est peut-être la composante la plus importante d'une base de données DHIS2. Il représente la dimension *quoi* et explique donc ce qui est collecté ou analysé. Dans certains contextes, il s'agit d'un indicateur, mais dans DHIS2, nous appelons cette unité de collecte et d'analyse un _élément de donnée_. L'élément de donnée représente souvent le décompte de quelque chose, et son nom décrit ce qui est compté, ex. "Doses de BCG administrées" ou "Cas de Paludisme". Lorsque les données sont collectées, validées, analysées, rapportées ou présentées, ce sont les éléments de données ou expressions fondées sur ces éléments de données qui décrivent le QUOI de ces données. De cette manière, les éléments de données deviennent importants pour tous les aspects du système et décident non seulement de la manière dont les données sont collectées, mais aussi et surtout la manière dont les valeurs de données sont représentées dans la base de données, ce qui conditionne la manière dont les données peuvent être analysées et présentées.

Lors de la conception des éléments de données, il convient de considérer les éléments de données comme des unités d'analyse des données et pas seulement comme des champs du formulaire de collecte des données. Chaque élément de données est autonome dans la base de données, complètement détaché du formulaire de collecte. Les rapports et autres résultats sont basés sur les éléments de données et les expressions/formules composées d'éléments de données et non sur les formulaires de collecte de données. Par conséquent, ce sont les besoins en matière d'analyse des données qui doivent conditionner le processus, et non l'apparence des formulaires de collecte de données.

### Ensemble de données et formulaires de saisie de données { #data-sets-and-data-entry-forms } 

Toute la saisie de données dans DHIS2 est organisée à l'aide d'ensembles de données. Un 
ensemble de données est une collection d'éléments de données regroupés pour la collecte 
de données. Dans le cas d'installations distribuées, ils définissent également 
des blocs de données destinés à l'exportation et à l'importation entre des instances de DHIS2 (ex. 
d'une installation locale d'un bureau d'arrondissement vers un serveur national). Les ensembles 
de données ne sont pas directement liés aux valeurs de données, mais uniquement par le biais de leurs 
éléments de données et de leurs fréquences. De ce fait, un ensemble de données peut être modifié, 
supprimé ou ajouté à tout moment sans affecter les données brutes 
déjà stockées dans le système, même si ces modifications vont sans doute affecter 
la façon dont les nouvelles données seront collectées.

Une fois que vous avez assigné un ensemble de données à une unité organisationnelle, cet ensemble de données sera disponible dans Data Entry (Saisie des données) (sous Services) pour les unités organisationnelles où vous l'avez assigné et pour les périodes valides selon le type de période de l'ensemble de données. Un formulaire de saisie de données par défaut s'affichera alors. Il s'agit simplement d'une liste des éléments de données appartenant à l'ensemble de données qui inclut une colonne pour la saisie des valeurs. Si votre ensemble de données contient des éléments de données avec des catégories telles que les tranches d'âge ou le sexe, de nouvelles colonnes seront automatiquement générées dans le formulaire par défaut en fonction des catégories. En plus du formulaire de saisie de données par défaut basé sur une liste, on a également le formulaire basé sur des sections et le formulaire personnalisé. Les formulaires à section offrent un peu plus de flexibilité lorsqu'il s'agit de présenter les données sous forme de tableau. Ils sont rapides et simples à concevoir. Souvent, votre formulaire de saisie de données aura besoin de plusieurs tableaux avec des sous-titres, et parfois, vous devez désactiver (griser) quelques champs du tableau (par exemple, lorsque certaines catégories ne s'appliquent pas à tous les éléments de données), ces deux fonctions sont prises en charge dans les formulaires à section. Si le formulaire que vous souhaitez concevoir est trop compliqué pour les formulaires par défaut ou les formulaires à section, vous pouvez utiliser un formulaire personnalisé. Cela prend plus de temps, mais vous disposez d'une totale liberté de conception. Le système DHIS2 intègre un éditeur HTML (FcK Editor) destiné au concepteur de formulaire. Vous pouvez soit concevoir le formulaire dans l'interface utilisateur, soit coller votre html directement (en utilisant la fenêtre Source dans l'éditeur).

### Règles de validation { #validation-rules } 

Une fois que vous avez configuré la partie du système relative à la saisie de données et commencé à collecter des données, il est donc temps de définir des règles de contrôle de la qualité des données permettant d'améliorer la qualité des données collectées. Vous pouvez alors ajouter autant de règles de validation que vous voulez. Celles-ci sont composées d'expressions de gauche et de droite qui, elles aussi, sont composées d'éléments de données, avec un opérateur entre les deux côtés. Les règles typiques consistent à comparer les totaux partiels aux totaux de quelque chose. Si vous avez par exemple deux éléments de données "Tests de dépistage du VIH" et "Résultat positif du test de dépistage", vous savez alors que dans le même formulaire (pour la même période et la même unité d'organisation), le nombre total de tests doit toujours être supérieur ou égal au nombre de tests positifs. Ces règles doivent être des règles absolues, ce qui signifie qu'elles sont mathématiquement correctes et non pas simplement des hypothèses ou sont "la plupart du temps correctes". Les règles peuvent être exécutées lors de la saisie de données, après le remplissage de chaque formulaire, ou dans un processus plus complexe dans plusieurs formulaires à la fois. Exemple : pour toutes les structures sanitaires du mois précédent, les résultats des tests listeront toutes les violations et les valeurs détaillées pour chaque côté de l'expression où la violation s'est produite pour faciliter le retour à la saisie des données et corriger les valeurs.

### Indicateurs { #indicators } 

Les indicateurs représentent peut-être la plus puissante fonctionnalité d'analyse de données de DHIS2. Alors que les éléments de données représentent les données brutes (comptes) collectées, les indicateurs représentent des formules fournissant des taux de couverture, des taux d'incidence, des ratios et d'autres unités d'analyse basées sur une formule. Un indicateur est composé d'un facteur (Exemple : 1,100, 100, 100 000), d'un numérateur et d'un dénominateur. Les deux derniers sont tous deux des expressions basées sur un ou plusieurs éléments de données. Exemple : l'indicateur "Couverture du BCG \<1 an" est défini par une formule avec un facteur 100, un numérateur ("Les doses BCG administrées aux enfants de moins de 1") et un dénominateur ("Population cible de moins de 1 an"). L'indicateur "Taux d'abandon de DPT1 à DPT3" est une formule de 100% x ("Doses de DPT1 administrées" - "Doses de DPT3 administrées") / ("Doses de DPT1 administrées").

La plupart des modules de rapport dans DHIS2 prennent en charge les éléments de données et les indicateurs et vous pouvez également les combiner dans des rapports personnalisés, mais la différence et la puissance des indicateurs par rapport aux données brutes (valeurs de données de l'élément de donnée) réside dans la possibilité de comparer des données entre différentes zones géographiques (par exemple les zones très peuplées ou rurales), la population cible pouvant être utilisée comme dénominateur.

Les indicateurs peuvent être ajoutés, modifiés et supprimés à tout moment sans interférer avec les valeurs de données contenues dans la base de données.

### Tableaux et rapports { #report-tables-and-reports } 

Les rapports standards dans DHIS2 constituent un moyen très flexible de présenter les données collectées. Les données peuvent être agrégées par n'importe quel niveau ou unité d'organisation, par élément de donnée, par indicateur, ainsi que dans le temps (mensuellement, trimestriellement, annuellement). Les tableaux de rapports représentent des sources de données personnalisées pour les rapports standards. Ils peuvent être définis de manière flexible dans l'interface utilisateur, puis accessibles via des concepteurs de rapports externes tels que iReport ou via des rapports HTML personnalisés. Ces conceptions de rapport peuvent ensuite être configurées comme des rapports facilement accessibles en un clic avec des paramètres afin que les utilisateurs puissent exécuter les mêmes rapports comme par exemple, tous les mois, lorsque de nouvelles données sont saisies. Elles peuvent également répondre aux besoins des utilisateurs à tous les niveaux, puisque l'unité d'organisation peut être sélectionnée au moment de l'exécution du rapport.

### SIG (Cartes) { #gis-maps } 

Dans le module SIG intégré, vous pouvez facilement afficher vos données sur des cartes, à la fois sur des polygones (zones) et sous forme de points (structures sanitaires), et soit en tant qu'éléments de données ou en tant qu'indicateurs. En fournissant les coordonnées de vos unités d'organisation au système, vous pouvez rapidement vous adapter à ce module. Consultez la section SIG pour plus de détails sur la façon de vous y prendre.

### Diagrammes et tableau de bord { #charts-and-dashboard } 

L'un des moyens les plus faciles d'afficher les données de votre indicateur est d'utiliser des graphiques. Un dialogue de diagramme facile à utiliser vous guidera dans la création de divers types de graphiques avec des données sur les indicateurs, les unités d'organisation et les périodes de votre choix. Ces graphiques peuvent facilement être ajoutés à l'une des quatre sections de votre tableau de bord et sont facilement disponibles immédiatement après votre connexion. Assurez-vous de définir le module du tableau de bord comme module de démarrage dans les paramètres utilisateur.

