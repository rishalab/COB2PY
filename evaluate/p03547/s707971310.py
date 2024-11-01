import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(5)

	def getINP(self):
		return super().getAsString(0, 3)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayINP(self):
		return super().getAsString(0, 3)

	def getX(self):
		return super().getAsString(3, 1)

	def setX(self, value):
		return super().setAsString(3, 1, value)

	def setX(self, value):
		return super().setAsString(3, 1, value)

	def getDisplayX(self):
		return super().getAsString(3, 1)

	def getY(self):
		return super().getAsString(4, 1)

	def setY(self, value):
		return super().setAsString(4, 1, value)

	def setY(self, value):
		return super().setAsString(4, 1, value)

	def getDisplayY(self):
		return super().getAsString(4, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		X, Y = INP.split(' ')
		self.setX(X)
		self.setY(Y)
		if self.getX() < self.getY() :
			print('<', sep='')
		else:
			if self.getX() == self.getY() :
				print('=', sep='')
			else:
				print('>', sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		X, Y = INP.split(' ')
		self.setX(X)
		self.setY(Y)
		if self.getX() < self.getY() :
			print('<', sep='')
		else:
			if self.getX() == self.getY() :
				print('=', sep='')
			else:
				print('>', sep='')
		exit()
		exit()
converted().main()