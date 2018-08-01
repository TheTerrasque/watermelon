from django.core.management.base import BaseCommand, CommandError
from mqtt_connection import mqtt_wrap
import json
from songs import models

testdata =  {
            'path': "/app/streamer/docker/streamtest/Darkman007_-_chipo_five.it",
            'artist': "[TEST] Darkman007",
            'title': "[TEST] chipo_five",
            'gain': "0",
        }

class Command(BaseCommand):
    help = 'Controls the streamer via MQTT'

    def on_message(self, client, userdata, msg):
        incoming = msg.payload
        data = models.Song.get_next_queued()
        if not data:
            data = testdata
        print("Got incoming", incoming, "and sent", data)
        client.publish("streamer/answer", json.dumps(data))

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("streamer/query")

    def handle(self, *args, **options):
        client = mqtt_wrap.getclient(self.on_connect, self.on_message, "streamcontroller")
        print("Starting up stream controller")
        client.loop_forever()