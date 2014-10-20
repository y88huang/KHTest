from util import *
#The master class.
class KHTester(object):
	def __init__(self, make, soln, input):
		self.suites = []
		self.make = make
		self.FileName = input
		self.SolutionName = soln
		self.inputOption = 0 #from commandLine , 1 from file.
	def start(self,InputOption=0):
		util.separatePrint("					COMPILING")
		util.runCommands(["make clean"])
		util.runCommands(["clear","rm *.diff"]);
		util.makeFile(self.make)
		util.separatePrint("					COMPILE SUCCEED")
		for suite in self.suites:
			suite.run(self.FileName, self.SolutionName,InputOption)
	def addTestSuite(self, suite):
		self.suites.append(suite)
