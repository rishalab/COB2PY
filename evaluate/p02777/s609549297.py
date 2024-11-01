import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(59)

	def getLN(self):
		return super().getAsString(0, 21)

	def setLN(self, value):
		return super().setAsString(0, 21, value)

	def setLN(self, value):
		return super().setAsString(0, 21, value)

	def getDisplayLN(self):
		return super().getAsString(0, 21)

	def getS(self):
		return super().getAsString(21, 10)

	def setS(self, value):
		return super().setAsString(21, 10, value)

	def setS(self, value):
		return super().setAsString(21, 10, value)

	def getDisplayS(self):
		return super().getAsString(21, 10)

	def getT(self):
		return super().getAsString(31, 10)

	def setT(self, value):
		return super().setAsString(31, 10, value)

	def setT(self, value):
		return super().setAsString(31, 10, value)

	def getDisplayT(self):
		return super().getAsString(31, 10)

	def getU(self):
		return super().getAsString(41, 10)

	def setU(self, value):
		return super().setAsString(41, 10, value)

	def setU(self, value):
		return super().setAsString(41, 10, value)

	def getDisplayU(self):
		return super().getAsString(41, 10)

	def getA(self):
		return super().getAsInt(51, 2, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(51, 2, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(51, 2, False, False, False)

	def getB(self):
		return super().getAsInt(53, 2, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(53, 2, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(53, 2, False, False, False)

	def getZA(self):
		return super().getAsString(55, 2)

	def setZA(self, value):
		return super().setAsString(55, 2, value)

	def setZA(self, value):
		return super().setAsString(55, 2, value)

	def getDisplayZA(self):
		return super().getAsString(55, 2)

	def getZB(self):
		return super().getAsString(57, 2)

	def setZB(self, value):
		return super().setAsString(57, 2, value)

	def setZB(self, value):
		return super().setAsString(57, 2, value)

	def getDisplayZB(self):
		return super().getAsString(57, 2)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		LN = input()
		self.setLN( LN )
		S, T = LN.split(' ')
		self.setS(S)
		self.setT(T)
		LN = input()
		self.setLN( LN )
		A, B = LN.split(' ')
		self.setA(A)
		self.setB(B)
		U = input()
		self.setU( U )
		if self.getS() == self.getU() :
			self.setA(-1+self.getA())
		else:
			self.setB(-1+self.getB())
		self.setZA(self.getA())
		self.setZB(self.getB())
		print(self.getDisplayZA(), ' ', self.getDisplayZB(), sep='')
		exit()
converted().main()