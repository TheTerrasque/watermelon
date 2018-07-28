#!/usr/bin/bash

apt-get update
#apt-get install -y apt-utils
apt-get install -y pwgen 
#mosquitto

cd /app/rest-backend
pip install -r requirements.txt
cp /app/rest-backend/docker/settings_local.py /app/rest-backend/watermelon/