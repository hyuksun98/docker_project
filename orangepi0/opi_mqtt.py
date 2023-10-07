from pyA20.gpio import gpio
from pyA20.gpio import port

import os
import dht
import time
import datetime
import paho.mqtt.client as mqtt

MAX_ITER = 30
broker_address = os.environ.get('BROKER','172.20.10.4')
broker_port = 1883 # Default MQTT port

# Initialize GPIO
PIN2 = port.PA6
gpio.init()

# Read data using pin
instance = dht.DHT(pin=PIN2)

# Create a MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

tz = datetime.timezone(datetime.timedelta(hours=9))

while MAX_ITER > 0:
    result = instance.read()
    if result.is_valid():
        print("Timestamp: " + str(datetime.datetime.now(tz=tz).replace(microsecond=0)))
        client.publish("/data/orangepi0", str(result.temperature)+ "/" + str(result.humidity))
        print("Monitor: Temp={0:0.1f}*C, Humidity={1:0.1f}%".format(result.temperature,result.humidity))
        MAX_ITER = MAX_ITER - 1

    time.sleep(1)

client.disconnect()
