import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(115)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getA(self):
		return super().getAsInt(100, 3, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(100, 3, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(100, 3, False, False, False)

	def getB(self):
		return super().getAsInt(103, 3, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(103, 3, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(103, 3, False, False, False)

	def getC(self):
		return super().getAsInt(106, 3, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(106, 3, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(106, 3, False, False, False)

	def getANS1(self):
		return super().getAsInt(109, 3, False, False, False)

	def setANS1(self, value, isRounded=False):
		return super().setAsInt(109, 3, value, isRounded, False, False, False)

	def getDisplayANS1(self):
		return super().getAsDisplayInt(109, 3, False, False, False)

	def getANS2(self):
		return super().getAsInt(112, 3, False, False, False)

	def setANS2(self, value, isRounded=False):
		return super().setAsInt(112, 3, value, isRounded, False, False, False)

	def getDisplayANS2(self):
		return super().getAsDisplayInt(112, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		A, B, C = INP.split(" ")
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getB()-self.getA() == self.getC()-self.getB() :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()
		exit()
converted().main()