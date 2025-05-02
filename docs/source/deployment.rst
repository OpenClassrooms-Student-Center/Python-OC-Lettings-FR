Deployment and Application Management
=====================================

Overview
--------

The deployment of the OC Lettings application is fully automated using a CI/CD pipeline powered by GitHub Actions:

1. Runs tests and measures code coverage
2. Builds a Docker image
3. Publishes the image to Docker Hub upon successful tests
4. Automatically triggers deployment on Render via webhook

**Key Benefits**

- Automated code quality checks before each deployment
- Version control for Docker images
- Zero manual intervention required for deployment
- Easy rollback to previous versions

Prerequisites
-------------

Before you begin, ensure you have:

- A Docker Hub account
- A Render account
- A GitHub account with access to the repository
- The following GitHub secrets configured:

  .. list-table::
     :header-rows: 1
     :widths: 30 70

     * - Secret Name
       - Description
     * - ``DOCKERHUB_USERNAME``
       - Your Docker Hub username
     * - ``DOCKERHUB_TOKEN``
       - Access token for Docker Hub
     * - ``SECRET_KEY``
       - Django secret key for production
     * - ``SENTRY_DSN``
       - Sentry DSN for error tracking

Deployment Steps
----------------

Initial Setup (One-Time)
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Docker Hub**

   - Create an account at https://hub.docker.com/
   - Create a new repository for the application
   - Generate an access token for GitHub Actions integration

2. **Render**

   - Create an account at https://render.com/
   - Create a new Web Service:
     - Click "New" then "Web Service"
     - Select "Existing image"
     - Connect your Docker Hub account
     - Specify the image: ``docker.io/<your-username>/oc-lettings-site:latest``

3. **Environment Variables**

   In your Render service settings, set:

   .. code-block:: none

      SECRET_KEY=your_django_secret_key
      SENTRY_DSN=your_sentry_dsn_url
      DEBUG=False
      ALLOWED_HOSTS=your-app.onrender.com

4. **Webhooks**

   - In Render: Settings → Deploys → Deploy Hooks
   - Create a new hook and copy the URL
   - In Docker Hub: add this webhook in your repository settings

5. **GitHub Secrets**

   - Go to your GitHub repository → Settings → Secrets → Actions
   - Add all required secrets listed above

Automated Deployment Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When code is pushed to the main branch, the deployment process is triggered:

.. code-block:: bash

   git add .
   git commit -m "Description of changes"
   git push origin master

The GitHub Actions workflow will automatically:

1. Run tests
2. Build the Docker image
3. Push the image to Docker Hub
4. Trigger deployment on Render

Manual Deployment
~~~~~~~~~~~~~~~~~

If you need to deploy manually:

.. code-block:: bash

   # Build the Docker image locally
   docker build -t <your-username>/oc-lettings-site:latest .

   # Push to Docker Hub
   docker push <your-username>/oc-lettings-site:latest

   # Trigger a manual deploy from the Render dashboard

Monitoring and Troubleshooting
-----------------------------

Application Logs
~~~~~~~~~~~~~~~~

- Access logs via the Render dashboard:
  1. Go to your Web Service
  2. Select the "Logs" tab
  3. Filter logs by timestamp or severity

.. tip::
   Use the "Live" option to stream logs in real time during deployments.

Error Tracking
~~~~~~~~~~~~~~

- All application errors are automatically captured by Sentry:
  1. Log in to your Sentry dashboard
  2. Navigate to the project
  3. View errors, frequency, and affected users

Rollback Procedure
~~~~~~~~~~~~~~~~~~

To revert to a previous version:

1. In the Render dashboard, go to "Deploys"
2. Find the previous working deployment
3. Click "Manual Deploy" → "Deploy existing image"
4. Select the specific version tag to restore

Running with Docker
===================

You can run the OC Lettings application using Docker either by building the image locally or by pulling the pre-built image from Docker Hub.

Build and Run Locally
---------------------

1. Build the Docker image:

   .. code-block:: bash

      docker build -t oc-lettings-site .

2. Run the container:

   .. code-block:: bash

      docker run -p 8000:8000 oc-lettings-site

Pull and Run from Docker Hub
----------------------------

1. Pull the image from Docker Hub:

   .. code-block:: bash

      docker pull <your-dockerhub-username>/oc-lettings-site:latest

2. Run the container:

   .. code-block:: bash

      docker run -p 8000:8000 <your-dockerhub-username>/oc-lettings-site:latest

.. note::
   Required environment variables (such as ``SECRET_KEY``, ``SENTRY_DSN``, etc.) should be configured as secrets in your hosting platform or Docker Hub. You do not need a local ``.env`` file unless you want to override them for local development.