from django.core.management.base import BaseCommand, CommandError
from mqtt_connection import mqtt_wrap
import json
from songs import models
import traceback

testdata =  {
            'path': "/app/streamer/docker/streamtest/Darkman007_-_chipo_five.it",
            'artist': "[TEST] Darkman007",
            'title': "[TEST] chipo_five",
            'gain': "0",
        }

class Command(BaseCommand):
    help = 'Controls the streamer and dscan via MQTT'

    def __init__(self):
        self.map = {
            "streamer/query": self.streamer_next_song,
            "dscan/response": self.update_song
        }

    def update_song(self, data):
        data = json.loads(data)
        song = data["in"]["id"]
        song = models.Song.objects.get(id= song) #pylint: disable=E1101
        


    def on_message(self, client, userdata, msg):
        incoming = msg.payload
        if msg.topic in self.map:
            try:
                topic, data = self.map[msg.topic](incoming)
                if topic:
                    client.publish(topic, json.dumps(data))
            except:
                tb = traceback.format_exc()
                self.client.publish("error/mqttcomm", tb)

    def streamer_next_song(self, message):
        data = models.Song.get_next_queued()
        if not data:
            data = testdata
        return ("streamer/answer", data)

    def on_connect(self, client, userdata, flags, rc):
        for key in self.map:
            client.subscribe(key)

    def handle(self, *args, **options):
        self.client = mqtt_wrap.getclient(self.on_connect, self.on_message, "streamcontroller")
        print("Starting up mqtt controller")
        self.client.loop_forever()