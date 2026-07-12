Architecture
============

Orange County Lettings is organized as a modular Django project. Each application
is responsible for a specific functional domain, improving maintainability and
allowing independent evolution of the different components.

Project structure
-----------------

The project is composed of three main Django applications:

- ``oc_lettings_site``: global project configuration, URL routing, WSGI application
  and project settings;
- ``lettings``: management of property listings and associated data;
- ``profiles``: management of user profiles and user-related information.

This separation follows Django's recommended application structure and keeps
business logic isolated from project configuration.

Application architecture
------------------------

The application follows Django's Model-View-Template (MVT) architecture:

- **Models** define the data structure and database interactions through Django ORM;
- **Views** handle HTTP requests, retrieve data and prepare responses;
- **Templates** provide the user interface rendered by the application.

Request flow
------------

A typical request follows this workflow:

1. The user sends an HTTP request.
2. Django resolves the URL through the project's routing configuration.
3. The corresponding view processes the request.
4. Models are used to retrieve or update data when required.
5. The view renders the appropriate template and returns an HTTP response.

Deployment architecture
-----------------------

The application is containerized using Docker and deployed automatically through a CI/CD
pipeline.

The production architecture relies on:

- Docker for application containerization;
- PostgreSQL as the production database;
- Gunicorn as the WSGI server;
- Render as the hosting platform.

The detailed source code reference generated from docstrings is available in the
dedicated API reference sections of this documentation.