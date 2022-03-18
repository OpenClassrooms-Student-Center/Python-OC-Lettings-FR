## Résumé

Site web d'Orange County Lettings

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

### Déploiement

#### Vue d'ensemble
Le déploiement de l'application est géré par un pipeline CircleCI. Chaque modification poussée sur le registre Github déclenche le test et le linting de la nouvelle version du code. Cependant, seules les modifications apportées à la branche master entraîneront un déploiement sur Docker, puis sur Heroku.

Le déploiement s'appuie sur les fichiers .circleci/config.yml et Dockerfile. Il se fait en plusieurs étapes (test/linting, conteneurisation, déploiement Sentry, déploiement sur Heroku); si l'une échoue, les suivantes ne seront pas exécutées.

#### Prérequis
- Un compte CircleCI
- Un compte Dockerhub (avec un dépôt)
- Un compte Heroku (avec une application)
- Un compte Sentry (avec un projet)

### Mise en place
Tout d'abord, clonez le dépôt Github. Après cela, rendez-vous sur votre compte CircleCI, cliquez sur le bouton "Ajoutez un projet" et suivez les instructions afin de lier votre nouveau dépôt à CircleCI. N'acceptez pas que CircleCI génère automatiquement un fichier config.yml pour vous (vous en avez déjà un).

**Votre dépôt Github est maintenant lié à votre propre pipeline CircleCI.** Nous allons maintenant le lier à votre compte Docker.

Rendez-vous dans le fichier ".circleci/config.yml" et remplacez "lgarrigoux/oc_lettings" par le nom de votre dépôt DockerHub, puis "oc-lettings-9" par le nom de  votre application Heroku.

Rendez-vous également dans les paramètres de votre application CircleCI et ajoutez les variables d'environnement suivantes :

- DOCKER_USER (votre nom d'utilisateur Docker),
- DOCKER_PASS (le mot de passe correspondant),
- HEROKU_TOKEN (le token associé à votre application Heroku, trouvable dans les paramètres de l'application"),
- SENTRY_AUTH_TOKEN (le token associé à votre compte Sentry),
- SENTRY_DNS (le DNS de votre projet Sentry),
- SENTRY_ORG et SENTRY_PROJECT (les noms de votre organisation et de votre project Sentry).

**Votre pipeline CircleCI est maintenant lié à votre conteneur Docker, à votre projet Sentry et à votre application Heroku.**

Rendez-vous maintenant sur la page Settings de votre projet Heroku et créez les Configs Vars suivantes : DEBUG et SECRET_KEY. DEBUG sera False et SECRET_KEY sera notre clef secrète Django.

**Pour vérifier que votre application est bien surveillée par Sentry**, naviguez vers l'URL "/sentry-debug/". Un nouvel événement s'affichera sur la page Issues de votre projet Sentry.

Votre déploiement est maintenant mis en place.
