---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/maintenance_use/localization-of-dhis2.md"
revision_date: '2022-08-08'
tags:
- Implémentation
---

# Localisation du DHIS 2{ #localization-of-dhis-2 }

## Concepts de localisation du DHIS 2 { #localization-intro }

La localisation suppose l'adaptation d'une application à un lieu spécifique. Lors de l'implémentation du DHIS 2 dans un pays donné, des ressources adéquates doivent être allouées pour traduire et localiser l'application si nécessaire. La traduction des éléments de l'interface utilisateur, des messages, de la présentation, des formats de date et d'heure, des devises et d'autres aspects doit être envisagée. Outre la traduction de l'interface utilisateur elle-même, le contenu des métadonnées de la base de données doit également être traduit.

Les traductions d'interface sont compilées dans le système lui-même, de sorte que les nouvelles traductions ne soient accessibles qu'avec une version plus récente du DHIS 2. Les traductions de base de données, quant à elles, sont spécifiques à votre implémentation et peuvent être ajoutées à votre instance DHIS 2 existante.

Ces deux aspects sont gérés de façon distincte et les processus et outils sont décrits ci-dessous.


## Localisation de l'interface utilisateur { #user-interface-localization }

### Aperçu { #overview } 

DHIS 2 prend en charge l'internationalisation (i18n) de l'interface utilisateur grâce à l'utilisation de chaînes de propriétés Java et de fichiers PO. Les fichiers de propriétés Java sont utilisés lorsque les messages proviennent du serveur Java back-end, tandis que les fichiers PO sont utilisés pour les applications front-end développées en JavaScript. Les applications Android du DHIS 2 utilisent un format XML spécifique.

> **Remarque**
>
> Le traducteur ne doit pas se préoccuper des différents formats de fichiers ressource ; la plate-forme de traduction masque ces détails et n'affiche que les chaînes avec les caractères à traduire. 
> Par exemple, la figure ci-dessous montre les chaînes source et cible lors de la traduction d'une ressource en français.
>>>>
> ![](resources/images/translation_ui.jpg)

