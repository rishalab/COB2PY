import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(103)

	def getLN(self):
		return super().getAsString(0, 43)

	def setLN(self, value):
		return super().setAsString(0, 43, value)

	def setLN(self, value):
		return super().setAsString(0, 43, value)

	def getDisplayLN(self):
		return super().getAsString(0, 43)

	def getA(self):
		return super().getAsInt(43, 10, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(43, 10, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(43, 10, False, False, False)

	def getB(self):
		return super().getAsInt(53, 10, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(53, 10, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(53, 10, False, False, False)

	def getC(self):
		return super().getAsInt(63, 10, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(63, 10, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(63, 10, False, False, False)

	def getK(self):
		return super().getAsInt(73, 10, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(73, 10, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(73, 10, False, False, False)

	def getANS(self):
		return super().getAsInt(83, 10, True, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(83, 10, value, isRounded, True, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(83, 10, True, False, False)

	def getZS(self):
		return super().getAsString(93, 10)

	def setZS(self, value):
		return super().setAsString(93, 10, value)

	def setZS(self, value):
		return super().setAsString(93, 10, value)

	def getDisplayZS(self):
		return super().getAsString(93, 10)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		ln = input()
		self.setLN( ln )
		A, B, C, K = ln.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		self.setK(K)
		if self.getK() <= self.getA() :
			self.setANS( self.getK())
		else:
			if self.getK() <= self.getA()+self.getB() :
				self.setANS( self.getA())
			else:
				self.setANS( self.getA()-(self.getK()-self.getA()-self.getB()))
		self.setZS(self.getANS())
		if 0 <= self.getANS() :
			print(self.getDisplayZS(), sep='')
		else:
			print("-", self.getDisplayZS(), sep='')
		exit()
		exit()
converted().main()