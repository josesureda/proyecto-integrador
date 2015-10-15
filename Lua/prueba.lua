--prueba
-- config.lua
-- Archivo de configuracion
broker = "192.168.0.101"
SSID = "pepowifi"
APPWD = "clavesegura"
mqttport = 1883
userID = ""
userPWD  = ""
clientID = "ESP1"
actuador1 = 5
actuador2 = 4
sensorbh1750 = true

function split(source, delimiters)
	local elements = {}
	local pattern = '([^'..delimiters..']+)'
	string.gsub(source, pattern, function(value) elements[#elements + 1] =     value;  end);
	return elements
end


wifi.sta.config(SSID,APPWD)
wifi.sta.connect()
currentState = waitAP
m = mqtt.Client(clientID, 120, userID, userPWD)
m:connect(broker, mqttport, 0, function ()
	print("conectado con broker")
end)


m:subscribe(node.chipid(), 0, function()	
	print("subcripto")
end)


m:on("offline", function ()
	print("desconectado")
	restart()
end)

m:on("message",function(conn, topic, data) 
	print("llego mensaje")
	tmr.delay(1000)
	operation(data)
	
end)
