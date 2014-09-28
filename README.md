dump1090mqtt
============

Publish [dump1090](http://www.satsignal.eu/raspberry-pi/dump1090.html) output to MQTT

The `topic` is `/adsb/RADAR/ICAOADDR` where 

* `RADAR` is specifed by `--radar` option which is your radar's ID
* `ICAOADDR` is [ICAO 24-bit Aircraft Address](http://en.wikipedia.org/wiki/Aviation_transponder_interrogation_modes#ICAO_24-bit_address)

usage
------

```
$ ./dump1090pub.py --help
Usage: dump1090pub.py [options]

Options:
  -h, --help            show this help message and exit
  -m MQTT_HOST, --mqtt-host=MQTT_HOST
                        MQTT broker hostname
  -p MQTT_PORT, --mqtt-port=MQTT_PORT
                        MQTT broker port number
  -u MQTT_USER, --mqtt-user=MQTT_USER
                        MQTT broker connect user
  -a MQTT_PASSWORD, --mqtt-password=MQTT_PASSWORD
                        MQTT broker connert password
  -H DUMP1090_HOST, --dump1090-host=DUMP1090_HOST
                        dump1090 hostname
  -P DUMP1090_PORT, --dump1090-port=DUMP1090_PORT
                        dump1090 port number
  -r RADAR, --radar-name=RADAR
                        name of radar. used as topic string
                        /adsb/RADAR/icaoaddr
  -c, --console         write out topic and payload to console
  ```

example
---------

```
./dump1090pub.py --radar T-RJTT36
```

