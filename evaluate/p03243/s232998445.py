import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getN(self):
		return super().getAsInt(0, 3, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		self.setN( (self.getN()+110)/111)
		self.setN( self.getN()*111)
		print(self.getDisplayN(), sep='')
		exit()
		exit()
converted().main()