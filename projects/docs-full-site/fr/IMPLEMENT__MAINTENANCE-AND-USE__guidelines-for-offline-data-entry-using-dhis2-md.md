---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/maintenance_use/offline-data-entry.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Lignes directrices pour la saisie de données hors ligne à l'aide du DHIS 2{ #offline_data_entry } 
<!--DHIS2-SECTION-ID:offline_data_entry-->

La méthode standard de facto pour le déploiement du DHIS 2 est désormais *en ligne*, ce qui signifie
qu'une seule instance de l'application est installée sur un serveur
connecté à Internet et que tous les utilisateurs se connectent à l'application à l'aide 
d'un navigateur web sur internet. Ceci a été rendu possible grâce à
l'augmentation constante de la disponibilité de l'internet (principalement l'internet mobile),
les offres de ressources informatiques en nuage aisément disponibles et bon marché
combiné au fait que DHIS 2 ne demande pas 
un débit important. Ces développements permettent d'accéder à des serveurs en ligne
même en zone rurale, à l'aide de modems Internet mobiles (également appelés
dongles).

Ce mode de déploiement en ligne a d'énormes implications positives pour
le processus d'implémentation et la maintenance de l'application par rapport au
style traditionnel hors ligne et autonome:

**Matériel** : Les exigences en matière de matériel du côté de l'utilisateur final se limitent à un
ordinateur /ordinateur portable raisonnablement moderne et à une connectivité Internet<!-- Mentionner le téléphone, puisque android est listé comme
alternative ? --> la connectivité par le biais d'une ligne fixe ou d'un modem mobile. Il n'est pas nécessaire
d'avoir un serveur spécialisé pour chaque utilisateur, n'importe quel ordinateur connecté à Internet
sera suffisant. Un serveur sera nécessaire pour les déploiements en ligne,
mais comme il n'y a qu'un (ou plusieurs) serveur(s) à
acheter et à entretenir, cela est nettement plus simple (et moins cher)
que de maintenir de nombreux serveurs séparés dans des lieux disparates. Étant donné que le prix des ressources informatiques en nuage continue de diminuer constamment
tout en augmentant la puissance de calcul, la mise en place d'un serveur puissant dans
le nuage est bien moins coûteuse que l'achat de matériel.

**Plate-forme logicielle**: Les utilisateurs finaux n'ont besoin que d'un navigateur web pour
se connecter au serveur en ligne. Tous les systèmes d'exploitation courants sont aujourd'hui livrés avec
un navigateur web et il n'y a pas d'exigence particulière quant au type ou
à la version<!--Je ne suis pas sûr que cela soit vrai, du moins dans la pratique -->. Cela signifie qu'en cas de problèmes graves 
tels que des infections par des virus ou la corruption de logiciels, on peut toujours
recourir au reformatage et à l'installation du système d'exploitation de l'ordinateur ou
obtenir un nouvel ordinateur/ordinateur portable. L'utilisateur peut continuer à saisir les données 
là où elles ont été laissées et aucune donnée ne sera perdue.

**Application logicielle:** Le style de déploiement de serveur central signifie que 
l'application peut être mise à niveau et maintenue de manière centralisée. 
Lorsque de nouvelles versions des applications sont publiées avec de nouvelles fonctionnalités et
des corrections de bogues, elles peuvent être déployées sur le serveur unique en ligne. Toutes les modifications
seront alors répercutées du côté client lors de la prochaine connexion des utilisateurs finaux
sur Internet. Cela a évidemment un impact positif énorme sur
le processus d'amélioration du système car les nouvelles fonctionnalités peuvent être distribuées
aux utilisateurs immédiatement, tous les utilisateurs accèdent à la même version de l'application, 
et les bogues et les problèmes peuvent être triés et déployés 
à la volée.<!-- Les bogues peuvent être déployés à la volée ! -->.

