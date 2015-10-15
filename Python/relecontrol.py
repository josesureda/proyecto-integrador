import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIR_PIN = 4				//Sensor en GPIO4
RELE_PIN = 17			//Actuador en GPI017
TIEMPO_APAGADO = 30		//Tiempo de espera por movimiento

rele_status = 0
contador = 0

GPIO.setup(PIR_PIN, GPIO.IN)	//Pin de sensor como entrada
GPIO.setup(RELE_PIN, GPIO.OUT)	//Pin de actuador como salida


try:
	print "Modulo Test Control Rele (CTRL+C para salir)"
	
	time.sleep(1)
	print "sensando"
	
	while True:
		if GPIO.input(PIR_PIN):
			print "Movimiento Detectado"
			contador = 0
			
			if(rele_status == 0)
				rele_status = 1
				GPIO.output(RELE_PIN, True)
				print "Lampara ON"
				
		if (contador == TIEMPO_APAGADO):
			GPIO.output(RELE_PIN, False)
			rele_status = 0
			print "Lampara OFF"
			
		
		time.sleep(1)
		contador = contador + 1
		print contador
	
except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()