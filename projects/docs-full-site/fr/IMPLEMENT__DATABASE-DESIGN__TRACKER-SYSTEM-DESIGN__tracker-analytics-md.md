---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/tracker-analytics.md"
revision_date: '2023-05-24'
tags:
- Implémentation
---

# Analyse du Tracker { #tracker-analytics } 

![](resources/images/image45.png "Step4")


Il existe quatre façons principales de consommation des données de suivi par les applications analytiques du DHIS2 afin de produire des résultats analytiques, tels que des tableaux, des graphiques et des cartes.


* Line Listing (Liste de Ligne)
* Éléments de données d'événements dans l'application Visualiseur de Données
* Indicateurs de programme
* Indicateurs (voir "Défi commun 4 : agrégation et désagrégation")

## Liste des lignes (v2.38 et plus) { #line-listing-v238-and-above } 

Produit une liste de toutes les inscriptions ou de tous les événements d'un programme qui répondent à des critères définis. Ces critères peuvent être une combinaison d'unités d'organisation, de dimensions temporelles et de valeurs de données spécifiques. Par exemple, vous pouvez définir une liste de lignes pour toutes les inscriptions au programme de traitement du paludisme, où l'unité d'organisation est l'ensemble des établissements du district, où les dates d'inscription se situent dans les 3 derniers mois et où la valeur de l'élément de données " Résultat du Cas " est le décès.

Les champs de chaque ligne de la liste peuvent être spécifiés par l'utilisateur, par exemple un attribut d'entité suivi ("identification du cas"), une valeur d'élément de données dans une étape donnée du programme ("médicament contre le paludisme"). L'exemple ci-dessous, tiré du programme d'événements de morbidité et de mortalité chez les patients hospitalisés, montre les admissions par date d'admission, par genre et par date de sortie, le tout filtré par l'âge à l'admission. Il combine donc des attributs d'entités suivies (TEA), des valeurs d'indicateurs de programme et des valeurs d'éléments de données.

Lorsque vous utilisez des programmes trackers, vous pouvez combiner plusieurs étapes et afficher les données des X derniers événements de chaque étape dans une liste horizontale.

