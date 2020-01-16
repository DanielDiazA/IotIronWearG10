import time
import seeed_dht
import os
import RPi.GPIO as GPIO
import smbus
import logging

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
	fin = False
	print("\n")
	print(bcolors.HEADER+bcolors.BOLD+"	    /       ||   \/   |     /   \     |   _  \     |           |")                            
	print("	   |   (----`|  \  /  |    /  ^  \    |  |_)  |    `---|  |----`")                              
	print("	    \   \    |  |\/|  |   /  /_\  \   |      /         |  |     ")                              
	print("	    -)   |   |  |  |  |  /  _____  \  |  |\  \----.    |  |     ")                             
	print("	|_______/    |__|  |__| /__/     \__\ | _| `._____|    |__|     ")                             
			                                                                              
	print(" __  .______        ______   .__   __. ____    __    ____  _______      ___      .______  ")    
	print("|  | |   _  \      /  __  \  |  \ |  | \   \  /  \  /   / |   ____|    /   \     |   _  \ ")  
	print("|  | |  |_)  |    |  |  |  | |   \|  |  \   \/    \/   /  |  |__      /  ^  \    |  |_)  |")    
	print("|  | |      /     |  |  |  | |  . `  |   \            /   |   __|    /  /_\  \   |      / ")   
	print("|  | |  |\  \----.|  `--'  | |  |\   |    \    /\    /    |  |____  /  _____  \  |  |\  \ ")
	print("|__| | _| `._____| \______/  |__| \__|     \__/  \__/     |_______|/__/     \__\ | _| `._____|"+bcolors.ENDC)
	
	print("\n\n")
	print(bcolors.HEADER+"----------Iniciando Smart IronWear----------")
	print("--------------------------------------------"+bcolors.ENDC)
	while not fin:
		log = ""
		
		print("\n")
		print("Iniciando lectura de sensores...")
		
		tempHumi = []
		tempHumi = calcTemp()
		temperatura = tempHumi[0]
		humedad = tempHumi[1]
		while temperatura == 0.0 or humedad == 0.0:
			print(bcolors.FAIL+"Fallo en el sensor, recalculando..."+bcolors.ENDC)
			tempHumi = calcTemp()
			temperatura = tempHumi[0]
			humedad = tempHumi[1]
		
		print(bcolors.OKGREEN+"-Lectura completada"+bcolors.ENDC)
			
		print(bcolors.OKBLUE+"Sensor de llama"+bcolors.ENDC)
		os.system ("python3 scripts/flame.py")
		print(bcolors.OKGREEN+"-Lectura completada"+bcolors.ENDC)
		
		print(bcolors.OKBLUE+"Sensor de pulso cardiaco"+bcolors.ENDC)
		os.system ("python3 scripts/heart.py > scripts/data/pulso.txt")
		print(bcolors.OKGREEN+"-Lectura completada"+bcolors.ENDC)
			
		# Lectura de datos recolectados desde los ficheros
		file = open("scripts/data/flame.txt", "r")
		llama = file.readline().strip('\n')
		llamaInt=int(llama)
		
		file = open("scripts/data/pulso.txt", "r")
		pulso = file.readline().strip('\n')
		pulsoInt = int(pulso)
		
		# Encendido de LEDs
		if 	pulsoInt > 140 or pulsoInt < 45:
			os.system("python3 scripts/led.py 18 > /dev/null 2>&1 &")
			if 	pulsoInt > 140:
				print(bcolors.WARNING+"WARNING: Pulso cardiaco superior a los valores recomendados."+bcolors.ENDC)
			if 	pulsoInt < 45:
				print(bcolors.WARNING+"WARNING: Pulso cardiaco inferior a los valores recomendados."+bcolors.ENDC)
			
		if llamaInt == 1:
			os.system("python3 scripts/led.py 16 > /dev/null 2>&1 &")
			print(bcolors.WARNING+"WARNING: Fuego detectado."+bcolors.ENDC)
			
		if humedad > 75 or temperatura > 33:
			os.system("python3 scripts/led.py 5 > /dev/null 2>&1 &")
			if humedad > 75:
				print(bcolors.WARNING+"WARNING: Humedad superior a lo valores seguros."+bcolors.ENDC)
			if temperatura > 33:
				print(bcolors.WARNING+"WARNING: Temperatura superior a lo valores seguros."+bcolors.ENDC)
		
		
		t=str(temperatura)
		h=str(humedad)
		p=str(pulso)
		l=str(llama)
		print("\n")
		print("Valores obtenidos:")
		print(bcolors.UNDERLINE+"Temperatura: "+t+"º, Humedad: "+h+"%, Fuego: " +l+", Frecuencia cardiaca: "+p+"ppm"+bcolors.ENDC)
		print("\n")
		print(bcolors.BOLD+bcolors.UNDERLINE+"Actualizando Log..."+bcolors.ENDC)
		log = "Temperatura: " + t+ "\n" + "Humedad: " + h + "\n" + "Frecuencia cardiaca: " + p
		if llamaInt == 1:
			log = log + "\n" + "Fuego detectado Peligro.\n"
		else:
			log = log + "\n" + "No se detecta fuego.\n\n"		
		
		log = log + time.strftime("%d/%m/%y") + "\n" + time.strftime("%H:%M:%S") + "\n\n\n\n"
		
		try:
			file = open("scripts/log/log.txt", "a+")
			file.write(log)
			print(bcolors.OKGREEN+"Log actualizado"+bcolors.ENDC)
			
			print("\n")
			s="python3 scripts/bd.py "+t+" " +h+" " +l+" "+p
			os.system ("python3 scripts/bd.py "+t+ " " +h+" " +l+" " +p )
			
			print(bcolors.BOLD+bcolors.OKGREEN+"Datos guardados en la BD"+bcolors.ENDC)
			print("\n")
		except IOError:
			print(bcolors.FAIL+"No se ha podido guardar"+bcolors.ENDC)
			print("\n")
		print(bcolors.HEADER+"--------------------------------------------"+bcolors.ENDC)	
		time.sleep(7)
		
		
def calcTemp():
	print(bcolors.OKBLUE+"Sensor de temperatura y humedad"+bcolors.ENDC)
	sensor = seeed_dht.DHT("11", 12)
	tempHumi = []
	humi, temp = sensor.read()
	tempHumi.append(temp)
	tempHumi.append(humi)
	return tempHumi
	


if __name__ == '__main__':
	main()
