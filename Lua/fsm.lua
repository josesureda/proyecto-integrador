currentpwm = 0

-- connAP: Inicia la coneccion con AP
-- retuns: nil
function connAP()
	wifi.sta.config(APSSID,APPWD)
	wifi.sta.connect()
	currentState = waitAP
end

-- waitAP: Espera a que se restablezca el enlace con AP
function waitAP()
	if wifi.sta.getip()== nil then
		print("IP no disponible...")
	else
		currentState = connMQTT
	end
end

-- connAP: Intenta conectar con broker
-- retuns: nil
function connMQTT()
	if wifi.sta.status() == 5 then
		m = mqtt.Client(clientID, 120, userID, userPWD)
		m:connect(MQTTIP, MQTTPORT, 0, function ()
			print("conectado con broker")
			currentState = subscribe
		end)

	else
		currentState = connAP
	end
end

-- Events: inicia la deteccion de eventos.
function events()
	m:on("offline", function ()
		print("desconectado")
		restart()
		end)

	m:on("message",function(conn, topic, data) 
		print("llego mensaje")
		tmr.delay(1000)
		dofile("operation.lua")
		operation(data)

		operation = nil
		
		end)
end

-- subscribe: se subscribe a los temas MQTT
function subscribe()
	if wifi.sta.status() == 5 then
	print(state)
	m:subscribe(node.chipid(), 0, function()	
		print("subcripto")
		end)

	events()
    events = nil

	tmr.stop(0)
	else
		currentState = connAP
	end
end

function restart()
	tmr.alarm(0, 1000, 1, function() 
	currentState() end)
end
