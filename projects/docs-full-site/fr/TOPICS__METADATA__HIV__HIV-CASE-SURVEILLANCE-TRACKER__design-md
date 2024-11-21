---
edit_url: "https://github.com/dhis2-metadata/HIV_CS-TRK-HIV_Case_Surveillance/blob/master/docs/hiv_case_surveillance_design.md"
revision_date: "2021-12-14"
---

# Conception du système de package des métadonnées pour la surveillance des cas de VIH { #hiv_cs_design }

## Contexte et objectif { #background-and-purpose }

Le système de surveillance des cas de VIH a été conçu pour soutenir la mise en œuvre des [directives consolidées de l’OMS concernant le suivi des patients atteints de VIH et la surveillance des cas centrés sur la personne (2017)](http://www.who.int/hiv/pub/guidelines/person-centred-hiv-monitoring-guidelines/en/) et des [directives consolidées d’information stratégique sur le VIH : renforcer l’impact par le suivi et la gestion des programmes](https://apps.who.int/iris/handle/10665/331697) mises à jour en 2020, ainsi que du Kit d’accélération numérique sur le VIH, qui n’a pas encore été publié.

La surveillance des cas de VIH est liée au suivi des patients, tout en étant distincte de celui-ci ; elle désigne la « déclaration d’un diagnostic initial d’infection par le VIH et d’événements sentinelles définis de la part de chaque personne diagnostiquée séropositive à un organisme de santé public chargé de surveiller et de contrôler l’épidémie. Les principaux événements sentinelles comprennent le diagnostic de VIH, le début de la prise en charge, l’initiation du TAR, la suppression virale et le décès. Les informations de chaque cas sont reliées dans le temps et conservées sous forme de données individuelles dans une base de données infranationale et/ou nationale. Dans certains pays, la surveillance des cas de VIH est désignée sous le nom de notification ou de signalement des cas, en particulier lorsqu’elle se limite au signalement de nouveaux diagnostics de VIH sans collecte de données longitudinales. La capacité à relier des notifications ou signalements des événements sentinelles à un cas dans le temps et à maintenir ces données sous forme désagrégées à un niveau individuel sont les caractéristiques distinctives des systèmes de surveillance des cas de VIH. »

Les principes de base du fonctionnement s’appuient sur les [directives consolidées de l’OMS relative à la surveillance du VIH centrée sur la personne](https://www.who.int/hiv/pub/guidelines/person-centred-hiv-monitoring-guidelines/en/) et leurs annexes correspondantes, tout en s’inspirant du [kit d’accélération numérique sur le VIH](https://www.who.int/reproductivehealth/publications/digital-accelerator-kits/en/) à paraître.

## Présentation de la conception du système { #system-design-overview }

### Cas d’utilisation { #use-case }

Les exigences relatives au suivi d’un cas individuel dans le temps et la mise en relation des événements sentinelles clés avec ce cas nécessitent l’utilisation de normes d’identification uniques, éventuellement composées d’un ou plusieurs identifiants uniques et/ou d’informations d’identification du patient. Le modèle des données de suivi du DHIS2 a pour but de répondre à ces exigences. Ce programme est conçu pour recueillir les éléments de données minimaux nécessaires en vue de produire les indicateurs requis identifiés par les [directives consolidées pour le suivi du VIH centré sur la personne](https://www.who.int/hiv/pub/guidelines/person-centred-hiv-monitoring-guidelines/en/). \
Le programme comprend un niveau basique d’aide à la décision et des invites pour guider les pays qui l’utiliseront dans un cadre clinique, ce qui augmentera la nécessité de saisir des données supplémentaires. Bien que l’objectif principal de cette configuration soit la gestion du programme, elle peut être modifiée pour être utilisée comme un outil de soins cliniques.

### Déroulement { #workflow }

![Déroulement](resources/images/workflow.png)

### Structure du programme { #programme-structure }

| Étape | Description |
| --- | --- |
| Inscription | Une fois qu’un patient est identifié comme étant séropositif au VIH, il doit être inscrit dans le programme de surveillance des cas de VIH. L’étape d’inscription requiert la saisie d’informations personnelles et d’identifiants uniques, dont certains seront générés automatiquement. Tous les patients inscrits dans ce registre sont séropositifs ; il est donc important que l’accès soit limité aux seules personnes concernées par ces informations, ce qui nécessite une adaptation aux politiques locales de protection de la vie privée des patients et aux besoins locaux. Les informations d’identification (profil du patient) sont disponibles sous la forme d’un widget dans l’écran de saisie des données du système de suivi. |
| Déclaration initiale de cas | La déclaration initiale de cas peut être remplie en même temps que l’inscription du patient. Cette étape fournit la base de référence pour le reste du traitement et comprend notamment la date du diagnostic du VIH et l’âge au moment du diagnostic. Si le patient appartient à un groupe de population clé, celui-ci peut être sélectionné ici. Il s’agit d’une étape non reproductible, car les détails de l’initiation ne sont recueillis qu’une seule fois pour chaque cas enregistré.  |
| Visite de traitement | La visite constitue l’étape où tous les éléments du traitement sont enregistrés. Une fois le motif de la visite enregistré, la première vérification porte sur le motif de la visite et permet de savoir si et quand la PVVIH a commencé son traitement. Le reste des éléments de données est masqué jusqu’au début du traitement. La deuxième vérification consiste à déterminer si la PVVIH est éligible à la thérapie préventive contre la tuberculose (TPT). Si c’est le cas, une section sur la TPT devient accessible et permet d’enregistrer le date de début, le type et la date de fin du traitement. Enfin, une vérification du statut du traitement permet de classer la PVVIH comme étant maintenue sous TAR, ayant arrêté son traitement, référée ailleurs ou décédée. Si le statut du traitement révèle que la personne est sous TAR, il devient possible d’ajouter le nombre de jours de TAR fournis et le système calcule automatiquement la date du dernier jour de TAR. Si le patient est sous TAR depuis plus de 180 jours, les champs d’informations concernant le test de charge virale apparaissent, notamment la date du test, le statut de la charge virale et, le cas échéant, la valeur de la charge virale précédente. Cette étape est reproductible, car elle sera réalisée de façon continue tout au long de la vie du patient, lorsqu’il se rendra dans l’établissement de santé pour récupérer ses médicaments, effectuer des examens de contrôle et les tests de charge virale habituels (et/ou ciblés), conformément aux directives cliniques nationales et celles de l’OMS. |
| Suivi | Cette étape n’est liée à aucun indicateur et sert exclusivement d’outil permettant d’enregistrer tout contact établi avec les patients qui ont manqué des visites de traitement et qui devront être recontactés. Cette étape est reproductible afin de permettre plusieurs suivis. |

## Configuration du Tracker { #tracker-configuration }

### Instance de l’entité suivie { #tracked-entity-instance }

Le programme utilise le type d’instance d’entité suivie « Personne ». La TEI sera inscrite pour toute sa durée de vie dans ce système de suivi et elle sera inscrite après avoir été diagnostiquée séropositive au VIH. Cela suppose qu’il existe un registre distinct pour les tests du VIH en dehors de ce programme.

### Phases { #stages }

#### Inscription et étapes initiales du cas { #enrollment-initial-case-stages }

L’étape de déclaration initiale de cas est incluse dans l’étape d’inscription afin de simplifier la saisie des données. Il est important de noter que les sections et certaines actions des règles du programme ne sont pas prises en charge lorsque l’étape est incluse dans l’écran d’inscription. Certains comportements du formulaire peuvent donc ne pas correspondre aux attentes.

![Inscription](resources/images/enrollment.png)

##### Inscription { #enrollment }

L’étape d’inscription rassemble tous les attributs d’une personne enregistrée. Chaque pays doit modifier l’inscription pour s’assurer qu’elle correspond à ses besoins et ses pratiques.

| Nom de l’attribut | Valeur |
| --- | --- |
| Unité d’organisation chargée de l’inscription | Unité d’organisation |
| Date d’inscription | Date |
| Prénom | texte |
| Nom de famille | texte |
| Date de naissance estimée | oui uniquement |
| Date de naissance | date |
| Genre | Options : homme/femme/transgenre/autre |
| Adresse (actuelle) | texte |
| Numéro de téléphone mobile | Numéro de téléphone |
| Pays de naissance | Liste des pays |
| Nº d’identité national | numéro/texte |
| Code de l’établissement de santé | texte |
| Identifiant du programme | Généré par le système |
| Identifiant NHIS | Généré par le système |
| Consentement à la communication – le client donne son accord pour être contacté | Oui/non |

###### Identifiants { #identifiers }

Actuellement, le programme dispose de quatre identifiants uniques en plus des informations d’identification personnelles, afin de minimiser les doublons. Si les identifiants sont tous réalisés au sein de la même instance du DHIS2, ils peuvent tous être validés comme uniques. La modification des identifiants sera probablement l’un des premiers changements nécessaires en vue de l’adaptation du package au contexte local.

Nº d’identité national : identifiant unique généralement fourni par un bureau national du CRVS.

Code de l’établissement de santé : identifiant local du patient qui peut être issu des dossiers papier existants.

Identifiant du programme : identifiant unique au sein du programme VIH. Il est parfois désigné sous le nom de numéro TAR ou numéro de patient. S’il n’existe pas au moment de l’inscription, il peut être ajouté ultérieurement.

Identifiant NHIS : identifiant pour le patient au sein du NHIS et indépendant au programme de surveillance des cas.

Le DHIS2 peut être programmé pour attribuer des identifiants uniques en fonction d’un ensemble de règles et d’une expression générale, ou pour permettre la saisie manuelle d’identifiants uniques et non uniques en fonction des besoins et des capacités du pays.

Sur les appareils Android, plusieurs problèmes se produisent si le modèle attribué par le système est séquentiel ou dépendant d’une date. Plus d’informations ici : [https://docs.dhis2.org/](https://docs.dhis2.org/en/implement/android-implementation/dhis2-configuration-for-android.html#implementation_guide_dhis2_config_reserved_id)

##### Cas initial { #initial-case }

L’étape du cas initial est annexée à l’étape de l’inscription à des fins de saisie des données. Cette étape vise à enregistrer les informations de base sur le dépistage du VIH du patient qui ne devraient pas changer. (En cas de modification de l’IPK, par exemple si le patient est libéré, ces informations peuvent être mises à jour ultérieurement dans le rapport de cas si cela est nécessaire).

| Nom | Valeur |
| --- | --- |
| Rapport de cas initial | date |
| Date du test positif au VIH | date |
| Type de test au niveau communautaire | Ensemble d’options : Type de dépistage au niveau communautaire : service mobile de dépistage (par exemple, par le biais de camionnettes ou de centres éphémères de dépistage) ; centres de conseil et de dépistage volontaires (hors établissement de santé) ; et autres dépistages au niveau communautaire. |
| Point d’entrée pour le dépistage au niveau des établissements | Ensemble d’options : Point d’entrée pour le dépistage au niveau des établissements : service mobile de dépistage (par exemple, par le biais de camionnettes ou de centres éphémères de dépistage) ; centres de conseil et de dépistage volontaires (hors établissement de santé) ; et autres dépistages au niveau communautaire. |
| Âge au moment du dépistage du VIH | Âge calculé (nombre entier) |
| Ce nourrisson est-il un cas de transmission materno-fœtale ? | Oui/non, visible uniquement si l’enfant a moins de 2 ans. |
| Cette personne appartient-elle à un groupe de population clé, tel que : hommes qui ont des rapports sexuels avec des hommes, utilisateurs de drogues par injection, personnes incarcérées ou placées dans d’autres structures fermées et travailleurs du sexe. | Oui/Non |
| Population clé - Hommes ayant des rapports sexuels avec des hommes | Oui uniquement |
| Population clé - Utilisateurs de drogues par injection | Oui uniquement |
| Population clé - Personnes incarcérées ou placées dans d’autres structures fermées | Oui uniquement |
| Population clé - Travailleurs du sexe | Oui uniquement |
| Population clé - Transgenre | Oui uniquement |

![Déclaration initiale de cas](resources/images/initial.png)

Si le sexe d’un patient est marqué comme « transgenre », un avertissement s’affiche pour inviter l’utilisateur à indiquer « transgenre » dans son statut de population clé.

#### Visite dans le cadre du traitement { #treatment-visit }

![Visite](resources/images/visit.png)

| Nom | Valeur | Commentaire/Logique |
| --- | --- | --- |
| Date de visite | Date | Caractéristique de la date de l’événement |
| Date d’échéance | Date | Date d’échéance de l’événement |
| Motif de la visite | Ensemble d’options « Motif de la visite » : Visite clinique, Récupération des médicaments antirétroviraux, Questions et préoccupations |  |
| Traitement commencé | Oui/non | La section Traitement est masquée lorsque « Oui » n’est pas sélectionné. La valeur « Oui » est transférée aux nouveaux événements. |
| Date d’initiation du traitement | Date | Il s’agit d’un élément de date utilisé pour calculer la date d’initiation du traitement. Une fois saisie la première fois, la valeur de la date renseignée est transférée aux visites suivantes |
| Le patient est éligible à la thérapie préventive contre la TB | Oui uniquement | Si cette case n’est pas cochée, les éléments relatifs à la TPT sont masqués |
| Date à laquelle le patient a été jugé éligible pour la thérapie préventive contre la TB | Date | À remplir une seule fois, se conserve lors des visites subséquentes |
| Thérapie préventive contre la TB initiée | Date | À remplir une seule fois, se conserve lors des visites subséquentes |
| Régime de thérapie préventive contre la TB | Ensemble d’options : Régime TTB | À remplir une seule fois, se conserve lors des visites subséquentes ; Voir onglet jaune « Ensemble d’options » |
| Date d’achèvement de la thérapie préventive contre la TB | Date | À remplir une seule fois, se conserve lors des visites subséquentes |
| Redémarrer la thérapie préventive contre la TB | Oui uniquement | Une fois cochée, rend les autres champs modifiables. S’affiche uniquement après l’achèvement de la thérapie contre la TB. |
| Statut du traitement | Ensemble d’options : Statut du patient | Si le statut n’est pas « maintenu sous TAR », le reste de l’étape est masqué |
| Actuellement enceinte | Oui uniquement | S’affiche uniquement si le client est « sous traitement » et s’il s’agit d’une femme. |
| Date du décès | date | S’affiche uniquement si l’option « Décès » est sélectionnée |
| Date du changement de statut du client | date | S’affiche uniquement si les options « Réutilisation du traitement », « Référé ailleurs » ou « Perdu de vue » sont sélectionnées |
| Date du test de charge virale du VIH | date | Uniquement visible si le nombre de jours entre le début du traitement et l’événement > 180 |
| Charge virale < 1000 | Case à cocher (Oui uniquement) | Uniquement visible si le nombre de jours entre le début du traitement et l’événement > 180 |
| Résultat du test de charge virale VIH | Nombre | Uniquement visible si le nombre de jours entre le début du traitement et l’événement >​ 180 et si « Charge virale < 1000 » n’est pas coché |
| Valeur précédente de la charge virale | Nombre | Visible uniquement si le nombre de jours entre le début du traitement et l’événement > 180. Affiche automatiquement la valeur de la charge virale précédente, s’il y a eu une visite précédente. |
| Jours de TAR fournis | Nombre |  |
| Dernière date avec TAR | Affiche la dernière date à laquelle le patient a pris les médicaments | Automatiquement calculé en fonction des valeurs « Date de visite » + « Jours de TAR fournis » |

L’étape Visite de traitement est divisée en trois sections.

Surveillance clinique :

La section de surveillance clinique commence par demander si la PVVIH a commencé ou non un traitement antirétroviral (TAR). Si le patient a commencé son traitement, la section du traitement s’affiche. De même, si le champ « Le patient est éligible à la thérapie préventive contre la TB » est coché, cette section s’affiche. Dans le cas contraire, les deux sections restent masquées. Si le traitement est initié après 14 jours, un message d’initiation tardive s’affiche dans la barre supérieure.

TPT : la section TPT enregistre la date à laquelle la personne a été jugée éligible à la thérapie préventive contre la TB (en fonction du dépistage initial et/ou du suivi des symptômes de la TB), la date de début et le régime de la thérapie, ainsi que la date d’achèvement. Une fois les valeurs saisies ici, elles sont conservées pour les étapes suivantes et aucune saisie de données supplémentaire n’est nécessaire.

Lorsque le patient a terminé son traitement, le champ « Redémarrer la TPT » s’affiche. En cochant cette case, vous pourrez supprimer les valeurs existantes et commencer un nouveau cycle de TPT.

![Thérapie préventive contre la TB](resources/images/tpt.png)

Traitement​ :

Le premier élément de données de la section du traitement demande de sélectionner le statut du traitement. Si un patient est marqué comme « Maintenu sous TAR », le reste des champs s’affiche. Si un patient est marqué comme décédé, ayant arrêté le traitement, officiellement référé ailleurs ou perdu de vue, les autres champs restent masqués.

Si le patient est sous TAR depuis moins de 180 jours (6 mois), un message indique « Les champs relatifs à la charge virale sont uniquement disponibles pour les patients sous TAR depuis six mois ou plus ». Lorsque le patient est sous TAR depuis 180 jours ou plus (de la date de début de traitement jusqu’à la date actuelle), les champs pour l’enregistrement du statut et du test de la charge virale s’affichent.

![Test de la charge virale](resources/images/viral_load.png)

Les champs relatifs à la charge virale incluent une case à cocher lorsque la PVVIH passe en suppression virale : moins de 1000 copies/ml, ce qui correspond aux directives actuelles de l’OMS, mais qui doit être adapté conformément aux directives cliniques nationales.

Si la charge virale est inférieure à 1000 copies/ml, le champ « Résultat du test de charge virale (saisi sous forme de nombre) » est masqué et la barre supérieure affiche la légende « La personne est en suppression virale ».

À la fin de la section, la saisie des jours de TAR fournis permet de calculer la dernière date de TAR, ce qui permet de planifier le prochain rendez-vous.

### Suivi { #follow-up }

![Suivi](resources/images/followup.png)

| Nom | Valeur | Commentaire |
| --- | --- | --- |
| Date de tentative de contact avec le client | date | Fonctionnalité |
| Motif du suivi | Motif du suivi : visite de soins cliniques manquée ; récupération des médicaments manquée ; visite de soins non cliniques manquée ; TAR non commencé ; statut VIH non concluant ; réception des résultats des tests ; autre motif de suivi (à préciser) |  |
| Méthode de suivi du VIH | Ensemble d’options pour la méthode de suivi : SMS ; Appel téléphonique ; Visite à domicile ; autre |  |
| Issue du suivi du VIH | Ensemble d’options pour l’issue du suivi : retour à l’établissement de santé ; auto-référé ailleurs ; hospitalisé ; refus de revenir ; non localisé ; décès (signalé) ; décès confirmé | En cas de sélection des options Décédé (signalé), Décès (confirmé), Non localisé ou Refus de revenir, un avertissement apparaît : « Si le statut d’un patient a changé (est décédé, a décidé d’arrêter le traitement, est en arrêt de traitement depuis pus de 28 jours, etc.), vous devez effectuer une étape de visite et enregistrer ce changement de statut. » |
| Notes de suivi du VIH | Texte long |  |

L’étape de suivi est conçue pour être utilisée lorsqu’un patient ne s’est pas présenté à son dernier rendez-vous, mais est toujours sous traitement. Elle n’est actuellement liée à aucun indicateur et peut être supprimée du programme si elle n’est pas utilisée dans un cadre clinique, sans que cela n’affecte les autres modules.

Elle enregistre la raison pour laquelle ce suivi est nécessaire (visite de soins cliniques manquée, récupération de médicaments manquée, visite non clinique manquée, TAR non commencé, statut VIH non concluant, réception des résultats des tests, autre motif de suivi), la méthode de suivi (SMS, appel téléphonique, visite à domicile ou autre) et le résultat du suivi (retour à l’établissement de santé, auto-référé ailleurs, hospitalisé, refus de revenir, patient non localisé, décès signalé, décès confirmé). Si, lors du suivi, le statut du traitement du patient a changé (par exemple, le patient a décidé d’arrêter le traitement), le programme invite l’utilisateur à compléter une option d’étape Visite et à l’enregistrer.

![Suivi](resources/images/followup2.png)

### Configuration de l’écran de saisie des données { #data-entry-screen-set-up }

Une installation initiale est nécessaire pour configurer de manière optimale l’écran de saisie des données du patient.

En cliquant sur l’icône en forme de rouage en haut à droite, vous pouvez accéder au menu des widgets et organiser le tableau de bord de saisie des données en fonction des processus locaux, en masquant ou en affichant les widgets.

![Menu des widgets](resources/images/widgets.png)

Nous recommandons d’utiliser le programme avec la « saisie de données tabulaires » plutôt que la « saisie de données chronologiques » et d’utiliser au minimum les widgets inscription, retour d’information, indicateurs, profil et rapport, ainsi que la barre supérieure. Les administrateurs du système peuvent verrouiller la configuration pour tous les autres utilisateurs.

![Barre supérieure](resources/images/topbar.png)

La barre d’informations supérieure peut être utilisée pour mettre en évidence les informations pertinentes. Dans cette image, elle indique le nom, la date de naissance, le nombre de jours depuis la dernière visite (s’il a dépassé les 28 jours) et le nombre de jours sans médicaments le cas échéant. Cette barre peut être modifiée et configurée pour afficher d’autres informations en fonction des besoins de l’utilisateur. Pour en savoir comment configurer la barre supérieure, consultez la documentation suivante : [https://docs.dhis2.org/en/use/user-guides/dhis-core-version-236/tracking-individual-level-data/tracker-capture.html#top-bar](https://docs.dhis2.org/en/use/user-guides/dhis-core-version-236/tracking-individual-level-data/tracker-capture.html#top-bar)

### Sécurité et accès { #security-and-access }

Pour des considérations générales sur la sécurité de votre instance DHIS2, veuillez consulter [https://dhis2.org/security/](https://dhis2.org/security/).

#### Paramètres de recherche { #search-settings }

Le programme est actuellement défini sur « Ouvert », ce qui signifie que, tant que les utilisateurs sont autorisés à effectuer des recherches dans d’autres unités d'organisation grâce aux [paramètres de recherche utilisateurs](https://docs.dhis2.org/en/implement/understanding-dhis2-implementation/users-and-user-roles.html) qui leur ont été attribués, ils pourront rechercher et accéder à des patients dans d’autres unités d'organisation.

Pour plus de sécurité, il conviendrait de configurer le programme comme **protégé**. Cela signifie qu’un utilisateur peut lire et écrire dans des instances d’entités suivies qui appartiennent à l’unité ou aux unités d'organisation pour lesquelles l’utilisateur a accès à la collecte de données, mais son champ de recherche doit être plus large que son champ de lecture/écriture afin de garantir qu’il identifiera tout patient existant lors de sa recherche, même si celui-ci n’appartient pas à son établissement. Si la recherche renvoie à un patient en dehors de son établissement, l’utilisateur a la possibilité d’accéder au dossier du patient en indiquant d’abord un motif pour accéder au dossier. On parle aussi de « briser la vitre » pour désigner cette approche de la confidentialité, car elle permet à l’utilisateur de prendre la décision d’accéder au dossier sans autorisation ou assistance extérieure, mais laisse une trace claire qui peut être vérifiée. Lorsque l’utilisateur a indiqué un motif pour briser la vitre, il acquiert la propriété temporaire de l’instance d’entité suivie (voir le [guide de l’utilisateur du tracker](https://docs.dhis2.org/2.34/en/dhis2_user_manual_en/using-the-tracker-capture-app.html#breaking-the-glass) pour plus d’informations.)

Veuillez noter que pour les implémentations basées sur Android, si vous souhaitez que les utilisateurs puissent rechercher des clients dans une unité d'organisation différente de la leur, les paramètres de recherche DOIVENT obligatoirement être définis sur « Ouvert », car les autres fonctionnalités de recherche ne sont pas prises en charge. Pour en savoir plus : [https://docs.dhis2.org/en/full/implement/dhis2-android-configuration-guide.html](https://docs.dhis2.org/en/full/implement/dhis2-android-configuration-guide.html)

#### Gestion des utilisateurs { #user-management }

Actuellement, il y a trois groupes d’utilisateurs inclus dans le package.

**Surveillance des cas de VIH – Analyse des données** : a accès aux tableaux de bord, mais ne peut pas modifier les métadonnées ou saisir de nouvelles données

**Surveillance des cas de VIH – Saisie des données** : peut saisir des données et créer de nouveaux dossiers de patients

**Surveillance des cas de VIH – Administrateur des métadonnées** : peut modifier les métadonnées

Les pays mettant en œuvre le programme doivent s’assurer que les utilisateurs disposent de droits de saisie de données pour leurs unités d'organisation respectives et de droits de recherche pour toutes les unités d'organisation qui fourniront des services relatifs au VIH, afin de faciliter les échanges entre les établissements de santé.

#### Orientations et propriété { #referrals-and-ownership }

Dans le Tracker, l’unité d'organisation est à la fois l’unité organisation d’inscription et la propriétaire du cas. La propriété du cas peut être transférée d’une unité d'organisation à une autre à l’aide de la fonctionnalité « déplacer définitivement » ou le patient peut simplement être dirigé vers des services, à l’aide de la fonction « orientation ponctuelle ». Le programme peut également être configuré pour permettre à plusieurs/toutes les unités d'organisation de pouvoir fournir des services (ou « enregistrer des événements ») même sans transfert de la propriété. Pour ce faire, il faut d’abord cliquer sur le bouton « orienter le patient »

![Orientation](resources/images/referral.png)

Cette action ouvrira la fenêtre d’orientation, qui permettra une orientation ponctuelle du patient ou un transfert permanent :

![Orientation](resources/images/referral2.png)

### Règles du programme { #program-rules }

Le programme comprend plusieurs règles logiques pour faciliter la saisie de données, le flux de travail et les calculs, ainsi que pour afficher des informations utiles.

| nom | identifiant | Description | priorité | condition |
| --- | --- | --- | --- | --- |
| Calculer l’âge au moment du dépistage du VIH | NkKReOZIHIX | Cette règle calcule le nombre d’années (nombre entier) entre la date de naissance et la date de diagnostic du VIH, et attribue la valeur à l’élément de donnée « Âge au moment du diagnostic » | 1 | d2:hasValue( 'HIV_TEST_DATE' ) |
| Jours sans médicaments | GxoeUZf5aWb | Cette règle est conçue pour s’afficher lorsqu’un patient est sans médicament depuis plus de 28 jours, et elle indique le nombre de jours sans médicament. |  | d2:daysBetween( #{Last Day With Medicine}, V{current_date} ) > 28 && d2:hasValue( 'Last Day With Medicine') |
| Afficher la date d’initiation du traitement | xiMJ5cEgJfN | Cette règle permet de disposer d’une date constante pour le début du traitement afin de pouvoir calculer les indicateurs. |  | d2:hasValue( 'Date of Initiation previous' ) |
| Afficher la date d’éligibilité à la TPT | xRECtYcrv6u | Affiche la date à laquelle un patient est devenu éligible à la TPT depuis sa première éligibilité. |  | d2:hasValue( 'Previously TPT eligible' ) && !#{TPT_Restart_Treatment} |
| Afficher une erreur si la date de test est avant la naissance | gZy3eQsP9Lx | Le test VIH ne peut pas avoir lieu avant la naissance du patient |  | d2:hasValue( 'HIV_TEST_DATE' ) && (#{HIV_TEST_DATE} < A{AGE}) |
| Afficher si précédemment éligible à la TPT | MvAYneJFL2Q | Affiche si précédemment éligible à la TPT | 1 | d2:hasValue( 'Previously TPT eligible' ) && !#{TPT_Restart_Treatment} |
| Afficher la dernière charge virale VIH | xr4PnRTTFjr | Cette règle affiche la dernière charge virale d’un patient lorsqu’il n’est pas en suppression virale. |  | d2:hasValue( 'Dernière charge virale VIH' ) |
| Afficher la date d’achèvement de la TPT si terminée | DICAiThz6Px | Affiche la date à laquelle un traitement a été terminé s’il a déjà été terminé. |  | d2:hasValue( 'TPT Date previously Completed' ) && !#{TPT_Restart_Treatment} |
| Afficher la date d’initiation de la TPT si initiée | O9TJOZkACxU | Affiche la date à laquelle un traitement a été initié s’il a déjà été initié |  | d2:hasValue( 'TPT Date Initiated Previous' ) && !#{TPT_Restart_Treatment} |
| Afficher le régime TPT précédemment adopté | rhdEpzJFAFn | Affiche le régime TPT suivi par le patient |  | d2:hasValue( 'TPT Regimen From previous' ) && !#{TPT_Restart_Treatment} |
| Afficher l’avertissement « Si une personne a changé le statut du patient, vous devez l’enregistrer dans l’étape de visite » | aE5Uc6sW8dL | Cette règle pour l’étape de suivi affiche un avertissement en cas de changement de statut, demandant son enregistrement dans l’étape de visite |  | #{Follow-up_Result} == 'REFUSED_TO_RETURN' \|\| #{Follow-up_Result} == 'REFUSED_TO_RETURN' \|\| #{Follow-up_Result} == 'DIED_REPORTED' \|\| #{Follow-up_Result} == 'DIED_CONFIRMED' \|\| #{Follow-up_Result} == 'NORESPONSE' |
| Erreur si aucune pop clé sélectionnée | uvE3pz9mye4 | Si la personne est marquée comme appartenant à un groupe de population clé, au moins un groupe de population clé doit être coché. |  | #{KEY_POPULATIONS_YN} == true && (!#{Keypop_drug} && !#{Keypop_MSM} && !#{Keypop_prisoner} && !#{Keypop_sex_worker} && !#{Keypop_trans}) |
| Masquer la date du décès si la personne n’est pas décédée | zDB2AmOWyEW | Si le patient n’est pas décédé, cette règle masque l’élément de donnée date du décès. |  | #{Patient Status} != 'DEAD' |
| Masquer la date de changement de traitement si le patient est retenu sous traitement ou décédé | CXMkCYwEzEw | Masquer la date de changement de traitement si le patient est retenu sous traitement ou décédé |  | #{Patient Status} != 'TREATMENTSTOPPED' && #{Patient Status} != 'TRANSFEROUT' && #{Patient Status} != 'LTFU' |
| Masquer si non éligible à la TPT | hCvSfbSiOUR | Si le patient n’est pas éligible à la TPT, masque la section TPT | 2 | !d2:hasValue('Eligible for TPT') |
| Masquer les options de population clé si non membre | rGcmQkBMjXF | Si le patient n’est pas marqué comme appartenant à une population clé, masquer les éléments de données de sélection de la population clé. |  | !#{KEY_POPULATIONS_YN} |
| Masquer enceinte si homme | vV7Isi7RnLl | Si le patient est un homme, la règle masque l’élément de données relative à la grossesse |  | A{Gender} != 'FEMALE' |
| Masquer la valeur de la charge virale précédente si les résultats de la charge virale précédente sont vides | amEUbPOt1T3 | Si le champ « charge virale » n’avait aucune valeur dans l’événement précédent, masque le champ « charge virale précédente ». |  | !d2:hasValue( 'Dernière charge virale VIH') |
| Masquer le redémarrage de la TPT si elle n’est pas encore achevée | t6qVz4JsE4a | Sauf si cette PVVIH a déjà achevé la TPT, masquer le champ « Redémarrer la TPT » |  | !d2:hasValue('Date d'achèvement précédente de la TPT') |
| Masquer les détails du traitement si le patient n’est pas sous traitement | p7XMeDbTSbL | À moins qu’il ne soit indiqué « traitement commencé » pour cette personne, la section relative au traitement est masquée. | 1 | #{Patient Status} != 'RETENU' |
| Masquer la section relative au traitement si le traitement n’a pas commencé | lEicuM1ELe8 | Masquer la section relative au traitement si le traitement n’a pas commencé | 2 | !#{Traitement du VIH commencé oui non} |
| Masquer la transmission verticale pour les moins de 2 ans | aPPWe4bwylP | Masque la transmission verticale, si une personne n’avait pas moins de 2 ans lorsqu’elle a reçu un diagnostic de VIH. | 20 | d2:yearsBetween( A{Date_of_birth}, #{HIV_TEST_DATE} ) >2 |
| Masquer les champs de charge virale si les jours entre la date d’initiation et la date de l’événement sont inférieurs à 180 | HlyEkb2OkDX | Si les jours entre la date d’initiation ou la date d’initiation précédente sont inférieurs à 180, la règle masque le statut de charge virale | 1 | d2:daysBetween(#{Date d’initiation}, V{event_date}) <= 180 |
| Masquer les résultats du test de charge virale si la charge virale est inférieure à 1 000 | S7jJk8oVx3E | Masquer les résultats du test de charge virale si la charge virale est inférieure à 1 000 | 1 | #{Charge virale du VIH inférieure à 1000} |
| Initiation tardive VIH | bf2FzSkov8N | Si le nombre de jours entre la date d’inscription et le début du traitement est supérieur à 14 jours = initiation tardive. |  | d2:daysBetween( V{enrollment_date}, #{Date d’initiation} ) > 14 |
| Valeur précédente de la charge virale VIH | oo3EDy9na3c | Attribue une valeur au champ « charge virale précédente » s’il y a une valeur dans le champ de charge virale dans l’événement précédent. |  | d2:hasValue( 'HIV Viral Load' ) |
| VIH - Afficher une valeur pour la prochaine date de visite suggérée | apjLE7Hu2mN | Date de l’événement actuel PLUS nombre de jours avec médicaments |  | d2:hasValue( 'VIH - jours avec médicaments' ) |
| Si le patient a pris des médicaments il y a moins de 28 jours, ne pas marquer comme PDV | qgyfb07Rze6 | Si le patient ne prend plus de médicaments depuis moins de 28 jours, cette règle affiche un message d’erreur lorsque « PDV » est sélectionné à l’étape de la visite. Les patients ne peuvent être marqués comme PDV que s’ils ne prennent plus de médicament depuis plus de 28 jours. |  | d2:hasValue( 'Statut du patient' ) && (#{Statut du patient}== 'LTFU') && d2:hasValue( 'Dernier jour avec médicaments' ) && d2:daysBetween( #{Dernier jour avec médicaments}, V{event_date} ) <= 28 |
| Si le traitement a déjà commencé, indiquer que le traitement a commencé. | jka5y2tAy9m | Si  « traitement contre le VIH déjà commencé » = vrai, indique que le traitement a commencé | 1 | d2:hasValue('VIH - Traitement commencé précédemment') |
| Si la charge virale est inférieure à 1 000 = Suppression virale | g8LDxurfW21 | Si le champ « Charge virale inférieure à 1 000 » est coché, la personne sera marquée comme étant en suppression virale. |  | #{Charge virale du VIH inférieure à 1000} |
| Marquer comme perdu de vue | Z5sfFPDSeri | Compte les jours entre le dernier jour sous médicament et la date actuelle. Si un patient ne prend plus de médicament depuis plus de 28 jours, la règle suggère qu’il pourrait être marqué comme perdu de vue |  | d2:daysBetween( #{Dernier jour sous médicaments}, V{current_date} ) >= 28 |
| Afficher le numéro de téléphone | lfTZ4R0Qees | Si un numéro de téléphone a été saisi, il s’affiche. |  | d2:hasValue( 'Méthode de suivi' ) |
| Afficher l’avertissement relatif aux tests de charge virale. | nCEVmOVXATp | Si les jours entre la date d’initiation ou la date d’initiation précédente sont inférieurs à 180, afficher le message « Les tests de charge virale ne doivent être effectués qu’après six mois de traitement » |  | d2:daysBetween( #{Date of Initiation}, V{event_date} ) <= 180 |
| Si TG affiche un avertissement, assigner à la pop clé TG | CxoJG6aPGxD | Si le patient a « Transgenre » comme attribut de genre, la règle invite à marquer la population clé comme TG |  | A{Gender} == 'TG' |

## Analyse { #analytics }

### Tableaux de bord et indicateurs { #dashboards-and-indicators }

Six tableaux de bord sont inclus dans le package de métadonnées, basés sur les indicateurs du programme et les indicateurs dérivés des données du programme de surveillance des cas de VIH. Par défaut, les tableaux de bord sont accessibles à tous les utilisateurs ayant accès au programme de surveillance des cas de VIH.

Chacun de ces tableaux de bord est décrit dans le tableau ci-dessous.

-   Déclaration des cas et données démographiques
-   Arrimage au TAR et rétention en soins
-   Charge virale
-   Thérapie préventive contre la TB
-   Statut épidémique\*
-   Surveillance au niveau de l’établissement

\*Notez qu’à des fins de comparaison, certains éléments du tableau de bord Statut épidémique dépendent des estimations officielles de la prévalence du VIH. Ces estimations peuvent être saisies sous forme de données agrégées dans le programme « Estimations PVVIH » pour tout niveau géographique et année où elles sont disponibles.

### Aperçu du tableau de bord { #dashboard-overview }

Nom du tableau de bord, description et questions sur l’utilisation des données

**VIH SC – 1. Déclaration de cas et données démographiques**

![Tableau de bord 1](resources/images/Dashboard1.png)

Nouveaux cas signalés par mois, zone géographique et groupe de population clé. Cas cumulés enregistrés par tranches d’âge, genre.

-   Comment l’enregistrement des nouveaux cas de VIH a-t-il évolué cette année par rapport à l’année dernière ?
-   La plupart des nouveaux cas de VIH ont-ils également commencé le TAR ?
-   L’épidémie est-elle concentrée dans un certain groupe de population clé ou région ?

**VIH SC – 2. Arrimage au TAR et rétention en soins**

![Tableau de bord 2](resources/images/Dashboard2.png)

Cumul des cas qui initient et poursuivent le TAR de façon régulière. Examine le statut des patients signalé le mois dernier, et l’attrition ou la mortalité au fil du temps.

-   Comment l’arrimage au TAR s’est-il amélioré au fil du temps ? Y a-t-il des districts ou des établissements de santé clés où l’arrimage au TAR est significativement plus faible ?
-   Combien de patients ont commencé le TAR le jour même de leur résultat de dépistage ?
-   Combien l’ont commencé dans les 14 jours ?
-   Quelles sont les tendances des patients perdus de vue lors des visites du mois dernier, par sexe ? Par district ?
-   L’attrition liée au TAR a-t-elle généralement augmenté au cours des 6 derniers mois ?

**VIH SC - 3. Charge virale**

![Tableau de bord 3](resources/images/Dashboard3.png)

Couverture des tests de charge virale et suppression de la charge virale chez tous les patients sous TAR pendant plus de 6 mois.

-   Y a-t-il 95 % des cas avec un test de charge virale en suppression de charge virale ?
-   Ce chiffre s’est-il amélioré depuis l’année dernière ?
-   Parmi tous les cas sous TAR depuis au moins 6 mois et toujours actifs, combien ont déjà effectué un test de charge virale ?
-   Le mois dernier, combien de patients ayant eu leur première visite après 6 mois sous TAR ont également eu un test de charge virale au cours du mois ? Cela varie-t-il selon les districts ?

**VIH SC - 4. Thérapie préventive contre la TB**

![Tableau de bord 4](resources/images/Dashboard4.png)

Initiation et achèvement de la thérapie préventive contre la tuberculose (TPT), cumulées par âge et par genre, ainsi que des régimes de TPT.

-   Quelle est la cascade du nombre total de cas de VIH avec éligibilité, initiation et achèvement de la TPT cette année ?
-   Les taux d’achèvement de la TPT ont-ils augmenté au cours des 12 derniers mois ?
-   Les adultes éligibles sont-ils plus susceptibles d’initier la TPT que les enfants éligibles ?
-   Y a-t-il des tendances par genre ?

**VIH SC - 5. Statut épidémique**

![Tableau de bord 5](resources/images/Dashboard5.png)

Cascade du VIH avec données de surveillance des cas et estimations globales du spectre en tant que dénominateurs annuels au niveau de la population.

-   Ma région atteint-elle les objectifs 95/95/95 ?
-   Y a-t-il suffisamment de cas inscrits dans le système de suivi VIH SC pour comparer avec l’estimation du spectre national du nombre total de cas identifiés ?
-   Comment les cas en suppression de CV ont-ils augmenté cette année par rapport à la fin de l’année dernière ?
-   Au cours des 6 derniers mois, combien de PVVIH ont commencé le TAR ?

**VIH SC - Surveillance au niveau de l’établissement**

![Tableau de bord 6](resources/images/Dashboard6.png)

Indicateurs basés sur les rencontres, spécialement conçus pour surveiller le déploiement de la VIH SC au niveau de l’établissement, y compris les nouveaux cas sous TAR, le centre de dépistage et le dernier statut hors TAR. - Quelle était la combinaison d’âge et de genre la plus courante pour les nouveaux cas le mois dernier ? - Les signalements de cas « perdus de vue » ont-ils augmenté ou diminué au cours des 12 derniers mois dans mon établissement ? - Quelle était la raison la plus fréquente des visites de patients au cours des 3 derniers mois ? - Quels patients ont interrompu leur TAR le mois dernier dans mon établissement ?

### Indicateurs et indicateurs de programme { #indicators-and-program-indicators }

Le package comprend 116 indicateurs du programme et indicateurs XYZ, basés sur des données individuelles recueillies dans le système de suivi. En règle générale, les indicateurs du programme comptent les cas de VIH répondant à des critères spécifiques ; les indicateurs sont des pourcentages basés sur ces comptages. Ces indicateurs de programme et indicateurs sont présentés sous forme de graphiques, de cartes et de tableaux qui sont affichés sur les tableaux de bord.

Il est conseillé de faire particulièrement attention aux indicateurs de programme signalés comme « cumulés », qui identifient tous les cas répondant aux critères spécifiés avant la fin d’une période donnée, indépendamment de la date d’inscription dans le système, et utilisent des « limites de période analytique » ouvertes. Notez qu’une désagrégation supplémentaire de tous les indicateurs de programme peut être configurée pour le contexte local en consultant le Guide de l’utilisateur du DHIS2. (<https://docs.dhis2.org/en/use/user-guides/dhis-core-version-236/analysing-data/data-visualizer.html>)

| pi_name | pi_shortname | pi_desc | pi_type |
| :-: | :-: | :-: | :-: |
| VIH - 0 à 4 ans | PVVIH (0-4, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Âge à l’inscription. | INSCRIPTION |
| VIH - 5 à 9 ans | PVVIH (5-9 ans, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - 10 à 14 ans | PVVIH (10-14, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - 15 à 19 ans | PVVIH (15-19 ans, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - 20 à 24 ans | PVVIH (20-24 ans, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - 25 à 49 ans | PVVIH (25-49 ans, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - 50 ans et + | PVVIH (50 ans et +, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Âge au diagnostic : 0_20 | VIH - ÂGE AU DIAGNOSTIC : 0_20 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 0_20 & Genre : Féminin | VIH - ÂGE AU DIAGNOSTIC : 0_20 & GEN...\_COMBO_4 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 0_20 & Genre : Masculin | VIH - ÂGE AU DIAGNOSTIC : 0_20 & GEN...\_COMBO_5 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 0_20 & Genre : Autre | VIH ÂGE AU DIAGNOSTIC : 0_20 & GEN...\_COMBO_6 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 0_20 & Genre : Transgenre | VIH ÂGE AU DIAGNOSTIC : 0_20 & GEN...\_COMBO_7 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 20_40 | VIH ÂGE AU DIAGNOSTIC : 20_40 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 20_40 & Genre : Féminin | VIH ÂGE AU DIAGNOSTIC : 20_40 & GE...\_COMBO_10 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 20_40 et Genre : Masculin | VIH - ÂGE AU DIAGNOSTIC : 20_40 & GE...\_COMBO_11 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 20_40 & Genre : Autre | VIH - ÂGE AU DIAGNOSTIC : 20_40 & GE...\_COMBO_12 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 20_40 & Genre ​: Transgenre | VIH - ÂGE AU DIAGNOSTIC : 20_40 & GE...\_COMBO_13 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 40_60 | VIH - ÂGE AU DIAGNOSTIC : 40_60 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 40_60 & Genre : Féminin | VIH - ÂGE AU DIAGNOSTIC : 40_60 & GE...\_COMBO_15 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 40_60 & Genre : Masculin | VIH - ÂGE AU DIAGNOSTIC : 40_60 & GE...\_COMBO_16 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 40_60 & Genre : Autre | VIH - ÂGE AU DIAGNOSTIC : 40_60 & GE...\_COMBO_17 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 40_60 & Genre : Transgenre | VIH - ÂGE AU DIAGNOSTIC : 40_60 & GE...\_COMBO_18 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 60_80 | VIH - ÂGE AU DIAGNOSTIC : 60_80 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 60_80 & Genre : Féminin | VIH - ÂGE AU DIAGNOSTIC : 60_80 & GE...\_COMBO_19 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 60_80 & Genre : Masculin | VIH - ÂGE AU DIAGNOSTIC : 60_80 & GE...\_COMBO_20 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 60_80 & Genre : Autre | VIH - ÂGE AU DIAGNOSTIC : 60_80 & GE...\_COMBO_21 |  | ÉVÉNEMENT |
| VIH - Âge au diagnostic : 60_80 & Genre : Transgenre | VIH ÂGE AU DIAGNOSTIC : 60_80 & GE...\_COMBO_22 |  | ÉVÉNEMENT |
| VIH - Âge inconnu | PVVIH (âge inconnu, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Test de proximité : services mobiles de dépistage | VIH - Test de proximité : SERVICES MOBILES DE DÉPISTAGE… |  | ÉVÉNEMENT |
| VIH - Test de proximité : autres tests de proximité | VIH Test de proximité : AUTRES TESTS DE… |  | ÉVÉNEMENT |
| VIH - Test de proximité : centres de conseil et dépistage volontaire | VIH Test de proximité : CENTRES DE CONSEIL... |  | ÉVÉNEMENT |
| VIH - actuellement enceinte | VIH - ACTUELLEMENT ENCEINTE |  | ÉVÉNEMENT |
| VIH - Jours depuis début du traitement | VIH - Jours depuis le début |  | INSCRIPTION |
| HIV - Test en établissement : établissement de soins prénatals | VIH - Test en établissement : SOINS PRÉNATALS… |  | ÉVÉNEMENT |
| VIH - Test en établissement : établissement de planning familial | VIH - Test en établissement : PLANNING FAMILIAL… |  | ÉVÉNEMENT |
| VIH - Test en établissement : autres tests en établissement | VIH - Test en établissement : AUTRE ÉTABLISSEMENT… |  | ÉVÉNEMENT |
| VIH - Test en établissement : dépistage à l’initiative du prestataire dans une clinique ou un établissement d’urgence | VIH - Test en établissement : DÉPISTAGE À L’INITIATIVE… |  | ÉVÉNEMENT |
| VIH - Test en établissement : établissement TB | VIH -Test en établissement : ÉTABLISSEMENT TB |  | ÉVÉNEMENT |
| VIH - Test en établissement : conseil et tests volontaires (au sein d’un établissement de santé) | VIH - Test en établissement : CONSEIL ET TESTS VOL… |  | ÉVÉNEMENT |
| VIH - Genre féminin | PVVIH (Féminin, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Genre masculin | PVVIH (masculin, total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Genre manquant | PVVIH (Genre SO, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Genre transgenre | PVVIH (TG, Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - Début de TAR 1 à 14 jours après dépistage | VIH début de TAR 1 à 14 jours après dépistage | Nombre de personnes ayant commencé leur traitement dans les 14 jours suivant l’inscription | INSCRIPTION |
| VIH - Début de TAR + de 15 jours après dépistage | VIH - début de TAR + de 15 jours après dépistage | Nombre de personnes ayant commencé leur traitement dans les 14 jours suivant l’inscription | INSCRIPTION |
| VIH - Début de TAR et décédé, cumulé | Décès d’un patient VIH sous traitement | Patients surveillés décédés sous surveillance | INSCRIPTION |
| VIH - Début de TAR et perdu de vue, cumulé | Patient VIH PDV sous traitement | Patients surveillés et dont le dernier rapport indique « perdus de vue » pendant leur traitement | INSCRIPTION |
| VIH - Début de TAR et transfert ailleurs, cumulé | VIH patient référé ailleurs sous traitement | Patients surveillés et dont le dernier rapport indique « référé ailleurs » pendant leur traitement | INSCRIPTION |
| VIH - Début de TAR, Cumulé | VIH patients tous sous traitement | Patients surveillés, y compris ceux décédés, référés ailleurs ou perdus de vue | INSCRIPTION |
| VIH - Début de TAR le même jour que le dépistage | VIH - Début de TAR le même jour que le dépistage | VIH - Début de traitement le même jour que le test positif | INSCRIPTION |
| VIH - Début de TAR pendant cette période | VIH - Début de TAR cette période |  | INSCRIPTION |
| VIH - pop clé : tous les groupes | VIH POPULATION CLÉ : Tous |  | ÉVÉNEMENT |
| VIH - Pop clé : consommateur de drogue injectable | VIH - Pop clé : Consommateur de drogue injectable |  | ÉVÉNEMENT |
| VIH - pop clé : plus d’un groupe | VIH - Pop clé : plus de 1 groupe |  | ÉVÉNEMENT |
| VIH - Pop clé : HRSH | VIH - Pop clé : HRSH |  | ÉVÉNEMENT |
| VIH - Pop clé : Prisonnier | VIH - Pop clé : Prisonnier |  | ÉVÉNEMENT |
| VIH - Pop clé : Travailleur du sexe | VIH - Pop clé : Travailleur du sexe |  | ÉVÉNEMENT |
| VIH - Pop clé : Transgenre | VIH - Pop clé : Transgenre |  | ÉVÉNEMENT |
| VIH - Nouveau cas | VIH - Nouveau cas |  | ÉVÉNEMENT |
| VIH - Nouveau cas sous TAR | VIH - Nouveau cas sous TAR |  | ÉVÉNEMENT |
| VIH - Nouveaux cas, Féminin | VIH_NOUVEAU_CAS GENRE : FÉMININ |  | ÉVÉNEMENT |
| VIH - Nouveaux cas, masculin | VIH - NOUVEAU CAS GENRE : MASCULIN |  | ÉVÉNEMENT |
| VIH - Nouveaux cas, Autre genre | VIH - NOUVEAU CAS GENRE : AUTRE |  | ÉVÉNEMENT |
| VIH - Nouveaux cas, Transgenre | VIH - NOUVEAU CAS GENRE : TRANSGENRE |  | ÉVÉNEMENT |
| VIH - Personnes vivant avec le VIH (Nouveau) | PVVIH (Nouveau) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Par date de SIGNALEMENT DU NOUVEAU CAS. | INSCRIPTION |
| VIH - Personnes vivant avec le VIH (Total) | PVVIH (Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - PVVIH ayant interrompu le TAR, cumulé, par établissement de visite | PVVIH_sous_TAR_INTERROMPU_VISITE_CUMU | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. La date de début du TAR doit être antérieure au début de la période de déclaration. Comptage de tous les patients qui ont interrompu le TAR dans l’établissement avant la fin de la période. Cette méthode compte deux fois les paires patient-unité d'organisation, et non les patients uniques, et doit être interprétée avec prudence. | ÉVÉNEMENT |
| VIH - PVVIH, TAR interrompu pendant la période, par établissement d’enregistrement | PVVIH sous TAR (Total, y compris les abandons) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. La date de début du TAR doit être antérieure au début de la période de déclaration. | INSCRIPTION |
| VIH - PVVIH sous TAR 6 mois (nouvelle visite durant cette période) | PVVIH, charge virale éligible (Visite effectuée) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. Doivent avoir effectué une visite durant la période | INSCRIPTION |
| VIH - PVVIH sous TAR 6 mois cette période | PVVIH, charge virale nouvellement éligible cette période | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le moment de la période, tout en étant dans la fenêtre d’éligibilité. | INSCRIPTION |
| VIH - PVVIH sous TAR 6 mois cette période et ayant reçu les résultats de la CV | PVVIH, nouvelle charge virale avec résultats | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le moment de la période, tout en étant dans la fenêtre d’éligibilité. | INSCRIPTION |
| VIH - PVVIH sous TAR 6 mois (Total) | PVVIH, charge virale éligible (Total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. | INSCRIPTION |
| VIH - PVVIH sous TAR (Nouveau sous TAR pour cette période) | PVVIH sous TAR (nouveau) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - PVVIH sous TAR avant la période, par établissement d’enregistrement | VIH - PVVIH sous TAR (Total, avant la période) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Examen de la période AVANT CETTE PÉRIODE pour la comparer à la période actuelle et analyser l’attrition. La date de début du TAR doit être antérieure au début de la période de déclaration. | INSCRIPTION |
| VIH - PVVIH sous TAR avant la période, par établissement de visite | PVVIH sous TAR_AVANT_VISITE | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Examen de la période AVANT CETTE PÉRIODE pour la comparer à la période actuelle et analyser l’attrition. La date de début du TAR doit être antérieure au début de la période de déclaration. Cette méthode compte deux fois les paires patient-unité d'organisation, et non les patients uniques, et doit être interprétée avec prudence. | ÉVÉNEMENT |
| VIH - PVVIH sous TAR (Total) | PVVIH sous TAR (total) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. | INSCRIPTION |
| VIH - PVVIH ayant des résultats de charge virale (nouveau résultat de CV cette période) | PVVIH avec résultats de charge virale (nouveau) | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. | INSCRIPTION |
| VIH - PVVIH ayant des résultats de charge virale (total) | PVVIH avec résultats de charge virale | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. | INSCRIPTION |
| VIH - PVVIH avec suppression de la charge virale (nouveau résultat de CV durant cette période) | PVVIH avec suppression de la charge virale, nouveau | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. CV < 1000 | INSCRIPTION |
| VIH - PVVIH dont la charge virale est supprimée (Total) | PVVIH dont la charge virale est supprimée | Toutes les personnes inscrites à ce programme sont des PVVIH, à l’exception de celles qui ont été référées ailleurs et de celles qui sont décédées. Doivent avoir eu les résultats du test VIH 6 mois avant le dernier événement. CV < 1000 | INSCRIPTION |
| VIH - PVVIH avec plus de 28 jours depuis la fin de la dernière période de prescription | VIH - Aucun médicament depuis 28 jours ou plus |  | INSCRIPTION |
| VIH - Motif de visite : récupération des médicaments antirétroviraux | VIH - MOTIF DE VISITE : RÉCUPÉRATION DES MÉDICAMENTS… |  | ÉVÉNEMENT |
| VIH - Motif de visite : visite clinique | VIH - MOTIF DE VISITE : VISITE CLINIQUE |  | ÉVÉNEMENT |
| VIH - Motif de visite : questions et préoccupations | VIH MOTIF DE VISITE : QUESTIONS ET PREOCCUPATONS |  | ÉVÉNEMENT |
| VIH - Décès signalé | VIH - Patient décédé | Patients surveillés et décédés sous surveillance | ÉVÉNEMENT |
| VIH - Signalé comme perdu de vue | VIH - Patient PDV | Patients surveillés et perdus de vue sous surveillance | ÉVÉNEMENT |
| VIH - Signalé comme ayant changé de lieu | VIH - Patient transféré | Patients surveillés et signalés comme référés ailleurs ou « ayant changé de lieu » | ÉVÉNEMENT |
| VIH - Signalé comme ayant arrêté le traitement | VIH Patient ayant arrêté le traitement | Patients signalés comme ayant arrêté le traitement | ÉVÉNEMENT |
| VIH - Testé positif dans la période | VIH - Testé positif |  | INSCRIPTION |
| VIH - Testé positif durant la période et ayant débuté le TAR | VIH, testé positif, début de TAR |  | INSCRIPTION |
| VIH - TPT terminée, cumulé | VIH - TPT terminée, cumulé |  | INSCRIPTION |
| VIH - TPT terminée cette période | VIH - TPT terminée cette période |  | INSCRIPTION |
| VIH - Éligible TPT, cumulé | VIH - Éligible TPT, cumulé |  | INSCRIPTION |
| VIH - Éligible TPT, cumulé (adulte, 15 ans et +) | VIH - Éligible à la TPT, cumulé, 15 ans et + | Âge à la date d’éligibilité à la TPT | INSCRIPTION |
| VIH - Éligible à la TPT, cumulé (masculin) | VIH - Éligible à la TPT, cumulé, masculin |  | INSCRIPTION |
| VIH - Éligible à la TPT, cumulé (pédiatrie, 0 à 14 ans) | VIH - Éligible à la TPT, cumulé, 0 à 14 ans | Âge à la date d’éligibilité à la TPT | INSCRIPTION |
| VIH - Éligible à la TPT, cumulé (transgenre) | VIH - Éligible à la TPT, cumulé, transgenre |  | INSCRIPTION |
| VIH - Éligible à la TPT cette période | VIH - Éligible à la TPT cette période |  | INSCRIPTION |
| VIH - TPT initiée, cumulé | VIH - TPT initiée, cumulé |  | INSCRIPTION |
| VIH - TPT initiée, cumulé (adulte, 15 ans et +) | VIH - TPT initiée, cumulé, 15 ans et + | Âge à la date d’éligibilité à la TPT | INSCRIPTION |
| VIH - TPT initiée, cumulé (féminin) | VIH - TPT initiée, cumulé, féminin |  | INSCRIPTION |
| VIH - TPT initiée, cumulé (masculin) | VIH - TPT initiée, cumulé, masculin |  | INSCRIPTION |
| VIH - TPT initiée, cumulé (pédiatrie, 0 à 14 ans) | VIH - TPT initiée, cumulé, 0 à 14 ans | Âge à la date d’éligibilité à la TPT | INSCRIPTION |
| VIH - TPT initiée, cumulé (transgenre) | VIH - TPT initiée, cumulé, transgenre |  | INSCRIPTION |
| VIH - TPT initiée cette période | VIH - TPT initiée cette période |  | INSCRIPTION |
| VIH - Statut du traitement : modifié | VIH - STATUT DU TRAITEMENT : MODIFIÉ |  | ÉVÉNEMENT |
| VIH - Statut du traitement : décès (documenté) | VIH - STATUT DU TRAITEMENT : DÉCÈS (DOCUMENTÉ) |  | ÉVÉNEMENT |
| VIH - Statut du traitement : perdu de vue | VIH - STATUT DU TRAITEMENT : PERDU DE VUE |  | ÉVÉNEMENT |
| VIH - Statut du traitement : sous TAR | VIH - STATUT DU TRAITEMENT : SOUS TAR |  | ÉVÉNEMENT |
| VIH - Statut du traitement : traitement refusé (arrêté) | VIH - STATUT DU TRAITEMENT : TRAITEMENT REFUSÉ (ARR…) |  | ÉVÉNEMENT |
| VIH - Statut du traitement : référé ailleurs | VIH STATUT DE TRAITEMENT : RÉFÉRÉ AILLEURS |  | ÉVÉNEMENT |
| VIH - Transmission verticale | VIH - TRANSMISSION VERTICALE |  | ÉVÉNEMENT |
| VIH - Visites (événements) | VIH - Evénements Visites |  | ÉVÉNEMENT |
| VIH - Visites (PVVIH uniques) | VIH - Personnes en visite |  | ÉVÉNEMENT |
| VIH - Test de CV Dénominateur annuel | VIH - Test de CV Dénom ANNUEL | Uniquement pour le niveau annuel. S’il s’agit de l’année en cours, inclut ceux qui ont été testés positifs au premier semestre. S’il s’agit de l’année dernière, inclut tous ceux qui ont été testés positifs. | INSCRIPTION |
| VIH - Test de CV numérateur annuel | Test CV Num ANNUEL | Uniquement pour le niveau annuel. Si la période de déclaration est cette année, et au second semestre, inclure le premier semestre de l’année. Si la période de déclaration est cette année et au premier semestre, aucun cas positif de cette année n’est éligible. Si c’est l’année dernière, tous les cas positifs de cette année sont éligibles pour le test cette année. | INSCRIPTION |

### Limitations liées à la propriété pour les indicateurs { #ownership-limitations-for-indicators }

Lorsqu’un indicateur de programme analyse les données du patient saisies pour deux événements ou plus, cela est rendu possible grâce à un indicateur de programme *de type inscription*.

Actuellement, les indicateurs du programme DHIS2 ne peuvent pas différencier l’unité d'organisation \_propriétaire_et  l’unité d'organisation \_d’inscription_. En pratique, cela signifie que lorsqu’un patient change d’établissement, aucun des indicateurs longitudinaux de ce patient n’est réaffecté au dernier établissement du patient. Ils restent tous affectés à l’établissement initial par lequel le patient est arrivé dans le programme.

Il s’agit d’une limitation critique de l’analyse du DHIS2 que les responsables de la mise en œuvre du package doivent prendre en compte, en particulier lors de l’interprétation des indicateurs longitudinaux de surveillance des cas tels que les taux de mortalité et les taux d’attrition. Les analyses de suivi basées sur l’unité d'organisation propriétaire de l’enregistrement ne sont actuellement pas prises en charge par le moteur d’indicateurs du DHIS2, mais seront disponibles dans les prochaines versions du DHIS2.

Jusqu’à ce que cette fonctionnalité soit prise en charge, les solutions alternatives consistent à s’appuyer sur des indicateurs nationaux ou à utiliser un script pour changer l’unité d'organisation d’inscription en unité d'organisation propriétaire. Pour plus d’informations sur cette solution alternative, consultez le guide d’installation

## Métadonnées { #metadata }

Sur notre référentiel github, vous trouverez le lien vers la dernière version des métadonnées. Notez qu’il ne s’agit pas de la version définitive de ce package et que celui-ci sera mis à jour dès que possible : [Lien vers github](https://github.com/dhis2/metadata-package-development/tree/master/metadata/HIV_Tracker )

## Compatibilité Android { #android-compatibility }

Le package est nativement compatible avec l’application de capture des données du DHIS2 pour Android. Il y a cependant quelques considérations à prendre en compte lors de l'implémentation de ce package avec des appareils Android :

### UiD attribués automatiquement { #automatically-assigned-uids }

Si vous utilisez des appareils Android et des identifiants générés automatiquement qui sont séquentiels ou basés sur des dates, vous devez savoir que pour pouvoir travailler hors ligne, les appareils Android réservent des ensembles d’UiD en bloc à l’avance. Cela signifie que les UiD attribués peuvent ne pas nécessairement correspondre à l’ordre chronologique dans lequel les patients sont enregistrés. Pour plus d’informations, voir [ici](https://docs.dhis2.org/en/implement/android-implementation/dhis2-configuration-for-android.html#implementation_guide_dhis2_config_reserved_id).

### Fonctionnalité de recherche { #search-functionality }

Notez que pour les implémentations sur Android, si vous souhaitez que les utilisateurs puissent rechercher des clients dans une unité d'organisation différente de la leur, les paramètres de recherche DOIVENT obligatoirement être réglés sur « ouvert », car les autres fonctionnalités de recherche ne sont pas entièrement prises en charge. Plus d’informations disponibles [ici](https://docs.dhis2.org/en/full/implement/dhis2-android-configuration-guide.html).
