import os
import signal
import json
import paho.mqtt.client as mqtt

broker = os.environ.get('BROKER', '')
port = int(os.environ.get('PORT', '1883'))
topic_list = os.environ.get('TOPICS', '[]')
new_topic_suffix = os.environ.get('NEW_TOPIC_SUFFIX', '_1')
qos = int(os.environ.get('QOS', '0'))
debug = bool(os.environ.get('DEBUG', 'false'))

timelive=60

if debug:
    print('TOPICS json: ' + topic_list)
    topics = json.loads(topic_list)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for topic in topics:
        print("Subscribing to topic: " + topic)
        client.subscribe(topic, qos)

def on_message(client, userdata, msg):
    new_topic = msg.topic + new_topic_suffix
    if debug:
        print("Got message '" + msg.payload.decode('utf-8') + "' from '"+ msg.topic +"', resending on " + new_topic)
    client.publish(new_topic, msg.payload)

def signal_handler(sig, frame):
    print("Disconnecting and exiting...")
    client.disconnect()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
