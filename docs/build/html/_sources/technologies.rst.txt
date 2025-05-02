Technologies and Programming Languages
=====================================

This section details all technologies and tools used in the OC Lettings project.

Core Technologies
-----------------

Python
^^^^^^
- **Version**: 3.12.3
- **Purpose**: Main programming language for the application backend
- **Key libraries**: See requirements.txt for a complete list of dependencies

Django
^^^^^^
- **Version**: 3.0
- **Purpose**: Web framework for building the application
- **Components used**:
  - Django ORM for database models
  - Django Templates for view rendering
  - Django Admin for content management

Database
--------

SQLite3
^^^^^^^
- **Purpose**: Database for development environment
- **Schema**: See the Database Structure section for detailed model information

Deployment and Infrastructure
-----------------------------

Docker
^^^^^^
- **Purpose**: Containerization for consistent deployment
- **Components**:
  - Dockerfile for building application image
  - Container orchestration for deployment

Sentry
^^^^^^
- **Purpose**: Error tracking and performance monitoring
- **Implementation**: Integrated with Django for automatic error reporting

Documentation
-------------

Sphinx
^^^^^^
- **Purpose**: Documentation generation tool
- **Components**:
  - autodoc for automatic code documentation
  - ReStructuredText for markup
  - ReadTheDocs theme for styling
- **Output**: HTML documentation with searchable interface

Frontend
--------

HTML/CSS
^^^^^^^^
- **Framework**: Bootstrap for responsive design
- **Templates**: Django template language for HTML generation
- **Static Files**: CSS and JavaScript assets for frontend functionality

Testing
--------

pytest
^^^^^^^^
- **Purpose**: Testing framework for unit and integration tests
- **Coverage**: Tests cover models, views, and business logic

Development Tools
-----------------

Version Control
^^^^^^^^^^^^^^^
- **Tool**: Git with GitHub
- **Purpose**: Track changes and collaborate on code

Code Quality
^^^^^^^^^^^^
- **flake8**: 
  - **Purpose**: Python linting tool for enforcing code style
  - **Configuration**: Customized in setup.cfg
  - **Integration**: Runs in CI/CD pipeline and locally before commits

CI/CD
^^^^^
- **Platform**: GitHub Actions
- **Purpose**: Continuous integration and deployment pipeline
- **Features**: Automated testing, linting, and deployment to production