from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(0)

	def getCONDITION(self):
		return super().getAsString(0, 0)

	def setCONDITION(self, value):
		return super().setAsString(0, 0, value)

	def initialize(self):
		self.setCONDITION('T')
		pass
	def main(self):
		self.initialize()
		if (self.getCONDITION() == 'T'):
			print("CONDITION IS TRUE")
		elif (self.getCONDITION() == 'F'):
			print("CONDITION IS FALSE")
converted().main()