**Maintenance de la base de données**: Comme pour le point précédent, les modifications des
métadonnées peuvent être effectuées sur le serveur en ligne de manière centralisée et
se propageront automatiquement à tous les clients lors de leur prochaine connexion au
serveur. Cela permet d'éviter les problèmes liés à 
la maintenance d'un ensemble de métadonnées mis à jour et normalisé, comme c'est le cas pour le
déploiement traditionnel hors ligne. C'est extrêmement pratique par
exemple pendant la phase initiale de développement de la base de données et pendant les
processus annuels de révision de la base de données, car les utilisateurs finaux auront accès à 
une base de données cohérente et normalisée même si les changements sont fréquents.

Bien qu'une implémentation du DHIS 2 peut être décrite comme un système en ligne, il convient 
de noter qu'un tel déploiement peut ne pas être purement en ligne et peut présenter certaines variations locales
en fonction des contraintes locales. Par exemple, alors que la plupart des utilisateurs dans
les pays bénéficient d'un accès facile à leur instance DHIS 2 nationale en utilisant leur 
internet mobile ou mieux<!-- Autre ? Le fixe n'est peut-être pas mieux... -->,
certains ont malheureusement encore du mal à accéder au système, que ce soit pour la saisie
ou l'analyse des données, dans les endroits où la connectivité Internet est instable ou
absente pendant de longues périodes. Pour ces utilisateurs en difficulté, 
il faut trouver d'autres moyens d'interagir avec le système.

Cette ligne directrice vise à fournir des conseils sur la manière d'atténuer l'effet du 
manque de réseau internet fiable dans les environnements difficiles.

##  Cas et solutions correspondantes { #offline_data_entry_cases } 
<!--DHIS2-SECTION-ID:offline_data_entry_cases-->

Dans cette section, nous examinerons les cas difficiles possibles et décrirons
les moyens de les résoudre ou de minimiser leurs effets sur les utilisateurs et
l'ensemble du système à court terme. Il est évident que les solutions proposées 
dans ces lignes directrices doivent être adaptées à chaque contexte tout en tenant 
compte de nombreux autres paramètres tels que la sécurité, les pratiques et
règles locales, etc. L'idée de ces lignes directrices n'est pas de prescrire des solutions
miracles qui peuvent fonctionner partout, mais de proposer des moyens de résoudre
les problèmes de connectivité dans certains endroits du pays.

Nous avons identifié trois (3) scénarios principaux :

  1. Une disponibilité internet limitée et des formulaires de saisie de données de petite taille
  1. L'accès à Internet est limité et les formulaires de saisie de données sont très volumineux
  1. Internet n'est pas du tout disponible

Nous reconnaissons que ces scénarios sont très simplistes car, dans 
la pratique, un établissement de santé peut avoir, par exemple, un petit formulaire hebdomadaire 
pour la surveillance des maladies, un grand formulaire pour le rapport d'activité mensuel et
un formulaire de taille moyenne pour un programme de santé. Le nombre de scénarios
possibles pour un environnement donné est donc plus important que ce qui est décrit 
ici.Il appartiendra donc à chaque équipe d'implémentation de discuter
avec les parties prenantes pour faire des choix simples qui répondent à tous les
scénarios dans un contexte donné. Dans la plupart des cas, environ 80 à 95% des
districts<!-- Avons-nous une source pour cela ? --> (ou des établissements de santé si la saisie des données
se fait à ce niveau) auront la même configuration en ce qui concerne
la disponibilité de l'internet et seuls les 5 à 20 % restants auront besoin
d'autres alternatives pour obtenir leurs données dans le DHIS 2.

### 1. Disponibilité limitée de l'internet (instabilité du signal ou données mobiles limitées) et petits formulaires de saisie des données.  { #offline_data_entry_cases_small } 
<!--DHIS2-SECTION-ID:offline_data_entry_cases_small-->

Par disponibilité limitée de l'internet, nous entendons le cas où :

  - le signal du réseau est disponible et bon, mais il n'y a pas suffisamment 
    de ressources nécessaires à l'achat de données mobiles pour travailler en ligne de manière continue
  - le réseau est bon mais instable ou n'est disponible qu'à une 
    période donnée de la journée
  - le signal du réseau est faible mais s'améliore de temps en temps et permet 
    de se connecter au DHIS 2

