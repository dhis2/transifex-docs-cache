---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/tracker_implementation/building-your-tracker-programs.md"
revision_date: '2023-01-26'
tags:
- Implémentation
---

# Planification de l'implémentation de votre Tracker { #planning-your-tracker-implementation }

L'objectif de cette section est de donner une vue d'ensemble des considérations qui mèneront à la réussite  de l'implémentation de votre Tracker. On note un regroupement par thème et des liens qui mènent vers des outils spécifiques.

Cette section couvrira :

1. Définition de l'objectif, du but et du champ d'application
2. Echelle
3. Procédure de Conception et de Configuration
4. Saisie de données en temps réel vs. Saisie de données secondaire
5. Mobile vs Web
6. Mise sur pied d'une équipe principale
7. Hébergement
8. Formation
9. Lancement

## DÉFINITION DE L'OBJECTIF, DU BUT ET DU CHAMP D'APPLICATION { #define-purpose-aim-and-scope }

Un objectif clair et des buts bien définis sont essentiels à la compréhension par tous du champ d'application et des limites du projet, ainsi qu'aux échanges en interne et en externe sur le processus d'élaboration et de gestion d'un programme Tracker.

- Définissez les objectifs principaux et les objectifs secondaires du programme Tracker.
- Identifiez les entités suivies, le champ d'application de la collecte des données et les responsables sanitaires impliqués dans la collecte de données.
- Trouvez un moyen pour identifier individuellement chaque membre de la population cible (vous pouvez par exemple utiliser des numéros d'identification uniques ou une combinaison d'attributs).
- Clarifiez les attentes initiales de l'équipe principale, ainsi que des autres parties prenantes et utilisateurs du système.
- Organisez une séance de remue-méninges et discutez des questions clés et sujets de préoccupation qui doivent être traités pendant la phase d'élaboration.
- Préparez-vous à mener une phase d'élaboration : Élaborez un calendrier et prévoyez des plans d'urgence pour faire face aux événements inattendus qui entraînent des retards. Evoquez les problèmes potentiels et discutez des mesures à prendre pour les atténuer.

## Détermination de l'échelle { #determining-scale }

