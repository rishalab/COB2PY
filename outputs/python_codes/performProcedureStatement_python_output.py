from Program import Program


class converted(Program):

	def __init__(self):
		super().__init__(0)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		PROCEDURE_1()
		PROCEDURE_2()
		PROCEDURE_3()
	def PROCEDURE_1():
		print('This is PROCEDURE-1')
	def PROCEDURE_2():
		print('This is PROCEDURE-2')
	def PROCEDURE_3():
		print('This is PROCEDURE-3')
converted().main()
