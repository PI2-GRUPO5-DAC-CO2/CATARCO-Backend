import sys
import json
import random
from catarco.settings import INSTALLED_APPS
from paho.mqtt import client as mqtt_client
sys.path.append("..")

port = 1883
broker = 'broker.emqx.io'
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        raw_data = json.loads(msg.payload.decode())
        data_str = raw_data[0].replace("\'", "\"")
        data = json.loads(data_str)
        key = list(data.keys())[2]

        if 'actuators' in INSTALLED_APPS:
            from .models import Actuator

            actuator = None
            try:
                actuator = Actuator.objects.get(
                    station_id=data['estacao_id'],
                    actuator_id=data['atuador_id']
                )
            except Actuator.DoesNotExist:
                actuator = Actuator.objects.create(
                    station_id=data['estacao_id'],
                    actuator_id=data['atuador_id'],
                    value=data[key]
                )
            else:
                if data[key] != actuator.value:
                    Actuator.objects.filter(
                        station_id=data['estacao_id'],
                        actuator_id=data['atuador_id']
                    ).update(
                        value=data[key]
                    )

    client.subscribe(f'/CATARCO/atuador/ventilador_r')
    client.subscribe(f'/CATARCO/atuador/sistema_r')
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
