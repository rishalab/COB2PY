import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(15)

	def getN(self):
		return super().getAsInt(0, 5, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 5, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 5, False, False, False)

	def getA(self):
		return super().getAsInt(5, 4, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(5, 4, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(5, 4, False, False, False)

	def getX(self):
		return super().getAsInt(9, 3, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(9, 3, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(9, 3, False, False, False)

	def getR(self):
		return super().getAsInt(12, 3, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(12, 3, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(12, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		N = input()
		self.setN( N )
		A = input()
		self.setA( A )
		self.setX(self.getN() / 500)
		self.setR(self.getN() % 500)
		if self.getR() <= self.getA() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()

	def MAIN_flow(self):
		N = input()
		self.setN( N )
		A = input()
		self.setA( A )
		self.setX(self.getN() / 500)
		self.setR(self.getN() % 500)
		if self.getR() <= self.getA() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()