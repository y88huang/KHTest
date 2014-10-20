import sys
import subprocess


STARS = "******************************************************************************************************"
BAR = "======================================================================================================"
SINGLE_BAR = "--------------------------------------------------------------------------------------------------"
EOF = "END OF COMMAND"

TMP_clenaup = ["rm CODE_OUTPUT", "rm SOLN_OUTPUT", "rm diffFile", "rm *.khtest"];

# MakeFile.
def separatePrint(content, star = True):
	if star:
		print STARS
		print content
		print STARS
	else:
		print BAR
		print content
		print BAR

def makeFile(makeCommand):
	ret = subprocess.call(makeCommand, shell = True)
	if ret != 0:
		print STARS
		print "CANNOT COMPILE, End of Test!"
		print STARS
		sys.exit(1)
# run an array of commands in sequence.
def runCommands(Commands):
	for cmd in Commands:
		ret = subprocess.call(cmd, shell = True)

def generateTestSuite(Code, Solution, Option, Input, InputOption, Error):
	if InputOption == 1:
		with open('TEST_INPUT.khtest', 'w') as afile: afile.write(Input)
		Input = 'TEST_INPUT.khtest'
	if Error == True:
		File1 = Code + " " + Option + " " + Input + " 2> CODE_OUTPUT"
		File2 = Solution + " "+ Option + " " + Input + " 2> SOLN_OUTPUT"
		DIFF = "diff CODE_OUTPUT SOLN_OUTPUT > diffFile"
	else :
		File1 = Code + " " + Option + " " + Input + "> CODE_OUTPUT"
		File2 = Solution + " "+ Option + " " + Input + "> SOLN_OUTPUT"
		DIFF = "diff CODE_OUTPUT SOLN_OUTPUT > diffFile"
	return [File1, File2, DIFF]

#clean up all the tmpFiles.
def cleanFiles():
	runCommands(TMP_clenaup)
