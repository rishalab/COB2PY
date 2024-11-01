import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(100)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		indata = input()
		self.setINDATA( indata )
		if self.getINDATA() == "SUN" :
			print("7", sep='')
		if self.getINDATA() == "MON" :
			print("6", sep='')
		if self.getINDATA() == "TUE" :
			print("5", sep='')
		if self.getINDATA() == "WED" :
			print("4", sep='')
		if self.getINDATA() == "THU" :
			print("3", sep='')
		if self.getINDATA() == "FRI" :
			print("2", sep='')
		if self.getINDATA() == "SAT" :
			print("1", sep='')
		exit()
		exit()
converted().main()