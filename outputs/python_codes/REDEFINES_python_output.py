from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(58)

	def getEMPLOYEE_RECORD(self):
		return super().getAsString(0, 58)

	def setEMPLOYEE_RECORD(self, value):
		return super().setAsString(0, 58, value)

	def getEMPLOYEE_NAME(self):
		return super().getAsString(0, 30)

	def setEMPLOYEE_NAME(self, value):
		return super().setAsString(0, 30, value)

	def getEMPLOYEE_NUMBER(self):
		return super().getAsString(30, 10)

	def setEMPLOYEE_NUMBER(self, value):
		return super().setAsString(30, 10, value)

	def getSALARY(self):
		return super().getAsFloat(40, 10, '99999999.99')

	def setSALARY(self, value, isRounded=False):
		return super().setAsFloat(40, 10, value, isRounded, '99999999.99')

	def getDATE_HIRED(self):
		return super().getAsString(50, 8)

	def setDATE_HIRED(self, value):
		return super().setAsString(50, 8, value)

	def getYEAR_HIRED(self):
		return super().getAsInt(50, 4)

	def setYEAR_HIRED(self, value, isRounded=False):
		return super().setAsInt(50, 4, value, isRounded)

	def getMONTH_HIRED(self):
		return super().getAsInt(54, 2)

	def setMONTH_HIRED(self, value, isRounded=False):
		return super().setAsInt(54, 2, value, isRounded)

	def getDAY_HIRED(self):
		return super().getAsInt(56, 2)

	def setDAY_HIRED(self, value, isRounded=False):
		return super().setAsInt(56, 2, value, isRounded)

	def getEMPLOYEE_NUMBER_DETAILS(self):
		return super().getAsString(0, 58)

	def setEMPLOYEE_NUMBER_DETAILS(self, value):
		return super().setAsString(0, 58, value)

	def getEMPLOYEE_NAME_DUMMY(self):
		return super().getAsString(0, 30)

	def setEMPLOYEE_NAME_DUMMY(self, value):
		return super().setAsString(0, 30, value)

	def getEMP_NUMBER_FIELDS(self):
		return super().getAsString(30, 10)

	def setEMP_NUMBER_FIELDS(self, value):
		return super().setAsString(30, 10, value)

	def getDEPARTMENT_CODE(self):
		return super().getAsString(30, 4)

	def setDEPARTMENT_CODE(self, value):
		return super().setAsString(30, 4, value)

	def getEMPLOYEE_ID(self):
		return super().getAsString(34, 6)

	def setEMPLOYEE_ID(self, value):
		return super().setAsString(34, 6, value)

	def getSALARY_DUMMY(self):
		return super().getAsFloat(40, 10, '99999999.99')

	def setSALARY_DUMMY(self, value, isRounded=False):
		return super().setAsFloat(40, 10, value, isRounded, '99999999.99')

	def getDATE_HIRED_DUMMY(self):
		return super().getAsString(50, 8)

	def setDATE_HIRED_DUMMY(self, value):
		return super().setAsString(50, 8, value)

	def getYEAR_DUMMY(self):
		return super().getAsInt(50, 4)

	def setYEAR_DUMMY(self, value, isRounded=False):
		return super().setAsInt(50, 4, value, isRounded)

	def getMONTH_DUMMY(self):
		return super().getAsInt(54, 2)

	def setMONTH_DUMMY(self, value, isRounded=False):
		return super().setAsInt(54, 2, value, isRounded)

	def getDAY_DUMMY(self):
		return super().getAsInt(56, 2)

	def setDAY_DUMMY(self, value, isRounded=False):
		return super().setAsInt(56, 2, value, isRounded)

	def getRAW_EMPLOYEE_DATA(self):
		return super().getAsString(0, 50)

	def setRAW_EMPLOYEE_DATA(self, value):
		return super().setAsString(0, 50, value)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		def BEGIN():
			print("Employee Name: ", self.getEMPLOYEE_NAME())
			print("Employee Number: ", self.getEMPLOYEE_NUMBER())
			print("Department Code: ", self.getDEPARTMENT_CODE())
			print("Employee ID: ", self.getEMPLOYEE_ID())
			print("Year Hired: ", self.getYEAR_HIRED())
			print("Salary: ", self.getSALARY())
			print("Raw Employee Data: ", self.getRAW_EMPLOYEE_DATA())
converted().main()
