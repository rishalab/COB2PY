import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(15)

	def getA(self):
		return super().getAsInt(0, 3, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(0, 3, False, False, False)

	def getB(self):
		return super().getAsInt(3, 3, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(3, 3, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(3, 3, False, False, False)

	def getC(self):
		return super().getAsInt(6, 3, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(6, 3, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(6, 3, False, False, False)

	def getRESULT(self):
		return super().getAsInt(9, 4, False, False, False)

	def setRESULT(self, value, isRounded=False):
		return super().setAsInt(9, 4, value, isRounded, False, False, False)

	def getDisplayRESULT(self):
		return super().getAsDisplayInt(9, 4, False, False, False)

	def getOVERFLOW_FLAG(self):
		return super().getAsString(13, 2)

	def setOVERFLOW_FLAG(self, value):
		return super().setAsString(13, 2, value)

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
		print("Simple ADD: ", sep='')
		self.setB(self.getA()+self.getB())
		print("A + B = ", self.getDisplayB(), sep='')
		print("ADD with GIVING: ", sep='')
		self.setRESULT(self.getA()+self.getB())
		print("A + B giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("ADD multiple variables: ", sep='')
		self.setRESULT(self.getA()+self.getB()+self.getC())
		print("A + B + C giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("ADD with literal values: ", sep='')
		self.setRESULT(15+self.getA())
		print("A + 15 giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("ADD multiple literals: ", sep='')
		self.setRESULT(5+10+15)
		print("5 + 10 + 15 giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("Simple SUBTRACT: ", sep='')
		self.setB(self.getB()-(self.getC()))
		print("B - C = ", self.getDisplayB(), sep='')
		print("SUBTRACT with GIVING: ", sep='')
		self.setRESULT(self.getB()-(self.getA()))
		print("B - A giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("SUBTRACT multiple variables: ", sep='')
		self.setRESULT(self.getB()-(self.getA()+self.getC()))
		print("B - A - C giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("SUBTRACT with literal values: ", sep='')
		self.setRESULT(self.getA()-(5))
		print("A - 5 giving RESULT = ", self.getDisplayRESULT(), sep='')
		print("SUBTRACT multiple literals: ", sep='')
		self.setRESULT(self.getB()-(5+10+3))
		print("B - 5 - 10 - 3 giving RESULT = ", self.getDisplayRESULT(), sep='')
		exit()
converted().main()
