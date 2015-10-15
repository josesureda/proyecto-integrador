import json

with open('outEvents.json') as outFile:
	outEvents = json.load(outFile)

with open('inEvents.json') as inFile:
	inEvents = json.load(inFile)

systate = {
	'eventos':0
}