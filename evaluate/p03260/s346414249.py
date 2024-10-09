import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(20)

	def getS(self):
		return super().getAsString(0, 3)

	def setS(self, value):
		return super().setAsString(0, 3, value)

	def getDisplayS(self):
		return super().getAsString(0, 3)

	def getS_O(self,idx1):
		return super().getAsString(0+ idx1*1, 1)

	def setS_O(self,idx1, value):
		return super().setAsString(0+ idx1*1, 1, value)

	def getDisplayS_O(self,idx1):
		return super().getAsString(0+ idx1*1, 1)

	def getSA(self,idx1):
		return super().getAsString(0+ idx1*1, 1)

	def setSA(self,idx1, value):
		return super().setAsString(0+ idx1*1, 1, value)

	def setSA(self,idx1, value):
		return super().setAsString(0+ idx1*1, 1, value)

	def getDisplaySA(self,idx1):
		return super().getAsString(0+ idx1*1, 1)

	def getIDX(self):
		return super().getAsInt(3, 6, False, False, False)

	def setIDX(self, value, isRounded=False):
		return super().setAsInt(3, 6, value, isRounded, False, False, False)

	def getDisplayIDX(self):
		return super().getAsDisplayInt(3, 6, False, False, False)

	def getW_VAL(self):
		return super().getAsInt(9, 2, False, False, False)

	def setW_VAL(self, value, isRounded=False):
		return super().setAsInt(9, 2, value, isRounded, False, False, False)

	def getDisplayW_VAL(self):
		return super().getAsDisplayInt(9, 2, False, False, False)

	def getW_SHOW(self):
		return super().getAsInt(11, 2, False, False, False)

	def setW_SHOW(self, value, isRounded=False):
		return super().setAsInt(11, 2, value, isRounded, False, False, False)

	def getDisplayW_SHOW(self):
		return super().getAsDisplayInt(11, 2, False, False, False)

	def getREM(self):
		return super().getAsInt(13, 2, False, False, False)

	def setREM(self, value, isRounded=False):
		return super().setAsInt(13, 2, value, isRounded, False, False, False)

	def getDisplayREM(self):
		return super().getAsDisplayInt(13, 2, False, False, False)

	def getANS(self):
		return super().getAsString(15, 3)

	def setANS(self, value):
		return super().setAsString(15, 3, value)

	def setANS(self, value):
		return super().setAsString(15, 3, value)

	def getDisplayANS(self):
		return super().getAsString(15, 3)

	def getW_A(self):
		return super().getAsInt(18, 1, False, False, False)

	def setW_A(self, value, isRounded=False):
		return super().setAsInt(18, 1, value, isRounded, False, False, False)

	def getDisplayW_A(self):
		return super().getAsDisplayInt(18, 1, False, False, False)

	def getW_B(self):
		return super().getAsInt(19, 1, False, False, False)

	def setW_B(self, value, isRounded=False):
		return super().setAsInt(19, 1, value, isRounded, False, False, False)

	def getDisplayW_B(self):
		return super().getAsDisplayInt(19, 1, False, False, False)

	def unstring(input_str, delimiter, *variables):
		parts = input_str.split(delimiter)
		result = []
		for i in range(min(len(parts), len(variables))):
			result.append(parts[i])
		result.extend([''] * (len(variables) - len(result)))
		return tuple(result)
	def initialize(self):
		for idx1 in range(0,3):
			self.setSA(idx1," ")
		self.setIDX(0,False)
		self.setANS("No")
		pass
	def main(self):
		self.initialize()
		S = input()
		self.setS( S )
		self.setIDX(1-1)
		while not (self.getIDX() > 3 - 1) :
			self.setIDX(self.getIDX() + 1)
			self.setW_A(self.getS_O(1 - 1))
			self.setW_B(self.getS_O(3 - 1))
			self.setW_VAL( self.getW_A()*self.getW_B()*self.getIDX())
			self.setW_SHOW(self.getW_VAL() / 2)
			self.setREM(self.getW_VAL() % 2)
			if self.getREM() == 1 :
				self.setANS("Yes")
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()