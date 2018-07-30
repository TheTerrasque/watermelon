#!/usr/bin/bash
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libshout-dev libmp3lame-dev libavformat-dev libchromaprint-dev wget unzip icecast2 pwgen

PASSWORD=$(pwgen -s 30 1)
echo $PASSWORD > /app/streamer_password.txt
sed -i -e "s/hackme/$PASSWORD/g" /app/streamer/docker/icecast.xml
sed -i -e "s/hackme/$PASSWORD/g" /app/streamer/docker/demosauce.conf
