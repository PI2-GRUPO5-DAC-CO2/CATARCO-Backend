from django.test import TestCase
import paho.mqtt.client as mqtt
import time     

class TestBrokerConnection(TestCase):
    def setUp(self):
        self.client = mqtt.Client("Test Client")
        self.client.on_connect = self.on_connect
        self.has_connected = False

    def on_connect(self, client, userdata, flags, rc):  # connect function
        if rc == 0:
            self.has_connected = True

    def test_connection(self):  # test to check connection to broker
        self.client.connect("mqtt.eclipseprojects.io", 1883)
        self.client.loop_start()
        time.sleep(2)
        self.client.loop_stop()
        self.assertTrue(self.has_connected)