import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(11)

	def getS(self):
		return super().getAsString(0, 4)

	def setS(self, value):
		return super().setAsString(0, 4, value)

	def setS(self, value):
		return super().setAsString(0, 4, value)

	def getDisplayS(self):
		return super().getAsString(0, 4)

	def getTMP(self):
		return super().getAsInt(4, 1, True, False, False)

	def setTMP(self, value, isRounded=False):
		return super().setAsInt(4, 1, value, isRounded, True, False, False)

	def getDisplayTMP(self):
		return super().getAsDisplayInt(4, 1, True, False, False)

	def getANS(self):
		return super().getAsInt(5, 1, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(5, 1, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(5, 1, False, False, False)

	def getI(self):
		return super().getAsInt(6, 1, False, False, False)

	def setI(self, value, isRounded=False):
		return super().setAsInt(6, 1, value, isRounded, False, False, False)

	def getDisplayI(self):
		return super().getAsDisplayInt(6, 1, False, False, False)

	def getSARY1(self):
		return super().getAsString(7, 4)

	def setSARY1(self, value):
		return super().setAsString(7, 4, value)

	def getDisplaySARY1(self):
		return super().getAsString(7, 4)

	def getSARY11(self,idx1):
		return super().getAsString(7+ idx1*1, 1)

	def setSARY11(self,idx1, value):
		return super().setAsString(7+ idx1*1, 1, value)

	def getDisplaySARY11(self,idx1):
		return super().getAsString(7+ idx1*1, 1)

	def getSARY(self,idx1):
		return super().getAsString(7+ idx1*1, 1)

	def setSARY(self,idx1, value):
		return super().setAsString(7+ idx1*1, 1, value)

	def setSARY(self,idx1, value):
		return super().setAsString(7+ idx1*1, 1, value)

	def getDisplaySARY(self,idx1):
		return super().getAsString(7+ idx1*1, 1)

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
		S = input()
		self.setS( S )
		self.setSARY(1 - 1,self.getS()[0:1])
		self.setSARY(2 - 1,self.getS()[1:2])
		self.setSARY(3 - 1,self.getS()[2:3])
		self.setSARY(4 - 1,self.getS()[3:4])
		self.setTMP(0)
		self.setI(1-1)
		while not (self.getI() > 4 - 1) :
			self.setI(self.getI() + 1)
			if self.getSARY(self.getI() - 1 ) == '+' :
				self.setTMP( self.getTMP()+1)
			else:
				self.setTMP( self.getTMP()-1)
		if 0 <= self.getTMP() :
			self.setANS(self.getTMP())
			print(self.getDisplayANS(), sep='')
		else:
			print(self.getDisplayTMP(), sep='')
		exit()

	def MAIN_flow(self):
		S = input()
		self.setS( S )
		self.setSARY(1 - 1,self.getS()[0:1])
		self.setSARY(2 - 1,self.getS()[1:2])
		self.setSARY(3 - 1,self.getS()[2:3])
		self.setSARY(4 - 1,self.getS()[3:4])
		self.setTMP(0)
		self.setI(1-1)
		while not (self.getI() > 4 - 1) :
			self.setI(self.getI() + 1)
			if self.getSARY(self.getI() - 1 ) == '+' :
				self.setTMP( self.getTMP()+1)
			else:
				self.setTMP( self.getTMP()-1)
		if 0 <= self.getTMP() :
			self.setANS(self.getTMP())
			print(self.getDisplayANS(), sep='')
		else:
			print(self.getDisplayTMP(), sep='')
		exit()
		exit()
converted().main()