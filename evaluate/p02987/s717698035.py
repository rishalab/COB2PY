import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getINP(self):
		return super().getAsString(0, 4)

	def setINP(self, value):
		return super().setAsString(0, 4, value)

	def getDisplayINP(self):
		return super().getAsString(0, 4)

	def getA(self):
		return super().getAsString(0, 1)

	def setA(self, value):
		return super().setAsString(0, 1, value)

	def setA(self, value):
		return super().setAsString(0, 1, value)

	def getDisplayA(self):
		return super().getAsString(0, 1)

	def getB(self):
		return super().getAsString(1, 1)

	def setB(self, value):
		return super().setAsString(1, 1, value)

	def setB(self, value):
		return super().setAsString(1, 1, value)

	def getDisplayB(self):
		return super().getAsString(1, 1)

	def getC(self):
		return super().getAsString(2, 1)

	def setC(self, value):
		return super().setAsString(2, 1, value)

	def setC(self, value):
		return super().setAsString(2, 1, value)

	def getDisplayC(self):
		return super().getAsString(2, 1)

	def getD(self):
		return super().getAsString(3, 1)

	def setD(self, value):
		return super().setAsString(3, 1, value)

	def setD(self, value):
		return super().setAsString(3, 1, value)

	def getDisplayD(self):
		return super().getAsString(3, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		if (True == ((self.getA() == self.getB()) and (self.getC() == self.getD()))):
			if self.getA() == self.getC() :
				print("No", sep='')
			else:
				print("Yes", sep='')
		elif (True == ((self.getA() == self.getC()) and (self.getB() == self.getD()))) or (True == ((self.getA() == self.getD()) and (self.getB() == self.getC()))):
			if self.getA() == self.getB() :
				print("No", sep='')
			else:
				print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()