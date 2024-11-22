---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/2.7/android-releases/2.7/ReleaseNote-2.7.0.md"
revision_date: "2022-10-17"
---

# Note de mise à jour de la version 2.7 de l'application Android du DHIS2 { #dhis2-android-app-version-27-release-notes }

## EXPÉRIENCE UTILISATEUR { #user-experience }

**Multiplication des zones cliquables dans les icônes et les boutons :** Certains boutons ou étiquettes cliquables de l'application Android comportaient de petites zones sensibles sur lesquelles l'utilisateur pouvait appuyer. L'ensemble de l'interface utilisateur a été revu et les zones touchables ont été augmentées. Par exemple, le bouton "+" pour créer une nouvelle étape ou l'icône "˅" pour ouvrir les détails TEI ou développer une section.[Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4728) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Increase-tappable-areas-card.png) | [Documentation]()

**Formulaires de saisie de données épurées :** Les champs de saisie comportaient un message d'aide indiquant "Insérer la valeur ici" qui demeurait après la saisie de la valeur. Nous avons conservé les indications lorsque le champ est vide, mais elles disparaissent désormais une fois la valeur saisie par l'utilisateur. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-3999) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Remove-hints-from-fields-card.png) | [Documentation]()

** Simplification du processus de création d'une étape de programme :** Lorsque l'utilisateur regroupe les événements par étape de programme dans un programme tracker, l'option de création d'une étape n'était visible que lorsque les événements de l'étape de programme spécifique étaient développés. Dans cette version, l'option pour créer un nouvel événement est toujours visible. Lorsque l'utilisateur appuie sur le bouton, cette étape du programme se déploie en affichant tous les événements déjà existants de cette étape particulière du programme. De plus, lorsqu'il n'y a qu'une seule option basée sur la configuration du programme, l'étape du programme disponible est sélectionnée automatiquement et l'étape de sélection de l'étape du programme est ignorée. [Jira 1](https://dhis2.atlassian.net/browse/ANDROAPP-4729) | [Jira 2](https://dhis2.atlassian.net/browse/ANDROAPP-3999) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Add-event-button-always-visible-card.png) | [Documentation]()

**Déplacer le bouton "Partager" dans le tableau de bord des TEI vers un menu secondaire :** Le tableau de bord des TEI présentait un bouton noir "Partager" qui utilisait un espace important sur l'écran et ne s'alignait pas avec le design visuel de l'application alors que la fonction est très peu utilisée. Le bouton a été supprimé et la fonction de partage d'une TEI par code QR a été placée dans le menu à trois points verticaux, dans le coin supérieur droit de l'écran. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4653) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Remove-share-button-from-TEI-dashboard-card.png) | [Documentation]()

**Navigation plus intuitive pour les sections d'événements :** La navigation en accordéon des sections de formulaire prêtait à confusion pour certains utilisateurs et l'action qui suivait le remplissage du dernier champ d'une section n'était pas intuitive. Cette version de l'application inclut un bouton "Suivant" à la fin de chaque section qui appelle l'utilisateur à l'action. La fonction de ce bouton est de fermer la section en cours et d'ouvrir la nouvelle section. [Jira]() | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Next-button-at-the-end-of-each-section-card.png) | [Documentation]()

**Nouveau dialogue de saisie pour les ensembles de données :** Lorsque l'utilisateur saisit des données dans un ensemble de données, le clavier s'ouvre en occupant la majeure partie de l'écran et le tableau de l'ensemble de données. Le nouveau dialogue de saisie ouvre un champ de saisie au-dessus du clavier qui affiche le nom de l'élément de données et les options de catégorie du champ sélectionné, ce qui permet à l'utilisateur de conserver son contexte lorsqu'il navigue dans les tableaux pendant la saisie des données. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4827) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Cell-editor-card.png) | [Documentation]()

## ANALYSES LOCALES { #local-analitics }

**Nouveau style de légende dans les tableaux :** Le style des légendes dans les tableaux présente un nouveau design qui assure un bon contraste et une bonne visibilité indépendamment de la couleur sélectionnée pour la légende. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4649) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Updated-table-legends-style-card.png) | [Documentation]()

