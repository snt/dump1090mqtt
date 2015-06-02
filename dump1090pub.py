#!/usr/bin/env python
"""
Publish dump1090 output to MQTT
"""

from socket import socket, AF_INET, SOCK_STREAM
import paho.mqtt.client as paho


def parse_options():
    """parse command line options
    Return:
      (options, args)
    """

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-m', '--mqtt-host', dest='mqtt_host',
                      help="MQTT broker hostname", default='127.0.0.1')
    parser.add_option('-p', '--mqtt-port', dest='mqtt_port', type="int",
                      help="MQTT broker port number", default=1883)
    parser.add_option('-u', '--mqtt-user', dest='mqtt_user',
                      help="MQTT broker connect user", default='')
    parser.add_option('-a', '--mqtt-password', dest='mqtt_password',
                      help="MQTT broker connert password", default='')
    parser.add_option('-H', '--dump1090-host', dest='dump1090_host',
                      help="dump1090 hostname", default='127.0.0.1')
    parser.add_option('-P', '--dump1090-port', dest='dump1090_port', type="int",
                      help="dump1090 port number", default=30003)
    parser.add_option('-r', '--radar-name', dest='radar',
                      help="name of radar. used as topic string /adsb/RADAR/icaoaddr",
                      metavar='RADAR')
    parser.add_option('-c', '--console', dest='console', action="store_true",
                      help="write out topic and payload to console")
    return parser.parse_args()

def publish():
    """publish to topic /radar/icioaddr with ADS-B feed read from socket"""

    (options, _) = parse_options()

    ttc = paho.Client()
    if options.mqtt_user != '':
        ttc.username_pw_set(options.mqtt_user, password=options.mqtt_password)
    ttc.connect(options.mqtt_host, options.mqtt_port)

    feeder_socket = socket(AF_INET, SOCK_STREAM)
    feeder_socket.connect((options.dump1090_host, options.dump1090_port))
    socket_file = feeder_socket.makefile()

    line = socket_file.readline()
    while line:
        try:
            line = line.strip()
            columns = line.split(',')
            topic = "/adsb/%s/%s" % (options.radar, columns[4])
            ttc.publish(topic, line)
            if options.console:
                print(topic, line)
            line = socket_file.readline()
        except IndexError:
            print('cannot parse line: %s' % line)

    ttc.disconnect()
    socket_file.close()
    feeder_socket.close()

if __name__ == '__main__':
    publish()

