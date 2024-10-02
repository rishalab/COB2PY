from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(21)

	def getNUM(self):
		return super().getAsString(0, 21)

	def setNUM(self, value):
		return super().setAsString(0, 21, value)

	def getDispalyNUM(self):
		return super().getAsString(0, 21)

	def setDispalyNUM(self, value):
		return super().setAsString(0, 21, value)

	def getWS_NUMBER1(self):
		val = super().getAsInt(0, 6, True, True, True)
		def getSTATE56(self):
			val = super().getAsInt(0, 6, True, True, True)
			return True if ((val==+5) ) else False
		return val

	def setWS_NUMBER1(self, value, isRounded=False):
		return super().setAsInt(0, 6, value, isRounded, True, True, True)

	def getDispalyWS_NUMBER1(self):
		return super().getAsString(0, 6)

	def setDispalyWS_NUMBER1(self, value):
		return super().setAsString(0, 6, value)

	def getWS_NUMBER2(self):
		return super().getAsInt(6, 5, True, False, False)

	def setWS_NUMBER2(self, value, isRounded=False):
		return super().setAsInt(6, 5, value, isRounded, True, False, False)

	def getDispalyWS_NUMBER2(self):
		return super().getAsString(6, 5)

	def setDispalyWS_NUMBER2(self, value):
		return super().setAsString(6, 5, value)

	def getWS_NUMBER3(self):
		return super().getAsInt(11, 5, True, False, False)

	def setWS_NUMBER3(self, value, isRounded=False):
		return super().setAsInt(11, 5, value, isRounded, True, False, False)

	def getDispalyWS_NUMBER3(self):
		return super().getAsString(11, 5)

	def setDispalyWS_NUMBER3(self, value):
		return super().setAsString(11, 5, value)

	def getWS_NUMBER4(self):
		return super().getAsInt(16, 5, True, False, True)

	def setWS_NUMBER4(self, value, isRounded=False):
		return super().setAsInt(16, 5, value, isRounded, True, False, True)

	def getDispalyWS_NUMBER4(self):
		return super().getAsString(16, 5)

	def setDispalyWS_NUMBER4(self, value):
		return super().setAsString(16, 5, value)

	def initialize(self):
		self.setWS_NUMBER1(-12345,False)
		self.setWS_NUMBER2(-12345,False)
		self.setWS_NUMBER3(-12345,False)
		self.setWS_NUMBER4(-12345,False)
		pass
	def main(self):
		self.initialize()
		print("Trailing Separate Character: ", self.getWS_NUMBER1())
		print("No Sign Specified: ", self.getWS_NUMBER2())
		print("Trailing Embedded Sign: ", self.getWS_NUMBER3())
		print("Leading Embedded Sign: ", self.getWS_NUMBER4())
		print("NUM group: ", self.getNUM())
converted().main()
