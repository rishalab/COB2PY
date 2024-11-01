import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(27)

	def getINP(self):
		return super().getAsString(0, 11)

	def setINP(self, value):
		return super().setAsString(0, 11, value)

	def setINP(self, value):
		return super().setAsString(0, 11, value)

	def getDisplayINP(self):
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

	def getX(self):
		return super().getAsInt(20, 3, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(20, 3, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(20, 3, False, False, False)

	def getQ(self):
		return super().getAsInt(23, 3, False, False, False)

	def setQ(self, value, isRounded=False):
		return super().setAsInt(23, 3, value, isRounded, False, False, False)

	def getDisplayQ(self):
		return super().getAsDisplayInt(23, 3, False, False, False)

	def getR(self):
		return super().getAsInt(26, 1, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(26, 1, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(26, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		A, B, C = INP.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		self.setX( self.getA()+self.getB()+self.getC())
		self.setQ(self.getX() / 2)
		self.setR(self.getX() % 2)
		if self.getR() == 1 :
			print("No", sep='')
		else:
			if self.getA() == self.getQ() or self.getB() == self.getQ() or self.getC() == self.getQ() :
				print("Yes", sep='')
			else:
				print("No", sep='')
		exit()
		exit()
converted().main()