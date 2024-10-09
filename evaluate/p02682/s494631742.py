import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(204)

	def getINP(self):
		return super().getAsString(0, 144)

	def setINP(self, value):
		return super().setAsString(0, 144, value)

	def setINP(self, value):
		return super().setAsString(0, 144, value)

	def getDisplayINP(self):
		return super().getAsString(0, 144)

	def getA(self):
		return super().getAsInt(144, 10, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(144, 10, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(144, 10, False, False, False)

	def getB(self):
		return super().getAsInt(154, 10, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(154, 10, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(154, 10, False, False, False)

	def getC(self):
		return super().getAsInt(164, 10, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(164, 10, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(164, 10, False, False, False)

	def getK(self):
		return super().getAsInt(174, 10, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(174, 10, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(174, 10, False, False, False)

	def getCNT(self):
		return super().getAsInt(184, 10, True, False, False)

	def setCNT(self, value, isRounded=False):
		return super().setAsInt(184, 10, value, isRounded, True, False, False)

	def getDisplayCNT(self):
		return super().getAsDisplayInt(184, 10, True, False, False)

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
		A, B, C, K = INP.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		self.setK(K)
		if (self.getA() >= self.getK()) :
			self.setA(self.getK())
			self.setC(0)
		else:
			if (self.getA()+self.getB() >= self.getK()) :
				self.setC(0)
			else:
				self.setC( self.getK()-self.getA()-self.getB())
		self.setCNT( self.getA()-self.getC())
		self.setOUT(self.getCNT())
		print(self.getDisplayOUT(), sep='')
		exit()
		exit()
converted().main()