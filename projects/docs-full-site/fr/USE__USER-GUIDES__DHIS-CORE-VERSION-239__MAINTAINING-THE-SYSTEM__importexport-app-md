---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.39/src/user/importexport-app.md"
revision_date: "2022-10-23"
tags:
    - Utilisation
    - DHIS version 2.39
---

# Application Import/Export { #import_export }

Dans un système de santé primaire, le SNIS implique généralement une application distribuée, où la même application est exécutée dans différents lieux géographiques (SSP, CSC, hôpitaux, districts et État). Nombre de ces lieux physiques ne disposent pas de connexion Internet et travaillent donc hors ligne. À un moment donné (normalement au niveau du district), les données doivent être synchronisées afin d'avoir une base de données consolidée pour une région géographique particulière. Pour cela, il est important de pouvoir exporter les données d'un lieu (qui travaille hors ligne, par exemple au niveau de l'établissement de santé) et de les importer dans un autre (par exemple au niveau du district). Cette fonction d'exportation et d'importation est donc une fonction cruciale d'un SNIS. Cette fonction nous aide également à surmonter, dans une certaine mesure, la dépendance à l'égard d'Internet, car les mises à jour des données peuvent être transférées par clé USB lorsqu'il n'y a pas de connectivité, ou par courrier électronique lorsque la connectivité à l'Internet est limitée. Le DHIS2 offre une fonctionnalité d'import-export robuste pour répondre à ces besoins.

Pour accéder à l'application Import/Export, cherchez Import/Export dans la barre d'en-tête supérieure. L'application Import/Export offre un certain nombre de services dont les détails sont présentés ci-dessous.

![](resources/images/import_export/overview.png)

## Importation de données { #importing_data }

### Enregistreur de la progression des importations { #import_progress_logger }

Peu importe ce que vous importez ("Données", "Événements", "GML", "Métadonnées" ou "Instances d'entités suivies"), vous pouvez toujours consulter l'état d'avancement de l'importation en consultant le "Résumé des tâches" en haut de la page.

### Résumés des importations { #metadata_import_summaries }

Au moment de remplir la demande d'importation, nous affichons les résumés d'importation au-dessus du formulaire d'importation. Les éventuelles incompatibilités ou erreurs sont indiquées dans le tableau sous le résumé principal de l'importation.

![](resources/images/import_export/import_summary.png)

### Importation de métadonnées { #metadata_import }

L'importation de métadonnées est accessible à partir de la barre latérale en cliquant sur Importation de métadonnées.

![](resources/images/import_export/metadata_import.png)

1.  Choisissez un fichier à télécharger

2.  Sélectionnez un format : _JSON_ , _CSV_ ou _XML_

3.  Sélectionnez les paramètres appropriés pour :

    -   Identificateur
    -   Mode rapport d'importation
    -   Mode d'économie d'énergie
    -   Stratégie d'importation
    -   Mode atomique
    -   Mode Fusion

4.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Mode Flush
    -   Ignorer le partage
    -   Ignorer la validation
    -   Async
    -   Stratégie inclusive

5.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

> **Conseil**
>
> **Il est fortement recommandé d'utiliser l'option "Dry run "** pour tester avant d'importer des données, pour s'assurer que vous gardez le contrôle sur toute modification de vos métadonnées, et pour vérifier les problèmes d'éléments de données ou de noms d'unités d'organisation désynchronisés

> **N.B.**
>
> Si une unité d'organisation, par exemple `Nduvuibu MCHP`, avait une référence inconnue à un objet dont l'ID est `aaaU6Kr7Gtpidn`, cela signifie que l'objet avec ID `aaaU6Kr7Gtpidn` n'était pas présent dans votre fichier importé, et qu'il n'a pas été trouvé dans la base de données existante.
>
> Vous pouvez contrôler cela en utilisant l'option **Identificateur** pour indiquer si vous souhaitez autoriser ou non l'importation d'objets ayant de telles références non valables. Si vous choisissez d'importer des références non valides, vous devrez alors corriger la référence manuellement dans le DHIS2 ultérieurement.

#### Correspondance des identificateurs dans DXF2 { #matching_identifiers_in_dxf2 }

Le format DXF2 prend actuellement en charge la correspondance de deux identificateurs, l'identificateur interne de DHIS2 (connu sous le nom d'UID), et utilisant également un identificateur externe appelé "code". Lorsque l'importateur essaie de rechercher des références (comme celle ci-dessus), il passe d'abord au champ UID, puis au champ code. Cela vous permet d'importer à partir de systèmes existants sans disposer d'un UID pour chaque objet de méta-données. Par exemple, si vous importez des données d'établissement à partir d'un système existant, vous pouvez laisser le champ ID complètement vide (DHIS2 le remplira pour vous) et mettre les identificateurs propres au système existant dans le champ de code ; cet identifiant doit être unique. Cela fonctionne non seulement pour les unités d'organisation, mais aussi pour toutes sortes de métadonnées, ce qui permet d'importer facilement des données à partir d'autres systèmes.

