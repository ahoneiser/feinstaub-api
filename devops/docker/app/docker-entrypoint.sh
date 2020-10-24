#!/bin/bash

# wait for postgres
until pg_isready -h ${DB_HOST} -p ${DB_PORT} >/dev/null 2>&1; do
  echo waiting for postgres ..
  sleep 1
done

# run migrations, collect staticfiles
python manage.py migrate
python manage.py collectstatic --noinput

# exec CMD
exec "${@}"
