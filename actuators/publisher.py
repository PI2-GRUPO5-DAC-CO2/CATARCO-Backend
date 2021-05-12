import random
from paho.mqtt import client as mqtt_client

port = 1883
broker = 'broker.emqx.io'
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc != 0:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, metrics):
    topic = metrics[0]
    payload_msg = metrics[1]

    msg = str(payload_msg)
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Back enviou: {msg}")
    else:
        print(f"Failed to send message to topic {topic}")


def run(metrics):
    client = connect_mqtt()
    publish(client, metrics)


if __name__ == '__main__':
    run()
