from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(0)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		self.PROCEDURE_1()
		self.PROCEDURE_2()
		self.PROCEDURE_3()
	def PROCEDURE_1(self):
		print('This is PROCEDURE-1')
	def PROCEDURE_2(self):
		print('This is PROCEDURE-2')
	def PROCEDURE_3(self):
		print('This is PROCEDURE-3')
converted().main()
