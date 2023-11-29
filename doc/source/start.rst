============
Installation
============

These steps describe how to install your development environment.

Clone the GitHub repository
---------------------------

.. code-block:: shell

   git clone https://github.com/Slb59/Oc-P13.git .

Create the virtual environment
------------------------------
Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, python and virtualenv.

 - mkdir .venv
 - rename the file .env.example en .env
 - change variable values to suit your configuration (see "Link the project to Sentry" for sentry configuration)
 - pip install pipenv
 - pipenv shell
  
Link the project to Sentry
--------------------------

Sentry is a platform that automatically flags errors and project exceptions.
It also allows for performance monitoring.

  - Create a Sentry account
  - Create a project with the platform
  - Retrieve the dsn key and embed it in your ''.env'' file
  - Log in to your Sentry account to view the logs retrieved by Sentry

Run the site
------------

 - python manage.py runserver
 - goto http://localhost:8000 with your browser
 - confirm that the site is working and that it is possible to navigate through the different pages
