import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getINP(self):
		return super().getAsInt(0, 2, False, False, False)

	def setINP(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDisplayINP(self):
		return super().getAsDisplayInt(0, 2, False, False, False)

	def getA(self):
		return super().getAsInt(2, 1, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(2, 1, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(2, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		INP = input()
		self.setINP( INP )
		self.setA( self.getINP()/10)
		self.setINP( self.getINP()-self.getA()*10)
		if self.getA() == 9 or self.getINP() == 9 :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()

	def MAIN_flow(self):
		INP = input()
		self.setINP( INP )
		self.setA( self.getINP()/10)
		self.setINP( self.getINP()-self.getA()*10)
		if self.getA() == 9 or self.getINP() == 9 :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()