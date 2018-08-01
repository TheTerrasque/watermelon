from django.conf import settings

import paho.mqtt.publish as mqttpublish
import paho.mqtt.client as mqtt

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.renderers import JSONRenderer

from django.utils import timezone

S = {}

def publish(topic, message, qos = 0, retain = False):
    if not getattr(settings, "MQTT_HOST", None):
        return False
    a = {
        "username": settings.MQTT_USER,
        "password": settings.MQTT_PASSWORD
    }
    mqttpublish.single(topic, message, hostname=settings.MQTT_HOST, auth = a, qos = qos, retain = retain)
    return True

@receiver(post_save)
def my_handler(sender, **kwargs):
    if sender in S:
        i = kwargs["instance"]
        r = S[sender](i)
        d = {
            "instance": r.data,
            "new" : kwargs["created"],
            "timestamp": timezone.now(),
            "id": i.id
        }
        json = JSONRenderer().render(d)
        t = sender.__name__
        publish("updates/%s" % t, json)


def getclient(on_connect=None, on_message = None, clientid=''):
    client = mqtt.Client(clientid)
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    client.connect(settings.MQTT_HOST)
    return client