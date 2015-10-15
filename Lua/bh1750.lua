local moduleName = ... 
local M = {}
_G[moduleName] = M
local GY_30_address = 0x23
local id = 0
local l
local CMD = 0x10
local init = false
local i2c = i2c
function M.init(sda, scl)
    i2c.setup(id, sda, scl, i2c.SLOW)
    init = true
end
local function read_data(ADDR, commands, length)
    i2c.start(id)
    i2c.address(id, ADDR, i2c.TRANSMITTER)
    i2c.write(id, commands)
    i2c.stop(id)
    i2c.start(id)
    i2c.address(id, ADDR,i2c.RECEIVER)
    tmr.delay(200000)
    c = i2c.read(id, length)
    i2c.stop(id)
    return c
end

local function read_lux()
    dataT = read_data(GY_30_address, CMD, 2)

    UT = dataT:byte(1) * 256 + dataT:byte(2)
    l = (UT*1000/12)
    return(l)
end

function M.read()
    if (not init) then
    else
        read_lux()
    end
end

function M.getlux()
    return l
end
return M
