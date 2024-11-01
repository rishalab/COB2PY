import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(62)

	def getINP(self):
		return super().getAsString(0, 32)

	def setINP(self, value):
		return super().setAsString(0, 32, value)

	def setINP(self, value):
		return super().setAsString(0, 32, value)

	def getDisplayINP(self):
		return super().getAsString(0, 32)

	def getX(self):
		return super().getAsInt(32, 10, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(32, 10, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(32, 10, False, False, False)

	def getA(self):
		return super().getAsInt(42, 10, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(42, 10, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(42, 10, False, False, False)

	def getB(self):
		return super().getAsInt(52, 10, True, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(52, 10, value, isRounded, True, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(52, 10, True, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		X, A, B = INP.split(' ')
		self.setX(X)
		self.setA(A)
		self.setB(B)
		self.setB(self.getB()-(self.getA()))
		if self.getB() <= 0 :
			print("delicious", sep='')
		else:
			if self.getB() <= self.getX() :
				print("safe", sep='')
			else:
				print("dangerous", sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		X, A, B = INP.split(' ')
		self.setX(X)
		self.setA(A)
		self.setB(B)
		self.setB(self.getB()-(self.getA()))
		if self.getB() <= 0 :
			print("delicious", sep='')
		else:
			if self.getB() <= self.getX() :
				print("safe", sep='')
			else:
				print("dangerous", sep='')
		exit()
		exit()
converted().main()