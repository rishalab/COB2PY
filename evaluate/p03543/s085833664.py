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

	def getN1(self):
		return super().getAsInt(0, 1, False, False, False)

	def setN1(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded, False, False, False)

	def getDisplayN1(self):
		return super().getAsDisplayInt(0, 1, False, False, False)

	def getN2(self):
		return super().getAsInt(1, 1, False, False, False)

	def setN2(self, value, isRounded=False):
		return super().setAsInt(1, 1, value, isRounded, False, False, False)

	def getDisplayN2(self):
		return super().getAsDisplayInt(1, 1, False, False, False)

	def getN3(self):
		return super().getAsInt(2, 1, False, False, False)

	def setN3(self, value, isRounded=False):
		return super().setAsInt(2, 1, value, isRounded, False, False, False)

	def getDisplayN3(self):
		return super().getAsDisplayInt(2, 1, False, False, False)

	def getN4(self):
		return super().getAsInt(3, 1, False, False, False)

	def setN4(self, value, isRounded=False):
		return super().setAsInt(3, 1, value, isRounded, False, False, False)

	def getDisplayN4(self):
		return super().getAsDisplayInt(3, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		if ((self.getN1() == self.getN2()) and (self.getN2() == self.getN3())) or ((self.getN2() == self.getN3()) and (self.getN3() == self.getN4())) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		exit()
		exit()
converted().main()