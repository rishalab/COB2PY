from Program import Program
class converted(Program):
	def getA(self):
		return super().getAsInt(0,4)

	def setA(self,value,isRounded):
		return super().setAsInt(0,4,value,isRounded)

	def getB(self):
		return super().getAsInt(4,4)

	def setB(self,value,isRounded):
		return super().setAsInt(4,4,value,isRounded)

	def getC(self):
		return super().getAsInt(8,4)

	def setC(self,value,isRounded):
		return super().setAsInt(8,4,value,isRounded)

	def getD(self):
		return super().getAsInt(12,4)

	def setD(self,value,isRounded):
		return super().setAsInt(12,4,value,isRounded)

	def getE(self):
		return super().getAsInt(16,4)

	def setE(self,value,isRounded):
		return super().setAsInt(16,4,value,isRounded)

	def getF(self):
		return super().getAsString(20,4)

	def setF(self,value):
		return super().setAsString(20,4,value)

	def getNUM3(self):
		return super().getAsFloat(24,3)

	def setNUM3(self,value,isRounded):
		return super().setAsFloat(24,3,value,isRounded,'9.99')

	def getNUM2(self):
		return super().getAsInt(27,4)

	def setNUM2(self,value,isRounded):
		return super().setAsInt(27,4,value,isRounded)

	def getNUM5(self):
		return super().getAsInt(31,5)

	def setNUM5(self,value,isRounded):
		return super().setAsInt(31,5,value,isRounded)

	def getNUM2_1(self):
		return super().getAsInt(36,4)

	def setNUM2_1(self,value,isRounded):
		return super().setAsInt(36,4,value,isRounded)

B += A 
print('A + B = ', B)
C += A + B + 50 
E += A + B + 50 
print('A + B + C = ', C, E)
D = A + C + B 
E = A + C + B 
print('A + B giving D = ', D, E)
E += 50 
print('50 + E = ', E)
D = C - (A + B)
E = C - (A + B)
print(D, E)
print('NUM1 + NUM1 = ', NUM1OFGROUP-2)
print('NUM2 + NUM2 = ', NUM2OFGROUP-2)
