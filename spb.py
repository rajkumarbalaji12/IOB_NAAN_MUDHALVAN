import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # Example GPIO pin for occupancy sensor

client = mqtt.Client()
client.on_connect = on_connect
client.connect("your-mqtt-broker", 1883, 60)

try:
    while True:
        if GPIO.input(17):
            print("Occupancy detected")
            client.publish("restroom/occupancy", "occupied")
        else:
            print("Restroom is vacant")
            client.publish("restroom/occupancy", "vacant")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
