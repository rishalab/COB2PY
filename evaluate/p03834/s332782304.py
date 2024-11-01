import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(41)

	def getINP(self):
		return super().getAsString(0, 20)

	def setINP(self, value):
		return super().setAsString(0, 20, value)

	def setINP(self, value):
		return super().setAsString(0, 20, value)

	def getDisplayINP(self):
		return super().getAsString(0, 20)

	def getS(self):
		return super().getAsString(20, 19)

	def setS(self, value):
		return super().setAsString(20, 19, value)

	def getDisplayS(self):
		return super().getAsString(20, 19)

	def getWK_S(self,idx1):
		return super().getAsString(20+ idx1*1, 1)

	def setWK_S(self,idx1, value):
		return super().setAsString(20+ idx1*1, 1, value)

	def setWK_S(self,idx1, value):
		return super().setAsString(20+ idx1*1, 1, value)

	def getDisplayWK_S(self,idx1):
		return super().getAsString(20+ idx1*1, 1)

	def getIDX(self):
		return super().getAsInt(39, 2, False, False, False)

	def setIDX(self, value, isRounded=False):
		return super().setAsInt(39, 2, value, isRounded, False, False, False)

	def getDisplayIDX(self):
		return super().getAsDisplayInt(39, 2, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		self.setS(self.getINP())
		self.setIDX(1-1)
		while not (self.getIDX() > 19 - 1) :
			self.setIDX(self.getIDX() + 1)
			if self.getWK_S(self.getIDX() - 1 ) == "," :
				self.setWK_S(self.getIDX() - 1 ," ")
			else:
				pass
		print(self.getDisplayS(), sep='')
		exit()
		exit()
converted().main()