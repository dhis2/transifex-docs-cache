---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/data-quality.md"
revision_date: '2023-01-11'
tags:
- Implémentation
---

# Qualité des Données { #data-quality } 

Ce chapitre traite de divers aspects relatifs à la qualité des données.

## Mesure de la qualité des données { #measuring-data-quality } 

Les données sont-elles complètes ? Sont-elles collectées à temps ? Sont-elles correctes ? Ce sont là 
des questions qu'il convient de se poser lors de l'analyse des données. La mauvaise qualité des données 
peut prendre de nombreuses formes : il ne s'agit pas seulement de chiffres erronés, mais aussi d'un manque de 
complétude ou de données trop anciennes (pour une utilisation efficace).

## Causes de la mauvaise qualité des données { #reasons-for-poor-data-quality } 

Il y a beaucoup de raisons pour expliquer la mauvaise qualité des données, on peut citer par exemple :

  - Quantités excessives collectées ; trop de données à collecter entraîne
    un manque de temps pour le faire et des "raccourcis" pour terminer le rapport 

  - Nombreuses étapes manuelles ; déplacement de chiffres, addition, etc. entre
    différents formulaires papier

  - Définitions imprécises ; interprétation erronée des champs 
    à remplir

  - Manque d'utilisation des informations : aucune incitation à améliorer la qualité

  - La fragmentation des systèmes d'information peut entraîner une duplication des
    déclarations

## Amélioration de la qualité des données { #improving-data-quality } 

L'amélioration de la qualité des données est une tâche de longue haleine et de nombreuses mesures sont 
de nature organisationnelle. Cependant, la qualité des données devrait être un problème à prendre en compte dès 
le début de tout processus de mise en œuvre, et certaines choses 
peuvent être traitées immédiatement, telles que les vérifications dans le DHIS2. Voici quelques mesures importantes 
d'amélioration de la qualité des données :

  - Modifier les formulaires de collecte de données et uniformiser les formulaires

  - Promouvoir l'utilisation des informations au niveau local, où les données sont collectées

  - Mettre en place des programmes pour vérifier la qualité des données

  - Inclure un cours sur la qualité des données dans la formation

  - Mettre en œuvre les contrôles de qualité des données dans DHIS2

## Utilisation de DHIS2 pour améliorer la qualité des données { #using-dhis2-to-improve-data-quality } 

DHIS2 dispose de plusieurs fonctionnalités qui peuvent contribuer à l'amélioration de la 
qualité des données : validation lors de la saisie des données pour s'assurer que les données sont saisies dans 
le bon format et dans une fourchette raisonnable, les règles de validation définies par 
l'utilisateur et basées sur des relations mathématiques entre les données 
saisies (par exemple, sous-totaux par rapport aux totaux), les fonctions d'analyse des valeurs aberrantes, ainsi que les 
rapports sur la couverture et l'exhaustivité des données. Plus indirectement, plusieurs 
des principes de conception du DHIS2 contribuent à améliorer la qualité des données, 
comme l'idée d'harmoniser les données dans un entrepôt de données 
intégré, de soutenir l'accès au niveau local aux données et aux outils d'analyse, et 
d'offrir une large gamme d'outils pour l'analyse et la diffusion des données. La 
qualité des données s'améliorera grâce à des processus 
de collecte de données plus structurés et harmonisés et à 
une meilleure utilisation de l'information à tous les niveaux. Voici un aperçu des fonctionnalités ciblant plus directement 
la qualité des données :

### Validation des saisies de données { #data-input-validation } 

Le type le plus élémentaire de contrôle de la qualité des données dans le DHIS2 consiste à s'assurer que 
les données saisies sont dans le bon format. Le DHIS2 envoie 
à l'utilisateur un message indiquant que la valeur saisie n'est pas dans le bon format 
et ne l'enregistre pas tant qu'elle n'a pas été remplacée par une valeur acceptée. 
Par exemple, il n'est pas possible d'entrer du texte dans un champ numérique. Les différents 
types de valeurs de données prises en charge dans le DHIS2 sont expliqués dans le manuel 
de l'utilisateur, dans le chapitre sur les éléments de données.

### Plages min et max { #min-and-max-ranges } 

