from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(3)

	def getMY_NUMBER(self):
		val = super().getAsInt(0, 3)
		def getIS_LOW_RANGE(self):
			val = super().getAsInt(0, 3)
			return True if ((val>=0 and val<=49) or (val>=51 and val<=55) or (val==42) or (val==89) ) else False
		def getIS_MID_RANGE(self):
			val = super().getAsInt(0, 3)
			return True if ((val>=50 and val<=79) ) else False
		def getIS_HIGH_RANGE(self):
			val = super().getAsInt(0, 3)
			return True if ((val>=80 and val<=100) ) else False
		def getIS_MULTIPLE_OF_5(self):
			val = super().getAsInt(0, 3)
			return True if ((val==5) or (val==10) or (val==15) or (val==20) or (val==25) or (val==30) or (val==35) or (val==40) or (val==45) or (val==50) or (val==55) or (val==60) or (val==65) or (val==70) or (val==75) or (val==80) or (val==85) or (val==90) or (val==95) or (val==100) ) else False
		return val

	def setMY_NUMBER(self, value, isRounded=False):
		return super().setAsInt(0, 3, value, isRounded)

	def initialize(self):
		self.setMY_NUMBER(0,False)
		pass
	def main(self):
		self.initialize()
		def MAIN_PARA(self):
			print("Enter a number (0-100): ")
			self.setMY_NUMBER(1+self.getMY_NUMBER())
			my-number = input()
converted().main()
