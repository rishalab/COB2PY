import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(18)

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

	def getSHO(self):
		return super().getAsInt(9, 3, False, False, False)

	def setSHO(self, value, isRounded=False):
		return super().setAsInt(9, 3, value, isRounded, False, False, False)

	def getDisplaySHO(self):
		return super().getAsDisplayInt(9, 3, False, False, False)

	def getAMA(self):
		return super().getAsInt(12, 3, False, False, False)

	def setAMA(self, value, isRounded=False):
		return super().setAsInt(12, 3, value, isRounded, False, False, False)

	def getDisplayAMA(self):
		return super().getAsDisplayInt(12, 3, False, False, False)

	def getANS(self):
		return super().getAsInt(15, 3, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(15, 3, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(15, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		A = input()
		self.setA( A )
		self.setSHO(self.getN() / 500)
		self.setAMA(self.getN() % 500)
		if self.getA() >= self.getAMA() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()