import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(30)

	def getS(self):
		return super().getAsString(0, 30)

	def setS(self, value):
		return super().setAsString(0, 30, value)

	def setS(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayS(self):
		return super().getAsString(0, 30)

	def unstring(input_str, delimiter, *variables):
		parts = input_str.split(delimiter)
		result = []
		for i in range(min(len(parts), len(variables))):
			result.append(parts[i])
		result.extend([''] * (len(variables) - len(result)))
		return tuple(result)
	def initialize(self):
		pass
	def main(self):
		self.initialize()
		S = input()
		self.setS( S )
		if self.getS() == "Sunny" :
			print("Cloudy", sep='')
		else:
			if self.getS() == "Cloudy" :
				print("Rainy", sep='')
			else:
				print("Sunny", sep='')
		exit()
		exit()
converted().main()