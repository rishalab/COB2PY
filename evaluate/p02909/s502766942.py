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
		if self.getINDATA() == "Sunny" :
			print("Cloudy", sep='')
		if self.getINDATA() == "Cloudy" :
			print("Rainy", sep='')
		if self.getINDATA() == "Rainy" :
			print("Sunny", sep='')
		exit()
		exit()
converted().main()