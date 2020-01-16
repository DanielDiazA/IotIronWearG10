#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


i=0
llama =0


def callback(channel):
	global llama
	#print("flame detected")
	llama=1
	
	
    
def devLlama():
	file = open("scripts/data/flame.txt", "w+")
	global llama
	if llama==1:
		llamaS = str(llama)
		file.write(llamaS)
		file.close()
		llama=0
	else:
		llamaS = str(llama)
		
		file.write(llamaS)
		file.close()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel,callback)  # assign function to GPIO PIN, Run function on change

while i<5:
	devLlama()
	time.sleep(0.5)
	i=i+1
