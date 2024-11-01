import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(26)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getH1(self):
		return super().getAsInt(10, 2, False, False, False)

	def setH1(self, value, isRounded=False):
		return super().setAsInt(10, 2, value, isRounded, False, False, False)

	def getDisplayH1(self):
		return super().getAsDisplayInt(10, 2, False, False, False)

	def getW1(self):
		return super().getAsInt(12, 2, False, False, False)

	def setW1(self, value, isRounded=False):
		return super().setAsInt(12, 2, value, isRounded, False, False, False)

	def getDisplayW1(self):
		return super().getAsDisplayInt(12, 2, False, False, False)

	def getH2(self):
		return super().getAsInt(14, 2, False, False, False)

	def setH2(self, value, isRounded=False):
		return super().setAsInt(14, 2, value, isRounded, False, False, False)

	def getDisplayH2(self):
		return super().getAsDisplayInt(14, 2, False, False, False)

	def getW2(self):
		return super().getAsInt(16, 2, False, False, False)

	def setW2(self, value, isRounded=False):
		return super().setAsInt(16, 2, value, isRounded, False, False, False)

	def getDisplayW2(self):
		return super().getAsDisplayInt(16, 2, False, False, False)

	def getWANS(self):
		return super().getAsInt(18, 4, False, False, False)

	def setWANS(self, value, isRounded=False):
		return super().setAsInt(18, 4, value, isRounded, False, False, False)

	def getDisplayWANS(self):
		return super().getAsDisplayInt(18, 4, False, False, False)

	def getANS(self):
		return super().getAsString(22, 4)

	def setANS(self, value):
		return super().setAsString(22, 4, value)

	def setANS(self, value):
		return super().setAsString(22, 4, value)

	def getDisplayANS(self):
		return super().getAsString(22, 4)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		H1, W1 = INP.split(' ')
		self.setH1(H1)
		self.setW1(W1)
		INP = input()
		self.setINP( INP )
		H2, W2 = INP.split(' ')
		self.setH2(H2)
		self.setW2(W2)
		self.setWANS( (self.getH1()-self.getH2())*(self.getW1()-self.getW2()))
		self.setANS(self.getWANS())
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()