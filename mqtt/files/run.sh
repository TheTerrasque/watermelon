#!/bin/ash
cp /app/mqtt_password /data/mqtt_password
echo "Habla Babla"
/usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf