import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO17 como salida
GPIO.setup(27, GPIO.OUT) ## GPIO27 como salida

def blink():
        print "Inicio programa..."
        iteracion = 0
        while iteracion < 30:
                GPIO.output(17, True) ## Enciendo el 17
                GPIO.output(27, False) ## Apago el 27
                time.sleep(1)
                GPIO.output(17, False) ## Apago el 17
                GPIO.output(27, True) ## Enciendo el 27
                time.sleep(1)
                iteracion++
        print "Ejecucion finalizada"
        GPIO.cleanup() ## Restablece GPIO a valores por defecto
		

	
blink()