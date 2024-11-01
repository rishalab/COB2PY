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

	def getN(self,idx1):
		return super().getAsInt(0+ idx1*1, 1, False, False, False)

	def setN(self,idx1, value, isRounded=False):
		return super().setAsInt(0+ idx1*1, 1, value, isRounded, False, False, False)

	def getDisplayN(self,idx1):
		return super().getAsDisplayInt(0+ idx1*1, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		if ((self.getN(1 - 1)+self.getN(2 - 1)+self.getN(3 - 1))/3 == self.getN(1 - 1)) or ((self.getN(2 - 1)+self.getN(3 - 1)+self.getN(4 - 1))/3 == self.getN(2 - 1)) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		exit()
		exit()
converted().main()