import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(12)

	def getLN(self):
		return super().getAsString(0, 5)

	def setLN(self, value):
		return super().setAsString(0, 5, value)

	def setLN(self, value):
		return super().setAsString(0, 5, value)

	def getDisplayLN(self):
		return super().getAsString(0, 5)

	def getA(self):
		return super().getAsInt(5, 1, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(5, 1, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(5, 1, False, False, False)

	def getB(self):
		return super().getAsInt(6, 1, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(6, 1, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(6, 1, False, False, False)

	def getC(self):
		return super().getAsInt(7, 1, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(7, 1, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(7, 1, False, False, False)

	def getFLG(self):
		return super().getAsInt(8, 1, False, False, False)

	def setFLG(self, value, isRounded=False):
		return super().setAsInt(8, 1, value, isRounded, False, False, False)

	def getDisplayFLG(self):
		return super().getAsDisplayInt(8, 1, False, False, False)

	def getANS(self):
		return super().getAsString(9, 3)

	def setANS(self, value):
		return super().setAsString(9, 3, value)

	def setANS(self, value):
		return super().setAsString(9, 3, value)

	def getDisplayANS(self):
		return super().getAsString(9, 3)

	def initialize(self):
		self.setFLG(0,False)
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		LN = input()
		self.setLN( LN )
		A, B, C = LN.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getA() == self.getB() and self.getB() != self.getC() :
			self.setFLG(1)
		if self.getB() == self.getC() and self.getC() != self.getA() :
			self.setFLG(1)
		if self.getC() == self.getA() and self.getA() != self.getB() :
			self.setFLG(1)
		if self.getFLG() == 1 :
			print("Yes", sep='')
		else:
			print("No", sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_flow(self):
		LN = input()
		self.setLN( LN )
		A, B, C = LN.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getA() == self.getB() and self.getB() != self.getC() :
			self.setFLG(1)
		if self.getB() == self.getC() and self.getC() != self.getA() :
			self.setFLG(1)
		if self.getC() == self.getA() and self.getA() != self.getB() :
			self.setFLG(1)
		if self.getFLG() == 1 :
			print("Yes", sep='')
		else:
			print("No", sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()