# bank_account.py
class BankAccount:
    """A simple bank account class with deposit, withdrawal, and transfer functionality."""

    def __init__(self, owner, balance=0):
        """Initialize the bank account with an owner and an optional starting balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance is available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def is_overdrawn(self):
        """Check if the account is overdrawn."""
        return self.balance < 0

    def transfer(self, amount, recipient):
        """Transfer money to another BankAccount object."""
        if not isinstance(recipient, BankAccount):
            raise TypeError("Recipient must be a BankAccount instance")
        self.withdraw(amount)  # Withdraw from sender
        recipient.deposit(amount)  # Deposit into recipient
        return self.balance

    def get_balance(self):
        """Return the current balance."""
        return self.balance  # Return the current balance
