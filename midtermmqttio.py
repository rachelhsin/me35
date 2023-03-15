import paho.mqtt.client as mqtt
import time
import math
from Adafruit_IO import Client

angle1 = [-142.617,-144.088,-148.828,-154.772,-160.172,-163.840,-166.026,-167.242,-168.005,-168.607,-168.835,-168.421,-167.124,-164.919,-162.077,-158.871,-155.527,-152.189,-148.920,-145.769,-142.775,-139.882,-136.948,-133.835,-130.414,-126.755,-123.075,-119.612,-116.610,-114.076,-111.863,-109.812,-107.761,-105.551,-103.017,-99.961,-96.199,-91.979,-87.854,-84.688]
angle2 = [77.948,81.207,88.839,97.884,106.006,111.850,115.883,118.789,121.201,123.466,125.347,126.534,126.730,125.844,124.120,121.821,119.201,116.439,113.626,110.848,108.185,105.570,102.781,99.583,95.746,91.372,86.847,82.610,79.119,76.416,74.257,72.368,70.456,68.229,65.380,61.540,56.391,50.429,44.686,40.691]

#adafruit
io = mqtt.Client()
io.username_pw_set("rachelhsin", "aio_Lakd89gTqqK2k84g7hroY9t1SVxl")
theta1 = io.feeds('theta1')
theta2 = io.feeds('theta2')

#leds
yellow = machine.Pin(26, machine.Pin.OUT)
green = machine.Pin(27, machine.Pin.OUT)
red = machine.Pin(28, machine.Pin.OUT)

red.on()

def on_connect(client, userdata, flags, rc):
    red.off()
    yellow.on()
    print("Connected")
    io.subscribe("rachelhsin/feeds/run")
   
def on_message(io, userdata, iomsg):
    print(str(iomsg.payload))
    if str(iomsg.payload) == "b'2'":
        yellow.off()
        green.on()
        print("Running motor")
        # Call the function to move the motors
        for i in range(len(angle1)):
            start_time = time.time()
            io.send_data(theta1.key, angle1[1])
            io.send_data(theta2.key, angle2[1])

            mqttmsg=(angle1[i],angle2[i])
            print(mqttmsg)
            print("IO Angles sent")
            
            mqttmsg=(angle1[i],angle2[i])
            print(mqttmsg)
            client.publish(topic, str(mqttmsg))
            print("MQTT Angles sent")
            
            yellow.on()
            time.sleep(0.1)
            yellow.off()
            
            time.sleep(3)
        green.off()
        yellow.on()

io.connect("io.adafruit.com", 1883, 60) # adafruit.io
io.on_connect = on_connect
io.on_message = on_message
io.connect("io.adafruit.com", 1883, 60)
io.loop_forever()
client.disconnect()