Et par petit formulaire de saisie, nous entendons un formulaire de saisie ayant moins 
cent<!-- Si j'avais deviné ce que signifiait "petit", je dirais
10-20 --> champs.

Ainsi, si la connectivité internet est limitée et que les formulaires de saisie de données sont petits,
deux possibilités s'offrent à vous pour résoudre le problème de connectivité : L'application de saisie de données Android,
et la saisie de données sur le web hors ligne.

#### Utilisation d'une application Android de saisie de données :{ #use-of-android-data-capture-app } 
<!-- Il faut s'assurer qu'elle est mise à jour au moment de la parution de la nouvelle version de 
l'application -->

L'application Saisie de données du DHIS 2 permet aux utilisateurs d'entrer des données dans un serveur DHIS 2
à l'aide d'un appareil Android. L'application télécharge les instances de formulaires
nécessaires à la saisie des données du serveur et les stocke 
sur l'appareil. Cela signifie que les utilisateurs peuvent saisir des données hors ligne pour les établissements
auxquels ils sont affectés, puis les télécharger sur le serveur DHIS 2 lorsqu'ils disposent d'une
une couverture réseau.

Pour ce faire, les utilisateurs devront se rendre sur Google Play à partir de 
leur appareil Android et de taper DHIS 2 data capture (saisie de donnée de DHIS2) et de voir apparaître 
l'écran suivant.

Installez ensuite l'application **Data Capture for DHIS 2**.(saisie de donnée de DHIS2)

![](resources/images/image5.png)

Une fois l'application installée et lancée, l'utilisateur devra
fournir l'url de son DHIS 2 national, son nom d'utilisateur et son mot de passe et
appuyez sur LOG IN.(Connexion)

<table style="border:1px;">
<tr>
<td style="width:40%;padding: 5 20 5 20;border:1px;">

![](resources/images/offline_data_entry/image4.jpg)
</td>
<td style="width:40%;padding: 5 20 5 20;border:0px;">
</td>
</tr>
</table>

Après une connexion réussie, l'application téléchargera automatiquement les 
formulaires et les unités d'organisation auxquels l'utilisateur est affecté et les stockera
localement pour la saisie des données. A partir de là, toute utilisation ultérieure de l'application pour
pour la saisie de données ne nécessitera pas de connexion internet car les instances de formulaires 
sont déjà stockées localement. La connexion internet ne sera nécessaire que pour
synchroniser les données avec le serveur. Cette opération peut être effectuée lorsque l'internet est disponible
localement.

<table style="border:0px;">
<tr>
<td style="width:40%;padding: 5 20 5 20 ;border:0px;">

![](resources/images/image9.jpg)
</td>
<td style="width:40%;padding: 5 20 5 20 ;border:0px;">

![](resources/images/image7.jpg)
</td>
</tr>
</table>

En ce qui concerne l'administration du système, l'organisation du formulaire de saisie des données en
sections dans DHIS 2 rendra la saisie des données plus fluide, et
plus agréable.

En ce qui concerne la synchronisation, lorsque la connectivité internet n'est pas disponible
l'utilisateur emporte son appareil mobile au district - pendant 
la réunion de district - ou à l'endroit le plus proche où l'internet est 
disponible.

#### Utilisation de la fonctionnalité hors ligne du module de saisie des données sur le web du DHIS 2{ #use-of-the-offline-capability-of-dhis-2-web-data-entry-module } 

Le module de saisie de données sur le web est le module de DHIS 2 qui permet la saisie de données à
l'aide du navigateur web. C'est la méthode habituelle de saisie des données
en ligne dans DHIS 2. Cependant, il dispose également d'une capacité "hors ligne" qui
permet de poursuivre la saisie des données même lorsque l'internet est
interrompu. Cela signifie que si l'utilisateur veut saisir des données 
à la fin du mois, il doit d'abord se connecter à l'internet, 
se connecter au DHIS 2 et ouvrir les formulaires de saisie pour au moins l'une des
installations auxquelles il est affecté. À partir de cette étape, il peut se déconnecter à
l'internet et poursuivre la saisie des données pour toutes ses structures et pour les
périodes qu'il souhaite, aussi longtemps que la fenêtre de la page web de saisie des données n'est pas fermée 
dans le navigateur web. Après avoir terminé la saisie des données, il peut fermer le 
navigateur et éteindre son ordinateur. Les données saisies seront stockées
localement dans le cache du navigateur et la prochaine fois que l'utilisateur se connectera 
au DHIS 2, il lui sera demandé de cliquer sur un bouton 
pour les télécharger.

