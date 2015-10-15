local sensor = require 'sensor'

sen1 = sensor.new("luxometro","I2C",{6,7},"lux")



print(sen1:get_pins()[1])

os.execute 'pause'
