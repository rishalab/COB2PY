import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(19)

	def getLN(self):
		return super().getAsString(0, 10)

	def setLN(self, value):
		return super().setAsString(0, 10, value)

	def setLN(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayLN(self):
		return super().getAsString(0, 10)

	def getK(self):
		return super().getAsInt(10, 3, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(10, 3, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(10, 3, False, False, False)

	def getX(self):
		return super().getAsInt(13, 6, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(13, 6, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(13, 6, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		LN = input()
		self.setLN( LN )
		K, X = LN.split(' ')
		self.setK(K)
		self.setX(X)
		if self.getX() <= 500*self.getK() :
			print("Yes", sep='')
		else:
			print("No", sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		LN = input()
		self.setLN( LN )
		K, X = LN.split(' ')
		self.setK(K)
		self.setX(X)
		if self.getX() <= 500*self.getK() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()