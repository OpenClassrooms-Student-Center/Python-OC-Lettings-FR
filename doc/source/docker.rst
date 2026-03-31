Docker
======

Construire l'image Docker
--------------------------

.. code-block:: bash

    docker build -t oc-lettings:local .

Tester en local
---------------

.. code-block:: bash

    docker run -p 8000:8000 \
      -e SECRET_KEY="test-key" \
      -e DEBUG=False \
      -e SENTRY_DSN="" \
      oc-lettings:local

Ensuite accède à http://localhost:8000

Pousser vers Docker Hub
-----------------------

.. code-block:: bash

    docker login
    docker push TON_USERNAME/oc-lettings:latest
