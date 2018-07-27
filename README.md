# watermelon
Next-generation web backend for streaming community radio.  Django providing REST API.

# Get up and running
## (Optional) Create a Virtualenv
* Follow instructions at https://virtualenv.pypa.io/en/stable/userguide/

## To set up python environment and database:
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver