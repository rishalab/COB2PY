import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(195)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getA(self):
		return super().getAsInt(100, 15, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(100, 15, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(100, 15, False, False, False)

	def getB(self):
		return super().getAsString(115, 5)

	def setB(self, value):
		return super().setAsString(115, 5, value)

	def setB(self, value):
		return super().setAsString(115, 5, value)

	def getDisplayB(self):
		return super().getAsString(115, 5)

	def getC(self):
		return super().getAsInt(120, 15, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(120, 15, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(120, 15, False, False, False)

	def getT(self):
		return super().getAsInt(135, 15, False, False, False)

	def setT(self, value, isRounded=False):
		return super().setAsInt(135, 15, value, isRounded, False, False, False)

	def getDisplayT(self):
		return super().getAsDisplayInt(135, 15, False, False, False)

	def getTEMP1(self):
		return super().getAsInt(150, 15, False, False, False)

	def setTEMP1(self, value, isRounded=False):
		return super().setAsInt(150, 15, value, isRounded, False, False, False)

	def getDisplayTEMP1(self):
		return super().getAsDisplayInt(150, 15, False, False, False)

	def getTEMP2(self):
		return super().getAsInt(165, 15, False, False, False)

	def setTEMP2(self, value, isRounded=False):
		return super().setAsInt(165, 15, value, isRounded, False, False, False)

	def getDisplayTEMP2(self):
		return super().getAsDisplayInt(165, 15, False, False, False)

	def getN(self):
		return super().getAsInt(180, 15, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(180, 15, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(180, 15, False, False, False)

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
		self.MAIN_flow()
	def MAIN(self):
		A = input()
		self.setA( A )
		self.setA( self.getA()*self.getA()*self.getA())
		self.setB(self.getA())
		print(self.getDisplayB(), sep='')
		exit()

	def MAIN_flow(self):
		A = input()
		self.setA( A )
		self.setA( self.getA()*self.getA()*self.getA())
		self.setB(self.getA())
		print(self.getDisplayB(), sep='')
		exit()
		exit()
converted().main()