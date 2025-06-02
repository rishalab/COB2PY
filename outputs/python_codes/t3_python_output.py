import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(50)

	def getNUM1(self):
		return super().getAsInt(0, 9, False, False, False)

	def setNUM1(self, value, isRounded=False):
		return super().setAsInt(0, 9, value, isRounded, False, False, False)

	def getDisplayNUM1(self):
		return super().getAsDisplayInt(0, 9, False, False, False)

	def getNUM2(self):
		return super().getAsInt(9, 9, False, False, False)

	def setNUM2(self, value, isRounded=False):
		return super().setAsInt(9, 9, value, isRounded, False, False, False)

	def getDisplayNUM2(self):
		return super().getAsDisplayInt(9, 9, False, False, False)

	def getNUM3(self):
		return super().getAsInt(18, 5, False, False, False)

	def setNUM3(self, value, isRounded=False):
		return super().setAsInt(18, 5, value, isRounded, False, False, False)

	def getDisplayNUM3(self):
		return super().getAsDisplayInt(18, 5, False, False, False)

	def getNUM4(self):
		return super().getAsInt(23, 6, False, False, False)

	def setNUM4(self, value, isRounded=False):
		return super().setAsInt(23, 6, value, isRounded, False, False, False)

	def getDisplayNUM4(self):
		return super().getAsDisplayInt(23, 6, False, False, False)

	def getNEG_NUM(self):
		return super().getAsInt(29, 9, True, False, False)

	def setNEG_NUM(self, value, isRounded=False):
		return super().setAsInt(29, 9, value, isRounded, True, False, False)

	def getDisplayNEG_NUM(self):
		return super().getAsDisplayInt(29, 9, True, False, False)

	def getCLASS1(self):
		return super().getAsString(38, 9)

	def setCLASS1(self, value):
		return super().setAsString(38, 9, value)

	def getDisplayCLASS1(self):
		return super().getAsString(38, 9)

	def getCHECK_VAL(self):
		return super().getAsInt(47, 3, False, False, False)

	def getPASS(self):
		val = self.getCHECK_VAL()
		return True if ((val >= 41 and val <= 100) ) else False

	def getFAIL(self):
		val = self.getCHECK_VAL()
		return True if ((val >= 0 and val <= 40) ) else False

	def setCHECK_VAL(self, value, isRounded=False):
		return super().setAsInt(47, 3, value, isRounded, False, False, False)

	def getDisplayCHECK_VAL(self):
		return super().getAsDisplayInt(47, 3, False, False, False)

	def initialize(self):
		self.setNEG_NUM(-1234,False)
		self.setCLASS1('ABCD ')
		return
	def main(self):
		self.initialize()
		self.setNUM1(25)
		self.setNUM3(25)
		self.setNUM2(15)
		self.setNUM4(15)
		if self.getNUM1() > self.getNUM2() :
			print('IN LOOP 1 - IF BLOCK', sep='')
			if self.getNUM3() == self.getNUM4() :
				print('IN LOOP 2 - IF BLOCK', sep='')
			else:
				print('IN LOOP 2 - ELSE BLOCK', sep='')
		else:
			print('IN LOOP 1 -ELSE BLOCK', sep='')
		self.setCHECK_VAL(65)
		if self.getPASS() :
			print('PASSED WITH ', self.getDisplayCHECK_VAL(), ' MARKS.', sep='')
		if self.getFAIL() :
			print('FAILED WITH ', self.getDisplayCHECK_VAL(), ' MARKS.', sep='')
		if (True == (self.getNUM1() < 2)):
			print('NUM1 LESS THAN 2', sep='')
		elif (True == (self.getNUM1() < 19)):
			print('NUM1 LESS THAN 19', sep='')
		elif (True == (self.getNUM1() < 1000)):
			print('NUM1 LESS THAN 1000', sep='')
		exit()
		exit()
converted().main()