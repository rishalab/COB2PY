import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(40)

	def getNAME(self):
		return super().getAsString(0, 30)

	def setNAME(self, value):
		return super().setAsString(0, 30, value)

	def getDisplayNAME(self):
		return super().getAsString(0, 30)

	def getUNITS(self):
		return super().getAsInt(30, 4, False, False, False)

	def setUNITS(self, value, isRounded=False):
		return super().setAsInt(30, 4, value, isRounded, False, False, False)

	def getDisplayUNITS(self):
		return super().getAsDisplayInt(30, 4, False, False, False)

	def getBILL(self):
		return super().getAsInt(34, 6, False, False, False)

	def setBILL(self, value, isRounded=False):
		return super().setAsInt(34, 6, value, isRounded, False, False, False)

	def getDisplayBILL(self):
		return super().getAsDisplayInt(34, 6, False, False, False)

	def initialize(self):
		return
	def main(self):
		self.initialize()
		print("Customer Name: ", sep='')
		NAME = input()
		self.setNAME( NAME )
		print("Units Consumed: ", sep='')
		UNITS = input()
		self.setUNITS( UNITS )
		if self.getUNITS() <= 100 :
			self.setBILL( self.getUNITS()*5)
		else:
			if self.getUNITS() <= 200 :
				self.setBILL( 100*5+(self.getUNITS()-100)*7)
			else:
				self.setBILL( 100*5+100*7+(self.getUNITS()-200)*10)
		print("-----------------------------", sep='')
		print("Customer: ", self.getDisplayNAME(), sep='')
		print("Units:    ", self.getDisplayUNITS(), sep='')
		print("Bill:     Rs", self.getDisplayBILL(), sep='')
		print("-----------------------------", sep='')
		exit()
		exit()
converted().main()