from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(2)

	def getA(self):
		return super().getAsInt(0, 2)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded)

	def initialize(self):
		self.setA(0,False)
		pass
	def main(self):
		self.initialize()
		while not ( A>10):
			print('Value of A: ', self.getA())
			self.setA(self.getA() * 2)
		print('HI')
converted().main()
