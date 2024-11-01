import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(2)

	def getNUM(self):
		return super().getAsInt(0, 2, False, False, False)

	def setNUM(self, value, isRounded=False):
		return super().setAsInt(0, 2, value, isRounded, False, False, False)

	def getDisplayNUM(self):
		return super().getAsDisplayInt(0, 2, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.MAIN_flow()
	def MAIN(self):
		NUM = input()
		self.setNUM( NUM )
		if self.getNUM() == 25 :
			print("Christmas", sep='')
		else:
			if self.getNUM() == 24 :
				print("Christmas Eve", sep='')
			else:
				if self.getNUM() == 23 :
					print("Christmas Eve Eve", sep='')
				else:
					if self.getNUM() == 22 :
						print("Christmas Eve Eve Eve", sep='')
		exit()

	def MAIN_flow(self):
		NUM = input()
		self.setNUM( NUM )
		if self.getNUM() == 25 :
			print("Christmas", sep='')
		else:
			if self.getNUM() == 24 :
				print("Christmas Eve", sep='')
			else:
				if self.getNUM() == 23 :
					print("Christmas Eve Eve", sep='')
				else:
					if self.getNUM() == 22 :
						print("Christmas Eve Eve Eve", sep='')
		exit()
		exit()
converted().main()