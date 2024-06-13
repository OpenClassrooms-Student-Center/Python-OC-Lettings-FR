Presentation
========================================

Oc Lettings
------------

OC Lettings is a django app displaying lettings and profiles to the user and an admin part.
The project was to refactor the app from oc_lettings_site only to oc_lettings_site, lettings and profile apps.
The project is tested thanks to all tests.py files and it is deployed to render url when git pull or push on main branch
and github actions validate the project.

Composition
------

1. **Django**:
    - This is a Django project.

2. **Flake8**:
    - Flake8 was used for linting.

3. **Sentry**:
    - Sentry provides a log system to avoid error and capture exceptions.

4. **Github Actions**:
    - Github Actions allows us to test the projec, buld and push the image to docker.

5. **Docker**:
    - Docker is used to build and push an image to render and allow our ci/cd pipeline to work efficiently.

6. **Render**:
    - Render get our image and deploy it on a url.
