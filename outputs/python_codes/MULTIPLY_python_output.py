from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(44)

	def getA(self):
		return super().getAsInt(0, 4)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded)

	def getB(self):
		return super().getAsInt(4, 4)

	def setB(self, value, isRounded=False):
		return super().setAsInt(4, 4, value, isRounded)

	def getC(self):
		return super().getAsInt(8, 4)

	def setC(self, value, isRounded=False):
		return super().setAsInt(8, 4, value, isRounded)

	def getD(self):
		return super().getAsInt(12, 4)

	def setD(self, value, isRounded=False):
		return super().setAsInt(12, 4, value, isRounded)

	def getE(self):
		return super().getAsInt(16, 4)

	def setE(self, value, isRounded=False):
		return super().setAsInt(16, 4, value, isRounded)

	def getF(self):
		return super().getAsInt(20, 4)

	def setF(self, value, isRounded=False):
		return super().setAsInt(20, 4, value, isRounded)

	def getG(self):
		return super().getAsInt(24, 4)

	def setG(self, value, isRounded=False):
		return super().setAsInt(24, 4, value, isRounded)

	def getGROUP_1(self):
		return super().getAsString(28, 7)

	def setGROUP_1(self, value):
		return super().setAsString(28, 7, value)

	def getNUM1(self):
		return super().getAsString(28, 3)

	def setNUM1(self, value):
		return super().setAsString(28, 3, value)

	def getNUM3(self):
		return super().getAsFloat(28, 3, '9.99')

	def setNUM3(self, value, isRounded=False):
		return super().setAsFloat(28, 3, value, isRounded, '9.99')

	def getNUM2(self):
		return super().getAsInt(31, 4)

	def setNUM2(self, value, isRounded=False):
		return super().setAsInt(31, 4, value, isRounded)

	def getGROUP_2(self):
		return super().getAsString(35, 9)

	def setGROUP_2(self, value):
		return super().setAsString(35, 9, value)

	def getNUM1_1(self):
		return super().getAsString(35, 5)

	def setNUM1_1(self, value):
		return super().setAsString(35, 5, value)

	def getNUM5(self):
		return super().getAsInt(35, 5)

	def setNUM5(self, value, isRounded=False):
		return super().setAsInt(35, 5, value, isRounded)

	def getNUM2_1(self):
		return super().getAsInt(40, 4)

	def setNUM2_1(self, value, isRounded=False):
		return super().setAsInt(40, 4, value, isRounded)

	def initialize(self):
		self.setA(10,False)
		self.setB(2000,False)
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
	def main(self):
		self.initialize()
		print('Initial Values: A=', self.getA(), ' B=', self.getB(), ' C=', self.getC(), ' D=', self.getD(), ' E=', self.getE(), ' F=', self.getF())
		self.setB(self.getB() * self.getA())
		print('After MULTIPLY A BY B: A=', self.getA(), ' B=', self.getB())
		self.setA(self.getA() * 2, True)
		self.setB(self.getB() * 2)
		print('After MULTIPLY 2 BY A B: A=', self.getA(), ' B=', self.getB())
		self.setC(3 * self.getA())
		print('After MULTIPLY 3 BY A GIVING C: C=', self.getC())
		self.setD(4 * self.getA(), True)
		print('After MULTIPLY 4 BY A GIVING D ROUNDED: D=', self.getD())
		self.setE(self.getA() * 2, True)
		self.setF(self.getA() * 2, True)
		print('After MULTIPLY A BY 2 GIVING E F: E=', self.getE(), ' F=', self.getF())
		self.setNUM3(self.getNUM3() * self.getNUM5(), True)
converted().main()
