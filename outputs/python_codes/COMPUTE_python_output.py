from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(16)

	def getSUM1(self):
		return super().getAsInt(0, 4)

	def setSUM1(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded)

	def getCOUNT1(self):
		return super().getAsInt(4, 2)

	def setCOUNT1(self, value, isRounded=False):
		return super().setAsInt(4, 2, value, isRounded)

	def getTOTAL(self):
		return super().getAsInt(6, 4)

	def setTOTAL(self, value, isRounded=False):
		return super().setAsInt(6, 4, value, isRounded)

	def getAVERAGE(self):
		return super().getAsFloat(10, 6)

	def setAVERAGE(self, value, isRounded=False):
		return super().setAsFloat(10, 6, value, isRounded, '9999.99')

	def initialize(self):
		self.setSUM1(100,False)
		self.setCOUNT1(5,False)
		pass
	def main(self):
		self.initialize()
		def BEGIN(self):
			self.setTOTAL( self.getSUM1()/self.getCOUNT1(), True)
			self.setAVERAGE( self.getSUM1()/self.getCOUNT1())
			print("Total: ", self.getTOTAL())
			print("Average: ", self.getAVERAGE())
converted().main()
