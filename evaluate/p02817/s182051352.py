import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(700)

	def getINP(self):
		return super().getAsString(0, 300)

	def setINP(self, value):
		return super().setAsString(0, 300, value)

	def setINP(self, value):
		return super().setAsString(0, 300, value)

	def getDisplayINP(self):
		return super().getAsString(0, 300)

	def getS(self):
		return super().getAsString(300, 100)

	def setS(self, value):
		return super().setAsString(300, 100, value)

	def setS(self, value):
		return super().setAsString(300, 100, value)

	def getDisplayS(self):
		return super().getAsString(300, 100)

	def getT(self):
		return super().getAsString(400, 100)

	def setT(self, value):
		return super().setAsString(400, 100, value)

	def setT(self, value):
		return super().setAsString(400, 100, value)

	def getDisplayT(self):
		return super().getAsString(400, 100)

	def getOUT(self):
		return super().getAsString(500, 200)

	def setOUT(self, value):
		return super().setAsString(500, 200, value)

	def setOUT(self, value):
		return super().setAsString(500, 200, value)

	def getDisplayOUT(self):
		return super().getAsString(500, 200)

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
		INP = input()
		self.setINP( INP )
		S, T = INP.split(" ")
		self.setS(S)
		self.setT(T)
		self.setOUT( self.getT() + self.getS())
		print(self.getDisplayOUT(), sep='')
		exit()
		exit()
converted().main()