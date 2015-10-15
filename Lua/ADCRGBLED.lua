
-- Sensor de luz en ADC(0), RGB LED conectado a gpio12(6) Green, gpio13(7) Blue & gpio15(8) Red.

function led(r,Sg,b) 
    pwm.setduty(8,r) 
    pwm.setduty(6,g) 
    pwm.setduty(7,b) 
end
 
function pseudoSin (idx)
    idx = idx % 128
    lookUp = 32 - idx % 64
    val = 256 - (lookUp * lookUp) / 4
    if (idx > 64) then
        val = - val;
    end
    return 256+val
end

pwm.setup(6,500,512) 
pwm.setup(7,500,512) 
pwm.setup(8,500,512)
pwm.start(6) 
pwm.start(7) 
pwm.start(8)

tmr.alarm(1,20,1,function() 
	idx = 3 * adc.read(0) / 2
  r = pseudoSin(idx)
  g = pseudoSin(idx + 43)
  b = pseudoSin(idx + 85)
	led(r,g,b)
	idx = (idx + 1) % 128		
	end)