#!/usr/bin/bash

#apt-get update
#apt-get install -y apt-utils
#apt-get install -y pwgen 
#mosquitto

cd /app/rest-backend
pip install -r requirements.txt
mkdir /app/rest-backend/watermelon/
cp /app/rest-backend/docker/settings_local.py /app/rest-backend/watermelon/

head -c 128 /dev/urandom | sha256sum | base64 | head -c 32 > /app/rest_secret