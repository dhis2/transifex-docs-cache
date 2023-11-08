---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/implementation/server-hosting.md"
revision_date: '2022-09-01'
tags:
- Implémentation
---

# Hébergement du serveur DHIS2{ #dhis2-server-hosting } 

Ce chapitre présente les défis liés à la mise en place d'un système DHIS2 en production. Il décrit les différentes approches que l'on rencontre couramment dans la pratique et examine d'un œil critique les avantages et les inconvénients de chacune d'entre elles. Il vise à fournir des conseils pratiques et pragmatiques aux organisations qui planifient la mise en œuvre de DHIS2. Le document se réfère à un ministère national de la santé (MDS) en tant que propriétaire potentiel du système, mais la plupart des considérations s'appliquent également à d'autres types d'organisations.

## Architecture { #architecture } 

### Installation la plus basique de DHIS2 { #most-basic-dhis2-installation } 

DHIS2 est une application web Java soutenue par une base de données qui peut être configurée pour fonctionner très simplement, en utilisant simplement un moteur de servlet Java tel que tomcat ou jetty et un serveur de base de données postgresql. Une personne ayant des compétences techniques raisonnables peut lire le guide de référence de DHIS2 et configurer les deux paquets ainsi que la connexion à la base de données qui les relie de manière relativement simple sur un ordinateur portable. Ce type d'installation est assez courant pour les développeurs ou les personnes qui souhaitent simplement essayer DHIS2 localement et voir à quoi il ressemble. Le fichier de l'application web DHIS2 (le fichier WAR) est téléchargé à partir de la page https://dhis2.org/downloads, la connexion à la base de données est configurée dans dhis.conf et l'application DHIS2 est accessible via un navigateur web se connectant au serveur tomcat en cours d'exécution.

![Simple architecture](resources/images/simple_architecture.png "Architecture simplifiée")

