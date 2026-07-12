Introduction
============

Project overview
----------------

Orange County Lettings is a Django-based web application that allows users to browse property listings and view detailed information about associated user profiles.

The project is designed with a modular architecture to ensure a clear separation of concerns between its different components (profiles, lettings, main site, etc.).

Development context
-------------------

This project was developed as part of the Python Application Developer program at OpenClassrooms.

It serves as a practical implementation of core software engineering concepts, including:

- Django web application development
- modular architecture design
- reproducible development environments
- CI/CD pipelines and automation

Technical objectives
--------------------

Beyond functional requirements, this project demonstrates the ability to manage a complete software development lifecycle:

- Git and GitHub version control
- code quality analysis with linting tools
- unit testing with pytest
- test coverage analysis
- automated workflows using GitHub Actions
- containerization with Docker
- automated deployment to production environments

High-level architecture
-----------------------

The application consists of several core components:

- a Django web application handling business logic and the user interface
- a relational database (SQLite in quickstart/testing, PostgreSQL in development and production)
- a CI/CD pipeline for automated testing and deployment
- a Docker-based deployment infrastructure hosted on Render

The following sections of this documentation provide more details on
installation, architecture, application components, use cases and deployment.