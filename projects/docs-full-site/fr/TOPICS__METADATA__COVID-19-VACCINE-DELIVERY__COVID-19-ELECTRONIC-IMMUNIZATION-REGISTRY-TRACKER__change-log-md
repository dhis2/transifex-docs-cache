---
edit_url: "https://github.com/dhis2-metadata/CVIR-Electronic_Immunization_Registry_Covid19_Vaccines/blob/master/docs/cvc_eir_change_log.md"
revision_date: "2021-12-01"
---

# Journaux des modifications { #cvc-eir-change-log }

Si vous avez installé l’un des packages en cours de développement avant sa sortie officielle, voici les principales modifications apportées entre chaque version :

## Journal des modifications de la version 0.1 { #change-log-for-version-01 }

1. Indicateurs « MAPI par produit » : Filtre modifié
2. Visualisation « COVAC-MAPI par type d’événement » : Ajout de Paralysie de Bell, Lymphadénopathie, Neurologique/Musculaire
3. Ajout d’une explication pour les visualisations des abandons
4. Ajout des alertes par SMS
5. Modification des règles du programme pour répondre aux exigences des androïdes
6. Correction de plusieurs fautes d’orthographe
7. Modification du numéro de lot en « Générer comme code-barres » sur Android
8. Modification des règles du programme pour l’attribution de valeurs aux maladies sous-jacentes, qui ne sont plus actives dans l’ensemble du programme, mais uniquement dans la phase de vaccination

## Journal des modifications de la version 0.2 { #change-log-for-version-02 }

1. Ajout des groupes d’utilisateurs : Administration des métadonnées de vaccination contre la COVID Collecte des données de vaccination contre la COVID Analyse des données de vaccination contre la COVID
2. Suppression de l’étape MAPI
3. Suppressions des indicateurs de la MAPI
4. Suppression des indicateurs du programme MAPI 
5. Ajout de l’élément de données « Présence de MAPI » dans la phase de vaccination

## Journal des modifications de la version 0.3 { #change-log-for-version-03 }

1. Ajout des fabricants
2. Ajout d'un ensemble d'options pour les fabricants
3. Ajout de Doses totales requises pour ce vaccin
4. Ajout d’une règle de programme qui masque le nom des fabricants en fonction du produit de vaccination
5. Ajout d’une règle de programme qui attribue le nombre de doses totales requises
6. Modification de « Dose administrée le » en « Dose administrée le (date de vaccination) »
7. Modification de l’attribut « Identifiant unique » en « Identifiant unique du PEV » afin de correspondre à la MAPI

## Journal des modifications de la version 0.4 { #change-log-for-version-04 }

1. Modification de l’élément de données « Type de vaccin » en « Vaccin administré » et remplacement des noms d’options des produits génériques (par exemple COVAC1) par des noms de produits et de fabricants (par exemple « mRNA-1273/Moderna »).
2. Modification de l’élément de données « Nom du vaccin » en « Fabricant du vaccin » et ajout d’une liste
3. Ajout de Gamaleya et Sinopharm et de leurs produits respectifs (voir le tableau ci-dessous)
4. Ajout d’une règle de programme pour renseigner automatiquement l’élément de données « Fabricant » selon le nom du vaccin.
5. Ajout d’une règle de programme pour masquer les options de nom de vaccin pour Astrazeneca
6. Ajout d’une règle de programme pour renseigner automatiquement l’élément de données « Ceci est la dernière dose » lorsqu’un patient reçoit une deuxième dose. (en supposant que tous les produits utilisés nécessitent deux doses conformément à leur calendrier vaccinal)
7. Modification de l’expression dans la règle du programme qui ne fixe pas une date pour la prochaine dose après administration de la dernière dose.
8. Modification de la notification de la MAPI de « Veuillez vous assurer d’enregistrer cet effet secondaire au stade de la MAPI » en « Veuillez mener une enquête sur la MAPI conformément aux procédures officielles requises »
9. Modification des codes des produits génériques

| Nom du vaccin | Code de l’option vaccinale (ancien) | Code de l’option vaccinale (actuel) | Nom du fabricant | Code d’option | Âge recommandé | Intervalle entre les doses | Nombre de doses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AZD1222 / AstraZeneca | COVAC1 | astrazeneca | AstraZeneca | astrazeneca | 18 | 10 jours (8-12\*) | 2 |
| AZD1222 / AstraZeneca | COVAC1 | astrazeneca | SKBio Astra Zeneca | skbioastrazeneca | 18 | 10 (8-12\*) | 2 |
| BNT162b2 / COMIRNATY Tozinameran (INN) / BioNTech/Pfizer | COVAC2 | biontechpfizer | Comirnaty, Tozinameran | biontechpfizer | 16 | 21 | 2 |
| mRNA-1273 / Moderna | COVAC3 | moderna | mRNA-1273 | moderna | 18 | 28 | 2 |
| Gamaleya | COVAC4 | gamaleya | Sputnik V | gamaleya | 18 | 21 | 2 |
| Vaccin contre le SARS-CoV-2 (cellule Vero), inactivé / Sinopharm | COVAC5 | sinopharm | Coronavac, BBIBP-CorV | sinopharm | 18 | 21 jours (21-28)\* | 2 |

## Journal des modifications de la version 0.5 { #change-log-for-version-05 }

1. Changement de COVAX en COVAC
2. Modification de l’ordre des listes de tâches personnalisées
3. Ajout du préfixe « COVAC » aux objets qui pourraient poser des problèmes lors de l’importation avec les instances ayant des packages existants (Sexe, Oui/Non/Inconnu/, Urbaine/Rurale).

## Journal des modifications de la version 1.1 { #change-log-for-version-11 }

1. Modification de la règle du programme : « Si le vaccin précédent est identique au vaccin actuel, masquer le champ d’explication »
2. Ajout de la règle de programme « Masquer la date suggérée pour la dose suivante si la deuxième dose et le produit vaccinal sont en rupture de stock ».
3. Modification de l’expression dans la règle du programme « Si le patient a eu des maladies sous-jacentes, transférer cette valeur à l’étape suivante » et ajout d’une action pour attribuer une valeur à la variable de la règle de programme actuelle.
4. Modification des expressions dans les règles du programme « Si XXX est inclus dans l’historique du client, attribuer une valeur à l’événement actuel ».
