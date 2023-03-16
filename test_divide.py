import unittest
import divide

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.a = 74543
        self.b = 6
        self.c = 0

    def testZero(self):
        self.assertRaises(ZeroDivisionError, divide.divide_function, self.a, self.c)

    def testDivide(self):
        result = divide.divide_function(self.a, self.b)
        self.assertEqual(result, round(self.a / self.b), "Divide function incorrect.")



if __name__ == "__main__":
    unittest.main()
