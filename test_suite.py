import unittest
from my_test_run import MyTest

firstSuite = unittest.TestSuite()

firstSuite.addTest(unittest.makeSuite(MyTest))


if __name__ == "__main__":
    unittest.main()