#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --settings=mysite.settings.production
python manage.py migrate --settings=mysite.settings.production
python manage.py collectstatic --settings=mysite.settings.production --no-input --clear
python manage.py update_index --settings=mysite.settings.production

exec "$@"