Dans ce cas, il est possible d'utiliser soit l'application de saisie de données androïde, soit 
la fonction web semi-offline du DHIS 2, ou les deux, en fonction de la 
taille des formulaires de saisie.<!-- On ne sait pas très bien à quoi se réfère l'expression "pour ce cas" -->
Toutefois, la suppression du cache du navigateur entraînera la perte des données stockées
localement. Il est donc recommandé de ne pas vider la mémoire cache sans
s'assurer que les données stockées localement ont bien été synchronisées.

Lorsque l'utilisateur est connecté et que l'internet est coupé (délibérément ou non)

![](resources/images/image1.png) <!-- PALD : Cette capture d'écran a été faite lorsque l'icône d'accueil ()en haut à gauche) était cassée. Je suggère que cette image soit remplacée! -->

Lorsque l'internet est rétabli et que l'utilisateur se connecte au DHIS 2

![](resources/images/image6.png)


### 2. Accès à Internet limité et formulaires de saisie de données volumineux{ #offline_data_entry_cases_huge } 
<!--DHIS2-SECTION-ID:offline_data_entry_cases_huge-->

<!-- L'option de saisie de données au format PDF existe-t-elle encore ? Où pourrait-on générer des formulaires de saisie de données au format PDF qui pourraient être gérés hors ligne et ensuite téléchargés ?-->

Lorsque l'internet mais la disponibilité est limitée mais que le formulaire d'entrée de données
contient plusieurs centaines de champs, cela limite les solutions envisageables. Dans 
ce cas, il n'est pas conseillé d'utiliser la saisie androïde pour deux
raisons :

  - il peut régulièrement se planter car il n'est pas conçu pour traiter des formulaires de 
    très grande taille<!-- Nous pourrions peut-être ne pas insister sur ce point... -->
  - il peut s'avérer fastidieux et épuisant pour les utilisateurs car
    l'écran est petit et ne permet pas une saisie rapide des données

La seule option possible est donc d'utiliser le module de saisie de données sur le web
hors ligne décrit ci-dessus ou de se rendre à l'endroit le plus proche où 
Internet est disponible lorsque l'utilisateur ne peut pas se permettre d'attendre la prochaine fois que
l'internet sera disponible dans sa région.


### 3. Internet n'est pas du tout disponible { #offline_data_entry_cases_no_available } 
<!--DHIS2-SECTION-ID:offline_data_entry_cases_no_available-->

Dans ce cas, trois options sont possibles :

  - L'utilisation de l'application Android pour la saisie des données au niveau local et la synchronisation des 
    données au niveau supérieur où l'internet est disponible si l'utilisateur 
    assiste régulièrement à des réunions à cet endroit. Cette solution n'est envisageable que si les formulaires
    sont de petite taille
  - Déménager dans le lieu le plus proche (si cela est possible) ou profiter
    d'une réunion régulière au niveau supérieur pour saisir des données à l'aide du module de saisie de données
    en ligne. Dans ce cas, en fonction de la connectivité internet,
    l'utilisateur peut travailler en ligne ou utiliser la capacité hors ligne 
    décrite dans la section [ci-dessus] (#offline_data_entry_cases_small).
  - Demandez au niveau supérieur là où l'internet est disponible pour la saisie des données,
    quelle que soit la taille du formulaire. Bien que la saisie des données se fasse
    au niveau supérieur, les données peuvent toujours être saisies pour chaque établissement de santé.


<!-- Il semble naturel d'ajouter une sorte de conclusion ou de résumé-->