### Importation de données { #import }

L'importation de données est accessible à partir de la barre latérale en cliquant sur Importation de données.

![](resources/images/import_export/data_import.png)

1.  Choisissez un fichier à télécharger

2.  Sélectionnez un format : _JSON_, _CSV_, _XML_, _ADX_ ou _PDF_

3.  Sélectionnez les paramètres appropriés pour :

    -   Stratégie
    -   Préchauffer le cache

4.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Schéma d'identification d'un élément de données
    -   Schéma d'identification d'une unité d'organisation
    -   Schéma d'identification
    -   Ignorer un contrôle existant

5.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

> **Conseil**
>
> **Il est fortement recommandé d'utiliser l'option Test à blanc** pour tester avant d'importer des données, afin de s'assurer que vous gardez le contrôle sur toute modification de vos métadonnées, et pour vérifier les problèmes d'éléments de données ou de noms d'unités d'organisation désynchronisés

#### Données PDF { #importPDFdata }

Le DHIS2 prend en charge l'importation de données au format PDF. On peut l'utiliser pour importer des données obtenues à partir des formulaires de saisie de données PDF hors ligne. Veuillez vous référer à la section **Gestion des ensembles de données** pour savoir comment produire un formulaire PDF pouvant être utilisé pour la saisie de données hors ligne.

Pour importer un fichier de données PDF, naviguez jusqu'à l'élément _Importation de données PDF_ dans le menu latéral. Téléchargez le fichier PDF complété et cliquez sur _Importer_.

### Importation d'événements { #event_import }

L'exportation d'événements est accessible à partir de la barre latérale en cliquant sur Exportation d'événements.

![](resources/images/import_export/event_import.png)

1.  Sélectionnez un format : _JSON_ , _CSV_ ou _XML_

2.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Schéma d'identification des événements
    -   Schéma d'identification d'un élément de données
    -   Schéma d'identification d'une unité d'organisation
    -   Schéma d'identification

3.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

### Importation de Earth Engine { #ee_import }

L'Importation de Earth Engine est accessible à partir de la barre latérale en cliquant sur Importation de Eaeth Engine.

Importez des données démographiques haute résolution depuis WorldPop à l'aide de Google Earth Engine. Un [compte Google Earth Engine](https://docs.dhis2.org/en/topics/tutorials/google-earth-engine-sign-up.html) est nécessaire à l'utilisation de cet importateur.

![](resources/images/import_export/ee_import.png)

#### Sélectionnez les données de Earth Engine à importer { #select-which-earth-engine-data-should-be-imported }

La première section du formulaire sert à configurer les données de Earth Engine à importer.

1. Sélectionnez les données de Earth Engine à importer. Actuellement, les choix portent sur _Population_ et _Groupes d'âge de la population_.

2. Après la sélection d'un ensemble de données, une période doit être sélectionnée. Une seule période peut être importée à la fois.

3. Choisissez la manière dont les données doivent être arrondies. Par défaut, les données ne sont pas arrondies.

