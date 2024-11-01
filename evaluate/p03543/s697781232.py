import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(20)

	def getN(self):
		return super().getAsInt(0, 4, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def getA(self):
		return super().getAsInt(4, 4, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(4, 4, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(4, 4, False, False, False)

	def getB(self):
		return super().getAsInt(8, 4, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(8, 4, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(8, 4, False, False, False)

	def getC(self):
		return super().getAsInt(12, 4, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(12, 4, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(12, 4, False, False, False)

	def getD(self):
		return super().getAsInt(16, 4, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(16, 4, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(16, 4, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		N = input()
		self.setN( N )
		self.setA( self.getN()/1000)
		self.setB( self.getN()-self.getA()*1000)
		self.setB( self.getB()/100)
		self.setC( self.getN()-self.getA()*1000-self.getB()*100)
		self.setC( self.getC()/10)
		self.setD( self.getN()-self.getA()*1000-self.getB()*100-self.getC()*10)
		if self.getA() == self.getB() and self.getB() == self.getC() :
			print("Yes", sep='')
		else:
			if self.getB() == self.getC() and self.getC() == self.getD() :
				print("Yes", sep='')
			else:
				print("No", sep='')
		exit()

	def MAIN_flow(self):
		N = input()
		self.setN( N )
		self.setA( self.getN()/1000)
		self.setB( self.getN()-self.getA()*1000)
		self.setB( self.getB()/100)
		self.setC( self.getN()-self.getA()*1000-self.getB()*100)
		self.setC( self.getC()/10)
		self.setD( self.getN()-self.getA()*1000-self.getB()*100-self.getC()*10)
		if self.getA() == self.getB() and self.getB() == self.getC() :
			print("Yes", sep='')
		else:
			if self.getB() == self.getC() and self.getC() == self.getD() :
				print("Yes", sep='')
			else:
				print("No", sep='')
		exit()
		exit()
converted().main()