import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getX(self):
		return super().getAsInt(0, 4, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		x = input()
		self.setX( x )
		if self.getX() < 1200 :
			print("ABC", sep='')
		else:
			print("ARC", sep='')
		exit()
		exit()
converted().main()