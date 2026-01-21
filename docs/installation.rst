Installation
============

There are two ways to run this project: local development or using Docker.

Quick Start - Local Development
--------------------------------

For experienced developers:

.. code-block:: bash

   git clone https://github.com/Faaab84/Python-OC-Lettings-FR
   cd P13_Mettez_echelle_application_django_architecture_modulaire
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

