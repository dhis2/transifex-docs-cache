# Note de mise à jour de la version 2.36 du DHIS

Le présent document se propose de décrire les principales fonctionnalités de la version initiale de la 2.36 du DHIS2. Cette version est entièrement compatible avec le DHIS2 [Android Capture App](https://www.dhis2.org/android-2-4) version 2.4.


## FONCTIONNALITÉS D'ANALYSE

**Diagrammes de dispersion :** Permet aux utilisateurs de représenter les unités d'organisation sous forme de points par rapport à deux variables pour une seule période au moyen de diagrammes de dispersion.

  - *Effectuez un zoom avant* en cliquant et en faisant glisser le curseur sur la zone que vous souhaitez agrandir. Cette opération est souvent nécessaire pour obtenir plus de détails dans les zones où de nombreuses unités d'organisation sont regroupées.
  - *La détection des valeurs aberrantes* peut être effectuée à l'aide d'un z-score standard, d'un z-score modifié ou d'un écart interquartile via le menu des options. Une ligne de seuil extrême verticale (axe des y) et horizontale (axe des x) peut également être appliquée. Approuvée par l'OMS, cette méthode constitue un moyen très efficace et précis pour identifier les valeurs aberrantes qui, souvent, représentent des problèmes de qualité des données. Vous pouvez identifier les valeurs aberrantes les plus susceptibles de fausser les statistiques nationales en utilisant la détection des valeurs aberrantes en combinaison avec les lignes de seuil extrêmes X et Y.

[Capture d'écran]() | [Docs]()

**Mode de présentation plein écran des éléments du tableau de bord : ** Permet d'agrandir tout élément du tableau de bord (graphique, carte ou tableau croisé dynamique) à la taille maximale de l'écran. Ce mode est idéal pour les présentations de données lors de réunions virtuelles ou en présentiel, directement à partir du tableau de bord.

[Capture d'écran]() | [Docs]()

**Légendes des diagrammes en barres et en colonnes :** Permet de modifier la couleur d'une barre ou d'une colonne en fonction d'une légende prédéfinie. Cela permet de mettre facilement en évidence les mauvaises et meilleures performances à l'aide de diagrammes en barres et en colonnes.

[Capture d'écran]() | [Docs]()

**Application Tableau de bord adaptée aux appareils mobiles :** L'application web Tableaux de bord du DHIS 2 est désormais plus conviviale et plus facile à utiliser sur les appareils mobiles. Cela vous permet d'utiliser le potentiel des tableaux de bord depuis votre appareil mobile. Vous pouvez désormais emporter vos tableaux de bord avec vous, les consulter à tout moment et partager des données avec qui vous voulez depuis le confort de votre téléphone. L'application a adopté plusieurs des principes des _Applications web progressive_ (PWA). Le support hors ligne des tableaux de bord sera disponible dans une prochaine version.

[Capture d'écran]() | [Docs]()



[Capture d'écran]() | [Docs]()



[Capture d'écran]() | [Docs]()



[Capture d'écran]() | [Docs]()



[Capture d'écran]() | [Docs]()


## FONCTIONNALITÉS DE SUIVI ET D'ÉVÉNEMENTS



[Jira]()



[Capture d'écran]() | [Documents]() | [Jira]()



[Documents]() | [Jira]()

## FONCTIONNALITÉS DE LA PLATE-FORME

**Détection des valeurs aberrantes :** Une nouvelle méthode optimisée de détection des valeurs aberrantes est disponible dans l'application Qualité des données. Les valeurs aberrantes sont désormais classées et les plus importantes sont renvoyées en premier, ce qui facilite grandement la recherche et la correction des valeurs aberrantes ayant un impact important sur votre analyse de données. Auparavant, les valeurs aberrantes étaient renvoyées sans ordre. Les valeurs aberrantes sont classées par *distance absolue par rapport à la moyenne*. Le *z-score* de la valeur, ainsi que la moyenne, l'écart-type, le minimum et le maximum sont disponibles dans la réponse.

[Capture d'écran]() | [Documentation utilisateur]() | [Documentation API]() 

**OpenID Connect :** La prise en charge d'OpenID Connect (OIDC) a été considérablement améliorée. Une solution générique est désormais disponible, laquelle fonctionnera avec la plupart des fournisseurs OIDC. Des fournisseurs spécifiques pour Azure et WSO2 ont également été ajoutés. Les fournisseurs dont le fonctionnement a été testé et vérifié sont notamment Google, Microsoft/Azure, Okta, Keykloak et WSO2. OIDC permet l'authentification unique sur plusieurs systèmes tout en gérant les identités dans un emplacement central.

[Documents]()



[Docs]() |[Jira 1](https://jira.dhis2.org/browse/DHIS2-10562)|[2](https://jira.dhis2.org/browse/DHIS2-10556)|[3](https://jira.dhis2.org/browse/DHIS2-10487)|[4](https://jira.dhis2.org/browse/DHIS2-8669)|[5](https://jira.dhis2.org/browse/DHIS2-8297)|[6](https://jira.dhis2.org/browse/DHIS2-5587)

**Expiration des comptes d'utilisateur:** Les comptes d'utilisateur peuvent désormais être configurés de manière à expirer à une date donnée. Cette fonctionnalité permet de créer des comptes temporaires, par exemple pour inviter des partenaires par le biais de comptes d'invités.

[Jira](https://jira.dhis2.org/browse/DHIS2-8089)

**Désactiver les utilisateurs inactifs:** Une nouvelle tâche est disponible pour désactiver automatiquement les utilisateurs qui sont restés inactifs (non connectés) pendant un certain nombre de mois. Cette opération est utile du point de vue de la sécurité pour éviter que les comptes d'utilisateurs inactifs ne soient compromis.

[Documents]()

**Partage de la lecture des données pour les vues SQL :** Le partage de la lecture des données est désormais requis pour la lecture des résultats d'une vue SQL. Cela permet aux responsables de la mise en œuvre d'accorder aux utilisateurs l'accès à la lecture des résultats des vues SQL sans leur donner la possibilité d'ajouter ou de modifier ces vues.

[Documents]()

**Performance des contrôles d'intégrité des données:** La performance des contrôles d'intégrité des données (dans l'application Administration des données) a également été améliorée et s'effectue beaucoup plus rapidement.

[Documents]()

**Désactiver l'exécution des règles du programme :** Une nouvelle propriété de configuration est disponible dans `dhis.conf` pour désactiver/activer l'exécution des règles du programme côté serveur.

[Documents]()

## FONCTIONNALITÉS DE L'API

**Nœud principal du cluster :** Dans une configuration de cluster, l'ID du nœud principal est disponible dans le nouveau point d'extrémité `/api/cluster/leader`. Cela permet aux administrateurs système de comprendre quel nœud du cluster agit en tant que leader et exécute les tâches planifiées.

[Docs](https://docs.dhis2.org/en/develop/using-the-api/dhis-core-version-master/maintenance.html#cluster-info)|[Jira](https://jira.dhis2.org/browse/DHIS2-102579)

**Suivi des valeurs de données :** Un nouveau point d'extrémité est disponible pour marquer les valeurs de données à des fins de suivi.

[Documentation](https://docs.dhis2.org/master/en/dhis2_developer_manual/web-api.html#follow-up)

**Fuseau horaire du serveur :** Les informations relatives au fuseau horaire du serveur sont ajoutées au point d'extrémité `/api/system/info`.

[Documentation]()

**Supprimer les résultats de validation :** Un nouveau point d'extrémité est disponible pour supprimer les résultats de validation.

 [Docs]()|[Jira](https://jira.dhis2.org/browse/DHIS2-74399)|

## INFORMATIONS RELATIVES À LA VERSION


|Informations relatives à la version|Lien|
| --- | --- |
|Télécharger la version et la base de données exemple|https://www.dhis2.org/downloads|
|Documentation|[https://www.dhis2.org/documentation](https://docs.dhis2.org/)|
|Notes de mise à jour|[Notes de mise à jour sur GitHub](https://github.com/dhis2/dhis2-releases/blob/master/releases/2.36/README.md)|
|Détails concernant chaque fonctionnalité de JIRA|https://jira.dhis2.org/issues/?filter=XXXXX|
|Aperçu des bugs corrigés sur JIRA|https://jira.dhis2.org/issues/?filter=XXXXX|
|Code source sur Github|https://github.com/dhis2|
|Instance de démonstration|https://play.dhis2.org/2.36/|
|Docker|`docker pull dhis2/core:2.36.0`<br>_pour plus de variantes d'images Docker, voir [dockerhub](https://hub.docker.com/repository/docker/dhis2/core)_|
|La communauté DHIS 2|https://community.dhis2.org/|
