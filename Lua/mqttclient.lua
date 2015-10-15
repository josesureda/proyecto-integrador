-- Engineered by MikeV, modded by rutierut

t=require("dht22")

broker = "10.0.1.32"     -- IP or hostname of MQTT broker
mqttport = 1883          -- MQTT port (default 1883)
userID = ""              -- username for authentication if required
userPWD  = ""            -- user password if needed for security
clientID = "ESP1"        -- Device ID
GPIO2 = 4                -- IO Index of GPIO2 which is connected to an LED
count = 0                -- Test number of mqtt_do cycles
mqtt_state = 0           -- State control


wifi.setmode(wifi.STATION)
wifi.sta.config("YOURSSID","YOURPWD")
wifi.sta.connect()


function dhtsensor()
dht22 = require("dht22")
dht22.read(GPIO2)
temp = dht22.getTemperature()
humid = dht22.getHumidity()
end

function mqtt_do()
     count = count + 1  -- For testing number of interations before failure
     
     if mqtt_state < 5 then
          mqtt_state = wifi.sta.status() --State: Waiting for wifi

     elseif mqtt_state == 5 then
     m = mqtt.Client(clientID, 120, userID, userPWD)
          m:connect( broker , mqttport, 0,
          function(conn)
               print("Connected to MQTT:" .. broker .. ":" .. mqttport .." as " .. clientID )
               mqtt_state = 20 -- Go to publish state              
          end)

     elseif mqtt_state == 20 then
          mqtt_state = 25 -- Publishing...
          dhtsensor() -- Getting values
          m:publish("Testtopic","Temperature: "..((temp-(temp % 10)) / 10).."."..(temp % 10).." C, Humidity: "..(humid / 10).."."..(humid % 10).."%", 0, 0,
          function(conn)
              -- Print confirmation of data published
              print(" Sent messeage #"..count.."\nTemp:"..((temp-(temp % 10)) / 10).."."..(temp % 10).."\nHumidity: "..(humid/10).."."..(humid % 10).."\npublished!")
              mqtt_state = 20  -- Finished publishing - go back to publish state.
          end)
     else print("Publishing..."..mqtt_state)
          mqtt_state = mqtt_state - 1  -- takes us gradually back to publish state to retry
     end

end

-- release module
dht22 = nil
package.loaded["dht22"]=nil

tmr.alarm(0, 10000, 1, function() mqtt_do() end) -- convert 10000 to dynamic variable