---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/maintenance_use/metadata_mgmt_procedures.md"
revision_date: '2022-08-25'
tags:
- Implémentation
---

# Procédures de gestion des métadonnées { #procedures-for-managing-metadata }
Cette section traite des procédures et des recommandations relatives à la maintenance à long terme des métadonnées dans le cadre de l'implémentation du DHIS2. Elle décrit les défis procéduraux associés à la coordination des processus de configuration à long terme et fournit des exemples de procédures opérationnelles normalisées qui peuvent être adaptées et utilisées pour une meilleure coordination de ces processus.

Les problèmes de procédure pouvant entraîner des complications lors de la gestion des métadonnées sont entre autres

- Instances de développement indisponibles ou mal utilisées
- Lacunes dans les procédures opérationnelles normalisées (PON) pour ajouter des métadonnées ou modifier de la configuration
- Manque de coordination lors de l'ajout de nouvelles métadonnées
- Hypothèses incorrectes lors de l'ajout de packages de données numériques basés sur des normes reconnues ou celles de l'OMS
- Révisions des outils de collecte de données au fil du temps

## Instances de développement indisponibles ou mal utilisées { #development-instances-not-available-or-not-used-properly }

Lorsque vous travaillez sur votre configuration DHIS2, il est recommandé de disposer d'au moins une instance de développement. Si vous avez plus d'une instance de production, vous devriez envisager d'avoir une copie de chacune de ces instances à des fins de création de nouvelles métadonnées ou de modification de votre configuration (figure 1).

![développement_vs_production](resources/images/dev_vs_production.png) **Figure 1**

De nombreux problèmes liés aux métadonnées résultent du fait que les utilisateurs ajoutent des métadonnées directement dans un système de production. Ces métadonnées ne sont pas configurées comme il se doit ou ne sont pas utilisées par le système, ce qui entraîne des modifications qui devront être corrigées lorsqu'elles seront identifiées.

L'utilisation d'un système de développement permet d'éviter ces problèmes, car les éléments du système de développement peuvent être supprimés s'ils ne sont pas nécessaires, et ce, sans aucune incidence sur la configuration ou les données du système de production.

## Procédures opérationnelles normalisées pour l'ajout de métadonnées ou la modification de la configuration { #standard-operating-procedures-for-adding-metadata-or-modifying-the-configuration }

