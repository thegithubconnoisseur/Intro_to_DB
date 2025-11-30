import unittest
from simple_calculator import SimpleCalculator 

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before 
        each test."""
        self.calc = SimpleCalculator()
        self.a = 10 
        self.b = 5

    def test_addition(self):
        self.assertEqual(self.calc.add(self.a,self.b), self.a + self.b)
        self.assertEqual(self.calc.add(-2,-2), -4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self.a, self.b), self.a - self.b)
        self.assertEqual(self.calc.subtract(-2,-2), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(self.a, self.b), self.a * self.b)
        self.assertEqual(self.calc.multiply(-2,-2), 4)
        self.assertEqual(self.calc.multiply(-2,2), -4)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(self.a, self.b), self.a/self.b)
        self.assertEqual(self.calc.divide(-2,-2), 1)
        self.assertEqual(self.calc.divide(-2,0),None)


if __name__ == "__main__":
    unittest.main()