import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(121)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getIN_A(self):
		return super().getAsInt(100, 3, False, False, False)

	def setIN_A(self, value, isRounded=False):
		return super().setAsInt(100, 3, value, isRounded, False, False, False)

	def getDisplayIN_A(self):
		return super().getAsDisplayInt(100, 3, False, False, False)

	def getIN_B(self):
		return super().getAsInt(103, 3, False, False, False)

	def setIN_B(self, value, isRounded=False):
		return super().setAsInt(103, 3, value, isRounded, False, False, False)

	def getDisplayIN_B(self):
		return super().getAsDisplayInt(103, 3, False, False, False)

	def getIN_C(self):
		return super().getAsInt(106, 3, False, False, False)

	def setIN_C(self, value, isRounded=False):
		return super().setAsInt(106, 3, value, isRounded, False, False, False)

	def getDisplayIN_C(self):
		return super().getAsDisplayInt(106, 3, False, False, False)

	def getIN_D(self):
		return super().getAsInt(109, 3, False, False, False)

	def setIN_D(self, value, isRounded=False):
		return super().setAsInt(109, 3, value, isRounded, False, False, False)

	def getDisplayIN_D(self):
		return super().getAsDisplayInt(109, 3, False, False, False)

	def getAB(self):
		return super().getAsInt(112, 3, False, False, False)

	def setAB(self, value, isRounded=False):
		return super().setAsInt(112, 3, value, isRounded, False, False, False)

	def getDisplayAB(self):
		return super().getAsDisplayInt(112, 3, False, False, False)

	def getBC(self):
		return super().getAsInt(115, 3, False, False, False)

	def setBC(self, value, isRounded=False):
		return super().setAsInt(115, 3, value, isRounded, False, False, False)

	def getDisplayBC(self):
		return super().getAsDisplayInt(115, 3, False, False, False)

	def getAC(self):
		return super().getAsInt(118, 3, False, False, False)

	def setAC(self, value, isRounded=False):
		return super().setAsInt(118, 3, value, isRounded, False, False, False)

	def getDisplayAC(self):
		return super().getAsDisplayInt(118, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B, IN_C, IN_D = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		self.setIN_C(IN_C)
		self.setIN_D(IN_D)
		self.setAB( self.getIN_A()-self.getIN_B())
		self.setBC( self.getIN_B()-self.getIN_C())
		self.setAC( self.getIN_A()-self.getIN_C())
		if (self.getAC() <= self.getIN_D()) or (self.getAB() <= self.getIN_D() and self.getBC() <= self.getIN_D()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B, IN_C, IN_D = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		self.setIN_C(IN_C)
		self.setIN_D(IN_D)
		self.setAB( self.getIN_A()-self.getIN_B())
		self.setBC( self.getIN_B()-self.getIN_C())
		self.setAC( self.getIN_A()-self.getIN_C())
		if (self.getAC() <= self.getIN_D()) or (self.getAB() <= self.getIN_D() and self.getBC() <= self.getIN_D()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()