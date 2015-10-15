--fade
function fade(pin, delay, current, value)
	if current <= value then
		for a=current,value,1 do pwm.setduty(pin,a) tmr.delay(delay) tmr.wdclr()  end 
	else
		for a=current,value,-1 do 
			pwm.setduty(pin,a) 
			tmr.delay(delay) 
			tmr.wdclr()
		end
	end 
    currentpwm=value
	return value
end
