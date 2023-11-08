---
edit_url: "https://github.com/dhis2/dhis2-docs-implementation/blob/master/content/chis_implementation/05_data_use.md"
revision_date: '2022-04-20'
tags:
- Implémentation
---

# Qualité et Utilisation des données  { #data-quality-and-use } 

L'objectif principal d'un CHIS est de générer des informations qui peuvent être utilisées par les ASC et autres parties prenantes à différents niveaux pour améliorer et renforcer les programmes de santé communautaire, le but étant d'améliorer la santé des populations.

Malgré l'importance primordiale de permettre l'utilisation des données, ce domaine est à la traîne dans les efforts de renforcement du CHIS, à un moment où l'attention porte de plus en plus sur l'utilisation des nouvelles technologies et appareils permettant d'automatiser la collecte et la transmission des données. Ce module vise donc à comprendre ce que nous entendons par utilisation des données, quels sont ses principaux déterminants, et comment elle peut être renforcée globalement.


## Le Cycle Vertueux de l'Utilisation des Données et de la Qualité des Données  { #the-virtuous-cycle-of-data-use-and-data-quality } 

Le "cercle vicieux des données" est un scénario dans lequel les ASC et les autres parties prenantes estiment que le CHIS fournit des données de mauvaise qualité, de sorte qu'ils ne font pas confiance au système et donc ne l'utilisent pas. Ils utilisent leurs propres sources, des enquêtes externes ou, pire encore, créent de nouveaux systèmes (aggravant la fragmentation) pour répondre à leurs besoins d'information. S'ils n'utilisent pas de données, le CHIS sera davantage négligé, produira des données de moins bonne qualité, et sera encore moins utilisé.

Heureusement, l'inverse est également valable, comme le montre le "cycle vertueux des données". Plus la qualité des données est fiable, plus elles sont utilisées, ce qui améliore encore leur qualité. Comme le montrent les boucles de retour d'information du diagramme, il s'agit d'un processus continu et progressif qui prend du temps et doit être stimulé par une demande croissante de données, une appropriation locale des données et des liens visibles entre les données et la prise de décision. Le résultat final de ce cercle vertueux est que l'utilisation des informations soit dynamique et devienne une habitude

Ce lien entre la qualité et l'utilisation des données suppose que les développeurs du CHIS s'attaquent au problème de la mauvaise utilisation des données tant du côté de la demande que de l'offre, et qu'ils renforcent leurs interactions. Du côté de la demande, il s'agit de renforcer la sensibilisation et les capacités des parties prenantes à utiliser les données pour améliorer la gestion de la santé communautaire, tandis que du côté de l'offre, il s'agit d'améliorer la qualité générale des données générées par le CHIS. Nous considérons le DHIS2 comme un outil capable de contribuer au renforcement de ces deux objectifs et de leurs interactions. Mais tout d'abord, nous discuterons de ce que nous entendons par qualité des données et de la manière dont les outils du DHIS2 peuvent contribuer à renforcer cette qualité.

![](resources/images/chis_figure12.png)


## Renforcement de l'Offre : Éléments Clés de la Qualité des Données{ #strengthening-supply-side-essential-elements-of-data-quality } 

Les données de bonne qualité sont celles que les décideurs considèrent comme fiables et sur lesquelles ils peuvent fonder leurs décisions. Les caractéristiques des données de bonne qualité sont les suivantes : L'exactitude, la complétude, la pertinence et la cohérence.

**Exactitude (précision)**
*Les données reflètent-elles  fidèlement la réalité qu'elles cherchent à mesurer?*

