import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(132)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getA1(self):
		return super().getAsInt(100, 8, False, False, False)

	def setA1(self, value, isRounded=False):
		return super().setAsInt(100, 8, value, isRounded, False, False, False)

	def getDisplayA1(self):
		return super().getAsDisplayInt(100, 8, False, False, False)

	def getA2(self):
		return super().getAsInt(108, 8, False, False, False)

	def setA2(self, value, isRounded=False):
		return super().setAsInt(108, 8, value, isRounded, False, False, False)

	def getDisplayA2(self):
		return super().getAsDisplayInt(108, 8, False, False, False)

	def getA3(self):
		return super().getAsInt(116, 8, False, False, False)

	def setA3(self, value, isRounded=False):
		return super().setAsInt(116, 8, value, isRounded, False, False, False)

	def getDisplayA3(self):
		return super().getAsDisplayInt(116, 8, False, False, False)

	def getR(self):
		return super().getAsInt(124, 8, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(124, 8, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(124, 8, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		indata = input()
		self.setINDATA( indata )
		A1, A2, A3 = indata.split(' ')
		self.setA1(A1)
		self.setA2(A2)
		self.setA3(A3)
		self.setR( self.getA1()+self.getA2()+self.getA3())
		if self.getR() >= 22 :
			print("bust", sep='')
		else:
			print("win", sep='')
		exit()
		exit()
converted().main()