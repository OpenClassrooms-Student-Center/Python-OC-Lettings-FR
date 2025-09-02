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

### Fichier .env
Le projet utilise un fichier `.env` pour centraliser les variables d'environnement sensibles.

Créez un fichier `.env` à la racine du projet avec comme variable:
  - SECRET_KEY
  - SENTRY_DSN
  - SECRET_DEPLOY_HOOK

Ne pas commit ce fichier dans Git, il doit être listé dans le `.gitignore`


### Docker

L'application dispose d'un `Dockerfile` pour créer une image Docker exécutable:
commande pour la création de l'image `docker build -t oc-lettings .`

Pour la partie CI/CD:
- Créer un compte docker sur Docker Hub (https://hub.docker.com/)
- Configurer vos identifiants dans les **secrets GitHub**:
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`(sous forme de token)

### CI/CD:

Un pipeline GitHub a été ajouté, déclenché à chaque push.
Il execute automatiquement les étapes suivantes:

- Lint avec `flake8`
- Tests unitaires avec `pytest`
- Build Docker
- Push vers Docker Hub
- Génération de la documentation


### Documentation 

La documentation technique est générée avec **Sphinx** et hebergée sur **Read the Docs**:

Créer sa propre doc 

1. Créer un compte sur https://readthedocs.org
2. Connecter votre repo GitHub
3. Importer le projet 
4. S'assurer que `.readthedocs.yml` est présent à la racine
5. Déclencher un build 

### Sentry

Étapes pour intégrer Sentry:

  1. Créer un compte sur https://sentry.io 
  2. Créer un projet Django
  3. Copier la clé DSN dans votre environnement de variable (.env)
  4. Ajouter le bloc de code de sentry générée dans sentry et la Clé DSN dans `oc_lettings_site/settings.py`


### Déploiement 

Render est connecté à Docker Hub pour tirer l'image automatiquement.

**Étapes pour configurer**

1. Créer un compte render (https://render.com)
2. Créer un Web service
3. Indiquer l'image Docker :
``` 
  docker.io/nom utilisateur/nom de l'application

```
4. Déploiement automatique à chaque image pushée

Exemple de lien de production :
  https://oc-lettings.onrender.com




