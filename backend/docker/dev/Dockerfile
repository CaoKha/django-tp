FROM python:3.11-alpine as build-image

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock poetry.toml ./

# Install packages only needed in build stage
RUN  \
  apk update && \
  apk upgrade && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip3 install poetry && \
  poetry install --no-cache && \
  apk --purge del .build-deps

RUN poetry export -f requirements.txt --output requirements.txt

# Use an official Python runtime as a parent image - Run stage
FROM python:3.11-alpine as runtime

ENV PYTHONUNBUFFERED=1

# Copy venv from build stage
COPY --from=build-image requirements.txt /app/backend/requirements.txt

# Install packages that are only needed runtime, postgresql-libs is needed to suppress warning when connecting to postgres
RUN  \
  apk update && \
  apk upgrade && \
  apk add bash postgresql-libs gcc python3-dev libc-dev && \
  rm -rf /var/cache/apk/*

RUN pip3 install -r /app/backend/requirements.txt

# Add the rest of the code
COPY . /app/backend
COPY ./scripts/ /app/

# Make port 8000 available for the app
ENV DJANGO_PORT 8000
EXPOSE 8000

# Change directory so that scripts could locate manage.py
WORKDIR /app/backend

# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
RUN ["chmod", "+x", "/app/entrypoint-dev.sh"]
ENTRYPOINT [ "/app/entrypoint-dev.sh" ]
