Installation
============

Python version
--------------

For this new app version, the Python version is the same : Python 3.10

Virtual environments
--------------------
In this Django application we use 2 virtual environments as below :

* One for the application environment (env)

* One for the ReadTheDocs documentation environment (env-docs)

Libraries
---------
The libraries used are for both environments :

App env
^^^^^^^
* django (==3.0)

* flake8 (==3.7.0)

* flake8-html (==0.4.3)

* pytest (==9.0.3)

* pytest-django (==4.12.0)

* pytest-cov (==7.1.0)

* six (==1.17.0)

* sentry-sdk (>=2.60.0,<3.0.0)

* python-dotenv (>=1.2.2,<2.0.0)

* gunicorn (>=26.0.0,<27.0.0)

* whitenoise (>=6.12.0,<7.0.0)

Documentation env
^^^^^^^^^^^^^^^^^
* Sphinx (==8.1.3)

* sphinx_rtd_theme (==3.1.0)

Dependency manager and installation
-----------------------------------

Pip
^^^

First, create the virtual environment :
.. code::

   py -3.10 -m venv env

Then, activate the virtual env :

* in Git Bash on Windows or on macOS / Linux

.. code::

   source env/bin/activate


* on Windows

.. code::

   env\Scripts\activate

To install dependencies, type :

.. code::

   pip install -r requirements.txt

Uv
^^

UV is an environment and dependencies manager.

To install environment and dependencies, type :

.. code::

   uv sync

UV will use the .toml file to know which Python version and dependencies to install.

Poetry
^^^^^^

POETRY is an environment and dependencies manager.

First, install the virtual environment :

.. code::

   py -3.10 -m venv env

Then, activate the virtual env :

.. code::

   poetry env activate

To install dependencies, type :

.. code::

   poetry install

POETRY will use the .toml file to know which dependencies to install.
