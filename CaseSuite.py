# a CaseSuite is a suite of cases with an option.
import util
from KHTestResult import KHTestResult

class  CaseSuite(object):
	def __init__(self, name, cases):
		self.name = name
		self.cases = cases
		self.FileName = ""
		self.SolutionName = ""

	def setFileName(self, input, soln):
		self.FileName = input
		self.SolutionName = soln

	def run(self, FileName, SolutionName, InputOption):
		total = len(self.cases)
		passed = 0
		util.separatePrint("				TESTING SUITE:"+self.name)
		for case in self.cases:
			if case.run(FileName, SolutionName,InputOption):
				passed = passed + 1
		Result = KHTestResult(self.name, passed, total)
		Result.printResult()
		separatePrint("				END OF "+self.name)
		return Result
