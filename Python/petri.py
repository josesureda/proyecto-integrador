"Objeto que contiene las matrices y vectores de la red de Petri"

import numpy as np
import csv

class PetriNet(object):

	def __init__(self,IFile,PFile,m0File,tFile):
		self.loadMatrix(IFile)
		self.loadVector(m0File)
		self.loadPolitics(PFile)
		self.loadAutom(tFile)

	def loadMatrix(self, fileName):
		with open(fileName) as f:
			aux = [map(int, row) for row in csv.reader(f)]
			self.i = np.matrix(aux)
			self.iBackwards = np.dot(self.i == -1,1)
			self.iFordwards = np.dot(self.i == 1,1)

	def loadPolitics(self, fileName):
		with open(fileName) as f:
			aux = [map(int, row) for row in csv.reader(f)]
			self.p = np.matrix(aux)

	def loadVector(self, fileName):
		with open(fileName) as f:
			aux = [map(int, row) for row in csv.reader(f)]
			self.m0 = np.array(aux)

	def loadAutom(self, fileName):
		with open(fileName) as f:
			aux = [map(int, row) for row in csv.reader(f)]
			self.t = np.array(aux)

	def enabledTransitions(self, currentMark):
		aux = np.dot(np.logical_not(currentMark),self.iBackwards)
		return np.dot(aux == 0,1)

	def enabledTransitionsIndex(self, currentMark):
		aux = np.dot(np.logical_not(currentMark),self.iBackwards)
		aux2 = np.dot(aux == 0,1)
		return np.where(aux2 == 1)[1]



