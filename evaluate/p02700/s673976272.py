import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(75)

	def getLN(self):
		return super().getAsString(0, 15)

	def setLN(self, value):
		return super().setAsString(0, 15, value)

	def setLN(self, value):
		return super().setAsString(0, 15, value)

	def getDisplayLN(self):
		return super().getAsString(0, 15)

	def getA(self):
		return super().getAsInt(15, 10, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(15, 10, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(15, 10, False, False, False)

	def getB(self):
		return super().getAsInt(25, 10, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(25, 10, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(25, 10, False, False, False)

	def getC(self):
		return super().getAsInt(35, 10, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(35, 10, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(35, 10, False, False, False)

	def getD(self):
		return super().getAsInt(45, 10, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(45, 10, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(45, 10, False, False, False)

	def getTK(self):
		return super().getAsInt(55, 10, False, False, False)

	def setTK(self, value, isRounded=False):
		return super().setAsInt(55, 10, value, isRounded, False, False, False)

	def getDisplayTK(self):
		return super().getAsDisplayInt(55, 10, False, False, False)

	def getAK(self):
		return super().getAsInt(65, 10, False, False, False)

	def setAK(self, value, isRounded=False):
		return super().setAsInt(65, 10, value, isRounded, False, False, False)

	def getDisplayAK(self):
		return super().getAsDisplayInt(65, 10, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		ln = input()
		self.setLN( ln )
		A, B, C, D = ln.split(' ')
		self.setA(A)
		self.setB(B)
		self.setC(C)
		self.setD(D)
		self.setTK( (self.getC()+self.getB()-1)/self.getB())
		self.setAK( (self.getA()+self.getD()-1)/self.getD())
		if self.getTK() <= self.getAK() :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()