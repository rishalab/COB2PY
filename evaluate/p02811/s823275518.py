import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(124)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getK(self):
		return super().getAsInt(100, 8, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(100, 8, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(100, 8, False, False, False)

	def getX(self):
		return super().getAsInt(108, 8, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(108, 8, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(108, 8, False, False, False)

	def getR(self):
		return super().getAsInt(116, 8, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(116, 8, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(116, 8, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		indata = input()
		self.setINDATA( indata )
		K, X = indata.split(' ')
		self.setK(K)
		self.setX(X)
		self.setR(500 * self.getK())
		if self.getR() >= self.getX() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()