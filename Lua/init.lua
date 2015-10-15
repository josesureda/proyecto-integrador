-- init.lua

dofile("config.lua")
dofile("functions.lua")
dofile("fsm.lua")

wifi.setmode(WIFIMODE)
connAP()
currentState = waitAP
restart()






