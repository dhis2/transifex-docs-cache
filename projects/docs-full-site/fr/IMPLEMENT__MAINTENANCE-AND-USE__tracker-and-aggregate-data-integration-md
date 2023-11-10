---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/maintenance_use/tracker-aggregate-integration.md"
revision_date: '2021-11-16'
tags:
- Implémentation
---

# Intégration des données du tracker et des données agrégées { #integrating-tracker-and-aggregate-data } 
Ce guide propose différentes approches pour combiner les données collectées dans le cadre des programmes tracker avec les données agrégées, afin qu'elles puissent être analysées et être utilisées ensemble. Les données de suivi et les données agrégées sont collectées et stockées séparément dans le DHIS2, mais il existe de nombreux cas où il est utile de combiner les deux types de données:

* Les données collectées par les programmes tracker et les ensembles de données agrégées peuvent être complémentaires. Par exemple, si le programme de suivi est utilisé comme registre électronique de vaccination, le calcul des couvertures vaccinales exige que les données sur les services collectées grâce au programme tracker soient combinées avec les estimations de la population généralement disponibles sous forme de données agrégées (annuelles).
* Dans de nombreux cas, les implémentations de trackers se font par étapes, en commençant par certains types d'établissements de santé ou par zone géographique. Par conséquent, les mêmes données peuvent être collectées grâce au tracker dans certains endroits et sous forme de données agrégées dans d'autres, et l'obtention d'un aperçu complet des données nécessite de combiner les données du tracker et les données agrégées. De telles approches différenciées ou hybrides peuvent également être permanentes.
* Les données collectées grâce au tracker peuvent partiellement se superposer dans les rapports globaux établis. Par exemple, un rapport mensuel sur les activités liées au paludisme peut inclure des informations à la fois sur les cas de paludisme et sur les activités préventives telles que la distribution de moustiquaires. Si le tracker est utilisé pour enregistrer les cas de paludisme, le rapport mensuel sur le paludisme peut être partiellement complété sur la base des données du tracker, tout en exigeant des rapports globaux sur les activités préventives.
* Lorsque le suivi est lancé dans un domaine programmatique (vaccination, VIH, etc.) où des données agrégées ont déjà été collectées, il est nécessaire, pour garantir la comparaison des données dans le temps, de combiner les données agrégées et les données de suivi afin de permettre une analyse longitudinale des données.
* Certains contrôles de qualité des données dans DHIS2 ne sont disponibles que pour les données agrégées. Pour appliquer ces contrôles aux données de suivi, il faut donc d'abord les agréger et les stocker en tant qu'éléments de données agrégées.

Il existe plusieurs façons d'y parvenir, en fonction des objectifs visés. Chacune de ces approches présente des avantages et des inconvénients. Dans la [section suivante] (approches - alternatives), trois approches générales pour combiner les données de suivi et les données agrégées sont présentées, suivies d'une section sur le [choix d'une approche] (#choosing-an-approach) qui présente des considérations et des exemples de cas où chacune de ces approches peut être appropriée. Ensuite, un [guide pratique] (#How-to-saving-aggregated-tracker-data-as-aggregate-data-values) est fourni pour l'approche basée sur l'enregistrement des données du tracker en tant que valeurs de données agrégées.

## Approches alternatives{ #alternative-approaches } 
Les données de suivi et les données agrégées peuvent être combinées dans DHIS2 :

- en affichant des données de suivi et des données agrégées en parallèle dans le même graphique, tableau, carte ou tableau de bord ;
- en combinant les données agrégées et les données de suivi à l'aide d'indicateurs agrégés ;
- en enregistrant les valeurs calculées sur la base des données de suivi en tant que valeurs de données agrégées.

Cette section présente un résumé des trois approches, avec les avantages et les inconvénients de chacune d'entre elles.

### Afficher les données de suivi et les données agrégées en parallèle { #showing-tracker-and-aggregate-data-side-by-side } 
Les données agrégées et les données de suivi peuvent être affichées et analysées ensemble si elles sont incluses dans les mêmes graphiques ou tableaux de Visualisation des données. En outre, des visualisations de données de suivi peuvent être créées dans les applications Rapport d'événement et Visualiseur d'événement, et combinées avec des visualisations de données agrégées dans les tableaux de bord. Tout utilisateur ayant accès aux deux types de données dans les applications analytiques du DHIS2 peut utiliser cette méthode.

<!-- TODO : Exemple de capture d'écran -->

> **Avantages:**
>
> *  facile à installer
> * Bien adapté à la présentation et à l'analyse de données complémentaires
> * des données détaillées peuvent être incluses (par exemple, des listes de cas)
>
> **Inconvénients:**
>
> *dimensionnalité limitée dans l'analyse des données de suivi, c'est-à-dire pour afficher les désagrégations par âge/sexe
> * pas totalement intégrées/comparables avec les données agrégées, par exemple les mêmes désagrégations ne peuvent pas être appliquées dans une visualisation unique même si elles sont disponibles dans les données sous-jacentes
> * exige que le tracker et les données agrégées se trouvent dans la même instance DHIS2

### Combiner des données avec des indicateurs agrégés  { #combining-data-through-aggregate-indicators } 
Les indicateurs agrégés peuvent être basés à la fois sur des données agrégées et des données de suivi, séparément ou combinées en un seul indicateur agrégé. Les éléments de données de suivi, les attributs des entités suivies et les indicateurs de programme peuvent tous être inclus dans le calcul des indicateurs agrégés.

Cette méthode peut s'avérer utile dans plusieurs cas de figure :

* Les mêmes données sont collectées à partir d'un ensemble de données agrégées et de programmes tracker dans différents établissements de santé, c'est-à-dire que certains collectent des données agrégées et d'autres des données individuelles à l'aide d'un tracker.
* Les mêmes données sont disponibles en tant que valeurs de données agrégées et valeurs de données de suivi sur des périodes différentes, par exemple si les données collectées en ce moment par le biais du suivi ont été collectées au cours des années précédentes en tant que données agrégées.
* Lorsque des indicateurs sont nécessaires sur la base d'une combinaison de données, par exemple des données sur les services collectées par le biais d'un système de suivi, combinées à des dénominateurs disponibles sous forme de données agrégées.

<!-- TODO : Exemple de capture d'écran -->

> **Avantages:**
>
> * relativement facile à installer
> * peut potentiellement dissimuler aux utilisateurs finaux la complexité de l'intégration des données agrégées et des données de suivi
> 
> **Inconvénients:**
>
> * les données des trackers ne peuvent pas être analysées avec des désagrégations telles que l'âge/le sexe en tant que dimensions de données distinctes
> * difficile à gérer dans les cas où il peut y avoir des données qui se superposent
> * exige que le tracker et les données agrégées se trouvent dans la même instance DHIS2

### Enregistrer les agrégats de données de suivi en tant que données agrégées{ #saving-aggregates-of-tracker-data-as-aggregate-data } 
Les données du Tracker peuvent être agrégées, par exemple en valeurs hebdomadaires ou mensuelles, et ces valeurs peuvent être enregistrées en tant que valeurs d'éléments de données agrégées dans DHIS2. Cela correspond à ce qui est souvent fait manuellement dans les établissements de santé lorsque les registres sont compilés chaque mois pour produire des rapports mensuels. Les indicateurs de programme peuvent être définis de manière à produire des chiffres agrégés basés sur les données du Tracker, correspondant à des éléments de données agrégés. La valeur de l'indicateur de programme doit représenter la même valeur que l'agrégat (par exemple, *nombre de nouveaux cas de tuberculose et de cas de rechute notifiés* ou *nombre de doses de BCG administrées à des enfants de moins d'1 an*). Le transfert de données peut être effectué sur une base Ad-hoc, selon les besoins, ou dans le cadre d'un processus de routine où les données sont transférées (automatiquement) à des intervalles fixes (voir la figure ci-dessous).

