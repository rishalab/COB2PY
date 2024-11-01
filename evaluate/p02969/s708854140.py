import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(10)

	def getINP(self):
		return super().getAsInt(0, 3, False, False, False)

	def setINP(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded, False, False, False)

	def getDisplayINP(self):
		return super().getAsDisplayInt(0, 3, False, False, False)

	def getANS(self):
		return super().getAsString(3, 7)

	def setANS(self, value):
		return super().setAsString(3, 7, value)

	def setANS(self, value):
		return super().setAsString(3, 7, value)

	def getDisplayANS(self):
		return super().getAsString(3, 7)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		self.setANS( 3*self.getINP()*self.getINP())
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()