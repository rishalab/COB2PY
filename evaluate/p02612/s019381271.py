import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(59)

	def getN(self):
		return super().getAsInt(0, 10, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 10, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 10, False, False, False)

	def getNUM(self):
		return super().getAsInt(10, 10, False, False, False)

	def setNUM(self, value, isRounded=False):
		return super().setAsInt(10, 10, value, isRounded, False, False, False)

	def getDisplayNUM(self):
		return super().getAsDisplayInt(10, 10, False, False, False)

	def getQT(self):
		return super().getAsInt(20, 10, False, False, False)

	def setQT(self, value, isRounded=False):
		return super().setAsInt(20, 10, value, isRounded, False, False, False)

	def getDisplayQT(self):
		return super().getAsDisplayInt(20, 10, False, False, False)

	def getRM(self):
		return super().getAsInt(30, 10, False, False, False)

	def setRM(self, value, isRounded=False):
		return super().setAsInt(30, 10, value, isRounded, False, False, False)

	def getDisplayRM(self):
		return super().getAsDisplayInt(30, 10, False, False, False)

	def getANS(self):
		return super().getAsInt(40, 10, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(40, 10, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(40, 10, False, False, False)

	def getZS(self):
		return super().getAsString(50, 9)

	def setZS(self, value):
		return super().setAsString(50, 9, value)

	def setZS(self, value):
		return super().setAsString(50, 9, value)

	def getDisplayZS(self):
		return super().getAsString(50, 9)

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
		N = input()
		self.setN( N )
		self.setQT(self.getN() / 1000)
		self.setRM(self.getN() % 1000)
		self.setNUM( 1000-self.getRM())
		self.setQT(self.getNUM() / 1000)
		self.setANS(self.getNUM() % 1000)
		self.setZS(self.getANS())
		print(self.getDisplayZS(), sep='')
		exit()
		exit()
converted().main()