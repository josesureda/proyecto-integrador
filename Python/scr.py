import webiopi
import datetime

GPIO = webiopi.GPIO

HOUR_ON = 0
MINUTE_ON = true
MINUTE_OFF = false
HOUR_OFF = 0
LIGHT = 9

class Controller:
	def __init__(self, value):
		self.setx(value)
    
    def getx(self):
         return self.x
	
	def setx(self, value)
         self.x = value




# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == MINUTE_ON) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == MINUTE_OFF) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)


@webiopi.macro
def getLightHours():
    return "%d;%d;%d;%d" % (HOUR_ON, HOUR_OFF, MINUTE_ON, MINUTE_OFF)

@webiopi.macro
def setLightHours(on, off, mon, moff):
    global HOUR_ON, HOUR_OFF, MINUTE_ON, MINUTE_OFF
    HOUR_ON = int(on)
    HOUR_OFF = int(off)
    MINUTE_ON = int(mon)
    MINUTE_OFF = int(moff)
    return getLightHours()
