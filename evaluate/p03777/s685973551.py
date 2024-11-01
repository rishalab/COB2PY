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

	def getA(self):
		return super().getAsString(3, 1)

	def setA(self, value):
		return super().setAsString(3, 1, value)

	def setA(self, value):
		return super().setAsString(3, 1, value)

	def getDisplayA(self):
		return super().getAsString(3, 1)

	def getB(self):
		return super().getAsString(4, 1)

	def setB(self, value):
		return super().setAsString(4, 1, value)

	def setB(self, value):
		return super().setAsString(4, 1, value)

	def getDisplayB(self):
		return super().getAsString(4, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		A, B = INP.split(' ')
		self.setA(A)
		self.setB(B)
		if self.getA() == 'H' :
			print(self.getDisplayB(), sep='')
		else:
			if self.getB() == 'H' :
				print('D', sep='')
			else:
				print('H', sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		A, B = INP.split(' ')
		self.setA(A)
		self.setB(B)
		if self.getA() == 'H' :
			print(self.getDisplayB(), sep='')
		else:
			if self.getB() == 'H' :
				print('D', sep='')
			else:
				print('H', sep='')
		exit()
		exit()
converted().main()