Pour éviter les erreurs de frappe lors de la saisie des données (par exemple, taper "1000" au lieu de
"100"), le DHIS2 vérifie que la valeur saisie se situe dans une fourchette 
raisonnable. Cette fourchette est basée sur les données précédemment collectées 
par le même établissement de santé pour le même élément de données, et se compose 
d'une valeur minimale et d'une valeur maximale. Dès que l'utilisateur saisit une valeur 
en dehors de cette fourchette, il est averti que la valeur n'est pas acceptée. Pour 
calculer les fourchettes raisonnables, le système a besoin d'au moins six 
mois (périodes) de données.

### Règles de validation { #validation-rules } 

Une règle de validation est basée sur une expression qui définit une relation 
entre un certain nombre d'éléments de données. L'expression comporte un côté gauche et 
un côté droit, ainsi qu'un opérateur qui définit si le premier doit être inférieur, 
égal ou supérieur au second. L'expression forme une 
condition qui doit affirmer que certains critères logiques sont remplis. Par 
exemple, une règle de validation pourrait affirmer que le nombre total de 
vaccins administrés aux nourrissons est inférieur ou égal au nombre total de 
nourrissons. Les côtés gauche et droit doivent renvoyer des valeurs numériques.


Les règles de validation peuvent être définies via l'interface utilisateur et exécutées 
ultérieurement pour vérifier les données existantes. Lors de l'exécution des règles de validation, 
l'utilisateur peut spécifier les unités d'organisation et les périodes pour lesquelles les données doivent être vérifiées, 
car une vérification de toutes les données existantes prendrait beaucoup de temps et pourrait 
ne pas être efficace non plus. Lorsque les contrôles sont terminés, un rapport sera
présenté à l'utilisateur avec les violations de validation expliquant quelles valeurs 
de données doivent être corrigées.

Les contrôles des règles de validation sont également intégrés dans le processus de saisie 
des données, de sorte que lorsque l'utilisateur aura fini de remplir un formulaire, les règles pourront être exécutées pour vérifier 
les données de ce formulaire uniquement, avant de le fermer.

### Analyse des valeurs aberrantes { #outlier-analysis } 

L'analyse des valeurs aberrantes basée sur un écart-type fournit un mécanisme 
permettant de révéler les valeurs numériquement éloignées du reste des données. 
Les valeurs aberrantes peuvent être le fruit du hasard, mais elles indiquent souvent une 
erreur de mesure ou une distribution à forte densité (conduisant à des nombres très élevés). 
Dans le premier cas, il convient de les écarter, tandis que dans le second, il convient d'être 
prudent dans l'utilisation d'outils ou d'interprétations qui supposent une 
distribution normale. L'analyse est basée sur la distribution normale 
standard.

### Complétude et ponctualité des rapports { #completeness-and-timeliness-reports } 

Les rapports d'exhaustivité indiquent le nombre d'ensembles de données (formulaires) 
soumis par unité d'organisation et par période. Vous pouvez utiliser l'une des trois 
méthodes suivantes pour calculer l'exhaustivité : 1) sur la base du bouton d'exhaustivité 
lors de la saisie des données, 2) sur la base d'un ensemble d'éléments de données obligatoires 
définis, ou 3) sur la base du nombre total de valeurs de données enregistrées pour un 
ensemble de données.

Les rapports d'exhaustivité indiquent également les unités d'organisation d'une 
région qui font des déclarations dans les délais, ainsi que le pourcentage des 
établissements qui font des déclarations dans les délais dans une région donnée. Le calcul de la ponctualité est basé sur un 
paramètre du système appelé Jours après la fin de la période pour être éligible à la 
soumission de données dans les délais.


## Calcul de l'intégralité des éléments de données { #calculating-completeness-for-data-elements }
Dans certaines implémentations du DHIS2, il a été observé que les rapports n'étaient pas cohérents pour tous les éléments de données d'un ensemble de données. Par défaut, DHIS2 n'évalue que les taux de déclaration des ensembles de données et non des éléments de données individuels de cet ensemble. L'objectif du taux de déclaration d'un élément de données est d'évaluer la cohérence de la déclaration d'une valeur unique. Ceci ne concerne que les éléments de données agrégés.

Un taux de reporting est : 100 x (Nombre de valeurs reçues / Nombre de valeurs attendues)

