---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/data-sets-and-forms.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Ensembles de données et formulaires { #data-sets-and-forms } 

Ce chapitre traite des ensembles de données et des formulaires, des types de formulaires 
disponibles et décrit les bonnes pratiques à suivre lors du passage des 
formulaires papier aux formulaires électroniques. 

## Qu'est-ce qu'un ensemble de données? { #what-is-a-data-set } 

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

Un ensemble de données possède un type de période qui contrôle la fréquence de collecte 
des données; elle peut être quotidienne, hebdomadaire, mensuelle, trimestrielle, 
semestrielle ou annuelle. Les éléments de données à inclure dans l'ensemble de données 
et le type de période sont définis par l'utilisateur, ainsi qu'un nom, un prénom 
et un code. Si des champs calculés sont nécessaires dans le formulaire de collecte (et 
pas seulement dans les rapports), alors des indicateurs peuvent également être affectés à 
l'ensemble de données, mais ceux-ci ne peuvent être utilisés que dans les formulaires personnalisés (voir 
plus bas).

Pour utiliser un ensemble de données dans la collecte de données pour le compte d'une unité d'organisation 
spécifique, l'utilisateur doit affecter cette unité d'organisation à l'ensemble de données. Ce 
mécanisme détermine quelles unités d'organisation peuvent utiliser quels ensembles de données et 
définit simultanément les valeurs cibles pour la complétude des données ( ex.
combien d'établissements de santé dans un district sont censés soumettre l'ensemble de données RCH 
tous les mois?)

Un élément de donnée peut appartenir à plusieurs ensembles de données, mais cela nécessite 
une réflexion approfondie, car il peut entraîner un chevauchement et une inconstance des données 
collectées si les ensembles de données ont par exemple des fréquences différentes et sont 
utilisés par les mêmes unités d'organisation.

## Qu'est-ce qu'un formulaire de saisie de données ? { #what-is-a-data-entry-form } 

Une fois que vous avez affecté un ensemble de données à une unité d'organisation, cet ensemble de données 
sera disponible dans Saisie de données (sous Service) pour les 
unités d'organisation auxquelles vous l'avez affecté et pour les périodes valides, 
en fonction du type de période de l'ensemble des données. Un formulaire de saisie de données par défaut 
s'affichera. Il s'agit tout simplement d'une liste d'éléments de données appartenant à 
l'ensemble de données et comportant une colonne pour la saisie des valeurs. Si votre 
ensemble de données contient des éléments de données avec des catégories telles que des groupes d'âge ou 
de sexe, des colonnes supplémentaires seront automatiquement générées dans le 
formulaire par défaut en fonction des catégories. En plus du formulaire de saisie de données basé sur une 
liste par défaut, il existe deux alternatives supplémentaires : le 
formulaire par section et le formulaire personnalisé.

### Types de formulaires de saisie de données { #types-of-data-entry-forms } 

Le DHIS2 propose à ce jour trois types de formulaires différents, qui sont 
décrits ci-après.

#### Formulaires par défaut { #default-forms } 

Un formulaire de saisie par défaut est simplement une liste des éléments de données 
appartenant à l'ensemble de données ainsi qu'une colonne pour la saisie des 
valeurs. Si votre ensemble de données contient des éléments de données dont la 
combinaison de catégories n'est pas par défaut, comme les groupes d'âge ou de sexe, des colonnes supplémentaires 
seront automatiquement générées dans le formulaire par défaut sur la base des 
différentes options/dimensions. Si vous utilisez plus d'une combinaison de catégories 
dans un ensemble de données, vous obtiendrez un tableau par combinaison de catégories 
dans le formulaire par défaut, avec des titres de colonnes différents pour les 
options.

#### Formulaires à section { #section-forms } 

