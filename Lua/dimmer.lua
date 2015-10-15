currentpwm=0
pwm.setup(2,200,0)
pwm.start(2)
for b=1,2,1 do
for a=0,1023,1 do pwm.setduty(2,a) tmr.delay(1000) tmr.wdclr()  end 

for a=1023,0,-1 do pwm.setduty(2,a) tmr.delay(1000) tmr.wdclr() end 
end