Les PON permettant d'ajouter des métadonnées doivent être disponibles pour toutes les implémentations de DHIS2. Vous pouvez consulter des exemples de procédures opérationnelles normalisées pour l'ajout de [métadonnées agrégées](https://docs.google.com/document/d/1VXnF5KPfiD45h6wH04kUNShQVno--TmckMHMyLqZm5I/edit?usp=sharing) et d'[utilisateurs](https://docs .google.com/document/d/1pqEQVV5JR7tyo8Zd09vDi3RVQ9E9R782OYNl-w9-5zQ/edit?usp=sharing) respectivement.

Lors de l'implémentation des procédures opérationnelles normalisées, il convient de proposer une formation sur chaque procédure spécifique et de continuer à évaluer son implémentation jusqu'à ce que la procédure définie devienne une norme. Ces procédures vont souvent au-delà de la personnalisation/modification des métadonnées et exigent que ceux qui font des ajouts ou modifient la configuration examinent attentivement la manière dont les éléments sont ajoutés et l'effet l'effet qui en résulte sur la facilité de fonctionnement du système dans son ensemble.

## Manque de coordination lors de l'ajout de nouvelles métadonnées { #lack-of-coordination-when-adding-new-metadata }

Au-delà des procédures spécifiques applicables à l'ajout de métadonnées ou à la modification de la configuration, ces actions doivent être menées de manière coordonnée. Cette coordination peut être simple, comme des discussions en interne entre les membres de l'équipe, ou plus complexe, comme un comité qui a une vue d'ensemble sur tous les projets planifiés et qui peut programmer des modifications en conséquence ; et elle dépendra du contexte d'implémentation.

Le manque de coordination peut souvent entraîner la création de doublons pour les métadonnées. Par exemple, si deux administrateurs ajoutent le même nouveau formulaire d'agrégation dans un système sans se tenir mutuellement informés, il est probable que certains éléments de métadonnées soient dupliqués dans le système.

Dans ce genre de situation, disposer d'un mécanisme de coordination qui informe les personnes chargées de configurer le système DHIS 2 de ce qui se passe, peut faire gagner du temps et de l'énergie par la suite, car la suppression de ces doublons peut s'avérer un processus long et fastidieux.

## Hypothèses incorrectes lors de l'ajout de packages de données numériques { #incorrect-assumptions-when-adding-digital-data-packages }

Les [paquages de l'OMS] (https://dhis2.org/who/) ou autres configurations basées sur des normes qui sont importées dans un système peuvent entraîner l'ajout d'une quantité importante de métadonnées dupliquées. Par exemple, les packages utilisent uniquement des indicateurs dans leur tableau de bord. Ces indicateurs peuvent être des doublons d'éléments de données existants. De plus, si les éléments d'un système existant contenant des métadonnées ne sont pas harmonisés avant l'importation d'un package basé sur des normes, cela peut entraîner la création d'éléments en double (tels que des options de catégorie, des ensembles d'options, etc.)

En règle générale, lors de l'importation d'un package basé sur des normes, essayez de réutiliser autant de métadonnées existantes que possible. Il vous faudra probablement modifier le fichier JSON du package avant de l'importer afin que les identifiants du fichier d'importation correspondent aux identifiants qui existaient déjà dans le système vers lequel vous effectuez l'importation.

Pour les tableaux de bord, les indicateurs dupliqués peuvent ne pas poser de problème, surtout s'ils sont correctement regroupés. Cela doit être jugé au cas par cas afin de déterminer leur impact sur le système avant d'importer le package.

**Remarque : L'importation de packages doit toujours être effectuée en premier lieu dans un système de développement. Ce n'est que lorsque tous les problèmes ont été résolus qu'ils peuvent être importés dans un système de production **

## Révisions des outils de collecte de données au fil du temps { #revisions-of-data-collection-tools-over-time }

Lorsque les outils de collecte de données sont mis à jour au fil du temps, des mesures peuvent être prises en faveur d'une réutilisation de certains objets plutôt que d'en créer des doublons.

### Programmes { #programs }

Dans la mesure du possible, n'hésitez pas à réutiliser des métadonnées entre différents programmes d'événements et de tracker. Ces métadonnées sont toujours associées au programme spécifique en cours de création et maintiendront la séparation requise au sein du système.

### Ensembles de données { #data-sets }

Concernant les ensembles de données agrégées, la réutilisation de métadonnées peut s'avérer moins évidente. Un problème est souvent rencontré lorsque les désagrégations sont modifiées d'un formulaire à l'autre. Considérons l'exemple présenté à la figure 2.

![aggregate_form_comparison.png](resources/images/aggregate_form_comparison.png)
**Figure 2**

Ce formulaire révèle que les désagrégations de chaque élément de données ont été modifiées. Plutôt que de créer de nouveaux éléments de données auxquels seront appliquées ces nouvelles désagrégations, vous pouvez utiliser une fonction appelée "Category combination override" (écraser une combinaison de catégories). Cette fonction permet d'associer un élément de données à plusieurs combinaisons de catégories sur la durée.

Pour écraser la combinaison de catégories, ouvrez votre ensemble de données à partir de l'application de maintenance. À l'endroit où vous ajoutez vos éléments de données, vous verrez une petite icône de clé à molette. Lorsque vous la survolez, le message suivant apparaît : "Ecraser la combinaison de catégories de l'élément de données" (figure 3).

![catcombo_override](resources/images/catcombo_override.png)
**Figure 3**

De là, vous ouvrirez un menu qui répertorie vos éléments de données sur le côté gauche et vous permet d'écraser les combinaisons de catégories sur le côté droit (Figure 4)

![écraser_une sélection_de combinaison de catégories](resources/images/catcombo_override_selection.png)

**Figure 4**

Sélectionnez simplement la combinaison de catégories pour l'élément de données que vous souhaitez écraser à l'aide de ce menu.

**Remarque : Il vous faudra peut-être créer de nouvelles options de catégorie, catégories et combinaisons de catégories. Si vous avez à le faire, veuillez consulter l'exemple [procédure d'agrégation des métadonnées].(https://docs.google.com/document/d/1VXnF5KPfiD45h6wH04kUNShQVno--TmckMHMyLqZm5I/edit?usp=sharing)**

Cette fonction présente un avantage particulier : elle vous permet d'examiner les données contenues dans ces éléments de données réutilisés sur de plus longues durées. Toutes les données saisies dans ces éléments de données à l'aide de l'ancien formulaire peuvent encore être examinées et comparées avec les périodes au cours desquelles le nouveau formulaire (et les nouvelles désagrégations) sont utilisés.

### Taux de déclaration agrégés { #aggregate-reporting-rates } 

Lorsque vous créez un nouvel ensemble de données destiné à remplacer un ensemble de données existant, vous devez penser à rationaliser vos taux de déclaration si nécessaire, étant donné que le nouvel ensemble de données que vous créez n'est associé par défaut à aucun des taux de déclaration existants. Si vous souhaitez conserver les taux de déclaration dans un même emplacement, vous pouvez les exporter/importer de l'ancien ensemble de données vers le nouveau. Il est recommandé de tester ce processus dans une instance de développement avant de l'exécuter avec votre système de production. _Prenez toujours soin de sauvegarder vos données avant de procéder à des importations_.

Afin de récupérer les taux de déclaration existants, vous pouvez interagir avec la ressource /completeDataSetRegistrations (terminer l'enregistrement de l'ensemble de données) et utiliser la requête suivante

```
api/completeDataSetRegistrations?dataSet=XA8e9AVn8Vo&startDate=2000-01-01&endDate=2017-07-01&orgUnit=mPlB2jqKNP0&children=true
```

**NB :** Vous devez remplacer l'ID de l'ensemble de données qui se trouve dans cet exemple par l'ID de l'ensemble de données de votre propre système, les dates par les dates dont vous avez besoin et les ID d'unités d'organisations par vos propres ID. Dans cet exemple, nous sélectionnons les taux de déclaration de toutes les unités d'organisation d'enfants ; vous remplacerez donc l'ID de l'unité d'organisation par l'ID de parent.

Un résultat sera renvoyé, composé des paramètres suivants pour chaque période pris en compte dans votre requête.

```
{completeDataSetRegistrations : [{"period":"201408","dataSet":"XvcWsuHBsGA","organisationUnit":"ZUwksatWvE8","attributeOptionCombo":"HllvX50cXC0","date":"2014-09-15"," stockéPar":"automatique"}]}
```

Une fois que vous avez récupéré les taux de déclaration, vous pouvez les intégrer au nouvel ensemble de données à l'aide d'une requête POST adressée au point de terminaison suivant

```
api/completeDataSetRegistrations
```

**NB :** Vous devez remplacer les ID des ensemble de données renvoyés dans la requête initiale par l'ID du nouvel ensemble de données vers lequel vous importez ces taux de déclaration. Faites-le avant de publier les informations dans la ressource completeDataSetRegistrations.

### Relier les données historiques à l'aide d'indicateurs { #linking-historical-data-using-indicators }

Lorsque vous créez de nouveaux éléments de données pour représenter un concept qui était déjà partiellement représenté, il peut être judicieux de créer des indicateurs qui relient ces éléments de données. Les données peuvent ainsi être visualisées dans le sens longitudinale au fil du temps (c'est-à-dire que vous pouvez visualiser les données des nouveaux et des anciens formulaires dans une même variable lorsque vous créez une sortie). Ce principe repose sur l'hypothèse selon laquelle les données des anciens et des nouveaux éléments de données ne se chevauchent pas (c'est-à-dire qu'elles ne sont pas collectées au cours de la même période, ce qui donnerait à l'indicateur une valeur incorrecte/dupliquée).

Pour ce faire, créez un nouvel indicateur et ajoutez le(s) élément(s) de données ancien(s) au(x) nouvel(aux) élément(s) de données. Cela vous permettra de créer diverses sorties, avec dans une même sortie les données historiques et les données actuelles représentées par la même variable. Si vous ne le faites pas, il vous faudra sélectionner les 2 (ou plus) éléments de données différents qui représentent désormais ce concept lors de l'analyse. Cela semblerait également désordonné car ils seraient représentés par des lignes différentes dans un graphique, des lignes ou des colonnes différentes dans un tableau, etc., avec des données affichées uniquement pour les variables pendant la période de collecte.

