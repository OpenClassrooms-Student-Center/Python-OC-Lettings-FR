Technologies
============

The Orange County Lettings project is built on a Python web stack designed to improve maintainability, reproducibility, and deployment automation.

Backend
-------

- Python 3.10: main programming language
- Django 3.0: web framework used for application structure, routing, and ORM

Databases
----------

- SQLite: used for CI unit tests and fast setup
- PostgreSQL: used in Docker and production environments

Containerization
-----------------

- Docker: container runtime for the application
- Docker Compose: configuration and orchestration of the application services

CI/CD
-----

- GitHub Actions: automated workflows for testing, linting, and deployment

Testing and code quality
------------------------

- pytest / pytest-django: unit and integration testing
- coverage: test coverage measurement
- flake8: linting for code style and quality
- black: code formatting

Production stack
----------------

- Gunicorn: WSGI HTTP server for running Django in production
- WhiteNoise: static file serving without external storage
- Render: cloud platform used for hosting and deployment

Monitoring and configuration
-----------------------------

- Sentry: error tracking and monitoring
- python-dotenv: environment variable management via `.env` files