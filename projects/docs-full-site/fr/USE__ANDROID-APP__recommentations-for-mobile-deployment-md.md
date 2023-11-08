---
edit_url: "https://github.com/dhis2/dhis2-android-docs/blob/main/content/capture-app/recommendations-for-a-dhis2-mobile-deployment.md"
revision_date: '2022-01-07'
tags:
- Utilisation
---

# Recommandations relatives à un déploiement de DHIS 2 sur mobile { #capture_app_recommendations }

Si vous prévoyez le déploiement de l'application Android DHIS2 sur le terrain, nous vous recommandons vivement de lire les [Lignes directrices pour la mise en œuvre sur les appareils mobiles] (https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/about-this-guide.html) publiées par UiO. Ce document contient des chapitres consacrés aux exigences technologiques, aux aspects de sécurité et de configuration, ainsi qu'aux recommandations de test et de déploiement. Vous trouverez ci-dessous une présentation succincte de certains aspects clés ; nous vous recommandons également de lire le document détaillé.

## Spécifications des appareils mobiles { #capture_app_recommendations_mobile_specs }

L'application Android est compatible et prise en charge par les versions 2.35 et 2.37 de DHIS 2. De plus, elle ne présente aucune modification importante par rapport aux versions 2.30 et 2.34.

Elle nécessite un appareil fonctionnant sous Android v4.4 (non recommandé mais pris en charge jusqu'en avril 2022) ou supérieur. Le minimum recommandé pour les nouveaux appareils est Android 7 ou supérieur.

Dans [la section spécifique des lignes directrices sur la mise en œuvre sur appareils mobiles](https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/mobile-device-specifications.html) vous trouverez des recommandations relatives à l'acquisition de nouveaux appareils mobiles pour un déploiement du Dhis2 sur Android.

## Test et essai pilote { #capture_app_recommendations_testing }

Si vous prévoyez un déploiement de l'application Android DHIS 2 sur le terrain, vous devez d'abord effectuer une série complète de tests de l'application dans votre propre configuration.

L'application a été largement testée avec les serveurs de démo. De plus, lors des tests bêta, elle a également été testée avec des configurations réelles. Nous savons cependant que chaque configuration DHIS 2 est particulière à bien des égards, et peut entraîner des incohérences que nous n'avons pas pu identifier.

Il est fortement recommandé d'effectuer un test complet de l'application sur votre propre serveur avant de procéder à l'essai pilote.

