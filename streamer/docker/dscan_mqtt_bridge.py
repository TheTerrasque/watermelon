import paho.mqtt.client as mqtt
import socket
import json
import datetime

import subprocess

DSCAN_PATH = "/app/streamer/demosauce/dscan"

MQTT_PASSWORD = open("/data/mqtt_password").read().strip()
MQTT_USER = "watermelon"
MQTT_HOST = "mqtt"

def listener():
    client = mqtt.Client("dscan_client")

    def on_connect(client, userdata, flags, rc):
        client.subscribe("dscan/query")

    def on_message(client, userdata, msg):
        print("Got message")
        data = json.loads(msg.payload)
        print("Decoded message")
        try:
            r = subprocess.check_output([DSCAN_PATH, "-r", data["path"]])
            r = r.decode("utf-8")
            print(r)
            resp = {}
            for line in r.split("\n"):
                if line.strip():
                    k, v = line.split(":", 1)
                    resp[k] = v
            response = json.dumps({"in": data, "out": resp})
        except Exception as e:
            response = json.dumps({"in": data, "error": str(e)})
        client.publish("dscan/response", response)
        
    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    client.connect(MQTT_HOST)

    client.loop_forever()

listener()