**Implémentation des fonctions d'agrégation manquantes :** Les fonctions d'agrégation suivantes sont désormais prises en charge dans les analyses locales : DERNIER, PREMIER, ORG_UNIT_MOYENNE_SOMME, ORG_UNIT_DERNIER_SOMME, DERNIER_DANS_LA PÉRIODE, ORG_UNIT_DERNIER_DANS_LA PÉRIODE_MOYENNE, ORG_UNIT_PREMIER_MOYENNE [Jira]([Implémentation des fonctions d'agrégation manquantes](https://dhis2.atlassian.net/browse/ANDROAPP-4883)) | [Documentation]()

## PROCESSUS DE SYNCHRONISATION { #sync-process }

**Ouvrir l'accueil après la synchronisation des métadonnées :** Lorsqu'un utilisateur se connecte à l'application Android pour la première fois, l'application doit télécharger toutes les métadonnées et les données, y compris les ressources des fichiers. En fonction de la configuration du serveur et de l'utilisateur, des ressources du serveur et de la connexion internet, ce processus peut être très long. Avant cette version, tout cela se passait sur l'écran d'accueil et l'utilisateur devait attendre pendant tout ce temps sur le même écran. Nous ne pouvons pas changer ce processus ou ce temps d'attente, mais nous pouvons le rendre plus interactif et informatif. Dans cette nouvelle version, l'application restera sur l'écran de démarrage pendant le téléchargement des métadonnées et s'ouvrira sur l'écran d'accueil une fois que les métadonnées seront dans l'appareil. Sur l'écran d'accueil, l'application indiquera à l'aide d'une roue de chargement sur chaque programme quand les données sont en cours de téléchargement et quand elles sont prêtes. L'utilisateur pourra voir combien de programmes sont en train de télécharger des données, ou terminés, ce qui rendra le processus d'attente plus transparent et informatif quant à sa progression. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4765) | [Screenshot](https://s3.eu-west-1.amazonaws.com/content.dhis2.org/dhis2-android/release+notes+2.7/Release+feature+cards/Android-2-7-Visual-data-sync-card.png) | [Documentation]()

**Pas de synchronisation complète au moment de l'ouverture de l'application :** Avant cette version, chaque fois qu'un utilisateur ouvrait l'application de capture DHIS2, celle-ci lançait un processus de synchronisation des données et des métadonnées, pour s'assurer que l'application était synchronisée avec le serveur. Dans la plupart des cas et des lieux, ce processus était très lent. Afin de faciliter le travail dans les cas les plus difficiles, nous avons supprimé ce processus de synchronisation. Lorsque l'utilisateur ouvre l'application, même s'il se déconnecte et se reconnecte, l'application s'ouvre sans effectuer de synchronisation complète. Les utilisateurs ont la possibilité de se synchroniser avec le serveur par le biais du bouton Refresh (Actualiser) quand ils le souhaitent. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4766) | [Documentation]()

## FONCTIONNALITÉS DU TRACKER { #tracker-features }

**Gestion de la propriété dans les renvois permanents :** Depuis la version 2.7, lorsqu'un utilisateur fait un renvoi permanent d'une TEI, la propriété est mise à jour en conséquence. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-4199) | [Documentation]()

## SOUTIEN À L'IMPLÉMENTATION SUR MOBILE { #mobile-implementation-support }

**Télécharger l'APK SMS :** À partir de cette version, l'application disponible dans Google Play intègre la fonctionnalité SMS. Dans les versions précédentes, cette fonctionnalité était uniquement disponible sur un apk disponible sur Github. [Jira](https://dhis2.atlassian.net/browse/ANDROAPP-3888) | [Documentation]()

## QUALITÉ, PERFORMANCE ET STABILITÉ { #quality-performance-and-stability }

**Ensembles de données**

-   [Problème sur Jira 1](https://dhis2.atlassian.net/browse/ANDROAPP-4811)
-   [Problème sur Jira 2](https://dhis2.atlassian.net/browse/ANDROAPP-4744)
-   [Problème sur Jira 3](https://dhis2.atlassian.net/browse/ANDROAPP-4754)
-   [Problème sur Jira 4](https://dhis2.atlassian.net/browse/ANDROAPP-4793)
-   [Problème sur Jira 5](https://dhis2.atlassian.net/browse/ANDROAPP-4828)
-   [Problème sur Jira 6](https://dhis2.atlassian.net/browse/ANDROAPP-4830)
-   [Problème sur Jira 7](https://dhis2.atlassian.net/browse/ANDROAPP-4855)
-   [Problème sur Jira 8](https://dhis2.atlassian.net/browse/ANDROAPP-4857)
-   [Problème sur Jira 9](https://dhis2.atlassian.net/browse/ANDROAPP-4942)

    **Processus de synchronisation**

-   [Problème sur Jira 1](https://dhis2.atlassian.net/browse/ANDROAPP-4892)
-   [Problème sur Jira 2](https://dhis2.atlassian.net/browse/ANDROAPP-4434)
-   [Problème sur Jira 3](https://dhis2.atlassian.net/browse/ANDROAPP-4767)
-   [Problème sur Jira 4](https://dhis2.atlassian.net/browse/ANDROAPP-4778)
-   [Problème sur Jira 5](https://dhis2.atlassian.net/browse/ANDROAPP-4800)

**Formulaires**

-   [Problème sur Jira 1](https://dhis2.atlassian.net/browse/ANDROAPP-4844)
-   [Problème sur Jira 2](https://dhis2.atlassian.net/browse/ANDROAPP-4845)
-   [Problème sur Jira 3](https://dhis2.atlassian.net/browse/ANDROAPP-4846)
-   [Problème sur Jira 4](https://dhis2.atlassian.net/browse/ANDROAPP-4847)
