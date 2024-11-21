---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/docs/cvc_eir_design.md"
revision_date: "2021-12-01"
---

# Conception du système de suivi du registre électronique d’immunisation contre la Covid-19 contre{ #cvc-eir-tracker-design }

## Introduction { #introduction }

Le document intitulé « Conception du système d’immunisation contre la COVID-19 » donne un aperçu du design conceptuel utilisé dans la configuration d’un programme de suivi DHIS2 servant de registre électronique d’immunisation contre la COVID-19. Ce document est destiné aux responsables de la mise en œuvre du DHIS2 au niveau national et régional pour soutenir la mise en œuvre et la localisation du package. Les flux de travail au plan local, les lignes directrices nationales et celles des produits vaccinaux concernés doivent être pris en compte lors de la localisation et de l’adaptation de ce package de configuration.

Ce package a été développé en réponse à un besoin exprimé par les pays et les partenaires de surveiller l’adoption et l’équité en matière de vaccins contre la COVID-19 dans les groupes prioritaires et de suivre les individus jusqu’à la fin de leur schéma vaccinal.

Ce package vise à améliorer la rapidité, l’exactitude des données, l’extension de la couverture, l’efficience et l’efficacité de la distribution des vaccins contre la COVID-19. Il s’appuie sur le document [Orientations sur l’élaboration d’un plan national de déploiement et de vaccination applicable aux vaccins contre la COVID-19] (https://www.who.int/publications/i/item/WHO-2019-nCoV-Vaccine_deployment-2020.1) ainsi que sur les feedbacks des responsables de l’OMS et des CDC, et sur les normes et directives générales en matière de vaccination adaptées du package du registre d’immunisation du DHIS2.

Les directives et politiques nationales étant différentes, ce package doit être adapté au contexte national.

## Aperçu de la conception du système { #system-design-overview }

### Cas d’utilisation { #use-case }

Le modèle de données tracker du DHIS2 permet d’enregistrer et de suivre un individu à travers une série de services de santé fournis au fil du temps. Ce modèle peut être utilisé pour suivre le respect des calendriers de vaccination, conformément à la politique nationale et aux recommandations relatives aux produits, ainsi que pour recueillir des données solides au niveau individuel afin de soutenir l’analyse de la distribution, de l’adoption et de l’achèvement des vaccins en fonction des données démographiques, des conditions sous-jacentes et d’autres variables.

### Contenu { #content }

Ce package contient :

-   Le programme tracker qui enregistre l’individu et chaque événement de vaccination
-   Un ensemble d’indicateurs de programme qui couvre les exigences issues des orientations de l’OMS en matière de déploiement des vaccins
-   Un ensemble d’indicateurs de programme qui alimente un ensemble de données agrégées pour le suivi quotidien
-   Un ensemble de données agrégées pour le suivi quotidien
-   Un ensemble d’indicateurs basés sur l’ensemble de données agrégées
-   Un tableau de bord de suivi quotidien basé sur l’ensemble de données agrégées

### Utilisateurs cibles { #intended-users }

Le programme est conçu pour soutenir les utilisateurs au niveau des cliniques et des établissements, en dotant le personnel de meilleurs outils de prise de décision et en plaçant le client au centre du système d’information, tout en éliminant les redondances dans les rapports. Toutefois, en fonction de l’infrastructure et des ressources disponibles dans le pays, la saisie des données peut être complétée au niveau des districts sur la base de registres papier.

-   Utilisateurs cliniques : le programme de suivi du registre électronique d’immunisation est optimisé pour la saisie des données au point d’intervention.
-   Personnel des établissements : si la saisie des données dans le DHIS2 au point d’intervention n’est pas possible, la tâche peut être confiée au personnel préposé à cet effet. Les listes de travail sont conçues pour aider le personnel des établissements à surveiller les patients qui ont besoin d’un suivi ou qui sont en retard par rapport à leur schéma de vaccination.
-   Responsables d’établissements, bureaux de santé de district et personnel du programme national : les données générées par le programme alimentent des tableaux de bord standardisés qui permettent de suivre l’adoption des vaccins, les abandons et la désagrégation en fonction de l’âge, du genre et de la profession

Illustration du déroulement :

![Déroulement](resources/images/Covac_workflow.png)

Le déroulement des opérations varie d’un pays à l’autre. La conception du programme doit être revue et adaptée en fonction du contexte. Par exemple, le déroulement illustré ci-dessus suppose que les individus sont enregistrés dans le DHIS2 lorsqu’ils se présentent sur un site de vaccination pour recevoir leur première dose. Il peut également être envisageable de pré-enregistrer les individus éligibles dans le système en tant qu’instances d’entité suivies (p. ex., à partir d’un registre existant d’agents de santé).

## Configuration du programme Tracker { #tracker-program-configuration }

| Structure | Description |
| --- | --- |
| Inscription | Si une personne n’est pas encore enregistrée dans l’instance, elle est enregistrée et inscrite dans le registre d’immunisation en tant que TEI (personne de type TEI) et ses données sont saisies dans Inscription en tant qu’attributs, qui correspondent aux packages COVID-19 existants pour le DHIS2. Attributs TEI : Identifiant national, Identifiant unique, Prénom, Sexe, Date de naissance estimée, Date de naissance (âge), Numéro de téléphone portable, Adresse (actuelle), Région, Profession |
| Étape 1 du programme : Vaccination | Il s’agit d’une étape qui peut être répétée. Les données de cette étape sont saisies chaque fois qu’une personne est vaccinée. Date de l’événement = date à laquelle la dose a été administrée \ date d’échéance = permet de programmer la dose suivante |
| Section 1.1 — Affections sous-jacentes | Informations sur les états de santé et/ou les affections sous-jacentes préexistantes qui ont été déterminées comme exposant à un risque significativement plus élevé d’infection grave ou de décès. Ce package contient les mêmes affections préexistantes que celles utilisées dans le reste des packages COVID. |
| Section 1.2 — Questions préalables à la vaccination | Pour la première dose, cette section demande si le client a eu la COVID-19 au cours des 90 derniers jours. Après la deuxième dose, elle demande également s’il y a |
| Section 1.3 — Vaccination | Enregistre les détails sur le type de vaccin fourni ainsi que le numéro de lot, la date d’expiration, et suggère une date pour la prochaine vaccination. |

### Éléments de données dans la phase de vaccination { #data-elements-in-the-vaccination-stage }

| Élément de données (Nom du formulaire) | Liés à des indicateurs | Liés à des certificats | Liés à des règles du programme |
| --- | --- | --- | --- |
| Dose administrée le (date de la vaccination) — Pas un élément de données | Oui | Oui | Oui |
| La patiente est-elle enceinte ou allaitante ? | Non | Non | Oui |
| Âge gestationnel (semaines) | Non | Non | Oui |
| Des affections sous-jacentes ? | Non | Non | Oui |
| Maladie cardiovasculaire, hypertension comprise | Non | Non | Oui |
| Maladie pulmonaire chronique | Non | Non | Oui |
| Diabète | Non | Non | Oui |
| Immunodéficience | Non | Non | Oui |
| Malignité | Non | Non | Oui |
| Maladie neurologique ou neuromusculaire chronique | Non | Non | Oui |
| Maladie rénale | Non | Non | Oui |
| Autres (veuillez spécifier) | Non | Non | Oui |
| Le patient a-t-il été infecté par la COVID-19 au cours des 90 derniers jours ? | Non | Non | Oui |
| Le patient a-t-il eu une réaction allergique grave (anaphylaxie) ou une réaction allergique immédiate, même si elle n’était pas grave, après avoir reçu la première dose de vaccin ? | Non | Non | Oui |
| Vaccin administré | Oui | Oui | Oui |
| Nom du vaccin | Oui | Oui | Oui |
| Veuillez expliquer pourquoi ce client a reçu des doses de différents produits | Non | Non | Oui |
| Numéro de lot du vaccin | Non | Oui | Non |
| Date d’expiration du vaccin | Non | Non | Non |
| Numéro de doses | Oui | Oui | Oui |
| Nombre total de doses requises pour ce vaccin | Non | Oui | Oui |
| Est-ce la dernière dose ? | Oui | Non | Oui |
| Date suggérée par le COVAC pour la dose suivante | Non | Non | Oui |
| Le client a-t-il eu une réaction indésirable après l’immunisation ? | Non | Non | Oui |

### Produits vaccinaux du programme { #vaccine-products-in-the-program }

Les produits propres à la COVID-19 disponibles dans le pays et les schémas vaccinaux varient selon les pays. Ce package comprend des produits vaccinaux conformes à la documentation disponible auprès de l’OMS, qui continuera à évoluer au fur et à mesure de [l’arrivée de vaccins sur le marché.](https://extranet.who.int/pqweb/sites/default/files/documents/Status_COVID_VAX_16Feb2021.pdf)

Afin de mieux démontrer la fonctionnalité, ces caractères génériques ont été configurés sur la base de cinq produits vaccinaux existants, mais il est important de vérifier et de configurer le programme en fonction des directives nationales d’adoption du produit.

| NOM du vaccin | Code d’option | Fabricant du vaccin | Code d’option | Recommandation en matière d’âge | Intervalle entre les doses | Nombre de doses |
| --- | --- | --- | --- | --- | --- | --- |
| AZD1222/AstraZeneca | astrazeneca | AstraZeneca | astrazeneca | 18 | 10 jours (8-12) | 2 |
| AZD1222/AstraZeneca | astrazeneca | SKBio Astra Zeneca | skbioastrazeneca | 18 | 10 (8-12) | 2 |
| BNT162b2 / COMIRNATY Tozinameran (INN) / BioNTech/Pfizer | biontechpfizer | BioNtech/Pfizer | biontechpfizer | 16 | 21 | 2 |
| mRNA-1273 / Moderna | moderna | Moderna | moderna | 18 | 28 | 2 |
| Sputnik V / Gamaleya | gamaleya | Gamaleya | gamaleya | 18 | 21 | 2 |
| Vaccin contre le SARS-CoV-2 (cellule Vero), inactivé / Sinopharm | sinopharm | Sinopharm | sinopharm | 18 | 21 jours (21-28) | 2 |

### Comment adapter les caractères génériques aux produits vaccinaux disponibles ? { #how-to-adapt-the-placeholders-to-the-available-vaccine-products }

#### Noms dans le formulaire { #names-in-the-form }

Pour que le nom dans le formulaire reflète les produits utilisés dans le pays, vous devez d’abord modifier les ensembles d’options « Fabricants de vaccins COVAC » et « Nom du vaccin COVAC » et changer les options en noms appropriés pour le pays.

![Ensemble d’options](resources/images/Covac_optionset_1.png)

![Ensemble d’options](resources/images/Covac_optionset_2.png)

#### Attribution automatique de fabricants et de marques à des noms { #auto-assigning-manufacturers-and-brands-to-names }

Les fabricants et les marques sont attribués automatiquement lorsqu’un produit vaccinal est sélectionné par des règles du programme basées sur le vaccin choisi, à moins que le vaccin ait plus d’un fabricant disponible. Dans ce cas, une règle du programme masque les options qui ne sont pas pertinentes et l’agent doit choisir le nom correct du fabricant, comme c’est le cas pour AstraZeneca.

##### Règle d’attribution automatique { #auto-assign-rule }

Par exemple, la règle du programme « Attribuer la marque et les fabricants à BioNtech/Pfizer » attribue le fabricant BioNtech/Pfizer lorsque « Comirnaty, Tozinameran » est sélectionné.

Elle utilise l’expression : `d2:hasValue( 'Vaccine_type' ) == true && #{Vaccine_type} == 'BIONTECHPFIZER'`

L’action de cette règle du programme consiste à attribuer à l’élément de données « Fabricant du vaccin » la valeur « BIONTTECHPFIZER », qui est le code d’option pour « BioNTech/Pfizer » ainsi que « BioTech/Pfizer » pour la marque.

##### Règle de masquage des options { #hide-options-rule }

Actuellement, la seule règle de ce type est « Attribuer la marque/Masquer les options AstraZeneca », car ce produit a deux fabricants différents (AstraZeneca et SK Bio Astra Zeneca). 
Cela signifie qu’au lieu d’attribuer un fabricant, la règle du programme masque les fabricants non pertinents et permet à l’agent de sélectionner l’un des deux fabricants actuellement disponibles.

#### Alerte relative à l’âge { #age-alert }

Selon le vaccin, il peut y avoir des limites d’âge inférieures. Si un vaccinateur administre une dose à une personne n’appartenant pas à la tranche d’âge recommandée, un avertissement est émis. Pour modifier cela, veuillez corriger les règles du programme :

« Si l’attribut Âge est inférieur à 18, prévenir qu’Astra Zeneca est recommandé pour les personnes âgées de 18 ans et plus »

« Si l’attribut Âge est inférieur à 16, prévenir que BiontechPfizer est recommandé pour les personnes âgées de 16 ans et plus » « Si l’attribut Âge est inférieur à 18, prévenir que Moderna est recommandé pour les personnes âgées de 18 ans et plus » « Si l’attribut Âge est inférieur à 18, prévenir que Gamaleya est recommandé pour les personnes âgées de 18 ans et plus » « Si l’attribut Âge est inférieur à 18, prévenir que Sinopharm est recommandé pour les personnes âgées de 18 ans et plus »

Les règles utilisent toutes une expression similaire :

`(#{Age_Calculé} < 18 ) && (#{Type de_Vaccine} =='ASTRAZENECA')`

où vous devez modifier le nombre, 18 dans ce cas, pour qu’il corresponde à l’âge requis.

L’action pour ces règles du programme consiste à afficher un avertissement : « Ce produit de vaccination est recommandé pour les personnes de 18 ans et plus ».

Vous devez également modifier cet avertissement pour qu’il corresponde aux directives nationales les plus appropriées.

#### Attribuer une date pour la dose suivante { #assign-a-date-for-next-dose }

Il n’y a actuellement aucun moyen pour un tracker d’attribuer une date pour l’événement suivant sur la base d’un élément de données. Nous avons ainsi configuré le tracker pour qu’il planifie automatiquement la date de la vaccination suivante 10 jours après la première dose, en supposant que le produit le plus utilisé serait Astra-zeneca. Une modification doit être apportée pour qu’il corresponde à l’intervalle en vigueur dans le pays, en changeant le paramètre de l’étape du programme de vaccination dans l’application de maintenance.

![Configuration du programme](resources/images/Covac_date_setting.png)

Il existe également un élément de données qui attribue automatiquement, à l’aide de règles du programme, une date recommandée en fonction du produit vaccinal. Pour modifier cela, il faut éditer la règle du programme :

« Attribuer une suggestion de date pour la prochaine dose AstraZeneca » (il existe une règle pour chaque produit) “.../dhis-web-maintenance/#/edit/programSection/programRule/ZT3tLrXXadf”

La règle du programme comporte deux actions

Première action : Afficher un avertissement à côté de l’élément de données « date suggérée pour la dose suivante » avec le texte « La dose suivante doit être administrée dans 10 jours »

Modifiez ce texte en fonction des besoins.

Deuxième action : Attribuer une valeur à l’élément de données « date suggérée pour la dose suivante » avec l’expression d2:addDays( V{event_date}, 10 )

Modifiez le nombre 10 avec le nombre de jours devant être attribué au vaccin disponible.

#### Dernière dose { #last-dose }

Il existe actuellement un élément de données oui/non appelé « Dernière dose » ; cet élément permet aux indicateurs de déterminer qu’un produit a terminé son schéma d’immunisation. Actuellement, tous les produits ont deux doses, et par conséquent, nous avons fait en sorte qu’après l’injection d’une deuxième dose, l’élément de données « Dernière dose » soit automatiquement coché comme « Oui ». Nous avons également masqué cet élément de données pour la première dose.

Pour modifier cet avertissement, éditez la règle du programme : « S’il s’agit de la deuxième dose, indiquez qu’il s’agit de la "dernière dose" pour tous les produits vaccinaux »

dhis-web-maintenance/#/edit/programSection/programRule/PJjKiFrvfuN

L’expression : `d2:hasValue( 'Dose_number' ) == true && #{Dose_number} == 'DOSE2'`

indique que si un agent sélectionne le numéro de doses donné comme étant la deuxième dose, il déclenche une action « attribuer une valeur » qui ajoute la valeur « vrai » à l’élément de données « Dernière dose » et à la variable de la règle du programme « Last_dose »

Pour modifier cela, éditez l’expression pour filtrer les vaccins non utilisés ou ayant un schéma différent.

#### Nombre total de doses { #total-number-of-doses }

L’élément de données « Nombre total de doses requises pour ce vaccin » est un élément de données rempli automatiquement qui affiche la quantité de doses requises pour le schéma vaccinal de ce vaccin. Actuellement, tous les vaccins ont un schéma de deux doses. Cependant, il existe une règle individuelle pour chaque vaccin en cas de changement ultérieur :

Pour modifier cela, éditez la règle correspondante : Attribuer un numéro de dose à NOMDUPRODUIT

et l’expression : `d2:hasValue( 'Vaccine_type' ) == true && #{Vaccine_type} == 'astrazeneca'`

Si le programme correspond au filtre, l’action attribuera une valeur à l’élément de données « Nombre total de doses ». Actuellement, toutes les règles attribuent la valeur « 2 » et masquent l’option pour une troisième dose.

#### Niveau d’accès { #access-level }

Le programme a été configuré en tant que programme « protégé », ce qui signifie que les utilisateurs peuvent effectuer des recherches dans d’autres unités d’organisation que celles auxquelles ils ont droit. Toutefois, s’ils veulent accéder à des dossiers dans un autre établissement, ils doivent utiliser la fonction « briser la vitre » et noter les raisons pour lesquelles ils accèdent à ces dossiers d’une autre unité d’organisation.

Notez que la fonction [briser la vitre n’est pas prise en charge par Android](https://docs.dhis2.org/2.35/en/dhis2_android_capture_app/programs.html#breaking-the-glass) et que les utilisateurs d’Android ne peuvent pas rechercher d’autres unités d’organisation lorsque le programme est défini comme protégé.

#### Détails de l’inscription { #enrollment-details }

La date d’inscription est égale à la « date d’enregistrement ». Il est prévu que l’utilisateur saisisse la date d’inscription lorsque la personne s’inscrit dans le programme du registre d’immunisation. Dans la majorité des cas, la date d’inscription coïncide avec la date de la première vaccination, à moins que les clients ne soient inscrits à l’avance dans le registre de vaccination.

Comme le programme utilise la date de naissance pour calculer les indicateurs du programme, elle est configurée comme obligatoire. Si une personne ne connaît pas sa date de naissance, il est possible de cocher la case « Date de naissance estimée » et d’entrer son âge approximatif ou une date de naissance approximative.

Bien que les informations sur l’inscription soient censées être complétées lors de la première inscription d’un cas, les valeurs des attributs peuvent être mises à jour à tout moment au cours d’une inscription active si de nouvelles informations sont disponibles (par exemple, les coordonnées).

#### Identifiants { #identifiers }

Le programme est configuré avec deux types d’identifiants uniques. Des identifiants supplémentaires peuvent être ajoutés au programme en fonction du contexte du pays.

**Identifiant unique** : identifiant généré automatiquement qui est unique pour l’ensemble du système (par exemple, l’instance du DHIS2 utilisée). Cet attribut TEI est configuré pour générer la valeur de l’attribut sur la base d’un modèle. Dans la version précédente du package, l’identifiant unique générait un numéro composé d’un préfixe et d’un nombre aléatoire, "PEV*" + RANDOM(########)". La dernière version a remplacé cet attribut par un motif séquentiel qui améliore les performances pour les grandes implémentations "PEV*"" + RANDOM(########)".

**Identifiant national** : cet identifiant est actuellement saisi manuellement et doit être adapté aux besoins de validation locaux.

![Étape d’inscription](resources/images/Covac_enrollment.png)

### Étape 1 du programme : Vaccination (reproduisible) { #program-stage-1-vaccination-repeatable }

Section 1.1 — Affections sous-jacentes.

![Affections sous-jacentes](resources/images/Covac_underlying.png)

Les affections sous-jacentes énumérées ici sont basées sur les directives pour les packages de surveillance des cas de COVID et de recherche des cas contacts. Elles incluent également des états de santé tels que la grossesse et l’allaitement. Les options de gestation et d’allaitement n’apparaissent que pour les femmes. Une fois que l’une des affections sous-jacentes (à l’exception de la grossesse) est sélectionnée, elle reste sélectionnée à l’étape suivante (car il s’agit d’une étape reproduisible) et est répertoriée dans la case de l’indicateur.

#### Section 1.2 — Questions préalables à la vaccination { #section-12-pre-immunization-questions }

Les questions préalables à la vaccination sont destinées à être remplies lors de chaque « événement », qui représente un service d’immunisation. En fonction des réponses sélectionnées, les règles du programme sont déclenchées pour fournir une aide à la décision

Actuellement, les deux questions sont :

« Le patient a-t-il été infecté par la COVID-19 au cours des 90 derniers jours ? »

Si la réponse est Oui, un avertissement s’affiche : « Le vaccin est recommandé aux personnes non infectées par la COVID-19 depuis au moins 90 jours »

Et

« Le patient a-t-il eu une réaction allergique grave (anaphylaxie) ou une réaction allergique immédiate, même si elle n’était pas grave, après avoir reçu la première dose du vaccin ? » qui n’est visible pour les patients que lorsqu’ils reçoivent leur deuxième dose (ou potentiellement troisième dose ou dose de rappel). Si « oui » est sélectionné, cela déclenche l’avertissement « Veuillez suivre les directives nationales pour les enquêtes sur les MAPI »

![Questions préalables à la vaccination](resources/images/Covac_preimmunization.png)

#### Section 1.3 — Informations sur la vaccination { #section-13-vaccination-information }

Cette section présente les services d’immunisation fournis. Elle enregistre les informations suivantes :

Vaccin administré (à l’aide de l’ensemble d’options « Nom du vaccin »)

Fabricants du vaccin (à l’aide de l’ensemble d’options « Fabricants de vaccins », remplissage automatique)

Marque de vaccin (à l’aide de l’ensemble d’options « Marque du vaccin »)

Le numéro de lot de cette dose

La date d’expiration de la dose

Le numéro de dose (1ère, 2ème ou rappel)

Le nombre de doses totales requises pour ce produit vaccinal (remplissage automatique)

Un élément de données pour confirmer s’il s’agit de la dernière dose du traitement (remplissage automatique)

Un élément de données calculé automatiquement et donnant une suggestion pour la prochaine dose (remplissage automatique)

Un élément de données demandant si le client a eu une réaction indésirable à la suite de l’immunisation (utilisé lors de la surveillance d’un patient immédiatement après avoir été vacciné)

Un élément de données pour compléter l’identification de l’agent de santé

![Section relative à la vaccination](resources/images/Covac_vaccination.png)

Si un patient reçoit un type de vaccin différent de celui enregistré lors de la première injection, un avertissement s’affiche : « Le type de vaccin que vous avez sélectionné n’est pas le même que le type de vaccin précédent que cette personne a reçu. La dernière dose administrée était "NOM DU VACCIN PRÉCÉDEMMENT ADMINISTRÉ" » Cela déclenche également un élément de données supplémentaire « Veuillez expliquer pourquoi ce client a reçu des doses de différents produits »

Une fois qu’un client a reçu la première dose, l’option pour la première dose est masquée dans l’élément de données. Pour les produits à seulement deux doses dans le schéma, la troisième est masquée. Les pays peuvent effectuer une configuration en fonction des produits vaccinaux qu’ils adoptent.

#### Planification d’événements { #scheduling-events }

L’étape est configurée pour « Demander à l’utilisateur de créer un nouvel événement lorsqu’une étape est terminée », ce qui fait apparaître une fenêtre contextuelle pour la planification du rendez-vous de suivi. Les « jours d’intervalle standard » sont actuellement définis sur 10 afin que la date du prochain rendez-vous (événement) soit programmée par défaut à 10 jours de la date de l’événement en cours, mais cette date peut être modifiée en fonction du produit utilisé.

### Groupes d’utilisateurs { #user-groups }

Le programme est fourni avec quatre groupes d’utilisateurs :

-   _COVAC — Administrateur des métadonnées d’immunisation contre la Covid :_ A le droit de modifier les métadonnées du package, mais pas d’y saisir des données
-   _COVAC — Saisie des données d’immunisation contre la Covid :_ A le droit de saisir des données dans le tracker
-   _COVAC — Analyse des données d’immunisation Covid :_ A accès aux tableaux de bord, mais ne peut pas saisir de données
-   _COVAC — Administrateur des données d’immunisation contre la Covid-19 :_ Il s’agit d’un groupe d’administrateurs partagés entre le tracker et l’agrégation. Les membres de ce groupe peuvent afficher les données dans les modules de suivi et d’agrégation, et capturer des données dans le module d’agrégation uniquement. Ce groupe d’utilisateurs est configuré pour les utilisateurs qui lancent le tracker pour agréger des scripts et accéder à l’ensemble de données via l’application de saisie de données.

Ces différents groupes doivent être adaptés aux besoins nationaux.

## Impression de certificats { #certificate-printing }

Le DHIS2 ne prend pas en charge l’impression d’un certificat de vaccination ou la génération d’un certificat électronique en tant que fonctionnalité principale, mais plusieurs pays ont adapté avec succès la plateforme afin de fournir des certificats numériques et imprimés.

### Notifications par SMS { #sms-notifications }

Le DHIS2 dispose d’un module de notifications par SMS. Toutefois, pour pouvoir utiliser les notifications, la configuration d’une passerelle SMS s’avère nécessaire. Consultez la documentation sur les passerelles SMS [ici](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/sms.html)

Le programme comprend un rappel par défaut, 7 jours avant la date d’échéance prévue pour un événement de vaccination :

« Madame, Monsieur, NOM DU CLIENT, vous avez rendez-vous pour votre vaccination contre la COVID-19 le DATE D’ÉCHÉANCE à NOM DE L’ÉTABLISSEMENT »

Et un message, 3 jours après la date d’échéance prévue :

« Madame, Monsieur, A{TfdH5KvFmMy}, vous aviez rendez-vous pour une dose de vaccin contre la COVID-19 le V{due_date}. Si vous n’avez pas reçu votre vaccin, veuillez contacter V{org_unit_name} dès que possible. Dans le cas contraire, vous pouvez ignorer ce message »

**REMARQUE :** En raison des limitations actuelles du module SMS, le message prévu trois jours après la date d’échéance sera envoyé, que l’événement ait eu lieu ou non. Jusqu’à ce que ce problème soit résolu, une solution de contournement consiste à configurer un script cronjob qui vérifie les événements en retard et planifie un message.

### Listes de travail { #working-lists }

Le programme comprend trois listes de travail personnalisées. Ces listes sont destinées à faciliter la gestion de la journée de travail des agents de santé au point d’intervention avec des listes de clients en fonction de leur calendrier de vaccination, et à mettre en évidence les rendez-vous en retard.

Les listes sont personnalisées selon la fonction « date d’échéance ». La date d’échéance est la date attribuée pour le prochain événement et elle est effectuée dès que le premier événement est terminé. Actuellement, le système sélectionne automatiquement un rendez-vous, 10 jours après la première vaccination, et l’agent ou le clinicien doit modifier cette date, si nécessaire. Il est donc important que la planification soit faite correctement pour l’utilisation des listes de travail.

Tous les clients enregistrés actifs : les clients enregistrés dans le programme de vaccination contre la COVID et ceux dont l’inscription n’a pas été terminée. On suppose que les clients ayant reçu toutes les doses de leurs vaccins auront terminé leur inscription au programme de vaccination. L’inscription incomplète sera donc indicative de tous les clients qui n’ont pas reçu une deuxième dose (ou la dernière dose pour les vaccins avec des schémas différents), indépendamment du fait qu’ils soient dans les délais ou en retard.

Clients avec rendez-vous : ceux qui ont une étape du programme de vaccination prévue dans le futur ou la journée en cours

Clients en retard d’une dose de vaccin : ceux qui ont un rendez-vous prévu dans le passé et sont donc en retard pour recevoir une dose de vaccin

Terminés : Ceux dont l’inscription est terminée

## Analyse { #analytics }

Pour optimiser les performances pour les déploiements à grande échelle prévus et l’utilisation de stratégies d’administration de vaccins de type campagne à grand volume, ce package est conçu pour servir des objets d’analyse et des tableaux de bord via le modèle de données agrégées.

En plus d’assurer des performances maximales pour les utilisateurs d’analyse qui accèdent aux tableaux de bord en temps quasi réel alors que la saisie de données à grand volume via le tracker est probablement en cours, l’agrégation des données de suivi et la diffusion des tableaux de bord via le domaine agrégé ont l’avantage supplémentaire de rendre les dimensions de données disponibles pour les utilisateurs d’analyses (par exemple, sur la base de catégories pour la désagrégation).

Afin de fournir des analyses COVID-19 à partir des données sources du programme de suivi du REI COVID-19, le package comprend les composants suivants : un ensemble de données agrégées avec des éléments de données et des combinaisons de catégories (afin de servir de cible pour pousser les données de suivi vers le modèle agrégé) ; un tableau de bord basé sur des indicateurs de domaine agrégés (remplace le tableau de bord basé sur un tracker (basé sur des indicateurs de programme) dans les versions précédentes) ; un groupe d’indicateurs de programme avec des attributs mappés sur les éléments de données/COC agrégés cibles

### Tableau de bord { #dashboard }

Ce package contient un tableau de bord de surveillance quotidienne COVAC simplifié (iBWlFCvvtkH) pour faciliter l’analyse quotidienne/en temps quasi réel pendant les activités d'administration de vaccins en mode campagne. Ce tableau de bord est conçu pour être aussi léger que possible, au service d’un ensemble de mesures de base optimisées pour le suivi quotidien des opérations de livraison de vaccins. Les indicateurs du tableau de bord ont été sélectionnés en tant que sous-ensemble des directives de surveillance incluses dans les orientations de l’OMS sur l’élaboration d’un plan national de déploiement et de vaccination applicables aux vaccins contre la COVID-19. [Orientations sur l’élaboration d’un plan national de déploiement et de vaccination (PNDV) applicable aux vaccins contre la COVID-19 de l’OMS] (https://www.who.int/publications/i/item/WHO-2019-nCoV-Vaccine_deployment-2020.1). Le « tableau de bord de suivi quotidien COVAC » ((iBWlFCvvtkH) est entièrement configuré sur la base d’indicateurs appartenant au groupe d’indicateurs COVAC – Quotidien (doQTIS8KJQH). Cela permettra aux pays de mapper les indicateurs de tableau de bord à leur propre ensemble d’éléments de données sous-jacents, si l’agrégat cible de l’ensemble de données et les éléments de données sont personnalisés pour une implémentation locale.

Pour un tableau de bord de suivi complet couvrant des aspects supplémentaires des conseils relatifs au suivi du PNDV de l’OMS (tels que la couverture vaccinale et l’adoption des vaccins par les groupes cibles, les indicateurs sur les événements indésirables, l’approvisionnement et la chaîne du froid), reportez-vous au [package de métadonnées du tableau de bord principal/agrégées de COVAC](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-aggregate/version-110/design.html).

Si votre instance dispose déjà d’un tableau de bord de la version précédente de ce package, il est recommandé de le supprimer ou d’en limiter l’accès à quelques utilisateurs. Pour obtenir des instructions sur la suppression des tableaux de bord, consultez le [guide d’installation](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-immunization-registry-tracker/installation.html)

### Ensemble de données agrégées { #aggregate-data-set }

Un ensemble de données agrégées « COVAC — Données tracker du REI (agrégées) » a été configuré avec une fréquence quotidienne comme cible pour pousser les valeurs de données calculées basées sur les indicateurs du programme de suivi vers le domaine agrégé. L’ensemble de données contient les éléments de données suivants :

1. Personnes ayant reçu une 1ère dose
2. Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel
3. Personnes ayant reçu la dernière dose recommandée
4. Personnes souffrant d'affections sous-jacentes

![Saisie de données agrégées](resources/images/covac_agg_data_entry.png)

Dans la mesure du possible, les combinaisons de catégories, les catégories (et leurs combinaisons d’options de catégorie et options de catégorie associées) ont été réutilisées à partir du [package de métadonnées du tableau de bord principal/agrégées COVAC](https://docs.dhis2.org/en/topics/metadata/covid-19-vaccine-delivery/covac-aggregate/version-110/design.html)  existant pour faciliter l’analyse des éléments de données de ces deux packages.

Ces éléments de données et COC devraient être alimentés à partir des indicateurs du programme tracker, comme décrit ci-dessous.

### Indicateurs de programme { #program-indicators }

Un groupe d’indicateurs de programme, COVAC-Tracker, à agréger (NXBR4r6MwAO) a été configuré et mappé (via des attributs) pour faciliter le transfert des valeurs de données vers les éléments de données et les COC du domaine agrégé cible, comme décrit ci-dessus. Un exemple de ce mappage est le suivant :

| Indicateur de programme (nom) | UID de l’indicateur de programme | Poussé vers les éléments de données agrégées (nom) | UID des éléments de données agrégées | Mappé à l’indicateur (nom) | UID de l’indicateur |
| --- | --- | --- | --- | --- | --- |
| Nombre de personnes recevant une première dose (femmes 0-59 ans) | RJ6pdxga9Od | COVAC — Personnes ayant reçu une 1ère dose | RjT7dmzunF4 | COVAC — Personnes ayant reçu une 1ère dose | GeAtojrj7Yy |
| Nombre de personnes recevant une première dose (femmes 60 ans et +) | x4L0LuEBHhW | COVAC — Personnes ayant reçu une 1ère dose | RjT7dmzunF5 | COVAC — Personnes ayant reçu une 1ère dose | GeAtojrj7Yy |
| Nombre de personnes recevant une première dose (hommes 0-59 ans) | hqm8znlAzkT | COVAC — Personnes ayant reçu une 1ère dose | RjT7dmzunF6 | COVAC — Personnes ayant reçu une 1ère dose | GeAtojrj7Yy |
| Nombre de personnes recevant une première dose (hommes 60 ans et +) | aIIHyDy8AMW | COVAC — Personnes ayant reçu une 1ère dose | RjT7dmzunF7 | COVAC — Personnes ayant reçu une 1ère dose | GeAtojrj7Yy |
| Nombre de personnes recevant une deuxième ou une troisième dose, ou une dose de rappel (femmes 0-59 ans) | xY4T9hHXNji | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | zmKNuqgsq8N | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | ddZjJCwXf6k |
| Nombre de personnes recevant une deuxième dose, une troisième dose ou une dose de rappel (femmes 60 ans et +) | h9G7i6mQKef | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | zmKNuqgsq8N | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | ddZjJCwXf6k |
| Nombre de personnes recevant une deuxième ou une troisième dose, ou une dose de rappel (hommes 0-59 ans) | MGjwUUNsE60 | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | zmKNuqgsq8N | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | ddZjJCwXf6k |
| Nombre de personnes recevant une deuxième ou une troisième dose, ou une dose de rappel (hommes 60 ans et +) | qh0kIjHZbP8 | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | zmKNuqgsq8N | COVAC — Personnes ayant reçu une 2ème dose, une 3ème dose ou une dose de rappel | ddZjJCwXf6k |
| Nombre de personnes qui ont reçu la dernière dose recommandée pour le produit vaccinal concerné (femmes 0-59 ans) | Zp39TSOR8eW | COVAC — Personnes ayant reçu la dernière dose recommandée | CB46jykiEye | COVAC — Personnes ayant reçu la dernière dose recommandée | OAZXVEjEEoD |
| Nombre de personnes ayant reçu la dernière dose recommandée pour le produit vaccinal concerné (femmes 60 ans et +) | XFUvVgqPukT | COVAC — Personnes ayant reçu la dernière dose recommandée | CB46jykiEye | COVAC — Personnes ayant reçu la dernière dose recommandée | OAZXVEjEEoD |
| Nombre de personnes qui ont reçu la dernière dose recommandée pour le produit vaccinal concerné (hommes 0-59 ans) | FZNIlzPRMmL | COVAC — Personnes ayant reçu la dernière dose recommandée | CB46jykiEye | COVAC — Personnes ayant reçu la dernière dose recommandée | OAZXVEjEEoD |
| Nombre de personnes ayant reçu la dernière dose recommandée pour le produit vaccinal concerné (hommes 60 ans et +) | zovL7DKBRuK | COVAC — Personnes ayant reçu la dernière dose recommandée | CB46jykiEye | COVAC — Personnes ayant reçu la dernière dose recommandée | OAZXVEjEEoD |
| Personnes souffrant d'affections sous-jacentes | Zn0UuSRYyJw | COVAC — Personnes souffrant d'affections sous-jacentes | OUI05zSKrqk | COVAC — Personnes souffrant d'affections sous-jacentes | KIgI3EPjs2T |

Des indicateurs de programme supplémentaires ont été configurés pour permettre une analyse ad hoc des données du tracker (par exemple, les taux de couverture calculés sur la base des données du tracker, etc.). Cependant, ces indicateurs de programme ne sont pas utilisés dans le tableau de bord COVAC - Suivi quotidien.

## Transfert des données de domaine tracker agrégées vers des valeurs de données de domaine agrégées { #transferring-aggregated-tracker-domain-data-to-aggregate-domain-data-values }

En plus des métadonnées fournies ci-dessus, les implémentations nécessiteront un mécanisme pour pousser les valeurs d’indicateur de programme du domaine de suivi vers l’ensemble de données agrégées cible. Vous trouverez plus d’informations à ce sujet dans ce chapitre du Guide de mise en œuvre du DHIS2 : [Intégration des données tracker et des données agrégées](https://docs.dhis2.org/en/implement/maintenance-and-use/tracker-and-aggregate-data-integration.html#how-to-saving-aggregated-tracker-data-as-aggregate-data-values)

## Considérations relatives à l'implémentation avec des appareils Android { #considerations-for-when-implementing-with-android-devices }

### Niveau d’accès « protégé » { #access-level-protected }

La fonctionnalité « briser la vitre » n’est pas encore prise en charge dans l’application de capture Android du DHIS2 à partir de la version 2.3. Si le programme est configuré comme « Protégé », le comportement par défaut pour Android sera le même que si le programme est configuré comme « Fermé ». Cela signifie qu’un utilisateur Android ne pourra pas lire ou modifier les inscriptions d’une TEI en dehors de son unité d'organisation. Les TEI enregistrées dans une unité d’organisation de recherche seront renvoyées par la recherche de type TE, mais si le programme est fermé ou protégé, l’utilisateur ne sera pas autorisé à voir ou à créer une nouvelle inscription. Si les utilisateurs d’Android doivent pouvoir accéder à la TEI en dehors de leur unité d'organisation de capture de données, le programme doit être configuré avec le niveau d’accès « Ouvert ». Suivez l’état de ce problème sur [Jira](https://jira.dhis2.org/browse/ANDROAPP-657)

### Date d’échéance de la dose { #dose-due-date }

La description de la date d’échéance ne s’affiche pas correctement sur Android et au lieu de préciser « Date d’échéance de la dose », elle indique « Date d’échéance » [Lien vers jira] (https://jira.dhis2.org/browse/ANDROAPP-3620)

### Identifiants de réserve { #reserve-ids }

L’identifiant unique de ce package est généré automatiquement et utilise le modèle "DATE_ACTUELLE(aaaa-MM-jj)-"-"-SEQUENTIEL(#####)". Avec les appareils Android, les valeurs de ces ID uniques générés par le système sont réservées à l’avance pour chaque appareil, afin de garantir que les valeurs sont uniques pour l’ensemble de l’instance. Cela signifie que la valeur de la date et du numéro de séquence ne correspondront pas nécessairement à la date du jour et à l’ordre chronologique de réception du vaccin par un patient. Vous pouvez trouver plus d’informations à ce sujet [ici] (https://docs.dhis2.org/en/implement/implementing-with-android/dhis2-configuration-for-android.html#configuration_reserved_id)
