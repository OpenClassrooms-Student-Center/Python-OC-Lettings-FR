Views and endpoints
===================

The application exposes web routes through Django URL routing.
Each route is associated with a view function responsible for processing
requests and returning the appropriate response.

Request handling
----------------

Django processes incoming requests through the following workflow:

1. The URL dispatcher matches the requested path with a configured route.
2. The associated view retrieves or processes the required data using models.
3. The view renders a template with the provided context.
4. Django returns the generated HTTP response to the client.

URL organization
----------------

Each Django application defines its own URL configuration:

- ``oc_lettings_site``: global URL configuration;
- ``lettings`` manages property listing pages;
- ``profiles`` manages user profile pages.

The application namespaces allow URL names to remain isolated between
different components.

Views reference
---------------

The following sections are automatically generated from the project's
view docstrings using Sphinx ``autodoc``.

Lettings views
~~~~~~~~~~~~~~

.. automodule:: lettings.views
   :members:

Profiles views
~~~~~~~~~~~~~~

.. automodule:: profiles.views
   :members: