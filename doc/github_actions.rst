Github Actions
===========

YML file steps
--------------------

**Step 1: Install Python, packages from requirements.txt and
link static assets to our project**

.. code-block:: bash

    name: Install dependencies
    run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Collect static files
        run: python manage.py collectstatic --noinput
        env:
        DJANGO_SETTINGS_MODULE: oc_lettings_site.settings

**Step 2: Linting**

.. code-block:: bash

    - name: Run linting
        run: flake8 .

**Step 3: Tests with coverage **

.. code-block:: bash

    - name: Run tests with coverage
        run: |
        pytest --cov=./ --cov-report=term-missing:skip-covered --cov-fail-under=80

**Step 4: Create Secrets for your github actions and use them**
1. Inside yout project, on Github, go to settings, secrets and variables, click on action and on new repository secret,
    add your docker username and your docker password like this:

.. code-block:: bash

    DOCKER_USERNAME="your_docker_username"
    DOCKER_PASSWORD="your_docker_password"

2. This is what we use inside the yml file to log and perform operations with docker:
    .. code-block:: bash
        - name: Build Docker image
        run: docker build . -t ${{ secrets.DOCKER_USERNAME }}/myapp:${{ github.sha }}

        - name: Log in to Docker Hub
            uses: docker/login-action@v1
        with:
            username: ${{ secrets.DOCKER_USERNAME }}
            password: ${{ secrets.DOCKER_PASSWORD }}

**Step 5: Pushing the image to docker hub**

.. code-block:: bash

    - name: Push Docker image to Docker Hub
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:${{ github.sha }}

**Step 6: Deploy the image to render**
1. Get your render deploy hook
    - Go to Render, got to your dashboard
    - Create a new web service
    - In the settings of your service, link your reposiroty to it, add this start command :
    .. code-block:: bash
        python manage.py runserver 0.0.0.0:$PORT
    -Copy the Deploy hook
2. Add the secret variable inside github actions as we previously see as :
    
.. code-block:: bash
    RENDER_DEPLOY_HOOK="your_render_deploy_hook"

3. This is what we use inside the yml file to link this project to your render web service :
    .. code-block:: bash
        - name: Deploy to Render
            run: |
            curl -X POST -d '' "${{ secrets.RENDER_DEPLOY_HOOK }}"
