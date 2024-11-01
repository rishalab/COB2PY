import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getINP(self):
		return super().getAsString(0, 3)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayINP(self):
		return super().getAsString(0, 3)

	def getS1(self):
		return super().getAsString(0, 1)

	def setS1(self, value):
		return super().setAsString(0, 1, value)

	def setS1(self, value):
		return super().setAsString(0, 1, value)

	def getDisplayS1(self):
		return super().getAsString(0, 1)

	def getS2(self):
		return super().getAsString(1, 1)

	def setS2(self, value):
		return super().setAsString(1, 1, value)

	def setS2(self, value):
		return super().setAsString(1, 1, value)

	def getDisplayS2(self):
		return super().getAsString(1, 1)

	def getS3(self):
		return super().getAsString(2, 1)

	def setS3(self, value):
		return super().setAsString(2, 1, value)

	def setS3(self, value):
		return super().setAsString(2, 1, value)

	def getDisplayS3(self):
		return super().getAsString(2, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		INP = input()
		self.setINP( INP )
		if (self.getS1() == self.getS2()) and (self.getS1() == self.getS3()) :
			print('No', sep='')
		else:
			print('Yes', sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		INP = input()
		self.setINP( INP )
		if (self.getS1() == self.getS2()) and (self.getS1() == self.getS3()) :
			print('No', sep='')
		else:
			print('Yes', sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()