![Exemple : Flux d'informations entre une instance DHIS2 avec des programmes de suivi et une instance DHIS2 HMIS avec des données agrégées.](resources/images/tracker_agg_information_flow.jpg)

![Exemple : Ensemble de données agrégées (in the data entry app) which has been automatically filled by the data pushed from tracker program indicators.](resources/images/tracker_agg_dataset_example.png)

Le transfert effectif des données des indicateurs de programme vers les éléments de données agrégées, peut s'effectuer de plusieurs manières. Il s'agit notamment de: 

* de façon manuelle ou via un script adressant une requête à l'[API DHIS2](#webapi) pour exporter les valeurs des indicateurs de programme et les importer ensuite dans DHIS2 à l'aide de l'[application d'importation/exportation](#import_export) ou de l'API ;
* l'automatisation de l'exportation et de l'importation des données de l'API à l'aide d'un script ;
* l'utilisation d'une des applications développées par la communauté DHIS2 et disponibles sur le [DHIS2 App Hub] (apps.dhis2.org) pour exporter et importer les données ;
* l'installation de [Prédicteurs] (#manage_predictor), qui peuvent être programmés pour transférer régulièrement les valeurs des indicateurs de programme dans les éléments de données agrégés.

Cette méthode est décrite plus en détail ci-dessous, en insistant sur comment automatiser le processus à l'aide de scripts.

> **Avantages:**
>
> * les données peuvent être analysées selon la même dimension que les données agrégées (voir l'exemple de la capture d'écran ci-dessous)
> * les données peuvent encore être combinées avec les données détaillées des trackers (c'est-à-dire la première méthode)
> * garantit qu'il n'y a pas de superposition entre les données du  tracker et les données agrégées
> * fonctionne lorsque les données du tracker et les données agrégées sont collectées dans des instances DHIS2 distinctes
> * peut améliorer l'efficacité et réduire la charge du serveur DHIS2 en matière d'analyse, étant donné que les demandes de données pré-agrégées sont souvent moins exigeantes que l'agrégation à la volée des données du tracker
>
> **Inconvénients:**
>
> * plus complexe à installer, et peut nécessiter beaucoup plus d'entretien continu
> * nécessite généralement des outils/scripts externes pour transférer des données via l'API
> * un mapping des données entre le tracker et les données agrégées doit être développé et entretenu
> *  si les données sont déplacées entre deux instances DHIS2, les unités d'organisation doivent également être harmonisées et synchronisées entre les instances

<!-- TODO - les deux captures d'écran ci-dessous devraient peut-être être fusionnées en une seule, en mettant un accent particulier sur la "dimensionnalité" -->

![Exemple : Suivi des cas de tuberculose pour agréger les rapports trimestriels sur la tuberculose pour les notifications relatives à la tuberculose. Valeurs des données des indicateurs de programme à partir des données du système de suivi(data elements/disaggregation can be produced, but not pivoted by dimensions as gender, age group)](resources/images/tracker_agg_pt.png)

![Exemple : Tableau de bord agrégé (with ability to pivot male/female as a data dimension)](resources/images/tracker_agg_dashboard.png)

## Choisir une méthode { #choosing-an-approach } 
Chacune de ces trois méthodes présente des avantages et des inconvénients, comme indiqué ci-dessus. Pour une seule implémentation, plusieurs d'entre elles peuvent être nécessaires. Par exemple, il peut être utile de présenter certaines données de suivi avec des mises à jour fréquentes ( par exemple, le nombre quotidien d'enfants vaccinés), en transférant également les valeurs agrégées des indicateurs de programme, en valeurs agrégées des éléments de données chaque mois, afin que les données puissent être comparées avec les établissements qui n'utilisent pas encore le tracker, ou avec une dimensionnalité supplémentaire (telle que les désagrégations par âge/sexe) qui ne peut pas facilement être effectuée directement avec des données agrégées.

Les deux premières méthodes sont relativement simples à appliquer, grâce aux applications standard intégrées à DHIS2. Alors que la configuration des indicateurs agrégés (deuxième méthode) doit être effectuée par un administrateur système ayant accès à la configuration de ces indicateurs, tout utilisateur ayant accès aux applications d'analyse de DHIS2 et aux données elles-mêmes peut utiliser ces méthodes. Cependant, une limite majeure est la nécessité d'avoir le tracker et les données agrégées dans la même instance de DHIS2.

La troisième méthode, qui consiste à enregistrer les données du tracker en tant que valeurs de données agrégées, présente certains avantages en termes d'analyse. Toutefois, il s'agit également de la seule méthode permettant d'intégrer des données de suivi à des données agrégées dans des instances DHIS2 distinctes. De nombreux pays disposent d'une instance DHIS2 mature et stable, utilisée principalement pour la saisie de données agrégées dans le cadre de programmes de santé dans un environnement intégré (par exemple, un Système d'Information sur la Gestion de la Santé, HMIS). Lors de l'implémentation du tracker DHIS2 pour la collecte de données au niveau individuel, il est généralement recommandé de le faire dans une instance DHIS2 distincte dédiée au déploiement du tracker. En séparant le tracker et les instances agrégées de DHIS2, les performances peuvent être mieux contrôlées par les administrateurs du système, les mises à jour de DHIS2 peuvent être effectuées de manière indépendante et les principes de gouvernance des données peuvent être appliqués pour garantir que les données personnelles identifiables recueillies par le tracker peuvent être protégées conformément aux politiques nationales et aux cadres de gouvernance.

Lorsqu'il existe un système de rapports agrégés de routine à partir des données du DHIS2, il est clairement avantageux de pouvoir exploiter la collecte de données individuelles à l'aide d'un tracker pour "rapporter" automatiquement des données agrégées au HMIS de routine. L'alternative est souvent que cela soit fait manuellement par les établissements de santé, puisque ces résumés agrégés sont importants pour la gestion des établissements de santé individuels, et que le rapport de routine des données agrégées est souvent obligatoire. La saisie de données individuelles par le biais du système de suivi DHIS2 peut améliorer la qualité des données communiquées dans le système d'information sur les ménages HMIS, tout en permettant une analyse ad hoc des données individuelles du système de suivi, selon les besoins.

Techniquement, il existe plusieurs façons de procéder. Dans la section "Comment faire" ci-dessous, l'accent est mis sur les étapes nécessaires à l'installation d'une migration automatisée des données du tracker vers des valeurs de données agrégées.

## Mode opératoire : enregistrement des données tracker agrégées en tant que valeurs de données agrégées{ #how-to-saving-aggregated-tracker-data-as-aggregate-data-values } 
Cette section décrit la méthode recommandée pour enregistrer les données de suivi sous forme de valeurs d'éléments de données agrégées. Bien qu'elle nécessite un outil ou un script externe dans le cadre du transfert des données, cette méthode s'appuie autant que possible sur les fonctionnalités existantes de DHIS2, de sorte que le script puisse être relativement simple. La méthode décrite ici est également celle adoptée dans les [paquets de configuration de l'OMS](dhis2.org/who) pour le DHIS2, qui comprend le mapping des variables entre les programmes de suivi et les ensembles de données agrégées, le cas échéant. Cette méthode est examinée plus en détail [ci-dessous] (#dhis2-digital-data-packages-and-linking-tracker-and-aggregate-data).

La méthode décrite ici est recommandée comme solution automatisée à long terme pour sauvegarder les données du tracker en tant que valeurs de données agrégées. Techniquement, il existe plusieurs autres façons d'agréger et de transférer les données, notamment en utilisant des prédicteurs, en exportant les données et en les transformant à l'aide d'autres logiciels (par exemple Excel), ou par le biais d'applications DHIS2 personnalisées (dont certaines sont disponibles dans le [DHIS2 App Hub] (apps.dhis2.org). Bien qu'ils ne soient pas décrits dans ce guide, ces outils et méthodes peuvent être utiles dans de nombreux cas, notamment en combinaison avec la démarche décrite ici. Par exemple, s'il est nécessaire d'effectuer uniquement des transferts ad hoc de données de temps en temps, ou lors d'une phase initiale d'implémentation d'un tracker, lorsque les données sont transférées principalement à des fins de test et que la configuration est encore en cours de modification.

### Considérations d'implémentation { #implementation-considerations } 
L'intégration des données collectées au moyen du tracker avec les flux de rapports agrégés existants ( par exemple le HMIS) nécessite de prendre des décisions relatives à la gouvernance des données, et cela affecte l'accès aux données, la gestion des systèmes et bien d'autres choses encore. Quelques aspects clés sont présentés ici.

#### Transfert de données { #data-transfer } 
Il y a deux aspects essentiels à prendre en compte en matière de transfert de données :

**Quelle est la fréquence de transfert des données agrégées du tracker vers les valeurs de données agrégées ? ** Lorsque le transfert est automatisé, la fréquence du transfert peut être quotidienne ou unique par période de rapport/d'agrégation (par exemple, hebdomadaire, mensuelle, trimestrielle). Des mises à jour plus fréquentes signifient que les données deviennent disponibles en tant que valeurs de données agrégées et peuvent être utilisées et analysées plus rapidement, et qu'elles sont mises à jour au fur et à mesure que de nouvelles informations à jour sont reçues. L'utilité de ces données dépend du programme tracker en question. Par exemple, la mise à jour quotidienne des données au cours d'une période de déclaration peut être une information utile si elle est mise à la disposition du personnel de l'établissement, mais elle est moins utile si l'objectif de l'agrégation est principalement de faciliter et d'automatiser la déclaration de routine du HMIS à des niveaux plus élevés.

**Combien de temps faut-il remonter pour ajouter des données et les mettre à jour?** En plus de la décision sur la fréquence de transfert des données, il faut décider jusqu'à quand (combien de périodes) les données doivent être mises à jour, et s'il faut ou non transférer les données pour la période en cours (pour laquelle les données ne seront pas complètes, voir le point précédent). Cette décision devra peut-être s'aligner sur les pratiques potentiellement existantes en matière de données agrégées, telles que le moment ou la manière dont elles sont validées et le fait qu'elles soient ou non verrouillées à un moment donné pour être modifiées, comme nous le verrons ci-dessous. Dans le même ordre d'idées, on peut se demander s'il convient d'établir une distinction entre la migration de nouvelles valeurs de données et la mise à jour de valeurs déjà déclarées.

Les échanges sur ces questions doivent tenir compte du fait que les données des systèmes de suivi sont souvent saisies rétroactivement sur la base de registres papier, plutôt que directement pendant la prestation de services ou les rencontres avec les patients. En outre, les données peuvent être corrigées et éditées pendant un certain temps après l'événement, par exemple si, lors d'une visite de suivi, une erreur est détectée dans les données de la visite précédente.

À moins qu'il n'y ait de raisons valables de procéder autrement, il est suggéré que les mises à jour et les vérifications soient effectuées en remontant aussi loin dans le temps qu'il y ait des chances raisonnables que des ajouts et des mises à jour soient apportés aux données de suivi sous-jacentes. Cela permet de s'assurer que les informations utilisées sont les plus correctes et les plus récentes, même si cela peut nécessiter des changements dans les normes de gestion des données du système HMIS, par exemple en ce qui concerne la validation et le verrouillage des données.

#### Qualité  et validation des données{ #data-quality-and-validation } 
Garantir la qualité des données est une préoccupation majeure tant pour les données du tracker que pour les données agrégées, et la liaison des deux, introduit de nouveaux dilemmes potentiels dans ce domaine. Il existe des outils et des méthodes permettant de limiter les risques d'erreurs lors de la collecte des données du tracker. Néanmoins, il y a toujours un risque que des erreurs surviennent. Pendant la période au cours de laquelle les données agrégées basées sur le tracker sont encore mises à jour régulièrement (comme décrit dans la section précédente), les corrections apportées aux données du tracker se transfèrent automatiquement aux données agrégées. Toutefois, il existe deux scénarios pour lesquels il convient de décider comment traiter les corrections apportées aux données :

**Si des erreurs sont détectées et corrigées dans le tracker**, après la période au cours de laquelle les données sont régulièrement transférées et/ou après que les données agrégées ont été validées et/ou verrouillées. Les moyens possibles pour résoudre ce problème sont les suivants : - la mise en place d'un système de gestion de l'information :

* vivre avec la divergence dans les données agrégées (si l'erreur est mineure) ;
* effectuer un transfert ad hoc des données pour les périodes concernées ;
* corriger manuellement les données agrégées.

**Si des problèmes de qualité des données sont détectés dans les données agrégées**. Ce scénario est moins probable, car seules des erreurs relativement importantes ou systématiques dans les données du tracker seront visibles lorsque les informations sont agrégées, ou si les données sont manifestement incomplètes. Les moyens possibles de résoudre ce problème sont les suivants :

* corriger les données sources dans le tracker, puis retransférer les données (si possible) ;
* corriger/éditer les données agrégées (si possible) et accepter la divergence.

Un autre aspect pertinent de la qualité des données lors de l'agrégation des données de suivi concerne l'actualité et la complétude des données, qui sont des mesures clés de la qualité des données pour les rapports agrégés (par exemple, dans le HMIS). Lorsque les données agrégées sont communiquées directement par l'intermédiaire du DHIS2, les utilisateurs cliquent sur un bouton pour indiquer qu'un ensemble de données particulier (formulaire de rapport) a été déclaré dans son intégralité. Ces données servent de base au calcul de l'actualité (soumissions dans un délai précis) et de la complétude des données. Lorsque les données agrégées sont générées sur la base des données de suivi, aucune information sur la complétude et l'actualité des données n'est disponible. Plusieurs méthodes peuvent être envisagées à cet effet :

* Dans certains cas, il ne pose pas de problème qu'il n'y ait pas de règles de complétude et d'actualité des données. Il n'y a généralement pas d'informations sur la complétude et l'actualité des données du tracker, et les valeurs des données agrégées générées à partir des données du tracker peuvent être considérées de la même manière. C'est le cas, par exemple, si les données sont transférées principalement pour faciliter l'analyse des données avec une dimensionnalité additionnelle, ou pour utiliser des outils d'analyse pour les données agrégées.
* Si les données constituent un sous-ensemble d'un ensemble particulier de données régulièrement déclarées, où d'autres parties sont saisies directement en tant que données agrégées, les informations relatives à la complétude des données de suivi, pourraient être vérifiées et déclarées dans le cadre de la complétude de l'ensemble des données.
* L'information sur la complétude et la promptitude peut être gérée manuellement par l'utilisateur responsable de la soumission des données agrégées. Cela peut se faire dans le cadre d'un processus de validation, où l'utilisateur vérifie les données (dans l'application de saisie des données agrégées) et confirme ensuite que les données sont complètes. Bien que ceci permette une étape de validation supplémentaire, ceci nécessite également plus de ressources, et une véritable validation des données exigerait dans une certaine mesure un certain degré de comptage manuel qui va en partie à l'encontre de l'objectif de l'automatisation de l'agrégation des données de suivi.
* Un script ou un outil peut assez facilement être développé dans le but de marquer automatiquement les ensembles de données comme étant complets si une certaine quantité (c'est-à-dire un nombre spécifié de valeurs d'éléments de données) a été rapportée. Cela convient parfaitement à l'identification des établissements de santé pour lesquels *quelques* données ont été déclarées, mais ce processus automatisé ne permet pas de déterminer si les déclarations sont en fait *complètes* au sens propre du terme.

En général, lorsque les données de suivi sont utilisées pour produire des valeurs de données agrégées, il s'agit d'une forme d'utilisation secondaire des données au-delà de ce pour quoi elles ont été collectées à l'origine. Il est important de communiquer clairement aux utilisateurs comment les questions de validation et de correction des données sont gérées, comment les questions telles que la " complétude " sont traitées, et que la " source de vérité " pour les données est clairement définie.

#### Accès aux données et propriété { #data-access-and-ownership } 
L'accès aux données de suivi et aux données agrégées dans DHIS2 est contrôlé par le partage, sur la base de groupes d'utilisateurs. Le partage des données de suivi et des valeurs de données agrégées générées à partir des données de suivi peut donc être différent et, dans le scénario courant où les deux types de données sont hébergés dans des instances DHIS2 différentes, les mêmes utilisateurs peuvent ne pas avoir accès au système du tout. Cela présente certains avantages, par exemple, les valeurs des données agrégées peuvent être partagées plus largement que les données de suivi sans que cela n'ait d'incidence sur la vie privée ou la sécurité. Par ailleurs, il est nécessaire de mettre en place un partage de données approprié dans deux instances différentes, et les utilisateurs peuvent également avoir besoin d'accéder à deux systèmes différents. (Il est possible d'utiliser [OpenID Connect](#install_oidc_configuration) pour permettre aux utilisateurs de partager leur nom d'utilisateur et leur mot de passe entre les deux instances).

En lien avec  *l'accès * aux données, la question de la propriété des données  se pose, une question également liée à la qualité et à la validation des données. Des procédures claires doivent être mises en place pour indiquer qui est responsable et "propriétaire" à la fois du tracker et des valeurs de données agrégées générées par le tracker. Ceci est particulièrement important dans les scénarios où plusieurs programmes de santé sont impliqués. Par exemple, si un programme tracker des vaccinations alimente en données un ensemble de données HMIS intégrées, agrégées, pour lesquelles une unité HMIS distincte est responsable.

#### Maintenance { #maintenance } 
La méthode décrite ici exige que des capacités techniques soient disponibles, tant pour le développement initial et la configuration d'une solution de transfert de données que pour la maintenance continue qui peut être nécessaire, par exemple en cas de modification de l'infrastructure du serveur DHIS2. Par ailleurs, si les métadonnées de l'instance de suivi ou de l'instance agrégée du HMIS sont modifiées, le mapping des indicateurs de programme vers les éléments de données agrégés pourrait nécessiter une mise à jour en conséquence.

#### Période de transition { #transition-period } 
Lorsque les données de suivi sont agrégées dans le but de remplacer les rapports agrégés existants (tels que les rapports HMIS de routine), il est souvent utile de prévoir une période de maintien des rapports parallèles, de 6 mois par exemple. Au cours de cette période, les chiffres agrégés générés par le tracker et par les procédures manuelles existantes doivent être comparés. Il est peu probable qu'ils soient totalement identiques, mais de telles comparaisons sont utiles parce qu'elles :

* devrait déclencher une discussion sur l'origine des divergences, par exemple en cas de problèmes de qualité des données (dans l'une ou l'autre des sources de données).
* Renseigne sur les décisions à prendre lorsque les données du système de suivi sont aussi complètes ou de meilleure qualité que les rapports manuels, de sorte que les rapports parallèles puissent être interrompus.

Techniquement, cela peut être réalisé en ayant un ensemble de données "shadow" distinct avec des éléments de données distincts dans l'instance d'agrégat, de sorte que deux ensembles parallèles de données agrégées puissent être conservés et comparés à cet endroit. Il est également possible de conserver une copie de l'ensemble de données agrégées dans l'instance de suivi et de l'utiliser pour les comparaisons.

### Hypothèses et étapes clés { #assumptions-and-key-steps } 
Lorsque les données de suivi et les données agrégées sont gérées dans des instances DHIS2 distinctes, ce qui est généralement recommandé, la migration des données entre les deux instances nécessite que les unités d'organisation soient les mêmes ou qu'elles aient au moins un ensemble d'identifiants communs. Étant donné que les unités d'organisation sont souvent réutilisées lorsque de nouvelles instances DHIS2 sont installées, cela peut ne pas poser de problème dans un premier temps. Toutefois, le maintien de la synchronisation des unités d'organisation entre deux ou plusieurs instances DHIS2 au fil du temps nécessite une gestion minutieuse, que les changements soient gérés manuellement ou par le biais d'un processus automatisé. Les prochains guides d'implémentation aborderont cette question plus en détail. Aux fins du présent guide, il est indispensable que les unités d'organisation soient harmonisées et qu'elles disposent d'un ensemble commun d'identifiants dans les deux instances. Dans les cas où les données de suivi sont migrées vers des valeurs de données agrégées au sein des mêmes instances DHIS2, la synchronisation des unités d'organisation n'est pas un problème.

D'un point de vue conceptuel, les étapes de la migration des agrégats de données de suivi vers des valeurs de données agrégées sont les suivantes :

1. Établir un mapping entre les indicateurs du programme et les éléments de données correspondants ainsi que les combinaisons d'options de catégories, en utilisant des codes.
2. Exporter les valeurs des indicateurs de programme sous la forme d'un *ensemble de valeurs de données* agrégé
3. Importer l'*ensemble de valeurs de données* en tant que valeurs d'éléments de données agrégées

Les sections suivantes expliquent (1) comment établir un mapping entre les indicateurs de programme et les éléments de données, (2) les API du DHIS2 pertinentes pour l'importation/exportation des valeurs de données, et (3) les aspects à prendre en compte lors de l'automatisation du processus d'importation et d'exportation.

### Mapping des indicateurs de programme avec les éléments de données agrégées{ #mapping-program-indicators-with-aggregate-data-elements } 
Pour produire des valeurs de données agrégées à partir des données de suivi, des indicateurs de programme doivent être définis pour chaque point de données. Chacune de ces valeurs de données correspond à un élément de données et, au besoin, à une combinaison d'options de catégorie. Un mapping utilisant un identifiant est donc nécessaire pour spécifier quel indicateur de programme se rapporte à quel élément de données spécifique (avec une combinaison d'options de catégorie). Bien qu'elle ne soit pas abordée en détail ici, le mapping peut également inclure des combinaisons d'options d'attributs.

![Illustration du mapping des données de suivi en données agrégées à l'aide d'indicateurs de programme.](resources/images/tracker_agg_mapping.png)

Il est recommandé d'utiliser les *codes* comme identifiant pour ce mapping, et cela est présenté ici.

> **Remarque** 
> Bien que la méthode décrite ici soit basée sur le mapping des données dans le système source (par le biais d'indicateurs de programme), elle pourrait, dans d'autres scénarios, être réalisée dans le système cible où les données sont importées, ou dans un logiciel intermédiaire ou une couche d'interopérabilité entre ces deux systèmes.

#### Coder des éléments de données { #coding-data-elements } 
Étant donné que les codes des combinaisons d'éléments de données et d'options de catégories seront ajoutés en tant qu'attributs aux indicateurs de programme, la première étape consiste à créer et/ou à ajouter un code aux éléments de données et aux combinaisons d'options de catégories. Cette opération doit être effectuée dans l'instance DHIS2 dans laquelle les valeurs des données agrégées seront sauvegardées. Si les éléments de données et les combinaisons d'options de catégorie ont déjà des codes, ceux-ci peuvent être utilisés. Il est également possible de définir des attributs personnalisés et de les affecter aux éléments de données à des fins de mapping, mais dans le cadre de ce guide, nous utiliserons le code intégré de l'élément de données.

Bien que cela ne soit pas strictement nécessaire, il peut être conseillé d'ajouter les éléments de données à un ensemble de données s'ils ne le sont pas déjà. Cet ensemble de données (ou ces ensembles) définit le type de période des données à transférer (par exemple, hebdomadaire, mensuel) et, lors de l'importation, les données agrégées du tracker seront validées par rapport à ce type de période. En outre, cette affectation peut servir de base au calcul ultérieur de la complétude des données.

#### Coder des indicateurs de programme{ #coding-program-indicators } 
Les indicateurs de programme ont un attribut fixe utilisé spécifiquement pour l'identifiant de la combinaison d'options de catégorie (et de la combinaison d'options d'attributs) qui est utilisé lorsque la valeur de l'indicateur de programme est exportée sous la forme d'un ensemble de valeurs de données.

<!-- TODO: Mise à jour de la capture d'écran avec des champs " vides "-->
![Champs d'indicateurs de programme pour la combinaison d'options de catégorie et d'attributs](resources/images/tracker_agg_coc_aoc_export.png)

Toutefois, il n'existe par défaut aucun champ correspondant permettant de spécifier l'identifiant (ex : code) de l'élément de données. En principe, le code de l'indicateur de programme lui-même *pourrait* être utilisé, mais cela échouera dans le scénario courant où plusieurs indicateurs de programme sont liés au même élément de données (avec différentes combinaisons d'options de catégorie). Il est donc recommandé de créer un [attribut](#about_attribute) attribué aux indicateurs de programme.

L'attribut personnalisé doit être du type `Text`. Il ne doit *pas* être obligatoire, car tous les indicateurs de programme ne seront pas liés à des éléments de données agrégés. Il ne doit *pas* être unique, puisque plusieurs indicateurs de programme peuvent pointer vers le même code d'élément de données. Enfin, il ne doit s'appliquer qu'à l'"indicateur de programme", puisqu'il n'est pas utile ailleurs. D'autres propriétés telles que le nom, la description et le code peuvent être définies en fonction de la convention de dénomination des métadonnées de l'implémentation en question. La capture d'écran ci-dessous montre comment l'attribut personnalisé inclus dans les paquets de métadonnées de l'OMS est configuré. Si cet attribut personnalisé a déjà été importé dans l'instance DHIS2 en question, il peut être réutilisé.

![Exemple de définition d'un attribut personnalisé permettant de relier les indicateurs de programme et les éléments de données agrégées.](resources/images/tracker_agg_custom_attribute_definition.png)

Une fois que l'attribut personnalisé est attribué aux indicateurs de programme, il apparaît comme un nouveau champ/attribut lors de l'ajout ou de la modification d'indicateurs de programme dans l'application Maintenance. Chaque indicateur de programme pour lequel des données doivent être transférées vers des éléments de données agrégés doit être créé et/ou modifié pour inclure le code de l'élément de données correspondant et le code de la combinaison d'options de catégorie.

L'ajout des indicateurs de programme à migrer vers un groupe d'indicateurs de programme peut s'avérer utile à la gestion d'un grand nombre d'indicateurs de programme. Par exemple, un script de migration des données peut cibler tous les indicateurs de programme dans un groupe d'indicateurs de programme, ce qui simplifie la configuration.

### L'API Web DHIS2 pour l'exportation et l'importation d'ensembles de valeurs de données (dataValueSets){ #dhis2-web-api-for-export-and-import-of-datavaluesets } 
Une fois que le mapping entre les indicateurs de programme et les éléments de données correspondants et les combinaisons d'options de catégorie a été effectué, les données agrégées des indicateurs de programme peuvent être exportées en tant que `dataValueSet` à partir du point de terminaison de l'API analytique et importées par la suite en tant que valeurs de données agrégées. Comme indiqué dans l'introduction, nous supposons, aux fins de ce guide, que les unités d'organisation sont identiques ou ont un identifiant commun dans l'instance DHIS2 dans laquelle les données doivent être importées et exportées.

#### Exportation { #export } 
Pour exporter des données à partir de l'API Web DHIS2, on utilise le point de terminaison `/api/analytics/dataValueSet`, décrit plus en détail dans la [documentation du développeur] (https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/analytics.html#webapi_analytics_data_value_set_format). Ce point d'accès peut renvoyer des données en représentation `JSON` ou `XML`. Il nécessite la spécification de trois paramètres :

* Données (dx) - qui sont les indicateurs de programme pour lesquels les données doivent être exportées.
* Période (pe) - la période pour laquelle les données doivent être exportées, laquelle doit correspondre au type de période des éléments de données agrégées vers lesquels les données doivent migrer.
* Unité d'organisation (uo) - les unités d'organisation pour lesquelles les données doivent être exportées.

Le format de ces paramètres est décrit en détail dans la [documentation du développeur] (https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/analytics.html#webapi_analytics_dimensions_and_items).

En plus de spécifier les données, la période et les unités d'organisation de la requête, il est également nécessaire de spécifier que les attributs personnalisés contenant les codes des éléments de données doivent être utilisés comme identifiant pour les valeurs de données dans l'ensemble de valeurs de données exporté. Pour ce faire, le paramètre facultatif `outputIdScheme` (schéma de sortie) doit pointer vers l'UID de l'attribut personnalisé. Les objets sans cet attribut (par exemple les unités d'organisation) seront ramenés à l'utilisation des UID.

Un appel API complet peut donc se présenter comme suit :
```
/api/analytics/dataValueSet.json?dimension=dx:Uvn6LCg7dVU;OdiHJayrsKo&dimension=pe:LAST_MONTH
&dimension=ou:lc3eMKXaEfw&outputIdScheme=ATTRIBUTE:vudyDP7jUy5
```

Cette requête renverra un fichier (au format JSON dans cet exemple) contenant les valeurs des données agrégées.

Comme indiqué dans la documentation sur le point de terminaison API `/analytics/dataValueSet`(analyse/ensemble de données), lors de l'utilisation de schémas d'identification basés sur les attributs pour l'exportation (comme dans ce guide), il y a un risque de produire des valeurs de données dupliquées. Cela peut se produire si plusieurs indicateurs de programme se sont vu attribuer la même combinaison d'éléments de données et de codes de combinaison d'options de catégorie. Le paramètre de requête booléen `duplicatesOnly` (doublons uniquement) peut être utilisé pour effectuer un débogage afin de ne renvoyer que les valeurs de données dupliquées, et cette vérification est recommandée après toute modification du mapping entre les indicateurs de programme et les éléments de données agrégées.
```
/api/analytics/dataValueSet.json?dimension=dx:Uvn6LCg7dVU;OdiHJayrsKo
 &dimension=pe:LAST_MONTH&dimension=ou:lc3eMKXaEfw&duplicatesOnly=true
```

Étant donné que l'exportation repose sur l'API analytique, seules les données incluses dans les [tableaux analytiques] (https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/maintaining-the-system/scheduling.html#scheduling_analytics_table) sont incluses. Par exemple, si les tableaux d'analyse sont programmés pour être mis à jour à minuit tous les jours et que le transfert est programmé à 23:00 tous les jours, les données de la journée en cours ne seront pas incluses.

#### Importation  { #import } 
Lorsqu'un fichier contenant des valeurs de données agrégées a été exporté depuis le point de terminaison `/api/analytics/dataValueSet` avec les paramètres appropriés décrits ci-dessus, il peut être importé directement dans l'instance DHIS2 vers laquelle les données doivent migrer. A des fins de test, le fichier de données peut être importé à l'aide de la fonction [Import/Export app] (https://docs.dhis2.org/en/use/user-guides/dhis-core-version-master/maintaining-the-system/importexport-app.html), ou via l'API Web DHIS2. Nous présentons ici comment utiliser l'API.

Le point de terminaison de l'API pour l'importation d'ensembles de valeurs de données est "/api/dataValueSets" (api/ensembles de valeurs de données), décrit plus en détail dans la [documentation destinée aux développeurs] (https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data.html#webapi_data_values). Les différents [paramètres d'importation] (https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/data.html#webapi_data_values_import_parameters) sont particulièrement importants et doivent être adaptés à nos besoins, comme décrit ici :

* `dataElementIdScheme` (schéma de données) et `categoryOptionComboIdScheme` (schéma d'options de catégorie) doivent avoir la valeur `code`, car nous utilisons des codes pour mapper les valeurs des indicateurs de programme aux éléments de données agrégés et aux combinaisons d'options de catégorie.
*  `orgUnitIdScheme`(schéma d'unité d'organisation) doit être défini de manière appropriée pour chaque cas particulier.
* `dryRun` (exécution à blanc) permet d'obtenir un résumé de l'importation sans importer les données, ce qui peut être utile pour les tests.
* `importStrategy`( Stratégie d'importation) devrait dans la plupart des cas être réglé sur `CREATE_AND_UPDATE`( Créer et mettre à jour), ce qui signifie que les nouvelles valeurs de données seront importées et que les valeurs existantes seront mises à jour. Dans certains cas, il *peut* être judicieux de ne mettre que `CREATE` (créer) ou `UPDATE` (mettre à jour), par exemple si l'on décide de ne pas mettre à jour les données existantes après un certain temps, mais d'autoriser l'ajout de nouvelles données. Ce point a été discuté plus en détail dans les [considérations de l'implémentation] (#implementation-considerations).

Cet exemple montre comment spécifier les paramètres appropriés lors de l'importation de données à l'aide de l'API :

```
/api/dataValueSets/dataElementIdScheme=CODE&categoryOptionComboIdScheme=CODE&importStrategy=CREATE_AND_UPDATE&dryRun=false
```

### Rédaction de scripts pour automatiser la migration des données { #writing-scripts-to-automate-data-migration } 
Un modèle de script permettant d'automatiser la migration de routine des données du tracker vers l'agrégat, au sein d'une même instance ou entre des instances DHIS2 distinctes, sera bientôt mis à disposition. Qu'il s'agisse d'adapter ce modèle ou de développer des outils ou des scripts personnalisés pour effectuer la migration, certaines recommandations doivent être suivies.

* Séparer le script exécutant l'exportation et l'importation de la configuration des données à migrer. Cela permet de modifier plus facilement la configuration sans risquer d'introduire des erreurs dans la logique du script et facilite également la mise en place de configurations multiples (c'est-à-dire une pour chaque programme tracker).
* Le script doit produire un journal contenant des événements et des informations clés, tels que le moment où le script a été lancé, un résumé des résultats de l'importation (en cas de succès) ou les détails de l'erreur (en cas d'échec).
* Un système doit être mis en place pour informer les personnes chargées de la migration des données en cas d'erreur, par exemple par le biais d'un serveur de messagerie configuré sur le serveur, ou en utilisant la fonctionnalité de messagerie du DHIS2 lui-même (accessible via l'API Web).
* Étant donné que l'exportation des données repose sur le point de terminaison analytique, il peut être utile que le script déclenche l'analyse et l'exportation une fois que ce processus est terminé.

### Packages de données numériques DHIS2 et liens entre les données du tracker et les données agrégées{ #dhis2-digital-data-packages-and-linking-tracker-and-aggregate-data } 
Les ensembles de données numériques du DHIS2 ont été développés pour favoriser la production de rapports et d'analyses agrégés, ainsi que la saisie de données du tracker et l'analyse au niveau de l'établissement. De plus amples informations sont disponibles sur [dhis2.org/who] (https://dhis2.org/who).

Des ensembles de données numériques agrégées (y compris des tableaux de bord agrégés standard) sont disponibles pour les programmes de santé tels que la tuberculose, le VIH, le paludisme, le RMNCAH et le suivi des maladies. Les ensembles de données agrégées comprennent: 

1. Ensemble de données, éléments de données et ensembles d'options de catégorie ("cible" pour l'envoi de données de suivi)
2. Codes de métadonnées conformes à ADX et permettant le mapping des valeurs de données du tracker vers l'agrégat "cible".

En outre, des ensembles de données de suivi sont en cours d'élaboration pour un nombre croissant de cas d'utilisation, tels que les registres électroniques de vaccination et le suivi basé sur les cas pour la tuberculose, le VIH et les rapports intégrés sur les maladies. Lorsque les ensembles de données de suivi sont conçus pour saisir des données qui peuvent être agrégées et soumises à l'ensemble de données agrégé correspondant, nous avons inclus les éléments suivants dans les ensembles de données numériques de suivi :

1. Les indicateurs de programme configurés pour produire des valeurs de données correspondant aux éléments de données et aux désagrégations inclus dans les données du pack de données numériques agrégées.
2. Attribut personnalisé pour "Code de l'élément de données agrégé".
3. Attributs par indicateur de programme, alimentés par les codes des éléments de données et le code de combinaison des options de catégorie de l'ensemble des données numériques agrégées.

### Résumé { #summary }
Etapes pour faire migrer les données de suivi vers des valeurs de données agrégées :

1. Définir une liste des variables pour lesquelles les données doivent être générées et transférées.
2. S'assurer que les éléments de données agrégées auxquels les données seront associées existent et ont un code.
3. Veiller à ce que les combinaisons d'options de catégorie attribuées à ces éléments de données aient un code.
4. Créer un attribut personnalisé affecté aux indicateurs de programme.
5. Assurez-vous que les indicateurs de programme produisant les valeurs des données agrégées existent, et attribuez-leur le code de la combinaison d'éléments de données et d'options de catégorie correspondante.
6. Exporter les valeurs des indicateurs de programme en tant qu'ensemble de valeurs de données en utilisant le point de terminaison de l'API Web `/api/analytics/dataValueSet`(analyse/ensemble de valeurs de données) dans l'instance DHIS2 qui héberge les données du tracker.
7. Importez l'ensemble de valeurs de données vers le point de terminaison `/api/dataValueSet`(api/ensemble de valeurs de données) de l'API Web dans l'instance DHIS2 qui contiendra les données agrégées.

### Problèmes connus { #known-issues } 
- Il existe un bug dans les versions antérieures 2.33-36 qui empêche les attributs personnalisés d'être exposés dans l'interface utilisateur ([Jira 8755](https://jira.dhis2.org/browse/DHIS2-7230)). Ce problème est résolu dans les dernières versions corrigées de DHIS2.
- Il y a un bug ([Jira 8868](https://jira.dhis2.org/browse/DHIS2-8868)) qui fait que l'outil metadata-dependency-export (métadonnées-dépendance-exportation) échoue lorsque des attributs personnalisés sont affectés à des indicateurs de programme.

