# English
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
- Initialize project with `poetry` 
If you already have experience with `package.json` in many javascript projects, it has litterally the same functionnality patterns. 
```bash
poetry init
```
This will create a `pyproject.toml` file.
Note: you can leave everything by defaults or you can config like this as an example
```bash
Package name [python]:  django-docker-app
Version [0.1.0]:  0.1.0
Description []:  TP Django
Author [None, n to skip]:  KhaNguyen
License []:  MIT
Compatible Python versions [^3.11]:  ^3.11

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "django-docker-app"
version = "0.1.0"
description = "TP Django"
authors = ["KhaNguyen"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
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
- Make sure you activate virtualenv before continuing
- Now add django library to our project
```bash
poetry add django
```
This will add django to pyproject.toml
- Install all packages in pyproject.toml within the virtualenv
```bash
poetry install
```
- Verify if all the packages inside pyproject.toml and their dependancies are installed
```
pip freeze
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


# French
## Configuration de Django avec Docker
### 1. Installations
- Installez `pyenv` en suivant les instructions [ici](https://github.com/pyenv/pyenv#unixmacos).
- Une fois `pyenv` installé, installez la version 3.11.5 de Python (recommandée) ou une version ultérieure.

Remarque : L'utilisation de pyenv vous permet de travailler avec différentes versions de Python en changeant de versions localement sans avoir besoin d'installer de nombreuses versions de Python globalement sur votre ordinateur.

```bash
pyenv install 3.11.5
```
- Définissez la version de python sur la version 3.11.5 localement.
```bash
pyenv local 3.11.5
```
Remarque : cela créera un fichier .python-version dans votre répertoire de travail actuel.

- Installez `poetry`
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Remarque : Pourquoi `poetry`? Voici les avantages de `poetry` par rapport à `pip` :

|Fonctionnalité|	Pip|	Poetry|
|--|--|--|
|Plateforme|	Python|	Python|
|Facilité d'utilisation|	Facile à utiliser|	Plus complexe|
|Fonctionnalités	|Peu de fonctionnalités	|De nombreuses fonctionnalités|
|Isolation|	Aucune isolation|	Fournit une isolation|
|Gestion des dépendances|	Gestion des dépendances de base|	Gestion des dépendances avancée|
|Packaging|	Pas de packaging|	Fournit un packaging|
|Publication|	Pas de publication|	Fournit une publication|

- Vérifiez si poetry est installé correctement
```bash
poetry --version
```
- Initialisez le projet avec poetry
Si vous avez déjà l'expérience des fichiers package.json dans de nombreux projets JavaScript, il a littéralement les mêmes modèles de fonctionalités.

```bash
poetry init
```
Ceci créera un fichier pyproject.toml.

Remarque : vous pouvez laisser tout par défaut ou vous pouvez le configurer comme suit :

```bash
Package name [python]:  django-docker-app
Version [0.1.0]:  0.1.0
Description []:  TP Django
Author [None, n to skip]:  KhaNguyen
License []:  MIT
Compatible Python versions [^3.11]:  ^3.11

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "django-docker-app"
version = "0.1.0"
description = "TP Django"
authors = ["KhaNguyen"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```
- Créez un environnement virtuel Python 3.11 avec poetry (si l'environnement virtuel n'existe pas, il en créera un nouveau)
```bash
poetry env use 3.11
```
- Activez l'environnement virtuel
```bash
source $(poetry env info --path)/bin/activate
```
Si vous voulez désactiver l'environnement virtuel, essayez cette commande :
```bash
deactivate
```
Remarque: Assurez-vous d'activer l'environnement virtuel avant de continuer
- Maintenant, ajoutez la bibliothèque Django à notre projet
```bash
poetry add django
```
Ceci ajoutera django à pyproject.toml

- Installez tous les packages dans pyproject.toml dans l'environnement virtuel
```bash
poetry install
```
- Vérifiez si tous les packages de pyproject.toml et leurs dépendances sont installés
```bash
pip freeze
```
### 2. Initialisation de Django
- Initialiser le projet Django :
```bash
django-admin startproject tp_django .
```
- Ajuster les paramètres pour différents environnements (dev, prod, etc.). 
Tout d'abord, nous créons un dossier nommé settings à l'intérieur de tp_django.
```bash
mkdir tp_django/settings
```
Créez 3 fichiers : `__init__.py`, `default.py` et `dev.py` (pour l'instant, nous n'avons que l'environnement de développement (dev)).

- `__init__.py` est utilisé pour marquer un répertoire comme un package Python afin que nous puissions utiliser l'opérateur de point pour importer des fichiers .py.
- `default.py` est la configuration par défaut des paramètres. Tout ce qui se trouve dans tp_django/settings.py est maintenant déplacé vers tp_django/settings/default.py. Après avoir créé default.py, supprimez le fichier tp_django/settings.py.
- `dev.py` est la configuration pour l'environnement de développement.
```bash
touch tp_django/settings/__init__.py
touch tp_django/settings/default.py
touch tp_django/settings/dev.py
```
- Puisque notre settings.py est maintenant supprimé, nous devons ajuster `manage.py`, `tp_django/asgi.py` et `tp_django/wsgi.py`.

Changez cette ligne :
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_django.settings")
```
par cette ligne :
```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_django.settings.default")
```
### 3.Configuration de Docker
- Installez Docker en suivant ce lien: https://docs.docker.com/engine/install/debian/ (il est recommandé d'utiliser Linux (Ubuntu/Debian) comme système d'exploitation).
- Créez un dossier nommé docker, et à l'intérieur, vous pouvez créer les dossiers dev (développement), qua (qualification) et prod (production), chacun contenant un fichier Dockerfile. Pour l'instant, nous n'avons que le dossier dev et un fichier Dockerfile à l'intérieur.
- Ajoutez ceci à votre Dockerfile :
```dockerfile
# image python
FROM python:3

# La définition de PYTHONUNBUFFERED à une valeur non vide différente de 0 garantit que
# la sortie Python, c'est-à-dire les flux stdout et stderr, sont envoyés directement au terminal
# (par exemple, votre journal de conteneur) sans être d'abord mis en mémoire tampon, ce qui vous permet de voir la sortie
# de votre application (par exemple, les journaux Django) en temps réel.
ENV PYTHONUNBUFFERED 1
# Cela empêche Python d'écrire des fichiers pyc.
ENV PYTHONDONTWRITEBYTECODE 1

# Créez un dossier /app à l'intérieur du conteneur Docker
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry

RUN poetry install
```
Cela configurera une image Docker pour notre projet
- Créez un fichier docker-compose.yml et ajoutez-y le code ci-dessous pour configurer et exécuter l'image Docker :
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
      # mappez le port de votre PC (premier numéro) au port Docker (second numéro)
      - "8000:8000"
```
- Exécutez l'application :
```bash
sudo docker compose up
```
- Pour reconstruire l'application, exécutez :
```bash
sudo docker compose --build
```
Vous pouvez maintenant voir l'application en cours d'exécution à l'adresse http://0.0.0.0:8000, comme une application Django normale.
Pour quitter et arrêter le conteneur, appuyez sur Ctrl+c dans le terminal.

