from Program import Program
import os

class converted(Program):

	def __init__(self):
		super().__init__(2)

	def getA(self):
		return super().getAsInt(0, 2, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDispalyA(self):
		return super().getAsString(0, 2)

	def setDispalyA(self, value):
		return super().setAsString(0, 2, value)

	def initialize(self):
		self.setA(0,False)
		pass
	def main(self):
		self.initialize()
		print('This is an inline PERFORM statement')
		self.setA(5)
		print('Value of A after MOVE: ', self.getA())
		self.setA(1+self.getA())
		print('Value of A after ADD: ', self.getA())
	exit()
converted().main()
