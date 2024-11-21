---
edit_url: "https://github.com/dhis2/dhis2-releases/blob/master/releases/2.38/README.md"
revision_date: "2022-03-23"
---

# Notes de mise à jour de la version 2.38 { #238-upgrade-notes }

## Support Java { #java-support }

Java JDK version 11 est requis à partir de DHIS 2.38. Cela signifie que vous ne pouvez plus utiliser Java 8 lorsque vous déployez le DHIS 2.38 et plus.

Java 11 est pris en charge pour le DHIS 2 depuis la version 2.35. Cela signifie que vous pouvez mettre votre serveur à niveau vers le JDK 11 tout en continuant à utiliser le DHIS 2.35 ou une version ultérieure en vue de la mise à niveau du DHIS 2.38. Java 11 s'est avéré être fiable et nettement plus rapide pour le DHIS 2.

Comme toujours, nous recommandons d'utiliser une distribution OpenJDK de Java, en raison de sa nature gratuite et open source. Les distributions OpenJDK 11 sont disponibles sur tous les principaux systèmes d'exploitation et constituent le JDK par défaut sur Ubuntu 20.04 LTS.

## Base de données { #database }

## API { #api }

-   L'exécution manuelle des tâches à l'aide de `/api/jobConfigurations/execute` est passée de la requête `GET` à `POST`.
-   L'identifiant du programme est désormais obligatoire pour l'étape du programme. Points de terminaison affectés : `/programStages`, `/metadata`
-   `GET /systemSettings` renvoyant JSONP (`Accept=application/javascript`) a été supprimé.
-   Plusieurs points de terminaison de l'API modifient légèrement leur objet racine de réponse pour s'aligner sur la majorité des points de terminaison. L'objet racine renvoyé avant la 2.38 deviendra le membre appelé `response` du nouvel objet racine renvoyé par la 2.38. Les consommateurs peuvent donc choisir d'utiliser `/api/37/...` pour obtenir l'ancien comportement ou doivent décompresser la nouvelle réponse en faisant `<root>.response` pour résoudre la racine précédente de la réponse 2.38.

    > **NOTE**
    >
    > In case of error responses this also entails an HTTP status code change from `200 OK` to `409 Conflict`.

    Voici les points de terminaison affectés :

    -   `POST /api/completeDataSetRegistrations` avec `JSON`/`XML` (seulement les non `async` affectés)
    -   `POST /api/dataValueSets` avec `JSON`/`XML`/`ADX`/`CSV` (seulement les non `async` affectés)
    -   `POST /api/metadata` avec `JSON`/`XML`/`GML`/`CSV` (seulement les non `async` affectés)
    -   `POST /api/predictions` (seulement les non `async` affectés)
    -   `PUT /api/predictions` (seulement les non `async` affectés)
    -   `PUT /api/relationships/{id}`
    -   `PUT /api/users/{uid}` with `JSON`/`XML`

## Autorités { #authorities }

## Audit { #audit }
