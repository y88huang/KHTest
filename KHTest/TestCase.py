from util import *
import os
#define test class.
class TestCase(object):
# test case class.
	def __init__(self, name, input, option = '', error=False):
		self.name = name
		self.input = input
		self.error = error #if output to stderr.
		self.FileName = ""
		self.SolutionName = ""
		self.option = option

	def run(self,FileName, SolutionName, InputOption):
		test = map(str,self.option)
		Option = ' '.join(test)
		print BAR
		print "Test Case: " + self.name + "  Option " + Option +"\n Input: "+self.input
		commands = generateTestSuite(FileName, SolutionName,Option, self.input,InputOption, self.error);
		runCommands(commands)
		isPassed = False
		print SINGLE_BAR
		if os.stat("diffFile").st_size == 0:
			print "PASSED!"
			isPassed = True
		else:
			print "Failed!"
			print ""
			print "TEST INPUT:"
			print self.input
			print "TEST OUTPUT:"
			isPassed = False
			runCommands(["cat diffFile"])
			runCommands(["cat diffFile>"+self.name+".diff"])
		print BAR
		# clean up tmpfiles.
		cleanFiles();
		return isPassed
