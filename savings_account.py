from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest added: ${interest}. New balance is {self.current_balance}")
