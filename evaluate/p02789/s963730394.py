import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(106)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getVARN(self):
		return super().getAsInt(100, 3, False, False, False)

	def setVARN(self, value, isRounded=False):
		return super().setAsInt(100, 3, value, isRounded, False, False, False)

	def getDisplayVARN(self):
		return super().getAsDisplayInt(100, 3, False, False, False)

	def getVARM(self):
		return super().getAsInt(103, 3, False, False, False)

	def setVARM(self, value, isRounded=False):
		return super().setAsInt(103, 3, value, isRounded, False, False, False)

	def getDisplayVARM(self):
		return super().getAsDisplayInt(103, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INDATA = input()
		self.setINDATA( INDATA )
		VARN, VARM = INDATA.split(' ')
		self.setVARN(VARN)
		self.setVARM(VARM)
		if self.getVARN() == self.getVARM() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()