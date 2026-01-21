# Site web d'Orange County Lettings

Ce repository contient le code source du site web d'Orange County Lettings, un site de location immobilière fictif développé dans le cadre du parcours "Développeur d'application - Python" d'OpenClassrooms.

Ce site web permet aux utilisateurs de consulter des profils de propriétaires et des annonces de locations immobilières. Il est construit avec le framework web Django et utilise une base de données SQLite pour stocker les informations.

## Architecture du projet

Le projet est structuré de la manière suivante :

- `oc_lettings_site/` : Dossier principal du projet Django. Contient les fichiers de configuration principaux du projet Django.
- `lettings/` : Application Django gérant les annonces de locations.
- `profiles/` : Application Django gérant les profils des propriétaires.
- `static/` : Contient les fichiers statiques (CSS, JavaScript, images).
- `templates/` : Contient les templates HTML utilisés pour rendre les pages web (accueil sur le site et pages 404 et 500, les autres templates sont intégrés dans les apps correspondantes).
- `oc-lettings-site.sqlite3` : Fichier de base de données SQLite.

## Documentation complète

La documentation détaillée du projet (architecture modulaire, schémas, description des apps, guides techniques, CI/CD, Sentry, etc.) est disponible sur ReadTheDocs :

https://python-oc-lettings-fr100.readthedocs.io/en/latest/installation.html#quick-start-local-development

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
- `pytest --cov --cov-fail-under=80`

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



### Configuration

Les variables d'environnement suivantes peuvent être configurées pour modifier le comportement du projet en local :
Créer un fichier .env avec les informations : 

- `DEBUG=False` : désactive le mode debug de Django.
- `SECRET_KEY=<votre_clé_secrète>` : Clé secrète utilisée par Django. Par défaut, une clé de développement est utilisée.
- `SENTRY_DSN=<votre_dsn_sentry>` : DSN pour Sentry. Par défaut, aucune valeur n'est définie.
- `ALLOWED_HOSTS=<"">` :ALLOWED_HOSTS (127.0.0.1,localhost,0.0.0.0,oc-lettings-site-latest-05t2.onrender.com)

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Vue d'ensemble

Le projet utilise un pipeline CI/CD automatisé via **GitHub Actions** pour déployer l'application en production sur **Render** :

1. **Validation du code** : Exécution automatique des tests (pytest avec couverture ≥ 80%) et vérification de la qualité du code (flake8)
2. **Containerisation** : Construction de l'image Docker et publication sur DockerHub
3. **Déploiement automatique** : Render détecte la nouvelle image et redémarre l'application
4. **Monitoring** : Sentry surveille les erreurs et performances en production

**Schéma du pipeline CI/CD** :

Le déploiement automatique se déclenche uniquement sur les pushs ou des merge vers la branche `master` après validation réussie des tests et du linting.

Pour chaque push sur des branches autres que `master`, une vérification des tests et du linting ainsi qu'un build Docker sont effectués et l'image est poussée sur DockerHub avec le tag du `sha du commit` + le tag `latest`, mais sans déploiement automatique.

---

### Prérequis

Pour effectuer un déploiement, les comptes et outils suivants sont nécessaires :

#### Comptes requis

- **GitHub** : Repository du projet avec GitHub Actions activé
- **DockerHub** : Registry pour stocker les images Docker
- **Render** : Plateforme d'hébergement pour l'application en production
- **Sentry** (optionnel) : Service de monitoring des erreurs

#### Conteneur local (pour tests manuels)

- Docker installé et configuré
- Accès SSH au repository GitHub
- CLI Docker connectée à DockerHub (pour pushs manuels d'images)

---

### Marche à suivre pour le déploiement initial

#### 1. Configuration DockerHub

1. Créer un compte sur [hub.docker.com](https://hub.docker.com)
2. Créer un repository public : `votre-username/oc-lettings-site`
3. Générer un Access Token :
   - Aller dans **Account Settings** → **Security** → **New Access Token**
   - Nom : `github-actions-token`
   - Permissions : **Read, Write, Delete**
   - Copier le token généré (il ne sera affiché qu'une seule fois)

#### 2. Configuration Render

1. Créer un compte sur [render.com](https://render.com)
2. Créer un nouveau **Web Service** :
   - **Type** : Docker
   - **Docker Image URL** : `votre-username/oc-lettings-site:latest`
   - **Region** : Choisir la région la plus proche
   - **Instance Type** : Free
3. Configurer les variables d'environnement dans Render :

   `SECRET_KEY`=<générer une clé secrète Django ou modifier celle du projet pour la production>
   `SENTRY_DSN`=<votre DSN Sentry>

4. Récupérer le **Deploy Hook URL** :
   - Aller dans **Settings** → **Deploy Hook**
   - Copier l'URL (format : `https://api.render.com/deploy/srv-xxxxx?key=yyyyy`)

#### 3. Configuration des GitHub Secrets

Ajouter les secrets suivants dans le repository GitHub (**Settings** → **Secrets and variables** → **Actions** → **New repository secret**) :

- `DOCKERHUB_TOKEN` : Token d'accès DockerHub
- `DOCKERHUB_USERNAME` : Nom d'utilisateur DockerHub
- `RENDER_DEPLOY_HOOK_URL` : URL du webhook Render

### Processus de déploiement

#### Déploiement automatique (recommandé)

Le déploiement est entièrement automatisé via GitHub Actions :

1. **Développer et tester localement** :
   Au préalable, tirer une branche depuis `master`, effectuer les modifications, puis exécuter les tests et le linting localement :

   ```bash
   pytest --cov --cov-fail-under=80
   flake8
   ```

2. **Pousser sur la branche actuelle** :

   ```bash
   git add .
   git commit -m "Description des modifications"
   git push
   ```

3. **Le pipeline s'exécute automatiquement** :

   - ✅ Tests unitaires (pytest avec couverture 80%)
   - ✅ Linting (flake8)

4. **Merge request sur la branche master** :

   Une fois fait, il faut merger la branche dans `master` via une pull request sur GitHub.

5. **Le pipeline s'exécute automatiquement** :
   Après le merge, le pipeline s'exécute automatiquement :

   - ✅ Tests unitaires (pytest avec couverture 80%)
   - ✅ Linting (flake8)
   - ✅ Build de l'image Docker
   - ✅ Push vers DockerHub (`latest` + tag avec SHA du commit)
   - ✅ Déclenchement du déploiement Render via webhook

6. **Vérifier le déploiement** :
   - Consulter les logs dans l'onglet **Actions** de GitHub
   - Vérifier le statut sur le dashboard Render
   - Accéder à l'application déployée : `https://votre-app.onrender.com`

---