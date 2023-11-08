---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/design-objectives-and-ideation.md"
revision_date: '2023-05-24'
tags:
- Implémentation
---

# Objectifs de la Conception et de l'Idéation { #design-objectives-and-ideation } 


## Introduction au guide de conception du système Tracker{ #introduction-to-the-tracker-system-design-guide } 

Ce guide présente certains des principes de conception fondamentaux permettant de créer des programmes Tracker utiles. La conception des programmes Tracker varie considérablement en fonction du cas d'utilisation et du contexte national du HIS (système d'information sanitaire). Ce guide est **produit pour traiter la majorité des cas d'utilisation dans le vaste domaine des services de santé qui suit les "personnes "**, bien que de nombreux principes génériques décrits s'appliquent également à la surveillance basée sur les cas, la logistique, l'éducation et d'autres domaines.

Le guide narratif qui suit sectionne le processus complexe de conception d'un tracker en cinq éléments interconnectés : **l'idéation formative, la définition de l'entité suivie, la structure des étapes du programme, l'analyse du tracker et la conception de l'interaction** Le guide suppose que votre équipe a déjà clairement défini la portée du projet et l'énoncé du problème, c'est-à-dire que vous savez quels problèmes spécifiques vous essayez de résoudre avec le Tracker. Toutefois, les processus de numérisation sont rarement linéaires : les conceptions et prototypes itératifs du programme Tracker nécessiteront probablement de revoir vos exigences en matière d'analyse ou de saisie de données, d'évaluer les compromis et d'explorer de nouvelles approches.

