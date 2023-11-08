---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/program-stages-structure.md"
revision_date: '2023-05-24'
tags:
- Implémentation
---

# Structure des étapes du programme { #program-stages-structure }


![](resources/images/image2.png "Step3")


Après avoir décidé quels identifiants personnels seront utilisés, vous êtes prêt à dessiner la structure générale de votre programme en définissant les **étapes du programme.**


Les programmes Tracker peuvent avoir une ou plusieurs étapes. Chaque étape définit un type d'événement spécifique au sein du programme, notamment les données à collecter, l'ordre de collecte, les validations de données ou la logique d'interaction (règles du programme). Si vous procédez par analogie avec les formulaires papier, vous pouvez considérer chaque étape du programme comme un formulaire spécifique dans le dossier du patient. Pour chaque type de rendez-vous avec un patient, qu'il s'agisse d'une consultation diagnostique ou d'un suivi de routine, le prestataire de soins doit remplir un formulaire particulier avec des questions prédéfinies.


Par exemple, un simple programme de « traitement de maladie » peut avoir une première étape consacrée au rapport de cas, suivie d'une étape de traitement, d'une étape de laboratoire et d'une étape de résultat.


![Programme de maladie simple](resources/images/simple_program.jpg ""){ .center width=70% }

Dans l'application de Saisie Tracker, cette conception des étapes de programme se présenterait comme suit :


![](resources/images/simple_program_TC.png ""){ .center width=80% }


À ce stade, trois caractéristiques importantes des étapes du programme doivent être prises en compte :

* **Contenu** : quelles sont les questions posées à chaque étape et comment doivent-elles être organisées ?
* **Fréquence** : certaines étapes peuvent-elles être exécutées plusieurs fois ?
* **Séquençage** : les étapes du programme doivent-elles être introduites dans un ordre précis et avec un certain intervalle de temps entre elles ?


## Contenu : Éléments de données et sections { #content-data-elements-and-sections }

Une étape de programme est essentiellement composée d'éléments de données et d'un formulaire de saisie de données.

La première étape de la création et de la dénomination d'une étape de programme consiste à lui attribuer des éléments de données. Voir **_Séquençage_** ci-dessous pour plus d'informations sur la saisie des détails des étapes de programme. S'il vous faut d'abord créer des éléments de données dans le domaine du tracker, référez-vous au guide utilisateur. Lors de la création des éléments de données, vous verrez qu'il existe plusieurs possibilités pour les **types** de **valeurs** des éléments de données. Vous pouvez également attribuer à l'élément de données un ensemble d'options (c'est-à-dire une liste à sélection multiple).

Voici quelques règles de base que vous pouvez appliquer lors de la création d'**éléments de données du domaine du tracker** :


* Le choix du type de valeur approprié pour votre élément de données est capital. Une fois que vous avez saisi une valeur pour cet élément de données dans un programme, il est difficile de modifier le type de valeur sans perdre les valeurs précédentes. D'autres caractéristiques de l'élément de données, telles que le nom, la description et les valeurs du zéro, peuvent être modifiées une fois que les valeurs sont enregistrées dans la base de données.
* Les types de valeurs les plus couramment utilisés sont : le texte, les valeurs entières et les nombres. Si vous utilisez d'autres types de valeurs plus restrictifs, prenez soin de lire attentivement la documentation et de tester le type de valeur à l'avance, afin de vous assurer que vous en avez réellement besoin.
* En général, pour garantir la qualité des données, l'utilisateur final doit saisir les données au _plus bas niveau d'abstraction_ possible. Par exemple, il est préférable de saisir la tension artérielle sous forme de valeur entière plutôt que sous forme de texte, tel que "TA hypertendue" et "TA normale". La tension artérielle peut être calculé automatiquement dans DHIS2 à partir de la valeur de la tension artérielle du patient, sur la base d'une convention nationale régissant le sujet.
* Si un type de valeur Texte est requis, il est préférable d'avoir un ensemble d'options plutôt qu'un texte libre saisi par l'utilisateur. Cela réduit les erreurs humaines et facilite l'analyse des données résultantes.
* "Type d'agrégation" fait référence à la méthode d'agrégation _par défaut_ lors de la combinaison des valeurs brutes des éléments de données pour tous les événements. Cependant, les indicateurs basés sur le tracker sont le plus souvent calculés à l'aide d'_indicateurs de programme (voir ci-dessous)_ plus flexibles et personnalisables une fois les données déjà saisies. Ne vous inquiétez donc pas si votre type d'agrégation doit être COUNT, NONE ou SUM.
* La plupart des éléments de données qui disposent d'un ensemble d'options utilisent le type de valeur TEXTE, lorsque le type de valeur de l'ensemble d'options est également TEXTE. Si vous utilisez un type de valeur différent pour un élément de données avec un ensemble d'options - par exemple, une liste de valeurs numériques - assurez-vous que l'élément de données et l'ensemble d'options aient le même type de valeur. N'oubliez pas non plus que l'agrégation de l'élément de données sera basée sur le code de l'ensemble d'options, et que ces codes devront donc être conformes au type de valeur choisi.
* Si le type de valeur est TEXTE, le type d'agrégation sera le plus souvent COUNT ou NONE.
* Si le type de valeur est numérique, le type d'agrégation sera le plus souvent COUNT, NONE, SUM ou AVERAGE. D'autres types d'agrégation sont disponibles pour les types de valeurs numériques (l'écart-type par exemple), mais faites des tests au préalable pour évaluer leur utilité.

