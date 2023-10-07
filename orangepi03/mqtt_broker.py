import paho.mqtt.client as mqtt
import time
import os
import sqlite3

broker_address = os.environ.get('BROKER','172.20.10.4')
broker_port = 1883

temp = 0.0
humid = 0.0

topics = ["/data/raspberrypi4", "/data/orangepi0"]

conn = sqlite3.connect('/app/orangepi03/data/broker.db')

cursor = conn.cursor()


def on_message(client, userdata, message):
    global temp, humid, cursor, conn
    topic = message.topic
    payload = message.payload.decode()
    payload_string = payload.split('/')

    temp = float(payload_string[0])
    humid = float(payload_string[1])

    cursor.execute('INSERT INTO dht (topic, temperature, humidity) VALUES (?, ?, ?)', (topic, temp, humid))

    conn.commit()

    print("Topic={}, Temp={:0.1f}*C, Humidity={:0.1f}%".format(topic, temp, humid))




client = mqtt.Client()

client.on_message = on_message

client.connect(broker_address, broker_port)

for t in topics:
    client.subscribe(t)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("The user terminated a program.")
finally:
    conn.close()
    client.disconnect()
