import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(30)

	def getLN(self):
		return super().getAsString(0, 10)

	def setLN(self, value):
		return super().setAsString(0, 10, value)

	def setLN(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayLN(self):
		return super().getAsString(0, 10)

	def getK(self):
		return super().getAsInt(10, 10, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(10, 10, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(10, 10, False, False, False)

	def getX(self):
		return super().getAsInt(20, 10, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(20, 10, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(20, 10, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		LN = input()
		self.setLN( LN )
		K, X = LN.split(' ')
		self.setK(K)
		self.setX(X)
		if self.getX() <= 500*self.getK() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()