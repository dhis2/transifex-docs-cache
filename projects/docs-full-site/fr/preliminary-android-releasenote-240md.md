# Note de mise à jour de la version 2.4 de l'application Android du DHIS2

DHIS2 [Android Capture App 2.4](https://www.dhis2.org/android-2-4) est disponible avec de nombreuses améliorations.
Brève description des fonctionnalités.

Cette version est entièrement compatible avec le [DHIS2 2.36 ](https://www.dhis2.org/236) et vous pouvez trouver ci-dessous les détails concernant les nouvelles fonctionnalités ainsi que les modifications.


## EXPÉRIENCE UTILISATEUR ET INTERFACE UTILISATEUR
**Nouvelle icône pour la recherche de TEI :** L'icône permettant la recherche des TEI a été modifiée de manière à refléter l'action de recherche/enregistrement. L'application android exige une recherche avant toute création d'une nouvelle TEI, mais les informations saisies dans les champs de recherche sont transférées dans les champs du formulaire d'enregistrement lorsque la recherche n'aboutit pas et que l'utilisateur décide d'entrer une nouvelle TEI. Ceci fait donc de la recherche une première étape de l'enregistrement, et c'est justement la raison pour laquelle l'icône a été mise à jour pour refléter cette action intégrée.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3527) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot01.png)

**Nouvelle barre de navigation :** La version actuelle et la prochaine version de l'application proposent de nouveaux modules tels que Analytics et Tasks (prochaine version). Pour développer la structure de l'application et offrir une navigation facile et intuitive à travers les nouveaux modules, la navigation est désormais déplacée vers une barre inférieure. La nouvelle barre de navigation est disponible dans la version actuelle des écrans du Tableau de bord Événement et Tracked Entity Instance. Elle sera ajoutée à d'autres écrans dans les prochaines versions, au fur et à mesure de l'implémentation de la nouvelle fonctionnalité. 

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3510) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot02.png) | [Capture d'écran2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot22.png)


**Nouvelle disposition des listes d'événements et d'ensembles de données :** L'interface utilisateur des listes d'événements et d'ensembles de données a été modifiée de manière à présenter un aspect conforme aux listes de TEI des programmes de suivi.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3562) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-3563) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot23.png) | [Capture d'écran2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot26.png)

**Les éléments de données obligatoires sont toujours affichés :** Lorsqu'un élément de données est configuré comme étant obligatoire, il ne pourra pas être masqué par les règles du programme. Ce comportement est conforme à celui de l'application Web Capture. 

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3497) 

**Appliquer des légendes aux champs d'éléments de données :** Désormais, lorsqu'un élément de données numérique dispose d'une légende, l'application affichera un badge avec la couleur et la description correspondant à la valeur de légende donnée.
[jira](https://jira.dhis2.org/browse/ANDROAPP-3312) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot12.png)

## SAISIE DES DONNÉES D'ÉVÉNEMENTS ET DE TRACKER

**Indicateurs de programme dans les programmes d'événements :** Les programmes d'événements affichent désormais des indicateurs de programme lors de la saisie des données d'événements. Les événements utilisent la nouvelle barre de navigation qui permet à l'utilisateur de basculer entre les détails de l'événement, le formulaire de saisie des données de l'événement et les indicateurs de programme d''événements.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3463) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot24.png)

## SAISIE DE DONNÉES DANS LES ENSEMBLES DE DONNÉES
**Indicateurs dans les ensembles de données :** Les ensembles de données affichent désormais des indicateurs dans l'écran de saisie des données. Les indicateurs seront affichés dans la section après les tableaux. 

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3464) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot25.png)


## ANALYSES LOCALES
**Les analyses locales hors ligne dans le Tableau de bord TEI :** Cette version de l'application permet l'affichage de graphiques et de tableaux dans le domaine d'une Instance d'entité suivie. Dans le Tableau de bord TEI, l'onglet "Indicateurs" a été remplacé par l'onglet "Analytics". Dans cette section, l'application affichera :

- Une valeur : soit un Élément de données, soit un Indicateur de programme.
- Retour d’information
- Graphiques permettant de visualiser l'évolution d'un élément de données ou d'un indicateur de programme dans le temps, par étapes répétables.
  - Diagramme à colonnes (sans fond)
  - Diagramme linéaire simple (sans fond)
  - Diagramme linéaire de croissance de l'enfant (fond basé sur les modèles de l'OMS) : poids pour l'âge, taille pour l'âge, poids pour la taille
