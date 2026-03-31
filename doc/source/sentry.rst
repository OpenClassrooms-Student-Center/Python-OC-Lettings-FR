Sentry
======

Configuration
-------------

1. Crée un compte sur https://sentry.io
2. Crée un nouveau projet Django
3. Copie le DSN fourni
4. Ajoute le DSN dans ton fichier `.env` :

.. code-block:: env

    SENTRY_DSN=https://...ton_dsn_sentry...

Tester l'intégration
--------------------

Lance cette commande pour vérifier que Sentry capture les erreurs :

.. code-block:: bash

    python manage.py runserver
