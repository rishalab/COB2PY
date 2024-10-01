from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(29)

	def getWS_NUM1(self):
		return super().getAsInt(0, 5)

	def setWS_NUM1(self, value, isRounded=False):
		return super().setAsInt(0, 5, value, isRounded)

	def getA(self):
		return super().getAsInt(5, 4)

	def setA(self, value, isRounded=False):
		return super().setAsInt(5, 4, value, isRounded)

	def getWS_STRING1(self):
		return super().getAsString(9, 10)

	def setWS_STRING1(self, value):
		return super().setAsString(9, 10, value)

	def getWS_STRING2(self):
		return super().getAsString(19, 10)

	def setWS_STRING2(self, value):
		return super().setAsString(19, 10, value)

	def initialize(self):
		self.setA(1000,False)
		pass
	def main(self):
		self.initialize()
		self.setWS_NUM1(self.getA())
		self.setWS_STRING1('HELLO')
		self.setWS_STRING2('HELLO')
		print('WS-NUM1: ', self.getWS_NUM1())
		print('WS-STRING1: ', self.getWS_STRING1())
		print('WS-STRING2: ', self.getWS_STRING2())
converted().main()
