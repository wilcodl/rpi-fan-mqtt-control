#!/usr/bin/python3

import RPi.GPIO as GPIO
import paho.mqtt.publish as mqttpub
import paho.mqtt.subscribe as mqttsub
import time
import sys

PIN1 = 11 # On / Off
PIN2 = 12 # Medium
PIN3 = 13 # High
ON = False
OFF = True

MQTT_HOST			= sys.argv[1]
MQTT_SPEED_TOPIC	= "ha/fan/forced_ventilation/speed/state"
MQTT_ON_TOPIC		= "ha/fan/forced_ventilation/on/state"
MQTT_TOPIC_FILTER	= "ha/fan/forced_ventilation/#"
MQTT_ON_SET			= 'ha/fan/forced_ventilation/on/set'
MQTT_SPEED_SET		= 'ha/fan/forced_ventilation/speed/set'

def change_fan(client, userdata, message):
	if message.topic == MQTT_ON_SET:
		value = message.payload.decode("utf-8")
		# print(value)

		if value == 'false':
			print('Off')
			GPIO.output(PIN1, OFF)

			mqttpub.single(MQTT_ON_TOPIC, "false", hostname=MQTT_HOST)
		elif value == 'true':
			print('On')
			GPIO.output(PIN1, ON)

			mqttpub.single(MQTT_ON_TOPIC, "true", hostname=MQTT_HOST)
		else:
			print('Invalid on input')

		time.sleep(0.1)
	
	elif message.topic == MQTT_SPEED_SET:
		value = message.payload.decode("utf-8")

		if value == 'low':
			print('Low')
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_SPEED_TOPIC, "low", hostname=MQTT_HOST)
		elif value == 'medium':
			print('Medium')
			GPIO.output(PIN2, ON)
			GPIO.output(PIN3, OFF)

			mqttpub.single(MQTT_SPEED_TOPIC, "medium", hostname=MQTT_HOST)
		elif value == 'high':
			print('High')
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, ON)

			mqttpub.single(MQTT_SPEED_TOPIC, "high", hostname=MQTT_HOST)
		else:
			print('Invalid speed input')

		time.sleep(0.1)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)

mqttpub.single(MQTT_ON_TOPIC, "false", hostname=MQTT_HOST)
mqttpub.single(MQTT_SPEED_TOPIC, "low", hostname=MQTT_HOST)

try:
	mqttsub.callback(change_fan, MQTT_TOPIC_FILTER, hostname=MQTT_HOST)

except KeyboardInterrupt:
	print("\nKeyboardInterrupt")
  
except:
	print("Other error or exception occurred!")
  
finally:
	mqttpub.single(MQTT_ON_TOPIC, "false", hostname=MQTT_HOST)
	mqttpub.single(MQTT_SPEED_TOPIC, "low", hostname=MQTT_HOST)
	GPIO.cleanup()