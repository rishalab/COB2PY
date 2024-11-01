import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(7)

	def getINP(self):
		return super().getAsString(0, 5)

	def setINP(self, value):
		return super().setAsString(0, 5, value)

	def getDisplayINP(self):
		return super().getAsString(0, 5)

	def getA(self):
		return super().getAsInt(0, 1, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(0, 1, False, False, False)

	def get(self):
		return super().getAsString(1, 1)

	def set(self, value):
		return super().setAsString(1, 1, value)

	def set(self, value):
		return super().setAsString(1, 1, value)

	def getDisplay(self):
		return super().getAsString(1, 1)

	def getB(self):
		return super().getAsInt(2, 1, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(2, 1, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(2, 1, False, False, False)

	def get_1(self):
		return super().getAsString(3, 1)

	def set_1(self, value):
		return super().setAsString(3, 1, value)

	def set_1(self, value):
		return super().setAsString(3, 1, value)

	def getDisplay_1(self):
		return super().getAsString(3, 1)

	def getC(self):
		return super().getAsInt(4, 1, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(4, 1, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(4, 1, False, False, False)

	def getCOUNT5(self):
		return super().getAsInt(5, 1, False, False, False)

	def setCOUNT5(self, value, isRounded=False):
		return super().setAsInt(5, 1, value, isRounded, False, False, False)

	def getDisplayCOUNT5(self):
		return super().getAsDisplayInt(5, 1, False, False, False)

	def getCOUNT7(self):
		return super().getAsInt(6, 1, False, False, False)

	def setCOUNT7(self, value, isRounded=False):
		return super().setAsInt(6, 1, value, isRounded, False, False, False)

	def getDisplayCOUNT7(self):
		return super().getAsDisplayInt(6, 1, False, False, False)

	def initialize(self):
		self.setCOUNT5(0,False)
		self.setCOUNT7(0,False)
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		if self.getA() == 5 :
			self.setCOUNT5(1+self.getCOUNT5())
		else:
			if self.getA() == 7 :
				self.setCOUNT7(1+self.getCOUNT7())
			else:
				pass
		if self.getB() == 5 :
			self.setCOUNT5(1+self.getCOUNT5())
		else:
			if self.getB() == 7 :
				self.setCOUNT7(1+self.getCOUNT7())
			else:
				pass
		if self.getC() == 5 :
			self.setCOUNT5(1+self.getCOUNT5())
		else:
			if self.getC() == 7 :
				self.setCOUNT7(1+self.getCOUNT7())
			else:
				pass
		if self.getCOUNT5() == 2 and self.getCOUNT7() == 1 :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()
		exit()
converted().main()