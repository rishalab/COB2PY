import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getN(self):
		return super().getAsInt(0, 4, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		N = input()
		self.setN( N )
		if 999 < self.getN() :
			print("ABD", sep='')
		else:
			print("ABC", sep='')
		exit()

	def MAIN_flow(self):
		N = input()
		self.setN( N )
		if 999 < self.getN() :
			print("ABD", sep='')
		else:
			print("ABC", sep='')
		exit()
		exit()
converted().main()