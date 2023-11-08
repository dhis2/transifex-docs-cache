---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/tracker_implementation/is-my-project-ready-for-tracker.md"
revision_date: '2021-09-21'
tags:
- Implémentation
---

# Mon projet est-il prêt pour le Tracker ? { #is-my-project-ready-for-tracker }

## Questions sur l'état de préparation et les principaux points à prendre en compte { #readiness-questions-and-key-considerations }

Cette section a pour but de décrire certaines des conditions clés du milieu qu'il convient de bien comprendre avant de procéder à l'implémentation d'un système Tracker. Étant donné que de nombreux pays où Tracker est introduit utilisent déjà DHIS2 pour le HMIS national ou d'autres agrégats, il est important de souligner certaines des principales différences entre DHIS2 Tracker et les systèmes d'agrégats, afin de planifier de manière appropriée les changements qu'il pourrait être nécessaire d'apporter à l'implémentation et à l'administration.

Les programmes Tracker élargissent souvent la portée du système d'information, en l'étendant à des utilisateurs qui n'utilisaient pas auparavant un système d'information électronique quel qu'il soit. De manière inhérente, les données individuelles requièrent des considérations supplémentaires en matière de confidentialité et de sécurité des données. Ces deux facteurs signifient que l'implémentation d'un programme Tracker nécessite généralement :

- des efforts de formation à grande échelle parmi les catégories de travailleurs susceptibles d'avoir des taux de rotation élevés ; 
- l'accent mis sur l'acceptation par l'utilisateur et sur le mapping avec les pratiques de travail existantes ;
- du matériel supplémentaire pour la saisie des données, notamment la gestion de ce matériel sur le long terme ;
- une couverture réseau fiable et/ou des stratégies pour remédier à une connexion intermittente ;
- une sensibilisation et une capacité accrues en matière de protection de la vie privée et de la sécurité ;
- une plus grande capacité d'assistance informatique pouvant résoudre les problèmes d'un plus grand nombre d'utilisateurs, répartis sur un territoire plus vaste.

Ces recommandations, ainsi que d'autres, seront examinées plus en détail dans les sections ci-dessous. La série de questions suivante peut être utile lors de l'évaluation initiale de l'état de préparation à l'implémentation d'un nouveau Tracker. **En particulier, si votre cas d'utilisation implique la collecte de données personnelles identifiables (liées à la santé ou autres), vous devriez examiner les questions suivantes et y réfléchir avant de commencer**.

- Y a-t-il une *volonté politique et institutionnelle* d'entreprendre l'implémentation d'une collecte de données individuelles à grande échelle au niveau du point de service ?

- Est-il possible de mettre en place un système de collecte de données effectives sur les lieux de soins, sans créer une charge de documentation supplémentaire pour les prestataires de soins ?

- Quelle est la *valeur ajoutée* et l'*utilisation significative* des données relatives au patient dans ce contexte ? Quelles sont les questions spécifiques auxquelles seules ces données peuvent répondre ?

- Comment les données seront-elles utilisées pour prendre des décisions importantes par les prestataires de soins, les responsables et les décideurs politiques ?

- Y a-t-il des lois et des règlements en place pour la collecte, le stockage et l'utilisation des données individuelles et des données permettant l'identification des personnes ? Par ailleurs, y a-t-il des mécanismes permettant de s'assurer que de telles lois seront en place dans un avenir proche ?

- Y a-t-il un financement suffisant et pérenne, des ressources et des capacités humaines pour la conception, l'implémentation (informatique et internet), la formation, la maintenance, la gestion des données et le suivi du système ?

- Y a-t-il un moyen d'identifier les clients de manière unique dans le cadre du système de santé ?

- Comment les dossiers des patients identifiables sont-ils actuellement collectés et diffusés sur un support papier ?

- Y a-t-il des lignes directrices cliniques/interventions cliniques ou au moins une forme d'orientation pour la pratique clinique ? Y a-t-il une liste des éléments à signaler dans le HMIS et leurs définitions détaillées ?

