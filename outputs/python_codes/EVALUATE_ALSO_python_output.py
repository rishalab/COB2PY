from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(2)

	def getX(self):
		return super().getAsInt(0, 1)

	def setX(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def getY(self):
		return super().getAsInt(1, 1)

	def setY(self, value, isRounded=False):
		return super().setAsInt(1, 1, value, isRounded)

	def initialize(self):
		self.setX(1,False)
		self.setY(2,False)
		pass
	def main(self):
		self.initialize()
		if (self.getX() == 1 and self.getY() == 2):
			print("X IS 1 AND Y IS 2")
		elif (self.getX() == 3 and self.getY() == 4):
			print("X IS 3 AND Y IS 4")
		else:
			print("COMBINATION DOES NOT MATCH")
converted().main()
