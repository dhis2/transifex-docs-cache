---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/ReleaseNote-2.38.md"
revision_date: "2022-05-05"
---

# Note de mise à jour de la version 2.38 du DHIS { #dhis-version-238-release-note }

## FONCTIONNALITÉS D'ANALYSE { #analytics-features }

**Nouvelle application Liste de lignes :** Cette nouvelle application constitue une amélioration considérable de la production de listes de lignes d'entités suivies dans DHIS2 par rapport à l'application de rapports d'événements. La nouvelle application de liste de lignes a reproduit toutes les fonctionnalités de liste de lignes de l'application de rapports d'événements, et elle a une expérience utilisateur complètement nouvelle et très améliorée qui rend beaucoup plus facile pour les utilisateurs de faire une liste de lignes d'entités suivies. Elle comprend également de nombreuses nouvelles fonctionnalités. Vous trouverez ci-dessous une liste de quelques-unes des principales nouvelles fonctionnalités :

-   Visualisation de plusieurs événements répétitifs : Vous êtes désormais en mesure de produire une liste de lignes pouvant afficher les données de plusieurs étapes répétées pour une seule entité suivie. Vous pouvez spécifier le nombre d'étapes répétées dont vous souhaitez voir les données. Ceci est utile pour de nombreux programmes de santé et d'éducation en permettant la visualisation de données capturées de manière répétée dans le temps pour un seul patient ou étudiant. [Capture d'écran 1](images/2.38repeatingevent.png) | [Capture d'écran 2](images/2.38repeatingevent2.png)
-   Nouvelles dimensions de période spécifiques au tracker : Dans la nouvelle application Liste de lignes, vous pouvez produire une liste de lignes indiquant la date d'inscription, la date de l'événement et/ou la date de l'incident. Ces éléments peuvent être définis, triés et affichés ensemble dans une seule liste de lignes. [Capture d'écran](2.38linelisttimedemensions.png)
-   Créé par et Dernière mise à jour par : Ceci vous permet de voir le nom de l'utilisateur ayant créé l'inscription ou l'utilisateur ayant mis à jour les données pour l'entité suivie.

