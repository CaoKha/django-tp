# TP Django Rest Framework (DRF) + React (Vite) + Postgres + Docker

Backend: DRF
Frontend: React + Vite
DB: Postgres

## Setup environment variables

### Backend

Inside backend, create your own folder to store environment variables

```bash
backend/.env/
├── dev
│   ├── .env.django.dev
│   └── .env.postgres.dev
└── prod
    ├── .env.django.prod
    └── .env.postgres.prod
```

The content of `.env.django.dev` will be somethin like this (put your own django SECRET_KEY and AUTH0 parameters)

```text
DJANGO_PORT=8000
AUTH0_DOMAIN=<your auth0 domain>
AUTH0_AUDIENCE=<your auth0 audience>
DJANGO_SETTINGS_MODULE=django_app.settings.dev 

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE_NAME=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db 
SQL_PORT=5432
```

The content of `.env.django.prod` will be like this

```text
DJANGO_PORT=8000
AUTH0_DOMAIN=<your auth0 domain>
AUTH0_AUDIENCE=<your auth0 audience>
DJANGO_SETTINGS_MODULE=django_app.settings.prod 

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE_NAME=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db 
SQL_PORT=5432

```

The content of `.env.postgres.dev` and `.env.postgres.prod` will be

```text
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
PGPORT=5432
```

### Frontend

Same like backend, create a folder `.env` inside `frontend` folder
```bash
frontend/.env
├── .env.dev
└── .env.prod
```

.env.dev
```
VITE_APP_AUTH0_DOMAIN=<your auth0 domain>
VITE_APP_AUTH0_CLIENT_ID=<your auth0 client id>
VITE_APP_AUTH0_CALLBACK_URL=http://localhost:3000/callback
VITE_APP_AUTH0_AUDIENCE=<your auth0 audience>
VITE_APP_API_SERVER_URL=http://localhost:8000
```
.env.prod (adapt this to your production working environment)
```text
VITE_APP_AUTH0_DOMAIN=<your auth0 domain>
VITE_APP_AUTH0_CLIENT_ID=<your auth0 client id>
VITE_APP_AUTH0_CALLBACK_URL=http://localhost:3000/callback
VITE_APP_AUTH0_AUDIENCE=<your auth0 audience>
VITE_APP_API_SERVER_URL=http://localhost:8000
```

## Run the project

Adapt this command to your favor OS. (Mine is Ubuntu/PopOS)

```bash
sudo docker compose -f docker-compose.dev.yml up --build
```

Stop the container by `Ctrl+C`. Then, when you finish, remove all the containers by

```bash
sudo docker compose -f docker-compose.dev.yml down -v
```

Note: Same steps for production (but this project is not production ready yet)

If you want to delete all dangling docker images and volumes in your PC. Try this:
```bash
sudo docker system prune -a --volumes
```
