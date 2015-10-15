
import csv
import numpy as np
	

with open('matrix.txt') as f:
    base = [map(int, row) for row in csv.reader(f)]

with open('initialMarking.txt') as f:
    marking = [map(int, row) for row in csv.reader(f)]

with open('backwards.txt') as f:
    backwards = [map(int, row) for row in csv.reader(f)]

initialMarking = np.array(marking)

m0 = np.transpose(initialMarking)
mexp= np.tile(m0,4)
matrix = np.matrix(base)
back = np.matrix(backwards)

matrixand = np.logical_and(mexp,back)
result = mexp-back

#result2 = np.all(result,-1)


print(back)
print(initialMarking)
print(matrix)
#print(mexp)
#print(mexp-back)
#matrix.append([0] *4)
#print(matrix)
#print(matrixand)
#print(result2)

n = np.logical_not(initialMarking)
print(n)
m = np.dot(n,back)
d = np.logical_not(m)
print(m)
print("Disparo:")
print(d)

v = np.dot(matrix,np.transpose(d))

v2 = np.dot(d,np.transpose(matrix))
print(v2)

m1 = initialMarking + v2
print(m1)

tiro = np.matrix("0,1,1,1")
print(tiro)

p = np.matrix("1,0,0,0;0,1,-1,-1;0,0,1,-1;0,0,0,1")
print(p)

r = np.dot(tiro,p,)
print(r)

result = r ==1
fin = result.tostring()


eventos = {fin :'10'}
print(eventos[fin])
print(eventos)

# vector de tipo de transicion
typeVector = [0] * 40

# vector de eventos registrados
eventVector = [0] * 40

# vector de transiciones sensibilizadas
sensibilityVector = [0] * 40

# vector de disparos
launchVector = [0] * 40

# vector de politicas
policyVector = [0] * 40


