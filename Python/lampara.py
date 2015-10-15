from random import randint
from time import clock

State = type("Estado", (object,),{})

class LamparaON(Estado):
	def Execute(self):
		print "Lampara ON"

class LamparaOFF(Estado):
	def Execute(self):
		print "Lampara OFF"

		
class Transicion(object):
	def __init__(self, toState):
		self.toState = toState
	
	def Execute(self):
		print "Transition"
		

		
class FSM(object):
	def __init__(self, maquina):
		self.maquina = maquina
			self.states = {ON