---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/tracker_implementation/introduction.md"
revision_date: '2021-09-20'
tags:
- Implémenter
---

# Introduction { #introduction } 

Tracker est l'application de la plateforme DHIS2 qui permet la saisie et l'utilisation de données individuelles et longitudinales. Les fonctionnalités de Tracker couvrent un large champ de besoins, allant du suivi de la qualité et de la disponibilité des puits d'eau à la collecte de données sur l'assiduité des élèves dans une salle de classe, en passant par la saisie de données sur les patients dans un dossier médical partagé. Pour les besoins de ce guide, de nombreux exemples seront tirés des systèmes de santé, bien que Tracker soit également largement utilisé pour les systèmes d'éducation, les systèmes environnementaux, la logistique, etc.

De nombreux pays et programmes profitent de la disponibilité accrue des réseaux et de la présence généralisée d'appareils mobiles et d'autres matériels pour rapprocher les systèmes d'information du niveau où les données primaires sont générées. Les données individuelles ajoutent de la précision et de la nuance aux ensembles de données saisies dans les systèmes d'information de routine, ce qui permet de réaliser des analyses ad hoc, de modifier les indicateurs dans le temps et d'améliorer la qualité des données. Au-delà de leur utilité pour les rapports et les analyses, les données individuelles peuvent également être utilisées pour éliminer les doublons, doter le personnel de niveau inférieur de meilleurs outils de prise de décision et placer le client au centre du système d'information. En bref, les données individuelles constituent la plus petite unité de données et, en tant que telles, elles peuvent être réutilisées de nombreuses façons pour satisfaire les divers besoins concurrentiels des systèmes d'information nationaux.

Ce guide a pour but d'aider à déterminer si Tracker est adapté à un cas d'utilisation potentiel et de fournir des conseils pratiques pour planifier des implémentations réussies. L'utilisation de Tracker à grande échelle introduit des facteurs supplémentaires qui doivent être pris en compte au-delà de ce qui peut déjà être en place pour une instance DHIS2 agrégée existante. Les possibilités et les avantages potentiels des systèmes d'information augmentent à mesure qu'un système passe des données agrégées → données anonymes suivies → données d'individus identifiables → données de patients en temps réel sur le lieu de soins. Les personnes qui planifient l'implémentation d'un système Tracker doivent reconnaître que les défis à relever s'accroissent au fur et à mesure que les avantages augmentent.

Ce guide d'implémentation fournit des recommandations pour vous aider à :

-  déterminer si Tracker répondra à vos besoins
-  évaluer le degré de préparation de votre établissement à l'introduction de la collecte de données au niveau individuel
-  comprendre en quoi l'implémentation de Tracker diffère de l'agrégat DHIS2
-  répondre aux préoccupations spécifiques des systèmes de données au niveau individuel, notamment en matière du respect de la vie privée et de la sécurité
-  examiner les enseignements tirés et les meilleures pratiques dérivées des cas d'utilisation réels
-  planifier l'introduction de votre (vos) programme(s) Tracker à l'échelle souhaitée
-  mettre en place une infrastructure qui permettra de pérenniser un programme Tracker

Le guide est divisé en deux sections principales :

- **Mon Projet est-il prêt pour le Tracker?** décrit cinq facteurs contextuels importants qu'il faudrait bien comprendre avant de planifier l'implémentation d'un Tracker.

    - L'adhésion et le soutien des institutions
    - Financement
    - Législation et politiques
    - Capacité et compétence
    - Infrastructure

- La rubrique **Élaborer votre (vos) programme(s) Tracker ** fournit des conseils et des recommandations spécifiques pour neuf aspects différents de l'implémentation d'un Tracker.

    - Définition de l'échelle
    - Procédure de conception et de configuration
    - Définition de votre cadre de S&E
    - Saisie de données en temps réel vs. saisie secondaire
    - Mobile vs web
    - Mise en place d'une infrastructure de soutien aux RH
    - Accueil
    - Formation et lancement
    - Relier Tracker à votre système agrégé

Les liens vers les outils de planification spécifiques sont fournis tout au long du document et dans l'annexe.

## À quoi peut servir le Tracker?{ #what-can-tracker-be-used-for } 

