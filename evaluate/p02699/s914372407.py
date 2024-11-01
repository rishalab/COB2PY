import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(16)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getS(self):
		return super().getAsInt(10, 3, False, False, False)

	def setS(self, value, isRounded=False):
		return super().setAsInt(10, 3, value, isRounded, False, False, False)

	def getDisplayS(self):
		return super().getAsDisplayInt(10, 3, False, False, False)

	def getW(self):
		return super().getAsInt(13, 3, False, False, False)

	def setW(self, value, isRounded=False):
		return super().setAsInt(13, 3, value, isRounded, False, False, False)

	def getDisplayW(self):
		return super().getAsDisplayInt(13, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		S, W = INP.split(' ')
		self.setS(S)
		self.setW(W)
		if (self.getW() >= self.getS()) :
			print('unsafe', sep='')
		else:
			print('safe', sep='')
		exit()
		exit()
converted().main()