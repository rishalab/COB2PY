import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(58)

	def getA(self):
		return super().getAsInt(0, 4, False, False, False)

	def setA(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayA(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def getB(self):
		return super().getAsInt(4, 4, False, False, False)

	def setB(self, value, isRounded=False):
		return super().setAsInt(4, 4, value, isRounded, False, False, False)

	def getDisplayB(self):
		return super().getAsDisplayInt(4, 4, False, False, False)

	def getC(self):
		return super().getAsInt(8, 4, False, False, False)

	def setC(self, value, isRounded=False):
		return super().setAsInt(8, 4, value, isRounded, False, False, False)

	def getDisplayC(self):
		return super().getAsDisplayInt(8, 4, False, False, False)

	def getD(self):
		return super().getAsInt(12, 4, False, False, False)

	def setD(self, value, isRounded=False):
		return super().setAsInt(12, 4, value, isRounded, False, False, False)

	def getDisplayD(self):
		return super().getAsDisplayInt(12, 4, False, False, False)

	def getE(self):
		return super().getAsInt(16, 4, False, False, False)

	def setE(self, value, isRounded=False):
		return super().setAsInt(16, 4, value, isRounded, False, False, False)

	def getDisplayE(self):
		return super().getAsDisplayInt(16, 4, False, False, False)

	def getF(self):
		return super().getAsInt(20, 4, False, False, False)

	def setF(self, value, isRounded=False):
		return super().setAsInt(20, 4, value, isRounded, False, False, False)

	def getDisplayF(self):
		return super().getAsDisplayInt(20, 4, False, False, False)

	def getG(self):
		return super().getAsInt(24, 4, False, False, False)

	def setG(self, value, isRounded=False):
		return super().setAsInt(24, 4, value, isRounded, False, False, False)

	def getDisplayG(self):
		return super().getAsDisplayInt(24, 4, False, False, False)

	def getGROUP_1(self):
		return super().getAsString(28, 8)

	def setGROUP_1(self, value):
		return super().setAsString(28, 8, value)

	def getDisplayGROUP_1(self):
		return super().getAsString(28, 8)

	def getNUM1(self):
		return super().getAsString(28, 4)

	def setNUM1(self, value):
		return super().setAsString(28, 4, value)

	def getDisplayNUM1(self):
		return super().getAsString(28, 4)

	def getNUM3(self):
		return super().getAsFloat(28, 4, '99.99', False, False, False)

	def setNUM3(self, value, isRounded=False):
		return super().setAsFloat(28, 4, value, isRounded, '99.99', False, False, False)

	def getDisplayNUM3(self):
		return super().getAsDisplayFloat(28, 4, '99.99', False, False, False)

	def getNUM2(self):
		return super().getAsInt(32, 4, False, False, False)

	def setNUM2(self, value, isRounded=False):
		return super().setAsInt(32, 4, value, isRounded, False, False, False)

	def getDisplayNUM2(self):
		return super().getAsDisplayInt(32, 4, False, False, False)

	def getGROUP_2(self):
		return super().getAsString(36, 9)

	def setGROUP_2(self, value):
		return super().setAsString(36, 9, value)

	def getDisplayGROUP_2(self):
		return super().getAsString(36, 9)

	def getNUM1_1(self):
		return super().getAsString(36, 5)

	def setNUM1_1(self, value):
		return super().setAsString(36, 5, value)

	def getDisplayNUM1_1(self):
		return super().getAsString(36, 5)

	def getNUM5(self):
		return super().getAsInt(36, 5, False, False, False)

	def setNUM5(self, value, isRounded=False):
		return super().setAsInt(36, 5, value, isRounded, False, False, False)

	def getDisplayNUM5(self):
		return super().getAsDisplayInt(36, 5, False, False, False)

	def getNUM2_1(self):
		return super().getAsInt(41, 4, False, False, False)

	def setNUM2_1(self, value, isRounded=False):
		return super().setAsInt(41, 4, value, isRounded, False, False, False)

	def getDisplayNUM2_1(self):
		return super().getAsDisplayInt(41, 4, False, False, False)

	def getNUM6(self):
		return super().getAsFloat(45, 4, '99.99', False, False, False)

	def setNUM6(self, value, isRounded=False):
		return super().setAsFloat(45, 4, value, isRounded, '99.99', False, False, False)

	def getDisplayNUM6(self):
		return super().getAsDisplayFloat(45, 4, '99.99', False, False, False)

	def getNUM7(self):
		return super().getAsFloat(49, 4, '99.99', False, False, False)

	def setNUM7(self, value, isRounded=False):
		return super().setAsFloat(49, 4, value, isRounded, '99.99', False, False, False)

	def getDisplayNUM7(self):
		return super().getAsDisplayFloat(49, 4, '99.99', False, False, False)

	def getANS(self):
		return super().getAsFloat(53, 5, '999.99', False, False, False)

	def setANS(self, value, isRounded=False):
		return super().setAsFloat(53, 5, value, isRounded, '999.99', False, False, False)

	def getDisplayANS(self):
		return super().getAsDisplayFloat(53, 5, '999.99', False, False, False)

	def initialize(self):
		self.setA(10,False)
		self.setB(2000,False)
		self.setC(0,False)
		self.setD(0,False)
		self.setE(0,False)
		self.setF(0,False)
		self.setG(0,False)
		self.setNUM3(20.0,False)
		self.setNUM2(20,False)
		self.setNUM5(20,False)
		self.setNUM2_1(40,False)
		self.setNUM6(15.55,False)
		self.setNUM7(10.49,False)
		pass
	def main(self):
		self.initialize()
		print('Initial Values: A=', self.getDisplayA(), ' B=', self.getDisplayB(), ' C=', self.getDisplayC(), ' D=', self.getDisplayD(), ' E=', self.getDisplayE(), ' F=', self.getDisplayF(), sep='')
		self.setB(self.getB() * self.getA())
		print('After MULTIPLY A BY B: A=', self.getDisplayA(), ' B=', self.getDisplayB(), sep='')
		self.setA(self.getA() * 2, True)
		self.setB(self.getB() * 2)
		print('After MULTIPLY 2 BY A B: A=', self.getDisplayA(), ' B=', self.getDisplayB(), sep='')
		self.setC(3 * self.getA())
		print('After MULTIPLY 3 BY A GIVING C: C=', self.getDisplayC(), sep='')
		self.setD(4 * self.getA(), True)
		print('After MULTIPLY 4 BY A GIVING D ROUNDED: D=', self.getDisplayD(), sep='')
		self.setE(self.getA() * 2, True)
		self.setF(self.getA() * 2, True)
		print('After MULTIPLY A BY 2 GIVING E F: E=', self.getDisplayE(), ' F=', self.getDisplayF(), sep='')
		self.setNUM3(self.getNUM3() * self.getNUM5(), True)
		self.setANS(self.getNUM6() * self.getNUM7())
		self.setNUM6(self.getNUM6() * self.getNUM7(), True)
		print('NUM6: ', self.getDisplayNUM6(), sep='')
		print('NUM7: ', self.getDisplayNUM7(), sep='')
		print('Result of multiplication (rounded): ', self.getDisplayANS(), sep='')
		exit()
converted().main()