Les formulaires à section offrent plus de flexibilité lorsqu'il s'agit d'utiliser 
des formes tabulaires et sont rapides et simples à concevoir. Votre formulaire de saisie de 
données nécessite souvent plusieurs tableaux avec sous-titres, et vous devez parfois 
désactiver (griser) quelques champs du tableau (Exemple : certaines catégories ne 
s'appliquent pas à tous les éléments de données). Ces deux fonctions sont prises en charge 
dans les formulaires à section. Après avoir défini un ensemble de données, vous pouvez définir ses sections 
avec des sous-ensembles d'éléments de données, une en-tête et d'éventuels champs gris 
dans le tableau de la section. L'ordre des sections dans un ensemble de données peut également être 
défini. Dans Saisie de Données, vous pouvez maintenant commencer à utiliser le formulaire à Section ( qui 
devrait apparaître automatiquement lorsque des sections sont disponibles pour l'ensemble 
de données sélectionné). La plupart des formulaires de saisie de données tabulaires doivent pouvoir être réalisés à l'aide 
de formulaires de section. L'utilisation de formulaires par section ou par défaut rend la vie plus facile 
car il n'est pas nécessaire de maintenir une conception de formulaire fixe qui inclut 
des références à des éléments de données. Si ces deux types de formulaires ne répondent pas 
à vos exigences, la troisième option est le formulaire de saisie de données personnalisé, totalement flexible, 
bien qu'il prenne plus de temps.

#### Formulaires personnalisés { #custom-forms } 

Lorsque le formulaire que vous souhaitez concevoir est trop compliqué pour les formulaires par défaut ou 
les formulaires de section, votre dernière option est l'utilisation d'un formulaire personnalisé. Cette option prend 
plus de temps, mais vous offre une flexibilité totale en termes de conception. Dans 
DHIS2, le concepteur de formulaire dispose d'un éditeur HTML intégré (CK Editor) qui vous 
permet soit de concevoir le formulaire dans l'interface graphique, soit de coller 
directement votre code HTML (en utilisant la fenêtre "source" de l'éditeur). Dans le 
formulaire personnalisé, vous pouvez insérer du texte statique ou des champs de données (liés à des éléments de données
+ combinaison d'options de catégorie) à n'importe quel endroit du formulaire et vous êtes 
totalement libre de concevoir la mise en page du formulaire. Une fois qu'un formulaire personnalisé 
a été ajouté à un ensemble de données, il sera disponible dans la saisie de données et utilisé
automatiquement.

Lors de l'utilisation d'un formulaire personnalisé, des champs calculés peuvent être utilisés 
pour afficher, par exemple, des totaux courants ou d'autres calculs basés sur les données 
saisies dans le formulaire. Cela peut s'avérer utile, par exemple, dans le cas de formulaires de stock ou 
de logistique qui requièrent le solde des articles, les articles nécessaires pour la période suivante, 
etc. Pour ce faire, l'utilisateur doit d'abord définir les expressions calculées 
en tant qu'indicateurs, puis affecter ces indicateurs à l'ensemble de données 
en question. Dans le concepteur de formulaires personnalisés, l'utilisateur peut ensuite affecter 
des indicateurs au formulaire de la même manière que les éléments de données. 
La limite de l'expression calculée est que tous les éléments de données 
utilisés dans l'expression doivent être disponibles dans le même ensemble de données puisque 
les calculs sont effectués à la volée dans le formulaire et ne sont pas basés sur 
des valeurs de données déjà stockées dans la base de données.

## Du papier au formulaire électronique - Leçons tirées de l'expérience { #from-paper-to-electronic-form-lessons-learned } 

Lors de la mise en place d'un système d'information de santé informatisé, le système 
devant être remplacé est souvent basé sur des rapports papiers. Le processus de migration 
vers la collecte électronique de données et l'analyse comporte quelques défis. Les 
sections suivantes indiquent les meilleures pratiques sur la façon de les relever.

### Identifier les éléments de données autonomes { #identify-self-contained-data-elements } 

Généralement, la conception d'un ensemble de données dans DHIS2 est basée sur certaines exigences 
d'un formulaire papier déjà utilisé. La logique des formulaires papier n'est 
pas la même que le modèle d'élément de donnée et d'ensemble de données du système DHIS2 ; par exemple, 
un champ dans un formulaire papier tabulaire est souvent décrit à la fois par des en-têtes de colonnes et 
du texte sur chaque ligne, et parfois aussi avec un titre de tableau d'introduction 
qui fournit plus de contexte. Dans la base de données, cela est saisi dans 
un élément de donnée atomique sans référence à une position dans un format de tableau visuel. 
Il est donc important de s'assurer que l'élément de donnée avec les 
catégories d'éléments de donnée facultatives reflète la pleine signification de chaque 
champ individuel dans le formulaire papier.

### Laisser les calculs et les répétitions à l'ordinateur - ne capturer que les données brutes { #leave-calculations-and-repetitions-to-the-computer-capture-raw-data-only } 

Un autre aspect important à prendre en considération lors de la conception des ensembles de données est 
que l'ensemble de données et le formulaire de saisie correspondant (qui est un ensemble 
de données avec une mise en page) est un outil de collecte de données et non un outil de rapport ou d'analyse. 
Il existe d'autres outils bien plus sophistiqués pour la production des données et 
l'établissement de rapports dans le DHIS2 que les formulaires de saisie. Les formulaires papier sont souvent 
conçus en tenant compte à la fois de la collecte des données et des rapports et vous pouvez donc 
voir des éléments tels que les valeurs cumulées (en plus 
des valeurs mensuelles), la répétition des données annuelles (les mêmes données démographiques 
déclarées chaque mois) ou même des valeurs des indicateurs telles que les taux de couverture dans 
le même formulaire que les données brutes mensuelles. Lorsque vous stockez les données brutes dans 
la base de données DHIS2 chaque mois et que vous disposez de toute la puissance de traitement 
nécessaire dans l'outil informatique, il n'est pas nécessaire (en fait, ce serait 
inadmissible et très probablement source d'incohérence) d'enregistrer des valeurs calculées manuellement 
telles que celles mentionnées ci-dessus. Vous devez uniquement 
saisir les données brutes dans vos ensembles de données/formulaires et laisser les calculs 
à l'ordinateur, ainsi que la présentation de ces valeurs aux outils de rapport 
du DHIS. Grâce à la fonctionnalité des rapports sur les ensembles de données, tous les formulaires à section tabulaire 
seront automatiquement dotés de colonnes supplémentaires à l'extrême droite, 
indiquant les valeurs totales et partielles pour chaque ligne (élément de données).

