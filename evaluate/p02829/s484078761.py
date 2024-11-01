import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(116)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getN(self):
		return super().getAsInt(100, 8, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(100, 8, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(100, 8, False, False, False)

	def getM(self):
		return super().getAsInt(108, 8, False, False, False)

	def setM(self, value, isRounded=False):
		return super().setAsInt(108, 8, value, isRounded, False, False, False)

	def getDisplayM(self):
		return super().getAsDisplayInt(108, 8, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		n = input()
		self.setN( n )
		m = input()
		self.setM( m )
		if self.getN() == 1 :
			if self.getM() == 2 :
				print("3", sep='')
			if self.getM() == 3 :
				print("2", sep='')
		if self.getN() == 2 :
			if self.getM() == 1 :
				print("3", sep='')
			if self.getM() == 3 :
				print("1", sep='')
		if self.getN() == 3 :
			if self.getM() == 2 :
				print("1", sep='')
			if self.getM() == 1 :
				print("2", sep='')
		exit()
		exit()
converted().main()