import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(22)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getC1(self):
		return super().getAsString(10, 3)

	def setC1(self, value):
		return super().setAsString(10, 3, value)

	def getDisplayC1(self):
		return super().getAsString(10, 3)

	def getC11(self):
		return super().getAsString(10, 1)

	def setC11(self, value):
		return super().setAsString(10, 1, value)

	def setC11(self, value):
		return super().setAsString(10, 1, value)

	def getDisplayC11(self):
		return super().getAsString(10, 1)

	def getC12(self):
		return super().getAsString(11, 1)

	def setC12(self, value):
		return super().setAsString(11, 1, value)

	def setC12(self, value):
		return super().setAsString(11, 1, value)

	def getDisplayC12(self):
		return super().getAsString(11, 1)

	def getC13(self):
		return super().getAsString(12, 1)

	def setC13(self, value):
		return super().setAsString(12, 1, value)

	def setC13(self, value):
		return super().setAsString(12, 1, value)

	def getDisplayC13(self):
		return super().getAsString(12, 1)

	def getC2(self):
		return super().getAsString(13, 3)

	def setC2(self, value):
		return super().setAsString(13, 3, value)

	def getDisplayC2(self):
		return super().getAsString(13, 3)

	def getC21(self):
		return super().getAsString(13, 1)

	def setC21(self, value):
		return super().setAsString(13, 1, value)

	def setC21(self, value):
		return super().setAsString(13, 1, value)

	def getDisplayC21(self):
		return super().getAsString(13, 1)

	def getC22(self):
		return super().getAsString(14, 1)

	def setC22(self, value):
		return super().setAsString(14, 1, value)

	def setC22(self, value):
		return super().setAsString(14, 1, value)

	def getDisplayC22(self):
		return super().getAsString(14, 1)

	def getC23(self):
		return super().getAsString(15, 1)

	def setC23(self, value):
		return super().setAsString(15, 1, value)

	def setC23(self, value):
		return super().setAsString(15, 1, value)

	def getDisplayC23(self):
		return super().getAsString(15, 1)

	def getC3(self):
		return super().getAsString(16, 3)

	def setC3(self, value):
		return super().setAsString(16, 3, value)

	def getDisplayC3(self):
		return super().getAsString(16, 3)

	def getC31(self):
		return super().getAsString(16, 1)

	def setC31(self, value):
		return super().setAsString(16, 1, value)

	def setC31(self, value):
		return super().setAsString(16, 1, value)

	def getDisplayC31(self):
		return super().getAsString(16, 1)

	def getC32(self):
		return super().getAsString(17, 1)

	def setC32(self, value):
		return super().setAsString(17, 1, value)

	def setC32(self, value):
		return super().setAsString(17, 1, value)

	def getDisplayC32(self):
		return super().getAsString(17, 1)

	def getC33(self):
		return super().getAsString(18, 1)

	def setC33(self, value):
		return super().setAsString(18, 1, value)

	def setC33(self, value):
		return super().setAsString(18, 1, value)

	def getDisplayC33(self):
		return super().getAsString(18, 1)

	def getOUT(self):
		return super().getAsString(19, 3)

	def setOUT(self, value):
		return super().setAsString(19, 3, value)

	def setOUT(self, value):
		return super().setAsString(19, 3, value)

	def getDisplayOUT(self):
		return super().getAsString(19, 3)

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
		self.setC1(self.getINP())
		INP = input()
		self.setINP( INP )
		self.setC2(self.getINP())
		INP = input()
		self.setINP( INP )
		self.setC3(self.getINP())
		self.setOUT( self.getC11() + self.getC22() + self.getC33())
		print(self.getDisplayOUT(), sep='')
		exit()
		exit()
converted().main()