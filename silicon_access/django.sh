#!/bin/bash

# Ejecutar migraciones de Django
python manage.py makemigrations
python manage.py migrate


# Si el superusuario no existe, crearlo
echo "Inicializando superusuario"
echo "from django.contrib.auth.models import User; User.objects.filter(username='silicon').exists() or User.objects.create_superuser('silicon', 'silicon@access.com','access' )" | python manage.py shell
echo "Supuerusuario creado"
# Iniciar el servidor Django
python manage.py runserver 0.0.0.0:8000
#exec "$@"