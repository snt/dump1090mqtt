FROM python:3.8.3-alpine3.12

WORKDIR /app
COPY startDump1090pub.sh .
COPY dump1090pub.py .
COPY sub.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["/app/startDump1090pub.sh"]
