FROM python:3.8-slim

# install necessary dependencies
RUN apt-get update && apt-get install -y \
python3-setuptools \
python3-dev \
gcc \
vim \
git \
net-tools \
mosquitto \
mosquitto-clients

RUN pip3 install Adafruit_DHT paho-mqtt

WORKDIR /app

COPY . .

WORKDIR /app/orangepi0/orangepi_zero_gpio

RUN python3 setup.py install

WORKDIR /app/orangepi0

RUN mv -f opi_sensor.py DHT11-DHT22-Python-library-Orange-PI
RUN mv -f opi_mqtt.py DHT11-DHT22-Python-library-Orange-PI

EXPOSE 1883

WORKDIR /app





