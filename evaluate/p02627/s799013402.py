import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getA(self):
		return super().getAsString(0, 1)

	def setA(self, value):
		return super().setAsString(0, 1, value)

	def setA(self, value):
		return super().setAsString(0, 1, value)

	def getDisplayA(self):
		return super().getAsString(0, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		a = input()
		self.setA( a )
		if self.getA() <= "Z" :
			print("A", sep='')
		else:
			print("a", sep='')
		exit()
		exit()
converted().main()