import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(70)

	def getLN(self):
		return super().getAsString(0, 30)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayLN(self):
		return super().getAsString(0, 30)

	def getN(self):
		return super().getAsInt(30, 10, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(30, 10, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(30, 10, False, False, False)

	def getM(self):
		return super().getAsInt(40, 10, False, False, False)

	def setM(self, value, isRounded=False):
		return super().setAsInt(40, 10, value, isRounded, False, False, False)

	def getDisplayM(self):
		return super().getAsDisplayInt(40, 10, False, False, False)

	def getANS(self):
		return super().getAsInt(50, 10, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(50, 10, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(50, 10, False, False, False)

	def getZS(self):
		return super().getAsString(60, 10)

	def setZS(self, value):
		return super().setAsString(60, 10, value)

	def setZS(self, value):
		return super().setAsString(60, 10, value)

	def getDisplayZS(self):
		return super().getAsString(60, 10)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		LN = input()
		self.setLN( LN )
		N, M = LN.split(' ')
		self.setN(N)
		self.setM(M)
		self.setANS( self.getN()*(self.getN()-1)/2+self.getM()*(self.getM()-1)/2)
		self.setZS(self.getANS())
		print(self.getDisplayZS(), sep='')
		exit()
		exit()
converted().main()