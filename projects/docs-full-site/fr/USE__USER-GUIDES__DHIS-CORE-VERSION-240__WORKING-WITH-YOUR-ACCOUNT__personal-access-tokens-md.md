---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.40/src/user/personal-access-tokens.md"
revision_date: '2022-03-21'
tags:
- DHIS Version 2.40
- Utilisation
---

# Jetons d'accès personnels { #personal_access_tokens }

## À propos des jetons d'accès personnel { #about-personal-access-tokens } 

Les jetons d'accès personnels (PAT) sont une alternative à l'utilisation de mots de passe lors 
de l'authentification au système DHIS2 lorsque l'on utilise l'API.

Les jetons d'accès personnel peuvent être une alternative plus sécurisée à l'authentification 
de base HTTP et devraient être votre choix privilégié lorsque vous créez une nouvelle application, un script, etc.

L'authentification de base HTTP est considérée comme non sécurisée car, entre autres, 
elle envoie votre nom d'utilisateur et votre mot de passe de façon indiscrète. Il est possible qu'elle soit abandonnée dans les versions 
futures de DHIS2 ou qu'elle devienne facultative, ce qui signifie que l'authentification de base devra 
être explicitement activée dans la configuration.

#### Problèmes de sécurité majeurs ! { #important-security-concerns } 

Vos jetons d'accès personnel hériteront automatiquement de toutes les permissions et autorisations dont dispose votre utilisateur. Il est donc extrêmement important de limiter l'accès que vous accordez à votre jeton en fonction de l'utilisation que vous comptez en faire, voir **Configurer votre jeton**.

> **Attention**
>
> Si vous souhaitez que le jeton n'ait accès qu'à une partie restreinte et spécifique du 
> serveur, il est plutôt recommandé de créer un nouvel utilisateur spécial auquel vous n'attribuerez que 
> les rôles et autorisations auxquels vous souhaitez qu'il ait accès.


## Contextes du serveur/script et du navigateur { #serverscript-and-browser-contexts } 

Lors de la création d'un jeton d'accès personnel à l'aide de l'application Profil Utilisateur, vous serez invité à sélectionner 
le contexte dans lequel le jeton sera utilisé.

Bien que les deux contextes vous permettent de spécifier la date d'expiration de votre jeton ainsi que les méthodes HTTP 
autorisées, ils diffèrent par les restrictions supplémentaires qu'ils fournissent.

### Contexte du serveur/script { #serverscript-context }

Le contexte du serveur/script s'applique aux cas d'utilisation où votre instance DHIS2 ne sera pas accessible par un navigateur, tels que les intégrations et les scripts.

En plus de vous permettre de définir la date d'expiration du jeton et les méthodes HTTP 
autorisées, vous pouvez dans ce contexte restreindre l'ensemble des adresses IP à partir desquelles ce 
jeton peut être utilisé. Par exemple, si vous limitez votre jeton à l'adresse IP 
`91.242.200.159` et qu'un tiers malveillant obtient votre jeton et tente de l'utiliser 
à partir de l'adresse IP `142.250.187.206`, votre instance DHIS2 rejettera 
cette requête malveillante.

> **Important**
>
> La validation de l'adresse IP repose sur l'en-tête `X-Transféré-À`, qui peut être usurpé. 
> Pour des raisons de sécurité, assurez-vous qu'un équilibreur de charge ou un proxy inverse écrase cet en-tête.

### Contexte du navigateur { #browser-context } 

Le contexte navigateur s'applique aux cas d'utilisation où votre instance DHIS2 sera 
accessible par un navigateur Web, tels que les portails publics ainsi que d'autres applications d'accès 
public.

