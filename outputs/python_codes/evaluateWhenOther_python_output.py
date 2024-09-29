from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getX(self):
		return super().getAsInt(0, 1)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def initialize(self):
		self.setX(15,False)
		pass
	def main(self):
		self.initialize()
		if (TRUE == self.getX() > 10):
			print("X IS GREATER THAN 10")
		elif (TRUE == self.getX() < 10):
			print("X IS LESS THAN 10")
		else:
			print("X IS EXACTLY 10")
converted().main()
