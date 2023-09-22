import os
import Adafruit_DHT as dht
import time
import datetime
import paho.mqtt.client as mqtt


MAX_ITER = 30

#selected_sensor = dht.DHT11
selected_sensor = dht.DHT11

if os.uname()[4].startswith("aarch64"):
    DHT_PIN = 4
else:
    raise Exception("Unsupported platform")


tz = datetime.timezone(datetime.timedelta(hours=9))


while MAX_ITER > 0:
    humidity, temperature = dht.read_retry(selected_sensor, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Timestamp: " + str(datetime.datetime.now(tz=tz).replace(microsecond=0)))
        print("Monitor: Temp={0:0.1f}*C, Humidity={1:0.1f}%".format(temperature,humidity))
        MAX_ITER = MAX_ITER - 1
    else:
        print("Monitor: Failed to retrieve sensor data..")

    time.sleep(1)


