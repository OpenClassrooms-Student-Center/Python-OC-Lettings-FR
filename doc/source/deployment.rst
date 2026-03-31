Déploiement
===========

Déployer sur Render
-------------------

1. Crée un compte sur https://render.com
2. Connecte ton repo GitHub
3. Crée un nouveau "Web Service"
4. Sélectionne le repo "Python-OC-Lettings-FR"
5. Configure les variables d'environnement :

   - `SECRET_KEY` : ta clé Django
   - `DEBUG` : False
   - `SENTRY_DSN` : ta DSN Sentry

6. Lance le déploiement

L'URL publique sera fournie par Render.
