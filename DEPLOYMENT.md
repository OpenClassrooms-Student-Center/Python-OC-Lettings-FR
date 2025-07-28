# Guide de Déploiement - OC Lettings Site

## Prérequis

- Docker et Docker Compose installés
- Compte DockerHub
- Compte Render (pour le déploiement)
- Variables d'environnement configurées

## Configuration des Variables d'Environnement

### GitHub Secrets (pour la CI/CD)

Configurez ces secrets dans votre repository GitHub :

- `DOCKER_USERNAME` : Votre nom d'utilisateur DockerHub
- `DOCKER_PASSWORD` : Votre token d'accès DockerHub
- `RENDER_TOKEN` : Votre token d'API Render
- `RENDER_SERVICE_ID` : L'ID de votre service Render

### Variables d'Environnement pour la Production

- `SECRET_KEY` : Clé secrète Django (générée automatiquement si non définie)
- `DEBUG` : `False` pour la production
- `ALLOWED_HOSTS` : Liste des domaines autorisés (séparés par des virgules)
- `DATABASE_URL` : URL de la base de données (optionnel, SQLite par défaut)
- `SENTRY_DSN` : URL Sentry pour le monitoring (optionnel)

## Test Local avec Docker

### 1. Build de l'image Docker

```bash
docker build -t oc-lettings-site .
```

### 2. Test avec Docker Compose

```bash
# Démarrer l'application
docker-compose up web

# Exécuter les tests
docker-compose run test
```

### 3. Test direct de l'image

```bash
# Démarrer le conteneur
docker run -p 8000:8000 oc-lettings-site

# Accéder à l'application
open http://localhost:8000
```

## Pipeline CI/CD

La pipeline GitHub Actions s'exécute automatiquement sur chaque push vers `main` :

1. **Tests** : Vérification de la qualité du code et couverture des tests (>80%)
2. **Test Docker** : Vérification que l'image Docker fonctionne
3. **Build & Push** : Construction et publication de l'image sur DockerHub
4. **Déploiement** : Déploiement automatique sur Render

## Déploiement sur Render

### Configuration du Service

1. Créez un nouveau service Web sur Render
2. Connectez votre repository GitHub
3. Configurez les variables d'environnement :
   - `DOCKER_IMAGE` : `votre-username/oc-lettings-site`
   - `SECRET_KEY` : Clé secrète Django
   - `DEBUG` : `False`
   - `ALLOWED_HOSTS` : Votre domaine Render

### Désactivation du Déploiement Automatique

⚠️ **Important** : Désactivez le déploiement automatique sur Render car la CI/CD GitHub Actions gère le déploiement.

## Structure des Fichiers

```
├── Dockerfile                 # Configuration Docker
├── docker-compose.yml         # Configuration Docker Compose
├── start.sh                   # Script de démarrage
├── requirements.txt           # Dépendances Python
├── .dockerignore             # Fichiers exclus de Docker
├── oc_lettings_site/
│   ├── settings.py           # Configuration développement
│   └── settings_production.py # Configuration production
└── .github/workflows/
    └── ci-cd.yml             # Pipeline CI/CD
```

## Sécurité

- Utilisateur non-root dans le conteneur
- Variables d'environnement pour les secrets
- Configuration de sécurité Django pour la production
- Headers de sécurité configurés

## Monitoring

- Logs structurés avec Django
- Intégration Sentry (optionnelle)
- Métriques de couverture de tests

## Troubleshooting

### Problèmes Courants

1. **Erreur de permissions** : Vérifiez que `start.sh` est exécutable
2. **Fichiers statiques manquants** : Vérifiez la configuration WhiteNoise
3. **Base de données** : Vérifiez les variables d'environnement DATABASE_URL

### Logs

```bash
# Voir les logs du conteneur
docker logs <container-id>

# Logs en temps réel
docker logs -f <container-id>
``` 