La mise en place et le fonctionnement de DHIS2 en production impliquent bien plus que les composants logiciels connectés. Les ressources matérielles doivent être approvisionnées et gérées. Les logiciels doivent être installés en tenant compte de la sécurité, des performances et de la facilité de maintenance. Dans la plupart des cas, il y aura plus d'un système DHIS2 et potentiellement d'autres systèmes au sein de l'architecture. Il faudra tenir compte de l'infrastructure environnante (systèmes de surveillance, systèmes de messagerie, composants d'interopérabilité, etc.) Et surtout, un mélange considérable de compétences techniques et d'expérience (warmware) est nécessaire pour concevoir, installer et gérer le système.

### DHIS2 en production { #dhis2-in-production } 

La planification d'un serveur DHIS2 qui fonctionne dans un environnement de production est un exercice beaucoup plus long et laborieux, car :
- en général, l'application devra être disponible en permanence, avec très peu de temps d'arrêt planifiés ou non
- les données qu'il contiendra sont précieuses et potentiellement sensibles
- les grands sites peuvent compter des dizaines de milliers d'utilisateurs et avoir des millions de registres
- le système devra être activement entretenu et mis à jour pendant de nombreuses années

Tous ces éléments donnent lieu à des exigences assez complexes en matière d'infrastructure physique, de contraintes de sécurité et de performance, ainsi qu'à un large éventail de compétences techniques, qui n'apparaissent pas immédiatement à la vue de l'architecture simple ci-dessus. Il est essentiel que l'implémentation du serveur soit correctement planifiée lors de la phase de planification d'une implémentation afin de pouvoir mobiliser les ressources physiques et humaines nécessaires pour répondre à ces exigences.

## Élaboration d'un plan{ #making-a-plan } 
### Sécurité { #security } 
Il est toujours judicieux d'avoir la sécurité à l'esprit dès le départ. Dans la pratique, cela pourrait signifier que vous avez prévu un budget :
1. intégrer un chargé de sécurité au sein de l'équipe centrale. Une grande partie du rôle du chargé de sécurité consistera à élaborer un plan de gestion de la sécurité, par exemple en suivant les lignes directrices de la norme ISO27001.
2. pour procéder à un audit annuel interne ou, de préférence, externe du système. Vous trouverez plus de détails sur la sécurité dans ce guide à la [section qui lui est dédiée](#security-considerations).
### Sauvegardes et archivage{ #backups-and-archiving } 
Les considérations détaillées ici doivent découler du plan de sécurité et être mises en place conformément au processus d'installation. Nous attirons particulièrement l'attention sur ce point car, d'après notre expérience au fil des ans, les " désastres " les plus courants que nous observons sont liés à des sauvegardes inadéquates, qui entraînent souvent une perte irrémédiable de données.

Les aspects importants du plan de sauvegarde à prendre en compte sont les suivants:
1. Quels sont les objectifs de récupération ponctuels (combien de données pouvez-vous vous permettre de perdre) ?
2. Automatisation. Un plan de sauvegarde qui dépend de l'intervention humaine pour effectuer les sauvegardes n'est pas un plan fiable
3. Archivage hors site. Le stockage des sauvegardes sur la même machine présente un certain intérêt, mais il faut tenir compte de la possibilité d'une défaillance catastrophique de la machine (ou des machines voisines). Cela inclut les machines virtuelles en nuage. Il faut également tenir compte du coût de la capacité des disques à grande vitesse. Pour ceux qui le peuvent, l'archivage hors site à l'aide du stockage d'objets (compatible S3) est désormais disponible auprès d'une série de fournisseurs de services en nuage et constitue généralement le moyen le moins cher et le plus simple pour gérer l'archivage.
4. Test. Les sauvegardes doivent être testées périodiquement (de préférence de manière automatisée) pour s'assurer que les fichiers que vous estimez avoir été sauvegardés le sont réellement.

Le plan de sauvegarde comporte d'autres aspects, mais le point important à souligner est qu'il doit être sérieusement envisagé dès le début d'un projet plutôt qu'après réflexion. Il y a toujours des compromis budgétaires à faire, donc tout plan de sauvegarde doit être correctement évalué en tenant compte des exigences de conservation par rapport au budget.

## Environnement physique { #physical-environment }

L'une des parties les plus importantes de votre plan consistera à prendre des décisions sur l'environnement physique dans lequel vos serveurs fonctionneront. Le premier grand choix consiste à posséder son propre équipement et ses propres installations d'hébergement ou à faire appel à un fournisseur de services en nuage et à payer pour l'utilisation des ressources et éventuellement d'autres services tels que la gestion des applications. Il n'y a pas de bonne ou de mauvaise réponse et votre choix sera déterminé par des facteurs tels que le coût, les compétences disponibles, l'infrastructure existante, la conformité réglementaire, etc. Le DHIS2 a été mis en œuvre avec succès à l'aide d'une variété de modèles de déploiement, bien que chacun d'entre eux s'accompagne de son propre ensemble de risques et de défis. Dans cette section, nous proposons quelques réflexions sur chacun d'entre eux et terminons par un bref tableau récapitulatif des facteurs à prendre en compte.

### A la base { #in-the-basement } 
Cette description légèrement ironique fait référence aux organisations qui achètent des équipements de serveur et les installent dans une salle de serveur dans le bâtiment. Le fait d'avoir tout à portée de main maximise le sentiment de contrôle sur les ressources, mais ce contrôle s'accompagne d'une plus grande responsabilité.

Cette approche est de loin la plus difficile à mettre en œuvre. Les défis courants sont les suivants :

1.  des contrôles de sécurité incendie insuffisants
2.  un risque de dégât des eaux dû à des climatiseurs et/ou à une plomberie environnante en mauvais état
3.  la présence d'un circuit électrique indépendant du réseau électrique du bâtiment
4.  un contrôle insuffisant ou inexistant de la poussière
5.  des câbles endommagés dus à une infestation de rongeurs
6.  la difficulté à accéder physiquement et à tout moment aux bâtiments gouvernementaux en dehors des heures de bureau

Les considérations architecturales à elles seules constituent une proposition assez coûteuse. Placer des équipements et des racks de classe serveur dans un environnement non réglementé réduira la durée de vie fonctionnelle et annulera les garanties.

En raison des coûts et des risques encourus, nous déconseillons dans la plupart des cas d'emprunter cette voie. Un plus grand nombre de compétences techniques sont également requises, notamment en matière d'ingénierie des centres de données, de réseau et de sécurité, ce qui peut être évité en utilisant l'une des approches ci-dessous.

### Centre de données d'un ministère ou du gouvernement { #ministry-or-national-government-data-centre } 
Conscients des difficultés susmentionnées, de nombreux pays ont adopté une stratégie consistant à concentrer les besoins d'hébergement dans des centres de données spécialement construits à l'échelle du gouvernement ou du ministère.

- le mode de gestion varie
- les compétences en matière de logiciels libres ne sont pas toujours répandues (utilisation fréquente de Windows, hyperV et vmware)
-  l'accès aux services et les modifications de la configuration du réseau, entre autres, peuvent être très lourds sur le plan administratif
-  les machines virtuelles surdimensionnées rencontrent des problèmes de performance, en particulier au niveau du disque des serveurs de bases de données

### Co-location ou hébergement virtuel au sein d'un pays { #in-country-co-location-or-virtual-hosting } 
Certains pays ont fait appel avec succès à des fournisseurs locaux de centres de données pour héberger des serveurs physiques (colocation) ou pour louer des ressources virtuelles. Cette approche présente l'avantage de répondre aux exigences en matière de géolocalisation des données (par exemple, toutes les données doivent être stockées dans le pays). Par ailleurs, le gouvernement a tendance à avoir plus d'influence sur ces entreprises que sur les grands fournisseurs commerciaux mondiaux - ils sont moins susceptibles d'être coupés lorsque le paiement de la facture est en retard !

Les risques potentiels de cette approche sont les suivants :
- en raison des économies d'échelle, l'hébergement local a tendance à être plus coûteux que les entreprises Cloud mondiales
- lorsque l'État a imposé qu'une entreprise donnée soit désignée comme « fournisseur privilégié », des problèmes de performance et de service à la clientèle sont souvent constatés

### Fournisseurs de services en nuage { #commercial-cloud-providers } 
- infrastructure générique en tant que service (linode, aws, azure, etc.)
- prestataires de services spécialisés DHIS2 - Logiciel en tant que service (BAO, BlueSquare, HISP SA, etc.)



|Approche|Description|Coût|Compétences|Sécurité|
|--------|-----------|----|------|--------|
|Au sous-sol|Le serveur est installé dans le ministère, généralement dans une salle reconvertie|Les coûts d'installation peuvent être élevés, pour mettre la salle aux normes en matière d'électricité, de climatisation, etc.|Un haut niveau de compétences est requis, allant de l'administration système à l'administration réseau en passant par des connaissances en gestion des centres de données|La sécurité physique et la sécurité du réseau sont des défis supplémentaires|
|Centre de données gouvernemental au niveau national|Les applications du ministère de la Santé sont hébergées dans un centre de données construit à cet effet et géré comme un service intergouvernemental|Le coût pour le ministère de la santé varie en fonction des mécanismes de recouvrement des coûts du centre de données. Il varie de zéro à beaucoup plus élevé que celui du cloud commercial.|Les compétences requises pour faire fonctionner le système se limitent à l'administration du système. Le centre de données doit disposer d'autres compétences liées aux réseaux ainsi qu'à la gestion et à l'approvisionnement des machines virtuelles.|Les préoccupations en matière de sécurité sont partagées par les responsables de la mise en œuvre et le fournisseur du centre de données|
|Cloud commercial 1 (Infrastructure en tant que service)|Le ministère de la Santé possède un compte auprès d'une entreprise commerciale de Cloud et paie pour l'utilisation des ressources du serveur|En général, c'est l'option la moins coûteuse. Variations considérables des plans de tarification sur le marché|Il suffit d'avoir des compétences d'administrateur système pour mettre en place et faire fonctionner le système. Des processus de gestion doivent être mis en place pour gérer le budget et s'assurer que les factures sont payées.|Les préoccupations en matière de sécurité sont partagées entre les responsables de la mise en œuvre et le fournisseur de services Cloud|
|Cloud commercial 2 (logiciel en tant que service)|Le ministère de la Santé possède un compte auprès d'une société commerciale qui propose la solution DHIS2 en tant que service|Plus coûteux que l'infrastructure en tant que service, mais supprime la nécessité de verser un salaire onéreux pour un administrateur système|Des processus de gestion doivent être mis en place pour gérer le budget et garantir le paiement des factures|La plupart des problèmes de sécurité sont gérés par le prestataire de services|

## Compétences requises { #required-skillset } 
DHIS2 est un système relativement complexe à administrer. L'équipe chargée de l'administration du système devra disposer d'une expertise et d'une expérience dans les domaines suivants: 
- ubuntu linux
- Proxy web Apache2 ou nginx
- Apache tomcat 
- Base de données Postgresql
Si cette expérience n'est pas disponible en interne, le ministère serait bien avisé de confier une partie de la gestion à une entité locale disposant d'un tel portefeuille de compétences, même si cela est considéré comme un arrangement transitoire.

## Maintenance { #maintenance } 

Au-delà de l'installation, les activités courantes consistent en général à :
1. fournir des instances de mise en scène, de test et de formation, au besoin
2. le contrôle des performances et l'adaptation du logiciel à la situation
3.  gérer et tester les sauvegardes
4.  la proposition de correctifs (fréquence typique de 4-6 semaines) pour les mises à jour de versions mineures 
5.  planifier et exécuter la mise à niveau majeure de l'instance DHIS2 (tous les ans)
6.  proposer des mises à niveau majeures du système d'exploitation et du serveur de base de données (tous les 2 ou 3 ans)

L'UIO peut fournir une formation sur l'architecture globale et tout ce qui est spécifique à DHIS2 et également relier les responsables de la maintenance à la communauté mondiale de pratique dans l'administration du système DHIS2. Il est à noter qu'il existe des exigences préalables en ce qui concerne les compétences énumérées ci-dessus. Il n'est ni pratique ni judicieux de dépendre des administrateurs de système qui n'ont pas l'expérience requise.

## Installation et configuration du logiciel{ #software-installation-and-configuration } 
L'équipe de l'UiO met à votre disposition un certain nombre de ressources pour faciliter l'installation :

- Le [guide] (https://docs.dhis2.org/en/manage/manage.html)de référence définitif de DHIS2 est tenu à jour par les développeurs de DHIS2 et il est important de le lire attentivement pour obtenir une description complète de la configuration et de la fonctionnalité de DHIS2 du point de vue du backend. Un administrateur système expérimenté peut y trouver ce dont il a besoin pour concevoir une installation DHIS2 prête pour la production. Il y a beaucoup de travail supplémentaire à faire pour approvisionner, surveiller et sécuriser l'environnement ambiant.
- Idéalement, l'installation devrait être automatisée, plutôt qu'une œuvre d'art réalisée à la main. Nous fournissons des [outils] ([https://github](https://github.com/bobjolliffe/dhis2-tools-ng)) pour automatiser au moins la plupart des aspects de l'installation à l'aide de conteneurs LXD. Ces outils se sont avérés utiles pour de nombreuses implémentations et s'inspirent des documents de référence ci-dessus et d'autres documents pour coder les bonnes pratiques par défaut.
- L'objectif actuel du [project](https://github.com/dhis2/dhis2-server-tools) est de moderniser le mode d'installation ci-dessus et de la réimplémenter pour utiliser des playbooks Ansible et dépendre moins des conteneurs LXD.

