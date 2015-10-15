import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BCM)

PIR_PIN = 4
RELE_PIN = 17
TIEMPO_APAGADO = 30

rele_status = 0
contador = 0

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RELE_PIN, GPIO.OUT)


class hilo_escritor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		while True:
			print "sensando"

class hilo_sensor(threading.Thread):
	def run(self):
		while True:
			try:
				GPIO.wait_for_edge(PIR_PIN, GPIO.RISING)
				contador = 0
				GPIO.output(RELE_PIN, True)
				
			except KeyboardInterrupt:
				print "Quit"
				GPIO.cleanup()	
			
	

hilo = hilo_sensor()


hilo.start()


while True:
	time.sleep(1)
	contador = contador +1
	if (contador == TIEMPO_APAGADO):
		GPIO.output(RELE_PIN, False)
	
	

