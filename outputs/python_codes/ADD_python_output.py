from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(15)

	def getA(self):
		return super().getAsInt(0, 3)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded)

	def getB(self):
		return super().getAsInt(3, 3)

	def setB(self, value, isRounded=False):
		return super().setAsInt(3, 3, value, isRounded)

	def getC(self):
		return super().getAsInt(6, 3)

	def setC(self, value, isRounded=False):
		return super().setAsInt(6, 3, value, isRounded)

	def getRESULT(self):
		return super().getAsInt(9, 4)

	def setRESULT(self, value, isRounded=False):
		return super().setAsInt(9, 4, value, isRounded)

	def getOVERFLOW_FLAG(self):
		return super().getAsString(13, 2)

	def setOVERFLOW_FLAG(self, value):
		return super().setAsString(13, 2, value)

	def initialize(self):
		self.setA(10,False)
		self.setB(20,False)
		self.setC(5,False)
		self.setOVERFLOW_FLAG('NY')
		pass
	def main(self):
		self.initialize()
		print("Simple ADD: ")
		self.setB(self.getA()+self.getB())
		print("A + B = ", self.getB())
		print("ADD with GIVING: ")
		self.setRESULT(self.getA()+self.getB())
		print("A + B giving RESULT = ", self.getRESULT())
		print("ADD multiple variables: ")
		self.setRESULT(self.getA()+self.getB()+self.getC())
		print("A + B + C giving RESULT = ", self.getRESULT())
		print("ADD with literal values: ")
		self.setRESULT(15+self.getA())
		print("A + 15 giving RESULT = ", self.getRESULT())
		print("ADD multiple literals: ")
		self.setRESULT(5+10+15)
		print("5 + 10 + 15 giving RESULT = ", self.getRESULT())
		print("Simple SUBTRACT: ")
		self.setB(self.getB()-(self.getC()))
		print("B - C = ", self.getB())
		print("SUBTRACT with GIVING: ")
		self.setRESULT(self.getB()-(self.getA()))
		print("B - A giving RESULT = ", self.getRESULT())
		print("SUBTRACT multiple variables: ")
		self.setRESULT(self.getB()-(self.getA()+self.getC()))
		print("B - A - C giving RESULT = ", self.getRESULT())
		print("SUBTRACT with literal values: ")
		self.setRESULT(self.getA()-(5))
		print("A - 5 giving RESULT = ", self.getRESULT())
		print("SUBTRACT multiple literals: ")
		self.setRESULT(self.getB()-(5+10+3))
		print("B - 5 - 10 - 3 giving RESULT = ", self.getRESULT())
converted().main()
