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

Ce projet utilise GitHub Actions pour automatiser le déploiement de l'application sur ECS

#### Fonctionnement du déploiement

1. Lorsqu'un push est créé sur n'importe quelle branche, les jobs suivants sont déclenchées :
  - compilations_and_tests : compile et teste le code.
2. Lorsqu'une pull request est créée sur la branche master, les jobs suivants sont déclenchés :
  - compilations_and_tests : compile et teste le code.
  - containerization_and_push : construit une image Docker, puis la pousse vers ECR et DockerHub.
  - build : met à jour la tâche ECS avec la nouvelle image Docker et déploie l'application mise à jour.

#### Configuration requise

Pour que le déploiement fonctionne correctement, vous devez disposer des éléments suivants :

1. Un compte AWS avec les autorisations pour Amazon ECS et Amazon ECR.
2. Un compte Docker Hub pour stocker les images Docker.
3. Les secrets GitHub :
- AWS_ACCESS_KEY_ID : votre clé d'accès AWS.
- AWS_SECRET_ACCESS_KEY : votre clé secrète AWS. 
- ECR_URL_REPOSITORY: l'url' de votre repository sur ECR.
- AWS_REGION: la region associé a votre compte AWS.
- DOCKERHUB_PASSWORD : le mot de passe de votre compte Docker Hub.
- DOCKERHUB_USERNAME : l'identifiant de votre compte Docker Hub.
4. Un cluster Amazon ECS avec un service comprenant la définition de tâche lettings-oc-docker.

#### Étapes de déploiement

1. Assurez-vous davoir la configuration requise.
2. Créez une nouvelle branche à partir de la branche main.
3. Apportez les modifications souhaitées au code et validez-les dans votre nouvelle branche.
4. Créez une pull request à partir de votre branche vers la branche master.
5. Attendez que les GitHub Actions se terminent et vérifiez que le déploiement a réussi.
6. Une fois le déploiement réussi, vous pouvez fusionner la pull request dans la branche main.

#### Commande unique de déploiement
Pour déployer votre site en une seule commande, suivez les étapes suivantes :

1. Assurez-vous de vous trouver dans le dossier racine du projet.
2. Assurez-vous de posséder un compte Docker Hub.
3. Tapez la commande suivante dans le terminal : `./deploy.sh`

Cette commande construira une image Docker de votre site avec le tag du hash du commit actuel, la poussera vers votre compte Docker Hub et la tirera localement pour que vous puissiez exécuter le site en utilisant l'image Docker.

Vous disposez maintenant dans votre Docker Hub et localement de l'image de votre site actuel.