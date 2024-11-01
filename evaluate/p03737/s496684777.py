import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adjust as necessary
from Program import Program

class converted(Program):

	def __init__(self):
		super().__init__(134)

	def getINP(self):
		return super().getAsString(0, 100)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def setINP(self, value):
		return super().setAsString(0, 100, value)

	def getDisplayINP(self):
		return super().getAsString(0, 100)

	def getS1(self):
		return super().getAsString(100, 10)

	def setS1(self, value):
		return super().setAsString(100, 10, value)

	def getDisplayS1(self):
		return super().getAsString(100, 10)

	def getS1A(self):
		return super().getAsString(100, 1)

	def setS1A(self, value):
		return super().setAsString(100, 1, value)

	def setS1A(self, value):
		return super().setAsString(100, 1, value)

	def getDisplayS1A(self):
		return super().getAsString(100, 1)

	def getS1B(self):
		return super().getAsString(101, 9)

	def setS1B(self, value):
		return super().setAsString(101, 9, value)

	def setS1B(self, value):
		return super().setAsString(101, 9, value)

	def getDisplayS1B(self):
		return super().getAsString(101, 9)

	def getS2(self):
		return super().getAsString(110, 10)

	def setS2(self, value):
		return super().setAsString(110, 10, value)

	def getDisplayS2(self):
		return super().getAsString(110, 10)

	def getS2A(self):
		return super().getAsString(110, 1)

	def setS2A(self, value):
		return super().setAsString(110, 1, value)

	def setS2A(self, value):
		return super().setAsString(110, 1, value)

	def getDisplayS2A(self):
		return super().getAsString(110, 1)

	def getS2B(self):
		return super().getAsString(111, 9)

	def setS2B(self, value):
		return super().setAsString(111, 9, value)

	def setS2B(self, value):
		return super().setAsString(111, 9, value)

	def getDisplayS2B(self):
		return super().getAsString(111, 9)

	def getS3(self):
		return super().getAsString(120, 10)

	def setS3(self, value):
		return super().setAsString(120, 10, value)

	def getDisplayS3(self):
		return super().getAsString(120, 10)

	def getS3A(self):
		return super().getAsString(120, 1)

	def setS3A(self, value):
		return super().setAsString(120, 1, value)

	def setS3A(self, value):
		return super().setAsString(120, 1, value)

	def getDisplayS3A(self):
		return super().getAsString(120, 1)

	def getS3B(self):
		return super().getAsString(121, 9)

	def setS3B(self, value):
		return super().setAsString(121, 9, value)

	def setS3B(self, value):
		return super().setAsString(121, 9, value)

	def getDisplayS3B(self):
		return super().getAsString(121, 9)

	def getANS(self):
		return super().getAsString(130, 3)

	def setANS(self, value):
		return super().setAsString(130, 3, value)

	def getDisplayANS(self):
		return super().getAsString(130, 3)

	def getANSX(self,idx1):
		return super().getAsString(130+ idx1*1, 1)

	def setANSX(self,idx1, value):
		return super().setAsString(130+ idx1*1, 1, value)

	def setANSX(self,idx1, value):
		return super().setAsString(130+ idx1*1, 1, value)

	def getDisplayANSX(self,idx1):
		return super().getAsString(130+ idx1*1, 1)

	def getIDX(self):
		return super().getAsInt(133, 1, False, False, False)

	def setIDX(self, value, isRounded=False):
		return super().setAsInt(133, 1, value, isRounded, False, False, False)

	def getDisplayIDX(self):
		return super().getAsDisplayInt(133, 1, False, False, False)

	def initialize(self):
		pass
	def main(self):
		self.initialize()
		INP = input()
		self.setINP( INP )
		S1, S2, S3 = INP.split(" ")
		self.setS1(S1)
		self.setS2(S2)
		self.setS3(S3)
		self.setANSX(1 - 1,self.getS1A())
		self.setANSX(2 - 1,self.getS2A())
		self.setANSX(3 - 1,self.getS3A())
		self.setIDX(1-1)
		while not (self.getIDX() > 3 - 1) :
			self.setIDX(self.getIDX() + 1)
			if (self.getANSX(self.getIDX() - 1 ) == ("a")):
				self.setANSX(self.getIDX() - 1 ,"A")
			elif (self.getANSX(self.getIDX() - 1 ) == ("b")):
				self.setANSX(self.getIDX() - 1 ,"B")
			elif (self.getANSX(self.getIDX() - 1 ) == ("c")):
				self.setANSX(self.getIDX() - 1 ,"C")
			elif (self.getANSX(self.getIDX() - 1 ) == ("d")):
				self.setANSX(self.getIDX() - 1 ,"D")
			elif (self.getANSX(self.getIDX() - 1 ) == ("e")):
				self.setANSX(self.getIDX() - 1 ,"E")
			elif (self.getANSX(self.getIDX() - 1 ) == ("f")):
				self.setANSX(self.getIDX() - 1 ,"F")
			elif (self.getANSX(self.getIDX() - 1 ) == ("g")):
				self.setANSX(self.getIDX() - 1 ,"G")
			elif (self.getANSX(self.getIDX() - 1 ) == ("h")):
				self.setANSX(self.getIDX() - 1 ,"H")
			elif (self.getANSX(self.getIDX() - 1 ) == ("i")):
				self.setANSX(self.getIDX() - 1 ,"I")
			elif (self.getANSX(self.getIDX() - 1 ) == ("j")):
				self.setANSX(self.getIDX() - 1 ,"J")
			elif (self.getANSX(self.getIDX() - 1 ) == ("k")):
				self.setANSX(self.getIDX() - 1 ,"K")
			elif (self.getANSX(self.getIDX() - 1 ) == ("l")):
				self.setANSX(self.getIDX() - 1 ,"L")
			elif (self.getANSX(self.getIDX() - 1 ) == ("m")):
				self.setANSX(self.getIDX() - 1 ,"M")
			elif (self.getANSX(self.getIDX() - 1 ) == ("n")):
				self.setANSX(self.getIDX() - 1 ,"N")
			elif (self.getANSX(self.getIDX() - 1 ) == ("o")):
				self.setANSX(self.getIDX() - 1 ,"O")
			elif (self.getANSX(self.getIDX() - 1 ) == ("p")):
				self.setANSX(self.getIDX() - 1 ,"P")
			elif (self.getANSX(self.getIDX() - 1 ) == ("q")):
				self.setANSX(self.getIDX() - 1 ,"Q")
			elif (self.getANSX(self.getIDX() - 1 ) == ("r")):
				self.setANSX(self.getIDX() - 1 ,"R")
			elif (self.getANSX(self.getIDX() - 1 ) == ("s")):
				self.setANSX(self.getIDX() - 1 ,"S")
			elif (self.getANSX(self.getIDX() - 1 ) == ("t")):
				self.setANSX(self.getIDX() - 1 ,"T")
			elif (self.getANSX(self.getIDX() - 1 ) == ("u")):
				self.setANSX(self.getIDX() - 1 ,"U")
			elif (self.getANSX(self.getIDX() - 1 ) == ("v")):
				self.setANSX(self.getIDX() - 1 ,"V")
			elif (self.getANSX(self.getIDX() - 1 ) == ("w")):
				self.setANSX(self.getIDX() - 1 ,"W")
			elif (self.getANSX(self.getIDX() - 1 ) == ("x")):
				self.setANSX(self.getIDX() - 1 ,"X")
			elif (self.getANSX(self.getIDX() - 1 ) == ("y")):
				self.setANSX(self.getIDX() - 1 ,"Y")
			elif (self.getANSX(self.getIDX() - 1 ) == ("z")):
				self.setANSX(self.getIDX() - 1 ,"Z")
			else:
				pass
		print(self.getDisplayANS(), sep='')
		exit()
		exit()
converted().main()