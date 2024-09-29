from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getX(self):
		return super().getAsInt(0, 1)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def initialize(self):
		self.setX(2,False)
		pass
	def main(self):
		self.initialize()
		if (self.getX() == 1):
			print("X IS 1")
		elif (self.getX() == 2):
			print("X IS 2")
		elif (self.getX() == 3):
			print("X IS 3")
		else:
			print("X IS SOMETHING ELSE")
converted().main()
