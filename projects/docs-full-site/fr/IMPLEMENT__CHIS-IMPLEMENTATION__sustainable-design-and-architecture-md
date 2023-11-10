---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/chis_implementation/06_dhis2_configuration.md"
revision_date: '2022-04-20'
tags:
- Implémentation
---

# Conception et architecture du CHIS DHIS2 durable{ #sustainable-chis-dhis2-design-and-architecture } 

Un CHIS durable doit être conçu de manière à satisfaire les besoins d'information des parties prenantes concernées et être assez flexible pour évoluer en fonction des besoins d'information du système qui évoluent constamment. Les considérations architecturales sont importantes car le CHIS ne doit pas être isolé et doit pouvoir communiquer avec d'autres systèmes. Cela nécessite un modèle de données bien conçu qui garantisse l'obtention des résultats envisagés pour le CHIS. Ce chapitre examine les éléments à prendre en compte pour élaborer une architecture et une conception solides pour un CHIS utilisant le DHIS2. Il a été rédigé en partant du principe que :

- Le responsable de la conception du modèle de données a une connaissance approfondie des modèles de données du DHIS : agrégés, événements et tracker.
- Le responsable du déploiement a une connaissance approfondie de l'infrastructure nationale et une expérience acquise lors de déploiements similaires.

## Processus de Conception, de Développement, de Test et de Déploiement du Système CHIS : { #chis-system-design-develop-test-and-deploy-process }

Le processus de conception d'un CHIS dans DHIS2 se décline en neuf étapes.

### 1. Mapping des processus opérationnels actuels { #1-mapping-current-state-business-processes } 

La pire configuration d'un CHIS dans DHIS2 est généralement celle dans laquelle les processus opérationnels du programme de santé communautaire actuel sont juste numérisés dans DHIS2 sans aucune modification pour les optimiser. Pour éviter cette erreur, la première étape de la conception d'un CHIS performant dans DHIS2 consiste à effectuer un mapping complet de l'état actuel du flux de données de suivi et d'évaluation du programme de santé communautaire. L'objectif principal de ce mapping est de :

1. Harmoniser les outils de rapport des ASC en un nombre aussi réduit que possible (1 ou 2).
2. Normaliser les outils de déclaration harmonisés dans tout le pays.
3. Identifier les exemples de bon fonctionnement.
4. Identifier les défauts de fonctionnement et trouver un moyen d'amélioration.

Le mapping du processus opérationnel actuel se fait essentiellement en deux étapes.

1. Compilation de tous les formulaires de collecte de données existants. Pour chaque formulaire, identifiez :
    - Quels sont les éléments de données et indicateurs présentes sur ce formulaire ? Font-ils partie du cadre de suivi et d'évaluation du CHIS ? Si non, doit-on toujours les saisir ?
    - Qui est responsable de la saisie des données et combien de temps cela prend-il?
    - A quelle fréquence le formulaire de déclaration est-il rempli ?
    - Quelles sont les erreurs ou difficultés courantes rencontrées lors du remplissage du formulaire de collecte de données ?
    - Quels outils d'aide sont intégrés au formulaire de collecte de données ? Fonctionnent-ils ? A-t-on besoin de plus d'outils ?
    - Faites un mapping du flux de données électronique ou papier du point de collecte au niveau central
        - Pour quelle unité organisationnelle les données sont-elles collectées ?
        - Quels sont les points d'agrégation ? Qui effectue les agrégations ?
2. Compilation de tous les outils actuels d'analyse et d'utilisation des données. Pour chaque outil, identifiez :
    - Quel est le niveau de granularité des données présentées ?
        * Niveau organisationnel d'agrégation (communauté, établissement, district ou national)
        * Période d'agrégation (quotidien, hebdomadaire, mensuel, etc.)
    - Quelles décisions sont prises ou actions menées sur la base de cet outil ?
    - Quels sont les problèmes ou défis rencontrés avec l'outil ?
    - Que pourrait-on faire pour résoudre ces problèmes ou relever ces défis ?

### 2. Éléments à prendre en compte lors de l'introduction des processus opérationnels dans DHIS2{ #2-considerations-in-translating-business-process-to-dhis2 }

L'introduction des flux de données des communautés dans DHIS2 est l'étape la plus importante du processus de conception. Neuf éléments essentiels doivent être pris en compte à cet effet. Il s'agit de :

1. Logique d'agrégation des données
2. Périodes et fréquence des rapports
3. Hiérarchie organisationnelle
4. Programmes de santé verticaux vis-à-vis du HMIS
5. Rapports des partenaires
6. Résultats : internes et externes
7. Considérations relatives aux infrastructures
8. Aspects technologiques à prendre en compte pour la collecte de données = sélection des outils
9. Sécurité

#### Logique d'agrégation de données { #logic-of-data-aggregation }

**L'extension du système existant de l'établissement** aux agents de santé communautaires doit garantir que la logique d'agrégation des données reste synchronisée au sein du CHIS en place. Lors de la conception de l'agrégation, cinq scénarios types peuvent se présenter.

1. **Déclaration des données agrégées par l'ASC** : Si les données agrégées sont collectées au niveau de l'établissement et que les ASC rapportent également des chiffres agrégés, la valeur additionnée des données de l'établissement et des ASC doit refléter la réalité. Par exemple :
    - Cas 1 - L'ASC est seul responsable de la déclaration de toutes les femmes enceintes enregistrées pour la CPN dans la région. Cet élément de données doit être rapporté par tous les ASC et son agrégation doit être considérée comme le nombre rapporté par l'établissement : c'est-à-dire : Nombre de femmes enceintes enregistrées pour la CPN au niveau de l'établissement = ASC1+ ASC2 ...
    - Cas 2 - Lorsque les ASC doivent rapporter cet élément de données des services communautaires et que l'établissement fournit également des services similaires, le nombre total de services fournis est obtenue par addition des chiffres fournis par les ASC et l'établissement : c'est-à-dire le nombre de femmes enceintes inscrites pour la CPN = établissement + ASC1+ ASC2 ...

    > **Note**
    > 
    > It is generally considered a best practice to have separate data sets for facilities and CHWs. Meaning, the CHW should not be submitting data via the facility data set. This is to minimize potential for double counting of patient between facility and CHW, and it enables better performance monitoring of CHWs and facilities.

2. **Déclaration de données basées sur des cas (tracker), où la localisation du cas n'est [pas]{.ul} importante** : Si des données agrégées sont collectées au niveau de l'établissement et que les ASC doivent collecter des données basées sur des noms/cas, l'agrégation de tous les cas/noms doit être effectuée au niveau de l'établissement. Cela signifie que les cas doivent être enregistrés en tant qu'entités suivies au niveau de l'établissement, même si les ASC sont en train de saisir les données.

    > For example, if there are 10 records of individual ANC cases captured by the CHW in the ANC tracker program for one month, then the facility value for ANC cases is 10. In DHIS2, this process of aggregation is automated.
    >
    > An example organizational hierarchy:
    >
    > - Facility (Org unit level)
    >   - ANC Case 1 (Tracked entity)
    >   - ANC Case 2 (Tracked entity)
    >   - ANC Case 3
    >   - etc.

