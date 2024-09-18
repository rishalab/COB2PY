from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(44)

	def getA(self):
		return super().getAsInt(0, 2)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded)

	def getB(self):
		return super().getAsInt(2, 2)

	def setB(self, value, isRounded=False):
		return super().setAsInt(2, 2, value, isRounded)

	def getC(self):
		return super().getAsInt(4, 2)

	def setC(self, value, isRounded=False):
		return super().setAsInt(4, 2, value, isRounded)

	def getD(self):
		return super().getAsInt(6, 2)

	def setD(self, value, isRounded=False):
		return super().setAsInt(6, 2, value, isRounded)

	def getE(self):
		return super().getAsInt(8, 2)

	def setE(self, value, isRounded=False):
		return super().setAsInt(8, 2, value, isRounded)

	def getF(self):
		return super().getAsInt(10, 2)

	def setF(self, value, isRounded=False):
		return super().setAsInt(10, 2, value, isRounded)

	def getG(self):
		return super().getAsInt(12, 2)

	def setG(self, value, isRounded=False):
		return super().setAsInt(12, 2, value, isRounded)

	def getH(self):
		return super().getAsInt(14, 2)

	def setH(self, value, isRounded=False):
		return super().setAsInt(14, 2, value, isRounded)

	def getI(self):
		return super().getAsInt(16, 3)

	def setI(self, value, isRounded=False):
		return super().setAsInt(16, 3, value, isRounded)

	def getJ(self):
		return super().getAsInt(19, 3)

	def setJ(self, value, isRounded=False):
		return super().setAsInt(19, 3, value, isRounded)

	def getK(self):
		return super().getAsInt(22, 3)

	def setK(self, value, isRounded=False):
		return super().setAsInt(22, 3, value, isRounded)

	def getL(self):
		return super().getAsInt(25, 3)

	def setL(self, value, isRounded=False):
		return super().setAsInt(25, 3, value, isRounded)

	def getNUM3(self):
		return super().getAsFloat(28, 4)

	def setNUM3(self, value, isRounded=False):
		return super().setAsFloat(28, 4, value, isRounded, '99.99')

	def getNUM4(self):
		return super().getAsInt(32, 4)

	def setNUM4(self, value, isRounded=False):
		return super().setAsInt(32, 4, value, isRounded)

	def getNUM5(self):
		return super().getAsFloat(36, 4)

	def setNUM5(self, value, isRounded=False):
		return super().setAsFloat(36, 4, value, isRounded, '99.99')

	def getNUM2(self):
		return super().getAsFloat(40, 4)

	def setNUM2(self, value, isRounded=False):
		return super().setAsFloat(40, 4, value, isRounded, '99.99')

	def initialize(self):
		self.setA(10,False)
		self.setB(23,False)
		self.setC(10,False)
		self.setD(5,False)
		self.setE(10,False)
		self.setF(5,False)
		self.setG(11,False)
		self.setH(50,False)
		self.setJ(12,False)
		self.setNUM3(3.0,False)
		self.setNUM4(2,False)
		self.setNUM5(11.0,False)
		self.setNUM2(12.0,False)
		pass
	def main(self):
		self.initialize()
		print('DIVIDE A INTO B.: A= ', self.getNUM3(), '  ,B= ', self.getNUM5(), 'kjoioh', self.getNUM2())
		self.setNUM5(self.getNUM5() / self.getNUM3(), True)
		self.setNUM2(self.getNUM2() / self.getNUM3())
		print('DIVIDE A INTO B.: NUM3= ', self.getNUM3(), '  ,NUM5= ', self.getNUM5(), 'kjj', self.getNUM2())
		print('DIVIDE D INTO C GIVING J: C= ', self.getC(), ' ,D= ', self.getD(), ', J= ', self.getJ())
		self.setJ(self.getC() / self.getD(), True)
		self.setH(self.getC() % self.getD())
		print('DIVIDE D INTO C GIVING J: C= ', self.getC(), ' ,D= ', self.getD(), ', J= ', self.getJ())
		print('DIVIDE E BY F GIVING I .: E= ', self.getE(), ' ,F= ', self.getF(), ', I= ', self.getI())
		self.setI(self.getE() / self.getF())
		self.setH(self.getE() % self.getF())
		print('DIVIDE E BY F GIVING I.: E= ', self.getE(), ' ,F= ', self.getF(), ', I= ', self.getI())
		print('DIVIDE G INTO H GIVING K REMAINDER L: G= ', self.getG(), ', H= ', self.getH(), ', K= ', self.getK(), ', L= ', self.getL())
		self.setK(self.getH() / self.getG(), True)
		self.setL(self.getH() % self.getG())
		print('DIVIDE G INTO H GIVING K REMAINDER L: G= ', self.getG(), ', H= ', self.getH(), ', K= ', self.getK(), ', L= ', self.getL())
converted().main()
