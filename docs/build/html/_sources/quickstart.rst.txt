Quick Start Guide
=================

This guide will help you get started with the OC Lettings application quickly.

Prerequisites
-------------

Make sure you have completed the installation steps described in the :doc:`installation` page.

Running the Development Server
------------------------------

1. Activate your virtual environment:

   .. code-block:: bash

      source venv/bin/activate  # Linux/macOS
      venv\Scripts\activate     # Windows

2. Start the Django development server:

   .. code-block:: bash

      python manage.py runserver

3. Open your web browser and navigate to http://localhost:8000

Navigation Guide
----------------

The application has several main sections:

* **Home Page** - http://localhost:8000/
* **Profiles** - http://localhost:8000/profiles/
* **Lettings** - http://localhost:8000/lettings/
* **Admin Panel** - http://localhost:8000/admin/ (requires login)

Using the Application
---------------------

Viewing Profiles
^^^^^^^^^^^^^^^^

1. Navigate to the profiles section
2. Click on any profile to view details

Viewing Lettings
^^^^^^^^^^^^^^^^

1. Navigate to the lettings section
2. Click on any letting to view details and address information

Admin Operations
^^^^^^^^^^^^^^^^

For administrative tasks (requires admin login):

1. Log in to the admin panel
2. Manage lettings, addresses, and user profiles