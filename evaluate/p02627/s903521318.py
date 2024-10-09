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
		A = input()
		self.setA( A )
		if (self.getA() >= 'A' and self.getA() <= 'Z') :
			print('A', sep='')
		else:
			print('a', sep='')
		exit()
		exit()
converted().main()