Lors du choix du type de valeur pour un élément de données, l'une des difficultés souvent rencontrées est la nécessité de sélectionner _plusieurs_ valeurs à partir d'une liste prédéfinie ("Sélection multiple "). Bien que cette fonction soit disponible dans [Agrégation des ensembles de données, à partir de la version 2.40] (https://dhis2.atlassian.net/browse/DHIS2-14481 ?), aucun type de valeur de données spécifique n'est prévu à cet effet dans DHIS2 Tracker. Par conséquent, deux stratégies de conception différentes sont utilisées.



* Si la liste des options est relativement courte (3 à 10) mais que les utilisateurs sont susceptibles de les sélectionner toutes ou aucune, configurez des éléments de données "Oui seulement" (case à cocher) distincts pour chaque option. Vous pouvez inclure une case à cocher "Sélectionner tout" ou une case à cocher "Sélectionner aucun". Cette méthode offre un maximum de possibilités pour la saisie des données, mais en cas d'excès, le formulaire de saisie risque d'être trop long.
* Si la liste des options est relativement longue (10 à 20 ou plus), mais que l'utilisateur n'en sélectionne généralement qu'un nombre limité (1 à 4), vous pouvez créer des éléments de données différents pour "Choix 1", "Choix 2", "Choix 3", etc., chacun avec le même ensemble d'options. Conformément aux règles du programme, le formulaire affiche l'élément de données Choix 2 lorsque le Choix 1 est renseigné, et affiche le Choix 3 lorsque le Choix 2 est renseigné (ci-dessous, vous trouverez plus de détails sur la conception des règles de programme).

Une fois que vous avez sélectionné les éléments de données, vous verrez sept ou huit possibilités de paramètres pour chaque élément. Pour la plupart des configurations de programme, vous ne devrez considérer que la case à cocher **Obligatoire **. Lors de la saisie des données pour l'étape, les utilisateurs ne pourront enregistrer leur événement que si tous les éléments de données obligatoires sont renseignés. En tant que concepteur du programme, vous devez déterminer avec soin si un élément de données est vraiment nécessaire et disponible pour tous les cas. S'il est toujours possible d'avoir une valeur nulle ou inconnue, l'élément de données ne doit pas être obligatoire, au risque d'embrouiller les utilisateurs finaux et d'entraîner une mauvaise qualité des données. Notez que si un élément de données ne peut être obligatoire que sous certaines conditions, il est possible de le configurer par le biais d'une règle de programme.

Pour plus de détails sur les autres paramètres, consultez le [Guide utilisateur](#créer-ou-modifier-un-programme-tracker).



![Sélectionner les éléments de données de l'étape du programme](resources/images/image11.png "Sélectionner les éléments de données de l'étape du programme")


Une fois que vous avez sélectionné le contenu de l'étape du programme, définissez la structure de saisie des données pour cette étape.

Tout comme les programmes d'événements et les ensembles de données, il existe trois types de formulaires de saisie de données dans Tracker :


| Type de formulaire | Description |
|:--|:----|
|Basique|Liste tous les éléments de données qui appartiennent au programme. Vous pouvez modifier l'ordre des éléments de données à tout moment.|
|Section|Une section regroupe les éléments de données dans un ordre spécifique. Vous pouvez ensuite organiser l'ordre des sections pour déterminer à tout moment la présentation souhaitée pour le formulaire de saisie de données.|
|Personnalisé|Définit le formulaire de saisie de données comme une page HTML que vous pouvez personnaliser selon vos besoins. (REMARQUE : cette option est UNIQUEMENT disponible dans l'application de saisie Tracker .)|



Si aucun formulaire personnalisé ou à sections 'est défini, le formulaire basique sera utilisé. Les formulaires basiques sont les plus simples à utiliser car ils sont essentiellement constitués de longues listes contenant tous les éléments de données attribués à l'étape. Cependant, si le nombre d'éléments de données de l'étape devient trop élevé et qu'il faut dérouler le formulaire pour les voir tous, l'utilisateur peut avoir du mal à trouver un élément de données spécifique.

Les sections sont essentiellement des entêtes secondaires dans le formulaire de saisie des données. Étant donné qu'elles regroupent les éléments de données, elles créent une sorte de structure verticale qui facilite la navigation à l'utilisateur final. Voilà pourquoi les **formulaires à sections sont généralement recommandés**. Dans l'application Android, toutes les sections sont réduites par défaut lors de l'ouverture de l'étape ; l'utilisateur doit cliquer sur l'en-tête de la section pour afficher les éléments de données qu'elle contient.

Les formulaires personnalisés offrent un maximum de flexibilité dans la conception dans DHIS2, d'une expérience de saisie de données qui imite les formulaires papier ou d'autres systèmes d'information nationaux, y compris des couleurs personnalisées, des images en ligne et des formats d'affichage. Cependant, la plupart des implémentations devraient éviter les formulaires personnalisés si possible, pour diverses raisons. Ils nécessitent un travail supplémentaire de configuration et de maintenance au fur et à mesure que de nouvelles données sont ajoutées ; ils ne fonctionnent pas dans l'application Android ; leur fonctionnement avec les nouvelles mises à jour du DHIS2 n'a pas été testé ; en cas de dysfonctionnement, ils requièrent l'intervention urgente d'un administrateur de système compétent et qui maîtrise le langage HTML. Les formulaires personnalisés sont prioritaires par rapport aux formulaires à sections, lorsque les deux sont disponibles.

Pour obtenir des informations sur la configuration des formulaires des étapes de programme, veuillez vous référer au [guide utilisateur](#configure_tracker_program_in_Maintenance_app). De plus, des exemples se trouvent dans les démos Play.


## Fréquence : étapes répétables { #frequency-repeatable-stages }

Les étapes de programme peuvent être uniques ou **répétables**. Pourquoi rendre une étape de programme répétable ? Pour les situations où l'étape permet de saisir des données sur un sujet dont le champ d'application est prévisible, mais dont la fréquence est indéfinie. Par exemple, un programme de surveillance du VIH peut avoir une étape répétable pour la visite du patient, parce que la plupart des patients reçoivent un traitement antirétroviral tous les mois. Ils peuvent recevoir ce traitement une, deux, dix fois ou des centaines de fois au cours de leur vie.

Il faut noter qu'une étape répétable peut être générée pour une inscription de façon illimitée. Or sans limite stricte, les utilisateurs finaux peuvent avoir du mal à revenir en arrière et à réviser ou modifier les événements répétés précédemment. Ils peuvent également créer involontairement des événements non nécessaires. Toutefois, les règles du programme peuvent être définies de manière à afficher un message d'avertissement ou un message d'erreur lorsque le nombre d'étapes d'un programme dépasse un certain seuil. Ce processus est décrit dans la communauté de pratique.

Le principal inconvénient de l'utilisation d'étapes répétables provient des analyses du DHIS2, en particulier des indicateurs de programme plus complexes qui utilisent des valeurs d'éléments de données provenant de plusieurs événements. Prenons l'exemple de la "phase de traitement" du programme décrit ci-dessus, et supposons que le traitement se fait généralement en quatre étapes.

Les indicateurs de programme suivants pourraient être envisagés avec une étape de traitement répétable :



* Le nombre moyen d'événements nécessaire au traitement d'un patient
* Nombre de patients inscrits l'année dernière et qui pour leur traitement, ont nécessité plus de cinq événements
* Nombre de patients de plus de 18 ans ayant reçu des médicaments lors de leur dernière visite de traitement
* Nombre de patients de sexe masculin ayant reçu des médicaments au cours d'un ou de plusieurs événements de traitement le mois dernier

Les indicateurs de programme suivants ne seraient PAS possibles avec une étape de traitement répétable, mais le _seraient_ avec des étapes de traitement qui suivent un ordre ordinal et sont distincts (Traitement 1, Traitement 2, etc.).



* Différence moyenne du poids du patient entre le premier et le dernier événement de traitement 
* Nombre de patients ayant reçu des médicaments lors d'une visite de traitement moins de 5 semaines après l'inscription le mois dernier
* Nombre de patients ayant reçu des médicaments lors de deux visites consécutives

D'un point de vue pratique et de maintenance, il est généralement plus simple d'utiliser moins d'étapes de programme. Toutefois, les exigences en matière d'analyse de votre programme doivent être prises en compte avant de finaliser la structure du programme, au cas où les étapes répétables posent problème.


## Séquençage : flux de travail lors des étapes et programmation des événements { #sequencing-stage-workflow-and-scheduling-events }

Observez à nouveau les diagrammes ci-dessus relatifs au cheminement des patients. Vous constaterez qu'il existe un cheminement prévisible pour les données des patients lorsqu'elles passent par un système de collecte de données. Les points d'entrée et de sortie du programme sont bien définis et certaines procédures standard sont exécutées entre les deux points.

Après avoir défini le contenu de chaque étape et déterminé si l'une d'entre elles peut être répétée, vous devez déterminer s'il existe un ordre logique que vos utilisateurs finaux peuvent suivre pour compléter les étapes. Cette logique de saisie des données par séquence doit être clairement définie dans le guide de conception de votre système afin de faciliter la formation des utilisateurs finaux du système Tracker et d'améliorer l'interprétation des analyses de ce système.

À titre d'exemple, le "Programme simple de traitement des maladies" comporte quatre étapes : un rapport initial sur la maladie, le traitement, les tests de laboratoire et les résultats. Lors de l'inscription, les détails du diagnostic sont consignés dans le rapport initial. Si le patient se rétablit, décède ou est perdu de vue, l'information est consignée au niveau des résultats. Le traitement et les tests de laboratoire peuvent être répétés à plusieurs reprises, mais ils doivent être effectués entre l'étape du rapport initial et celle des résultats. En général, les tests de laboratoire et les visites de traitement sont documentés de manière asynchrone par des agents de santé différents, dans un laboratoire et dans une clinique.


![Programme simple de traitement de maladie](resources/images/simple_program.jpg){ .largeur du centre=80% }

Le processus par lequel l'utilisateur final passe du formulaire du rapport de cas initial à celui du traitement et enfin à celui du test de laboratoire doit être examiné plus en détail.



* Un dossier peut-il être ouvert pour le cas avant que le diagnostic ne soit confirmé par un test de laboratoire ?
* Un traitement peut-il être administré avant que le diagnostic ne soit confirmé par un résultat de laboratoire ?
* Les patients doivent-ils recevoir un traitement le même jour où le rapport de cas initial a été établi ?
* Si un test de suivi est requis après un traitement clinique, comment tenir laboratoire informé ?
* Y a-t-il un intervalle recommandé entre les visites de traitement ? Par ex. une fois tous les 30 jours ?

Ces questions nécessitent l'intervention d'un expert en la matière ayant une connaissance approfondie des procédures de gestion des cas et des flux de travail cliniques du système de santé. Si des protocoles stricts doivent être suivis, par exemple un nombre minimum de jours entre les visites de traitement, ils peuvent être renforcés grâce au système DHIS2.

À cette phase de conception, il peut être instructif d'examiner les différents types de dates dans DHIS2 Tracker et leur lien avec le processus de saisie des données.

Ce tableau présente les dates qui peuvent être modifiées par l'utilisateur final lors de la saisie des données. Ils peuvent être modifiés lors de la configuration du programme afin de faciliter la compréhension de ces concepts compte tenu des contextes.


|Date|Description|
|--- |--- |
|Date d’inscription|La date à laquelle la TEI est inscrite au programme|
|Date de l’incident|La date de l'incident à l'origine du premier événement pour la TEI|
|Date du rapport|La date de l'événement à utiliser pour faire le rapport. Il peut s'agir de la date réelle de la rencontre ou de la date à laquelle l'événement a été enregistré dans le système.|
|Date d’échéance|Il s'agit de la date à laquelle l'événement doit se produire. Une date d'échéance future peut être fixée lors de l'inscription ou lors de la saisie des données. Contrairement à la date du rapport, la date de l'événement peut être fixée dans le futur.|

Il y a plus de dates enregistrées pour chaque événement. Voir la liste complète dans [Annexe A](#appendix-a-tracker-dates) ci-dessous.


Aucune méthode par défaut ne permet de définir un ordre strict pour la saisie des données dans une étape de programme dans Tracker. Cependant, quelques approches pratiques permettent d'ordonner les étapes de programme dans le but d'orienter l'utilisateur final.

Tout d'abord, les étapes du programme peuvent être triées lors de la configuration du programme dans l'application de maintenance. Allez dans **(4) Étapes du programme** Cliquez sur n'importe quelle étape dans le menu à trois points "Actions" et vous pourrez déplacer l'étape vers le haut ou vers le bas de la liste. Après avoir cliqué sur "Enregistrer", l'ordre de tri vertical des étapes sera modifié dans l'application de Saisie Tracker, indépendamment du fait que vous ajoutiez de nouvelles étapes de programme avec le widget "Saisie de données tabulaires" ou avec le widget "Saisie de données chronologiques".




![Organiser les étapes dans l'ordre](resources/images/stage_order_select.png){ .largeur du centre=80% }




![L'ordre de tri est affiché dans la liste des étapes du programme lors de l'ajout d'un nouvel événement](resources/images/image34.png "Ordre de tri-nouvel événement"){ .largeur du centre=80% }




![...et l'ordre des étapes dans le widget de saisie de données tabulaires](resources/images/image36.png "Ordre de tri-saisie de données tabulaires"){ .largeur du centre=80% }


Dans certains cas, les implémentations peuvent rendre l'ordre des étapes plus clair avec l'ajout d'un préfixe ordinal à chaque nom d'étape, par exemple, Étape 0 - Accouchements précédents, Étape 1 - Première visite CPN, 2 - Deuxième visite CPN, etc.

Les règles de programme permettent également de faire respecter l'ordre des étapes du programme. Vous remarquez que le programme de CPN ci-dessus a une étape "Visite de soins post-partum" inscrite dans l'application de maintenance, mais que cette étape n'est pas encore visible lors de la saisie des données. Cela est dû au fait qu'il existe une règle de programme qui permet de masquer l'étape des Soins Post-partum à moins qu'une naissance n'ait été enregistrée à l'étape des "Soins à la naissance". Ces règles de programme pourraient être superposées afin d'appliquer une logique séquentielle stricte, de sorte que l'achèvement de l'étape 1 débloque l'étape 2, l'achèvement de l'étape 2 débloque l'étape 3, etc.

Ces méthodes supplémentaires permettent de définir un ordre séquentiel standard pour les étapes de programme.



* **Afficher la première étape sur la page d'enregistrement** permettra d'intégrer la première étape listée sur la page d'enregistrement L'utilisateur devra donc compléter la première étape avant l'inscription d'un patient au programme. Dans l'application de maintenance, ce paramètre est configuré dans la section "Détails du programme", et non dans la section "Détails des étapes du programme".



![Première étape sur la page d'enregistrement](resources/images/image5.png "Page d'enregistrement"){ .largeur du centre=80% }


* **Demander à l'utilisateur de terminer le programme après avoir terminé l'étape**. Ce paramètre d'étape de programme permet de marquer l'étape finale de la séquence, car il amène l'utilisateur à mettre fin à l'inscription une fois l'étape terminée.



!["Êtes-vous sûr de vouloir terminer cet événement et cette inscription ?"](resources/images/image1.png "Demander à l'utilisateur de terminer"){ .largeur du centre=80% }


* **Ouvrir le formulaire de saisie des données après l'inscription** permet à l'utilisateur d'accéder directement au formulaire de saisie des données de l'étape après avoir terminé l'enregistrement. Cela signifie que l'événement sera ouvert par défaut, avec un statut ACTIF. [Ce paramètre](#enregistrement-avec-formulaire-de-saisiie-de-données-ouvert) n'est activé que si ["Générer automatiquement des évènements"](#enregistrement-avec-génération-automatique-d'évènements) est coché.
* **Générer automatiquement des événements (programmés)** après l'inscription. Ce paramètre permet de générer automatiquement un événement programmé pour l'étape un nombre défini de jours après la date d'inscription. Par exemple, l'étape du rapport de cas initial peut s'ouvrir immédiatement après l'inscription, tandis que l'étape du laboratoire est générée automatiquement et programmée pour avoir lieu sept jours après le début du programme. Cela signifie que le rapport de cas initial a lieu avant l'étape du laboratoire. N'utilisez ce paramètre que si le programme respecte une séquence standard d'événements avec un intervalle de temps prévisible entre ces événements.
* **Définir un intervalle pour le prochain événement programmé dans une étape répétable du programme**: Une fois que l'utilisateur a terminé une étape répétable du programme, il peut programmer le prochain événement de l'étape. Le programme propose automatiquement une date d'échéance pour le prochain événement. Il peut s'agir de la date de l'événement le plus récent plus la valeur ["jours d'intervalle standard"](https://community.dhis2.org/t/automatic-scheduling/45961/2), ou d'un élément de données de type date provenant du dernier événement (configurer les règles du programme comme dans l'exemple [ici](https://community.dhis2.org/t/same-report-date-for-2-different-events/46735/6)).
*  **Types de périodes d'événements** Ce paramètre configurable définit un type de période spécifique pour chaque événement de l'étape du programme. Au lieu de sélectionner une date pour l'événement, les utilisateurs finaux sélectionnent une période, telle qu'un jour, une semaine ou un mois. Les utilisateurs ne peuvent pas introduire plus d'un événement pour la période sélectionnée. Voir l'exemple d'un type de période d'événement "quotidien" ici.

Le tableau ci-dessous résume les approches de configuration pour le séquençage des étapes du programme


 <table>
   <tr>
    <td> <strong> Ordre des étapes </strong>
    </td>
    <td> <strong> Contrôle du flux </strong>
    </td>
    <td> <strong> Méthodes de configuration </strong>
    </td>
   </tr>
   <tr>
    <td rowspan="3"> Premier
    </td>
    <td> Directives strictes (l'utilisateur doit s'y conformer)
    </td>
    <td> Afficher la première étape sur la page d'enregistrement
    </td>
   </tr>
   <tr>
    <td> Directives Souples (l'utilisateur peut ne pas s'y conformer)
    </td>
    <td> Ouvrir le formulaire de saisie des données après l'inscription
    </td>
   </tr>
   <tr>
    <td> Directives strictes
    </td>
    <td> Les règles du programme masquent les autres étapes jusqu'à l'achèvement de la première étape
    </td>
   </tr>
   <tr>
    <td rowspan="3"> Milieu
    </td>
    <td> Directives Souples
    </td>
    <td> Orientent l'utilisateur vers l'étape suivante à travers des boîtes d'avertissement, en ajoutant des préfixes aux noms d'étape, etc.
    </td>
   </tr>
   <tr>
    <td> Directives strictes
    </td>
    <td> Règles du programme permettant de signaler une erreur à la fin des étapes lorsqu'elles sont introduites dans un ordre incorrect
    </td>
   </tr>
   <tr>
    <td> Directives Souples
    </td>
    <td> Étapes programmées automatiquement avec des dates d'échéance fixées dans un ordre particulier (l'étape la plus éloignée dans le futur est la « dernière » )
    </td>
   </tr>
   <tr>
    <td rowspan="2"> Dernier
    </td>
    <td> Souple
    </td>
    <td> Le paramètre de l'étape du programme : demande à l'utilisateur de mettre fin au programme après avoir terminé l'étape
    </td>
   </tr>
   <tr>
    <td> Souple/Stricte
    </td>
    <td> La règle de programme : affiche un avertissement demandant à l'utilisateur de mettre fin au programme après avoir saisi les données dans la dernière étape du programme
    </td>
   </tr>
 </table>



## Événements programmés et dates d'échéance { #scheduled-events-and-due-dates }

De la même façon que les patients peuvent avoir des rendez-vous, une personne inscrite à un programme tracker peut être programmée pour un événement. En termes techniques, un événement a le statut `PROGRAMMÉ` s'il a une date d'échéance, et non s'il a une date de rapport. Les événements programmés peuvent aider l'utilisateur final à déterminer l'ordre dans lequel les étapes doivent être introduites lors de la saisie des données. Ils peuvent être visualisés dans l'application Line Listing de DHIS2, et une liste de tâches dans l'application de Saisie peut montrer les rendez-vous à venir ou manqués. De plus, la "date d'échéance" peut être utilisée pour programmer des notifications, telles que des rappels aux patients pour des rendez-vous à venir.

Cependant, la fonctionnalité de programmation d'événements a des limites qui doivent être prises en compte.


* Chaque inscription ne peut avoir qu'un seul événement programmé à la fois pour chaque étape de programme, même si l'étape est répétable.
* La date d'échéance suggérée automatiquement peut être un week-end ou un jour férié. L'utilisateur doit donc confirmer si la date d'échéance est valide avant de programmer l'événement.
* Les utilisateurs peuvent modifier la date d'échéance d'un événement quand ils le souhaitent. Mais ces reprogrammations ne sont pas enregistrées et seule la dernière date d'échéance est disponible. De plus, une fois qu'un événement programmé est ouvert et que le statut de l'événement passe de "programmé" à "actif", vous ne pouvez pas connaître le moment où cette action s'est produite, ni l'utilisateur qui a ouvert le programme. Cela signifie qu'il est difficile d'analyser le suivi des rendez-vous, c'est-à-dire d'estimer le nombre de rendez-vous programmés qui deviennent des visites actives.
* Dans de nombreux cas d'utilisation, une étape du programme ne sera _jamais_ programmé, et donc le concept de "date d'échéance" peut juste prêter à confusion pour les utilisateurs finaux. Dans un tel scénario, vous pouvez envisager de cocher "Masquer la date d'échéance" lors de la configuration des détails de l'étape du programme dans l'application Maintenance.


### Les cycles de vie des événements et des inscriptions { #the-event-and-enrollment-lifecycles }

Chaque événement et inscription a un champ dédié à son statut. Ils peuvent également être marqués comme supprimés (mis en corbeille) ou perdus de vue. S'ils disposent des autorisations appropriées, les utilisateurs finaux peuvent également créer ou supprimer des événements.

Une fois votre tracker déployé, vous souhaiterez peut-être vérifier à quel point les utilisateurs suivent le flux de contrôle prescrit ou enquêter sur les données erronées. Ces champs dédiés au statut des événements et des inscriptions vous aideront à comprendre l'activité des utilisateurs et également à générer des indicateurs de programme appropriés.

**Inscriptions**

* **ACTIF** Utilisé pendant que l'entité suivie participe au programme.
* **TERMINÉ** Utilisé lorsque l'entité suivie termine sa participation au programme.
* **ANNULÉ**. "Désactivé" dans l'interface utilisateur Web. Utilisé lorsque l'entité suivie a annulé sa participation au programme.


**Événements**


* **ACTIF**. Lorsque des événements sont créés avec la fonction « Ajouter nouveau », ils sont immédiatement définis sur ACTIF. Lorsqu'un événement a le statut ACTIF, ses informations peuvent être modifiées. Les événements TERMINÉ peuvent redevenir ACTIF et vice versa.
* **TERMINÉ**. Un événement n'est TERMINÉ que lorsqu'un utilisateur clique sur le bouton Terminer. Si un événement a le statut TERMINÉ, ses informations ne peuvent pas être modifiées. Les événements ACTIF peuvent redevenir TERMINÉ et vice versa.
* **IGNORÉ**. Utilisé pour les événements programmés dont on a plus besoin. Un bouton est dédié à cette fonction dans l'application de Saisie Tracker.
* **PROGRAMMÉ**. Lorsqu'un événement n'a pas de date d'événement (mais qu'il a une date d'échéance), l'événement est enregistré avec le statut PROGRAMMÉ. Lorsque des événements sont créés avec l'onglet "Programmer un événement", ils sont immédiatement définis comme PROGRAMMÉ jusqu'à ce qu'ils aient une date d'événement.
* **EN RETARD**. Si la date d'échéance d'un événement programmé (pas de date d'événement) expire, l'évènement peut être considérer comme EN RETARD.
* **VISITÉ**. (Cette fonction a été retirée depuis la version 2.38. VISITED est passé à ACTIF). Dans l'application de Saisie Tracker, il est possible d'atteindre le niveau VISITÉ en ajoutant un nouvel événement avec une date d'événement, puis en le quittant avant l'introduction des données. Le statut VISITÉ n'est pas visible dans l'interface utilisateur et de toutes les façons, il est traité de la même manière qu'un événement ACTIF.


## Une ou plusieurs étapes ? Regroupement des services sous la forme sections vs étapes { #one-stage-or-multiple-grouping-services-as-sections-vs-stages }

En examinant les éléments décrits ci-dessus, nous constatons que les données peuvent être organisées aussi bien par étapes de programme que par sections à l'intérieur des étapes. Les étapes de programme peuvent être uniques ou répétables. Les règles de programme peuvent être utilisées pour afficher ou masquer certaines étapes ou sections en fonction des valeurs de données précédentes, ce qui crée des flux de contrôle pour la saisie des données dans un ordre défini.

L'une des étapes les plus importantes dans la conception des programmes tracker est donc de comprendre comment utiliser efficacement les étapes et les sections pour mettre ensemble différents éléments de données.

Dans le domaine de la santé, nous pouvons regrouper les éléments de données tracker en ensembles de **"services"** fournis à chaque personne. Ces services pourraient être fournis :


* pendant le même rendez-vous et par le même prestataire
* pendant le même rendez-vous, mais par des prestataires différents
* dans une séquence standard de rendez-vous périodiques
* de manière asynchrone et non structurée, avec des prestations enregistrées lors d'une même rencontre ou de rencontres différentes, par le même prestataire ou des prestataires différents

En règle générale, **_un utilisateur doit pouvoir inscrire tous les services fournis lors d'une même consultation dans la même étape du programme_**. Il n'est pas nécessaire de passer à d'autres étapes, sauf si différents utilisateurs saisissent des données pour des services différents ou si des données supplémentaires ne seront disponibles qu'ultérieurement (par exemple, des résultats de tests, une nouvelle visite du patient, etc.)

Ci-dessous quelques exemples de la manière dont les services d'un même programme peuvent être transformés en étapes ou en sections. Nous reviendrons à l'exemple précédent d'un "programme de traitement" générique avec des étapes pour le rapport de cas, le traitement, le laboratoire et le résultat. Les services de traitement et de laboratoire pourraient-ils être considérés comme faisant partie de la même étape ?



1. **Tous les services principaux dans la même étape répétable "Visite"**
    1. Une telle configuration est idéale lorsque tous les services peuvent être fournis lors d'une même visite et par la même personne
    2. Dans cet exemple, le rapport de cas n'est pas répétable car il ne se produit qu'une seule fois, au moment de l'inscription.
    3. Cet exemple montre également une section "Sélectionner les services" avec des cases à cocher (éléments de données "Oui seulement") et des règles de programme permettant de masquer les autres sections de services à moins que ces services ne soient "cochés". Cela pourrait accélérer le flux de travail de l'utilisateur en lui permettant d'ignorer facilement des sections (services) qui comportent beaucoup de questions.
    4. On peut supposer que le résultat est enregistré en même temps que le résultat d'un traitement ou d'un test de laboratoire. Si une valeur est saisie pour le résultat du cas, une règle de programme demande à l'utilisateur de terminer l'inscription. Les règles de programme peuvent également empêcher l'ouverture de futurs événements de visite pour ce cas.


![](resources/images/image50.png "All core services one repeatable Visit stage"){ .largeur du centre=80% }



2. **Tous les services principaux ont leurs propres étapes non répétables ou répétables**
    1. Il est préférable que les résultats des tests de laboratoire soient saisis à un moment différent du traitement proposé (par des utilisateurs différents ou à des moments différents).
    2. Cependant, les indicateurs de programme entre les étapes de traitement et de résultats de laboratoire sont plus difficiles à déterminer. Par exemple, " Nombre de jours entre un résultat de laboratoire positif et le traitement " ou " A reçu un traitement deux fois ou plus avant de recevoir un résultat de laboratoire positif "
    3. Cet exemple comporte toujours une étape de rapport de cas non répétable qui permet de saisir les informations principales du cas. Certains programmes permettent également d'afficher ou de masquer les événements ultérieurs à une étape en fonction des informations saisies lors de l'inscription ou du rapport de cas initial.
    4. Étant donné que l'étape des résultats de laboratoire et celle du traitement sont distinctes, il en est de même pour l'étape des résultats. Vous pouvez ici configurer le paramètre permettant de terminer le programme après l'achèvement de l'étape.



![](resources/images/image49.png "All core services as their own non-repeatable or repeatable stages"){ .largeur du centre=80% }




3. **Une étape de visite répétable / affichage d'autres étapes si nécessaire**
    1. Comme dans l'exemple 2, les services principaux (traitement et résultats de laboratoire) sont divisés en deux étapes répétables pour des utilisateurs différents. Cependant, les deux étapes peuvent avoir une même liste de questions - par exemple une liste de "vérification rapide" des symptômes du patient pouvant nécessiter des soins d'urgence - avant l'ajout de nouveaux événements à l'une ou l'autre des étapes du service. Cette liste d'éléments de données pourrait constituer l'essentiel des données à saisir à chaque visite, étant donné que les informations sur le traitement et les résultats de laboratoire sont saisis de manière asynchrone par des prestataires différents.
    2. Comme dans l'exemple # 1, cette étape de la visite pourrait inclure des questions sur la "sélection des services", y compris des règles de programme permettant de masquer les étapes suivantes jusqu'à ce que l'étape en cours soit terminée.
    3. Cela permet également de déterminer le nombre réel de "visites" lorsqu'il y a deux ou plusieurs sections répétables. Dans l'exemple #2, les indicateurs de programme pourraient déterminer le nombre total d'événements relatifs au traitement et aux résultats de laboratoire qui se sont produits, mais pas le nombre d'événements qui se sont produits lors d'une même rencontre (c'est-à-dire le même jour).
    4. Si plusieurs conditions du programme et plusieurs résultats de laboratoire sont possibles, il faudra peut-être enregistrer chaque résultat comme un événement distinct.
    5. Autres programmes de prévention, différents prestataires qui offrent des services différents = saisie de données asynchrone




![](resources/images/image39.png "One repeatable Visit stage, show other stages as needed"){ .largeur du centre=80% }




4. **Chaque version d'un service a sa propre étape**
    1. Il n'y a pas d'étapes répétables. Il faut donc partir du principe qu'il y a un nombre maximum de rendez-vous lors de l'inscription (par exemple, un maximum de trois tests de suivi pour chaque personne en contact avec un cas de tuberculose ; les étapes FU 1, FU 2 et FU3 peuvent donc être des étapes distinctes).
NB: FU pour test de suivi (follow-up en anglais)
    2. Dans certains cas d'utilisation, chaque personne peut ou doit faire l'objet de plusieurs consultations dont le nombre est déterminé. Par exemple, une personne suspectée d'avoir contracté la tuberculose doit être examinée EXACTEMENT cinq fois, selon un calendrier fixe entre chaque visite. Dans ce scénario, il serait logique d'avoir une étape distincte non répétable pour chaque niveau de la séquence : Traitement n° 1, Traitement n° 2, Traitement n° 3, etc. Les règles du programme pourraient masquer tous les autres traitements jusqu'à ce que le traitement n° 1 soit terminé ; le traitement n° 3 est masqué jusqu'à ce que le traitement n° 2 soit terminé, et ainsi de suite.
    3. Le principal avantage de cette approche est qu'elle permet de définir des intervalles fixes entre les dates d'échéance de chaque rencontre. Il est également plus facile de filtrer les données des indicateurs du programme d'inscription en fonction du niveau où une valeur d'élément de données spécifique est apparue dans la séquence ("Les cas contact de tuberculose qui commencent le traitement à la visite n° 3").
    4. Cette méthode n'est toutefois pas recommandée, car le système évolue et cela affectera probablement le nombre de rencontres. Et il est difficile de revenir à une étape répétable une fois les données saisies. Les listes de lignes et les indicateurs de programme relatifs aux événements sont plus difficiles à configurer, car ils nécessitent la combinaison de plusieurs étapes. De plus, gérer chaque étape séparément peut s'avérer contraignant, étant donné que des modifications doivent être apportées à chacune de ces étapes. Le personnel chargé de la saisie des données peut également avoir du mal à travailler.

![](resources/images/image44.png "Each iteration of a service has its own stage"){ .largeur du centre=80% }


**Exemple de tracker de prévention du VIH**

Dans ce programme de prévention du VIH en Amérique latine, chaque inscription commence par une étape d'évaluation des risques pour les données de surveillance des cas (tel que le statut principal de la population). Une fois inscrit, chaque rendez-vous devient une "visite" avec plusieurs sections, affichées ou cachées selon les besoins, pour le test VIH, la prophylaxie post-exposition, le suivi de l'évaluation des risques et le dépistage des IST. Si le risque de contracter le VIH est élevé, une autre section est prévue pour la prophylaxie pré-exposition. Si un cas est testé séropositif lors de l'inscription, une boîte d'avertissement suggère qu'il soit inscrit à un programme distinct de surveillance des cas d'infection au VIH.


![Exemple de programme de prévention du VIH](resources/images/image42.png "Exemple de structure de programme")


La conception de l'étape du programme a des implications sur la conception d'analyses appropriées pour la liste des lignes et l'agrégation des données de tracker. Pour les programmes de santé où les utilisateurs ont plusieurs "points de contact" avec le même individu, il peut être plus facile de séparer les flux de travail des utilisateurs en différentes étapes de programme. Cependant, comme nous le verrons, il est généralement plus facile de configurer et d'utiliser les indicateurs de programme lorsque toutes les données sont regroupées dans une seule étape du programme.


## Annexe A : Dates du Tracker { #appendix-a-tracker-dates }

** Liste complète des dates disponibles dans le modèle Tracker **

|Date de Tracker|Visible|Description|
|--- |--- |--- |
|Date de création de la TEI|API|Première instance d'entité suivie (TEI) créée dans la base de données du DHIS2.|
|Date de la dernière mise à jour de la TEI|API|Dernière fois qu'un attribut de la TEI a été mis à jour|
|Date de création de la TEI au niveau du client|API|Date à laquelle la TEI a été générée par l'utilisateur final. Utilisé lors de la synchronisation de la TEI créée sur l'application Android avec la base de données DHIS2.|
|Date de création de l'inscription|API|Première inscription créée dans la base de données du DHIS2.|
|Date de la dernière mise à jour de l'inscription|API|La dernière fois qu'un événement de l'inscription a été mis à jour|
|Date d’inscription|API/UI|La date à laquelle la TEI est inscrite au programme|
|Date de l’incident|API/UI|La date de l'événement qui déclenche le premier événement pour la TEI|
|Date d'achèvement|API|Date à laquelle l'inscription a été marquée comme terminée|
|Date de création de l'événement|API|Premier événement généré dans la base de données DHIS2.|
|Date de la dernière mise à jour de l'événement|API|Dernière fois qu'une valeur de données de l'événement a été mise à jour|
|Date de l'événement|API/UI|La date saisie par l'utilisateur pour indiquer le moment où l'événement se produit|
|Date d’échéance|API/UI|La date prévue pour l'événement, générée à la fin de l'événement précédent, ou générée automatiquement, ou modifiée lorsque l'événement débute.|

