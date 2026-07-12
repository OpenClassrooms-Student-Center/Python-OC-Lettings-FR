Installation
============

This section explains how to install and configure the Orange County Lettings project in a local environment or with Docker.

It complements the README by providing a more detailed setup procedure and environment configuration.

The project supports two installation modes:

- local Python environment (development)
- Docker-based environment (production-like)

Prerequisites
-------------

Ensure the following tools are installed:

- Git
- Python 3.10+
- Docker and Docker Compose (optional but recommended)

Project cloning
---------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Local development setup
-----------------------

This setup is intended for development without containers.

Virtual environment
~~~~~~~~~~~~~~~~~~~

Create and activate a virtual environment to isolate dependencies:

.. code-block:: bash

   python -m venv venv

   # Linux / macOS
   source venv/bin/activate

   # Windows
   venv\Scripts\activate

Dependencies installation
~~~~~~~~~~~~~~~~~~~~~~~~~

Install project dependencies:

.. code-block:: bash

   pip install -r requirements.txt

This includes Django, testing tools, code quality utilities, and deployment dependencies.

Environment configuration
-------------------------

The application uses environment variables for configuration.

Create a `.env` file at the project root.

Required variables:

- SECRET_KEY
- DEBUG
- USE_SQLITE
- SENTRY_DSN (optional)

For PostgreSQL environments:

- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT

Database setup
--------------

Apply database migrations before starting the application:

.. code-block:: bash

   python manage.py migrate

Run development server
----------------------

.. code-block:: bash

   python manage.py runserver

Access the application at:

http://localhost:8000

Docker setup
-------------

A Docker Compose configuration is provided to run the full application stack with a single command.

This setup is recommended for:

- production-like execution
- reproducibility
- avoiding local dependency issues

Start containers:

.. code-block:: bash

   docker compose up --build

Container initialization
------------------------

On startup, the container automatically:

- applies database migrations
- starts the Gunicorn server

This is handled by the `start.sh` script and ensures the database schema is always up to date before serving requests.

Environment differences
-----------------------

- Local setup: SQLite (lightweight, portability)
- Docker setup: PostgreSQL (production-like)
