#!/usr/bin/python3

import RPi.GPIO as GPIO
import paho.mqtt.publish as mqttpub
import paho.mqtt.subscribe as mqttsub
import time
import sys
import yaml

with open("config.yml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

PIN1 = cfg['pinout']['PIN1'] # On / Off
PIN2 = cfg['pinout']['PIN2'] # Medium
PIN3 = cfg['pinout']['PIN3'] # High

ON = False
OFF = True

MQTT_HOST			= cfg['mqtt']['host']
MQTT_SPEED_TOPIC	= cfg['mqtt']['topic_prefix'] + "/speed/state"
MQTT_ON_TOPIC		= cfg['mqtt']['topic_prefix'] + "/on/state"
MQTT_TOPIC_FILTER	= cfg['mqtt']['topic_prefix'] + "/#"
MQTT_ON_SET			= cfg['mqtt']['topic_prefix'] + '/on/set'
MQTT_SPEED_SET		= cfg['mqtt']['topic_prefix'] + '/speed/set'

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

print("rPi Fan MQTT Control v0.1")

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