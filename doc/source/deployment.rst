==================================
Development and deployment Process
==================================

Run the site locally with Django
---------------------------------

 - start virtual environnement [1]_
 - python manage.py collectstatic
 - python manage.py runserver
 - goto http://localhost:8000 with your browser
 - goto http://localhost:8000/admin to access the admin panel
 you can connect with user admin and mot de passe Abc1234!
 - goto http://localhost:8000/sentry-debug/ to generate a ZeroDivisionError and verify your Sentry account

 .. [1] by setting the DEBUG variable in the .env file to true, you can view the debug-toolbar

Run the site locally via Docker
-------------------------------

 - create a dockerhub account
 - install docker desktop
 - retrieve the docker image to run the application locally : 