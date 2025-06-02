import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(69)

	def getFIRST_VAR(self):
		return super().getAsFloat(0, 5, '999.99', True, False, False)

	def setFIRST_VAR(self, value, isRounded=False):
		return super().setAsFloat(0, 5, value, isRounded, '999.99', True, False, False)

	def getDisplayFIRST_VAR(self):
		return super().getAsDisplayFloat(0, 5, '999.99', True, False, False)

	def getSECOND_VAR(self):
		return super().getAsFloat(5, 5, '999.99', True, False, False)

	def setSECOND_VAR(self, value, isRounded=False):
		return super().setAsFloat(5, 5, value, isRounded, '999.99', True, False, False)

	def getDisplaySECOND_VAR(self):
		return super().getAsDisplayFloat(5, 5, '999.99', True, False, False)

	def getTHIRD_VAR(self):
		return super().getAsString(10, 6)

	def setTHIRD_VAR(self, value):
		return super().setAsString(10, 6, value)

	def setTHIRD_VAR(self, value):
		return super().setAsString(10, 6, value)

	def getDisplayTHIRD_VAR(self):
		return super().getAsString(10, 6)

	def getFOURTH_VAR(self):
		return super().getAsString(16, 5)

	def setFOURTH_VAR(self, value):
		return super().setAsString(16, 5, value)

	def setFOURTH_VAR(self, value):
		return super().setAsString(16, 5, value)

	def getDisplayFOURTH_VAR(self):
		return super().getAsString(16, 5)

	def getGROUP_VAR(self):
		return super().getAsString(21, 48)

	def setGROUP_VAR(self, value):
		return super().setAsString(21, 48, value)

	def getDisplayGROUP_VAR(self):
		return super().getAsString(21, 48)

	def getSUBVAR_1(self):
		return super().getAsInt(21, 3, False, False, False)

	def setSUBVAR_1(self, value, isRounded=False):
		return super().setAsInt(21, 3, value, isRounded, False, False, False)

	def getDisplaySUBVAR_1(self):
		return super().getAsDisplayInt(21, 3, False, False, False)

	def getSUBVAR_2(self):
		return super().getAsString(24, 15)

	def setSUBVAR_2(self, value):
		return super().setAsString(24, 15, value)

	def setSUBVAR_2(self, value):
		return super().setAsString(24, 15, value)

	def getDisplaySUBVAR_2(self):
		return super().getAsString(24, 15)

	def getSUBVAR_3(self):
		return super().getAsString(39, 15)

	def setSUBVAR_3(self, value):
		return super().setAsString(39, 15, value)

	def setSUBVAR_3(self, value):
		return super().setAsString(39, 15, value)

	def getDisplaySUBVAR_3(self):
		return super().getAsString(39, 15)

	def getSUBVAR_4(self):
		return super().getAsString(54, 15)

	def setSUBVAR_4(self, value):
		return super().setAsString(54, 15, value)

	def setSUBVAR_4(self, value):
		return super().setAsString(54, 15, value)

	def getDisplaySUBVAR_4(self):
		return super().getAsString(54, 15)

	def initialize(self):
		self.setSECOND_VAR(-123.45,False)
		self.setTHIRD_VAR('ABCDEF')
		self.setFOURTH_VAR('A121$')
		self.setSUBVAR_1(337,False)
		self.setSUBVAR_2('LALALALA')
		self.setSUBVAR_3('LALALA')
		self.setSUBVAR_4('LALALA')
		pass
	def main(self):
		self.initialize()
		print("1ST VAR :", self.getDisplayFIRST_VAR(), sep='')
		print("2ND VAR :", self.getDisplaySECOND_VAR(), sep='')
		print("3RD VAR :", self.getDisplayTHIRD_VAR(), sep='')
		print("4TH VAR :", self.getDisplayFOURTH_VAR(), sep='')
		print("GROUP VAR :", self.getDisplayGROUP_VAR(), sep='')
		exit()
		exit()
converted().main()