#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# Si el superusuario no existe, crearlo
echo "Inicializando superusuario"
echo "from django.contrib.auth.models import User; User.objects.filter(username='silicon').exists() or User.objects.create_superuser('silicon', 'silicon@access.com','access' )" | python manage.py shell
echo "Supuerusuario creado"
