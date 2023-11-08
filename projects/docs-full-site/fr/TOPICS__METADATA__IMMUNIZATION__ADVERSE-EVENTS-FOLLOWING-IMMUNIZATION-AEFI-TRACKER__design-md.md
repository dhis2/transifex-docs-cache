---
edit_url: "https://github.com/dhis2-metadata/AEFI-TRK-Adverse_Events_Following_Immunization/blob/master/docs/adverse_events_following_immunization_aefi_tracker_design.md"
revision_date: "2022-02-04"
---

# Conception du système de suivi des manifestations adverses post immunisation (MAPI) { #aefi-design }

## Objectif { #purpose }

Le document sur la conception du système de suivi des manifestations adverses post immunisation (MAPI) donne un aperçu de la conception utilisée dans la configuration d’un programme de suivi servant à prendre en charge la notification, la déclaration et l’investigation des cas de MAPI aux niveaux national et infranational. Ce document est destiné à être utilisé par les responsables de la mise en œuvre du DHIS2 et les gestionnaires de données des programmes de vaccination pour être en mesure de soutenir le déploiement et la localisation du package. Les flux de travail locaux et les directives nationales doivent être pris en compte dans la localisation et l’adaptation de ce package de configuration.

## Contexte { #background }

Le package de données numériques sur les manifestations adverses post immunisation (MAPI) a été développé pour soutenir [l’Initiative mondiale pour la sécurité des vaccins (GVSI) de l’OMS.](https://www.who.int/vaccine_safety/initiative/en/) La gestion efficace et efficiente des MAPI est une composante essentielle de tous les programmes de vaccination afin d’assurer le maintien de la confiance du public envers la vaccination. Les MAPI sont calquées sur le [formulaire de notification et d’investigation de MAPI de l’OMS](https://www.who.int/vaccine_safety/initiative/tools/AEFI_reporting_form_EN_Jan2016.pdf) et permettent à l’utilisateur de saisir des données basées sur les cas à l’aide des [25 variables de base] recommandées par l’OMS (https://www.who.int/vaccine_safety/news/HL_1/en/), facilitent l’investigation des manifestations adverses et génèrent des données fiables pour la prise de décision. Le tracker MAPI vise à soutenir une approche durable de la surveillance de la sécurité des vaccins.

Les MAPI peuvent être adaptées pour le suivi de la sécurité des vaccins contre la Covid-19. Des discussions sont en cours avec des experts en contenu à l’OMS pour comprendre les exigences et l’intégration à cette conception.

## Présentation de la conception du système { #system-design-overview }

### Cas d’utilisation { #use-case }

Le modèle de données de suivi utilisé dans le DHIS2 permet de suivre un cas individuel de MAPI au fil du temps et d’établir un lien avec un identifiant unique. Ce programme permet aux prestataires de soins de santé, aux gestionnaires de programmes de vaccination et aux régulateurs aux niveaux infranational et national de signaler, d’accéder, de modifier et d’analyser les données sur les MAPI.

Le programme est conçu pour soutenir les flux de travail aux niveaux infranational et national afin de permettre la notification des manifestations adverses par les établissements, le remplissage de formulaires d’investigation de premier niveau par les agents de vaccination de district, et les enquêtes et résultats au niveau national. Ce [programme](https://drive.google.com/file/d/19iP8_G0Q2uAkJAhBR5xOz0PMTvuve9q0/view?usp=sharing) a également la capacité de fonctionner comme un référentiel national pour stocker, modifier et extraire des informations pour les décisions politiques et réglementaires et être le pivot autour duquel la performance de la surveillance locale des MAPI est évaluée.

Le package de suivi des MAPI comprend des indicateurs standard et un support de tableau de bord, qui sont remplis automatiquement pour faciliter l’analyse. De plus, il est possible de générer des notifications pour alerter les enquêteurs et favoriser une réponse rapide.

Ce programme est un programme autonome qui peut être adopté seul ou en combinaison avec d’autres programmes de suivi, y compris le package de suivi du registre électronique d’immunisation du DHIS2.

### Utilisateurs cibles { #intended-users }

Le programme de suivi des MAPI est conçu pour prendre en charge un flux de travail général pour les notifications et les investigations sur les MAPI. La première étape d’adoption du module consiste à identifier les utilisateurs et les rôles appropriés correspondant aux processus de votre pays. Les rôles suivants doivent être discutés et recensés avant l’adoption.

-   Personnel clinique et en établissement : des données minimales peuvent être collectées au point d’intervention ou par le personnel de l’établissement pour notifier et alerter le niveau suivant d’intervention et d’investigation.
-   Gestionnaires d’établissement, responsable de la vaccination de district/médecin de district : examinent et effectuent la saisie des données, et réalisent une analyse des données spécifiques au sous-district. Les listes de travail sont conçues pour aider le personnel à suivre les cas tout au long des étapes de l’investigation.
-   Agent du PEV de l’État/de la province, comité des MAPI de l’État/de la province : examinent et réalisent la saisie des données, effectuent également l’analyse spécifique au district, l’évaluation de la causalité et la génération de signaux.
-   Gestionnaire national du PEV, comité national MAPI, centre NRA/PV : examinent les données et effectuent une analyse spécifique à l’État/à la province ou au sous-État/à la province, aident à l’évaluation de la causalité et à la génération de signaux.
-   Utilisateurs de l’analyse des données à plusieurs niveaux : les données peuvent être ventilées par niveau hiérarchique et affichées sur des tableaux de bord appropriés aux niveaux de l’établissement, du district et à l’échelle nationale. Les chargés du contrôle sanitaire et les directeurs de programme peuvent également utiliser les données pour superviser et suivre la qualité des soins et les exigences en matière de documentation.

Bien que ce package soit conçu pour renforcer la surveillance de la sécurité des vaccins aux niveaux national et infranational, les 25 variables de base incluses ici faciliteront une notification de meilleure qualité dans les bases de données mondiales telles que Vigibase. L’inclusion de la cartographie des variables et de la norme E2B appliquée par Vigibase réduira encore la charge des notifications ascendantes.

Exemple de points d’entrée possibles pour les utilisateurs cibles

![Points d’entrée](resources/images/AEFI_Tracker_design_01.png)

### Structure du programme { #program-structure }

![Structure du programme des MAPI](resources/images/AEFI_Tracker_design_02.png)

### Flux de travail suite à un cas de MAPI { #workflow-following-an-aefi-case }

Le programme est conçu pour que le cas de MAPI soit inscrit dans l’unité d’organisation de l’établissement _où le cas présentant un MAPI a été vacciné_, même si les données sont saisies par les enquêteurs ou les déclarants d’un autre établissement. Cela permet d’analyser les manifestations adverses sur le site de vaccination. L’utilisateur qui saisit les données sélectionne le site de vaccination (par exemple, l’établissement) dans la hiérarchie des unités d’organisation et sélectionne le programme MAPI pour enregistrer le cas.

L’unité déclarante (l’établissement où le client a présenté des symptômes de manifestations adverses) est saisie en tant qu’élément de données dans la première étape du programme, avec le nom du formulaire « Adresse de l’établissement de santé déclarant ». En ce qui concerne les MAPI, la saisie des données est souvent effectuée au niveau du district, ce qui signifie que les utilisateurs de district (ou toute personne responsable de la saisie des données pour les investigations sur les MAPI) doivent avoir un accès en lecture/écriture à tous les sites de vaccination (établissements, postes de proximité, etc.) du district pour le programme de saisie des données sur les MAPI.

Dans les contextes où les établissements sont en mesure de déclarer directement les données initiales sur les cas de MAPI dans le DHIS2, il existe des scénarios probables où les manifestations adverses sont déclarées ou se présentent dans un établissement autre que le site de vaccination d’origine. Dans ces cas, l’unité déclarante envoie généralement des informations au site de vaccination ou à l’agent de district responsable afin de terminer la notification.

Dans les rares cas où le site de vaccination est situé dans un autre district, l’agent de vaccination de district responsable de l’unité déclarante est généralement censé demander à l’agent de district responsable du site de vaccination de déclarer les données.

Les flux de données nationaux et les procédures standard de notifications doivent être soigneusement pris en compte lors de l’adoption de ce programme pour permettre l’affectation des utilisateurs et l’accès en conséquence.

### Groupes d’utilisateurs { #user-groups }

Les trois principaux groupes d’utilisateurs suivants sont configurés et inclus dans le package de métadonnées :

-   Saisie des données MAPI
    -   Il peut s’agir d’utilisateurs tels que l’enquêteur MAPI
    -   Peut afficher les métadonnées
    -   Peut capturer des données pour toutes les étapes du programme
-   Accès aux MAPI
    -   Ces utilisateurs peuvent inclure des agents de surveillance, des agents de vaccination de district et des agents nationaux du PEV, et sont généralement chargés d’analyser les données.
    -   Peut afficher les métadonnées
    -   Peut afficher les données pour toutes les étapes du programme
-   Administrateur des MAPI
    -   Ces utilisateurs peuvent inclure l’unité principale du HMIS ou l’équipe d’assistance informatique qui a accès à la modification des métadonnées pour prendre en charge la localisation du package.
    -   Peut modifier les métadonnées
    -   Pas d’accès aux données.

En outre, trois autres groupes d’utilisateurs ont été configurés pour permettre aux notifications et à différents types d’utilisateurs d’afficher ou de capturer des données en fonction de leur rôle dans le processus d’investigation des MAPI en attribuant un accès basé sur _l’étape du programme_. Ceux-ci sont destinés à fournir un exemple de la manière dont une vue et une capture décentralisées des données pourraient avoir lieu avec des utilisateurs à différents niveaux (par exemple, le responsable du PEV de district responsable de l’investigation initiale par rapport au programme national chargé de l’examen des données de l’investigation).

-   MAPI – Niveau des districts
    -   Capture de données pour l’étape des MAPI
    -   Afficher les données pour l’étape de premier niveau de prise de décision et l’étape de niveau national
-   Prise de décision de premier niveau concernant les MAPI
    -   Afficher les données au stade des MAPI
    -   Capturer des données au premier niveau de prise de décision
    -   Afficher les données au niveau national
-   MAPI – Niveau national
    -   Afficher les données sur le stade MAPI et la première étape de prise de décision
    -   Capturer des données au niveau national

L’accès des utilisateurs doit être adapté au contexte local et attribué aux personnes appropriées selon la fonction professionnelle. Par exemple, les agents de vaccination de district peuvent être inclus dans le groupe d’utilisateurs de l’accès aux MAPI, mais n’ont accès qu’à leur district. En savoir plus sur la configuration des utilisateurs et la gestion des utilisateurs dans la [documentation du DHIS2.](https://docs.dhis2.org/master/en/dhis2_user_manual_en/manage-users-user-roles-and-user-groups.html)

### Logique de la structure du programme { #rationale-for-program-structure }

Les MAPI sont calquées sur le [formulaire de notification et d’investigation de l’OMS pour les MAPI](https://www.who.int/vaccine_safety/initiative/tools/AEFI_reporting_form_EN_Jan2016.pdf) et permettent à l’utilisateur de saisir des données basées sur les cas à l’aide des [25 variables de base] recommandées par l’OMS (https://www.who.int/vaccine_safety/news/HL_1/en/), facilitent l’investigation au sujet des manifestations adverses et génèrent des données fiables pour la prise de décision.

### Les 25 variables de base des MAPI{ #aefi-25-core-variables }

| VARIABLES DE BASE | DESCRIPTION | Nom et UID des métadonnées |
| --- | --- | --- |
| **Identité** |  |  |
| 1. Date à laquelle le centre national a reçu le premier signalement de la MAPI | Date de création de l’étape de niveau national pour le cas de MAPI I | MAPI – Date d'examen pour approbation au niveau national <br> cWMUoQEuvtR |
| 2. Pays où cette MAPI a été signalée | Le nom du pays où les données ont été saisies pour la première fois | « Pays où cette MAPI a été signalée » <br> [Capturé par le parent de la hiérarchie de l’unité d’organisation nationale] |
| 3. Lieu (adresse) | Emplacement géographique du cas (adresse) | Adresse (actuelle) <br> [attribut TEI] <br> VCtm2pySeEV |
| 4. Numéro unique mondial | Numéro unique utilisé pour communiquer les détails du cas au niveau international | MAPI – Classification finale <br> D42M2tdJo7R |
| **Identifiant du patient** |  |  |
| 5. Identifiant du patient | Le nom du patient ou ses initiales selon la décision du pays | Prénom <br> [attribut TEI] <br> TfdH5KvFmMy |
| 6. Date de naissance | Anniversaire | Date de naissance <br> [attribut TEI] <br> BiTsLcJQ95V |
| 7. Sexe | Masculin ou féminin | Sexe <br> [attribut TEI] <br> CklPZdOd6H1 |
| 8. Antécédents médicaux | Texte libre | MAPI – Antécédents médicaux <br> IV9W7YXh939 |
| **Vaccin** |  |  |
| 9. Nom du principal vaccin suspect (générique) | Le vaccin soupçonné d’avoir causé la MAPI | Nom du vaccin_MAPI 1 <br> uSVcZzSM3zg <br> Nom du vaccin_MAPI 2 <br> g9PjywVj2fs <br> Nom du vaccin_MAPI 3 <br> OU5klvkk3SM <br> Nom du vaccin_MAPI 4 <br> menOXwIFZh5 |
| 10. Autres vaccins administrés juste avant la MAPI | Autres vaccins administrés juste avant la MAPI | MAPI – Nom autre vaccin 1 <br> yr2dELskXm4 <br> MAPI – Nom autre vaccin 2 <br> dKWFXaSNIef <br> MAPI – Nom autre vaccin 3 <br> NmQkARV9bm4 <br> MAPI – Nom autre vaccin 4 <br> PDDaOMSiSDG |
| 11. Numéro de lot de vaccin | Numéro de lot de tous les vaccins mentionnés ci-dessus | MAPI – Numéro de lot (vaccin 1) <br> LNqkAlvGplL <br> MAPI – Numéro de lot (vaccin 2) <br> b1rSwGRcY5W <br> MAPI – Numéro de lot (vaccin 3) <br> YBnFoNouH6f <br> MAPI – Numéro de lot (vaccin 4) <br> BHAfwo6JPDA <br> [Eléments de données] |
| 12. Numéro de dose de ce vaccin particulier | Le numéro de dose du vaccin | MAPI – Dose de vaccin 1 <br> LIyV4t7eCfZ <br> MAPI – Dose de vaccin 2 <br> E3F414izniN <br> MAPI – Dose de vaccin 3 <br>WlE0K4xCc14 <br> MAPI – Dose de vaccin 4 <br> Aya8C25DXHe |
| 13. Numéro de lot de diluant | Le numéro de lot (le cas échéant) | MAPI – Numéro de lot de diluant 1 <br> FQM2ksIQix8 <br> MAPI – Numéro de lot de diluant 2 <br> ufWU3WStZgG <br> MAPI – Numéro de lot de diluant 3 <br> MLP8fi1X7UX <br> MAPI – Numéro de lot de diluant 4 <br> MyWtDaOdlyD |
| **Manifestation** |  |  |
| 14. Date et heure de la vaccination | Date et heure de la vaccination | MAPI_Date de vaccination 1 <br> dOkuCjpD978 <br> MAPI – Heure de vaccination 1 <br> BSUncNBb20j <br> MAPI_Date de vaccination 2 <br> VrzEutEnzSJ <br> MAPI – Heure de vaccination 2 <br> fZFQVZFqu0q <br> MAPI_Date de vaccination 3 <br> f4WCAVwjHz0 <br> MAPI – Heure de vaccination 3 <br> VQKdZ1KeD7u <br> MAPI_Date de vaccination 4 <br> H3TKHMFIN6V <br> MAPI – Heure de vaccination 4 <br> S1PRFSk8Y9v |
| 15. Date et heure d’apparition de la MAPI | Date et heure d’apparition de la MAPI | MAPI – Date de début de la MAPI <br> vNGUuAZA2C2 <br> MAPI – Heure de la MAPI <br> NyCB1VAOfJd |
| 16. Manifestations adverses | Diagnostic + signes et symptômes du cas | MAPI – Groupe d’éléments de données des manifestations adverses <br> yhXZIbQuxOt <br> Tous les éléments de données mappés dans ce groupe d’éléments de données |
| 17. Issue de la MAPI | Rétablie/résolue ; en cours de rétablissement/en cours de résolution ; non rétablie/non résolue ; rétablie/résolue avec séquelles ; fatale ; inconnue | MAPI – Issue de MAPI <br> yRrSDiR5v1M |
| 18. Gravité | Si la manifestation a entraîné la mort, menacé la vie du patient, causé une invalidité, une hospitalisation ou une anomalie congénitale | MAPI – Manifestation grave signalée <br> fq1c1A3EOX5 |
| **Déclarant** |  |  |
| 19. Nom du premier déclarant de la MAPI | Nom du premier déclarant de la MAPI | MAPI – Déclarant du cas de MAPI <br> uZ9c4fKXuNS |
| 20. Établissement/lieu | L’adresse du déclarant | MAPI – Adresse du déclarant <br> Q20pEixZxCs |
| 21. Fonction/Service | Désignation du déclarant | MAPI – Fonction/Service <br> Tgi4xP5DCzr |
| 22. Identifiant de messagerie | Identifiant de messagerie du déclarant | MAPI – Adresse de messagerie <br> UmXSiK5Jlr4 |
| 23. Numéro de téléphone du déclarant | Téléphone | MAPI – Coordonnées <br> iLaon1495vY |
| 24. Date du rapport | Date à laquelle le rapport a été soumis par le déclarant dans le DHIS2 | « Date de compilation du rapport » <br> [capturée par la date de la manifestation pour l’étape du programme MAPI] |
| **Autres** |  |  |
| 25. Commentaires (le cas échéant) | Texte libre | MAPI – Commentaires <br> LaMvzTltCOP |

### Configuration du programme de suivi { #tracker-program-configuration }

| Structure | Description |
| --- | --- |
| Inscription | Une fois qu’un enfant est identifié comme présentant une MAPI, il doit être inscrit au programme MAPI. L’étape d’inscription comprendra des informations personnelles et des identifiants uniques, dont certains seront générés automatiquement. <br> Date d’inscription = « Date à laquelle le patient a notifié la manifestation au système de santé », date à laquelle l’enfant est inscrit au programme MAPI. |
| Attributs | Les attributs incluent des informations sur l’enfant et les identifiants du cas <br> – Identifiant du cas MAPI <br> Identifiant système unique (PEV) <br> Prénom <br> Nom de famille <br> Sexe <br> Date de naissance <br> Adresse <br> Coordonnées de la mère/du soignant |
| Étape 1 : MAPI | Cette étape est une étape **non reproductible**. Les données de cette étape sont saisies lorsqu’une MAPI est signalée. Comprend des informations détaillées sur les MAPI et des éléments de données nécessaires à l’analyse. <br> Cette étape du programme comporte un formulaire personnalisé qui correspond au formulaire papier que les professionnels de la santé sont habitués à utiliser. <br> Date de la manifestation = « Date de compilation du rapport ». Il s’agit de la date à laquelle le formulaire MAPI est initié. Également DOR (Date of Report, ou date du rapport) dans l’analyse de la surveillance des MAPI. |
| Étape 2 : Premier niveau de prise de décision | Cette étape est une étape **non reproductible**. Les données de cette étape sont saisies lorsque le premier niveau de prise de décision est terminé. <br> Cette étape du programme comporte un formulaire personnalisé qui correspond au formulaire papier que les professionnels de la santé sont habitués à utiliser. <br> Date de la manifestation = « Date du rapport » Il s’agit de la date à laquelle le formulaire du premier niveau de prise de décision est initié. |
| Étape 3 : Niveau national | Cette étape est une étape **non reproductible**. Les données de cette étape sont saisies lorsque l’investigation au niveau national est terminée. <br> Cette étape du programme comporte un formulaire personnalisé qui correspond au formulaire papier que les professionnels de la santé sont habitués à utiliser. <br> Date de la manifestation = « Date du rapport » Il s’agit de la date à laquelle le formulaire au niveau national est initié. |

### Détails de l’inscription { #enrollment-details }

L’inscription d’un nouveau patient est un processus relativement simple. Lorsque vous saisissez des informations personnelles, le DHIS2 vous avertit s’il existe des patients potentiels en double. Une fois qu’une unité d’organisation est sélectionnée, elle est liée au patient.

La description de la date d’inscription est « Date à laquelle le patient a déclaré la manifestation au système de santé ». Il s’agit de la date à laquelle l’enfant a été inscrit au programme MAPI. Cette date est également utilisée comme DON (Date of Notification, ou date de notification) dans l’analyse de surveillance des MAPI.

L’unité d’organisation d'inscription sélectionnée doit refléter celle de l’établissement **_où le cas de MAPI (TEI) a reçu la vaccination,_** même si les données sont saisies par les enquêteurs ou déclarées dans un autre établissement.

![Capture d’écran de l’inscription avec les détails](resources/images/AEFI_Tracker_design_03.png)

### Attributs { #attributes }

Dans les pays où le registre électronique d’immunisation du DHIS est utilisé, la personne présentant la manifestation adverse est probablement déjà enregistrée en tant que TEI dans Tracker. Au fur et à mesure que l’utilisateur entre des attributs pour enregistrer l’inscription, le DHIS2 effectue une recherche et alerte l’utilisateur des correspondances possibles. L’utilisateur doit sélectionner la personne existante qui correspond et continuer la saisie des données afin de ne pas créer de TEI en double. De cette façon, la MAPI sera également liée au dossier de vaccination de l’individu qui peut être vu dans le programme du Registre d’immunisation.

Certains champs sont obligatoires pour réduire le risque de saisie de données erronées si un utilisateur n’est pas en mesure de saisir tous les champs de données. Bien que les informations sur l’inscription soient censées être complétées lorsqu’un cas est inscrit pour la première fois, les valeurs d’attribut peuvent être mises à jour à tout moment au cours d’une inscription active si de nouvelles informations deviennent disponibles (par exemple, les coordonnées).

### Identifiants { #identifiers }

Plusieurs identifiants ont été appliqués à la configuration et peuvent être adaptés en fonction du contexte national.

1. Identifiant unique généré par le système : un attribut TEI **« Identifiant système unique (PEV) »** a été configuré en tant qu’attribut unique dans le DHIS2. L’identifiant est généré automatiquement en fonction du modèle : PEV + Numéro séquentiel à 8 chiffres ALÉATOIRE(########) pour être suffisamment adapté à la population. Cet attribut TEI est destiné à être spécifique au programme ; c’est-à-dire qu’il s’agit d’un identifiant unique au sein du système utilisé uniquement par le programme national du PEV : les MAPI et le registre électronique d’immunisation. Cet attribut TEI est partagé à la fois dans le registre électronique d’immunisation et les programmes MAPI pour faciliter les liaisions entre les deux. **Étant donné que cet identifiant est généré par le système, il est garanti que, dans une instance DHIS2 intégrée, deux TEI ne pourraient pas avoir le même identifiant de système unique PEV**. Le modèle peut être modifié pour la mise en œuvre dans le pays en fonction d’autres paramètres.

2. Identifiant de cas : cet attribut **« Identifiant de cas MAPI »** est propre au flux de travail MAPI. En règle générale, une manifestation adverse se voit attribuer manuellement un identifiant unique, généralement au niveau du district ou même au niveau national. Cet attribut TEI est configuré en tant que texte libre pour s’adapter à l’attribution d’identifiant mise en œuvre dans le contexte de chaque pays, et peut être mis à jour pour inclure la validation selon le format attendu.

Des identifiants supplémentaires peuvent être ajoutés au programme en fonction du contexte national. Par exemple, si un identifiant national existe, il peut être ajouté en tant qu’attribut TEI aux MAPI et à d’autres programmes tracker. Cet attribut est attaché au PEV lui-même et restera constant d’un programme à l’autre.

![Capture d’écran d’inscription](resources/images/AEFI_Tracker_design_04.png)

**Unité d’organisation d’inscription :** est basée sur la hiérarchie des unités d’organisation (niveaux national, district, établissement). L’accessibilité de la visualisation et de la création de graphiques dans différentes « unités d’organisation » est basée sur le rôle de l’utilisateur.

### Accès { #access }

Le **programme** est configuré comme étant **protégé** afin de protéger les données personnellement identifiables contre tout accès non autorisé. Cela signifie qu’un utilisateur peut lire et écrire dans des instances d’entités suivies qui appartiennent aux unités d’organisation auxquelles il se voit attribuer un accès à la capture de données, mais la portée de ses recherches doit être plus large que son accès en lecture/écriture afin qu’il puisse identifier toutes les TEI existantes lors d’une recherche, même si celles-ci n’appartiennent pas à son unité d’organisation. Si la recherche renvoie une TEI existante en dehors de son unité d’organisation, l’utilisateur a la possibilité d’accéder au dossier du patient en enregistrant d’abord un motif pour accéder au dossier. On parle aussi de « briser la vitre » pour désigner cette approche de la confidentialité, car elle permet à l’utilisateur de prendre la décision d’accéder au dossier sans autorisation ou assistance extérieure, mais laisse une trace claire qui peut être vérifiée. Lorsque l’utilisateur a indiqué un motif pour briser la vitre, il obtient la propriété temporaire de l’instance d’entité suivie (voir le [Guide de l’utilisateur du système de suivi](https://docs.dhis2.org/2.34/en/dhis2_user_manual_en/using-the-tracker-capture-app.html#breaking-the-glass) pour plus d’informations.)

Les utilisateurs achevant l’étape 1 seront probablement basés au niveau du district et auront la responsabilité d’enquêter sur les manifestations adverses dans toutes les unités d’organisation de leur district. Afin d’attribuer correctement les données à l’unité d’organisation où la vaccination a été pratiquée, cet utilisateur au niveau du district doit avoir un accès en lecture/écriture à toutes les unités d’organisation dont il est responsable.

### Formulaire personnalisé { #custom-form }

Ce programme comporte un formulaire HTML personnalisé qui est aligné sur le formulaire papier que les professionnels de la santé utilisent habituellement. Tout ajout d’éléments au formulaire nécessitera une certaine adaptation du formulaire personnalisé. Si vous ne souhaitez pas utiliser le formulaire, il peut être supprimé et le formatage standard DHIS2 peut être utilisé en suivant les instructions du guide d’installation. **Notez que les règles de masquage du programme ne fonctionneront pas avec le formulaire personnalisé, bien que la logique du formulaire puisse toujours être appliquée à l’aide de javascript.**

### Étape 1 du programme: MAPI { #program-stage-1-aefi }

Cette étape est une étape **non reproductible**, car chaque manifestation adverse pour un individu est considérée comme une inscription menant à une investigation. Les données sont saisies pour cette étape lorsqu’une MAPI est signalée, et elles comprennent des informations détaillées sur les MAPI et les données nécessaires à l’analyse.

La date de la manifestation pour ce programme est identifiée comme la « Date de compilation du signalement », qui correspond à la date à laquelle le formulaire MAPI est lancé. Cette date est également utilisée comme DOR (Date de rapport) dans l’analyse de surveillance des MAPI. L’étape peut être complétée par plusieurs utilisateurs, selon les processus de travail du pays, avec un utilisateur de niveau inférieur fournissant les informations initiales et un utilisateur de niveau supérieur fournissant plus de détails.

![MAPI : capture d’écran 1](resources/images/AEFI_Tracker_design_05.png)

![MAPI : capture d’écran 2](resources/images/AEFI_Tracker_design_06.png)

![MAPI : capture d’écran 3](resources/images/AEFI_Tracker_design_07.png)

![MAPI : capture d’écran 4](resources/images/AEFI_Tracker_design_08.png)

![MAPI : capture d’écran 5](resources/images/AEFI_Tracker_design_09.png)

### Étape 2 du programme : Premier niveau de prise de décision { #program-stage-2-first-decision-making-level }

Cette étape est une étape **non reproductible**. Les données de cette étape sont saisies lorsque le premier niveau de prise de décision est terminé et qu’une décision a été prise quant à savoir si une enquête sur les MAPI est nécessaire.

La date de l'événement pour ce programme est nommée par défaut « Date du rapport », qui est supposée être la date à laquelle les données sont entrées dans le système. Le nom de la date de l'événement peut être modifié selon les protocoles nationaux. Cette étape reproduit le formulaire de notification et d’investigation de l’OMS, et prend en charge l’analyse pour l’investigation. Un élément de données pour la « date à laquelle l’enquête est planifiée » est inclus à cette étape pour soutenir l’analyse des indicateurs du système de surveillance.

![Premier niveau de prise de décision](resources/images/AEFI_Tracker_design_10.png)

### Étape 3 du programme : Niveau national { #program-stage-3-national-level }

Cette étape est une étape **non reproductible**.

La date de l'événement pour ce programme est nommée par défaut « Date du rapport », qui est supposée être la date à laquelle le rapport est entré dans le système. Cette étape reproduit le formulaire de notification et d’investigation de l’OMS. De plus, une date est incluse en tant qu’élément de données pour analyser la date à laquelle le rapport a été reçu au niveau national (ce qui est important pour les indicateurs de surveillance concernant le temps entre les notifications).

### Règles de programme { #program-rules }

À des fins de validation et de qualité des données, les règles de programme suivantes ont été configurées conformément aux recommandations de l’OMS. Si ces conditions sont remplies, le programme est configuré pour déclencher l’action « _Afficher l’avertissement à la fin_ » afin d'informer l’utilisateur responsable de la saisie des données des erreurs de qualité des données :

-   Si la date prévue de l’investigation est antérieure à la date de vaccination
-   Si la date de décès est antérieure à la date d’apparition (date de début de la MAPI)
-   Si la date de notification est antérieure à la date de vaccination
-   Si la date d’apparition est antérieure à la date de vaccination
-   Si la date de notification au niveau national est antérieure à la date de notification
-   Si la date de vaccination est antérieure à la date de naissance
-   Si la date de vaccination est antérieure à la date de reconstitution

Un certain nombre de règles de programme supplémentaires ont été configurées pour faciliter la saisie des données. Celles-ci peuvent être consultées dans le fichier de révision des métadonnées. **Notez que lors de l’utilisation du formulaire personnalisé, les règles de programme « masquer le champ » configurées pour faciliter la saisie des données ne fonctionneront pas correctement en raison du flux de travail du formulaire personnalisé standard.** Avec le formulaire personnalisé, les règles de programme afficheront un avertissement une fois que l'utilisateur aura cliqué sur le bouton Terminé. Cependant, ces règles de programme sont incluses dans la configuration pour les pays qui choisissent de ne pas utiliser le formulaire personnalisé.

Des règles **d’affichage et de masquage** ont été ajoutées pour les vaccins avec diluants. Tous les vaccins ne sont pas reconstitués avec un diluant. Une liste de vaccins avec diluants a été configurée sur la base des recommandations de l’OMS et des [vaccins préqualifiés de l’OMS](https://extranet.who.int/pqweb/vaccines/prequalified-vaccines?field_vaccines_effective_date%5Bdate%5D=&field_vaccines_effective_date_1%5Bdate%5D=&field_vaccines_name=&search_api_views_fulltext=&field_pharmaceutical_form=Lyophilised%20active%20component%20%20to%20be%20reconstituted%20with%20excipient%20diluent%20before%20use&field_vaccines_number_of_doses=&page=6). Lorsqu’un vaccin reconstitué avec un diluant est choisi, les éléments de date associés aux diluants s’affichent en fonction des règles de programme et permettent à l’utilisateur d’ajouter les informations sur le diluant.

**Vaccins avec diluants :**

-   Fièvre jaune
-   Haemophilus influenzae type B (Hib)
-   BCG
-   Dengue
-   Encéphalite japonaise
-   Rougeole
-   Rougeole et Rubéole
-   Rougeole, Oreillons et Rubéole
-   Méningocoque A
-   Grippe pandémique (H1N1)
-   Rotavirus
-   Rage
-   Rubéole
-   Varicelle
-   Diphtérie-Tétanos-Coqueluche (cellule entière) – Hép B – Haemohilus influenzae type B (penta)

![Informations sur le diluant](resources/images/AEFI_Tracker_design_28.png)

## Fonctionnalités supplémentaires configurées pour une prise en charge du programme { #additional-features-configured-to-support-the-program }

### Mises à jour relatives à la COVID 19 { #covid-19-updates }

Les exigences en matière de COVID 19 ont été mises à jour dans le programme

Nous avons mis à jour les ventilations des groupes d’âge pour l’analyse

-   0 à 1 an
-   1 à 5 ans
-   5 à 18 ans
-   18 à 60 ans
-   Plus de 60 ans

Les femmes enceintes et allaitantes ont été ajoutées avec les règles de programme suivantes.

-   Champs obligatoires à remplir : sexe et date de naissance
-   Si > 10 ans et que la femme est enceinte et allaitante

![Notifications de la barre supérieure](resources/images/AEFI_Tracker_design_12.png)

Une liste des vaccins connus contre la COVID-19 a été ajoutée à la liste déroulante pour « Nom du vaccin ». Elle doit être examinée par chaque pays et mise à jour à mesure que davantage de vaccins sont approuvés. Il existe également une option pour « COVID-19 : autre », à laquelle du texte libre peut être ajouté.

Le champ « Nom de la marque, dont nom du fabricant » a été ajouté en tant que zone de texte libre pour le contexte COVID.

![Vaccins contre la Covid 19](resources/images/AEFI_Tracker_design_13.png)

Trois options de manifestations adverses ont été ajoutées spécifiquement pour la COVID

-   Paralysie de Bell
-   Anaphylaxie
-   Lymphadénopathie

Texte ajouté dans le formulaire de notification deS MAPI

« Antécédents médicaux (y compris les antécédents de réaction similaire ou autres allergies), les médicaments concomitants et les dates d’administration (exclure ceux utilisés pour traiter la réaction), d’autres informations pertinentes (par exemple, d’autres cas) ».

![Texte ajouté](resources/images/AEFI_Tracker_design_14.png)

Section au niveau national mise à jour avec les classifications de causalité.

Par exemple :

![Classifications de causalité 1](resources/images/AEFI_Tracker_design_15.png)

![Classifications de causalité 2](resources/images/AEFI_Tracker_design_16.png)

Mises à jour du tableau de bord des MAPI de la COVID :

Le tableau de bord des MAPI de la COVID contient des indicateurs clés de suivi qui sont alignés sur les recommandations de l’OMS.

Le premier groupe de graphiques du tableau de bord donne un aperçu rapide des MAPI par type de vaccin contre la COVID, par zone géographique et par manifestations/réactions.

![Tableau de bord des MAPI de la COVID – 1.2](resources/images/AEFI_Tracker_design_29.png)

![Tableau de bord des MAPI de la COVID – 1.2](resources/images/AEFI_Tracker_design_30.png)

![Tableau de bord des MAPI de la COVID – 1.3](resources/images/AEFI_Tracker_design_31.png)

Le deuxième groupe de graphiques montre les manifestations adverses suivant le type de vaccination contre la COVID par statut de grossesse et d’allaitement

![Tableau de bord des MAPI de la COVID – 2.1](resources/images/AEFI_Tracker_design_32.png)

#### MAPI – Classification finale de l’évaluation de la causalité { #aefi-final-causality-assessment-classification }

Cette visualisation se trouve sur le tableau de bord des MAPI.

-   MAPI – Classification finale

Diagramme circulaire : montre le nombre total de cas de MAPI ventilés par classification finale de l’évaluation de la causalité

![MAPI – Classification finale](resources/images/AEFI_Tracker_design_26.png)

#### MAPI – Sous-classification de l’évaluation finale de la causalité { #aefi-final-causality-assessment-sub-classification }

Cette visualisation se trouve sur le tableau de bord des MAPI.

MAPI – Graphique circulaire de sous-classification finale : montre le nombre total de cas de MAPI ventilés par sous-classification finale d’évaluation de la causalité

![MAPI – Sous-classification finale de l’évaluation de la causalité](resources/images/AEFI_Tracker_design_27.png)

### Notifications { #notifications }

Les notifications ont été configurées pour déclencher une notification à des groupes d’utilisateurs définis (par exemple, stade MAPI, premier niveau et niveau national) en fonction de l’achèvement de l’étape du programme. Ces notifications peuvent être envoyées par des messages système, un e-mail externe (par exemple l’e-mail configuré dans le compte de l’utilisateur) ou par SMS si une passerelle SMS est configurée. Les notifications sont facultatives en fonction de l’utilisation et des exigences du pays, et peuvent être désactivées.

Les notifications suivantes sont préconfigurées dans le package :

1. **Evénement MAPI signalé** : envoyé à la fin de l’étape du programme MAPI aux _utilisateurs de l’unité d’organisation_ (par exemple, l’établissement) pour alerter qu’une manifestation adverse a été signalée.
2. **Étape MAPI terminée** : envoyée à la fin de l’étape du programme MAPI au groupe d’utilisateurs de _prise de décision de premier niveau concernant les MAPI_ pour qu’il examine le rapport MAPI et lance la prochaine mesure d’investigation.
3. ** Examen pour le premier niveau de prise de décision concernant les MAPI terminé :** notification envoyée en fonction des règles du programme au _groupe d’utilisateurs au niveau national concernant les MAPI_ lorsque la prise de décision de premier niveau est terminée afin que le comité national examine et approuve le rapport conformément aux protocoles nationaux.
4. **Investigation sur les MAPI requise :** notification envoyée en fonction de la règle de programme si une investigation a été jugée nécessaire sur la base des éléments de données à l’étape de prise de décision de premier niveau ; envoyée aux utilisateurs du _groupe de district pour les MAPI_ qui devraient commencer la première partie de l’investigation.
5. **Évaluation nationale des MAPI terminée :** notification envoyée à la fin de l’étape au niveau national aux utilisateurs du groupe d’utilisateurs _MAPI au niveau national_ pour indiquer que l’examen national a été achevé et approuvé, et que les prochaines mesures, telles que la notification à l'échelle mondiale, peuvent être prises.

Vous trouverez des informations sur la configuration des notifications d’étape de programme ici. <https://docs.dhis2.org/2.33/en/dhis2_user_manual_en/configure-programs-in-the-maintenance-app.html#create-a-program-stage-notification>. La configuration de la messagerie SMS nécessite la configuration d’une passerelle SMS. Vous pouvez trouver des informations sur sa configuration en suivant ce lien <https://docs.dhis2.org/master/en/developer/html/webapi_sms.html>

### Liste descriptive { #line-listing }

La liste descriptive incluse dans le tableau de bord reflète les 25 variables de base identifiées par le Comité consultatif mondial de la sécurité vaccinale (GACVS) en juin 2012. Ces variables de base couvrent les exigences attendues pour la communication vers les bases de données régionales et mondiales de sécurité des vaccins. Des efforts sont en cours pour cartographier et coder ces variables dans le guide E2B utilisé par Vigibase, la base de données mondiale de l’OMS sur les rapports de sûreté des cas individuels.

![Liste descriptive](resources/images/AEFI_Tracker_design_17.png)

-   **Remarque :** la capture d’écran ci-dessus ne représente pas la liste complète ; veuillez vous reporter au DHIS2 pour obtenir la liste dans son intégralité
-   Tous les champs de la liste descriptive au niveau de l’établissement proviennent directement du programme MAPI. Cela inclut les champs du processus d’enregistrement ainsi que la première étape du programme (intitulée **« MAPI »**). La source de chacun des champs de la liste descriptive est identifiée ci-dessous.

| Nº de champ/colonne | Nom de la variable | Source | Description |
| --- | --- | --- | --- |
| 1 | Numéro |  | Numéro du cas dans la liste |
| 2 | DOR (date de rapport – date de compilation du rapport) | Étape MAPI | La date de l'événement de l’étape du programme MAPI |
| 3 | DON (date de notification – date à laquelle le patient a notifié l'événement au système de santé) | Étape d’enregistrement | Date à laquelle le patient a notifié l'événement au système de santé. Date de l’inscription. |
| 4 | Date de l’incident |  | S.O. (champ à ignorer) |
| 5 | Unité d’organisation | Étape d’enregistrement | Unité d’organisation (qui vient de la hiérarchie) et représente très probablement l’établissement dans lequel la MAPI a été enregistrée |
| 6 | MAPI – Déclarant du cas | Étape MAPI | La personne ayant signalé le cas de MAPI |
| 7 | MAPI – Adresse du déclarant | Étape MAPI | L’adresse de la personne ayant signalé le cas de MAPI |
| 8 | Identifiant du cas de MAPI | Étape d’enregistrement | L’identifiant unique du cas de MAPI attribué localement |
| 9 | Prénom | Étape d’enregistrement | Le prénom du cas |
| 10 | Nom de famille | Étape d’enregistrement | Le nom de famille du cas |
| 11 | Date de naissance | Étape d’enregistrement | La date de naissance du cas |
| 12 | Sexe | Étape d’enregistrement | Le sexe biologique du cas |
| 13 | Date de début de la MAPI | Étape MAPI | La date de l’incident de MAPI (la date à laquelle la MAPI a commencé) |
| 14 | Cas graves de MAPI | Étape MAPI | Identifie si le cas était grave ou non |
| 15 | MAPI – Issue de la MAPI | Étape MAPI | Identifie l’issue du cas telle qu’elle a été identifiée par le personnel de santé |
| 16 | MAPI – Date de vaccination 1 | Étape MAPI | La date à laquelle le **premier** vaccin a été administré au cas |
| 17 | MAPI – Nom du vaccin 1 | Étape MAPI | Le nom du **premier** vaccin qui a été administré au cas |
| 18 | MAPI – numéro de lot (vaccin 1) | Étape MAPI | Le numéro de lot du **premier** vaccin qui a été administré au cas |
| 19 | MAPI – Numéro de lot du diluant 1 | Étape MAPI | Le numéro de lot du diluant utilisé dans le **premier** vaccin qui a été administré au cas |
| 20 | MAPI – Date de vaccination 2 | Étape MAPI | La date à laquelle le **deuxième** vaccin (le cas échéant) a été administré au cas |
| 21 | MAPI – Nom du vaccin 2 | Étape MAPI | Le nom du **deuxième** vaccin (le cas échéant) qui a été administré au cas |
| 22 | MAPI – numéro de lot (vaccin 2) | Étape MAPI | Le numéro de lot du **deuxième** vaccin (le cas échéant) qui a été administré au cas |
| 23 | MAPI – Numéro de lot du diluant 2 | Étape MAPI | Le numéro de lot du diluant utilisé dans le **deuxième** vaccin (le cas échéant) qui a été administré au cas |
| 24 | MAPI – Date de vaccination 3 | Étape MAPI | La date à laquelle le **troisième** vaccin (le cas échéant) a été administré au cas |
| 25 | MAPI – Nom du vaccin 3 | Étape MAPI | Le nom du **troisième** vaccin (le cas échéant) qui a été administré au cas |
| 26 | MAPI – numéro de lot (vaccin 3) | Étape MAPI | Le numéro de lot du **troisième** vaccin (le cas échéant) qui a été administré au cas |
| 27 | MAPI – Numéro de lot du diluant 3 | Étape MAPI | Le numéro de lot du diluant utilisé dans le **troisième** vaccin (le cas échéant) qui a été administré au cas |
| 28 | Manifestations adverses (éléments de données individuels) | Étape MAPI | Une liste de toutes les manifestations adverses possibles signalées dans le cadre du programme. Cela inclut toutes les manifestations graves et non graves qui sont signalées pour un cas et constitue les colonnes restantes de la liste descriptive |

#### Champs sources { #source-fields }

![Enregistrement](resources/images/AEFI_Tracker_design_18.png)

![Étape MAPI – Section concernant le déclarant](resources/images/AEFI_Tracker_design_19.png)

![Étape MAPI – Informations sur la vaccination](resources/images/AEFI_Tracker_design_20.png)

![Étape MAPI – Informations sur la MAPI](resources/images/AEFI_Tracker_design_21.png)

#### Visualisations { #visualizations }

Un certain nombre de champs de la liste descriptive sont représentés sous forme de visualisations dans les tableaux de bord, disponibles dans le package de configuration. Celles-ci peuvent toutes être modifiées pour répondre aux besoins locaux si nécessaire. Une brève description de la ou des visualisation(s) associées à chaque champ de la liste descriptive est présentée ci-dessous.

-   Champs sans visualisations : Numéro, MAPI – Déclarant du cas, MAPI – Adresse du déclarant, Identifiant du cas de MAPI, Prénom, Nom de famille, Date de début de la MAPI, MAPI – Date de vaccination 1, MAPI – Date de vaccination 2, MAPI – Date de vaccination 3, MAPI – Numéro de lot (vaccin 1), MAPI – Numéro de lot (vaccin 2), MAPI – Numéro de lot (vaccin 3), MAPI – Numéro de lot de diluant 1, MAPI – Numéro de lot de diluant 2, MAPI – Numéro de lot de diluant 3

-   DOR (date du rapport – date de compilation du rapport). Veuillez vous reporter au tableau de bord de surveillance des MAPI pour plus d’informations sur la façon dont cette variable est utilisée afin de générer des résultats pour le programme

-   DON (date de notification – date à laquelle le patient a notifié la manifestation au système de santé). Veuillez vous reporter au tableau de bord de surveillance des MAPI pour plus d’informations sur la façon dont cette variable est utilisée afin de générer des résultats pour le programme

-   DOO (date d’apparition – date de début des MAPI). Veuillez vous reporter au tableau de bord de surveillance des MAPI pour plus d’informations sur la façon dont cette variable est utilisée afin de générer des résultats pour le programme

![Liste descriptive nationale de cas MAPI](resources/images/AEFI_Tracker_design_22.png)

-   **Remarque :** la capture d’écran ci-dessus ne représente pas la liste complète ; veuillez vous reporter au DHIS2 pour obtenir la liste dans son intégralité

La liste descriptive de niveau national a été ajoutée avec les mises à jour COVID. Cette liste récapitulative est dérivée des données incluses dans le formulaire de notification des MAPI dans la section "Niveau national". Ce qui inclut des informations relatives aux données au niveau de l’établissement, qui sont collectées dans le formulaire.

-   Située sur le tableau de bord des MAPI avec le titre « Résumé national des MAPI (cette année) ».
-   Se compose des informations suivantes (il est recommandé d’avoir la liste descriptive ouverte dans le DHIS2 lors de l’examen de cette description).
-   Tous les champs de la liste descriptive au niveau de l’établissement proviennent directement du programme MAPI. Cette liste comprend également les données du processus d’enregistrement, la première étape du programme (intitulée **« MAPI »**), ainsi que la troisième étape du programme (intitulée « Niveau national »). La source de chacun des champs de la liste descriptive est identifiée ci-dessous.

| Nº de champ/colonne | Nom de la variable | Source | Description |
| --- | --- | --- | --- |
| 1 | Numéro |  | Numéro du cas dans la liste |
| 2 | DON (date de notification – date à laquelle le patient a notifié la manifestation au système de santé) | Étape d’enregistrement | Date à laquelle le patient a notifié la manifestation au système de santé. Date de l’inscription. |
| 3 | Date de l’incident |  | S.O. (champ à ignorer) |
| 4 | Unité d’organisation | Étape d’enregistrement | Unité d’organisation (qui vient de la hiérarchie) et représente très probablement l’établissement dans lequel la MAPI a été enregistrée |
| 5 | Identifiant du cas de MAPI | Étape d’enregistrement | L’identifiant unique du cas de MAPI attribué localement |
| 6 | MAPI — Date de visualisation pour approbation au niveau national  | Étape au niveau national | La date à laquelle le rapport de MAPI a été reçu au niveau national en vue de son approbation |
| 7 | MAPI – Date de la classification finale | Étape au niveau national | La date à laquelle la classification finale de la MAPI a été effectuée |
| 8 | MAPI – Diagnostic valide | Étape au niveau national | Le diagnostic validé et utilisé pour l’évaluation de la causalité |
| 9 | MAPI – Nom du vaccin 1 | Étape MAPI | Le nom du premier vaccin qui a été administré au cas |
| 10 | MAPI – Date de vaccination 1 | Étape MAPI | La date à laquelle le premier vaccin a été administré pour le cas. |
| 11 | MAPI – Nom du vaccin 2 | Étape MAPI | Le nom du deuxième vaccin (le cas échéant) qui a été administré au cas |
| 12 | MAPI – Date de vaccination 2 | Étape MAPI | La date à laquelle le second vaccin (le cas échéant) a été administré pour le cas. |
| 13 | MAPI – Nom du vaccin 3 | Étape MAPI | Le nom du quatrième vaccin (le cas échéant) qui a été administré au cas |
| 14 | MAPI – Date de vaccination 3 | Étape MAPI | La date à laquelle le troisième vaccin (le cas échéant) a été administrée au cas. |
| 15 | MAPI – Nom du vaccin 4 | Étape MAPI | Le nom du quatrième vaccin (le cas échéant) qui a été administré au cas. |
| 16 | MAPI – Date de vaccination 4 | Étape MAPI | La date à laquelle le quatrième vaccin (le cas échéant) a été administré au cas. |
| 17 | MAPI – Classification finale de l’évaluation de la causalité | Étape au niveau national | L’évaluation finale de la causalité de la MAPI telle que déterminée par l’équipe d’examen au niveau national |
| 18 | MAPI – Sous-classification finale de l’évaluation de la causalité | Étape au niveau national | La sous-classification finale de l’évaluation de la causalité des MAPI, comme déterminée par l’équipe chargée de l'examen au niveau national |

La liste descriptive met en évidence le lien entre la vaccination ayant causé une MAPI et la classification et la sous-classification finales de l’évaluation de la causalité telles que déterminées par l’équipe chargée de l’examen au niveau national.

#### Champs sources { #source-fields }

![Enregistrement](resources/images/AEFI_Tracker_design_23.png)

![Étape MAPI – Informations sur la vaccination](resources/images/AEFI_Tracker_design_24.png)

![Étape au niveau national](resources/images/AEFI_Tracker_design_25.png)

## Compatibilité Android pour la collecte de données { #android-compatibility-for-data-collection }

Les packages de données numériques sont optimisés pour la collecte de données Android à l’aide de l’application DHIS2 Capture, téléchargeable gratuitement sur [Google Play Store](https://play.google.com/store/apps/details?id=com.dhis2&hl=en). Les points suivants sont des limites connues de l’application DHIS2 Android Capture v 2.2.0 avec des conséquences sur ce package tracker :

-   Le formulaire personnalisé de saisie de données n’est pas pris en charge

## Tableaux de bord, analyses et indicateurs { #dashboards-analytics-and-indicators }

Le package comprend des indicateurs de programme préconfigurés et alignés sur les exigences de l’OMS. Le tableau de bord inclus dans le package est conçu pour l’analyse au niveau national, mais peut également être consulté par le personnel au niveau infranational pour son propre district ou sa propre province.

Le tableau de bord suit les recommandations de l’OMS en matière de génération de résultats analytiques dans le cadre de l’analyse épidémiologique descriptive et celui des indicateurs clés de surveillance de la sécurité des vaccins (par exemple, le délai entre la notification et l’enquête entre les niveaux du système).

## Références { #references }

OMS. (2018). Sécurité mondiale des vaccins : initiative mondiale pour la sécurité des vaccins (GVSI). Récupéré de : <https://www.who.int/vaccine_safety/initiative/en/>

OMS. (2018). Sécurité mondiale des vaccins : manifestations adverses post immunisation (MAPI). Récupéré de : <https://www.who.int/vaccine_safety/committee/topics/global_AEFI_monitoring/en/>
