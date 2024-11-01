import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(27)

	def getN(self):
		return super().getAsInt(0, 3, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 3, False, False, False)

	def getX(self):
		return super().getAsInt(3, 5, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(3, 5, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(3, 5, False, False, False)

	def getY(self):
		return super().getAsInt(8, 5, False, False, False)

	def setY(self, value, isRounded=False):
		return super().setAsInt(8, 5, value, isRounded, False, False, False)

	def getDisplayY(self):
		return super().getAsDisplayInt(8, 5, False, False, False)

	def getSHO(self):
		return super().getAsInt(13, 2, False, False, False)

	def setSHO(self, value, isRounded=False):
		return super().setAsInt(13, 2, value, isRounded, False, False, False)

	def getDisplaySHO(self):
		return super().getAsDisplayInt(13, 2, False, False, False)

	def getAMA(self):
		return super().getAsInt(15, 2, False, False, False)

	def setAMA(self, value, isRounded=False):
		return super().setAsInt(15, 2, value, isRounded, False, False, False)

	def getDisplayAMA(self):
		return super().getAsDisplayInt(15, 2, False, False, False)

	def getANS(self):
		return super().getAsInt(17, 5, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(17, 5, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(17, 5, False, False, False)

	def getANSS(self):
		return super().getAsString(22, 5)

	def setANSS(self, value):
		return super().setAsString(22, 5, value)

	def setANSS(self, value):
		return super().setAsString(22, 5, value)

	def getDisplayANSS(self):
		return super().getAsString(22, 5)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		self.setX( 800*self.getN())
		self.setSHO(self.getN() / 15)
		self.setAMA(self.getN() % 15)
		self.setY( 200*self.getSHO())
		self.setANS( self.getX()-self.getY())
		self.setANSS(self.getANS())
		print(self.getDisplayANSS(), sep='')
		exit()
		exit()
converted().main()