Pour calculer le taux de déclaration d'un élément de données, nous devons définir un indicateur avec le numérateur (nombre de valeurs reçues) et le dénominateur (nombre de valeurs attendues), et avec un facteur de 100 (type d'indicateur de pourcentage). Il n'y a qu'une seule façon de définir le numérateur, mais il existe plusieurs options pour calculer le dénominateur.

Les versions 2.38 et supérieures du DHIS permettent de définir directement de tels indicateurs. Dans les versions 2.37 et inférieures, les prédicteurs devraient être utilisés en tant qu'étape intermédiaire dans le calcul. Ces deux approches sont décrites séparément.

### Instructions pour 2.38 et au-delà{ #instructions-for-238-and-higher }

Les versions 2.38 et supérieures du DHIS permettent de calculer le numérateur et le dénominateur directement à l'aide d'indicateurs. Pour le dénominateur, il existe plusieurs possibilités de définition, c'est-à-dire le "nombre attendu de rapports", chacune d'entre elles étant décrite et accompagnée d'indications concernant le moment où elle est appropriée.


#### Numérateur { #numerator } 
Le *numérateur* doit être le **nombre de valeurs** pour un élément de données. Pour cela, nous recommandons d'utiliser les instructions conditionnelles subExpression (sous-Expression) et isNotNull (estNonNul) dans l'expression. Cela renverra la valeur 1 chaque fois qu'un nombre (y compris zéro) sera saisi pour cet élément de données. Un exemple est donné ci-dessous.

![Exemple d'expression du numérateur](resources/images/de_completeness_1.png)

Pour les éléments de données qui sont désagrégés avec une combinaison de catégories, vous devriez déterminer s'il faut compter les éléments de données comme "déclarés" s'il y a des données pour n'importe laquelle des désagrégations (combinaisons d'options de catégories), ou s'il est plus judicieux d'établir l'indicateur de l'intégralité pour une désagrégation en particulier. Dans l'exemple ci-dessus, c'est la première solution qui est retenue. Pour vérifier l'intégralité d'une combinaison d'options de catégorie, il convient d'inclure son ID dans l'expression interne.

#### Définition d'un dénominateur { #denominator-definition }
Il s'agit des principales options permettant de définir le calcul du dénominateur, c'est-à-dire le nombre de rapports attendus :

1. Nombre de valeurs rapportées d'un autre élément de données faisant partie du même ensemble de données
2. Nombre d'unités auxquelles l'ensemble de données, dont l'élément de données fait partie est attribué
3. Nombre d'unités d'organisation qui ont déjà déclaré l'élément de données lui-même

##### Option 1 { #option-1 }

Cette option consiste à utiliser le nombre de valeurs rapportées pour un autre élément de données comme **valeurs attendues** dans le calcul intégral des données. Cet autre élément de données peut être choisi sur la base de différents critères, décrits ci-dessous.

L'une des limites de cette approche est qu'elle ne donne pas un aperçu **de tout** l'ensemble des données, mais seulement de l'intégralité d'éléments de données spécifiques au sein des ensembles de données. Elle doit donc être analysée en même temps que l'exhaustivité générale des ensembles de données ou, par exemple, l'option 2.

###### Basé sur l'indicateur de base { #based-on-core-indicator }
Si l'élément de données pour lequel vous souhaitez obtenir un taux de déclaration est utilisé dans le calcul d'un indicateur clé de performance avec des données régulièrement rapportées dans le dénominateur, il est recommandé d'utiliser le nombre de valeurs rapportées pour le dénominateur afin de calculer leur exhaustivité. Cette option n'est pas viable si l'élément de données n'est pas utilisé dans le calcul d'un indicateur ou si le dénominateur est basé sur une estimation de la population ou une autre valeur qui n'est pas déclarée avec la même périodicité que le numérateur.

Pour expliquer cette option, nous commencerons par un exemple d'indicateur, *Cas suspects dépistés au paludisme (%)* :

> Nombre total de cas de paludisme dépistés / (cas suspects en clinique + cas suspects dans la communauté)


Nous voulons maintenant connaître le taux de déclaration de *Total des cas dépistés du paludisme* et nous utiliserons donc *cas suspects en clinique et cas suspects dans la communauté* pour définir le nombre de nos valeurs attendues. Si je voulais créer un taux de déclaration d'un élément de données basé sur la première option de dénominateur, le dénominateur dans cet exemple serait :

