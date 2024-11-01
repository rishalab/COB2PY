import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(104)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getIN_A(self):
		return super().getAsInt(100, 2, False, False, False)

	def setIN_A(self, value, isRounded=False):
		return super().setAsInt(100, 2, value, isRounded, False, False, False)

	def getDisplayIN_A(self):
		return super().getAsDisplayInt(100, 2, False, False, False)

	def getIN_B(self):
		return super().getAsInt(102, 2, False, False, False)

	def setIN_B(self, value, isRounded=False):
		return super().setAsInt(102, 2, value, isRounded, False, False, False)

	def getDisplayIN_B(self):
		return super().getAsDisplayInt(102, 2, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		if (self.getIN_A() <= 8) and (self.getIN_B() <= 8) :
			print('Yay!', sep='')
		else:
			print(':(', sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		if (self.getIN_A() <= 8) and (self.getIN_B() <= 8) :
			print('Yay!', sep='')
		else:
			print(':(', sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()