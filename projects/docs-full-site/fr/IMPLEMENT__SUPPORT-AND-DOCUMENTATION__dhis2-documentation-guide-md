---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/support_documentation/dhis2-documentation-guide.md"
revision_date: '2023-05-31'
tags:
- Implémentation
---

# Guide sur la documentation du DHIS 2 { #doc_guide_chapter } 

## Présentation du système de documentation du DHIS 2 { #docs_1 } 

Le DHIS 2 est un système de gestion de l'information basé sur le web, qui fait l'objet d'un 
développement très actif, avec généralement deux versions majeures par an. Chaque 
version comprend généralement quelques nouveautés et des fonctionnalités 
supplémentaires. Compte tenu de la rapidité du développement, du grand nombre 
d'utilisateurs et de la distribution du système à l'échelle mondiale, un système de 
documentation détaillé  est requis.

Dans ce chapitre, nous allons décrire le système de documentation du DHIS 2 et comment vous 
pouvez y contribuer.

## Introduction { #docs_2 } 

La documentation du DHIS 2 est rédigée au format Markdown [Commonmark] (https://commonmark.org). 
L'un des principaux avantages du format Markdown est 
que le contenu et la présentation sont totalement séparés. 
Commonmark est une spécification fortement définie et hautement compatible du 
format Markdown. 
Étant donné que le format Markdown peut être transformé en une grande variété de formats (HTML, 
PDF, etc.) et qu'il est basé sur du texte, il est idéal pour 
la documentation du système.

Il existe une large gamme d'éditeurs de texte qui peuvent être utilisés pour la 
création de fichiers Markdown. Pour Linux et Windows, 
[ghostwriter](https://wereturtle.github.io/ghostwriter/) est une bonne option ; 
il est gratuit et prend en charge l'aperçu par page double et les feuilles de style personnalisées.

L'un des concepts clés à prendre en compte lors de la conception d'une documentation au 
format Markdown ou dans d'autres formats de présentation neutre est que le **contenu** 
du document doit être traité en premier lieu. La **présentation** du 
document se fera dans une étape de transformation distincte, au cours de laquelle le 
texte source sera rendu dans différents formats, tels que HTML et 
PDF. Le document doit donc être bien organisé et 
structuré, en tenant compte des balises et des éléments de structure appropriés.

Il est conseillé de subdiviser le document en plusieurs sections à l'aide 
des en-têtes de section. De cette façon, les chapitres très complexes pourront être subdivisés en éléments plus petits et plus faciles à gérer. 
Ce concept est pratiquement identique à celui de Microsoft Word ou 
d'autres programmes de traitement de texte. Le processus se chargera automatiquement de la numérotation 
des sections lors de la conception du document.


## Premiers pas avec GitHub { #docs_3 } 

Le système de documentation du DHIS 2 est géré sur 
[GitHub] (https://github.com/dhis2) à travers une variété de 
dépôts de code source. GitHub est une plateforme qui permet 
à plusieurs personnes de collaborer sur des projets de logiciels. Pour ce faire, 
un système de contrôle de version est nécessaire 
pour gérer toutes les modifications que les utilisateurs peuvent apporter. GitHub utilise le 
système de contrôle de source *git*. Bien que ce document ne décrive pas les 
fonctionnalités de *git*, les utilisateurs qui souhaitent 
produire de la documentation devront au minimum comprendre 
les principes de base du fonctionnement du système. Une orientation de base est fournie à cet effet dans la section suivante. Le 
lecteur est invité à consulter le [git manual] (https://git-scm.com/book/en/v2) 
pour plus d'informations.

Pour pouvoir commencer à faire des ajouts ou à apporter des modifications à la documentation, vous devez d'abord 
procéder à une extraction du code source. Si vous n'avez pas encore de 
compte GitHub, vous devez en créer un. Vous pouvez le faire 
[ici] (https://github.com/). Une fois inscrit sur GitHub, vous devrez 
demander l'accès au groupe *dhis2-documenters* si vous souhaitez 
modifier directement le code source de la documentation. Cependant, tout le monde peut 
cloner la documentation dans son propre référentiel, lui apporter des 
modifications et demander à ce que ces modifications soient intégrées au 
code source de la documentation via une demande de fusion (pull request) au référentiel principal.

La structure du site de documentation est définie dans le référentiel de construction [dhis2-docs-builder](https://github.com/dhis2/dhis2-docs-builder). Si vous souhaitez apporter votre contribution à la structure, des modifications seront requises ; cela ne concerne généralement que l'équipe interne du DHIS2.

> **Conseil**
>
> La meilleure façon de trouver la source du document que vous souhaitez modifier est de le chercher sur le site Web docs.dhis2.org. Lorsque vous le trouvez, cliquez sur l'icône "Modifier" en haut de la page.

## Obtenir la source du document { #docs_4 } 

Pour pouvoir modifier la documentation, vous devez télécharger la source 
de la documentation sur votre ordinateur. GitHub utilise un système de contrôle 
de version appelé Git. Il existe différentes méthodes pour faire fonctionner Git 
sur votre système, en fonction du système d'exploitation que vous 
utilisez. Un bon guide détaillé sur les systèmes d'exploitation Microsoft peut être 
consulté 
[ici] (https://help.github.com/articles/getting-started-with-github-for-windows). 
Par ailleurs, si la ligne de commande vous convient, vous pouvez 
télécharger Git à partir de [cette page](http://git-scm.com/download/win). Si vous 
utilisez Linux, vous devrez installer Git sur votre système via 
votre gestionnaire de packages ou à partir du code source. Une référence très complète 
sur l'utilisation de git est disponible sous plusieurs formats différents 
[ici](http://git-scm.com/book).

Une fois que vous avez installé Git sur votre système, vous devrez télécharger 
la source du document. Suivez cette procédure :

1.  Assurez-vous que Git est installé.

2.  Dans les systèmes Windows, visitez l'URL du dépôt concerné et
    cliquez sur "Cloner dans le bureau". Si vous utilisez la ligne de commande, tapez simplement
    `git clone git@github.com:dhis2/dhis2-docs.git` (notez que dans cet exemple
    `dhis2` est le propriétaire du dépôt et `dhis2-docs` est le nom du dépôt)

3.  Le processus de téléchargement devrait commencer et tous les fichiers source de la documentation
    seront téléchargés dans le dossier que vous avez spécifié.

4.  Une fois que vous avez les sources, assurez-vous de créer votre propre branche pour
    l'éditer. Exécutez simplement `git checkout -b mybranch` où *mybranch*
    est le nom de la branche que vous souhaitez créer.

## Modifier la documentation { #docs_5 } 

Lorsque vous rédigez ou modifiez la documentation, il existe quelques **conventions clés spécifiques au projet dont vous devez tenir compte**. Elles sont décrites dans cette section. 
De plus, plusieurs extensions Markdown sont implémentées et présentées pour des raisons pratiques dans la section [Markdown support and extensions] (Prise en charge du Markdown et extensions) (#markdown_support_and_extensions) plus loin dans ce document.


### Utiliser les images { #using-images } 

Les ressources images doivent être placées dans un sous-dossier en lien avec document en cours d'édition. Par exemple, pour le chapitre `content/android/android-event-capture-app.md`, les images se trouvent dans le dossier `content/android/resources/images/<rest-of-path>` et sont référencées de la manière suivante ` ![](resources/images/<rest-of-path>)`

#### modeler les images { #styling-images } 

Si vous souhaitez contrôler l'alignement et la taille des images, vous pouvez profiter d'une extension Markdown que nous utilisons. Il vous permet de définir des attributs tels que la largeur, la hauteur et la classe entre accolades à la fin de la définition de l'image. Par exemple:
```
![](resources/images/maintainence/predictor_sequential.png){ largeur=50% }
```
fera de votre image 50 % de la largeur de la page (il est préférable d'utiliser des pourcentages pour prendre en charge une variété de formulaires de sortie), tandis que
```
![](resources/images/maintainence/predictor_sequential.png){ .largeur du centre=50% }
```
va également centrer l'image sur la page (en raison de la définition de la classe `.center` en css).

Lorsque les images sont écrites comme
```
![Approuver et accepter](resources/images/data_approval/approval_level_steps.png)
```
C'est-à-dire qu'avec la mention entre crochets, ils sont rendus sous forme de figures avec des mentions. Ceux-ci sont centrés par défaut, avec une mention centrée en italique.

#### Faire des captures d'écran { #taking-screenshots } 

Pour les captures d'écran de l'interface Web de DHIS 2, nous vous recommandons d'utiliser le navigateur Chrome, avec les deux extensions suivantes :
1. [Window Resizer](https://chrome.google.com/webstore/detail/window-resizer/kkelicaakdanhinjdeammmilcgefonfh?hl=en). Utilisez ceci pour régler la résolution sur **1440x900**
2. [Fireshot](https://chrome.google.com/webstore/detail/take-webpage-screenshots/mcbpblocgmgfnpjjppndjkmgjaogfceg?hl=en). Utilisez ceci pour créer rapidement un instantané de la **partie visible**

> *Fireshot peut même capturer toute la page, c'est-à-dire en la faisant défiler, si vous le souhaitez. Il peut également capturer uniquement une zone sélectionnée (mais la largeur maximale doit toujours être de 1440px)*

Lorsque vous faites des captures d'écran avec l'application Android, la taille doit être définie sur **360x640**.

#### Localiser les images { #localising-images } 

La localisation des images est possible si les versions d'une image spécifiques à une langue sont stockées à côté de l'image d'origine. Le nom du fichier doit être le même que celui de la version originale en anglais, mais doit inclure `_` plus le code de la langue à la fin du nom, avant l'extension.

Par exemple, si vous voulez avoir une version française de
`ressources/images/my_screenshot.png`
Vous pouvez simplement créer la version française et l'enregistrer sous
`ressources/images/my_screenshot_fr.png`

Le lien dans la documentation doit toujours renvoyer à l'image originale. Lorsque le site de la documentation prend en charge chacune des langues, les images localisées seront identifiées et utilisées à la place des images originales en anglais.

> *Le code de langue est la première partie de l'URL que vous voyez après "docs.dhis2.org/" lorsque vous consultez la version localisée de la documentation. Au moment de la rédaction, par exemple, nous avons `fr`, `es_419`, `pt`, `cs` et `zh`.*


### Références de section { #name_of_section } 

Afin de fournir des références fixes (ancres) dans la documentation, nous pouvons définir une chaîne de texte fixe qui sera appliquée à toutes les sections. Avec notre processeur Markdown, cela se fait par ajout d'un identifiant de hachage entre les crochets, à la fin de la ligne comportant le titre de la section, par exemple
```
## Validation { #webapi_validation }

Pour générer un résumé de validation des données, vous pouvez faire interagir ...
```

Définit l'identifiant de section de l'en-tête de niveau 2 **Validation** sur "webapi_validation", qui peut alors être référencé comme "#webapi_validation" à partir de *tout* fichier html.

> **Remarque**
>
> Afin de permettre la création de liens par référence d'ancre à partir d'autres documents, essayez de garder les identifiants de section uniques. Par exemple, si "#webapi_validation" est unique dans toute la documentation, vous pouvez y faire référence à partir de n'importe quelle autre partie de la documentation en utilisant simplement `[nom du lien](`<!--prevent-replacement-->`#webapi_validation)`. 
> Si l'identifiant de la section référencée n'est pas unique, le processeur document tentera de résoudre l'ancre la plus proche avec ce nom. *Lorsque le fichier de liaison appartient à une version spécifique, le processeur ignorera les ancres appartenant à des versions différentes*.

> **Attention**
>
> Notre documentation est compilée à la fois en pages et en documents complets. Pour cette raison, il n'est pas conseillé d'inclure des chemins d'accès dans les références inter-documents. Veuillez utiliser des identifiants de section uniques, comme décrit ci-dessus, afin que les liens soient correctement définis dans les deux types de documents.

Veuillez suivre la convention des lettres minuscules et des traits de soulignement, afin de créer des identifiants qui servent également de noms de fichiers lorsque nous procédons à un fractionnement des fichiers comme partie intégrante du processus de génération du document.


### Tableaux  { #tables } 

En tant qu'extension du Commonmark pur, sont également pris en charge les *tableaux GFM* (définis avec des canaux de communication`|`), tels que:

```
| Type de tableau | Descriptif |
|:--|:----|
|Commonmark (HTML)| Tableaux décrits en HTML pur |
|Github Flavour Markdown (GFM) | Tableaux décrits avec des canaux de communication : plus faciles à lire/éditer, mais limités en complexité |
```

qui produit une sortie comme:

| Type de tableau | Description |
|:--|:----|
|Commonmark (HTML)| Tableaux décrits en HTML pur |
|Github Flavour Markdown (GFM)| Tableaux décrits avec des canaux de communication : plus faciles à lire/éditer, mais limités en complexité|

Les tableaux simples sont bien plus faciles à utiliser. 
Ils se limitent à une seule ligne de texte (c'est-à-dire que chaque rangée doit occuper une seule ligne), mais vous pouvez, par exemple, utiliser les tags `<br>` pour créer des sauts de ligne et si nécessaire, scinder les paragraphes à l'intérieur des cellules. 
Vous pouvez également continuer à utiliser les tableaux HTML lorsque vous avez vraiment besoin d'une plus grande complexité (mais vous pouvez également vous demander s'il existe une meilleure façon de présenter les données).

## Bibliographie du DHIS 2 { #dhis-2-bibliography } 

Pour l'instant, les références bibliographiques ne sont pas prises en charge dans la version Markdown de la documentation DHIS 2.


## Gestion d'une documentation multilingue  { #docs_8 } 

La documentation DHIS 2 a été traduite dans plusieurs langues différentes, 
notamment le français, l'espagnol et le portugais. Si vous souhaitez  
traduire la documentation ou contribuer à l'une des 
traductions existantes, veuillez contacter l'équipe chargée de la documentation du DHIS 2 
via l'e-mail fourni à la fin de ce chapitre.


## Validation de vos modifications sur GitHub { #docs_10 } 

Après avoir édité votre document, vous devez valider 
vos modifications sur GitHub. Ouvrez une invite de commande sur Windows ou un 
shell sur Linux, et accédez au dossier dans lequel vous avez placé votre 
documentation. Si vous avez ajouté de nouveaux fichiers ou dossiers à votre répertoire local, 
vous devrez les ajouter à l'arborescence source avec la commande `git 
add `, suivie du/des nom(s) du/des dossier(s) ou du/des fichier(s) que vous avez ajouté. 
Assurez-vous d'inclure un commentaire descriptif lors de votre validation.

`
git commit 
-m 
"Documentation améliorée sur les importations d'unités d'organisation avec CSV."
`

Enfin, vous devez pousser les modifications vers votre référentiel avec la commande `git 
push origin mybranch`, où "mybranch" est le nom de la branche que vous 
avez créée lorsque vous avez extrait le document source ou sur laquelle 
vous êtes en train de travailler. Pour ce faire, vous aurez besoin des 
autorisations requises pour confirmer vos modifications dans le référentiel. Une fois 
les modifications confirmées, [vous pouvez faire 
une demande de fusion] (https://github.com/dhis2/dhis2-docs/pulls) pour qu'elles soient fusionnées 
avec la branche principale (master branch). Vos modifications seront examinées par l'équipe chargée de la documentation principale 
et testées pour s'assurer de leur pertinence, ainsi 
que de leur qualité. Comme mentionné précédemment, vous pouvez également ajouter 
vos modifications à votre propre référentiel GitHub, si vous n'avez pas accès au 
référentiel principal, et faire une demande d'intégration pour que vos modifications soient intégrées à la branche principale.

Si vous avez des questions ou si vous avez du mal à vous en sortir, posez simplement 
une question sur notre [communauté de pratique de développement](https://community.dhis2.org/c/development).


## Prise en charge du Markdown et extensions { #markdown_support_and_extensions }

Cette section tente de capturer le Markdown et les extensions qui sont prises en charge dans le cadre de la documentation du DHIS 2, et de fournir un aperçu des styles appliqués.


### Titre h3  { #h3-heading } 
#### Titre h4 { #h4-heading } 
##### Titre h5 { #h5-heading } 
###### Titre h6 { #h6-heading } 

Corps du texte.

### Règles horizontales { #horizontal-rules } 

```
___

---

***
```

___

---

***



### Importance{ #emphasis } 

**Ce texte est en gras**

__Ce texte est en gras__

*Ce texte est en italique*

_Ce texte est en italique_

~~Barré~~


### Blocs de citations  { #blockquotes } 

=== "Exemples"

    > Les blocs de citations peuvent également être insérés...
    >> ...en utilisant d'autres signes supérieurs côte à côte...
    > > > ... ou avec des espaces entre les flèches.

=== "Markdown"

    ```
    > Les blocs de citations peuvent également être insérés...
    >> ...en utilisant d'autres signes supérieurs côte à côte...
    > > > ... ou avec des espaces entre les flèches.
    ```

### Code { #code } 

`code` incorporé

Code incorporé mis en évidence`#!js var test = 0;` fait dans

```
`#!js var test = 0;`
```

Code indenté

    // Certains commentaires
    ligne 1 du code
    ligne 2 du code
    ligne 3 du code


Code de bloc "clôtures"

```
Texte d'exemple ici...
```

Mise en évidence de la syntaxe

```js
var foo = fonction (barre) {
  barre de retour++;
};

console.log(foo(5));
```

Longues lignes

```
Buffle buffle (les animaux appelés "buffle" de la ville de Buffle) [qui] Buffle buffle buffle (que les animaux de la ville intimident) buffle Buffalo buffle (intimident ces animaux dans cette ville).
```

Mise en surbrillance de lignes spécifiques

=== "Rendu"

    ``` py hl_lines="2 3"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

=== "Markdown"

    ````
    ``` py hl_lines="2 3"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    ````

Ajouter un titre

=== "Rendu"

    ``` py hl_lines="2 3" title="bubble_sort.py"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

=== "Markdown"

    ````
    ``` py hl_lines="2 3" title="bubble_sort.py"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    ````




### Listes { #lists } 

Non ordonné

+ Créez une liste en commençant une ligne par `+`, `-` ou `*`
+ Les sous-listes sont générées en indentant 2 espaces :
    - Le changement de caractère marqueur force le début d'une nouvelle liste :
        * Ac tristique libero volutpat at
        + Facilisis in pretium nisl aliquet

            ```
            an indented code block
            ```

        - Nulla volutpat aliquam velit
+ Très facile!

Ordonné

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. Vous pouvez utiliser des numéros séquentiels...
1. ... ou conservez tous les numéros comme au `1`.

Commencer la numérotation avec un décalage ? :

57. foo
1. bar

Multi-niveaux

1. premier élément
2. encore premier niveau
    1. deuxième niveau
    2. encore deuxième
        1. troisième niveau
        ```
        a block of code at the third level
        ```
        2. encore troisième niveau
    3. à nouveau deuxième niveau
3. retour au premier niveau
    1. deuxième
        1. Oh, arrêtez !

### Tableaux  { #tables } 

| Paramètre de retour | Description |
| :--------------- | :---------- |
| aoc | Identifiant de combinaison d'options d'attributs |
| pe | Identifiant de période |
| ou | Identifiant d'unité d'organisation |
| autorisations | Les autorisations : 'mayApprove' (peut approuver), 'mayUnapprove'(peut désapprouver), 'mayAccept' (peut accepter), 'mayUnaccept' (peut ne pas accepter) et 'mayReadData' (peut lire les données) (mêmes définitions que pour obtenir le statut d'approbation unique.) |
| État | Un des états d'approbation des données (comme pour obtenir un statut d'approbation unique.) |
| wf | Identifiant du workflow d'approbation des données |


Colonnes alignées à droite et centrées

| Paramètre de retour | Description |
| ---------------: | :----------: |
| aoc | Identifiant de combinaison d'options d'attributs |
| pe | Identifiant de période |
| ou | Identifiant d'unité d'organisation |
| autorisations | Les autorisations : 'mayApprove' (peut approuver), 'mayUnapprove'(peut désapprouver), 'mayAccept' (peut accepter), 'mayUnaccept' (peut ne pas accepter) et 'mayReadData' (peut lire les données) (mêmes définitions que pour obtenir le statut d'approbation unique.) |
| État | Un des états d'approbation des données (comme pour obtenir un statut d'approbation unique.) |
| wf | Identifiant du workflow d'approbation des données |


### Liens { #links } 

[link text](http://docs.dhis2.org)

[lien avec le titre](http://docs.dhis2./org "texte du titre !")

Lien converti automatiquement https://github.com/dhis2


### Images { #images } 

Les images sont affichées en taille réelle avec une largeur maximale de 100 %

```
![](resources/images/dhis2_screenshots.jpg)
```

![](resources/images/dhis2_screenshots.jpg)


L'ajout d'un titre rend automatiquement le résultat sous forme de figure. 
Les classes et les styles incorporés peuvent être ajoutés entre accolades.

```
![Le titre](resources/images/dhis2_screenshots.jpg){ .largeur du centre=50% }

```

![Le titre](resources/images/dhis2_screenshots.jpg){ .largeur du centre=50% }


### Youtube { #youtube } 

Les vidéos Youtube peuvent être intégrées de la même manière que les images. Mettez simplement le lien d'intégration de la vidéo Youtube au lieu d'un fichier image

``` markdown
![](https://www.youtube.com/embed/UqXSMaXBtD8)
```

![](https://www.youtube.com/embed/UqXSMaXBtD8)

> **Remarque**
> 
>Assurez-vous d'utiliser le lien d'"intégration" youtube!

Comme avec les images, l'ajout d'un titre rendra la vidéo sous forme de figure

```
![DHIS2 : Informations pour l'action](https://www.youtube.com/embed/UqXSMaXBtD8)
```

![DHIS2 : Informations pour l'action](https://www.youtube.com/embed/UqXSMaXBtD8)


### Avertissements{ #admonitions } 

Les avertissements suivants sont pris en charge, avec des styles prédéfinis, en plus des blocs de citations généraux.

#### Remarque { #note } 

=== "Remarque"

    > **Remarque**
    >
    > Une note contient des informations supplémentaires qui doivent être prises en compte ou
    > une référence vers plus d'informations potentiellement utiles.

=== "Markdown"

    ```
    > **Note**
    >
    > A note contains additional information which should be considered or a
    > reference to more information which may be helpful.
    ```

#### Conseil { #tip } 

=== "Astuce"

    > **Astuce**
    >
    > Une astuce peut être utile, par exemple comment effectuer une
    > tâche particulière plus efficacement.

=== "Markdown"

    ```
    > **Tip**
    >
    > A tip can be a useful piece of advice, such as how to perform a
    > particular task more efficiently.
    ```

#### Important { #important } 

=== "Important"

    > **Important**
    >
    > Les informations importantes ne doivent pas être ignorées. Elles indiquent généralement
    > des éléments nécessaires à l'application.

=== "Markdown"

    ```
    > **Important**
    >
    > Important information should not be ignored, and usually indicates
    > something which is required by the application.
    ```

#### Attention { #caution } 

=== "Attention"

    > **Attention**
    >
    > Les informations contenues dans ces sections doivent être
    > pris en compte. Dans le cas contraire, des résultats inattendus peuvent survenir dans
    > l'analyse, la performance ou les fonctionnalités.

=== "Markdown"

    ```
    > **Caution**
    >
    > Information contained in these sections should be carefully
    > considered, and if not heeded, could result in unexpected results in
    > analysis, performance, or functionality.
    ```

#### Avertissement { #warning } 

=== "Avertissement"

    > **Attention**
    >
    > Si les informations contenues dans ces sections ne sont pas prises en compte, cela pourrait entraîner
    > une perte permanente des données ou rendre moins facile l'utilisation du système en général.

=== "Markdown"

    ```
    > **Warning**
    >
    > Information contained in these sections, if not heeded, could result
    > in permanent data loss or affect the overall usability of the system.
    ```

#### Travail en cours  { #work-in-progress } 

=== "Travail en cours"

    > **Travail en cours**
    >
    > Les informations contenues dans ces sections indiqueront les problèmes ou erreurs sur lesquels nous travaillons actuellement.

=== "Markdown"

    ```
    > **Work In Progress**
    >
    > Information contained in these sections, will indicate that these are issues or errors we are currently working on.
    ```

#### Exemple { #example } 

=== "Exemple"

    > **Exemple**
    >
    > Une façon de porter une attention particulière aux exemples.
    >
    > Les avertissements peuvent inclure des blocs de code
    >
    > ```js
    > var foo = fonction (barre) {
    > barre de retour++ ;
    > } ;
    >
    > console.log(foo(5));
    > ```

=== "Markdown"

    ```
    > **Example**
    >
    > A way to bring special attention to examples.
    >
    > Admonitions can include a code blocks
    >
    > ```js
    > var foo = function (bar) {
    >   return bar++;
    > };
    >
    > console.log(foo(5));
    > ```
    ```


### Équations mathématiques { #mathematical-equations } 

[MathJax](https://www.mathjax.org/) permet d'afficher du contenu mathématique dans le navigateur en prenant en charge la composition mathématique sous diverses formes (par exemple [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Mathematics), [MathML](https://en.wikipedia.org/wiki/MathML), [AsciiMath](http://asciimath.org/)).

Les blocs doivent être entourés de `\[ ... \]` ou `$$ ... $$` ou `\commencer{} ... \se terminer{}` sur des lignes séparées.
Les blocs incorporés doivent être entourés de `$...$` ou `\(...\)`.

=== "Équations"

    \[
    Indicateur = {\frac{BcgVaccinationsMoinsD'unAn}{PopulationCibleMoinsD'unAn}} \times 100
    \]

    \[3 < 4\]

    \begin{align}
        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

    L'équation d'onde pour \( u \) est

    \begin{équation}
      \frac{\partial^2u}{\partial t^2} = c^2\nabla^2u
    \end{équation}

    où \( \nabla^2 \) est le laplacien spatial et \( c \) est constant.

    Cette équation $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$ est inline.

    L'homomorphisme $f$ est injectif si et seulement si son noyau n'est que l'
    ensemble singleton $e_G$, car sinon $\existe a,b\in G$ avec $a\neq b$ tel que $f(a)=f(b)$.

=== "Markdown"

    ```
    \[
    Indicator = {\frac{BcgVaccinationsUnder1Year}{TargetPopulationUnder1Year}} \times 100
    \]

    \[3 < 4\]

    \begin{align}
        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

    The wave equation for \( u \) is

    \begin{equation}
      \frac{\partial^2u}{\partial t^2} = c^2\nabla^2u
    \end{equation}

    where \( \nabla^2 \) is the spatial Laplacian and \( c \) is constant.

    This equation $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$ is inline.

    The homomorphism $f$ is injective if and only if its kernel is only the 
    singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such that $f(a)=f(b)$.
    ```



### Remplacements typographiques { #typographic-replacements } 

| Markdown       | Résultat
| -------------- |--------
| `(tm)`         | (tm)
| `(c)`          | (c)
| `(r)`          | (r)
| `c/o`          | c/o
| `+/-`          | +/-
| `-->`          | -->
| `<--`          | <--
| `<-->`         | <-->
| `=/=`          | =/=
| `1/4, etc.`    | 1/4, etc.
| `1er 2ème etc.` |1er 2ème etc


### Indice inférieur / Indice supérieur { #subscript-superscript } 


    - 19^th^
    - H~2~O

- 19^th^
- H~2~O


++Texte inséré++

==Texte marqué==


### [Notes de bas de page](https://github.com/markdown-it/markdown-it-footnote) { #footnoteshttpsgithubcommarkdown-itmarkdown-it-footnote } 

Lien de la note de bas de page 1[^premier].

Lien de la note de bas de page 2[^deuxième].

Définition de la note de bas de page inline ^ [Texte de la note de bas de page inline].

Référence de note de bas de page dupliquée[^deuxième].

[^first]: La note de bas de page **peut avoir un balisage**

    et plusieurs paragraphes.

[^second]: Texte de la note de bas de page.


### Listes des définitions  { #definition-lists } 

Terme 1 
: Définition 1 avec une continuation paresseuse.

Terme 2 avec *balisage inline* 
: Définition 2

        { quelques codes font partie de la définition 2 }

    Troisième paragraphe de la définition 2.

### Keys  { #keys } 

Keys une extension qui facilite la saisie et le design des touches du clavier. D'un point de vue syntaxique, les touches sont constituées autour du symbole 
`+`. Une touche ou une combinaison de touches est entourée de `++`, chaque touche étant séparée des autres par un `+`.

> **Exemple**
>
> === "Sortie" 
> ++ctrl+alt+suppr++.
>
> === "Markdown" 
>   ``` 
> ++ctrl+alt+suppr++ 
>   ```

Le rendu de clé suivant est pris en charge.

=== "Modificateur"

    Nom            | Affichage           | Pseudonymes
    --------------- | ----------------- | -------
    `alt`           | ++alt++           |
    `left-alt`      | ++left-alt++      | `lalt`
    `right-alt`     | ++right-alt++     | `ralt`
    `alt-graph`     | ++alt-graph++     | `altgr`
    `command`       | ++command++       | `cmd`
    `left-command`  | ++left-command++  | `lcommand`, `lcmd`, `left-cmd`
    `right-command` | ++right-command++ | `rcommand`, `rcmd`, `right-cmd`
    `control`       | ++control++       | `ctrl`
    `left-control`  | ++left-control++  | `lcontrol`, `lctrl`, `left-ctrl`
    `right-control` | ++right-control++ | `rcontrol`, `rctrl`, `right-ctrl`
    `function`      | ++function++      | `fn`
    `meta`          | ++meta++          |
    `left-meta`     | ++left-meta++     | `lmeta`
    `right-meta`    | ++right-meta++    | `rmeta`
    `option`        | ++option++        | `opt`
    `left-option`   | ++left-option++   | `loption`, `lopt`, `left-opt`
    `right-option`  | ++right-option++  | `roption`, `ropt`, `right-opt`
    `shift`         | ++shift++         |
    `left-shift`    | ++left-shift++    | `lshift`
    `right-shift`   | ++right-shift++   | `rshift`
    `super`         | ++super++         |
    `left-super`    | ++left-super++    | `lsuper`
    `right-super`   | ++right-super++   | `rsuper`
    `windows`       | ++windows++       | `win`
    `left-windows`  | ++left-windows++  | `lwindows`, `left-win`, `lwin`
    `right-windows` | ++right-windows++ | `rwindows`, `right-win`, `rwin`

=== "Fonction"

    Nom | Affichage | Pseudonymes
    ----- | ------- | -------
    `f1` | ++f1++ |
    `f2` | ++f2++ |
    `f3` | ++f3++ |
    `f4` | ++f4++ |
    `f5` | ++f5++ |
    `f6` | ++f6++ |
    `f7` | ++f7++ |
    `f8` | ++f8++ |
    `f9` | ++f9++ |
    `f10` | ++f10++ |
    `f11` | ++f11++ |
    `f12` | ++f12++ |
    `f13` | ++f13++ |
    `f14` | ++f14++ |
    `f15` | ++f15++ |
    `f16` | ++f16++ |
    `f17` | ++f17++ |
    `f18` | ++f18++ |
    `f19` | ++f19++ |
    `f20` | ++f20++ |
    `f21` | ++f21++ |
    `f22` | ++f22++ |
    `f23` | ++f23++ |
    `f24` | ++f24++ |

=== "Alphanumérique"

    Nom    | Affichage | Pseudonymes
    ------- | --------- | -------
    `0`     | ++0++     |
    `1`     | ++1++     |
    `2`     | ++2++     |
    `3`     | ++3++     |
    `4`     | ++4++     |
    `5`     | ++5++     |
    `6`     | ++6++     |
    `7`     | ++7++     |
    `8`     | ++8++     |
    `9`     | ++9++     |
    `a`     | ++a++     |
    `b`     | ++b++     |
    `c`     | ++c++     |
    `d`     | ++d++     |
    `e`     | ++e++     |
    `f`     | ++f++     |
    `g`     | ++g++     |
    `h`     | ++h++     |
    `i`     | ++i++     |
    `j`     | ++j++     |
    `k`     | ++k++     |
    `l`     | ++l++     |
    `m`     | ++m++     |
    `n`     | ++n++     |
    `o`     | ++o++     |
    `p`     | ++p++     |
    `q`     | ++q++     |
    `r`     | ++r++     |
    `s`     | ++s++     |
    `t`     | ++t++     |
    `u`     | ++u++     |
    `v`     | ++v++     |
    `w`     | ++w++     |
    `x`     | ++x++     |
    `y`     | ++y++     |
    `z`     | ++z++     |
    `espace` | ++espace++ | `spc`

=== "Ponctuation"

    Nom | Affichage | Pseudonymes
--------------- | ----------------- | -------
`barre oblique inverse` | ++barre oblique inverse++ |
`bar` | ++bar++ | `barre verticale`
`accolade gauche` | ++accolade-gauche++ | `accolade ouverte`
`accolade droite` | ++accolade droite++ | `fermer la parenthèse`
`parenthèse-gauche` | ++parenthèse-gauche++ | `parenthèse ouverte`
`parenthèse droite` | ++parenthèse-droite++ | `fermer la parenthèse`
`deux points` | ++deux-points++ |
`virgule` | ++virgule++ |
`guillemets doubles` | ++guillemet double++ | `dblquote`
`égal` | ++égal++ |
`exclamation` | ++exclamation++ | `exclamation`
`grave` | ++grave++ | `accent grave`
`plus grand` | ++plus grand++ | `supérieur à`, `gt`
`moins` | ++moins++ | `inférieur à`, `lt`
`moins` | ++moins++ | `trait d'union`
`période` | ++période++ |
`plus` | ++plus++ |
`question` | ++question++ | `point d'interrogation`
`point-virgule` | ++point-virgule++ |
`guillemet simple` | ++apostrophe++ |
`barre oblique` | ++barre oblique++ |
`tilde` | ++tilde++ |
`tiret bas` | ++tiret bas++ |

=== "Navigation"

    Name | Affichage | Pseudonymes
    -------------- | --------------- | -------
    `flèche vers le haut` | ++flèche vers le haut++ | `vers le haut`
    `flèche vers le bas` | ++flèche vers le bas++ | `vers le bas`
    `flèche-gauche` | ++flèche-gauche++ | `gauche`
    `flèche-droite` | ++flèche-droite++ | `droit`
    `page précédente` | ++page précédente++ | `prior`, `page précédente`, `pg-up`
    `page suivante` | ++page suivante++ | `suivant`, `page-dn`, `pg-dn`
    `accueil` | ++accueil++ |
    `fin` | ++fin++ |
    `onglet` | ++onglet++ | `tabulateur`

=== "Édition"

    Nom | Affichage | Pseudonymes
    ----------- | -------------- | -------
    `retour arrière` | ++retour arrière++ | `retour`, `bksp`
    `supprimer` | ++supprimer++ | `sup`
    `insérer` | ++insérer++ | `ins`

=== "Action"

    Nom | Affichage | Pseudonymes
    -------------- | -----------------| -------
    `pause` | ++pause++ | `annuler`
    `verrouillage des majuscules` | ++verrouillage des majuscules++ | `capitale`, `cplk`
    `clair` | ++clear++ | `clr`
    `éjecter` | ++éjecter++ |
    `entrer` | ++enter++ | `retourner`
    `échapper` | ++échapper++ | `éch`
    `aide` | ++aide++ |
    `écran d'impression` | ++écran d'impression++ | `prtsc`
    `arrêt-défilement` | ++scroll-lock++ | `faire défiler`

=== "Clavier numérique"

    Nom | Affichage | Pseudonymes
    --------------- | ----------------- | -------
    `num0` | ++num0++ |
    `num1` | ++num1++ |
    `num2` | ++num2++ |
    `num3` | ++num3++ |
    `num4` | ++num4++ |
    `num5` | ++num5++ |
    `num6` | ++num6++ |
    `num7` | ++num7++ |
    `num8` | ++num8++ |
    `num9` | ++num9++ |
    `num-astérisque` | ++num-astérisque++ | `multiplier`
    `num-clair` | ++num-clair++ |
    `num-supprimer` | ++num-supprimer++ | `num-sup`
    `num-égal` | ++num-égal++ |
    `verrouillage numérique` | ++verr-num++ | `numlk`, `numlock`
    `num-moins` | ++num-moins++ | `soustraire`
    `num-plus` | ++num-plus++ | `ajouter`
    `num-séparateur` | ++num-séparateur++ | `décimal`, `séparateur`
    `num-slash` | ++num-slash++ | `diviser`
    `num-entrer` | ++num-entrer++ |

=== "Clés supplémentaires"

    Nom | Affichage | Pseudonymes
    ------------------- | --------------------- | -------
    `backtab` | ++backtab++ | `bktab`
    `navigateur-retour` | ++navigateur-retour++ |
    `favoris du navigateur` | ++ favoris du navigateur ++ | `favoris`
    `navigateur-avant` | ++navigateur-avant++ | `avant`
    `accueil-navigateur` | ++accueil-navigateur++ |
    `rafraîchissement-navigateur` | ++ rafraîchissement-navigateur ++ | `rafraîchir`
    `recherche-navigateur` | ++recherche-navigateur++ | `rechercher`
    `navigateur-arrêt` | ++navigateur-arrêt++ |
    `copier` | ++copier++ |
    `menu contextuel` | ++menu contextuel++ | `applications`, `menu`
    `empreinte digitale` | ++empreinte digitale++ | `empreinte digitale`
    `mail` | ++mail++ | `lancer-mail`
    `média` | ++média++ | `lancer-media`
    `media-piste-suivante` | ++media-piste-suivante++ | `piste suivante`
    `média-pause` | ++media-pause++ | `mettre en pause`
    `lecture-media` | ++lecture-media++ | `lecture`
    `media-lecture-pause` | ++media-lecture-pause++ | `lecture-pause`
    `media-piste-précédente` | ++media-piste-précédente++ | `piste-précédente`
    `media-arrêt` | ++media-arrêt++ | `arrêter`
    `pouvoir` | ++pouvoir++ |
    `imprimer` | ++imprimer++ |
    `réinitialiser` | ++réinitialiser++ |
    `sélectionner` | ++sélectionner++ |
    `veille` | ++veille++ |
    `volume-bas` | ++volume-bas++ | `vol-bas`
    `volume-muet` | ++volume-muet++ | `muet`
    `augmenter-volume` | ++augmenter-volume++ | `augmenter-volume`
    `zoomer` | ++zoomer++ |

=== "Souris"

    Nom | Affichage | Pseudonymes
    --------------- | ----------------- | -------
    `bouton gauche` | ++bouton-gauche++ | `lbouton`
    `bouton du milieu` | ++bouton du milieu++ | `mbouton`
    `bouton droit` | ++bouton droit++ | `rbouton`
    `bouton-x1` | ++x-bouton1++ | `xbouton1`
    `x-bouton2` | ++x-bouton2++ | `xbouton2`


### Émojis { #emojies } 

Plusieurs ensembles d'emojis sont pris en charge en saisissant le nom de l'emoji entouré de deux-points: par exemple, `:smile:`. 
Vous trouverez ci-dessous la liste des ensembles communs ; ceux qui n'ont pas de résultats ne sont actuellement pas pris en charge.

=== "Personnes"

    :bowtie: :smile: :laughing: :blush: :smiley: :relaxed: :smirk: :heart_eyes: :kissing_heart: :kissing_closed_eyes: :flushed: :relieved: :satisfied: :grin: :wink: :stuck_out_tongue_winking_eye: :stuck_out_tongue_closed_eyes: :grinning: :kissing: :kissing_smiling_eyes: :stuck_out_tongue: :sleeping: :worried: :frowning: :anguished: :open_mouth: :grimacing: :confused: :hushed: :expressionless: :unamused: :sweat_smile: :sweat: :disappointed_relieved: :weary: :pensive: :disappointed: :confounded: :fearful: :cold_sweat: :persevere: :cry: :sob: :joy: :astonished: :scream: :neckbeard: :tired_face: :angry: :rage: :triumph: :sleepy: :yum: :mask: :sunglasses: :dizzy_face: :imp: :smiling_imp: :neutral_face: :no_mouth: :innocent: :alien: :yellow_heart: :blue_heart: :purple_heart: :heart: :green_heart: :broken_heart: :heartbeat: :heartpulse: :two_hearts: :revolving_hearts: :cupid: :sparkling_heart: :sparkles: :star: :star2: :dizzy: :boom: :collision: :anger: :exclamation: :question: :grey_exclamation: :grey_question: :zzz: :dash: :sweat_drops: :notes: :musical_note: :fire: :hankey: :poop: :shit: :+1: :thumbsup: :-1: :thumbsdown: :ok_hand: :punch: :facepunch: :fist: :v: :wave: :hand: :raised_hand: :open_hands: :point_up: :point_down: :point_left: :point_right: :raised_hands: :pray: :point_up_2: :clap: :muscle: :metal: :fu: :walking: :runner: :running: :couple: :family: :two_men_holding_hands: :two_women_holding_hands: :dancer: :dancers: :ok_woman: :no_good: :information_desk_person: :raising_hand: :bride_with_veil: :person_with_pouting_face: :person_frowning: :bow: :couplekiss: :couple_with_heart: :massage: :haircut: :nail_care: :boy: :girl: :woman: :man: :baby: :older_woman: :older_man: :person_with_blond_hair: :man_with_gua_pi_mao: :man_with_turban: :construction_worker: :cop: :angel: :princess: :smiley_cat: :smile_cat: :heart_eyes_cat: :kissing_cat: :smirk_cat: :scream_cat: :crying_cat_face: :joy_cat: :pouting_cat: :japanese_ogre: :japanese_goblin: :see_no_evil: :hear_no_evil: :speak_no_evil: :guardsman: :skull: :feet: :lips: :kiss: :droplet: :ear: :eyes: :nose: :tongue: :love_letter: :bust_in_silhouette: :busts_in_silhouette: :speech_balloon: :thought_balloon:

=== "Nature"

    :sunny: :umbrella: :cloud: :snowflake: :snowman: :zap: :cyclone: :foggy: :ocean: :cat: :dog: :mouse: :hamster: :rabbit: :wolf: :frog: :tiger: :koala: :bear: :pig: :pig_nose: :cow: :boar: :monkey_face: :monkey: :horse: :racehorse: :camel: :sheep: :elephant: :panda_face: :snake: :bird: :baby_chick: :hatched_chick: :hatching_chick: :chicken: :penguin: :turtle: :bug: :honeybee: :ant: :beetle: :snail: :octopus: :tropical_fish: :fish: :whale: :whale2: :dolphin: :cow2: :ram: :rat: :water_buffalo: :tiger2: :rabbit2: :dragon: :goat: :rooster: :dog2: :pig2: :mouse2: :ox: :dragon_face: :blowfish: :crocodile: :dromedary_camel: :leopard: :cat2: :poodle: :paw_prints: :bouquet: :cherry_blossom: :tulip: :four_leaf_clover: :rose: :sunflower: :hibiscus: :maple_leaf: :leaves: :fallen_leaf: :herb: :mushroom: :cactus: :palm_tree: :evergreen_tree: :deciduous_tree: :chestnut: :seedling: :blossom: :ear_of_rice: :shell: :globe_with_meridians: :sun_with_face: :full_moon_with_face: :new_moon_with_face: :new_moon: :waxing_crescent_moon: :first_quarter_moon: :waxing_gibbous_moon: :full_moon: :waning_gibbous_moon: :last_quarter_moon: :waning_crescent_moon: :last_quarter_moon_with_face: :first_quarter_moon_with_face: :moon: :earth_africa: :earth_americas: :earth_asia: :volcano: :milky_way: :partly_sunny: :octocat: :squirrel:

=== "Objets"

    :bamboo: :gift_heart: :dolls: :school_satchel: :mortar_board: :flags: :fireworks: :sparkler: :wind_chime: :rice_scene: :jack_o_lantern: :ghost: :santa: :christmas_tree: :gift: :bell: :no_bell: :tanabata_tree: :tada: :confetti_ball: :balloon: :crystal_ball: :cd: :dvd: :floppy_disk: :camera: :video_camera: :movie_camera: :computer: :tv: :iphone: :phone: :telephone: :telephone_receiver: :pager: :fax: :minidisc: :vhs: :sound: :speaker: :mute: :loudspeaker: :mega: :hourglass: :hourglass_flowing_sand: :alarm_clock: :watch: :radio: :satellite: :loop: :mag: :mag_right: :unlock: :lock: :lock_with_ink_pen: :closed_lock_with_key: :key: :bulb: :flashlight: :high_brightness: :low_brightness: :electric_plug: :battery: :calling: :email: :mailbox: :postbox: :bath: :bathtub: :shower: :toilet: :wrench: :nut_and_bolt: :hammer: :seat: :moneybag: :yen: :dollar: :pound: :euro: :credit_card: :money_with_wings: :e-mail: :inbox_tray: :outbox_tray: :envelope: :incoming_envelope: :postal_horn: :mailbox_closed: :mailbox_with_mail: :mailbox_with_no_mail: :door: :smoking: :bomb: :gun: :hocho: :pill: :syringe: :page_facing_up: :page_with_curl: :bookmark_tabs: :bar_chart: :chart_with_upwards_trend: :chart_with_downwards_trend: :scroll: :clipboard: :calendar: :date: :card_index: :file_folder: :open_file_folder: :scissors: :pushpin: :paperclip: :black_nib: :pencil2: :straight_ruler: :triangular_ruler: :closed_book: :green_book: :blue_book: :orange_book: :notebook: :notebook_with_decorative_cover: :ledger: :books: :bookmark: :name_badge: :microscope: :telescope: :newspaper: :football: :basketball: :soccer: :baseball: :tennis: :8ball: :rugby_football: :bowling: :golf: :mountain_bicyclist: :bicyclist: :horse_racing: :snowboarder: :swimmer: :surfer: :ski: :spades: :hearts: :clubs: :diamonds: :gem: :ring: :trophy: :musical_score: :musical_keyboard: :violin: :space_invader: :video_game: :black_joker: :flower_playing_cards: :game_die: :dart: :mahjong: :clapper: :memo: :pencil: :book: :art: :microphone: :headphones: :trumpet: :saxophone: :guitar: :shoe: :sandal: :high_heel: :lipstick: :boot: :shirt: :tshirt: :necktie: :womans_clothes: :dress: :running_shirt_with_sash: :jeans: :kimono: :bikini: :ribbon: :tophat: :crown: :womans_hat: :mans_shoe: :closed_umbrella: :briefcase: :handbag: :pouch: :purse: :eyeglasses: :fishing_pole_and_fish: :coffee: :tea: :sake: :baby_bottle: :beer: :beers: :cocktail: :tropical_drink: :wine_glass: :fork_and_knife: :pizza: :hamburger: :fries: :poultry_leg: :meat_on_bone: :spaghetti: :curry: :fried_shrimp: :bento: :sushi: :fish_cake: :rice_ball: :rice_cracker: :rice: :ramen: :stew: :oden: :dango: :egg: :bread: :doughnut: :custard: :icecream: :ice_cream: :shaved_ice: :birthday: :cake: :cookie: :chocolate_bar: :candy: :lollipop: :honey_pot: :apple: :green_apple: :tangerine: :lemon: :cherries: :grapes: :watermelon: :strawberry: :peach: :melon: :banana: :pear: :pineapple: :sweet_potato: :eggplant: :tomato: :corn:

=== "Lieux"

    :house: :house_with_garden: :school: :office: :post_office: :hospital: :bank: :convenience_store: :love_hotel: :hotel: :wedding: :church: :department_store: :european_post_office: :city_sunrise: :city_sunset: :japanese_castle: :european_castle: :tent: :factory: :tokyo_tower: :japan: :mount_fuji: :sunrise_over_mountains: :sunrise: :stars: :statue_of_liberty: :bridge_at_night: :carousel_horse: :rainbow: :ferris_wheel: :fountain: :roller_coaster: :ship: :speedboat: :boat: :sailboat: :rowboat: :anchor: :rocket: :airplane: :helicopter: :steam_locomotive: :tram: :mountain_railway: :bike: :aerial_tramway: :suspension_railway: :mountain_cableway: :tractor: :blue_car: :oncoming_automobile: :car: :red_car: :taxi: :oncoming_taxi: :articulated_lorry: :bus: :oncoming_bus: :rotating_light: :police_car: :oncoming_police_car: :fire_engine: :ambulance: :minibus: :truck: :train: :station: :train2: :bullettrain_front: :bullettrain_side: :light_rail: :monorail: :railway_car: :trolleybus: :ticket: :fuelpump: :vertical_traffic_light: :traffic_light: :warning: :construction: :beginner: :atm: :slot_machine: :busstop: :barber: :hotsprings: :checkered_flag: :crossed_flags: :izakaya_lantern: :moyai: :circus_tent: :performing_arts: :round_pushpin: :triangular_flag_on_post: :jp: :kr: :cn: :us: :fr: :es: :it: :ru: :gb: :uk: :de:

=== "Symboles"

    :one: :two: :three: :four: :five: :six: :seven: :eight: :nine: :keycap_ten: :1234: :zero: :hash: :symbols: :arrow_backward: :arrow_down: :arrow_forward: :arrow_left: :capital_abcd: :abcd: :abc: :arrow_lower_left: :arrow_lower_right: :arrow_right: :arrow_up: :arrow_upper_left: :arrow_upper_right: :arrow_double_down: :arrow_double_up: :arrow_down_small: :arrow_heading_down: :arrow_heading_up: :leftwards_arrow_with_hook: :arrow_right_hook: :left_right_arrow: :arrow_up_down: :arrow_up_small: :arrows_clockwise: :arrows_counterclockwise: :rewind: :fast_forward: :information_source: :ok: :twisted_rightwards_arrows: :repeat: :repeat_one: :new: :top: :up: :cool: :free: :ng: :cinema: :koko: :signal_strength: :u5272: :u5408: :u55b6: :u6307: :u6708: :u6709: :u6e80: :u7121: :u7533: :u7a7a: :u7981: :sa: :restroom: :mens: :womens: :baby_symbol: :no_smoking: :parking: :wheelchair: :metro: :baggage_claim: :accept: :wc: :potable_water: :put_litter_in_its_place: :secret: :congratulations: :m: :passport_control: :left_luggage: :customs: :ideograph_advantage: :cl: :sos: :id: :no_entry_sign: :underage: :no_mobile_phones: :do_not_litter: :non-potable_water: :no_bicycles: :no_pedestrians: :children_crossing: :no_entry: :eight_spoked_asterisk: :eight_pointed_black_star: :heart_decoration: :vs: :vibration_mode: :mobile_phone_off: :chart: :currency_exchange: :aries: :taurus: :gemini: :cancer: :leo: :virgo: :libra: :scorpius: :sagittarius: :capricorn: :aquarius: :pisces: :ophiuchus: :six_pointed_star: :negative_squared_cross_mark: :a: :b: :ab: :o2: :diamond_shape_with_a_dot_inside: :recycle: :end: :on: :soon: :clock1: :clock130: :clock10: :clock1030: :clock11: :clock1130: :clock12: :clock1230: :clock2: :clock230: :clock3: :clock330: :clock4: :clock430: :clock5: :clock530: :clock6: :clock630: :clock7: :clock730: :clock8: :clock830: :clock9: :clock930: :heavy_dollar_sign: :copyright: :registered: :tm: :x: :heavy_exclamation_mark: :bangbang: :interrobang: :o: :heavy_multiplication_x: :heavy_plus_sign: :heavy_minus_sign: :heavy_division_sign: :white_flower: :100: :heavy_check_mark: :ballot_box_with_check: :radio_button: :link: :curly_loop: :wavy_dash: :part_alternation_mark: :trident: :black_square: :white_square: :white_check_mark: :black_square_button: :white_square_button: :black_circle: :white_circle: :red_circle: :large_blue_circle: :large_blue_diamond: :large_orange_diamond: :small_blue_diamond: :small_orange_diamond: :small_red_triangle: :small_red_triangle_down: :shipit:


### Mermaid { #mermaid } 

Les diagrammes [Mermaid.js](https://mermaid-js.github.io/mermaid/) sont désormais pris en charge.


#### Organigrammes { #flowcharts } 

[Flowcharts](https://mermaid-js.github.io/mermaid/#/flowchart) sont des diagrammes qui représentent les charges de travail ou processus. Les étapes 
sont rendues sous forme de nœuds de différents types et sont reliées par des arêtes, décrivant 
l'ordre approprié des étapes:


=== "Exemple"

    ``` mermaid
    graphique LR
    A[Début] --> B{Erreur ?} ;
    B -->|Oui| C[Hum...] ;
    C --> D[Débogage] ;
    D --> B ;
    B ---->|Non| E[Yay !] ;
    ```

=== "Markdown"

    ```

        ``` mermaid
        graph LR
        A[Start] --> B{Error?};
        B -->|Yes| C[Hmm...];
        C --> D[Debug];
        D --> B;
        B ---->|No| E[Yay!];
        ```

    ```

#### Diagrammes de séquence { #sequence-diagrams } 

Les [Diagrammes de séquence](https://mermaid-js.github.io/mermaid/#/sequenceDiagram) décrivent un scénario spécifique comme les interactions séquentielles 
entre plusieurs objets ou acteurs, y compris les messages échangés 
entre ces acteurs:


=== "Exemple"

    ``` mermaid
    %%{init: {'mirrorActors': false } }%%

    sequenceDiagram

        autonumber
        participant G as package URL<br><br>(github/S3)
        participant M as metatran
        participant T as transifex
        participant F as filesystem<br><br>(path)
        G->>M: package file 
        T->>M: pull latest translation strings
        opt 
            note over M: swap base language
        end

        opt 
            note over M: include/exclude languages
        end
        M->>+F: New package file
    ```

=== "Markdown"

    ```
        ``` mermaid
        %%{init: {'mirrorActors': false } }%%

        sequenceDiagram

            autonumber
            participant G as package URL<br><br>(github/S3)
            participant M as metatran
            participant T as transifex
            participant F as filesystem<br><br>(path)
            G->>M: package file 
            T->>M: pull latest translation strings
            opt 
                note over M: swap base language
            end

            opt 
                note over M: include/exclude languages
            end
            M->>+F: New package file
        ```
    ```



#### graphiques git  { #git-graphs } 


Les [Graphiques Git](https://mermaid.js.org/syntax/gitgraph.html#gitgraph-diagrams) fournissent une représentation graphique des commits git et des actions git sur diverses branches.


=== "Exemple"

    ``` mermaid
    %%{init: { 'logLevel': 'debug', 'theme': 'dark', 'gitGraph': {
    'showBranches': true, 
    'showCommitLabel':false, 
    'mainBranchName': 'master'}} 
    }%%

    gitGraph
        commit
        commit
        branch "2.39"
        checkout "2.39"
        commit
        checkout master
        commit
        checkout "2.39"
        branch "patch/2.39.0"
        checkout "patch/2.39.0"
        commit
        checkout master
        commit
        checkout "2.39"
        commit
        checkout "patch/2.39.0"
        commit tag: "2.39.0"
        checkout master
        commit
        checkout "2.39"
        commit
        commit
        checkout "master"
        commit
        checkout "2.39"
        branch "patch/2.39.1"
        checkout "patch/2.39.1"
        commit
        commit tag: "2.39.1"
        checkout "2.39"
        commit
        checkout "patch/2.39.1"
        branch "hotfix 2.39.1.1"
        commit tag: "2.39.1.1"
    ```

=== "Markdown"

    ```
        ``` mermaid
        %%{init: { 'logLevel': 'debug', 'theme': 'dark', 'gitGraph': {
        'showBranches': true, 
        'showCommitLabel':false, 
        'mainBranchName': 'master'}} 
        }%%

        gitGraph
            commit
            commit
            branch "2.39"
            checkout "2.39"
            commit
            checkout master
            commit
            checkout "2.39"
            branch "patch/2.39.0"
            checkout "patch/2.39.0"
            commit
            checkout master
            commit
            checkout "2.39"
            commit
            checkout "patch/2.39.0"
            commit tag: "2.39.0"
            checkout master
            commit
            checkout "2.39"
            commit
            commit
            checkout "master"
            commit
            checkout "2.39"
            branch "patch/2.39.1"
            checkout "patch/2.39.1"
            commit
            commit tag: "2.39.1"
            checkout "2.39"
            commit
            checkout "patch/2.39.1"
            branch "hotfix 2.39.1.1"
            commit tag: "2.39.1.1"
        ```

    ```