```
sousExpression(if( estNonNul(#{sVDDqpaKwBH}) || estNonNul(#{ylTxB8pDdW6}),1,0))
```

![](resources/images/de_completeness_2.png)

Cette expression renverra une valeur 1 si quelque chose (y compris un zéro) est saisi pour les cas suspects cliniques ou les cas suspects dans la communauté, ce qui correspond alors au nombre attendu de rapports de cas de paludisme dépistés (notre numérateur).

L'avantage de cette option est qu'elle donne une bonne indication de l'intégralité/de la cohérence des données utilisées pour calculer un indicateur de base particulier (comme *Cas suspects testés pour le paludisme (%)* dans l'exemple ci-dessus).


*Basé sur un élément de données connexe*

Cette option est similaire à la précédente, mais elle consiste à utiliser un élément de données étroitement lié à l'élément de données du numérateur pour calculer le dénominateur. Par exemple, si vous recherchez un taux de déclaration pour les cas de paludisme hospitalisés de moins de 5 ans (numérateur), vous pouvez envisager d'utiliser les cas de paludisme hospitalisés de 5 ans et plus, les décès dus au paludisme hospitalisés, les cas de paludisme ambulatoires, etc.


*Basé sur un élément de données dans le même ensemble de données*

Cette option est similaire à la précédente, mais elle utilise un élément de données déclaré dans le même ensemble de données ou la même section d'ensemble de données que l'élément de données pour lequel vous calculez le taux de déclaration (numérateur) - sans qu'il y ait nécessairement un lien logique. Avec cette approche, vous devez choisir un élément de données qui est toujours (ou souvent) rapporté dans l'ensemble de données. Par exemple, dans un ensemble de données sur la santé maternelle, il est probable le nombre d'établissements de santé qui déclarent un élément de données pour les "premières visites de soins prénatals" soit plus élevé que celui de l'"accouchement assisté", et les "premières visites de soins prénatals" constituent donc une meilleure estimation du nombre de déclarations attendues.


##### Option 2 { #option-2 } 

Cette option est recommandée pour les pays qui collectent un élément de données dans plusieurs ensembles de données et qui souhaitent néanmoins disposer des rapports prévus sur la base de l'affectation de l'unité d'organisation de l'ensemble de données.

Pour configurer cette option, il vous suffit de sélectionner les rapports **attendus** ou **réels** pour les ensembles de données que vous souhaitez additionner dans le dénominateur. Ces rapports peuvent être sélectionnés sous l'onglet "Taux de rapport" dans la fenêtre d'expression de l'indicateur. Le choix de **déclarations réelles** donnera un indicateur de l'exhaustivité de l'élément de données parmi les unités d'organisation qui ont déclaré, tandis que l'utilisation de **déclarations attendues** donnera un indicateur de l'exhaustivité de l'élément de données parmi toutes les unités d'organisation censées déclarer.

![](resources/images/de_completeness_5.png)

![](resources/images/de_completeness_7.png)


##### Option 3 { #option-3 } 

