#pip install requests psutil
import time
import requests
import psutil
import argparse

# constants
URL = 'https://corlysis.com:8086/write'
READING_DATA_PERIOD_MS = 1000.0
SENDING_PERIOD = 5
MAX_LINES_HISTORY = 1000
db="Smart_IronWear"
token="184b4969f985876c1d7f01d0f10b7885"
def main():
	parser = argparse.ArgumentParser()
	#parser.add_argument("db", help="database name")
	#parser.add_argument("token", help="secret token")
	parser.add_argument("temperatura")
	parser.add_argument("humedad")
	parser.add_argument("llama")
	parser.add_argument("pulso")
	args = parser.parse_args()

	corlysis_params = {"db": db, "u": "token", "p": token,"temperatura":args.temperatura,"humedad":args.humedad,"llama":args.llama,"pulso":args.pulso, "precision": "ms"}

	# initialization
	payload = ""
	counter = 1
	problem_counter = 0
	i=0
	# infinite loop
	while i<5:
		unix_time_ms = int(time.time()*1000)
		temperatura=int(args.temperatura)
		humedad= int(args.humedad)
		llama= int(args.llama)
		pulso=int(args.pulso)
		# read sensor data and convert it to line protocol
		line = "server_data temperatura={},humedad={},llama={},pulso={} {}\n".format(temperatura,
																   humedad,llama,pulso,
																   unix_time_ms)

		payload += line

		if counter % SENDING_PERIOD == 0:
			try:
			# try to send data to cloud
				r = requests.post(URL, params=corlysis_params, data=payload)
				if r.status_code != 204:
					raise Exception("data not written")
					payload = ""
			except:
				problem_counter += 1
				#print('cannot write to InfluxDB')
				if problem_counter == MAX_LINES_HISTORY:
					problem_counter = 0
					payload = ""

		counter += 1

		# wait for selected time
		time_diff_ms = int(time.time()*1000) - unix_time_ms
		#print("enviardatos")
		if time_diff_ms < READING_DATA_PERIOD_MS:
			time.sleep((READING_DATA_PERIOD_MS - time_diff_ms)/10000.0)
		i=i+1
		

if __name__ == "__main__":
		main()

