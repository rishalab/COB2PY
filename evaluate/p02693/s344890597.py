import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(38)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getK(self):
		return super().getAsInt(10, 4, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(10, 4, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(10, 4, False, False, False)

	def getA(self):
		return super().getAsInt(14, 4, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(14, 4, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(14, 4, False, False, False)

	def getB(self):
		return super().getAsInt(18, 4, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(18, 4, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(18, 4, False, False, False)

	def getS1(self):
		return super().getAsInt(22, 4, False, False, False)

	def setS1(self, value, isRounded=False):
		return super().setAsInt(22, 4, value, isRounded, False, False, False)

	def getDisplayS1(self):
		return super().getAsDisplayInt(22, 4, False, False, False)

	def getS2(self):
		return super().getAsInt(26, 4, False, False, False)

	def setS2(self, value, isRounded=False):
		return super().setAsInt(26, 4, value, isRounded, False, False, False)

	def getDisplayS2(self):
		return super().getAsDisplayInt(26, 4, False, False, False)

	def getA1(self):
		return super().getAsInt(30, 4, False, False, False)

	def setA1(self, value, isRounded=False):
		return super().setAsInt(30, 4, value, isRounded, False, False, False)

	def getDisplayA1(self):
		return super().getAsDisplayInt(30, 4, False, False, False)

	def getA2(self):
		return super().getAsInt(34, 4, False, False, False)

	def setA2(self, value, isRounded=False):
		return super().setAsInt(34, 4, value, isRounded, False, False, False)

	def getDisplayA2(self):
		return super().getAsDisplayInt(34, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		K = input()
		self.setK( K )
		INP = input()
		self.setINP( INP )
		A, B = INP.split(' ')
		self.setA(A)
		self.setB(B)
		self.setS1(self.getA() / self.getK())
		self.setA1(self.getA() % self.getK())
		self.setS2(self.getB() / self.getK())
		self.setA2(self.getB() % self.getK())
		if ((self.getS1() > 1) and (self.getS2() > 1)) or ((self.getA() <= self.getK()) and (self.getB() >= self.getK())) :
			print('OK', sep='')
		else:
			print('NG', sep='')
		exit()
		exit()
converted().main()