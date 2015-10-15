gpio.mode(5,gpio.INT)
counter = 0
time = 20

function pir()
    counter = 0
    err = pcall(function () 
    m:publish("control",node.chipid()..",4,1,1",0,0)
    end)
end

gpio.trig(5, "up",pir)

tmr.alarm(0, 1000, 1, function()
    if counter < time then
        counter = counter + 1
        elseif counter == time then
            err = pcall(function () 
            m:publish("control",node.chipid()..",4,1,0",0,0)
            end)
            counter = time + 1
        end

        end)
