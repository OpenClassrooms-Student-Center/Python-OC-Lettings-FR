Installation
============

Prérequis
---------

- Python 3.11+
- Git
- PostgreSQL (pour production)
- Docker Desktop

Installation locale
-------------------

.. code-block:: bash

    git clone https://github.com/TON_USERNAME/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

Configuration du fichier .env
-----------------------------

Crée un fichier `.env` à la racine du projet :

.. code-block:: env

    SECRET_KEY=ta_clé_secrète_django
    DEBUG=True
    SENTRY_DSN=ta_dsn_sentry_optionnelle

Lancer le serveur de développement
-----------------------------------

.. code-block:: bash

    python manage.py migrate
    python manage.py runserver