4. Sélectionnez les unités d'organisation vers lesquelles les données seront importées. Si vous sélectionnez des unités d'organisation niveau établissement, vous devez choisir une géométrie associée à l'établissement. Sans géométrie associée à l'établissement, Earth Engine ne peut pas déterminer la population.

![](resources/images/import_export/ee_ou_associated_geometry.png)

#### Sélectionnez les éléments de données vers lesquels les données de Earth Engine doivent être importées { #select-the-data-elements-to-import-the-earth-engine-data-into }

Après avoir configuré l'ensemble de données de Earth Engine, vous devez sélectionner l'élément de données vers lequel les données doivent être importées. Pour les ensembles de données scindés en sous-groupes, tels que "Groupes d'âge de la population", l'élément de données DHIS2 doit avoir des sous-éléments sous la forme de combinaisons d'options de catégorie, lesquelles correspondent aux sous-groupes de l'ensemble de données de Earth Engine.

![](resources/images/import_export/ee_group_coc_mapping.png)

> **Configuration des éléments de données pour l'importation depuis Earth Engine**
>
> Lors de la configuration des éléments de données DHIS2 qui vont contenir des données de Earth Engine, si vous prévoyez d'importer des données vers plusieurs niveaux d'unité organisationnelle, assurez-vous que ces niveaux soient ajoutés en tant que niveaux d'agrégation dans la configuration des éléments de données.
>
> Lorsque certains ensembles de données de Earth Engine contiennent des sous-groupes, l'élément de données DHIS2 doit être configuré avec les combinaisons d'options de catégorie correspondantes. Par exemple, l'ensemble de données « Tranches d'âge de la population » est divisé en sous-groupes de genre (homme, femme) et d'âge (par intervalle de 5 ans).
>
> Sur l'interface DHIS2, cela signifie que vous devez avoir une catégorie Homme/Femme et une catégorie de tranche d'âge de 5 ans (<1an, 1-4ans, 5-9ans, 10-14ans... 80+yans). Ces catégories permettent de former des combinaisons.
>
> Conseil de professionnel : pour faire correspondre automatiquement la combinaison d'options de catégorie au sous-groupe de Earth Engine, ajoutez un code à chaque combinaison qui correspond au nom du groupe de Earth Engine. Par exemple, avec « Tranches d'âge de la population », les groupes sont nommés : F_0, F_1, F_5..., M_0, M_1, M_5...

#### Exécutez l'importation { #run-the-import }

Après la sélection des combinaisons d'éléments de données et des options de catégorie, le bouton Aperçu s'active. Après avoir examiné les données que vous souhaitez importer, vous pouvez d'abord effectuer un essai  ou procéder à l'importation proprement dite.

![](resources/images/import_export/ee_data_preview.png)

### Importation de Géométrie d'Unité d'Organisation { #geometry_import }

Accessible depuis la barre latérale en cliquant sur _Importation de la Géométrie de l'Unité d'Organisation_. Deux formats de géométrie sont pris en charge : GeoJSON et GML. GeoJSON est le format recommandé et peut également être utilisé pour importer des géométries associées (zones de chalandise).

#### Importation GeoJSON { #geojson_import }

![](resources/images/import_export/geojson_import.png)

1.  Téléchargez un fichier au format GeoJSON.

2.  Par défaut, l'identifiant de la fonctionnalité GeoJSON doit correspondre à celui de l'unité d'organisation.

3.  Cochez **Faire correspondre la propriété GeoJSON à l'unité d'organisation ** pour faire correspondre une propriété de fonctionnalité. Saisisez le nom de la propriété GeoJSON et sélectionnez l'identifiant de l'unité d'organisation (_Id_, _Code_ ou _Nom_).

4.  Cochez **Importer en tant que géométrie associée** pour importer les éléments GeoJSON en tant que géométries associées aux unités d'organisation (par exemple, les zones d'attraction). Sélectionnez au niveau de l'attribut de géométrie la destination des données. Cela nécessite un attribut de type _GeoJSON_ appliqué à _Unité d'organisation_. Cet attribut peut être défini dans l'application Maintenance.