- Tableaux de l'évolution d'un élément de données ou d'un indicateur de programme dans le temps, par étapes répétables.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-664) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot07.png) | [Capture d'écran2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot06.png) | [Capture d'écran3](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot08.png)

## CARTES
**Affichage des attributs et des éléments de données :** Il est désormais possible d'afficher dans la carte les attributs et les éléments de données ainsi que les coordonnées des TEI, des inscriptions et des événements. Lorsqu'un programme dispose d'attributs ou d'éléments de données configurés sous forme de coordonnées ou de polygones, ceux-ci seront répertoriés en tant que couches cartographiques à afficher dans les cartes.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2893) | [Jira2](https://jira.dhis2.org/browse/ANDROAPP-2978) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot18.png) | [Capture d'écran2](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot19.png)

**Afficher l'emplacement actuel :** Lorsque l'utilisateur ouvre la carte, l'emplacement actuel de l'appareil s'affiche.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3466) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot17.png)

**Navigation vers l'emplacement sélectionné :** Lorsque l'utilisateur ouvre la carte, il pourra ouvrir l'application de navigation par défaut (c'est-à-dire Google Maps) à partir de l'application Android Capture de DHIS2. L'application de navigation par défaut s'ouvrira pour guider la navigation depuis l'emplacement actuel de l'utilisateur jusqu'à la coordonnée précédemment sélectionnée à partir d'une TEI, d'un Enrôlement, d'un Attribut, d'un Événement ou d'un Élément de données.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3467) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot05.png)


## RECHERCHE, ENREGISTREMENT ET TABLEAU DE BORD DE TEI

**Le formulaire de recherche s'ouvre en mode plein écran :** L'écran de recherche couvre la majeure partie de l'écran dans la plupart des implémentations qui ne permettent pas de voir la liste des TEI résultante. Pour éviter toute confusion, le formulaire de recherche des TEI sera ouvert en mode plein écran et les résultats seront affichés lorsque l'utilisateur retournera à l'écran du programme de suivi. 

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3528) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot21.png) 

**Afficher l'unité d'organisation enrôlante dans la liste des TEI :** Lorsque l'utilisateur ouvre un programme de suivi et qu'une liste de TEI s'affiche, l'unité d'organisation enrôlante figurera sur la carte TEI après les attributs TEI. 

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3039) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot16.png)


## FONCTIONNALITÉS DE SUIVI ET D'ÉVÉNEMENTS
**Listes de tâches :** Les listes de tâches ont été implémentées et sont disponibles dans les programmes d'événements ou de suivi. Les listes des tâches sont téléchargées depuis le serveur et l'utilisateur de l'application ne peut les modifier. L'utilisateur a la possibilité d'ajouter des filtres à une liste des tâches sélectionnée.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-651) | [Screenshot](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot14.png) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot15.png)

**Modifier la date d'inscription ou d'incident :** La date d'inscription et d'incident dans les programmes Tracker peut être modifiée même si des événements générés automatiquement ont été créés. Ce comportement aligne la fonctionnalité sur l'implémentation actuelle dans l'application Web Capture.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2510) | [Capture d'écran](https://s3-eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.4/2.4-release-screenshot13.png)

**Unité d'organisation d'une étape de programme non modifiable :** L'unité d'organisation d'une étape de programme (événement) ne peut pas être modifiée. Ce comportement aligne la fonctionnalité sur l'implémentation actuelle dans l'application Web Capture.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3019) 



INFORMATIONS RELATIVES À LA VERSION

|Informations relatives à la version|Lien|
| --- | --- |
|Télécharger l'application à partir de Google Play ou Github (*ADD GITHUB*)|[https://www.dhis2.org/app-store ](https://www.dhis2.org/app-store)| 
|Documentation et Javadocs|[https://www.dhis2.org/android-documentation ](https://www.dhis2.org/android-documentation)|
|Détails sur chaque fonctionnalité de la JIRA ( connexion requise)|[Fonctionnalités de la 2.4](https://jira.dhis2.org/issues/?filter=11956)|
|Aperçu des bugs corrigés sur JIRA ( connexion requise)|[Bugs dans la 2.4](https://jira.dhis2.org/issues/?filter=11957)|
|Instance de démonstration (utilisateur/mot de passe)|[https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) android / Android123|
|La communauté DHIS 2|[La communauté mobile https://community.dhis2.org ](https://community.dhis2.org/c/subcommunities/mobile/16)|
|Code source sur Github|[https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app)|
|Code source de SDK sur Github |[SDK 1.4.0 ](https://github.com/dhis2/dhis2-android-sdk/releases/tag/1.4.0)| 

