import paho.mqtt.client as mqtt
import time

broker_address = "192.168.200.136"
broker_port = 1883

temp = 0.0
humid = 0.0

topics = ["/data/raspberrypi4", "/data/orangepi0"]

def on_message(client, userdata, message):
    global temp, humid
    topic = message.topic
    payload = message.payload.decode()
    payload_string = payload.split('/')

    temp = float(payload_string[0])
    humid = float(payload_string[1])

    print("Topic={}, Temp={:0.1f}*C, Humidity={:0.1f}%".format(topic, temp, humid))


client = mqtt.Client()

client.on_message = on_message

client.connect(broker_address, broker_port)

for t in topics:
    client.subscribe(t)

client.loop_forever()
