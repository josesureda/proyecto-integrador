local sensor = require 'nodo'

i = sensor.new("PIR","GPIO")

print(i:get_nombre())

print(i:get_tipo())

os.execute 'pause'