Comme le reste de la plateforme DHIS2, Tracker dispose d'un modèle de données générique qui permet à l'utilisateur de le configurer pour de nombreux objectifs différents. À la base, Tracker permet à l'utilisateur de définir un type particulier d'objet (personne, produit, échantillon de laboratoire, zone de captage, etc.) qu'il souhaite suivre dans le temps (une entité suivie), de définir les données qu'il souhaite collecter sur cette entité (attributs, éléments de données), de placer les éléments de données dans un ordre spécifique avec des conditions ou une logique d'accompagnement (étapes du programme, règles du programme) et de déterminer les analyses qui doivent être produites (indicateurs du programme, rapports d'événements, visualisations de données, etc.)

Un exemple de programme Tracker simple pourrait être un programme de collecte d'informations sur les cas de paludisme sur le lieu de soins. L'entité suivie serait une personne, définie par des attributs tels que le prénom, le nom, la date de naissance ou le village. En général, les attributs sont des données sur l'entité suivie (c'est-à-dire la personne) qui devraient raisonnablement rester les mêmes au cours de la période de suivi et sont souvent utilisés pour identifier l'entité (la personne) de manière unique. Le programme devrait contenir des éléments de données tels que les symptômes, les tests effectués et leurs résultats, le traitement administré, etc. Ces éléments de données pourraient comporter des options préconfigurées pour les réponses possibles, telles que les tests disponibles, ou une logique permettant de garantir la qualité des données, telles que les valeurs minimales et maximales possibles pour un élément de données quelconque. Les données collectées seraient visibles par l'utilisateur clinique dans le cadre du dossier médical partagé du patient atteint de paludisme, mais pourraient également être utilisées pour générer les rapports mensuels requis par le programme national de contrôle du paludisme, fournir une aide à la décision au clinicien, générer des rappels par SMS au patient pour promouvoir l'adhésion au traitement, ou alimenter un tableau de bord clinique contenant des indicateurs de performance clés. Pour tous ces objectifs, les données n'ont été collectées qu'une seule fois, lors de la visite du patient, mais ont été réutilisées à de nombreuses reprises pour des besoins différents.

Le DHIS2 permet également de collecter des données individuelles sans suivi longitudinal à l'aide des applications Capture et Event. Le suivi non longitudinal (programmes d'événements) sera également mentionné tout au long de cette documentation. Les programmes d'événements suivent généralement le même modèle de données que Tracker, à l'exception de la définition d'une entité suivie, qui n'est pas nécessaire pour le suivi non longitudinal. Un exemple d'un tel programme d'événement pourrait être le rapport des données sur les cas de paludisme figurant sur les listes de diffusion. Les données de la liste des cas saisies par un programme d'événement pourraient contenir les mêmes données individuelles que dans le programme précédent (entité suivie), mais sans relier ces données à une entité suivie (patient) pour un suivi longitudinal dans le temps. Par conséquent, les données ne feraient pas partie d'un dossier médical partagé (ou ne seraient peut-être pas utilisées pour générer des rappels par SMS au patient, ou d'autres fonctions qui reposent sur le suivi d'une entité dans le temps) ; cependant, le programme Event pourrait recueillir des données plus granulaires sur les cas de paludisme qu'un modèle de données agrégées, ce qui améliorerait la capacité d'analyse.

Comme le révèlent les exemples ci-dessus, le suivi et la collecte de données individuelles sont très différents des rapports agrégés traditionnels pour les systèmes d'information sur la gestion de la santé (HMIS). Seule une des utilisations potentielles décrites ci-dessus est possible grâce à la collecte de données agrégées --  celle des rapports mensuels -- alors que les utilisations relatives aux patients-, aux cliniciens- et aux établissements ne sont possibles que grâce à la collecte de données individuelles.

En ce qui concerne les rapports de routine, la collecte de données individuelles permet d'améliorer l'interprétation et l'analyse des données et,  --essentiellement --, de prendre les mesures qui s'imposent. Par exemple, un rapport global peut indiquer que la couverture vaccinale globale est de 80 %, mais ne précise pas si les 20 % restants correspondent à des erreurs de déclaration, à l'exclusion involontaire de certains individus/groupes (en raison de facteurs géographiques ou démographiques) ou à d'autres facteurs. Les chiffres globaux ne permettent pas non plus d'identifier spécifiquement les enfants non vaccinés qui pourraient faire l'objet d'un suivi dans le cadre d'un programme de sensibilisation ciblé. Dans cet exemple, les chiffres globaux répondent à un besoin fondamental des ministères de la santé, celui de rendre compte des progrès accomplis au niveau national par rapport à un indicateur global, mais pas aux besoins des responsables des programmes de vaccination ou des prestataires de services, qui doivent prendre des mesures spécifiques pour améliorer la couverture vaccinale.

