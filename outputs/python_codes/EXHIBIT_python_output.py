from Program import Program
import os

class converted(Program):

	def __init__(self):
		super().__init__(22)

	def getGROUP_1(self):
		return super().getAsString(0, 20)

	def setGROUP_1(self, value):
		return super().setAsString(0, 20, value)

	def getDispalyGROUP_1(self):
		return super().getAsString(0, 20)

	def setDispalyGROUP_1(self, value):
		return super().setAsString(0, 20, value)

	def getMYNAME(self):
		return super().getAsString(0, 20)

	def setMYNAME(self, value):
		return super().setAsString(0, 20, value)

	def getDispalyMYNAME(self):
		return super().getAsString(0, 20)

	def setDispalyMYNAME(self, value):
		return super().setAsString(0, 20, value)

	def getAGE(self):
		return super().getAsInt(20, 2, False, False, False)

	def setAGE(self, value, isRounded=False):
		return super().setAsInt(20, 2, value, isRounded, False, False, False)

	def getDispalyAGE(self):
		return super().getAsString(20, 2)

	def setDispalyAGE(self, value):
		return super().setAsString(20, 2, value)

	def initialize(self):
		self.setMYNAME('Alice')
		self.setAGE(30,False)
		pass
	def main(self):
		self.initialize()
		print('MYNAME in GROUP_1',' = ', self.getMYNAME(),end='		')
		print(1,end='	')
		exit()
converted().main()
