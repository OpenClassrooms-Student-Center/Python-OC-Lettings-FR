==================================
Development and deployment Process
==================================

Run the site locally with Django
---------------------------------

 - start virtual environnement [1]_
 - python manage.py collectstatic
 - python manage.py runserver
 - goto http://localhost:8000 with your browser
 - goto http://localhost:8000/admin to access the admin panel
 you can connect with user admin and mot de passe Abc1234!
 - goto http://localhost:8000/sentry-debug/ to generate a ZeroDivisionError and verify your Sentry account


Run the site locally via Docker
-------------------------------

 - create a dockerhub account
 - install docker desktop
 - retrieve the docker image to run the application locally : docker pull slb59/lettings
 - make sure the local server is not running
 - launch the server : docker compose -f compose/docker-compose.yml up -d
 - the site should work the same way with the same urls, as if using the local procedure
 - To shut down the server without deleting the created resources: docker compose stop, and to stop it by destroying all the resources created: docker compose down

.. [1] by setting the DEBUG variable in the .env file to true, you can view the debug-toolbar

quality control
---------------

Linting
^^^^^^^

- activate the virtual environment
- Flake8 is a wrapper around these tools:

    - PyFlakes
    - pycodestyle
    - Ned Batchelder’s McCabe script

    .. code-block:: shell
       
       flake8

- isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type
    .. code-block:: shell
       
       isort . --check

- black is the uncompromising Python code formatter.
    .. code-block:: shell
    
       black . --check

- pylint is a static code analyser for Python 2 or 3.
    .. code-block:: shell
        
       pylint . --recursive=y > logs/pylint.txt
    
    then you can check the logs/pylint.txt file

- pytest framework makes it easy to write unit tests
    .. code-block:: shell
        
       pytest

    You can check the tests coverage with:
    .. code-block:: shell
    
       pytest --cov=. --cov-report=html

    then check the result in htmlcov.index.html

    You can also check the html report logs/pytest-report.html with:
    .. code-block:: shell
    
       pytest --html=logs/pytest-report.html
