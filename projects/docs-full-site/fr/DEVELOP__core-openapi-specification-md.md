---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/developer/web-api/openapi.md"
revision_date: '2023-03-21'
tags:
- Développer
---

# OpenAPI { #openapi } 

Le serveur DHIS2 peut fournir un document OpenAPI pour son API.
Ce document est créé à la volée à partir de l'analyse de l'API réelle.
Cela signifie que le document est terminé, mais que des détails peuvent être perdus ou mal interprétés
en raison des limites de l'analyse.

Les formats JSON et YAML sont supportés par tous les points d'entrée de l'OpenAPI.
YAML doit être consulté avec un en-tête `Accepter` de `application/x-yaml`.

Pour récupérer un document unique contenant tous les points d'accès du serveur, utilisez :

    GET /api/openapi.json
    GET /api/openapi.yaml

OBS ! Sachez que cette opération génère un document de plusieurs Mo.

Il est possible d'accéder à un document pour un point de terminaison spécifique en ajoutant soit 
`openapi.json` ou `openapi.yaml` au chemin racine d'un point de terminaison. 
Par exemple, pour générer un document pour les points de terminaison `/users`, utilisez :

    GET /api/users/openapi.json
    GET /api/users/openapi.yaml

Pour générer un document avec une sélection spécifique de chemins d'accès à la racine 
et/ou des étiquettes, le point d'accès général `/openapi` peut être utilisé avec un ou plusieurs 
sélecteurs `étiquette` et `chemin`.

    GET /api/openapi/openapi.json?path=/users&path=/dataElements
    GET /api/openapi/openapi.yaml?tag=system&tag=metadata

Les étiquettes disponibles sont :

* `utilisateur`
* `données`
* `métadonnées`
* `ui`
* `analyses`
* `système`
* `messagerie`
* `tracker`
* `intégration`
* `connexion`
* `requête`
* `gestion`

