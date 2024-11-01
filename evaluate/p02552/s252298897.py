import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getX(self):
		return super().getAsInt(0, 1, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(0, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		X = input()
		self.setX( X )
		if self.getX() == 0 :
			print(1, sep='')
		else:
			print(0, sep='')
		exit()

	def MAIN_flow(self):
		X = input()
		self.setX( X )
		if self.getX() == 0 :
			print(1, sep='')
		else:
			print(0, sep='')
		exit()
		exit()
converted().main()