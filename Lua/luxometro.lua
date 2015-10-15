tmr.alarm(0, 1000, 1, function()

    SDA_PIN = 6 -- sda pin, GPIO12
    SCL_PIN = 5 -- scl pin, GPIO14

    bh1750 = require("bh1750")
    bh1750.init(SDA_PIN, SCL_PIN)
    bh1750.read(OSS)
    l = bh1750.getlux()
    print("lux: "..(l / 100).."."..(l % 100).." lx")

    -- release module
    bh1750 = nil
    package.loaded["bh1750"]=nil

end)
