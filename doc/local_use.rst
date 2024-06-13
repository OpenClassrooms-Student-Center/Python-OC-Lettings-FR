Local Usage
===========

Launching the Server
--------------------

**Step 1: Activate the environment**

.. code-block:: bash

    # On Windows
    .\env\Scripts\activate

    # On Unix or MacOS
    source env/bin/activate

**Step 2: Launch the server**

.. code-block:: bash

    python manage.py runserver

Launching Tests
---------------

**Step 1: Activate the environment**

.. code-block:: bash

    # On Windows
    .\env\Scripts\activate

    # On Unix or MacOS
    source env/bin/activate

**Step 2: Navigate to the application**

.. code-block:: bash

    cd ./lettings || cd ./profiles || cd ./oc_lettings_site

**Step 3: Execute the tests**

.. code-block:: bash

    pytest tests.py

**To test all files at once, without leaving the root directory:**

.. code-block:: bash

    pytest --cov

Launching Linting
-----------------

**Step 1: Activate the environment**

.. code-block:: bash

    # On Windows
    .\env\Scripts\activate

    # On Unix or MacOS
    source env/bin/activate

**Step 2: Execute flake8**

.. code-block:: bash

    flake8
