import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(29)

	def getLN(self):
		return super().getAsString(0, 13)

	def setLN(self, value):
		return super().setAsString(0, 13, value)

	def setLN(self, value):
		return super().setAsString(0, 13, value)

	def getDisplayLN(self):
		return super().getAsString(0, 13)

	def getN(self):
		return super().getAsInt(13, 10, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(13, 10, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(13, 10, False, False, False)

	def getK(self):
		return super().getAsInt(23, 2, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(23, 2, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(23, 2, False, False, False)

	def getCNT(self):
		return super().getAsInt(25, 2, False, False, False)

	def setCNT(self, value, isRounded=False):
		return super().setAsInt(25, 2, value, isRounded, False, False, False)

	def getDisplayCNT(self):
		return super().getAsDisplayInt(25, 2, False, False, False)

	def getANS(self):
		return super().getAsString(27, 2)

	def setANS(self, value):
		return super().setAsString(27, 2, value)

	def setANS(self, value):
		return super().setAsString(27, 2, value)

	def getDisplayANS(self):
		return super().getAsString(27, 2)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		LN = input()
		self.setLN( LN )
		N, K = LN.split(' ')
		self.setN(N)
		self.setK(K)
		self.setCNT(1)
		while not ( self.getN() < self.getK() ** self.getCNT()):
			self.setCNT(1+self.getCNT())
		self.setANS(self.getCNT())
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()