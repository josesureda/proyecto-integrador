--init.lua

require("config")


-- connectAP: Intenta conectar con AP cada 1000 milisegundos
-- retuns: nil
function connectAP()	
	wifi.sta.config("pepowifi","clavesegura")
	wifi.sta.connect()
	tmr.alarm(1, 1000, 1, function()
		if wifi.sta.getip()== nil then
			print("IP no disponible...")
		else
			tmr.stop(1)
			currentState = connectMQTT
		end
	end)
end

-- connectAP: Intenta conectar con broker
-- retuns: nil
function connectMQTT()
	if wifi.sta.status() == 5 then
		m = mqtt.Client(clientID, 120, userID, userPWD)
		m:connect(broker, mqttport, 0, function ()
			print("conectado con broker")
			mqtt_state = 1
			currentState = listen
		end)
	else
		currentState = connectAP
	end
end

function listen()
	print("escuchando")
end

states = {connectAP, connectMQTT, listen, proactive, reactive}

-- getState: Establece un estado
-- returns: estado
function getState(option)
	return states[option];
end 

currentState = getState(1)
mqtt_state = 0


tmr.alarm(0, 1000, 1, function() currentState() end)