from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(44)

	def getA(self):
		return super().getAsInt(0, 4)

	def setA(self, value, isRounded):
		return super().setAsInt(0, 4, value, isRounded)

	def getB(self):
		return super().getAsInt(4, 4)

	def setB(self, value, isRounded):
		return super().setAsInt(4, 4, value, isRounded)

	def getC(self):
		return super().getAsInt(8, 4)

	def setC(self, value, isRounded):
		return super().setAsInt(8, 4, value, isRounded)

	def getD(self):
		return super().getAsInt(12, 4)

	def setD(self, value, isRounded):
		return super().setAsInt(12, 4, value, isRounded)

	def getE(self):
		return super().getAsInt(16, 4)

	def setE(self, value, isRounded):
		return super().setAsInt(16, 4, value, isRounded)

	def getF(self):
		return super().getAsInt(20, 4)

	def setF(self, value, isRounded):
		return super().setAsInt(20, 4, value, isRounded)

	def getG(self):
		return super().getAsInt(24, 4)

	def setG(self, value, isRounded):
		return super().setAsInt(24, 4, value, isRounded)

	def getNUM3(self):
		return super().getAsFloat(28, 3)

	def setNUM3(self, value, isRounded):
		return super().setAsFloat(28, 3, value, isRounded, '9.99')

	def getNUM2(self):
		return super().getAsInt(31, 4)

	def setNUM2(self, value, isRounded):
		return super().setAsInt(31, 4, value, isRounded)

	def getNUM5(self):
		return super().getAsInt(35, 5)

	def setNUM5(self, value, isRounded):
		return super().setAsInt(35, 5, value, isRounded)

	def getNUM2_1(self):
		return super().getAsInt(40, 4)

	def setNUM2_1(self, value, isRounded):
		return super().setAsInt(40, 4, value, isRounded)

	def initialize(self):
		self.setA(10,False)
		self.setB(20,False)
		self.setC(0,False)
		self.setD(0,False)
		self.setE(0,False)
		self.setF(0,False)
		self.setG(0,False)
		self.setNUM3(20.0,False)
		self.setNUM2(20,False)
		self.setNUM5(20,False)
		self.setNUM2_1(40,False)
		pass
    print('Initial Values: A=', A, ' B=', B, ' C=', C, ' D=', D, ' E=', E, ' F=', F)
    setB(getB() * getA())
    print('After MULTIPLY A BY B: A=', A, ' B=', B)
    setA(getA() * 2, True)
    setB(getB() * 2)
    print('After MULTIPLY 2 BY A B: A=', A, ' B=', B)
    setC(3 * getA())
    print('After MULTIPLY 3 BY A GIVING C: C=', C)
    setD(4 * getA(), True)
    print('After MULTIPLY 4 BY A GIVING D ROUNDED: D=', D)
    setE(getA() * 2, True)
    setF(getA() * 2, True)
    print('After MULTIPLY A BY 2 GIVING E F: E=', E, ' F=', F)
    setNUM3(getNUM3() * getNUM5(), True)
