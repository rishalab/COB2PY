from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getX(self):
		return super().getAsInt(0, 1)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def initialize(self):
		self.setX(4,False)
		pass
	def main(self):
		self.initialize()
		if (1 <= self.getX() <= 5):
			print("X IS BETWEEN 1 AND 5")
		elif (self.getX() == 6):
			print("X IS 6")
		else:
			print("X IS GREATER THAN 6")
converted().main()
