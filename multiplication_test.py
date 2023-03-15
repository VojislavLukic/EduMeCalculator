import unittest
from multiplication import Calculations

class TestMultiplication(unittest.TestCase):
    
    def test_multiply(self):
        #test if result of multiplication is correct
        calculation = Calculations(2, 5)
        self.assertEqual(calculation.multiply(), 10, 'Wrong result of multiplication.')
        
if __name__ == '__main__':
    unittest.main()
