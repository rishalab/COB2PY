import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(108)

	def getSTR(self):
		return super().getAsString(0, 100)

	def setSTR(self, value):
		return super().setAsString(0, 100, value)

	def setSTR(self, value):
		return super().setAsString(0, 100, value)

	def getDisplaySTR(self):
		return super().getAsString(0, 100)

	def getA(self):
		return super().getAsInt(100, 2, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(100, 2, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(100, 2, False, False, False)

	def getB(self):
		return super().getAsInt(102, 2, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(102, 2, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(102, 2, False, False, False)

	def getC(self):
		return super().getAsInt(104, 2, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(104, 2, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(104, 2, False, False, False)

	def getCOUNT5(self):
		return super().getAsInt(106, 1, False, False, False)

	def setCOUNT5(self, value, isRounded=False):
		return super().setAsInt(106, 1, value, isRounded, False, False, False)

	def getDisplayCOUNT5(self):
		return super().getAsDisplayInt(106, 1, False, False, False)

	def getCOUNT7(self):
		return super().getAsInt(107, 1, False, False, False)

	def setCOUNT7(self, value, isRounded=False):
		return super().setAsInt(107, 1, value, isRounded, False, False, False)

	def getDisplayCOUNT7(self):
		return super().getAsDisplayInt(107, 1, False, False, False)

	def initialize(self):
		self.setCOUNT5(0,False)
		self.setCOUNT7(0,False)
		pass
	def main(self):
		self.initialize()
		self.MAIN_PROCEDURE_flow()
	def MAIN_PROCEDURE(self):
		STR = input()
		self.setSTR( STR )
		A, B, C = STR.split(" ")
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if (self.getA() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getA() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if (self.getB() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getB() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if (self.getC() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getC() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if self.getCOUNT5() == 2 and self.getCOUNT7() == 1 :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()

	def MAIN_PROCEDURE_flow(self):
		STR = input()
		self.setSTR( STR )
		A, B, C = STR.split(" ")
		self.setA(A)
		self.setB(B)
		self.setC(C)
		if (self.getA() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getA() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if (self.getB() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getB() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if (self.getC() == (5)):
			self.setCOUNT5(1+self.getCOUNT5())
		elif (self.getC() == (7)):
			self.setCOUNT7(1+self.getCOUNT7())
		if self.getCOUNT5() == 2 and self.getCOUNT7() == 1 :
			print("YES", sep='')
		else:
			print("NO", sep='')
		exit()
		exit()
converted().main()