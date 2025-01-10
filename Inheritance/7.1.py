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

class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, initial_balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):

    def __init__(self, account_number, account_holder, initial_balance=0.0, transaction_limit=5, reward_threshold=1000):
        super().__init__(account_number, account_holder, initial_balance)
        self.transaction_limit = transaction_limit
        self.transaction_count = 0
        self.reward_threshold = reward_threshold
        self.rewards = 0

    def deposit(self, amount):
        if self.transaction_count >= self.transaction_limit:
            raise ValueError("Transaction limit reached. Cannot deposit.")
        super().deposit(amount)
        self.transaction_count += 1

        # Reward Program
        if amount >= self.reward_threshold:
            reward = amount * 0.01  # 1% of the deposit amount
            self.rewards += reward
            print(f"Reward of ${reward:.2f} earned! Total rewards: ${self.rewards:.2f}")

    def withdraw(self, amount):
        if self.transaction_count >= self.transaction_limit:
            raise ValueError("Transaction limit reached. Cannot withdraw.")
        super().withdraw(amount)
        self.transaction_count += 1

    def reset_transaction_count(self):
        self.transaction_count = 0
        print("Transaction count reset to 0.")