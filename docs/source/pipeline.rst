Pipeline
========

The Orange County Lettings project uses a continuous integration and deployment
pipeline based on GitHub Actions.

The pipeline automates code validation, Docker image creation, and production
deployment in order to ensure that only validated changes can reach the
production environment.

Pipeline workflow
-----------------

The global workflow follows these steps:

#. A developer pushes changes or creates a Pull Request on GitHub.
#. The ``compile`` job validates the source code quality and runs automated tests.
#. When validation succeeds on the production branch, the ``containerize`` job
   builds and publishes the Docker image.
#. The ``deploy`` job triggers the production deployment on Render.

::

    Developer
        |
        v
    GitHub repository
        |
        v
    GitHub Actions
        |
        +----------------+
        |   compile      |
        |----------------|
        | Dependencies   |
        | flake8         |
        | pytest         |
        | coverage       |
        +----------------+
                |
                v
        (master branch only)
                |
                v
        +----------------+
        | containerize   |
        |----------------|
        | Docker build   |
        | Docker Hub     |
        +----------------+
                |
                v
        +----------------+
        | deploy         |
        |----------------|
        | Render Hook    |
        +----------------+


Compile job
-----------

The ``compile`` job runs for every push and Pull Request.

Its purpose is to validate that the application remains stable before any
deployment operation.

The job performs:

- installation of Python dependencies;
- static code analysis using ``flake8``;
- execution of automated tests using ``pytest``;
- measurement of test coverage.

The application uses a minimum coverage threshold to prevent significant
regressions from being introduced.

Containerize job
----------------

The ``containerize`` job runs only after a successful ``compile`` job and only
for changes merged into the production branch.

It is responsible for creating and publishing the production Docker image.

The job performs:

- Docker image build;
- image tagging using the Git commit SHA;
- creation of a ``latest`` image tag;
- publication to Docker Hub.

Using immutable SHA-based tags allows each production image to be uniquely
identified and traced back to a specific source revision.

Deploy job
----------

The ``deploy`` job is executed after the Docker image has been successfully
published.

It triggers a Render deployment through a Deploy Hook.

This mechanism allows GitHub Actions to remotely start a new production
deployment without storing deployment credentials inside the repository.

Monitoring and logging
----------------------

The application integrates Sentry to monitor runtime behavior and production
issues.

The monitoring strategy relies on three levels of information:

- **Logs**: general application events and informational messages used to
  understand normal application activity;
- **Warnings**: abnormal situations that do not prevent the application from
  running but may require attention;
- **Errors**: application failures requiring investigation, including server
  errors such as HTTP 500 responses.

HTTP 404 responses are also monitored to help identify invalid routes or
unexpected user navigation patterns.

This monitoring approach provides visibility into application health after
deployment and helps detect issues that are not visible during automated tests.