Étant donné que les systèmes de données individuelles (c'est-à-dire le Tracker) ciblent les niveaux les plus bas dans un système, les programmes Tracker peuvent augmenter considérablement le nombre d'utilisateurs, de matériels/appareils, de ressources techniques et le soutien organisationnel nécessaires à l'implémentation et à la maintenance du système. Les pays disposent souvent d'un personnel qualifié limité, pour gérer les déploiements. De même, les coûts associés à cette opération sont considérables.

L'échelle peut faire référence à plusieurs dimensions : l'échelle programmatique, l'échelle fonctionnelle ou l'échelle géographique, entre autres.

La mise à l'échelle géographique peut donc prendre du temps et absorber des ressources. Différentes stratégies permettent de le faire, c'est-à-dire couvrir complètement une région ou commencer "modestement" dans plusieurs régions en même temps et augmenter l'échelle à un rythme légèrement plus lent en parallèle.

Au fur et à mesure que vous évoluez, un effet boule de neige tend à se produire. Le nombre d'utilisateurs peut augmenter de façon exponentielle, ce qui nécessite plus de personnel et des mécanismes de soutien plus solides. Ainsi, les planificateurs peuvent s'assurer que les équipes d'assistance soient équipées pour gérer un volume et une vitesse accrus en tenant compte des éléments suivants :

**Finaliser et tester le Tracker avant de le déployer à grande échelle**
Recueillez des preuves et démontrez l'impact du Tracker avant de le déployer. Prévoyez un budget réduit pour les fonctionnalités sans impact ou fonctionnalités coûteuses en ressources mais à l'impact limité. Vous devez avoir une conception/configuration finale, testée et pilotée par les utilisateurs et qui produit les résultats escomptés en termes de gestion des informations et de rapports souhaités AVANT un déploiement à grande échelle. Pas d'expérimentation pendant la phase de déploiement. En d'autres termes, testez votre système et configurez-le pour 100 utilisateurs et non 5000.

**Gestion**
Assurez-vous qu'il existe des mécanismes de gestion solides et une répartition claire des responsabilités avant un déploiement à grande échelle. Contrôlez ce processus pour vous assurer qu'il soit respecté. Une bonne gestion est également essentielle pour garantir la flexibilité et l'adaptabilité de votre projet tracker, par exemple les ajouts de nouvelles options ou de nouvelles cliniques. Qui prend ces décisions ? Comment les documenter et comment les communiquer aux utilisateurs ?

**Coûts et considérations financières**
Examinez votre modèle de financement, y compris les moyens de génération de revenus, les modèles d'entreprise sociale, le coût par utilisateur et les moyens financiers destinés à soutenir l'initiative. Le déploiement à échelle entraîne une augmentation des coûts opérationnels en termes d'assistance, d'appareils et de connectivité.

**Amélioration du système**
Plus vous évoluez, plus vous devez gérer de connexions. Cela nécessite davantage de ressources en matière de mémoire, de puissance de traitement, de stockage et de connectivité.

Une partie du processus de déploiement consiste à ce que vous disposiez d'un plan de récupération rapide, car de plus en plus de personnes dépendent du système.

**Réviser l'étape pilote**
Souvent, le déploiement à grande échelle ne se fait pas  avec le même outil et la même approche que dans un projet pilote, surtout en ce qui concerne le niveau de ressources humaines et d'expertise nécessaire en matière de formation et de soutien pour atteindre le niveau d'utilisation atteint dans un projet pilote. Par conséquent, examinez votre outil et votre approche d'implémentation et pensez aux aspects qui peuvent être modifiés et simplifiés afin d'atteindre votre objectif principal.


*Reférences*:    

- Principes du Développement Numérique

*Outils*:

- Évaluation de l'état de préparation


## Procédure de conception et de configuration { #design-and-configuration-process }

**Impliquer activement les utilisateurs dans la conception et la configuration de votre programme Tracker** afin d'améliorer leur performance. Pour développer un programme Tracker, il faut définir les données à saisir, un flux de travail ainsi que les règles du programme. Cette étape doit être menée en étroite collaboration avec les utilisateurs, car elle concerne directement leur travail.

Nous recommandons de démarrer le processus de conception en posant les questions suivantes: 

1. Quelle est la finalité des données que vous collectez ? Comment comptez-vous utiliser les données ?
2. Qui bénéficiera de l'implémentation de Tracker ?
3. Comment les utilisateurs qui saisissent les données pourront-ils bénéficier de l'implémentation de Tracker ?
4. Recueillez-vous ces données aujourd'hui ? De quelle manière ? Quel est le flux de données actuel ?
5. Y a-t-il des éléments de données que vous recueillez actuellement et dont vous n'avez pas besoin ?


**PHASE D'ELABORATION**

Mieux connaître le système de santé (ou un autre système que le programme Tracker couvrira, pour les implémentations non sanitaires) afin d'appréhender les "points faibles" du système actuel, identifier les possibilités d'amélioration et mettre au point un système utile et adapté qui traite de ces problèmes et opportunités. Il s'agit entre autres de comprendre le travail des agents de santé, les données qu'ils collectent, leur flux de travail clinique et leurs systèmes de surveillance et de rapport.

- Préparer et entreprendre des visites sur le terrain pour faire un mapping des flux de travail cliniques et des demandes de supervision et de rapport avec la participation de tous les responsables du personnel de santé qui devrait utiliser le Tracker.
- Préparer et entreprendre des rencontres avec les parties prenantes pour informer, explorer et obtenir des commentaires.
- Vérifier les directives nationales (cliniques) existantes en rapport avec le champ d'application du Tracker.
- Faire un mapping du flux de travail existant en matière de documentation : Documentez ce que les travailleurs font actuellement et assurez-vous que votre conception soutienne leurs pratiques de travail plutôt que de les alourdir.
- Faire un mapping des indicateurs et des points de données associés pour l'établissement des rapports.
- Voyez s'il est nécessaire de réviser les lignes directrices ou les points de rapports. Si tel est le cas, établissez des plans parallèles pour la révision des lignes directrices et des rapports.

**PHASE D'ÉLABORATION**

- Aillez un aperçu des directives cliniques, des interventions, des indicateurs et des algorithmes actuels.
- Sur la base des lignes directrices actuelles, ainsi que des indicateurs et des points de données pour les rapports , élaborez des algorithmes et des points de données pour le suivi électronique.
- Définissez les groupes cibles et le niveau de complexité de l'aide à la décision. En fonction du niveau de soutien au flux de travail, établissez des règles et faites-en part aux développeurs de logiciels dans un cadre convenu à l'avance.
- Faites des révisions régulières pour vous assurer que la traduction des développeurs réponde aux besoins des prestataires de soins de santé.

**PERSONNALISATION ET PHASE DE TEST**

Cette phase consiste en une collaboration constante avec les parties prenantes, les développeurs de logiciels, les responsables de l'implémentation et les utilisateurs, dont les avis seront intégrés.

- Mettez au point un système numérique structuré et facilement accessible pour le partage d'avis au sein du groupe de travail principal.
- Veiller à ce que le développement du contenu réponde aux attentes des parties prenantes, des utilisateurs du système et des partenaires financiers.
- Continuez les discussions ouvertes sur la traduction, l'utilisation des boutons d'information, etc., afin d'éviter des mauvaises interprétations.
- Veillez au maintien des processus parallèles qui impliquent et favorisent le partage d'informations entre tous les groupes d'utilisateurs pendant ces phases.
- Définissez des étapes pour les développeurs, les chargés de l'implémentation et les utilisateurs.
- Mettez au point un système numérique en ligne, structuré et facilement accessible permettant de recueillir des commentaires complets et détaillés des utilisateurs finaux.

**Boîte à outils des données sanitaires du DHIS2 et de l'OMS**

DHIS2 travaille en partenariat avec l'Organisation mondiale de la santé (OMS) sur une variété d'initiatives relatives à la santé, y compris la création de métadonnées normalisées visant à renforcer l'utilisation des données au niveau national et international. La Boîte à outils des données sanitaires du DHIS2, approuvé par l'OMS, fournit un ensemble d'outils numériques permettant de faciliter l'adoption des normes de l'OMS en matière de données sanitaires de routine au sein du système national d'information sanitaire de routine. Alignés sur la Boîte à outils de l'OMS pour les données de systèmes d'information sanitaire de routine, les modules d'analyse intégrée et les modules du DHIS2 spécifiques aux programmes sont conçus conformément aux orientations internationales en matière d'analyse des données et aux normes de mesure. La boîte à outils du DHIS2 fournit une implémentation de référence entièrement numérisée, composée de packs de métadonnées installables, de documentation technique, de bases de données de démonstration et de conseils d'implémentation. Les ensembles de métadonnées du DHIS2 approuvés par l'OMS peuvent être installés dans des systèmes du DHIS2 autonomes ou intégrés dans des instances DHIS2 existantes et adaptés au contexte national. Les ensembles de métadonnées réunissent les normes internationales et les pratiques de conception du DHIS2 fondées sur des données probantes pour les systèmes d'information sanitaire intégrés dans une boîte à outils installable, qui peut être utilisée à titre de référence en matière de conception ou en tant que système importé pour une utilisation locale.

Pour plus d'informations sur la documentation et les outils de données sanitaires du DHIS2 et de l'OMS, [voir ici](https://dhis2.org/who/).

## Détermination de votre cadre de S&E { #determining-your-me-framework }

Un cadre de suivi et d'évaluation (S&E) est un élément essentiel de l'implémentation d'un Tracker du DHIS2. Il permet non seulement d'évaluer l'état d'avancement et les succès dans l'implémentation mais aussi d'identifier les points à améliorer. Une bonne implémentation du Tracker nécessite un cadre de suivi et d'évaluation robuste pour garantir que la collecte de données, les pratiques en matière d'utilisation, les mises à jour du DHIS2, la gestion des utilisateurs, la sécurité, l'hébergement, l'assistance aux utilisateurs et la formation soient tous gérés efficacement.

**À quoi ressemble une implémentation réussie d'un Tracker ?**

Une implémentation réussie du Tracker doit avoir un cadre de S&E complet qui couvre tous les aspects de l'implémentation. Sont inclus des évaluations régulières de la collecte de données, des pratiques en matière d'utilisation des données, des mises à jour du DHIS2, la gestion des utilisateurs, la sécurité, l'hébergement, l'assistance aux utilisateurs et la formation. Le cadre de suivi et d'évaluation devrait également inclure un processus d'identification et de résolution de tout problème qui survient.

**Maintenir et évaluer la collecte de données**

Il est important d'évaluer régulièrement le processus de collecte des données afin de s'assurer de sa précision, de sa complétude et de sa rapidité. Il s'agit notamment d'évaluer la qualité des données saisies, leur complétude et le respect des délais de transmission. L'identification et la résolution des problèmes liés à la collecte des données permettront d'améliorer la qualité générale des données.

**Maintenir et évaluer les pratiques en matière d'utilisation des données**

L'évaluation régulière des pratiques en matière d'utilisation des données permet de garantir que les données soient utilisées efficacement de sorte à éclairer la prise de décision et qu'elles soient utilisées conformément aux buts et aux objectifs de l'organisation. Il s'agit notamment d'évaluer la qualité de l'analyse des données, l'utilisation des données dans la prise de décision et l'efficacité de leur diffusion.

**Maintenir et évaluer les nouvelles versions du DHIS 2**

Il est important d'être en phase avec les nouvelles versions du DHIS2, pour s'assurer que l'implémentation utilise la version la plus récente du logiciel. Il s'agit notamment d'évaluer régulièrement la version de DHIS2 utilisée, d'évaluer les avantages d'une mise à jour vers une nouvelle version et d'effectuer toutes les mises à jour nécessaires.

**Maintenir et évaluer la gestion des utilisateurs**

L'évaluation régulière de la gestion des utilisateurs permet de s'assurer que les utilisateurs disposent d'un accès approprié au système, que leurs rôles et autorisations soient correctement configurés et que les comptes d'utilisateurs soient gérés de manière efficace. Il s'agit entre autres d'évaluer le nombre d'utilisateurs actifs, le nombre de nouveaux utilisateurs et le nombre d'utilisateurs inactifs.

**Maintenir et évaluer la sécurité**

L'évaluation régulière des mesures de sécurité appliquées à l'implémentation permet de s'assurer de la protection des données et de la conformité du système aux règles de sécurité. Il s'agit entre autres d'évaluer l'efficacité des procédures d'authentification et d'autorisation du système, la sécurité du milieu d'hébergement et l'efficacité du plan de reprise après sinistre du système.

**Maintenir et évaluer l'hébergement**

L'évaluation régulière du milieu d'hébergement permet de s'assurer de la bonne configuration du système, de son fonctionnement et de sa disponibilité pour les utilisateurs. Il s'agit entre autres d'évaluer la stabilité, les performances et la sécurité du milieu d'hébergement, ainsi que la disponibilité du système.

**Maintenir et évaluer l'assistance aux utilisateurs**

L'évaluation régulière de l'assistance aux utilisateurs permet de s'assurer que ces derniers peuvent utiliser efficacement le système et que tous les problèmes sont résolus dans les meilleurs délais. Il s'agit entre autres d'évaluer la réactivité et l'efficacité de l'équipe d'assistance aux utilisateurs, ainsi que la qualité de la documentation relative à cette assistance.

**Maintenir et évaluer la formation**

L'évaluation régulière du programme de formation permet de garantir une bonne formation aux utilisateurs et une adéquation du programme par rapport aux besoins de l'organisation. Il s'agit entre autres d'évaluer l'efficacité du programme de formation, la qualité du matériel de formation et le nombre d'utilisateurs ayant participé au programme.

Il convient de noter que le cadre de suivi et d'évaluation doit être régulièrement examiné et mis à jour afin de s'assurer qu'il réponde aux besoins de l'organisation et qu'il soit aligné sur ses buts et objectifs. Il doit également être conforme à toutes les dispositions et normes nationales et internationales relatives à la sécurité et à la protection des données.


## Saisie de données en temps réel vs saisie de données secondaire { #real-time-vs-secondary-data-entry }

**Déterminez si les données doivent être saisies en temps réel**. La structuration de votre projet en dépend considérablement. Les Trackers sont utilisés pour suivre des personnes dans le cadre de programmes bien définis, avec des éléments de données et règles associés. Les données peuvent être saisies par le personnel de santé pendant les consultations (sur les lieux de soins et en temps réel) ou en fin de journée (ou lorsqu'il a le temps de les saisir). Ces deux approches différentes influent évidemment sur l'utilisation du Tracker.

La saisie des données en temps réel facilite la prise de décision rapide, la validation des données et permet d'éviter la saisie d'une même information à plusieurs reprises. Cependant, elle requiert également une connexion internet fiable, souvent indisponible dans certaines localités. De plus, la saisie de données en temps réel peut nécessiter l'utilisation d'appareils mobiles, ce qui peut poser des défis supplémentaires tels que la maintenance des appareils, l'alimentation électrique et la formation du personnel de santé.

Si les données sont saisies en fin de journée ou lorsque le personnel de santé le souhaite, les défis liés à la saisie des données en temps réel sont évités. Cela implique également que les données ne seront pas disponibles en temps réel, compliquant ainsi la prise de décision rapide.

Lors du choix de la méthode, il convient de prendre en compte les ressources disponibles, le contexte local ainsi que les buts et objectifs de l'organisation. Il convient également de mettre en application des procédures opérationnelles normalisées (PON) précises pour la sauvegarde des dossiers papier, de faciliter les recherches de clients et de mettre en place des mécanismes pour éviter des erreurs (par exemple, des dispositions empêchant de saisir des dates futures).

## Mobile vs Web{ #mobile-vs-web }

**Évaluez les conditions d'accès à Internet des personnes chargées de la saisie des données** Dans certains contextes ou dans certaines localités, il est difficile, voire impossible, d'accéder au serveur central en ligne du DHIS2 avec un ordinateur. L'application de Saisie Android du DHIS2 a été conçue et développée pour pallier à ces situations. Cependant, l'utilisation d'appareils mobiles dans l'implémentation du DHIS2 affectera votre projet sur plusieurs plans. Cette décision doit donc être prise avec discernement et en toute connaissance de cause.

**Web ou mobile ?** 
Deux facteurs principaux sont à prendre en compte lorsque vous envisagez d'intégrer une composante mobile à l'implémentation de votre Tracker : la disponibilité d'Internet et la mobilité de vos postes de santé. L'implémentation d'un Tracker peut nécessiter la prise en compte d'un seul de ces deux facteurs, ou des deux à la fois. Nous allons essayer de les définir et vous aider à analyser votre situation dans cette section.

- **Mobilité** : Certaines équipes offrent leurs services dans différents endroits grâce à des unités mobiles. Certains lieux visités par l'unité mobile peuvent disposer d'établissements dotés d'un poste de travail adéquat pour la collecte des données, mais la saisie des données se fait souvent dans un environnement plus dynamique ou dans l'unité mobile lui-même. Dans une situation pareille, au lieu d'utiliser un ordinateur portable (ce qui n'est pas très aisé), un appareil mobile peut être plus approprié.

- **Disponibilité d'Internet**: Plusieurs endroits présentent des difficultés d'accès à Internet. Deux scénarios sont envisageables : *La connexion Internet est instable ou limitée* et *La connexion Internet n'est pas disponible*.

    - Lorsque *la connexion Internet est instable ou limitée* à certains moments de la journée, l'option mobile ou Web est envisageable pour la saisie des données. La saisie de données en ligne avec le DHIS2 permet de poursuivre la saisie de données lorsque la connexion Internet est interrompue. Les données saisies seront stockées localement dans le cache du navigateur web et elles seront automatiquement téléchargées lorsque l'utilisateur sera à nouveau connecté. Il convient de noter que cette fonction hors ligne dépend du stockage au niveau du navigateur web et qu'elle ne sera efficace que si la fenêtre du navigateur reste ouverte. Si un utilisateur en train de recueillir des données hors ligne, ferme cette fenêtre où il travaille alors qu'il est toujours en mode hors ligne, les données seront malheureusement perdues. La fonction hors ligne *absorbe* les effets des interruptions intermittentes de la connexion Internet afin d'offrir une expérience de travail fluide et stable, mais il ne s'agit pas d'une solution hors ligne complète.

    - Lorsque *la connexion Internet n'est pas disponible*, envisagez l'utilisation de l'application Android de Saisie du DHIS2, qui offre une assistance hors ligne complète pour la collecte de données. Cette application peut être utilisée avec des appareils mobiles et des tablettes, de même qu'avec d'autres appareils tels que les Chromebooks. L'application de Saisie Android peut donc être utilisée lorsque la connexion Internet n'est pas disponible, mais que les personnes chargées de la collecte des données peuvent se déplacer.

**Implications de l'utilisation de l'application Android** 
L'application de Saisie Android du DHIS2 facilite la collecte de données du Tracker en mode hors ligne, mais elle a également des implications qui doivent être prises en compte dès les premières phases du projet. L'utilisation d'une composante mobile dans votre implémentation pourrait avoir un impact sur votre stratégie de planification, de budgétisation, de formation, de configuration et de déploiement, etc.

- **Configuration du DHIS2:** Lorsque vous configurez le Tracker pour une utilisation avec des appareils mobiles, il vous faut prêter une attention particulière à la configuration des utilisateurs mobiles, à leur accès à la saisie des données et aux unités d'organisation. Les utilisateurs mobiles recueillent généralement des données dans les zones les plus reculées et les plus inaccessibles. Par conséquent, on ne s'attend pas à ce qu'un utilisateur mobile recueille des données auprès d'un grand nombre d'établissements. Aucun nombre maximum d'unités d'organisation n'est fixé pour l'application, mais si le nombre d'unités est très élevé, les performances de l'application peuvent être affectées en fonction des ressources disponibles sur l'appareil (mémoire, processeur). En général, moins de 250 unités d'organisation ne devrait pas poser de problème, mais ce nombre reste très élevé dans un cas typique d'utilisation mobile.
Il est également très important de prêter attention à la configuration des règles et des indicateurs du programme. L'application Android entend prendre en charge toutes les fonctionnalités web du Tracker, même si certaines fonctionnalités peuvent opérer un peu différemment sur Android ou être pris en compte dans le développement de l'application en attendant d'être implémentées. Une liste détaillée sur le fonctionnement des règles et des indicateurs de programme sur Android est disponible dans les sections _Règles de programme_ et _Indicateurs de programme_ de la [documentation de l'application Android] (<[https://www.dhis2.org/android-documentation](https://www.dhis2.org/android-documentation)>).

- **Représentation visuelle de la collecte de données:** L'expérience utilisateur de l'application Android a été pensée pour être très visuelle et intuitive. Des icônes et des couleurs peuvent être utilisées pour configurer les formulaires de saisie de données et leur affichage. La représentation visuelle est configurable par l'administrateur du système. Il existe une bibliothèque d'icônes avec plus de 400 images et une palette de couleurs. Les icônes et les couleurs peuvent être assignées aux principaux objets de métadonnées : Options, Éléments de données, Attributs, Programmes / Ensembles de données. Vous trouverez plus d'informations sur la configuration visuelle du DHIS2 dans la section _Configurations visuelles_ de la [documentation de l'application Android] (<[https://www.dhis2.org/android-documentation](https://www.dhis2.org/android-documentation)>).

- **Test :** La phase de test est très importante dans toute implémentation du DHIS2. Vous devez tester l'application Android conjointement avec la configuration de votre serveur, pour vous assurer que toutes les configurations effectuées sur le serveur sont bien prises en compte et qu'elles fonctionnent dans l'application. Cette étape est très importante lors de la configuration des règles du programme. Vous trouverez de plus amples informations sur les différents types de tests et sur la planification des phases de test pour votre projet dans la section _Tests_ des [Directives pour l'implémentation du DHIS2 mobile](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf).

- **Sécurité :** En fonction de la configuration de votre Tracker, il se peut que vous stockiez des données personnelles sur des appareils mobiles et que des conflits surviennent entre le besoin du système de santé de disposer de données identifiables et le droit du patient au respect de sa vie privée. Il est donc primordial de veiller à ce que les données personnelles ne soient accessibles qu'au personnel de santé autorisé à en disposer. La bonne gestion des données personnelles est un aspect important dans la formation des utilisateurs, et il est crucial d'établir des procédures opérationnelles normalisées (PON) décrivant les mesures de sécurité à appliquer, et de veiller à ce que ces procédures soient partagées avec tous les utilisateurs et que ces derniers les respectent. Les administrateurs de système jouent également un important rôle lors de la configuration du niveau d'accès des utilisateurs, en s'assurant que le niveau d'accès aux données soit approprié pour chaque utilisateur. Les recommandations relatives à une approche adéquate  aux questions de sécurité et de confidentialité pour toute implémentation du DHIS2 mobile figurent dans la section _Sécurité et Confidentialité des données _ des [Directives pour l'implémentation du DHIS 2 mobile (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf). 
A FAIRE; ajouter un lien qui mène vers la section Sécurité de ce document !

- **Achat d'appareils mobiles:** L'acquisition d'appareils mobiles est un aspect clé du déploiement mobile et doit être prise en compte dans la planification, la budgétisation et la logistique. La meilleure stratégie est de se procurer les appareils les plus performants et les plus modernes possibles, de sorte qu'ils puissent être utilisés tout au long du projet. En ce sens, il convient de retarder le plus possible le gros de l'acquisition (en d'autres termes, tous les appareils qui ne sont pas nécessaires pour la phase initiale d'essai et de pilotage), plutôt que d'acheter tous les appareils dès le début de la planification. La technologie, et en particulier les appareils mobiles, évolue très rapidement. Un modèle d'appareil est normalement renouvelé chaque année, ce qui permet aux consommateurs de bénéficier d'améliorations techniques significatives d'une année à l'autre à un prix similaire. Les caractéristiques des appareils mobiles pouvant être utilisés avec l'application de Saisie Android du DHIS2 sont disponibles [ici] (https://docs.google.com/document/d/1jZjw-hb1W8sszkPU9yPWrPoow91gEkTb0nyZJh3IJQQ/edit).
Après avoir effectué tous les tests et achevé votre projet pilote, vous êtes prêt pour le déploiement à grande échelle avec l'acquisition du matériel et des services nécessaires. Vous trouverez des conseils sur l'acquisition du matériel mobile dans la section _Déploiement à grande échelle_ des [Lignes directrices pour l'implémentation du DHIS2 Mobile] (https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf). Nous résumons ci-dessous les principaux aspects à prendre en compte au cours de cette phase :

  1) Achat d'appareils vs PAP (prenez vos appareils personnels) : L'avantage du PAP est qu'il permet de réduire le coût initial d'acquisition des appareils ainsi que les coûts administratifs et de la logistique. Toutefois, l'utilisation du modèle PAP sous-entend qu'il faudra gérer un environnement matériel très hétérogène, c'est-à-dire différents appareils et versions Android OS. Les utilisateurs finaux pourraient donc avoir des aptitudes différentes à saisir et à examiner les données, et la mise à niveau de l'instance centrale du Tracker pourrait s'avérer problématique, car les nouvelles versions peuvent avoir une rétrocompatibilité limitée avec les anciennes versions de l'application. Le principal avantage de l'achat d'appareils pour les utilisateurs finaux est l'uniformité des appareils et des versions de l'application, mais cette approche augmente les coûts du matériel et implique des défis logistiques liés à la distribution des appareils mobiles, ainsi qu'à leur maintenance et à leur remplacement au fil du temps.

  2) Distribution de l'application : vous pouvez installer directement l'application de Saisie Android en utilisant l'APK disponible sur [Github] (https://github.com/dhis2/dhis2-android-capture-app/releases) ou en utilisant [Google Play] (https://play.google.com/store/apps/details?id=com.dhis2). Avec Google Play, la mise à jour de l'application sur tous vos appareils est plus facile, mais il vous faudra installer automatiquement toutes les mises à jour de l'application. L'installation de l'APK vous permet de déterminer le moment de la mise à jour et la version correspondante, mais elle nécessite un processus plus complexe pour la mise à jour de tous vos appareils et n'est pas recommandée pour les projets qui n'utilisent pas de logiciel de gestion d'appareils mobiles (voir le point suivant).

  3) Contrats de télécommunication: le processus de sélection et de signature d'un contrat avec un opérateur de téléphonie mobile varie selon les pays et dépend également des procédures d'approvisionnement de votre organisation.

- **Gestion et Maintenance des appareils:** La Gestion des Appareils Mobiles (MDM) fait référence aux logiciels utilisés pour la gestion des appareils mobiles. Un logiciel MDM est nécessaire pour la prise en charge de centaines d'appareils, le contrôle de la distribution des fichiers APK sur tous ces appareils, la d=fourniture d'une assistance technique et l'application des politiques institutionnelles. Vous trouverez plus d'informations sur les caractéristiques recommandées pour un logiciel MDM, les options disponibles et des conseils sur la sélection du logiciel MDM adapté à votre projet dans la section _Gestion des Appareils Mobiles_ des [Directives pour l'implémentation mobile du DHIS2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/Publications/DHIS+2+Mobile+Implementation+Guidelines.pdf).

## Ressources humaines et Assistance informatique { #human-resources-and-it-support }

Toute implémentation du Tracker ne réussira que si elle est menée par les bonnes personnes. Avant de démarrer un projet Tracker, il est important de s'assurer de la disponibilité d'un personnel compétent.

Voici quelques éléments à prendre en compte lorsque vous constituez votre équipe :

1. Privilégiez les engagements à long terme. Les personnes responsables de l'implémentation du Tracker doivent faire partie du projet dès son démarrage.

2. Les ressources nationales présentes à tous les niveaux du système (de santé) doivent être impliquées dès le démarrage du projet. Le transfert de l'historique du projet, des décisions et des pratiques habituelles entre les consultants externes et le personnel permanent est souvent difficile.

3. Si vous disposez déjà d'une instance DHIS2 agrégée, rappelez-vous que les personnes qui gèrent les données agrégés ne sont pas automatiquement « qualifiées » pour le projet Tracker, car le Tracker est différent des rapports agrégés.


|Rôle | Responsabilités/tâches |
|:------|----------------------|
|Chef de projet | Gérer le projet Tracker|
|Responsable de la configuration et du développement    | Diriger les travaux de développement|
|Responsable de la sécurité | Responsable de la sécurité, de la politique ++|
|Responsable de la formation   | Organiser des formations|
|Responsable des Tests | Diriger les travaux de test|
|Formateurs | Organiser des sessions de formation avec les utilisateurs finaux|
|Responsable de l'assistance | Diriger les efforts d'assistance|
|Répartition du Personnel d'assistance| Recevoir des demandes d'assistance et aider les utilisateurs|

### Unité d'assistance informatique { #it-support-unit }

L'assistance doit être disponible à proximité de l'utilisateur, ce qui nécessite souvent la création d'une nouvelle structure d'assistance informatique au niveau du district ou du sous-district. Si le Tracker est utilisé en temps réel, l'assistance technique doit toujours être disponible pendant les heures de travail pour résoudre et signaler les problèmes. Si le Tracker prend en compte les décisions cliniques, le personnel informatique doit comprendre le flux de travail clinique et la manière dont il est représenté dans le système. Ainsi, l'équipe d'assistance technique du Tracker peut avoir des compétences et des expériences différentes de celles des autres responsables d'informations sanitaires, et peut constituer un nouveau cadre de travail au sein de votre système de santé.

**Structure et gestion de l'équipe**

Chaque membre de l'unité d'assistance informatique doit être formé avant le premier utilisateur final et doit connaître parfaitement le système et son fonctionnement. Souvent, l'unité d'assistance informatique est composée de ceux qui dirigent la formation des utilisateurs finaux. Le personnel d'assistance devrait être présenté aux utilisateurs finaux pendant la formation afin de tisser des liens et d'instaurer une relation de confiance dès le départ. Le travail du personnel d'assistance consiste essentiellement en une "supervision constructive" des activités. Pour être efficace, le personnel d'assistance doit également être bien informé, respecté et respectueux, mais il n'est généralement pas en position d'autorité directe sur l'utilisateur final, car cela pourrait dissuader ce dernier de poser des questions techniques et de signaler des anomalies dans le système.

Une fois l'équipe en place, une hiérarchie de travail interne peut être établie, allant d'une amélioration des capacités techniques au sommet de la hiérarchie (par exemple, l'administrateur du système est au sommet de la hiérarchie), à une amélioration de l'accès aux utilisateurs finaux au bas de la hiérarchie (par exemple, le superviseur direct de l'utilisateur final, le personnel d'assistance sur le terrain). Au cours de cette phase d'organisation du personnel, il convient d'élaborer des procédures opérationnelles normalisées pour signaler les problèmes soulevés par les utilisateurs finaux et y répondre.

**Outils essentiels à toutes les unités d'assistance informatique**

- Document sur les Questions Fréquemment Posées (FAQ) : Il s'agit d'un document décrivant, au moyen de graphiques et/ou dans la langue locale, les procédures opérationnelles normalisées relatives à la saisie des données et les mesures à prendre en cas de bugs. Une FAQ doit être distribuée pendant toutes les formations, et elle doit être régulièrement mise à jour par l'unité d'assistance informatique et partagée avec les utilisateurs finaux au fur et à mesure que le système Tracker évolue.

- Gestion des appareils mobiles : Pour protéger les données des patients, un système distinct de gestion des dossiers doit être mis en place pour savoir quels utilisateurs ont accès à quel appareil, afin d'identifier les appareils perdus ou volés et suivre la situation. Ce système peut être aussi simple qu'une feuille de calcul, mais dans les situations plus importantes et plus complexes, un système MDM (Gestion des appareils mobiles) adapté à l'entreprise peut être utilisé pour suivre l'emplacement des appareils et effacer à distance les données d'un appareil individuel, si nécessaire.

- Gestion des utilisateurs : l'unité d'assistance informatique doit être en mesure de documenter et de gérer les tâches d'administration système de base telles que la création de nouveaux comptes d'utilisateurs, la désactivation des comptes d'utilisateurs inactifs ou la réinitialisation des mots de passe.

- Plate-forme de suivi des indicateurs clés du système : ces indicateurs clés incluent les nouvelles inscriptions par unité d'organisation, les utilisateurs inactifs, les périodes d'indisponibilité du serveur, etc. L'unité d'assistance informatique devrait avoir accès aux indicateurs agrégés dans un tableau de bord DHIS2 qui y est dédié, où elle peut consulter la progression de l'implémentation par période et par région.

- Plateforme de gestion des cas pour l'enregistrement des bugs et des tickets : Ces plateformes (à l'instar de JIRA) permettent aux membres de l'équipe d'assistance informatique de saisir, d'éditer, d'attribuer, de suivre et de résoudre les bugs et autres tickets, et permettent aux superviseurs de contrôler les principaux facteurs liés à la prestation, tels que le nombre de tickets ouverts et de bugs non résolus, le temps moyen de réponse, etc.

- Plateforme de gestion des connaissances : Il s'agit d'un référentiel où les employés peuvent apprendre de tickets précédents (ce qui permet de constituer une base de connaissances). L'unité d'assistance informatique comprend l'expérience réelle de l'utilisateur avec le Tracker mieux que tout autre implémenteur ou administrateur de système, et son point de vue peut être très utile pour adapter le Tracker aux besoins des utilisateurs. Une plateforme de connaissances - électronique, ou sous forme de rencontres régulières entre les membres du personnel - peut permettre de partager des expériences communes, des frustrations ou des idées pour améliorer le système.

- Hotline pour signaler des bugs : Cette hotline peut prendre plusieurs formes. Par exemple, il peut s'agir d'un numéro de téléphone réservé au personnel d'assistance et communiqué à chaque utilisateur, ou d'une adresse électronique où les utilisateurs peuvent envoyer des messages et des captures d'écran. Quel que soit le format, une PON (procédure opérationnelle normalisée) doit être mise en place, avec la hoteline, pour permettre le signalement des bugs sur la plateforme de gestion des cas mentionnée plus haut.

- Groupes de discussion publics : Plusieurs équipes d'assistance estiment que la création de groupes de discussion entre le personnel et les utilisateurs finaux peut favoriser l'apprentissage mutuel (par exemple, Whatsapp ou Wechat pour partager des captures d'écran, des messages vocaux ou des solutions créatives aux problèmes courants).

*Références*:

- [Principes du Développement Numérique](https://digitalprinciples.org/)


## Hébergement { #hosting }

Le programme Tracker et les données collectées du DHIS2 doivent être hébergés sur un serveur. Cela peut se faire localement (par exemple au ministère de la santé ou des technologies de l'information), par l'intermédiaire d'un prestataire local ou sur le cloud. Chaque option a ses avantages et ses inconvénients. Par exemple, héberger une implémentation du Tracker sur le cloud règle les défis liés à la capacité du serveur et aux temps d'arrêt, mais l'hébergement des données hors du pays peut poser des problèmes d'ordre juridique, sauf si un fournisseur local assure le service. Quelle que soit la stratégie d'hébergement, la sécurité est un aspect clé. Elle comprend la gestion des identités, les authentifications et autorisations (restriction d'accès aux données ou aux services) et la protection des serveurs.

De plus, il faudra décider si le Tracker doit être configuré dans une instance distincte ou dans la même instance que votre système agrégé. L'un des avantages d'une instance distincte est la possibilité de générer directement des rapports à partir des données du Tracker. Cependant, le fait de les avoir tous les deux dans une même instance nécessite des procédures opérationnelles normalisées (PON) plus strictes pour la gestion des comptes d'utilisateurs afin de garantir que l'accès aux données des patients soit restreint de manière appropriée.

**Principes clés d'hébergement et de sécurité qui doivent être inclus dans votre plan d'hébergement, que l'instance soit locale ou dans le cloud :**

- Le système d'exploitation est une édition Long-Term Service (LTS) ou service à long terme.
- Une procédure automatique permet d'appliquer les correctifs de sécurité du système d'exploitation
- Un pare-feu est configuré au niveau du système pour autoriser un accès minimal.
- L'accès se fait via Secure Shell (SSH) comme convenu (clés, pas d'accès root, etc.)
- La version du DHIS2 n'a pas plus de 3 versions de retard par rapport à la dernière version, et un mécanisme permet d'appliquer régulièrement les correctifs.
- Un système de sauvegarde automatisé est en place et est régulièrement testé, y compris en hors-site.
- Les contrôles d'accès à la base de données PostgreSQL garantissent un accès minimal
- Un serveur proxy Web est correctement configuré (SSL Labs test A+) avec Secure Sockets Layer (SSL)
- Toutes les données de la base sont stockées sur une partition de données distincte (permettant le cryptage et les paramètres de performance)
- Un système de surveillance et d'alerte est mis en place
      - Plusieurs options sont disponibles, en fonction du contexte. Par exemple, boombox peut convenir avec email + logwatch + munin.
- Électricité suffisante et stable pour charger les appareils
- Si vous utilisez la version Android, un réseau doit être disponible pour assurer la synchronisation.
- Si vous utilisez la version Web, un réseau stable est disponible


**Gestion et durabilité des systèmes informatiques :**

Il existe de la documentation sur les plans et protocoles de sécurité, tant à un niveau élevé qu'au niveau des procédures techniques. Cette documentation est particulièrement importante lorsque les systèmes sont hébergés localement sans culture de la "sécurité avant tout".

Un responsable doit être désigné pour l'élaboration, la maintenance et l'implémentation du plan de sécurité. Un autre responsable de la sécurité doit s'engager à identifier et à atténuer les risques. Ces deux rôles requièrent de l'expérience, des aptitudes et de la motivation.

Veiller à ce qu'il existe un ensemble documenté de contrôles techniques obligatoires, de même qu'une procédure d'audit de ces contrôles.

PON publiées et disponibles pour la sécurité opérationnelle, physique et celle du réseau (verrouillage des PC, mots de passe sécurisés, cryptage des données, etc.), ainsi que pour la surveillance et la réponse en cas de panne ou de brèche dans le système.


## Formation et déploiement { #training-and-rollout }

**Planifier une formation continue et de haute qualité** Le renforcement des capacités est essentiel à la réussite d'un programme Tracker, et doit être à la fois de haute qualité et se poursuivre régulièrement tout au long du programme. Il ne suffit pas de former les utilisateurs une fois pour toutes : votre plan de formation doit prévoir une formation initiale et une remise à niveau régulière. Les utilisateurs en première ligne du Tracker sont généralement des agents de santé locaux qui peuvent être moins à l'aise avec la technologie que le personnel de district qui travaille souvent avec des données agrégées. Une formation bien conçue permettra aux stagiaires de se familiariser avec les outils et d'apprendre à intégrer le Tracker à leur travail.

Un principe clé est de **concevoir le matériel de formation en collaboration avec les utilisateurs**. Travailler en étroite collaboration avec les utilisateurs lorsque vous concevez le matériel de formation vous permettra de déterminer quels concepts sont difficiles à comprendre pour les utilisateurs, afin que vous puissiez améliorer votre matériel et le programme de formation. Effectuez une première formation complète avec un groupe d'utilisateurs réels afin de parfaire votre cours.

Identifiez l'approche de formation appropriée : Vous pouvez organiser votre formation de diverses façons (par exemple en vidéo, tests en ligne, sur le terrain, sous forme de réunion). Vous pouvez utiliser une des méthodes ou une combinaison de méthodes.

**Impliquer le personnel de santé** et pas seulement le personnel informatique pendant les formations afin d'expliquer et d'insister sur les raisons sanitaires qui sous-tendent les opérations de saisie de données. Ceci est particulièrement important pour les configurations qui impliquent une aide à la décision. Les utilisateurs finaux peuvent ainsi mieux comprendre l'importance du programme Tracker, ce qui peut conduire à une saisie plus complète et plus précise des données, et donc à une plus grande probabilité que le programme atteigne ses objectifs. 
Réviser le matériel en fonction des feedbacks des participants au cours, ou si des révisions du programme Tracker rendent l'ancien matériel de formation inadapté.

**Logistique** 
Planifier la formation des utilisateurs du Tracker sous forme d'une série d'étapes de formation, afin qu'ils soient remis à niveau après un certain temps. Le programme de remise à niveau devrait de préférence s'aligner sur les cycles de révision du logiciel Tracker, afin de faciliter l'introduction des utilisateurs finaux aux changements et aux nouvelles fonctionnalités du programme.

Notez que la formation d'un grand groupe d'utilisateurs ( notamment répartis sur une vaste zone géographique) nécessitera souvent que vous formiez d'abord d'autres formateurs (dans le cadre d'une formation des formateurs ou ToT) au début de la formation, afin de renforcer votre capacité de formation. 
Conservez une trace des utilisateurs du Tracker qui ont été formés dans un tableur, sur une liste ou sur toute autre base de données centralisée, et établissez une PON pour mettre à jour cette liste lorsque de nouveaux membres rejoignent l'équipe, ou lorsque des membres du personnel quittent l'équipe ou sont relocalisés. Les nouveaux membres du personnel ou ceux qui n'ont pas reçu de formation doivent être formés le plus tôt possible. 
Choisissez avec soin le lieu de la formation. La formation peut se dérouler soit sur le terrain (sur le lieu de travail des utilisateurs ou à proximité), soit dans le cadre de formations centralisées qui rassemblent en un même lieu de plus grands groupes d'utilisateurs provenant de différents lieux de travail. Les deux approches présentent des aspects positifs et négatifs. Quel que soit le lieu de la formation, la personne chargée de la planification devra régler les détails logistiques tels que le lieu, le transport, la restauration, les ordinateurs, l'accès à l'internet, etc.

Si possible, formez les utilisateurs avec les appareils qu'ils utiliseront pour leur travail. Ne sous-estimez pas le temps nécessaire aux utilisateurs pour se connecter et se familiariser avec l'appareil - cela peut prendre beaucoup de temps au début du programme de formation pour que tous les participants soient prêts d'un point de vue technique. Il est recommandé que plusieurs membres de l'équipe de formation soient disponibles pour aider à résoudre ces problèmes au fur et à mesure qu'ils se présentent. 
Planifier le suivi de la formation régulière, de la formation sur le terrain et de la formation de remise à niveau.

**Formation dans des zones à faible bande passante** 
Si la connexion Internet est trop lente, peu fiable ou inexistante sur votre lieu de formation, il vous faudra installer une instance locale de Tracker et la configurer pour la formation, sur une machine ou un serveur local, de sorte que les participants puissent se connecter via un réseau local commun, une adresse IP ou un hébergement local. Même dans des zones où l'accès à internet est satisfaisant, des problèmes de réseau peuvent survenir lorsqu'un grand nombre d'utilisateurs accèdent à l'instance web du Tracker via un réseau WiFi ou un point d'accès à internet. Par conséquent, il est généralement conseillé de disposer d'une instance de formation comme solution de secours dans ces cas-là.



## Associer Tracker à votre système de données agrégées { #relating-tracker-to-your-aggregate-data-system }

Lors de la conception du Tracker, il est important de prendre en compte les exigences de base du Système National d’Information Sanitaire (SNIS) pour éviter de rapporter les mêmes informations plus d'une fois. Les données saisies dans le Tracker constituent la base pour la génération de nombres agrégés. Par exemple, s'il y a 4 informations de patients qui sont saisies, 2 avec la condition X et 2 avec la condition Y, le Tracker devrait prendre en charge le système d'agrégation, plutôt que d'être un fardeau supplémentaire pour les collecteurs de données. La conception du système doit prendre en compte les modalités de satisfaction des exigences en matière de données agrégées, à l'aide des données saisies via le Tracker.

Différentes options peuvent être envisagées, telles que les méthodes automatisées ou manuelles avec l'aide d'outils. Il est essentiel de disposer d'un flux de travail, d'outils et d'un modèle de gouvernance bien définis pour garantir la qualité et la complétude des données, ainsi que pour le processus d'autorisation des données. Il s'agit notamment de déterminer qui peut approuver et traiter les données, des données individuelles aux données agrégées, ainsi que la manière dont ce processus se déroule.

En planifiant l'intégration avec le SNIS, assurez-vous d'examiner attentivement les indicateurs, de produire les rapports, d'établir un modèle de gestion de la qualité et de la publication des données, et de veiller à ce que les mécanismes de révision des données soient opérationnels. Il est important d'impliquer les prestataires de soins dans le processus pour qu'ils comprennent les indicateurs et qu'ils puissent contribuer à leur détermination. De plus, il convient d'impliquer le ministère et les décideurs politiques dans le processus afin qu'ils comprennent les différences fondamentales entre la manière dont les rapports étaient établis auparavant et maintenant avec un Tracker ou un registre électronique.

**Intégration dans le SNIS**

Les données saisies dans le Tracker constituent la base pour la génération de chiffres agrégés. Le tracker doit faciliter la tâche du système d'agrégation, plutôt que d'être une contrainte supplémentaire pour les collecteurs de données. La conception du système doit prendre en compte les exigences relatives aux données agrégées, en utilisant les données saisies via le tracker. En d'autres termes, le flux de travail doit éviter aux agents de santé un surplus de travail. Ces derniers ne devraient pas agréger et saisir les données manuellement dans le SNIS.

La différence entre les systèmes de collecte de données agrégées, où les chiffres finaux sont saisis dans des formulaires de rapport en ligne, et un tracker ou registre électronique qui effectue des rapports automatisés est que la conception du logiciel nécessite beaucoup plus d'effort pour couvrir tous les besoins concernant les rapports et les indicateurs. Il est important de définir ce que sont les indicateurs et de comprendre ce qui doit être mesuré, y compris le numérateur et le dénominateur.

La suppression des rapports sur papier peut prendre du temps, de même que le changement des habitudes. Il est important de s'assurer que les prestataires de soins comprennent les indicateurs et soient en mesure de participer à leur calcul. De plus, il convient d'impliquer le ministère et les décideurs politiques dans le processus afin qu'ils comprennent les différences fondamentales entre la manière dont les rapports étaient établis auparavant et maintenant avec un registre électronique.

> *Références* :
>
> Venkateswaran M : Attributs et conséquences des données des systèmes d'information sanitaire pour les soins prénatals - état de santé, performance et politique du système de santé, thèse de doctorat, Université de Bergen.
>
> Venkateswaran M, Mørkrid K, Khader KA, Awwad T, Friberg IK, Ghanem B, Hijaz T, Frøen JF : Comparaison entre les données cliniques individuelles des registres prénataux et les indicateurs des systèmes d'information de santé de routine pour les soins prénataux en Cisjordanie : Une étude transversale. PloS one 2018, 13(11) : e0207813

