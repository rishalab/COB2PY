import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(20)

	def getINP(self):
		return super().getAsString(0, 11)

	def setINP(self, value):
		return super().setAsString(0, 11, value)

	def setINP(self, value):
		return super().setAsString(0, 11, value)

	def getDisplayINP(self):
		return super().getAsString(0, 11)

	def getA(self):
		return super().getAsInt(11, 3, True, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(11, 3, value, isRounded, True, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(11, 3, True, False, False)

	def getB(self):
		return super().getAsInt(14, 3, True, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(14, 3, value, isRounded, True, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(14, 3, True, False, False)

	def getC(self):
		return super().getAsInt(17, 3, True, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(17, 3, value, isRounded, True, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(17, 3, True, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		A, B, C = INP.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if self.getB()-self.getA() == self.getC()-self.getB() :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		A, B, C = INP.split(' ')
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