---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/support_documentation/support.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Aide { #support } 

La communauté DHIS2 utilise un ensemble de plateformes de collaboration et de coordination 
pour l'information et la fourniture de téléchargements, de documentation, de 
développement, de code source, de spécifications de fonctionnalité, de suivi des bogues. 
Ce chapitre les décrit plus en détail.

## Page d'accueil : dhis2.org { #home-page-dhis2org } 

La page d'accueil de DHIS2 se trouve à l'adresse *https://www.dhis2.org/*. La page *Téléchargements* 
fournit des liens pour télécharger les fichiers WAR de DHIS2, l'application de Saisie mobile 
Android, le code source, des exemples de bases de données, ainsi que des liens vers des ressources et des 
guides supplémentaires. Veuillez noter que nous fournissons des mises à jour de maintenance pour les trois dernières 
versions de DHIS2. Nous vous recommandons de consulter régulièrement la page de 
téléchargement et de mettre à jour votre serveur en ligne avec un patch stable 
correspondant à votre version de DHIS2. Les informations sur la version et la révision de la construction peuvent être trouvées 
sous la page *A propos de DHIS2* à l'intérieur de votre instance DHIS2.

Le menu de navigation fournit des descriptions claires du contenu du site, et 
un champ de recherche dans l'en-tête vous permet d'effectuer facilement des recherches dans le site.


## Plate-forme de collaboration : community.dhis2.org { #collaboration-platform-communitydhis2org } 

La principale plateforme de collaboration de DHIS2 est la *Communauté de pratique DHIS2*. Le site est 
accessible à l'adresse *https://community.dhis2.org/* et est basé sur la plateforme de Discussion.

La Communauté de Pratique est utilisée pour faciliter le soutien de la communauté aux problèmes des utilisateurs de DHIS2, ainsi 
que pour aider à identifier les bogues potentiels dans les versions existantes du logiciel et les demandes 
de fonctionnalités pour les versions futures. C'est également un endroit où les membres de la communauté peuvent partager des histoires, 
des bonnes pratiques et des défis liés à la mise en œuvre de DHIS2, collaborer avec d'autres 
ur des projets et proposer leurs services à l'ensemble de la communauté. Les utilisateurs peuvent configurer leur compte de Communauté 
de Pratique en fonction de leurs préférences individuelles en matière de paramètres de notification, et peuvent répondre 
aux questions existantes par e-mail.

La section *Assistance* de la Communauté de Pratique comprend tous les sujets qui ont été créés en utilisant 
l'ancienne plateforme de collaboration du DHIS2, Launchpad, qui n'est plus active.

Les bogues identifiés au sein de la Communauté de Pratique doivent être soumis à l'équipe principale de DHIS2 sur *Jira*

## Signaler un problème { #reporting-a-problem } 

Si vous rencontrez un problème lors de l'utilisation du DHIS2, veuillez suivre les étapes suivantes :

  - Effacez complètement le cache du navigateur web (également appelé historique ou données de navigation) 
    (vous pouvez utiliser l'application Nettoyage du cache du navigateur dans DHIS2 ; sélectionnez toutes les options avant de procéder à la suppression).

  - Vider le cache de l'application DHIS2 : Allez dans Administration des données -> Maintenance,
    Vider le cache de l'application DHIS2 : Allez dans Administration des données -> Maintenance,

Si le problème persiste, rendez-vous dans la Communauté de pratique et utilisez des termes clés pour rechercher 
des sujets que d'autres utilisateurs ont publiés et qui décrivent des problèmes similaires, afin de savoir si votre problème 
a déjà été signalé et résolu. Si vous ne parvenez pas à trouver un fil de discussion décrivant un problème similaire, 
vous devez créer un nouveau sujet dans la catégorie *Assistance*. Les membres de la communauté 
et l'équipe DHIS2 vous répondront pour tenter de vous aider à résoudre votre problème.

Si la réponse que vous avez reçue dans la communauté de pratique indique que vous avez identifié 
un bogue, vous devez publier un rapport de bogue sur DHIS2 Jira.

## Suivi du développement : jira.dhis2.org{ #development-tracking-jiradhis2org } 

*Jira* est le site où l'on peut signaler des problèmes et suivre les exigences, les progrès et la feuille de route 
du logiciel DHIS2. Le site DHIS2 Jira est accessible à l'adresse https://jira.dhis2.org/.

Si vous trouvez un bogue dans DHIS2, vous pouvez le signaler sur Jira en vous rendant sur 
la page d'accueil Jira de DHIS2, en cliquant sur *créer* dans le menu supérieur, en sélectionnant "bogue" comme type de 
problème et en renseignant les champs requis.

Pour que les développeurs puissent vous aider, vous devez fournir autant d'informations 
utiles que possible :

  - Version DHIS2 : Consultez la page d'aide - \> A propos de DHIS2 et
    indiquez la version et la révision du logiciel.

  - Navigateur web, version comprise.

  - Système d'exploitation, version comprise.

  - Conteneur de servlets / journal Tomcat : Indiquez toute sortie dans le journal Tomcat
    (typiquement catalina.out) liée à votre problème.

  - Console du navigateur web : Dans le navigateur web Chrome, cliquez sur F12, puis sur
    "Console", et recherchez les exceptions liées à votre problème.

  - Actions menant au problème : décrivez aussi clairement que possible 
    les mesures que vous avez prises et qui ont mené au problème ou à cette exception.

  - Description du problème : Décrivez clairement le problème, pourquoi vous pensez qu'il 
    s'agit d'un problème et quel est le comportement que vous attendez du système.

Votre rapport de bogue sera examiné par l'équipe de test et d'assurance qualité, qui lui attribuera un statut. 
S'il est valide, son statut sera défini comme "À FAIRE" et sera visible par l'équipe de développement 
ans sa planification des étapes et des versions. Il peut alors être confié à un développeur 
et être corrigé. Notez que les corrections de bogues sont incorporées dans la branche principale et dans les branches 
des trois dernières versions (supportées) du DHIS2 - ainsi, plus de tests et de retours aux 
équipes de développeurs conduisent à une meilleure qualité de votre logiciel.

Si vous souhaitez suggérer une nouvelle fonctionnalité à mettre en œuvre dans DHIS2, vous 
devez d'abord lancer une discussion sur la communauté de pratique afin d'obtenir des avis sur votre 
idée et de confirmer que la fonctionnalité que vous suggérez n'existe pas déjà. 
Une fois ces étapes franchies, vous pouvez soumettre une demande de fonctionnalité sur DHIS2 Jira 
en cliquant sur "Créer" dans le menu supérieur et en sélectionnant "Fonctionnalité" comme type de problème. 
Votre demande de fonctionnalité sera examinée par l'équipe de développement et, si elle est acceptée, 
un développeur et une version de lancement lui seront attribués. Les utilisateurs du DHIS2 peuvent voter pour apporter 
leur soutien aux demandes de fonctionnalités qui ont été soumises. Les demandes de fonctionnalités existantes 
peuvent être consultées en utilisant la fonction "filtre" de Jira.


## Code source: github.com/dhis2 { #source-code-githubcomdhis2 } 

Les différentes branches du code source, y compris les branches ''master'' et ''release'', 
peuvent être consultées à l'adresse *https://github.com/dhis2*

