Installation
=============

These steps describe how to install your development environment.

Clone the GitHub repository
----------------------------
 - git clone https://github.com/Slb59/Oc-P13.git .

Create the virtual environment
------------------------------
Pipenv is a Python virtualenv management tool that supports a multitude of systems and nicely bridges the gaps between pip, python and virtualenv.

 - mkdir .venv
 - rename the file .env.example en .env
 - change variable values to suit your configuration
 - pip install pipenv
 - pipenv shell
  
Link the project to Sentry
---------------------------
Sentry is a platform that automatically flags errors and project exceptions.
It also allows for performance monitoring.
