Database
========

The Orange County Lettings project uses a relational database system to store
application data.

Django's Object-Relational Mapping (ORM) is used to interact with the database
through Python models instead of writing direct SQL queries.

Database environments
---------------------

The project uses different database backends depending on the execution
environment:

- **SQLite** is used for quickstart and automated tests. It provides a lightweight
  database solution requiring no additional service configuration.
- **PostgreSQL** is used for Docker and production environments. It provides a
  more robust and scalable database system suitable for deployment.

The database engine is selected through environment configuration.

Data models
-----------

The application data is organized through Django models defined in each
application.

Main entities include:

- ``Letting``: represents a property listing;
- ``Address``: stores the location information associated with a letting;
- ``Profile``: extends Django's built-in authentication system by associating additional information with each user.

The models are managed through Django migrations, which ensure that the
database schema remains synchronized with the application code.

Database reference
------------------

The following sections are automatically generated from the project's model
docstrings using Sphinx ``autodoc``.

Lettings models
~~~~~~~~~~~~~~~

.. automodule:: lettings.models
   :members: Address, Letting

Profiles models
~~~~~~~~~~~~~~~

.. automodule:: profiles.models
   :members: Profile