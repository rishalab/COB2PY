import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(16)

	def getSUM1(self):
		return super().getAsInt(0, 4, False, False, False)

	def setSUM1(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplaySUM1(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def getCOUNT1(self):
		return super().getAsInt(4, 2, False, False, False)

	def setCOUNT1(self, value, isRounded=False):
		return super().setAsInt(4, 2, value, isRounded, False, False, False)

	def getDisplayCOUNT1(self):
		return super().getAsDisplayInt(4, 2, False, False, False)

	def getTOTAL(self):
		return super().getAsInt(6, 4, False, False, False)

	def setTOTAL(self, value, isRounded=False):
		return super().setAsInt(6, 4, value, isRounded, False, False, False)

	def getDisplayTOTAL(self):
		return super().getAsDisplayInt(6, 4, False, False, False)

	def getAVERAGE(self):
		return super().getAsFloat(10, 6, '9999.99', False, False, False)

	def setAVERAGE(self, value, isRounded=False):
		return super().setAsFloat(10, 6, value, isRounded, '9999.99', False, False, False)

	def getDisplayAVERAGE(self):
		return super().getAsDisplayFloat(10, 6, '9999.99', False, False, False)

	def initialize(self):
		self.setSUM1(100,False)
		self.setCOUNT1(5,False)
		pass
	def main(self):
		self.initialize()
		exit()
	def BEGIN(self):
		self.setTOTAL( self.getSUM1()/self.getCOUNT1(), True)
		self.setAVERAGE( self.getSUM1()/self.getCOUNT1())
		print("Total: ", self.getDisplayTOTAL(), sep='')
		print("Average: ", self.getDisplayAVERAGE(), sep='')
		exit()
converted().main()
