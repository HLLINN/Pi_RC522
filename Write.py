#!/usr/bin/env python
import RPi.GPIO as GPIO
#import SimpleMFRC522
from mfrc522 import SimpleMFRC522
#reader = SimpleMFRC522.SimpleMFRC522()
reader = SimpleMFRC522()
try:
	
 text = raw_input('New data:')
 print("Now place your tag to write")
 reader.write(text)
 print("Written")
finally:
 GPIO.cleanup()
