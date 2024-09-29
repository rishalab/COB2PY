from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getX(self):
		return super().getAsInt(0, 1)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def initialize(self):
		self.setX(3,False)
		pass
	def main(self):
		self.initialize()
		if (self.getX() != 5):
			print("X IS NOT 5")
		elif (self.getX() == 5):
			print("X IS 5")
		else:
			print("X IS SOMETHING ELSE")
converted().main()