Tous les messages du DHIS 2 devraient toujours comporter une chaîne en anglais. Lorsque l'utilisateur sélectionne une langue donnée et qu'une traduction est disponible dans cette langue, la traduction est affichée. Toutefois, si la chaîne n'est pas disponible dans la langue souhaitée, des règles de récupération seront appliquées. Lorsque deux traductions données, telles que le portugais et le portugais brésilien, ont des messages communs, il n'est pas nécessaire d'effectuer une traduction complète dans la variante linguistique. Seuls les messages différents doivent être traduits. 
Les règles de récupération sont alors appliquées comme suit (en supposant que l'utilisateur ait sélectionné le portugais brésilien :

1.  Afficher le message en portugais brésilien s'il existe.

2.  S'il n'existe pas dans la variante linguistique, utiliser le message en portugais, s'il existe.
     

3.  S'i le message n'existe ni dans la langue de base ni dans la variante, choisissez la langue par défaut, l'anglais.
     


> **Important**
>
> Certaines chaînes sources telles que "dd MMM yyyy 'to '" qui sont utilisées pour le formatage date/heure dans DHIS2. Une partie de la valeur ne doit pas être traduite car il s'agit d'un champ de formatage spécial utilisé par Java ou JavaScript pour insérer ou formater une chaîne. Dans cet exemple, la partie de la valeur qui **peut** être traduite serait "to", par exemple "a" en espagnol. La chaîne spéciale qui ne doit **pas** être traduite est "dd MMM yyyy". Si ce type de chaînes de format date sont traduites, cela peut entraîner des erreurs dans l'application !
> **Important**
>
> Certaines variables spéciales (par exemple {0} ) utilisent des crochets. Cela indique une variable qui sera remplacée par un nombre ou une autre valeur par l'application. Vous devez placer cette notation de variable au bon endroit et veiller à ne pas la modifier.
>>>>>>>>>>

### Plateforme de traduction{ #translation-server }

DHIS2 utilise désormais [transifex] (https://www.transifex.com) comme plateforme principale de gestion des traductions. Vous pouvez accéder aux ressources du DHIS2 sur le site [translate.dhis2.org](https://translate.dhis2.org), ou directement sur le serveur https://www.transifex.com/hisp-uio/public.

### Comment puis-je participer aux traductions ? { #how-do-i-contribute-to-translations }

#### S'inscrire en tant que traducteur { #register-as-a-translator }

La première étape consiste à accéder au projet. Il existe deux façons d'y parvenir :

1. Accéder à la plateforme et créez un compte transifex, puis
    - demander l'accès à notre organisation "HISP UiO" en tant que membre de l'équipe de traduction "DHIS 2 Core Apps".
    Transifex propose quelques instructions utiles
ici :
[Débuter en tant que traducteur] (https://docs.transifex.com/getting-started-1/translators)

1. Envoyez un e-mail à l'équipe DHIS2 à l'adresse translate@dhis2.org pour demander l'accès.
Veuillez fournir :
    - le nom, l'adresse e-mail et la langue de traduction du ou des utilisateurs auxquels vous voulez que nous accordions l'accès, et
    - quelques informations sur les raisons pour lesquelles vous souhaitez contribuer aux traductions du DHIS2

#### Traduire { #edit-translations }

Une fois que vous avez obtenu l'accès en tant que traducteur, vous pouvez commencer à traduire à l'aide de l'éditeur Web transifex.

Transifex propose un guide utile ici : [Traduire en ligne avec l'éditeur Web] (https://docs.transifex.com/translation/translating-with-the-web-editor)

Dans la mesure du possible, les projets représentent les applications DHIS 2 à l'identique. Par exemple, le projet **APP : Data Visualizer** contient les chaînes de traduction de l'application Visualiseur de données.

Nos projets transifex pour l'interface utilisateur DHIS2 ont l'un des éléments suivants en début de nom :

- **APP:** indique que le projet contient des chaînes pour une application spécifique
- **APP-COMPONENT:** indique que le projet est une bibliothèque de composants utilisée par les applications.
- **ANDROID:** indique que le projet est une application Andriod

De plus, **APP: Server-Side Resources** (Ressources du serveur) contient des chaînes utilisées par plusieurs applications, à savoir :
- "Saisie de données"
- "Maintenance"
- "Tableaux croisés dynamiques"
- "Rapports"

Dans les projets, nous avons des ressources qui représentent des fichiers de localisation dans le code source. Afin de prendre en charge plusieurs versions de DHIS2 avec les mêmes fichiers de localisation, la _version_ est associée à chaque instance du fichier. Ainsi, pour **APP : Data Visualizer** (visualiseur de données), la liste des ressources se présente comme suit dans l'éditeur Web :

![](resources/images/transifex_data_vis.jpg)

Par exemple, il n'y a qu'une seule ressource source pour l'application (`en.pot`), mais nous avons ajouté la version 2.31 (v31) et toutes les versions suivantes jusqu'à la dernière version développée (master). La version est affichée dans le champ "Catégorie", et est également visible en tant que préfixe du nom de la ressource, par exemple `v31--en-pot`.

> **Remarque**
>
> En général, nous demandons aux traducteurs de se concentrer sur la ressource "**master**" ; elle contient généralement toutes les chaînes des versions précédentes, et lorsque des traductions sont ajoutées, la plate-forme ajoutent également les traductions correspondantes au niveau des versions précédentes. Voir la section [localisation](https://dhis2.org/localization/#section-2) de notre site web.

> **Astuce** { .tip }
>
> Pour une langue et une version DHIS2 données, vous pouvez voir les parties traduites. En plus, des liens directs vous conduisent vers toutes les ressources concernées sur transifex, à partir de la section [localisation](https://dhis2.org/localization/#section-2) de notre site web.

### À quel moment les nouvelles traductions seront-elles disponibles dans le système ?{ #when-will-new-translations-be-available-in-the-system }

Nous avons un service de nuit qui extrait les nouvelles traductions de la plateforme transifex et ouvre une demande d'extraction sur le code source.

Le service passe en revue tous les projets et toutes les langues prises en charge et effectue les opérations suivantes :

1. Extraction des fichiers de localisation de transifex (**lorsqu'au moins 20% de la ressource est traduite**)
2. Lancement d'une demande d'extraction au niveau du code source si des modifications sont détectées pour la langue.

Les demandes d'extraction sont examinées et intégrées dans la base du code dans le cadre du processus de développement normal.

> **Information**
>
> Les traductions ajoutées dans transifex seront intégrées dans la prochaine version stable disponible et dans toutes les versions de DHIS2 prises en charge.>
> _Pour vous assurer de l'intégration de vos traductions dans la prochaine version stable, contactez-nous (translate@dhis2.org) et expliquez vos besoins. Nous vous dirons ce que nous pouvons faire._

> **Astuce**
>
> Les traductions que vous ajoutez dans transifex devraient être visibles dans toutes les versions de démonstration de développement sur notre serveur Play (https://play.dhis2.org) le plus souvent pour un délai de quelques jours.

### Comment ajouter une nouvelle langue ?{ #how-do-i-add-a-new-language }

Veuillez nous contacter par courriel translate@dhis2.org, ou sur la [Communauté de pratique] (https://community.dhis2.org/c/translation) et nous ajouterons cette langue aux projets sur transifex.

Une fois que les ressources de cette langue auront été traduites à plus de 20 %, elles commenceront à être intégrées dans le système. Elles seront alors visibles dans les versions de démonstration de développement et disponibles dans les versions ultérieures.

> **Remarque**
>
> DHIS2 gère l'emplacement des métadonnées (base de données) sans recourir à l'interface utilisateur (IU). _Voir la section suivante._


## Traduction des métadonnées / de la base de données { #metadata-database-translations }

En plus de la traduction de l'interface utilisateur, DHIS 2 prend également en charge la localisation du contenu des métadonnées dans la base de données. Il est possible de traduire des objets individuels via l'application **Maintenance**, mais afin de mieux prendre en charge un flux de travail de traduction standard, une application spécialisée a été développée.

De nouveaux emplacements de métadonnées peuvent être ajoutés dans **Maintenance > Emplacements**.

### Application de Traduction du DHIS 2{ #translations-app }

L' **Application de Traduction** de DHIS 2 peut être utilisée pour traduire toutes les métadonnées (éléments de données, catégories, unités d'organisation, etc.) dans n'importe quelle langue disponible dans la base de données.

Pour commencer, il suffit de choisir **Application de Traduction** dans le menu supérieur.

![](resources/images/translations_app.png)

1.  Choisissez le type d'objet que vous voulez traduire dans le menu déroulant **Objet**,
    par exemple "Éléments de données".

2.  Assurez-vous que vous avez défini la bonne langue comme **Langue cible**.

3.  Choisissez le type d'objet que vous voulez traduire, et traduisez toutes les propriétés
    (Nom, Nom abrégé, Description, etc).
    Ces propriétés varient d’un objet à l’autre.

4.  Cliquez sur "Enregistrer" lorsque vous avez terminé la traduction de l'objet
    pour enregistrer vos modifications.


> **Remarque**
>
>Vous pouvez rechercher un terme spécifique à l'aide de la fonction de recherche située dans le coin supérieur droit de l'application.

