import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(26)

	def getINP(self):
		return super().getAsString(0, 14)

	def setINP(self, value):
		return super().setAsString(0, 14, value)

	def setINP(self, value):
		return super().setAsString(0, 14, value)

	def getDisplayINP(self):
		return super().getAsString(0, 14)

	def getX(self):
		return super().getAsInt(14, 4, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(14, 4, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(14, 4, False, False, False)

	def getA(self):
		return super().getAsInt(18, 4, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(18, 4, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(18, 4, False, False, False)

	def getB(self):
		return super().getAsInt(22, 4, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(22, 4, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(22, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		X, A, B = INP.split(' ')
		self.setX(X)
		self.setA(A)
		self.setB(B)
		self.setA(self.getA()-(self.getX()))
		self.setB(self.getB()-(self.getX()))
		if self.getA() < self.getB() :
			print('A', sep='')
		else:
			print('B', sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		X, A, B = INP.split(' ')
		self.setX(X)
		self.setA(A)
		self.setB(B)
		self.setA(self.getA()-(self.getX()))
		self.setB(self.getB()-(self.getX()))
		if self.getA() < self.getB() :
			print('A', sep='')
		else:
			print('B', sep='')
		exit()
		exit()
converted().main()