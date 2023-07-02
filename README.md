# Django-PostgreSQL

## Initial setup

Initialize the Poetry project and add its requirements:

```bash
poetry init
poetry add django psycopg2-binary
```

Start the django project and application:

```bash
poetry run django-admin startproject academia
cd academia
poetry run python manage.py startapp polls
```

## Setup

Spin up a PostgreSQL database:

```bash
docker run --name academia-postgres -e POSTGRES_PASSWORD=academia -e POSTGRES_USER=academia -e POSTGRES_DB=academia -p 5432:5432 -d postgres:15.3
```

Install:

```bash
poetry install
```

Run:

```bash
poetry run python manage.py runserver 0.0.0.0:8000
```

## Migrations

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
