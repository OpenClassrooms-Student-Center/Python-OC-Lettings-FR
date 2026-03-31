## Résumé

Site web d'Orange County Lettings (projet Django modulaires : applications `home`, `lettings`, `profiles`).

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository.
- Git CLI.
- SQLite3 CLI.
- Interpréteur Python, version 3.11 ou supérieure.
- (Optionnel) Docker Desktop si vous souhaitez utiliser l’exécution via conteneur.

Dans le reste de la documentation sur le développement local sans Docker, 
il est supposé que la commande `python` de votre OS shell exécute l'interpréteur 
Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux (sans Docker)

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone <URL DE VOTRE FORK>`
- `cd Python-OC-Lettings-FR`

#### Créer l'environnement virtuel

- `python -m venv venv`
- `apt-get install python3-venv` (si l'étape précédente échoue avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement : `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel :  
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.11 ou supérieure :  
  `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel :  
  `which pip`
- Pour désactiver l'environnement : `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer 
   (vous devriez voir plusieurs profils et locations via les applications`lettings` et `profiles`).

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
- Se connecter à la base de données :  
  `.open test_db.sqlite3`
- Afficher les tables dans la base de données :  
  `.tables`
- Afficher les colonnes dans la table des profils :  
  `pragma table_info(oc_lettings_site_profile);`  *(adapter au nom réel de la table si différent)*
- Lancer une requête sur la table des profils, par exemple :  
  `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `user`, mot de passe `Abc1234!` (ou les identifiants définis dans vos fixtures / données locales).

### Exécution avec Docker (optionnel)

Si vous utilisez Docker :

- Construire l’image :  
  `docker build -t oc-lettings:local .`
- Lancer le conteneur :  
  `docker run -p 8000:8000 -e SECRET_KEY="test_key" -e DEBUG=False oc-lettings:local`
- Aller sur `http://localhost:8000` dans un navigateur.

*(Adapter cette section si vous utilisez `docker-compose` et un volume pour la base SQLite.)*

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel :  
  `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par :  
  `(Get-Command <my-command>).Path`
