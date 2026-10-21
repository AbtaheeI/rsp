class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("You cannot deposit a negative number")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("You cannot withdraw a negative number")
        self.balance -= amount

    @property
    def is_empty(self):
        return self.balance == 0

    def describe(self):
        return f"{self.owner} has ${self.balance}"

    
        