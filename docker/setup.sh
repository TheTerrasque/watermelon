#!/usr/bin/bash
mkdir /data

apt-get update
#apt-get install -y apt-utils
apt-get install -y pwgen mosquitto

cd /app/rest-backend
pip install -r requirements.txt
cp /app/docker/settings_local.py /app/rest-backend/watermelon/