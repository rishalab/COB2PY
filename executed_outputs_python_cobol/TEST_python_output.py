import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(8)

	def getI(self):
		return super().getAsInt(0, 2, False, False, False)

	def setI(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDisplayI(self):
		return super().getAsDisplayInt(0, 2, False, False, False)

	def getJ(self):
		return super().getAsInt(2, 2, False, False, False)

	def setJ(self, value, isRounded=False):
		return super().setAsInt(2, 2, value, isRounded, False, False, False)

	def getDisplayJ(self):
		return super().getAsDisplayInt(2, 2, False, False, False)

	def getK(self):
		return super().getAsInt(4, 2, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(4, 2, value, isRounded, False, False, False)

	def getDisplayK(self):
		return super().getAsDisplayInt(4, 2, False, False, False)

	def getL(self):
		return super().getAsInt(6, 2, False, False, False)

	def setL(self, value, isRounded=False):
		return super().setAsInt(6, 2, value, isRounded, False, False, False)

	def getDisplayL(self):
		return super().getAsDisplayInt(6, 2, False, False, False)

	def initialize(self):
		self.setI(0,False)
		self.setJ(0,False)
		self.setK(0,False)
		self.setL(0,False)
		pass
	def main(self):
		self.initialize()
		self.setI(1-1)
		while not (self.getI() > 10 - 1) :
			self.setI(self.getI() + 1)
			self.setJ(1-1)
			while not (self.getJ() > 5 - 1) :
				self.setJ(self.getJ() + 1)
				print('Value of I: ', self.getDisplayI(), ', Value of J: ', self.getDisplayJ(), sep='')
		self.setK(1-1)
		while not (self.getK() > 10 - 1) :
			self.setK(self.getK() + 1)
			print('Value of K: ', self.getDisplayK(), sep='')
		print('HI', sep='')
		exit()
converted().main()
