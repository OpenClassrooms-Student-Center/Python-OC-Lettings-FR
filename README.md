## Résumé

### Site web d'Orange County Lettings  

### Branche développement : [![CircleCI](https://circleci.com/gh/Olrio/P13/tree/new_dev.svg?style=svg)](https://circleci.com/gh/Olrio/P13/tree/new_dev)  
### Branche master: [![CircleCI](https://circleci.com/gh/Olrio/P13/tree/master.svg?style=svg)](https://circleci.com/gh/Olrio/P13/tree/master)

<p>
  <img src="https://img.shields.io/github/last-commit/Olrio/P13" alt="">
  <img src="https://img.shields.io/docker/image-size/olrio/orange_lettings?label=docker image size" alt="">
</p>

## Développement local
### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`  

## Déploiement  

**Remarque** : Les outils d'intégration/développement continus (**CircleCI**) et de déploiement sur serveur (**Heroku**) décrits ci-après sont ceux qui ont été utilisés par l'auteur.  
Des alternatives existent mais leur utilisation ne sera pas décrite ici.


### Prérequis (en plus de ceux cités précédemment)

- Compte CircleCI 
- Compte DockerHub
- Compte Heroku
- Heroku CLI

### Création du pipeline d'intégration continue / déploiement continu (CI/CD)

Le principe de l'intégration continue / déploiement continu (ou CI/CD) repose sur une automatisation des processus.  
Les opérations de CI/CD sont paramétrées pour être mises en oeuvre lorsque certaines conditions sont réunies, généralement l'envoi sur GitHub d'une nouvelle version de l'application.  
Cela suppose donc une liaison de votre repository GitHub à votre compte CircleCI.  

#### Préparation du dépôt GitHub

- Créez un dépôt GitHub dédié au projet
- Localement, récupérez les scripts du projet : `git pull git@github.com:Olrio/P13.git`  
- Créez et activez un environnement virtuel `venv` (conserver ce nom qui est utilisé dans les fichiers *.ignore* et *.setup*)  
  `python -m venv venv` puis `source venv/bin/activate`  
- Pour une utilisation locale, copiez à la racine de votre projet le fichier `.env` qui vous a été fourni par ailleurs et qui contient la clé de sécurité nécessaire au fonctionnement de cette application Django. Ce fichier `.env` ne doit pas être publié sur GitHub.  
- Installez les packages requis : `pip install -r requirements.txt`  
- Vous pouvez vérifier que votre installation est fonctionnelle en lançant l'application `python manage.py runserver` et en ouvrant un navigateur    à la page `http://127.0.0.1:8000/`  
- Poussez le projet dans votre dépôt GitHub  

#### Connexion de CircleCI à votre dépôt GitHub

- Connectez-vous à votre compte *CircleCI*  
- Dans la page *Projects* de *CircleCI*, localisez votre compte GitHub et votre projet qui héberge le code de *Orange County Lettings*.  
- Cliquez sur *Set-Up Project*, choisissez *fastest* et validez la branche principale (*main* ou *master*).  

Le pipeline d'intégration continue se lance automatiquement et devrait échouer car à ce stade vous n'avez pas encore configuré *Docker* et *Heroku*.  
Notez que si vous consultez votre projet sur votre dépôt GitHub, vous constatez la présence d'une croix rouge à côté du nom du dernier commit. En cliquant sur cette croix, vous retrouvez les informations sur les jobs CircleCI effectués.  

Votre liaison GitHub/CircleCI est néanmoins désormais fonctionnelle.  

### Création de l'image Docker via le pipeline CircleCI  

Vous devez fournir à CircleCI votre identifiant et votre mot de passe DockerHub afin que le processus de création et publication d'images Docker via le pipeline s'effectue correctement.  

Pour ce faire, choisissez *Projects* dans le menu de gauche, cliquez sur le nom de votre projet puis sur *Project Settings* à la droite de votre écran.  

Sur la page des Settings de votre projet, choisissez *Environment variables* dans le menu de gauche.  

Cliquez sur *Add Environment Variable*.  

