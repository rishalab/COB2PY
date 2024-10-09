import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(19)

	def getINP(self):
		return super().getAsString(0, 10)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def setINP(self, value):
		return super().setAsString(0, 10, value)

	def getDisplayINP(self):
		return super().getAsString(0, 10)

	def getX(self):
		return super().getAsInt(10, 3, False, False, False)

	def setX(self, value, isRounded=False):
		return super().setAsInt(10, 3, value, isRounded, False, False, False)

	def getDisplayX(self):
		return super().getAsDisplayInt(10, 3, False, False, False)

	def getY(self):
		return super().getAsInt(13, 3, False, False, False)

	def setY(self, value, isRounded=False):
		return super().setAsInt(13, 3, value, isRounded, False, False, False)

	def getDisplayY(self):
		return super().getAsDisplayInt(13, 3, False, False, False)

	def getI(self):
		return super().getAsInt(16, 3, False, False, False)

	def setI(self, value, isRounded=False):
		return super().setAsInt(16, 3, value, isRounded, False, False, False)

	def getDisplayI(self):
		return super().getAsDisplayInt(16, 3, False, False, False)

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
		INP = input()
		self.setINP( INP )
		X, Y = INP.split(' ')
		self.setX(X)
		self.setY(Y)
		self.setI(1-1)
		while not (self.getI() > self.getX() or self.getI()*2+(self.getX()-self.getI())*4 == self.getY() or self.getI()*4+(self.getX()-self.getI())*2 == self.getY() - 1) :
			self.setI(self.getI() + 1)
		if (self.getI() <= self.getX()) :
			print('Yes', sep='')
		else:
			print('No', sep='')
		exit()
		exit()
converted().main()