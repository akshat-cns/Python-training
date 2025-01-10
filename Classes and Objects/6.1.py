class BankAccount:

    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        self.balance -= amount
        print(f"Withdrawn ${amount:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance
