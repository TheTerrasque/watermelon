#!/bin/ash
cp /app/mqtt_password /data/mqtt_password
/usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf