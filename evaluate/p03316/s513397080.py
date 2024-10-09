import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(152)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getN(self):
		return super().getAsInt(100, 10, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(100, 10, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(100, 10, False, False, False)

	def getS(self):
		return super().getAsString(110, 10)

	def setS(self, value):
		return super().setAsString(110, 10, value)

	def getDisplayS(self):
		return super().getAsString(110, 10)

	def getWK_S(self,idx1):
		return super().getAsInt(110+ idx1*1, 1, False, False, False)

	def setWK_S(self,idx1, value, isRounded=False):
		return super().setAsInt(110+ idx1*1, 1, value, isRounded, False, False, False)

	def getDisplayWK_S(self,idx1):
		return super().getAsDisplayInt(110+ idx1*1, 1, False, False, False)

	def getIDX(self):
		return super().getAsInt(120, 2, False, False, False)

	def setIDX(self, value, isRounded=False):
		return super().setAsInt(120, 2, value, isRounded, False, False, False)

	def getDisplayIDX(self):
		return super().getAsDisplayInt(120, 2, False, False, False)

	def getANS(self):
		return super().getAsInt(122, 10, False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsInt(122, 10, value, isRounded, False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayInt(122, 10, False, False, False)

	def getSHO(self):
		return super().getAsInt(132, 10, False, False, False)

	def setSHO(self, value, isRounded=False):
		return super().setAsInt(132, 10, value, isRounded, False, False, False)

	def getDisplaySHO(self):
		return super().getAsDisplayInt(132, 10, False, False, False)

	def getAMA(self):
		return super().getAsInt(142, 10, False, False, False)

	def setAMA(self, value, isRounded=False):
		return super().setAsInt(142, 10, value, isRounded, False, False, False)

	def getDisplayAMA(self):
		return super().getAsDisplayInt(142, 10, False, False, False)

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
		INP = input()
		self.setINP( INP )
		self.setN(self.getINP())
		self.setS(self.getINP())
		self.setIDX(1)
		while not ( (self.getIDX() == 10) or (self.getWK_S(self.getIDX() - 1 ) == " ")):
			self.setANS(self.getWK_S(self.getIDX() - 1 )+self.getANS())
			self.setIDX(1+self.getIDX())
		self.setSHO(self.getN() / self.getANS())
		self.setAMA(self.getN() % self.getANS())
		if self.getAMA() == 0 :
			print("Yes", sep='')
		else:
			print("No", sep='')
		exit()
		exit()
converted().main()