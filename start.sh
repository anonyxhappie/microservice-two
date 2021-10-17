#!/bin/bash
echo 'Running migrations...'
cd /code1
python ./manage.py migrate
# python ./manage.py runserver 8000 &
cd /code2
python ./manage.py migrate
# python ./manage.py runserver 8001 &
cd /code3
python ./manage.py migrate
# python ./manage.py runserver 8002 &

echo 'Migrations Complete!'
