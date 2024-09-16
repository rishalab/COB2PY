from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(44)

	def getA(self):
		return super().getAsInt(0, 2)

	def setA(self, value, isRounded):
		return super().setAsInt(0, 2, value, isRounded)

	def getB(self):
		return super().getAsInt(2, 2)

	def setB(self, value, isRounded):
		return super().setAsInt(2, 2, value, isRounded)

	def getC(self):
		return super().getAsInt(4, 2)

	def setC(self, value, isRounded):
		return super().setAsInt(4, 2, value, isRounded)

	def getD(self):
		return super().getAsInt(6, 2)

	def setD(self, value, isRounded):
		return super().setAsInt(6, 2, value, isRounded)

	def getE(self):
		return super().getAsInt(8, 2)

	def setE(self, value, isRounded):
		return super().setAsInt(8, 2, value, isRounded)

	def getF(self):
		return super().getAsInt(10, 2)

	def setF(self, value, isRounded):
		return super().setAsInt(10, 2, value, isRounded)

	def getG(self):
		return super().getAsInt(12, 2)

	def setG(self, value, isRounded):
		return super().setAsInt(12, 2, value, isRounded)

	def getH(self):
		return super().getAsInt(14, 2)

	def setH(self, value, isRounded):
		return super().setAsInt(14, 2, value, isRounded)

	def getI(self):
		return super().getAsInt(16, 3)

	def setI(self, value, isRounded):
		return super().setAsInt(16, 3, value, isRounded)

	def getJ(self):
		return super().getAsInt(19, 3)

	def setJ(self, value, isRounded):
		return super().setAsInt(19, 3, value, isRounded)

	def getK(self):
		return super().getAsInt(22, 3)

	def setK(self, value, isRounded):
		return super().setAsInt(22, 3, value, isRounded)

	def getL(self):
		return super().getAsInt(25, 3)

	def setL(self, value, isRounded):
		return super().setAsInt(25, 3, value, isRounded)

	def getNUM3(self):
		return super().getAsFloat(28, 4)

	def setNUM3(self, value, isRounded):
		return super().setAsFloat(28, 4, value, isRounded, '99.99')

	def getNUM4(self):
		return super().getAsInt(32, 4)

	def setNUM4(self, value, isRounded):
		return super().setAsInt(32, 4, value, isRounded)

	def getNUM5(self):
		return super().getAsFloat(36, 4)

	def setNUM5(self, value, isRounded):
		return super().setAsFloat(36, 4, value, isRounded, '99.99')

	def getNUM2(self):
		return super().getAsFloat(40, 4)

	def setNUM2(self, value, isRounded):
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
    print('DIVIDE A INTO B.: A= ', getNUM3(), '  ,B= ', getNUM5(), 'kjoioh', getNUM2())
    setNUM5(getNUM5() / getNUM3(), True)
    setNUM2(getNUM2() / getNUM3())
    print('DIVIDE A INTO B.: NUM3= ', getNUM3(), '  ,NUM5= ', getNUM5(), 'kjj', getNUM2())
    print('DIVIDE D INTO C GIVING J: C= ', getC(), ' ,D= ', getD(), ', J= ', getJ())
    setJ(getC() / getD())
    setK(getC() / getD(), True)
    setH(getC() % getD())
    print('DIVIDE D INTO C GIVING J: C= ', getC(), ' ,D= ', getD(), ', J= ', getJ())
    print('DIVIDE E BY F GIVING I .: E= ', getE(), ' ,F= ', getF(), ', I= ', getI())
    setI(getE() / getF())
    setH(getE() % getF())
    print('DIVIDE E BY F GIVING I.: E= ', getE(), ' ,F= ', getF(), ', I= ', getI())
    print('DIVIDE G INTO H GIVING K REMAINDER L: G= ', getG(), ', H= ', getH(), ', K= ', getK(), ', L= ', getL())
    setK(getH() / getG(), True)
    setL(getH() % getG())
    print('DIVIDE G INTO H GIVING K REMAINDER L: G= ', getG(), ', H= ', getH(), ', K= ', getK(), ', L= ', getL())
