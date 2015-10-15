-- operation.lua
-- operation: Evalua mensajes recibido y ejecuta funciones
function operation(data)
	t = split(data,",")
    
	if t[1] == "1" then
		print("configuracion")
	end
	if t[1] == "2" then
		print("solicitud")
		bh1750 = require("bh1750")
    	bh1750.init(6, 5)
    	bh1750.read(OSS)
		lux = bh1750.getlux()
		bh1750 = nil
    	package.loaded["bh1750"]=nil
        m:publish("control",node.chipid()..",4,"..(lux/100).."."..(lux % 100)..",lux",0,0)
    	lux= nil
	end
	if t[1] == "4" then
		print("Evento")
        local a = tonumber(t[2])
        local b = tonumber(t[3])
		if contains(OUTPUTS,a) and (b == 1 or b == 0) then
            print("GPIO")
		    gpio.write(a,b)
		end
		if PWM == a	then
			dofile("fade.lua")
			currentpwm = fade(5000,b)
			print("PWM")
			fade = nil
			--currentpwm = fade(a, tonumber(t[3]))
		end
        a=nil
        b=nil
	end
	t =nil
end
