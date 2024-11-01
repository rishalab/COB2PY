import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getR(self):
		return super().getAsInt(0, 4, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		R = input()
		self.setR( R )
		if self.getR() < 1200 :
			print("ABC", sep='')
		else:
			if self.getR() < 2800 :
				print("ARC", sep='')
			else:
				print("AGC", sep='')
		exit()
		exit()
converted().main()