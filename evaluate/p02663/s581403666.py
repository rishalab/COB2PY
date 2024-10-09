import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(120)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getH1(self):
		return super().getAsInt(100, 2, False, False, False)

	def setH1(self, value, isRounded=False):
		return super().setAsInt(100, 2, value, isRounded, False, False, False)

	def getDisplayH1(self):
		return super().getAsDisplayInt(100, 2, False, False, False)

	def getM1(self):
		return super().getAsInt(102, 2, False, False, False)

	def setM1(self, value, isRounded=False):
		return super().setAsInt(102, 2, value, isRounded, False, False, False)

	def getDisplayM1(self):
		return super().getAsDisplayInt(102, 2, False, False, False)

	def getH2(self):
		return super().getAsInt(104, 2, False, False, False)

	def setH2(self, value, isRounded=False):
		return super().setAsInt(104, 2, value, isRounded, False, False, False)

	def getDisplayH2(self):
		return super().getAsDisplayInt(104, 2, False, False, False)

	def getM2(self):
		return super().getAsInt(106, 2, False, False, False)

	def setM2(self, value, isRounded=False):
		return super().setAsInt(106, 2, value, isRounded, False, False, False)

	def getDisplayM2(self):
		return super().getAsDisplayInt(106, 2, False, False, False)

	def getK(self):
		return super().getAsInt(108, 4, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(108, 4, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(108, 4, False, False, False)

	def getW(self):
		return super().getAsInt(112, 4, False, False, False)

	def setW(self, value, isRounded=False):
		return super().setAsInt(112, 4, value, isRounded, False, False, False)

	def getDisplayW(self):
		return super().getAsDisplayInt(112, 4, False, False, False)

	def getOUT(self):
		return super().getAsString(116, 4)

	def setOUT(self, value):
		return super().setAsString(116, 4, value)

	def setOUT(self, value):
		return super().setAsString(116, 4, value)

	def getDisplayOUT(self):
		return super().getAsString(116, 4)

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
		H1, M1, H2, M2, K = INP.split(' ')
		self.setH1(H1)
		self.setM1(M1)
		self.setH2(H2)
		self.setM2(M2)
		self.setK(K)
		self.setW( self.getH2()*60+self.getM2()-(self.getH1()*60+self.getM1()))
		self.setOUT( self.getW()-self.getK())
		print(self.getDisplayOUT(), sep='')
		exit()
		exit()
converted().main()