from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(1)

	def getNUM(self):
		return super().getAsInt(0, 1)

	def setNUM(self, value, isRounded=False):
		return super().setAsInt(0, 1, value, isRounded)

	def initialize(self):
		self.setNUM(8,False)
		pass
	def main(self):
		self.initialize()
		if not self.getNUM() != 10 :
			print("NUM is not equal to 10.")
		else:
			print("NUM is equal to 10.")
converted().main()
