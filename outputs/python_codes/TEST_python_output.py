from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getMY_NUMBER(self):
		return super().getAsInt(0, 3)

	def setMY_NUMBER(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded)

	def initialize(self):
		self.setMY_NUMBER(0,False)
		pass
	def main(self):
		self.initialize()
		def MAIN_PARA(self):
			print("Enter a number (0-100): ")
			my-number = input()
converted().main()
