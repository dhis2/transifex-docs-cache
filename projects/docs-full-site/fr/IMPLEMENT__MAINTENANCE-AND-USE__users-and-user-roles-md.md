---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/maintenance_use/users-and-user-roles.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Utilisateurs et rôles d'utilisateurs { #users-and-user-roles } 

## À propos de la gestion des utilisateurs { #about_user_userrole } 

Plusieurs utilisateurs peuvent accéder simultanément au DHIS2 et chaque utilisateur peut avoir 
des différents types d'autorisations. Vous pouvez donc régler ces autorisations de manière à ce que 
certains utilisateurs ne puissent que saisir des données, tandis que d'autres ne peuvent que générer 
des rapports.

  - Vous pouvez créer autant d'utilisateurs, de rôles d'utilisateurs et de groupes d'utilisateurs que vous 
    souhaitez.

  - Vous pouvez attribuer des pouvoirs spécifiques à des groupes d'utilisateurs ou à des 
    utilisateurs individuels via des rôles d'utilisateur.

  - Vous pouvez créer plusieurs rôles d'utilisateur, chacun disposant de ses propres autorités.

  - Vous pouvez attribuer des rôles d'utilisateur aux utilisateurs pour leur accorder
    les autorités correspondantes.

  - Vous pouvez attribuer à chaque utilisateur des unités d'organisation. L'utilisateur peut ensuite 
    saisir des données pour les unités d'organisation qui lui sont attribuées.



Tableau: Termes et définitions relatifs à la gestion des utilisateurs

| Terme | Définition | Exemple |
|---|---|---|
| Autorisations | Une autorisation pour effectuer une ou plusieurs tâches spécifiques | Créer un nouvel élément de données <br> <br> Mettre à jour une unité d'organisation <br> <br> Consulter un rapport |
| Utilisateur | Le compte utilisateur DHIS2 d'une personne | administrateur<br><br>traore<br><br>invité |
| Rôle de l'utilisateur | Un groupe d'autorités | Commis à la saisie des données<br><br>Administrateur du système<br><br>Accès au programme de soin prénatal |
| Groupe d’utilisateurs | Un groupe d'utilisateurs | Personnel du Kenya <br> <br> Destinataires des feedbacks <br> <br> Coordinateurs du programme VIH |

L'application **Utilisateurs** vous permet de gérer les utilisateurs, les rôles des utilisateurs et les groupes d'utilisateurs.



Tableau : Objets dans l'application "Utilisateurs"

| Type d'objet | Fonctions disponibles |
|---|---|
| Utilisateur | Créer, modifier, inviter, cloner, désactiver, afficher par unité d'organisation, supprimer, afficher les détails  |
| Rôle de l'utilisateur | Créer, modifier, partager, supprimer et afficher les détails |
| Groupe d’utilisateurs | Créer, modifier, rejoindre, quitter, partager, supprimer et afficher les détails |

### À propos des utilisateurs { #about-users } 

Chaque utilisateur dans DHIS2 doit avoir un compte d'utilisateur identifié par un 
nom d'utilisateur. Vous devez enregistrer un prénom et un nom de famille pour chaque utilisateur ainsi 
que des informations de contact, par exemple une adresse électronique et un numéro de
téléphone.

Vous devez enregistrer les bonnes coordonnées. DHIS2 
utilise ces informations pour contacter directement les utilisateurs, par exemple pour envoyer 
des courriels afin de les informer d'événements importants. Vous pouvez également utiliser les 
informations de contact pour partager, par exemple, des tableaux de bord et des tableaux croisés dynamiques.

Un utilisateur de DHIS2 est associé à une unité d'organisation. Vous devez donc 
attribuer l'unité d'organisation où l'utilisateur travaille.

Lorsque vous créez un compte d'utilisateur pour un responsable de l'enregistrement du district, vous devez 
lui attribuer le district où il travaille comme unité d'organisation.

L'unité organisationnelle assignée influence la manière dont l'utilisateur peut utiliser le DHIS2 :

  - Dans l'application **Saisie de données**, un utilisateur ne peut saisir des données que pour
    l'unité d'organisation à laquelle il est associé et pour les unités d'organisation
    qui lui sont subordonnées dans la hiérarchie. Par exemple, un responsable de l'enregistrement du district
    ne pourra enregistrer des données que pour son district et les 
    établissements qui lui sont subordonnés.

  - Dans l'application **Utilisateurs**, un utilisateur ne peut ajouter de nouveaux utilisateurs que pour
    l'unité d'organisation à laquelle il est associé, ainsi que pour les 
    unités d'organisation qui lui sont subordonnées dans la hiérarchie.

  - Dans l'application **Rapports**, un utilisateur ne peut consulter que les rapports de son
    unité d'organisation et de celles qui lui sont subordonnées. (C'est un point que nous envisageons 
    d'ouvrir pour permettre de faire des rapports de comparaison.)

Une aspect important de la gestion des utilisateurs consiste à contrôler quels utilisateurs sont 
autorisés à créer de nouveaux utilisateurs et avec quelles autorités. Dans le système DHIS2, vous pouvez 
contrôler quels utilisateurs sont autorisés à effectuer cette tâche. Le principe clé 
est qu'un utilisateur ne peut accorder des autorités et un accès à des ensembles de données que 
s'il y a accès lui-même. Le nombre d'utilisateurs au niveau national, provincial et 
du district est souvent relativement peu élevé et peut être créé et 
géré par les administrateurs du système. Si la grande majorité des 
établissements saisit directement les données dans le système, le nombre 
d'utilisateurs peut devenir trop important. Il est donc recommandé de déléguer et 
de décentraliser cette tâche aux responsables de district, ce qui rendra le 
processus plus efficace et permettra de mieux soutenir les utilisateurs des établissements.

