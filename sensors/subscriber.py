import random
import time
import sys
from paho.mqtt import client as mqtt_client


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
        print(f"Minerador recebeu: `{msg.payload.decode()}`")

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