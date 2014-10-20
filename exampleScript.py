#!/usr/bin/env python
import KHTest
import sys
import random
from KHTest.CaseSuite import CaseSuite
from KHTest.TestCase import TestCase
from KHTest.KHTester import KHTester

TYPE = sys.argv[1]

INPUT = "./buffer"
SOLN = "./bufferBUSY_64" if TYPE == "busy" else "./bufferNOBUSY_64"

MAKE = "make buffer KIND="+ ("BUSY" if TYPE == "busy" else "NOBUSY")

ZeroSuite = CaseSuite("ZeroSuite",[TestCase("Zeros","0 0 0 0 0",["-s"]), TestCase("1 Zero","0",["-s"]), 
									TestCase("TWO","2 5 4",["-s"])])

def standardRandomTest(Num):
	CASE = [];
	for i in range(0,Num):
		rd = random.randint(0,5)
		tp = []
		for j in range(0,rd):
			option = random.randint(1,100)
			tp.append(str(option))
		tmpCase = TestCase(str(i),"",tp)
		CASE.append(tmpCase)
	suite = CaseSuite("StandardSuite",CASE)
	return suite

StandardSuite = standardRandomTest(100);

TEST_MODULE = KHTester(MAKE,INPUT, SOLN)
TEST_MODULE.addTestSuite(StandardSuite)
TEST_MODULE.start()