### À propos des rôles des utilisateurs { #about-user-roles } 

Un rôle d'utilisateur dans le DHIS2 est un groupe d'autorités. Une autorité signifie
l'autorisation d'effectuer une ou plusieurs tâches spécifiques.

Un rôle d'utilisateur peut contenir des autorités permettant de créer un nouvel élément de donnée, mettre à jour une unité d'organisation ou visualiser un rapport.

Un utilisateur peut avoir plusieurs rôles d'utilisateur. Dans ce cas, les autorités de l'utilisateur seront 
la somme de toutes les autorités et de tous les ensembles de données contenus dans les rôles d'utilisateur. Cela 
signifie que vous pouvez mélanger et faire correspondre les rôles d'utilisateur à des fins particulières au lieu 
de n'en créer que de nouveaux.

Un rôle d'utilisateur est associé à une collection d'ensembles de données. Cela concerne 
l'application **Saisie de données** : un utilisateur ne peut saisir que les données des ensembles de données 
enregistrés pour son rôle d'utilisateur. Cela peut être utile lorsque, par exemple, 
vous souhaitez autoriser agents des programmes de santé à ne saisir que les données de 
leurs formulaires de saisie concernés.

Recommandations :

  - Créer un rôle d'utilisateur pour chaque poste au sein de l'organisation.

  - Créer les rôles des utilisateurs en définissant parallèlement quel utilisateur effectue 
    quelles tâches dans le système.

  - Ne donnez aux rôles d'utilisateur que les pouvoirs exacts dont ils ont besoin pour effectuer
    leur travail, pas plus. Seules les personnes censées effectuer une tâche
    doivent avoir le pouvoir de l'exécuter.

### À propos des groupes d'utilisateurs { #about-user-groups } 

Un groupe d'utilisateurs est un groupe composés uniquement d'utilisateurs. Vous utilisez les groupes d'utilisateurs lorsque vous configurez 
le partage d'objets ou de notifications, par exemple les rapports push ou les notifications 
de programmes.

Voir également :

[Partage](https://ci.dhis2.org/docs/master/en/user/html/sharing.html)

[Gérer les notifications
du programme](https://docs.dhis2.org/master/en/user/html/manage_program_notification.html)

[Gérer les rapports
push](https://docs.dhis2.org/master/en/user/html/manage_push_report.html)

## Déroulement { #user_mgt_workflow } 

1.  Définissez les postes dont vous avez besoin pour votre projet et identifiez 
    les tâches que les différents postes effectueront.

2.  Créez plus ou moins un rôle d'utilisateur pour chaque poste.

3.  Créez des utilisateurs.

4.  Attribuez des rôles d'utilisateur aux utilisateurs.

5.  Affectez les utilisateurs à des unités d'organisation.

6.  (Facultatif) Regrouper les utilisateurs en groupes d'utilisateurs.

7.  Partager des ensembles de données avec des utilisateurs ou des groupes d'utilisateurs via la boîte de dialogue Partage dans
    la section Gestion des ensembles de données de l'application Maintenance.

> **Conseil**
>
> Pour permettre aux utilisateurs de saisir des données, vous devez donc les ajouter à un 
> niveau d'unité d'organisation et partager avec eux un ensemble de données.

## Exemple : gestion des utilisateurs dans un système sanitaire { #user_mgt_example } 

Dans un système de santé, les utilisateurs sont logiquement regroupés en fonction de la tâche qu'ils accomplissent et du poste qu'ils occupent.

1.  Définir les utilisateurs qui doivent jouer le rôle d'administrateur du système.
    Ils font souvent partie de la division nationale du HIS et devraient avoir
    toute autorité dans le système.

2.  Créez plus ou moins un rôle d'utilisateur pour chaque poste.

Voici des exemples de positions courantes :


| Position | Tâches spécifiques | Autorités recommandées | Commentaire |
|---|---|---|---|
| Administrateurs système | Configurer la structure de base (métadonnées) du système. | Ajoutez, mettez à jour et supprimez les éléments de base du système, par exemple les éléments de données, les indicateurs et les séries de données. | Seuls les administrateurs du système doivent modifier les métadonnées. <br> Si vous autorisez des utilisateurs à modifier les métadonnées, alors qu'ils ne font pas partie de l'équipe des administrateurs du système, cela peut entraîner des problèmes de coordination. <br> <br> Les mises à jour du système ne doivent être effectuées que par les administrateurs du système. |
| Directeur national de la santé<br><br>Directeur provincial de la santé | Suivi et analyse des données | Accès au module de rapports, aux applications **Cartes**, **Qualité des données** et au tableau de bord. | Vous n'avez pas besoin d'accès pour entrer des données, modifier des éléments de données ou des séries de données. |
| Responsables de la division du système national d'information sanitaire (HISO) <br> <br> Responsables des archives et de l'information sanitaires de district (DHRIO) <br> <br> Responsables des archives et de l'information sanitaires des établissements (HRIO) | Entrer les données provenant des établissements qui ne sont pas en mesure de le faire directement <br> <br> Surveiller, évaluer et analyser les données | Accès à toutes les applications d'analyse et de validation <br> <br> Accès à l'application **Entrée de Données**. | - |
| Commis à la saisie de données | - | - | - |

