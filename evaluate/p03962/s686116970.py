import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(20)

	def getSTR(self):
		return super().getAsString(0, 11)

	def setSTR(self, value):
		return super().setAsString(0, 11, value)

	def setSTR(self, value):
		return super().setAsString(0, 11, value)

	def getDisplaySTR(self):
		return super().getAsString(0, 11)

	def getA(self):
		return super().getAsInt(11, 3, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(11, 3, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(11, 3, False, False, False)

	def getB(self):
		return super().getAsInt(14, 3, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(14, 3, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(14, 3, False, False, False)

	def getC(self):
		return super().getAsInt(17, 3, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(17, 3, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(17, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_PROCEDURE_flow()
	def MAIN_PROCEDURE(self):
		STR = input()
		self.setSTR( STR )
		A, B, C = STR.split(" ")
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getA() == self.getB() and self.getB() == self.getC() :
			print(1, sep='')
		else:
			if self.getA() == self.getB() and self.getB() != self.getC() :
				print(2, sep='')
			else:
				if self.getB() == self.getC() and self.getC() != self.getA() :
					print(2, sep='')
				else:
					if self.getC() == self.getA() and self.getA() != self.getB() :
						print(2, sep='')
					else:
						print(3, sep='')
		exit()

	def MAIN_PROCEDURE_flow(self):
		STR = input()
		self.setSTR( STR )
		A, B, C = STR.split(" ")
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getA() == self.getB() and self.getB() == self.getC() :
			print(1, sep='')
		else:
			if self.getA() == self.getB() and self.getB() != self.getC() :
				print(2, sep='')
			else:
				if self.getB() == self.getC() and self.getC() != self.getA() :
					print(2, sep='')
				else:
					if self.getC() == self.getA() and self.getA() != self.getB() :
						print(2, sep='')
					else:
						print(3, sep='')
		exit()
		exit()
converted().main()