En plus de vous permettre de définir la date d'expiration du jeton et les méthodes HTTP autorisées, dans 
ce contexte, vous pouvez restreindre les sites Web où votre jeton est 
intégré. Cette restriction est obtenue à l'aide de l'[en-tête Référence 
HTTP](https://en.wikipedia.org/wiki/HTTP_referer).

> **Important**
>
> Ceci n'est pas une fonctionnalité de sécurité. L'en-tête de `référence` peut être facilement usurpé. 
> Ce paramètre est destiné à dissuader les développeurs tiers non autorisés à se 
connecter 
> aux instances d'accès public.


## Cas d'utilisation { #use-cases }

Les jetons d'accès personnel sont utiles lorsque des services externes et des intégrations doivent 
communiquer en toute sécurité avec votre instance DHIS2. Etant donné que les jetons héritent des autorisations 
du compte auquel ils sont associés, vous pouvez vous assurer que vos intégrations ne puissent 
lire et modifier que les données pertinentes.

Les jetons d'accès personnel constituent également une alternative plus sécurisée à l'authentification de base HTTP et devraient 
être votre choix privilégié lorsque vous créez une nouvelle application, un script, etc.


## Considérations en matière de sécurité { #security-considerations } 

### Considérez vos jetons d'accès personnel comme des mots de passe { #treat-your-pats-like-passwords } 

Vous devez considérer vos jetons d'accès personnel  comme des mots de passe et les garder secrets. Si vous pensez qu'un jeton a été divulgué ou usurpé, retirez-le  immédiatement.

Transmettez si possible des jetons à vos scripts et applications sous la forme d'une variable environnementale au lieu de les coder en dur.

### La validation de l'adresse IP peut être contournée dans certains cas { #ip-address-validation-can-be-bypassed-in-some-cases } 

Les restrictions d'adresse IP pour les jetons de contexte serveur reposent sur 
l'en-tête `X-Transféré-À`, qui peut être usurpé. Pour empêcher l'usurpation, configurez 
votre équilibreur de charge ou votre proxy inverse de manière à écraser l'en-tête.

### L'en-tête de `référence` n'est pas une fonction de sécurité  { #the-referer-header-is-not-a-security-feature } 

Alors que les restrictions de référence pour les jetons de contexte navigateur sont utiles pour limiter 
les abus, l'en-tête de `référence` peut être usurpé. Ne vous fiez pas aux restrictions 
de référence car l'en-tête de `référence` n'est pas une fonctionnalité de sécurité.


## Créer des jetons d'accès personnel { #creating-pats } 

Les jetons d'accès personnel sont créés à l'aide de l'application Profil Utilisateur.

1. Connectez-vous avec votre nom d'utilisateur et votre mot de passe et accédez à votre page de profil. L'application 
   Profil de l'utilisateur est accessible en cliquant sur votre avatar dans le coin supérieur 
   droit, et en choisissant "Modifier le profil" dans le menu déroulant.

   ![](resources/images/personal_access_tokens/user_profile.png)
2. Choisissez "Jetons d'accès personnel" dans la barre latérale de navigation située à gauche de l'écran

   ![](resources/images/personal_access_tokens/manage_tokens.png)
3. Cliquez sur le bouton "Générer un nouveau jeton" pour afficher la nouvelle fenêtre de dialogue du jeton

   ![](resources/images/personal_access_tokens/contexts.png)
4. Choisissez le contexte approprié au nouveau jeton 
5. Entrez une date d'expiration appropriée pour votre jeton
6. Vous pouvez éventuellement configurer les restrictions spécifiques au contexte de votre jeton (adresses IP
   pour les contextes de serveur ou les références pour les contextes de navigateur).
7. Vous pouvez aussi choisir les méthodes HTTP auxquelles votre jeton doit avoir accès lors de l'utilisation du 
   REST API de votre instance
8. Cliquez sur le bouton "Générer un nouveau jeton"
9. Votre jeton sera généré et ne vous sera montré qu'une seule fois. Il est donc important 
   que vous puissiez copier la clé du jeton dès à présent et l'enregistrer dans un endroit sûr pour pouvoir l'utiliser ultérieurement.

   ![](resources/images/personal_access_tokens/new_token.png)

> **Important**
>
> Cette clé de jeton secrète générée ne sera affichée qu'une seule fois. Il est donc important 
> que vous la copiez maintenant et que vous la sauvegardiez en lieu sûr pour une utilisation ultérieure. 
> La clé de jeton secrète sera hachée de manière sécurisée sur le serveur, et seul le hachage de cette clé sécurisée 
> sera enregistré dans la base de données ; ceci pour minimiser les risques relatifs à la sécurité s'il arrivait qu'une personne obtienne 
> un accès non autorisé à la base de données, de la même manière que les mots de passe sont gérés.

### Contexte du serveur  { #server-context } 

Les jetons pour les contextes serveur peuvent restreindre les adresses IP à partir desquelles ils peuvent être utilisés.

Ces adresses IP peuvent être fournies dans la zone de saisie « Adresses IP autorisées », 
à raison d'une adresse par ligne.

### Contexte du navigateur { #browser-context } 

Les jetons pour les contextes des navigateurs peuvent restreindre les pages Web à partir desquelles ils peuvent être utilisés.

Ces URL peuvent être fournies dans la zone de saisie "Référents autorisés", à raison d'une URL 
par ligne.


## Utiliser les jetons d'accès personnel { #using-pats } 

Pour faire une demande avec votre jeton nouvellement créé, utilisez convenablement l'en-tête 
d'autorisation .

Le format de l'en-tête d'autorisation est :

```
Autorisation : ApiToken [YOUR_SECRET_API_TOKEN_KEY]
```

Exemple utilisant l'API JavaScript `fetch`  :

```js
récupérer(url, {
  en-têtes: {
    'Autorisation': 'ApiToken d2pat_5xVA12xyUbWNedQxy4ohH77WlxRGVvZZ1151814092',
  }
})
```

### Configuration du serveur { #server-configuration } 

> **Important**
>
> Avant la version DHIS2 2.38, la fonction jetons d'accès personnel a été désactivée par défaut. 
> Pour activer les jetons, `activez` la propriété `enable.api_token.authentication` dans le fichier dhis.conf.

