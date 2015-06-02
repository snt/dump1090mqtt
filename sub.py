# -*- coding: utf-8 -*-
"""
Subscriber test code
To run:
    python sub.py host port user password

host, port, user and password are MQTT broker's ones.
"""

import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe("/adsb/#")

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    print host, port
    username = sys.argv[3]
    password = sys.argv[4]
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username, password=password)
    client.connect(host, port=port, keepalive=60)
    client.loop_forever()

