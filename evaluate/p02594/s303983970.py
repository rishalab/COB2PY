import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(2)

	def getX(self):
		return super().getAsInt(0, 2, True, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, True, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(0, 2, True, False, False)

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
		X = input()
		self.setX( X )
		if self.getX() < 30 :
			print('No', sep='')
		else:
			print('Yes', sep='')
		exit()
		exit()
converted().main()