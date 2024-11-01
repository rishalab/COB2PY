import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getS(self):
		return super().getAsString(0, 3)

	def setS(self, value):
		return super().setAsString(0, 3, value)

	def setS(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayS(self):
		return super().getAsString(0, 3)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		S = input()
		self.setS( S )
		if (self.getS() == 'ABC') :
			print('ARC', sep='')
		else:
			print('ABC', sep='')
		exit()
		exit()
converted().main()