DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

MQTT_PASSWORD = open("/data/mqtt_password").read().strip()
MQTT_HOST = "mqtt"

SECRET_KEY = open("/app/rest_secret").read().strip()