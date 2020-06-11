FROM alpine:latest

RUN apk update
RUN apk add python3 py3-pip
RUN pip install paho-mqtt
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY sh.startDump1090pub /usr/bin
COPY dump1090pub.py /usr/bin
COPY sub.py /usr/bin

ENTRYPOINT ["/usr/bin/sh.startDump1090pub"]

CMD /usr/bin/sh.startDump1090pub
