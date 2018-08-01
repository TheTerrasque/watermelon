#!/usr/bin/bash
cp /app/streamer_password.txt /data/streamer_password.txt

echo "Starting icecast"
/usr/bin/icecast2 -c /app/icecast.xml