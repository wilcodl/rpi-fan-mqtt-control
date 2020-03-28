#!/usr/bin/python3

import RPi.GPIO as GPIO
import yaml

with open("config.yml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

PIN1 = cfg['pinout']['PIN1'] # On / Off
PIN2 = cfg['pinout']['PIN2'] # Medium
PIN3 = cfg['pinout']['PIN3'] # High
ON = False
OFF = True

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN3, GPIO.OUT, initial=GPIO.HIGH)

print("0: Off\n1: Low\n2: Medium\n3: High\nq: Quit")

try:
	while True:
		mode = input("Mode: ")

		if mode == '0':
			print('Off')
			GPIO.output(PIN1, ON)
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, OFF)
		elif mode == '1':
			print('Low')
			GPIO.output(PIN1, OFF)
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, OFF)
		elif mode == '2':
			print('Medium')
			GPIO.output(PIN1, OFF)
			GPIO.output(PIN2, ON)
			GPIO.output(PIN3, OFF)
		elif mode == '3':
			print('High')
			GPIO.output(PIN1, OFF)
			GPIO.output(PIN2, OFF)
			GPIO.output(PIN3, ON)
		elif mode == 'q':
			break
		else:
			print('Invalid input')

except KeyboardInterrupt:
	print("\nKeyboardInterrupt")
  
except:
	print("Other error or exception occurred!")
  
finally:
	GPIO.cleanup()
