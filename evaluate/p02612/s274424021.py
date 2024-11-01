import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(16)

	def getN(self):
		return super().getAsInt(0, 5, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 5, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 5, False, False, False)

	def getS(self):
		return super().getAsInt(5, 4, False, False, False)

	def setS(self, value, isRounded=False):
		return super().setAsInt(5, 4, value, isRounded, False, False, False)

	def getDisplayS(self):
		return super().getAsDisplayInt(5, 4, False, False, False)

	def getOT(self):
		return super().getAsInt(9, 4, False, False, False)

	def setOT(self, value, isRounded=False):
		return super().setAsInt(9, 4, value, isRounded, False, False, False)

	def getDisplayOT(self):
		return super().getAsDisplayInt(9, 4, False, False, False)

	def getOUT(self):
		return super().getAsString(13, 3)

	def setOUT(self, value):
		return super().setAsString(13, 3, value)

	def setOUT(self, value):
		return super().setAsString(13, 3, value)

	def getDisplayOUT(self):
		return super().getAsString(13, 3)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		self.setS(self.getN() / 1000)
		self.setOT(self.getN() % 1000)
		self.setOT( 1000-self.getOT())
		if self.getOT() == 1000 :
			self.setOT(0)
		self.setOUT(self.getOT())
		print(self.getDisplayOUT(), sep='')
		exit()
		exit()
converted().main()