from bank_account import BankAccount

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
