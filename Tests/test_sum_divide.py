import unittest
import sys
sys.path.insert(0, "../")
import Calculator

#### unit testing

class TestFunctions(unittest.TestCase):


    def setUp(self):
        self.a = 74543
        self.b = 6

# test to ensure input variables are integers
    def test_if_integer(self):
        self.assertTrue((isinstance(self.a, int) and isinstance(self.b, int)), "One or both of input variables are not an integer")


#test to ensure input variables do not raise zero exception -
### not used as redundant
    # def test_raises_no_exception(self):
    #     try:
    #         Calculator.divide_function_round(self.a, self.b)
    #     except ZeroDivisionError as error:
    #         assert False, f"Error was raised: {error}. Cannot divide by zero."

    # def test_raises_error(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         #Calculator.divide_function_round(self.a,self.b)

# tests for each of the above functions
    def test_sum(self):
        result = Calculator.sum_function(self.a,self.b)
        self.assertEqual(result, self.a + self.b, "Sum function incorrect.")

    def test_divide_rounded(self):
        result = Calculator.divide_function_round(self.a,self.b)
        try:
            self.assertEqual(result, round(self.a / self.b), "Divide function incorrect.")
        except ZeroDivisionError:
            print("divide value is zero")

if __name__ == "__main__":
    unittest.main()
