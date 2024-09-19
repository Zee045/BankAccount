from bank_account import SavingsAccount, CheckingAccount

def main():
    # Create instances of SavingsAccount
    savings1 = SavingsAccount("Alice", 1000, 100, 0.05)
    savings2 = SavingsAccount("Bob", 500, 50, 0.03)

    # Create instances of CheckingAccount
    checking1 = CheckingAccount("Charlie", 2000, 200, 500)
    checking2 = CheckingAccount("Dana", 1500, 150, 300)

    # Test methods for SavingsAccount
    savings1.deposit(200)
    savings1.add_interest()
    savings1.withdraw(150)
    savings1.customer_information()

    savings2.deposit(300)
    savings2.add_interest()
    savings2.withdraw(100)
    savings2.customer_information()

    # Test methods for CheckingAccount
    checking1.deposit(500)
    checking1.transfer(400)
    checking1.withdraw(300)
    checking1.customer_information()

    checking2.deposit(200)
    checking2.transfer(350)
    checking2.withdraw(100)
    checking2.customer_information()

if __name__ == "__main__":
    main()
