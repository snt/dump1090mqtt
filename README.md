dump1090mqtt
============

Publish dump1090 output to MQTT

The `topic` is `/adsb/RADAR/ICAOADDR` where 

* `RADAR` is specifed by `--radar` option which is your radar's ID
* `ICAOADDR` is [ICAO 24-bit Aircraft Address](http://en.wikipedia.org/wiki/Aviation_transponder_interrogation_modes#ICAO_24-bit_address)

example
---------

```
./dump1090pub.py --radar T-RJTT36
```