3. **Déclaration de données basées sur des cas (tracker) lorsque la localisation du cas est importante** : Lorsque la localisation du cas est importante (c'est-à-dire le village, la communauté, etc.) dans le cadre du contrôle épidémiologique des maladies (ex : détection des cas actifs de paludisme) ou des services de proximité de porte à porte (ex : campagnes de vaccination), il peut être préférable que le cas soit enregistré dans le programme de tracker par rapport à l'unité organisationnelle la plus proche de son lieu d'habitation, là où il réside. Dans ce cas, le rapport agrégé de l'établissement sera un ensemble de données distinct et seuls les cas agrégés survenus dans l'établissement seront enregistrés. Souvent, avec des programmes de contrôle épidémiologique, les établissements rapportent également des cas individuels.

    > For example, in a malaria program where CHW are performing active case detection to villages of people who test positive for malaria the individual case should be enrolled against the village. This allows CHWs to know the location of cases for active case detection. Example organizational hierarchy below:

    > - Facility (Org unit level)
    >   - Village (Org unit level)
    >       - Malaria Case 1 (Tracked entity)
    >       - Malaria Case 2 (Tracked entity)
    >       - etc.

4. **Déclaration de données basées sur les cas (tracker) lorsque l'association des cas avec les ASC est importante:** Dans les situations où il est important d'associer des cas spécifiques à un ASC qui fournit des services (ex : programme d'éducation à la santé), le cas peut être enregistré dans le programme de tracker par rapport à l'ASC qui est configuré en tant qu'unité organisationnelle. Afin de gérer efficacement le taux de rotation élevé des ASC, l'unité organisationnelle de l'ASC doit représenter son poste et pas nécessairement son nom, ce qui signifie que l'ASC opérant en tant qu'unité d'organisation peut être remplacé sans que le nom de l'unité organisationnelle ne doive être modifié.

    > For example, in a HIV/AIDs education program where a CHW will provide young women with STI education, contraceptives, and counseling and testing it may be very important to associate an individual case with a specific CHW. The example organizational hierarchy is below:
    >
    > - Facility (Org unit level)
    >   - CHW 1 (org unit level)
    >       - Girl 1 (Tracked entity)
    >       - Girl 2
    >   - CHW 2
    >       - Girl 3 (tracked entity)

5. **Conception d'un nouveau CHIS** : lorsqu'il n'est pas nécessaire d'ajouter des éléments à un HIS d'établissement existant, la conception d'un nouveau CHIS  permet de définir une logique d'agrégation qui soit relativement indépendante de la nécessité de synchroniser l'agrégation avec l'établissement. Par exemple, si un CHIS est conçu juste pour une campagne ou un événement spécifique, il est donc relativement indépendant de la logique d'agrégation de l'établissement.


#### Périodes /Fréquence des rapports{ #reporting-periodsfrequency }

Important lorsque la période de rapport pour les ASC est différente de la période de rapport au niveau suivant, à savoir l'établissement. La fréquence des rapports des ASC doit être la même ou plus fréquente que celle des rapports des établissements. Les rapports de l'établissement ne doivent pas être plus fréquents que ceux des ASC. Par exemple :

Élément de données des ASC :

- Nombre de moustiquaires distribuées aujourd'hui (rapport quotidien)
- Nombre de moustiquaires distribuées cette semaine (rapport hebdomadaire)

Élément de données de l'établissement :

- Nombre de moustiquaires distribuées ce mois

Dans le premier cas (a) Avec 30 rapports quotidiens, le total mensuel agrégé de moustiquaires distribuées sera calculé comme suit : Total des moustiquaires distribuées = Établissement (mois) + ASC Jour 1 + ASC Jour 2 . . . . . + ASC Jour 30

Dans le deuxième cas (b) Avec 4 rapports hebdomadaires, le total mensuel agrégé de moustiquaires distribuées sera calculé comme suit : Total des moustiquaires distribuées = Établissement (Mois) + ASC Semaine 1 + ASC semaine 2 . . . . . + ASC semaine 4

Si la période des rapports est la même pour l'ASC et l'établissement, nous devons nous assurer que les logiques d'agrégation correspondent, tel qu'indiqué plus haut.

#### Unités d'organisation et Hiérarchie { #organization-units-and-hierarchy }

Un autre aspect important à prendre en compte est l'ajout des ASC dans la hiérarchie de déclaration des données. Compte tenu de l'importance et du nombre d'ASC, ce sujet sera l'un des importants à traiter lors la conception du CHIS.

Une arborescence représente la division administrative ou géographique à l'intérieur d'une hiérarchie. Par exemple:

> - Pays, siège \[L1\]
>   - Province, district (unité administrative) \[L2\]
>       - Établissement, clinique, hôpital ( offrant des services) \[L3\]

Dans l'exemple ci-dessus, la hiérarchie des unités organisationnelles suit la division administrative et géographique. La hiérarchie est ensuite divisée en unités organisationnelles telles qu'une province, un district ou un établissement donné. Les unités organisationnelles s'occupent de : la saisie des données, la sécurité : la saisie et les résultats, et l'analyse : les données sont agrégées / remontent la chaîne hiérarchique **(Règle d'or : l'agrégation doit toujours être pertinente).**.

**Lorsqu'elle est correctement configurée, la hiérarchie organisationnelle doit permettre à l'utilisateur de savoir :**

1. **Où** les données sont associées (patient individuel, ménage, village, établissement de santé, postes de santé communautaires, etc.).
2. **Quelle** est est la signification des données. Les données peuvent-elles être agrégées de manière pertinente en remontant la hiérarchie ? Les données saisies dans cette unité organisationnelle sont-elles pertinentes à ce niveau ?
3. **Quand** les données sont-elles saisies. La période assignée à l'ensemble de données ou au programme doit pouvoir être agrégée graduellement en remontant la hiérarchie. Par exemple, il n'est pas possible qu'un élément de données mensuel au niveau de la communauté soit agrégé à un élément de données hebdomadaire de son établissement principal.
4. **Qui** collecte les données et fournit les services. Ceci est particulièrement important avec les programmes de santé communautaire où nous avons besoin de connaître les actions et les services fournis par chaque ASC. Il est possible de le configurer au niveau de la hiérarchie.


> Important
>
> **Toute hiérarchie doit passer le test de hiérarchie du CHIS:**
>
> 1. Permet-elle de collecter des données par rapport à une unité organisationnelle qui représente le lieu et la personne auxquels les données sont associées ?
> 2. La hiérarchie organisationnelle permet-elle d'effectuer des contrôles de sécurité et d'accès ?
> 3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
> 4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)

Sur la base d'expériences pratiques dans différents pays, les scénarios de hiérarchie organisationnelle suivants peuvent être envisagés :

##### Cas 1 - Un ou plusieurs ASC travaillent dans des villages données (MAIS PAS dans d'autres villages). { #case-1-one-or-more-chw-work-in-specific-villages-but-not-in-other-villages }

> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissement \[L3\]
>           - Village \[L4\]
>               - ASC 1 \[L5 ou Entité Suivie\]
>               - ASC 2 \[L5 ou Entité Suivie\]
>           - Village \[L4\]
>               - ASC 3 \[L5 ou Entité Suivie\]
>               - ASC 4 \[L5 ou Entité Suivie\]

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Oui, les données peuvent être saisies au niveau de l'ASC [L5], qui n'est présent que dans un seul village [L4]. Cela signifie que les données ont été collectées par un Agent de Santé spécifique et qu'elles sont propres sans équivoque à un Village spécifique.*
2. La hiérarchie organisationnelle permet-elle d'effectuer des contrôles de sécurité et d'accès ?
*Oui, chaque ASC sera affecté à sa propre unité d'organisation, ce qui est le niveau le plus bas. Cela implique qu'il/elle ne pourra voir que les données qu'il/elle a lui-même/elle-même collectées.*
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Oui, l'agrégation à chaque niveau permettra d'accumuler des données au niveau des agents de santé, des villages, des établissements, des régions...*
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Oui, les données peuvent toujours être associées au niveau où elles ont été saisies, et dans ce cas, il s'agit de l'ASC.*

Oui, elle réussit le test.

**Si vous envisagez de représenter l'ASC comme une entité suivie** : Dans ce cas, les ASC pourraient être représentés comme des entités suivies si le programme l'exige. Cependant, cette méthode n'est pas recommandée lorsque les ASC sont également chargés de rendre compte d'un autre type d'entité suivie, tels que les cas de paludisme ou les ruptures de stock, qui doivent être associés aux ASC. Dans ce cas, l'ASC doit être représenté comme une unité organisationnelle.

Cette configuration est recommandée lorsque les ASC doivent être associés à une entité suivie.

> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissement \[L3\]
>           - Village \[L4\]
>               - ASC 1 \[L5\]
>                   - Cas de Paludisme \[Entité Suivie\]
>                   - Cas de Paludisme \[Entité Suivie\]


##### Cas 2 - L'ASC exerce dans plusieurs villages/communautés. Les ASC Ne partagent PAS les villages.{ #case-2-chw-works-in-several-villagescommunities-chws-do-not-share-villages } 

> - Pays\[L1\]
>   - Régions \[L2\]
>       - Etablissement \[L3\]
>           - ASC 1 \[L4\]
>               - Village A \[L5 ou Entité Suivie\]
>               - Village B \[L5 ou Entité Suivie\]
>           - ASC 2 \[L4\]
>               - Village C \[L5 ou Entité Suivie\]
>               - Village D \[L5 ou Entité Suivie\]


Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Oui, les données peuvent être saisies au niveau du village [L5], qui ne relève que d'un seul ASC [L4]. Cela signifie que les données ont été collectées dans un village spécifique et qu'elles sont sans équivoque la propriété d'un Agent de Santé spécifique.*
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Oui, chaque agent de santé sera affecté à sa propre unité d'organisation \[L4\], et pourra consulter les données qui appartiennent à cette unité d'organisation et à ses subordonnées \[L5\]. Dans ce cas, les subordonnées sont les Villages dans lesquels l'agent de santé travaille, et il/elle ne pourra donc accéder qu'aux données qu'il/elle a lui-même/elle-même collectées*.
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Oui, l'agrégation à chaque niveau permettra d'accumuler des données au niveau du village, de l'agent de santé, des établissements, des régions...*
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Oui, les données peuvent toujours être associées au niveau de l'Agent de Santé \[L4\].*

Oui, elle réussit le test sur le web ou Android, mais ne fonctionne pas avec la collecte de données par SMS.

**Si vous envisagez de représenter le village comme une entité suivie:** Des raisons programmatiques ou administratives peuvent expliquer le choix de représenter les villages comme des entités suivies, par exemple si la situation des villages change constamment en raison des migrations saisonnières de la population (raisons administratives) ou s'il est nécessaire de suivre les villages dans le cadre d'un programme de sensibilisation ou d'éducation (raisons programmatiques). Un problème se pose lorsque, par exemple, un patient d'un village doit également être suivi et associé au village par le biais d'une relation. Actuellement, DHIS2 n'est pas en mesure de faire des analyses d'entités suivies basées sur des relations entre deux types d'entités suivies différents. Par conséquent, il est recommandé que si les patients doivent être suivis et associés à un village, que le village reste une unité organisationnelle. Prenons l'exemple ci-dessous :

Cette configuration est recommandée lorsqu'un village doit être associé à une entité suivie.

> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissements \[L3\]
>           - ASC 1 \[L4\]
>               - Village A \[L5\]
>                   - Patient 1 \[Entité Suivie\]
>                   - Patient 2 \[Entité Suivie\]
>                   - Patient 3 \[Entité Suivie\]

##### Cas 3 - L'ASC exerce dans plus d'un village/communauté{ #case-3-chw-works-in-more-than-one-villagecommunity } 
> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissements\[L3\]
>           - Village A \[L4\]
>               - ASC 1 \[L5\]
>               - ASC 2 V-A \[L5\]
>           - Village B \[L4\]
>               - ASC 2 V-B \[L5\]
>               - ASC 3 \[L5\]

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Oui, les données peuvent être collectées au niveau de I'ASC \[L5\], qui dépend d'un ou de plusieurs villages \[L4\]. Cela signifie que les données ont été collectées par l'Agent de Santé spécifique et qu'elles appartiennent sans équivoque à un Village spécifique.*
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Oui, chaque ASC sera affecté à sa propre unité d'organisation, ce qui est le niveau le plus bas. Cela implique qu'il/elle ne pourra voir que les données qu'il/elle a lui-même/elle-même collectées.*
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Non, il est possible d'agréger les données par village, par établissement, par région... Cependant, en raison de la présence répétée des ASC dans différents villages (ASC 2 dans cet exemple), il est impossible d'agréger les données par ASC en suivant la hiérarchie*.
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Oui, les données peuvent toujours être associées au niveau de l'ASC \[L5\].*

Non, il ne réussit pas le test car l'activité des ASC ne peut pas être agrégée en raison de la répétition des noms. Pareil avec les opérations par SMS.

##### Cas 4 - Plusieurs ASC exercent dans un même village. { #case-4-multiple-chws-works-in-single-village } 

> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissements \[L3\]
>           - ASC 1 \[L4\]
>               - Village A AS1 \[L5\]
>               - Village B AS1 \[L5\]
>           - ASC 2 \[L4\]
>               - Village B AS2 \[L5\]

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Oui, les données peuvent être saisies au niveau du Village \[L5\], qui dépend uniquement de l'ASC \[L4\]. Cela signifie que les données ont été collectées dans un Village spécifique et qu'elles appartiennent sans équivoque à un Agent de Santé spécifique.*
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Oui, chaque ASC sera affecté à sa propre unité d'organisation \[L4\], et pourra consulter les données qui appartiennent à cette unité d'organisation et à ses subordonnées \[L5\]. Dans ce cas, les subordonnées sont les Villages dans lesquels l'agent de santé travaille, et il/elle ne pourra donc accéder qu'aux données qu'il/elle a lui-même/elle-même collectées*.
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Non, l'agrégation à chaque niveau permet d'accumuler des données relatives aux agents de santé, aux établissements, aux régions... mais il est impossible d'agréger les données par village en suivant la hiérarchie (voir le village B).*
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Oui, les données peuvent toujours être associées au niveau de l'Agent de Santé \[L4\].*

Non, il ne réussit pas le test. Les données des villages ne peuvent pas être agrégées. Pareil avec les opérations par SMS.

##### Cas 5 - L'ASC est assigné à un village en tant qu'utilisateur mais n'est pas représenté dans la hiérarchie. { #case-5-chw-is-assigned-to-a-village-as-a-user-but-not-represented-in-the-hierarchy }

> - Pays\[L1\]
>   - Régions \[L2\]
>       - Etablissement \[L3\]
>           - Village A \[L4\]
>           - Village B \[L4\]

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Les données peuvent être partiellement saisies au niveau du village \[L4\], mais il n'y a pas d'unité d'organisation en rapport avec l'Agent de Santé.*
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Partiellement, à condition que l'Agent de Santé soit autorisé à accéder à toutes les données du Village auquel il/elle est affecté(e).*
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Partiellement, à condition qu'il ne soit pas nécessaire de procéder à une agrégation par Agent de Santé. L'agrégation à chaque niveau permettra d'accumuler des données dans les villages, les établissements, les régions...*
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Non, l'ASC n'est pas présent dans la hiérarchie et nous ne pouvons pas filtrer les données par Agent de Santé en suivant la hiérarchie.*

Partiellement (3 premières questions mais pas 4). L'activité d'un seul ASC n'est pas défini dans la hiérarchie et ne pourra pas être consultée dans les analyses. Des analyses personnalisées pourraient être effectuées pour rendre cela possible, mais ces analyses nécessiteront développement et maintenance.

##### Cas 6 - Les données communautaires sont présentées sous forme agrégée au niveau de l'établissement ou à un niveau supérieur. { #case-6-community-data-is-submitted-as-aggregate-at-facility-or-higher-level }

> - Pays \[L1\]
>   - Régions \[L2\]
>       - Etablissements\[L3\] ← Données agrégées au niveau des villages

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Non, nous ne pouvons pas enregistrer de données au détriment de la communauté ou du village*.
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Non, toutes les données relatives aux villages et aux communautés seront accessibles à tous les utilisateurs assignés au niveau de l'établissement \[L3\]*
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Non, l'agrégation à chaque niveau commencera au niveau de l'établissement, il est impossible d'avoir des données agrégées par village ou par communauté*.
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Non, l'ASC n'est pas présent dans la hiérarchie et nous ne pouvons pas filtrer les données par Agent de Santé en suivant la hiérarchie.*

Non, il ne réussit pas le test. Les données d'une communauté ne peuvent pas être désagrégées.

##### Cas 7 - Représentation d'un ASC comme  Option de Catégorie { #case-7-representing-a-chw-as-category-option }

Dans les petits CHIS avec moins de 250 ASC, il est possible d'utiliser les ASC comme options de catégorie. Cette configuration réussira le test. Le graphique ci-dessous illustre comment cette option peut permettre d'associer un village à plusieurs ASC :

![](resources/images/chis_figure21.png)

*Figure 4.1:* Possibilités de relations lorsque les ASC sont représentés par des options de catégorie.

Réussit-t-il le test ?

1. Est-il possible de saisir les données en fonction d'une unité organisationnelle qui représente l'endroit et la personne à laquelle les données sont associées ?
*Oui, les données peuvent être saisies au niveau du village \[L4\] et il est possible de les relier à l'Agent de Santé en utilisant la Catégorie de l'Agent de Santé comme filtre.*
2. La hiérarchie organisationnelle permet-elle de mettre en place des contrôles de sécurité et d'accès ?
*Partiellement, si l'Agent de Santé est autorisé à accéder à toutes les données du Village auquel il/elle est affecté(e).*
3. L'agrégation produit-elle les résultats souhaités : indicateurs, analyses, tableaux de bord, cartes, etc.
*Oui, l'agrégation à chaque niveau permet d'accumuler les données dans les villages, les établissements, les régions... Les données peuvent être classées par Agent de Santé en utilisant la Catégorie comme filtre*.
4. Les données peuvent-elles être associées à un seul ASC ? (Pas nécessaire, mais vivement recommandé)
*Oui, les données sont liées à l'Agent de Santé par l'intermédiaire de l'Option de Catégorie sélectionnée lors de la Saisie des Données*.

Oui, il réussit le test. Cependant, **cette configuration ne peut pas être utilisée pour les grands CHIS qui utilisent un nombre important d'ASC**. Actuellement, elle n'est pas non plus activée pour la saisie de données par SMS ou Android sans une application personnalisée.

##### Nettoyage de la hiérarchie organisationnelle{ #keeping-the-organizational-hierarchy-clean } 

DHIS2 ne prend pas en charge plusieurs hiérarchies organisationnelles. Pour permettre l'exploration des données à grande échelle, chaque niveau doit représenter un seul type d'unité de rapport. Avoir différents types d'unités de rapport à un même niveau rend quasiment impossible toute analyse dans DHIS2. Par exemple :

> **Mauvais**
> 
> - Etablissement\[Niveau de l'unité d'organisation\]
>   - ASC 1 \[Niveau de l'unité d'organisation\]
>   - Village 1
>   - ASC 2
>   - Village 2
>   - Forage 1
>   - Forage 2
>   - Village 3
>   - Village 4
>   - Forage 3
>   - Forage 4
>   - Forage 5

> **Bon**
> 
> - Etablissement \[Niveau de l'unité d'organisation\]
>   - ASC 1 \[Niveau de l'unité d'organisation\]
>       - Village 1 \[Niveau de l'unité d'organisation\]
>           - Forage 1 \[Tracked Entity\]
>           -  Forage 2
>       - Village 2
>           -  Forage 3
>   - ASC 2
>       - Village 3
>           -  Forage 4
>           -  Forage 5
>       - Village 4

> **Avertissement**
>
> Si les ASC sont inclus dans la hiérarchie, la meilleure pratique consiste à nommer l'unité organisationnelle selon le poste et non selon le nom réel de l'ASC. Par exemple, si Peter Banda est un ASC travaillant dans l'Etablissement de Santé de Choma, son unité organisationnelle sera nommée "Ndola ASC 01" et non "Peter Banda CHW". Dans cet exemple, si Peter quitte son rôle d'ASC, un nouvel ASC peut être formé pour le remplacer et remplir l'unité organisationnelle Choma ASC 01. Si 20 % des ASC doivent être remplacés chaque année et que le nom de l'ASC correspond au nom de l'unité organisationnelle qu'il représente, alors 20 % de l'unité organisationnelle du CHIS devront être changés chaque année.

##### Echelle - Quelle est la taille maximale que peut avoir la hiérarchie ? { #scale-how-big-is-too-big-for-the-hierarchy }

Si les ASC ou les communautés prises individuellement sont inclus dans la hiérarchie et que le CHIS est étendu à l'échelle nationale, il est très probable que le CHIS/HMIS contienne des dizaines de milliers d'unités organisationnelles. Tant que les unités organisationnelles sont bien définies et organisées, il est tout à fait possible d'en avoir un très grand nombre. Par exemple, le CHIS de Zambie contient près de 45 000 unités organisationnelles représentant tous les villages du pays.

Pour gérer les nombreuses conditions présentées ci-dessus, les ASC peuvent être définis comme unités organisationnelles dans DHIS2 ou comme utilisateurs de ces unités organisationnelles. Dans chaque cas, il convient d'examiner et d'évaluer toute la hiérarchie organisationnelle du pays ou du projet, afin de s'assurer que la hiérarchie est raisonnable et qu'elle ne dépasse pas généralement  7 à 8 niveaux.

#### Programme de santé vertical par rapport au HMIS{ #vertical-health-program-vis-a-vis-hmis }

Lorsque les ASC sont invités à rendre compte des données spécifiques à un programme de santé (paludisme, VIH, habitudes alimentaires des nourrissons, conseils sur la contraception, etc.) et que ces données doivent être incluses dans le système de rapport de l'établissement/le HMIS de routine, des ajouts doivent être effectués dans l'ensemble de données de l'établissement qui figure dans le DHIS2.

#### Rapports sur les partenaires { #partner-reporting } 

Lorsque les ASC sont invités à rendre compte de projets spécifiques menés par un partenaire (et non du système d'information sanitaire de routine de l'établissement), il convient de définir et de suivre les ensembles et flux de données spécifiques du projet, lesquels seront indépendants du système d'information sanitaire de routine.

#### Résultats : Interne et externe{ #outputs-internal-and-external } 

[Tableaux de bord, visualisations, rapports internes, rapports des donateurs, rapports d'autres agences]{.ul} - Résultats et analyses attendus du système constituent l'un des éléments fondamentaux de la conception du CHIS. Bien que cette règle s'applique généralement à la conception de tous les systèmes d'information à tous les niveaux, elle revêt une importance cruciale dans un CHIS lorsque la portée des données est considérable et a des implications immédiates sur la charge de travail d'un ASC.

#### Considérations relatives aux infrastructures{ #infrastructure-considerations } 

- **Infrastructure de base et hébergement - DHIS local vs sur le Cloud:** Dimensionnement - L'hébergement du serveur devient crucial pour un CHIS si l'on veut réaliser des rapports mobiles par SMS. Les rapports par SMS ne fonctionneront pas si le serveur est hébergé sur un cloud hors du pays, car une messagerie internationale sera requise. Le serveur doit donc être hébergé dans le pays concerné par les opérations.
- **Configuration et maintenance de la passerelle SMS:** Pour que les rapports par SMS soient possibles, l'intégration avec la passerelle SMS est une condition essentielle. Les fournisseurs de passerelles locaux ou nationaux doivent être contactés et les API vérifiées pour que l'intégration soit possible.
- **Gratuit vs payé par l'utilisateur:** Si les SMS sont gratuits pour l'expéditeur/l'ASC, l'intégration nécessite un fournisseur de services mobiles ou un fournisseur de services de passerelle avec un abonnement gratuit. Dans ce cas, le coût doit être pris en charge par le ministère de la santé au niveau central et le service doit être fourni gratuitement aux ASC.
- **Gestion du temps de communication et remboursement des agents:** Lorsqu'un système de rapport mobile est utilisé par les ASC (SMS ou Internet), l'utilisation et la gestion du temps de communication doivent être prises en compte pour ce type de rapport. Un système efficace de remboursement des ASC doit être défini, car si les ASC ne reçoivent pas l'argent à temps pour compenser leurs dépenses, ils pourraient être réticents à l'utilisation du téléphone.
- **Evaluation de la connectivité du réseau et de l'alimentation électrique:** Lors de la mise en place d'un système de rapport pour des ASC qui utilisent des téléphones mobiles, une évaluation de la couverture du réseau doit être envisagée, en particulier dans les zones rurales et les zones frontalières. Les horaires de connexion à Internet varient souvent et doivent être pris en compte dans la définition des routines de transmission des rapports. Les ASC font souvent face à une fourniture d'électricité intermittente ; ce qui les empêche de transmettre leurs rapports et de recharger leurs téléphones et autres appareils.
- **Propriété et utilisation des appareils :**
    - Dès la remise des appareils (téléphones, tablettes, etc.) aux ASC, il est important de se convenir sur la "propriété" des appareils ainsi que les responsabilités en matière de maintenance, d'entretien et de perte. Il y a souvent confusion sur la question de savoir si l'appareil appartient à l'institution ou à l'individu, et quelles responsabilités incombent à chacun.
    - Toutefois, s'il est prévu que les ASC utilisent des appareils personnels pour effectuer des rapports, il est d'autant plus important de clarifier les aspects relatifs au coût du temps de communication/des données, ainsi que le mécanisme de remboursement.

#### Aspects technologiques à prendre en compte pour l'acquisition des données, c'est-à-dire la sélection d'outils { #technology-considerations-for-data-acquisition-ie-tool-selection }

| | **Papier** | **SMS/USSD** | **Téléphones simples** | **Smartphones** | **Intégration d'un tierce partie** | **Ordinateurs** |
|:- |:- |:- |:- |:- |:- |:- |
| **Quand l'utiliser** | Toujours une option, surtout lorsque la numérisation des données n'est pas une priorité | Lorsque la numérisation des données à la source est une priorité, la quantité de données à rapporter est très faible, l'internet mobile n'est pas disponible ou la mise à disposition de téléphones n'est pas possible. | Lorsque la numérisation des données à la source est une priorité, la quantité de données à rapporter est plus élevée, les ASC éprouvent des difficultés à utiliser les smartphones et l'Internet mobile est disponible | Lorsque la numérisation des données à la source est une priorité, la quantité de données à rapporter est considérable, l'internet mobile est disponible et les ASC peuvent utiliser des smartphones. | Lorsque la numérisation des données à la source est une priorité et qu'une solution de collecte de données est mise en place | La numérisation des données se fait en fonction de la disponibilité des ordinateurs |
| **Extensibilité** (géographie, service, utilisateurs, domaines) | Extensible aux trois éléments | Techniquement facile à étendre, mais la formation des utilisateurs sera nécessaire lors de l'ajout de nouveaux éléments | Facilement extensible en termes de géographie et de nombre d'utilisateurs, mais les exigences croissantes en matière de déclaration des données ne pourront pas être prises en charge | Facilement extensible en termes de géographie et de nombre d'utilisateurs. Les exigences croissantes en matière de déclaration des données pourront également être prises en charge | La gestion de l'intégration est une tâche permanente ; l'extension du nombre d'utilisateurs est la plus simple à réaliser, tandis que celle des services et des domaines devra être développée dans l'approche d'intégration | Facilement extensible aux 3 niveaux |
| **Granularité des données** | Concevable pour une désagrégation plus poussée | Déconseillé pour les données très désagrégées ou les longs formulaires | Déconseillé pour les données très désagrégées ou les programmes de tracker avec plusieurs étapes. | Concevable pour des programmes de désagrégation plus poussée et des programmes de tracker complexes. | L'approche d'intégration doit être intégrée à toutes les collectes, quelque soient les éléments concernés | Concevable pour une désagrégation plus poussée |
| **Durabilité** (coût initial, coût continu) | Impression initiale et continue ; Coût de la formation | Solution peu coûteuse ; mais en cas de volume extrêmement élevé de SMS, les coûts peuvent devenir considérables ; la formation représente un coût ; inciter l'ASC à produire des rapports. | Coût de la formation initiale et continue ; Approvisionnement; coûts d'Internet continus ; Inciter l'ASC à produire des rapports. | Coût de la formation initiale et continue ; Approvisionnement; coûts d'Internet continus ; Inciter l'ASC à produire des rapports. | L'intégration de systèmes présente un coup élevé | Frais de formation initiale; Maintenance du matériel en continue  |
| **Capacité humaine** | Nécessite une formation sur les formulaires et la logique des formulaires par rapport aux registres | Nécessite une formation sur les formulaires et la logique des SMS. Certains problèmes importants peuvent survenir avec des messages abrégés pour les SMS et des erreurs de délai d'attente pour l'USSD. | Nécessite une formation sur les formulaires et sur la déclaration des données à l'aide de l'application. Les ASC doivent être en mesure de résoudre les problèmes élémentaires liés aux applications et au téléphone | Nécessite une formation sur les formulaires et sur la déclaration des données à l'aide de l'application. Les ASC doivent être en mesure de résoudre les problèmes élémentaires liés aux applications et au téléphone | La formation des ASC n'est pas nécessaire, car l'intégration se fait au niveau du serveur | Formation sur les formulaires : Formation sur la logique des formulaires par rapport aux registres |

*Figure 4.3:* Conceptualisation de l'acquisition de données

#### Sécurité { #security } 

DHIS2 est fondamentalement un logiciel très sûr. De plus, beaucoup de pays disposent de législations strictes en matière de sécurité des données, surtout en ce qui concerne les données des patients. Assurez-vous de connaître toutes les lois et politiques nationales relatives à la sécurité des données avant de développer un CHIS dans DHIS2. Pour ce qui est de l'application du CHIS dans DHIS2, plusieurs éléments sont à prendre en compte :

- Si les ASC suivent des patients à titre individuel, assurez-vous que les ASC ne puissent voir que les patients qui leur sont assignés.
- Assurez-vous que les utilisateurs ne puissent avoir accès qu'aux données qui s'appliquent à leur rôle, leurs actions et leurs décisions. Les utilisateurs ne doivent pas avoir accès à plus de données que ce dont ils ont besoin.
- L'accès aux données doit toujours être protégé par au moins un niveau de contrôle d'accès (par exemple, un mot de passe, un code PIN, etc.). "Déverrouiller" un appareil mobile par simple balayage n'est pas considéré comme un contrôle d'accès.
- L'interception de données non cryptées via des signaux mobiles est possible par SMS, USSD et J2ME. Des mesures préventives peuvent être mises en place. Veuillez contacter l'équipe principale du DHIS2 pour plus d'informations.
- Les serveurs doivent se trouver dans un environnement sûr.
- Les utilisateurs ne doivent pas avoir plus d'accès aux applications ou aux fonctionnalités du DHIS2 que ce qui est nécessaire en fonction des rôles qu'ils occupent.
- Les paramètres de partage et de confidentialité dans DHIS2 peuvent augmenter considérablement la sécurité, mais doivent être gérés avec soin. Pour plus d'informations, veuillez consulter le manuel d'utilisation du DHIS2.

### 3. Développer des maquettes et des prototypes de résultats d'analyses (mécanismes de retour d'information) { #3-develop-mock-ups-and-prototypes-of-analytics-outputs-feedback-mechanisms }

Tous les systèmes d'information doivent être conçus pour l'utilisation des données. Avant d'entamer la construction d'un bâtiment, l'architecte doit savoir exactement ce à quoi il ressemblera et quelles seront ses caractéristiques, en réalisant un plan et une maquette ou un prototype. De même, pour un CHIS, avant la configuration du système, toutes les analyses des parties prenantes, les mécanismes de retour d'information et les tableaux de bord doivent être conçus et disposer de maquettes et de prototypes.

Le chapitre 2 présente le process d'identification des parties prenantes et le chapitre 3 traite du process de sélection des mécanismes de retour d'information pour les parties prenantes. À présent que vous connaissez le cadre d'utilisation des données (qui a besoin de données et comment elles doivent être présentées), la dernière étape consiste à créer des maquettes et des prototypes de ce à quoi ressembleront réellement ces mécanismes de retour d'information.

Une maquette est un modèle réduit de ce à quoi ressemblent les mécanismes de retour d'information. Par exemple, vous trouverez ci-dessous une maquette d'un tableau de bord ICCM de district. Cette maquette a été développée avant la configuration de la base de données.

*Figure 4.4:* Prototype d'un tableau de bord de district pour un CHIS![](resources/images/chis_figure22.jpg)


La maquette est ensuite utilisée pour :

- S'assurer que tous les éléments de données et indicateurs dont ont besoin les parties prenantes soient inclus dans le système.
- Tous les indicateurs peuvent apparaître dans les analyses présentées, en tenant compte du degré de granularité de ces analyses. Par exemple, la maquette des diagrammes à barres ci-dessus représente les comptages hebdomadaires au niveau du poste de santé communautaire (PSC). Cela signifie que nous sommes en mesure de calculer ces indicateurs à partir des données dont nous disposons, à la fréquence souhaitée (hebdomadaire) au niveau du PSC. En revanche, si les éléments de données dont nous disposons ne permettent à générer cet indicateur que sur une base mensuelle au niveau de l'établissement, nous ne serions pas en mesure de calculer l'indicateur à un niveau de granularité suffisant pour répondre aux besoins (hebdomadaire et au niveau du PSC).
- Guider le développement actuel des mécanismes d'analyse et de retour d'information en direct.

### 4. Dessin du flux de données CHIS dans DHIS2{ #4-drawing-chis-data-flow-in-dhis2 }

Ce processus vise à :

1. Développer une idée claire du CHIS souhaité dans DHIS2
2. Formuler les voies et moyens permettant d'harmoniser les flux de données existants parallèles ou redondants
3. Résoudre les problèmes de lourdeur et d'imprécision liés aux procédures opérationnelles normalisées.
4. Formuler les voies et moyens permettant de rassembler plusieurs hiérarchies de rapports de données en une seule.
5. Identifier les outils de travail ou d'assistance qui pourraient être intégrés aux outils de collecte de données de DHIS2.
6. Développer un nouveau diagramme/wireframe de flux de données

### 5. Élaboration de Directives pour la Déclaration de données{ #5-developing-reporting-guidelines }

Les chapitres consacrés à l'évaluation et à la conception du système définissent clairement le flux de données du début à la fin. Pour élaborer des directives relatives à la collecte des données, commencez par le premier événement du flux de données et progressez vers le haut en incluant tous les événements, qu'ils utilisent du papier, des applications mobiles ou des ordinateurs. **Pour chaque point où les données sont collectées ou transmises, il convient de définir le processus exact et les responsabilités relatives à la manière dont cet événement est réalisé**.

Pour chaque étape du flux de données, définissez chaque événement au format illustré au niveau de la Figure 4.4.

------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| **Manifestation** | ***Nom de l'événement*** |
| :- | :- |
| Ensemble(s) de données/outil(s) de déclaration des données |  Le nom de l'ensemble de données ou des outils de déclaration des données |
| Modalité de transmission ou de saisie |  Nommez l'application utilisée et l'appareil sur lequel il est utilisé ou décrivez la trace écrite de la saisie des données. (Retirez cette option si l'événement est uniquement une collecte de données et non une transmission ou une saisie dans DHIS2) |
| Responsable |  Il s'agit de la personne/rôle responsable de la réalisation de cet événement. |
| Périodicité |  Fréquence à laquelle cet événement se produit. Par exemple, "mensuel", "hebdomadaire" ou "trimestriel |
| Date limite de l'événement |  Moment où l'événement doit être terminé. Par exemple, "Le 10 du mois en cours", "A 17h00 le mardi de la semaine en cours" ou "Le 5 du premier mois du prochain trimestre". |
| Transmission des données ou élément incitatif à la saisie des données |  Qu'est-ce qui incite à la déclaration des données et comment l'élément incitatif est-il offert ? (le cas échéant) |
| Contrôles de la qualité des données effectués |  Décrivez les contrôles effectuées dans le cadre de cet événement. Cela n'inclut pas les contrôles de qualité effectués après la transmission des données. |
| Accès aux outils de déclaration des données | Comment les outils de déclaration de données utilisés (par exemple les registres, les formulaires de déclaration, les applications, les téléphones, etc.) sont-ils stockés, consultés et réapprovisionnés ? |
| Récit |  Le récit décrit l'événement dans un texte long. Il est très spécifique. Il peut inclure des bonnes pratiques, des instructions pour le remplissage des registres papier, des instructions pour la commande ou la création de nouveaux registres, des instructions pour l'utilisation des téléphones portables, etc. Examinez la situation de manière pratique et identifiez ce qui pourrait constituer des entraves à la transmission des données. |

*Figure 4.5:* Procédures opératoires standard (SOPs) pour la Saisie des données

#### Questions récurrentes sur les directives relatives à la collecte de données { #frequent-questions-on-data-capture-guidelines }

Que se passe-t-il si mon CHIS dispose d'une trace écrite allant des ASC ou de la communauté à l'établissement ou au district ?

Certains CHIS ne prévoient pas de transmission de données au niveau des ASC ou des communautés. Dans ce cas, les dossiers papier ou les registres sont produits au niveau de la communauté, puis transportés physiquement vers les établissements ou les niveaux supérieurs. Il est important que le protocole couvre *toutes* les activités du CHIS, même s'il s'agit de documents papier, car le respect des délais et la qualité d'une étape de transmission de données ont un impact direct sur le succès de l'étape suivante.

Les directives relatives à la collecte de données peuvent-elles être élaborées compte tenu des rôles des utilisateurs du CHIS ?

Oui. Vous êtes peut-être plus habitué à des PON basées sur les rôles programmatiques, alors que ces directives sur la collecte des données sont basées sur le flux de données. Beaucoup de pays et de programmes intègrent les directives relatives à la collecte des données dans un PON programmatique plus large, organisé en fonction des rôles/titres des parties prenantes (par exemple, ASC, superviseur des ASC, responsable de la santé au niveau du district, etc.) Les directives sur la collecte des données peuvent être incorporées dans ce format à condition que chaque événement effectué par la partie prenante soit suffisamment détaillé.

Que se passe-t-il si dans mon CHIS, des registres de patients dématérialisés sont utilisés au niveau des ASC ?

Dans certains CHIS, les ASC peuvent suivre des patients à titre individuel d'une manière totalement dématérialisée via l'application DHIS2 tracker ou une application similaire sur un téléphone Android ou un simple téléphone mobile. Dans ce cas, il n'y aura pas de registre papier où les informations sont consignées initialement ni de production de rapports périodiques agrégés. Dans ces cas, il est généralement préférable de considérer l'interaction entre le patient et l'ASC et la collecte des données du patient comme un événement unique à inclure dans les directives relatives à la collecte des données. Gardez ces facteurs à l'esprit :

- Dans certains cas, l'utilisation du tracker augmente de manière significative la charge de travail de l'ASC en matière de déclaration de données. Ainsi, dans les contextes où le nombre de patients est élevé, le tracker peut s'avérer très contraignant. Cependant, s'il est configuré comme un outil d'aide à l'ASC qui utilise les règles du programme et la skip logic (logique de saut) de l'application de tracker, il peut réduire la charge de travail en matière de déclaration de données, augmenter la qualité des données et soutenir les prestations de l'ASC.
- Le tracker fournira des données beaucoup plus granulaires et s'est avéré approprié au niveau communautaire dans l'élimination des maladies, le contrôle des épidémies, l'élargissement des programmes de vaccination, le suivi de l'orientation et le suivi des nouveau-nés.
- Au niveau communautaire, le tracker ne devrait être utilisé qu'en cas d'action ciblée qui nécessite des données provenant d'une seule entité suivie. La réponse spécifique à ces données doit également être définie dans les directives de collecte de données.

### 6. Développement d'un dictionnaire de métadonnées du CHIS { #6-develop-chis-meta-data-dictionary }

Un dictionnaire de métadonnées est utilisé pour décrire tous les attributs de métadonnées. Il permet aux utilisateurs et aux administrateurs du système de comprendre la signification et l'objectif de chaque élément de métadonnées.

### 7. Configuration de DHIS2 { #7-perform-dhis2-configuration }

Dernière étape après la constitution d'un dictionnaire de métadonnées pour configurer le système DHIS2. Les directives étape par étape pour la configuration de DHIS2 ont été bien documentées et sont disponibles sur le site Web de DHIS2 ([[www.dhis2.org/documentation]{.ul}](http://www.dhis2.org/documentation)).

### 8. Alimentation du prototype de base de données et test{ #8-populate-prototype-database-and-test }

Il est essentiel de tester minutieusement un CHIS avant de le déployer. Les tests visent plusieurs objectifs :

- Tester le calcul des indicateurs - les données simulées ou acquises doivent être importées dans le prototype de base de données afin de tester la pertinence de tous les calculs d'indicateurs.
- Approbation des utilisateurs (analyses) - pour tester l'acceptation par toutes les parties prenantes de l'expérience utilisateur des analyses, des tableaux de bord et des mécanismes de retour d'information.
- Approbation des utilisateurs (saisie des données) - pour tester si toutes les parties prenantes effectuant la saisie de données sont satisfaites de l'expérience utilisateur de la saisie de données. Il est également nécessaire de tester si la skip logic (logique de saut), les validations, les alertes, la l'assistance à la tâche ou les outils d'aide fonctionnent et si les utilisateurs sont satisfaits.
- Identification et signalement des bugs. Pratiquement toutes les nouvelles bases de données présentent des défauts ou des bugs. Si vous testez minutieusement votre base de données, la plupart de ces bugs seront détectés. La meilleure approche consiste à résoudre tous les bugs avant de déployer votre CHIS à grande échelle. Les bugs peuvent être signalés dans DHIS2 JIRA ([[http://jira.dhis2.org]{.ul}](http://jira.dhis2.org))

> Important
> 
> **Disposer d'une base de données "bac à sable" pour les tests**
> Vous devez disposer d'une copie de votre base de données de production, que vous utiliserez pour effectuer vos tests. Toute modification apportée à votre base de données de production doit d'abord être testée dans votre "bac à sable" avant d'être appliquée à votre base de données de production.

> Important
>
> **Mises à jour des versions du DHIS2**
> Restez informé sur les versions de DHIS2. Une nouvelle version de DHIS2 est publiée tous les quatre mois. Généralement, il est recommandé d'avoir une ou deux versions de retard par rapport aux versions les plus récentes. Si vous ne suivez pas l'évolution des versions, vous pouvez avoir du mal à trouver des personnes pour vous aider à utiliser votre version de DHIS2 lorsque vous rencontrerez de sérieux problèmes. Les mises à jour doivent être planifiées bien à l'avance. Le procédé de test décrit ici pour une nouvelle base de données peut être utilisé pour d'une mise à jour. Gardez à l'esprit que la mise à jour d'une grande base de données de production s'accompagne très souvent de la panne ou de l'arrêt d'un élément du système. Voilà pourquoi vous devez planifier et effectuer des tests minutieux avant de procéder à la mise à jour.

### 9. Déploiement { #9-deploy }

Le CHIS peut être déployé de différentes manières. La stratégie de déploiement dépend de nombreux éléments tels que la stratégie de formation, la portée du CHIS, etc. En général, il existe deux stratégies de déploiement : le "Big Bang" et le déploiement progressif. Ces deux stratégies nécessitent pratiquement la même quantité de ressources.

1. Le "Big Bang" - Cette stratégie de déploiement est souvent utilisée dans des situations où le développement, les tests et la formation initiale des utilisateurs peuvent ou doivent être effectués rapidement. Il s'agit généralement d'un CHIS de petite envergure sur lequel travaille au départ un important personnel d'assistance à l'implémentation. Cette stratégie est privilégiée dans les situations de crise nécessitant une réaction rapide, comme lors d'une épidémie où les données communautaires sont nécessaires au contrôle de l'épidémie. Étant donné que cette stratégie est employée dans la précipitation, des problèmes techniques seront certainement identifiés après le déploiement, lesquels problèmes pourraient entraver l'utilisation du système.
2. Déploiement progressif - Il s'agit de l'approche la plus courante pour le déploiement du CHIS, qui s'effectue région par région. En fonction de la portée du CHIS, cette stratégie peut nécessiter plusieurs années, mais elle permet d'obtenir un CHIS beaucoup plus stable et bien testé.

## Assistance technique à plusieurs niveaux du CHIS { #tiered-technical-support-to-chiss }

Pour fournir une assistance au CHIS, l'unité technique centrale doit être en mesure de recueillir, de cataloguer et de traiter toutes les demandes d'assistance, les erreurs et les défauts du système (également connus sous le nom de " bugs "). Dans la plupart des importants systèmes d'information, un système d'assistance à plusieurs niveaux est nécessaire. "A plusieurs niveaux" signifie que les problèmes mineurs peuvent être traités par les superviseurs de niveau inférieur et que les problèmes plus difficiles ou plus complexes sont transférés vers les niveaux supérieurs jusqu'à ce qu'ils parviennent à la personne capable de les résoudre. Vous trouverez ci-dessous un modèle de système d'assistance à plusieurs niveaux du CHIS, accompagné d'un exemple de problème que chaque niveau est censé traiter.

![](resources/images/chis_figure23.png)

*Figure 4.6*: Modèle d'un système d'assistance à plusieurs niveaux du CHIS

La plupart des problèmes qui nécessitent une assistance sont des problèmes mineurs pouvant être résolus au premier niveau d'assistance. Ce premier niveau est souvent celui des superviseurs directs des ASC. Ce premier niveau devrait être en mesure de résoudre les problèmes mineurs liés au matériel et aux logiciels. Lorsque les superviseurs de l'ASC ne parviennent pas à résoudre le problème, celui-ci doit être transféré à un niveau supérieur.

Les demandes de niveau 2 sont souvent traitées par les responsables des systèmes d'information au niveau des districts ou au niveau infranational, qui sont formés pour gérer les problèmes de configuration du système et tous les problèmes complexes liés à l'interface utilisateur, à l'importation et à l'exportation de données.

Les demandes de niveau 3 sont généralement traitées par les responsables de l'assistance informatique au niveau central. Ils doivent être en mesure de répondre à toutes les demandes de maintenance du back-end.

Les pays dotés d'un CHIS de très grande portée auront plus de trois niveaux. En revanche, les programmes plus petits peuvent en avoir moins. Quel que soit le nombre de niveaux, il est essentiel que les demandes d'assistance puissent être soumises par n'importe quel utilisateur directement via son instance DHIS2, par téléphone ou par e-mail. En utilisant l'application de messagerie, l'utilisateur peut envoyer un message au groupe d'utilisateurs "Central Technical Support" (Assistance technique centrale) pour son groupe d'assistance technique infranational, en fonction de la configuration des niveaux. Le groupe d'utilisateurs " Technical Support " (Assistance technique) est généralement composé de techniciens du niveau central. De même, ils peuvent contacter directement l'équipe technique par téléphone ou par e-mail. Une fois qu'une demande d'assistance a été envoyée à l'équipe technique, cette dernière doit accuser réception de la demande dans un délai court, maximum 12 heures.

*Bonne Pratique*

Il est nécessaire de disposer d'une ligne téléphonique d'assistance technique 24 heures sur 24 et d'un service d'assistance pour les utilisateurs du DHIS2, géré par le personnel d'assistance du HMIS central. Lorsque les utilisateurs du système rencontrent des difficultés dans son utilisation, s'ils ont l'impression de ne pas pouvoir bénéficier d'une assistance technique, ils risquent en fin de compte de ne plus l'utiliser. Une ligne téléphonique d'assistance technique gratuite et un service d'assistance fonctionnant 24 heures sur 24 peuvent donner aux utilisateurs le sentiment d'être soutenus et de pouvoir résoudre les problèmes à la volée. De plus, les utilisateurs du CHIS qui disposent d'un ordinateur peuvent utiliser la messagerie du DHIS2 pour envoyer des demandes d'assistance au groupe d'utilisateurs du service d'assistance. Vous trouverez ci-dessous un exemple du guide de l'Afrique du Sud sur l'utilisation de son service d'assistance intégré à DHIS2 messenger.

![](resources/images/chis_figure24.png)
![](resources/images/chis_figure25.png)


## Quelques directives de conception pour un CHIS plus durable { #some-design-guidelines-for-more-sustainable-chis }

Cette section présente quelques directives de conception pour développer des CHIS plus durables. Un thème récurrent dans ces directives est notre effort pour passer d'une approche axée sur l'offre à une approche axée sur la demande, centrée sur l'humain et visant à réduire la charge de travail des ASC en matière de collecte de données et à ajouter de la valeur à leur travail quotidien. Ces directives de conception sont entre autres :

1. Développer le CHIS selon une démarche de conception participative
2. Avoir une approche architecturale de la conception au cœur du projet
3. Concevoir le CHIS sur la base d'un cadre global de gouvernance et de normes de données
4. Concevoir le CHIS de manière à soutenir l'action locale plutôt que de permettre un contrôle et un surveillance accrus depuis le sommet hiérarchique
5. Développer le CHIS en tenant compte de l'infrastructure existante, qui doit nécessairement être de nature hybride
6. Planifier une évolution progressive des systèmes et éviter de concevoir des systèmes sur la base d'une approche à la "table rase"

Ces directives vont être traitées plus en détail.

### Approche de conception participative { #participatory-design-approach }

Une approche de conception participative suppose que les utilisateurs finaux ne sont pas simplement des fournisseurs passifs de données et des destinataires de systèmes "conçus de toutes pièces", mais qu'ils participent activement à leur co-construction avec les équipes de conception et de développement. Si, traditionnellement, diverses techniques ont été décrites pour permettre une conception participative (récits, groupes de discussion, entretiens, maquettes, etc.), ces techniques ont été développées en partant d'un principe de colocalisation, de systèmes uniques, utilisés en grande partie dans des contextes organisationnels uniques. Cependant, les différents contextes des CHIS en termes de portée, d'expérience préalable de l'informatisation, de niveaux d'alphabétisation et d'extrême diversité, exigent que ces techniques soient adaptées et étendues avec délicatesse et intelligence.

L'avènement des systèmes basés sur le web crée une distance géographique et culturelle accrue entre les concepteurs et les développeurs de systèmes et les utilisateurs, ce qui rend encore plus difficile l'utilisation des techniques traditionnelles de conception participative. Pour être efficaces, les méthodes de conception participative doivent être adaptées au contexte actuel, ce qui peut impliquer l'utilisation de méthodes en ligne couplées à d'autres moyens locaux. Bien évidemment, c'est plus facile à dire qu'à faire, compte tenu de certains défis évoqués, mais cette démarche doit faire partie intégrante du processus de planification des projets.

> **Exemple**
>
> **Étude de cas : Conception participative en Inde**
> Un projet HISP en cours en zone rurale en Inde vise à mettre en place des systèmes centrés sur le patient pour les soins de santé primaires. Ce projet est le fruit d'une collaboration entre l'équipe HISP de l'université d'Oslo et de l'Inde, et une équipe de santé publique du Post Graduate Institute of Medical Education Research (PGIMER), à Chandigarh, en Inde. Cette collaboration a permis de réunir l'expertise multidisciplinaire nécessaire à la conception du système
> 
> Pour garantir la participation active des ASC, un "laboratoire vivant" (recherche participative) a été mis en place dans une clinique rurale, zone d'étude désignée par le PGIMER. Le laboratoire vivant est devenu un lieu où l'équipe chargée de l'étude de conception travaille avec les ASC et les médecins pour comprendre les défis auxquels ils sont confrontés ainsi que leurs besoins quotidiens. Etant donné que le laboratoire vivant est installé dans la clinique, les ASC ont pu s'approprier le système en se sentant intégré à son processus d'évolution, et les deux parties ont pu s'échanger leurs points de vue. L'équipe de développeurs a pu s'imprégner de l'environnement de travail des des ASC, ce qui n'aurait pas été possible avec les approches de conception traditionnelles.
>
> Par exemple, au cours d'une discussion, les ASC ont demandé à ce que le système génère des registres primaires. L'idée était nouvelle, car l'approche habituelle considérait les registres primaires comme une évidence et commençait la conception en se basant sur les formats de collecte de données existants. Cette idée a permis de structurer la conception du système d'une nouvelle manière ; et le système, une fois achevé, a apporté plus de valeurs et donné une plus grande satisfaction professionnelle aux ASC. 

De ce passage, il faut retenir la nécessité de développer des approches de conception dans un contexte qui reflète l'environnement de travail des ASC. Le laboratoire vivant est l'une de ces approches, et il y en aura certainement d'autres. Dans différents contextes, des approches appropriées devront être élaborées pour permettre la mise en œuvre de ces processus de conception contextualisée.

### Approche architecturale de la conception au cœur du projet{ #architectural-thinking-at-the-core-of-design }

En termes simples, l'approche architecturale suppose une approche systémique et holistique qui vise à garantir que les différents systèmes existants puissent " communiquer entre eux " d'une manière relativement transparente. Cette communication entre systèmes ne se limite pas à un défi technique nécessitant des solutions techniques. Elle s'applique également à des exigences institutionnels complexes qui visent la création d'un canal de communication entre les programmes et les personnels de santé. Il s'agit sans aucun doute d'un défi plus important que la mise en œuvre de solutions techniques, et qui doit être traité comme une priorité.

Une autre caractéristique de l'approche architecturale est de considérer le développement du système comme une approche à long terme et évolutive, avec des décisions qui ne doivent pas être prises sur la base de considérations statiques et ponctuelles. Il s'agit donc de ne pas prendre des décisions à un moment donné qui vous empêcheront d'opérer d'autres choix à l'avenir ; des choix qui pourraient être disponibles et préférables.

Par exemple, la décision d'utiliser une plateforme propriétaire peut vous empêcher de développer une interopérabilité avec d'autres systèmes à l'avenir. Cela nécessite une approche prospective, qui cherche à anticiper les besoins futurs en matière d'information, et à être en phase avec les tendances technologiques et les nouvelles opportunités qui se présenteront à l'avenir. La conception du système doit nous permettre de relever ces défis et de tirer parti des opportunités qui se présenteront.

> **Exemple**
> 
> **Étude de cas : Conception collaborative dans un laboratoire vivant**
>
> Prenant un autre exemple du projet de laboratoire vivant, un des points de départ de sa conception a été de comprendre les différents systèmes utilisés par les ASC.
>
> Les ASC travaillaient avec 9 systèmes différents (informatiques et papier) composés de 22 registres primaires et de 30 rapports mensuels, avec beaucoup de chevauchements et de redondances entre eux. Un mapping des redondances a permis de répertorier tous les éléments de données de ces registres, d'identifier les doublons présents et de créer une liste consolidée de tous les éléments de données non répétés. Cette liste a ensuite été utilisée pour élaborer les définitions de métadonnées qui seront personnalisées dans la base de données du DHIS2. De plus, ces métadonnées ont été adaptées au MDDS (Metadata and Data Standards) national pour garantir leur évolutivité. De cette manière, des liens ont été établis entre les différents systèmes, garantissant ainsi une coordination lors de la collecte des données. Cela a ensuite permis de générer les registres primaires, principale préoccupation des ASC.
> 
> Ce processus a été mené conjointement par les ASC et les concepteurs du système. Travailler en équipe leur a permis d'identifier les éléments non désirés ou inutilisés, ce qui n'aurait pas été possible si les concepteurs avaient opéré seuls. Ce processus a également permis de garantir que le CHIS conçu soit intégré au travail quotidien des ASC, et visait principalement à apporter une valeur ajoutée aux ASC en réduisant leur charge de travail. En outre, il a été conçu pour être étendu à l'avenir, par exemple par un alignement sur les normes nationales en termes de production des rapports requis, pour une remontée d'informations et un soutien à l'action locale.

Un point important à retenir de ce passage est que la conception d'un système ne se limite pas à l'élaboration de solutions techniques, mais qu'elle doit être intégrée au travail quotidien des ASC et aux outils qu'ils utilisent.

### Conception pour Soutenir l'Action Locale { #design-to-support-local-action }

L'action locale fait référence à tout le travail effectué par l'ASC. Elle inclut toutes les tâches relatives à l'information, lesquels concernent les fonctions d'enregistrement, d'établissement de rapports et de suivi exercées par les ASC. L'action locale représente l'enregistrement et l'établissement de rapports par l'ASC, ainsi que l'analyse locale des données et la prise de mesures en vue d'améliorer la prestation des services de santé. Bien que l'analyse soit un aspect important du travail des ASC, et que nous cherchions à la renforcer, nous ne devons pas perdre de vue les fonctions d'enregistrement et d'établissement de rapports que les ASC sont tenus d'accomplir. Il serait injuste d'attendre d'un ASC qu'il améliore sa fonction d'action, tout en ignorant ses fonctions d'enregistrement et d'établissement de rapports, car il sera réprimandé par ses aînés.

Un aspect important du processus de conception est de comprendre ce que les ASC considèrent comme étant une action locale pertinente ( qui couvre leurs trois fonctions principales), et les résultats qu'ils attendent du CHIS pour le soutenir dans leurs différentes fonctions.

Dans l'exemple du laboratoire vivant évoqué plus haut, l'un des principaux besoins de l'ASC était d'aider à la création de registres primaires, car cela réduirait considérablement sa charge de travail et lui permettrait de consacrer plus de temps à la fourniture de soins plus efficaces. Une telle approche illustre également l'avantage d'appréhender les systèmes dans leur globalité (approche holistique) plutôt que de se limiter à un programme spécifique et autonome. Les avantages de l'adoption d'une approche holistique sont ressentis à travers les différents rôles des ASC et les programmes de santé. En revanche, une approche isolée et distincte accentue la fragmentation et ne présente que des avantages limités.

Le chapitre 3 fournit plus d'exemples sur l'utilisation locale du système ; nous ne reviendrons donc pas sur ce sujet ici. Le lecteur est invité à lire ce chapitre pour obtenir des exemples plus spécifiques d'approches visant à améliorer l'utilisation locale.

### Adoption d'Approches Hybrides { #adopt-hybrid-approaches }

Les approches hybrides sont celles qui répondent à une multiplicité de contextes, de conditions politiques et d'infrastructures. Il s'agit là d'un élément clé qui permet de garantir l'évolutivité du système et, par là, sa durabilité. Les conditions communautaires sont variables, multiples et relativement dynamiques. Le processus de conception du CHIS doit nécessairement être hybride et capable de répondre à cette multiplicité. Les approches hybrides englobent les approches techniques, institutionnelles et de gestion de projet.

Par exemple, la conception d'un système dont le fonctionnement repose entièrement sur la connectivité internet ne répond qu'à un seul critère -- la présence d'une connexion internet continue et fiable -- et ce système ne peut fonctionner que si ces conditions sont remplies. Un tel système a peu de chances de s'étendre, car il est peu probable qu'une connexion Internet idéale soit disponible dans toute une province, ou même dans tous les sous-districts à l'intérieur d'un district. Une approche consisterait à concevoir un système hybride capable de fonctionner dans des zones ayant un accès à Internet ou non. Permettre la saisie de données hors ligne, puis la synchronisation des données avec le serveur lorsque Internet est disponible, est une solution pratique qui permet de gérer ces contextes multiples. Le DHIS2 a adopté cette approche, ce qui a contribué à son utilisation généralisée dans une multitude d'environnements et de contextes.

> **Exemple**
>
> **Étude de cas : Différentes approches en Afrique du Sud et à Cuba**
>Des contextes politiques différents nécessitent également des approches hybrides.
> Le projet HISP en Afrique du Sud a connu un grand succès avec des approches participatives ascendantes dans un contexte post-apartheid en mutation, où l'amélioration de la situation des travailleurs de santé était au cœur de l'agenda de la réforme du système sanitaire.
>
> Cette même approche, une fois appliquée au projet HISP à Cuba, a été un échec cuisant, car l'environnement était extrêmement descendant ; une situation voulue par le bureau du président. Dans cet environnement, le HISP aurait dû d'abord obtenir l'aval du sommet, utiliser cet aval pour créer des espaces permettant de travailler avec des approches de conception participative sur le terrain, et développer progressivement l'appropriation en utilisant cette approche. Faute d'approbation au sommet, ceux qui était chargés de l'exécution du projet ont hésité à adopter cette approche étrangère, à savoir la conception ascendante du HISP, et ont finalement rejeté le projet.

De cette discussion, l'on peut retenir la nécessité d'analyser d'abord les contextes, puis d'identifier des approches réalisables pour la conception et l'implémentation. Il faut toujours être ouvert à l'adaptation et à l'improvisation en cours de route, et ne pas ignorer des approches qui pourraient fonctionner dans des contextes et situations temporelles différents.

### Conception du CHIS sur la base des forces existantes { #design-chis-based-on-existing-strengths }

L'approche HISP de la conception de CHIS a toujours souligné l'importance de la fondation en place, des pratiques de travail existantes et de l'histoire du CHIS en vigueur, et cherche à le nourrir ou à le cultiver au fil du temps. Cette approche part du principe que tous les systèmes ont une histoire et un passé, et qu'il existe des systèmes profondément enracinés, ainsi que des comportements et attitudes humains, qui ne peuvent jamais être éliminés.

Cette approche du HISP est à l'opposé de l'approche de la "table rase" qui a été largement adoptée par les consultants en gestion en Amérique du Nord dans les années 90. Cette dernière a été mise en œuvre via la méthodologie de la "réingénierie des processus opérationnels" (Business Process Reengineering - BPR). Cette approche de la table rase a été adaptée par les concepteurs de CHIS lorsqu'ils n'accordaient pas d'importance à ce qui existait déjà ; mais elle n'a pas eu beaucoup de succès, notamment lors de son adoption en Éthiopie au début de l'année 2000 dans le cadre du processus de réforme du secteur de la santé.

L'hypothèse dominante à propos du développement du système BPR se fonde sur une approche de la table rase, qui

1. Cherche à "effacer" les processus et systèmes existants et à repartir de zéro, en créant une table rase.

2. Elle suppose que les pratiques de travail et les attitudes existantes des ASC sont irrationnelles, non modernes, et qu'elles doivent être supprimées et remplacées par des techniques et des technologies plus modernes et rationnelles.

> **Exemple**
>
> **Étude de cas : Conception du CHIS au Mozambique**
> Un projet HISP allait introduire le DHIS au sein du système de santé communautaire au Mozambique. Lors de la formation au niveau communautaire, plusieurs forces ont été observées chez les ASC.
>
> 1. Les ASC avaient une grande capacité à effectuer plusieurs tâches. Ils ont développé cette capacité au fil de décennies de travail dans des environnements où les ressources sont extrêmement limitées. Par exemple, ils pouvaient fournir des soins et effectuer en même temps des tâches administratives.
> 2. Les ASC entretenaient des liens très étroits avec différents milieux locaux et non professionnels, tels que l'église. Ainsi, lorsque l'imprimante du centre de santé ne fonctionnait pas, ils se rendaient à l'église la plus proche pour imprimer les rapports dont ils avaient besoin d'urgence.
>
>u lieu de considérer les pratiques des ASC comme étant irrationnelles et entravant l'introduction de nouveaux systèmes, leur potentiel a été pris en compte pour soutenir l'introduction du système.
> 
> Cet exemple a mis en évidence les limites des approches existantes qui consistent à concevoir un système et à le mettre en œuvre en faisant "table rase" de tout ce qui existait.

Il ressort de cette discussion la nécessité de prendre sérieusement en compte l'histoire (les acquis) dans le processus de conception du système, de déterminer ses atouts et ses inconvénients, et de voir comment les atouts peuvent être progressivement exploités et valorisés au fil du temps.

## Interopérabilité avec DHIS2 dans le CHIS { #interoperability-with-dhis2-in-chis } 

### Pourquoi Interopérabilité ? { #why-interoperability } 

Les communautés sont souvent caractérisées par une faible couverture Internet, des infrastructures inégales et des systèmes essentiellement manuels, ce qui rend très difficile le déploiement d'un système entièrement basé sur le web. Il peut également y avoir plusieurs systèmes déjà en place, appartenant à différentes parties prenantes, qui remplissent des fonctions distinctes et dont le degré d'acceptation par les utilisateurs est élevé. Il est donc nécessaire de trouver d'autres moyens, grâce à l'interopérabilité, d'introduire les données dans DHIS2 afin de procéder aux agrégations requises, de créer des tableaux de bord analytiques et d'assurer le suivi des soins dispensés aux patients. L'interopérabilité vise à permettre à deux systèmes de se partager des données sans être perturbés. Par opposition, l'intégration implique la fusion de deux systèmes en un seul, de sorte qu'un seul système continue à fonctionner et que l'autre ne soit plus nécessaire. Étant donné que le propriétaire d'un système est généralement réticent à abandonner son système, l'intégration se heurtera souvent à une certaine résistance dans le contexte du CHIS.

En résumé, l'interopérabilité peut être considérée comme répondant aux cas d'utilisation suivants :

- Des systèmes comme ODK et CommCare sont utilisés dans divers contextes pour collecter des données individuelles et agrégées, et doivent interopérer avec DHIS.
- Etant donné que la couverture des réseaux mobiles est plus importante que celle d'Internet et que le téléphone mobile est facilement transportable, ce dernier peut être utilisé pour collecter les données, lesquelles peuvent être transmises plus facilement par SMS. Ces données transmis par SMS doivent ensuite être importées dans le DHIS2 et traitées ultérieurement.
- Là où les systèmes manuels dominent, les feuilles Excel peuvent être utilisées pour la saisie des données. Ces fichiers Excel doivent ensuite être introduits dans DHIS2 pour un traitement ultérieur.
- Les données communautaires peuvent également être collectées auprès des hôpitaux, où se rendent les résidents en vue de recevoir des soins de référence. Ces données hospitalières, généralement collectées dans un système de dossier médical électronique, doivent également interopéré avec DHIS2.

Nous donnons des exemples de cas d'utilisation qui illustrent les conditions susmentionnées, puis un aperçu technique de la manière dont l'interopérabilité a été réalisée avec le DHIS2. Pour chacun de ces cas d'utilisation, nous présentons également quelques orientations techniques sur la manière dont l'interopérabilité  peut être réalisée dans d'autres contextes.

## Cas d'utilisation d'interopérabilité { #use-cases-of-interoperability } 

### Open Data Kit (ODK) -- DHIS2 { #open-data-kit-odk-dhis2 } 

L'Institut national d'épidémiologie de Chennai, en Inde, développe un système sur DHIS2 pour surveiller l'évolution de la fièvre. L'objectif est d'enregistrer tous les cas de fièvre signalés dans un district afin de comprendre les schémas épidémiologiques qui expliquent ces cas. Pour ce faire, il est nécessaire de saisir des données nominatives sur la surveillance de la fièvre, ce qu'ils font à l'aide d'ODK. Chaque cas donne lieu à l'enregistrement des informations démographiques requises et des détails concernant la fièvre. Ces données doivent ensuite être transférées vers le DHIS2 pour un suivi plus approfondi, la génération de hotspots et l'élaboration de rapports et d'indicateurs qui seront affichés sur le tableau de bord. interopérer ODK et DHIS2 a donc été une tâche essentielle dans le processus de développement du système.

### CommCare -- DHIS2 { #commcare-dhis2 } 

Au Népal, l'Institut Hellen Keller (HKI) utilise DHIS2 comme système de suivi de la nutrition. Issu du recensement de la population et des ménages dans des districts sélectionnés du Népal, DHIS2 collecte des données individuelles sur la démographie et certains paramètres nutritionnels. Sur la base de ces données, des interventions sont menées et l'impact sur les besoins en paramètres nutritionnels est évalué au niveau des individus. Pour collecter ces données programmatiques, HKI utilise CommCare. Les données programmatiques de CommCare doivent interopérer avec les données de recensement de DHIS2. DHIS2 est également utilisé pour d'autres formats de rapport de données répondant à d'autres besoins du programme. Il est donc nécessaire de créer un "Data warehouse" (entrepôt de données) commun où les données de ces différents programmes, ainsi que les données sur la nutrition, pourraient être analysées en fonction d'indicateurs transversaux et affichées sur des tableaux de bord attrayants et faciles à utiliser.

### Importation Excel -- DHIS2 { #excel-import-dhis2 }

Alors que l'utilisation de feuilles Excel pour les données communautaires est un cas d'utilisation courant dans le contexte du CHIS, le cas d'utilisation examiné ici concerne la gestion globale du paludisme sur la base des cas. Ce projet, mis en œuvre dans l'État d'Odisha en Inde, prévoit une collecte de données sur les cas de paludisme dans un format nominatif à l'aide d'Excel, en raison de la faible disponibilité d'Internet. Les fichiers Excel contenant des données basées sur des noms sont régulièrement envoyés aux autorités supérieures par e-mail, clé USB, etc. Au niveau central, le fichier Excel est converti en CSV et importé manuellement dans DHIS2 via l'application d'importation de données. DHIS2 est alors en mesure d'agréger automatiquement les données aux niveaux supérieurs du HMIS. Le DHIS2 contient donc à la fois des données basées sur des noms et des données agrégées. Il est donc nécessaire de transférer les données de ces feuilles Excel vers DHIS2 afin de contrôler et de maintenir la qualité des données et de permettre une connexion entre les différents éléments du dossier du patient. Le défi ici était d'élaborer une méthodologie permettant d'importer les données Excel dans DHIS2.

### Importation de données par SMS -- DHIS2 { #sms-data-import-dhis2 }

Les rapports par SMS constituent un autre moyen courant de collecte et de transmission de données au niveau des structures de santé communautaires. L'OMS en Inde a initié l'utilisation d'un système utilisant les SMS afin de soutenir l'administration massive de médicaments (Mass Drug Administration) afin de lutter contre la FL (Filariose lymphatique), ceci, dans le cadre d'une campagne couvrant 34 districts ruraux en Inde sur une période intense d'une semaine. Les SMS ont été préférés à la transmission de données par Internet un nombre important d'ASC n'avaient pas les moyens de se procurer des smartphones et n'avaient donc pas été formés à leur utilisation. En outre, le choix s'est porté sur les SMS parce que la collecte de données ne concernait que quelques éléments (tels que le nombre de ménages visités, le nombre d'hommes, de femmes et d'enfants auxquels le médicament a été administré et les effets secondaires observés). Dans le cadre de cette campagne, les ASC se rendaient de maison en maison pour administrer les médicaments. Ils enregistraient les données sur leur téléphone, puis les envoyaient par SMS au DHIS2, où des tableaux de bord dynamiques ont été élaborés pour surveiller la couverture quotidienne et par zone géographique.

### Interopérabilité entre OpenMRS et DHIS2{ #open-mrs-and-dhis2-interoperability } 

OpenMRS est la plateforme sur laquelle un DME (dossier médical électronique) a été personnalisé pour un système intégré de gestion hospitalière pour le compte d'un hôpital de district dans l'Himachal Pradesh, en Inde. Le système collecte les données des patients à titre individuel au fur et à mesure qu'ils passent les différentes étapes dans l'hôpital : enregistrement, facturation, OPD, IPD, tests de laboratoire, pharmacie, etc. Ces données individuelles doivent être agrégées (par hôpital, service, période, etc.), puis envoyées au DHIS2. À ce niveau, des rapports agrégés sur la morbidité et la mortalité peuvent être élaborés ; des indicateurs administratifs et de gestion des hôpitaux (par exemple, la durée moyenne des séjours et les taux d'occupation des lits) peuvent être générés ; et des comparaisons entre les différents hôpitaux de l'État peuvent être effectuées. Cela n'aurait pas été possible avec le seul système OpenMRS. Le travail technique a donc consisté à développer une interopérabilité entre les deux applications et à s'assurer que leurs deux bases de données soient synchronisées à des intervalles prédéfinis.

Après avoir présenté ces différents cas d'utilisation de l'interopérabilité avec DHIS2, la section suivante traitera de l'approche technique, de même que des directives pour l'implémentation de cette interopérabilité .

## Approche technique pour l'interopérabilité { #technical-approach-for-interoperability } 

### Pour les cas ODK et CommCare{ #for-odk-and-commcare-cases } 

Un même processus a été suivi dans les deux cas pour développer l'interopérabilité. L'outil (Data Motor) a été conçu pour obtenir des données depuis l'application CommCare/ODK. Les données sont extraites de l'API via ce pool et sont ensuite transférées vers l'application DHIS2 toujours via l'API. Le diagramme ci-dessous illustre ce processus.

![ODK.jpg](resources/images/chis_figure26.jpg)


*Figure 4.6 :* Modèle d'interopérabilité entre DHIS2 et CommCare et ODK

#### Directives pour l'implémentation { #guidelines-for-implementation }

1. Identifiez les "**points de données**" qui doivent être partagés à partir du système de collecte de données.
2. Déterminez leur place dans le modèle de données du système d'où ils doivent être **extraits**.
3. Déterminez leur place dans le modèle de données du système vers lequel ils doivent être **transférés**.
    - Dans le cas du DHIS2, il s'agit d'éléments de données, de périodes et d'unités d'organisation
    - Dans le cas d'ODK et de CommCare, il s'agit de questions/invites à la saisie de données.
4. Faites correspondre les deux modèles de données sur la base d'un **identifiant unique** que choisirez entre les deux.
5. Réalisez le data motor
    - Extrayez les données d'un système de collecte de données,
    - Restructurez les données pour les adapter au modèle de données de l'autre système de collecte de données
    - Transférez les données restructurées vers l'autre système
    - Conservez un identifiant unique dans les deux systèmes pour les contrôles d'intégrité
6. Configurez le data motor pour qu'il s'exécute automatiquement de façon périodique
7. Conservez une trace de toutes les activités effectuées par le data motor pour assurer le suivi et le débogage.

### Importation Excel vers DHIS2 { #excel-import-to-dhis2 }

Un micro Excel a été créé dans DHIS2 à partir d'un modèle Excel prédéfini. Les données d'Excel sont mises en correspondance avec les UID des éléments de données, unités d'organisation et périodes pour lesquels les données doivent être importées dans DHIS2. La mise en correspondance dans Excel ne doit être effectuée qu'une seule fois. Une fois la mise en correspondance effectuée, les données peuvent être conservées dans les feuilles Excel et importées dans l'application DHIS lorsque la connexion Internet est disponible. Les données sont transférées vers DHIS2 par l'intermédiaire des UID mis en correspondance dans la feuille Excel et  transmises aux différents programmes et étapes de programme dans DHIS2 lorsqu'il s'agit de données basées sur le nom.

**Directives pour l'implémentation**

- Pour maintenir la qualité des données, un minimum de champs de texte ouverts doit être utilisé dans le format. Il faut plus d'options déroulantes pour permettre à l'utilisateur de sélectionner les options requises qui peuvent être facilement associées aux valeurs de données du DHIS2.
- La feuille doit être protégée de sorte que l'utilisateur ne puisse lui ajouter de nouveaux champs ou lui apporter des modifications dans l'application.
- Les validations telles qu'observées dans DHIS2 doivent être développées dans les feuilles Excel.
- Les codes d'unité d'organisation sont préférables pour le transfert des données vers DHIS2 afin d'éviter toute incohérence avec les noms d'unité d'organisation.
- Il est important d'avoir un identifiant unique pour chaque dossier dans DHIS2. Cet identifiant unique peut ensuite être utilisé pour relier les dossiers longitudinaux (étapes du programme) du patient. Ce dernier pourra donc être mis à jour au fur et à mesure qu'il effectue des visites. Cela permettra également d'éviter la création de doublons.

### Pour l'interopérabilité OpenMRS-DHIS2 { #for-openmrs-dhis2-interoperability } 

Le module d'interopérabilité entre le DME basé sur OpenMRS et le DHIS2 a été développé par l'équipe HISP India pour soutenir une architecture dans laquelle les données de visites basées sur des noms sont stockées sur le serveur de chaque hôpital. Ces données sont ensuite agrégées via des requêtes et transférées vers le référentiel de l'État (DHIS2) via un module d'échange de données. L'architecture envisagée prévoyait que les données basées sur des noms soient conservées au niveau de l'établissement et que les données agrégées soient transférées vers le portail DHIS2 de l'État par l'intermédiaire du module d'échange de données.

Avec la norme relative à l'interopérabilité (SDMX - Statistical Data and Metadata Exchange (Echange de données et de métadonnées statistiques), initialement promue par l'OMS et remplacée ultérieurement par la norme ADX), les données étaient échangées entre OpenMRS et DHIS2, et toutes les métadonnées (éléments de données et établissements) étaient synchronisées sur DHIS2 ; les informations agrégées étaient transférées périodiquement vers DHIS2 à l'aide de ses services API. Les rapports échangés comprenaient tous les rapports de programmes nationaux de lutte contre les maladies, des rapports sur les profils des maladies pour la population, et des rapports sur les stocks et les inventaires. L'implémentation de ce module a été un véritable défi. D'un point de vue technique, le transfert de données nécessitait l'écriture de centaines de requêtes afin d'agréger et d'introduire les données dans DHIS2. Au début, cette opération était réalisée manuellement ; certains membres du personnel n'avaient qu'à appuyer sur le bouton d'exportation. Lorsque l'exportation n'était pas régulière, le processus de transfert était automatisé pour que la synchronisation des données se fasse quotidiennement et à une heure fixe. Le défi ici était l'intermittence et le manque de fiabilité de la connexion Internet et de l'alimentation en électricité.

L'architecture de cet échange de données est esquissée à la figure 4.7.

![OpenMRS.png](resources/images/chis_figure27.png)

*Figure 4.7:*  Interaction entre DHIS2 et OpenMRS

#### Directives pour l'implémentation { #guidelines-for-implementation }

- Toutes les données à transférer vers DHIS2 doivent être définies en tant qu'éléments de données dans DHIS2. Des ensembles de données doivent être créés pour les rapports agrégés requis.
- Tous les indicateurs doivent être créés dans DHIS2, et toutes les données du numérateur (telles que le nombre de lits et de médecins) doivent être stockées dans DHIS2. Elles seront ensuite utilisées pour la génération des indicateurs.
- Les requêtes doivent être écrites pour permettre l'agrégation des données (basées sur des noms) de la base de données de OpenMRS, puis leur publication dans DHIS2 en tant qu'éléments de données définis.
- Les rapports et les tableaux de bord doivent être personnalisés dans DHIS2
- Un programmateur automatique doit être développé pour permettre l'échange périodique des données.

### Importation de SMS vers DHIS2 { #sms-import-in-dhis2 }

Une passerelle SMS et des API sont nécessaires pour recevoir les SMS dans le DHIS2. Si des messages de retour d'information doivent également être envoyés aux utilisateurs (pour confirmer la réception ou non du SMS dans le DHIS2), une API sera également nécessaire pour l'envoi de messages. Les messages doivent être envoyés à un numéro spécifique et peuvent être lus pour un ensemble prédéfini d'éléments de données. Des séparateurs tels que le point (.) ou l'espace ( ) pourraient être utilisés pour séparer les éléments de données lors de l'envoi des messages afin de faciliter leur compréhension par l'utilisateur. Les numéros de téléphone des utilisateurs doivent être enregistrés dans les unités organisationnelles auxquelles ils appartiennent. Ainsi, lorsqu'un SMS est reçu en provenance d'un numéro, il peut être enregistré dans l'unité organisationnelle correspondante.

#### Directives pour l'implémentation { #guidelines-for-implementation }

- En utilisant la fonctionnalité SMS, les éléments de données à rapporter ne doivent pas être trop nombreux pour que l'utilisateur puisse se souvenir de la séquence. La séquence et le format doivent être fournis sur papier à l'ASC pour faciliter son utilisation.
- Les numéros de téléphone de tous les utilisateurs doivent être enregistrés et il faut veiller à ce qu'ils envoient leurs messages avec les mêmes numéros, pour que les données soient enregistrées dans les unités d'organisation appropriées.
- Les images ci-dessous décrivent les différentes captures d'écran que l'utilisateur verra lors de l'envoi de son SMS et de la réception du message de confirmation.

![sms.png](resources/images/chis_figure28.png)


*Figure 4.8:* Exemple d'importation de SMS vers DHIS2

## Cas d'utilisation { #use-cases }

### Cas d'utilisation en Inde - Rapports par appareils mobiles effectués par les ASC { #india-use-case-mobile-based-reporting-by-chws }

Les rapports par appareils mobiles sont essentiels au CHIS dans de nombreux contextes. Cette section abordera trois modes différents de rapports par appareils mobiles sur la santé communautaire en Inde.

1. Rapports par SMS pour le HMIS au Pendjab, en Inde.
2. Rapports par SMS pour soutenir l'enquête sur le cancer au Pendjab, en Inde.
3. Rapports par GPRS pour le HMIS dans l'Himachal Pradesh, en Inde.

Dans chaque cas, nous fournissons des détails sur la technologie, les processus d'implémentation et de renforcement des capacités, les problèmes et les défis rencontrés et la manière dont ils ont été résolus.

#### Rapports par SMS pour le HMIS au Pendjab, en Inde { #sms-based-reporting-for-hmis-in-punjab-india }

En 2011, le Ministère de la Santé national a lancé un projet pilote dans 5 blocs de 5 États différents, impliquant environ 200 ASC, afin de tester l'efficacité technique des rapports par appareils mobiles au niveau communautaire.

Une application JAVA a été développée en J2ME et installée sur les téléphones portables des ASC. Un modem avec une carte SIM a été installé au niveau du bloc (sous-district) pour recevoir les messages. Le logiciel "SMS Listener" a été installé sur l'ordinateur du responsable du programme au niveau du bloc, de même que l'application DHIS2 hors ligne. Lorsque l'ASC envoie son rapport via l'application mobile, le rapport est reçu sous forme de SMS. Le SMS Listener installé reçoit ce SMS sous forme binaire et importe les données dans l'unité organisationnelle appropriée après avoir identifié le numéro de téléphone de l'expéditeur. Le numéro de téléphone de chaque agent de santé est saisi au niveau de l'unité d'organisation qui lui est associé, dans l'application DHIS2 hors ligne. Le projet pilote a permis de tirer quelques enseignements utiles. Des problèmes techniques ont été rencontrés, tels que la saturation des modems, des problèmes de signal dans les régions montagneuses et quelques pertes de données. Certains ASC étaient réticents à utiliser le téléphone portable car ils préféraient les rapports sur papier.

Dans l'ensemble, les projets pilotes ont été une réussite ; ce qui a amené le Punjab et l'Himachal Pradesh à être pour une pleine extension de cette méthode de rapports par appareils mobiles dans leurs états.

#### Rapports basés sur la cybersanté pour le HMIS au Pendjab{ #mhealth-based-reporting-for-hmis-in-punjab } 

L'État du Pendjab compte environ 5 000 ASC. Chaque sous-centre a 2 ANM (Auxiliary Nurse Midwife/infirmières sages-femmes auxiliaires), l'une est régulière et l'autre contractuelle. L'État a fourni à chaque ANM un téléphone portable (Nokia 2330 Classic) pour leur permettre de rapporter mensuellement les données de routine du HIMS.

Contrairement au projet pilote qui utilisait le DHIS2 hors ligne, le Pendjab a opté pour une application en ligne, développée en J2ME (JAVA) et en langue pendjabi. L'application était installée via Bluetooth sur le téléphone portable de l'ANM et fonctionnait avec des SMS. L'ANM devait remplir trois formulaires : rapport quotidien, rapport mensuel 1 et rapport mensuel 2. Après avoir rempli ces formulaires, il envoyait ses données par SMS sur le numéro dont la carte SIM était installée dans le modem au niveau du serveur de l'État. Après l'importation des données dans DHIS2, un SMS de confirmation est envoyé à l'ANM pour confirmer que son rapport a été reçu. Deux modems ont été installés sur le serveur de l'État, un modem pour chacun des 10-10 districts.

![téléphone 1.jpg](resources/images/chis_figure29.jpg)
![téléphone 2.jpg](resources/images/chis_figure30.jpg)

*Figure 4.9:* Exemple d'application de saisie de données J2ME

L'application DHIS2 fonctionnait en ligne avec les trois ensembles de données. Le numéro de portable de chaque ANM était enregistré au niveau du sous-centre où elle était affectée. Dès qu'un message est reçu, il est converti en fichier XML et importé dans DHIS2 vers l'unité d'organisation associée au numéro expéditeur. Étant donné que chaque sous-centre avait deux ANM, deux unités d'organisation supplémentaires ont été créées pour chacune d'entre elles, ANM1 et ANM2, et les numéros ont été enregistrés sous leur nom d'utilisateur respectif. Ce projet avec système mobile s'est déroulé parallèlement à l'application du HMIS de l'État sur DHIS2, et il était prévu qu'après quelques mois de rapports, toutes les données communautaires dans DHIS2 ne seraient fournies que par le biais de rapports avec système mobile.

En plus des téléphones portables, une connexion CUG a été fournie aux ANM. Elle comprenait un crédit Rs 200 pour leur permettre d'envoyer leurs rapports par SMS ainsi qu'une fonction d'appel gratuite.

![what.png](resources/images/chis_figure31.png)


*Figure 4.10:* Modèle de flux de données du cas d'utilisation au Pendjab

Le processus d'implémentation comportait les étapes suivantes :

- Acquisition du matériel : Nokia 2330 Classic avec carte SIM et modem de modèle EZ-SMS pour la réception des SMS.
- Finalisation des formats : Trois formats ont été finalisés : Ensemble de données Journalier, Mensuel 1 et Mensuel 2 avec respectivement 10, 56 et 83 éléments de données. 
- Classification ANM : Les ANM ont été classés en ANM 1 et ANM2.
- Installation : Le fichier JAR des trois ensembles de données a été installé via Bluetooth dans 5 000 téléphones portables et des autocollants mentionnant les noms et les sous-centres des ANM ont été collés au dos des téléphones portables. Ce processus s'est déroulé au QG de l'État pendant un mois et demi.
- Distribution des téléphones portables dans les districts : Après l'installation, les téléphones portables ont été envoyés dans les districts respectifs et distribués aux ANM avant les formations.
- Préparation du manuel de formation : le manuel de formation en pendjabi a ensuite été préparé. Il décrit l'utilisation de l'application à l'aide de captures d'écran et de diagrammes. Les exemplaires du manuel ont été distribués pendant la session de formation.
- Renforcement des capacités : Les formations sur l'utilisation de l'application ont été réalisées en 2 mois. Elles ont touché 4545 agents de santé et ont été réalisées au niveau des états/districts/blocs/sous-centres. Des équipes de deux membres ont été créées, chacune couvrant 5 à 7 districts. Au premier jour, un TOT de district a été réalisé, suivi de formations au niveau des blocs.
- Conseils pratiques : Pendant un an, une équipe de 3 membres basée au QG de l'État a fourni des conseils pratiques sur l'utilisation de l'application/du système.

#### Problèmes et défis rencontrés { #issues-and-challenges-experienced }

**Ensemble de données journalières:** Au début, les ANM étaient réticents à utiliser l'application, mais avec le temps, la situation s'est améliorée. Cette réticence était principalement due aux rapports journaliers. Ceux-ci incluaient des éléments de données représentant des activités réalisées principalement le mercredi dans le cadre des sessions du PEV (Programme élargi de vaccination), ce qui signifie qu'en dehors du mercredi, les éléments étaient rapportés avec des valeurs nulles. Avec ce modèle, les ANM ont estimé que les administrateurs auraient l'impression qu'elles ne travaillaient pas assez les autres jours. Pour surmonter cette réticence croissante, les administrateurs ont dû finalement renoncer à l'établissement de rapports journaliers.

**Facteur d'âge :** Les ANM âgées étaient réticentes, car elles n'avaient jamais utilisé de téléphone portable auparavant. Par conséquent, leur apprendre à utiliser l'application était une tâche difficile.

**Autres problèmes :** Des problèmes de signal, d'équilibre et des retards avec les rapports (messages) de confirmation côté serveur ont été rencontrés en raison de la forte activité sur l'application.

**Saturation des modems:** Les modems recevaient près de 5 000 SMS par jour, ce qui représentait une charge énorme pour le serveur de l'État et pour le modem, et retardait l'envoi du message de confirmation. Les ANM paniquaient, se demandant si leurs rapports avaient été reçus ou non. En outre, l'envoi de messages a commencé à échouer car l'opérateur de téléphonie mobile ne conservait les messages non reçus que pendant trois jours sur son serveur. Deux modems supplémentaires ont été installés pour l'envoi des messages de confirmation afin de mieux répartir la charge entre modems.

![](resources/images/chis_figure32.jpg)
*Figure 4.11:A pourcentage de l'état des données par district montrant le pourcentage de déclaration dans les premiers jours.*

Pourcentage du statut des données par district indiquant le pourcentage des rapports aux premiers jours.

**Points clés à retenir:**

- Augmenter la fréquence des rapports juste parce que la technologie le permet n'est pas une bonne idée car cela donne aux ANM l'impression d'être de plus en plus surveillées.
- Les modems semblaient sous équipés pour gérer un grand trafic de SMS. Une passerelle pour les SMS aurait été plus appropriée pour un projet à grande échelle.
- L'État prévoit utiliser une application Android pour effectuer les rapports du HMIS.

### Cas d'utilisation d'un rapport d'enquête sur le cancer par SMS au Punjab{ #punjab-sms-based-cancer-survey-reporting-use-case } 

Après le succès des rapports journaliers du HMIS en 2011, l'État a lancé en 2012 un nouveau projet utilisant SMS pour l'enquête sur le cancer pour :

- Sensibiliser aux signes précurseurs et aux symptômes du cancer.
- Permettre une détection précoce de la maladie sur la base des symptômes
- Identifier l'incidence de la maladie (nombre réel de cas) pour une planification ultérieure

Le processus de réalisation de l'enquête est brièvement décrit :

- L'enquête dans les zones rurales a été réalisée par des ASC, et dans les zones urbaines, par des étudiants en sciences infirmières et en médecine
- Les enquêteurs se sont rendus dans chaque ménage de leur région
- L'enquête a été réalisée à l'aide d'un questionnaire comprenant des formulaires : D'abord pour recueillir des informations basiques sur chaque membre d'un ménage, telles que le nom, la tranche d'âge, le niveau d'instruction, les antécédents familiaux de cancer, etc. Ensuite, si une personne était atteinte d'un cancer ou présentait des symptômes de cancer, des détails spécifiques à la maladie étaient recueillis et transmis par téléphone portable (application JAVA SMS) au DHIS2.
- Les mêmes téléphones portables (Nokia 2330) et modems ont été utilisés pour l'enquête.

La liste des anciens numéros de téléphone a été utilisée, puis les nouveaux numéros ont été ajoutés et enregistrés dans l'application DHIS2. L'enquêteur envoyait un SMS concernant un cas particulier ; le SMS était converti en fichier XML, puis importé dans l'unité d'organisation correspondante, où un numéro d'identification unique était généré et renvoyé dans le SMS de confirmation. L'enquêteur notait ensuite ce numéro unique dans le formulaire spécifique afin de suivre le cas dans l'application en ligne. L'application mobile était utilisée dans les zones rurales, tandis que dans les zones urbaines où Internet était plus fiable, les données étaient saisies directement dans l'application en ligne.

#### Flux de données  { #data-flow } 

![](resources/images/chis_figure33.png)


*Figure 4.12:* Flux de données du niveau du sous-centre au niveau de l'État.

#### Le processus de renforcement des capacités { #the-capacity-building-process }

Avant un déploiement dans tout l'État, un projet pilote a été réalisé dans un district sur 2 blocs, et un processus d'implémentation similaire à celui du HMIS a été mis en place. Une équipe de formation de 150 membres a été constituée et la formation dans tout l'État a été réalisée en deux semaines.

- Les formations ont été réalisées au QG du district ou au niveau du bloc
- Une équipe de formation de deux à trois membres a conduit la formation sur chaque site.
- L'assiduité des participants à la formation a été prise en compte
- Les téléphones portables des ASC ont été collectés lorsqu'ils se sont rendus à la formation
- Un membre de l'équipe était chargé de l'installation de l'application. L'autre dispensait la formation, à l'aide d'un émulateur et dune présentation PowerPoint
- Lors de la session pratique, l'agent de terrain a été formé sur la façon de remplir tous les champs de l'ensemble de données et d'envoyer les données via le téléphone portable.
- Pour les zones urbaines, le formulaire a été conçu sur le DHIS2 Tracker. Le dossier individuel était saisi sur l'écran d'enregistrement des patients et les résultats sous forme de rapports pouvaient être consultés au niveau des rapports disponibles dans l'application.

La transmission des données des zones rurales via des rapports par téléphones portables s'est déroulée sans problème, même si le problème de saturation du modem a persisté. Pour résoudre ce problème, un administrateur de serveur a été affecté à la salle des serveurs de l'État pour surveiller le trafic SMS en temps réel. Dans les zones urbaines, les utilisateurs ne pouvaient pas sauvegarder les données dans l'application en ligne en raison de l'énorme base de données. Pour résoudre ce problème, une fonctionnalité d'importation Excel a été introduite pour la saisie des données du proforma 2 dans les feuilles Excel, lesquelles étaient ensuite transférées vers le DHIS2.

### Cas d'utilisation : Rapports du HMIS par SMS dans l'Himachal Pradesh { #himachal-pradesh-sms-based-hmis-reporting-use-case }

Après un projet pilote réalisé dans un seul bloc, l'État a décidé d'initier un projet pilote dans tout l'État. Les leçons tirées de l'expérience du Pendjab ont permis de passer d'une application SMS à une application GPRS. Voici quelques leçons tirées du projet pilote au Pendjab :

- La recharge du GPRS coûtait plus chère que le SMS
- La connectivité avec le GPRS était médiocre dans les régions montagneuses et éloignées.
- L'État n'a pas fourni de téléphones aux ANM. Elles on utilisé leurs propres portables.
- Le GPRS n'était pas compatible avec de nombreux téléphones d'utilisateurs ni avec le navigateur Opera mini. Sur 201 téléphones mobiles, seuls 74 téléphones étaient compatibles, soit seulement 37 %.
- Les ANM ont estimé que l'utilisation d'une solution Web était difficile et que les paramètres du GPRS à configurer sur le téléphone leur étaient contraignants.

Après les leçons tirées du projet pilote, l'État a décidé d'opter pour une application J2ME. Le formulaire mensuel du sous-centre a été choisi pour les rapports. L'État a ensuite décidé d'acheter des téléphones pour les ANM et a choisi le Nokia C1-01, et 50 roupies ont été données à chaque ANM pour la recharge. Comme au Pendjab, une application J2ME utilisant les SMS a été développée pour l'envoi des rapports. Cependant, les formats choisis ne concernaient pas uniquement les sous-centres comme au Pendjab, mais des formats multiples ont été sélectionnés :

- Formulaire SC - Pour les agents de santé du sous-centre (mensuel)
- IDSP -- Pour les agents de santé du sous-centre (hebdomadaire)
- Formulaire SSP 1 & Formulaire SSP 2 -- Pour les agents de santé SSP (mensuel)
- Formulaire CHC 1 & Formulaire CHC 2 -- Pour les agents de santé du CHC (mensuel)
- Mortalité -- Pour les agents de santé du SC, SSP, CHC (mensuel)

Des fichiers JAR ont été créés pour tous ces formats et installés sur les téléphones des différents établissements.

#### Passerelle SMS { #sms-gateway-solution }

L'implémentation au Pendjab a révélé que le modem n'était pas la solution appropriée pour un déploiement dans tout l'État. C'est pourquoi une passerelle SMS a été utilisée en lieu et place du modem.

- Le Département des technologies de l'information (DIT) de l'État disposait déjà d'une passerelle SMS achetée auprès d'un opérateur privé.
- Les implémenteurs ont contacté ce fournisseur pour qu'il réalise l'intégration avec DHIS2. Mais l'État a ensuite changé de fournisseur au profit du département informatique du gouvernement. L'intégration a donc dû être refaite.
- Le serveur et la passerelle SMS ont tous deux été placés au niveau du bureau informatique de l'État, ce qui a créé de nombreux défis logistiques.
- L'application finale intégrée à la passerelle SMS a été déployée.

Quelques problèmes rencontrés :

- Lors des tests, il a été constaté que le département informatique du gouvernement ne prenait pas en charge les SMS compressés précédemment utilisés au Pendjab.
- Le serveur ne prenait en charge que la longueur de base des SMS, soit 160 caractères, et pour certains opérateurs, seulement 110/120 caractères. Cette longueur était souvent insuffisante, car nos SMS étaient précédés d'un mot-clé HP NRHM.
- Au 161è caractère, le serveur ne pouvait pas reconnaître le second SMS qui n'était pas préfixé par HP NRHM et, par conséquent, le second SMS était perdu, ce qui empêchait la transmission de données complètes.
- Le formulaire du SC a donc été subdivisé en trois parties contenant chacune 100 caractères. Mais cette solution n'était pas la plus optimale.
- L'application a alors été retravaillée, de sorte que le deuxième SMS, au 121e caractère, soit également préfixé par le mot-clé HP NRHM. Le deuxième SMS était coupé au 121e caractère, ce qui a rendu l'établissement des rapports plus fluide.
- Dans certains blocs, l'ANM était responsable de plusieurs sous-centres, mais dans l'application, un seul numéro de téléphone pouvait être attribué à une unité d'organisation. Pour y remédier, un code d'installation à 4 chiffres a été introduit pour chaque unité d'organisation. Ainsi, un agent de santé peut rendre compte de plusieurs unités d'organisation à partir d'un même téléphone portable.

![](resources/images/chis_figure34.jpg)


*Figure 4.13 : Les ANM examinant l'application lors d'une des sessions de formation dans le district de Kangra.*

##### Processus de renforcement des capacités { #capacity-building-process } 

- La formation s'est déroulée principalement au niveau du bloc, par le biais d'une équipe de formation de 2-3 personnes.
- La présence des participants à la formation ainsi que leurs numéros de portable ont été relevés.
- Les téléphones portables des agents de santé ont été collectés lorsqu'ils se sont rendus à la formation.
- Un membre de l'équipe était responsable de l'installation de l'application tandis que l'autre était responsable de la formation sur les formats et l'application.
- Les numéros de téléphones ont été enregistrés dans les unités d'organisation respectives dans DHIS2.
- Un des membres a sensibilisé les agents de santé à envoyer leur rapport à l'aide de téléphones portables via l'émulateur. Une formation pratique en a suivi.
- Des directives ont été données sur les formats et décrites dans les manuels de formation qui ont été distribués à tous les agents de santé.
- Les codes des établissements respectifs ont également été donnés aux agents de santé, et il leur a été demandé d'envoyer un SMS factice afin de vérifier le fonctionnement de l'application.
- Ensuite, ces données fictives ont été supprimées du serveur et il a été demandé aux agents de santé de commencer leurs rapports mensuelles à la date prévue.

##### Problèmes et défis { #issues-and-challenges } 

- Le fournisseur de la passerelle SMS a été remplacé, ce qui a nécessité une refonte de l'ensemble du processus d'intégration.
- Les SMS étaient relativement chers pour le code court.
- Le code court a été modifié. Il a donc fallu changer à nouveau le code court dans 201 téléphones mobiles
- Le déploiement et la maintenance du serveur étaient difficiles en raison des normes gouvernementales strictes. Par exemple, aucun accès à distance au serveur n'était possible. La mise à jour du serveur devait donc se faire en personne à chaque fois.

Le tableau ci-dessous résume les différences d'approches de l'application de santé mobile au Pendjab et dans l'Himachal.


| **Pendjab** | **Himachal Pradesh** |
| :- | :- |
| Basé sur les SMS J2ME | Basé sur les SMS J2ME |
| Modem | Passerelle SMS |
| Formulaire SC uniquement | Plusieurs formulaires : SC, CHC et IDSP formulaire S |
| L'État a fixé les dates de formation | L'État organise ses propres formations HMIS en même temps que les TOT mobiles du district. Lors des TOT de district, les dates des formations en bloc ont été fixées. L'application est en cours d'installation dans les formations de bloc elles-mêmes. |
| Plan tarifaire CUG postpayé d'Airtel | Prépayé, pas de CUG, BSNL |
| La formation n'est dispensée qu'aux ANM et aux superviseurs. | Tous les agents de santé et superviseurs ont été formés. |

*Figure 4.14 :* Différence entre les cas d'utilisation en Inde.

