#!/usr/bin/bash
cd /app/rest-backend

sleep 4 #To let the db start up fully

## Setup that needs the database to be running
# Migrate databae model
python3 manage.py migrate
# Create admin user if does not exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@myproject.com', 'admin');exit()" | python3 manage.py shell

# Run dev server
python3 manage.py runserver 0:8000