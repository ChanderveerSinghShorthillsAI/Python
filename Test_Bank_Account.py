# test_bank_account.py
import unittest
from  Bank_Account import BankAccount  # Import the BankAccount class

class TestBankAccount(unittest.TestCase):
    """Unit tests for the BankAccount class."""

    def setUp(self):
        """Runs before each test. Initializes test accounts."""
        self.account1 = BankAccount("Alice", 100)
        self.account2 = BankAccount("Bob", 50)

    def test_initial_balance(self):
        """Test if the initial balance is set correctly."""
        self.assertEqual(self.account1.get_balance(), 100)  # Normal case
        self.assertGreater(self.account1.get_balance(), 50)  # Account1 has more than 50
        self.assertLess(self.account2.get_balance(), 100)  # Account2 has less than 100

    def test_deposit(self):
        """Test deposit functionality."""
        self.account1.deposit(50)
        self.assertEqual(self.account1.get_balance(), 150)  # 100 + 50 = 150

        with self.assertRaises(ValueError):  # Test deposit of a negative amount
            self.account1.deposit(-10)

    def test_withdraw(self):
        """Test withdrawing money."""
        self.account1.withdraw(40)
        self.assertEqual(self.account1.get_balance(), 60)  # 100 - 40 = 60
        self.assertFalse(self.account1.is_overdrawn())  # Ensure account is NOT overdrawn

    def test_withdraw_insufficient_funds(self):
        """Test withdrawal exceeding balance should raise ValueError."""
        with self.assertRaises(ValueError):  # Expecting an error
            self.account1.withdraw(200)

    def test_overdrawn_status(self):
        """Test if is_overdrawn() correctly identifies overdrawn accounts."""
        self.assertFalse(self.account1.is_overdrawn())  # Should be False initially

        with self.assertRaises(ValueError):
            self.account1.withdraw(150)  # Would cause overdraw, so error expected
        
        self.assertFalse(self.account1.is_overdrawn())  # Still should be False

    def test_transfer(self):
        """Test transferring money between accounts."""
        self.account1.transfer(30, self.account2)  # Alice transfers 30 to Bob
        self.assertEqual(self.account1.get_balance(), 70)  # 100 - 30 = 70
        self.assertEqual(self.account2.get_balance(), 80)  # 50 + 30 = 80

        with self.assertRaises(ValueError):  # Transferring more than available
            self.account1.transfer(500, self.account2)

        with self.assertRaises(TypeError):  # Transferring to a non-BankAccount object
            self.account1.transfer(10, "Not an Account")

    def test_object_type(self):
        """Test if an instance belongs to the correct class."""
        self.assertIsInstance(self.account1, BankAccount)  # Should be a BankAccount
        self.assertNotIsInstance("Random String", BankAccount)  # Should NOT be a BankAccount

if __name__ == "__main__":
    unittest.main()
