import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(103)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getIN_A(self):
		return super().getAsInt(100, 1, False, False, False)

	def setIN_A(self, value, isRounded=False):
		return super().setAsInt(100, 1, value, isRounded, False, False, False)

	def getDisplayIN_A(self):
		return super().getAsDisplayInt(100, 1, False, False, False)

	def getIN_B(self):
		return super().getAsInt(101, 1, False, False, False)

	def setIN_B(self, value, isRounded=False):
		return super().setAsInt(101, 1, value, isRounded, False, False, False)

	def getDisplayIN_B(self):
		return super().getAsDisplayInt(101, 1, False, False, False)

	def getIN_C(self):
		return super().getAsInt(102, 1, False, False, False)

	def setIN_C(self, value, isRounded=False):
		return super().setAsInt(102, 1, value, isRounded, False, False, False)

	def getDisplayIN_C(self):
		return super().getAsDisplayInt(102, 1, False, False, False)

	def unstring(input_str, delimiter, *variables):
		parts = input_str.split(delimiter)
		result = []
		for i in range(min(len(parts), len(variables))):
			result.append(parts[i])
		result.extend([''] * (len(variables) - len(result)))
		return tuple(result)
	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_001_flow()
	def MAIN_001(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B, IN_C = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		self.setIN_C(IN_C)
		if (self.getIN_A() == self.getIN_B()) and (self.getIN_B() != self.getIN_C()) or (self.getIN_B() == self.getIN_C()) and (self.getIN_C() != self.getIN_A()) or (self.getIN_C() == self.getIN_A()) and (self.getIN_A() != self.getIN_B()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
	def MAIN_EXIT(self):
		exit()

	def MAIN_001_flow(self):
		INP = input()
		self.setINP( INP )
		IN_A, IN_B, IN_C = INP.split(' ')
		self.setIN_A(IN_A)
		self.setIN_B(IN_B)
		self.setIN_C(IN_C)
		if (self.getIN_A() == self.getIN_B()) and (self.getIN_B() != self.getIN_C()) or (self.getIN_B() == self.getIN_C()) and (self.getIN_C() != self.getIN_A()) or (self.getIN_C() == self.getIN_A()) and (self.getIN_A() != self.getIN_B()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		self.MAIN_EXIT_flow()

	def MAIN_EXIT_flow(self):
		exit()
		exit()
converted().main()