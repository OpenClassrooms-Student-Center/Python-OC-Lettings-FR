Configuration
==============

Variables d'environnement
-------------------------

Fichier `.env` à la racine du projet :

- `SECRET_KEY` : Clé secrète Django (ne pas commiter)
- `DEBUG` : `True` en développement, `False` en production
- `SENTRY_DSN` : DSN pour l'intégration Sentry (optionnel)

Base de données
---------------

Le projet utilise SQLite en développement et PostgreSQL en production.

Sentry
------

Pour activer Sentry, définis la variable `SENTRY_DSN` dans `.env`.
