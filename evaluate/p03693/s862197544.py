import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(17)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getINP2(self):
		return super().getAsString(10, 3)

	def setINP2(self, value):
		return super().setAsString(10, 3, value)

	def getDisplayINP2(self):
		return super().getAsString(10, 3)

	def getR(self):
		return super().getAsInt(10, 1, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(10, 1, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(10, 1, False, False, False)

	def getG(self):
		return super().getAsInt(11, 1, False, False, False)

	def setG(self, value, isRounded=False):
		return super().setAsInt(11, 1, value, isRounded, False, False, False)

	def getDisplayG(self):
		return super().getAsDisplayInt(11, 1, False, False, False)

	def getB(self):
		return super().getAsInt(12, 1, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(12, 1, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(12, 1, False, False, False)

	def getSHO(self):
		return super().getAsInt(13, 3, False, False, False)

	def setSHO(self, value, isRounded=False):
		return super().setAsInt(13, 3, value, isRounded, False, False, False)

	def getDisplaySHO(self):
		return super().getAsDisplayInt(13, 3, False, False, False)

	def getAMA(self):
		return super().getAsInt(16, 1, False, False, False)

	def setAMA(self, value, isRounded=False):
		return super().setAsInt(16, 1, value, isRounded, False, False, False)

	def getDisplayAMA(self):
		return super().getAsDisplayInt(16, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		R, G, B = INP.split(" ")
		self.setR(R)
		self.setG(G)
		self.setB(B)
		self.setSHO(self.getINP2() / 4)
		self.setAMA(self.getINP2() % 4)
		if self.getAMA() == 0 :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()
		exit()
converted().main()