*****************************************
Instructions for installing the project.
*****************************************

To install and interact with this project, you will need the following prerequisites:

- DockerHub account
- AWS account (for deployment)
- GitHub account
- Python 3.10 or higher
- Your credentials entered into GitHub secrets

Here are the steps to clone and run the OC Lettings project:

1. **Clone the Django Project:**

- Navigate to the directory where you want to clone the Django project in your terminal or command prompt:

.. code-block::

    cd path/to/your/directory

- Clone the Django project repository using Git:

.. code-block::

    git clone <repository_url>

Replace <repository_url> with the URL of the Django project repository on GitHub or another Git hosting platform.

2. **Create and Activate a Virtual Environment:**

- Navigate into the cloned project directory and Create a new virtual environment:

.. code-block::

    python3 -m venv venv

- Activate the virtual environment:

.. code-block::

    source venv/bin/activate

3. **Install Project Dependencies:**

.. code-block::

    pip install -r requirements.txt

4. **Set Up Django Project:**

Navigate to the Django project directory containing manage.py and run database migrations (if applicable):

.. code-block::

    python manage.py migrate


If you have followed all these steps, you should now be able to perform the actions outlined in the quick start guide.
