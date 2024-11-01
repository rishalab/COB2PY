import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(43)

	def getMAX_SM(self):
		return super().getAsInt(0, 2, False, False, False)

	def setMAX_SM(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDisplayMAX_SM(self):
		return super().getAsDisplayInt(0, 2, False, False, False)

	def getN(self):
		return super().getAsInt(2, 6, False, False, False)

	def setN(self, value, isRounded=False):
		return super().setAsInt(2, 6, value, isRounded, False, False, False)

	def getDisplayN(self):
		return super().getAsDisplayInt(2, 6, False, False, False)

	def getHALF(self):
		return super().getAsInt(8, 5, False, False, False)

	def setHALF(self, value, isRounded=False):
		return super().setAsInt(8, 5, value, isRounded, False, False, False)

	def getDisplayHALF(self):
		return super().getAsDisplayInt(8, 5, False, False, False)

	def getI(self):
		return super().getAsInt(13, 5, False, False, False)

	def setI(self, value, isRounded=False):
		return super().setAsInt(13, 5, value, isRounded, False, False, False)

	def getDisplayI(self):
		return super().getAsDisplayInt(13, 5, False, False, False)

	def getA(self):
		return super().getAsInt(18, 6, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(18, 6, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(18, 6, False, False, False)

	def getB(self):
		return super().getAsInt(24, 6, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(24, 6, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(24, 6, False, False, False)

	def getASM(self):
		return super().getAsInt(30, 2, False, False, False)

	def setASM(self, value, isRounded=False):
		return super().setAsInt(30, 2, value, isRounded, False, False, False)

	def getDisplayASM(self):
		return super().getAsDisplayInt(30, 2, False, False, False)

	def getBSM(self):
		return super().getAsInt(32, 2, False, False, False)

	def setBSM(self, value, isRounded=False):
		return super().setAsInt(32, 2, value, isRounded, False, False, False)

	def getDisplayBSM(self):
		return super().getAsDisplayInt(32, 2, False, False, False)

	def getSM(self):
		return super().getAsInt(34, 2, False, False, False)

	def setSM(self, value, isRounded=False):
		return super().setAsInt(34, 2, value, isRounded, False, False, False)

	def getDisplaySM(self):
		return super().getAsDisplayInt(34, 2, False, False, False)

	def getR(self):
		return super().getAsInt(36, 1, False, False, False)

	def setR(self, value, isRounded=False):
		return super().setAsInt(36, 1, value, isRounded, False, False, False)

	def getDisplayR(self):
		return super().getAsDisplayInt(36, 1, False, False, False)

	def getANS(self):
		return super().getAsString(37, 2)

	def setANS(self, value):
		return super().setAsString(37, 2, value)

	def setANS(self, value):
		return super().setAsString(37, 2, value)

	def getDisplayANS(self):
		return super().getAsString(37, 2)

	def getZS(self):
		return super().getAsString(39, 3)

	def setZS(self, value):
		return super().setAsString(39, 3, value)

	def setZS(self, value):
		return super().setAsString(39, 3, value)

	def getDisplayZS(self):
		return super().getAsString(39, 3)

	def getDUMMY(self):
		return super().getAsString(42, 1)

	def setDUMMY(self, value):
		return super().setAsString(42, 1, value)

	def setDUMMY(self, value):
		return super().setAsString(42, 1, value)

	def getDisplayDUMMY(self):
		return super().getAsString(42, 1)

	def initialize(self):
		self.setMAX_SM(99,False)
		pass
	def main(self):
		self.initialize()
		N = input()
		self.setN( N )
		self.setHALF(self.getN() / 2)
		self.setSM(self.getMAX_SM())
		self.setI(1-1)
		while not (self.getHALF() < self.getI() - 1) :
			self.setI(self.getI() + 1)
			self.setA(self.getI())
			self.setB(self.getN()-(self.getI()))
			self.setASM(0)
			self.setBSM(0)
			while not ( self.getA() <= 0):
				self.setA(self.getA() / 10)
				self.setR(self.getA() % 10)
				self.setASM(self.getR()+self.getASM())
			while not ( self.getB() <= 0):
				self.setB(self.getB() / 10)
				self.setR(self.getB() % 10)
				self.setBSM(self.getR()+self.getBSM())
			self.setBSM(self.getASM()+self.getBSM())
			if self.getBSM() < self.getSM() :
				self.setSM(self.getBSM())
		self.setZS(self.getSM())
		print(self.getDisplayZS(), sep='')
		exit()
		self.UNANS_flow()
	def UNANS(self):
		DUMMY, ANS = ZS.split(' ')
		self.setDUMMY(DUMMY)
		self.setANS(ANS)

	def UNANS_flow(self):
		DUMMY, ANS = ZS.split(' ')
		self.setDUMMY(DUMMY)
		self.setANS(ANS)
		exit()
converted().main()