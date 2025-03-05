# test_calculator.py
import unittest
from Calculator import Calculator  # Import the Calculator class

class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """This method runs before each test. It initializes a Calculator instance."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition of numbers."""
        self.assertEqual(self.calc.add(3, 2), 5)  # 3 + 2 = 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(self.calc.add(0, 0), 0)  # 0 + 0 = 0

    def test_subtract(self):
        """Test subtraction of numbers."""
        self.assertEqual(self.calc.subtract(3, 2), 1)  # 3 - 2 = 1
        self.assertEqual(self.calc.subtract(2, 3), -1)  # 2 - 3 = -1
        self.assertEqual(self.calc.subtract(0, 0), 0)  # 0 - 0 = 0

    def test_multiply(self):
        """Test multiplication of numbers."""
        self.assertEqual(self.calc.multiply(3, 2), 6)  # 3 * 2 = 6
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # -1 * 1 = -1
        self.assertEqual(self.calc.multiply(0, 5), 0)  # 0 * 5 = 0

    def test_divide(self):
        """Test division of numbers."""
        self.assertEqual(self.calc.divide(6, 2), 3)  # 6 / 2 = 3
        self.assertEqual(self.calc.divide(-6, 2), -3)  # -6 / 2 = -3
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # 5 / 2 = 2.5

    def test_divide_by_zero(self):
        """Test division by zero should raise ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)  # Expect ValueError for division by zero

if __name__ == "__main__":
    unittest.main()
