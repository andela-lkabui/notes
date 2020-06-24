#!/bin/bash

set -e

until PGPASSWORD=$POSTGRES_PASSWORD pg_isready -h "db" -p "5432" -q; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

echo "The environment is: $ENVIRONMENT"

if [ "$ENVIRONMENT" == "TESTING" ]; then
  python manage.py test
else
  # Apply database migrations
  echo "Apply database migrations"
  python manage.py migrate

  # Start server
  echo "Starting server"
  python manage.py runserver 0.0.0.0:8080
fi
