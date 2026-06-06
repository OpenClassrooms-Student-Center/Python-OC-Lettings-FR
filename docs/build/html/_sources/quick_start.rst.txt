Quick start guide
=================

Launching server
----------------

Local server
^^^^^^^^^^^^
Please follow the steps as below :

* Open a terminal
* Go to project folder - example :

    .. code::

        cd oc_lettings_site

* Activate the virtual environment as described previously
* Create environment variables (to avoid to add raw Sentry key into the code) :

  * With Power Shell :

    .. code::

        $env:SENTRY_KEY = "your_key"

  * With Git Bash :

    .. code::

        export SENTRY_KEY = "your_key"

* Launch the local server by typing the command :

    .. code::

        python manage.py runserver

Web server
^^^^^^^^^^

Please follow the procedure described in :doc:`deployment section <deployment>` regarding the GitHub Actions or Gitlab CI/CD workflow, Docker containerization
and automatic deployment.

Launching the APP
-----------------

Please follow the steps as below :

* With local server, open a web browser and type the urls :

    .. code::

        http://127.0.0.1:8000/

    .. code::

        http://127.0.0.1:8000/admin

    for the admin panel (username: `admin`, password: given in the project technical specifications)

* With web server (after deployment), open a web browser and type the url :

    * Your Heroku app url given in the Heroku dashboard, for example the url below :

        `Heroku app url example <https://orange-county-lettings-7b4c4811f25f.herokuapp.com>`_

You also need to specify all required environment variables used by the application in your Heroku app.
Please follow the procedure detailed in the Heroku sub-section in :doc:`deployment section <deployment>`.
