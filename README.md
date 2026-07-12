# Orange County Lettings 

## Présentation du projet 

Orange County Lettings est une application web développée avec Django pour une start-up spécialisée dans la location de biens immobiliers aux États-Unis.

Ce projet a consisté à améliorer une application existante en la restructurant autour d'une architecture Django modulaire et en mettant en place une chaîne d'intégration et de déploiement continus (CI/CD).

La documentation complète du projet est disponible ici : 

## Fonctionnalités

L'application permet de consulter les principales informations du service Orange County Lettings à travers une interface web développée avec Django.

Les fonctionnalités disponibles sont les suivantes :

- consultation des annonces immobilières ;
- consultation des profils utilisateurs ;
- accès à l'interface d'administration Django pour la gestion des données.

## Architecture

Le projet est organisé selon une architecture Django modulaire composée de trois applications principales :

- **oc_lettings_site** : configuration générale du projet (settings, routage, serveur WSGI) ;
- **lettings** : gestion des annonces immobilières ;
- **profiles** : gestion des profils utilisateurs.

Cette organisation permet de séparer les responsabilités de chaque composant et facilite la maintenance ainsi que l'évolution de l'application.

L'application est conteneurisée avec Docker et déployée automatiquement via une pipeline CI/CD sur la plateforme Render.

Pour une description détaillée de l'architecture, du déploiement et de l'infrastructure, consultez la documentation complète du projet.

## Stack technique

Le projet s'appuie sur les technologies suivantes :

- **Langage :** Python 3.10
- **Framework :** Django 3.0
- **Bases de données :** SQLite (développement rapide), PostgreSQL (Docker et production)
- **Conteneurisation :** Docker, Docker Compose
- **CI/CD :** GitHub Actions
- **Tests et qualité :** pytest, pytest-django, coverage, flake8, black
- **Monitoring :** Sentry
- **Production :** Gunicorn, WhiteNoise, Render
- **Configuration :** python-dotenv

## Utilisation en local

### Prérequis

Pour exécuter le projet localement, les outils suivants sont nécessaires :

- Git ;
- Python 3.10 ou supérieur ;
- Docker et Docker Compose (optionnel, pour une exécution conteneurisée).

### Installation

Clonez le dépôt puis installez les dépendances dans un environnement virtuel :

```bash
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR

python -m venv venv
source venv/bin/activate    # Linux / macOS
# ou
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

Créez ensuite un fichier .env à la racine du projet et renseignez les variables d'environnement nécessaires.

### Lancement de l'application

#### Avec Django

```bash
python manage.py migrate
python manage.py runserver
```

#### Avec Docker Compose

```bash
docker compose up --build
```

L'application est ensuite accessible à l'adresse :

http://localhost:8000

Pour plus d'informations sur la configuration de l'environnement, les variables d'environnement ou l'utilisation de Docker Compose, consultez la documentation complète.

## Tests et qualité du code

Les principaux outils de qualité peuvent être exécutés depuis la racine du projet :

```bash
flake8        # Analyse statique
pytest        # Tests unitaires
pytest --cov  # Couverture des tests
```

Ces vérifications sont également exécutées automatiquement par la pipeline CI/CD à chaque `push` et à chaque Pull Request.

## Pipeline CI/CD

Le projet utilise une pipeline GitHub Actions pour automatiser les contrôles qualité, la construction de l'image Docker et le déploiement en production.

```text
Push / Pull Request
        │
        ▼
GitHub Actions
        │
        ▼
Job "compile"
        │
        ├── Installation des dépendances
        ├── Analyse statique (flake8)
        └── Tests unitaires + couverture
        │
        └──────────────► Validation réussie
                          │
                          ▼
                 (push sur master uniquement)
                          │
                          ▼
                 Job "containerize"
                          │
                          ├── Build Docker
                          ├── Tag SHA
                          ├── Tag latest
                          └── Push DockerHub
                          │
                          ▼
                    Job "deploy"
                          │
                          ▼
                         Render
```

Les informations sensibles utilisées par la pipeline sont stockées dans les **GitHub Actions Secrets** et ne sont jamais versionnées dans le dépôt.

## Déploiement

L'application est déployée automatiquement sur **Render** à partir de la pipeline GitHub Actions.

Lorsqu'un changement est fusionné sur la branche `master`, la pipeline :

1. construit une image Docker ;
2. publie cette image sur Docker Hub ;
3. déclenche le déploiement sur Render via un Deploy Hook.

Au démarrage du conteneur, le script `start.sh` applique automatiquement les migrations Django avant de lancer le serveur Gunicorn.

L'application s'exécute en production avec une base de données PostgreSQL managée par Render. L'ensemble de la configuration est assuré au moyen de variables d'environnement et le service est vérifié automatiquement par le mécanisme de **Health Check** de Render.

## Autres commandes utiles

### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Liens utiles

Les documentations officielles suivantes permettent d'approfondir les technologies utilisées dans ce projet :

- GitHub : https://docs.github.com/fr
- Docker : https://docs.docker.com/
- GitHub Actions : https://docs.github.com/fr/actions
- Render : https://render.com/docs

## Auteur

Jérémy Muller, étudiant en développement applicatif python chez OpenClassrooms.

GitHub : https://github.com/Jeremuller/
