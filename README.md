## Django setup with Docker
### 1. Installations
- Go to the link for `pyenv` installation information [here](https://github.com/pyenv/pyenv#unixmacos)
- After finish installing `pyenv`, install python version 3.11.5 (recommended) or later

Note: Using pyenv allows us to work with different versions of python by switching between versions locally without the need to 
install many python versions globally on our computer.
```bash
pyenv install 3.11.5
```
- Set the version of `python` to version 3.11.5 locally
```bash
pyenv local 3.11.5
```
Note: this will create a `.python-version` file in your current working directory
- Install `poetry`
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Note: Why `poetry`? This is advantage of Poetry vs Pip 
|Feature|	Pip|	Poetry|
|--|--|--|
|Platform|	Python|	Python|
|Ease of use|	Easy to use	|More complex|
|Features|	Few features|	Many features|
|Isolation|	No isolation|	Provides isolation|
|Dependency management	|Basic dependency management	|Advanced dependency management|
|Packaging	|No packaging	|Provides packaging|
|Publishing|	No publishing|	Provides publishing|
- Verify if poetry is installed properly
```bash
poetry --version
```
- Initialize project with `poetry`, this will create a `pyproject.toml` file. 
If you already have experience with `package.json` in many javascript projects, it has litterally the same functionnality patterns. 
```bash
poetry init
```
- Create a python 3.11 virtual environment with poetry (if virtualenv does not exist, it will create a new one)
```bash
poetry env use 3.11
```
- Activate the virtualenv
```bash
source $(poetry env info --path)/bin/activate
```
- If you want to deactivate the virtualenv, try this command:
```bash
deactivate
```
- Now add django library to our project
```bash
poetry add django
```
This will add django to pyproject.toml
- Install all packages in pyproject.toml within the virtualenv
```bash
poetry install
```
### 2. Initialize django
- Initialize django project:
```bash
django-admin startproject tp_django .
```
- Adjust settings for different environements (dev, prod, etc...). First we create a folder name `settings` inside `tp_django`. 
```bash
mkdir tp_django/settings
```
Create 3 files: `__init__.py`, `default.py`, `dev.py`(for now, we only have development (dev) environment)
- `__init__.py` is used to mark a directory as a Python package so that we can use dot operator to import .py file
- `default.py` is the default config for settings. Everything in `tp_django/settings.py` is now move to `tp_django/settings/default.py`. 
After creating `default.py`, delete the `tp_django/settings.py` file
- `dev.py` is the config for development environment
```bash
touch tp_django/settings/__init__.py
touch tp_django/settings/default.py
touch tp_django/settings/dev.py
```
Because our settings.py is now gone. We have to adjust `manage.py`, `tp_django/asgi.py` and `tp_django/wgsi`.
Change this line:
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_django.settings")
```
to this line:
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_django.settings.default")
```
### 3. Setup Docker
- Install docker by follow this [link](https://docs.docker.com/engine/install/debian/) (using Linux (Ubuntu/Debian) as OS is recommended)
- Create a folder name `docker`, inside we can create folder `dev` (development), `qua` (qualification) and `prod` (production), each stores a `Dockerfile` file.
For now, we only have `dev` folder and a `Dockerfile` inside it.
- Add this to your Dockerfile:
```dockerfile
# python image
FROM python:3

# Setting PYTHONUNBUFFERED to a non-empty value different from 0 ensures that 
# the python output i.e. the stdout and stderr streams are sent straight to terminal 
# (e.g. your container log) without being first buffered and that you can see the output 
# of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# create a folder /app inside docker container
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry

RUN poetry install
```
This will setup a docker image for our project 
- Create a `docker-compose.yml` file and a this code below in order to set up and run the docker image:
```yaml
version: "3"

services:
  api:
    command: "poetry run python manage.py runserver --settings tp_django.settings.dev 0.0.0.0:8000"
    build: 
      context: .
      dockerfile: ./docker/dev/Dockerfile
    volumes:
      - .:/app
    ports:
      # map your pc port (first number) to docker port (second number)
      - "8000:8000"
```
- Run application
```
sudo docker compose up
```
- To rebuild application, run
```
sudo docker compose --build 
```
Now you can see application running as http://0.0.0.0:8000 just like normal django application
To quit and stop container, in terminal, press `Ctrl+c` on your keyboard
