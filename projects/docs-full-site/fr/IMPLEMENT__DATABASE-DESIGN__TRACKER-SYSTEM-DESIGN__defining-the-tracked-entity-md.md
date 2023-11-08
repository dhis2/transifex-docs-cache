---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/database_design/defining-the-tracked-entity.md"
revision_date: '2023-05-24'
tags:
- Implémentation
---

# Définition de I'Entité Suivie { #defining-the-tracked-entity } 
![](resources/images/image43.png "Step2")


À cette étape, vous avez réalisé une cartographie détaillée du système de déclaration et commencé le mapping de ces concepts du système de déclaration vers les terminologies du DHIS2. Il peut être utile de revoir les concepts clés du DHIS2 pour se rappeler la différence entre les Instances d'Entité Suivie (IES), les Enrôlements, les Attributs d'Entité Suivie (AES) et les Éléments de Données.


Dans les sections suivantes, nous nous appuierons sur ces connaissances pour décrire :


* L'unité centrale d'analyse dans les rapports de routine ("*quel type d'enregistrement est suivi?*")
* Les points de données qui identifient chaque enregistrement comme distinct des autres ("*comment les utilisateurs recherchent-ils et identifient-ils un enregistrement unique?*”)

## Personnes et Cas { #persons-and-cases } 

La première question à se poser est de savoir si la personne suivie aura plusieurs rencontres ou suivis. S'il n'y a qu'un seul "point de contact" avec ce client, par exemple une campagne de vaccination à dose unique, vous pouvez songer à utiliser le [modèle de données de saisie d'événement] (#about_event_capture_app) plutôt. L'utilisation de Tracker ne présente qu'un intérêt limité, à moins que le client ne soit consulté plusieurs fois. En effet, le suivi au niveau individuel représente une charge supplémentaire pour les prestataires de soins qui doivent saisir et consulter les identifiants des patients, ainsi qu'un risque inutile pour la sécurité des données en stockant des informations aussi sensibles lorsqu'elles ne sont pas strictement nécessaires.

La deuxième question est de savoir si l'enrollement est **répétable**, c'est-à-dire si une personne peut être considérée comme un "cas" plus d'une fois au cours de sa vie. Pour certains programmes de suivi des maladies chroniques, tels que la vaccination chez les enfants et le VIH, le cas est considéré comme dupliqué si la même personne s'inscrit plus d'une fois. Pour d'autres, tels que les soins prénatals ou les enquêtes sur le paludisme, il peut être courant que la personne passe par le programme plusieurs fois. Cette décision a des conséquences sur le processus de recherche, la déduplication des enregistrements et le calcul des indicateurs.

Il est à noter que la majorité des cas d'utilisation du Tracker ont un type d'instance d'entité suivie "Personne", à l'exception des "cas" de surveillance des maladies. Les personnes peuvent être inscrites dans plusieurs programmes où elles reçoivent différents types de services de santé ; pour avoir un aperçu de l'histoire clinique d'une personne, il est donc utile de relier toutes les inscriptions du patient dans les différents programmes à un TEI "Personne" commun. Dans les scénarios de surveillance des maladies, il peut être plus approprié d'utiliser un type d'instance d'entité suivie "cas", où chaque cas se voit attribuer son propre numéro d'identification unique et est considéré comme un enregistrement distinct. Dans un tel scénario, la rapidité de la notification est la plus urgente : il n'est pas nécessaire de relier les cas antérieurs du patient, et la recherche du TEI de la personne pour relier toutes les inscriptions antérieures du patient ne fait que ralentir le processus de saisie des données sans apporter de valeur ajoutée.

En outre, certains cas d'utilisation spécialisés nécessitent un suivi de personnes non physiques en tant qu'entités suivies, par exemple un programme logistique de suivi de fournitures médicales ou de médicaments.

> **Remarque**
>
> Pour décrire les scénarios de Suivi les plus courants, ce guide se basera sur des cas d'utilisation où le Type d'Entité Suivie
> est une "personne", un "patient" ou un "client", sauf mention particulière.


## Identifiants et Éléments de Données { #identifiers-and-data-elements } 

La prochaine étape importante consiste à séparer les **Attributs de l'Entité Suivie** des autres points de données importants.

En règle générale, les Attributs d'Entité Suivie (AES) permettent d'identifier le dossier TEI comme appartenant à un client spécifique. Certains d'entre eux peuvent être _consultables_, ce qui signifie que les utilisateurs peuvent consulter la base de données DHIS2 à l'aide d'une valeur AES pour trouver le dossier d'inscription de leur patient. L'utilisateur n'a qu'à examiner l'AES du dossier pour savoir si le dossier appartient à son client.

Elles ne sont généralement saisies qu'une seule fois -- la toute première fois qu'un client est inscrit au programme Tracker -- et doivent donc être considérées comme des valeurs fiables et semi-fixes qui changent rarement d'un rendez-vous à un autre.

Les **Eléments de Données** sont toutes les autres données saisies dans le cadre du programme de suivi. Ils sont normalement utilisés pour représenter l'état de santé d'un client, le diagnostic, le traitement, le résultat ou d'autres services reçus. Par rapport à l'AES, ils sont beaucoup plus susceptibles de changer entre les rendez-vous avec le prestataire de soins de santé. Il est à noter que ces éléments de données doivent utiliser le type de domaine "Tracker" pour les distinguer des éléments de données utilisés dans le domaine agrégé.


> Les ***Attributs d'Entité Suivie*** se rapportent à l'*identité* d'un client et aident l'utilisateur à vérifier que le TEI qu'il voit dans le DHIS2 représente bien la personne en question.
>
> Les ***Éléments de Données*** sont tous les autres *champs du formulaire* et concernent généralement le dossier médical d'un client ou d'autres prestations qu'il a reçues dans le cadre du programme.


Les exemples standard d'Attributs de l'Entité Suivie sont notamment le Nom du Client, la Date de Naissance, le Numéro de Téléphone, et d'autres identifiants nationaux. Les éléments de données varient souvent d'un domaine de santé à l'autre, mais contiennent souvent le Diagnostic de la Maladie, le Poids du Patient, les Résultats de Laboratoire, les Médicaments Fournis, et le Résultat du Traitement.

Les Éléments de Données aussi bien que les Attributs d'Entité Suivie ont un certain nombre de types, notamment les Dates, Oui/Non, Oui uniquement, Texte libre, et le Choix multiple " Choisir-Un " (Ensembles d'options). La liste complète des types de valeurs d'Attributs d'Entité Suivie et des types de valeurs d'Éléments de Données se trouve dans le [Guide de l'Utilisateur du Tracker](#configure_tracked_entity)

Par ailleurs, des [règles de programme](#about_program_rules) peuvent être appliquées pour valider les valeurs de ces champs, ou appliquer une logique de saut pour les afficher uniquement dans certaines circonstances. Les règles de programme permettent de produire des mécanismes dynamiques en réponse à chaque entrée de l'utilisateur dans le tracker et la saisie d'événements. Vous trouverez plus d'informations sur les règles de programme dans la section [Conception d'interaction](#interaction-design) et dans le Guide de l'utilisateur.


## Attributs d'entités suivies comme Identifiants Personnels { #tracked-entity-attributes-as-personal-identifiers } 

Les Attributs d'Entité Suivie peuvent être décrits comme les points de données qui relient l'identité d'un client spécifique à son dossier médical individuel. Ils aident les prestataires de soins à _enregistrer_ une personne unique, puis à _rechercher_ et _récupérer_ ce même dossier. Dans certains cas, comme celui des registres de vaccination, un identifiant peut également _vérifier_ l'éligibilité d'une personne pour des prestations. Dans de nombreux contextes, tous les patients n'ont pas accès à des identifiants nationaux ; selon la Banque mondiale, [plus d'1 milliard de personnes dans le monde] (https://id4d.worldbank.org/global-dataset/visualization) ne disposent pas d'une pièce d'identité officielle. Dans ces cas, un prestataire de soins peut avoir besoin de recourir à des combinaisons de différents Attributs d'Entité Suivie pour identifier de façon unique le patient dans le Tracker.


> Un Attribut d'Entité Suivie idéal est à la fois **_universel_** (haute disponibilité) et **_unique_** (haute spécificité). Les programmes Tracker auront généralement besoin de plusieurs AES pour aider les utilisateurs à effectuer des actions de recherche, d'enregistrement et de vérification.


Le tableau ci-dessous présente des exemples courants d'AES en fonction de la disponibilité et de la spécificité, sur la base de l'expérience des implémenteurs du DHIS2.

|Nom de la TEA|Disponibilité|Spécificité|Observations
|:--|:--|:--|:----|
|Nom de famille|Élevé|Faible|Dans tout contexte culturel, il y a souvent une forte proportion de clients portant le même nom de famille (Smith, Gonzales, Banda, Ali, Devi, etc.). La saisie d'un nom de famille en texte libre est également sujette à des problèmes d'orthographe ou de translittération.|
|Date de naissance|Moyennement-élevé|Élevée|De nombreux clients peuvent ne pas connaître leur date de naissance exacte. Il convient de noter que l'AES de type "âge" calcule une date de naissance estimée à partir de l'âge déclaré en années au moment de l'inscription, et qu'il est donc très imprécis et incohérent lorsqu'il est utilisé dans différents programmes. Une meilleure solution consiste à compléter l'AES "Date de naissance" par un AES "Oui-uniquement" pour "La Date de Naissance est Estimée".|
|Numéro de téléphone|Moyennement-élevé|Élevée|Les numéros de téléphone peuvent servir d'identifiants distincts, bien qu'ils puissent changer au fil du temps lorsque les clients changent de fournisseur de services mobiles. Il convient de noter que certains clients peuvent ne pas posséder de téléphone ou partager l'accès au téléphone avec quelqu'un d'autre. Les règles du programme peuvent valider la longueur ou les premiers chiffres du numéro de téléphone lors de la saisie des données.|
|Addresse|Moyennement - Faible|Moyennement-élevé|Un grand nombre de clients en milieu urbain et rural vivent dans des logements collectifs ou dans des résidences sans adresse. Sujet à des fautes d'orthographe en texte libre et peu utile en tant que critère de recherche des clients.|
|Village de Résidence (ou Autres Zones Géographiques Régionales)|Élevée|Faible|Il peut être utile de confirmer le résultat d'une recherche, en particulier si la résidence est sans adresse. Mais des problèmes similaires de fautes d'orthographe et de faible précision des recherches persistent.|
|Nº d’identité national|Moyennement - Faible|Très Élevé|Bien que L'état civil et les statistiques démographiques (CRVS) se soient améliorés à l'échelle mondiale, de nombreux pays ne disposent pas d'un identifiant universel et unique, tel qu'une carte d'identité nationale. Bien que l'unicité soit élevée dans les pays disposant d'un système d'identification national, [les enquêtes montrent] (https://www.unaids.org/sites/default/files/media_asset/JC2640_nationalhealthidentifiers_en.pdf&sa=D&source=docs&ust=1683242277689786&usg=AOvVaw2ahTy7lR7SrC3qNRM7qAF5) que la couverture peut être inégalement répartie. Les femmes, les enfants et les personnes à faible revenu sont moins susceptibles d'avoir une carte d'identité nationale dans les pays à faible revenu. Certaines implémentations du DHIS2 relient leur système à un registre central CRVS afin de saisir automatiquement une carte d'identité nationale dans le dossier du client.|
|Pays d'Origine|Moyen|Très Faible|Peut être utile dans le cadre de la surveillance des maladies pour identifier l'origine de la maladie, compléter l'adresse du client ou identifier les inégalités en matière de soins. Non recommandé pour la recherche de clients.|
|Carte nationale d'(assurance) maladie|Moyen|Élevée|Lorsque de tels cartes existent, certains pays peuvent disposer de plusieurs systèmes d'assurance ou de plusieurs identificateurs nationaux. Ainsi, les utilisateurs peuvent être amenés à sélectionner un identifiant national parmi plusieurs lors de l'enregistrement et de la recherche (par exemple, le numéro de passeport, le numéro du système d'assurance, ou le certificat de naissance).|
|Numéro d'identification du cas (écrit)|Moyen|Élevée|Certaines unités de santé disposent d'un numéro d'identification unique pour chaque patient, préimprimé sur les registres papier. Ce numéro peut être saisi manuellement dans le DHIS2 lors de l'enregistrement*.|
|Identifiant unique (généré automatiquement)|Élevée (web) Moyennement-élevée (Android) | Élevée|Le DHIS2 peut remplir automatiquement les champs d'identifiants uniques selon des modèles séquentiels ou aléatoires. Ces identifiants sont conservés localement sur les appareils Android, qui nécessitent une synchronisation régulière avec le serveur pour actualiser la liste locale des identifiants disponibles de sorte que les identifiants qui contiennent des identifiants séquentiels ou des dates ne puissent avoir des [conséquences sur les performances](#implementation_guide_dhis2_config_reserved_id) ou un [comportement inattendu](https://community.dhis2.org/t/question-regarding-expiry-of-reserved-ids-of-an-auto-generated-unique-values-configured-with-a-text-pattern-containing-current-date-mm-yyyy/40761/2). Pour plus d'informations sur la méthode TextPattern, consultez le [Guide de l'utilisateur](#working-with-textpattern).|



\*  Dans de nombreux scénarios, une "personne" peut être considérée comme un " Cas " du programme plusieurs fois au cours de sa vie. Par conséquent, le numéro d'Identification d'un Cas ne doit être utilisé comme Attribut d'Entité Suivie que si le Type d'Entité Suivie est _Cas_. Si le Type d'Entité Suivie est _Personne_, l'identifiant du Cas peut être utilisé comme élément de données dans une étape du programme comme contrôle de vérification, mais il ne doit *pas* être utilisé comme Attribut d'Entité Suivie, puisqu'une personne peut avoir plus d'un identifiant de Cas. Inversement, dans un contexte de surveillance des maladies où le type d'entité suivie est un "Cas" au lieu d'une "personne", un implémenteur ne peut pas utiliser d'identifiant personnel unique tel que l'identifiant national, car il pourrait être reproduit pour plusieurs cas appartenant à la même personne.


### Partage d'AES entre les programmes { #sharing-tea-across-programs } 

Les valeurs d'AES d'un client peuvent également être partagées entre toutes ses inscriptions dans la même base de données DHIS2, ce qui accélère la saisie des données et soutient les efforts de déduplication dans les milieux où les zones de santé partagent des clients (par exemple, la surveillance des cas de tuberculose et de VIH).

Si un AES ne sera utilisé que dans un seul programme, il doit être [assigné au programme lui-même] (#create-or-edit-a-tracker-program). Si l'AES doit être partagé entre plusieurs programmes, vous devez l'affecter à l'entité suivie _type_. Si vous décidez d'utiliser la fonction [Relations](#relationship-model.html) pour relier deux instances d'entités suivies dans deux programmes distincts (par exemple une mère dans la CPN et un enfant dans le Suivi des Vaccinations), l'AES assigné au Type d'Entité Suivie sera affiché dans la boîte de dialogue lorsque vous rechercherez le TEI "cible" pour ajouter la relation à l'actuel TEI "d'origine".


### Rendre l'AES consultable { #making-tea-searchable } 

Les AES sont essentiels pour rechercher les dossiers des clients, mais afin d'améliorer les performances du système, vous pouvez souhaiter restreindre la recherche à un sous-ensemble plus petit de tous les AES associés au programme. Certains types de recherche peuvent renvoyer un trop grand nombre de résultats ou entraîner de longs délais pour le serveur. Il existe donc un équilibre inhérent entre la souplesse et les performances de la recherche.

Toutefois, en règle générale, vous devriez envisager de diviser tous les AES consultables en segments aussi petits que possible. Par exemple, au lieu d'un AES consultable pour "nom complet", envisagez d'en créer un pour "nom de famille" et un autre pour "prénom". En segmentant les critères de recherche de cette manière, vous obtiendrez généralement des résultats plus rapides qu'en recherchant l'intégralité du nom complet pour chaque AES.

L'AES peut également être marquée comme "confidentielle" lors de la configuration du programme. Si le cryptage est activé dans l'instance DHIS2, toutes les AES "confidentielles" seront cryptées au repos dans la base de données. Il convient de noter que cela signifie que l'AES confidentielle ne peut pas être utilisée comme critère de recherche par les utilisateurs finaux.


### Le Profil de Base des Cas de l'AES { #the-core-tea-case-profile } 

Un ensemble d'AES de base saisis dans les programmes de surveillance des cas, tels que la date de naissance et le prénom, ont été pré-générés pour de nombreux ensembles de métadonnées DHIS2. Une recommandation importante pour les nouveaux programmes de surveillance est d'installer le [package de la Bibliothèque Commune de Métadonnées] (#gen-lib-design), qui comprend le profil de Base des cas de l'OMS, comme point de départ pour la configuration du programme.


### Établissement d'un lien entre le Tracker et les registres de la population{ #linking-tracker-with-population-registers } 

Dans l'esprit de "saisir les données une fois, les utiliser plusieurs fois", certains pays ont pris la décision de connecter leur base de données nationale d'enregistrement de l'état civil (ou "registre de population") aux programmes Tracker du DHIS2 utilisés pour les cas d'utilisation prioritaires. Au lieu de rechercher des TEI existants dans un assortiment de détails démographiques dans un programme, puis d'ajouter laborieusement des valeurs d'attributs TEI pour chaque "nouveau" patient, les utilisateurs finaux effectuent simplement une recherche par numéro d'identifiant national, et les attributs TEI clés tels que le nom, la date de naissance et le genre sont remplis automatiquement. Le processus de recherche est ainsi plus efficace et les données démographiques ont plus de chances d'être exactes et de grande qualité.

> **:mag : Cas d'Utilisation par Pays**
>
>Il existe différentes approches pour établir un lien avec les registres Tracker de la population, en fonction des caractéristiques de la population, du cas d'utilisation des programmes de santé et du contexte juridique. Lors des campagnes de vaccination contre le Covid-19, le Cap-Vert et le [Sri Lanka ] (https://community.dhis2.org/t/implementing-large-scale-immunization-tracker-sri-lankan-experience/43008), ainsi que d'autres pays, ont trouvé pratique d'exporter les données du registre national de la population, de les transformer en instances d'entités suivies dans DHIS2, puis d'effectuer une importation unique de ces TEI dans leur système national de suivi des vaccins contre le Covid. Dans les deux pays, il était possible d'importer les données dans une seule instance DHIS2 en raison de la taille raisonnable de la population (500 000 et 21 millions) et de la portée limitée de la campagne de vaccination (adultes). Pour la surveillance continue de la santé publique, les sous-populations sensibles ou la fourniture de services aux personnes non enregistrées telles que les nourrissons, un lien direct avec le système CRVS "en direct" peut s'avérer plus approprié. Par exemple, au Rwanda, un javascript personnalisé dans la page de Tracker du DHIS2 permet une requête API directement vers le système national CRVS sur la base de l'Identifiant national saisi ; lorsque le résultat de la recherche est confirmé, les détails démographiques sont automatiquement ajoutés à la page d'enregistrement. Cette intégration DHIS2-CRVS va dans les deux sens. Dans le [système de suivi de la vaccination des enfants au Rwanda] (https://dhis2.org/rwanda-crvs-eir-integration/), les nouvelles naissances non enregistrées saisies dans le système de suivi notifient aux officiers d'état civil qu'ils doivent fournir un certificat de naissance.


## Un Programme ou Plusieurs ? { #one-program-or-multiple } 

À ce stade, vous devez déterminer si vous avez besoin d'un seul ou de plusieurs programmes pour votre système Tracker. Un programme définit la séquence d'événements qu'une entité peut suivre - le "cadre" des événements - et les attributs requis lorsqu'une entité rejoint le programme. S'il existe _plusieurs façons d'entrer dans un programme ou d'en sortir_, vous pouvez envisager d'avoir un programme distinct pour chacune d'entre elles.

> **Exemple**
>
>Un laboratoire peut analyser plusieurs échantillons pour une personne présumée atteinte de tuberculose, mais chaque patient tuberculeux reçoit un ensemble défini de soins de la part de la clinique. Étant donné que le laboratoire et la clinique ont des flux de travail différents, des utilisateurs différents et des entités différentes à suivre (échantillons de test ou individus), il convient d'envisager des programmes distincts pour la saisie des données de laboratoire et la surveillance des cas de tuberculose. Tout patient tuberculeux recevant déjà un traitement pourrait être immédiatement inscrit dans un programme de surveillance des cas de tuberculose, mais un cas suspect ne serait inscrit dans le programme de surveillance des cas de tuberculose, qu'après qu'un test confirmé ait été signalé par le laboratoire dans le programme Laboratoire. S'il s'agissait d'un programme intégré de surveillance des cas de tuberculose et de dépistage de la tuberculose, la majorité des inscriptions seraient des cas suspects, et seuls certains recevraient un traitement.



Le système de suivi DHIS2 prend en charge ce type de comportement en permettant à la TEI d'être inscrite dans plusieurs programmes. Les Attributs du TEI peuvent être partagés ou distincts entre chaque programme. Différents groupes d'utilisateurs peuvent avoir accès à chaque programme en fonction de leurs tâches de déclaration. En outre, des listes de lignes pourraient être générées pour afficher l'inscription du TEI dans chaque programme distinct. Toutefois, dans la version 2.40 du DHIS2, il n'existe aucune méthode permettant d'analyser les instances d'entités suivies en fonction des valeurs des éléments de données dans plusieurs programmes.