[Capture d'écran](images/2.38_linelist_2.png)

**Zones desservies pour les unités d'organisation (établissements, écoles, postes de santé, etc.):** Le DHIS 2.38 prend en charge plusieurs géométries (points et formes) pour toutes les unités d'organisation. Celles-ci peuvent être visualisées dans l'application Cartes pour toute couche standard par le biais d'une option dans le sélecteur d'unité d'organisation. En pratique, cela signifie que les administrateurs du système peuvent télécharger les zones de desserte de leurs établissements, postes de santé communautaires, écoles, hôpitaux, etc. et visualiser toutes les données par zone de desserte.

[Capture d'écran](images/2.38_catchment_area.png) | [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-235/analysing-data/maps.html) |

**Prise en charge de la couche de bâtiments/structures de Google Earth:** Dans l'application Cartes, les utilisateurs peuvent désormais voir les contours des structures identifiées par l'ensemble de données Open Building de Google. Cet ensemble de données comprend 516 millions de bâtiments (64% du continent africain). Il est utile pour l'estimation de la population, la planification urbaine, les programmes de sensibilisation et de santé, et les interventions humanitaires par exemple. Le nombre de bâtiments peut être indiqué par les limites des bassins versants ou des unités org.

[Capture d'écran 1](images/2.38_structures_1.png) | [Capture d'écran 2](images/2.38_structures_2.png) | [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-235/analysing-data/maps.html) |

**Prise en charge des Vector tiles dans Cartes:** L'application Maps utilise et prend désormais en charge les vector tiles. Cela devrait permettre d'améliorer les performances et de mettre à jour la technologie sous-jacente.

**Remplacement du type d'agrégation de l'indicateur:** Un indicateur peut spécifier un type d'agrégation, remplaçant le type par défaut attribué à un élément de données. Par exemple, si un élément de données a le type d'agrégation SUM, un indicateur peut aussi rapporter la valeur par AVERAGE, COUNT, FIRST, LAST, MIN, MAX, etc.

_Exemple d'expression dans les indicateurs : #{EX2jBdKe4Yq}.aggregationType(COUNT)_ Description: Enseignants ER Formés.aggregationType(COUNT)

[Docs](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

**Indicateur minDate et maxDate:** Une date minimale et/ou maximale peut être spécifiée pour récupérer un élément de données pour un indicateur. Cela peut être utile lorsque la sémantique des données change de temps en temps, nécessitant différents calculs pour le même résultat. Cela permet à un indicateur d'établir un rapport cohérent à travers ces changements en modifiant la façon dont l'indicateur est calculé dans le temps. N'oubliez pas que la fonction periodOffset (depuis 2.36) peut également être utilisée pour inclure des données d'une période différente dans l'expression d'un indicateur.

_Exemple d'expression minDate et maxDate dans les indicateurs : #{EX2jBdKe4Yq}.minDate(2021-1-1).maxDate(2021-6-30)_ Description: Enseignants ER Formés.minDate(2021-1-1).maxDate(2021-6-30) -> Seules les valeurs comprises entre le 1er janvier 2021 et le 30 juin 2021 pour les enseignants ER formés seront utilisées dans le calcul de l'indicateur.

_Exemple d'expression periodOffset dans les indicateurs : #{EX2jBdKe4Yq} + #{EX2jBdKe4Yq}.periodOffset(-1) + #{EX2jBdKe4Yq}.periodOffset(-2)_ Description : Enseignants ER Formés + Description : Enseignants ER Formés + Enseignants ER Formés.periodOffset(-1) + Enseignants ER Formés.periodOffset(-2) -> Somme des Enseignants ER Formés au cours des trois derniers mois par rapport à la période sélectionnée dans l'application analytique utilisée pour visualiser cette valeur.

[Docs](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

**Sous-expressions d'indicateurs (pour 2.38.1):** Les indicateurs peuvent compter le nombre d'unités d'organisation où un élément de données se compare d'une manière spécifique avec une valeur fixe.

_Exemple d'expression de sous-expression dans les indicateurs : sous-Expression( si (#{vq2q03TrNi} > 100, 1, 0) )_ Description : sous-Expression(if(SIMR Paludisme>100,1,0)) -> Compte le nombre d'unités d'organisation où plus de 100 cas de paludisme ont été signalés au cours d'une période donnée définie dans l'application analytique utilisée pour visualiser cette valeur.

[Docs](https://docs.dhis2.org/en/full/use/user-guides/dhis-core-version-236/dhis2-user-manual.html#manage_indicator)

## FONCTIONNALITÉS DU TRACKER ET ÉVÉNEMENT { #tracker-and-event-features }

**Améliorations des listes de travail des programmes Tracker : ** La fonctionnalité des listes de travail des programmes Tracker a été élargie pour être similaire à celle des listes de travail des événements. L'application Capture permet désormais de configurer, sauvegarder, partager, supprimer et mettre à jour les listes de travail via l'interface utilisateur.

[Capture d'écran 1](images/Working_list.png) | [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#capture_views) | [Jira](https://jira.dhis2.org/browse/DHIS2-9275)

**Traduction des actions de règles de programme dans Tracker Capture et Capture app:** Le contenu des actions de règles de programme - le "texte statique" qui est visualisé pour les utilisateurs, peut être traduit et affiché dans les programmes Tracker. [Jira](https://jira.dhis2.org/browse/DHIS2-12137)

**Description et URL pour les éléments de données et les attributs des entités suivies:** La description et l'URL définies pour ces éléments de données sont affichées dans un popover. On peut accéder à ce popover en cliquant sur l'icône "i" qui s'affiche après le nom de l'élément de données. La description est définie dans l'application de maintenance et peut être utilisée pour donner plus d'informations sur ce qu'il faut capturer pour l'élément de données.

[Capture d'écran 1](images/Capture_DE_description.png) | [Jira](https://jira.dhis2.org/browse/DHIS2-5345)

**Nouvelle composante d'unité d'organisation implémentée dans l'application Capture:** La composante d'unité d'organisation utilisée dans l'application Capture a été remplacée par l'unité d'organisation remaniée de d2-ui.

[Jira](https://jira.dhis2.org/browse/DHIS2-11806)

**Prise en charge de GS1 Data Matrix:** GS1 Data Matrix est utilisé pour le codage à barres des produits pharmaceutiques et de santé, et prendra en charge les cas d'utilisation de la chaîne d'approvisionnement. Compte tenu de la valeur d'un champ formaté selon la norme GS1 Data Matrix et d'une clé de chaîne provenant des identificateurs d'application GS1, il existe désormais une prise en charge des règles de programme qui extraient les valeurs de ce texte délimité et attribuent des valeurs à leurs champs désignés. Ceci est mis en œuvre dans Saisie Tracker, Capture et l'application Android Capture.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#program_rules_operators_functions) | [Jira](https://jira.dhis2.org/browse/DHIS2-12353)

**Type de données/valeur pour la Variable de règle de programme : ** Pour les variables de règle de programme avec le type de source "valeur calculée", l'application de maintenance proposera à l'utilisateur d'attribuer un type de valeur. Le type de valeur par défaut pour les valeurs calculées sera le texte. Pour tous les autres types de sources de variables de règles de programme, la sélection du type de valeur ne doit pas être visible, car la variable hérite du type de l'élément de données sous-jacent ou de l'attribut de l'entité suivie.

[Jira](https://jira.dhis2.org/browse/DHIS2-12096)

**Les programmes peuvent rester ouverts même après la date de fin de l'option d'attribut:** Un programme spécifique peut rester ouvert après la fermeture de l'option d'attribut correspondante.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/configuring-the-system/programs.html#tracker_enter_programs_details) | [Jira](https://jira.dhis2.org/browse/DHIS2-12118)

**L'application Capture est publiée de façon continue : ** À partir de la version 2.38, l'application Capture sera publiée de façon continue sur le hub des applications. Les corrections de bugs et les nouvelles fonctionnalités seront donc disponibles pour être téléchargées et intégrées au moment où elles seront nécessaires, sans avoir à mettre à jour le reste de l'application. La première version mise à jour de l'application Capture sera disponible sur le hub des applications peu après la sortie de la version 2.38.0. Le hub des applications est accessible via l'application de gestion des applications.

**Fonctionnalités de suivi dans l'application Capture:** En plus de la fonctionnalité de suivi qui a été ajoutée dans la version 2.37 pour le test bêta fermé, des fonctionnalités supplémentaires ont été ajoutées. La nouvelle fonctionnalité peut être testée en installant l'application Capture mise à jour à partir du hub des applications, et en choisissant d'utiliser les fonctions de suivi dans l'application Capture. Seuls les super-utilisateurs ou les utilisateurs ayant accès à la modification des métadonnées du programme disposeront de la fonctionnalité d'opt-in. La nouvelle fonctionnalité de suivi qui peut être testée en se connectant est présentée ici :

-   Widget de profil de la TEI : Sur le tableau de bord d'inscription, vous pouvez afficher le widget de profil de l'instance d'entité suivie. À l'intérieur du widget de profil, vous pouvez voir les valeurs des attributs clés. Cliquez sur le bouton Modifier pour apporter des modifications au profil de l'instance de l'entité suivie. L'édition du profil ouvre un dialogue dans lequel les attributs du profil peuvent être modifiés. 
    [Jira](https://jira.dhis2.org/browse/DHIS2-10946)
-   Formulaire widget de programmation d'événements : Au lieu de signaler un événement, l'utilisateur peut choisir de programmer un événement plus tard. Cela se fait avec une date programmée. La boîte de dialogue s'ouvre avec une suggestion de date programmée, et cette date est déterminée par un ensemble de règles provenant de la configuration des étapes du programme et de la configuration du programme. 
    [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#schedule-event-widget-form) | [Jira](https://jira.dhis2.org/browse/DHIS2-11861)
-   Actions rapides dans le tableau de bord des inscriptions : Le widget d'actions rapides offre des raccourcis pour les actions fréquemment utilisées pour l'inscription en cours, y compris la création d'un événement et la programmation d'un événement. 
    [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#quick-actions) | [Jira](https://jira.dhis2.org/browse/DHIS2-11953)
-   "Ajouter nouveau" pour les inscriptions terminées dans le widget d'inscription : Il ne peut y avoir qu'une seule inscription active à la fois, mais si toutes les inscriptions sont terminées, il y aura une option pour réinscrire la TEI dans le programme dans le widget d'inscription, si le programme permet plus d'une inscription par TEI. Si le programme ne permet pas plus d'une inscription, le bouton d'ajout sera désactivé. [Jira](https://jira.dhis2.org/browse/DHIS2-12141)
-   Réinscrire une instance d'entité suivie existante : Si vous avez sélectionné une instance d'entité suivie dans le sélecteur verrouillé et que vous sélectionnez un programme différent, vous pouvez désormais réinscrire des TEI existantes dans d'autres programmes. La page d'inscription sera pré-remplie avec toutes les valeurs d'attributs d'entités suivies qui se chevauchent. 
    [Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/tracking-individual-level-data/capture.html#re-enroll-an-existing-tracked-entity-instance) | [Jira](https://jira.dhis2.org/browse/DHIS2-12141)

## FONCTIONNALITÉS DE LA PLATE-FORME { #platform-features }

**Notifications de vérification de version:** Un nouveau service de notification de vérification de version du système DHIS 2 est introduit, lequel enverra des notifications sous la forme de messages dans la boîte de réception du système DHIS 2 lorsque des versions plus récentes du DHIS 2 seront disponibles. Cela inclut les versions majeures et les correctifs. Ceci est utile pour encourager les administrateurs système à mettre à jour le système DHIS 2 afin de maintenir leur instance sécurisée et à jour.

Docs | [Jira](https://jira.dhis2.org/browse/DHIS2-9897)

**Attributs de métadonnées GeoJSON:** GeoJSON est désormais pris en charge comme type de valeur pour les attributs de métadonnées. Cela vous permet de stocker un nombre illimité de documents GeoJSON, par exemple pour les unités d'organisation.

[Docs]() | [Jira](https://jira.dhis2.org/browse/DHIS2-12328)

**Exportation DX:** L'application d'importation/exportation permet désormais d'importer et d'exporter des données en utilisant le format de données ADX.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/maintaining-the-system/importexport-app.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-4978)

**Niveau de log configurable:** Les niveaux de log peuvent maintenant être configurés dans le fichier de configuration `dhis.conf` au niveau du package. Cela signifie que vous pouvez spécifier le niveau de log à sortir pour des frameworks et modules spécifiques dans DHIS 2 directement dans le fichier de configuration de DHIS 2.

[Docs](https://docs.dhis2.org/en/manage/performing-system-administration/dhis-core-version-master/installation.html#log-level-configuration) | [Jira](https://jira.dhis2.org/browse/DHIS2-11898)

**Notifications de désactivation de compte:** Lors de la désactivation automatique d'utilisateurs par le biais de la tâche programmée de désactivation d'utilisateurs, une notification par e-mail peut être envoyée à l'utilisateur concerné. Le nombre de jours avant la notification peut être défini dans la configuration de la tâche. Ceci est utile pour donner aux utilisateurs une chance de se connecter avant la désactivation de leur compte.

[Docs](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-238/maintaining-the-system/scheduling.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-11589)

**Schéma d'entrée des ensembles de valeurs de données:** Les schémas d'entrée sont désormais pris en charge pour le point de terminaison de l'API des ensembles de valeurs de données, ce qui vous permet d'importer des données en utilisant le champ de code pour référencer les métadonnées.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-238/data.html) | [Jira](https://jira.dhis2.org/browse/DHIS2-9822)

**Nom court des ensembles de groupes:** Les ensembles de groupes d'indicateurs et d'options de catégories ont désormais des propriétés de nom court, ce qui permet un rendu précis et convivial. Les noms courts sont désormais utilisés comme noms de colonnes dans les tables de ressources au lieu des noms.

[Jira](https://jira.dhis2.org/browse/DHIS2-7317)

**Gestion du cache des données analytiques:** Le cache des données analytiques est désormais automatiquement vidé lorsque les tables de la base de données analytique sont mises à jour. Cela garantit que les requêtes analytiques lisent les dernières données des données analytiques et réduit le décalage entre la mise à jour des tables analytiques et l'apparition des données dans les visualisations de données.

[Jira](https://jira.dhis2.org/browse/DHIS2-12072)

### FONCTIONNALITÉS DE L'API DE LA PLATE-FORME { #platform-api-features }

**Améliorations de l'entrepôt de données:** L'API de l'entrepôt de données a connu de nombreuses améliorations pour en faire un entrepôt de données à part entière et le rendre plus utile aux applications Web et aux autres clients.

-   **Filtrage des champs:** Vous permet de renvoyer uniquement les clés et valeurs spécifiques des entrées dans l'entrepôt de données à l'aide du paramètre `fields`. Le fonctionnement est similaire au filtrage des champs dans l'API des métadonnées. Le filtrage a lieu au niveau de l'espace de noms et est utile lorsqu'un client a besoin de lister de nombreuses entrées avec des clés/valeurs spécifiques dans une seule requête. [Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#datastore-query-api) | [Jira](https://jira.dhis2.org/browse/DHIS2-12154)
-   **Pagination:** Dans les réponses aux requêtes, la pagination est prise en charge et activée par défaut. Vous pouvez spécifier la pagination explicitement avec les paramètres `page` et `pageSize`. La pagination est utile lorsque l'on travaille avec des espaces de noms comportant un grand nombre d'entrées. [Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#datastore-query-api) | [Jira](https://jira.dhis2.org/browse/DHIS2-12329)
-   **Filtrage des entrées:** Vous permet de faire correspondre et de filtrer les entrées d'un espace de noms en fonction de divers opérateurs, tels que `eq`, `lt`, `le`, `gt`, `ge`, `like`, `null`, en utilisant le paramètre `filter`. Le fonctionnement est similaire au filtrage des objets dans l'API de métadonnées. Le filtrage est utile lorsqu'un client souhaite lister de nombreuses entrées qui correspondent à un ou plusieurs critères. [Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data-store.html#filtering-entries) | [Jira](https://jira.dhis2.org/browse/DHIS2-12331)
-   **Triage:** Vous permet de trier les entrées d'un espace de noms de manière ascendante ou descendante en fonction d'une clé/valeur spécifique en utilisant le paramètre `order`. Ceci est utile lorsque les clients ont des exigences spécifiques pour trier une liste d'entrées. Docs | [Jira](https://jira.dhis2.org/browse/DHIS2-12330)

**Enregistrement des requêtes:** Les clients de l'API peuvent désormais soumettre une valeur avec l'en-tête HTTP `X-Request-ID` qui est incluse dans toutes les déclarations de journal. Ceci est utile lorsque vous regardez les journaux du DHIS 2 et que vous essayez de comprendre quel client/application a fait une requête, par exemple lorsque vous déboguez un problème qui s'applique à une installation spécifique d'une application Android sur un téléphone.

[Docs](https://docs.dhis2.org/en/manage/performing-system-administration/dhis-core-version-238/installation.html#log-configuration) | [Jira](https://jira.dhis2.org/browse/DHIS2-6494)

**Annuler les tâches des tables d'analyse:** Vous pouvez désormais annuler (arrêter) les tâches des tables d'analyse en cours d'exécution. Ceci est utile pour arrêter les tâches de longue durée sans avoir à attendre qu'elles se terminent.

Docs | [Jira](https://jira.dhis2.org/browse/DHIS2-6314)

### FONCTIONS DES DÉVELOPPEURS DE LA PLATE-FORME { #platform-developer-features }

## INFORMATIONS SUR LA VERSION { #release-info }

| Informations sur la version | Lien |
| --- | --- |
| Télécharger la version et la base de données exemple | https://www.dhis2.org/downloads |
| Documentation | [https://docs.dhis2.org](https://docs.dhis2.org/) |
| Notes de mise à jour | [Notes de mise à jour sur GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/README.md) |
| Liste complète des fonctionnalités et des bogues de cette version | [Notes de mise à jour](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/ReleaseNote-2.38.md) |
| Code source sur Github | https://github.com/dhis2 |
| Instance de démonstration | https://play.dhis2.org/2.38/ |
| Image Docker | `docker pull dhis2/core:2.38.0` |
| Images Docker Hub | https://hub.docker.com/repository/docker/dhis2/core |
| Forum de la communauté | https://community.dhis2.org/ |
