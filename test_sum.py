import unittest
import sum

#### unit testing

class TestFunctions(unittest.TestCase):


    def setUp(self):
        self.a = 74543
        self.b = 6

# test to ensure input variables are integers
    def test_if_integer(self):
        self.assertTrue((isinstance(self.a, int) and isinstance(self.b, int)), "One or both of input variables are not an integer")

# tests for each of the above functions
    def test_sum(self):
        result = sum.sum_function(self.a,self.b)
        self.assertEqual(result, self.a + self.b, "Sum function incorrect.")

if __name__ == "__main__":
    unittest.main()
