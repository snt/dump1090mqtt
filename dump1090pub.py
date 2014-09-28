#!/usr/bin/env python

from socket import *
import paho.mqtt.client as paho
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option('-m', '--mqtt-host', dest='mqtt_host', help="MQTT broker hostname", default='127.0.0.1')
parser.add_option('-p', '--mqtt-port', dest='mqtt_port', type="int", help="MQTT broker port number", default=1883)
parser.add_option('-u', '--mqtt-user', dest='mqtt_user', help="MQTT broker connect user", default='')
parser.add_option('-a', '--mqtt-password', dest='mqtt_password', help="MQTT broker connert password", default='')

parser.add_option('-H', '--dump1090-host', dest='dump1090_host', help="dump1090 hostname", default='127.0.0.1')
parser.add_option('-P', '--dump1090-port', dest='dump1090_port', type="int", help="dump1090 port number", default=30003)

parser.add_option('-r', '--radar-name', dest='radar', help="name of radar. used as topic string /adsb/RADAR/icaoaddr", metavar='RADAR')

parser.add_option('-c', '--console', dest='console', action="store_true", help="write out topic and payload to console")

(options, args) = parser.parse_args()

MQTT_HOST=options.mqtt_host
MQTT_PORT=options.mqtt_port
MQTT_USER=options.mqtt_user
MQTT_PASSWORD=options.mqtt_password

DUMP1090_HOST=options.dump1090_host
DUMP1090_PORT=options.dump1090_port

RADAR=options.radar

CONSOLE=options.console

ttc = paho.Client()
if MQTT_USER != '':
  ttc.username_pw_set(MQTT_USER, password=MQTT_PASSWORD)
ttc.connect(MQTT_HOST, MQTT_PORT)

cs = socket(AF_INET, SOCK_STREAM)
cs.connect((DUMP1090_HOST, DUMP1090_PORT))
f = cs.makefile()

line = f.readline()
while line:
  line = line.strip()
  xs = line.split(',')
  topic = "/adsb/%s/%s" % (RADAR, xs[4])
  ttc.publish(topic, line)
  if CONSOLE:
    print topic, line
  line = f.readline()

ttc.disconnect()
f.close()
cs.close()