- Comment les données relatives aux établissements et aux patients sont-elles actuellement collectées, gérées et partagées au sein du système de santé ?

*Références*:

1.  Liste de contrôle mERA: [https://www.bmj.com/content/352/bmj.i1174](https://www.bmj.com/content/352/bmj.i1174)
2.  Principes du Développement Numérique
3.  Informatique de Santé Publique - une perspective des pays en voie de développement: [https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&](https://global.oup.com/academic/product/public-health-informatics-9780198758778?cc=ps&lang=en&)


## Considérations générales{ #general-considerations }

### Adhésion et soutien des institutions { #institutional-buy-in-and-support }

**Assurez-vous de l'adhésion et du soutien des institutions dès le début de votre projet** pour créer un engagement à long terme. Un projet Tracker est étroitement lié à la pratique du travail et à la gestion des données et nécessitera du temps, de l'attention et des ressources. Il modifiera les pratiques de travail sur le terrain dans un sens positif s'il est bien mené et dans un sens négatif s'il est mal mené. Il est donc essentiel que le projet bénéficie d'un soutien solide de la part des principales parties prenantes, telles que les responsables de programme, les unités informatiques, les chefs de service, etc. Ce groupe de travail sera habilité à prendre des décisions telles que le remplacement de certains niveaux de rapports papier ou l'adaptation des processus de supervision pour répondre aux nouveaux indicateurs clés de performance rendus possibles par la saisie et l'analyse des données au niveau individuel.

Identifier la division/le département de l'organisation de santé concernée (ministère de la santé, établissement de santé publique, etc.) ayant un potentiel de croissance durable pour accueillir une équipe de développement administratif de base à long terme. Mobiliser les services concernés qui devraient être impliqués, tels que ceux qui travaillent à la collecte et à la gestion des données et à l'informatique, ainsi que les responsables de la politique de santé et les implémenteurs qui peuvent fournir des informations sur les flux de travail des agents de santé. Obtenir un accord sur le fait que le groupe de travail n'est pas destiné à se dissoudre à la fin de l'extension, mais qu'il doit plutôt se transformer en administrateurs et gestionnaires de systèmes à long terme.

Avant de s'engager dans un projet Tracker à grande échelle, il convient d'examiner le cadre de financement pour les investissements importants et à long terme nécessaires à la durabilité, en particulier en ce qui concerne l'acquisition des appareils, les coûts permanents du réseau et la formation, à la fois au début du projet et la formation de routine au fil du temps pour les nouveaux utilisateurs. Les objectifs et les ressources allouées par les mécanismes de financement sont-ils alignés avec le groupe responsable de la mise en œuvre de Tracker ? L'introduction de Tracker remplacera-t-elle des coûts dans d'autres domaines, tels que l'impression de formulaires de rapport, qui peuvent être reprogrammés une fois que le système est adopté et fonctionne bien ?

Examinez comment le tracker pourrait affecter et potentiellement apporter des améliorations à tous les niveaux, et pas seulement aux utilisateurs finaux. Par exemple, un programme Tracker qui correspond au flux de travail clinique pour le traitement antirétroviral pourrait être conçu pour apporter des avantages à la personne sous traitement, grâce à des rappels de rendez-vous et à un dossier clinique partagé entre les sites de traitement ARV. Il pourrait apporter des avantages au prestataire de soins en automatisant certains aspects de ses rapports et en fournissant une aide à la décision. Il pourrait être bénéfique pour le superviseur en fournissant des informations concrètes sur les performances et les défis basés sur les données ; et il pourrait être bénéfique pour les gestionnaires de programmes en ajoutant non seulement des données en temps réel, mais aussi en introduisant de nouveaux types d'indicateurs, tels que ceux basés sur la rapidité ou la qualité, en raison des possibilités offertes par les données au niveau individuel.

La conception axée sur ces résultats permet non seulement d'accroître considérablement la valeur du système, mais aussi de garantir l'adoption et la satisfaction des utilisateurs, et peut apporter des améliorations significatives à la prestation des soins de santé. Ce type de caractéristiques peut également contribuer à obtenir l'adhésion des donateurs et le financement de plusieurs d'entre eux, car le système peut satisfaire des objectifs multiples.



*Références*:

 - [Principes de l'Alignement des Donateurs pour la Santé Numérique](https://www.ictworks.org/principles-donors-digital-health/#.XXtj2SiF7mE)
  - [Principes du Développement Numérique](https://digitalprinciples.org/)


### Financement{ #funding }

**Assurer un financement durable pour le développement, l'implémentation, la formation et le soutien continu** tout au long du cycle de vie des projets trackers. L'implémentation d'un tracker nécessite un financement dans les phases suivantes :

- Collecte et développement des besoins
- Formation de l'équipe informatique de base, du personnel administratif et des gestionnaires de programmes, en particulier s'ils ne sont familiers qu'avec les rapports agrégés.
- Achat et remplacement de dispositifs et de solutions de sauvegarde (dispositifs alternatifs et papier)
- Déroulement / mise à l'échelle
- Formation des utilisateurs finaux, avec indemnités journalières et salaires des travailleurs.
- Coûts de connectivité (internet) et de SMS, le tracker peut nécessiter des investissements dans l'infrastructure afin de le maintenir sur le terrain.
- Assistance informatique au niveau de l'utilisateur final
- Hébergement
- Poursuite de l'évaluation et de la maintenance du programme tracker
- Formation(s) de recyclage

L'expérience acquise lors de l'implémentation de systèmes tracker montre que le lancement et le déploiement de projets Tracker constituent la phase la plus exigeante en termes de ressources. La conception d'un programme Tracker complexe modélisant les flux de travail cliniques et remplaçant les rapports papier peut prendre un an, tout comme l'obtention d'une adhésion et d'un soutien adéquats. Les formations nationales de milliers d'utilisateurs nécessitent beaucoup de ressources. La fourniture de nouveau matériel, tel que des appareils Android ou des ordinateurs portables, nécessite un investissement important. L'embauche et la formation du personnel supplémentaire au sein de l'unité informatique pour gérer une forte augmentation du nombre d'utilisateurs nécessitent une augmentation des budgets.

Au fil du temps, les coûts les plus importants sont liés à la formation de recyclage et à l'assistance permanente aux utilisateurs. Pour garantir une implémentation durable du tracker, il est crucial que le financement soit assuré non seulement jusqu'à la mise à l'échelle, mais aussi pour couvrir les coûts de routine à l'avenir. En général, les projets ne sont pas pérennes lorsque les fonds alloués à une équipe informatique suffisamment étoffée et/ou à la maintenance et à la formation continue sont insuffisants.

Les coûts liés à la mise en place de systèmes individuels peuvent être quelque peu compensés par l'amélioration des processus, la réduction des budgets consacrés à l'impression et au transport des formulaires papier, l'amélioration du respect des lignes directrices et des mécanismes d'orientation, etc. Ceci dit, la numérisation des processus de travail actuels est un investissement à long terme et il faut envisager dès le départ de tels projets comme un changement dans la pratique courante, nécessitant un soutien continu.

*Références*:

 - Ensemble Didactique - Formation ([http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf](http://eregistries.org/wp-content/uploads/2017/11/05-training.pdf))
 - Registres d'Évaluation des Résultats des Patients : Guide de l'utilisateur [Internet]. 3e édition. [https://www.ncbi.nlm.nih.gov/books/NBK208631/](https://www.ncbi.nlm.nih.gov/books/NBK208631/)

### Législation et politiques { #legislation-and-policies }

Avant de déployer Tracker, il est important d'examiner la législation et les politiques locales, nationales et internationales en matière de protection de la vie privée et de gestion des données. La collecte de données individuelles est catégoriquement différente de celle de données agrégées et exige une plus grande attention à la protection de la vie privée et à la sécurité. En l'absence de politiques nationales bien définies, des lignes directrices sur la sécurité et la confidentialité des données - à la fois techniques et administratives - doivent être élaborées et approuvées. Les pratiques appropriées qui doivent être claires et documentées vont de l'accès aux données aux exigences en matière d'hébergement, en passant par les pratiques des utilisateurs.

De nombreuses données relatives à la santé des personnes peuvent avoir de graves conséquences si la vie privée n'est pas protégée. Par exemple, dans les pays où il est illégal ou culturellement inacceptable d'être une femme enceinte non mariée, une violation de ces informations pourrait porter préjudice à la personne et à sa famille. Si le client n'est pas sûr que ses données seront correctement protégées, il risque de ne pas parler ouvertement de ses problèmes de santé avec son prestataire de soins, ce qui réduira la qualité du traitement. Les données personnelles identifiables peuvent être exploitées à des fins politiques ou pour identifier des individus appartenant à des groupes systématiquement marginalisés.

Plusieurs domaines spécifiques doivent être examinés au cours de la phase de planification de l'implémentation d'un système Tracker. Comme indiqué dans l'outil d'analyse de la situation des registres électroniques [eRegistries Situation Analysis Tool ](http://eregistries.org/wp-content/uploads/2017/06/Situation-Analysis.pdf), il existe cinq domaines sur lesquels il convient de se focaliser :

1. comprendre le paysage juridique
2. la gestion actuelle des registres de santé
3. les orientations, la législation et les pratiques actuelles associées à la collecte et au stockage des données
4. exigences en matière de surveillance et de rapports
5. les implications éthiques et sociales existantes et potentielles

Les politiques peuvent être radicalement différentes d'un pays à l'autre, et il est extrêmement important de les évaluer localement au début de chaque projet Tracker. Il est également essentiel d'obtenir le soutien local pour les politiques de protection de la vie privée. L'expérience a montré que même un document juridique bien conçu, élaboré à l'extérieur, sans l'aval des autorités locales, peut être mis de côté et ne pas être utilisé parce que les organisations locales n'ont pas été impliquées dans son élaboration et n'a pas été traduit dans la langue locale. L'utilisateur final doit être pris en compte dans tous les aspects de l'implémentation d'un Tracker - notamment en ce qui concerne la législation et les politiques.

Les données au niveau individuel ont une valeur significative pour la recherche et l'analyse futures, longtemps après leur collecte. Un article du [2018 IMIA Yearbook of Medical Informatics] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6115206/?report=reader#!po=43.3333) montre que le nombre de demandes d'accès aux dossiers médicaux est en augmentation. Pour aider à garantir une bonne gestion des données sensibles à l'avenir, il faut envisager d'établir des procédures pour les accords de partage de données, s'ils ne sont pas déjà stipulés au niveau local. Cela permettra de maintenir une approche systématique et équitable des demandes d'information et de leur utilisation - qu'elles émanent d'un organisme de recherche, d'un donateur ou d'une autre partie intéressée. Dans les situations où il n'existe pas ou peu d'orientations, il est recommandé de répondre aux préoccupations exposées dans le [kit de gouvernance des e-répertoires] (http://eregistries.org/wp-content/uploads/2017/08/eregistries-governance-toolkit.pdf) et d'obtenir l'adhésion des pouvoirs publics aux politiques courantes en matière de partage des données et d'accès à celles-ci.

Une bonne planification du projet prévoit du temps et des ressources pour identifier les politiques, procédures et protocoles essentiels en matière de protection de la vie privée et de sécurité. La boîte à outils de gouvernance des registres électroniques fournit des conseils pratiques sur la manière de franchir ces étapes. Un examen approfondi, avec les parties prenantes locales, des données qui seront collectées et de la manière dont elles pourraient être utilisées à mauvais escient peut contribuer à faire avancer le processus. Il est également important d'identifier un calendrier de révision de votre plan de protection de la vie privée, car les politiques changent au fil du temps. Se tenir informé de ces changements vous aidera à mieux planifier le développement, l'implémentation et la maintenance de Tracker.

Des détails spécifiques sur les fonctions de confidentialité du logiciel Tracker et des conseils pour une configuration correcte peuvent être trouvés dans les [guides d'utilisation et d'implémentation du DHIS2](https://docs.dhis2.org/2.33/en/index.html).

*Références*:

 - [Boîte à outils d'orientation relative à la gouvernance](http://eregistries.org/wp-content/uploads/2017/08/eregistries-governance-toolkit.pdf)
 - [Boîte à outils relative à l'analyse de la situation](http://eregistries.org/wp-content/uploads/2017/06/Situation-Analysis.pdf)
 - [Frost MJ, Tran JB, Khatun F, Friberg IK, Rodriguez, DC : Que faut-il pour être un gestionnaire national efficace de l'intégration de la santé numérique pour le renforcement des systèmes de santé dans les pays à faible revenu et à revenu intermédiaire ? Santé mondiale : Sciences et pratiques 2018, Vol 6, Supplément 1] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6203416/pdf/S18.pdf)
 - [Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF : les registres électroniques de la santé de la mère et de l'enfant. BMC pregnancy and childbirth 2016, 16(1):279](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035445/)
 - [Kloss L, Brodnik, M, Rinsehart-Thompson, L : Accès et divulgation des informations de santé personnelles : A Challenging Privacy Landscape in 2016-2018. IMIA Yearbook of Medical Informatics 2018, 60-66](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6115206/?report=reader#!po=43.3333)
 -  La boîte à outils 2012 de l'OMS et de l'Union internationale des télécommunications (UIT) pour les stratégies nationales en matière de santé en ligne http://apps.who.int/iris/handle/10665/75211
 - Feuille de route 2015 pour la surveillance et la responsabilisation en matière de santé https://www.who.int/hrh/documents/roadmap4health-measurement_accountability.pdf?ua=1Foundations


### Capacité et compétence{ #capacity-and-competence }

Compte tenu de la portée accrue de Tracker, à la fois en termes d'utilisateurs et de support informatique, il est important d'**évaluer et d'assurer une capacité suffisante et des compétences pertinentes** pour planifier, concevoir, développer, soutenir et utiliser le programme Tracker. Il est possible qu'il y ait des régions dans le pays où Tracker est adapté, et d'autres régions où il ne l'est pas, en fonction de la capacité des utilisateurs prévus et de leur accès au matériel et au réseau appropriés. Dans de nombreux cas, il est préférable de déployer Tracker par étapes, plutôt que d'essayer de l'introduire comme un système de routine dans des zones ou avec des utilisateurs qui ne sont pas préparés. Il convient de procéder à une évaluation avant d'élaborer le plan de déploiement, afin d'orienter l'extension et la portée du système en fonction de sa pertinence.

Le groupe de travail des principales parties prenantes décrit dans la section **Adhésion et soutien de l'institution** doit être impliqué dès le début afin d'évaluer le groupe d'utilisateurs auquel le système sera destiné, de déterminer quel service sera responsable du soutien à long terme, qui sera chargé d'assurer la formation, à la fois au début et au fil du temps, etc.

Une formation supplémentaire peut être nécessaire pour l'unité informatique, afin d'accroître sa capacité à gérer correctement les données personnelles identifiables, ou de fournir une assistance pour tout nouveau matériel fourni.

Les outils et les tableaux de bord configurés dans Tracker doivent être conçus avec les utilisateurs cibles afin de s'assurer qu'ils sont appropriés et acceptés.

La formation des utilisateurs peut nécessiter non seulement des programmes spécifiques pour le système, mais aussi une formation générale sur l'utilisation, la maintenance et le dépannage du matériel et de l'accès au réseau. Des outils de travail simples et l'accès à une assistance informatique de premier niveau doivent être développés et mis en place afin d'augmenter le nombre de besoins des utilisateurs qui peuvent être traités en dehors de l'équipe centrale.


*Références et Ressources*:

- Myhre SL, Kaye J, Bygrave LA, Aanestad M, Ghanem B, Mechael P, Frøen JF : Registres électroniques : gouvernance pour les registres électroniques de santé maternelle et infantile. BMC pregnancy and childbirth 2016, 16(1):279
- [Kit d'apprentissage en développement de logiciels](http://eregistries.org/learning-packages/)
- [Boîte à outils d'orientation sur la gouvernance](http://eregistries.org/learning-packages/)
- [Principes du Développement Numérique](https://digitalprinciples.org/)


### Infrastructure { #infrastructure }

Il est important de garantir une infrastructure appropriée et suffisante, qui peut être différente pour Tracker que pour d'autres systèmes numériques existants. Il existe trois groupes d'infrastructures nécessaires :

**Électricité et réseau** Dans les régions où le réseau est stable, l'utilisation de Tracker via le navigateur d'un ordinateur portable ou d'un ordinateur de bureau est appropriée. Les données du navigateur sont envoyées instantanément au serveur, sans stockage local en dehors du cache du navigateur. Cela permet de garantir la fidélité des données et de tirer parti de la puissance de calcul du serveur. Dans les zones où la connectivité est intermittente ou faible, l'application DHIS2 Android est nécessaire pour utiliser Tracker, car elle crée une copie locale de la base de données et permet à l'utilisateur de continuer à travailler sans connexion directe au serveur central. Les projets basés sur Android impliquent des exigences supplémentaires en ce qui concerne l'accès à l'électricité pour la recharge, les coûts des SMS et des données, etc. Pour plus d'informations, consultez le document intitulé [DHIS2 Android App Implementation Guidelines] (https://www.dhis2.org/android-documentation).

**Serveurs et hébergement** Avec l'augmentation du nombre d'utilisateurs, la solution d'hébergement existante pour l'agrégat DHIS2 peut ne pas être adéquate, et les implémentations basées sur Android exercent une pression encore plus forte sur les ressources du serveur. Alors que pour les systèmes de rapports mensuels, il est parfois acceptable de s'attendre à des options d'hébergement peu performantes, les programmes Tracker qui soutiennent les processus de travail quotidiens ou les flux de travail cliniques nécessitent une disponibilité constante et une assistance informatique réactive en cas de problème. Il est particulièrement vital d'établir une sauvegarde de routine des données de suivi sur un site séparé, de manière à ce que la perte de données critiques sur le serveur principal puisse être rapidement résolue. Évaluez les méthodes d'hébergement actuelles, y compris le matériel et les ressources humaines disponibles, afin d'élaborer une approche pour l'implémentation de votre système de suivi. Il est recommandé que les programmes Tracker contenant des données personnelles identifiables soient hébergés dans un environnement distinct du système global, afin de garantir une plus grande sécurité. Bien que de nombreux pays hébergent actuellement des installations locales de DHIS2, il est intéressant d'envisager une option d'hébergement en nuage pour les programmes Tracker, où le matériel et l'assistance technique conformes aux normes de l'industrie peuvent être garantis au fil du temps.

**Matériel pour les utilisateurs finaux** En raison de l'adoption à grande échelle des projets de santé numérique, il est possible que le matériel existant disponible pour les utilisateurs ciblés soit suffisant pour l'implémentation d'un nouveau tracker. Une évaluation devrait être menée pour examiner la disponibilité des ordinateurs et des appareils Android, et déterminer si du matériel supplémentaire est nécessaire. Des accords à long terme pour la maintenance et le remplacement du matériel devraient être établis afin de garantir la durabilité du système Tracker au-delà de la durée de vie du matériel acheté initialement.

### Considérations en matière de sécurité{ #security-considerations } 

La sécurité est avant tout une question de personnes. Les personnes qui sont les sujets des données collectées ; les personnes qui utilisent les données ; les personnes qui sont responsables de l'application des mesures techniques ; et les personnes dont la responsabilité est de gérer la sécurité du projet tracker concerné.

Il ne suffit pas de supposer que les responsables de l'implémentation technique auront fait de leur mieux pour rendre le système aussi sûr que possible. Afin de respecter la réglementation et d'éviter tout risque juridique, il est généralement nécessaire de pouvoir démontrer que des mesures raisonnables ont été prises pour sécuriser le système. Au minimum, cela implique que : 

1.  Un rôle est défini au sein de l'organisation, dont la responsabilité est de s'occuper des questions liées à la sécurité. Il peut s'agir d'un chef de la sécurité, d'un responsable de la protection des données ou d'une autre personne. L'important est qu'il y ait une personne dont le travail consiste à se préoccuper des questions de sécurité et à en rendre compte. Idéalement, il ne s'agit pas d'un rôle technique, mais d'un rôle plus proche de la haute direction.
2.  Le programme Tracker doit faire l'objet d'un plan de sécurité documenté. Ce plan est parfois appelé posture de sécurité. Il doit indiquer les principes qui sont importants pour l'organisation et les processus qui sont en place pour identifier, surveiller et atténuer les risques de manière continue et variée. Le plan de sécurité peut inclure d'autres processus tels que les politiques d'utilisation acceptable (pour les employés), les accords de non-divulgation (pour les contractants), les politiques d'accès, les plans de sauvegarde et de reprise après sinistre, les normes minimales pour le déploiement et la configuration des logiciels, etc.

Dans certaines organisations, le rôle du responsable de la sécurité est déjà établi et bien défini. Dans beaucoup d'autres, il s'agit d'un besoin évolutif qui se manifeste dans un environnement caractérisé par l'absence d'une réglementation solide, la faiblesse des institutions informatiques et des structures de gestion, et le manque de formation appropriée. Il existe des normes et des méthodologies qui peuvent être utiles pour définir un tel rôle, telles que la série ISO27000 (y compris des documents gratuits [en ligne](https://www.iso27001security.com/html/toolkit.html) et des modèles utiles). Il ne s'agit pas d'un élément fréquemment mentionné dans les propositions de financement et de budget, mais la formation à la gestion de la sécurité pourrait bien être l'un des éléments les plus importants à prendre en considération et à budgétiser.

Une liste non exhaustive de tâches prioritaires à envisager :
1.  Assurez-vous que la configuration du logiciel est techniquement solide, documentée et de préférence automatisée. Il existe diverses stratégies permettant de répondre aux préoccupations en matière de sécurité, et quelques-unes d'entre elles sont décrites dans le guide d'installation du DHIS2. Pour les administrateurs système, participer à l'académie des serveurs est un bon moyen de rencontrer des pairs et d'échanger des idées. Il est également possible d'interagir avec la communauté des administrateurs de serveurs par l'intermédiaire de la communauté de pratique. Il existe également un groupe télégramme d'administrateurs système DHIS2, qui peut s'avérer utile pour poser des questions et y répondre. (pour y participer, envoyez un courriel à Lamin - laminbjawara@gmail.com ).
2. assurez-vous d'avoir une équipe (au moins 2) d'administrateurs système qui sont responsables de la maintenance quotidienne du système. Le fait de dépendre d'une seule personne pour ce rôle est l'un des plus grands risques identifiés dans de nombreuses implémentations.
3.  Comme mentionné plus haut, quelqu'un DOIT être responsable de la sécurité. Ce rôle devrait :
- rendre compte directement à la direction
- gérer le risque global (le registre des risques est votre ami)
- s'assurer que les administrateurs système font leur travail
- connaître la législation, les contraintes et les procédures opérationnelles normalisées locales concernant le traitement des données et la protection de la vie privée. En leur absence, ou lorsqu'elles sont 
inadéquates, élaborer et tenir à jour des lignes directrices en matière de bonnes pratiques au niveau local.
4. Veiller à ce qu'il y ait un plan de sauvegarde, y compris hors site, qui soit régulièrement testé. La perte pure et simple de données irrécupérables est le problème de sécurité le plus courant dans les pays.
5. Les systèmes Tracker DHIS2 doivent faire l'objet d'un audit régulier. Cet audit peut être effectué officiellement par un auditeur général, de pair à pair au sein de la communauté DHIS2 ou en faisant appel aux services d'un auditeur externe. Les audits sont le meilleur moyen de s'assurer que les systèmes restent conformes aux politiques de sécurité.

