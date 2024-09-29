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
		self.setX(4,False)
		self.setY(6,False)
		pass
	def main(self):
		self.initialize()
		if (self.getX()+self.getY() == 10):
			print("THE SUM OF X AND Y IS 10")
		elif (self.getX()+self.getY() == 20):
			print("THE SUM OF X AND Y IS 20")
		else:
			print("THE SUM IS NEITHER 10 NOR 20")
converted().main()
