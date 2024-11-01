import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(8)

	def getN(self):
		return super().getAsString(0, 4)

	def setN(self, value):
		return super().setAsString(0, 4, value)

	def setN(self, value):
		return super().setAsString(0, 4, value)

	def getDisplayN(self):
		return super().getAsString(0, 4)

	def getINP(self):
		return super().getAsString(4, 4)

	def setINP(self, value):
		return super().setAsString(4, 4, value)

	def getDisplayINP(self):
		return super().getAsString(4, 4)

	def getINP1(self):
		return super().getAsInt(4, 1, False, False, False)

	def setINP1(self, value, isRounded=False):
		return super().setAsInt(4, 1, value, isRounded, False, False, False)

	def getDisplayINP1(self):
		return super().getAsDisplayInt(4, 1, False, False, False)

	def getINP2(self):
		return super().getAsInt(5, 1, False, False, False)

	def setINP2(self, value, isRounded=False):
		return super().setAsInt(5, 1, value, isRounded, False, False, False)

	def getDisplayINP2(self):
		return super().getAsDisplayInt(5, 1, False, False, False)

	def getINP3(self):
		return super().getAsInt(6, 1, False, False, False)

	def setINP3(self, value, isRounded=False):
		return super().setAsInt(6, 1, value, isRounded, False, False, False)

	def getDisplayINP3(self):
		return super().getAsDisplayInt(6, 1, False, False, False)

	def getINP4(self):
		return super().getAsInt(7, 1, False, False, False)

	def setINP4(self, value, isRounded=False):
		return super().setAsInt(7, 1, value, isRounded, False, False, False)

	def getDisplayINP4(self):
		return super().getAsDisplayInt(7, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		self.setINP(self.getN())
		if (True == ((self.getINP1() == self.getINP2()) and (self.getINP2() == self.getINP3()))) or (True == ((self.getINP2() == self.getINP3()) and (self.getINP3() == self.getINP4()))):
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()