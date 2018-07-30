#!/usr/bin/sh
mkdir /app
head -c 128 /dev/urandom | sha256sum | base64 | head -c 32 > /app/mqtt_password
/usr/bin/mosquitto_passwd -b /mosquitto/config/mosquitto.passwd watermelon $(cat /app/mqtt_password)

