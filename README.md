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

Pour générer le rapport de couverture:
- `coverage run --source='.' manage.py test`
- `coverage report`


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
### Récapitulatif Haut Niveau du Fonctionnement du Déploiement

Notre pipeline CI/CD automatise le processus de déploiement en suivant ces étapes clés :

#### Compilation et Tests
Lors de chaque push, les modifications sont d'abord soumises à une phase de compilation et de tests. Cela assure que le code est fonctionnel, respecte les normes de codage et que la couverture des tests est supérieure à 80 %.

#### Conteneurisation
Si les tests réussissent et que le push est fait sur la branche master, une image Docker est construite, taguée avec le hash du commit et poussée vers le Docker Hub.

#### Déploiement en Production 
Lorsqu'une mise à jour est poussée sur la branche master, l'image Docker est récupérée et déployée automatiquement sur notre serveur Render pour mettre à jour le site en production.


### Configuration Requise
Pour que le déploiement fonctionne correctement, assurez-vous que Docker et Docker Compose soient bien installés sur votre machine.

### Mise en production
Pour mettre en production en utilisant le pipeline CI/CD, deux ooptions s'offrent à vous :
#### 1. Pousser des Modifications sur master
Commitez vos Modifications : Ajoutez et commitez vos modifications localement.

<code>
git add . <br>
git commit -m "Description des modifications"</code>
<br><br>
Pousser sur master : Envoyez vos commits sur la branche master du dépôt distant.

<code>git push origin master</code>

#### 2. Fusionner dans master (si applicable)
Si vous travaillez sur une branche de fonctionnalité ou de correctif et que vous souhaitez fusionner ces changements dans master :

Créez une Pull Request : Créez une Pull Request (PR) dans GitHub depuis votre branche de fonctionnalité vers master.

Revue de Code : Une fois la PR approuvée, fusionnez la PR dans master. 

#### Tester En Ligne (Optionnel)
Visitez le site à l'url suivante pour vérifier que tout est en ordre:<br>
https://ocr-p13.onrender.com/

#### Tester Localement (Optionnel)

Pour tester localement avant le déploiement, vous pouvez récupérer l'image Docker depuis Docker Hub et lancer un conteneur localement (remplacer commit_hash par le hash du dernier commit):

<code>
docker login <br>
docker pull clementboloch/ocr_p13:latest <br>
docker run -d -p 8000:8000 clementboloch/ocr_p13:latest
</code>

Accédez à http://localhost:8000 dans votre navigateur pour voir l'application.