5.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

> **Conseil**
>
> **Il est fortement recommandé d'utiliser l'option Test à blanc** pour tester avant d'importer des données, afin de s'assurer que vous gardez le contrôle de toute modification de vos géométries d'unités d'organisation.

#### Importation GML { #gml_import }

![](resources/images/import_export/gml_import.png)

1.  Téléchargez un fichier en utilisant le format _GML_ (Langage de balisage géographique).

2.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

### Importation d'instances d'entités suivies { #tei_import }

L'importation des instances d'entités suivies est accessible à partir de la barre latérale en cliquant sur Importation des TEI.

![](resources/images/import_export/tei_import.png)

1.  Choisissez un fichier à télécharger

2.  Sélectionnez un format : _JSON_ ou _XML_

3.  Sélectionnez les paramètres appropriés pour :

    -   Identificateur
    -   Mode rapport d'importation
    -   Mode d'économie d'énergie
    -   Stratégie d'importation
    -   Mode atomique
    -   Mode Fusion

4.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Mode Flush
    -   Ignorer le partage
    -   Ignorer la validation
    -   Stratégie inclusive

5.  Cliquez sur le bouton **Importer** pour télécharger le fichier et lancer le processus d'importation.

> **Conseil**
>
> **Il est fortement recommandé d'utiliser l'option Test à blanc** pour tester avant d'importer des données, afin de s'assurer que vous gardez le contrôle de toute modification de vos instances d'entités suivies.

## Exportation de données { #exporting-data }

### Exportation de métadonnées { #metadata_export }

L'exportation de métadonnées est accessible à partir de la barre latérale en cliquant sur Exportation de métadonnées.

![](resources/images/import_export/metadata_export.png)

1.  Choisissez la liste des objets que vous souhaitez exporter.

2.  Sélectionnez un format : _JSON_

3.  Choisissez un type de compression: _Zip_ , _gzip_ ou _non compressé_.

4.  Vous êtes libre de cocher _Ignorer les paramètres de partage et d'accès_ ou non.

5.  Cliquez sur **Exporter les métadonnées**, ce qui ouvrira une nouvelle fenêtre de navigateur web qui vous fournira un fichier à télécharger sur votre ordinateur local.

### Exportation de métadonnées avec des dépendances { #metadata_export_dependencies }

L'exportation de métadonnées avec dépendances vous permet de créer des exportations ordinaires pour les objets de métadonnées. Ce type d'exportation comprendra les objets de métadonnées et les objets liés à l'objet de métadonnées, c'est-à-dire les métadonnées appartiennant à l'objet principal.

Tableau : Types d'objets et leurs dépendances

| Type d'objet | Dépendances incluses dans l'exportation |
| --- | --- |
| **Ensembles de données** | Eléments de données<br>   <br> Sections <br>   <br> Indicateurs <br>   <br> Types d'Indicator <br>   <br> Attributs<br>   <br> Formulaires de saisie <br>   <br> Ensemble de données <br>   <br> Légendes <br>   <br> Combinaisons de catégories <br>   <br> Catégorie<br>   <br> Options de catégorie <br>   <br> Combinations d'options de catégorie<br>   <br>Ensemble d'options |
| Programmes | Formulaire de saisie <br>   <br>Entité suivie <br>   <br> Etapes de programme <br>   <br>Attributs de programme <br>   <br> Indicateurs de programme <br>   <br> Règles de programme <br>   <br> Actions de la règle de programme <br>   <br> Variables de la règle de programme <br>   <br> Attributs du programme <br>   <br> Eléments de données <br>   <br> Combinaison de catégories <br>   <br> Catégories<br>   <br> Options de catégorie <br> <br> Combinaisons d'options de catégorie <br> <br> Ensemble d'options |
| Combinaison de catégories | <<Combinaisons de catégories<br> Catégories<br>Options de catégorie<br> <br>Combinaisons d'options de catégorie<br> <br>Attributs>> |
| Tableau de bord | <Eléments du tableau de bord <br>   <br>Graphiques   <br> Graphiques d'évènements <br>   <br> Tableau croisé dynamique <br>   <br> Rapports d'évènements <br>   <br> Cartes<br>   <br> Rapports<br>   <br> Ressources> |
| Groupes d'éléments de données | Eléments de données <br>   <br> Combinaisons de catégories <br>   <br> Catégories<br>   <br> Options de catégories <br>   <br>Combinaisons d'options de catégorie <br>   <br> Ensemble d'options <br>   <br> Attributs <br>   <br> Ensemble de légendes <br>   <br> Légendes |
| Ensemble d'options | Option |

