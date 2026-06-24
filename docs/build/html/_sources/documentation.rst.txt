Documentation
=============

Environment configuration
-------------------------
In the `env-docs` virtual environment, you must install Sphinx library if not already installed as explained in the :doc:`installation section <installation>`.

.. code::

    pip install sphinx

.. code::

    poetry add sphinx

.. code::

    uv add sphinx

Documentation project initialization
------------------------------------
Please create a "docs" folder or use one if existing and type in your terminal the command below to initialize the documentation :

.. code::

    sphinx-quickstart

You can choose default options and validate. It will create all required files used by ReadTheDocs documentation.

Documentation editing
---------------------
You can use the index.rst as an entry point for the documentation content. Please use reStructuredText language in order to add content.
If you need help, you can check the url below to see `reStructuredText help documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.

Documentation local building
----------------------------
To generate your documentation locally while editing content, you must type in your terminal the command below :

.. code::

    .\docs\make.bat html

ReadTheDocs configuration
-------------------------
Here are the steps to follow if you want to generate another documentation in your account into the ReadTheDocs website :

* First, you need to create an account on the ReadTheDocs website if you don't already have one.

* Then create a new documentation project and link it to your Git platform :
    * Click on "Import a repository" and then "Connect to GitHub/GitLab"
    * Click on "+" button to finalise the importation
    * The two accounts are synchronized

* Configure the options of the ReadTheDocs projects

* Configure the option for the automatic building and release after each push & commit on GitHub/Gitlab

* Finally, ReadTheDocs will detect each modification and will rebuild the documentation online

ReadTheDocs documentation access
--------------------------------
ReadTheDocs provides an URL to your documentation online. You can include that URL in your repository `readme.md` file.
