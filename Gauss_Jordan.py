#This is a Gauss Jordan python implementation, it can be used to find solutions for 3x3 linear transformations or system of equations, i enjoyed coding this.
#Note that Ax=v, x is the solution we're looking for
A = [[0 for i in range(3)] for j in range(3)]
v = []
for i in range(3):
	for j in range(3):
		q = input("put the {},{} entry: ".format(i,j))
		A[i][j] = int(q)
#the v VECTOR
for i in range(3):
	q = input("put v element: ")
	v.append(int(q))

class comp():
	def multiple(self, x, i):
		Diag = A[x][x]
		notDiag = A[i][x]
		if(Diag != 0 and notDiag != 0):
			div = notDiag / Diag
			if(div > 0 ):
				sign = -1
			else:
				sign = 1
			div = abs(div)
			for b in range(3):
				A[i][b] = (div * sign* A[x][b]) + A[i][b]
			v[i] = (div * sign* v[x]) + v[i]
	def divide(self, x):
		for i in range(3):
			if(i != x):
				self.multiple(x, i)
	def cleanup(self, x):
		v[x] = v[x] / A[x][x]
		A[x][x] = 1

class  main():
	c = comp()
	#COMPUTATION
	for x in range(3):
		c.divide(x)
	for x in range(3):
		c.cleanup(x)
	print("The solution to the system of equations is:")
	print(v)
