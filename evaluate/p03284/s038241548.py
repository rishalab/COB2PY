import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(111)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getIN_N(self):
		return super().getAsInt(100, 3, False, False, False)

	def setIN_N(self, value, isRounded=False):
		return super().setAsInt(100, 3, value, isRounded, False, False, False)

	def getDisplayIN_N(self):
		return super().getAsDisplayInt(100, 3, False, False, False)

	def getIN_K(self):
		return super().getAsInt(103, 3, False, False, False)

	def setIN_K(self, value, isRounded=False):
		return super().setAsInt(103, 3, value, isRounded, False, False, False)

	def getDisplayIN_K(self):
		return super().getAsDisplayInt(103, 3, False, False, False)

	def getMAISU(self):
		return super().getAsInt(106, 3, False, False, False)

	def setMAISU(self, value, isRounded=False):
		return super().setAsInt(106, 3, value, isRounded, False, False, False)

	def getDisplayMAISU(self):
		return super().getAsDisplayInt(106, 3, False, False, False)

	def getAMARI(self):
		return super().getAsInt(109, 2, False, False, False)

	def setAMARI(self, value, isRounded=False):
		return super().setAsInt(109, 2, value, isRounded, False, False, False)

	def getDisplayAMARI(self):
		return super().getAsDisplayInt(109, 2, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		INP = input()
		self.setINP( INP )
		IN_N, IN_K = INP.split(' ')
		self.setIN_N(IN_N)
		self.setIN_K(IN_K)
		self.setMAISU(self.getIN_N() / self.getIN_K())
		self.setAMARI(self.getIN_N() % self.getIN_K())
		if (self.getAMARI() == 0) :
			print('0', sep='')
		else:
			print('1', sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		INP = input()
		self.setINP( INP )
		IN_N, IN_K = INP.split(' ')
		self.setIN_N(IN_N)
		self.setIN_K(IN_K)
		self.setMAISU(self.getIN_N() / self.getIN_K())
		self.setAMARI(self.getIN_N() % self.getIN_K())
		if (self.getAMARI() == 0) :
			print('0', sep='')
		else:
			print('1', sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()