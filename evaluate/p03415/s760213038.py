import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(15)

	def getINP(self):
		return super().getAsString(0, 3)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def setINP(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayINP(self):
		return super().getAsString(0, 3)

	def getC1(self):
		return super().getAsString(3, 3)

	def setC1(self, value):
		return super().setAsString(3, 3, value)

	def getDisplayC1(self):
		return super().getAsString(3, 3)

	def getC11(self):
		return super().getAsString(3, 1)

	def setC11(self, value):
		return super().setAsString(3, 1, value)

	def setC11(self, value):
		return super().setAsString(3, 1, value)

	def getDisplayC11(self):
		return super().getAsString(3, 1)

	def get(self):
		return super().getAsString(4, 2)

	def set(self, value):
		return super().setAsString(4, 2, value)

	def set(self, value):
		return super().setAsString(4, 2, value)

	def getDisplay(self):
		return super().getAsString(4, 2)

	def getC2(self):
		return super().getAsString(6, 3)

	def setC2(self, value):
		return super().setAsString(6, 3, value)

	def getDisplayC2(self):
		return super().getAsString(6, 3)

	def get_1(self):
		return super().getAsString(6, 1)

	def set_1(self, value):
		return super().setAsString(6, 1, value)

	def set_1(self, value):
		return super().setAsString(6, 1, value)

	def getDisplay_1(self):
		return super().getAsString(6, 1)

	def getC22(self):
		return super().getAsString(7, 1)

	def setC22(self, value):
		return super().setAsString(7, 1, value)

	def setC22(self, value):
		return super().setAsString(7, 1, value)

	def getDisplayC22(self):
		return super().getAsString(7, 1)

	def get_2(self):
		return super().getAsString(8, 1)

	def set_2(self, value):
		return super().setAsString(8, 1, value)

	def set_2(self, value):
		return super().setAsString(8, 1, value)

	def getDisplay_2(self):
		return super().getAsString(8, 1)

	def getC3(self):
		return super().getAsString(9, 3)

	def setC3(self, value):
		return super().setAsString(9, 3, value)

	def getDisplayC3(self):
		return super().getAsString(9, 3)

	def get_3(self):
		return super().getAsString(9, 2)

	def set_3(self, value):
		return super().setAsString(9, 2, value)

	def set_3(self, value):
		return super().setAsString(9, 2, value)

	def getDisplay_3(self):
		return super().getAsString(9, 2)

	def getC33(self):
		return super().getAsString(11, 1)

	def setC33(self, value):
		return super().setAsString(11, 1, value)

	def setC33(self, value):
		return super().setAsString(11, 1, value)

	def getDisplayC33(self):
		return super().getAsString(11, 1)

	def getANS(self):
		return super().getAsString(12, 3)

	def setANS(self, value):
		return super().setAsString(12, 3, value)

	def getDisplayANS(self):
		return super().getAsString(12, 3)

	def getA1(self):
		return super().getAsString(12, 1)

	def setA1(self, value):
		return super().setAsString(12, 1, value)

	def setA1(self, value):
		return super().setAsString(12, 1, value)

	def getDisplayA1(self):
		return super().getAsString(12, 1)

	def getA2(self):
		return super().getAsString(13, 1)

	def setA2(self, value):
		return super().setAsString(13, 1, value)

	def setA2(self, value):
		return super().setAsString(13, 1, value)

	def getDisplayA2(self):
		return super().getAsString(13, 1)

	def getA3(self):
		return super().getAsString(14, 1)

	def setA3(self, value):
		return super().setAsString(14, 1, value)

	def setA3(self, value):
		return super().setAsString(14, 1, value)

	def getDisplayA3(self):
		return super().getAsString(14, 1)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		self.setC1( self.getINP())
		INP = input()
		self.setINP( INP )
		self.setC2( self.getINP())
		INP = input()
		self.setINP( INP )
		self.setC3( self.getINP())
		self.setA1(self.getC11())
		self.setA2(self.getC22())
		self.setA3(self.getC33())
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()