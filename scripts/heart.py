import time,sys
import RPi.GPIO as GPIO
import smbus
import random

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

i=0
class grove_fingerclip_heart_sensor:
	address = 0x50

	def pulse_read(self):
		
		#print(bus.read_byte(0x50))
		#print(bus.read_i2c_block_data(self.address, 1,1))
		#print(bus.read_i2c_block_data(self.address, 1,1))
		#block = bus.read_i2c_block_data(self.address,4)
		print("x")

if __name__ == "__main__":		
	#pulse= grove_fingerclip_heart_sensor()
	
	while i==0:
		try:
			#pulse.pulse_read()
			x=(random.randint(1, 100))
			if x >=85:
				print(random.randint(150,160))
			else:
				print(random.randint(50,85))
			i=i+1
		except IOError:
			print("Error")
		time.sleep(0.5)

