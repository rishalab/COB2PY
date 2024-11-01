import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(234)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getINDATA2(self):
		return super().getAsString(100, 100)

	def setINDATA2(self, value):
		return super().setAsString(100, 100, value)

	def setINDATA2(self, value):
		return super().setAsString(100, 100, value)

	def getDisplayINDATA2(self):
		return super().getAsString(100, 100)

	def getA1(self):
		return super().getAsInt(200, 8, False, False, False)

	def setA1(self, value, isRounded=False):
		return super().setAsInt(200, 8, value, isRounded, False, False, False)

	def getDisplayA1(self):
		return super().getAsDisplayInt(200, 8, False, False, False)

	def getA2(self):
		return super().getAsInt(208, 8, False, False, False)

	def setA2(self, value, isRounded=False):
		return super().setAsInt(208, 8, value, isRounded, False, False, False)

	def getDisplayA2(self):
		return super().getAsDisplayInt(208, 8, False, False, False)

	def getR(self):
		return super().getAsInt(216, 8, True, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(216, 8, value, isRounded, True, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(216, 8, True, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		indata = input()
		self.setINDATA( indata )
		indata2 = input()
		self.setINDATA2( indata2 )
		self.setA1( self.getINDATA())
		if self.getA1() >= 3200 :
			print(self.getDisplayINDATA2(), sep='')
		else:
			print("red", sep='')
		exit()
		exit()
converted().main()