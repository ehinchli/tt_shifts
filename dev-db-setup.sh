#!/bin/zsh

# ONLY FOR DEV ENVIRONMENT
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('evan', '', 'admin')" | python manage.py shell


