Installation Instructions
=========================

Local Development
-----------------

Prerequisites
~~~~~~~~~~~~~

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

.. note::
   In the rest of the local development documentation, it is assumed that the ``python`` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

macOS / Linux
~~~~~~~~~~~~~

Clone the repository
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/mumz0/Python-OC-Lettings-FR.git

Create the virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   python -m venv venv
   # If the previous step gives errors with a package not found on Ubuntu:
   apt-get install python3-venv
   
   # Activate the environment
   source venv/bin/activate

Verify your environment:

.. code-block:: bash

   # Confirm that Python runs in the virtual environment
   which python
   
   # Confirm Python version is 3.6 or higher
   python --version
   
   # Confirm pip is in the virtual environment
   which pip
   
   # To deactivate the environment
   deactivate

Run the site
^^^^^^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pip install --requirement requirements.txt
   python manage.py runserver

Open your browser at http://localhost:8000 and confirm that the site works and it is possible to navigate (you should see several profiles and lettings).

Linting
^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   flake8

Unit tests
^^^^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   source venv/bin/activate
   pytest

Database
^^^^^^^^

.. code-block:: bash

   cd /path/to/Python-OC-Lettings-FR
   sqlite3
   
   # In SQLite prompt:
   .open oc-lettings-site.sqlite3
   .tables
   
   # Display the columns in the profiles table
   pragma table_info(Python-OC-Lettings-FR_profile);
   
   # Run a query on the profiles table
   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
   
   # Exit SQLite
   .quit

Admin panel
^^^^^^^^^^^

1. Go to http://localhost:8000/admin
2. Log in with user ``admin``, password ``Abc1234!``

.. warning::
   For security reasons, change these credentials in production environments.

Windows
~~~~~~~

Using PowerShell, follow the same instructions as for macOS/Linux except:

- To activate the virtual environment:

  .. code-block:: powershell
  
     .\venv\Scripts\Activate.ps1
     
- Replace ``which <my-command>`` with ``(Get-Command <my-command>).Path``