import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(68)

	def getINP(self):
		return super().getAsString(0, 30)

	def setINP(self, value):
		return super().setAsString(0, 30, value)

	def setINP(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayINP(self):
		return super().getAsString(0, 30)

	def getS(self):
		return super().getAsString(30, 10)

	def setS(self, value):
		return super().setAsString(30, 10, value)

	def setS(self, value):
		return super().setAsString(30, 10, value)

	def getDisplayS(self):
		return super().getAsString(30, 10)

	def getT(self):
		return super().getAsString(40, 10)

	def setT(self, value):
		return super().setAsString(40, 10, value)

	def setT(self, value):
		return super().setAsString(40, 10, value)

	def getDisplayT(self):
		return super().getAsString(40, 10)

	def getA(self):
		return super().getAsInt(50, 2, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(50, 2, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(50, 2, False, False, False)

	def getB(self):
		return super().getAsInt(52, 2, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(52, 2, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(52, 2, False, False, False)

	def getU(self):
		return super().getAsString(54, 10)

	def setU(self, value):
		return super().setAsString(54, 10, value)

	def setU(self, value):
		return super().setAsString(54, 10, value)

	def getDisplayU(self):
		return super().getAsString(54, 10)

	def getANS_A(self):
		return super().getAsString(64, 2)

	def setANS_A(self, value):
		return super().setAsString(64, 2, value)

	def setANS_A(self, value):
		return super().setAsString(64, 2, value)

	def getDisplayANS_A(self):
		return super().getAsString(64, 2)

	def getANS_B(self):
		return super().getAsString(66, 2)

	def setANS_B(self, value):
		return super().setAsString(66, 2, value)

	def setANS_B(self, value):
		return super().setAsString(66, 2, value)

	def getDisplayANS_B(self):
		return super().getAsString(66, 2)

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
		S, T = INP.split(' ')
		self.setS(S)
		self.setT(T)
		INP = input()
		self.setINP( INP )
		A, B = INP.split(' ')
		self.setA(A)
		self.setB(B)
		INP = input()
		self.setINP( INP )
		self.setU(self.getINP())
		if self.getS() == self.getU() :
			self.setANS_A( self.getA()-1)
			self.setANS_B(self.getB())
		else:
			self.setANS_A(self.getA())
			self.setANS_B( self.getB()-1)
		print(self.getDisplayANS_A(), ' ', self.getDisplayANS_B(), sep='')
		exit()
		exit()
converted().main()