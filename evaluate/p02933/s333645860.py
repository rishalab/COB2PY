import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(166)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getA(self):
		return super().getAsInt(100, 11, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(100, 11, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(100, 11, False, False, False)

	def getB(self):
		return super().getAsInt(111, 11, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(111, 11, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(111, 11, False, False, False)

	def getC(self):
		return super().getAsInt(122, 11, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(122, 11, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(122, 11, False, False, False)

	def getTEMP1(self):
		return super().getAsInt(133, 11, False, False, False)

	def setTEMP1(self, value, isRounded=False):
		return super().setAsInt(133, 11, value, isRounded, False, False, False)

	def getDisplayTEMP1(self):
		return super().getAsDisplayInt(133, 11, False, False, False)

	def getTEMP2(self):
		return super().getAsInt(144, 11, False, False, False)

	def setTEMP2(self, value, isRounded=False):
		return super().setAsInt(144, 11, value, isRounded, False, False, False)

	def getDisplayTEMP2(self):
		return super().getAsDisplayInt(144, 11, False, False, False)

	def getN(self):
		return super().getAsInt(155, 11, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(155, 11, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(155, 11, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		A = input()
		self.setA( A )
		INP = input()
		self.setINP( INP )
		if self.getA() >= 3200 :
			print(self.getDisplayINP(), sep='')
		else:
			print("red", sep='')
		exit()

	def MAIN_flow(self):
		A = input()
		self.setA( A )
		INP = input()
		self.setINP( INP )
		if self.getA() >= 3200 :
			print(self.getDisplayINP(), sep='')
		else:
			print("red", sep='')
		exit()
		exit()
converted().main()