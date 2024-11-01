import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(9)

	def getA(self):
		return super().getAsInt(0, 3, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(0, 3, False, False, False)

	def getE(self):
		return super().getAsInt(3, 3, False, False, False)

	def setE(self, value, isRounded=False):
		return super().setAsInt(3, 3, value, isRounded, False, False, False)

	def getDisplayE(self):
		return super().getAsDisplayInt(3, 3, False, False, False)

	def getK(self):
		return super().getAsInt(6, 3, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(6, 3, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(6, 3, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		A = input()
		self.setA( A )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		K = input()
		self.setK( K )
		self.setE(self.getE()-(self.getA()))
		if self.getE() <= self.getK() :
			print('Yay!', sep='')
		else:
			print(':(', sep='')
		exit()

	def MAIN_flow(self):
		A = input()
		self.setA( A )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		E = input()
		self.setE( E )
		K = input()
		self.setK( K )
		self.setE(self.getE()-(self.getA()))
		if self.getE() <= self.getK() :
			print('Yay!', sep='')
		else:
			print(':(', sep='')
		exit()
		exit()
converted().main()