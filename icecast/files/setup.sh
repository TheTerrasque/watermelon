#!/usr/bin/bash
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 pwgen

PASSWORD=$(pwgen -s 30 1)
echo $PASSWORD > /app/streamer_password.txt
sed -i -e "s/hackme/$PASSWORD/g" /app/icecast.xml