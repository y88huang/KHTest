from util import *
class KHTestResult(object):
	def __init__(self,name, passed, total):
		self.passed = passed
		self.name = name
		self.total = total

	def printResult(self):
		print BAR
		print "			Test Result For "+self.name
		print "			Total: " + str(self.total)
		print "			Failed: " + str(self.total - self.passed)
		print BAR