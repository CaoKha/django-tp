# python image
FROM python:3.11.5
# Setting PYTHONUNBUFFERED to a non-empty value different from 0 ensures that 
# the python output i.e. the stdout and stderr streams are sent straight to terminal 
# (e.g. your container log) without being first buffered and that you can see the output 
# of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# create a folder /backend inside docker container
WORKDIR /backend
COPY poetry.lock pyproject.toml /backend/
RUN pip3 install poetry
RUN poetry install --no-dev
COPY common /backend/common
COPY authz /backend/authz
COPY django_app /backend/django_app
COPY messages_api /backend/messages_api
COPY gunicorn.conf.py manage.py /backend/