- Les données reflètent-elles la situation réelle de la communauté ?
- Y a-t-il des erreurs dans la saisie des données ?
 - Les valeurs exactes sont-elles enregistrées aux bons emplacements ?
 - S'il y a des erreurs, sont-elles systématiques (par exemple, dues à une mauvaise compréhension de l'indicateur), accidentelles (c'est-à-dire aléatoires) ou intentionnelles ?
- Des erreurs de calcul sont-elles commises ?


**Complétude** 
*Tous les ASC font-ils des rapports sur tous les éléments de données qu'ils sont censés rapporter?*

- Toutes les unités font-elles des rapports ?
- Les ASC transmettent-ils tous les formulaires attendus ?
- Dans chaque rapport, les éléments de données requis sont-ils tous mentionnés ?
- Quel est le pourcentage de rapports "zéro" (c'est-à-dire que pour les cellules sans prestation de service, c'est un zéro qui est inscrit et non une case vide) ?

**Actualité (Promptitude)**
*Les données sont-elles communiquées en temps voulu, conformément aux normes établies?*

- Les établissements font-ils leurs rapports avant la date limite fixée par le ministère de la Santé ?
- Les périodes de rapports sont-elles normalisées dans tout le pays (c'est-à-dire que la période de rapport commence et se termine aux mêmes dates dans tous les établissements et districts) ?

**Cohérence**
*Les modèles de données rapportés sont-ils cohérents et ne comportent-ils pas de valeurs aberrantes?*

- La comparaison avec les mois précédents révèle-t-elle une tendance constante (par exemple, une répartition similaire des cas de maladies ou une proportionnalité âge/genre) ?
- Arrive-t-il que des ASC rapportent des valeurs incohérentes (c'est-à-dire des valeurs atypiques) ?

## Outils de Qualité des Données dans le DHIS2 { #data-quality-tools-in-dhis2 } 

Outre l'utilisation des données, plusieurs outils de qualité des données sont intégrés au DHIS2 :

**Validation des données saisies:** Le contrôle de qualité des données le plus basique dans le DHIS2 consiste à s'assurer que les données saisies sont au bon format. Le DHIS2 envoie à l'utilisateur un message indiquant que la valeur saisie n'est pas au bon format et que l'enregistrement ne sera possible que si elle est remplacée par une valeur acceptable. Par exemple, vous ne pouvez pas saisir de texte dans un champ numérique. Les différents types de valeurs de données prises en charge dans le DHIS2 sont expliqués dans le manuel de l'utilisateur, au chapitre consacré aux éléments de données.

**Valeurs minimales et maximales:** Pour éviter les erreurs de frappe lors de la saisie des données (par exemple, saisir "1000" au lieu de "100"), le DHIS2 vérifie que la valeur saisie se situe dans une fourchette raisonnable. Cette fourchette est basée sur les données précédemment collectées par le même établissement de santé pour le même élément de données, et se compose d'une valeur minimale et d'une valeur maximale. Dès que l'utilisateur saisit une valeur en dehors de cette fourchette, il reçoit une alerte selon laquelle cette valeur n'est pas acceptée. Pour déterminer les fourchettes raisonnables, le système a besoin d'au moins six mois (périodes) de données.

**Règles de validation:** Une règle de validation définit une relation entre un certain nombre d'éléments de données. L'expression définit une condition qui doit indiquer si certains critères logiques sont remplis. Par exemple, une règle de validation pourrait indiquer si le nombre total de vaccins administrés aux nourrissons est inférieur ou égal au nombre total de nourrissons.

Les règles de validation peuvent être définies via l'interface utilisateur et exécutées ultérieurement pour vérifier les données existantes. Lors de l'exécution des règles de validation, l'utilisateur peut spécifier les unités d'organisation et les périodes pour lesquelles les données doivent être vérifiées. Lorsque les contrôles sont terminés, un rapport est présenté à l'utilisateur avec les violations de validation indiquant les valeurs de données qui doivent être corrigées.

Les contrôles des règles de validation sont également intégrés dans le processus de saisie de données. De cette manière, lorsque l'utilisateur finit de remplir un formulaire, les règles peuvent être exécutées pour vérifier uniquement les données de ce formulaire, avant la fermeture de ce dernier.

**Application DQA et d'analyse des valeurs atypiques de l'OMS : ** L'application DQA de l'OMS est disponible dans le DHIS2.27 et dans les versions plus récentes. Cet outil très performant permet d'analyser la cohérence des données dans le temps et d'identifier les valeurs atypiques. L'analyse des valeurs atypiques basée sur l'écart-type permet de révéler les valeurs numériquement éloignées des autres données. Les valeurs atypiques peuvent résulter du hasard, mais elles témoignent souvent d'une erreur de mesure ou d'une répartition incorrecte (ce qui produit des chiffres très élevés). Dans le premier cas, il est préférable de les écarter, tandis que dans le second, il convient d'être prudent dans l'utilisation des outils ou des interprétations qui reposent sur l'hypothèse d'une répartition normale. L'analyse est basée sur la répartition standard.

**Rapports sur la complétude et la promptitude :** Les rapports sur la complétude indiquent le nombre d'ensembles de données (formulaires) qui ont été soumis par unité d'organisation et par période. Il existe trois méthodes différentes pour déterminer la complétude :

1. Méthode utilisant la fonction complétude lors de la saisie des données.
2. Méthode utilisant un ensemble d'éléments de données obligatoires définis.
3. Méthode utilisant le nombre total de valeurs de données enregistrées pour un ensemble de données.

Le rapport sur la promptitude est basé sur un paramètre système appelé "Jours après la fin de la période pour soumettre les données à temps" et montre

- les unités d'organisation d'une zone qui communiquent à temps,
- le pourcentage des établissements d'une zone, qui communiquent à temps leurs données.


## Ressources Supplémentaires sur la Qualité des Données { #additional-data-quality-resources } 

*Retrouvez ces ressources dans les annexes de ce document.*

1. **Amélioration de la qualité des données de santé, des recommandations et des directives** "Ce rapport met l'accent sur les mesures à mettre en place pour améliorer la qualité des données. Les améliorations suggérées se basent sur les leçons tirées au Malawi, lesquels leçons sont également valables au-delà du cadre national."
2. **Manuel de l'outil de qualité du DHIS2**. Il s'agit d'un manuel d'utilisation de base de l'outil de qualité du DHIS2. Le manuel explique les fonctionnalités de l'outil, comme une contribution au renforcement des capacités et aux ateliers. L'outil de qualité des données ne se limite pas à l'affichage d'erreurs potentielles, mais l contribue également à une meilleure appréhension de la qualité des données.
3. **Directives relatives à la qualité des données du CBHIS mobile**. Il s'agit d'orientations générales et complètes sur les systèmes d'information sanitaire des communautés. On note 3 sections :
    - Conception de systèmes de collecte de données mobile pour une meilleure qualité des données. Ce volet comprend des directives sur la conception de systèmes de collecte de données mobile, ainsi qu'une liste de contrôle pour évaluer les formulaires et les mécanismes de collecte de données mobile d'un système.
    - Mise en œuvre de programmes visant à accroître l'appropriation et l'engagement en faveur de la qualité des données. Ce volet comprend des directives sur la responsabilisation et l'appropriation de la qualité des données, ainsi qu'une liste de contrôle permettant d'évaluer les boucles de retour d'information et de motiver les agents de santé en première ligne, sur les questions relatives à la qualité des données.
    - Vérification des données de terrain du CBHIS. Ce volet fournit des conseils sur la manière d'adapter un outil CVT (Community Trace and Verify) pour vérifier si les personnes déclarées comme bénéficiaires de services ont effectivement reçu ces services".
4. **Outil d'Audit de la Qualité des Données**. L'outil de DQA se concentre sur (1) la vérification de la qualité des données rapportées et (2) l'évaluation de la gestion des données sous-jacentes et des systèmes de rapport pour les indicateurs de résultats standard du programme. Deux versions de l'outil de DQA ont été développées :
    - l'"Outil d'Audit de la Qualité des Données": Il fournit des directives à utiliser par une équipe d'audit externe chargée d'évaluer la capacité d'un programme/projet à rapporter des données de qualité ; et
    - l'" Outil d'Evaluation de la Qualité des Données de Routine " (EQDR) est une version simplifiée de l'outil de AQD. Il permet aux programmes et aux projets d'évaluer la qualité de leurs données et de renforcer leurs systèmes de gestion des données et de rapports ".


## Renforcement de la demande: Comprendre les niveaux d'utilisation des données { #strengthening-demand-side-understanding-levels-of-data-use }

![](resources/images/chis_figure13.png)

Figure 3 : Triangle d'information montrant trois niveaux d'utilisation des informations

Comme le montre la figure 2, l'utilisation des données pour le CHIS s'effectue à trois niveaux qui fonctionnent en interaction.

### Niveau Client/Bénéficiaire { #clientbeneficiary-level }

L'individu qui bénéficie des services de santé d'un ASC est appelé client ou bénéficiaire, et devrait être le principal niveau d'action des ASC et des acteurs communautaires dans le cadre de la fourniture de soins préventifs, promotionnels, réhabilitatifs ou curatifs. Les bénéficiaires sont les femmes enceintes, les enfants de moins de cinq ans, les communautés qui implémentent les programmes de santé et les ménages souffrant de maladies chroniques infectieuses et non transmissibles. Les différents programmes du système de santé traitent souvent ces bénéficiaires séparément, en fonction des programmes de soins auxquels ils sont inscrits, ce qui a des répercussions sur le CHIS et limite la prise en compte générale des besoins en matière de soins et de bien-être.

L'un des objectifs du CHIS est de fournir un aperçu plus général des besoins des bénéficiaires ainsi que des différents services de santé dont ils bénéficient.

### Niveau Établissement { #facility-level } 

Le responsable de l'établissement utilise les données pour garantir des moyens adéquats aux activités de la communauté et pour assurer une supervision constructive. Les établissements sont le lien entre les communautés et le système de santé, et les responsables d'établissements sont les premiers interlocuteurs des ASC, lesquels bénéficient d'une supervision appropriée et de conseils sur la manière d'améliorer les soins de santé dispensés aux bénéficiaires.

Pour assurer ces fonctions et d'autres formes d'assistance, telles que la mise à disposition d'infrastructures, de personnel et d'équipements adéquats, les établissements ont besoin de données du CHIS qui sont fiables.

Les établissements sont également en première ligne pour promouvoir les "discussions sur les données", en fournissant des commentaires aux ASC et aux parties prenantes sur les prestations et sur d'autres activités afin de promouvoir le cycle vertueux des données. Les données du CHIS fournissent également aux établissements un tableau des ressources nécessaires et des "données manquantes" qui montrent le réel fardeau des maladies dans leur région, et permettent de s'assurer que les ASC fournissent les services nécessaires conformément au programme de services de santé de base. Les établissements doivent combiner les données du CHIS avec les données sur leurs propres services afin de dresser un aperçu de la santé de la population desservie, en vue d'une remontée des informations vers le district et les instances supérieures.

### Niveau Systèmes de Santé  { #health-systems-level } 

Les responsables des niveaux supérieurs (district et national) utilisent l'approche système pour renforcer les systèmes de gouvernance, de ressources humaines, de prestation de services, d'infrastructures, de finances et d'information des ASC. Les données proviennent de sources multiples, notamment le CHIS, le système d'information sanitaire de l'établissement, les systèmes spécifiques au programme, les recensements et les enquêtes sanitaires, et visent deux objectifs.

1. Élaborer des politiques et des plans qui façonnent le CHIS, y compris la décentralisation, la répartition des ressources, les procédures opérationnelles normalisées et l'assistance aux tâches réalisées par les ASC.
2. Surveiller et communiquer sur les indicateurs du système de santé tels que les ODD, les OMD et les indicateurs de performance clés qui comportent des données du CHIS.

Les données du CHIS sont utilisées à de multiples niveaux et à des fins diverses. Un CHIS efficace devient ainsi une base solide pour l'ensemble du système d'information sanitaire du pays. Les différents objectifs du CHIS peuvent être liés aux fonctions d'enregistrement, de suivi et de rapport définies au chapitre 1. Alors que l'enregistrement et le suivi sont des fonctions fondamentales permettant de soutenir les services au niveau des clients/bénéficiaires, la fonction de rapport s'appuie sur la fonction d'enregistrement pour répondre aux besoins d'information de l'établissement et des systèmes de santé.

## Principes pour améliorer l'utilisation des données { #principles-to-enhance-data-use }

Dans cette sous-section, nous allons discuter des principes clés de conception du CHIS qui permettent d'améliorer l'utilisation des données :

1. Conception pour une utilisation décentralisée
2. Permet une utilisation locale impliquant plusieurs parties prenantes
3. Renforce les mécanismes de retour d'information
4. Conception pour une utilisation durable des données
5. Élaborer des plans d'action communautaires
6. Développer le cadre de suivi et d'évaluation du CHIS
7. Renforcer les capacités de la communauté en matière d'utilisation des données

### 1. Utilisation décentralisée { #1-decentralized-use } 

Au fur et à mesure que l'on s'éloigne de la communauté, les données sont de moins en moins exploitées. L'un des principes fondamentaux de l'approche CHIS du HISP est l'utilisation des données le plus proche possible du lieu où elles sont produites. Un CHIS décentralisé permet aux ASC, aux superviseurs et aux leaders communautaires de s'approprier le programme et d'en assumer la responsabilité. Lorsque les personnes les plus proches des lieux s'approprient les résultats sanitaires d'un programme et en sont responsables, les résultats de ce programme sont plus probants. Le fait de ramener l'autorité et la responsabilité aux couches les plus basses va démontrer toute l'utilité du CHIS.

Plus le CHIS est conçu de manière à renforcer la prise de décision au niveau local, plus les informations sont susceptibles d'être réclamées et utilisées au niveau des couches inférieures afin d'améliorer les prestations de services. Pour ce faire, le CHIS doit fournir des données d'une grande précision et des outils d'analyse faciles à utiliser. Un CHIS conçu principalement pour soutenir la prise de décision au niveau local, avec une partie des données qui remontent de manière collective, garantira une amélioration de la qualité des données et favorisera leur utilisation efficace au niveau local pour des prises de décision éclairées.

> **Exemple**
>
> **Utilisation décentralisée des données : L'exemple du PEV**
> Toute personne ayant visité de petits centres de santé ruraux partout dans le monde aura vu des graphiques de couverture cumulée du PEV fièrement affichés au mur. Cette pratique exemplaire a été mise en place par une unité de Genève qui a convaincu tous les pays du monde de surveiller le PEV au niveau de l'établissement en traçant un simple graphique qui enregistre les principales vaccinations réalisées chaque mois en vue d'atteindre un objectif fixé. Cette pratique a été maintenue pendant de longues années grâce à des procédures simples d'utilisation des données, décrites dans le cycle vertueux des données ci-dessus.
> 
> 1. Le personnel de l'établissement est formé pour remplir les graphiques à l'aide de SOP claires et simples dans la langue locale.
> 2. Le personnel de l'établissement se réjouit de voir la couverture augmenter chaque mois.
> 3.  Les superviseurs, y compris ceux d'autres programmes, vérifient ces graphiques lorsqu'ils visitent un établissement. 
> 4. Les districts disposent des ressources nécessaires pour fournir des graphiques tout prêts (photocopiés si nécessaire) pour chaque produit dans chaque établissement, et pour assurer la supervision du PEV. 
> 5. Les unités nationales du PEV ont été convaincues que cette pratique est courante dans tous les autres pays et qu'elles devraient donc l'adopter elles aussi !  
> 6. Les membres de la communauté, lorsqu'ils visitent l'établissement, s'attendent à voir comment le PEV fonctionne dans leur localité.


### 2. Impliquer les parties prenantes { #2-engaging-stakeholders }

Diverses organisations locales, gouvernementales, non gouvernementales et de la société civile s'emploient à garantir la santé de la communauté. Il s'agit notamment des chefs de village, des responsables politiques locaux, des groupes de femmes et des ONG qui participent à des activités telles que l'implémentation de programmes, la formation, le suivi des données, les enquêtes sur les événements critiques tels que les décès maternels et infantiles, etc. Bien que le principal acteur du CHIS soit le gouvernement local, la participation de ces autres acteurs à l'amélioration de la qualité des données, à l'amélioration de leur utilisation et à la diffusion des informations au grand public peut contribuer grandement à renforcer le CHIS.


> **Exemple**
>
> **Impliquer les parties prenantes : L'exemple du Pendjab**
> Récemment, l'État du Pendjab, en Inde, a mis en place un portail de transparence sur la santé, dans lequel tous les établissements publics et privés habilités par l'État peuvent fournir des informations détaillées sur leur établissement, notamment l'adresse, la personne de contact, les services offerts et leurs coûts respectifs, l'équipement disponible et les médecins de garde. Grâce à ces informations, tout membre de la communauté devrait être en mesure d'identifier les services de santé auxquels il peut accéder, où il doit se rendre et quel est le meilleur coût. Le citoyen peut également attribuer une note aux services qu'il a reçus, note qui peut ensuite être utilisée par d'autres citoyens pour orienter leur choix en matière d'accès aux services. En rendant ces informations sur les établissements de santé accessibles au public, l'utilisation des informations répond à deux objectifs essentiels. D'une part, elle permet au personnel de santé de faire de meilleurs choix en matière de soins de santé. Deuxièmement, elle permet à l'État d'identifier les lacunes au niveau de la prestation de services et de prendre les dispositions qui s'imposent.

### 3. Renforcement des Mécanismes de Retour d'information{ #3-strengthening-feedback-mechanisms }

Lorsque des mécanismes de retour d'information *forts* sont implémentés, des phénomènes profonds peuvent être observés, mais deux se distinguent :

1. Les taux de rapport et la précision des données s'améliorent, car les ASC comprennent la valeur des données de qualité.
2. Si les acteurs communautaires suivent leurs propres performances au niveau local, ils améliorent également leurs performances.

Nous savons d'après le modèle de retour d'information transformationnelle qu'un mécanisme de retour d'information ***fort*** est celui qui:

- **Améliore la transparence des informations.** Les personnes qui ont besoin de données en disposent. Les données brutes peuvent être converties en connaissances et être exploitées.
- **Favorise un dialogue à double sens.** Les mécanismes de retour d'information doivent permettre de relier les parties prenantes aux performances du programme de santé communautaire. Au fur et à mesure que les parties prenantes prennent des décisions et agissent sur la base des connaissances qu'elles obtiennent grâce aux mécanismes de retour d'information, la santé communautaire est impactée et cela se reflète ensuite sur les données affichées au niveau des mécanismes de retour d'information. Ce processus cyclique est une forme de dialogue à double sens. Une autre forme de rétroaction qui permet un dialogue à double sens est l'appui et la supervision, qui sont abordés au chapitre 5. |
- **Favorise la mise en place de réseaux d'apprentissage.** Lorsque les différents acteurs communautaires reçoivent un retour d'information, ils peuvent travailler en réseau et concevoir des solutions plus solides et plus robustes aux problèmes de santé de la communauté. On pense souvent à tort que les projets de santé communautaire doivent régler tous les problèmes auxquels une communauté est confrontée. En réalité, les programmes de santé communautaire les plus solides sont ceux qui permettent à la communauté d'apprendre de ses membres et d'élaborer ses propres solutions éclairées.

Les mécanismes de retour d'information réduisent les obstacles entre les données, la prise de décision et les actions, mais le fait de juste transmettre des données aux parties prenantes n'aura pas cet effet. Un mécanisme de retour d'information doit permettre à la partie prenante de recevoir des données et de les transformer en informations. L'information a un sens, alors que les données brutes sont généralement considérées comme abstraites et dépourvues de sens. L'information doit ensuite être transformée en connaissance. La connaissance est liée à un contexte et peut susciter une action, mais cela n'est possible que si la partie prenante fait confiance à la source de l'information, c'est-à-dire aux données brutes. C'est pourquoi :

- **Chaque mécanisme de retour d'information doit être adapté à la meilleure méthode de transmission des informations à une partie prenante, en fonction de ses caractéristiques et de son rôle**.

Par conséquent, il ne suffit pas de transmettre des informations via un tableau de bord sur un ordinateur. Cela vaut particulièrement pour les établissements et les communautés, qui n'ont probablement pas accès à un ordinateur, qui n'ont pas le temps ni la capacité de faire de l'exploration de données. Dans ce cas, il convient de ne diffuser que les indicateurs cruciaux qui ne nécessitent pas d'ordinateur ou de connexion à une application.

Il existe plusieurs types de mécanismes de retour d'information. Vous trouverez ci-dessous un tableau décrivant ces différents types. Le choix du type de retour d'information à utiliser dépend du rôle et des activités des parties prenantes que vous avez identifiées. En règle générale, une même partie prenante peut disposer de plusieurs types de mécanismes de retour d'information.

![](resources/images/chis_figure14.jpg)


*Figure 3.3:* Modèle de mécanisme de retour d'information

#### Guide pour l'élaboration de mécanismes de retour d'information { #guidance-on-developing-feedback-mechanisms } 

Il n'existe pas de solution technologique unique pour chaque partie prenante. Par exemple, un ASC peut recevoir un SMS automatisé lui rappelant d'envoyer son rapport mensuel de surveillance des maladies. Il peut également recevoir par SMS un rapport HTML automatisé qui montre les performances de sa communauté ou de sa zone de couverture en termes de fardeau des maladies par rapport au district et à d'autres communautés. Dans cet exemple, l'ASC bénéficie de mécanismes de retour d'information qui soutiennent son flux de travail, mais aussi l'intervention ou la prestation de services. Les deux sont transmis par SMS, car c'est le moyen le plus direct d'atteindre les agents. Un simple message texte incite à une action très spécifique. Le rapport HTML ne dit peut-être pas explicitement à l'agent de mener des actions spécifiques, mais peut l'inciter à mener une action dont il sait qu'il améliorera la performance de sa zone de couverture.

Lors du choix de la meilleure technologie et de la meilleure messagerie, les éléments suivants peuvent être pris en compte :

1. Quels indicateurs fournissent les informations que les parties prenantes utilisent pour orienter leurs décisions et leurs actions ? -- La meilleure pratique consiste à établir une liste d'indicateurs minimums essentiels avec les parties prenantes, étant donné qu'un trop grand nombre d'indicateurs crée de la confusion et rend les mécanismes de retour d'information inefficaces.
2. Quelle est la capacité technique de l'ASC à interpréter les données ? -- La meilleure pratique consiste à conserver des informations qui peuvent être interprétées par un enfant qui n'a reçu que peu d'éducation formelle. Le "test des 12 ans" vous permettra de garantir que les données présentées sont facilement compréhensibles et exploitables.
3. Quelle est la fréquence à laquelle les parties prenantes ont besoin d'être informées ? Certaines parties prenantes ont-elles besoin d'informations ciblées ? Des rapports formels doivent-ils être produits pour les différentes parties prenantes (bulletin d'information, diffusion d'informations mensuelles ou trimestrielles) ? À qui les parties prenantes diffusent-elles les informations ?
4. La personne chargée de l'exploration des données est souvent différente de celle qui fait la présentation et la communication. Demandez qui fait la présentation ?
5. Quel est le moyen le plus direct de leur présenter les données ? N'oubliez pas que le moyen le plus direct est souvent l'envoi de notifications par courrier électronique ou par SMS. Autoriser l'accès aux données uniquement par le biais des tableaux de bord du DHIS2 peut constituer un obstacle à l'accès au données.
6. Comment l'indicateur sera-t-il saisi ? Si vous identifiez un indicateur pour un mécanisme de retour d'information, vous devez vous assurer que les éléments de données de cet indicateur soient saisis au bon niveau hiérarchique et à la bonne fréquence, pour permettre la mise en place des mécanismes de retour d'information.

**Outils automatisés pour les retours d'information-- DHIS2**

La diffusion des informations se fait de multiples façons. Rappelons que les données nécessaires à la prise de décision doivent être facilement accessibles. Vous trouverez ci-dessous quelques exemples de technologies utilisées dans le cadre des mécanismes de retour d'information. Il ne s'agit pas d'une liste exhaustive, mais d'une mise en évidence des solutions technologiques courantes en matière de retour d'information, telles qu'elles sont appliquées dans le cadre d'un système d'information sanitaire.

- **SMS automatisés :** Le DHIS2 peut envoyer des messages automatisés dans les cas suivants :
- **Alertes de règles de validation:** Les règles de validation peuvent être utilisées à des fins diverses. La vérification de la qualité des données est la pratique la plus courante, mais les règles de validation peuvent également être utilisées dans le cadre d'alertes programmatiques. Considérons une règle de validation "Total des cas de choléra == 0". Dans ce cas, chaque fois que le nombre de cas de choléra signalés est supérieur à zéro, le groupe d'utilisateurs chargé de recevoir les alertes automatisées relatives aux règles de validation sera informé de l'existence de cas de choléra, à l'endroit exact où ils ont été signalés, et pourra ainsi envoyer une équipe pour lutter contre la maladie.
- **Rappel pour la transmission des données:** Il est toujours préférable d'envoyer des rappels par SMS aux agents de santé des établissements et des communautés pour qu'ils transmettent leurs données de routine. Souvent, les agents de santé communautaires ne surveillent pas de près le jour du mois ou même la semaine. Il convient donc de leur rappeler de communiquer leurs données.
- **Rappel d'événements à venir à l'aide d'un tracker:** Cette fonction pourrait être utilisée pour suivre des patients de la communauté dans le cadre d'un traitement, le but étant de leur rappeler un rendez-vous à venir. Il pourrait également être utilisé pour rappeler à un agent de santé communautaire les personnes qu'il doit rencontrer pour un suivi, par exemple dans le cadre d'un projet de suivi des nouveau-nés.
- **Alerte en cas de rendez-vous manqué à l'aide d'un tracker:** Permettre aux agents de santé communautaire de suivre les personnes de leur communauté qui ont manqué un rendez-vous peut s'avérer très efficace, surtout si les prestataires de soins cliniques ne sont pas en mesure de suivre les patients qui ont manqué leur rendez-vous.
- **Rapport HTML:** Les parties prenantes utilisent souvent des technologies mobiles différentes, mais pratiquement tous les appareils mobiles disposent désormais d'un navigateur web. Grâce à iReports, des rapports peuvent être produits pour une partie prenante spécifique en fonction de son niveau d'autorisation dans le DHIS2. Par exemple, vous pouvez produire un rapport standard qui sera envoyé à tous les chefs. Ils ne pourront voir dans ce rapport que les données relatives aux unités d'organisation qui leur ont été attribuées. Vous pouvez ensuite insérer le lien vers le rapport dans un SMS automatique qui leur sera envoyé à tous. Lorsque ces derniers reçoivent le SMS et cliquent sur le lien, le navigateur web s'ouvre automatiquement sur leur rapport personnalisé.
- **E-mails automatisés :** Tout comme les SMS automatisés, le DHIS2 peut être configuré pour envoyer des e-mails automatisés dans les cas suivants :
    - Publier le tableau de bord
    - Alertes de règles de validation
    - Messagerie
    - Partage des interprétations
- **Sites internet destinés au public:** Des analyses publiques peuvent être publiées sur un site internet grâce à l'application portail internet ou grâce à une page personnalisée. Cette méthode s'est avérée très efficace pour permettre au grand public ou aux gouvernements d'accéder à des données relatives à la santé de leurs communautés.
- **Tableaux de bord normalisés et personnalisés:** Le DHIS2 permet aux utilisateurs disposant des autorisations requises d'accéder à des tableaux de bord personnalisés ou normalisés, lesquels comprennent un large éventail d'analyses (graphiques, cartes, tableaux croisés dynamiques, tableaux de performances, tableaux de classement, etc.)
- **Rapports PDF :** Avec des rapports standard, le DHIS2 peut produire des rapports PDF automatisés et personnalisés.
- **Rapports HTML :** Le DHIS2 peut produire des rapports HTML automatisés. Ces rapports peuvent être utilisés pour déterminer des indicateurs complexes qui ne sont pas disponibles dans le système
- **Application Android Tableau de bord :** L'application Tableau de bord permet à toute personne disposant d'un tableau de bord DHIS2 d'accéder à ce tableau de bord via son smartphone Android.
- **Partage des interprétations des données dans le DHIS2:** Tous les outils d'analyse développés dans le DHIS2 peuvent recevoir des commentaires, et ces derniers peuvent être mis à la disposition du public ou d'un groupe d'utilisateurs spécifique. C'est un moyen efficace qui permet de partager des informations avec des groupes d'utilisateurs et de susciter des échanges autour de ces informations. Cette méthode permet également de partager des informations et d'assigner des tâches à plusieurs utilisateurs.
- **Applications Tableau de performances:** Les tableaux de performances sont des outils d'analyse simples mais puissants qui permettent de présenter rapidement une importante quantité de données facilement exploitables. Les tableaux de performances ont été spécialement conçus pour les équipes sanitaires des villages, ce qui permet aux acteurs de santé communautaire de se faire rapidement une idée précise des lacunes des services de santé de leur communauté.

> **Tableaux de bord**
> 
> Les tableaux de bord permettent d'accéder facilement à des analyses avec des paramètres prédéfinis. Les graphiques, les tableaux et les cartes sont produits une seule fois et rassemblés dans des tableaux de bord thématiques, puis affichés sur la page d'accueil du DHIS2. Ces visualisations sont mises à jour au fur et à mesure que de nouvelles données sont introduites dans le système. Toute personne ayant accès à ce tableau de bord peut facilement trouver ces visualisations dès qu'elle ouvre le DHIS2, ce qui l'encourage à effectuer des visites régulières et à approfondir l'analyse des données.
>
> Tout comme les notifications de boucle de retour d'information, ces visualisations peuvent être personnalisées pour chaque groupe d'utilisateurs et chaque unité d'organisation. Combinées à des "périodes relatives", ces visualisations peuvent être mises à jour et personnalisées en fonction du rôle et de l'emplacement du visualiseur. Supposons que vous soyez obstétricien et que vous encadriez des accoucheuses traditionnelles dans un district rurale. À la fin du mois de mars, vous pouvez recevoir du ministère de la santé un tableau statique intitulé "mortalité maternelle dans le pays pour le compte de l'année dernière". Si vous ouvrez votre tableau de bord DHIS2, vous verrez probablement un diagramme à barres interactif intitulé "Décès maternels dans *Mon* district le mois dernier, par établissement". Ces informations sont beaucoup plus significatives pour vous, et vous pouvez les utiliser pour éclairer vos programmes.

##### **Étude de cas: Widget du tableau de bord d'assainissement des chefs en Zambie** { #case-study-zambia-chiefs-sanitation-dashboard-widget } 
En 2014, le ministère zambien des collectivités locales et du logement a lancé, avec le soutien de l'UNICEF, le projet d'assainissement total piloté par la communauté (ATPC). Afin d'impliquer les acteurs communautaires, ce projet permet aux chefs locaux de disposer de données exploitables sur l'assainissement dans leurs communautés, grâce à un widget du tableau de bord DHIS2, sur une tablette. Les questions et réponses ci-dessous illustrent la manière dont il a été décidé de présenter ces mécanismes de retour d'information aux chefs.
**1.Quels sont les indicateurs qui fournissent les informations utilisées par les parties prenantes pour orienter leurs décisions et leurs actions?** Le statut d'absence de défécation à l'air libre (ODF) est la mesure de la couverture des ménages par des "latrines adéquates". Cet indicateur permet d'indiquer aux chefs les zones où les résultats sont bons et où les résultats sont médiocres.
**2. Quelle est leur capacité technique à analyser les données?**
Les chefs sont généralement peu doués en matière d'analyse de données. Voilà pourquoi on ne leur présente qu'un seul indicateur : la couverture en latrines. Les chefs veulent connaître leurs performances par rapport aux chefferies voisines. On leur présente donc la couverture en latrines de toute la chefferie dans un diagramme à barres par rapport aux chefferies voisines. Ils sont également informés des performances de leur district par rapport à l'ensemble du pays de même que des performances de chaque village au sein de leur chefferie. 
**3. A quelle fréquence les parties prenantes ont-elles besoin d'obtenir des informations?** Les chefs rencontrent les chefs de village tous les mois, mais ils peuvent se rendre dans les villages ou procéder à des inspections à tout moment.
**4. Qui présente les données?** Les chefs peuvent comprendre les données directement à partir du widget. Dans certaines situations où le chef n'est pas en mesure de le faire, un de ses conseillers est formé sur l'utilisation de la tablette et du widget.
**5. Quelle est la manière la plus directe et la plus efficace de leur présenter et de leur communiquer ces données ? ** Les chefs doivent pouvoir consulter ces données à tout moment. Tous les chefs sont en mesure d'utiliser des téléphones intelligents, mais la mémorisation des identifiants de connexion a été identifiée comme un obstacle à l'utilisation des applications. Par conséquent, les chefs se voient présenter ces analyses via un widget, sur une tablette fournie par le projet.
**6. Comment ces données seront-elles saisies ? ** Le nombre de personnes vivant dans des zones à faible densité de population est calculé comme suit : (nombre de latrines adéquates/nombre de ménages) X 100. Le nombre de latrines adéquates et le nombre de ménages sont saisis mensuellement par le groupe d'action pour l'assainissement du village à partir des informations fournies par les ménages sur papier. Tous les mois, un responsable de la communauté collecte les données des ménages au niveau du village et les transmet au CHIS par l'intermédiaire d'une application du DHIS2, laquelle application fonctionne sur un téléphone utilisée dans le cadre du projet. Pour plus d'informations sur ce cas d'utilisation, veuillez consulter le cas d'utilisation sur l'assainissement en Zambie en annexe. La figure 1 de cette étude de cas montre le widget des chefs Mukobela.

![](resources/images/chis_figure15.png)
![](resources/images/chis_figure16.png)

*Figure 1:* Exemple de widget de la Chefferie du Chef Mukobela


### 4. Conception pour une Utilisation Durable { #4-design-for-sustainable-use } 

Pour tirer pleinement profit du CHIS, le système doit être utilisé de manière durable, ce qui signifie que les procédures d'utilisation seront soutenues à long terme et qu'elles devraient être capables d'évoluer en fonction des nouveaux besoins. Parmi les étapes vers une utilisation durable, on peut citer des objectifs, des cibles et des indicateurs clairement définis, ainsi qu'un cadre de suivi et d'évaluation du CHIS.

**A : Indicateurs, objectifs et cibles du CHIS**

Des objectifs et cibles largement convenus et un ensemble d'indicateurs qui leur sont associés constituent l'outil de base pour promouvoir le passage à un CHIS axé sur l'information. Pour garantir une utilisation maximale, toutes les données collectées par le CHIS doivent être directement associées aux indicateurs sélectionnés afin de suivre les efforts déployés pour améliorer les performances du système de santé.

Les indicateurs définis comme *"variables qui aident à mesurer les changements, directement ou indirectement*" ^[OMS, 1981] sont au cœur de la promotion d'une culture de l'utilisation des informations. La conception d'indicateurs utiles aux communautés est au cœur du processus de suivi des services et systèmes de santé communautaires et constitue l'une des compétences les plus importantes requises pour la conception d'un CHIS.

Un bon indicateur fournit des informations sur un large ensemble de conditions à travers une mesure unique et permet aux ASC et à leurs superviseurs de se comparer à d'autres personnes effectuant un travail similaire. Les indicateurs destinés aux acteurs communautaires (ASC, responsables communautaires, groupes de santé communautaires) doivent être :

Un recueil de normes et de méthodes de mesure de 40 indicateurs a été élaboré par l'OMS^[OMS, 2017] et, au niveau régional, par l'Organisation Ouest-Africaine de la Santé. Ces normes doivent être adaptées aux contextes nationaux et, à nouveau, au niveau communautaire.

### 5.  Élaborer des Plans d'Action Communautaires  { #5-develop-community-action-plans } 

Les plans d'action communautaires varient d'un pays à un autre, mais l'objectif principal est de disposer d'un même ensemble d'activités approuvées par les acteurs locaux et qui seront exécutées dans un délai déterminé. Ces plans doivent être élaborés à partir de données du CHIS générées localement, de l'analyse initiale de la situation à l'utilisation d'indicateurs pour le suivi des résultats, en passant par la définition des objectifs et l'allocation des ressources.

![](resources/images/chis_figure17.png) 
Traditionnellement, dans la plupart des systèmes de santé, le niveau le plus bas pour élaborer des plans d'action est le district, mais un CHIS solide peut mettre en place des mécanismes de rapport et de retour d'information au niveau communautaire afin d'élaborer des plans d'action à ce niveau. Cette méthode peut s'avérer très efficace pour améliorer les performances des programmes, renforcer l'autorité locale et inculquer le sens de l'appropriation et de la responsabilité.

Les plans d'action peuvent être élaborés de différentes manières et varient d'un pays à un autre, voire d'une communauté à une autre, mais de bonnes pratiques universelles en matière de plans d'action communautaire sont à prendre en considération, comme le montre la liste ci-dessous :

- Faire connaître le plan d'action afin d'obtenir une responsabilisation maximale
    - Exposer publiquement le plan d'action dans un lieu de rassemblement de la communauté tel qu'un centre de santé, une école, un point d'eau, un lieu de cérémonie traditionnelle, etc.
    - Disposer d'un site web permettant au tout un chacun de consulter les performances de la communauté. S'assurer que tous les membres de la communauté sachent comment accéder au site web.
    - S'assurer que d'autres organisations de la communauté, telles que les associations de parents d'élèves et enseignants, les groupes d'études religieuses, les clubs socio-sportifs, les groupes de femmes, etc. soient également informées de l'existence du plan d'action.
- Transformez le plan d'action en contrat.
    - Faites signer le plan d'action aux membres de la communauté et assurez-vous qu'ils reconnaissent avoir compris ce qui doit être fait.
    - Exiger que la communauté soumette électroniquement son plan d'action au CHIS, avec une photo de ce plan ou une saisie manuelle.

### 6. Élaborer le Cadre de S&E du CHIS  { #6-develop-chis-me-framework } 

Un cadre de suivi et d'évaluation (S&E) doit être mis en œuvre pour suivre et évaluer le plan d'action, en utilisant les mêmes indicateurs et paramètres que le plan.

Le cadre de S&E est une méthode systématique d'organisation et de définition d'indicateurs, d'objectifs et de valeurs et cibles de référence. Ce cadre fait également partie des procédures opérationnelles normalisées.

Le cadre de suivi et d'évaluation déterminera les indicateurs dont disposent les parties prenantes et servira de base à l'évaluation des performances et à l'élaboration de plans d'action.

Vous trouverez ci-dessous un modèle de cadre de S&E communautaire :


| **Programme** | **Indicateur Clé** | **Numérateur** | **Dénominateur** | **Date (de référence)** | **Objectif de 2020** | **Source de Données** | **Fréquence** | **Responsable** |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| Soins Prénatals (CPN) | **Couverture de la 1ère visite** | 1ères visites de CPN | Grossesses attendues | 72% | 80% | CHIS | Mensuel | ASC |
| Soins Prénatals (CPN) | **Couverture de LLITN en CPN** | LLITN distribuées en CPN | Grossesses attendues | 62% | 80% | CHIS | Trimestrielle | ASC |
| Accouchement et soins postnatals | **Taux d'accouchements dans les établissements de santé** | Accouchements dans les établissements de santé | Accouchements attendus | 43% | 55% | CHIS | Mensuel | Établissement |
| Accouchement et soins postnatals | **Couverture de CPoN** | CPoN \<48 heures | Accouchements attendus | 52% | 70% | CHIS | Mensuel | ASC / Etablissement |
| PMTCT | **Taux de dépistage du VIH en CPN** | Dépistage du VIH en CPN | 1ères visites de CPN | 72% | 90% | SNIS | Mensuel | Établissement / ASC |
| PEV | **Couverture de la rougeole** | Doses de vaccin contre la rougeole administrées | Enfants \<1 an | 53% | 75% | SNIS | Mensuel | Établissement |
| Paludisme | **Taux de paludisme** | Cas de paludisme traités | TDR Réalisés | 47% | 70% | CHIS | Trimestrielle | ASC |

*Tableau 1 Modèle de cadre de S&E communautaire, avec les indicateurs de performance clés.*

### 7. Renforcer la Capacité des Communautés en matière d'Utilisation des Données  { #7-build-community-capacity-for-data-use } 

Des méthodes ingénieuses permettent d'encourager l'utilisation des données au niveau local. Dans cette section, nous allons identifier quelques-unes qui sont reconnues efficaces.

#### Narration { #storytelling } 

La narration est une compétence qui existe dans toutes les communautés et qui a été transmise de génération en génération. C'est un bon moyen pour communiquer des informations, car raconter des histoires est un moyen basique pour notre cerveau de traiter et d'organiser les informations, et les histoires aident à relier le "Pourquoi", la valeur principale de ce que nous faisons, au "Quoi" et au "Quand" de la base de données.

Le CHIS et la formation doivent être conçus dans le but d'aider les ASC à raconter à leurs communautés des histoires pertinentes en rapport avec les données, ce qui constitue une part importante du retour d'information. Le CHIS doit aider les ASC à comprendre le contexte de l'audience, à choisir une illustration appropriée qui met l'accent sur les questions clés, puis à raconter l'histoire. La conception d'une histoire est importante et chaque histoire doit comporter les éléments suivants :

1. Le Début - Présentez l'intrigue et définissez le contexte
2. Le Milieu -- Prenez du temps dans cette partie. Parlez de "ce qui pourrait " convaincre votre public de la nécessité d'agir
3. La Fin -- Terminez votre histoire par un appel à l'action

Le storyboard est une technique utile qui permet d'établir une structure, de trouver le fil conducteur de l'histoire et de mettre en évidence les éléments importants.

#### Encourager la compétition amicale{ #encourage-friendly-competition } 

La comparaison entre unités de rapport similaires favorise la concurrence au niveau  des communautés et constitue un autre moyen d'encourager l'utilisation des données. Si les ASC ou les communautés comprennent les actions spécifiques qui pourraient être entreprises pour résoudre un problème de santé communautaire, on pourrait alors permettre aux communautés de se concurrencer et offrir un "prix" aux plus performantes.

> **Exemple**
>
> **Compétition - Exemple de la pulvérisation intradomiciliaire d'insecticides à effet rémanent en Zambie**
> Le Centre national de lutte contre le paludisme et ses partenaires utilisent le DHIS2 pour suivre en temps réel la pulvérisation intradomiciliaire d'insecticides à effet rémanent effectuée par les ASC. Ils ont ensuite décerné un prix à l'agent qui a pulvérisé le plus grand nombre de maisons et un autre prix au village comptant le plus grand nombre de maisons pulvérisées. Les villages et les ASC sont ensuite encouragés à suivre les performances de leurs pairs en temps réel. Ce type de compétition a un réel impact pour un coût minime.

#### Renforcer les Champions Communautaires { #empower-community-champions } 

L'identification de "champions" en matière d'utilisation des données au sein des communautés est essentielle pour assurer la viabilité du CHIS. Les champions varient d'une communauté à l'autre, mais tous doivent rester en contact avec les responsables du programme et recevoir des données susceptibles de promouvoir son adoption. Dans la plupart des communautés, les chefs traditionnels ou religieux exercent une influence considérable et sont en mesure de s'adresser régulièrement à un grand nombre de personnes. Leur fournir des données et des actions spécifiques que la communauté peut mettre en œuvre pour améliorer ses performances peut être le meilleur moyen de diffuser le programme auprès d'un plus grand public.

Les champions communautaires (chefs traditionnels, religieux, etc.) doivent avoir l'influence nécessaire pour exiger des membres de la communauté qu'ils suivent les actions. Les membres de la communauté qui ne respectent pas le plan d'action ou qui entravent sa mise en œuvre peuvent être sanctionnés.

> **Exemple**
>
> **Les champions de la communauté - Les prêcheurs de l'assainissement en Zambie** 
> En Zambie, les pasteurs ont reçu des sermons en langue locale avec des références à des passages spécifiques de la Bible sur l'importance de l'assainissement dans les communautés. Ces chefs religieux très respectés sont alors en mesure d'atteindre un large public au sein de la communauté.

#### Stimuler l'action locale{ #stimulate-local-action } 

Amener les parties prenantes, les responsables et les agents de changement de la communauté à faire ce qu'ils ont prévu de faire constitue souvent un obstacle majeur au programme. Si l'organisation au niveau de la communauté est médiocre ou si les ASC sont eux-mêmes peu réactifs ou simplement débordés, la communauté peut avoir beaucoup de mal à mener à bien les activités qu'elle s'est fixées. Il est essentiel de susciter un sentiment de responsabilité et d'appropriation des résultats de ces activités. Vous trouverez ci-dessous quelques bonnes pratiques pour y parvenir :

- Appels téléphoniques des superviseurs aux ASC ou aux membres de la communauté qui ont des responsabilités.
- Suivre les indicateurs clés qui montrent l'impact des actions.
- Montrer les indicateurs d'autres communautés afin qu'elles puissent évaluer leurs performances et se concurrencer.
- Récompensez la communauté la plus performante avec une cérémonie, un certificat ou un trophée.
- Produire un bulletin d'information de district/d'État qui classe les communautés en fonction de leur performance et comprend des récits sur les succès et les meilleures pratiques.

> **Exemple**
>
> **Action locale - Punition pour améliorer l'accès à l'assainissement** 
> En Zambie, les membres de la communauté qui ne voulaient pas construire de latrines ont été contraints d'en construire au palais du chef chaque mois jusqu'à ce qu'ils en construisent une dans leur propre maison. Les latrines du palais du chef pouvaient alors être utilisées lors de cérémonies traditionnelles, de réunions communautaires et de mariages, qui se déroulent souvent au palais du chef.

## Étude de cas : Utilisation locale des informations en Indonésie | { #case-study-local-use-of-information-in-indonesia } 
L'Indonésie est un pays densément peuplé, avec une population estimée à 260 millions d'habitants et des infrastructures bien développées avec des disparités entre régions. Sur le plan administratif, le pays est divisé en 36 provinces et 514 districts. Le ministère de la santé (également connu sous le nom de Kementerian Kesehatan) est une institution gouvernementale qui gère les questions relatives à la santé publique, au sein du gouvernement indonésien. La fourniture de soins de santé de base dans le pays dépend essentiellement des prestations au niveau des établissements de santé, qui sont gérés par les districts. Les établissements de santé plus importants, tels que les hôpitaux publics, sont gérés directement par le département des services hospitaliers du ministère de la santé. La participation de la communauté à l'amélioration des services de santé a été adoptée en Indonésie par le biais des services de santé communautaires (UKBM). Cela implique la création de pustu (sous-centre de santé), posyandu (poste de santé intégré) et poskesdes (poste de santé de village) (Profil de santé de l'Indonésie 2014). En Indonésie, comme dans la plupart des pays, les données sanitaires sont collectées au niveau inférieur, la plupart du temps sur une base mensuelle, et envoyées au niveau supérieur. L'essentiel des décisions ainsi que la planification sont décidées au niveau supérieur, avec des réglementations et des politiques imposées par la hiérarchie.

Dans sa volonté de renforcer le CHIS, le ministère de la santé indonésien et ses partenaires se sont engagés dans une mission visant à introduire des tableaux de bord de district en tant que plateforme de diffusion intégrée. L'initiative a consisté en une activité d'analyse de la situation au cours de laquelle une étude a été menée pour identifier les infrastructures existantes et les signaler au niveau des tableaux de bord du district. L'étude a révélé plusieurs résultats, mais ce rapport tente de documenter les résultats observés sur l'utilisation locale des informations au plus bas niveau.

**Flux de données** 
Au niveau communautaire, les données collectées portent essentiellement sur la santé de la mère et de l'enfant, étant donné que ce sont ces deux membres de la famille qui doivent être traités en priorité dans les services de santé. Au niveau de l'établissement de santé, les données des patients non hospitalisés et hospitalisés sont collectées avec d'autres données provenant des programmes de santé (VIH, tuberculose, paludisme, etc.). Les données des établissements de santé sont généralement agrégées et envoyées au niveau administratif supérieur pour être traitées et analysées. L'utilisation des systèmes d'information sanitaire pour gérer les données est très répandue, avec des disparités au démarrage des systèmes. Par exemple, certains postes communautaires avaient accès au système d'information sanitaire pour la collecte et la déclaration des données, alors que d'autres postes dans d'autres districts collectaient et déclaraient leurs données sur papier et dans des cahiers.

![](resources/images/chis_figure18.png)

*Figure 1:* Flux de données du niveau communautaire au niveau national

**Utilisation locale des informations** - Approches Observées lors de l'Évaluation

- *Stratégies de diffusion des données:*  les établissements de santé et les postes communautaires disposaient d'un moyen structuré pour documenter les cas mères-enfants au sein de la communauté. Les figures 2 et 3 présentent les rapports graphiques et textuels que les établissements utilisent pour suivre les cas de maternité au sein de leur communauté. Le mécanisme graphique classe également les cas en trois catégories (rouge, vert et jaune). Les cas en rouge sont ceux qui sont exposés à des facteurs de risque, les cas en jaune présentent des facteurs de risque intermédiaires et les cas en vert sont ceux qui présentent un faible risque. Les cas sont également positionnés dans leur village et dans leur rue pour faciliter le suivi.

![](resources/images/chis_figure19.jpg)
![](resources/images/chis_figure20.png)

*Figure 2 & 3:* Utilisation locale des données

- *Réunions mensuelles en SSP:*  les données fournies par les agents de santé communautaires sont généralement collectées par le responsable du programme à la fin du mois. Des réunions régulières sont organisées au cours desquelles les directeurs de programme rendent compte de la couverture des villages et discutent des problèmes de santé survenus au cours du mois ainsi que des priorités. Des discussions plus approfondies ont eu lieu sur la manière d'améliorer les résultats et sur les zones où la couverture est faible, par exemple la couverture vaccinale.
- *Réunion trimestrielle avec les acteurs concernés:* Chaque trimestre, une réunion intersectorielle est organisée au niveau du district. Les responsables des établissements de santé présentent les données sanitaires du trimestre en cours et discutent du rôle des acteurs intersectoriels (chefs de sous-district, chefs de village, chefs religieux, écoles, etc.) dans l'amélioration des services communautaires.

