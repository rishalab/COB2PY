from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(29)

	def getNUM_DECIMAL(self):
		return super().getAsString(0, 29)

	def setNUM_DECIMAL(self, value):
		return super().setAsString(0, 29, value)

	def getDispalyNUM_DECIMAL(self):
		return super().getAsString(0, 29)

	def setDispalyNUM_DECIMAL(self, value):
		return super().setAsString(0, 29, value)

	def getWS_DECIMAL1(self):
		val = super().getAsFloat(0, 8, '99999.99', True, True, True)
		def getSTATE56(self):
			val = super().getAsFloat(0, 8, '99999.99', True, True, True)
			return True if ((val==+5) ) else False
		return val

	def setWS_DECIMAL1(self, value, isRounded=False):
		return super().setAsFloat(0, 8, value, isRounded, '99999.99', True, True, True)

	def getDispalyWS_DECIMAL1(self):
		return super().getAsString(0, 8)

	def setDispalyWS_DECIMAL1(self, value):
		return super().setAsString(0, 8, value)

	def getWS_DECIMAL2(self):
		return super().getAsFloat(8, 7, '99999.99', True, False, False)

	def setWS_DECIMAL2(self, value, isRounded=False):
		return super().setAsFloat(8, 7, value, isRounded, '99999.99', True, False, False)

	def getDispalyWS_DECIMAL2(self):
		return super().getAsString(8, 7)

	def setDispalyWS_DECIMAL2(self, value):
		return super().setAsString(8, 7, value)

	def getWS_DECIMAL3(self):
		return super().getAsFloat(15, 7, '99999.99', True, False, False)

	def setWS_DECIMAL3(self, value, isRounded=False):
		return super().setAsFloat(15, 7, value, isRounded, '99999.99', True, False, False)

	def getDispalyWS_DECIMAL3(self):
		return super().getAsString(15, 7)

	def setDispalyWS_DECIMAL3(self, value):
		return super().setAsString(15, 7, value)

	def getWS_DECIMAL4(self):
		return super().getAsFloat(22, 7, '99999.99', True, False, True)

	def setWS_DECIMAL4(self, value, isRounded=False):
		return super().setAsFloat(22, 7, value, isRounded, '99999.99', True, False, True)

	def getDispalyWS_DECIMAL4(self):
		return super().getAsString(22, 7)

	def setDispalyWS_DECIMAL4(self, value):
		return super().setAsString(22, 7, value)

	def initialize(self):
		self.setWS_DECIMAL1(-1234.56,False)
		self.setWS_DECIMAL2(-1234.56,False)
		self.setWS_DECIMAL3(-1234.56,False)
		self.setWS_DECIMAL4(-1234.56,False)
		pass
	def main(self):
		self.initialize()
		print("Leading Separate Character: ", self.getWS_DECIMAL1())
		print("No Sign Specified: ", self.getWS_DECIMAL2())
		print("Trailing Embedded Sign: ", self.getWS_DECIMAL3())
		print("Leading Embedded Sign: ", self.getWS_DECIMAL4())
		print("NUM group: ", self.getNUM_DECIMAL())
		exit()
converted().main()
