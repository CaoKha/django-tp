## Steps
### 1. Installations
- Go to the link for `pyenv` installation information [here](https://github.com/pyenv/pyenv#unixmacos)
- After finish installing `pyenv`, install python version 3.11.5 (recommended) or later
```bash
pyenv install 3.11.5
```
- Set the version of `python` to version 3.11.5 locally
```bash
pyenv local 3.11.5
```
- Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Verify if poetry is installed properly
```bash
poetry --version
```
- Initialize project with `poetry`, this will create a `pyproject.toml` file. 
If you work with `javascript`, it has litterally the same functionnality patterns. 
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
- Start django project:
```bash
django-admin startproject tp_django .
```
- Adjust settings for different environements (dev, prod, etc...). First we create a folder name `settings` inside `tp_django`. 
```bash
mkdir tp_django/settings
```
Create 3 files: `__init__.py`, `default.py`, `dev.py`(for now, we only have developpement (dev) environment)
- `__init__.py` is used to mark a directory as a Python package so that we can use dot operator to import .py file
- `default.py` is the default config for settings. Everything in `tp_django/settings.py` is now move to `tp_django/settings/default.py`. 
After creating `default.py`, delete the `tp_django/settings.py` file
- `dev.py` is the config for developpement environment
### 3. Setup Docker
- Install docker by follow this [link](https://docs.docker.com/engine/install/debian/) (using Linux (Ubuntu/Debian) as OS is recommended)
- Run application
```
sudo docker compose up
```
- To rebuild application, run
```
sudo docker compose --build 
```
