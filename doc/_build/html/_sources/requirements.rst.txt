Requirements
===============================================

Environment Setup
-----------------

After cloning or forking the repository, you need to set up a virtual environment and install the required packages. Follow these steps:

1. **Create a virtual environment**:

    Depending on your operating system and preference, you can create a virtual environment using `venv` (included in Python 3.3 and later) or any other tool like `virtualenv`.

    For `venv`, run:

    .. code-block:: bash

        python -m venv env

    Activate the environment:

    .. code-block:: bash

        # On Windows
        .\env\Scripts\activate

        # On Unix or MacOS
        source env/bin/activate

2. **Install the required packages**:

    Install all dependencies listed in the `requirements.txt` file using pip:

    .. code-block:: bash

        pip install -r requirements.txt

This setup will ensure that all necessary libraries and packages are installed in your virtual environment, keeping your project's dependencies isolated from other Python projects.

Secret Variables
-----------------

Create a .env file at root, and add these lines with the proper infos :
    .. code-block:: bash
        DOCKER_USERNAME="your_docker_username"
        DOCKER_PASSWORD="your_docker_password"
        SENTRY_DSN="your_sentry_dsn"
