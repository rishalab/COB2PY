import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getB(self):
		return super().getAsString(0, 1)

	def setB(self, value):
		return super().setAsString(0, 1, value)

	def setB(self, value):
		return super().setAsString(0, 1, value)

	def getDisplayB(self):
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
		B = input()
		self.setB( B )
		if (TRUE == self.getB() == 'A'):
			print('T', sep='')
		elif (TRUE == self.getB() == 'T'):
			print('A', sep='')
		elif (TRUE == self.getB() == 'C'):
			print('G', sep='')
		elif (TRUE == self.getB() == 'G'):
			print('C', sep='')
		else:
			pass
		exit()
		exit()
converted().main()