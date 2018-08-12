import paho.mqtt.client as mqtt
import socket
import json
import datetime

MQTT_PASSWORD = open("/data/mqtt_password").read().strip()
MQTT_USER = "watermelon"
MQTT_HOST = "mqtt"

def encode(data):
    l = []
    for k, v in data.items():
        l.append('%s=%s' % (k, v))
    return '\n'.join(l)

def listen():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("", 32167))
    listener.settimeout(None)

    while True:
        listener.listen()
        conn, addr = listener.accept()
        print("Got connection")
        data = conn.recv(1024).strip()
        if data:
            print("Got data from socky: ", data)
            answer = sendreceive(data)
            answer = encode(answer)
            answer = answer.encode("utf-8")
            conn.send(answer)
        conn.close()
    
    listener.close()

def sendreceive(message):
    client = mqtt.Client("sockulf")

    returndata={}

    def on_connect(client, userdata, flags, rc):
        client.subscribe("streamer/answer")
        #client.publish("streamer/query", message)
        #print("Command sent")

    def on_message(client, userdata, msg):
        #print("msg received", msg)
        returndata['data'] = json.loads(msg.payload)
        #print("Got return data")
        
    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    client.connect(MQTT_HOST)

    wait = 3
    lastsent = None

    while returndata == {}:
        if not lastsent or datetime.datetime.now() - datetime.timedelta(seconds=3) > lastsent:
            client.publish("streamer/query", message)
            lastsent = datetime.datetime.now()
        client.loop(wait)
        
    
    client.disconnect()
    return returndata['data']

listen()