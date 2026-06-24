Deployment
==========

Django settings
---------------
The Django application's `settings.py` file is used to configure the application regarding some very important
environment variables used by the CI/CD pipeline such as "DEBUG" and "DJANGO_ALLOWED_HOSTS" (the latter must be set on
your Heroku profile) and regarding the static files used by the application's front-end.

Static files and WhiteNoise
---------------------------

You can find the detailed specific configuration of WhiteNoise library by checking the url below : `WhiteNoise <https://whitenoise.readthedocs.io/en/stable/django.html>`_

Configuration
^^^^^^^^^^^^^
If you’re familiar with Django you’ll know what to do. If you’re just getting started with a new Django project then you’ll need add the following to the bottom of your settings.py file:

.. code::

    STATIC_ROOT = BASE_DIR / "staticfiles"

Enable WhiteNoise
^^^^^^^^^^^^^^^^^
The WhiteNoise library has to be installed before if not already done.
Please edit your `settings.py` file and add WhiteNoise to the MIDDLEWARE list.
The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware (if you are using it) and before all other middleware:

.. code::

    MIDDLEWARE = [
        # ...
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        # ...
    ]

Add compression and caching support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
WhiteNoise comes with a storage backend which compresses your files and hashes them to unique names, so they can safely be cached forever. To use it, set it as your staticfiles storage backend in your settings file:

.. code::

    STORAGES = {
        # ...
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

Docker containerization
-----------------------
A Dockerfile in the repository root defines the process for building an image of the application and its dependencies
as a Docker container. Here are the main steps in this image building :

* Copy the dependencies from the `requirements.txt` file and install them.

* Retrieve the static files of the Django application.

* Run Gunicorn (a library required for deployment on Heroku) on the specified application (for example, `oc_lettings_site.wsgi:application`), and the specified host and port.

CI/CD pipeline
--------------
GitHub Actions is the CI/CD solution provided by GitHub, while GitLab uses GitLab CI/CD pipelines.

The `.yml` file structures the CI/CD pipelines and it is used by GitHub for creating GitHub Actions or used by Gitlab for creating CI/CD workflow.

CI pipeline
^^^^^^^^^^^
The continuous integration (CI) pipeline ensures the quality of the code.
The CI pipeline defined in the "ci" job runs as follows:

* Checkout on the branch from which the push was performed

* Installing the project's dependencies

* Running linters (quality step)

* Running tests with the `pytest` command (testing step)

* Finally, loading the quality and test coverage reports

CD pipeline
^^^^^^^^^^^
The Continuous Delivery (CD) pipeline ensures the delivery and deployment of the app.
The CD pipeline defined in the "deploy" job works as follows:

* Requires the successful execution of the previous continuous integration (CI) job (described earlier) on the master branch.

* Checkout on the master branch. If the commit & push are performed from another branch, the CD pipeline is not executed.

* The Docker image is initialized.

* The Docker image is built and pushed (containerization process).

* The Heroku command-line interface (CLI) is installed.

* Deployment to Heroku.

Secrets/variables
-----------------
In order to use correctly this Django web application, you must define some secrets in your Git platform secrets section.
Those secrets are used in the django.yml file that describes the CI/CD pipeline.

GitHub
^^^^^^

Here's how you can add a secret on GitHub :

* Go to your GitHub profile and open the project repository.

* Click on "Settings", then on the "Secrets & Variables" section, and finally on the "Actions" button in the dropdown menu.

* Next, click on "New Repository Secret" and enter the secret name and the secret value. Then confirm. The new secret is added to the repository.

Gitlab
^^^^^^

Here's how you can add a secret variable on GitLab :

* Go to your GitLab profile and open the project repository.

* In the left sidebar, click on "Settings" and then on "CI/CD".

* Expand the "Variables" section.

* Click on "Add variable".

* Enter the variable key (name) and the variable value, then click on "Add variable" to save it.

* The new variable is now available in the GitLab CI/CD pipeline.

Required secrets/variables
^^^^^^^^^^^^^^^^^^^^^^^^^^

Here are all the required secrets/variables :

* DOCKER_PASSWORD

* DOCKER_USERNAME

* HEROKU_API_KEY

* HEROKU_USER_EMAIL

* SENTRY_KEY

When created, you can then use this secret with the variable `secrets` as shown below :

.. code::

    ${{ secrets.<THE SECRET NAME> }}

All secrets are used according to this format in the django.yml file which describes the CI/CD pipeline.

The variable attribute name and the secret name has to be rigorously identical.

Heroku
------

GitHub
^^^^^^

Once the GitHub actions are successfully completed, the application is deployed as a web service. Please check the
application's Heroku URL or click the "View application" button in your Heroku account to view the web application.

If the GitHub actions failed, please review the logs on GitHub or in Heroku, fix the errors, and try the deployment
again.

Gitlab
^^^^^^

Once the Gitlab CI/CD is successfully completed, the application is deployed as a web service. Please check the
application's Heroku URL or click the "View application" button in your Heroku account to view the web application.

If the Gitlab CI/CD failed, please review the logs on the platform or in Heroku, fix the errors, and try the deployment
again.

Environment variables
^^^^^^^^^^^^^^^^^^^^^
The application needs some environment variables to work well. You must specify the variables into your Heroku app.
Please follow the steps below :

* Go into your app in Heroku dashboard

* Go to settings section

* scroll down to "config vars" sub-section

* click on the "Reveal Config Vars" button to reveal the variables if some are already existing

* For each environment variable needed by the project, enter the "key" and the "value", and validate by clicking the "add' button

Hera are all the variables regarding Django you need to provide :

====================   =================================================================
Key                    Value
====================   =================================================================
DEBUG                  False (required for production deployment, True otherwise in dev)
DJANGO_ALLOWED_HOSTS   localhost,127.0.0.1,<your heroku url>.herokuapp.com
SECRET_KEY             <your Django secret key>
====================   =================================================================

Monitoring with Sentry
----------------------
In this project, the CI/CD pipeline uses the Sentry SDK for exceptions and logs monitoring.

You will need a Sentry account to run the application correctly. Therefore, please register on the Sentry website
if you don't already have one.

Another step: Before using the deployment pipeline, you must define a secret or variable into your Git platform for the Sentry key, required to link
the application to your Sentry account. Please see the "Secrets" subsection above.

Troubleshooting
---------------
In this section we focus on some common issues that arise in this kind of pipeline.

Heroku application crashes immediately
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here are the possible causes :

* bad port

* non-used port

* bad Gunicorn configuration


Example :
If the application crashes immediately after deployment, ensure Gunicorn binds to the environment PORT variable:

.. code:: bash

   gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT

ALLOWED_HOSTS errors
^^^^^^^^^^^^^^^^^^^^
Example :
A HTTP 400 error usually indicates that the Heroku domain is missing from DJANGO_ALLOWED_HOSTS, environment variable
defines in Heroku app.

.. code:: bash

    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,my-app.herokuapp.com

Static files not loading
^^^^^^^^^^^^^^^^^^^^^^^^
Here are the possible causes :

* collectstatic not implemented

* WhiteNoise not used

* STATIC_ROOT not defined in Django app settings.py file

Docker build fails
^^^^^^^^^^^^^^^^^^
Here are the possible causes :

* secrets missing

* invalid Heroku API key

* bad Docker login

* release failed