Dans cette option, nous vérifions si l'établissement a rapporté l'élément de données que vous évaluez pour le taux de déclaration au cours des 12 derniers mois (d'autres périodes plus longues ou plus courtes peuvent être utilisées). Ce faisant, l'élément de données du numérateur est le même que celui du dénominateur, sauf que nous utilisons également l'expression periodOffSet pour évaluer si une valeur a été enregistrée au cours de chacun des 12 derniers mois.

![](resources/images/de_completeness_6.png)

Exemple de dénominateur de l'option 3.

```
subExpression(if(isNotNull(#{fbfJHSPpUQD}.periodOffset(-1)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-2)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-3)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-4)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-5)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-6)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-7)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-8)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-9)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-10)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-11)) || isNotNull(#{fbfJHSPpUQD}.periodOffset(-12)),1,0))
```

### Instructions pour la version 2.37 ou inférieure. { #instructions-for-237-or-lower }

Si vous utilisez la version 2.37 ou une version inférieure, vous devrez utiliser une combinaison de variables prédictives et d'indicateurs pour calculer les taux de déclaration des éléments de données. Un prédicteur sera utilisé pour calculer la valeur des **rapports attendus** et la sauvegarder en tant qu'élément de données, un autre prédicteur est utilisé pour calculer la valeur des **rapports attendus** et la sauvegarder en tant qu'élément de données, et enfin ces deux éléments de données sont combinés en un indicateur d'exhaustivité.

Notez que les prédicteurs devront être programmés pour être exécutés sur le serveur. Voir la section **Etapes finales** pour obtenir des instructions à ce sujet.


#### Numérateur { #numerator } 

À cet effet, vous devez créer un prédicteur qui utilise les instructions confidentielles isNotNull dans le générateur. Il renverra la valeur 1 chaque fois qu'un nombre (y compris zéro) sera saisi pour cet élément de données.

Étapes de création du prédicteur :

1. Faites en sorte que les sorties de données soient des éléments d'information.

2. Attribuez à votre prédicteur l'élément de sortie de données.

3. Définir le type de période (généralement mensuelle).

4. Attribuer le niveau de l'unité d'organisation pour l'analyse (généralement le niveau de l'établissement).

5. Configurez le générateur comme suit.

6. Régler le nombre d'échantillons séquentiels à 0

7. Régler le nombre d'échantillons annuels à 0

8. Ne rien inscrire dans le champ de comptage des sauts séquentiels.

9. Créez un groupe de prédicteurs et ajoutez ce prédicteur à ce groupe.

10. Définissez maintenant le prédicteur pour le dénominateur et ajoutez ce prédicteur au même groupe de prédicteurs que celui auquel vous avez ajouté le prédicteur du numérateur.

![](resources/images/de_completeness_3.png)


#### Dénominateur { #denominator }

Le dénominateur peut être l'une de ces options.

1. Nombre de valeurs rapportées d'un autre élément de données faisant partie du même ensemble de données
2. Nombre d'unités auxquelles l'ensemble de données, dont l'élément de données fait partie est attribué
3. Nombre d'unités d'organisation qui ont déjà déclaré l'élément de données lui-même

##### Option 1 { #option-1 }

Cette option consiste à utiliser le nombre de valeurs rapportées pour un autre élément de données comme valeurs attendues dans le calcul intégral des données. Cet autre élément de données peut être choisi sur la base de différents critères, décrits ci-dessous.

L'une des limites de cette approche est qu'elle ne donne pas un aperçu de tout l'ensemble des données, mais seulement de l'intégralité d'éléments de données spécifiques au sein des ensembles de données. Elle doit donc être analysée en même temps que l'exhaustivité générale des ensembles de données ou, par exemple, l'option 2.

###### Basé sur l'indicateur de base { #based-on-core-indicator }
Si l'élément de données pour lequel vous souhaitez obtenir un taux de déclaration est utilisé dans le calcul d'un indicateur clé de performance avec des données régulièrement rapportées dans le dénominateur, il est recommandé d'utiliser le nombre de valeurs rapportées pour le dénominateur afin de calculer leur exhaustivité. Cette option n'est pas viable si l'élément de données n'est pas utilisé dans le calcul d'un indicateur ou si le dénominateur est basé sur une estimation de la population ou une autre valeur qui n'est pas déclarée avec la même périodicité que le numérateur.

Pour expliquer cette option, nous commencerons par un exemple d'indicateur, *Cas suspects dépistés au paludisme (%)* :

> Nombre total de cas de paludisme dépistés / (cas suspects en clinique + cas suspects dans la communauté)

Pour calculer le taux de déclaration des *Cas suspects dépistés pour le paludisme (%)*, nous utiliserons **cas suspects en clinique** et **cas suspects dans la communauté** pour définir le nombre de nos valeurs attendues. Pour créer le prédicteur du dénominateur de cet exemple, il faut d'abord suivre les étapes 1-4 de la création du numérateur décrite ci-dessus. Le générateur dans cet exemple est :

```
if(isNotNull(Cas suspects en clinique) OR isNotNull(Cas suspects dans la Communauté),1,0)
```

![](resources/images/de_completeness_4.png)

Définir le nombre d'échantillons séquentiels à 0. Définir le nombre d'échantillons annuels à 0. Laisser la case du nombre de sauts séquentiels vierge et ajouter le prédicteur au groupe de prédicteurs.

