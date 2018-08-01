#!/usr/bin/bash
#/usr/bin/icecast2 -b -c /app/streamer/docker/icecast.xml
echo -n "mqtt pw is : " 
cat /data/mqtt_password
echo

PASSWORD=$(cat /data/streamer_password.txt)
sed -e "s/hackme/$PASSWORD/g" /app/streamer/docker/demosauce.conf > /data/demosauce.conf
echo "Streamer pw: $PASSWORD"


echo "Starting streamer"
/app/streamer/demosauce/demosauce -c /data/demosauce.conf
echo "Streamer exit"