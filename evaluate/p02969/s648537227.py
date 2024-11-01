import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(196)

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
		return super().getAsString(115, 6)

	def setB(self, value):
		return super().setAsString(115, 6, value)

	def setB(self, value):
		return super().setAsString(115, 6, value)

	def getDisplayB(self):
		return super().getAsString(115, 6)

	def getC(self):
		return super().getAsInt(121, 15, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(121, 15, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(121, 15, False, False, False)

	def getT(self):
		return super().getAsInt(136, 15, False, False, False)

	def setT(self, value, isRounded=False):
		return super().setAsInt(136, 15, value, isRounded, False, False, False)

	def getDisplayT(self):
		return super().getAsDisplayInt(136, 15, False, False, False)

	def getTEMP1(self):
		return super().getAsInt(151, 15, False, False, False)

	def setTEMP1(self, value, isRounded=False):
		return super().setAsInt(151, 15, value, isRounded, False, False, False)

	def getDisplayTEMP1(self):
		return super().getAsDisplayInt(151, 15, False, False, False)

	def getTEMP2(self):
		return super().getAsInt(166, 15, False, False, False)

	def setTEMP2(self, value, isRounded=False):
		return super().setAsInt(166, 15, value, isRounded, False, False, False)

	def getDisplayTEMP2(self):
		return super().getAsDisplayInt(166, 15, False, False, False)

	def getN(self):
		return super().getAsInt(181, 15, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(181, 15, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(181, 15, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		A = input()
		self.setA( A )
		self.setA( 3*self.getA()*self.getA())
		self.setB(self.getA())
		print(self.getDisplayB(), sep='')
		exit()

	def MAIN_flow(self):
		A = input()
		self.setA( A )
		self.setA( 3*self.getA()*self.getA())
		self.setB(self.getA())
		print(self.getDisplayB(), sep='')
		exit()
		exit()
converted().main()