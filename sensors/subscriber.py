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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        data_str = msg.payload.decode().replace("\'", "\"")
        data = json.loads(data_str)
        key = list(data.keys())[2]


        if 'sensors' in INSTALLED_APPS:
            from .models import Sensor

            sensor = None
            try:
                sensor = Sensor.objects.get(id=data['sensor_id'])
            except Sensor.DoesNotExist:
                sensor = Sensor.objects.create(
                    id=data['sensor_id'],
                    station_id=data['estacao_id'],
                    value=data[key]
                )
            else:
                sensor = Sensor.objects.get(id=data['sensor_id'])
                if data[key] != sensor.value :
                    Sensor.objects.filter(id=data['sensor_id']).update(
                        value=data[key]
                    )


    client.subscribe(f'/CATARCO/sensor/velocidade')
    client.subscribe(f'/CATARCO/sensor/umidade')
    client.subscribe(f'/CATARCO/sensor/temperatura')
    client.subscribe(f'/CATARCO/sensor/pressao')
    client.subscribe(f'/CATARCO/sensor/nivel')
    client.subscribe(f'/CATARCO/sensor/co2')
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
