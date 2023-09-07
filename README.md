## Steps
### 1. Installations
- Go to the link for `pyenv` installation information [](https://github.com/pyenv/pyenv#unixmacos)
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
- Init virtual environment with `poetry`:
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

### 2. Setup Docker
