import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(157)

	def getRECORD_AREA2(self):
		return super().getAsString(0, 110)

	def setRECORD_AREA2(self, value):
		return super().setAsString(0, 110, value)

	def getDisplayRECORD_AREA2(self):
		return super().getAsString(0, 110)

	def getEMP_NAME(self):
		return super().getAsString(0, 20)

	def setEMP_NAME(self, value):
		return super().setAsString(0, 20, value)

	def setEMP_NAME(self, value):
		return super().setAsString(0, 20, value)

	def getDisplayEMP_NAME(self):
		return super().getAsString(0, 20)

	def getEMP_DATA(self):
		return super().getAsString(20, 90)

	def setEMP_DATA(self, value):
		return super().setAsString(20, 90, value)

	def getDisplayEMP_DATA(self):
		return super().getAsString(20, 90)

	def getEMP_ID(self):
		return super().getAsInt(20, 5, False, False, False)

	def setEMP_ID(self, value, isRounded=False):
		return super().setAsInt(20, 5, value, isRounded, False, False, False)

	def getDisplayEMP_ID(self):
		return super().getAsDisplayInt(20, 5, False, False, False)

	def getEMP_SALARY(self):
		return super().getAsFloat(25, 7, '99999.99', False, False, False)

	def setEMP_SALARY(self, value, isRounded=False):
		return super().setAsFloat(25, 7, value, isRounded, '99999.99', False, False, False)

	def getDisplayEMP_SALARY(self):
		return super().getAsDisplayFloat(25, 7, '99999.99', False, False, False)

	def getEMP_GENDER(self):
		return super().getAsString(32, 1)

	def setEMP_GENDER(self, value):
		return super().setAsString(32, 1, value)

	def setEMP_GENDER(self, value):
		return super().setAsString(32, 1, value)

	def getDisplayEMP_GENDER(self):
		return super().getAsString(32, 1)

	def getEMP_ADDRESS(self,idx1):
		return super().getAsString(33+ idx1*7, 7)

	def setEMP_ADDRESS(self,idx1, value):
		return super().setAsString(33+ idx1*7, 7, value)

	def getDisplayEMP_ADDRESS(self,idx1):
		return super().getAsString(33+ idx1*7, 7)

	def getEMP_AGE(self,idx1):
		return super().getAsInt(33+ idx1*7, 2, False, False, False)

	def setEMP_AGE(self,idx1, value, isRounded=False):
		return super().setAsInt(33+ idx1*7, 2, value, isRounded, False, False, False)

	def getDisplayEMP_AGE(self,idx1):
		return super().getAsDisplayInt(33+ idx1*7, 2, False, False, False)

	def getEMP_CHILD(self,idx1):
		return super().getAsInt(35+ idx1*7, 5, False, False, False)

	def setEMP_CHILD(self,idx1, value, isRounded=False):
		return super().setAsInt(35+ idx1*7, 5, value, isRounded, False, False, False)

	def getDisplayEMP_CHILD(self,idx1):
		return super().getAsDisplayInt(35+ idx1*7, 5, False, False, False)

	def getEMP_ADDRESS2(self):
		return super().getAsString(103, 7)

	def setEMP_ADDRESS2(self, value):
		return super().setAsString(103, 7, value)

	def getDisplayEMP_ADDRESS2(self):
		return super().getAsString(103, 7)

	def getEMP_AGE_1(self):
		return super().getAsInt(103, 2, False, False, False)

	def setEMP_AGE_1(self, value, isRounded=False):
		return super().setAsInt(103, 2, value, isRounded, False, False, False)

	def getDisplayEMP_AGE_1(self):
		return super().getAsDisplayInt(103, 2, False, False, False)

	def getEMP_CHILD_1(self):
		return super().getAsInt(105, 5, False, False, False)

	def setEMP_CHILD_1(self, value, isRounded=False):
		return super().setAsInt(105, 5, value, isRounded, False, False, False)

	def getDisplayEMP_CHILD_1(self):
		return super().getAsDisplayInt(105, 5, False, False, False)

	def getRECORD_AREA3(self):
		return super().getAsString(110, 47)

	def setRECORD_AREA3(self, value):
		return super().setAsString(110, 47, value)

	def getDisplayRECORD_AREA3(self):
		return super().getAsString(110, 47)

	def getEMP_NAME_1(self):
		return super().getAsString(110, 20)

	def setEMP_NAME_1(self, value):
		return super().setAsString(110, 20, value)

	def setEMP_NAME_1(self, value):
		return super().setAsString(110, 20, value)

	def getDisplayEMP_NAME_1(self):
		return super().getAsString(110, 20)

	def getEMP_DATA_1(self):
		return super().getAsString(130, 27)

	def setEMP_DATA_1(self, value):
		return super().setAsString(130, 27, value)

	def getDisplayEMP_DATA_1(self):
		return super().getAsString(130, 27)

	def getEMP_ID_1(self):
		return super().getAsInt(130, 5, False, False, False)

	def setEMP_ID_1(self, value, isRounded=False):
		return super().setAsInt(130, 5, value, isRounded, False, False, False)

	def getDisplayEMP_ID_1(self):
		return super().getAsDisplayInt(130, 5, False, False, False)

	def getEMP_SALARY_1(self):
		return super().getAsFloat(135, 7, '99999.99', False, False, False)

	def setEMP_SALARY_1(self, value, isRounded=False):
		return super().setAsFloat(135, 7, value, isRounded, '99999.99', False, False, False)

	def getDisplayEMP_SALARY_1(self):
		return super().getAsDisplayFloat(135, 7, '99999.99', False, False, False)

	def getEMP_GENDER_1(self):
		return super().getAsString(142, 1)

	def setEMP_GENDER_1(self, value):
		return super().setAsString(142, 1, value)

	def setEMP_GENDER_1(self, value):
		return super().setAsString(142, 1, value)

	def getDisplayEMP_GENDER_1(self):
		return super().getAsString(142, 1)

	def getEMP_ADDRESS_1(self):
		return super().getAsString(143, 7)

	def setEMP_ADDRESS_1(self, value):
		return super().setAsString(143, 7, value)

	def getDisplayEMP_ADDRESS_1(self):
		return super().getAsString(143, 7)

	def getEMP_AGE_2(self):
		return super().getAsInt(143, 2, False, False, False)

	def setEMP_AGE_2(self, value, isRounded=False):
		return super().setAsInt(143, 2, value, isRounded, False, False, False)

	def getDisplayEMP_AGE_2(self):
		return super().getAsDisplayInt(143, 2, False, False, False)

	def getEMP_CHILD_2(self):
		return super().getAsInt(145, 5, False, False, False)

	def setEMP_CHILD_2(self, value, isRounded=False):
		return super().setAsInt(145, 5, value, isRounded, False, False, False)

	def getDisplayEMP_CHILD_2(self):
		return super().getAsDisplayInt(145, 5, False, False, False)

	def getEMP_ADDRESS2_1(self):
		return super().getAsString(150, 7)

	def setEMP_ADDRESS2_1(self, value):
		return super().setAsString(150, 7, value)

	def getDisplayEMP_ADDRESS2_1(self):
		return super().getAsString(150, 7)

	def getEMP_AGE_3(self):
		return super().getAsInt(150, 2, False, False, False)

	def setEMP_AGE_3(self, value, isRounded=False):
		return super().setAsInt(150, 2, value, isRounded, False, False, False)

	def getDisplayEMP_AGE_3(self):
		return super().getAsDisplayInt(150, 2, False, False, False)

	def getEMP_CHILD_3(self):
		return super().getAsInt(152, 5, False, False, False)

	def setEMP_CHILD_3(self, value, isRounded=False):
		return super().setAsInt(152, 5, value, isRounded, False, False, False)

	def getDisplayEMP_CHILD_3(self):
		return super().getAsDisplayInt(152, 5, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.setEMP_NAME('JOHN SMITH          ')
		self.setEMP_ID_1('00001')
		self.setEMP_SALARY(5000)
		self.setEMP_GENDER('M')
		print("Employee Name: ", self.getDisplayEMP_NAME(), sep='')
		print("Employee ID: ", self.getDisplayEMP_ID(), sep='')
		print("Employee Salary: ", self.getDisplayEMP_SALARY(), sep='')
		print("Employee Gender: ", self.getDisplayEMP_GENDER(), sep='')
		print(self.getDisplayEMP_AGE_1(), sep='')
		exit()
converted().main()
