from catarco.settings import INSTALLED_APPS
from paho.mqtt import client as mqtt_client
import random
import time
import json
import sys
sys.path.append("..")

broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def get_id(key):
    if key == 'sistema':
        return 1
    
    return 2


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        raw_data = json.loads(msg.payload.decode())
        data_str = raw_data[0].replace("\'", "\"")
        data = json.loads(data_str)
        key = list(data.keys())[0]

        if 'actuators' in INSTALLED_APPS:
            from .models import Actuator

            id = get_id(key)
            actuator = None
            try:
                actuator = Actuator.objects.get(id=id, actuator_id=data['atuador_id'])
            except Actuator.DoesNotExist:
                actuator = Actuator.objects.create(
                    id=id,
                    actuator_id=data['atuador_id'],
                    station_id=data['estacao_id'],
                    value=data[key]
                )
            else:
                Actuator.objects.filter(id=id, actuator_id=data['atuador_id']).update(
                    value=data[key]
                )

    client.subscribe(f'/CATARCO/atuador/ventilador_r')
    client.subscribe(f'/CATARCO/atuador/sistema_r')
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
