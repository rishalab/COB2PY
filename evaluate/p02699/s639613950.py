import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(50)

	def getLN(self):
		return super().getAsString(0, 30)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayLN(self):
		return super().getAsString(0, 30)

	def getS(self):
		return super().getAsInt(30, 10, False, False, False)

	def setS(self, value, isRounded=False):
		return super().setAsInt(30, 10, value, isRounded, False, False, False)

	def getDisplayS(self):
		return super().getAsDisplayInt(30, 10, False, False, False)

	def getW(self):
		return super().getAsInt(40, 10, False, False, False)

	def setW(self, value, isRounded=False):
		return super().setAsInt(40, 10, value, isRounded, False, False, False)

	def getDisplayW(self):
		return super().getAsDisplayInt(40, 10, False, False, False)

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
		ln = input()
		self.setLN( ln )
		S, W = ln.split(' ')
		self.setS(S)
		self.setW(W)
		if self.getW() < self.getS() :
			print("safe", sep='')
		else:
			print("unsafe", sep='')
		exit()
		exit()
converted().main()