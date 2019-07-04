import unittest
from noname_company import *


class MyTest(unittest.TestCase):

#    def setUP(self):
#        self.worker1 = Developer("Steve", "Wozniak2", 1000 , 3)
#        self.designer1 = Designer("Dan", "Moris1", 1100, 5, 0.9)
#        self.manager1 = Manager("Virktor", "Piatochkin1", 800, 3)

    def test_dev_salary(self):
        self.assertEqual(self.worker1.show_finance(), 1200)

    def test_designer_salary(self):
        self.assertEqual(self.designer1.show_finance(), 1638)

    def test_manager_salary(self):
        self.assertEqual(self.manager1.show_finance(), 1000)

    @classmethod
    def setUpClass(cls):
        cls.worker1 = Developer("Steve", "Wozniak2", 1000 , 3)
        cls.designer1 = Designer("Dan", "Moris1", 1100, 6, 0.9)
        cls.manager1 = Manager("Virktor", "Piatochkin1", 800, 3)
        print("before tests")



if __name__ == "__main__" :
    unittest.main()

