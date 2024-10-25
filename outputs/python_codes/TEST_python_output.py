import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(4)

	def getCHOICE(self):
		return super().getAsInt(0, 4, False, False, False)

	def setCHOICE(self, value, isRounded=False):
		return super().setAsInt(0, 4, value, isRounded, False, False, False)

	def getDisplayCHOICE(self):
		return super().getAsDisplayInt(0, 4, False, False, False)

	def unstring(input_str, delimiter, *variables):
		parts = input_str.split(delimiter)
		result = []
		for i in range(min(len(parts), len(variables))):
			result.append(parts[i])
		result.extend([''] * (len(variables) - len(result)))
		return tuple(result)
	def initialize(self):
		self.setCHOICE(10,False)
		pass
	def main(self):
		self.initialize()
		self.MAIN_PROCEDURE_flow()
	def MAIN_PROCEDURE(self):
		self.setCHOICE(2)
		if self.getCHOICE() == 1:
			self.INIT_PROC_flow()
		if self.getCHOICE() == 2:
			self.MAIN_PROC_flow()
		if self.getCHOICE() == 3:
			self.END_PROC_flow()
	def INIT_PROC(self):
		print("In INIT-PROC.", sep='')
	def MAIN_PROC(self):
		print("In MAIN-PROC.", sep='')
		self.INIT_PROC_flow()
		exit()
	def END_PROC(self):
		print("In END-PROC.", sep='')
		exit()

	def MAIN_PROCEDURE_flow(self):
		self.setCHOICE(2)
		if self.getCHOICE() == 1:
			self.INIT_PROC_flow()
		if self.getCHOICE() == 2:
			self.MAIN_PROC_flow()
		if self.getCHOICE() == 3:
			self.END_PROC_flow()
		self.INIT_PROC_flow()

	def INIT_PROC_flow(self):
		print("In INIT-PROC.", sep='')
		self.MAIN_PROC_flow()

	def MAIN_PROC_flow(self):
		print("In MAIN-PROC.", sep='')
		self.INIT_PROC_flow()
		exit()
		self.END_PROC_flow()

	def END_PROC_flow(self):
		print("In END-PROC.", sep='')
		exit()
		exit()
converted().main()