class BankAccount:
    #Shaza Ghanem
    bank_title = "Your Bank Name"

    def __init__(self, customer_name, current_balance, minimum_balance=None):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = "123456789"
        self.routing_number = "987654321"

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Was Deposited: ${amount} . New balance is {self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance: #to make sure the withdrawal is only allowed if the remaining balance after the withdrawal is above the minimum balance
            self.current_balance -= amount
            print(f"Withdrew: ${amount} . New balance is {self.current_balance}")
        else:
            print("Denied: Insufficient balance")

    def customer_information(self):
        print(f"Bank: {self.bank_title}")
        print(f"Customer: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self.account_number}")
        print(f"Routing Number: {self.routing_number}")

 # Create instances
account1 = BankAccount("Alice", 1000, 100)
account2 = BankAccount("Bob", 500, 50)

# Test methods
account1.deposit(200)
account1.withdraw(150)
account1.customer_information()

account2.deposit(300)
account2.withdraw(100)
account2.customer_information()

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest added: ${interest}. New balance is {self.current_balance}")

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount <= self.transfer_limit:
            self.current_balance -= amount
            print(f"Transferred: ${amount}. New balance is {self.current_balance}")
        else:
            print(f"Transfer denied: Amount exceeds transfer limit of ${self.transfer_limit}")