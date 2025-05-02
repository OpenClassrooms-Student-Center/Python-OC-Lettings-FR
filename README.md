## Summary

Orange County Lettings website

## Local Development

### Prerequisites

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the local development documentation, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Create the virtual environment

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step gives errors with a package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm that the `python` command runs the Python interpreter in the virtual environment
`which python`
- Confirm that the Python interpreter version is 3.6 or higher `python --version`
- Confirm that the `pip` command runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm that the site works and it is possible to navigate (you should see several profiles and lettings).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/Python-OC-Lettings-FR`
- Open a shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display the tables in the database `.tables`
- Display the columns in the profiles table, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Log in with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except:

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Deployment

### Overview of the deployment process

The application deployment is done via a GitHub Actions CI/CD pipeline that:
1. Runs tests and coverage
2. Builds a Docker image
3. Publishes the image to Docker Hub when tests succeed
4. Automatically triggers a deployment on Render using a webhook

This architecture allows:
- Verifying code quality before deployment
- Maintaining versioned Docker images
- Deploying automatically without manual intervention

### Prerequisites

- A Docker Hub account
- A Render account
- A GitHub account with configured secrets:
  - `DOCKERHUB_USERNAME`: Docker Hub username
  - `DOCKERHUB_TOKEN`: Docker Hub token
  - `SECRET_KEY`: Django secret key
  - `SENTRY_DSN`: Sentry DSN key

### Deployment Steps

#### Initial setup (to be done once)

1. Configure Docker Hub:
   - Create an account on [Docker Hub](https://hub.docker.com/) if you don't have one
   - Create a new repository for the application
   - Generate an access token for GitHub Actions

2. Create an account on [Render](https://render.com/) if you don't already have one

3. From the Render dashboard, create a new Web Service:
   - Click on "New" then "Web Service"
   - Select "Existing image"
   - Connect your Docker Hub account
   - Specify the image: `docker.io/your-username/oc-lettings-site:latest`

4. Configure environment variables on Render:
   - In your service settings, go to "Environment"
   - Add the following variables:
     - `SECRET_KEY`: your Django secret key
     - `SENTRY_DSN`: Sentry DSN key

5. Configure the Render webhook for automatic deployment:
   - In your Render service settings, go to "Deploys" then "Deploy Hooks"
   - Create a new hook and copy the generated URL
   - Go to Docker Hub, in your repository settings
   - Add a new webhook pointing to the Render URL

6. Configure secrets in GitHub:
   - Go to your GitHub repository → Settings → Secrets → Actions
   - Add the secrets mentioned in the prerequisites

#### Automatic deployment flow

1. When you push code to the main branch:
   ```bash
   git push origin master