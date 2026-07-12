Deployment
==========

The Orange County Lettings application is deployed on Render using a
containerized production environment.

Production architecture
-----------------------

The production environment relies on:

- Docker for application containerization;
- Render as hosting platform;
- PostgreSQL as persistent database;
- Gunicorn as WSGI server;
- WhiteNoise for static file serving.

Deployment process
------------------

The deployment process is automated through the CI/CD pipeline.

When changes are merged into the production branch, the pipeline:

#. Builds a new Docker image.
#. Publishes the image to Docker Hub.
#. Triggers a deployment on Render using a Deploy Hook.
#. Starts the updated production container.

The Render Deploy Hook allows the CI/CD pipeline to remotely trigger a new
deployment while keeping deployment credentials outside the source code.

Application startup
-------------------

When the container starts:

#. The environment variables are loaded.
#. Database migrations are applied through ``start.sh``.
#. Gunicorn starts the Django application.
#. The application becomes available through the Render service.

Configuration management
------------------------

Sensitive configuration values are provided through environment variables.

The following elements are configured externally:

- Django secret key;
- database credentials;
- deployment settings.
