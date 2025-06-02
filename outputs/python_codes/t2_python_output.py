import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(90)

	def getNUM1(self):
		return super().getAsInt(0, 9, False, False, False)

	def setNUM1(self, value, isRounded=False):
		return super().setAsInt(0, 9, value, isRounded, False, False, False)

	def getDisplayNUM1(self):
		return super().getAsDisplayInt(0, 9, False, False, False)

	def getNUM2(self):
		return super().getAsInt(9, 9, False, False, False)

	def setNUM2(self, value, isRounded=False):
		return super().setAsInt(9, 9, value, isRounded, False, False, False)

	def getDisplayNUM2(self):
		return super().getAsDisplayInt(9, 9, False, False, False)

	def getNUMA(self):
		return super().getAsInt(18, 9, False, False, False)

	def setNUMA(self, value, isRounded=False):
		return super().setAsInt(18, 9, value, isRounded, False, False, False)

	def getDisplayNUMA(self):
		return super().getAsDisplayInt(18, 9, False, False, False)

	def getNUMB(self):
		return super().getAsInt(27, 9, False, False, False)

	def setNUMB(self, value, isRounded=False):
		return super().setAsInt(27, 9, value, isRounded, False, False, False)

	def getDisplayNUMB(self):
		return super().getAsDisplayInt(27, 9, False, False, False)

	def getNUMC(self):
		return super().getAsInt(36, 9, False, False, False)

	def setNUMC(self, value, isRounded=False):
		return super().setAsInt(36, 9, value, isRounded, False, False, False)

	def getDisplayNUMC(self):
		return super().getAsDisplayInt(36, 9, False, False, False)

	def getRES_DIV(self):
		return super().getAsInt(45, 9, False, False, False)

	def setRES_DIV(self, value, isRounded=False):
		return super().setAsInt(45, 9, value, isRounded, False, False, False)

	def getDisplayRES_DIV(self):
		return super().getAsDisplayInt(45, 9, False, False, False)

	def getRES_MULT(self):
		return super().getAsInt(54, 9, False, False, False)

	def setRES_MULT(self, value, isRounded=False):
		return super().setAsInt(54, 9, value, isRounded, False, False, False)

	def getDisplayRES_MULT(self):
		return super().getAsDisplayInt(54, 9, False, False, False)

	def getRES_SUB(self):
		return super().getAsInt(63, 9, False, False, False)

	def setRES_SUB(self, value, isRounded=False):
		return super().setAsInt(63, 9, value, isRounded, False, False, False)

	def getDisplayRES_SUB(self):
		return super().getAsDisplayInt(63, 9, False, False, False)

	def getRES_ADD(self):
		return super().getAsInt(72, 9, False, False, False)

	def setRES_ADD(self, value, isRounded=False):
		return super().setAsInt(72, 9, value, isRounded, False, False, False)

	def getDisplayRES_ADD(self):
		return super().getAsDisplayInt(72, 9, False, False, False)

	def getRES_MOV(self):
		return super().getAsString(81, 9)

	def setRES_MOV(self, value):
		return super().setAsString(81, 9, value)

	def setRES_MOV(self, value):
		return super().setAsString(81, 9, value)

	def getDisplayRES_MOV(self):
		return super().getAsString(81, 9)

	def initialize(self):
		self.setNUM1(10,False)
		self.setNUM2(10,False)
		self.setNUMA(100,False)
		self.setNUMB(15,False)
		pass
	def main(self):
		self.initialize()
		self.setNUMC( (self.getNUM1()*self.getNUM2()))
		self.setRES_DIV(self.getNUMA() / self.getNUMB())
		self.setRES_MULT(self.getNUMA() * self.getNUMB())
		self.setRES_SUB(self.getNUMB()-(self.getNUMA()))
		self.setRES_ADD(self.getNUMA()+self.getNUMB())
		self.setRES_MOV(self.getNUMA())
		self.setNUM1(0)
		self.setNUM2(0)
		print("NUMC:", self.getDisplayNUMC(), sep='')
		print("RES-DIV:", self.getDisplayRES_DIV(), sep='')
		print("RES-MULT:", self.getDisplayRES_MULT(), sep='')
		print("RES-SUB:", self.getDisplayRES_SUB(), sep='')
		print("RES-ADD:", self.getDisplayRES_ADD(), sep='')
		print("RES-MOV:", self.getDisplayRES_MOV(), sep='')
		print("REINITIALIZED NUM1: ", self.getDisplayNUM1(), sep='')
		print("REINITIALIZED NUM2: ", self.getDisplayNUM2(), sep='')
		exit()
		exit()
converted().main()