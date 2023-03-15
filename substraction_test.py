import unittest

from substraction import substract

class TestSubstration(unittest.TestCase):
    #test if substraction result is correct
    def test_result_of_substraction(self):
        self.assertEqual(substract(3,2),1,"The substraction result is wrong.")
    #test if raises error when result is negative
    def test_raise_if_negative_result(self):
        self.assertRaises(ValueError,substract,4,9)

if __name__ == '__main__':
    unittest.main()
