---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/indicators.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Indicateurs { #indicators } 

Ce chapitre traite des sujets suivants:

  - Qu'est-ce qu'un indicateur

  - Les buts des indicateurs

  - La collecte de données axée sur les indicateurs

  - Gestion des indicateurs dans DHIS2

La section suivante décrit ces sujets plus en détail.

## Qu'est-ce qu'un indicateur { #what-is-an-indicator } 

Dans DHIS2, l'indicateur est un élément central de l'analyse des données. Un indicateur 
est une formule calculée basée sur une combinaison d'éléments de données, 
d'options de catégories, éventuellement de constantes et d'un facteur. Il existe deux types 
d'indicateurs : ceux qui ont un dénominateur et ceux qui n'en ont pas. 
Les totaux calculés, qui peuvent être composés de plusieurs éléments de données, 
n'ont pas de dénominateur. Les indicateurs de couverture (ratios, 
pourcentages, etc.) sont composés de deux formules d'éléments de données, l'une 
représentant le numérateur et l'autre le dénominateur.

Les indicateurs sont donc constitués de formules d'éléments de données et d'autres 
composants et sont toujours multipliés par un facteur (par exemple 1, 100, 100, 100 
000). Le facteur est essentiellement un nombre qui est multiplié par le 
résultat du numérateur divisé par le dénominateur. A titre d'exemple concret, 
l'indicateur "Couverture BCG <1 an" est défini par une formule avec un 
acteur 100 (afin d'obtenir un pourcentage), un numérateur ("doses de BCG 
administrées à des enfants de moins d'un an") et un dénominateur ("population cible 
de moins d'un an"). L'indicateur "Taux d'abandon du DPT1 au DPT3" est une formule 
de 100 % x ("doses de DPT1 administrées" - "doses de DPT3 administrées") / ("doses 
de DPT1 administrées").



Tableau : exemples d'indicateurs

| Indicateur | Formule | Numérateur | Dénominateur | Facteur |
|---|---|---|---|---|
| Couverture des <1 an entièrement vaccinés | Entièrement vacciné/Population <1 an x 100 | Entièrement vacciné | Population < 1 | 100 (Pourcentage) |
| Taux de mortalité maternelle | Décès maternels/naissances vivantes x 100 000 | Décès maternels | Naissances vivantes | 100 000 (le TMM se calcule par tranche de 100 000) |
| Nombre total de personnes participant à des programmes de soins | Nombre total de personnes participant à des programmes de soins x 1 | Nombre total de participants à des programmes de soins (Homme âgé de < 18 ans) + Nombre total de participants à des programmes de soins (Homme âgé de plus de 18 ans) + Nombre total de participantes à des programmes de soins (Femme âgée de < 18 ans) + Nombre total de participantes à des programmes de soins (Femme âgée de plus de 18 ans) | Aucun | 1 |

## Les buts des indicateurs { #purpose-of-indicators } 

Les indicateurs définis avec des numérateurs et des dénominateurs sont 
généralement plus utiles pour l'analyse. Comme il s'agit de proportions, ils 
sont comparables dans le temps et dans l'espace, ce qui est très important puisque 
les unités d'analyse et de comparaison, telles que les districts, varient en taille et 
évoluent dans le temps. Un district de 1000 habitants pourrait avoir 
moins de cas d'une maladie donnée qu'un district de 10 000 habitants. 
Cependant, les valeurs d'incidence d'une maladie donnée seront 
comparables entre les deux districts en raison de l'utilisation des 
populations respectives de chaque district.

Les indicateurs permettent donc des comparaisons et constituent le principal outil d'analyse 
des données. DHIS2 devrait fournir des indicateurs pertinents pour l'analyse de tous 
les programmes de santé, et pas seulement des données brutes. La plupart des modules de rapport de DHIS2 
prennent en charge les éléments de données aussi bien que les indicateurs, et vous pouvez également les combiner 
dans des rapports personnalisés.

## La collecte de données axée sur les indicateurs { #indicator-driven-data-collection } 

Étant donné que les indicateurs se prêtent mieux à l'analyse que les éléments de données, 
le calcul des indicateurs devrait être le principal moteur de la 
collecte de données. Il arrive souvent que de nombreuses données soient collectées mais 
ne soient jamais utilisées dans un indicateur, ce qui réduit considérablement la possibilité d'utiliser 
les données. Soit les éléments de données collectés devraient être inclus dans 
les indicateurs utilisés pour la gestion, soit ils ne devraient probablement pas être collectés 
du tout.

Dans le cadre de la mise en œuvre, une liste d'indicateurs utilisés pour la gestion 
devrait être définie et mise en œuvre dans le DHIS2. Pour l'analyse, la formation 
devrait se concentrer sur l'utilisation des indicateurs et sur les raisons pour lesquelles ils sont mieux adaptés 
que les éléments de données à cette fin.

## Gestion des indicateurs dans DHIS 2 { #managing-indicators } 

Les indicateurs peuvent être ajoutés, supprimés ou modifiés à tout moment dans DHIS2 
sans affecter les données. Les indicateurs ne sont pas stockés sous forme de valeurs dans 
DHIS2, mais sous forme de formules, qui sont calculées chaque fois que l'utilisateur en a 
besoin. Par conséquent, une modification des formules n'entraînera qu'un appel à des éléments 
de données différents lors de l'utilisation de l'indicateur à des fins d'analyse, sans que 
les valeurs des données sous-jacentes ne soient modifiées. Pour plus d'informations 
sur la gestion des indicateurs, veuillez vous référer au chapitre sur les indicateurs dans 
la documentation utilisateur de DHIS2.

