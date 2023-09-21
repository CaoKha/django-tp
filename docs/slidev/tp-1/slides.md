---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left 
mdc: true
---

# Django React Docker

Kha Nguyen

<!-- <div class="pt-12"> -->
<!--   <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10"> -->
<!--     Press Space for next page <carbon:arrow-right class="inline"/> -->
<!--   </span> -->
<!-- </div> -->

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>


<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: slide-left
---

# Table of contents

<br>
<Toc maxDepth="1"></Toc>



<!--
You can have `style` tag in markdown to override the style for the current page.
Learn more: https://sli.dev/guide/syntax#embedded-styles
-->


<!--
Here is another comment.
-->

---
layout: default
---

# Demo

 
[Github](https://github.com/CaoKha/django-tp)


---
transition: slide-up
---

# Keypoints

<br>

- 🛠 **Hierarchy** - Overview of the project structure 

- 📤 **Environments** - Development VS Production

- 📞 **Connection** - Connection between Frontend and Backend 

- 🔓 **Security** - Social authentication with Auth0 
---
layout: default
---

# Project Hierarchy

There are 3 main components: **backend**, **frontend** and **docker-compose.yml**  

<div grid="~ cols-2 gap-4">
<div>

```bash {0|2-16|17-18|0}
.
├── backend
│   ├── auth
│   ├── db.sqlite3
│   ├── django_app
│   ├── docker
│   ├── gunicorn.conf.py
│   ├── manage.py
│   ├── messages_api
│   ├── poetry.lock
│   ├── poetry.toml
│   ├── __pycache__
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   └── scripts
├── docker-compose.dev.yml
├── docker-compose.prod.yml
```

</div>
<div>

```bash {0|1-4|5-17|18-19}
├── docs
│   ├── en
│   ├── fr
│   └── slidev
├── frontend
│   ├── dist
│   ├── docker
│   ├── index.html
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   ├── README.md
│   ├── src
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── LICENSE
└── README.md
```

</div>
</div>


---

# Docker

<div grid="~ cols-3 gap-4">
<div>


```bash {0|3-4}
.
├── backend
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── docs
├── frontend
├── LICENSE
└── README.md
```

</div>
<div>

```bash {0|1,7,9}
backend
├── auth
├── db.sqlite3
├── django_app
├── docker
│   ├── dev
│   │   └── Dockerfile
│   └── prod
│       └── Dockerfile
├── gunicorn.conf.py
├── manage.py
├── messages_api
├── poetry.lock
├── poetry.toml
├── __pycache__
├── pyproject.toml
├── README.md
├── requirements.txt
└── scripts

```

</div>
<div>

```bash {0|1,5,7}
frontend
├── dist
├── docker
│   ├── dev
│   │   └── Dockerfile
│   └── prod
│       └── Dockerfile
├── index.html
├── node_modules
├── package.json
├── package-lock.json
├── public
├── README.md
├── src
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

</div>
</div>

---
class: px-20
---

# Dockerfile

Frontend

```docker
FROM node:18-alpine

WORKDIR /frontend

# COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
```


---
preload: false
hideInToc: true
---

# Dockerfile
Backend

<div grid="~ cols-2 gap-4">
<div>

```docker
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
```
</div>
<div>

```docker
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
```
</div>
</div>
---

# Docker Compose

<div grid="~ cols-3 gap-4">
<div>

```yaml {all|10|all}
version: "3"
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: ./docker/dev/Dockerfile
    volumes:
      - ./frontend:/frontend
    ports:
      - "5173:3000"
    env_file:
      ./frontend/.env/.env.dev
```
</div>
<div>

```yaml {all|11-13}
  backend:
    build: 
      context: ./backend
      dockerfile: ./docker/dev/Dockerfile
    env_file:
      ./backend/.env/dev/.env.django.dev
    ports:
      - "8000:8000" 
    volumes:
      - ./backend:/backend
    depends_on:
      db:
        condition: service_healthy
```
</div>
<div>

```yaml {all|11-15}
  db:
    image: postgres:15
    restart: always
    hostname: db
    volumes:
      - db-data:/var/lib/postgresql/data
    env_file:
      ./backend/.env/dev/.env.postgres.dev
    ports:
      - "5433:5432"   
    healthcheck:
      test: [ "CMD", "pg_isready", "-U","postgres","-d","postgres" ]
      interval: 10s
      timeout: 5s
      retries: 5
volumes:
  db-data:
```
</div>
</div>

---

# Development VS Production

<div grid="~ cols-2 gap-4">

<div>

development
```docker
# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
RUN ["chmod", "+x", "/app/entrypoint-dev.sh"]
ENTRYPOINT [ "/app/entrypoint-dev.sh" ]
```

```shell
#!/bin/bash
python manage.py wait_for_db

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:"$DJANGO_PORT"
```
</div>
<div>

production
```docker
# Be sure to use 0.0.0.0 for the host within the Docker container,
# otherwise the browser won't be able to find it
RUN ["chmod", "+x", "/app/entrypoint-prod.sh"]
ENTRYPOINT [ "/app/entrypoint-prod.sh" ]
```

```shell
#!/bin/bash
python manage.py wait_for_db

python manage.py makemigrations --no-input

python manage.py migrate --no-input

gunicorn django_app.wsgi:application -b 0.0.0.0:"$DJANGO_PORT"
```
</div>

</div>

---
---
# Connect frontend and backend


```markdown {all|1}
- REST
- Websocket
- gRPC

```

<div v-click grid="~ cols-2 gap-2">
<div>
.env.django.dev

```text
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 *
DJANGO_PORT=8000
AUTH0_DOMAIN=
AUTH0_AUDIENCE=
DJANGO_SETTINGS_MODULE=django_app.settings.dev

EXTERNAL_DATABASE=true
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE_NAME=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db 
SQL_PORT=5432
```
</div>
<div>
.env.react.dev

```text
VITE_APP_AUTH0_DOMAIN=
VITE_APP_AUTH0_CLIENT_ID=
VITE_APP_AUTH0_CALLBACK_URL=http://localhost:3000/callback
VITE_APP_AUTH0_AUDIENCE=https://tp-django.example.com
VITE_APP_API_SERVER_URL=http://localhost:8000
```
```ts
const apiServerUrl = import.meta.env.VITE_APP_API_SERVER_URL;

export const getPublicResource = async (): Promise<ApiResponse> => {
  const config: AxiosRequestConfig = {
    url: `${apiServerUrl}/api/messages/public`,
    method: "GET",
    headers: {
      "content-type": "application/json",
    },
  };

  const { data, error } = (await callExternalApi({ config })) as ApiResponse;

  return {
    data,
    error,
  };
};
```
</div>
</div>

---

# Auth0 

<img src="/auth0.png" class="h-100 px-2"/>
