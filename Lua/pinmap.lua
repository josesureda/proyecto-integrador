-- mapa de pines GPIO
gpiomap= {[0]=3,[2]=4,[4]=2,[5]=1,[12]=6,[13]=7,[14]=5,[15]=8,[16]=0}

gpio.write(gpiomap[5],1)
gpio.write(gpiomap[4],1)
gpio.mode(gpiomap[5],gpio.OUTPUT)
gpio.mode(gpiomap[4],gpio.OUTPUT)
pwm.setup(2,600,0)
pwm.start(2)