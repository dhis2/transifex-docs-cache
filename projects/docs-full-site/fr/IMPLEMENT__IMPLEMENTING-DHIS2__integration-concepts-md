---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/implementation/integration-concepts.md"
revision_date: '2021-09-15'
tags:
- Implémentation
---

# Concepts d'intégration { #integration } 

DHIS2 est une plateforme ouverte et ses implémenteurs contribuent activement
aux initiatives d'interopérabilité, telles que openHIE. La base de données de l'application
DHIS2 est conçue dans un souci de flexibilité. Les structures de données telles
que les éléments de données, les unités d'organisation, les formulaires et les rôles des utilisateurs peuvent être définis
en toute liberté via l'interface utilisateur de l'application. Cela permet
d'adapter le système à une multitude de contextes locaux 
et de cas d'utilisation. Le DHIS2 répond à de nombreuses exigences en matière de saisie et d'analyse des données de routine
qui apparaissent dans les mises en œuvre nationales, à la fois pour les scénarios HMIS 
et en tant que système de collecte et de gestion des données de base dans 
des domaines tels que [la logistique, la gestion des laboratoires et 
les finances] (#Intégration_et_interopérabilité).

## Intégration et interopérabilité { #Integration_and_interoperability } 

Sur la base de l'approche de sa plate-forme, le DHIS2 est en mesure de recevoir et d'héberger
des données provenant de différentes sources et de les partager avec d'autres systèmes et mécanismes 
de rapport. Une distinction importante des concepts d'intégration est la 
différence entre l'intégration des données et l'interopérabilité des systèmes:

  - Lorsque l'on parle d'**intégration**, on pense au processus qui vise à
    faire apparaître différents systèmes d'information comme un seul, à mettre
    les données électroniques à la disposition de tous les utilisateurs concernés, ainsi qu'à
    l'harmonisation des définitions et des dimensions afin qu'il soit possible 
    de combiner les données d'une manière utile.

  - Un concept apparenté est l'**interopérabilité**, qui est une des stratégies
    permettant l'intégration. Nous considérons que DHIS2 est interopérable avec d'autres
    applications logicielles en raison de sa capacité à échanger des données.
    Par exemple, DHIS2 et OpenMRS sont interopérables, car ils permettent
    de partager des définitions de données et des données entre eux. L'interopérabilité
    dépend des normes relatives aux formats de données, aux interfaces, aux codes et
    aux terminologies. Dans l'idéal, il s'agirait de normes convenues au niveau international,
    mais dans la pratique, il peut également s'agir de normes de facto
    (qui sont largement acceptées et utilisées, mais qui ne font pas nécessairement
    l'objet d'un vote formel au sein d'un organisme de normalisation) et d'autres 
    accords plus locaux dans un contexte particulier.

DHIS2 est souvent utilisé comme un entrepôt de données intégré, car il contient 
des données (agrégées) provenant de diverses sources, telles que [la santé de la mère et de l'enfant, 
le programme de lutte contre le paludisme, les données de recensement et les données sur les stocks et les ressources 
humaines] (#Objectifs_de_l'intégration). Ces sources de données partagent la 
même plateforme, DHIS2, et sont disponibles au même endroit. Ces 
sous-systèmes sont donc considérés comme intégrés dans un seul système.

L'interopérabilité permettra en outre d'intégrer des sources de données provenant d'autres
applications logicielles. Par exemple, si les données de recensement sont stockées dans un
[registre d'état civil ou dans un système d'événements vitaux] spécialisé 
(#Information_Santé), l'interopérabilité entre cette base de données et 
le DHIS2 signifierait que les données de recensement seraient également accessibles dans le DHIS2.

Enfin, l'activité d'intégration la plus fondamentale (qui n'est pas toujours prise 
en compte dans le débat sur l'interopérabilité) est la possibilité 
d'intégrer dans le DHIS2 des données provenant de systèmes sur support papier existants
ou de systèmes verticaux parallèles. Les données seront saisies directement dans DHIS2 sans passer 
par une autre application logicielle. Ce processus est basé sur 
la création de définitions d'indicateurs cohérentes et peut déjà réduire considérablement 
la fragmentation et améliorer l'analyse des données grâce à un référentiel de données
intégré.

## Objectifs de l'intégration { #Objectives_of_integration } 

Dans la plupart des pays, on trouve de nombreux systèmes **isolés** d'information 
sur la santé, ce qui pose de nombreux problèmes de gestion de l'information. 
Les Systèmes d'Information de Santé Publique ont connu une croissance explosive et souvent 
non coordonnée au cours des dernières années. Les technologies modernes de l'information 
rendent moins coûteuse la mise en œuvre de solutions ICT4D, ce qui peut conduire à une
grande diversité de solutions. Un exemple stupéfiant a été la déclaration du moratoire sur la mSanté 
du ministère ougandais de la santé en 2012, en réaction à une 
avalanche d'environ [50 solutions de 
mSanté] (http://www.ictworks.org/2012/02/22/ugandan-mhealth-moratorium-good-thing) 
qui ont été mises en œuvre en l'espace de quelques années. La plupart de ces 
solutions étaient des approches autonomes qui ne partageaient pas leurs données avec 
les systèmes nationaux et qui ont rarement été développées au-delà du statut de projet pilote.

Cela peut conduire à la conclusion que tous les systèmes devraient être connectés ou 
que **l'interopérabilité est un objectif** en soi. Cependant, le DHIS2 est 
souvent utilisé dans des contextes où l'infrastructure est faible et où 
les ressources nécessaires pour faire fonctionner les systèmes de base de manière fiable sont rares. La fragmentation 
est un problème sérieux dans ce contexte, mais les approches d'interopérabilité 
ne peuvent résoudre qu'une partie des problèmes de fragmentation - et 
souvent les approches d'interopérabilité entraînent une couche supplémentaire de 
complexité.


>**Exemple**
>
> **Complexité des solutions logistiques au Ghana** 
> Dans le domaine de la logistique ou de la gestion de la chaîne d'approvisionnement, on trouve souvent une multitude de solutions logicielles parallèles. Celles-ci se chevauchent ou se font concurrence au sein d'un même pays. Comme l'indique le site [Étude de JSI en 2012](http://docplayer.net/23773118-Ghana-landscape-analysis-of-supply-chain-management-software-tools-in-use.html), il a été rapporté que dix-huit (18!) outils logiciels différents ont été utilisés dans la chaîne d'approvisionnement de santé publique, rien qu'au Ghana.

L'interopérabilité des systèmes semble donc être une possibilité d'éliminer 
la fragmentation et les redondances et de donner aux agents de santé publique une image concise 
et équilibrée des sources de données disponibles. Toutefois, l'effort nécessaire pour
connecter de nombreuses solutions logicielles redondantes serait très important et 
semble donc discutable. Dans un premier temps, l'accent devrait être mis sur 
la **réduction du nombre de systèmes parallèles** et sur l'identification des systèmes les plus 
performants, qui pourront ensuite être intégrés.

Sur cette base, nous souhaitons définir les principaux objectifs 
des approches d'intégration du DHIS2 :

  - **Calcul des indicateurs** : De nombreux indicateurs sont basés sur
    des numérateurs et des dénominateurs provenant de différentes sources de données. Les exemples
    sont notamment les taux de mortalité, avec certaines données sur la mortalité comme numérateur 
    et des données sur la population comme dénominateur, les taux de couverture du personnel 
    et de charge de travail du personnel (données sur les ressources humaines et données sur la population et les 
    effectifs), les taux de vaccination, et ainsi de suite. Pour le calcul, vous
    avez besoin des données du numérateur et du dénominateur, qui doivent donc
    être intégrées dans un entrepôt de données unique. Plus il y a de sources
    de données intégrées, plus il est possible de générer des indicateurs à partir
    du référentiel central.

  - **Réduire le traitement manuel** et la saisie des données : Les différentes
    données étant regroupées au même endroit, il n'est pas nécessaire d'extraire et de traiter manuellement les 
    indicateurs, ni de réintroduire les données dans l'entrepôt de données.
    L'interopérabilité entre les systèmes de différents types de données
    (tels que les registres de patients et les entrepôts de données agrégées) permet 
    aux logiciels des sous-systèmes de calculer et de partager des données
    par voie électronique. Cela réduit le nombre d'étapes manuelles impliquées dans
    le traitement des données, ce qui améliore la qualité des données.

  - **Réduire les redondances** : Souvent, les données qui se chevauchent et qui sont redondantes sont 
    saisies par les différents systèmes parallèles. Par exemple,
    les éléments de données relatifs au VIH/SIDA seront-ils saisis à la fois 
    par les multiples programmes généraux de conseil et de dépistage et par le programme spécialisé
    sur le VIH/SIDA. L'harmonisation des outils de collecte de données de ces programmes
    réduira la charge de travail totale des utilisateurs finaux. Ceci
    signifie que ces sources de données peuvent être intégrées dans DHIS2 et
    harmonisées avec les éléments de données existants, ce qui implique des exigences
    en matière de saisie et d'analyse des données.

  - Améliorer les **aspects organisationnels** : Si toutes les données peuvent être traitées par
    une seule unité au sein du ministère de la santé, au lieu de divers sous-systèmes
    gérés par les différents programmes de santé, cette unité peut être
    professionnalisée. Avec un personnel dont la seule responsabilité est la gestion,
    le traitement et l'analyse des données, des compétences plus spécialisées peuvent être
    développées et le traitement de l'information peut être rationalisé.

  - Intégration de **programmes verticaux** : Le domaine typique de la santé publique
    comporte de nombreux acteurs et systèmes existants. Une base de données intégrée
    contenant des données provenant de diverses sources est plus précieuse
    et plus utile que des bases de données fragmentées et isolées. Par exemple, lorsque
    l'analyse des données épidémiologiques est combinée avec des données spécialisées
    [sur le VIH/SIDA, la tuberculose, les ressources financières et humaines, ou lorsque
    l'immunisation est combinée avec des données sur la logistique/le stock](#nn), on
    obtient une image plus complète de la situation.

DHIS2 peut contribuer à la rationalisation et à la **simplification de l'architecture du système**, 
en répondant à des questions telles que : Quel est l'objectif de l'effort d'intégration ? 
Le DHIS2 peut-il contribuer à réduire le nombre de systèmes ? L'intégration du DHIS2 peut-elle 
contribuer à fournir des informations de gestion pertinentes à moindre
coût, à plus grande vitesse et avec une meilleure qualité de données que les 
systèmes existants ? Le DHIS2 est-il le meilleur outil pour remplacer d'autres systèmes, ou une 
autre solution adaptée et interopérable avec le DHIS2 est-elle plus 
appropriée ? Des informations plus pratiques sur la définition de ces objectifs sont 
disponibles dans la *[ÉTAPE 1 du guide de mise en œuvre
en 6 étapes *] (https://www.dhis2.org/downloads).

## Échange d'informations sur la santé{ #Health_information } 

Étant donné qu'il existe différents cas d'utilisation des informations sur la santé, il existe 
différents types d'applications logicielles fonctionnant dans le secteur de la santé. 
Nous utilisons le terme d'architecture de l'information sur la santé pour décrire 
un plan ou un aperçu des différentes applications logicielles, de leurs utilisations spécifiques 
et des connexions de données. L'architecture sert de plan pour 
coordonner le développement et l'interopérabilité des différents sous-systèmes 
au sein d'un système d'information sur la santé plus vaste. Il est conseillé d'élaborer 
un plan qui couvre tous les composants, y compris les domaines qui 
n'utilisent actuellement aucun logiciel, afin d'être en mesure de voir de manière adéquate 
les exigences en termes de partage des données. Ces exigences devraient ensuite 
faire partie des spécifications du logiciel une fois qu'il est développé ou 
acheté.

Le **[openhealth information exchange (openHIE)] (https://ohie.org/)** 
est une interprétation interopérable de cette architecture, dans laquelle un HMIS ou 
le DHIS2 joue souvent un rôle important. Le cadre openHIE a 
été développé avec un accent particulier mis sur les pays à faibles ressources, 
grâce à la participation de plusieurs institutions et partenaires de développement, 
y compris le programme HISP d'Oslo.

L'aperçu schématique ci-dessous montre les principaux éléments du cadre openHIE, 
qui comprend une couche de composants, une couche de services d'interopérabilité 
et des systèmes externes. La couche de composants openHIE couvre les métadonnées ou
données de référence (terminologie, clients, établissements), les données personnelles (personnel, 
antécédents des patients) et les statistiques nationales sur la santé. L'objectif est de 
garantir la disponibilité des mêmes métadonnées dans tous les systèmes qui 
participent à l'échange de données correspondant (par exemple, les définitions des indicateurs, 
la dénomination des établissements, le codage et la classification). Dans certains cas,
comme celui du registre principal des établissements, les données peuvent également être utilisées 
pour fournir des informations au grand public par l'intermédiaire d'un portail web. Alors que
la couche d'interopérabilité assure le courtage des données entre les différents 
systèmes, la couche des systèmes externes contient plusieurs sous-systèmes, dont la plupart se situent 
au niveau des points de service, dont les fonctions se chevauchent souvent.

Il existe différentes approches pour définir une architecture de cybersanté. Dans le 
contexte de la ligne directrice DHIS2, nous distinguons les approches basées 
sur une connexion 1:1 par rapport aux approches basées sur une connexion n:n 
(many-to-many).

### *1:1* intégration { #integrationSection } 

Dans de nombreux pays, un HMIS national est souvent le premier système à être déployé 
dans un grand nombre d'établissements et à gérer un grand nombre de données 
sur une base mensuelle ou trimestrielle. Lorsque les pays commencent à développer 
l'architecture de leur système de santé, DHIS2 est souvent connecté à 
d'autres systèmes. Cette connexion se fait souvent directement par un 
simple script qui automatise le transfert des données.

On parle de connexion 1:1 parce qu'elle est limitée à deux systèmes. Dans le 
cas d'une intégration LMIS/HMIS, un LMIS transférera des données au DHIS2 
omme défini dans le script. Cette approche pratique représente souvent une 
première étape et constitue l'un des cas d'utilisation les plus courants sur la voie d'une 
architecture openHIE interopérable. Toutefois, cette simplicité présente également 
des inconvénients : Dans le cas où un deuxième système logistique souhaiterais 
transférer des données à DHIS2 (par exemple, des données sur les produits 
pour un programme de lutte contre une maladie spécifique), un deuxième script devra être écrit pour effectuer cette 
tâche. Ces deux scripts s'exécuteraient alors indépendamment l'un de l'autre, 
ce qui donnerait lieu à deux connexions 1:1 distinctes.

### Intégration *n:n*.{ #nn } 

Une autre approche consiste à placer un logiciel spécialement conçu pour 
servir de **couche d'interopérabilité** ou d'approche BUS, gérant le 
transfert de données entre plusieurs systèmes possibles de part et d'autre (n:n). 
Cela pourrait être le cas si, par exemple, vous vouliez collecter des données au niveau 
des stocks par le biais de différentes applications du LMIS, puis les partager avec 
un LMIS d'entrepôt central, le HMIS et un système de programmes verticaux de lutte contre les maladies. Le 
logiciel de référence openHIE qui assume ce rôle est ["OpenHIM"] (http://openhim.org), mais
des systèmes tels que ["MOTECH"] (https://motechproject.org/) ont également été utilisés 
à cet effet, comme nous le verrons plus bas.

Bien que cette approche puisse entraîner un effort initial plus important, elle promet 
de faciliter les projets d'intégration ultérieurs, car la couche d'interopérabilité 
est alimentée par des définitions et des mappings qui peuvent être 
réutilisés pour connecter les futurs systèmes.

Dans la pratique, cette approche pose certains problèmes. L'activation des 
API nécessite un effort considérable de la part de ressources qualifiées et, à 
chaque nouvelle version d'un système impliqué, les flux de données doivent être testés 
à nouveau et, le cas échéant, adaptés. En outre, pour réussir, ces 
projets de mise en œuvre doivent généralement passer par une série 
d'[*étapes complexes*](https://www.dhis2.org/downloads), telles que 
l'accord sur une approche de l'interopérabilité intégrée dans la stratégie nationale 
de cybersanté, la définition de normes de données et d'une structure de 
maintenance durable, et l'obtention d'un consensus entre les parties prenantes sur la
propriété des données et les politiques de partage. L'interconnexion des données et des 
systèmes peut avoir des conséquences à long terme : elle crée de nouveaux rôles, emplois 
et tâches qui n'existaient pas auparavant et qui n'avaient peut-être pas été prévus 
(gouvernance des métadonnées, administration de systèmes complexes, négociateurs de 
limites, etc.)


> **Exemple**
>
> **Couche intermédiaire Grameen DHIS2/CommCare au Sénégal** 
> Dans les [notions d'intégration](#integration), [MOTECH](https://motechproject.org/) sert de couche intermédiaire technique entre un système LMIS pour la collecte de données mobiles au niveau des établissements de santé ([CommCare](http://www.commcarehq.org)) et DHIS2. On va ainsi l'utiliser pour définir le mappage des données, les règles de transformation et les contrôles de qualité des données. L'interface est configurée pour transférer les données de CommCare Supply vers DHIS2 chaque fois que des données sont enregistrées dans un formulaire CommCare dans les établissements. Pour chaque produit de base, les données relatives à la consommation, au stock disponible, aux pertes et aux ruptures de stock sont transférées de CommCare vers DHIS2. 
La hausse de l'investissement initial de l'approche sénégalaise laisse entrevoir une architecture système plus ambitieuse à long terme, en prévision du fait que la plateforme MOTECH peut être utilisée pour accueillir d'autres tâches d'interopérabilité à l'avenir. Cependant, nous observons qu'aucune des activités nationales n'est étroitement intégrée dans une architecture de cybersanté, ce qui définirait clairement les domaines prioritaires, les systèmes principaux pour chaque priorité, ainsi que les relations et les API qui en découlent entre ces différents composants. On peut affirmer que les projets d'interopérabilité reposent sur des bases fragiles en l'absence de consensus préalable sur un plan directeur architectural. D'un autre côté, il est également utile de permettre aux initiatives du système de se développer organiquement, tant qu'elles sont ancrées dans des besoins nationaux bien fondés.

### Architecture, normes et mapping { #architecture-standards-and-mapping } 

Un élément important d'une architecture de cybersanté est l'inclusion de 
**normes internationales de cybersanté**. Les normes sont particulièrement importantes 
pour les connexions n:n, et le sont moins pour les connexions directes (1:1).

Certaines normes se situent au niveau technique (par exemple, les méthodes de transmission), 
d'autres au niveau du contenu (par exemple, les 100 indicateurs de base de l'OMS). L'alignement progressif 
des initiatives des systèmes nationaux sur ces normes peut permettre 
aux pays d'accéder à des solutions avérées, en bénéficiant de l'innovation médicale et 
technologique.


> **Exemple**
>
> **PEV du Ghana** 
> Le cas du Ghana illustre comment les exigences de l'OMS en matière d'établissement de rapports du PEV servent à définir des données standard dans DHIS2. Cette normalisation au niveau des ensembles de données et de la terminologie est la base de l'intégration du système. Concernant le système DHIS2, des travaux sont en cours avec l'OMS pour développer des ensembles de données normalisés, qui pourraient à l'avenir ouvrir de nouvelles possibilités d'interopérabilité et améliorer l'efficacité en s'assurant que les métadonnées restent relativement cohérentes entre les systèmes, et en encourageant également les pays à réutiliser les solutions existantes.

Au niveau **linguistique**, il est nécessaire d'être cohérent dans 
les définitions. Si vous disposez de deux sources de données pour les mêmes données, elles doivent 
être comparables. Par exemple, si vous recueillez des données sur le paludisme auprès de 
cliniques standard et d'hôpitaux, ces données doivent décrire la 
même chose si elles doivent être combinées pour les totaux et les indicateurs. Si un 
hôpital rapporte les cas de paludisme par sexe mais pas par groupe d'âge, et que d'autres 
cliniques les rapportent par groupe d'âge mais pas par sexe, ces données ne peuvent être 
analysées en fonction de l'une ou l'autre de ces dimensions (même s'il est possible de 
calculer le nombre total de cas). Il est donc nécessaire de se mettre d'accord sur 
des définitions uniformes.

Outre des définitions uniformes dans les différents sous-systèmes, 
des **normes d'échange de données** doivent être adoptées si les données doivent être partagées 
par voie électronique. Les différentes applications logicielles en ont besoin pour se 
comprendre. DHIS2 prend en charge plusieurs formats de données 
lors de l'importation et de l'exportation, y compris la norme la plus courante, ADX. D'autres 
applications logicielles prennent également en charge ce format, qui permet le 
partage des définitions de données et des données agrégées entre elles. Pour DHIS2, 
cela signifie qu'il prend en charge l'importation de données agrégées fournies par 
d'autres applications, telles que [OpenMRS] (http://openmrs.org) (pour la gestion 
des patients) et [iHRIS] (https://www.ihris.org/) (pour la gestion des 
ressources humaines).

Un élément crucial de l'architecture est la manière d'organiser le **mapping** 
des données. Généralement, les métadonnées des différents systèmes ne correspondent pas exactement. 
À moins qu'un ministère de la santé n'ait mis en œuvre une politique conséquente de normalisation des données, 
différents systèmes auront des codes et des étiquettes différents pour un établissement. 
Un système peut l'appeler *Hôpital de district - 123*, l'autre système peut
l'appeler Centre de traitement du paludisme - 15. Pour pouvoir transférer 
des données, il faut stocker à un endroit donné les informations correspondant 
à ces deux établissements.

Dans le cas d'une connexion 1:1, cette correspondance doit être établie et 
maintenue pour chaque connexion ; dans le cas d'une approche d'interopérabilité 
n:n, un côté des définitions peut être réutilisé.

Afin de garantir la fluidité des données, vous devez définir 
clairement les responsabilités de part et d'autre du système en ce qui concerne la 
maintenance des données et la résolution des problèmes. Par exemple, des procédures 
standard doivent être définies au préalable pour des activités telles que l'ajout, 
le changement de nom, la désactivation temporaire ou la suppression d'une installation dans l'un ou l'autre 
des deux systèmes. Les modifications des champs de la base de données qui sont inclus dans un 
enregistrement de données transféré doivent également être coordonnées de manière systématique.

## Données agrégées et transactionnelles { #aggregate-and-transactional-data } 

Le système DHIS2 a étendu sa portée à de nombreux systèmes de santé. Partant 
de ses bases familières d'ensembles de données agrégées pour les données de routine, il a
inclus des données relatives aux patients, puis des données dans les domaines des RH, des finances, 
de la logistique et de la gestion des laboratoires, pour évoluer vers des données opérationnelles ou 
transactionnelles.

Nous pouvons faire la différence entre les données transactionnelles et les données agrégées. Un 
**système transactionnel** (ou système opérationnel du point de vue de l'entrepôt 
de données) est un système qui collecte, stocke et modifie des données 
précises. Ce système est généralement utilisé au jour le jour pour la 
saisie et la validation des données. Le design est optimisé pour améliorer les performances des insertions et 
des mises à jour. Le système DHIS2 peut incorporer des données agrégées provenant de sources de données 
externes, normalement agrégées dans la dimension spatiale (la hiérarchie des unités 
organisationnelles), la dimension temporelle (sur plusieurs périodes) et pour 
les formules des indicateurs (expressions mathématiques comprenant des éléments de données).

Lorsque nous envisageons un système transactionnel, tel qu'un logiciel de logistique pour 
l'ensemble de la chaîne d'approvisionnement ou certaines de ses parties, nous devons prendre une 
décision fondamentale : Avez-vous besoin de suivre toutes les transactions détaillées à tous
les niveaux, y compris les opérations telles que les retours, les transferts entre 
installations, la lecture des codes-barres, la gestion des lots et des dates de péremption ? Ou bien pouvez-vous obtenir 
la plupart des résultats nécessaires à la prise de décision en utilisant des données agrégées ?

Les chaînes d'approvisionnement peuvent souvent être bien contrôlées et, dans une certaine mesure, gérées, 
pour autant que les données soient disponibles de manière fiable à l'endroit et au moment où elles sont nécessaires 
pour les décisions opérationnelles et à des fins de contrôle. Les principaux 
indicateurs *entrée, consommation et niveau des stocks en fin de période* peuvent 
être gérés sans transactions électroniques et suffisent souvent à donner une 
vue d'ensemble des performances du système, ce qui peut réduire les besoins 
d'investissement dans le système.

Il est important d'être réaliste quant aux données à collecter, à leur fréquence et  qui 
les utilisera, afin de ne pas créer des systèmes qui échouent 
en raison d'un manque d'utilisation ou d'attentes irréalistes quant à la manière dont les données seront 
utilisées. Les systèmes numériques de gestion de la logistique fonctionnent bien lorsqu'ils 
sont pleinement intégrés dans les flux de travail habituels et qu'ils sont conçus pour 
faciliter le travail des utilisateurs ou le rendre plus efficace.

> **Remarque**
> 
> L'attente selon laquelle des données plus détaillées conduisent à une meilleure gestion logistique 
> n'est pas toujours satisfaite. Parfois, la tentative ambitieuse de 
> collecter régulièrement des données sur les transactions logistiques se traduit par une baisse 
> de la qualité des données, par exemple parce que l'enregistrement des données, qui devrait
> se faire sur une base quotidienne plutôt que mensuelle ou trimestrielle, n'est 
> pas effectué de manière fiable. En revanche, si le système transactionnel 
> est bien entretenu et contrôlé, des données plus détaillées peuvent aider 
> à identifier les inexactitudes et les problèmes de qualité des données, à réduire le gaspillage (dû 
> à la péremption ou à la défaillance du CCE), à soutenir un rappel, à gérer les performances et 
> à améliorer la prise de décision au sein de la chaîne d'approvisionnement. L'analyse 
> de données détaillées peut aider à découvrir les causes profondes de certains problèmes et 
> à améliorer la qualité des données à long terme.

Le DHIS2 peut jouer différents rôles dans les scénarios d'interopérabilité. Un scénario 
d'interopérabilité courant consiste à ce que le DHIS2 reçoive des données agrégées d'un 
système opérationnel, dans lequel le système opérationnel additionne les 
transactions avant de les transmettre au DHIS2. Toutefois, le DHIS2 pourrait aussi, dans une 
certaine mesure, être configuré pour stocker des données transactionnelles détaillées, 
qu'il reçoit de systèmes externes ou qui sont saisies directement dans 
le DHIS2.

Sur cette base, nous tentons d'établir une vue d'ensemble comparative, en comparant la 
gestion des données agrégées du DHIS2 avec la gestion des données d'un système spécialisé 
externe. Cela peut servir d'orientation approximative, mais n'est pas statique puisque 
les capacités du DHIS2 et son interprétation par les implémenteurs 
s'élargissent presque à chaque version.


| Zone | DHIS2 agrégé | Systèmes spécialisés externes |
|---|---|---|
| Logistique | Des données agrégées, par exemple les niveaux mensuels des stocks des établissements, peuvent être envoyées via le DHIS2. Le système DHIS2 peut produire des rapports simples sur les niveaux de stock ainsi que la consommation. | La gestion de la chaîne d'approvisionnement soutient les opérations du système logistique et peut suivre les mouvements de stocks en détail (émission, réapprovisionnement, affectation, gaspillage) et enregistrer des informations telles que les numéros de lot de production. Les systèmes MSC créent des rapports de prévision, de réapprovisionnement et de contrôle élaborés, rendant ainsi possible le suivi en temps réel des niveaux de stock, des notifications (stock insuffisant, gestion du flux de travail, défaillance du matériel frigorifique, etc.), des prévisions étayées et des commandes d'urgence. |
| Finances | Des données agrégées, comme par exemple les dépenses totales ou le niveau des liquidités, peuvent être envoyées via le DHIS2. Le système DHIS2 peut produire des rapports simples de synthèse financière sur les budgets restants par exemple. | Les systèmes de gestion financière permettent une traçabilité complète des transactions financières conformément aux exigences légales, notamment la budgétisation, les transferts, les annulations, les remboursements, etc. Le marquage multidimensionnel des transactions permet d'établir des rapports analytiques. |
| Suivi des patients | Les données relatives aux maladies ou aux programmes sont collectées via le DHIS2. Le DHIS2 Tracker permet également d'obtenir une vue longitudinale simplifiée des dossiers médicaux, y compris l'historique du patient et les cheminements cliniques multi-étapes. | Les systèmes de gestion hospitalière spécialisés peuvent couvrir et optimiser des flux de travail complexes entre différents services (par exemple, réception, comptoir de paiement, salles, services de consultations externes, services d'hospitalisation, laboratoire, imagerie, salle de stockage, administration des finances et des ressources humaines, maintenance des dispositifs médicaux, etc.) |
| Ressources humaines | Le système DHIS2 collecte des indicateurs liés aux ressources humaines, par exemple les postes prévus et les postes vacants par établissement. | Un système spécialisé de gestion des ressources humaines peut assurer le suivi des informations détaillées sur le statut et les mutations d'un agent de santé (accréditation, promotion, congé sabbatique, changement de poste, changement de lieu, formation complémentaire). Ce système prévoit des rapports prédéfinis permettant de superviser et de planifier les opérations. |

## Différents scénarios d'intégration du DHIS2{ #different-dhis2-integration-scenarios } 

Les différents objectifs décrits ci-dessus conduisent à différents scénarios 
d'intégration. Le système DHIS2 peut assumer plusieurs **rôles** dans une architecture de système:

  - Saisie des données : saisie des données (hors ligne, mobile), importation des données (données transactionnelles,
    données agrégées)

  - Stockage, visualisation et analyse des données à l'aide d'outils intégrés (DWH,
    rapports, SIG)

  - Partage des données avec des outils externes (comme DVDMT), via des API ou des applications web

    Dans les paragraphes suivants, nous examinons les approches de saisie 
    et de partage des données, puis nous présentons l'exemple de l'intégration verticale
    dans laquelle le DHIS2 joue souvent tous ces rôles.

    Le rôle du DHIS2 dans le stockage, la visualisation et l'analyse des données est abordé
    séparément dans la [section sur l'entrepôt
    de données](https://docs.dhis2.org/master/en/implementer/html/ch05.html).

### Saisie des données { #data-input } 

La manière dont le DHIS2 traite l'entrée des données comporte plusieurs aspects. Au 
niveau le plus élémentaire, le DHIS2 sert à remplacer ou au moins à refléter les formulaires 
de collecte de données sur support papier, en intégrant les données par voie électronique. Il en résultera 
des activités **de saisie manuelle des données** au niveau de l'établissement ou de l'administration 
de la santé. L'option suivante consiste à **importer des données**. Le DHIS2 
permet d'importer des données par le biais d'une interface utilisateur, ce qui est une méthode 
nécessitant peu de connaissances techniques, mais qui doit être exécutée manuellement 
chaque fois que des données doivent être mises à disposition. Une description détaillée des 
fonctions d'importation est disponible dans les [guides de l'utilisateur 
DHIS2] (https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#import).


> **Conseil**
>
> La saisie manuelle des données et l'approche d'importation nécessitent relativement peu d'efforts techniques. Elles peuvent également être utilisées temporairement pour piloter une approche d'intégration de données. Cela permet à l'utilisateur de tester des indicateurs et des rapports, sans avoir à employer des ressources techniques dédiées au développement de fonctions d'interopérabilité automatisées, que ce soit par une connexion 1:1 ou n:n.

### Partage de données{ #data-sharing } 

Il existe trois scénarios de partage, (1) un simple [*exportation de données*](https://docs.dhis2.org/master/en/user/html/dhis2_user_manual_en_full.html#export),
(2) [*DHIS2 et (3) les applications ou sites web externes qui se connectent à l'application 
DHIS Web
API*](https://docs.dhis2.org/master/en/developer/html/dhis2_developer_manual_full.html). 
Comme pour les fonctions d'importation décrites dans la section sur la saisie des données, 
la manière la plus accessible de partager les données est d'utiliser les fonctions d'exportation 
de données disponibles dans le menu utilisateur, ce qui ne nécessite que peu 
de connaissances techniques.

Grâce à sa conception modulaire, le DHIS2 peut être complété par **des modules logiciels
supplémentaires, qui peuvent être téléchargés à partir du DHIS2**[*App 
store*] (https://www.dhis2.org/appstore). Ces modules logiciels peuvent 
coexister avec les modules de base du DHIS2 et être intégrés dans 
le portail et le système de menus du DHIS2. Il s'agit d'une caractéristique importante, car elle 
permet d'étendre le système avec des fonctionnalités supplémentaires en cas de besoin, 
généralement pour répondre aux exigences spécifiques d'un pays, comme cela a été souligné précédemment.

L'inconvénient de l'extensibilité du module logiciel est qu'elle impose
plusieurs contraintes au processus de développement. Les développeurs qui créent
les fonctionnalités supplémentaires sont limités à la technologie DHIS2 en termes de
langage de programmation et de cadres logiciels, en plus des
contraintes imposées à la conception des modules par la solution de portail DHIS2.
En outre, ces modules doivent être inclus dans le logiciel DHIS2 lorsque le
logiciel est construit et déployé sur le serveur web, et non de manière dynamique pendant
l'exécution.

Afin de surmonter ces limitations et de parvenir à un couplage plus souple
entre la couche de service DHIS2 et les artefacts logiciels supplémentaires, 
l'équipe de développement du DHIS2 a décidé de créer une **API Web**. Cette API Web
est conforme aux règles du style architectural REST. Cela suppose
que :

  - L'API Web fournit une interface navigable et lisible par machine pour 
    le modèle de données complet du DHIS2. Par exemple, on peut accéder à la liste complète 
    des éléments de données, puis naviguer à l'aide de l'hyperlien fourni vers
    un élément de données particulier qui nous intéresse, puis naviguer à l'aide de
    l'hyperlien fourni vers la liste des formulaires dont cet élément de données fait 
    Par exemple, les clients n'effectueront des transitions d'état qu'en utilisant les
    hyperliens qui sont intégrés dynamiquement dans les réponses.

  - L'accès aux données s'effectue par le biais d'une interface uniforme (URL) utilisant un
     protocole bien connu. Il n'y a pas de formats ou de protocoles de transport fantaisistes,
    mais simplement le protocole HTTP, qui a été testé et qui est bien compris,
    et qui est le principal élément constitutif du Web aujourd'hui. Cela 
    signifie que les développeurs tiers peuvent mettre au point des logiciels utilisant le
     modèle de données et les données DHIS2 sans connaître la technologie spécifique de DHIS2
    ou se conformer aux contraintes de conception de DHIS2.

  - Toutes les données, y compris les métadonnées, les rapports, les cartes et les graphiques, appelés 
    ressources dans la terminologie REST, peuvent être récupérées dans la plupart des
    formats de représentation populaires du web d'aujourd'hui, tels que HTML,
    XML, JSON, PDF et PNG. Ces formats sont largement pris en charge par
    les applications et les langages de programmation et offrent aux développeurs tiers
    un vaste champ d'options de mise en œuvre.

Cette API Web peut être accessible par différents systèmes d'informations externes. 
Les efforts nécessaires pour développer de nouveaux systèmes d'informations et les maintenir 
à long terme sont souvent largement sous-estimés. Au lieu de partir de 
zéro, une nouvelle application peut être construite sur la base de l'API Web.

Les systèmes externes peuvent offrir différentes options de visualisation et 
de présentation des données DHIS2, par exemple sous forme de tableaux de bord, de composants SIG et de composants 
graphiques. Les portails Web destinés au domaine de la santé peuvent utiliser le système DHIS2 comme 
principale source de données agrégées. Le portail peut se connecter à l'API Web 
et communiquer avec des ressources pertinentes telles que des cartes, des graphiques, 
des rapports, des tableaux et des documents statiques. Ces vues de données peuvent visualiser dynamiquement 
des données agrégées basées sur des requêtes sur la dimension unité organisationnelle, 
indicateur ou période. Le portail peut apporter une valeur ajoutée à 
l'accessibilité des informations de plusieurs manières. Il peut être structuré 
de manière conviviale et rendre les données accessibles aux utilisateurs inexpérimentés. 
Le [portail Web Tanzania 
HMIS](https://appstore.hisptanzania.org/) en est un exemple.

## Modèle de maturité du DHIS2 { #dhis2-maturity-model } 

En tenant compte de tous les éléments ci-dessus sur l'architecture du système et 
les types de données, les responsables de la mise en œuvre de DHIS2 peuvent aborder 
les mises en œuvre de plusieurs manières :

  - Se concentrer sur les données transactionnelles ou agrégées

  - Se concentrer sur l'intégration des données ou l'interopérabilité des systèmes

Compte tenu des efforts requis pour mettre en œuvre l'interopérabilité des systèmes, de 
nombreux ministères de la santé optent pour le raccourci pragmatique consistant à intégrer 
des données telles que les données de base sur les stocks **directement dans leur système 
DHIS2 national existant**. En tant que plateforme à évolution rapide, DHIS2 a ajouté de 
nombreuses fonctionnalités au cours des dernières années, en particulier dans DHIS2 Tracker. 
Si l'on prend l'exemple des données logistiques, les principales fonctions suivantes sont 
actuellement disponibles :

  - Le formulaire de saisie des données reflète le formulaire papier largement utilisé pour les rapports et les demandes
    (R\&R). La saisie des données par les établissements est possible via 
    un navigateur de bureau ou une application mobile, également en mode hors ligne. Ces
    formulaires électroniques peuvent être remplis par le personnel sur la base des fiches de stock papier,
    qui sont normalement placées à côté des produits dans la 
    salle de stockage.

  - DHIS2 peut ensuite produire des rapports pour le
    suivi des performances au niveau central, permettant aux gestionnaires de produits et de programmes de comprendre 
    le fonctionnement du système logistique. Selon le mode de
    fonctionnement du système logistique, ces données peuvent également soutenir 
    la prise de décision opérationnelle, bien qu'une analyse plus complète
    des processus opérationnels logistiques et des utilisateurs devrait d'abord être effectuée.

  - Les données relatives aux stocks peuvent être transformées en indicateurs logistiques, qui peuvent
    être mis en contexte avec d'autres indicateurs du programme, par exemple
    en croisant le nombre de patients traités pour une pathologie spécifique 
    et la consommation de médicaments correspondante.

Bien que chaque pays étudié dans les cas d'utilisation ait sa propre voie 
de développement vers l'intégration des systèmes, certains enseignements communs peuvent 
être tirés de leurs expériences. Le modèle de maturité ci-dessous décrit une 
approche évolutive pour faire face aux défis de l'intégration et de l'interopérabilité, 
permettant aux différents acteurs d'un système de santé national 
d'acquérir des habitudes professionnelles en matière d'analyse et d'utilisation des données.

Le modèle de maturité suggère de passer des données agrégées aux données transactionnelles 
et des systèmes autonomes aux systèmes interopérables (en utilisant l'exemple des 
données logistiques).

1.  Le DHIS2 est souvent l'un des premiers systèmes à couvrir l'administration de la santé
    et plusieurs niveaux d'établissements d'un pays. Dans un premier temps,
    des indicateurs de base sur les maladies sont couverts (correspondant par exemple aux
    100 Indicateurs de Santé de Base de l'OMS).

2.  Dans une seconde phase, les différentes parties prenantes cherchent à compléter les 
    données relatives aux maladies et à la prestation de services qu'elles communiquent avec les données de base du LMIS.
    Cela peut se faire sur une base agrégée dans le DHIS2, par exemple en
    incluant les niveaux de stock et la consommation dans les rapports périodiques. Cela
    fournira des informations de haut niveau sur la performance  du système logistique,
    mais pourra ou non fournir des informations suffisantes pour soutenir l'amélioration 
    des opérations du système logistique.

3.  À un stade plus avancé, il peut y avoir un besoin légitime de 
    systèmes logistiques spécialisés, en particulier lorsqu'une vue transactionnelle très détaillée
    est souhaitée pour avoir un contrôle plus granulaire (par exemple,
    les retours, les transferts entre installations, les numéros de lots et les dates d'expiration,
    etc.). DHIS2 Tracker peut offrir certaines fonctions de gestion des données relatives 
    aux événements ou aux patients, mais ne peut pas toujours atteindre le degré de 
    soutien au flux de travail fourni par d'autres solutions plus spécialisées.

4.  Dans un environnement technologique et managérial mature, les transactions logistiques
    peuvent être partagées avec le DHIS2 sous une forme agrégée, passant
    ainsi d'un scénario autonome à un scénario intégré.

## Étapes de mise en œuvre pour une intégration réussie des données et des systèmes{ #implementation-steps-for-successful-data-and-system-integration } 

L'objectif de ce guide de mise en œuvre du DHIS2, étape par étape, est de 
fournir aux implémenteurs une méthodologie pour créer et soutenir un scénario 
d'intégration du DHIS2. Le guide est basé sur les meilleures pratiques et 
les leçons apprises. Il préconise une approche itérative, 
agile et axée sur le pays, qui commence par la collecte de témoignages d'utilisateurs 
et d'exigences fonctionnelles. Le guide est conçu comme un cadre qui peut 
être adapté au contexte spécifique de chaque pays. Le contenu 
décrit des exemples spécifiques pour chaque étape, détaillant les témoignages des utilisateurs, 
les spécifications des données, les outils de travail et les listes de contrôle pour guider l'utilisation du 
logiciel de mise en œuvre de référence. La structure de base, y compris les 6 
étapes, est basée sur la [méthodologie de mise en œuvre de l'OpenHIE] 
(https://wiki.ohie.org/display/documents/OpenHIE+Planning+and+Implementation+Guides) :

**Étape 1** : Identifier les partenaires et les facteurs de motivation pour l'amélioration des 
données des établissements

**Étape 2** : Documenter les spécifications du registre des établissements et les témoignages des utilisateurs

**Étape 3** : Configurer l'instance initiale

**Étape 4** : Identifier les lacunes et le développement itératif via les tests utilisateurs

**Étape 5** : Étendre la mise en œuvre du registre

**Étape 6** : Apporter un soutien continu

Outre ces étapes liées à l'interopérabilité, il convient également 
de se reporter à certaines expériences générales en matière de mise en œuvre du système DHIS2 
et aux meilleures pratiques présentées dans les sections concernées dans 
les documents [Recommandations pour la mise en œuvre d'une solution HIS 
au niveau national](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e86) et [Configuration d'une nouvelle base
de données](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e250). 
également vitale pour les projets d'interopérabilité, l'approche **participative** est 
couramment utilisée pour mettre en œuvre un système DHIS2. Cette approche 
met l'accent sur l'inclusion, dès le début du projet, d'[une équipe 
locale](https://docs.dhis2.org/master/en/implementer/html/dhis2_implementation_guide_full.html#d0e255) 
ayant des compétences et des antécédents différents, afin que ses membres puissent entrer en fonction dès que 
possible.

### Étape 1 : Définition de la stratégie, des parties prenantes et des objectifs en matière d'utilisation des données{ #step-1-define-strategy-stakeholders-and-data-usage-objectives } 

Dans un premier temps, les objectifs du projet d'intégration seront 
définis. Comme pour tout projet technologique, il doit y avoir un
**consensus clair sur les objectifs stratégiques et fonctionnels**. L'innovation 
technologique et la faisabilité ne doivent pas être les seules forces motrices, mais 
plutôt un objectif organisationnel clairement défini. C'est pourquoi cette étape 
vise également à répondre à la question suivante : "Pourquoi voulons-nous connecter des systèmes 
ou intégrer des données provenant de différentes sources avec DHIS2 ?"

D'un point de vue pratique, cela conduit à des questions sur l'approche de l'intégration des données.
telles que :

  - Souhaitez-vous éliminer les formulaires papier ou même les ensembles de données
    redondants ou inutiles ?

  - Pouvez-vous intégrer les données (agrégées) dans le système DHIS2 ?

  - Pouvez-vous intégrer les données détaillées (par exemple au niveau du patient ou au niveau transactionnel)
    dans DHIS2, en utilisant les fonctions de suivi de DHIS2 ?

  - Si vous souhaitez créer une connexion d'échange de données entre DHIS2 et
    un autre système, comment définissez-vous la propriété et les responsabilités ?

Les activités visant à répondre à cette question sont décrites ci-dessous et poseront 
les bases d'un projet d'interopérabilité du DHIS2.

#### Identification des parties prenantes et de leurs motivations{ #identify-stakeholders-and-motivations } 

La nature des projets d'interopérabilité veut qu'il y ait plus d'une 
partie prenante. Les parties prenantes de différents domaines doivent se mettre d'accord sur une approche commune 
du système, par exemple l'équipe responsable du HMIS national 
(par exemple le département S&E ou le département de la planification) et le département de la logistique 
dans le cas de la mise en œuvre d'un LMIS (système de gestion et d'information logistiques). Ces deux domaines principaux ont souvent 
des sous-divisions, par exemple, dans le domaine de la logistique, l'unité d'approvisionnement, 
l'unité d'entreposage, l'unité de transport. En outre, les parties prenantes des programmes spécifiques aux maladies 
auront leurs propres régimes et gestionnaires de 
produits. Outre ces acteurs locaux, les partenaires internationaux 
(agences, donateurs, ONG internationales, cabinets de conseil) sont souvent impliqués 
dans le processus de prise de décision.

Il est donc judicieux de se pencher sur les principales motivations des 
parties prenantes et sur la manière d'atténuer les risques résultant 
d'intérêts potentiellement divergents.

  - Les départements centraux du ministère de la santé, tels que **M\&E&**Planning, sont souvent les principaux
    acteurs de la normalisation des indicateurs et des systèmes informatiques

  - **Les services informatiques centraux** s'intéressent de manière générale aux choix
    et à la propriété des technologies (souvent contrôlés au niveau local), ainsi 
    qu'à l'achat de matériel et de logiciels. Ils s'occupent souvent des questions de réseau et de matériel,
    mais manquent d'expérience en ce qui concerne les architectures et les échanges de données complexes
    basés sur le web.

  - **Les programmes de lutte contre les maladies spécialisées** sont souvent soumis à des pressions pour obtenir
    des indicateurs très spécifiques, à la fois pour leur propre gestion et pour répondre aux 
    approches des donateurs. Ils peuvent également se sentir plus
    à l'aise pour contrôler leur propre système informatique afin de s'assurer que leurs
    besoins sont prioritaires.

  - **Les domaines fonctionnels spécialisés** (tels que les ressources humaines,
    la logistique, la gestion des hôpitaux) sont souvent dans une position en sandwich, 
    devant répondre aux besoins d'information de plusieurs parties prenantes différentes,
    tout en essayant d'atteindre l'efficacité opérationnelle avec
    des ressources limitées.

En identifiant les personnes intéressées par la fourniture ou l'utilisation des données, les 
responsables de la mise en œuvre peuvent commencer à former une équipe de projet pour orienter 
les travaux de conception et de mise en œuvre. Une méthode pour caractériser les parties prenantes consiste 
à regrouper les parties intéressées selon leurs rôles fonctionnels. L'infrastructure et les procédures existantes 
sont également importantes pour comprendre les 
options de gouvernance et de conservation. Comprendre les parties prenantes et 
leurs systèmes correspondants est une première étape cruciale.

#### Inventaire du système de cybersanté{ #ehealth-system-inventory } 

Il est important d'avoir une vision claire du contexte global des systèmes informatiques. 
Cela permet de s'assurer que les investissements dans l'interopérabilité sont réalisés pour 
renforcer les principaux systèmes et qu'ils contribuent à une 
**simplification** de l'architecture du système. Par exemple, si 
l'inventaire des systèmes montre qu'il y a beaucoup de systèmes fonctionnels redondants, 
par exemple plus de 10 systèmes ou modules logistiques différents dans un 
pays, le projet d'interopérabilité devrait essayer de contribuer à une 
rationalisation à moyen ou long terme de cette situation. Il pourrait s'agir de 
participer à un processus national de recherche de consensus afin d'identifier les solutions 
les plus sûres pour l'avenir, de désigner des "champions" nationaux pour chaque 
spécialité et d'élaborer une feuille de route pour l'alignement de ces systèmes ou données et 
la suppression des systèmes sous-utilisés ou redondants.

Dans ce contexte, il est également intéressant d'analyser si des 
indicateurs simples peuvent être collectés et gérés dans le DHIS2 lui-même et comment cela peut 
compléter les efforts d'amélioration du système logistique (comme cela est expliqué plus loin 
dans un [exemple de SIMT](#lm)). Une fois que les systèmes stables et durables 
ont été identifiés, la planification d'un échange de données avec le DHIS2 
peut commencer.

#### Exploration des opportunités et des défis { #explore-opportunities-and-challenges } 

Les motivations qui président à la mise en œuvre peuvent être détaillées en fonction 
des opportunités ou des défis perçus par les parties prenantes. Il peut s'agir 
du désir de partager des données entre les systèmes liés aux établissements de santé 
pour la gestion de la chaîne d'approvisionnement, le suivi et l'évaluation, 
la prestation de services de santé et bien d'autres systèmes. Les témoignages des utilisateurs et les cas d'utilisation 
seront documentés en profondeur au cours de l'étape 2, mais il est également nécessaire d'avoir une vision de haut niveau 
des motivations qui poussent à s'engager avec les partenaires.

#### Organisation et RH { #organisation-and-hr } 

Des politiques nationales claires sur l'intégration des données, la propriété des données, les routines 
de collecte, de traitement et de partage des données doivent être mises en place dès le 
début du projet. L'intégration perturbe souvent le flux normal 
des données pendant un certain temps, ce qui fait que, pour beaucoup, les perspectives à long terme 
d'un système plus efficace doivent être évaluées à leur juste valeur par rapport à la 
perturbation à court terme. L'intégration est donc souvent un processus par étapes, 
où des mesures doivent être prises afin qu'elle se déroule le plus harmonieusement possible.


> **Exemple**
>
> **CHIM du Ghana**
>
> - **Coopération des parties prenantes** : Le *Centre de gestion de l'information sur la santé* (Centre for Health Information Management ou CHIM) du Ghana a une position claire à l'égard des programmes verticaux et d'autres partenaires dotés d'initiatives logicielles appropriées. Pour le CHIM, le système DHIS2 constitue une option de collecte de données attrayante, qui aide les autres parties prenantes du GHS à se connecter à DHIS2 et à travailler sur une stratégie d'interopérabilité commune, faisant ainsi évoluer le système DHIS2 en fonction des besoins des parties prenantes. **Cela inclut également les accords d'échange de données**.
> - **Sentiment fort d'appropriation du système** : Le CHIM est fortement déterminé à développer le savoir-faire nécessaire au sein de l'équipe du CHIM pour configurer et entretenir le système. L'équipe du CHIM est composée d'agents d'informations sanitaires, ayant des compétences en santé publique et en gestion des données.

De même, le fait de disposer de **procédures de maintenance et de mise à jour 
du système** clairement définies peut certainement aider à gérer l'interopérabilité.


> **Exemple**
>
> **CHIM du Ghana** 
> À titre d'exemple, dans le cas du système DHIS2 au Ghana, un cycle annuel clair de mise à jour du système est en place : Vers la fin de chaque année, de nouveaux indicateurs sont créés et les formulaires papier correspondants sont émis. Le personnel reçoit une formation et se prépare à saisir des données. Le nouveau formulaire pour les données du PEV a été inclus dans ce cycle de mise à jour et le personnel du PEV est prêt à saisir les données dans le cadre de ce processus. Cette procédure systématique permet au GHS de répondre rapidement aux besoins des parties prenantes telles que le programme PEV et de satisfaire leurs besoins en matière de données et de rapports avec un investissement limité et prévisible. Elle met le CHIM en position de contribuer à la rationalisation et à la simplification de l'architecture du système de santé national, en intégrant progressivement la gestion des données pour des programmes plus **verticaux**, tant du côté de la saisie que de l'analyse des données.

Un principe clé de HISP est d'impliquer l'équipe locale dans la construction du 
système dès le début, avec l'aide d'experts externes si 
nécessaire, et de ne pas retarder le transfert de connaissances vers la fin de la 
mise en œuvre. L'appropriation passe avant tout par la construction du système 
et la maîtrise de chaque étape du processus.

### Étape 2 : Documenter les spécifications et les exigences{ #step-2-document-specifications-and-requirements } 

  - Collecter les métadonnées existantes

  - Documenter les spécifications des données

  - Recueillir les témoignages des utilisateurs

### Étape 3 : Mener à bien les spécifications et identifier les lacunes { #step-3-carry-out-specifications-and-identify-gaps } 

  - Mettre en œuvre les spécifications

  - Identifier et prioriser les témoignages des utilisateurs incomplets

### Étape 4 : Itération et Test de l'Utilisateur{ #step-4-iteration-and-user-testing } 

  - Développement agile et itératif

  - Test utilisateur

  - Collecter, rapprocher et télécharger les données

### Étape 5 : Mise à l'échelle { #step-5-scale-up } 

  - Confirmer les rôles et responsabilités des utilisateurs

  - Former les utilisateurs

  - Intégrations critiques

### Étape 6 : Soutien continu{ #title_nxr_lxp_41b } 

Si, pendant la phase de mise en œuvre, une structure de soutien temporaire 
doit être disponible, une structure de soutien permanente doit être 
mise en place par la suite. Le principal défi consiste à définir clairement les responsabilités. Dans une 
situation idéale, nous avons affaire à deux systèmes stables qui ont déjà chacun 
leur propre structure de soutien clairement définie.

Cependant, dans la réalité, certains défis récurrents doivent être relevés: 
de nombreux systèmes de santé publique connaissent des évolutions dynamiques, entraînant 
des changements dans les besoins de collecte de données ou le calcul des indicateurs.

L'interopérabilité tend à être une charge technique et organisationnelle 
fastidieuse. Les trois initiatives décrites ont consommé un 
effort considérable de **ressources** qualifiées pour activer les API. En 
outre, à chaque nouvelle version d'un système impliqué, les flux de données 
doivent être testés à nouveau et, si nécessaire, adaptés. Pour réussir, ces 
projets de mise en œuvre doivent généralement passer par une série d'étapes complexes,
telles que l'accord sur une approche de l'interopérabilité intégrée dans 
la stratégie nationale de cybersanté, la définition de normes de données et 
d'une structure de maintenance durable, et l'obtention d'un consensus entre les parties 
prenantes sur la propriété des données et les politiques de partage. L'interconnexion des données et des systèmes peut avoir des conséquences à long terme: 
elle crée **de nouveaux rôles, tâches et catégories de travail** qu'il convient de prévoir 
(gouvernance des métadonnées, administration de systèmes complexes, 
négociateurs de frontières, etc.) Une solution pourrait consister à discuter au préalable des nouvelles 
responsabilités, en les attribuant à des descriptions de poste, à des équipes 
et à des postes spécifiques.

#### Responsabilité des métadonnées { #metadata-responsibility } 

Un autre domaine important est celui de la **gouvernance des métadonnées**, en particulier 
dans les scénarios d'utilisation secondaire des données. Dans une configuration autonome,
les métadonnées, telles que les codes d'installation ou de produit, peuvent être gérées sans
grande considération pour les besoins des autres parties prenantes. Mais dans un 
environnement d'interopérabilité, les changements de métadonnées auront des effets en dehors 
du système individuel. La gouvernance des métadonnées peut être très formalisée 
grâce à des registres ou plus manuelle grâce à des processus humains.

Afin de déterminer l'approche appropriée, il est utile d'estimer 
*l'effort de maintenance des métadonnées* prévu et les conséquences de 
métadonnées non synchronisées entre différents systèmes. Dans le cas des 
intégrations LMIS/DHIS2, il existe potentiellement des milliers d'identifiants d'installations 
qui pourraient être désynchronisés. Cependant, les identifiants des établissements 
ne changent normalement pas souvent, car l'infrastructure physique de 
la plupart des systèmes de santé publique est relativement constante. En ce qui concerne les produits, 
bien que les régimes et les médicaments prioritaires puissent changer au fil du temps, le nombre d'ensembles 
de données est relativement restreint : la liste des produits d'un programme 
contient souvent moins de 20 produits. Par conséquent, il peut être souvent pratique de 
mettre à jour un produit manuellement et de ne pas investir dans des solutions d'interopérabilité 
telles qu'une synchronisation automatisée des métadonnées.

## Cas d'utilisation spécifiques d'intégration et d'interopérabilité{ #specific-integration-and-interoperability-use-cases } 

DHIS2 a étendu son champ d'action à de nombreux systèmes de santé. Partant 
de la base familière des ensembles de données agrégées pour les données de routine, il a 
inclus des données relatives aux patients, puis des données dans les domaines des ressources humaines, des finances, 
de la logistique et de la gestion des laboratoires. Cette évolution est conforme au 
développement du DHIS2 dans de nombreux pays, où les implémenteurs 
poussent l'utilisation au-delà de son champ d'application initial.

Cela se reflète également dans l'architecture globale du système. Étant donné que 
l'extension des fonctionnalités du DHIS2 réduit l'urgence d'introduire ou 
de maintenir d'autres systèmes spécialisés, le nombre d'interfaces de données potentielles 
diminue. Cette **réduction de la complexité** de l'architecture du système 
est certainement un avantage pour un Système de Santé dont les ressources sont limitées.

Depuis plusieurs années, DHIS2 a développé ses activités de gestion de données 
de manière organique, permettant à l'utilisation effective de déboucher sur des solutions
parfois imprévues. Cependant, il y a aussi des limites aux domaines dans lesquels l'utilisation de DHIS2 
semble utile. Dans les sections suivantes, des systèmes spéciaux seront 
décrits.

### Gestion de la logistique { #lm } 

**a) Introduction**

Les systèmes de gestion logistique **(LMIS)** ou les systèmes de gestion de la chaîne
d'approvisionnement **(SCM)** servent à remplacer les systèmes sur support papier afin d'accroître 
la normalisation, la transparence, la rapidité de l'approvisionnement, l'efficacité, 
la sécurité, la rentabilité et de réduire les déchets. Les SCMS/LMIS nationaux peuvent
couvrir des fonctions telles que la planification des produits, la budgétisation, l'approvisionnement, 
le stockage, la distribution et le réapprovisionnement des médicaments essentiels et 
des consommables.

**b) Mise en œuvre du LMIS dans le système DHIS2**

Les chaînes d'approvisionnement peuvent souvent être bien contrôlées à l'aide de données agrégées uniquement, à 
condition que les données soient fournies de manière fiable par tous les niveaux concernés et qu'elles fassent l'objet d'un suivi. 
Les principaux indicateurs que sont l'apport, la consommation et le niveau des stocks en 
fin de période peuvent être gérés sans transactions électroniques et suffisent souvent 
à donner une vue d'ensemble, ce qui réduit les besoins d'investissement dans le système. 
En tant que plateforme évoluant très rapidement, DHIS2 a ajouté de nombreuses 
fonctionnalités au cours des dernières années, en particulier dans DHIS2 Tracker. Les 
principales fonctions suivantes sont actuellement disponibles :

  - Le formulaire de saisie des données reflète le formulaire papier largement utilisé pour les rapports et les demandes
    (R\&R). La saisie des données par les établissements est possible via 
    le navigateur de bureau ou une application mobile, y compris en mode hors ligne. En 
    mode en ligne, le formulaire peut calculer les propositions de réquisition, offrant 
    au gestionnaire de l'établissement la possibilité de modifier la demande et de la commenter. Ces 
    formulaires électroniques peuvent être remplis par le personnel sur la base des fiches de stock papier,
    qui sont normalement placées à côté des produits dans la 
    salle de stockage.

  - DHIS2 peut alors produire des rapports pour la prise de décision centrale, donnant
    aux gestionnaires de produits et de programmes la possibilité d'accepter ou de modifier
    les suggestions de livraison.

  - Les données relatives aux stocks peuvent être transformées en indicateurs logistiques, qui peuvent
    être mis en contexte avec d'autres indicateurs du programme, par exemple
    en croisant le nombre de patients traités pour une pathologie spécifique 
    et la consommation de médicaments correspondante.

**c) Options d'interopérabilité**

Le LMIS est un domaine où une multitude de solutions logicielles parallèles, qui se chevauchent ou qui se font concurrence, 
peuvent être trouvées dans un seul pays. Comme l'a montré une étude 
JSI réalisée en 2012 ( Ministère de la santé du Ghana, juillet 2013 : Analyse du panorama 
des outils de gestion de la chaîne d'approvisionnement utilisés), dix-huit (18\!) 
outils logiciels différents ont été documentés comme étant utilisés dans la 
chaîne d'approvisionnement de la santé publique uniquement au Ghana.

Bien qu'une configuration de base du LMIS basée sur des données agrégées puisse vous mener 
très loin, dans certains cas, un LMIS transactionnel est nécessaire si vous devez 
suivre des opérations aussi détaillées que les retours, les transferts entre établissements, 
la lecture des codes-barres, la gestion des lots et des dates d'expiration. De même, certaines fonctions spécialisées du siège, 
telles que la création de rapports de prévision, de réapprovisionnement et de contrôle élaborés, 
sont souvent réalisées à l'aide d'outils spécialisés.

Le DHIS2 a intégré des données agrégées provenant de systèmes externes tels que
openLMIS et CommCare par le biais d'interfaces de données automatisées. En conséquence, 
les données sur les stocks sont disponibles dans des tableaux de bord partagés, qui affichent les services de santé 
et stock les données les unes à côté des autres.