Plus de détails peuvent être trouvés ici dans [documentation](#using-the-line-listing-app).


![Application de liste de lignes](resources/images/image21.png "Line Listing app"){.largeur du centre="90%"}


Notez que de nombreuses fonctionnalités de la liste de lignes sont également possibles avec une liste de travail dans l'application de saisie ou l'application de suivi. Pour l'utilisateur final, la liste de travail peut être plus utile que la liste de lignes, car il n'est pas nécessaire d'ouvrir une nouvelle fenêtre/application pour afficher la liste des patients, et en cliquant sur un cas individuel dans une liste de travail, vous accédez directement au profil du TEI.

Pour les analystes de données, les listes de lignes sont très utiles pour repérer les valeurs aberrantes individuelles qui remplissent certaines conditions, en particulier entre les unités d'organisation et les périodes. Cependant, il est très difficile de voir _les tendances sous-jacentes_ dans les données en visualisant une longue liste d'événements ou d'inscriptions. Au fur et à mesure que les programmes de suivi prennent de l'ampleur, vous souhaiterez voir les données de suivi agrégées de manière significative.

L'équipe centrale du DHIS2 recommande d'utiliser la nouvelle application Liste de lignes plutôt que l'ancienne application "Rapports d'événements", qui a été remplacée par la Liste de lignes et ne sera plus prise en charge dans les versions futures.


## Éléments de données d'événements dans l'application Visualiseur de données { #event-data-items-in-data-visualizer-app } 

Il est également possible d'agréger certains éléments de données d'événements directement dans l'application Visualiseur de données pour produire des tableaux croisés dynamiques et des graphiques. Les rapports de l'application Visualiseur de données peuvent être traités et modifiés en temps réel par l'utilisateur final.

Il est important de noter que seules les valeurs numériques peuvent être agrégées. Le mode d'agrégation de ces valeurs numériques est défini par le type d'agrégation de l'élément de données, ou l'agrégation peut être définie dans les _Options_ pour l'ensemble de la visualisation. Ces visuels de données de suivi peuvent être générés directement à partir de l'application Visualiseur de données :

_Poids moyen en grammes à la naissance dans le programme pour enfants, par mois dans l'établissement_

_Nombre total de ménages contrôlés par des enquêtes ciblées sur le paludisme, par district, durant l'année en cours_

Pour certaines configurations, le Visualiseur de données peut être un moyen rapide d'obtenir un résumé des données d'entrée de l'événement. Mais il existe des **limites** critiques à l'agrégation directe d'éléments de données :


* La recherche inclut toutes les valeurs d'éléments de données trouvées dans tous les événements pour les dimensions données du programme, de l'unité d'organisation et de la période. Si l'élément de données est présent dans plusieurs étapes ou dans une étape répétable, ces valeurs d'éléments de données seront agrégées ensemble.
* Seule la date de l'événement peut être utilisée comme dimension temporelle, et non la date d'inscription, ni une limite de période rétrospective pour créer une "cohorte" d'événements antérieurs au début de la période.
* Il est impossible d'agréger les données en fonction de la valeur d'un ensemble d'options (variable catégorielle), tel que le nombre total d'événements où l'élément de données " Résultat " est " Guéri ".
* Il est impossible d'appliquer des filtres pour exclure des valeurs d'éléments de données numériques saisies par erreur au-dessus ou au-dessous de seuils, comme exclure tous les "poids de nourrissons supérieurs à 10 000 g"
* Il est impossible de créer des désagrégations basées sur une deuxième donnée d'événement, qu'elle soit numérique ou catégorielle, telle que "poids à la naissance, au-delà et en deçà de 35 semaines de gestation" ou "poids à la naissance par sexe"
* Notez qu'avec l'application **Maps** (cartes), vous pouvez appliquer des filtres sur les éléments de données d'événements lors des recherches sur les couches d'événements. Les recherches filtrées peuvent également agréger des valeurs à des niveaux géographiques supérieurs. Ces filtres ne sont pas disponibles dans l'application Data Visualizer (visualiseur de données).

Par ailleurs, il est très difficile d'afficher dans l'application de visualisation des données des décomptes d'événements ou d'inscriptions de base répondant à des critères donnés. Pour les suivis courants dans le domaine de la santé, vous souhaitez générer un simple décompte des patients ou des rencontres qui remplissent certaines conditions. L'agrégation des valeurs des éléments de données individuels n'est pas aussi essentielle.


## Indicateurs de programme { #program-indicators } 

Les indicateurs de programme (IP) vous permettent de configurer facilement les recherches multicouches de vos données au niveau individuel. Ils permettent la création de valeurs basées sur des éléments de données et/ou des attributs d'entités suivies appartenant aux programmes trackers. Essentiellement, nous pouvons prendre les éléments de données individuels d'un programme tracker et générer des valeurs agrégées à utiliser dans l'analyse de routine.

L'IP peut être utilisé pour résumer les données au sein d'un événement ou d'une campagne entière, en combinant des données saisies à plusieurs étapes différentes ou des attributs d'entité suivis. Certaines configurations peuvent également inclure l'IP dans le "tableau de bord TEI" sur le web ou Android, afin de fournir des calculs à travers ou à l'intérieur des événements et de fournir un résumé de l'inscription à l'utilisateur pendant la saisie des données (nombre total d'événements, % de valeurs d'éléments de données non renseignées, nombre de jours écoulés depuis la dernière visite, etc). Cette section se concentre sur la configuration des indicateurs de programme afin d'afficher des données récapitulatives (comptes, sommes, moyennes, etc.) pour tous les événements ou inscriptions au sein d'une unité d'organisation/période spécifiée.

Il existe deux _types_ d'indicateurs de programme :


* **Événement** : Dimensions basées sur l'unité d'organisation de l'événement et (par défaut) la date de l'événement. Cette opération est basée sur tous les événements d'une même étape du programme.
* **Inscription** : Dimensions basées sur l'unité d'organisation de l'inscription et (par défaut) la date d'inscription. Peut évaluer des valeurs de données provenant de plusieurs étapes du programme, mais lors d'une recherche basée sur une seule valeur d'élément de données, les données de l'événement le plus récent de chaque étape répétable sont évaluées par défaut.


![Types d'indicateurs de programme](resources/images/image31.png){ .largeur centrale="80%" }


Les indicateurs de programme comportent cinq composantes qui définissent le mode de calcul de la valeur. Ils sont évalués dans cet ordre (voir ci-dessous pourquoi cela peut être important).

|Évaluation|Composante|Observation|
|--- |--- |--- |
|1|Unité d'organisation|Pour le type d'événement, il s'agit de l'unité d'organisation de l'événement. Pour le type d'affiliation, il s'agit de l'unité d'organisation de l'affiliation, même si certains événements d'une affiliation sont saisis ailleurs.|
|2|Période|Défini par les limites de la période d'analyse. Selon le type d'IP, il s'agit par défaut de la date d'affiliation ou de la date d'événement qui se situe entre le début et la fin de la période de déclaration.|
|3|Filtre|Créez un filtre de valeurs pour l'événement ou l'inscription. Il comprend les valeurs des attributs des instances d'entités suivies, ou tout élément de données à l'intérieur d'une étape spécifique du programme (type d'événement), ou tout élément de données à l'intérieur de toutes les étapes du programme. Diverses [fonctions et variables sont disponibles] (#program_indicator_functions_variables_operators) pour des opérations supplémentaires, comme le filtrage des TEI pour lesquels le nombre d'années entre la date d'inscription et la date de naissance est supérieur à 18.|
|4|Expression|Les critères ci-dessus définissent les affiliations (ou événements) à inclure. L'expression est la valeur appliquée à chaque inscription (ou événement). Il s'agit généralement de event_count, enrollment_count ou tei_count, mais il peut également s'agir d'une valeur d'élément de données ou d'une expression plus complexe.|
|5|Type d'Agrégation|Comment agréger l'expression appliquée à chaque inscription (ou événement). Généralement, il s'agit du "nombre" ou de la "moyenne".|



Les IP sont plus puissantes dans la condition **FILTER** (filtre) qui permet de définir si une inscription ou un événement répond à certains critères. Les critères de filtrage peuvent être tirés de _plusieurs_ éléments de données et/ou d'événements et/ou d'attributs d'entités suivies. Cette capacité est d'une importance cruciale dans la plupart des contextes de rapports centrés sur les patients et les cas, où il ne s'agit pas d'agréger des valeurs d'éléments de données atomiques, mais plutôt de compter les événements (rencontres) et les patients (inscriptions) qui remplissent un certain nombre de conditions.

Pour cette raison, il est **vivement recommandé de configurer des indicateurs de programme** pour tous les besoins de rapports de routine du système Tracker.


### Qu'est-ce qu'un Indicateur de Programme et pourquoi est-il important ?{ #what-is-a-program-indicator-really-and-why-does-it-matter } 

Techniquement, un indicateur de programme est un extrait Java préconfiguré qui peut être traduit par le moteur d'analyse DHIS2 en une expression SQL. Lorsque vous incluez un indicateur de programme dans une requête  analytique, par exemple en ouvrant un graphique dans le Visualiseur de données, cette expression SQL est combinée avec les dimensions de la période et de l'unité d'organisation dans une requête , et la recherche de base de données résultante des tables analytiques d'inscription et/ou d'événement renvoie un résultat.

|  |  | 
| ----- | -------- | 
| ![](resources/images/image22.png "Program Indicator output in pivot table")     |  ![](resources/images/image47.png "Program Indicator filter")         |

![La sortie, la configuration et la requête SQL pour une requête  d'indicateur de programme unique](resources/images/image4.png "Requête  d'indicateurs de programme Requête  SQL")


Une brève explication technique est importante pour comprendre quelques éléments clés des Indicateurs de Programme.

Premièrement, les IP permettent de construire des requêtes SQL très complexes avec une configuration minimale de la part du concepteur du système. Dans l'exemple ci-dessus, une seule ligne de code dans le filtre d'IP produit 8 lignes de code SQL, qui seraient répétées pour chaque dimension de période et d'unité d'organisation d'une requête analytique. Comparés aux requêtes SQL, les indicateurs de programme sont relativement faciles à configurer et, lorsqu'ils sont gérés habilement, ils sont suffisamment flexibles pour couvrir _la plupart_ des requêtes importantes que vous devriez effectuer sur les données des trackers.

En deuxième lieu, les valeurs des indicateurs de programme ne sont pas stockées dans la base de données DHIS2, mais elles fournissent un cadre pour une requête vers les tables analytiques de la base de données qui est effectuée "à la volée", ou dès qu'une visualisation avec un indicateur de programme est chargée par un utilisateur final. Cela signifie qu'il n'est pas nécessaire de générer à nouveau les tables d'analyse à chaque fois que vous créez ou modifiez un indicateur de programme.

Ces deux points présentent des compromis. Les IP sont souples et faciles à mettre en place, mais les requêtes SQL qui en résultent ne sont pas optimisées en termes de performances et, à grande échelle, elles peuvent être très inefficaces. Les IP sont également calculés à la demande, ce qui signifie que chaque fois qu'un utilisateur charge un tableau de bord avec des indicateurs de programme, il déclenche également une requête dans la base de données. De nombreux utilisateurs peuvent effectuer simultanément des requêtes analytiques inefficaces, ce qui exerce une pression inutile sur le serveur et entraîne un ralentissement important de l'ensemble du système.

>:mag : **Étude de Cas par Pays**
>
> L'impact des indicateurs de performance du programme était évident lors des campagnes de vaccination Covid-19, lorsque des millions d'inscriptions au tracker étaient consultées quotidiennement par des centaines de tableaux de bord d'utilisateurs finaux, ce qui entraînait souvent de sérieux problèmes de performance. Les [leçons tirées de cette expérience] (#tracker-performance-at-scale) ont fourni un cadre avec des techniques spécifiques pour améliorer l'analyse des trackers à l'échelle, comme les [scripts tracker-to-Aggregate] (#integrating-tracker-and-aggregate-data) pour écrire périodiquement les valeurs des indicateurs de programme dans des éléments de données agrégées.

Enfin, tout comme les éléments de données agrégées, les indicateurs de programme **requièrent une dimension d'unité d'organisation et une dimension de période** pour renvoyer une valeur significative. Mais alors qu'un élément de données agrégées est saisi pour une seule période et une seule unité d'organisation, les données de suivi sont naturellement beaucoup plus compliquées : une seule inscription aura probablement plusieurs événements au fil du temps, et chaque événement peut être saisi par différents établissements. Toutefois, l'IP ne produira en fin de compte qu'une seule valeur pour chaque combinaison d'unité d'organisation et de période. Lorsque vous concevez des indicateurs de programme, vous devez donc examiner attentivement la manière dont le "où" et le "quand" de vos données longitudinales doivent être interprétés.

Les exemples suivants illustrent les difficultés rencontrées lors de la définition et de la configuration des indicateurs de programme, notamment en ce qui concerne le type d'indicateur de programme, les limites de la période, l'affectation de l'unité d'organisation et la (dés)agrégation.


### Défi commun 1 : Événement vs type d'inscription  { #common-challenge-1-event-vs-enrollment-type } 

La décision la plus importante lors de l'élaboration d'un indicateur de programme est de savoir s'il doit s'agir d'un type d'événement ou d'un type d'inscription.

La plupart des implémenteurs savent que les deux types d'IP peuvent être filtrés par des valeurs d'éléments de données et/ou des valeurs d'attributs d'entités suivies (TEA). Et si l'indicateur de programme doit évaluer des valeurs provenant de deux étapes de programme ou plus, seule l'IP de type inscription peut être utilisée.

Mais une erreur très fréquente consiste à confondre les deux types de données lors de l'agrégation de données provenant d'étapes répétables du programme.

Rappelons que les événements représentent des _rencontres_ distinctes et que les inscriptions représentent des _fichiers par cas_ distincts. Lorsque vous utilisez des indicateurs de programme pour produire des comptages agrégés de données de suivi, la même logique conceptuelle s'applique : en général, nous utilisons des IP de type événement lorsque nous voulons compter des rencontres distinctes, et nous utilisons ceux de type inscription lorsque nous voulons compter des dossiers de cas distincts (ou des personnes).

Les implémenteurs doivent se poser la question suivante : _Est-ce que je veux résumer toutes les rencontres, ou seulement les personnes uniques?_

Dans cet exemple tiré de l'académie Utilisation du Tracker Niveau 1, nous comptons les cas avec des conditions sous-jacentes dans un programme de vaccination Covid-19. L'élément de données "COVAC - Conditions sous-jacentes" se trouve dans une étape répétable du programme.


![](resources/images/image25.png "Data element for underlying condition"){ .largeur du centre=70% }


Nous créons deux indicateurs de programme : l'un est le type d'inscription avec l'agrégation du nombre d'inscriptions, et l'autre est le type d'événement avec l'agrégation du nombre d'événements.

Vous verrez que l'indicateur basé sur les événements indique des valeurs plus élevées car il compte la variable de l'affection sous-jacente pour chaque événement ; cela n'a pas de sens dans ce scénario si vous voulez connaître le nombre total de personnes uniques atteintes d'une affection sous-jacente.


![Inscriptions et événements](resources/images/image38.png){ .largeur du centre=80% }


Pourquoi cela ? 

Un même patient peut avoir plusieurs événements avec cette valeur d'élément de données. Ces événements peuvent tous avoir lieu au cours de la même période. En outre, la même personne peut avoir des événements dans différents districts (unités d'organisation). Il existe donc **un risque élevé de double comptage des individus avec le type d'événement IP**.

Par ailleurs, il n'y a qu'une seule date d'affiliation et une seule unité d'organisation affiliée, associées à chaque affiliation.


|  |  |  | 
| ----- | -------- | -------- | 
| ![](resources/images/image40.png "Tracker data dimensions")| ![](resources/images/image15.png "Events")|![](resources/images/image16.png "Enrollments") | 


<span style="text-decoration:underline;"> </span>

<span style="text-decoration:underline;">Si vous souhaitez compter des individus uniques, le mode de recrutement est généralement la meilleure approche..</span>

Mais regardez à nouveau l'exemple d'indicateur de programme pour les affections sous-jacentes. Il est possible d'avoir un recrutement avec deux réponses distinctes à cette question. Il se peut qu'une affection sous-jacente n'ait pas été signalée lors de la visite initiale et que la valeur soit différente lors d'une visite ultérieure. Comment un indicateur de programme de type recrutement pourrait-il gérer des valeurs multiples pour un élément de données au cours d'une même étape du programme ?

Dans une étape du programme qui comporte des événements répétés, les indicateurs de type de recrutement utilisent les données **de l'événement le plus récent qui comporte une valeur pour cet élément de données.** Dans le diagramme ci-dessous, les recrutements ne sont pas comptabilisés s'ils ne comportent aucun événement pour l'étape du programme dans le filtre, et seuls les événements comportant une valeur pour l'élément de données sont évalués.

Il est généralement intéressant de ne prendre en compte que la valeur la plus récente pour chaque cas, car cette valeur peut être considérée comme plus prompte et plus précise. Mais dans certains cas, vous souhaiteriez évaluer tous les recrutements qui ont _jamais_ eu une certaine valeur pour un élément de données. C'est là que les fonctions de la classe **`d2:count`** sont utiles dans le filtre de l'IP. Elles garantissent que l'indicateur de programme évalue tous les événements de chaque recrutement et compte le nombre de ceux qui répondent aux critères.

En utilisant ces fonctions dans les filtres d'indicateurs de programmes, vous pouvez répondre à des questions telles que celles-ci :



* `d2:compte(#{jdRD35YwbRH.zocHNQIQBIN})>=1`

_“Combien de patients atteints de tuberculose ont obtenu au moins un résultat à l'examen microscopique par frottis ?"_


* `d2:valeur de compte (countIfValue)(#{jdRD35YwbRH.zocHNQIQBIN},'Positive')>=1`

_“Combien de patients atteints de tuberculose ont obtenu au moins un résultat _positif_ pour un test de microscopie par frottis ”?_


* `d2:countIfCondition(#{edqlbukwRfQ.vANAXwtLwcT},'>8')>=1`

_“Combien de grossesses ont fait l'objet d'au moins une CPN avec une valeur d'hémoglobine supérieure à 8?”_



![Requête IP de base sur le recrutement](resources/images/image14.png "Enrollment"){ .largeur du centre="80%" }



Vous pouvez créer un filtre d'indicateur de programme avec une combinaison d'éléments de données et de valeurs d'attributs d'entités suivies. Avec les indicateurs de recrutement, ces éléments de données peuvent provenir de différentes étapes du programme, et vous pouvez même rechercher une valeur d'élément de données qui répond à certains critères dans tous les événements d'une étape. Cependant, vous ne pouvez pas construire plusieurs sous-expressions dans un filtre `d2:countIfCondition` pour vous assurer que deux valeurs d'éléments de données sont présentes dans le même événement.

Par exemple, vous pouvez filtrer les recrutements pour lesquels un événement a signalé des affections sous-jacentes :

`d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Yes')>=1`

Il est également possible de filtrer les recrutements pour lesquels un événement a fait état d'une grossesse et un événement a fait état d'affections sous-jacentes :

`d2:countIfValue(#{covacprogramUID.pregnancymarkUID},'Yes')>=1  && d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Yes')>=1`

Mais vous NE POUVEZ PAS filtrer qu'une grossesse et des affections sous-jacentes ont été signalées dans le MÊME événement avec des indicateurs de programme de type recrutement. Ce type d'évaluation (deux valeurs dans le même événement) n'est possible qu'avec les indicateurs de programme de type événement.

Enfin, les implémentations à grande échelle doivent tenir compte du fait que _<span style="text-decoration:underline;">lorsque des fonctions de comptage* sont ajoutées au filtre, des problèmes de performance pour l'évaluation de l'indicateur de programme se posent</span>_. Dans le backend, les indicateurs de type inscription rejoignent le tableau analyse_inscription_[programmeUID] avec analyse_événement_[étapeUID] chaque fois que l'indicateur de programme est soumis à une requête. chaque utilisation de count* au cours de cette requête entraînera un balayage distinct de la table des événements et une jonction distincte. La flexibilité de `d2:countIf` est à l'origine de certains des retards les plus importants observés lors du chargement des tableaux de bord.

Les différences entre les deux types d'IP sont décrites dans le tableau ci-dessous.


||Type d'événement|Type de recrutement|
|--- |--- |--- |
|Unité d'organisation dx|Unité d'organisation de l'événement|Unité d'organisation de l'inscription|
|Période dx (par défaut)|Date de l'événement|Date d’inscription|
|Possibilité de filtrage à partir des valeurs TEA|Oui|Oui|
|Possibilité de filtrer plusieurs valeurs en une seule étape non répétable|Oui|Oui|
|Possibilité de filtrage par valeurs multiples dans une étape répétable|Oui|Sélectionne la valeur du dernier événement de l'étape dans la période*|
|Possibilité de filtrage en fonction des valeurs à plusieurs stades du programme|Non|Oui|


 \* Si une fonction `d2:countIfValue` est appliquée, la valeur peut apparaître dans n'importe quel événement d'une étape répétable. Si la fonction est appliquée à plusieurs éléments de données, chacune des valeurs des éléments de données d'une étape répétable peut se présenter, mais au cours d'événements différents.


### Défi commun n° 2 : Périodicité des Indicateurs de Programme{ #common-challenge-2-program-indicator-periodicity }

Toutes les requêtes analytiques requièrent au moins une dimension de période, telle que "la semaine dernière", "janvier 2022" ou "cette année". Cependant, les données du tracker sont longitudinales par nature, et ne sont donc pas liées de manière inhérente à une seule période de base.

Les indicateurs de programme définissent la périodicité d'une requête analytique à l'aide des **_limites de la période analytique_**.

Toutes les dates dérivées des données tracker peuvent être utilisées comme cibles de délimitation pour évaluer les données tracker. Si la valeur de la date spécifiée se situe dans la fourchette établie par ces limites de période, l'affiliation ou l'événement en question est inclus dans la requête.

Deux valeurs par défaut sont automatiquement configurées lorsque vous choisissez le type d'indicateur de programme.



* Par défaut, la date à utiliser comme valeur cible de délimitation est déterminée par le type d'indicateur de programme. L'IP de type recrutement  utilise la date de recrutement comme cible, tandis que l'IP de type événement utilise la date de l'événement.
* Par défaut, les limites de la période sont fixées au début et à la fin de la période de déclaration dans la requête analytique.


![Délimitation de la période de recrutement](resources/images/image18.png "Délimitation de la période de recrutement"){ .largeur du centre="80%" }


Par conséquent, pour _la plupart_ des indicateurs de programme de type événement, la périodicité de l'indicateur de programme est définie comme les dates d'événement tombant dans la période de référence. Pour _la plupart_ des indicateurs de programme de type recrutement, la périodicité de l'indicateur de programme est définie comme les dates de recrutement tombant dans la période de référence.

Les graphiques ci-dessous montrent comment les limites de période par défaut pour le type d'événement et le type de recrutement IP sélectionnent les événements ou les recrutements à évaluer. Si vous placez un indicateur de programme dans un tableau croisé dynamique pour effectuer une requête sur les événements survenus en avril de cette année, les limites par défaut d'un indicateur de programme de type d'événement évalueront tous les événements survenus au cours du mois d'avril de cette année.

|  |  | 
| ----- | -------- |
| ![](resources/images/image26.png "Tracker data dimensions")| ![](resources/images/image16.png "Events")|


Toutefois, ces limites de période par défaut peuvent être adaptées à des besoins analytiques spécifiques.


##### Suppression d'une Délimitation de Période { #removing-a-period-boundary }

Il peut être utile de considérer le premier mot d'un type de limite temporelle, "avant" ou "après", comme des flèches qui pointent vers l'arrière ou vers l'avant dans le temps. Le fait d'avoir deux délimitations avec des directions temporelles opposées ("après le début" et "avant la fin") garantit que les délimitations sont fermées. Si vous supprimez l'un ou l'autre, les limites deviennent indéterminées. Ceci peut être utilisé pour créer un indicateur de programme **_cumulatif_**, comme dans "compter tous les inscrits avant la fin de la période de déclaration". Une requête pour le mois d'avril sélectionnerait alors toutes les inscriptions effectuées avant la fin du mois d'avril.

Il est à noter que ce type d'IP de "comptage cumulatif" doit être utilisé avec précaution en raison de ses implications en termes de performances. Si vous deviez effectuer une requête sur les 12 derniers mois de données avec un IP de comptage cumulatif, une requête cumulative distincte serait effectuée pour chacune de ces périodes mensuelles, au lieu d'additionner les comptages mensuels subséquents (en ajoutant le total du mois 2 à la valeur cumulée du mois 1, en ajoutant le total du mois 3 à la valeur cumulée du mois 2, etc.)


![](resources/images/image41.png "Open enrollment boundary"){ .largeur du centre="80%" }


![Ouverture des limites pour le recrutement](resources/images/image10.png "Ouverture des limites pour le recrutement"){ .largeur du centre="80%" }



##### Ajout et Fusion des Limites de Périodes { #adding-and-mixing-period-boundaries }

En utilisant une IP de type recrutement pour filtrer les valeurs de données de deux ou plusieurs événements, on pense souvent à tort que les limites de la période couvrent la période au cours de laquelle ces événements se sont produits. Or, comme décrit ci-dessus, les limites de la période par défaut ciblent toutes _les dates d'inscription_ au sein de la période. Dans les programmes de gestion de cas où les cas sont généralement actifs pendant une longue période, par exemple un programme de suivi des cas de VIH, la plupart des dates d'inscription peuvent en fait se situer de nombreux mois ou années avant la période visée.

Dans de tels scénarios, vous pouvez basculer la cible de délimitation d'une IP de type recrutement sur la date de l'événement. Toutes les affiliations avec au moins un événement tombant dans la période de déclaration sont alors évaluées.


![](resources/images/image18.png "Mixed period boundaries"){ .largeur du centre="80%" }

![Délimitations de périodes fusionnés ](resources/images/image13.png "Délimitations de périodes fusionnés "){ .largeur du centre="80%" }


Tout comme il est possible de modifier ou de supprimer des délimitations de périodes, il est également possible de superposer plusieurs types de délimitations de périodes afin de restreindre davantage la périodicité.

Par exemple, vous pouvez avoir une IP de type recrutement qui limite son évaluation aux dates d'événement comprises dans la période, et aux dates du recrutement antérieures à la date de début de la période. Ceci garantit que tous les événements exploités sont des "suivis", puisque le recrutement a été ouvert pour la première fois au cours d'une période précédente.

> **Astuce**
>
> Si vous incluez une valeur d'élément de données dans le filtre, l'IP effectuera une requête sur la valeur d'élément de données dans le dernier événement de suivi de ce mois. Si cette valeur d'élément de données est incorporée dans une fonction `d2:countIfValue()`, la requête de l'IP recherchera les valeurs d'élément de données de tous les événements suivis de ce mois.


![](resources/images/image12.png){ .largeur du centre="80%" }

![Délimitation des événements sur l'IP du recrutement](resources/images/image9.png "Délimitation des événements sur l'IP du recrutement"){ .largeur du centre="80%" }


Si la cible délimitée doit être limitée aux événements d'une étape spécifique, vous pouvez sélectionner la cible délimitée "Personnalisée" et saisir le texte `PS_EVENTDATE:{programStageUid}`

La cible de délimitation personnalisée peut également être un attribut d'entité suivie ou un élément de données de type date, par exemple un TEIA de date de naissance, ou une valeur d'élément de données pour la "date de résultat d'un test de laboratoire". Voir le [Guide de l'utilisateur](#about_program_indicators) pour plus d'exemples de cibles de délimitation personnalisées et d'éléments de données supplémentaires.


##### Décalage de la Délimitation de la Période{ #period-boundary-offsets }

Dans la plupart des scénarios, la période de la requête analytique est la période pendant laquelle les événements ou les enrôlements doivent avoir lieu. Dans quelques cas très spécifiques d'utilisation de l'analyse longitudinale, l'indicateur de programme doit évaluer les données de suivi d'une certaine période avant (ou après) la période de rapport. On parle alors de **cohortes**, et elles peuvent être utiles dans divers contextes :



* Abandons : évaluation des recrutements pour lesquels des événements devaient se produire au cours de la période de déclaration, mais qui n'ont pas eu lieu.
* Intervalles entre les événements attendus qui ne correspondent pas à l'intervalle de la période de déclaration :
    * Un test de laboratoire doit être effectué 6 semaines après une hospitalisation.
    * La visite de routine pour la prise en charge de l'hypertension doit avoir lieu toutes les 5 semaines, et vous voulez savoir combien de personnes ont contrôlé leur tension artérielle lors de leur dernière visite au cours des trois mois précédents.
* Gestion du programme : une cohorte VIH dénombre les patients qui ont suivi un traitement antirétroviral pendant six mois précis au cours de la période, et combien d'entre eux ont subi un test de charge virale.

Lors de la définition des limites d'une période, deux valeurs facultatives - Décaler la période selon un montant et Type de période - définissent la manière de déplacer ("décaler") les limites de la période par rapport à la période de déclaration.

Dans l'exemple ci-dessous, les limites de la période analytique pour une PI de type inscription  sont décalées d'un mois. Le type de période de décalage est Mensuel et la période de Décalage par nombre est -1.

C'est ainsi que nous créons une **_cohorte_** avec notre indicateur de programme en déplaçant la fenêtre d'analyse pour examiner les données du tracker d'une période antérieure, par rapport à la période d'analyse.

> **Important**
>
> Les décalages de période avec des valeurs négatives repositionneront la cible _en arrière_ dans le temps. Les limites de décalage positives sont plus rares dans la pratique, puisqu'elles évaluent les données du tracker _après_ la fin de la période de déclaration. Il s'agit d'un scénario peu probable pour l'"analyse en temps réel" dans les cas d'utilisation courants du HIS.


![](resources/images/image3.png "Period offset example"){ .largeur du centre="80%" }

![Décalage de période](resources/images/image24.png "Exemple de décalage de période"){ .largeur du centre="80%" }


Il est important de noter dans cet exemple que la date limite pour l'inscription a simplement été déplacée à exactement un mois avant l'ouverture de la période d'analyse et qu'elle se termine un mois avant la clôture de la période de déclaration.


* Une requête pour le mois de Mai montre le nombre d'inscriptions enregistrés pour le mois d'avril.
* Une requête annuelle pour l'année 2022 évaluerait en fait tous les enregistrements du 1er décembre 2021 au 30 novembre 2022.
* Une requête hebdomadaire pour la semaine 18 2023 (du 1er -7 mai) serait également décalée d'un mois et évaluerait toutes les inscriptions du 1er -7 avril 2023.

Pour développer l'indicateur de programme "cohorte", vous pouvez combiner les limites de période de la date d'inscription et de la date de l'événement comme dans la section précédente, mais en utilisant le décalage de période de manière efficace.

Dans cet exemple, nous voulons compter les inscriptions qui ont été créées au cours du mois précédent mais qui ont eu au moins un événement au cours du mois de déclaration actuel. Cela peut être utile pour décrire le suivi des cas : combien de nouveaux cas dans votre programme ont fait l'objet d'une visite de suivi dans un délai d'un mois ?


![](resources/images/image23.png "Cohort type PI"){ .largeur du centre="80%" }


![IP de cohorte avec délimitation de périodes mixtes](resources/images/image20.png "Indicateur de programme de type cohorte"){ .largeur du centre="80%" }


_Cohorte à fenêtre fixe ou cohorte à fenêtre relative?_

Notez que nous avons encore défini des décalages de période _à la fois_ sur les limites de la période d'ouverture et de la période de fermeture pour la date d'inscription. Ici, la "fenêtre" pour notre cohorte est constituée de toutes les inscriptions effectuées entre un mois avant l'ouverture de la période d'analyse et un mois avant la clôture de la période d'analyse. Cette fenêtre de cohorte est donc **_dépendante de la durée de la période d'analyse_**.

Si les utilisateurs finaux choisissent une période d'analyse hebdomadaire, la fenêtre de cohorte sera d'une semaine, tandis que s'ils choisissent une période d'analyse annuelle, la fenêtre de cohorte sera d'un an, et ainsi de suite.

Cela n'est pas idéal pour beaucoup de situations d'analyse de cohortes, où une durée fixe de la fenêtre de la cohorte est élémentaire dans la définition de l'indicateur du programme lui-même. Vous souhaitez, par exemple, déterminer le nombre de patients souffrant d'hypertension qui ont bénéficié d'une visite de suivi dans les 90 jours suivant leur inscription. Ou alors, vous souhaitez définir une fenêtre de cohorte mensuelle comme ci-dessus, mais calculer le nombre mensuel moyen de cas dans cette cohorte mensuelle sur une année.

Une option consiste à utiliser une cohorte flexible de "fenêtre relative", mais à indiquer dans le nom ou la description de l'indicateur de programme qu'elle ne doit être utilisée qu'avec des types de périodes spécifiques, par exemple mensuelles. Toutefois, cette option risque de donner lieu à des interprétations erronées.

Si votre indicateur de programme spécifie une fenêtre fixe pour la cohorte, il est <span style="text-decoration:underline;">préférable de baser l'ouverture et la fermeture des limites de la période de la cohorte sur un **seul** point</span>, tel que le début de la période analytique. Cette approche garantit une durée fixe de la fenêtre de la cohorte, quelle que soit la période visée.

Dans l'exemple ci-dessous, une cohorte d'inscription mensuelle est générée, même si la période de déclaration est hebdomadaire. On pourrait imaginer l'ajout de limites ciblant la date de l'événement, pour répondre à la question suivante : "combien de cas inscrits le mois précédent ont eu une visite de suivi au cours de la semaine actuelle ?"


![](resources/images/image35.png "Enrollment offset"){ .largeur du centre="80%" }


![Longueur fixe du décalage d'inscription](resources/images/image33.png "Décalage d'inscription"){ .largeur du centre="80%" }


Notez que la durée de la cohorte étant un élément fixe et essentiel de la définition de l'indicateur de programme, vous devrez créer un nouvel indicateur de programme pour chaque durée fixe de la cohorte nécessaire (cohorte mensuelle, cohorte hebdomadaire, etc).


### Défi commun 3 : Transferts et Propriété{ #common-challenge-3-transfers-and-ownership }

Les sections précédentes sur l'analyse des trackers ont examiné les complexités qui découlent des données longitudinales épisodiques à travers une seule dimension : le temps. Une autre dimension essentielle est la **localisation**. Comme nous l'avons vu plus haut, l'unité d'organisation est la première composante analysée lors du calcul d'un indicateur de programme. Dès lors, comment déterminer le "lieu" d'une inscription lorsque les événements qui y sont associés ont en fait eu lieu dans plusieurs unités d'organisation distinctes ?


Dans les systèmes de santé, les patients se déplacent souvent d'un établissement de santé à l'autre pour bénéficier de services pour la même pathologie. Ils peuvent être diagnostiqués dans un centre de santé primaire, puis transférés dans une clinique spécialisée pour le traitement. Les résultats de leurs tests peuvent être saisis par un technicien de laboratoire dans un autre lieu. Un agent de santé communautaire peut effectuer une visite à domicile après le début du traitement.

> :mag : **Cas pratiques par pays**
>
> Selon le contexte, les déplacements de patients peuvent être très fréquents. [Dans un essai du Tracker DHIS2 pour les soins prénatals au Bangladesh](https://www.researchprotocols.org/2021/7/e26918) for example, pregnancy registrations and follow up treatment could be provided both by community health workers and public rural health clinics, all sharing the same patient health record on a Tracker program with Open access. Out of about [14,000 total registrations](https://iambodo.github.io/projects/tutorials/ereg_migration_viz_types.html), 81 % des patients ont eu au moins une visite de suivi après l'enregistrement initial ; sur les 7750 visites de suivi, environ 8 % ont eu lieu dans une unité d'organisation différente de celle où l'enregistrement a eu lieu. Cela signifie que différents établissements publics - et même différents _types_ d'établissements - ont fourni des services à la même personne.

Dans le Tracker du DHIS2, plusieurs unités d'organisation peuvent saisir des données d'événement pour la même inscription. Il existe trois façons différentes pour le deuxième établissement ("unité d'organisation B") d'accéder à un enregistrement d'inscription créé dans un autre établissement ("unité d'organisation A") et de créer un nouvel événement.



* Le patient effectue une **visite spontanée** à l'Unité d'Organisation B. Cela suppose que le champ de recherche de l'utilisateur autorise l'accès à la TEI enregistrée dans l'Unité d'Organisation A. Cela suppose également que le niveau d'accès au programme est soit Ouvert, soit Audité, soit Protégé. (Voir [Docs](l#webapi_nti_access_level) pour une explication des différents paramètres d'accès au programme).
* L'utilisateur de l'unité d'organisation A fait une **référence unique** à l'unité d'organisation B. Le programme peut avoir n'importe quel niveau d'accès pour permettre cela, mais l'unité d'organisation B devra se voir attribuer le programme. Les utilisateurs de l'unité d'organisation B ne pourront saisir des données que pour un seul événement au cours de l'étape spécifiée du programme, et ils ne pourront pas modifier les événements précédents.
* L'utilisateur de l'unité d'organisation A effectue un **transfert permanent** vers l'unité d'organisation B. Le programme peut avoir n'importe quel niveau d'accès pour permettre cela, mais l'unité d'organisation B devra se voir attribuer le programme. Cette procédure diffère de celle de l'orientation ponctuelle, car l'unité d'organisation B aura accès à toutes les étapes du programme pour l'inscription, qui seront également accessibles à l'unité d'organisation B dans les listes de travail et par le biais d'une recherche. Après ce transfert, on peut dire que cette inscription "appartient" à l'unité d'organisation B, car la propriété a été conférée.

Vous trouverez des informations sur l'utilisation des fonctions de renvoi unique et de transfert permanent dans l'application Tracker Capture dans le guide de l'utilisateur. Les flux de travail de transfert et de renvoi sont actuellement en cours de conception pour l'application Capture.

Schématisons la manière dont les indicateurs de programme gèrent les inscriptions avec des événements provenant de différentes unités d'organisation. Dans les exemples ci-dessous, un **transfert permanent** est effectué de l'unité d'organisation A vers l'unité d'organisation B.


![Transfert définitif de propriété](resources/images/image6.png "Transfert de propriété de A à B pendant la période"){ .largeur du centre="80%" }


En règle générale, un indicateur de programme de type événement déterminera simplement sa dimension "Où" en fonction des événements qui ont eu lieu dans chaque unité d'organisation. De même, un indicateur de programme de type inscription sera évalué sur la base des unités d'organisation dans lesquelles les utilisateurs ont créé chaque inscription à l'origine.


|  |  | 
| ----- | -------- |
| ![](resources/images/image32.png "Transfers and event PI")| ![](resources/images/image27.png "Transfers and enrollment PI")|

Lorsque des transferts ont lieu, il est difficile de répondre avec précision à l'aide de l'IP à certains types de requêtes, telles que les suivantes :


* Au total, combien de **patients uniques** ont été reçus dans l'unité d'organisation A et dans l'unité d'organisation B au cours du mois d'avril ?
    * Problématique : un événement de type IP avec une expression V{enrollment_count} compterait toutes les inscriptions uniques qui ont eu au moins un événement dans l'unité d'organisation A et l'unité d'organisation B. Mais lors de l'agrégation à un niveau supérieur, cela compterait deux fois le patient transféré, qui a eu des événements dans les deux unités d'organisation au cours de la même période.
* En supposant qu'au moins une visite ait lieu chaque mois, à combien de patients l'unité d'organisation B doit-elle s'attendre en mai ?
    * Problématique : l'IP pourrait compter toutes les inscriptions effectuées dans l'unité d'organisation B avant le début du mois de mai, mais cela n'inclurait pas le transfert en provenance de l'unité d'organisation A, qui devrait être prévu en mai.
* Pour toutes les inscriptions effectuées auprès de l'unité organisationnelle A en mars, combien de visites de suivi ont été effectuées en avril ?
    * Problématique : il serait possible de construire un type d'événement IP avec des limites de période analytique personnalisées pour trouver les inscriptions effectuées avant le mois de mars et les événements effectués au mois d'avril. Toutefois, avec le type d'événement IP, les deux événements après le transfert vers l'unité d'organisation B ne seraient pas comptabilisés pour l'unité d'organisation A.

Dans certains programmes de lutte contre des maladies chroniques de longue durée, une inscription peut rester ouverte pendant longtemps et un même patient peut être transféré plusieurs fois. La question fondamentale devient plus évidente lorsque l'on travaille avec l'IP de type inscription pour analyser les données sur plusieurs événements à différents intervalles, tels qu'un événement d'inscription avec une visite de suivi au moment opportun.

Dans cet exemple simple, nous voulons savoir combien de patients se sont inscrits au cours du mois précédent, mais ont également eu une visite de suivi (événement) au cours de la période de déclaration. Comment devons-nous classer les patients qui ont été transférés pendant ou dans la période de déclaration ? Est-il plus important de savoir où ils ont été inscrits ou de connaître le lieu de leur dernière visite ?



![](resources/images/image23.png ){ .largeur du centre="80%"  }


![Enrôlement de type IP dans lequel les événements et les enrôlements se produisent dans différentes unités d'organisation.](resources/images/image19.png "Inscription le mois précédent, événement de suivi au cours de la période de déclaration"){ .largeur du centre="80%" }


Mais ici, _seule l'unité d'organisation de l'inscription peut être utilisée_. Cela pourrait avoir de graves conséquences pour les grandes implémentations telles que les systèmes de suivi du VIH ou de la nutrition infantile, où les patients peuvent être inscrits pendant plusieurs années et être transférés à plusieurs reprises. Lorsque les patients ont été transférés, l'unité d'organisation de l'inscription donne une image erronée de l'unité d'organisation qui était réellement responsable de la fourniture des services et la saisie des données. La plupart des gestionnaires de programmes souhaiteraient plutôt contrôler le statut des patients en fonction du dernier endroit où ils ont reçu des services, et non du lieu où les patients se sont inscrits plusieurs années auparavant.


##### Analyse de la propriété (v2.40 et plus)  { #ownership-analytics-v240-and-above } 

À partir de la version 2.40 du DHIS2, le "champ de l'unité d'organisation" pour le calcul de l'IP est disponible dans l'application Maintenance ( qui se trouve au-dessus des paramètres des limites de la période d'analyse pour chaque IP). Cette fonctionnalité offre aux concepteurs de systèmes une plus grande flexibilité pour configurer la dimension de l'unité d'organisation du calcul de l'IP, et résout les problèmes identifiés ci-dessus.

Il existe désormais plusieurs options pour attribuer l'unité d'organisation utilisée pour le calcul de l'IP.

* Unité d'organisation de l'événement (valeur par défaut pour l'événement de type IP, non disponible pour l'inscription de type IP)
* Unité d'organisation d'inscription (valeur par défaut pour l'inscription de type IP)
* Unité d'organisation de l'enregistrement (où la TEI a été créée)
* Unité d'organisation propriétaire au début de la période de déclaration
* Unité d'organisation propriétaire à la fin de la période de déclaration

Les deux dernières options permettent aux concepteurs de configurer le mode de détermination de la dimension de l'unité d'organisation de l'IP : le lieu avant _ou après_ qu'un transfert soit effectué au cours de la période de déclaration.

Revenons à l'exemple précédent. Nous voulons voir les patients qui se sont inscrits au cours du mois précédent et qui ont eu au moins un événement au cours de la période de déclaration. Ici, nous sélectionnons "**Owner at end organisation unit**(Propriétaire de l'unité d'organisation finale)" comme **champ de l'unité d'organisation**.


![](resources/images/image8.png){ .largeur du centre="80%" }


![Le champ de l'unité d'organisation est propriétaire à la fin de la période de déclaration](resources/images/image37.png "Inscription du type IP avec le champ de l'unité d'organisation"){ .largeur du centre="80%" }


Que se passe-t-il ? Les deux inscriptions transférées de l'unité d'organisation A sont désormais comptées pour l'unité d'organisation B. En effet, elles appartenaient à l'unité d'organisation B à la fin de la période de déclaration faisant l'objet de la requête.

Pour en revenir aux défis précédents, une utilisation intelligente de l'analyse de la propriété pourrait s'avérer déterminante pour leur résolution.


* Au total, combien de **patients uniques** ont été reçus dans l'unité d'organisation A et dans l'unité d'organisation B au cours du mois d'avril ?
    * _Problématique : un événement de type IP avec une expression V{enrollment_count} compterait toutes les inscriptions uniques qui ont eu au moins un événement dans l'unité d'organisation A et l'unité d'organisation B. Mais lors de l'agrégation à un niveau supérieur, cela compterait deux fois le patient transféré, qui a eu des événements dans les deux unités d'organisation au cours de la même période._
    * Réponse : Une inscription de type IP avec une expression V{enrollment_count}, et des limites de période cible d'événement au début et à la fin du mois. Le champ de l'unité d'organisation est "propriétaire à la fin du mois", les inscriptions transférées sont comptabilisées pour l'unité d'organisation A et non pour l'unité d'organisation B.
* En supposant que les patients aient au moins une visite par mois, à combien de patients l'unité d'organisation B doit-elle s'attendre en Mai ?
    * _Problématique : l'IP pourrait compter toutes les inscriptions effectuées dans l'unité d'organisation B avant le début du mois de mai, mais cela n'inclurait pas le transfert en provenance de l'unité d'organisation A, qui devrait être prévu en Mai._
    * Réponse : Une inscription de type IP avec une expression V{enrollment_count} et des limites de période cible d'inscription avant le début du mois. Le champ de l'unité d'organisation est "propriétaire au début de la période de déclaration", et les inscriptions transférées sont comptabilisées pour l'unité d'organisation B.
* Pour toutes les inscriptions effectuées auprès de l'unité organisationnelle A en mars, combien de visites de suivi ont été effectuées en avril ?
    * _Problématique : il serait possible de construire un type d'événement IP avec des limites de période analytique personnalisées pour trouver les inscriptions effectuées avant le mois de mars et les événements effectués au mois d'avril. Toutefois, avec le type d'événement IP, les deux événements après le transfert vers l'unité d'organisation B ne seraient pas comptabilisés pour l'unité d'organisation A._
    * Réponse : Un événement de type IP avec une expression V{event_count}, des limites de période cible d'inscription avec un décalage de période pour couvrir le mois précédent, et des limites de période cible d'événement pour saisir tous les événements au cours de la période de déclaration. Vous pouvez ensuite décider de comment traiter les transferts effectués au cours de la période de déclaration. Si le champ de l'unité d'organisation est "propriétaire au début de la période de déclaration", les deux événements de l'unité d'organisation B, créés après le transfert de propriété, seront toujours comptabilisés pour l'unité d'organisation A.

Plusieurs précautions doivent être prises lors de l'utilisation de l'unité d'organisation de la propriété dans les analyses.



* Même en cas de décalage des limites de la période d'analyse qui fait avancer ou reculer la fenêtre d'analyse dans le temps, la dimension de l'unité d'organisation reste le propriétaire au **début ou à la fin de la période de déclaration**.
* Si plusieurs périodes sont combinées dans une telle requête, il convient d'utiliser le propriétaire au début de la première période ou le propriétaire à la fin de la dernière période. Ainsi, bien que "Mois cette année" et "Cette année" couvrent la même période, "Mois cette année" affichera 12 périodes et calculera la propriété à la fin de chaque mois séparément, tandis que "Cette année" affichera une seule période et examinera uniquement la propriété à la fin de l'année.
* Les renvois ne confèrent pas la propriété de l'inscription et de ses événements. Lorsque des renvois sont effectués, seule l'unité d'organisation "renvoyée" en est propriétaire à des fins d'analyse.
* Lorsqu'un transfert permanent est effectué dans Capture ou Tracker Capture, la date du transfert de propriété est la **_date actuelle_**. Par conséquent, si le personnel chargé de la saisie des données enregistre des renvois effectués dans le passé ou effectue une saisie rétroactive des anciennes données, l'historique de la propriété doit être mis à jour avec précision dans le backend SQL du DHIS2 par les administrateurs du système.
* Depuis la version 2.40, le nombre total d'orientations et de transferts ne peut pas être calculé à l'aide des indicateurs du programme. Des questions telles que "Combien de patients ont été transférés au cours de cette période ?" et "Combien de patients ont été orientés au total, et parmi eux, combien ont terminé l'événement après leur orientation ?" ont été posées. Bien qu'il soit possible de [trouver cette information grâce aux visualisations SQL] (https://community.dhis2.org/t/calculate-transferred-patients/44892/3) de la table "Ownership history", il n'est pas encore possible de développer un IP pour calculer le nombre d'actions de transfert ou d'orientation à partir de mai 2023. Ce point est en cours d'élaboration pour les prochaines versions du DHIS2.


### Défi commun 4 : Agrégation et Désagrégation{ #common-challenge-4-aggregation-and-disaggregation } 

Dans les sections précédentes, nous avons supposé que la valeur attendue d'un indicateur de programme devait être un nombre de cas ou de rencontres répondant à certaines conditions. Nous allons maintenant voir comment la configuration des indicateurs de programme peut être adaptée pour produire d'autres résultats que le nombre de cas, par exemple des pourcentages ou des moyennes.

Tout d'abord, rappelons que chaque indicateur de programme nécessite une "expression" et un "type d'agrégation", tous deux utilisés pour agréger les valeurs de l'IP. Pour l'IP en tant que nombre de cas, ces expressions sont généralement très simples, comme Expression = V{enrollment_count} et Type d'Aggregation  = Count. Elles peuvent être adaptées à différentes agrégations, telles que "le nombre moyen de vaccins administrés à chaque enfant né l'année dernière".

Ensuite, il est important de se rappeler que les indicateurs de programme peuvent également constituer le numérateur ou le dénominateur d'un indicateur. Ici, vous pouvez relier les saisies de données basées sur le tracker aux valeurs de données agrégées provenant des ensembles de données DHIS2. La plupart des programmes utilisent cette approche dite des "super indicateurs" pour calculer les **_taux de couverture de la population_** d'une intervention, en intégrant les valeurs de la population dans le dénominateur et les valeurs des indicateurs de programme dans le dénominateur. Par exemple, vous pouvez calculer le nombre de nouveau-nés vaccinés au BCG en tant que pourcentage de tous les nouveau-nés nés dans un établissement de santé, où les vaccins BCG administrés sont dérivés d'un programme tracker et le nombre de nouveau-nés est un formulaire HMIS au niveau de l'établissement. Le numérateur et le dénominateur de l'indicateur peuvent inclure des expressions en ligne, et l'indicateur lui-même a un type d'agrégation.

Si un indicateur de programme est inclus dans le numérateur d'un indicateur, quatre propriétés différentes définissent l'agrégation chaque fois que la valeur de l'indicateur est demandée. Ces propriétés sont appliquées dans un ordre spécifique, décrit ci-dessous.

**Propriétés d'agrégation et ordonnance calculée**


|Ordonnance|Fonctionnalité|Niveau d'agrégation appliqué|Exemple|
|--- |--- |--- |--- |
|1|Expression de l'IP|Chaque événement (ou recrutement, selon le type d'IP)|Jours entre la date de naissance et le premier vaccin du BCG|
|2|Type d'agrégation de l'IP|Parmi tous les événements (ou enregistrements) pour chaque période et dimension d'unité d'organisation|Nombre moyen de jours entre la naissance et le vaccin du BCG|
|3|Expressions de l'indicateur (numérateur/dénominateur)|Modifie la valeur de l'IP après le type d'agrégation, si nécessaire, avant de diviser le numérateur par le dénominateur.|Si l'unité d'organisation est en moyenne à plus de 60 jours entre la naissance et le BCG, la valeur est 1, sinon 0.|
|4|Indicateur du Type d'Agrégation|Comment combiner des valeurs de plusieurs unités d'organisation et/ou de plusieurs périodes ?|Nombre total d'unités d'organisation de l'établissement qui fournissent un "TAR tardif" au cours de cette période|


Qu'en est-il de la _désagrégation_ des indicateurs de programme par des caractéristiques importantes de la TEI, telles que l'âge et le sexe du patient ? Contrairement aux indicateurs agrégés, les indicateurs de programme ne permettent pas la désagrégation des données à la volée par combinaison d'options de catégorie. Afin de désagréger un indicateur de programme, un nouvel indicateur de programme doit être créé pour chaque désagrégation requise.

Pour créer une désagrégation, une nouvelle sous-expression est jointe au **filtre** de l'indicateur de programme. Par exemple, le filtre pour les _patients souffrant des affections sous-jacentes_ PI décrit dans la section ci-dessus :

`d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Yes')>=1`

L'ajout d'une désagrégation pour le sexe du patient nécessiterait deux indicateurs de programme supplémentaires filtrant les valeurs d'attributs d'entités suivies, l'un pour les Hommes et l'autre pour les Femmes.

`d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Oui')>=1 && A{sexe}==’Masculin’`

`d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Oui')>=1 && A{sexe}==’Féminin’`

Pour restreindre le filtre en fonction de l'âge, ajoutez une sous-expression pour filtrer le temps écoulé entre la date de naissance et la date de début de la période d'analyse.

`d2:countIfValue(#{covacprogramUID.underlyingcondUID},'Oui')>=1 && d2 yearsBetween(A{dob}, V{analytics_period_start}>=60)`

Ces ajouts peuvent ne pas représenter un défi pour la production d'un petit nombre de désagrégations. Cependant, dans les situations où il existe de nombreuses désagrégations, il est pénible de dupliquer et de modifier manuellement chaque indicateur de programme, et de maintenir les changements à long terme. Par exemple, la désagrégation selon deux sexes et quatre tranches d'âge nécessiterait huit indicateurs de programme différents.

Deux applications DHIS2 personnalisées ont été développées pour automatiser la désagrégation des indicateurs de programme par affections multiples.

 * [Application de désagrégation des indicateurs de programme (crédit : HISP Tanzanie)] (https://github.com/hisptz/program-indicator-disaggregator)

* [Application Program Dataset Connector (crédit : BAO systems)] (https://community.dhis2.org/t/program-dataset-connector-pdac/42988)


> **Astuce**
>
> Si vous utilisez l'application PDAC, vous pouvez appliquer des désagrégations d'un indicateur de programme à des combinaisons de catégories d'un élément de données agrégé. Cela facilite le passage des données de suivi aux données agrégées, ce qui présente un certain nombre d'avantages tels que l'accélération des requêtes analytiques sur les tableaux de bord.


## Implications de l'analyse du Tracker pour l'utilisation des données { #implications-of-tracker-analytics-for-data-use } 

* Les données Tracker sont à la fois longitudinales et réparties géographiquement. Cela signifie que les données d'un TEI unique ne sont pas intrinsèquement liées à une période ou à une unité d'organisation. Les indicateurs de programme définissent comment effectuer des requêtes sur les données tracker en fonction d'une dimension de période et d'une dimension d'unité d'organisation.
* Lors de la conception d'un indicateur de programme pour l'agrégation des données tracker, il est essentiel de définir si vous comptez des rencontres uniques (événements) ou des patients (inscriptions, ou, si l'inscription est répétable, TEI).
* Tous les comptages de patients uniques<span style="text-decoration:underline;"> doivent </span>utiliser l'IP de type inscription, car le type d'événement entraîne un double comptage des patients aux niveaux inférieurs. De même, tous les IP longitudinaux (calculs nécessitant des données provenant de plus d'un événement) <span style="text-decoration:underline;">doivent </span>utiliser l'IP de type inscription. Pour les versions du DHIS2 inférieures à 2.40, les dénombrements de patients et les indicateurs longitudinaux sont liés à l'unité d'organisation où le patient s'est inscrit, qui n'est parfois pas le lieu où les services ont été fournis.
* L'IP de type inscription constitue un moyen puissant de requête de données longitudinales, mais dans les contextes de gestion des patients où l'inscription est susceptible d'être ouverte pour une longue durée, l'ajout d'instructions `d2:countIf()` doit être utilisé avec discrétion. Lorsqu'elles sont calculées à la volée dans les tableaux de bord, ces instructions ralentissent les tableaux de bord et réduisent les performances du système.
* Dans l'IP de type inscription, il est possible de mal interpréter la dimension "où" comme étant l'unité d'organisation de l'événement, plutôt que l'unité d'organisation de l'inscription. Ce point doit être communiqué aux utilisateurs finaux des données dans les tableaux de bord et les formations.
* Lorsque vous développez des IP avec des "limites de période d'analyse" ou des "unités d'organisation" personnalisées, veillez à inclure un texte décrivant ces personnalisations dans le nom et la description de l'IP et de tout indicateur dont il fait partie, ainsi que dans toute visualisation ou tableau de bord présentant ces données, afin d'aider à interpréter le résultat.
* À l'échelle nationale, les IP de type événement sont généralement beaucoup plus rapides à calculer que les IP de type inscription, et potentiellement plus faciles à interpréter pour les utilisateurs finaux. Lorsque vous concevez des indicateurs de programme essentiels pour votre programme, essayez de trouver des moyens d'inclure toutes les données pertinentes du programme dans une seule étape du programme si possible. Les règles de programme permettent une attribution des valeurs des éléments de données d'un événement précédent aux événements suivants ou à une autre étape. En outre, les règles de programme peuvent être utilisées pour ne afficher que des sections spécifiques des étapes du programme en fonction de certaines valeurs de données saisies, ce qui facilite l'inclusion de toutes les données pertinentes dans une seule étape.
* Voir le Guide sur l'Implémentation du Tracker pour plus de leçons tirées des systèmes de vaccination COVID-19 sur la configuration de [L'analyse du tracker à grande échelle] (#analytics-performance).

Une fois que vous avez une idée des attributs des entités suivies, des étapes du programme, des éléments de données et des indicateurs de programme requis, vous devriez être en mesure de dessiner un **système de conception** pour votre système de suivi proposé, en mettant en évidence la méthode de progression d'une inscription individuelle entre chaque étape. Voir la documentation DHIS2 Metadata Package pour des [exemples] (https://docs.dhis2.org/en/topics/metadata/disease-surveillance/acute-febrile-illness/design.html#program-configuration).

Après avoir élaboré un schéma pour votre programme, ou un premier prototype, vous devez examiner les caractéristiques supplémentaires qui faciliteront la saisie des données par l'utilisateur final.

Vous pouvez également examiner ce premier prototype avec les parties prenantes et une sélection d'utilisateurs finaux afin d'obtenir un retour d'information sur la faisabilité de la conception du programme proposé.

