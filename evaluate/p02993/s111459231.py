import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(235)

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
		return super().getAsInt(115, 15, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(115, 15, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(115, 15, False, False, False)

	def getC(self):
		return super().getAsInt(130, 15, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(130, 15, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(130, 15, False, False, False)

	def getD(self):
		return super().getAsInt(145, 15, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(145, 15, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(145, 15, False, False, False)

	def getE(self):
		return super().getAsInt(160, 15, False, False, False)

	def setE(self, value, isRounded=False):
		return super().setAsInt(160, 15, value, isRounded, False, False, False)

	def getDisplayE(self):
		return super().getAsDisplayInt(160, 15, False, False, False)

	def getT(self):
		return super().getAsInt(175, 15, False, False, False)

	def setT(self, value, isRounded=False):
		return super().setAsInt(175, 15, value, isRounded, False, False, False)

	def getDisplayT(self):
		return super().getAsDisplayInt(175, 15, False, False, False)

	def getTEMP1(self):
		return super().getAsInt(190, 15, False, False, False)

	def setTEMP1(self, value, isRounded=False):
		return super().setAsInt(190, 15, value, isRounded, False, False, False)

	def getDisplayTEMP1(self):
		return super().getAsDisplayInt(190, 15, False, False, False)

	def getTEMP2(self):
		return super().getAsInt(205, 15, False, False, False)

	def setTEMP2(self, value, isRounded=False):
		return super().setAsInt(205, 15, value, isRounded, False, False, False)

	def getDisplayTEMP2(self):
		return super().getAsDisplayInt(205, 15, False, False, False)

	def getN(self):
		return super().getAsInt(220, 15, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(220, 15, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(220, 15, False, False, False)

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
		self.MAIN_flow()
	def MAIN(self):
		A = input()
		self.setA( A )
		self.setB( self.getA()/10)
		self.setB( self.getA()-self.getB()*10)
		self.setA( (self.getA()-self.getB())/10)
		self.setC( self.getA()/10)
		self.setC( self.getA()-self.getC()*10)
		self.setA( (self.getA()-self.getC())/10)
		self.setD( self.getA()/10)
		self.setD( self.getA()-self.getD()*10)
		self.setA( (self.getA()-self.getD())/10)
		self.setE(self.getA())
		if self.getB() == self.getC() or self.getC() == self.getD() or self.getE() == self.getD() :
			print("Bad", sep='')
		else:
			print("Good", sep='')
		exit()

	def MAIN_flow(self):
		A = input()
		self.setA( A )
		self.setB( self.getA()/10)
		self.setB( self.getA()-self.getB()*10)
		self.setA( (self.getA()-self.getB())/10)
		self.setC( self.getA()/10)
		self.setC( self.getA()-self.getC()*10)
		self.setA( (self.getA()-self.getC())/10)
		self.setD( self.getA()/10)
		self.setD( self.getA()-self.getD()*10)
		self.setA( (self.getA()-self.getD())/10)
		self.setE(self.getA())
		if self.getB() == self.getC() or self.getC() == self.getD() or self.getE() == self.getD() :
			print("Bad", sep='')
		else:
			print("Good", sep='')
		exit()
		exit()
converted().main()