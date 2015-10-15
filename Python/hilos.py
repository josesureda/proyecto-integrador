
import time
import threading



PIR_PIN = 4
RELE_PIN = 17
TIEMPO_APAGADO = 30

rele_status = 0
global contador
contador = 0




class hilo_sensor(threading.Thread):
        def __init__(self):
                threading.Thread.__init__(self)
        def run(self):
                global contador
                while True:
                        contador = 1
                        print "sensando"

class hilo_contador(threading.Thread):
        def run(self):
                while True:
                        print "contando"


hilo1 = hilo_sensor()

hilo2 = hilo_contador()

hilo1.start()
#hilo2.start()

while True:
        print contador

