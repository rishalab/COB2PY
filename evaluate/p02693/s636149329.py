import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(70)

	def getLN(self):
		return super().getAsString(0, 30)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def setLN(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayLN(self):
		return super().getAsString(0, 30)

	def getA(self):
		return super().getAsInt(30, 10, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(30, 10, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(30, 10, False, False, False)

	def getB(self):
		return super().getAsInt(40, 10, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(40, 10, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(40, 10, False, False, False)

	def getK(self):
		return super().getAsInt(50, 10, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(50, 10, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(50, 10, False, False, False)

	def getQ(self):
		return super().getAsInt(60, 10, False, False, False)

	def setQ(self, value, isRounded=False):
		return super().setAsInt(60, 10, value, isRounded, False, False, False)

	def getDisplayQ(self):
		return super().getAsDisplayInt(60, 10, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		K = input()
		self.setK( K )
		ln = input()
		self.setLN( ln )
		A, B = ln.split(' ')
		self.setA(A)
		self.setB(B)
		self.setQ(self.getB() / self.getK())
		if self.getA() <= self.getQ()*self.getK() :
			print("OK", sep='')
		else:
			print("NG", sep='')
		exit()
		exit()
converted().main()