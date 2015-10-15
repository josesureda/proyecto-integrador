# coding=utf-8

import os
import sys
import time
import termios
import json
import pickle

import MQTT
import numpy as np
import petri
import state

def main():
	endMain = False
	#os.system('clear')
	print(" Cargando red de Petri por defecto...\n")
	redPetri = petri.PetriNet('I','P','m0','T')
	d = np.dot(redPetri.t,0)
	state.systate['eventos'] = np.dot(redPetri.t,0)
	e = np.dot(redPetri.t,0)
	mi = redPetri.m0
	print("Matriz de Incidencia:")
	print(redPetri.i)
	print("")
	print("Matriz de Incidencia Backwards:")
	print(redPetri.iBackwards)
	print("")
	print("Matriz de Incidencia Fordwards:")
	print(redPetri.iFordwards)
	print("")
	print("Matriz de Politicas:")
	print(redPetri.p)
	print("")
	print("Vector de marcado inicial M0:")
	print(redPetri.m0)
	print("")
	print("Vector de transiciones automaticas:")
	print(redPetri.t)
	print("")
	print("Transiciones sensibilizadas:")
	print(redPetri.enabledTransitions(redPetri.m0))
	print("")
	print("Vector eventos:")
	print(e)
	print("")
	print("Vector de disparo:")
	print(d)
	d = np.dot(redPetri.t,redPetri.p)
	print(d)
	print("")
	print("Indice de disparo:")
	print(np.where(d == 1)[1])
	#print(redPetri.enabledTransitionsIndex(redPetri.m0))
	print("")
	#petris = str(redPetri.enabledTransitions(redPetri.m0))
	#print(petris)


	print(" GESTION DE ILUMINACION\n")
	print(" 1 - Ver lista de sensores")
	print(" 2 - Ver lista de actuadores")
	print(" 3 - Control manual")
	print(" 4 - Control automatico")
	print(" 5 - Salir\n")

	#d = {1: {'16560579':'4,4','nodeID':'4,3'}, 2: {'A1':'id,4,4'}};


	actuadores = {}

	actuadores['A1'] = {'IdNodo':'16560579', 'IdActuador':'1'}
	actuadores['A2'] = {'IdNodo':'16560579', 'IdActuador':'2'}

	while not endMain:
		try:
			termios.tcflush(sys.stdin, termios.TCIOFLUSH) # Limpiamos el stdin
			optionSelected = raw_input()
			# Opcion 1 - Ver Sensores
			if optionSelected is '1':
				print("Lista de Sensores:")
				#MQTT.client.publish("16560579","4,1,0")

			# Opcion 2 - Ver actuadores
			elif optionSelected is '2':
				print("Lista de Actuadores:")
				for keys,values in actuadores.items():
					print(str(keys) + " - "+str(values))

			# Opcion 3 - Control manual actuador
			elif optionSelected is '3':
				print("Ingrese IdActuador:")
				IdNodo = raw_input()
				print("Ingrese valor:")
				valueActuador = raw_input()
				try:
					MQTT.client.publish(actuadores[IdNodo]['IdNodo'], "4," + actuadores[IdNodo]['IdActuador'] + "," + valueActuador)
				except:
					print('No se registra un actuador con Id:'+IdNodo)

			# Opcion 4 - Control manual actuador
			elif optionSelected is '4':
				while True:
					print("------------------------------------------")
					time.sleep(1)
					#print("Ingrese Evento:")
					#index= raw_input()
					e = state.systate['eventos']
					print("Vector de Eventos:")
					print(e)
					st = redPetri.enabledTransitions(mi)
					et = np.logical_or(e,redPetri.t)
					state.systate['eventos'] = np.dot(redPetri.t,0)
					print("Vector transiciones sensibilizadas:")
					print(et)
					et = np.logical_and(et,st)
					et = np.dot(et,1)
					d = np.dot(et,redPetri.p)
					print("Vector de disparos posibles:")
					print(et)
					print("Vector de prioridades:")
					print(d)
					dv = np.dot(redPetri.t,0)
					try:
						dv[0,np.where(d == 1)[1][0,0]] = 1
					except:
						pass
					print("Vector de disparo a realizar:")
					print(dv)
					#print(redPetri.i)
					mi = mi + np.dot(dv,np.transpose(redPetri.i))
					print("Vector de marcado resultante:")
					print (mi)
					print("------------------------------------------")

					try:
						disparo = str(np.where(d == 1)[1][0,0])
					except:
						pass


					#print(disparo)

					try:
						MQTT.client.publish(state.outEvents[disparo]['IdNodo'], "4," + state.outEvents[disparo]['IdActuador'] + "," + state.outEvents[disparo]['value'])
					except:
						pass


			

			# Opcion 4 - Salir
			elif optionSelected is '5':
				endMain = True
				MQTT.client.loop_stop()
			# Opcion inválida
			else:
				print("Opción inválida!")
		except KeyboardInterrupt:
			endMain = True

if __name__ == '__main__':
	main() 
