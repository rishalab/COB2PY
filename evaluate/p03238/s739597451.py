import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(169)

	def getINDATA(self):
		return super().getAsString(0, 100)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def setINDATA(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINDATA(self):
		return super().getAsString(0, 100)

	def getA1(self):
		return super().getAsInt(100, 8, False, False, False)

	def setA1(self, value, isRounded=False):
		return super().setAsInt(100, 8, value, isRounded, False, False, False)

	def getDisplayA1(self):
		return super().getAsDisplayInt(100, 8, False, False, False)

	def getA2(self):
		return super().getAsInt(108, 8, False, False, False)

	def setA2(self, value, isRounded=False):
		return super().setAsInt(108, 8, value, isRounded, False, False, False)

	def getDisplayA2(self):
		return super().getAsDisplayInt(108, 8, False, False, False)

	def getA3(self):
		return super().getAsInt(116, 8, False, False, False)

	def setA3(self, value, isRounded=False):
		return super().setAsInt(116, 8, value, isRounded, False, False, False)

	def getDisplayA3(self):
		return super().getAsDisplayInt(116, 8, False, False, False)

	def getR(self):
		return super().getAsInt(124, 8, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(124, 8, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(124, 8, False, False, False)

	def getG(self):
		return super().getAsInt(132, 8, False, False, False)

	def setG(self, value, isRounded=False):
		return super().setAsInt(132, 8, value, isRounded, False, False, False)

	def getDisplayG(self):
		return super().getAsDisplayInt(132, 8, False, False, False)

	def getR2(self):
		return super().getAsInt(140, 8, False, False, False)

	def setR2(self, value, isRounded=False):
		return super().setAsInt(140, 8, value, isRounded, False, False, False)

	def getDisplayR2(self):
		return super().getAsDisplayInt(140, 8, False, False, False)

	def getDISP(self):
		return super().getAsString(148, 21)

	def setDISP(self, value):
		return super().setAsString(148, 21, value)

	def setDISP(self, value):
		return super().setAsString(148, 21, value)

	def getDisplayDISP(self):
		return super().getAsString(148, 21)

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
		a1 = input()
		self.setA1( a1 )
		if self.getA1() == 1 :
			print("Hello World", sep='')
		else:
			a2 = input()
			self.setA2( a2 )
			a3 = input()
			self.setA3( a3 )
			self.setR( self.getA3()+self.getA2())
			self.setDISP(self.getR())
			print(self.getDisplayDISP(), sep='')
		exit()
		exit()
converted().main()