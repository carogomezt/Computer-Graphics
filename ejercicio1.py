import math

class Vector:
	def __init__(self, data):
		self.data = data

	def __str__(self):
		return str(self.data)

	def __getitem__(self, b):
		return self.data[b]

	#Pendiente de una recta
	def slope(self, point):
		return (point[1] - self.data[1]) / (point[0] - self.data[0])

	#Ecuacion de una recta
	def eqLine(self, k):
		b = self.data[1] + (k * -self.data[0])
		if(b >= 0):
			return "y = " + str(k) + "x + " + str(b)
		else:
			return "y = " + str(k) + "x" + str(b)

	#Dado un segmento retorna un vector
	def segtoVect(self, point):
		x = point[0] - self.data[0]
		y = point[1] - self.data[1]
		vec = [x,y]
		return vec

	#Magnitud de un vector
	def lengtofVec(self):
		temp = 0
		for val in self.data:
			temp += val * val
		return math.sqrt(temp)

	#Suma de vectores
	def addVector(self, vect):
		result = []
		for i in range(len(self.data)):
			result.append(self.data[i] + vect[i])
		return result

	#Producto punto
	def dotProduct(self, vect):
		temp = 0
		for i in range(len(self.data)):
			temp += self.data[i] * vect[i]
		return temp

	#Producto escalar
	def scalarProduct(self, k):
		result = []
		for i in range(len(self.data)):
			result.append(self.data[i] * k)
		return result

	#Vector unitario
	def unitVector(self, p):
		result = []
		for val in self.data:
			result.append(val / p)
		return result




a = Vector([3.0, 3.0])
b = Vector([9.0, 6.0])

#print(a.eqLine(a.slope(b)))

p = Vector([2.0 , 3.0])
q = Vector([8.0, 5.0])

#print(p.segtoVect(q))
res = Vector(p.segtoVect(q))
#print(res.lengtofVec())
#print(p.addVector(q))
#print(p.dotProduct(q))
print(p.scalarProduct(2))
p = a.lengtofVec()
print(a.unitVector(p))