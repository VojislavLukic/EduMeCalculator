import unittest

# function to return sum of 2 integers
def sum_function(intA, intB):
    return intA+intB

# funtion to divide 2 integers and return as float
def divide_function(intA, intB):
    return intA/intB

# function to divide 2 integers and return value rounded to nearest integer
def divide_function_round(intA, intB):
    return round(intA/intB)

#### unit testing

class TestFunctions(unittest.TestCase):


    def setUp(self):
        self.a = 8967678
        self.b = 5675

# test to ensure input variables are integers
    def test_if_integer(self):
        self.assertTrue(isinstance(self.a, int) and isinstance(self.b, int))

# tests for each of the three above functions
    def test_sum(self):
        result = sum_function(self.a,self.b)
        self.assertEqual(result, self.a + self.b)

    def test_divide(self):
        result = divide_function(self.a,self.b)
        self.assertEqual(result, self.a/self.b)

    def test_divide_rounded(self):
        result = divide_function_round(self.a,self.b)
        self.assertEqual(result, round(self.a/self.b))

if __name__ == "__main__":
    unittest.main()