L'un des avantages liés à l'utilisation de Tracker en tant que système individuel est sa capacité à s'aligner sur le système agrégé existant DHIS2, qui est déjà utilisé dans la plupart des pays à revenu faible ou intermédiaire en tant que système d'information sur les maladies infectieuses (HMIS) national. Contrairement à un dossier médical électronique (DME) autonome ou à une autre application, Tracker encourage la collecte de données structurées qui peuvent être agrégées et introduites dans le système national d'information sur les ménages, remplaçant ainsi la saisie et l'agrégation de données secondaires par des données de source primaire.

En tant que composante fondamentale de la plateforme DHIS2, Tracker est mis à jour deux fois par an, en même temps que le reste du logiciel DHIS2. Les améliorations apportées au système Tracker proviennent de l'implémentation réelle dans les pays et sont conformes aux recommandations mondiales, , notamment les [Directives de l'OMS sur les interventions numériques pour le renforcement des systèmes de santé] (https://www.who.int/reproductivehealth/publications/digital-interventions-health-system-strengthening/en/). Parmi les dix interventions recommandées, Tracker dispose de fonctionnalités spécifiques pour prendre en charge les éléments suivants :

- Déclaration de naissance
- Déclaration de décès
- Déclaration des stocks et gestion des produits de base
- Communication ciblée avec le client
- Soutien aux décisions du personnel de santé
- Suivi numérique de l'état de santé du client et des services associés au soutien à la prise de décision
- Suivi numérique associé à une aide à la décision et à une communication ciblée avec les clients
- Mise à disposition numérique de contenus de formation et d'éducation pour les professionnels de la santé

Afin de profiter pleinement de ces caractéristiques, il faut que les données collectées soient systématiques et conformes aux normes en vigueur. Dans le domaine des soins de santé, les services de santé primaire et publique qui sont fortement axés sur des lignes directrices et des flux de travail fixes sont particulièrement adaptés aux programmes Tracker. Par exemple, dans le domaine des consultations prénatales(CPN), la plupart des pays disposent de lignes directrices assorties d'algorithmes pour le dépistage et la prise en charge des patients en fonction des résultats des tests, qui peuvent être intégrés dans Tracker afin de suivre un flux de travail clinique de routine, répondant à la fois aux besoins du prestataire de soins et à ceux en matière d'établissement de rapports. Dans des domaines plus complexes des soins de santé, avec des algorithmes de décision moins documentés et moins bien définis (comme dans un hôpital de référence, par exemple), Tracker peut être mieux utilisé pour une simple collecte de données, permettant au clinicien de déterminer la meilleure utilisation des données pour le triage des patients, et permettant aux éléments de données standardisés d'être utilisés pour des rapports supplémentaires ou à d'autres fins.


## Exemples des Cas d'Utilisation de Tracker { #example-tracker-use-cases } 

Tout au long de ce guide, nous ferons référence à des cas d'utilisation pour donner des exemples concrets de principes de planification, de points de décision, d'utilisation de logiciels et de données, d'obstacles et de problèmes courants, et d'enseignements tirés à différents stades du processus de planification et de l'implémentation de Tracker. Un bref résumé introductif de ces cas d'utilisation individuels est fourni ici. Des informations plus détaillées sur certains cas d'utilisation sont disponibles sur le site www.dhis2.org.

### Packages du Tracker pré-configurés { #pre-configured-tracker-packages } 

L'outil [Analysis and use of Health Facility Data toolkit] de l'OMS (https://www.who.int/healthinfo/tools_data_analysis_routine_facility/en/) a permis de créer des programmes Tracker préconfigurés pour couvrir une série de sujets liés à la santé. Ces programmes sont destinés à servir de point de départ aux programmes nationaux, permettant une configuration ultérieure pour s'adapter au contexte local, tout en conservant les normes mondiales en matière d'indicateurs et de pratiques. Ils peuvent être ajoutés aux systèmes DHIS2 existants, ensemble ou séparément. Ces paquets sont accessibles à partir du lien ci-dessus, ainsi que sur le site who.dhis2.org. Les paquets préconfigurés actuels traitent des sujets suivants :

- Effets indésirables de la Vaccination
- Déclaration de naissance, de mortinatalité et de décès pour les CRVS
- Cause du décès (y compris les codes CIM-10 de la liste de mortalité initiale)
- Enquête sur les sites de multiplication du paludisme
- Diagnostic et traitement du paludisme, enquête sur les cas et les ménages
- Enquête sur les foyers de paludisme
- Campagnes de vaccination de masse
- Registre des Vaccinations de routine
- Surveillance des Cas de Tuberculose

D'autres paquets encore en cours de développement sont accessibles à l'adresse suivante : https://who.dhis2.org/documentation/work_in_progress.html.

### Botswana : Programme de Nutrition et de Vaccination { #botswana-nutrition-and-immunization-program } 

Le Botswana a lancé un programme mixte de nutrition et de vaccination qui fournit des services clés aux jeunes enfants bénéficiant d'une assistance nutritionnelle, tout en veillant à ce que les enfants atteignent leurs indicateurs de croissance et reçoivent tous les vaccins. En collaboration avec l'équipe du Botswana, la plateforme Tracker a été améliorée pour produire des z-scores standardisés permettant une évaluation rapide du poids par rapport à la taille, du poids par rapport à l'âge et de la taille par rapport à l'âge.

### Ghana : VIH/TAR et autres modules du eTracker { #ghana-hivart-and-other-etracker-modules } 

Depuis 2012, les services de santé du Ghana ont mené un programme pionnier de déclaration des données au niveau des patients par le biais des programmes DHIS2 Tracker ("eTrackers"). En 2019, ils utilisaient 8 modules eTracker différents. Un excellent exemple est leur eTracker VIH/TAR, qui suit les patients individuels à travers le dépistage et le traitement et facilite l'identification et le suivi des défaillants par le personnel de santé, tout en soutenant le flux de déclaration des données agrégées sur le VIH, en cours au Ghana depuis 2006.

### Palestine : Registre électronique de la Santé Maternelle et Infantile{ #palestine-maternal-and-child-health-eregistry } 

Chaque femme en Palestine se voit attribuer une clinique de soins de santé primaires, et si cette clinique ne fournit pas les services dont elle a besoin, elle est invitée à se rendre dans une clinique de niveau supérieur. Ce système d'orientation nécessite un registre électronique qui contrôle l'accès aux dossiers cliniques des patients, favorise la continuité des soins entre les différents sites de soins de santé, permet la saisie de données à partir de plusieurs points différents et fournit des analyses pour aider à prendre des décisions dans le cadre des directives de soins prénatals en Palestine. Notre collaboration avec la Palestine a débuté en 2014. Le développement et l'implémentation du registre électronique de la santé maternelle et infantile (SMI) ont inclus une approche itérative et un dialogue dynamique entre les développeurs, les décideurs politiques, les responsables de la santé publique et les prestataires de soins de santé. Cette implémentation se caractérise par une utilisation intensive de messages SMS automatisés pour communiquer avec les patients, ainsi que de tableaux de bord d'amélioration de la qualité pour mesurer la performance des cliniques et soutenir la prestation de soins de qualité.

### Zimbabwe : Programme National de Lutte contre le Paludisme{ #zimbabwe-national-malaria-control-program } 

L'implémentation du DHIS2 Android Tracker au Zimbabwe a commencé en 2014 en tant que projet de collaboration entre le Programme national de lutte contre le paludisme ( PNLP ) et l'Université d'Oslo, et a depuis été étendu pour couvrir près de la moitié des plus de 60 districts du pays. Cette implémentation comprend la collecte de données hors ligne, des données de localisation détaillées, ainsi que la collecte et l'analyse de données en temps quasi réel. Il s'agit d'un exemple de collaboration avec de multiples parties prenantes au niveau mondial pour développer un programme susceptible d'être étendu à d'autres régions géographiques et à d'autres types de maladies.

