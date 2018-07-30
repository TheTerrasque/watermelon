#!/usr/bin/bash
/usr/bin/icecast2 -b -c /app/streamer/docker/icecast.xml
/app/streamer/demosauce/demosauce -c /app/streamer/docker/demosauce.conf