Saisissez `DOCKERHUB_USER` dans le champ *Name* et votre nom d'utilisateur DockerHub dans le champ *Value*.  
Renouvelez l'opération pour la variable `DOCKERHUB_PASS` qui contient votre mot de passe pour vous connecter à votre compte DockerHub.  
Ajoutez une troisième variable d'environnement, `DOCKERHUB_REPO`, qui correspond au nom de votre dépôt DockerHub (sans le préfixe 'username /').  

Enfin, créez la variable d'environnement `DJANGO_SECRET_KEY` qui contient la clé de sécurité de l'application Django. Sa valeur figure dans le fichier `.env` qui vous a été communiqué mais qui ne doit pas être publié sur GitHub.  


**Remarque :** Veillez à bien respecter le nom des variables d'environnement (DOCKERHUB_USER, DOCKERHUB_PASS, DOCKERHUB_REPO et DJANGO_SECRET_KEY) pour un fonctionnement correct du pipeline CI/CD.

Une fois l'image de votre application créée et envoyée sur Docker Hub, vous pouvez vérifier que le processus s'est correctement déroulé en entrant la commande suivante dans votre terminal : `docker pull <your DockerHub username>/<your DockerHub repo>:latest && docker run -p 8000:8000 <your DockerHub username>/<your DockerHub repo>:latest`

### Déploiement sur Heroku  

#### Création de l'application sur Heroku

Dans un terminal : 
- connectez-vous à Heroku avec la commande `heroku login`  
- votre navigateur internet ouvre une page et vous devez cliquer sur *login*. Fournissez votre adresse email et votre mot de passe pour vous identifier sur Heroku.  
- revenez à votre terminal qui devrait afficher : *Logging in... done Logged in as my email*  
- saisissez `heroku create <app_name>`, app_name étant le nom de votre application déployée sur Heroku.  

#### Configuration du pipeline CI/CD

Le fichier *config.yml* de CircleCI gère l'interaction avec Heroku au moyen de variables d'environnement.  
Dans l'onglet *Environment Variables* de votre projet CircleCI, ajoutez la variable `HEROKU_APP_NAME` qui prend comme valeur le nom de l'application app_name que vous venez de créer sur Heroku.  
A des fins de sécurisation, vous devrez également ajouter une variable `HEROKU_API_KEY` dont la valeur est votre API_KEY que vous pouvez récupérer sur la page *Account* de votre compte Heroku.  


La configuration de votre pipeline CI/CD est désormais terminée et il sera mis en oeuvre lorsque du nouveau contenu sera poussé sur votre dépôt GitHub.  

**Remarque 1 :** La conteneurisation Docker et le déploiement sur Heroku ne concernent que le contenu de la branche *master* de votre projet.  Si votre branche principale est une branche *main*, vous devrez, soit la renommer en *master*, soit modifier le fichier *config.yml* et remplacer à la ligne 71 `master:master` par `main:master`.  

**Remarque 2 :** Il est fortement recommandé de ne pas permettre de pousser du nouveau contenu directement sur la branche principale de votre dépôt GitHub. Utilisez une branche accessoire pour l'ajout de tout nouveau contenu puis poussez ce contenu dans une branche accessoire correspondante sur GitHub et effectuez une pull request pour intégrer le contenu à votre branche principale.  

### Utilisation de Sentry

L'application utilise *Sentry* pour la journalisation des évènements.

Il vous faut donc bénéficier d'un compte Sentry ou en créer un à défaut.  

- Connectez-vous à votre compte *Sentry*
- Créez un Projet dédié à l'application *Orange County Lettings*  
- Rendez-vous à l'onglet *Project Details* de votre Projet et sélectionnez les *Settings* en haut à droite (roue crantée).  
- Choisissez *Client Keys (DSN)* dans le menu à gauche  
- Copiez la valeur de la clé DSN
- Rendez-vous dans l'onglet *Environment Variables* des Settings de votre projet sur *CircleCI*  
- Ajoutez une variable `SENTRY_DSN` dont la valeur est la clé DSN que vous venez de copier.  

Votre pipeline CI/CD est maintenant relié à Sentry et lui transmet les erreurs survenues.

