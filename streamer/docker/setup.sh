#!/usr/bin/bash
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libshout-dev libmp3lame-dev libavformat-dev libchromaprint-dev wget unzip
pip install paho-mqtt