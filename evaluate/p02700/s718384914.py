import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(38)

	def getINP(self):
		return super().getAsString(0, 20)

	def setINP(self, value):
		return super().setAsString(0, 20, value)

	def setINP(self, value):
		return super().setAsString(0, 20, value)

	def getDisplayINP(self):
		return super().getAsString(0, 20)

	def getA(self):
		return super().getAsInt(20, 3, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(20, 3, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(20, 3, False, False, False)

	def getB(self):
		return super().getAsInt(23, 3, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(23, 3, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(23, 3, False, False, False)

	def getC(self):
		return super().getAsInt(26, 3, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(26, 3, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(26, 3, False, False, False)

	def getD(self):
		return super().getAsInt(29, 3, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(29, 3, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(29, 3, False, False, False)

	def getK1(self):
		return super().getAsInt(32, 3, False, False, False)

	def setK1(self, value, isRounded=False):
		return super().setAsInt(32, 3, value, isRounded, False, False, False)

	def getDisplayK1(self):
		return super().getAsDisplayInt(32, 3, False, False, False)

	def getK2(self):
		return super().getAsInt(35, 3, False, False, False)

	def setK2(self, value, isRounded=False):
		return super().setAsInt(35, 3, value, isRounded, False, False, False)

	def getDisplayK2(self):
		return super().getAsDisplayInt(35, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		A, B, C, D = INP.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		self.setD(D)
		self.setK1( (self.getA()+self.getD()-1)/self.getD())
		self.setK2( (self.getC()+self.getB()-1)/self.getB())
		if (self.getK1() >= self.getK2()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		exit()
		exit()
converted().main()