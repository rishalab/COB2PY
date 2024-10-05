from Program import Program
import os

class converted(Program):

	def __init__(self):
		super().__init__(8)

	def getI(self):
		return super().getAsInt(0, 2, False, False, False)

	def setI(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDispalyI(self):
		return super().getAsString(0, 2)

	def setDispalyI(self, value):
		return super().setAsString(0, 2, value)

	def getJ(self):
		return super().getAsInt(2, 2, False, False, False)

	def setJ(self, value, isRounded=False):
		return super().setAsInt(2, 2, value, isRounded, False, False, False)

	def getDispalyJ(self):
		return super().getAsString(2, 2)

	def setDispalyJ(self, value):
		return super().setAsString(2, 2, value)

	def getK(self):
		return super().getAsInt(4, 2, False, False, False)

	def setK(self, value, isRounded=False):
		return super().setAsInt(4, 2, value, isRounded, False, False, False)

	def getDispalyK(self):
		return super().getAsString(4, 2)

	def setDispalyK(self, value):
		return super().setAsString(4, 2, value)

	def getL(self):
		return super().getAsInt(6, 2, False, False, False)

	def setL(self, value, isRounded=False):
		return super().setAsInt(6, 2, value, isRounded, False, False, False)

	def getDispalyL(self):
		return super().getAsString(6, 2)

	def setDispalyL(self, value):
		return super().setAsString(6, 2, value)

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
				print('Value of I: ', self.getI(), ', Value of J: ', self.getJ())
		self.setK(1-1)
		while not (self.getK() > 10 - 1) :
			self.setK(self.getK() + 1)
			print('Value of K: ', self.getK())
		print('HI')
		exit()
converted().main()