![](resources/images/import_export/metadata_dependency_export.png)

![](resources/images/import_export/metadata_dependency_export_object_types.png)

1.  Sélectionnez un type d'objet : _Ensemble de données_, _Programmes_, _Combinaison de catégories_, _Tableau de bord_, _Groupes d'éléments de données_ ou_Ensemble d'options_.

2.  Sélectionnez un objet.

3.  Sélectionnez un format : _JSON_

4.  Choisissez un type de compression: _Zip_ , _GZip_ ou _non compressé_.

5.  Cliquez sur **Exporter les dépendances des métadonnées**, ce qui ouvrira une nouvelle fenêtre de navigateur web qui vous fournira un fichier à télécharger sur votre ordinateur local.

### Exportation de données { #data_export }

L'exportation de données est accessible à partir de la barre latérale en cliquant sur Exportation de données.

![](resources/images/import_export/data_export.png)

1.  Sélectionnez les unités d'organisation à partir desquelles les données seront exportés.

2.  Choisissez si vous souhaitez que l'exportation prenne en compte les descendants des unités d'organisation sélectionnées à l'étape 1 ou uniquement les unités d'organisation sélectionnées manuellement.

3.  Sélectionnez les ensembles de données qui seront exportés.

4.  Définissez les dates de début et de fin

5.  Sélectionnez un format : _JSON_, _CSV_, _XML_, _ADX_

6.  Sélectionnez un mode de compression : **Zip** , **GZip** ou **Non compressé**.

7.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Inclure les éléments supprimés
    -   Schéma d'identification d'un élément de données
    -   Schéma d'identification d'une unité d'organisation
    -   Schéma d'identification

8.  Cliquez sur **Exporter les données**, ce qui ouvrira une nouvelle fenêtre de navigateur web qui vous fournira un fichier à télécharger sur votre ordinateur local.

### Exportation d'événements { #event_export }

L'exportation d'événements est accessible à partir de la barre latérale en cliquant sur Exportation d'événements.

![](resources/images/import_export/event_export.png)

Vous pouvez exporter des données d'événement ou de suivi en utilisant les formats JSON, CSV ou XML.

1.  Sélectionnez une unité d'organisation.

2.  Sélectionnez l'inclusion :

    -   _Sélectionnée_ : Exporter les données de l'événement uniquement pour l'unité d'organisation sélectionnée

    -   _Directement en dessous_ : Exporter les données de l'événement, y compris le premier niveau des unités d'organisation dans les sélections ainsi que l'unité d'organisation sélectionnée elle-même.

    -   _Toutes en dessous_ : Exporter les données d'événements pour toutes les unités d'organisation dans les sélections ainsi que pour l'unité d'organisation sélectionnée elle-même.

3.  Sélectionnez un programme et une étape du programme (le cas échéant).

4.  Définissez les dates de début et de fin

5.  Sélectionnez un format : _JSON_ , _CSV_ ou _XML_

6.  Choisissez un mode de compression: _Zip_ , _GZip_ ou _non compressé_.

7.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Inclure les éléments supprimés
    -   Schéma d'identification d'un élément de données
    -   Schéma d'identification d'une unité d'organisation
    -   Schéma d'identification

8.  Cliquez sur **Exporter les événements**, ce qui ouvrira une nouvelle fenêtre de navigateur web qui vous fournira un fichier à télécharger sur votre ordinateur local.

### Exportation d'instances d'entités suivies { #tei_export }

