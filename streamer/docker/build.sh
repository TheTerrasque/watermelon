#!/usr/bin/bash

cd /app/streamer/demosauce

echo "Configuring streamer make"
yes | ./configure

echo "Compiling streamer and dscan"
make -j2 all