Pour plus d'informations sur comment naviguer dans l'application de maintenance DHIS2 afin d'effectuer les tâches de configuration décrites, veuillez vous référer au [Guide de l'utilisateur DHIS2].(#configure_programs_in_maintenance_app) Un bref résumé du modèle de données du Tracker est disponible dans la documentation [ici](https://docs.dhis2.org/en/topics/training-docs/tracker-use-academy/tracker-data-model/tracker-data-model-session-summary.html) et est présentée sur Youtube [ici](https://www.youtube.com/watch?v=bQFJ1TYB4Cc&list=PLo6Seh-066Rwew5Dh50otwA0__hCDYdwQ&index=3). For a step-by-step guided exercise on configuring Tracker from scratch, you can check the[ Trainer’s Guide to Creating a Tracker Program](https://docs.dhis2.org/en/topics/training-docs/tracker-config-course/traineraposs-guide-to-creating-a-tracker-program.html). 

Pour en savoir plus sur les stratégies d'implémentation de Tracker et les bonnes pratiques, veuillez vous référer au **Guide d'implémentation de Tracker**.


## Objectifs de la Conception du Tracker { #objectives-of-tracker-design } 

Dans le cadre de la numérisation des soins de santé, l'enregistrement des données individuelles via DHIS2 Tracker vise au moins trois objectifs majeurs : l'amélioration des **résultats analytiques**, la **structuration des flux de travail** de la prestation de services et une **expérience satisfaisante pour l'utilisateur** lors de la collecte régulière des données.

Dans certains domaines de la conception de systèmes, ces objectifs peuvent fonctionner de pair, mais ils présentent souvent des priorités et des perspectives compétitives.


![Objectifs de Conception](resources/images/objectives_drawing.jpg "Équilibrer les Objectifs du Tracker"){ .largeur centrale=80%}

Supposons, par exemple, qu'un agent de santé saisisse les données d'un patient concernant sa visite mensuelle pour hypertension et son traitement médicamenteux. L'agent de santé du district souhaite que ce programme indique le nombre total de patients dont la tension artérielle n'est pas contrôlée, répartis en fonction des données démographiques et des comorbidités telles que le diabète, afin de savoir comment allouer les ressources. Le responsable de l'établissement de santé insiste sur le fait que le patient ne peut recevoir des médicaments contre le diabète qu'une fois que le nouveau diagnostic a été confirmé par un résultat de laboratoire. L'agent de santé, qui a cinquante cas à enregistrer aujourd'hui, a répondu à une douzaine de questions complexes sur le statut du patient, mais doit attendre les résultats du laboratoire de diabète pour saisir les données relatives aux médicaments dans Tracker. Il peut préférer simplement conserver un document Word avec ses notes pour chaque patient reçu, et faire un décompte manuel pour les nouveaux patients atteints de diabète.

L'objectif final de la conception d'un "programme tracker" est donc de fournir une solution socio-technique qui réponde suffisamment à ces trois objectifs. Le concepteur doit s'efforcer de comprendre chaque point de vue et de gérer les tensions qui apparaissent au cours du processus de conception.




## Phase d'Idéation Formative { #formative-ideation-phase } 


![](resources/images/image0.png "Step1")


Au cours de la [phase formative de l'implémentation du tracker] (https://docs.dhis2.org/en/implement/tracker-implementation/build-your-tracker-programs.html#design-and-configuration-process), vous devez consulter fréquemment les utilisateurs finaux et les principales parties prenantes du programme au sein du système de santé. Les questions posées lors des entretiens, les visites sur le terrain et les groupes de discussion vous donneront une idée du flux de travail clinique actuel pour la gestion du diagnostic, du traitement et des soins des patients, ainsi que du flux de données dérivées des patients depuis l'établissement au niveau national. L'objectif ici est de créer une vue d'ensemble détaillée des pratiques actuelles de déclaration au sein du système de santé, puis d'explorer, de définir et d'"imaginer" différentes interventions sociales et techniques dans le cadre du projet qui sont liées à la collecte systématique de données au niveau individuel.

Cette phase implique la compréhension des compétences techniques et des tâches des agents de santé, des données qu'ils collectent régulièrement, de leur flux de travail clinique, du rôle des gestionnaires de données et des superviseurs, ainsi que d'autres rapports de routine utilisés par les décideurs. Des cadres utiles pour structurer ce type d'informations sont présentés dans la boîte à outils du projet de numérisation du DHIS2 Design Lab (https://www.mn.uio.no/hisp/english/dhis2-design-lab/digitalization-project-toolkit/). Les kits d'adaptation numérique de l'OMS fournissent également des exemples de Personas d'utilisateurs génériques, de scénarios d'utilisateurs et de flux de travail génériques.

Il est très important de collecter les formulaires papier ou électroniques existants dans le cadre de votre projet afin de comprendre quels types de données individuelles sont actuellement collectées, quels indicateurs sont requis aux niveaux national et sous-national et comment les établissements gèrent leurs registres au quotidien. Vous devez être en mesure de décrire comment les données importantes sont régulièrement enregistrées, traitées et transférées, à partir de multiples perspectives.


### Diagramme sur la Procédure de Rapport Actuelle { #diagram-current-reporting-procedure } 

À la fin de vos entretiens, vous devriez être en mesure de décrire ces perspectives en tant que processus opérationnels et d'illustrer ces processus à l'aide de **diagrammes de flux**. Les exemples ci-dessous illustrent divers processus opérationnels pour l'enregistrement et la communication des _données de cas de Covid-19 :



* un **flux de travail des services clients** ou un diagramme de "parcours du patient", décrivant comment les personnes passent d'un prestataire de services à l'autre en fonction des résultats de leurs tests ou de leurs traitements, du point de vue de la personne. Exemple : [CDC Interim Guidance on Covid-19 Case Investigation (2020)] (https://www.researchgate.net/figure/Client-Flow-for-Integrated-EPI-Family-Planning-Services_fig2_273133507). Voir également un exemple de planification familiale et de PEV : [_Successful Proof of Concept of Family Planning and Immunization Integration in Liberia,_ Cooper et al. Global Health Science and Practice 2015](https://www.researchgate.net/figure/Client-Flow-for-Integrated-EPI-Family-Planning-Services_fig2_273133507).
* un **diagramme de flux de travail du registre** décrivant comment l'enregistrement d'un dossier individuel est traité par différents prestataires de services ou gestionnaires de données, en fonction des différentes voies de dépistage, de traitement et de prise en charge. Exemple: [DHIS2 Metadata Toolkit [DHIS2 Metadata Toolkit for a Covid-19 Case Surveillance Tracker program](https://docs.dhis2.org/en/topics/metadata/covid-19-surveillance/covid-19-case-surveillance/design.html#workflow-covid-19-case-surveillance-tracker)
* un **graphique de flux de données** montrant les types et la fréquence des données qui sont systématiquement échangées entre les institutions de santé concernées ou entre les juridictions. Exemple : [CDC Covid-19 Case Surveillance FAQ ] (https://www.cdc.gov/coronavirus/2019-ncov/images/case-surveillance.jpg?_=67746?noicon)
* [en cas de rapport provenant de cliniques] un **algorithme clinique**, ou un "arbre de décision", illustrant l'ordre dans lequel un agent de santé donné doit recueillir des informations sur le patient, procéder au dépistage, au triage, au diagnostic et/ou à la prestation de services pour une pathologie spécifique. Exemple : [_Adoption of COVID-19 triage strategies for low-income settings,_ Ayebare et al. The Lancet Respiratory Medicine, March 2020](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600%2820%2930114-4/fulltext)

> **Astuce**
>
> Outils recommandés pour les diagrammes de flux : Stylo/papier, Excel/Powerpoint, diagrammes.net, draw.io, Miro, lucidchart, etc.

Après avoir revu les diagrammes de flux avec les parties prenantes du programme, vous devriez être en mesure d'identifier les exigences en matière de collecte de données pour votre système Tracker, à savoir les indicateurs de rapport essentiels, les indicateurs de S&E du programme, les identifiants personnels, les listes de questions et les listes d'options. Il est donc important de se concentrer sur la documentation des points de données les plus essentiels pour toutes les parties prenantes et de créer une liste distincte d'indicateurs demandés et facultatifs "intéressants à avoir" pour les examiner ultérieurement. Les exigences en matière de collecte de données peuvent être documentées dans Excel ou un outil similaire à ce stade précoce, avant de configurer un prototype dans DHIS2.


### Mapping des Concepts du Système de Santé au Tracker DHIS2 { #mapping-health-system-concepts-to-dhis2-tracker } 

Vous êtes maintenant prêt à commencer à dessiner la structure du système Tracker DHIS2.

En examinant les diagrammes décrits ci-dessus, vous devriez être en mesure de " mapper " ces concepts de système de santé avec leurs équivalents dans DHIS2.


|Concept du Système de Santé|Représentation du Tracker DHIS2|
|--- |--- |
|Client, Patient ou Cas Suspect|Instance d'entité suivie (personne ou cas)|
|Dossier du cas|Inscription|
|Identifiant du patient|Attribut d'instance de l'entité suivie|
|Rencontre|Événement|
|Rendez-vous|Événement programmé|
|Champ de formulaire/ Variable de données|Élément de données|


Pour une présentation complète de la terminologie du modèle de données des trackers, voir la [documentation de l'Académie d'utilisation des trackers].(https://docs.dhis2.org/en/topics/training-docs/tracker-use-academy/tracker-data-model/tracker-data-model-session-summary.html).