L'Exportation des instances d'entités suivies est accessible à partir de la barre latérale en cliquant sur Exportation des TEI.

![](resources/images/import_export/tei_export.png)

Vous pouvez exporter des données d'événement ou de suivi en utilisant les formats JSON, CSV ou XML.

1.  Sélectionnez les unités d'organisation à inclure.

2.  Choisissez si vous voulez filtrer par programme ou type d'entité suivie.

3.  Sélectionnez un format : _JSON_ , _CSV_ ou _XML_

4.  Cliquez sur **Options avancées** si vous souhaitez ajuster un ou plusieurs des paramètres suivants avant l'importation :

    -   Filtrer par date de dernière mise à jour
    -   Mode d'utilisateur assigné
    -   Inclure les éléments supprimés
    -   Inclure tous les attributs
    -   Schéma d'identification d'un élément de données
    -   Schéma d'identification des événements
    -   Schéma d'identification d'une unité d'organisation
    -   Schéma d'identification

5.  Cliquez sur **Exporter les instances d'entités suivies**, ce qui ouvrira une nouvelle fenêtre de navigateur web qui vous fournira un fichier à télécharger sur votre ordinateur local.

## Aperçu des tâches { #job_overview }

La page d'aperçu des tâches peut être consultée dans la barre latérale en cliquant sur _Aperçu des tâches_.

![](resources/images/import_export/job_overview.png)

Cette page vous permet de vérifier l'état d'avancement de toutes les importations que vous avez lancées au cours de cette session. Vous pouvez voir la liste de toutes les tâches sur le côté gauche et des détails relatifs à une tâche spécifique sélectionnée sur le côté droit.

### Filtrage par type de tâche d'importation { #filtering-by-import-job-type }

![](resources/images/import_export/job_overview_filter.png)

Par défaut, les tâches de tous les types d'importation sont affichées dans la liste des tâches, mais vous pouvez filtrer les catégories qui vous intéressent en cliquant sur les filtres des types de tâches au-dessus de la liste des tâches.

### Recréer une ancienne tâche { #recreating-a-previous-job }

![](resources/images/import_export/job_overview_recreate.png)

Vous pouvez recréer les tâches d'importation précédemment exécutées en cliquant sur le bouton _Recréer une tâche_ situé au bas de la page, à condition que vous ayez sélectionné une tâche dans la liste. Cela vous amènera à la page d'importation appropriée et vous permettra de remplir tous les détails du formulaire conformément à la tâche que vous avez choisie de recréer.

## Schémas { #schemes }

Les différents schémas utilisés dans de nombreuses pages d'importation et d'exportation sont également connus sous le nom de schémas d'identification et sont utilisés pour relier les objets de métadonnées à d'autres métadonnées lors de l'importation, et pour restituer les métadonnées dans le cadre du processus d'exportation.

Tableau : Valeurs disponibles

| Schéma | Description |
| --- | --- |
| ID, UID | Correspondance avec l'identifiant permanent DHIS2. il s'agit du schéma d'identification par défaut. |
| CODE | Correspondre avec le code DHIS2, principalement utilisé pour échanger des données avec un système externe. |
| NOM | Correspondre avec le nom DHIS2. Veuillez noter que c'est l'élément disponible en tant que _nom.de l'objet_ qui est utilisé, et non le nom traduit. Notez également que les noms ne sont pas toujours uniques. Lorsque des noms sont déjà utilisés, ils ne peuvent plus l'être. |
| ATTRIBUT:ID | Correspondre avec l'attribut de métadonnées. Cet attribut doit être assigné au type sur lequel vous faites correspondre, d'autant plus que la propriété unique est définie sur _vrai_. Cette fonctionnalité permet principalement d'échanger des données avec des systèmes externes. Il présente certains avantages par rapport à _CODE_ puisque plusieurs attributs peuvent être ajoutés. Il peut donc se synchroniser avec plus d'un système. |

### Schéma d'identification { #id-scheme }

Le schéma d'identification s'applique à tous les types d'objets, mais peut également être écrasé par des types d'objets plus spécifiques.
