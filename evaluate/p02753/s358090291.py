import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(103)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getS(self):
		return super().getAsString(100, 3)

	def setS(self, value):
		return super().setAsString(100, 3, value)

	def getDisplayS(self):
		return super().getAsString(100, 3)

	def getS1(self):
		return super().getAsString(100, 1)

	def setS1(self, value):
		return super().setAsString(100, 1, value)

	def setS1(self, value):
		return super().setAsString(100, 1, value)

	def getDisplayS1(self):
		return super().getAsString(100, 1)

	def getS2(self):
		return super().getAsString(101, 1)

	def setS2(self, value):
		return super().setAsString(101, 1, value)

	def setS2(self, value):
		return super().setAsString(101, 1, value)

	def getDisplayS2(self):
		return super().getAsString(101, 1)

	def getS3(self):
		return super().getAsString(102, 1)

	def setS3(self, value):
		return super().setAsString(102, 1, value)

	def setS3(self, value):
		return super().setAsString(102, 1, value)

	def getDisplayS3(self):
		return super().getAsString(102, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		self.setS(self.getINP())
		if (True == ((self.getS1() == self.getS2()) and (self.getS2() == self.getS3()))):
			print("No", sep='')
		else:
			print("Yes", sep='')
		exit()
		exit()
converted().main()