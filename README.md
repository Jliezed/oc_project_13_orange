<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![oc-project][oc-project-shield]][oc-project-url]
[![django][django-shield]][django-url]
[![postgresql][postgresql-shield]][postgresql-url]
[![tests][tests-shield]][tests-url]
[![linting][linting-shield]][linting-url]
[![docker][docker-shield]][docker-url]
[![cicd][ci-cd-pipeline-shield]][ci-cd-pipeline-url]
[![circleci][circleci-shield]][circleci-url]
[![heroku][heroku-shield]][heroku-url]
[![sentry][sentry-shield]][sentry-url]





<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">OC - PROJECT N°13 - Django App Deployment - CI/CD Pipeline </h1>

  <p align="center">
   Orange County Lettings is a small Django App deployed on Heroku and using a CI/CD Pipeline.
    <br />
</p>
</div>

<img src="https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80">
<a href="https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80"><small>By Ian Dooley</small></a>




<!-- ABOUT THE PROJECT -->
## Project Overview
![Overview](static/assets/oc_project_13_overview.gif)


<p align="right">(<a href="#top">back to top</a>)</p>



## Built With & Tools

* Python 
* Django
* Docker
* CircleCI
* Heroku
* Sentry

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Clone the repo

   ```sh
   git clone https://github.com/Jliezed/oc_project_13_orange.git
   ```

### Run the app:
### -> with a virtual environment
Install venv library (if not yet in your computer)
   ```sh
   pip install venv
   ```
Create a virtual environment
   ```sh
   python -m venv env
   ```
Activate the virtual environment
   ```sh
   source env/bin/activate
   ```
#### Install packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
      
#### Access to the App by running the server
   ```sh
   python manage.py runserver
   ```
#### Go to http://127.0.0.0:8000/ to access the app
#### Go to http://127.0.0.0:8000/admin/ to access the admin panel (user: `admin`, password: `Abc1234!`)

### -> with Docker
#### Build the image
   ```sh
   docker build -t oc_project_13_orange .
   ```

#### Run the container
   ```sh
    docker run -p 8000:8000 oc_project_13_orange
   ```

#### Go to http://localhost:8000/ to access the app
#### Go to http://localhost:8000/admin/ to access the admin panel (user: `admin`, password: `Abc1234!`)

<p align="right">(<a href="#top">back to top</a>)</p>

## Lintings & Tests
### Run Flake8
   ```sh
   flake8
   ```
### Run Tests
   ```sh
  python manage.py test
   ```


<p align="right">(<a href="#top">back to top</a>)</p>

## Deployment - CI/CD Pipeline
Define in the `.circleci/config.yml` file the steps to be executed by CircleCI when a new commit is pushed to the repository.
![CI/CD Pipeline](static/assets/circleci.png)
### Step 1: Pip & Requirements
- Install pip
- Install requirements
- If the installation fails, the build is stopped
- If the installation passes, the build continues

### Step 2: Linting
- Run Flake8 to check the code quality
- If Flake8 fails, the build is stopped
- If Flake8 passes, the build continues

### Step 3: Testing
- Run tests
- If tests fail, the build is stopped
- If tests pass, the build continues
- Tests results are saved in CircleCI

### Step 4: Build Docker Image
- Build the Docker image
- If the build fails, the build is stopped
- If the build passes, the build continues
- The image is tagged with the commit SHA
- The image is pushed to Docker Hub
- Required: 
  - Pip & Requirements passed
  - Linting passed
  - Testing passed
- Only on branch: Master

### Step 5: Deploy to Heroku
- Deploy the Docker image to Heroku
- If the deployment fails, the build is stopped
- If the deployment passes, the build ends
- Required:
  - Build Docker Image passed

### Live URL: https://oc-lettings-jliezed.herokuapp.com
<p align="right">(<a href="#top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

[ci-cd-pipeline-shield]: https://img.shields.io/badge/-CICD%20PIPELINE-blue?style=for-the-badge
[ci-cd-pipeline-url]: https://circleci.com/

[circleci-shield]: https://img.shields.io/badge/-CIRCLECI-blue?style=for-the-badge
[circleci-url]: https://circleci.com/

[heroku-shield]: https://img.shields.io/badge/-HEROKU-blue?style=for-the-badge
[heroku-url]: https://www.heroku.com/

[sentry-shield]: https://img.shields.io/badge/-SENTRY-blue?style=for-the-badge
[sentry-url]: https://sentry.io/

[docker-shield]: https://img.shields.io/badge/-DOCKER-blue?style=for-the-badge
[docker-url]: https://www.docker.com/

[django-shield]: https://img.shields.io/badge/-DJANGO-blue?style=for-the-badge
[django-url]: https://www.djangoproject.com/

[postgresql-shield]: https://img.shields.io/badge/-POSTGRESQL-blue?style=for-the-badge
[postgresql-url]: https://www.postgresql.org/

[tests-shield]: https://img.shields.io/badge/-TESTS-blue?style=for-the-badge
[tests-url]: https://docs.djangoproject.com/en/3.2/topics/testing/

[linting-shield]: https://img.shields.io/badge/-LINTING-blue?style=for-the-badge
[linting-url]: https://flake8.pycqa.org/en/latest/