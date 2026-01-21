Installation
============

There are two ways to run this project: local development or using Docker.

Quick Start - Local Development
--------------------------------

For experienced developers:

    Les variables d'environnement suivantes peuvent être configurées pour modifier le comportement du projet en local :
    Créer un fichier .env avec les informations :

  `DEBUG=False` : désactive le mode debug de Django.
  `SECRET_KEY=<votre_clé_secrète>` : Clé secrète utilisée par Django. Par défaut, une clé de développement est utilisée.
  `SENTRY_DSN=<votre_dsn_sentry>` : DSN pour Sentry. Par défaut, aucune valeur n'est définie.
  `ALLOWED_HOSTS=<"">` :ALLOWED_HOSTS (127.0.0.1,localhost,0.0.0.0,oc-lettings-site-latest-05t2.onrender.com)

.. code-block:: bash

   git clone https://github.com/Faaab84/Python-OC-Lettings-FR
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver

The application will be available at http://127.0.0.1:8000/


Quick Start - Docker
--------------------

Pull and run the pre-built Docker image:

.. code-block:: bash

   docker pull faaab68/oc-lettings-site:latest
   docker run -p 8000:8000 faaab68/oc-lettings-site:latest

The application will be available at http://127.0.0.1:8000/

.. note::
   The Docker image runs with production settings (gunicorn + WhiteNoise).


Detailed Instructions
---------------------

For complete installation guide, configuration options, and environment variables, see the 
`project README on GitHub <https://github.com/Faaab84/Python-OC-Lettings-FR>`_.

