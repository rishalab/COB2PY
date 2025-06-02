import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(120)

	def getWS_CNT1(self):
		return super().getAsInt(0, 2, False, False, False)

	def setWS_CNT1(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDisplayWS_CNT1(self):
		return super().getAsDisplayInt(0, 2, False, False, False)

	def getWS_CNT2(self):
		return super().getAsInt(2, 2, False, False, False)

	def setWS_CNT2(self, value, isRounded=False):
		return super().setAsInt(2, 2, value, isRounded, False, False, False)

	def getDisplayWS_CNT2(self):
		return super().getAsDisplayInt(2, 2, False, False, False)

	def getWS_STRING(self):
		return super().getAsString(4, 25)

	def setWS_STRING(self, value):
		return super().setAsString(4, 25, value)

	def setWS_STRING(self, value):
		return super().setAsString(4, 25, value)

	def getDisplayWS_STRING(self):
		return super().getAsString(4, 25)

	def getWS_STRING_DEST(self):
		return super().getAsString(29, 30)

	def setWS_STRING_DEST(self, value):
		return super().setAsString(29, 30, value)

	def setWS_STRING_DEST(self, value):
		return super().setAsString(29, 30, value)

	def getDisplayWS_STRING_DEST(self):
		return super().getAsString(29, 30)

	def getWS_STR1(self):
		return super().getAsString(59, 15)

	def setWS_STR1(self, value):
		return super().setAsString(59, 15, value)

	def setWS_STR1(self, value):
		return super().setAsString(59, 15, value)

	def getDisplayWS_STR1(self):
		return super().getAsString(59, 15)

	def getWS_STR2(self):
		return super().getAsString(74, 7)

	def setWS_STR2(self, value):
		return super().setAsString(74, 7, value)

	def setWS_STR2(self, value):
		return super().setAsString(74, 7, value)

	def getDisplayWS_STR2(self):
		return super().getAsString(74, 7)

	def getWS_STR3(self):
		return super().getAsString(81, 7)

	def setWS_STR3(self, value):
		return super().setAsString(81, 7, value)

	def setWS_STR3(self, value):
		return super().setAsString(81, 7, value)

	def getDisplayWS_STR3(self):
		return super().getAsString(81, 7)

	def getWS_COUNT(self):
		return super().getAsInt(88, 2, False, False, False)

	def setWS_COUNT(self, value, isRounded=False):
		return super().setAsInt(88, 2, value, isRounded, False, False, False)

	def getDisplayWS_COUNT(self):
		return super().getAsDisplayInt(88, 2, False, False, False)

	def getWS_UNSTR(self):
		return super().getAsString(90, 30)

	def setWS_UNSTR(self, value):
		return super().setAsString(90, 30, value)

	def setWS_UNSTR(self, value):
		return super().setAsString(90, 30, value)

	def getDisplayWS_UNSTR(self):
		return super().getAsString(90, 30)

	def initialize(self):
		self.setWS_CNT1(0,False)
		self.setWS_CNT2(0,False)
		self.setWS_STRING('ABCDADADADABVDFDFFAF')
		self.setWS_STR1('TUTORIALSPOINT')
		self.setWS_STR2('WELCOME')
		self.setWS_STR3('TO AND')
		self.setWS_COUNT(1,False)
		self.setWS_UNSTR('WELCOME TO TUTORIALSPOINT')
		pass
	def main(self):
		self.initialize()
			print("WS-CNT1 : ", self.getDisplayWS_CNT1(), sep='')
			print("WS-CNT2 : ", self.getDisplayWS_CNT2(), sep='')
			print("OLD STRING : ", self.getDisplayWS_STRING(), sep='')
			print("NEW STRING : ", self.getDisplayWS_STRING(), sep='')
			print('OVERFLOW!', sep='')
			print('WS-STRING : ', self.getDisplayWS_STRING_DEST(), sep='')
			print('WS-COUNT : ', self.getDisplayWS_COUNT(), sep='')
			print('WS-STR1 : ', self.getDisplayWS_STR1(), sep='')
			print('WS-STR2 : ', self.getDisplayWS_STR2(), sep='')
			print('WS-STR3 : ', self.getDisplayWS_STR3(), sep='')
			exit()
		exit()
converted().main()