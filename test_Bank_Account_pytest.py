import pytest
from Bank_Account import BankAccount  # Import the BankAccount class

@pytest.fixture
def sample_accounts():
    """Fixture to create two test accounts before running tests."""
    account1 = BankAccount("Alice", 100)
    account2 = BankAccount("Bob", 50)
    return account1, account2  # Return both accounts

def test_initial_balance(sample_accounts):
    """Test if the initial balance is set correctly."""
    account1, account2 = sample_accounts
    assert account1.get_balance() == 100  # Pytest uses `assert`
    assert account2.get_balance() == 50
    assert account1.get_balance() > 50  #  No need for assertGreater()
    assert account2.get_balance() < 100  #  No need for assertLess()

def test_deposit(sample_accounts):
    """Test depositing money into the account."""
    account1, _ = sample_accounts
    account1.deposit(50)
    assert account1.get_balance() == 150  # No need for assertEqual()

    with pytest.raises(ValueError):  #  Pytest uses `pytest.raises()`
        account1.deposit(-10)  # Should raise ValueError

def test_withdraw(sample_accounts):
    """Test withdrawing money."""
    account1, _ = sample_accounts
    account1.withdraw(40)
    assert account1.get_balance() == 60
    assert not account1.is_overdrawn()  #  No need for assertFalse()

def test_withdraw_insufficient_funds(sample_accounts):
    """Test withdrawal exceeding balance should raise ValueError."""
    account1, _ = sample_accounts
    with pytest.raises(ValueError):  # Pytest simplifies this!
        account1.withdraw(200)  # More than available balance

def test_overdrawn_status(sample_accounts):
    """Test if is_overdrawn() correctly identifies overdrawn accounts."""
    account1, _ = sample_accounts
    assert not account1.is_overdrawn()  #Simplified assertion

    with pytest.raises(ValueError):
        account1.withdraw(150)  # Should raise ValueError before overdrawing

    assert not account1.is_overdrawn()  # No overdraft allowed

def test_transfer(sample_accounts):
    """Test transferring money between accounts."""
    account1, account2 = sample_accounts
    account1.transfer(30, account2)
    assert account1.get_balance() == 70
    assert account2.get_balance() == 80

    with pytest.raises(ValueError):  # Transferring more than available
        account1.transfer(500, account2)

    with pytest.raises(TypeError):  # Transferring to a non-BankAccount object
        account1.transfer(10, "Not an Account")

def test_object_type(sample_accounts):
    """Test if an instance belongs to the correct class."""
    account1, _ = sample_accounts
    assert isinstance(account1, BankAccount)  # Pytest uses `isinstance()`
    assert not isinstance("Random String", BankAccount)  # No need for assertNotIsInstance()
