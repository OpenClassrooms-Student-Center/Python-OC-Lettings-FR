.. oc_lettings_site documentation master file, created by
   sphinx-quickstart on Sat Jan 17 21:17:22 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OC Lettings Site's documentation!
============================================

.. Add your content using ``reStructuredText`` syntax. See the
.. `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
.. documentation for details.

OC Lettings Site is a modular Django application designed to manage rental properties and user profiles.
The project emphasizes a scalable architecture, maintainability, and adherence to best practices in software development, including CI/CD and comprehensive documentation.

.. note::
Pour les instructions d'installation et de déploiement, consultez le
README du projet sur GitHub <https://github.com/Faaab84/Python-OC-Lettings-FR>_.


.. toctree::
   :maxdepth: 2
   :caption: Table des matières

   installation
   technologies
   database
   usage
   ci_cd_architecture
   api_reference
   about

Indices
=======

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
About
-----

This project is a modular Django site comprising several applications:

- **oc_lettings_site**: Django project folder containing:

  - ``settings.py``: Application configuration

  - ``urls.py``: Main URL routing

  - ``wsgi.py``: WSGI interface for production servers

- **lettings**: Manages rental listings (models, views, templates)
- **profiles**: Manages user profiles (models, views, templates)

The advantage of this approach is to separate concerns, making the codebase more maintainable and scalable.

This allows unique responsibilities for each module, facilitating testing and future enhancements.

The project's goal is to ensure maintainability and scalability of the architecture while adhering to best practices in CI/CD and documentation.

Indices
-------

- This documentation is built with **Sphinx** and published on **Read The Docs**.
- Technical documentation (classes, functions…) is automatically generated from **docstrings** using `sphinx.ext.autodoc`.

Useful indices for navigation:

- For installation steps: see the *Installation* section
- For the code architecture: see the *Architecture* section
- For the technology stack: see the *Technologies* section
- For database structure: see the *Database* section
- For using the project: see the *Usage* section
- For CI/CD pipeline: see the *CI/CD Architecture* section
- For details of the Python API: see the *API Reference* section
