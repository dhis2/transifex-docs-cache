---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/android-releases/2.6/ReleaseNote-2.6.0.md"
revision_date: "2022-04-18"
---

# Note de publication de l'application Android DHIS2 version 2.6 { #dhis2-android-app-version-26-release-notes }

## FONCTIONNALITÉS D'AIDE À L'IMPLÉMENTATION { #implementation-support-features }

**Prise en charge de plusieurs utilisateurs hors ligne : ** L'application Android peut désormais fonctionner avec un maximum de 3 utilisateurs différents en mode hors ligne. Les utilisateurs devront avoir accès à Internet pour la première connexion de chaque compte et pourront ensuite changer de compte sans avoir besoin d'accéder à Internet. Les utilisateurs pourront gérer les comptes d'utilisateurs et supprimer des comptes si nécessaire. Lorsque le nombre maximum de comptes sera atteint, il sera nécessaire de supprimer un des comptes existants pour se connecter à un nouveau compte.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-653) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users.png) | [Capture d'écran 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Multiple-users-2.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_multiuser)

**Dépannage de la configuration:** Cette fonctionnalité est destinée aux administrateurs. L'application Android intègre une option dans l'écran des paramètres pour vérifier certains aspects de la configuration du DHIS2.

-   Langue : l'utilisateur pourra changer la langue de l'interface utilisateur de l'application afin d'identifier les étiquettes, les boutons ou les invites erronées ou sans traduction.
-   Validation des règles du programme : ce validateur vérifie les règles du programme dans l'appareil et affiche les incohérences de configuration.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-1655) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting.png) | [Capture d'écran 2](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Configuration-troubleshooting-2.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_configuration_troubleshooting)

## ANALYSES HORS LIGNE { #offline-analytics }

**Prise en charge des légendes pour les tableaux dans les analyses:** Les légendes sont affichées dans les tableaux croisés dynamiques en activant la fonction "Utiliser les légendes pour la couleur du graphique" dans l'application Data Visualizer. L'application Android colorera les cellules en utilisant soit la légende prédéfinie par élément de données, soit une légende unique pour l'ensemble du tableau croisé dynamique, en fonction des paramètres définis dans Web.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4500) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Legend-Sets.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_pivot_legends)

## FONCTIONNALITÉS DU TRACKER { #tracker-features }

**Briser la glace:** Si le programme est configuré avec un niveau d'accès "Protégé" et qu'une recherche est effectuée en dehors du champ d'application de l'utilisateur, une boîte de dialogue demandant une raison d'accès sera affichée pour que l'utilisateur puisse temporairement passer outre le privilège de propriété du programme. Cela signifie que l'utilisateur aura accès aux données relatives au programme.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-657) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Break-the-glass.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_breaking_the_glass)

**Rendre la recherche obligatoire de TEI configurable:** La recherche de TEI avant la création n'est pas obligatoire actuellement. En utilisant l'application Android Settings App (v2.2.0), il est possible de configurer le flux utilisateur pour la création de TEI. Si la fonctionnalité est activée, l'application Android affichera un bouton "create new" après l'ouverture d'un programme et une recherche sera facultative.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4545) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Mandatory-TEI-Search-Config.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_configurable_search)

**Flux de recherche hors ligne/en ligne distincts:** Pour améliorer le temps de réponse dans les résultats de recherche, l'application Android effectue désormais une recherche hors ligne en premier lieu et affiche les résultats tout en effectuant une recherche en ligne dans un second temps, de manière transparente pour l'utilisateur. La recherche hors ligne est proposée comme deuxième étape lorsque les attributs utilisés dans la recherche contiennent au moins un attribut TET (Tracked Entity Type).

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4023) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Search-flow.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_offline_online_search)

## FONCTIONNALITÉS DE SAISIE ET DE SYNCHRONISATION DES DONNÉES { #data-entry-and-sync-features }

**Scanner et afficher les codes QR Data matrix GS1:** Si un type de rendu d'attribut ou d'élément de données est configuré en tant que code QR, l'application Android sera en mesure de lire et de traiter la chaîne de caractères en tant que codes Data Matrix GS1. Combiné avec l'utilisation des fonctions d2 dans les règles du programme, les différents champs d'un code GS1 peuvent être enregistrés dans différents éléments de données ou attributs (d2:extractDataMatrixValue(key, dataMatrixText)).

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4329) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-GS1-Data-matrix.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_gs1)

**Autoriser l'utilisateur à " actualiser les données " pour obtenir les dernières données mises à jour depuis le serveur : ** Les utilisateurs peuvent désormais récupérer les dernières données depuis le serveur avant de saisir de nouvelles données. Un bouton de réactualisation est désormais disponible pour déclencher une synchronisation granulaire dans les écrans suivants :

-   Accueil
-   Recherche
-   Tableau de bord des TEI
-   Liste des programmes d'événement
-   Détails sur l'événement
-   Liste des ensembles de données
-   Détails de l'ensemble des données

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4331) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Refresh-data.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_refresh_data)

**Rendu des icônes dans les formulaires d'inscription:** La saisie de données basée sur des icônes peut désormais être utilisée dans les formulaires d'inscription. Lorsqu'une section d'inscription contient un ou plusieurs attributs d'entités suivies auxquels sont attribués des ensembles d'options et des icônes, l'application est capable de les afficher sous forme de matrice ou de séquence en fonction du type de rendu de la section. Dans les sections précédentes de l'application, cette fonctionnalité n'était disponible que pour les éléments de données.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4258) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Render-icons-in-enrollment-forms.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_icon_lib)

**Améliorer le flux Enregistrer et Terminer dans les événements : ** De nouvelles boîtes de dialogue s'affichent lors de l'enregistrement d'une inscription ou d'un événement. Le bouton "Rouvrir" est désormais situé dans l'écran de détails et il ne sera disponible que si l'utilisateur a l'autorité correcte ("événements non terminés") pour rouvrir un événement terminé. Le concept et le dialogue "achèvement" sont désormais plus intuitifs et plus conviviaux.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4610) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Save-and-complete-flow.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Nouveau design pour les avertissements/erreurs et les dialogues d'achèvement:** Les messages d'erreur et d'avertissement ont été améliorés pour fournir à l'utilisateur des informations plus nombreuses et de meilleure qualité. Les nouveaux dialogues lors de l'enregistrement permettent à l'utilisateur d'ignorer les modifications, d'enregistrer et de corriger plus tard ou de continuer à éditer le formulaire pour corriger les valeurs en fonction de la configuration.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4591) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Warnings-errors-dialogs.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_common_features_errors)

**Amélioration du design des colonnes des ensembles de données : ** Les flèches de redimensionnement sont désormais situées dans le coin supérieur gauche de l'écran.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3016) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Dataset-span.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/datasets-features.html#capture_app_data_sets_row)

**Afficher l'indice de l'UO sélectionnée lors de l'ouverture de la hiérarchie des UO:** Si une unité d'organisation est sélectionnée, lors de l'affichage de la hiérarchie, toutes les UO ascendantes (parentes) seront en gras pour aider l'utilisateur à naviguer dans la sélection précédente.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-2520) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.6/Release+Feature+Cards/Android-2-6-Ou-hint.png) | [Documentation](https://docs.dhis2.org/en/use/android-app/android-specific-features.html#capture_app_generic_orgunit)

**Améliorer la prévention de la duplication des identifiants uniques :** lors d'une recherche par attributs uniques et de la création d'une nouvelle inscription, si la recherche renvoie un résultat, l'application ne conservera pas les valeurs des attributs uniques dans le formulaire d'inscription.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4250) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_programs_search)

**Masquer le bouton de sauvegarde si le formulaire n'est pas modifiable:** Si un événement est expiré ou dispose uniquement de droits de visualisation, le bouton de sauvegarde sera masqué.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4613) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#capture_app_common_features_complete_reopen)

**Alignement de la barre inférieure de navigation des événements:** L'onglet détails de la barre de navigation des événements a été amélioré pour offrir une meilleure expérience utilisateur.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-3651) | [Documentation](https://docs.dhis2.org/en/use/android-app/program-features.html#navigation-bar)

**Améliorer le design de l'élément de données "Oui seulement" : ** L'étiquette "Oui" à côté de la case à cocher ou du bouton radio a été supprimée.

[Jira](https://jira.dhis2.org/browse/ANDROAPP-4493) | [Documentation](https://docs.dhis2.org/en/use/android-app/visual-configurations.html#capture_app_visual_render)

## MAINTENANCE { #maintenance }

**Qualité / Sécurité / Performance:** Vous pouvez trouver une liste de problèmes liés à la qualité, la sécurité et la performance en ouvrant ce [filtre jira](https://jira.dhis2.org/issues/?filter=12363).

**Correction des bogues : ** Vous pouvez trouver une liste des bogues corrigés dans cette version en ouvrant ce [filtre jira](https://jira.dhis2.org/issues/?filter=12364).

## INFORMATIONS SUR LA VERSION { #release-info }

| Informations sur la version | Lien |
| --- | --- |
| Télécharger l'application à partir de Google Play ou Github | [Google Play](https://www.dhis2.org/app-store) - [Github](https://github.com/dhis2/dhis2-android-capture-app/releases) |
| Documentation | [https://www.dhis2.org/android-documentation](https://docs.dhis2.org/en/full/use/dhis2-android-app.html) |
| Détails sur chaque fonctionnalité de JIRA ( connexion requise) | [Fonctionnalités de la 2.6 ](https://jira.dhis2.org/issues/?filter=12365) |
| Aperçu des bugs corrigés sur JIRA ( connexion requise) | [2.6 Bugs](https://jira.dhis2.org/issues/?filter=12364) |
| Instance de démonstration (utilisateur/mot de passe) | [https://play.dhis2.org/demo/ ](https://play.dhis2.org/demo/) Credentials: android / Android123 |
| La communauté DHIS 2 | [https://community.dhis2.org Mobile Community ](https://community.dhis2.org/c/subcommunities/mobile/16) |
| Code source sur Github | [https://github.com/dhis2/dhis2-android-capture-app ](https://github.com/dhis2/dhis2-android-capture-app) |
| Code source de SDK sur Github | [https://github.com/dhis2/dhis2-android-sdk](https://github.com/dhis2/dhis2-android-sdk) |
