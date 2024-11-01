import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getINP(self):
		return super().getAsString(0, 3)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayINP(self):
		return super().getAsString(0, 3)

	def getS1(self):
		return super().getAsInt(0, 1, False, False, False)

	def setS1(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded, False, False, False)

	def getDisplayS1(self):
		return super().getAsDisplayInt(0, 1, False, False, False)

	def getS2(self):
		return super().getAsInt(1, 1, False, False, False)

	def setS2(self, value, isRounded=False):
		return super().setAsInt(1, 1, value, isRounded, False, False, False)

	def getDisplayS2(self):
		return super().getAsDisplayInt(1, 1, False, False, False)

	def getS3(self):
		return super().getAsInt(2, 1, False, False, False)

	def setS3(self, value, isRounded=False):
		return super().setAsInt(2, 1, value, isRounded, False, False, False)

	def getDisplayS3(self):
		return super().getAsDisplayInt(2, 1, False, False, False)

	def getANS(self):
		return super().getAsInt(3, 1, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(3, 1, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(3, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		self.setANS( self.getS1()+self.getS2()+self.getS3())
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()