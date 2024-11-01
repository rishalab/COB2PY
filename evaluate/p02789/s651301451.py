import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(16)

	def getLN(self):
		return super().getAsString(0, 7)

	def setLN(self, value):
		return super().setAsString(0, 7, value)

	def setLN(self, value):
		return super().setAsString(0, 7, value)

	def getDisplayLN(self):
		return super().getAsString(0, 7)

	def getN(self):
		return super().getAsInt(7, 3, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(7, 3, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(7, 3, False, False, False)

	def getM(self):
		return super().getAsInt(10, 3, False, False, False)

	def setM(self, value, isRounded=False):
		return super().setAsInt(10, 3, value, isRounded, False, False, False)

	def getDisplayM(self):
		return super().getAsDisplayInt(10, 3, False, False, False)

	def getANS(self):
		return super().getAsString(13, 3)

	def setANS(self, value):
		return super().setAsString(13, 3, value)

	def setANS(self, value):
		return super().setAsString(13, 3, value)

	def getDisplayANS(self):
		return super().getAsString(13, 3)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		LN = input()
		self.setLN( LN )
		N, M = LN.split(' ')
		self.setN(N)
		self.setM(M)
		if self.getN() == self.getM() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()