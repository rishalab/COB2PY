import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(22)

	def getINP(self):
		return super().getAsString(0, 7)

	def setINP(self, value):
		return super().setAsString(0, 7, value)

	def setINP(self, value):
		return super().setAsString(0, 7, value)

	def getDisplayINP(self):
		return super().getAsString(0, 7)

	def getN(self):
		return super().getAsInt(7, 3, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(7, 3, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(7, 3, False, False, False)

	def getK(self):
		return super().getAsInt(10, 3, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(10, 3, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(10, 3, False, False, False)

	def getANS(self):
		return super().getAsString(13, 3)

	def setANS(self, value):
		return super().setAsString(13, 3, value)

	def setANS(self, value):
		return super().setAsString(13, 3, value)

	def getDisplayANS(self):
		return super().getAsString(13, 3)

	def getD(self):
		return super().getAsInt(16, 3, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(16, 3, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(16, 3, False, False, False)

	def getR(self):
		return super().getAsInt(19, 3, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(19, 3, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(19, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		N, K = INP.split(' ')
		self.setN(N)
		self.setK(K)
		self.setD(self.getN() / self.getK())
		self.setR(self.getN() % self.getK())
		if 0 == self.getR() :
			print(0, sep='')
		else:
			print(1, sep='')
		exit()
		exit()
converted().main()