*Basé sur un élément de données connexe*

Cette option est similaire à la précédente, mais elle consiste à utiliser un élément de données étroitement lié à l'élément de données du numérateur pour calculer le dénominateur. Par exemple, si vous recherchez un taux de déclaration pour les cas de paludisme hospitalisés de moins de 5 ans (numérateur), vous pouvez envisager d'utiliser les cas de paludisme hospitalisés de 5 ans et plus, les décès dus au paludisme hospitalisés, les cas de paludisme ambulatoires, etc.


*Basé sur un élément de données dans le même ensemble de données*

Cette option est similaire à la précédente, mais elle utilise un élément de données déclaré dans le même ensemble de données ou la même section d'ensemble de données que l'élément de données pour lequel vous calculez le taux de déclaration (numérateur) - sans qu'il y ait nécessairement un lien logique. Avec cette approche, vous devez choisir un élément de données qui est toujours (ou souvent) rapporté dans l'ensemble de données. Par exemple, dans un ensemble de données sur la santé maternelle, il est probable le nombre d'établissements de santé qui déclarent un élément de données pour les "premières visites de soins prénatals" soit plus élevé que celui de l'"accouchement assisté", et les "premières visites de soins prénatals" constituent donc une meilleure estimation du nombre de déclarations attendues.


##### Option 2 { #option-2 } 

Cette option est recommandée pour les pays qui collectent un élément de données dans plusieurs ensembles de données et qui souhaitent néanmoins disposer des rapports prévus sur la base de l'affectation de l'unité d'organisation de l'ensemble de données.

Cette option ne nécessite *pas* la création d'un prédicteur pour le numérateur. Pour configurer cette option, il vous suffit de sélectionner les rapports **attendu** ou **réel** pour les ensembles de données que vous souhaitez additionner dans le dénominateur, ainsi que la valeur du numérateur générée par le prédicteur comme décrit ci-dessus. Les rapports réels/attendus peuvent être sélectionnés dans l'onglet "Taux de déclaration" de la fenêtre d'expression de l'indicateur. En choisissant **rapports réels**, vous obtiendrez un indicateur de l'exhaustivité de l'élément de données parmi les unités d'organisation qui ont fait un rapport, tandis qu'en utilisant **rapports attendus**, vous obtiendrez un indicateur de l'exhaustivité de l'élément de données parmi toutes les unités d'organisation qui devraient faire un rapport.


![](resources/images/de_completeness_5.png)

![](resources/images/de_completeness_7.png)


##### Option 3 { #option-3 } 

Dans cette option, nous vérifions si l'établissement a rapporté l'élément de données que vous évaluez pour le taux de déclaration au cours des 12 derniers mois (d'autres périodes plus longues ou plus courtes peuvent être utilisées). Ce faisant, l'élément de données du numérateur est le même que celui du dénominateur, sauf que nous utilisons également l'expression periodOffSet pour évaluer si une valeur a été enregistrée au cours de chacun des 12 derniers mois.

Ce prédicteur pour l'option 3 est défini de la même manière que les étapes 1-4 du numérateur. Le générateur devrait être :

![](resources/images/de_completeness_8.png)

Le nombre d'échantillons séquentiels doit être fixé à 12 si vous souhaitez obtenir un échantillon de 12 mois précédents. Tout autre nombre de mois peut être également échantillonné en modifiant cette valeur.

Réglez le nombre d'échantillons annuels à 0. Laisser vierge la case du nombre de sauts séquentiels et ajouter le prédicteur au groupe de prédicteurs.

#### Étapes finales { #final-steps }

1. Dans l'application de planification, créez une règle prédictive et définissez son exécution hebdomadaire. Sélectionnez le groupe de règles prédicteurs qui comprend les prédicteurs pour le numérateur et le dénominateur. La valeur relative de départ doit être -30 et la valeur relative de fin doit être 0 pour les données mensuelles.

2. Assurez-vous que la règle prédictive est programmée quelques heures avant l'exécution des tables analytiques.

3. Créez les indicateurs de taux de déclaration des éléments de données qui incluent les éléments de données du numérateur et du dénominateur que vous avez définis à partir des variables prédictives. L'indicateur doit être défini en pourcentage.

